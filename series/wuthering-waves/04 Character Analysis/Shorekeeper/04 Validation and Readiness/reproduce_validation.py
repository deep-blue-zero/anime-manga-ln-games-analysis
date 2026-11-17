#!/usr/bin/env python3
"""Check Shorekeeper draft packet structure, media joins and private source pin."""

from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import re

HERE = Path(__file__).resolve().parent.parent
PREFIX = "WUWA_SHOREKEEPER_"
COMMIT = "353f2eaed119bc9f680eab92807d20ac75a79b40"
LANGUAGES = {"en", "ja", "ko", "zh"}
MEDIA_SUFFIXES = {".wav", ".flac", ".wem", ".mp3", ".mp4", ".png", ".webp", ".pak"}




# Exact character-root-relative paths after the artifact-class migration.
PACKET_ARTIFACT_PATHS = {'AUDIO_MATCHED_SEMANTIC_CASES.json': '03 Audiovisual and Voice/AUDIO_MATCHED_SEMANTIC_CASES.json', 'CHARACTER_VISUAL_DESIGN_PROFILE.json': '03 Audiovisual and Voice/CHARACTER_VISUAL_DESIGN_PROFILE.json', 'CHARACTER_VISUAL_DESIGN_PROFILE.md': '03 Audiovisual and Voice/CHARACTER_VISUAL_DESIGN_PROFILE.md', 'CHARACTER_VISUAL_REFERENCE_MANIFEST.json': '03 Audiovisual and Voice/CHARACTER_VISUAL_REFERENCE_MANIFEST.json', 'VALIDATION_REPORT.json': '04 Validation and Readiness/VALIDATION_REPORT.json', 'WUWA_SHOREKEEPER_AETHERFIN_RETURN_RIVER_MONITORING_AND_UNUSED_BIRTHDAY_PROFILE.md': '01 Evidence and Source-Facing/WUWA_SHOREKEEPER_AETHERFIN_RETURN_RIVER_MONITORING_AND_UNUSED_BIRTHDAY_PROFILE.md', 'WUWA_SHOREKEEPER_ANALYSIS_PACKET_README.md': 'WUWA_SHOREKEEPER_ANALYSIS_PACKET_README.md', 'WUWA_SHOREKEEPER_AV_AND_HUMAN_RETRIEVAL_PLAN.md': '03 Audiovisual and Voice/WUWA_SHOREKEEPER_AV_AND_HUMAN_RETRIEVAL_PLAN.md', 'WUWA_SHOREKEEPER_AV_HUMAN_RETRIEVAL_CROSSWALK.md': '03 Audiovisual and Voice/WUWA_SHOREKEEPER_AV_HUMAN_RETRIEVAL_CROSSWALK.md', 'WUWA_SHOREKEEPER_BATTLE_EMBODIMENT_AND_LIMIT_LANGUAGE_PROFILE.md': '01 Evidence and Source-Facing/WUWA_SHOREKEEPER_BATTLE_EMBODIMENT_AND_LIMIT_LANGUAGE_PROFILE.md', 'WUWA_SHOREKEEPER_CHARACTER_DEEP_DIVE_PRE_AV.md': '01 Evidence and Source-Facing/WUWA_SHOREKEEPER_CHARACTER_DEEP_DIVE_PRE_AV.md', 'WUWA_SHOREKEEPER_CHARACTER_MODEL_PACKAGE.json': '02 Reconstruction/WUWA_SHOREKEEPER_CHARACTER_MODEL_PACKAGE.json', 'WUWA_SHOREKEEPER_CHOICE_DELEGATION_AND_CONTINUITY_PROFILE.md': '01 Evidence and Source-Facing/WUWA_SHOREKEEPER_CHOICE_DELEGATION_AND_CONTINUITY_PROFILE.md', 'WUWA_SHOREKEEPER_CLAIM_REVISION_LEDGER.md': '04 Validation and Readiness/WUWA_SHOREKEEPER_CLAIM_REVISION_LEDGER.md', 'WUWA_SHOREKEEPER_EVIDENCE_AND_FALSIFICATION_MATRIX.md': '01 Evidence and Source-Facing/WUWA_SHOREKEEPER_EVIDENCE_AND_FALSIFICATION_MATRIX.md', 'WUWA_SHOREKEEPER_HONAMI_TASTE_DIAGNOSTIC_UNCERTAINTY_AND_RIFT_BOUNDARY_PROFILE.md': '01 Evidence and Source-Facing/WUWA_SHOREKEEPER_HONAMI_TASTE_DIAGNOSTIC_UNCERTAINTY_AND_RIFT_BOUNDARY_PROFILE.md', 'WUWA_SHOREKEEPER_MODEL_FIDELITY_AND_STRESS_TEST_PRE_AV.md': '04 Validation and Readiness/WUWA_SHOREKEEPER_MODEL_FIDELITY_AND_STRESS_TEST_PRE_AV.md', 'WUWA_SHOREKEEPER_ORDINARY_LIFE_AND_PREFERENCES_PROFILE.md': '01 Evidence and Source-Facing/WUWA_SHOREKEEPER_ORDINARY_LIFE_AND_PREFERENCES_PROFILE.md', 'WUWA_SHOREKEEPER_RECONSTRUCTIVE_PROFILE_PRE_AV.md': '02 Reconstruction/WUWA_SHOREKEEPER_RECONSTRUCTIVE_PROFILE_PRE_AV.md', 'WUWA_SHOREKEEPER_RELATIONSHIP_STATE_AND_ORDINARY_LIFE_PROFILE.md': '01 Evidence and Source-Facing/WUWA_SHOREKEEPER_RELATIONSHIP_STATE_AND_ORDINARY_LIFE_PROFILE.md', 'WUWA_SHOREKEEPER_SELF_EXCLUSION_SOUL_AND_SHARED_WORLD_PROFILE.md': '01 Evidence and Source-Facing/WUWA_SHOREKEEPER_SELF_EXCLUSION_SOUL_AND_SHARED_WORLD_PROFILE.md', 'WUWA_SHOREKEEPER_SONORO_SELF_BLAME_TEA_AND_EVACUATION_MEMORY_PROFILE.md': '01 Evidence and Source-Facing/WUWA_SHOREKEEPER_SONORO_SELF_BLAME_TEA_AND_EVACUATION_MEMORY_PROFILE.md', 'WUWA_SHOREKEEPER_SOURCE_CENSUS_CHRONOLOGY_AND_IDENTITY_AUDIT.md': '04 Validation and Readiness/WUWA_SHOREKEEPER_SOURCE_CENSUS_CHRONOLOGY_AND_IDENTITY_AUDIT.md', 'WUWA_SHOREKEEPER_SOURCE_DEFINED_AUDIO_COHORT_AUDIT.md': '04 Validation and Readiness/WUWA_SHOREKEEPER_SOURCE_DEFINED_AUDIO_COHORT_AUDIT.md', 'WUWA_SHOREKEEPER_SPEECH_AND_MACHINE_VOICE_PROFILE_PRE_AV.md': '03 Audiovisual and Voice/WUWA_SHOREKEEPER_SPEECH_AND_MACHINE_VOICE_PROFILE_PRE_AV.md', 'WUWA_SHOREKEEPER_TETHYS_NAMES_PROPERTY_AND_SONORO_BURDEN_PROFILE.md': '01 Evidence and Source-Facing/WUWA_SHOREKEEPER_TETHYS_NAMES_PROPERTY_AND_SONORO_BURDEN_PROFILE.md', 'WUWA_SHOREKEEPER_WAVESLINE_WARMTH_TERMINAL_AND_SHARED_ROAD_PROFILE.md': '01 Evidence and Source-Facing/WUWA_SHOREKEEPER_WAVESLINE_WARMTH_TERMINAL_AND_SHARED_ROAD_PROFILE.md', 'reproduce_validation.py': '04 Validation and Readiness/reproduce_validation.py'}

