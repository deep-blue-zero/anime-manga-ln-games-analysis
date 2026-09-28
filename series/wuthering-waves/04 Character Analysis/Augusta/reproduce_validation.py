#!/usr/bin/env python3
"""Validate Augusta's draft packet; optionally crosscheck private primary evidence.

This is a structural/identity/media-join check, not literary truth, graph-path
exhaustiveness, generative fidelity, or human listening. Only --write-report writes.
"""

from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import re


HERE = Path(__file__).resolve().parent
COMMIT = "353f2eaed119bc9f680eab92807d20ac75a79b40"
LANGUAGES = {"en", "ja", "ko", "zh"}
MEDIA_SUFFIXES = {".wav", ".flac", ".wem", ".mp3", ".mp4", ".png", ".webp", ".pak"}


def jsonl(path: Path) -> list[dict]:
    with path.open(encoding="utf-8") as handle:
        return [json.loads(line) for line in handle if line.strip()]


def require(condition: bool, message: str, checks: list[str]) -> None:
    if not condition:
        raise AssertionError(message)
    checks.append(message)


def validate(source_root: Path | None) -> dict:
    checks: list[str] = []
    matrix = (HERE / "WUWA_AUGUSTA_EVIDENCE_AND_FALSIFICATION_MATRIX.md").read_text(encoding="utf-8")
    evidence_ids = set(re.findall(r"\| (AUG-E\d{2}) \|", matrix))
    claim_ids = set(re.findall(r"\| (AUG-C\d{2}) —", matrix))
    require(evidence_ids == {f"AUG-E{index:02d}" for index in range(1, 45)},
            "44 contiguous evidence bundles", checks)
    require(claim_ids == {f"AUG-C{index:02d}" for index in range(1, 41)},
            "40 contiguous claim rows", checks)
    angel_profile = (HERE / "WUWA_AUGUSTA_ANGEL_FABIANUM_TESTIMONY_AND_HOPE_PROFILE.md").read_text(
        encoding="utf-8")
    require("flow#/8402/4/29–30" in angel_profile
            and "FavorWord_130617_Content" in angel_profile
            and "AUG-E26" in angel_profile,
            "Angel specialist separates witnessed change from later hope", checks)
    cohort_profile = (HERE / "WUWA_AUGUSTA_SOURCE_DEFINED_AUDIO_COHORT_AUDIT.md").read_text(
        encoding="utf-8")
    require("189 semantic voice occurrences" in cohort_profile
            and "not a controlled actor experiment" in cohort_profile
            and "source_generation_frozen: true" in cohort_profile,
            "source-cohort report retains count, inference boundary and freeze state", checks)
    combat_profile = (HERE / "WUWA_AUGUSTA_COMBAT_TRIGGER_AND_ARCHIVE_KEY_IDENTITY_PROFILE.md").read_text(
        encoding="utf-8")
    require("#/2519" in combat_profile and
            "FavorWord_130632_Content" in combat_profile and
            "#/2622" in combat_profile and
            "source_generation_frozen: true" in combat_profile,
            "combat archive crosswalk retains nonmonotonic key and source pin", checks)
    hunt_profile = (HERE / "WUWA_AUGUSTA_HUNT_AEOLUS_AND_RECOGNITION_AFTER_VICTORY_PROFILE.md").read_text(
        encoding="utf-8")
    require(all(token in hunt_profile for token in
                ("QuestTree_Summary_210080", "QuestTree_Summary_240803",
                 "XJZM_34_1", "InfoDisplay_26010001_Text", "AUG-E35", "AUG-E36")),
            "hunt and Aeolus specialist retains exact source and matrix anchors", checks)
    earthrend_profile = (HERE / "WUWA_AUGUSTA_EARTHREND_HUNT_CONSULTANT_AND_VOLUNTEER_COMMAND_PROFILE.md").read_text(
        encoding="utf-8")
    require(all(token in earthrend_profile for token in
                ("flow#/8371/3", "flow#/8380/3", "flow#/8388/4",
                 "Main_Linaxita_2_9_370_57", "250004", "1580", "350006",
                 "AUG-E37", "AUG-E38", "AUG-E39")),
            "Earthrend specialist keeps plan, narrator and speaker identities distinct", checks)
    authority_profile = (HERE / "WUWA_AUGUSTA_SILVA_VERDICT_AVIDIUS_INVITATION_AND_EVACUATION_PROFILE.md").read_text(
        encoding="utf-8")
    require(all(token in authority_profile for token in
                ("flow#/6989/4", "flow#/8381/3", "flow#/10906/3",
                 "MAIN_RYAM_44_23", "FavorWord_130614_Content",
                 "AUG-E40", "AUG-E41", "AUG-E42", "64 distinct")),
            "Silva/Avidius/evacuation specialist retains distinct actions and evidence", checks)
    whisper_profile = (HERE / "WUWA_AUGUSTA_WHISPER_GUIDANCE_PROPHETIC_TEST_AND_ANGEL_IDENTITY_PROFILE.md").read_text(
        encoding="utf-8")
    require(all(token in whisper_profile for token in
                ("flow#/8413/1", "flow#/8415/1", "flow#/8416/1",
                 "QuestNodeData#/13922", "350005", "AUG-E43", "AUG-E44",
                 "AUG-C39", "AUG-C40", "96 distinct")),
            "whisper specialist retains exact sources, speaker and inference boundaries", checks)
    require(not any(path.suffix.lower() in MEDIA_SUFFIXES for path in HERE.rglob("*") if path.is_file()),
            "no raw media in Git packet", checks)
    for path in HERE.glob("WUWA_AUGUSTA_*.md"):
        body = path.read_text(encoding="utf-8")
        require(body.startswith("---\n") and "\nstatus: draft_noncurrent\n" in body,
                f"draft authority: {path.name}", checks)
        require("\ndo_not_use_as_current_authority: true\n" in body,
                f"noncurrent flag: {path.name}", checks)
        require(f"\nsource_commit: {COMMIT}\n" in body,
                f"source pin: {path.name}", checks)
    model = json.loads((HERE / "WUWA_AUGUSTA_CHARACTER_MODEL_PACKAGE.json").read_text(encoding="utf-8"))
    require(model["authority"] == "draft_noncurrent" and model["source_commit"] == COMMIT,
            "model authority and source pin", checks)
    rules = model["rules"]
    require({rule["id"] for rule in rules} ==
            {f"AUG-R{index:02d}" for index in range(1, 22)} and len(rules) == 21,
            "21 contiguous model rules", checks)
    friend_rule = next(rule for rule in rules if rule["id"] == "AUG-R07")
    require("memory-erasure mechanism" in friend_rule["exceptions_and_limits"]
            and "not fully disclosed" in friend_rule["behavioral_tendency"],
            "Iuno friendship rule separates suspected pain from known mechanism", checks)
    require(all(set(rule["evidence_ids"]) <= evidence_ids for rule in rules),
            "all model evidence IDs resolve", checks)
    require(all(rule["probability"] is None for rule in rules),
            "no fabricated numerical probabilities", checks)
    probes = (HERE / "WUWA_AUGUSTA_MODEL_FIDELITY_AND_STRESS_TEST_PRE_AV.md").read_text(encoding="utf-8")
    require(set(re.findall(r"\| (AUG-P\d{2}) \|", probes)) ==
            {f"AUG-P{index:02d}" for index in range(1, 51)},
            "50 contiguous non-blind probes", checks)
    require("eighth constructed interaction test" in probes and
            "AUG-E36–E39" in probes and
            "ninth constructed interaction test" in probes and
            "AUG-E40–E42" in probes,
            "constructed Earthrend and authority interactions are explicitly unrun", checks)
    require("tenth constructed interaction test" in probes
            and "E42–E44" in probes and "C39–C40" in probes,
            "constructed whisper countertest is explicitly unrun", checks)
    cases = json.loads((HERE / "AUDIO_MATCHED_SEMANTIC_CASES.json").read_text(encoding="utf-8"))
    require(cases["semantic_cases"] == 18 and len(cases["cases"]) == 18,
            "18 matched semantic cases", checks)
    crosswalk = (HERE / "WUWA_AUGUSTA_AV_HUMAN_RETRIEVAL_CROSSWALK.md").read_text(encoding="utf-8")
    require(all(f"`{case['text_key']}`" in crosswalk for case in cases["cases"]),
            "all 18 exact sound cases occur in AV crosswalk", checks)
    require("FavorStory_130604_Content" in crosswalk and "independent direct primary witness" in crosswalk,
            "Magno death remains a causal negative-control target", checks)
    require(all(token in crosswalk for token in
                ("AUG-R10", "AUG-R11", "AUG-R12", "MAIN_RYAM_44_23",
                 "Main_Linaxita_2_9_320_9", "Main_Linaxita_2_9_350_19")),
            "three new scene controls and exact-line nominations present", checks)
    require(all(token in crosswalk for token in
                ("R13", "R14", "Main_Linaxita_2_9_515_9",
                 "Main_Linaxita_2_9_515_12", "Main_Linaxita_2_9_515_15",
                 "Main_Linaxita_2_9_525_8", "Main_Linaxita_2_9_525_11",
                 "Main_Linaxita_2_9_525_14")),
            "whisper exact-line nominations and runtime controls present", checks)
    require(sum(len(case["renders"]) for case in cases["cases"]) == 72,
            "72 selected render variants", checks)
    require(all({render["language"] for render in case["renders"]} == LANGUAGES
                for case in cases["cases"]), "each case has four dubs", checks)
    require(all(len(render[name]) == 64 for case in cases["cases"] for render in case["renders"]
                for name in ("wem_sha256", "canonical_pcm_sha256", "flac_sha256")),
            "selected render hashes present", checks)
    selected_renders = [render for case in cases["cases"] for render in case["renders"]]
    require(sum(render["event_id"] is None and render["numeric_media_id"] is None
                for render in selected_renders) == 32
            and all((render["event_id"] is None) == (render["numeric_media_id"] is None)
                    for render in selected_renders),
            "32/72 paired null event and numeric-media IDs preserved", checks)
    angel_cases = {case["text_key"]: case for case in cases["cases"]
                   if case["text_key"] in ("Main_Linaxita_2_9_470_35",
                                           "Main_Linaxita_2_9_470_36")}
    require(len(angel_cases) == 2
            and angel_cases["Main_Linaxita_2_9_470_35"]["source_locator"].endswith(
                "/8402/Actions!/4/Params/TalkItems/29")
            and angel_cases["Main_Linaxita_2_9_470_36"]["source_locator"].endswith(
                "/8402/Actions!/4/Params/TalkItems/30"),
            "two witnessed Angel-report sound cases retain exact source positions", checks)
    result = {"packet": "Augusta", "scope": "AUGUSTA_PINNED_3_6_0_TEXT_AUDIO_PRE_AV",
              "checks": checks, "source_crosscheck": "not_requested"}
    if source_root is not None:
        source = source_root / "ANALYSIS" / "Characters" / "Augusta"
        voice = source_root / "_voice_media" / "character" / "complete_voice_corpus" / "Augusta" / "v0_1"
        summary = source_root / "_research" / "character_packets" / "Augusta" / "audio_work" / "AUDIO_MEASUREMENT_SUMMARY.json"
        audit = json.loads((source / "COLLECTION_AUDIT.json").read_text(encoding="utf-8"))
        quest_nodes = {
            node["Id"]: node for node in json.loads(
                (source_root / "_sources" / "Arikatsu_WutheringWaves_Data" /
                 "BinData" / "QuestTree" / "questtreenode.json").read_text(encoding="utf-8"))
        }
        require(quest_nodes[211000]["NextNode"] == 210080
                and quest_nodes[210080]["PreNode"] == [211000]
                and quest_nodes[210080]["QuestArray"] == [311000001, 311000002]
                and quest_nodes[210080]["Summary"] == "QuestTree_Summary_210080",
                "public ascent and joint-hunt quest-tree links", checks)
        require(all(quest_nodes[node]["MainQuestNode"] == 210080
                    for node in (240802, 240803, 240804))
                and quest_nodes[240802]["NextNode"] == 240803
                and quest_nodes[240803]["NextNode"] == 240804
                and quest_nodes[240804]["PreNode"] == [240803]
                and quest_nodes[240804]["QuestArray"] == [176750003],
                "Aeolus sidequest ordering and main-node attachment", checks)
        mentions = {row["text_key"]: row for row in jsonl(source / "source_mentions.jsonl")}
        require(all(key in mentions and
                    all(mentions[key]["localizations"][language]["status"] == "resolved"
                        for language in ("zh-Hans", "en", "ja", "ko"))
                    for key in ("QuestTree_Summary_211000", "QuestTree_Summary_210080",
                                "QuestTree_Summary_240804", "XJZM_34_1")),
                "four resolved locale witnesses for ascent, hunt, letter summary and letter", checks)
        hunt_text = mentions["QuestTree_Summary_210080"]["localizations"]
        require("克里斯托弗正谋划着某些事" in hunt_text["zh-Hans"]["content"]
                and "Cristoforo is already plotting" in hunt_text["en"]["content"]
                and "クリストフォロ" in hunt_text["ja"]["content"]
                and "크리스토포로" in hunt_text["ko"]["content"],
                "four-locale victory followed by hidden continuing plot", checks)
        letter_text = mentions["XJZM_34_1"]["localizations"]
        require("驳回你的申请" in letter_text["zh-Hans"]["content"]
                and "It is hereby denied" in letter_text["en"]["content"]
                and "却下した" in letter_text["ja"]["content"]
                and "반려합니다" in letter_text["ko"]["content"],
                "four-locale literal withdrawal rejection", checks)
        letter_flow = next(row for row in jsonl(source / "RAW_RELEVANT_FLOW_STATES.jsonl")
                           if row["source_locator"].endswith("/flowstate.json#/10025"))
        letter_actions = json.loads(letter_flow["raw"]["Actions"])
        require(letter_actions[1]["Params"]["TalkItems"][0]["TidTalk"] == "XJZM_34_1"
                and letter_actions[1]["Params"]["TalkItems"][0]["WhoId"] == 750189,
                "letter is displayed in exact flow action with technical speaker 750189", checks)
        raw_flows = {
            int(row["source_locator"].rsplit("#/", 1)[1]): row["raw"]
            for row in jsonl(source / "RAW_RELEVANT_FLOW_STATES.jsonl")
        }
        first_whisper = json.loads(raw_flows[8413]["Actions"])[1]
        first_items = first_whisper["Params"]["TalkItems"]
        require(raw_flows[8413]["StateKey"] == "剧情_2_6_狄斯台地主线_上半_2_23_1"
                and first_whisper["Name"] == "ShowTalk"
                and len(first_items) == 14
                and first_whisper["Params"]["TalkSequence"] == [list(range(1, 15))]
                and not first_whisper["Params"].get("SequenceTransitions")
                and first_items[0]["Type"] == "Option"
                and first_items[0]["Options"][0]["TidTalkOption"] == "Main_Linaxita_2_9_515_2"
                and first_items[0]["Options"][0]["Actions"] == []
                and all(item.get("WhoId") == 250022 and item.get("PlayVoice") is True
                        for item in first_items[1:]),
                "8413 whisper testimony has one empty-action Rover option and 13 linear Augusta turns", checks)
        later_whisper = json.loads(raw_flows[8415]["Actions"])[1]
        later_items = later_whisper["Params"]["TalkItems"]
        require(raw_flows[8415]["StateKey"] == "剧情_2_6_狄斯台地主线_上半_2_25_1"
                and later_whisper["Name"] == "ShowTalk"
                and len(later_items) == 17
                and later_whisper["Params"]["TalkSequence"] == [list(range(1, 18))]
                and not later_whisper["Params"].get("SequenceTransitions")
                and Counter(item.get("WhoId") for item in later_items) == {350005: 6, 250022: 11}
                and all(item.get("PlayVoice") is True for item in later_items)
                and [later_items[index]["TidTalk"] for index in (6, 9, 12)] == [
                    "Main_Linaxita_2_9_525_8", "Main_Linaxita_2_9_525_11",
                    "Main_Linaxita_2_9_525_14"],
                "8415 confrontation keeps hostile speaker, Augusta and order distinct", checks)
        silent_retort = json.loads(raw_flows[8416]["Actions"])[1]["Params"]["TalkItems"][3]
        require(silent_retort["WhoId"] == 250022
                and silent_retort["TidTalk"] == "Main_Linaxita_2_9_530_4"
                and silent_retort.get("PlayVoice") is not True,
                "8416 anti-divinity retort is source-unvoiced", checks)
        earthrend_specs = ((8371, 3, 14, 12868, "311000001_127", 19),
                           (8380, 3, 28, 12927, "311000001_131", 14),
                           (8388, 4, 38, 12929, "311000001_133", 15))
        quest_rows = json.loads((source_root / "_sources" / "Arikatsu_WutheringWaves_Data" /
                                 "BinData" / "QuestNodeData" / "questnodedata.json").read_text(
                                     encoding="utf-8"))
        whisper_quest = quest_rows[13922]
        require(whisper_quest["Key"] == "311000002_160"
                and whisper_quest["Data"]["Condition"]["Flow"] == {
                    "FlowListName": "剧情_2_6_狄斯台地主线_上半_2", "FlowId": 23,
                    "StateId": 1},
                "8413 has a direct exact-state quest join; 8415 is not substituted for it", checks)
        for row_index, action_index, flow_id, node_index, node_key, augusta_count in earthrend_specs:
            node = quest_rows[node_index]
            flow = node["Data"]["Condition"]["Flow"]
            require(node["Key"] == node_key and flow["FlowId"] == flow_id
                    and flow["StateId"] == 1
                    and flow["FlowListName"] == "剧情_2_6_狄斯台地主线_上半_1",
                    f"exact quest-node association for Earthrend flow {flow_id}", checks)
            actions = json.loads(raw_flows[row_index]["Actions"])
            items = actions[action_index]["Params"]["TalkItems"]
            require(actions[action_index]["Name"] == "ShowTalk"
                    and sum(item.get("WhoId") == 250022 and item.get("PlayVoice") is True
                            for item in items) == augusta_count,
                    f"Augusta speaker and voiced count in flow row {row_index}", checks)
        earthrend_items = {
            row_index: json.loads(raw_flows[row_index]["Actions"])[action_index]["Params"]
            for row_index, action_index, *_ in earthrend_specs
        }
        late = earthrend_items[8388]
        by_id = {item["Id"]: item for item in late["TalkItems"]}
        sequence = late["TalkSequence"][0]
        require(sequence.index(49) == sequence.index(22) + 1
                and sequence.index(23) == sequence.index(49) + 1
                and by_id[49]["WhoId"] == 83
                and by_id[49]["TidTalk"] == "Main_Linaxita_2_9_370_57",
                "failed-plan narration is inserted between dialogue items 22 and 23", checks)
        require(by_id[24]["WhoId"] == by_id[31]["WhoId"] == 250004
                and by_id[41]["WhoId"] == 1580
                and by_id[42]["WhoId"] == 350006
                and by_id[44]["WhoId"] == by_id[45]["WhoId"] == 250022,
                "consultant, younger volunteer, elder and Augusta have distinct speakers", checks)
        authority_specs = (
            (6989, 4, 9725, "125000126_33", "剧情_2_4_七丘主线_上2", 3, 5, 31, 6),
            (8381, 3, 12928, "311000001_132", "剧情_2_6_狄斯台地主线_上半_1", 29, 1, 15, 5),
            (10906, 3, 14490, "311000001_227", "剧情_2_6_狄斯台地主线_上半_1", 85, 2, 19, 5),
        )
        authority_items = {}
        for row_index, action_index, node_index, node_key, flow_name, flow_id, state_id, item_count, augusta_count in authority_specs:
            node = quest_rows[node_index]
            flow = node["Data"]["Condition"]["Flow"]
            require(node["Key"] == node_key
                    and (flow["FlowListName"], flow["FlowId"], flow["StateId"]) ==
                    (flow_name, flow_id, state_id),
                    f"exact quest-node join for authority scene {row_index}", checks)
            action = json.loads(raw_flows[row_index]["Actions"])[action_index]
            items = action["Params"]["TalkItems"]
            authority_items[row_index] = items
            require(action["Name"] == "ShowTalk" and len(items) == item_count
                    and sum(item.get("WhoId") == 250022 and item.get("PlayVoice") is True
                            for item in items) == augusta_count,
                    f"Augusta speaker and voiced count in authority scene {row_index}", checks)
        arena = authority_items[6989]
        arena_by_key = {item["TidTalk"]: item for item in arena if "TidTalk" in item}
        require(all(arena[index]["WhoId"] == 250022 for index in (2, 21, 23, 24, 25, 26))
                and arena[21]["TidTalk"] == "MAIN_RYAM_44_23"
                and arena[26]["TidTalk"] == "MAIN_RYAM_44_28"
                and arena[27]["WhoId"] == 850351
                and arena_by_key["MAIN_RYAM_44_18"]["WhoId"] == 250024
                and arena_by_key["MAIN_RYAM_44_22"]["WhoId"] == 250024,
                "arena allegation, Temple request/verdict, Augusta order and Julia response have separate speakers", checks)
        avidius = authority_items[8381]
        require(all(avidius[index]["WhoId"] == 250022 for index in range(6, 11))
                and avidius[7]["TidTalk"] == "Main_Linaxita_2_9_320_9"
                and avidius[9]["TidTalk"] == "Main_Linaxita_2_9_320_11"
                and avidius[11]["WhoId"] == 1580,
                "Avidius power naming, invitation and acceptance preserve speaker order", checks)
        crisis = authority_items[10906]
        require(crisis[3]["WhoId"] == 250022
                and all(crisis[index]["WhoId"] == 350005 for index in range(5, 11))
                and all(crisis[index]["WhoId"] == 250024 for index in range(11, 15))
                and all(crisis[index]["WhoId"] == 250022 for index in range(15, 19))
                and crisis[17]["TidTalk"] == "Main_Linaxita_2_9_350_19",
                "hostile voice, Iuno condition and Augusta evacuation retain distinct speaker sequence", checks)
        witnesses = {
            row["text_key"]: row["values"]
            for row in jsonl(source / "CONTEXT_TEXT_WITNESSES.jsonl")
        }
        require("no defense capabilities" in witnesses["Main_Linaxita_2_9_135_7"]["en"]["content"]
                and "완전히" in witnesses["Main_Linaxita_2_9_135_7"]["ko"]["content"],
                "Anchor Stone EN/KO personal-protection wording differs", checks)
        require("only option" in witnesses["Main_Linaxita_2_9_370_35"]["en"]["content"]
                and "一貫している" in witnesses["Main_Linaxita_2_9_370_35"]["ja"]["content"],
                "crisis option wording differs between EN and JA", checks)
        images = witnesses["MAIN_RYAM_44_23"]
        require("景象" in images["zh-Hans"]["content"]
                and "映像" in images["ja"]["content"]
                and "weight of your actions" in images["en"]["content"]
                and "무엇을 해야" in images["ko"]["content"],
                "Silva visual-evidence references occur in ZH/JA, not the same wording in EN/KO", checks)
        require("西尔瓦家" in witnesses["MAIN_RYAM_44_18"]["zh-Hans"]["content"]
                and "the Silvas" in witnesses["MAIN_RYAM_44_18"]["en"]["content"]
                and "Do not ever return" in witnesses["MAIN_RYAM_44_28"]["en"]["content"],
                "family-wide Iuno request differs from Augusta's Julia-directed departure order", checks)
        require("权力" in witnesses["Main_Linaxita_2_9_320_9"]["zh-Hans"]["content"]
                and "desire for power" in witnesses["Main_Linaxita_2_9_320_9"]["en"]["content"]
                and "Stand next to me" in witnesses["Main_Linaxita_2_9_320_11"]["en"]["content"],
                "Avidius power desire and invitation are explicit", checks)
        require("咳咳" in witnesses["Main_Linaxita_2_9_350_14"]["zh-Hans"]["content"]
                and "ゲホ" in witnesses["Main_Linaxita_2_9_350_14"]["ja"]["content"]
                and "콜록" in witnesses["Main_Linaxita_2_9_350_14"]["ko"]["content"]
                and "cough" not in witnesses["Main_Linaxita_2_9_350_14"]["en"]["content"].lower()
                and "If, and I say if" in witnesses["Main_Linaxita_2_9_350_15"]["en"]["content"]
                and "no one is left behind" in witnesses["Main_Linaxita_2_9_350_19"]["en"]["content"],
                "Iuno's conditional question and localized printed cough precede civilian evacuation", checks)
        require("每一次战斗时" in witnesses["Main_Linaxita_2_9_515_9"]["zh-Hans"]["content"]
                and "when to dodge" in witnesses["Main_Linaxita_2_9_515_9"]["en"]["content"]
                and "命运总会用更残酷" in witnesses["Main_Linaxita_2_9_515_12"]["zh-Hans"]["content"]
                and "has come true" in witnesses["Main_Linaxita_2_9_515_14"]["en"]["content"]
                and "語りかけてくる" in witnesses["Main_Linaxita_2_9_515_14"]["ja"]["content"],
                "guidance, reported punishment and JA/EN prophecy wording are preserved", checks)
        require("为什么现在又要" in witnesses["Main_Linaxita_2_9_525_8"]["zh-Hans"]["content"]
                and "对安吉尔做了什么" in witnesses["Main_Linaxita_2_9_525_11"]["zh-Hans"]["content"]
                and "what is stopping you" in witnesses["Main_Linaxita_2_9_525_14"]["en"]["content"]
                and "阻む理由は、どこにも" in witnesses["Main_Linaxita_2_9_525_14"]["ja"]["content"],
                "contradicted prophecy, unanswered Angel query and EN/JA invitation fork", checks)
        direct = audit["scopes"]["direct_character"]
        require(audit["valid"] and direct["voice_completeness_valid"],
                "selected collection audit valid", checks)
        require((audit["raw_flow_states"], audit["context_text_keys"],
                 audit["quest_references"], audit["distinct_quest_ids"]) ==
                (207, 4055, 108, 18), "contextual collection denominator", checks)
        require((direct["candidate_occurrences"], direct["accepted_occurrences"],
                 direct["source_voiced"], direct["source_unvoiced"]) ==
                (660, 643, 537, 106), "direct occurrence denominator", checks)
        require((direct["semantic_voice_lines"], direct["render_associations"],
                 direct["unique_flac_objects"]) ==
                (605, 2420, 2399), "voice line, association, object denominators", checks)
        decisions = jsonl(source / "occurrence_identity_crosswalk.jsonl")
        require(Counter(row["character_attribution"] for row in decisions) ==
                {"accepted_solo": 643, "rejected": 12, "unresolved": 5},
                "identity crosswalk counts", checks)
        line_rows = jsonl(voice / "COMPLETE_VOICE_LINE_ANALYSIS.jsonl")
        require(len(line_rows) == 605, "605 selected semantic voice rows", checks)
        whisper_renders = []
        for row_index, expected_count in ((8413, 13), (8415, 11)):
            cohort = [row for row in line_rows if
                      f"/{row_index}/Actions!/1/Params/TalkItems/" in row["source_locator"]]
            renders = [render for row in cohort for render in row["renders"]]
            require(len(cohort) == expected_count and len(renders) == 4 * expected_count
                    and all({render["voice_language"] for render in row["renders"]} == LANGUAGES
                            for row in cohort)
                    and len({render["canonical_pcm_sha256"] for render in renders}) == len(renders)
                    and all(render.get("event_id") is None
                            and render.get("numeric_media_id") is None
                            and render["source_wem_exists"]
                            and render["source_wem_sha256_verified"]
                            and render["materialization_status"] == "flac_roundtrip_pcm_identical"
                            for render in renders),
                    f"whisper row {row_index}: four-dub distinct PCM-valid paired-null joins", checks)
            whisper_renders.extend(renders)
        require(len(whisper_renders) == 96
                and len({render["canonical_pcm_sha256"] for render in whisper_renders}) == 96
                and not any("/8416/Actions!/1/Params/TalkItems/3" in row["source_locator"]
                            for row in line_rows),
                "24 whisper lines join 96 distinct PCM objects; unvoiced retort is absent", checks)
        for row_index, action_index, _, _, _, augusta_count in earthrend_specs:
            cohort = [row for row in line_rows if
                      f"/{row_index}/Actions!/{action_index}/Params/TalkItems/" in row["source_locator"]]
            renders = [render for row in cohort for render in row["renders"]]
            require(len(cohort) == augusta_count and len(renders) == 4 * augusta_count
                    and len({render["canonical_pcm_sha256"] for render in renders}) == len(renders)
                    and all(render["materialization_status"] == "flac_roundtrip_pcm_identical"
                            for render in renders),
                    f"Earthrend row {row_index}: four-dub distinct PCM-valid selected renders", checks)
        authority_renders = []
        for row_index, action_index, *_rest in authority_specs:
            augusta_count = _rest[-1]
            cohort = [row for row in line_rows if
                      f"/{row_index}/Actions!/{action_index}/Params/TalkItems/" in row["source_locator"]]
            renders = [render for row in cohort for render in row["renders"]]
            require(len(cohort) == augusta_count and len(renders) == 4 * augusta_count
                    and all({render["voice_language"] for render in row["renders"]} == LANGUAGES
                            for row in cohort)
                    and len({render["canonical_pcm_sha256"] for render in renders}) == len(renders)
                    and all(render.get("event_id") is None
                            and render.get("numeric_media_id") is None
                            and render["materialization_status"] == "flac_roundtrip_pcm_identical"
                            for render in renders),
                    f"authority row {row_index}: four-dub distinct PCM-valid paired-null render joins", checks)
            authority_renders.extend(renders)
        require(len(authority_renders) == 64
                and len({render["canonical_pcm_sha256"] for render in authority_renders}) == 64,
                "16 authority-scene lines join 64 distinct technical PCM objects", checks)
        by_key = {row["text_key"]: row for row in line_rows}
        metaphor = next(row for row in line_rows if row["source_locator"].endswith(
            "/7804/Actions!/4/Params/TalkItems/6"))
        require("鬣狗" in metaphor["text_witnesses"]["zh"]["content"]
                and "wolf" in metaphor["text_witnesses"]["en"]["content"]
                and "ハイエナ" in metaphor["text_witnesses"]["ja"]["content"]
                and "하이에나" in metaphor["text_witnesses"]["ko"]["content"],
                "fate metaphor's EN wolf versus ZH/JA/KO hyena fork", checks)
        require("找到安吉尔" in by_key["Main_Linaxita_2_9_470_35"]["text_witnesses"]["zh"]["content"]
                and "变成了可怕的怪物" in
                by_key["Main_Linaxita_2_9_470_36"]["text_witnesses"]["zh"]["content"]
                and "再也没见到过她" in
                by_key["Main_Linaxita_2_9_470_36"]["text_witnesses"]["zh"]["content"],
                "Angel testimony preserves found/transformed/no-later-sighting sequence", checks)
        package = json.loads((source / "character_source_package.json").read_text(encoding="utf-8"))
        combat_words = [word for word in package["favor_words"]
                        if 130632 <= word["id"] <= 130669]
        require(len(package["favor_words"]) == 68 and len(combat_words) == 37 and
                130650 not in {word["id"] for word in combat_words} and
                all(word["id"] != int(re.fullmatch(
                    r"FavorWord_(\d+)_Content", word["raw"]["Content"]).group(1))
                    for word in combat_words),
                "37 mismatched combat/traversal/reward raw IDs within 68 archive rows", checks)
        table_rows = re.findall(
            r"^\| (1306\d{2}) \| (1306\d{2}) \| `(?:favorword)?#/(\d+)` \|",
            combat_profile, re.MULTILINE)
        table_map = {int(raw_id): (int(key_suffix), int(position))
                     for raw_id, key_suffix, position in table_rows}
        require(len(table_rows) == len(table_map) == 37 and
                set(table_map) == {word["id"] for word in combat_words} and
                all(table_map[word["id"]] == (
                    int(re.fullmatch(r"FavorWord_(\d+)_Content", word["raw"]["Content"]).group(1)),
                    int(word["source_locator"].rsplit("/", 1)[-1]))
                    for word in combat_words),
                "all 37 published combat row/key/source-position pairs match pinned source", checks)
        archive_by_locator = {row["source_locator"]: row for row in line_rows
                              if row["record_class"] == "character_favor_archive"}
        friend_line = next(row for row in line_rows
                           if row["text_key"] == "FavorWord_130613_Content")
        friend_text = friend_line["text_witnesses"]
        require("痛苦" in friend_text["zh"]["content"]
                and "远比她告诉我的要多" in friend_text["zh"]["content"]
                and "deeper than what she's ever told me" in friend_text["en"]["content"]
                and "苦しみ" in friend_text["ja"]["content"]
                and "고통" in friend_text["ko"]["content"],
                "four archive witnesses support partly undisclosed Iuno pain", checks)
        combat_renders = []
        for word in combat_words:
            row = archive_by_locator[word["source_locator"]]
            require(row["text_key"] == word["raw"]["Content"] and
                    row["technical_render_coverage_status"] == "complete" and
                    len(row["renders"]) == 4 and
                    {render["voice_language"] for render in row["renders"]} == LANGUAGES,
                    f"exact complete four-dub combat voice join: raw {word['id']}", checks)
            require(all(word["content"]["values"]["zh-Hans" if lang == "zh" else lang]
                        ["content"] == row["text_witnesses"][lang]["content"]
                        for lang in LANGUAGES) and
                    all(render["event_path"] == word["voice_asset"] and
                        render["event_id"] is not None and
                        render["numeric_media_id"] is not None and
                        render["source_wem_exists"] and
                        render["source_wem_sha256_verified"] and
                        render["materialization_status"] == "flac_roundtrip_pcm_identical"
                        for render in row["renders"]),
                    f"text/event/media/PCM roundtrip for combat raw {word['id']}", checks)
            combat_renders.extend(row["renders"])
        require(len(combat_renders) == 148 and
                len({render["canonical_pcm_sha256"] for render in combat_renders}) == 148 and
                len({render["event_id"] for render in combat_renders}) == 37,
                "37 combat events and 148 distinct four-dub PCM-valid renders", checks)
        memory_scene = next(
            row for row in jsonl(source / "SCENE_AND_EVIDENCE_LEDGER.jsonl")
            if row["flow_state_row_index"] == 7741 and row["action_index"] == 5)
        memory_lines = {item["talk_id"]: item for item in memory_scene["talk_items"]}
        require(memory_lines[10]["technical_speaker_id"] == 250022
                and "神王的呓语" in memory_lines[10]["text_witnesses"]["zh"]["content"]
                and "分辨出它的蛊惑" in memory_lines[11]["text_witnesses"]["zh"]["content"]
                and "AUG-E30" in matrix,
                "later Sovereign-whisper account retains attribution and resistance", checks)
        angel_word = next(item["content"] for item in package["favor_words"]
                          if item["content"]["text_key"] == "FavorWord_130617_Content")
        require("信じたい" in angel_word["values"]["ja"]["content"]
                and "坚信" in angel_word["values"]["zh-Hans"]["content"],
                "JA wished belief and ZH conviction remain distinct from verified survival", checks)
        ascension_keys = {f"FavorWord_1306{suffix}_Content" for suffix in range(27, 32)}
        ascension = {item["content"]["text_key"]: item for item in package["favor_words"]
                     if item["content"]["text_key"] in ascension_keys}
        require(set(ascension) == ascension_keys, "five exact ascension content keys", checks)
        for offset, suffix in enumerate(range(27, 32)):
            key = f"FavorWord_1306{suffix}_Content"
            item = ascension[key]
            require(item["id"] == 130600 + suffix and
                    item["source_locator"].endswith(f"favorword.json#/{2501 + offset}") and
                    item["title"]["values"]["en"]["content"] ==
                    f"Ascension: {('I', 'II', 'III', 'IV', 'V')[offset]}",
                    f"archive row/key/locator/title: {key}", checks)
            require(all(item["content"]["values"][lang]["status"] == "resolved"
                        for lang in ("zh-Hans", "en", "ja", "ko")),
                    f"four resolved ascension witnesses: {key}", checks)
        sword = ascension["FavorWord_130627_Content"]["content"]["values"]
        require("执剑人的意志" in sword["zh-Hans"]["content"] and
                "will that commands" in sword["en"]["content"] and
                "剣を握る者の意志" in sword["ja"]["content"],
                "ascension-I wielder-will image", checks)
        roots = ascension["FavorWord_130628_Content"]["content"]["values"]
        require("元老院的官邸" in roots["zh-Hans"]["content"] and
                "大竞技场的高台" in roots["zh-Hans"]["content"] and
                "neither the Senate nor the Colosseum" in roots["en"]["content"],
                "ascension-II roots rather than office/spectacle", checks)
        sun = ascension["FavorWord_130629_Content"]["content"]["values"]
        require("唯有" in sun["zh-Hans"]["content"] and
                "only with" in sun["en"]["content"] and
                "限り" in sun["ja"]["content"] and
                "비춰야만" in sun["ko"]["content"],
                "ascension-III sun condition localization", checks)
        rules_word = ascension["FavorWord_130630_Content"]["content"]["values"]
        require("腐朽的规则下" in rules_word["zh-Hans"]["content"] and
                "When the rules are rigged" in rules_word["en"]["content"] and
                "腐敗した秩序の下" in rules_word["ja"]["content"] and
                "맞서는" in rules_word["ko"]["content"],
                "ascension-IV under-versus-against corrupt rules", checks)
        future = ascension["FavorWord_130631_Content"]["content"]["values"]
        require("if I had my way" in future["en"]["content"] and
                "也许" in future["zh-Hans"]["content"] and
                "かもしれぬ" in future["ja"]["content"] and
                "마음에 걸리는" in future["ko"]["content"],
                "ascension-V arena-preference contrast", checks)
        index = {(row["text_key"], row["semantic_voice_occurrence_id"]): row for row in line_rows}
        for case in cases["cases"]:
            row = index[(case["text_key"], case["semantic_voice_occurrence_id"])]
            require(case["source_locator"] == row["source_locator"],
                    f"source locator: {case['text_key']}", checks)
            require(all(row["text_witnesses"][lang]["status"] == "resolved"
                        for lang in LANGUAGES),
                    f"selected witnesses resolved: {case['text_key']}", checks)
            expected = {(render["runtime_render_variant_id"], render["canonical_pcm_sha256"],
                         render["flac_sha256"]) for render in row["renders"]}
            observed = {(render["render_variant_id"], render["canonical_pcm_sha256"],
                         render["flac_sha256"]) for render in case["renders"]}
            require(expected == observed, f"exact render join: {case['text_key']}", checks)
            source_by_variant = {render["runtime_render_variant_id"]: render
                                 for render in row["renders"]}
            require(all(render["event_id"] == source_by_variant[render["render_variant_id"]].get("event_id") and
                        render["numeric_media_id"] == source_by_variant[render["render_variant_id"]].get("numeric_media_id") and
                        render["source_virtual_path"] == source_by_variant[render["render_variant_id"]]["source_virtual_path"] and
                        render["wem_sha256"] == source_by_variant[render["render_variant_id"]]["expected_wem_sha256"]
                        for render in case["renders"]),
                    f"event/media/path/WEM join: {case['text_key']}", checks)
        for key in sorted(ascension_keys):
            case = next(case for case in cases["cases"] if case["text_key"] == key)
            require(case["source_locator"] == ascension[key]["source_locator"] and
                    len(case["renders"]) == 4 and
                    all(render["event_id"] is not None and render["numeric_media_id"] is not None
                        for render in case["renders"]),
                    f"exact archive locator and four explicit-ID renders: {key}", checks)
            if key == "FavorWord_130631_Content":
                require(all(render["qc_flags"] == ["long_object_check_subtitle_extent"]
                            for render in case["renders"]),
                        "ascension-V long-object extent review flag preserved in four dubs", checks)
            else:
                require(all(not render["qc_flags"] for render in case["renders"]),
                        f"clean-QC added ascension case: {key}", checks)
        audio = json.loads(summary.read_text(encoding="utf-8"))
        require((audio["manifest_objects"], audio["measured_objects"],
                 audio["repeated_pcm_manifest_rows"]) == (2399, 2399, 1),
                "full local audio measurement counts", checks)
        require(not audio["failed_objects"], "no local audio measurement failures", checks)
        cohort_path = summary.parent / "AUGUSTA_SOURCE_COHORT_AUDIT.json"
        cohort_bytes = cohort_path.read_bytes()
        cohort = json.loads(cohort_bytes)
        require(hashlib.sha256(cohort_bytes).hexdigest() ==
                "1c2f608c307a028a5c55a711f595937ab452915923a619708a0037039ea0b3b9",
                "source-cohort report matches documented frozen hash", checks)
        require(cohort["character"] == "Augusta"
                and len(cohort["cohorts"]) == 9
                and sum(group["semantic_lines"] for group in cohort["cohorts"]) == 189
                and sum(group["render_associations"] for group in cohort["cohorts"]) == 756,
                "nine exact source cohorts retain 189/756 denominator", checks)
        members = [member for group in cohort["cohorts"] for member in group["members"]]
        require(len({member["semantic_voice_occurrence_id"] for member in members}) == 189
                and len({member["canonical_pcm_sha256"] for member in members}) == 756
                and all(group["language_statistics"][lang]["integrity_pass_objects"] ==
                        group["semantic_lines"] for group in cohort["cohorts"] for lang in LANGUAGES),
                "cohort members unique and all selected objects integrity-valid", checks)
        source_by_occurrence = {row["semantic_voice_occurrence_id"]: row for row in line_rows}
        require(all(member["semantic_voice_occurrence_id"] in source_by_occurrence
                    and member["source_locator"] == source_by_occurrence[
                        member["semantic_voice_occurrence_id"]]["source_locator"]
                    and any(render["render_analysis_id"] == member["render_analysis_id"]
                            and render["canonical_pcm_sha256"] == member["canonical_pcm_sha256"]
                            for render in source_by_occurrence[
                                member["semantic_voice_occurrence_id"]]["renders"])
                    for member in members),
                "cohort membership matches exact semantic source and render IDs", checks)
        require(sum(group["language_statistics"][lang]["pitch_qualified_objects"]
                    for group in cohort["cohorts"] for lang in LANGUAGES) == 751,
                "751/756 selected objects qualify for pitch summaries", checks)
        result["source_crosscheck"] = "passed"
    result["result"] = "pass"
    result["check_count"] = len(checks)
    return result


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-root", type=Path,
                        help="Extraction workspace for deeper local evidence crosscheck")
    parser.add_argument("--write-report", action="store_true")
    args = parser.parse_args()
    report = validate(args.source_root)
    if args.write_report:
        (HERE / "VALIDATION_REPORT.json").write_text(
            json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8", newline="\n")
    print(json.dumps({key: report[key] for key in
                      ("packet", "source_crosscheck", "result", "check_count")}, indent=2))


if __name__ == "__main__":
    main()
