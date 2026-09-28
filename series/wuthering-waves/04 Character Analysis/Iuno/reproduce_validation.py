#!/usr/bin/env python3
"""Validate Iuno's draft packet and optionally crosscheck private evidence.

Structural, identity, text-quality and media joins only: not literary truth,
exhaustive branch coverage, generative fidelity or human listening.
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
    matrix = (HERE / "WUWA_IUNO_EVIDENCE_AND_FALSIFICATION_MATRIX.md").read_text(encoding="utf-8")
    evidence_ids = set(re.findall(r"\| (IUN-E\d{2}) \|", matrix))
    claim_ids = set(re.findall(r"\| (IUN-C\d{2}) —", matrix))
    require(len(evidence_ids) == 47, "47 unique evidence bundles", checks)
    require(len(claim_ids) == 42, "42 unique claim rows", checks)
    require(not any(path.suffix.lower() in MEDIA_SUFFIXES for path in HERE.rglob("*") if path.is_file()),
            "no raw media in Git packet", checks)
    for path in HERE.glob("WUWA_IUNO_*.md"):
        body = path.read_text(encoding="utf-8")
        require(body.startswith("---\n") and "\nstatus: draft_noncurrent\n" in body,
                f"draft authority: {path.name}", checks)
        require("\ndo_not_use_as_current_authority: true\n" in body,
                f"noncurrent flag: {path.name}", checks)
        require(f"\nsource_commit: {COMMIT}\n" in body,
                f"source pin: {path.name}", checks)
    archive_profile = (HERE / "WUWA_IUNO_ARCHIVE_KEY_FATE_AND_FALLEN_VOICE_PROFILE.md"
                       ).read_text(encoding="utf-8")
    require("All **80** favor-word rows" in archive_profile and
            "49 combat/system rows" in archive_profile and
            "196 distinct" in archive_profile,
            "archive offset and combat/system scope documented", checks)
    model = json.loads((HERE / "WUWA_IUNO_CHARACTER_MODEL_PACKAGE.json").read_text(encoding="utf-8"))
    require(model["authority"] == "draft_noncurrent" and model["source_commit"] == COMMIT,
            "model authority and source pin", checks)
    rules = model["rules"]
    require(len(rules) == 24 and len({rule["id"] for rule in rules}) == 24,
            "24 distinct model rules", checks)
    require(all(set(rule["evidence_ids"]) <= evidence_ids for rule in rules),
            "all model evidence IDs resolve", checks)
    require(all(rule["probability"] is None for rule in rules),
            "no fabricated numerical probabilities", checks)
    probes = (HERE / "WUWA_IUNO_MODEL_FIDELITY_AND_STRESS_TEST_PRE_AV.md").read_text(encoding="utf-8")
    require(len(set(re.findall(r"\| (IUN-P\d{2}) \|", probes))) == 47,
            "47 non-blind probes", checks)
    require("## Ten interaction tests" in probes and
            "**An archived fall is not the end" in probes and all(
                f"R{number:02d}" in probes for number in range(1, 25)),
            "ten interaction tests and twenty-four-rule challenge map", checks)
    cases = json.loads((HERE / "AUDIO_MATCHED_SEMANTIC_CASES.json").read_text(encoding="utf-8"))
    require(cases["semantic_cases"] == 24 and len(cases["cases"]) == 24,
            "24 matched semantic cases", checks)
    crosswalk = (HERE / "WUWA_IUNO_AV_HUMAN_RETRIEVAL_CROSSWALK.md").read_text(encoding="utf-8")
    require(all(f"`{case['text_key']}`" in crosswalk for case in cases["cases"]),
            "all 24 exact sound cases occur in AV crosswalk", checks)
    require("remnant 350026" in crosswalk and "optional moonwatching" in crosswalk,
            "remnant and optional-route controls in AV crosswalk", checks)
    require("IUN-R08" in crosswalk and "IUN-R09" in crosswalk and
            "Main_Rinascita_2_12_21_11" in crosswalk,
            "late monitoring and anchoring controls in AV crosswalk", checks)
    require(all(f"IUN-R{number:02d}" in crosswalk for number in range(10, 13)) and
            "MAIN_RYAM_44_22" in crosswalk and
            "Main_Linaxita_2_9_320_16" in crosswalk,
            "arena, invocation and field controls in AV crosswalk", checks)
    require(all(f"IUN-R{number:02d}" in crosswalk for number in range(13, 16)) and
            "Main_Linaxita_2_10_27_12" in crosswalk and
            "Main_Linaxita_2_9_350_15" in crosswalk,
            "remnant memory and embodied crisis controls in AV crosswalk", checks)
    require(sum(len(case["renders"]) for case in cases["cases"]) == 96,
            "96 selected render variants", checks)
    require(all({render["language"] for render in case["renders"]} == LANGUAGES
                for case in cases["cases"]), "each case has four dubs", checks)
    selected_renders = [render for case in cases["cases"] for render in case["renders"]]
    require(sum(render["event_id"] is None and render["numeric_media_id"] is None
                for render in selected_renders) == 44,
            "44 selected renders preserve paired null event/media IDs", checks)
    require(all((render["event_id"] is None) == (render["numeric_media_id"] is None)
                for render in selected_renders), "selected event/media nulls remain paired", checks)
    require(all(len(render[name]) == 64 for case in cases["cases"] for render in case["renders"]
                for name in ("wem_sha256", "canonical_pcm_sha256", "flac_sha256")),
            "selected render hashes present", checks)
    result = {"packet": "Iuno", "scope": "IUNO_PINNED_3_6_0_TEXT_AUDIO_PRE_AV",
              "checks": checks, "source_crosscheck": "not_requested"}
    if source_root is not None:
        source = source_root / "ANALYSIS" / "Characters" / "Iuno"
        voice = source_root / "_voice_media" / "character" / "complete_voice_corpus" / "Iuno" / "v0_1"
        summary = source_root / "_research" / "character_packets" / "Iuno" / "audio_work" / "AUDIO_MEASUREMENT_SUMMARY.json"
        audit = json.loads((source / "COLLECTION_AUDIT.json").read_text(encoding="utf-8"))
        direct = audit["scopes"]["direct_character"]
        require(audit["valid"] and direct["voice_completeness_valid"],
                "selected collection audit valid", checks)
        require((audit["raw_flow_states"], audit["context_text_keys"],
                 audit["quest_references"], audit["distinct_quest_ids"]) ==
                (152, 2463, 46, 9), "contextual collection denominator", checks)
        require((direct["candidate_occurrences"], direct["accepted_occurrences"],
                 direct["source_voiced"], direct["source_unvoiced"]) ==
                (595, 585, 460, 125), "direct occurrence denominator", checks)
        require((direct["semantic_voice_lines"], direct["render_associations"],
                 direct["unique_flac_objects"]) ==
                (540, 2162, 2155), "voice line, association, object denominators", checks)
        decisions = jsonl(source / "occurrence_identity_crosswalk.jsonl")
        require(Counter(row["character_attribution"] for row in decisions) ==
                {"accepted_solo": 585, "rejected": 5, "unresolved": 5},
                "identity crosswalk counts", checks)
        placeholders = [row for row in decisions if row["character_attribution"] == "accepted_solo"
                        and 17908 <= row["flow_state_row_index"] <= 17911]
        require(len(placeholders) == 20 and all(not row["play_voice"]
                and row["state_key"].startswith("剧情_LIANBO_TEST_3.4") for row in placeholders),
                "20 accepted unvoiced test-state placeholders", checks)
        unvoiced_actions = {(7742, 1): 6, (9973, 2): 8,
                            (10491, 6): 17, (11529, 6): 22}
        require(all(
            len(rows := [row for row in decisions
                         if row["flow_state_row_index"] == state and
                         row["action_index"] == action]) == count and
            all(row["character_attribution"] == "accepted_solo" and
                row["play_voice"] is False for row in rows)
            for (state, action), count in unvoiced_actions.items()),
            "fear confession, late support and two optional outings are accepted but unvoiced", checks)
        late_voiced_decisions = [row for row in decisions
                                 if row["flow_state_row_index"] == 9975 and
                                 row["action_index"] == 5]
        require(len(late_voiced_decisions) == 8 and
                all(row["character_attribution"] == "accepted_solo" and
                    row["play_voice"] is True and
                    row["technical_speaker_id"] == 250024
                    for row in late_voiced_decisions),
                "eight later voiced Iuno occurrence candidates", checks)
        present_indices = {0, 2, 3, 5, 6, 20, 21, 22}
        quotation_indices = set(range(7, 18))
        reanchor_decisions = [row for row in decisions
                              if row["flow_state_row_index"] == 7764 and
                              row["action_index"] == 3 and
                              row["talk_index"] in present_indices | quotation_indices]
        require(len(reanchor_decisions) == 19 and
                all(row["character_attribution"] == "accepted_solo" and row["play_voice"] is True
                    and row["technical_speaker_id"] == (350026 if row["talk_index"] in present_indices else 178)
                    for row in reanchor_decisions),
                "present remnant and quoted earlier-self occurrences retain distinct technical IDs", checks)
        witnesses = {row["text_key"]: row["values"] for row in jsonl(source / "CONTEXT_TEXT_WITNESSES.jsonl")}
        require("如果还有下次" in witnesses["Main_Linaxita_2_10_63_51"]["zh-Hans"]["content"]
                and "原原本本全部告诉你" in witnesses["Main_Linaxita_2_10_63_52"]["zh-Hans"]["content"],
                "Rover's conditional full-account promise is in pinned Chinese witnesses", checks)
        require("もう一度初めから友達" in witnesses["Main_Linaxita_2_10_63_32"]["ja"]["content"]
                and "第三个人" in witnesses["Main_Linaxita_2_10_63_37"]["zh-Hans"]["content"],
                "fresh-friendship and third-party privacy witness boundaries", checks)
        raw_return = next(row for row in jsonl(source / "RAW_RELEVANT_FLOW_STATES.jsonl")
                          if row["source_locator"].endswith("#/7759"))
        return_params = json.loads(raw_return["raw"]["Actions"])[3]["Params"]
        return_items = return_params["TalkItems"]
        privacy_item = return_items[37]
        require(privacy_item["PlotLineKey"] == "Main_Linaxita_2_10_63_37"
                and [option["PlotLineKey"] for option in privacy_item["Options"]] == [
                    "Main_Linaxita_2_10_63_38", "Main_Linaxita_2_10_63_39",
                    "Main_Linaxita_2_10_63_40"]
                and [option["Actions"][0]["Params"]["TalkId"]
                     for option in privacy_item["Options"]] == [30, 32, 33],
                "return privacy choice has three distinct JumpTalk targets", checks)
        require(return_params["TalkSequence"][6:10] == [[29], [30, 31], [32], [33]],
                "privacy response sequences keep teasing, agreement and consideration separate", checks)
        require([(return_items[i]["Id"], return_items[i]["PlotLineKey"])
                 for i in (38, 39, 40, 41)] == [
                     (30, "Main_Linaxita_2_10_63_41"),
                     (31, "Main_Linaxita_2_10_63_42"),
                     (32, "Main_Linaxita_2_10_63_43"),
                     (33, "Main_Linaxita_2_10_63_44")],
                "three privacy response routes retain their exact Iuno line keys", checks)
        require(all(any(action["Name"] == "JumpTalk" and action["Params"]["TalkId"] == 34
                        for action in return_items[i].get("Actions", [])) for i in (39, 40, 41)),
                "alternative privacy routes rejoin at TalkId 34", checks)
        late_states = {int(row["source_locator"].rsplit("/", 1)[1]): row["raw"]
                       for row in jsonl(source / "RAW_RELEVANT_FLOW_STATES.jsonl")
                       if row["source_locator"].endswith(("#/9973", "#/9975"))}
        require(set(late_states) == {9973, 9975} and
                late_states[9973]["StateKey"] == "剧情_2_7_黎那汐塔主线_上半_2_25_1" and
                late_states[9975]["StateKey"] == "剧情_2_7_黎那汐塔主线_上半_2_27_1",
                "two later Chapter 2.7 state identities", checks)
        quest_refs = jsonl(source / "QUEST_CONTEXT_REFERENCES.jsonl")
        arena_hunt_states = {int(row["source_locator"].rsplit("/", 1)[1]): row["raw"]
                             for row in jsonl(source / "RAW_RELEVANT_FLOW_STATES.jsonl")
                             if row["source_locator"].endswith(("#/6989", "#/8378", "#/8381"))}
        require(set(arena_hunt_states) == {6989, 8378, 8381} and
                arena_hunt_states[6989]["StateKey"] == "剧情_2_4_七丘主线_上2_3_5" and
                arena_hunt_states[8378]["StateKey"] == "剧情_2_6_狄斯台地主线_上半_1_25_1" and
                arena_hunt_states[8381]["StateKey"] == "剧情_2_6_狄斯台地主线_上半_1_29_1",
                "arena and two hunt states retain separate exact identities", checks)
        expected_quest_nodes = ((6989, "125000126", "#/9725"),
                                (8378, "311000001", "#/11349"),
                                (8381, "311000001", "#/12928"))
        require(all(any(str(ref["quest_id"]) == quest_id and
                        ref["source_locator"].endswith(locator) and
                        any(link["state_key"] == arena_hunt_states[state]["StateKey"]
                            for link in ref["matching_references"])
                        for ref in quest_refs)
                    for state, quest_id, locator in expected_quest_nodes),
                "three exact quest-node joins without asserting runtime path", checks)
        court_params = json.loads(arena_hunt_states[6989]["Actions"])[4]["Params"]
        court = court_params["TalkItems"]
        court_iuno_indices = {14, 15, 16, 20, 28, 29, 30}
        require(len(court) == 31 and court_params["TalkSequence"] == [list(range(1, 32))] and
                {index for index, item in enumerate(court) if item.get("WhoId") == 250024} ==
                court_iuno_indices and
                [option["TidTalkOption"] for option in court[12]["Options"]] ==
                ["MAIN_RYAM_44_13", "MAIN_RYAM_44_14"] and
                all(court[index].get("PlayVoice") is True for index in court_iuno_indices),
                "court graph separates alternative Rover entrance, seven Iuno turns and shared continuation", checks)
        require(court[0]["WhoId"] == 250009 and court[6]["WhoId"] == 850351 and
                court[21]["WhoId"] == 250022 and court[26]["WhoId"] == 250022 and
                court[27]["WhoId"] == 850351 and
                [court[index]["TidTalk"] for index in (14, 15, 16, 20, 26, 27)] ==
                ["MAIN_RYAM_44_16", "MAIN_RYAM_44_17", "MAIN_RYAM_44_18",
                 "MAIN_RYAM_44_22", "MAIN_RYAM_44_28", "MAIN_RYAM_44_29"],
                "allegation, defense, Temple verdict, Ephor order and submission keep speakers", checks)
        invocation_params = json.loads(arena_hunt_states[8378]["Actions"])[3]["Params"]
        invocation = invocation_params["TalkItems"]
        field_params = json.loads(arena_hunt_states[8381]["Actions"])[3]["Params"]
        field = field_params["TalkItems"]
        field_iuno_indices = {1, 2, 3, 4, 5, 12, 13, 14}
        require(len(invocation) == 7 and
                invocation_params["TalkSequence"] == [list(range(1, 8))] and
                all(item.get("WhoId") == 250024 and item.get("PlayVoice") is True
                    for item in invocation) and
                [item["TidTalk"] for item in invocation] ==
                [f"Main_Linaxita_2_9_115_{number}" for number in range(1, 8)],
                "seven separate voiced Aquila/sight invocation turns", checks)
        require(len(field) == 15 and
                field_params["TalkSequence"] == [list(range(1, 16))] and
                {index for index, item in enumerate(field) if item.get("WhoId") == 250024} ==
                field_iuno_indices and field[0]["Options"][0]["TidTalkOption"] ==
                "Main_Linaxita_2_9_320_2" and
                all(field[index].get("PlayVoice") is True for index in field_iuno_indices) and
                all(field[index]["WhoId"] == 250022 for index in range(6, 11)) and
                field[11]["WhoId"] == 1580,
                "field description, Augusta/Avidius exchange and rest invitation retain speakers", checks)
        require("有罪，这就是圣殿的判断" in
                witnesses["MAIN_RYAM_44_22"]["zh-Hans"]["content"] and
                "离开七丘" in witnesses["MAIN_RYAM_44_28"]["zh-Hans"]["content"] and
                "get eyes on this beast" in witnesses["Main_Linaxita_2_9_115_5"]["en"]["content"] and
                "阿奎拉，拜托你了" in witnesses["Main_Linaxita_2_9_115_5"]["zh-Hans"]["content"] and
                "결과를 예측할 수 없는" in
                witnesses["Main_Linaxita_2_9_320_7"]["ko"]["content"] and
                "between Augusta and Avidius" in
                witnesses["Main_Linaxita_2_9_320_16"]["en"]["content"] and
                "奥古斯塔和角斗士" in
                witnesses["Main_Linaxita_2_9_320_16"]["zh-Hans"]["content"],
                "Temple/Ephor distinction and hunt localization forks", checks)
        require("这些景象" in witnesses["MAIN_RYAM_44_23"]["zh-Hans"]["content"] and
                "映像" in witnesses["MAIN_RYAM_44_23"]["ja"]["content"] and
                "weight of your actions" in
                witnesses["MAIN_RYAM_44_23"]["en"]["content"] and
                "Julia Silva" in witnesses["MAIN_RYAM_44_23"]["en"]["content"] and
                "离开七丘" in witnesses["MAIN_RYAM_44_28"]["zh-Hans"]["content"],
                "uninspected image references and Augusta's Julia-directed order remain distinct", checks)
        memory_crisis_states = {int(row["source_locator"].rsplit("/", 1)[1]): row["raw"]
                                for row in jsonl(source / "RAW_RELEVANT_FLOW_STATES.jsonl")
                                if row["source_locator"].endswith(
                                    ("#/7761", "#/7805", "#/10906"))}
        require(set(memory_crisis_states) == {7761, 7805, 10906} and
                memory_crisis_states[7761]["StateKey"] ==
                "剧情_2_6_狄斯台地主线_下半_混沌之间_1_11" and
                memory_crisis_states[7805]["StateKey"] ==
                "剧情_2_6_狄斯台地主线_下半_混沌之间_3_1" and
                memory_crisis_states[10906]["StateKey"] ==
                "剧情_2_6_狄斯台地主线_上半_1_85_2",
                "mother-image, familiar-site and earlier crisis remain distinct states", checks)
        require(all(any(str(ref["quest_id"]) == "886000001" and
                        ref["source_locator"].endswith("plothandbookconfig.json#/55") and
                        any(link["state_key"] == memory_crisis_states[state]["StateKey"]
                            for link in ref["matching_references"])
                        for ref in quest_refs) for state in (7761, 7805)) and
                any(str(ref["quest_id"]) == "311000001" and
                    ref["source_locator"].endswith("questnodedata.json#/14490") and
                    any(link["state_key"] == memory_crisis_states[10906]["StateKey"]
                        for link in ref["matching_references"])
                    for ref in quest_refs),
                "memory states and crisis have source-class-specific exact quest joins", checks)
        mother_params = json.loads(memory_crisis_states[7761]["Actions"])[5]["Params"]
        mother = mother_params["TalkItems"]
        familiar_params = json.loads(memory_crisis_states[7805]["Actions"])[5]["Params"]
        familiar = familiar_params["TalkItems"]
        crisis_params = json.loads(memory_crisis_states[10906]["Actions"])[3]["Params"]
        crisis = crisis_params["TalkItems"]
        require(len(mother) == 10 and mother_params.get("TalkSequence") is None and
                [item.get("WhoId") for item in mother] ==
                [350028] * 2 + [350029] * 4 + [350026] * 4 and
                [mother[index]["TidTalk"] for index in range(6, 10)] ==
                ["Main_Linaxita_2_10_27_11", "Main_Linaxita_2_10_27_12",
                 "Main_Linaxita_2_10_27_10", "Main_Linaxita_2_10_27_13"],
                "mother-image speakers and four questioning remnant turns stay separate", checks)
        require(len(familiar) == 5 and familiar_params.get("TalkSequence") is None and
                all(item.get("WhoId") == 350026 and item.get("PlayVoice") is True
                    for item in familiar) and
                [item["TidTalk"] for item in familiar] ==
                [f"Main_Linaxita_2_10_39_{suffix}" for suffix in (1, 3, 4, 5, 6)],
                "five partial-familiarity remnant turns retain source order", checks)
        require(len(crisis) == 19 and
                crisis_params["TalkSequence"] == [list(range(1, 20))] and
                [item.get("WhoId") for item in crisis[5:11]] == [350005] * 6 and
                [item.get("WhoId") for item in crisis[11:15]] == [250024] * 4 and
                [item.get("WhoId") for item in crisis[15:19]] == [250022] * 4 and
                [crisis[index]["TidTalk"] for index in range(11, 15)] ==
                [f"Main_Linaxita_2_9_350_{suffix}" for suffix in range(13, 17)],
                "hostile voice, four Iuno questions and Augusta's answer retain speakers", checks)
        require("想象" in witnesses["Main_Linaxita_2_10_27_12"]["zh-Hans"]["content"] and
                "本物の彼女じゃない" in
                witnesses["Main_Linaxita_2_10_27_13"]["ja"]["content"] and
                "我不知道" in witnesses["Main_Linaxita_2_10_39_3"]["zh-Hans"]["content"] and
                "如果" in witnesses["Main_Linaxita_2_9_350_15"]["zh-Hans"]["content"] and
                "咳咳" in witnesses["Main_Linaxita_2_9_350_14"]["zh-Hans"]["content"] and
                "ゲホ" in witnesses["Main_Linaxita_2_9_350_14"]["ja"]["content"] and
                "콜록" in witnesses["Main_Linaxita_2_9_350_14"]["ko"]["content"] and
                "cough" not in witnesses["Main_Linaxita_2_9_350_14"]["en"]["content"].lower() and
                "临时营地" in witnesses["Main_Linaxita_2_9_350_19"]["zh-Hans"]["content"],
                "imagined image, incomplete memory, conditional fate and cough localization witnesses", checks)
        late_quest_key = late_states[9975]["StateKey"]
        require(any(str(row["quest_id"]) == "158800019" and
                    row["source_locator"].endswith("plothandbookconfig.json#/57") and
                    any(ref["state_key"] == late_quest_key
                        for ref in row["matching_references"])
                    for row in quest_refs) and
                not any(ref["state_key"] == late_states[9973]["StateKey"]
                        for row in quest_refs for ref in row["matching_references"]),
                "only voiced later state has retained exact quest join via PlotHandBook", checks)
        monitoring = json.loads(late_states[9973]["Actions"])[2]["Params"]["TalkItems"]
        anchoring = json.loads(late_states[9975]["Actions"])[5]["Params"]["TalkItems"]
        require(len(monitoring) == 8 and
                all(item["WhoId"] == 250024 and "PlayVoice" not in item
                    for item in monitoring) and
                [option["Actions"][0]["Params"]["TalkId"]
                 for option in monitoring[0]["Options"]] == [2, 3] and
                [monitoring[index]["Actions"][0]["Params"]["TalkId"]
                 for index in (1, 4)] == [6, 6],
                "unvoiced monitoring fork rejoins before gift and group reassurance", checks)
        require(len(anchoring) == 14 and
                all(anchoring[index]["WhoId"] == 250024 and
                    anchoring[index].get("PlayVoice") is True
                    for index in range(1, 9)) and
                anchoring[0]["WhoId"] == anchoring[11]["WhoId"] == 250022 and
                anchoring[10]["WhoId"] == 1316 and
                [option["Actions"][0]["Params"]["TalkId"]
                 for option in anchoring[5]["Options"]] == [7, 8] and
                [anchoring[index]["Actions"][0]["Params"]["TalkId"]
                 for index in (6, 7)] == [9, 9],
                "voiced Iuno branch replies remain separate from Augusta and Abby turns", checks)
        require("信标被毁" in witnesses["Main_Rinascita_2_12_209_5"]["zh-Hans"]["content"] and
                "riddled with noise" in witnesses["Main_Rinascita_2_12_209_5"]["en"]["content"] and
                "更加敏感" in witnesses["Main_Rinascita_2_12_209_7"]["zh-Hans"]["content"] and
                "than any device" in witnesses["Main_Rinascita_2_12_209_7"]["en"]["content"] and
                "他の人より" in witnesses["Main_Rinascita_2_12_209_7"]["ja"]["content"] and
                "还有我们" in witnesses["Main_Rinascita_2_12_209_10"]["zh-Hans"]["content"],
                "damaged-data, localized attunement and collective-help witnesses", checks)
        require("如果这里面" in witnesses["Main_Rinascita_2_12_21_4"]["zh-Hans"]["content"] and
                "If Leviathan" in witnesses["Main_Rinascita_2_12_21_4"]["en"]["content"] and
                "锚定" in witnesses["Main_Rinascita_2_12_21_10"]["zh-Hans"]["content"] and
                "연결" in witnesses["Main_Rinascita_2_12_21_10"]["ko"]["content"] and
                "经历、感受、理解" in
                witnesses["Main_Rinascita_2_12_21_11"]["zh-Hans"]["content"],
                "conditional analogy, anchor/connection and experiential-trace witnesses", checks)
        raw_reanchor = next(row for row in jsonl(source / "RAW_RELEVANT_FLOW_STATES.jsonl")
                            if row["source_locator"].endswith("#/7764"))
        reanchor_items = json.loads(raw_reanchor["raw"]["Actions"])[3]["Params"]["TalkItems"]
        require({i for i, row in enumerate(reanchor_items) if row["WhoId"] == 350026} ==
                present_indices and
                {i for i, row in enumerate(reanchor_items) if row["WhoId"] == 178} ==
                quotation_indices,
                "raw Chaos scene separates present remnant from remembered quotations", checks)
        require(all(witnesses[row["text_key"]]["zh-Hans"]["content"] == "说点什么吧"
                    and all(witnesses[row["text_key"]][lang]["status"] == "empty"
                            for lang in ("en", "ja", "ko")) for row in placeholders),
                "test rows contain only generic Chinese and empty other witnesses", checks)
        messages = jsonl(source / "WAVESLINE_MESSAGES.jsonl")
        require(len(messages) == 3 and all(row["content_extraction_status"] == "metadata_only_scope"
                                            for row in messages),
                "three WavesLine shells have no extracted content", checks)
        package = json.loads((source / "character_source_package.json").read_text(encoding="utf-8"))
        memory_request = next(row for row in package["favor_words"]
                              if row["content"]["text_key"] == "FavorWord_141004_Content")
        require(memory_request["id"] == 141005 and
                memory_request["source_locator"].endswith("favorword.json#/2543") and
                memory_request["voice_asset"].endswith(
                    "play_favor_word_younuo_sys_toplayer04.play_favor_word_younuo_sys_toplayer04"),
                "memory-request archive row, locator and explicit event path", checks)
        memory_values = memory_request["content"]["values"]
        require(all(memory_values[lang]["status"] == "resolved"
                    for lang in ("zh-Hans", "en", "ja", "ko")) and
                "记得的人比忘记的人更痛苦" in memory_values["zh-Hans"]["content"] and
                "You'd be the exception" in memory_values["en"]["content"] and
                "あなたにだけは私の存在を……私の全てを覚えていてほしい" in
                    memory_values["ja"]["content"] and
                "네가 내 마음을 잊지 않을 거라는 희망" in memory_values["ko"]["content"],
                "four localized memory-request witnesses and material translation contrast", checks)
        ascension_keys = {f"FavorWord_1410{suffix}_Content" for suffix in range(27, 32)}
        ascension = {row["content"]["text_key"]: row for row in package["favor_words"]
                     if row["content"]["text_key"] in ascension_keys}
        require(set(ascension) == ascension_keys, "five exact ascension content keys", checks)
        for offset, suffix in enumerate(range(27, 32)):
            key = f"FavorWord_1410{suffix}_Content"
            row = ascension[key]
            require(row["id"] == 141000 + suffix + 1 and
                    row["source_locator"].endswith(f"favorword.json#/{2566 + offset}") and
                    row["title"]["values"]["en"]["content"] ==
                    f"Ascension: {'I' * (offset + 1) if offset < 3 else ('IV' if offset == 3 else 'V')}",
                    f"archive row/key/locator/title offset: {key}", checks)
            require(all(row["content"]["values"][lang]["status"] == "resolved"
                        for lang in ("zh-Hans", "en", "ja", "ko")),
                    f"four resolved ascension witnesses: {key}", checks)
        first = ascension["FavorWord_141027_Content"]["content"]["values"]
        require("锚定" in first["zh-Hans"]["content"] and
                "anchor job" in first["en"]["content"] and
                "アンカー" in first["ja"]["content"],
                "ascension-I anchoring language", checks)
        warning = ascension["FavorWord_141029_Content"]["content"]["values"]
        require("一起坠入" in warning["zh-Hans"]["content"] and
                "we might" in warning["en"]["content"] and
                "一緒に" in warning["ja"]["content"],
                "ascension-III shared possible risk", checks)
        desire = ascension["FavorWord_141030_Content"]["content"]["values"]
        require("喜欢的" in desire["zh-Hans"]["content"] and
                "anything else I want" in desire["en"]["content"] and
                "手を離さない" in desire["ja"]["content"] and
                "가만두지" in desire["ko"]["content"],
                "ascension-IV desire and language-sensitive pursuit", checks)
        seeing = ascension["FavorWord_141031_Content"]["content"]["values"]
        require("我看见" in seeing["zh-Hans"]["content"] and
                "I see" in seeing["en"]["content"] and
                "見た" in seeing["ja"]["content"] and
                "봤어" in seeing["ko"]["content"],
                "ascension-V seeing aspect contrast", checks)
        require("窥视命运的能力" in witnesses["Main_Linaxita_2_9_360_27"]["zh-Hans"]["content"],
                "live-story fate-peering trade counterweight", checks)
        line_rows = jsonl(voice / "COMPLETE_VOICE_LINE_ANALYSIS.jsonl")
        require(len(line_rows) == 540, "540 selected semantic voice rows", checks)
        line_by_locator = {row["source_locator"]: row for row in line_rows}
        arena_hunt_groups = ((6989, 4, court, sorted(court_iuno_indices)),
                             (8378, 3, invocation, list(range(7))),
                             (8381, 3, field, sorted(field_iuno_indices)))
        arena_hunt_voice: list[dict] = []
        for state, action, items, indices in arena_hunt_groups:
            for index in indices:
                locator = (f"wuwa://{COMMIT}/BinData/flowState/flowstate.json#/"
                           f"{state}/Actions!/{action}/Params/TalkItems/{index}")
                row = line_by_locator[locator]
                arena_hunt_voice.append(row)
                require(row["text_key"] == items[index]["TidTalk"] and
                        row["technical_speaker_id"] == 250024 and
                        row["record_class"] == "story_dialogue" and
                        row["voice_reconciliation_status"] == "resolved_media" and
                        {render["voice_language"] for render in row["renders"]} == LANGUAGES and
                        all(row["text_witnesses"][lang]["status"] == "resolved"
                            for lang in LANGUAGES),
                        f"arena/hunt source, speaker, key and four text witnesses: {state}/{action}/{index}",
                        checks)
        arena_hunt_renders = [render for row in arena_hunt_voice for render in row["renders"]]
        require(len(arena_hunt_voice) == 22 and len(arena_hunt_renders) == 88 and
                len({render["canonical_pcm_sha256"] for render in arena_hunt_renders}) == 88,
                "22 arena/hunt Iuno semantic lines and 88 distinct PCM renders", checks)
        require(all(render["materialization_status"] == "flac_roundtrip_pcm_identical" and
                    render.get("event_id") is None and
                    render.get("numeric_media_id") is None and
                    render["source_wem_exists"] and
                    render["source_wem_sha256_verified"] and
                    (source_root / render["flac_relative_path"]).is_file()
                    for render in arena_hunt_renders),
                "arena/hunt renders are present, PCM-valid and retain paired-null event/media IDs", checks)
        memory_crisis_groups = ((7761, 5, mother, range(6, 10), 350026),
                                (7805, 5, familiar, range(5), 350026),
                                (10906, 3, crisis, range(11, 15), 250024))
        memory_crisis_voice: list[dict] = []
        for state, action, items, indices, speaker in memory_crisis_groups:
            for index in indices:
                locator = (f"wuwa://{COMMIT}/BinData/flowState/flowstate.json#/"
                           f"{state}/Actions!/{action}/Params/TalkItems/{index}")
                row = line_by_locator[locator]
                memory_crisis_voice.append(row)
                require(row["text_key"] == items[index]["TidTalk"] and
                        row["technical_speaker_id"] == speaker and
                        row["record_class"] == "story_dialogue" and
                        row["voice_reconciliation_status"] == "resolved_media" and
                        {render["voice_language"] for render in row["renders"]} == LANGUAGES and
                        all(row["text_witnesses"][lang]["status"] == "resolved"
                            for lang in LANGUAGES),
                        f"remnant/crisis source, speaker, key and witnesses: {state}/{action}/{index}",
                        checks)
        memory_crisis_renders = [render for row in memory_crisis_voice
                                 for render in row["renders"]]
        require(len(memory_crisis_voice) == 13 and len(memory_crisis_renders) == 52 and
                len({render["canonical_pcm_sha256"] for render in memory_crisis_renders}) == 52,
                "13 remnant/crisis Iuno semantic lines and 52 distinct PCM renders", checks)
        require(all(render["materialization_status"] == "flac_roundtrip_pcm_identical" and
                    render.get("event_id") is None and
                    render.get("numeric_media_id") is None and
                    render["source_wem_exists"] and
                    render["source_wem_sha256_verified"] and
                    (source_root / render["flac_relative_path"]).is_file()
                    for render in memory_crisis_renders),
                "remnant/crisis renders are present, PCM-valid and retain paired-null event/media IDs", checks)
        late_voice = [line_by_locator[
            f"wuwa://{COMMIT}/BinData/flowState/flowstate.json#/9975/Actions!/5/Params/TalkItems/{index}"]
            for index in range(1, 9)]
        require(all(row["text_key"] == anchoring[index]["TidTalk"] and
                    {render["voice_language"] for render in row["renders"]} == LANGUAGES and
                    all(render["materialization_status"] == "flac_roundtrip_pcm_identical" and
                        render.get("event_id") is None and
                        render.get("numeric_media_id") is None and
                        render["source_wem_exists"] and
                        render["source_wem_sha256_verified"] and
                        (source_root / render["flac_relative_path"]).is_file()
                        for render in row["renders"])
                    for index, row in enumerate(late_voice, 1)),
                "eight later Iuno turns have thirty-two valid four-dub renders without explicit event/media IDs", checks)
        late_renders = [render for row in late_voice for render in row["renders"]]
        require(len(late_renders) == 32 and
                len({render["canonical_pcm_sha256"] for render in late_renders}) == 32 and
                not any("#/9973/Actions!/2/Params/TalkItems/" in row["source_locator"]
                        for row in line_rows),
                "thirty-two distinct late PCM objects and no borrowed unvoiced monitoring row", checks)
        late_nominations = ((1, "21_2"), (3, "21_4"), (4, "21_5"),
                            (6, "21_9"), (7, "21_10"), (8, "21_11"))
        require(all(anchoring[index]["TidTalk"] ==
                    f"Main_Rinascita_2_12_{suffix}" and
                    f"Main_Rinascita_2_12_{suffix}" in crosswalk and
                    len(late_voice[index - 1]["renders"]) == 4
                    for index, suffix in late_nominations),
                "six exact late briefing keys nominate twenty-four render associations", checks)
        archive = sorted(package["favor_words"], key=lambda row: row["id"])
        archive_by_locator = {row["source_locator"]: row for row in line_rows
                              if "/BinData/favor/favorword.json#/" in row["source_locator"]}
        require(len(archive) == 80 and len(archive_by_locator) == 80,
                "80 source and semantic archive rows", checks)
        trigger_renders: list[dict] = []
        trigger_events: set[int] = set()
        for offset, raw in enumerate(archive):
            raw_id = 141002 + offset
            text_key = f"FavorWord_{141001 + offset}_Content"
            source_index = 2540 + offset
            locator = raw["source_locator"]
            require(raw["id"] == raw_id and raw["content"]["text_key"] == text_key and
                    locator.endswith(f"/favorword.json#/{source_index}") and
                    locator in archive_by_locator,
                    f"archive raw/Content/exact-locator identity: {raw_id}", checks)
            semantic = archive_by_locator[locator]
            require(semantic["text_key"] == text_key and
                    semantic["technical_render_coverage_status"] == "complete" and
                    len(semantic["renders"]) == 4 and
                    {render["voice_language"] for render in semantic["renders"]} == LANGUAGES,
                    f"archive semantic and four-dub join: {raw_id}", checks)
            require(all(semantic["text_witnesses"][voice_lang]["content"] ==
                        raw["content"]["values"][text_lang]["content"]
                        for voice_lang, text_lang in
                        (("zh", "zh-Hans"), ("en", "en"), ("ja", "ja"), ("ko", "ko"))),
                    f"archive four-text witness join: {raw_id}", checks)
            require(all(render["event_path"] == raw["voice_asset"] and
                        isinstance(render["event_id"], int) and
                        isinstance(render["bank_id"], int) and
                        isinstance(render["numeric_media_id"], int) and
                        render["source_wem_exists"] and
                        render["source_wem_sha256_verified"] and
                        render["materialization_status"] == "flac_roundtrip_pcm_identical" and
                        render["canonical_pcm_sha256"] ==
                        render["expected_canonical_pcm_sha256"]
                        for render in semantic["renders"]),
                    f"archive event/media/WEM/PCM join: {raw_id}", checks)
            if raw_id >= 141033:
                trigger_renders.extend(semantic["renders"])
                trigger_events.update(render["event_id"] for render in semantic["renders"])
        require(len(trigger_renders) == 196 and len(trigger_events) == 49 and
                len({render["canonical_pcm_sha256"] for render in trigger_renders}) == 196,
                "49 combat/system events and 196 distinct PCM objects", checks)
        by_key = {row["content"]["text_key"]: row for row in archive}
        fate = by_key["FavorWord_141049_Content"]
        fallen = by_key["FavorWord_141069_Content"]
        require(fate["id"] == 141050 and fate["title"]["values"]["en"]["content"] ==
                "Resonance Skill: XII" and
                by_key["FavorWord_141050_Content"]["title"]["values"]["en"]["content"] ==
                "Resonance Liberation: I" and
                "命运" in fate["content"]["values"]["zh-Hans"]["content"] and
                "Fate... revealed" in fate["content"]["values"]["en"]["content"],
                "Skill XII existing-neighbor-key and fate wording contrast", checks)
        require(fallen["id"] == 141070 and
                fallen["title"]["values"]["en"]["content"] == "Fallen: II" and
                "已存在过" in fallen["content"]["values"]["zh-Hans"]["content"] and
                "left my mark" in fallen["content"]["values"]["en"]["content"] and
                "存在している" in fallen["content"]["values"]["ja"]["content"] and
                "존재했었어" in fallen["content"]["values"]["ko"]["content"],
                "Fallen II four-witness existence/mark and trigger distinction", checks)
        require(all(str(event_id) in crosswalk for event_id in
                    (3771678227, 1424501745, 517603479, 2751270229, 359709123)),
                "five exact combat/world event-ID retrieval nominations", checks)
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
        memory_case = next(case for case in cases["cases"]
                           if case["text_key"] == "FavorWord_141004_Content")
        require(memory_case["source_locator"] == memory_request["source_locator"] and
                {render["language"]: render["qc_flags"] for render in memory_case["renders"]} == {
                    "en": [],
                    "ja": ["long_object_check_subtitle_extent"],
                    "ko": ["long_object_check_subtitle_extent"],
                    "zh": ["long_object_check_subtitle_extent"],
                } and
                all(render["event_id"] == 2473040026 and
                    render["numeric_media_id"] is not None for render in memory_case["renders"]),
                "four mapped memory-request renders preserve explicit IDs and three QC flags", checks)
        for key in sorted(ascension_keys):
            case = next(case for case in cases["cases"] if case["text_key"] == key)
            require(case["source_locator"] == ascension[key]["source_locator"] and
                    len(case["renders"]) == 4 and
                    all(render["event_id"] is not None and render["numeric_media_id"] is not None
                        and not render["qc_flags"] for render in case["renders"]),
                    f"exact archive locator and four clean explicit-ID renders: {key}", checks)
        audio = json.loads(summary.read_text(encoding="utf-8"))
        require((audio["manifest_objects"], audio["measured_objects"],
                 audio["repeated_pcm_manifest_rows"]) == (2155, 2155, 3),
                "full local audio measurement counts", checks)
        require(not audio["failed_objects"], "no local audio measurement failures", checks)
        cohort_path = source_root / "_research" / "character_packets" / "Iuno" / \
            "audio_work" / "IUNO_SOURCE_COHORT_AUDIT.json"
        cohort_bytes = cohort_path.read_bytes()
        cohorts = json.loads(cohort_bytes)
        expected_cohorts = {
            ("fate_trade", ("8386/4",), 42, 168),
            ("joint_plan", ("8408/3",), 32, 128),
            ("farewell", ("7741/5",), 13, 52),
            ("chaos_fragment", ("7747/5",), 8, 32),
            ("reanchor_present", ("7764/3@0+2-3+5-6+20-22",), 8, 32),
            ("remembered_self_quotes", ("7764/3@7-17",), 11, 44),
            ("return_disclosure", ("7759/3",), 35, 140),
            ("later_evacuation", ("8878/7",), 21, 84),
        }
        require(hashlib.sha256(cohort_bytes).hexdigest() ==
                "e43b288b47de62e88d2f3e8854dd5e3e47e5b893792a12f11ef828455a0e3514" and
                cohorts["source_commit"] == COMMIT and
                cohorts["line_analysis_sha256"] == audio["line_analysis_sha256"],
                "source-cohort report hash and line-generation pin", checks)
        require({(row["name"], tuple(row["source_actions"]), row["semantic_lines"],
                  row["render_associations"]) for row in cohorts["cohorts"]} == expected_cohorts,
                "eight source-defined cohorts and exact TalkItem selection denominators", checks)
        members = [member for cohort in cohorts["cohorts"] for member in cohort["members"]]
        require(len(members) == 680 and
                len({member["semantic_voice_occurrence_id"] for member in members}) == 170 and
                len({member["canonical_pcm_sha256"] for member in members}) == 680 and
                sum(stat["pitch_qualified_objects"] for cohort in cohorts["cohorts"]
                    for stat in cohort["language_statistics"].values()) == 663 and
                all(stat["measured_objects"] == stat["integrity_pass_objects"] ==
                    stat["channel_counts"].get("1", 0)
                    for cohort in cohorts["cohorts"]
                    for stat in cohort["language_statistics"].values()) and
                cohorts["human_perceptual_review_performed"] is False,
                "680 distinct integrity-valid mono renders with no claimed listening", checks)
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