def packet_artifact(root: Path, name: str) -> Path:
    return root / PACKET_ARTIFACT_PATHS.get(name, name)

def jsonl(path: Path) -> list[dict]:
    with path.open(encoding="utf-8") as handle:
        return [json.loads(line) for line in handle if line.strip()]


def require(ok: bool, note: str, checks: list[str]) -> None:
    if not ok:
        raise AssertionError(note)
    checks.append(note)


def validate(source_root: Path | None) -> dict:
    checks: list[str] = []
    matrix = (packet_artifact(HERE, f"{PREFIX}EVIDENCE_AND_FALSIFICATION_MATRIX.md")).read_text(encoding="utf-8")
    evidence = set(re.findall(r"\| (SHK-E\d{2}) \|", matrix))
    claims = set(re.findall(r"\| (SHK-C\d{2}) —", matrix))
    require(len(evidence) == 39, "39 evidence bundles", checks)
    require(len(claims) == 39, "39 claim rows", checks)
    require(not any(p.suffix.lower() in MEDIA_SUFFIXES for p in HERE.rglob("*") if p.is_file()),
            "no raw media in Git packet", checks)
    expected = (
        "ANALYSIS_PACKET_README.md", "AV_AND_HUMAN_RETRIEVAL_PLAN.md",
        "CHARACTER_DEEP_DIVE_PRE_AV.md", "CHOICE_DELEGATION_AND_CONTINUITY_PROFILE.md",
        "CLAIM_REVISION_LEDGER.md", "EVIDENCE_AND_FALSIFICATION_MATRIX.md",
        "MODEL_FIDELITY_AND_STRESS_TEST_PRE_AV.md",
        "ORDINARY_LIFE_AND_PREFERENCES_PROFILE.md",
        "RECONSTRUCTIVE_PROFILE_PRE_AV.md",
        "RELATIONSHIP_STATE_AND_ORDINARY_LIFE_PROFILE.md",
        "SELF_EXCLUSION_SOUL_AND_SHARED_WORLD_PROFILE.md",
        "SOURCE_DEFINED_AUDIO_COHORT_AUDIT.md",
        "SOURCE_CENSUS_CHRONOLOGY_AND_IDENTITY_AUDIT.md",
        "BATTLE_EMBODIMENT_AND_LIMIT_LANGUAGE_PROFILE.md",
        "AETHERFIN_RETURN_RIVER_MONITORING_AND_UNUSED_BIRTHDAY_PROFILE.md",
        "SONORO_SELF_BLAME_TEA_AND_EVACUATION_MEMORY_PROFILE.md",
        "WAVESLINE_WARMTH_TERMINAL_AND_SHARED_ROAD_PROFILE.md",
        "HONAMI_TASTE_DIAGNOSTIC_UNCERTAINTY_AND_RIFT_BOUNDARY_PROFILE.md",
        "TETHYS_NAMES_PROPERTY_AND_SONORO_BURDEN_PROFILE.md",
        "SPEECH_AND_MACHINE_VOICE_PROFILE_PRE_AV.md",
    )
    for suffix in expected:
        path = packet_artifact(HERE, f"{PREFIX}{suffix}")
        body = path.read_text(encoding="utf-8")
        require(body.startswith("---\n") and "\nstatus: draft_noncurrent\n" in body,
                f"draft authority: {path.name}", checks)
        require("\ndo_not_use_as_current_authority: true\n" in body,
                f"noncurrent flag: {path.name}", checks)
        require(f"\nsource_commit: {COMMIT}\n" in body,
                f"source pin: {path.name}", checks)
    model = json.loads((packet_artifact(HERE, f"{PREFIX}CHARACTER_MODEL_PACKAGE.json")).read_text(encoding="utf-8"))
    require(model["authority"] == "draft_noncurrent" and model["source_commit"] == COMMIT,
            "model authority and source pin", checks)
    require(len(model["rules"]) == 24 and len({r["id"] for r in model["rules"]}) == 24,
            "24 distinct model rules", checks)
    require(all(set(r["evidence_ids"]) <= evidence and r["probability"] is None
                for r in model["rules"]), "evidence-linked nonnumeric rules", checks)
    probes = (packet_artifact(HERE, f"{PREFIX}MODEL_FIDELITY_AND_STRESS_TEST_PRE_AV.md")).read_text(encoding="utf-8")
    require(len(set(re.findall(r"\| (SHK-P\d{2}) \|", probes))) == 38,
            "38 non-blind probes", checks)
    require("## Ten interacting failure tests" in probes and all(
                f"R{number:02d}" in probes for number in range(1, 25)),
            "ten interaction tests and twenty-four-rule challenge map", checks)
    cases = json.loads((packet_artifact(HERE, "AUDIO_MATCHED_SEMANTIC_CASES.json")).read_text(encoding="utf-8"))
    require(cases["semantic_cases"] == 15 and len(cases["cases"]) == 15,
            "15 matched semantic cases", checks)
    crosswalk = (packet_artifact(HERE, "WUWA_SHOREKEEPER_AV_HUMAN_RETRIEVAL_CROSSWALK.md")).read_text(encoding="utf-8")
    require(all(f"`{case['text_key']}`" in crosswalk for case in cases["cases"]),
            "all 15 exact sound cases occur in AV crosswalk", checks)
    require("terminal Agent" in crosswalk and "lie to Rover" in crosswalk and "postrepair state" in crosswalk,
            "recipient and core-state controls in AV crosswalk", checks)
    require(set(re.findall(r"\| (SHK-R\d{2}) \|", crosswalk)) ==
                {f"SHK-R{number:02d}" for number in range(1, 15)},
            "fourteen runtime/identity/trigger controls", checks)
    require(sum(len(c["renders"]) for c in cases["cases"]) == 60,
            "60 selected render variants", checks)
    require(all({r["language"] for r in c["renders"]} == LANGUAGES for c in cases["cases"]),
            "all selected cases have four dubs", checks)
    require(all(len(r[f]) == 64 for c in cases["cases"] for r in c["renders"]
                for f in ("wem_sha256", "canonical_pcm_sha256", "flac_sha256")),
            "selected media hashes present", checks)
    result = {"packet": "Shorekeeper", "scope": "SHOREKEEPER_PINNED_3_6_0_TEXT_AUDIO_PRE_AV",
              "checks": checks, "source_crosscheck": "not_requested"}
    if source_root is not None:
        source = source_root / "ANALYSIS" / "Characters" / "Shorekeeper"
        voice = source_root / "_voice_media" / "character" / "complete_voice_corpus" / "Shorekeeper" / "v0_1"
        summary = source_root / "_research" / "character_packets" / "Shorekeeper" / "audio_work" / "AUDIO_MEASUREMENT_SUMMARY.json"
        audit = json.loads((source / "COLLECTION_AUDIT.json").read_text(encoding="utf-8"))
        direct = audit["scopes"]["direct_character"]
        require(audit["valid"] and direct["voice_completeness_valid"],
                "collection valid and selected voice complete", checks)
        require((audit["raw_flow_states"], audit["context_text_keys"],
                 audit["quest_references"], audit["distinct_quest_ids"],
                 audit["message_records"]) == (157, 2684, 79, 18, 4),
                "context collection denominator", checks)
        require((direct["candidate_occurrences"], direct["accepted_occurrences"],
                 direct["source_voiced"], direct["source_unvoiced"]) ==
                (624, 619, 483, 136), "direct occurrence denominator", checks)
        require((direct["semantic_voice_lines"], direct["complete_voice_lines"],
                 direct["missing_voice_lines"], direct["unresolved_reason_rows"]) ==
                (543, 543, 0, 0), "selected semantic voice completeness", checks)
        require((direct["render_associations"], direct["runtime_object_rows"],
                 direct["unique_flac_objects"], direct["unique_flac_bytes"]) ==
                (2172, 2052, 2048, 524309692), "media denominators and bytes", checks)
        crosswalk = jsonl(source / "occurrence_identity_crosswalk.jsonl")
        require(Counter(r["character_attribution"] for r in crosswalk) ==
                {"accepted_solo": 619, "rejected": 5}, "identity crosswalk counts", checks)
        rejected = {(r["flow_state_row_index"], r["talk_index"])
                    for r in crosswalk if r["character_attribution"] == "rejected"}
        require(rejected == {(3451, 1), (4214, 0), (5200, 0), (5200, 1), (5200, 2)},
                "five nearby non-Shorekeeper turns remain rejected", checks)
        messages = jsonl(source / "WAVESLINE_MESSAGES.jsonl")
        require(len(messages) == 4 and
                [row["contact_name"]["values"]["en"]["content"] for row in messages] ==
                ["Chisa", "Shorekeeper", "Aemeath", "Valentina"],
                "four message pointers have four distinct named contacts", checks)
        message = next(row for row in messages if row["short_message_id"] == 30073)
        require(message["source_locator"].endswith("/shortmessage.json#/72") and
                message["flow_state_locator"].endswith("/flowstate.json#/14519") and
                message["state_key"] == "剧情_1.0至2.8剧情回填_6_1" and
                message["content_extraction_status"] == "metadata_only_scope" and
                message["raw"]["WhichChat"] == 42 and
                message["raw"]["QuestId"] == 0 and
                message["raw"]["ListenQuestId"] == 0 and
                message["direct_quest_links"] == [] and
                message["structural_counts"]["talk_items_total"] == 11,
                "Shorekeeper message pointer, raw graph target and no direct quest/time join", checks)
        message_raw = next(row for row in jsonl(source / "RAW_RELEVANT_FLOW_STATES.jsonl")
                           if row["source_locator"].endswith("/flowstate.json#/14519"))
        message_actions = json.loads(message_raw["raw"]["Actions"])
        message_items = message_actions[1]["Params"]["TalkItems"]
        require(message_actions[1]["Name"] == "ShowTalk" and
                len(message_items) == 11 and
                [item["Id"] for item in message_items] == list(range(1, 12)) and
                [item["WhoId"] for item in message_items] ==
                [701100, 701100, 701100, 701052, 701100, 701100,
                 701100, 701052, 701100, 701100, 701100] and
                all("PlayVoice" not in item for item in message_items),
                "eleven ordered, source-unvoiced message items retain speaker ownership", checks)
        speaker_root = source_root / "_sources" / "Arikatsu_WutheringWaves_Data"
        speaker_rows = {row["Id"]: row for row in json.loads(
            (speaker_root / "BinData" / "speaker" / "speaker.json").read_text(encoding="utf-8"))}
        zh_speakers = {row["Id"]: row["Content"] for row in json.loads(
            (speaker_root / "Textmaps" / "zh-Hans" / "speaker" / "Speaker.json")
            .read_text(encoding="utf-8"))}
        require(speaker_rows[701100]["Name"] == 6155 and
                speaker_rows[701052]["Name"] == 6107 and
                "守岸人" in zh_speakers[6155] and
                "{PlayerName}" in zh_speakers[6107],
                "Shorekeeper and Rover/player message speaker tables remain distinct", checks)
        require([item["TidTalk"] for item in message_items] ==
                ["phone_JL_5_1", "phone_JL_5_2", "phone_JL_5_3",
                 "phone_JL_5_6", "phone_JL_5_10", "phone_JL_5_11",
                 "phone_JL_5_7", "phone_JL_5_13", "phone_JL_5_14",
                 "phone_JL_5_8", "phone_JL_5_9"] and
                [message_items[i]["Options"][0]["Actions"][0]["Params"]["TalkId"]
                 for i in (2, 6)] == [4, 8] and
                [message_items[i]["Actions"][0]["Params"]["TalkId"]
                 for i in (3, 7)] == [5, 9] and
                [len(message_items[i]["Options"]) for i in (2, 6)] == [1, 1] and
                [message_items[i]["Options"][0]["TidTalkOption"]
                 for i in (2, 6)] == ["phone_JL_5_4", "phone_JL_5_12"],
                "two one-option message continuations do not create alternate routes", checks)
        require(message_items[-1]["Type"] == "PhoneMessage" and
                message_items[-1]["MessageType"] == {"Type": "Emoji", "EmojiId": 177} and
                message_items[-1]["TidTalk"] == "phone_JL_5_9",
                "last Shorekeeper-associated item is an emoji, not a spoken line", checks)
        message_identity = [row for row in crosswalk if row["flow_state_row_index"] == 14519]
        require(len(message_identity) == 9 and
                {row["talk_index"] for row in message_identity} ==
                {0, 1, 2, 4, 5, 6, 8, 9, 10} and
                all(row["technical_speaker_id"] == 701100 and
                    row["character_attribution"] == "accepted_solo" and
                    row["play_voice"] is False and
                    row["resolved_media_association_count"] == 0
                    for row in message_identity),
                "nine accepted message occurrences include one emoji and no media", checks)
        message_witnesses = {row["text_key"]: row for row in
                             jsonl(source / "CONTEXT_TEXT_WITNESSES.jsonl")
                             if row["text_key"].startswith("phone_JL_5_")}
        require(len(message_witnesses) == 13 and
                all({"zh-Hans", "en", "ja", "ko"} <= row["values"].keys() and
                    all(row["values"][lang]["status"] == "resolved"
                        for lang in ("zh-Hans", "en", "ja", "ko"))
                    for row in message_witnesses.values()),
                "thirteen item-and-caption text keys have four resolved witnesses", checks)
        require("阳光" in message_witnesses["phone_JL_5_1"]["values"]["zh-Hans"]["content"] and
                "泰缇斯" in message_witnesses["phone_JL_5_7"]["values"]["zh-Hans"]["content"] and
                "见字如面" in message_witnesses["phone_JL_5_13"]["values"]["zh-Hans"]["content"] and
                "my Shorekeeper" in message_witnesses["phone_JL_5_4"]["values"]["en"]["content"] and
                "我的守岸人" not in message_witnesses["phone_JL_5_4"]["values"]["zh-Hans"]["content"] and
                message_witnesses["phone_JL_5_9"]["values"]["en"]["content"] == "Bouquet",
                "typed warmth, Tethys and EN-only possessive caption remain distinct", checks)
        deep_shore = next(r for r in jsonl(source / "SCENE_AND_EVIDENCE_LEDGER.jsonl")
                          if r["flow_state_row_index"] == 4198 and r["action_index"] == 2)
        require(not deep_shore["sequence_transitions"] and
                deep_shore["talk_items"][24]["technical_speaker_id"] == 1398 and
                deep_shore["talk_items"][24]["text_key"] == "Heihaian_main_1_3_5619_37",
                "deep-shore item 24 is Shorekeeper's promise, not a Rover option", checks)
        require(any(seq.index(25) + 2 < len(seq) and
                    seq[seq.index(25):seq.index(25) + 3] == [25, 26, 27]
                    for seq in deep_shore["talk_sequences"] if 25 in seq),
                "deep-shore promise, apology and cost remain one ordered action", checks)
        lahai = next(r for r in jsonl(source / "SCENE_AND_EVIDENCE_LEDGER.jsonl")
                     if r["flow_state_row_index"] == 10100 and r["action_index"] == 2)
        lahai_items = {item["text_key"]: item for item in lahai["talk_items"]}
        lahai_keys = {f"Main_LahaiRoi_3_1_2_{suffix}"
                      for suffix in (3, 6, 7, 14, 16, 20, 21, 25, 26, 29)}
        require(lahai_keys <= lahai_items.keys() and all(
            lahai_items[key]["technical_speaker_id"] == 1398 and
            all(lahai_items[key]["text_witnesses"][lang]["status"] == "resolved"
                for lang in ("zh", "en", "ja", "ko"))
            for key in lahai_keys),
            "later Lahai departure exact Shorekeeper keys and four text witnesses", checks)
        require("推测" in lahai_items["Main_LahaiRoi_3_1_2_20"]["text_witnesses"]["zh"]["content"] and
                "will undergo" in lahai_items["Main_LahaiRoi_3_1_2_21"]["text_witnesses"]["en"]["content"] and
                "应该能够" in lahai_items["Main_LahaiRoi_3_1_2_21"]["text_witnesses"]["zh"]["content"] and
                "无法通过通讯" in lahai_items["Main_LahaiRoi_3_1_2_29"]["text_witnesses"]["zh"]["content"],
                "departure conjecture, treatment-strength and communication bounds", checks)
        lahai_raw = next(r for r in jsonl(source / "RAW_RELEVANT_FLOW_STATES.jsonl")
                         if r["source_locator"].endswith("/flowstate.json#/10100"))
        lahai_actions = json.loads(lahai_raw["raw"]["Actions"])
        require(lahai_actions[2]["Name"] == "ShowTalk" and
                lahai_actions[2]["Params"]["TalkItems"][5]["TidTalk"] ==
                "Main_LahaiRoi_3_1_2_7" and
                len(lahai_actions[2]["Params"]["TalkItems"][5]["Options"]) == 2,
                "offered drink retains two player-response routes", checks)
        aetherfin = next(r for r in jsonl(source / "SCENE_AND_EVIDENCE_LEDGER.jsonl")
                         if r["flow_state_row_index"] == 4741 and r["action_index"] == 5)
        af_items = aetherfin["talk_items"]
        require(len(af_items) == 31 and af_items[0]["technical_speaker_id"] == 83 and
                all(t["technical_speaker_id"] == 1398 for t in af_items[1:]) and
                all(t["play_voice"] is False for t in af_items),
                "Aetherfin ledger: observer plus thirty named, normalized unvoiced turns", checks)
        require(all(all(t["text_witnesses"][lang]["status"] == "resolved"
                        for lang in LANGUAGES) for t in af_items[1:]),
                "Aetherfin named turns preserve four text witnesses", checks)
        af_raw = next(r for r in jsonl(source / "RAW_RELEVANT_FLOW_STATES.jsonl")
                      if r["source_locator"].endswith("/flowstate.json#/4741"))
        af_actions = json.loads(af_raw["raw"]["Actions"])
        af_talk = af_actions[5]["Params"]["TalkItems"]
        def option_targets(item: dict) -> list[int]:
            return [option["Actions"][0]["Params"]["TalkId"]
                    for option in item.get("Options", [])
                    if option.get("Actions")]
        require(af_actions[5]["Name"] == "ShowTalk" and len(af_talk) == 31 and
                all("PlayVoice" not in item for item in af_talk) and
                [option_targets(af_talk[i]) for i in (0, 14, 19)] ==
                [[2, 4], [16, 17], [21, 26, 29]],
                "Aetherfin raw absent voice flags and three choice split sets", checks)
        require([af_talk[i]["Actions"][0]["Params"]["TalkId"]
                 for i in (2, 4, 15, 16, 24, 27)] ==
                [6, 6, 18, 18, 20, 20],
                "Aetherfin alternative replies reconverge and optional topics loop", checks)
        lines = jsonl(voice / "COMPLETE_VOICE_LINE_ANALYSIS.jsonl")
        require(len(lines) == 543, "543 selected semantic voice rows", checks)
        require(not any("#/14519/Actions!/1/Params/TalkItems/" in line["source_locator"]
                        for line in lines),
                "source-unvoiced WavesLine items have no selected decoded voice cohort", checks)
        scenes = {(r["flow_state_row_index"], r["action_index"]): r
                  for r in jsonl(source / "SCENE_AND_EVIDENCE_LEDGER.jsonl")}
        story_specs = ((3456, 2, 17, 16), (3825, 1, 10, 10), (4173, 1, 13, 13))
        story_rows = []
        scene_members = []
        for state_row, action, item_count, named_count in story_specs:
            scene = scenes[(state_row, action)]
            require(len(scene["talk_items"]) == item_count and
                    sum(t["technical_speaker_id"] == 1398 and t["play_voice"]
                        for t in scene["talk_items"]) == named_count,
                    f"source action {state_row}/{action}: raw item and Shorekeeper voice counts",
                    checks)
            members = [t for t in scene["talk_items"]
                       if t["technical_speaker_id"] == 1398 and t["play_voice"]]
            require(all(all(t["text_witnesses"][lang]["status"] == "resolved"
                            for lang in LANGUAGES) for t in members),
                    f"source action {state_row}/{action}: four resolved text witnesses", checks)
            linked = [line for line in lines if line["source_locator"] in
                      {t["source_locator"] for t in members}]
            require(len(linked) == named_count and
                    {(line["source_locator"], line["text_key"]) for line in linked} ==
                    {(t["source_locator"], t["text_key"]) for t in members},
                    f"source action {state_row}/{action}: exact semantic voice joins",
                    checks)
            story_rows.extend(linked)
            scene_members.extend(members)
        story_renders = [render for line in story_rows for render in line["renders"]]
        require(len(story_rows) == 39 and len(story_renders) == 156 and
                len({r["canonical_pcm_sha256"] for r in story_renders}) == 156 and
                all({r["voice_language"] for r in line["renders"]} == LANGUAGES
                    for line in story_rows),
                "three additional actions: 39 named voice lines and 156 distinct four-dub PCM objects",
                checks)
        require(all(r["materialization_status"] == "flac_roundtrip_pcm_identical" and
                    len(r["canonical_pcm_sha256"]) == 64 and
                    r.get("event_id") is None and r.get("numeric_media_id") is None
                    for r in story_renders),
                "new story-action renders are PCM-valid without invented numeric Wwise IDs",
                checks)
        scene_keys = {t["text_key"]: t for t in scene_members}
        require("如果" in scene_keys["Heihaian_main_1_3_51_28"]["text_witnesses"]["zh"]["content"] and
                "longing" in scene_keys["Heihaian_main_1_3_51_38"]["text_witnesses"]["en"]["content"] and
                "好苦" in scene_keys["Heihaian_main_1_3_5605_10"]["text_witnesses"]["zh"]["content"] and
                "预警" in scene_keys["Heihaian_main_1_3_5609_3"]["text_witnesses"]["zh"]["content"] and
                "evacuation" in scene_keys["Heihaian_main_1_3_5609_5"]["text_witnesses"]["en"]["content"] and
                "not sure" in scene_keys["Heihaian_main_1_3_5609_17"]["text_witnesses"]["en"]["content"],
                "self-blame, tea, warning, evacuation and replica-uncertainty text anchors",
                checks)
        raw_states = {int(r["source_locator"].rsplit("/", 1)[-1]): r
                      for r in jsonl(source / "RAW_RELEVANT_FLOW_STATES.jsonl")
                      if r["source_locator"].rsplit("/", 1)[-1].isdigit()}
        tethys_scene = scenes[(3455, 2)]
        tethys_items = tethys_scene["talk_items"]
        tethys_members = [item for item in tethys_items
                          if item["technical_speaker_id"] == 1398]
        require(tethys_scene["state_key"] == "剧情_1_3_黑海岸主线_10_2" and
                len(tethys_items) == 17 and len(tethys_members) == 14 and
                [item["technical_speaker_id"] for item in tethys_items] ==
                [354] + [1398] * 12 + [354, 354, 1398, 1398] and
                tethys_scene["talk_sequences"] == [list(range(1, 18))] and
                not tethys_scene["sequence_transitions"],
                "Tethys archive action keeps one ordered Rover/Shorekeeper graph", checks)
        require(all(item["play_voice"] is False and
                    all(item["text_witnesses"][language]["status"] == "resolved"
                        for language in LANGUAGES)
                    for item in tethys_members),
                "fourteen Shorekeeper source-unvoiced turns retain four text witnesses", checks)
        tethys_raw = json.loads(raw_states[3455]["raw"]["Actions"])[2]
        require(tethys_raw["Name"] == "ShowTalk" and
                len(tethys_raw["Params"]["TalkItems"]) == 17 and
                all("PlayVoice" not in item for item in
                    tethys_raw["Params"]["TalkItems"]),
                "Tethys archive raw voice flags are absent, not inferred from media", checks)
        tethys_identity = [row for row in crosswalk
                           if row["flow_state_row_index"] == 3455 and
                           row["action_index"] == 2]
        require(len(tethys_identity) == 14 and
                {row["source_locator"] for row in tethys_identity} ==
                {item["source_locator"] for item in tethys_members} and
                all(row["character_attribution"] == "accepted_solo" and
                    row["play_voice"] is False and
                    row["resolved_media_association_count"] == 0
                    for row in tethys_identity) and
                not any("#/3455/Actions!/2/Params/TalkItems/" in line["source_locator"]
                        for line in lines),
                "Tethys archive identities have zero selected audio associations", checks)
        tethys_keys = {item["text_key"]: item["text_witnesses"]
                       for item in tethys_items}
        owner = tethys_keys["Heihaian_main_1_3_50_16"]
        vessel = tethys_keys["Heihaian_main_1_3_50_17"]
        require("所有物" in owner["zh"]["content"] and
                "所有物" in owner["ja"]["content"] and
                "소유" in owner["ko"]["content"] and
                "guardian" in owner["en"]["content"] and
                "索诺拉" in vessel["zh"]["content"] and
                "ソノラ" in vessel["ja"]["content"] and
                "소노라" in vessel["ko"]["content"] and
                "created for this purpose" in vessel["en"]["content"],
                "pre-repair property/guardian and Sonoro/purpose localization fork", checks)
        require("百亿" in tethys_keys["Heihaian_main_1_3_50_8"]["zh"]["content"] and
                "100億" in tethys_keys["Heihaian_main_1_3_50_8"]["ja"]["content"] and
                "手" in tethys_keys["Heihaian_main_1_3_50_13"]["zh"]["content"] and
                "손" in tethys_keys["Heihaian_main_1_3_50_13"]["ko"]["content"],
                "Tethys archive casualty magnitude and reaching-hands wording remain localized", checks)
        tethys_refs = jsonl(source / "QUEST_CONTEXT_REFERENCES.jsonl")
        node = next(row for row in tethys_refs
                    if row["source_locator"].endswith("/questnodedata.json#/4216"))
        handbook = next(row for row in tethys_refs
                        if row["source_locator"].endswith("/plothandbookconfig.json#/17"))
        require(node["raw"]["Key"] == "145000004_65" and
                any(ref["state_key"] == tethys_scene["state_key"]
                    for ref in node["matching_references"]) and
                any(ref["state_key"] == tethys_scene["state_key"] and
                    ref["pointer"] == "/123/Flow"
                    for ref in handbook["matching_references"]),
                "Tethys archive exact quest-node and handbook state references", checks)
        sonoro_raw = json.loads(raw_states[3456]["raw"]["Actions"])[2]["Params"]["TalkItems"]
        tea_raw = json.loads(raw_states[3825]["raw"]["Actions"])[1]["Params"]["TalkItems"]
        require(len(next(t for t in sonoro_raw if t.get("TidTalk") ==
                         "Heihaian_main_1_3_51_28")["Options"]) == 3 and
                len(next(t for t in tea_raw if t.get("TidTalk") ==
                         "Heihaian_main_1_3_5605_4")["Options"]) == 2,
                "Sonoro three-reassurance and tea two-preference raw option menus",
                checks)
        honami_specs = ((9389, 4, 17, 8, 32), (9395, 4, 15, 9, 36))
        honami_lines = []
        honami_keys = {}
        for row_index, action_index, item_count, voiced_count, render_count in honami_specs:
            scene = scenes[(row_index, action_index)]
            members = [t for t in scene["talk_items"]
                       if t["technical_speaker_id"] == 1398 and t["play_voice"]]
            require(len(scene["talk_items"]) == item_count and
                    len(members) == voiced_count and
                    all(all(t["text_witnesses"][language]["status"] == "resolved"
                            for language in LANGUAGES) for t in members),
                    f"Honami {row_index}/{action_index}: item, Shorekeeper and four-text counts",
                    checks)
            linked = [line for line in lines if line["source_locator"] in
                      {t["source_locator"] for t in members}]
            renders = [render for line in linked for render in line["renders"]]
            require(len(linked) == voiced_count and len(renders) == render_count and
                    {(line["source_locator"], line["text_key"]) for line in linked} ==
                    {(t["source_locator"], t["text_key"]) for t in members} and
                    all({r["voice_language"] for r in line["renders"]} == LANGUAGES
                        for line in linked),
                    f"Honami {row_index}/{action_index}: exact occurrence and four-dub render joins",
                    checks)
            require(len({r["canonical_pcm_sha256"] for r in renders}) == render_count and
                    all(r["materialization_status"] == "flac_roundtrip_pcm_identical" and
                        all(len(r[field]) == 64 for field in
                            ("canonical_pcm_sha256", "flac_sha256", "expected_wem_sha256")) and
                        r.get("event_id") is None and r.get("bank_id") is None and
                        r.get("numeric_media_id") is None for r in renders),
                    f"Honami {row_index}/{action_index}: distinct PCM and unresolved explicit Wwise IDs",
                    checks)
            honami_lines.extend(linked)
            honami_keys.update({t["text_key"]: t for t in members})
        require(len(honami_lines) == 17 and
                len({r["canonical_pcm_sha256"] for line in honami_lines
                     for r in line["renders"]}) == 68,
                "two Honami actions are seventeen already-selected lines and 68 PCM objects",
                checks)
        honami_tea = json.loads(raw_states[9389]["raw"]["Actions"])[4]["Params"]
        honami_rift = json.loads(raw_states[9395]["raw"]["Actions"])[4]["Params"]
        require(honami_tea["TalkSequence"][:3] == [[1, 2, 3], [4], [5]] and
                [o["OptionTextKey"] for o in
                 honami_tea["SequenceTransitions"]["0"]] ==
                ["Main_Honami_2_8_2_43_4", "Main_Honami_2_8_2_43_5"] and
                {honami_tea["SequenceTransitions"][route][0]["NextSequenceIndex"]
                 for route in ("1", "2")} == {3},
                "Honami drink alternative sugar/tea replies reconverge", checks)
        require(honami_rift["TalkSequence"][:3] == [[1], [2, 3], [4, 5, 6]] and
                [o["OptionTextKey"] for o in
                 honami_rift["SequenceTransitions"]["0"]] ==
                ["Main_Honami_2_8_2_65_2", "Main_Honami_2_8_2_65_3"] and
                {honami_rift["SequenceTransitions"][route][0]["NextSequenceIndex"]
                 for route in ("1", "2")} == {3},
                "Honami diagnostic alternative Rover replies reconverge", checks)
        signature = honami_keys["Main_Honami_2_8_2_65_11"]["text_witnesses"]
        require("相似" in signature["zh"]["content"] and
                "identical" in signature["en"]["content"] and
                "似た" in signature["ja"]["content"] and
                "비슷한" in signature["ko"]["content"] and
                "苦" in honami_keys["Main_Honami_2_8_2_43_3"]["text_witnesses"]["zh"]["content"],
                "Honami localized similar-versus-identical and tolerable bitterness anchors", checks)
        require(not any("#/4741/Actions!/5/Params/TalkItems/" in line["source_locator"]
                        for line in lines),
                "Aetherfin action absent from selected decoded voice cohort", checks)
        package = json.loads((source / "character_source_package.json").read_text(encoding="utf-8"))
        combat = {row["content"]["text_key"]: row for row in package["favor_words"]
                  if row["content"]["text_key"] in
                  {f"FavorWord_1505{suffix}_Content" for suffix in range(45, 53)}}
        require(len(combat) == 8 and all(
            combat[f"FavorWord_1505{suffix}_Content"]["id"] == 150500 + suffix and
            combat[f"FavorWord_1505{suffix}_Content"]["source_locator"].endswith(
                f"favorword.json#/{1520 + suffix - 45}") and
            all(combat[f"FavorWord_1505{suffix}_Content"]["content"]["values"][lang]["status"] ==
                "resolved" for lang in ("zh-Hans", "en", "ja", "ko"))
            for suffix in range(45, 53)),
            "eight exact combat archive rows and four resolved witnesses each", checks)
        require("疼痛的感觉" in combat["FavorWord_150546_Content"]["content"]["values"]["zh-Hans"]["content"] and
                "The feeling of" in combat["FavorWord_150546_Content"]["content"]["values"]["en"]["content"] and
                "可用性降低" in combat["FavorWord_150548_Content"]["content"]["values"]["zh-Hans"]["content"] and
                "Durability lowered" in combat["FavorWord_150548_Content"]["content"]["values"]["en"]["content"] and
                "機能低下" in combat["FavorWord_150548_Content"]["content"]["values"]["ja"]["content"] and
                "가동률 저하" in combat["FavorWord_150548_Content"]["content"]["values"]["ko"]["content"],
                "pain and reduced-capacity localization contrast", checks)
        require("不要妨碍我" in combat["FavorWord_150549_Content"]["content"]["values"]["zh-Hans"]["content"] and
                "실패할 순 없어" in combat["FavorWord_150549_Content"]["content"]["values"]["ko"]["content"] and
                "别为我难过" in combat["FavorWord_150551_Content"]["content"]["values"]["zh-Hans"]["content"] and
                "Durability... depleted" in combat["FavorWord_150552_Content"]["content"]["values"]["en"]["content"] and
                "使用限度" in combat["FavorWord_150552_Content"]["content"]["values"]["zh-Hans"]["content"],
                "interference, grief and final-limit localization contrasts", checks)
        battle_events = {46: (1521, 936801762, "behitfly_02"),
                         47: (1522, 542532701, "hpdown01"),
                         48: (1523, 542532702, "hpdown02"),
                         51: (1526, 1613711691, "die_02"),
                         52: (1527, 1613711690, "die_03")}
        require(all(combat[f"FavorWord_1505{suffix}_Content"]["voice_asset"].endswith(
                    f"{stem}.play_favor_word_shouanren_com_{stem}")
                    for suffix, (_, _, stem) in battle_events.items()),
                "five explicit battle-event paths retained at source rows", checks)
        require(all(
            len(rows := [row for row in lines
                         if row["text_key"] == f"FavorWord_1505{suffix}_Content"]) == 1 and
            rows[0]["source_locator"] == combat[f"FavorWord_1505{suffix}_Content"]["source_locator"] and
            {render["voice_language"] for render in rows[0]["renders"]} == LANGUAGES and
            all(render["event_id"] == event_id and
                render["numeric_media_id"] is not None and
                render["materialization_status"] == "flac_roundtrip_pcm_identical" and
                len(render["canonical_pcm_sha256"]) == 64 and
                len(render["flac_sha256"]) == 64 for render in rows[0]["renders"])
            for suffix, (_, event_id, _) in battle_events.items()),
            "five battle barks preserve four exact explicit-ID PCM-valid render joins", checks)
        require(all(
            len(rows := [row for row in lines
                         if row["text_key"] == f"FavorWord_1505{suffix}_Content"]) == 1 and
            len(rows[0]["renders"]) == 4 and
            all(render["event_id"] is not None and
                render["numeric_media_id"] is not None and
                render["materialization_status"] == "flac_roundtrip_pcm_identical"
                for render in rows[0]["renders"])
            for suffix in range(45, 53)),
            "all eight combat archive entries have four explicit-ID PCM-valid renders", checks)
        index = {(r["text_key"], r["semantic_voice_occurrence_id"]): r for r in lines}
        for c in cases["cases"]:
            row = index[(c["text_key"], c["semantic_voice_occurrence_id"])]
            require(c["source_locator"] == row["source_locator"],
                    f"source locator: {c['text_key']}", checks)
            require(all(row["text_witnesses"][lang]["status"] == "resolved" for lang in LANGUAGES),
                    f"four text witnesses: {c['text_key']}", checks)
            expected_r = {(r["runtime_render_variant_id"], r["canonical_pcm_sha256"], r["flac_sha256"])
                          for r in row["renders"]}
            observed_r = {(r["render_variant_id"], r["canonical_pcm_sha256"], r["flac_sha256"])
                          for r in c["renders"]}
            require(expected_r == observed_r, f"exact render join: {c['text_key']}", checks)
        cohort_path = source_root / "_research" / "character_packets" / "Shorekeeper" / "audio_work" / "SHOREKEEPER_SOURCE_COHORT_AUDIT.json"
        cohort_bytes = cohort_path.read_bytes()
        require(hashlib.sha256(cohort_bytes).hexdigest() ==
                "8ffdfc8197f0fd1cc176a9780273e6e4c29fc5e003e9e357c61a0ce113c57303",
                "pinned nine-action cohort artifact hash", checks)
        cohort_audit = json.loads(cohort_bytes)
        require(cohort_audit["character"] == "Shorekeeper" and
                cohort_audit["source_commit"] == COMMIT and
                cohort_audit["line_analysis_sha256"] == hashlib.sha256(
                    (voice / "COMPLETE_VOICE_LINE_ANALYSIS.jsonl").read_bytes()).hexdigest(),
                "cohort character, source and line-table pin", checks)
        require(cohort_audit["whole_measured_object_count"] == 2048 and
                cohort_audit["whole_measured_integrity_pass_count"] == 2048 and
                not cohort_audit["human_perceptual_review_performed"],
                "cohort whole-scope QC without implied listening", checks)
        cohorts = cohort_audit["cohorts"]
        require(len(cohorts) == 9 and
                sum(c["semantic_lines"] for c in cohorts) == 208 and
                sum(c["render_associations"] for c in cohorts) == 832,
                "nine cohorts: 208 semantic lines and 832 render associations", checks)
        members = [member for cohort in cohorts for member in cohort["members"]]
        require(len(members) == 832 and
                len({m["semantic_voice_occurrence_id"] for m in members}) == 208 and
                len({m["canonical_pcm_sha256"] for m in members}) == 832 and
                len({m["render_analysis_id"] for m in members}) == 832,
                "cohorts are distinct selected semantic, render and PCM sets", checks)
        for cohort in cohorts:
            require(len(cohort["source_actions"]) == 1 and
                    cohort["render_associations"] == len(cohort["members"]) and
                    cohort["semantic_lines"] == len({
                        m["semantic_voice_occurrence_id"] for m in cohort["members"]}),
                    f"cohort member accounting: {cohort['name']}", checks)
            row, action = cohort["source_actions"][0].split("/")
            expected_locator_fragment = f"#/{row}/Actions!/{action}/Params/TalkItems/"
            require(all(expected_locator_fragment in m["source_locator"] and
                        set(m["flags"]) <= {"pitch_fewer_than_10_voiced_frames",
                                             "pitch_parameter_sensitive", "pitch_edge_band_frequent"}
                        for m in cohort["members"]),
                    f"exact action ownership and bounded pitch flags: {cohort['name']}", checks)
        member_joins_valid = True
        for m in members:
            row = index[(m["text_key"], m["semantic_voice_occurrence_id"])]
            render = next(r for r in row["renders"] if r["render_analysis_id"] == m["render_analysis_id"])
            member_joins_valid &= (m["source_locator"] == row["source_locator"] and
                                   (m["voice_language"], m["canonical_pcm_sha256"], m["flac_sha256"]) ==
                                   (render["voice_language"], render["canonical_pcm_sha256"], render["flac_sha256"]))
        require(member_joins_valid, "832 cohort members match pinned semantic and PCM renders", checks)
        audio = json.loads(summary.read_text(encoding="utf-8"))
        require((audio["manifest_objects"], audio["measured_objects"],
                 audio["repeated_pcm_manifest_rows"]) == (2048, 2048, 4),
                "measured-object counts", checks)
        require(not audio["failed_objects"] and not audio["human_perceptual_review_performed"],
                "no local measurement failures; human listening not implied", checks)
        result["source_crosscheck"] = "passed"
    result["result"] = "pass"
    result["check_count"] = len(checks)
    return result


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-root", type=Path)
    parser.add_argument("--write-report", action="store_true")
    args = parser.parse_args()
    report = validate(args.source_root)
    if args.write_report:
        (packet_artifact(HERE, "VALIDATION_REPORT.json")).write_text(
            json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8", newline="\n")
    print(json.dumps({k: report[k] for k in
                      ("packet", "source_crosscheck", "result", "check_count")}, indent=2))


if __name__ == "__main__":
    main()
