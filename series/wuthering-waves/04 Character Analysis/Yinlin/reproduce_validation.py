#!/usr/bin/env python3
"""Validate Yinlin's draft packet and optional private evidence joins.

Checks source identity/structure/retrieval, not literary truth or listening.
Read-only unless --write-report is specified. No media or raw text is copied.
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
COHORT_SHA256 = "b1dd590084042d3e29036067ca60f12bf6bcc6ad0eb626cdbd84aea5525743d1"
COHORT_SPECS = {
    "puppet_explanation": ("997/7", 15, 60),
    "private_case_exposition": ("1004/6@0-21", 22, 88),
    "rover_risk_and_offer": ("1004/6@22-34+42-43", 15, 60),
    "yuanyuan_care_under_cover": ("1004/6@36+38+40-41", 4, 16),
    "postfight_social_approach": ("1006/7@0-9", 10, 40),
    "tracking_admission": ("1006/7@10-15", 6, 24),
    "posttracker_tactics": ("1006/7@16-23", 8, 32),
    "guardian_reveal_under_cover": ("349/5", 21, 84),
    "hostage_performance": ("350/4", 5, 20),
    "living_people_objection": ("673/3", 6, 24),
    "vocation_without_file": ("1092/1", 11, 44),
    "postcase_account": ("353/6@0-13", 14, 56),
    "grief_and_complicity": ("353/6@14-28", 15, 64),
    "future_and_tentative_trust": ("353/6@29-37", 9, 36),
    "party_as_self": ("15092/6@1-3+5-7", 6, 24),
    "renewed_covert_duty": ("15092/6@10-18+20-24", 14, 56),
}


def jsonl(path: Path) -> list[dict]:
    with path.open(encoding="utf-8") as handle:
        return [json.loads(line) for line in handle if line.strip()]


def require(condition: bool, message: str, checks: list[str]) -> None:
    if not condition:
        raise AssertionError(message)
    checks.append(message)


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def selected_by_source_action(source_locator: str, selector: str) -> bool:
    match = re.search(r"#/(\d+)/Actions!/(\d+)/Params/TalkItems/(\d+)$", source_locator)
    if not match:
        return False
    action_part, _, talk_part = selector.partition("@")
    row, action = (int(part) for part in action_part.split("/"))
    if (int(match[1]), int(match[2])) != (row, action):
        return False
    if not talk_part:
        return True
    talk_index = int(match[3])
    for interval in talk_part.split("+"):
        bounds = interval.split("-")
        low, high = int(bounds[0]), int(bounds[-1])
        if low <= talk_index <= high:
            return True
    return False


def source_render_tuple(semantic_id: str, locator: str, text_key: str, render: dict) -> tuple:
    return (
        semantic_id, locator, text_key, render["voice_language"],
        render["render_analysis_id"], render["canonical_pcm_sha256"], render["flac_sha256"],
    )


def audit_render_tuple(member: dict) -> tuple:
    return (
        member["semantic_voice_occurrence_id"], member["source_locator"], member["text_key"],
        member["voice_language"], member["render_analysis_id"],
        member["canonical_pcm_sha256"], member["flac_sha256"],
    )


def validate(source_root: Path | None) -> dict:
    checks: list[str] = []
    matrix = (HERE / "WUWA_YINLIN_EVIDENCE_AND_FALSIFICATION_MATRIX.md").read_text(encoding="utf-8")
    evidence_ids = set(re.findall(r"\| (YIN-E\d{2}) \|", matrix))
    claim_ids = set(re.findall(r"\| (YIN-C\d{2}) —", matrix))
    require(evidence_ids == {f"YIN-E{i:02d}" for i in range(1, 43)},
            "42 contiguous evidence bundles", checks)
    require(claim_ids == {f"YIN-C{i:02d}" for i in range(1, 41)},
            "40 contiguous material claims", checks)
    require(
        not any(path.suffix.lower() in MEDIA_SUFFIXES for path in HERE.rglob("*") if path.is_file()),
        "no media in Git packet",
        checks,
    )
    for path in HERE.glob("WUWA_YINLIN_*.md"):
        body = path.read_text(encoding="utf-8")
        require(body.startswith("---\n") and "\nstatus: draft_noncurrent\n" in body, f"draft authority: {path.name}", checks)
        require("\ndo_not_use_as_current_authority: true\n" in body, f"not-current flag: {path.name}", checks)
    model = json.loads((HERE / "WUWA_YINLIN_CHARACTER_MODEL_PACKAGE.json").read_text(encoding="utf-8"))
    require(model["authority"] == "draft_noncurrent" and model["source_commit"] == COMMIT, "model authority/source pin", checks)
    rules = model["rules"]
    require(len(rules) == 21 and len({rule["id"] for rule in rules}) == 21, "21 distinct model rules", checks)
    require(all(set(rule["evidence_ids"]) <= evidence_ids for rule in rules), "all model rule evidence IDs resolve", checks)
    require(all(rule["probability"] is None for rule in rules), "no fabricated numeric behavioral probabilities", checks)
    probes = (HERE / "WUWA_YINLIN_MODEL_FIDELITY_AND_STRESS_TEST_PRE_AV.md").read_text(encoding="utf-8")
    require(set(re.findall(r"\| (YIN-P\d{2}) \|", probes)) ==
            {f"YIN-P{i:02d}" for i in range(1, 42)},
            "41 contiguous non-blind probes", checks)
    cases = json.loads((HERE / "AUDIO_MATCHED_SEMANTIC_CASES.json").read_text(encoding="utf-8"))
    require(cases["semantic_cases"] == 15 and len(cases["cases"]) == 15, "15 matched semantic cases", checks)
    crosswalk = (HERE / "WUWA_YINLIN_AV_HUMAN_RETRIEVAL_CROSSWALK.md").read_text(encoding="utf-8")
    require(all(f"`{case['text_key']}`" in crosswalk for case in cases["cases"]),
            "all 15 exact sound cases occur in AV crosswalk", checks)
    require(all(f"**YIN-S{number:02d} —" in crosswalk for number in range(1, 16)),
            "15 sound cases have individual retrieval capsules", checks)
    require(set(re.findall(r"\| (YIN-R\d{2}) \|", crosswalk)) == {f"YIN-R{number:02d}" for number in range(1, 13)},
            "twelve runtime/audience/variant retrieval controls", checks)
    require("tracker" in crosswalk and "source-unvoiced" in crosswalk and "restoration" in crosswalk,
            "consent, festival, and later-file controls in AV crosswalk", checks)
    require(sum(len(case["renders"]) for case in cases["cases"]) == 60, "60 selected render records", checks)
    require(all({r["language"] for r in case["renders"]} == LANGUAGES for case in cases["cases"]), "every case spans four languages", checks)
    require(
        all(len(r["wem_sha256"]) == 64 and len(r["canonical_pcm_sha256"]) == 64 and len(r["flac_sha256"]) == 64 for case in cases["cases"] for r in case["renders"]),
        "selected render hashes present",
        checks,
    )
    require(sum(r["event_id"] is None and r["numeric_media_id"] is None for case in cases["cases"] for r in case["renders"]) == 32,
            "32 of 60 selected renders retain paired null event/media IDs", checks)
    ascension_keys = {"FavorWord_130222_Content", "FavorWord_130224_Content", "FavorWord_130253_Content"}
    ascension_cases = {case["text_key"]: case for case in cases["cases"] if case["text_key"] in ascension_keys}
    require(set(ascension_cases) == ascension_keys, "resilience, shared-purpose, and direct-feeling cases selected", checks)
    require(all(r["event_id"] is not None and r["numeric_media_id"] is not None
                for case in ascension_cases.values() for r in case["renders"]),
            "new ascension render event/media IDs explicit", checks)
    result = {"packet": "Yinlin", "scope": "YINLIN_PINNED_3_6_0_TEXT_AUDIO_PRE_AV", "checks": checks, "source_crosscheck": "not_requested"}
    if source_root is not None:
        source = source_root / "ANALYSIS" / "Characters" / "Yinlin"
        voice = source_root / "_voice_media" / "character" / "complete_voice_corpus" / "Yinlin" / "v0_1"
        measurement = source_root / "_research" / "character_packets" / "Yinlin" / "audio_work" / "AUDIO_MEASUREMENT_SUMMARY.json"
        quest_tree = json.loads((source_root / "_sources" / "Arikatsu_WutheringWaves_Data" /
                                 "BinData" / "QuestTree" / "questtreenode.json").read_text(encoding="utf-8"))
        quest_node = next(node for node in quest_tree if node["Id"] == 120030)
        require(quest_node["QuestArray"] == [114000018] and
                quest_node["Summary"] == "QuestTree_Summary_120030",
                "Yinlin quest-node to retrospective synopsis link", checks)
        synopsis = next(row for row in jsonl(source / "source_mentions.jsonl")
                        if row["text_key"] == "QuestTree_Summary_120030")["localizations"]
        require(all(synopsis[language]["status"] == "resolved"
                    for language in ("zh-Hans", "en", "ja", "ko")) and
                "捉拿归案" in synopsis["zh-Hans"]["content"] and
                "bring him to justice" in synopsis["en"]["content"] and
                "逮捕" in synopsis["ja"]["content"] and
                "체포하여 재판에 회부" in synopsis["ko"]["content"],
                "four-language capture synopsis and KO trial-referral limit", checks)
        confrontation = next(row for row in jsonl(source / "SCENE_AND_EVIDENCE_LEDGER.jsonl")
                             if row["flow_state_row_index"] == 1092 and row["action_index"] == 1)
        require([(confrontation["talk_items"][index]["technical_speaker_id"],
                  confrontation["talk_items"][index]["text_key"])
                 for index in (0, 15, 16, 19)] ==
                [(370, "Character_YinLin_51_1"), (811, "Character_YinLin_51_18"),
                 (370, "Character_YinLin_51_19"), (919, "Character_YinLin_51_23")],
                "direct scene ends around surrender and Patroller arrival", checks)
        audit = json.loads((source / "COLLECTION_AUDIT.json").read_text(encoding="utf-8"))
        direct = audit["scopes"]["direct_character"]
        require(audit["valid"] and direct["voice_completeness_valid"], "selected collection audit valid", checks)
        require(
            (direct["accepted_occurrences"], direct["source_voiced"], direct["source_unvoiced"], direct["candidate_occurrences"]) == (463, 374, 89, 469),
            "direct occurrence denominator",
            checks,
        )
        require(
            (direct["semantic_voice_lines"], direct["render_associations"], direct["unique_flac_objects"]) == (439, 1776, 1725),
            "voice line/association/object denominators",
            checks,
        )
        decisions = jsonl(source / "occurrence_identity_crosswalk.jsonl")
        require(Counter(row["character_attribution"] for row in decisions) == {"accepted_solo": 463, "rejected": 6}, "identity crosswalk state counts", checks)
        package = json.loads((source / "character_source_package.json").read_text(encoding="utf-8"))
        archive = {row["content"]["text_key"]: row for row in package["favor_words"]}
        all_ascension = [f"FavorWord_{key}_Content" for key in (130221, 130222, 130223, 130224, 130253)]
        require(all(key in archive for key in all_ascension), "five ascension archive entries retained", checks)
        require(all(archive[key]["content"]["values"][language]["status"] == "resolved"
                    for key in all_ascension for language in ("zh-Hans", "en", "ja", "ko")),
                "four-language ascension text witnesses resolved", checks)
        require("强韧的精神" in archive["FavorWord_130222_Content"]["content"]["values"]["zh-Hans"]["content"]
                and "unbreakable will" in archive["FavorWord_130222_Content"]["content"]["values"]["en"]["content"],
                "resilience versus English invulnerability wording", checks)
        require("和你一起" in archive["FavorWord_130224_Content"]["content"]["values"]["zh-Hans"]["content"],
                "shared-purpose ascension wording", checks)
        final = archive["FavorWord_130253_Content"]["content"]["values"]
        require("信任" in final["zh-Hans"]["content"] and "喜爱" in final["zh-Hans"]["content"]
                and "友好" in final["ja"]["content"] and "사랑" in final["ko"]["content"],
                "trust-versus-liking and JA/KO intimacy divergence", checks)
        require(archive["FavorWord_130253_Content"]["source_locator"].endswith("/947"),
                "Ascension V source position retained separately from I–IV", checks)
        context = {row["text_key"]: row for row in jsonl(source / "CONTEXT_TEXT_WITNESSES.jsonl")}
        def zh(key: str) -> str:
            return context[key]["values"]["zh-Hans"]["content"]
        call = next(row for row in jsonl(source / "RAW_RELEVANT_FLOW_STATES.jsonl")
                    if row["source_locator"].endswith("#/812"))
        actions = json.loads(call["raw"]["Actions"])
        talk = actions[6]["Params"]["TalkItems"]
        option_slots = {index: item["Options"][0]
                        for index, item in enumerate(talk) if item.get("Options")}
        require(actions[6]["Name"] == "ShowTalk" and len(talk) == 11 and
                "TalkSequence" not in actions[6]["Params"] and
                {index: option["TidTalkOption"] for index, option in option_slots.items()} ==
                {3: "Character_YinLin_26_5",
                 6: "Character_YinLin_26_9",
                 8: "Character_YinLin_26_12"} and
                all(option["Actions"] == [] for option in option_slots.values()) and
                [item["WhoId"] for item in talk] == [370, 83] + [370] * 9 and
                talk[0]["TidTalk"] == "Character_YinLin_26_1" and
                talk[1]["TidTalk"] == "Character_YinLin_26_2" and
                talk[8]["TidTalk"] == "Character_YinLin_26_11",
                "812 call action has ten Yinlin turns, one cue and three nonbranching prompts",
                checks)
        require("真的要这么做" in zh("Character_YinLin_26_1") and
                "我认为没必要" in zh("Character_YinLin_26_3") and
                "在和治安署的联络员进行联络" in zh("Character_YinLin_26_6") and
                "礼荣和媛媛保护起来" in zh("Character_YinLin_26_7") and
                "人偶带到安全的地方" in zh("Character_YinLin_26_10"),
                "unheard instruction is followed by explicit protection and later inquiry plan",
                checks)
        safehouse = context["Character_YinLin_26_11"]["values"]
        require("联络员告诉我" in safehouse["zh-Hans"]["content"] and
                "My contact informed me" in safehouse["en"]["content"] and
                "治安署に潜入調査員が使う隠れ家の場所を伝えた" in
                safehouse["ja"]["content"] and
                "연락원이 그러는데" in safehouse["ko"]["content"],
                "JA reverses safe-house information flow versus ZH/EN/KO",
                checks)
        emergency = next(row for row in jsonl(source / "RAW_RELEVANT_FLOW_STATES.jsonl")
                         if row["source_locator"].endswith("#/1090"))
        emergency_actions = json.loads(emergency["raw"]["Actions"])
        emergency_talk = emergency_actions[4]["Params"]["TalkItems"]
        require(emergency["raw"]["StateKey"] == "剧情_剧情_角色_吟霖线新_89_1"
                and emergency_actions[4]["Name"] == "ShowTalk"
                and emergency_actions[4]["Params"]["TalkSequence"] == [list(range(1, 9))]
                and len(emergency_talk) == 8
                and [item["WhoId"] for item in emergency_talk] ==
                [370, 918, 370, 918, 370, 370, 370, 370]
                and {index: item["Options"][0]["TidTalkOption"]
                     for index, item in enumerate(emergency_talk) if item.get("Options")} ==
                {4: "Character_YinLin_43_6", 5: "Character_YinLin_43_8"},
                "1090 emergency sequence separates child, Yinlin, and two single player options",
                checks)
        quest_nodes = json.loads((source_root / "_sources" / "Arikatsu_WutheringWaves_Data" /
                                  "BinData" / "QuestNodeData" / "questnodedata.json").read_text(encoding="utf-8"))
        emergency_node = quest_nodes[1430]
        require(emergency_node["Key"] == "114000018_103"
                and emergency_node["Data"]["Condition"]["Flow"]["FlowListName"] ==
                "剧情_剧情_角色_吟霖线新"
                and emergency_node["Data"]["Condition"]["Flow"]["FlowId"] == 89
                and emergency_node["Data"]["Condition"]["Flow"]["StateId"] == 1,
                "1090 flow state has exact child-quest condition match", checks)
        evacuation = context["Character_YinLin_43_3"]["values"]
        require("带大家" in evacuation["zh-Hans"]["content"]
                and "everyone" in evacuation["en"]["content"]
                and "皆を" in evacuation["ja"]["content"]
                and "할머니를 데리고" in evacuation["ko"]["content"]
                and "모두" not in evacuation["ko"]["content"]
                and "误入歧途" in zh("Character_YinLin_43_6")
                and "一切都告诉我" in zh("Character_YinLin_43_8")
                and "先想办法活下去" in zh("Character_YinLin_43_10"),
                "evacuation scope differs in KO and Rover owns defense/truth demand",
                checks)
        factory = next(row for row in jsonl(source / "RAW_RELEVANT_FLOW_STATES.jsonl")
                       if row["source_locator"].endswith("#/1260"))
        factory_actions = json.loads(factory["raw"]["Actions"])
        factory_talk = factory_actions[1]["Params"]["TalkItems"]
        require(factory_actions[1]["Name"] == "ShowTalk"
                and factory_actions[1]["Params"]["TalkSequence"] == [list(range(1, 7))]
                and [item["WhoId"] for item in factory_talk] == [370, 370, 370, 370, 812, 370]
                and factory_talk[4]["TidTalk"] == "Character_YinLin_61_5"
                and factory_talk[4]["Options"][0]["TidTalkOption"] == "Character_YinLin_61_6",
                "1260 factory sequence keeps parenthetical under technical speaker 812",
                checks)
        recording = context["Character_YinLin_61_5"]["values"]
        require("偃师大人的研究" in zh("Character_YinLin_61_4")
                and "prove what he's been up to" in recording["en"]["content"]
                and all("prove" not in recording[language]["content"].lower()
                        for language in ("zh-Hans", "ja", "ko")),
                "factory research cover and EN-only explicit proof motive stay distinct",
                checks)
        tablet_state = next(row for row in jsonl(source / "RAW_RELEVANT_FLOW_STATES.jsonl")
                            if row["source_locator"].endswith("#/668"))
        tablet_action = json.loads(tablet_state["raw"]["Actions"])[3]
        tablet_talk = tablet_action["Params"]["TalkItems"]
        tablet_sequence = tablet_action["Params"]["TalkSequence"]
        tablet_transitions = tablet_action["Params"]["SequenceTransitions"]
        require(tablet_state["raw"]["StateKey"] == "剧情_角色_吟霖线_副本临时_1_2"
                and tablet_action["Name"] == "ShowTalk" and len(tablet_talk) == 24
                and tablet_sequence == [list(range(1, 12)), [12], [13], list(range(14, 25))]
                and [(entry["NextSequenceIndex"], entry["OptionText"])
                     for entry in tablet_transitions["0"]] ==
                [(1, "（给出触板）"), (2, "你休想……")]
                and tablet_transitions["1"][0]["NextSequenceIndex"] == 3
                and tablet_transitions["2"][0]["NextSequenceIndex"] == 3
                and [tablet_talk[index]["WhoId"] for index in (5, 11, 12, 14, 15, 23)] ==
                [811, 370, 370, 812, 812, 812],
                "668 tablet handover has two exclusive reply paths converging on mediated text",
                checks)
        tablet_scene = next(row for row in jsonl(source / "SCENE_AND_EVIDENCE_LEDGER.jsonl")
                            if row["flow_state_row_index"] == 668 and row["action_index"] == 3)
        tablet_items = tablet_scene["talk_items"]
        require(Counter(item["technical_speaker_id"] for item in tablet_items) ==
                {370: 14, 811: 4, 812: 6}
                and all(item["play_voice"] and item["story_production_media"] == []
                        for item in tablet_items if item["technical_speaker_id"] == 812)
                and all("Zapstring" in item["speaker"]["names"]["en"]["content"]
                        for item in tablet_items if item["technical_speaker_id"] == 812),
                "668 direct cover speech versus six unresolved Zapstring tablet media rows",
                checks)
        trust = next(item for item in tablet_items if item["text_key"] == "Character_YinLin_45_19")
        witnesses = trust["text_witnesses"]
        require("选择相信我" in witnesses["zh"]["content"]
                and "follow my instructions" in witnesses["en"]["content"]
                and "人形に筆談" in witnesses["ja"]["content"]
                and "날 믿어줘" in witnesses["ko"]["content"]
                and "我在这家伙身上安装" in
                next(item for item in tablet_items if item["text_key"] == "Character_YinLin_45_6")["text_witnesses"]["zh"]["content"]
                and "在路上我会解开" in
                next(item for item in tablet_items if item["text_key"] == "Character_YinLin_45_30")["text_witnesses"]["zh"]["content"],
                "factory trust/obedience divergence, Dollmaker tracker claim, and future restraint promise",
                checks)
        require("人格和记忆" in zh("Character_YinLin_18_3")
                and "超频的风险" in zh("Character_YinLin_18_8")
                and "不得而知" in zh("Character_YinLin_18_7"),
                "replica resemblance, Overclock risk, and unknown provenance stay separate", checks)
        require("人偶" in zh("Character_YinLin_10_35")
                and "更像人" in zh("Character_YinLin_14_8"),
                "constructed puppet identification and later moral rebuke coexist", checks)
        require("负责拉拢新人" in zh("Character_YinLin_18_10")
                and "不会把那些人偶" in zh("Character_YinLin_14_15"),
                "Li Rong recruitment and refusal to surrender prototypes retained", checks)
        require("过去也不能抹去" in zh("Character_YinLin_75_13")
                and "火焰可能会引来" in zh("Character_YinLin_75_14")
                and "活人更重要" in zh("Character_YinLin_75_17"),
                "workshop burn reversal has historical, practical, and living-person grounds", checks)
        line_rows = jsonl(voice / "COMPLETE_VOICE_LINE_ANALYSIS.jsonl")
        require(len(line_rows) == 439, "439 selected voice-line records", checks)
        call_keys = {
            "Character_YinLin_26_1": 0, "Character_YinLin_26_3": 2,
            "Character_YinLin_26_4": 3, "Character_YinLin_26_7": 5,
            "Character_YinLin_26_10": 7, "Character_YinLin_26_11": 8,
        }
        call_lines = [row for row in line_rows if row["text_key"] in call_keys]
        require(len(call_lines) == 6 and
                all(line["source_locator"].endswith(
                    f"/812/Actions!/6/Params/TalkItems/{call_keys[line['text_key']]}") and
                    len(line["renders"]) == 4 and
                    all(render["source_wem_sha256_verified"] and
                        render["materialization_status"] ==
                        "flac_roundtrip_pcm_identical"
                        for render in line["renders"])
                    for line in call_lines),
                "six call/plan semantic lines join to twenty-four PCM-valid dub renders",
                checks)
        for selector, item_to_key, expected in (
            ("1090/Actions!/4", {0: "Character_YinLin_43_1", 2: "Character_YinLin_43_3",
                                   4: "Character_YinLin_43_5", 5: "Character_YinLin_43_7",
                                   6: "Character_YinLin_43_9", 7: "Character_YinLin_43_10"}, 6),
            ("1260/Actions!/1", {0: "Character_YinLin_61_1", 1: "Character_YinLin_61_2",
                                   2: "Character_YinLin_61_3", 3: "Character_YinLin_61_4",
                                   5: "Character_YinLin_61_7"}, 5),
        ):
            scene_lines = [line for line in line_rows if f"/{selector}/Params/TalkItems/" in line["source_locator"]]
            require(len(scene_lines) == expected
                    and {line["text_key"] for line in scene_lines} == set(item_to_key.values())
                    and all(line["source_locator"].endswith(
                        f"/{selector}/Params/TalkItems/{next(index for index, key in item_to_key.items() if key == line['text_key'])}")
                        and len(line["renders"]) == 4
                        and all(render["source_wem_sha256_verified"]
                                and render["materialization_status"] == "flac_roundtrip_pcm_identical"
                                for render in line["renders"])
                        for line in scene_lines),
                    f"{selector} exact voiced occurrences and four-dub PCM joins", checks)
        tablet_lines = [line for line in line_rows
                        if selected_by_source_action(line["source_locator"], "668/3")]
        require(len(tablet_lines) == 14
                and {line["text_key"] for line in tablet_lines} ==
                {item["text_key"] for item in tablet_items if item["technical_speaker_id"] == 370}
                and sum(len(line["renders"]) for line in tablet_lines) == 64
                and len({render["canonical_pcm_sha256"] for line in tablet_lines
                         for render in line["renders"]}) == 58
                and all(render["source_wem_sha256_verified"] and
                        render["materialization_status"] == "flac_roundtrip_pcm_identical"
                        for line in tablet_lines for render in line["renders"]),
                "668 fourteen direct Yinlin lines resolve to 64 valid renders and 58 PCM identities",
                checks)
        for key in ("Character_YinLin_45_5", "Character_YinLin_45_15"):
            line = next(item for item in tablet_lines if item["text_key"] == key)
            by_language = {language: [render for render in line["renders"]
                                      if render["voice_language"] == language]
                           for language in LANGUAGES}
            require(all(len(renders) == 2 for renders in by_language.values())
                    and len({r["canonical_pcm_sha256"] for r in by_language["en"]}) == 2
                    and all(len({r["canonical_pcm_sha256"] for r in by_language[language]}) == 1
                            for language in ("ja", "ko", "zh")),
                    f"668 {key} EN distinct versus JA/KO/ZH same-PCM gender-path pairs", checks)
        line_index = {(row["text_key"], row["semantic_voice_occurrence_id"]): row for row in line_rows}
        for case in cases["cases"]:
            line = line_index[(case["text_key"], case["semantic_voice_occurrence_id"])]
            require(case["source_locator"] == line["source_locator"], f"source locator {case['text_key']}", checks)
            expected = {(r["runtime_render_variant_id"], r["canonical_pcm_sha256"], r["flac_sha256"]) for r in line["renders"]}
            observed = {(r["render_variant_id"], r["canonical_pcm_sha256"], r["flac_sha256"]) for r in case["renders"]}
            require(expected == observed, f"render join {case['text_key']}", checks)
        audio = json.loads(measurement.read_text(encoding="utf-8"))
        require((audio["manifest_objects"], audio["measured_objects"], audio["repeated_pcm_manifest_rows"]) == (1725, 1725, 4), "full local audio measurement counts", checks)
        require(not audio["failed_objects"], "no local audio measurement failures", checks)
        cohort_path = source_root / "_research" / "character_packets" / "Yinlin" / "audio_work" / "YINLIN_SOURCE_COHORT_AUDIT.json"
        cohort_audit = json.loads(cohort_path.read_text(encoding="utf-8"))
        require(sha256_file(cohort_path) == COHORT_SHA256, "private source-cohort audit SHA-256", checks)
        require(cohort_audit["source_commit"] == COMMIT and cohort_audit["source_generation"] == model["source_generation"],
                "source-cohort pin matches packet", checks)
        require(cohort_audit["line_analysis_sha256"] == sha256_file(voice / "COMPLETE_VOICE_LINE_ANALYSIS.jsonl")
                and cohort_audit["object_measurements_sha256"] == sha256_file(measurement.parent / "AUDIO_OBJECT_MEASUREMENTS.jsonl")
                and cohort_audit["measurement_summary_sha256"] == sha256_file(measurement),
                "cohort source and measurement inputs byte-pinned", checks)
        require(cohort_audit["whole_measured_object_count"] == 1725
                and cohort_audit["whole_measured_integrity_pass_count"] == 1725
                and not cohort_audit["human_perceptual_review_performed"]
                and not cohort_audit["video_review_performed"],
                "cohort measurement complete without claimed human AV", checks)
        cohorts = {cohort["name"]: cohort for cohort in cohort_audit["cohorts"]}
        require(len(cohort_audit["cohorts"]) == 16 and set(cohorts) == set(COHORT_SPECS),
                "16 named source-defined cohorts", checks)
        all_members: list[dict] = []
        for name, (selector, semantic_count, render_count) in COHORT_SPECS.items():
            cohort = cohorts[name]
            members = cohort["members"]
            require(cohort["source_actions"] == [selector]
                    and cohort["semantic_lines"] == semantic_count
                    and cohort["render_associations"] == render_count
                    and len(members) == render_count
                    and not cohort["semantic_lines_without_renders"],
                    f"cohort selector and counts: {name}", checks)
            expected = {
                source_render_tuple(line["semantic_voice_occurrence_id"], line["source_locator"], line["text_key"], render)
                for line in line_rows if selected_by_source_action(line["source_locator"], selector)
                for render in line["renders"]
            }
            observed = {audit_render_tuple(member) for member in members}
            require(len(expected) == render_count and observed == expected,
                    f"exact source-to-render membership: {name}", checks)
            all_members.extend(members)
        semantic_ids = {member["semantic_voice_occurrence_id"] for member in all_members}
        render_ids = {member["render_analysis_id"] for member in all_members}
        pcm_ids = {member["canonical_pcm_sha256"] for member in all_members}
        require((len(semantic_ids), len(render_ids), len(pcm_ids), len(all_members)) == (181, 728, 725, 728),
                "disjoint cohort union: 181 semantic / 728 renders / 725 PCM", checks)
        special = [member for member in all_members if selected_by_source_action(member["source_locator"], "353/6@28")]
        special_by_language = {language: [member for member in special if member["voice_language"] == language]
                               for language in LANGUAGES}
        require(len(special) == 8 and {member["text_key"] for member in special} == {"Character_YinLin_58_36"}
                and all(len(group) == 2 and len({member["render_analysis_id"] for member in group}) == 2
                        for group in special_by_language.values())
                and len({member["canonical_pcm_sha256"] for member in special_by_language["en"]}) == 2
                and all(len({member["canonical_pcm_sha256"] for member in special_by_language[language]}) == 1
                        for language in ("ja", "ko", "zh")),
                "353/6/28 EN variant versus JA/KO/ZH same-PCM aliases", checks)
        festival_actions = {(3987, 6): 10, (3991, 6): 4, (3992, 7): 23, (4231, 1): 11}
        for (row, action), expected_count in festival_actions.items():
            rows = [item for item in decisions if item["character_attribution"] == "accepted_solo"
                    and item["flow_state_row_index"] == row and item["action_index"] == action]
            require(len(rows) == expected_count and all(item["play_voice"] is False for item in rows)
                    and not any(line["source_locator"] == item["source_locator"] for item in rows for line in line_rows),
                    f"earlier festival source-unvoiced: {row}/{action}", checks)
        require(sum(selected_by_source_action(line["source_locator"], "15092/6") for line in line_rows) == 20,
                "later 15092/6 party has 20 selected voiced lines", checks)
        result["source_crosscheck"] = "passed"
    result["result"] = "pass"
    result["check_count"] = len(checks)
    return result


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-root", type=Path, help="Extraction workspace root for deeper local evidence crosscheck")
    parser.add_argument("--write-report", action="store_true")
    args = parser.parse_args()
    report = validate(args.source_root)
    if args.write_report:
        (HERE / "VALIDATION_REPORT.json").write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8", newline="\n")
    print(json.dumps({key: report[key] for key in ("packet", "source_crosscheck", "result", "check_count")}, indent=2))


if __name__ == "__main__":
    main()
