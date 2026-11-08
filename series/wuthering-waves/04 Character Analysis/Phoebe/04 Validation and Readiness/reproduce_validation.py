#!/usr/bin/env python3
"""Validate Phoebe's draft packet and optional private evidence joins.

Checks structure, authority, source identity and media retrieval, not literary
truth or human performance. Read-only unless --write-report is supplied.
"""

from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import re
from statistics import median


HERE = Path(__file__).resolve().parent.parent
COMMIT = "353f2eaed119bc9f680eab92807d20ac75a79b40"
LANGUAGES = {"en", "ja", "ko", "zh"}
MEDIA_SUFFIXES = {".wav", ".flac", ".wem", ".mp3", ".mp4", ".png", ".webp", ".pak"}




# Exact character-root-relative paths after the artifact-class migration.
PACKET_ARTIFACT_PATHS = {'AUDIO_MATCHED_SEMANTIC_CASES.json': '03 Audiovisual and Voice/AUDIO_MATCHED_SEMANTIC_CASES.json', 'CHARACTER_VISUAL_DESIGN_PROFILE.json': '03 Audiovisual and Voice/CHARACTER_VISUAL_DESIGN_PROFILE.json', 'CHARACTER_VISUAL_DESIGN_PROFILE.md': '03 Audiovisual and Voice/CHARACTER_VISUAL_DESIGN_PROFILE.md', 'CHARACTER_VISUAL_REFERENCE_MANIFEST.json': '03 Audiovisual and Voice/CHARACTER_VISUAL_REFERENCE_MANIFEST.json', 'VALIDATION_REPORT.json': '04 Validation and Readiness/VALIDATION_REPORT.json', 'WUWA_PHOEBE_ANALYSIS_PACKET_README.md': 'WUWA_PHOEBE_ANALYSIS_PACKET_README.md', 'WUWA_PHOEBE_ARCHIVE_SKILL_KEY_SHARED_TEXT_AND_COMBAT_FAITH_PROFILE.md': '01 Evidence and Source-Facing/WUWA_PHOEBE_ARCHIVE_SKILL_KEY_SHARED_TEXT_AND_COMBAT_FAITH_PROFILE.md', 'WUWA_PHOEBE_AV_AND_HUMAN_RETRIEVAL_PLAN.md': '03 Audiovisual and Voice/WUWA_PHOEBE_AV_AND_HUMAN_RETRIEVAL_PLAN.md', 'WUWA_PHOEBE_AV_HUMAN_RETRIEVAL_CROSSWALK.md': '03 Audiovisual and Voice/WUWA_PHOEBE_AV_HUMAN_RETRIEVAL_CROSSWALK.md', 'WUWA_PHOEBE_CARE_AUTHORITY_AND_CONSENT_PROFILE.md': '01 Evidence and Source-Facing/WUWA_PHOEBE_CARE_AUTHORITY_AND_CONSENT_PROFILE.md', 'WUWA_PHOEBE_CETUS_REPLY_RECEIVING_AND_SELFHOOD_PROFILE.md': '01 Evidence and Source-Facing/WUWA_PHOEBE_CETUS_REPLY_RECEIVING_AND_SELFHOOD_PROFILE.md', 'WUWA_PHOEBE_CHARACTER_DEEP_DIVE_PRE_AV.md': '01 Evidence and Source-Facing/WUWA_PHOEBE_CHARACTER_DEEP_DIVE_PRE_AV.md', 'WUWA_PHOEBE_CHARACTER_MODEL_PACKAGE.json': '02 Reconstruction/WUWA_PHOEBE_CHARACTER_MODEL_PACKAGE.json', 'WUWA_PHOEBE_CIVIC_FAITH_VAULT_TRANSFER_AND_REBUILDING_PROFILE.md': '01 Evidence and Source-Facing/WUWA_PHOEBE_CIVIC_FAITH_VAULT_TRANSFER_AND_REBUILDING_PROFILE.md', 'WUWA_PHOEBE_CLAIM_REVISION_LEDGER.md': '04 Validation and Readiness/WUWA_PHOEBE_CLAIM_REVISION_LEDGER.md', 'WUWA_PHOEBE_EARLY_CITY_GUIDE_COMMON_ECHO_AUTHORITY_AND_CARNEVALE_PROFILE.md': '01 Evidence and Source-Facing/WUWA_PHOEBE_EARLY_CITY_GUIDE_COMMON_ECHO_AUTHORITY_AND_CARNEVALE_PROFILE.md', 'WUWA_PHOEBE_EVIDENCE_AND_FALSIFICATION_MATRIX.md': '01 Evidence and Source-Facing/WUWA_PHOEBE_EVIDENCE_AND_FALSIFICATION_MATRIX.md', 'WUWA_PHOEBE_HOLIDAY_INVITATION_AND_ECHO_DESTINATION_AGENCY_PROFILE.md': '01 Evidence and Source-Facing/WUWA_PHOEBE_HOLIDAY_INVITATION_AND_ECHO_DESTINATION_AGENCY_PROFILE.md', 'WUWA_PHOEBE_MODEL_FIDELITY_AND_STRESS_TEST_PRE_AV.md': '04 Validation and Readiness/WUWA_PHOEBE_MODEL_FIDELITY_AND_STRESS_TEST_PRE_AV.md', 'WUWA_PHOEBE_ORDINARY_JOY_GIFTS_AND_SELF_WISH_PROFILE.md': '01 Evidence and Source-Facing/WUWA_PHOEBE_ORDINARY_JOY_GIFTS_AND_SELF_WISH_PROFILE.md', 'WUWA_PHOEBE_RELATIONSHIP_STATE_AND_ORDINARY_LIFE_PROFILE.md': '01 Evidence and Source-Facing/WUWA_PHOEBE_RELATIONSHIP_STATE_AND_ORDINARY_LIFE_PROFILE.md', 'WUWA_PHOEBE_SIREN_TIDEBREAKER_ECOLOGY_AND_DIALOGUE_PROFILE.md': '01 Evidence and Source-Facing/WUWA_PHOEBE_SIREN_TIDEBREAKER_ECOLOGY_AND_DIALOGUE_PROFILE.md', 'WUWA_PHOEBE_SOURCE_CENSUS_CHRONOLOGY_AND_IDENTITY_AUDIT.md': '04 Validation and Readiness/WUWA_PHOEBE_SOURCE_CENSUS_CHRONOLOGY_AND_IDENTITY_AUDIT.md', 'WUWA_PHOEBE_SPEECH_AND_MACHINE_VOICE_PROFILE_PRE_AV.md': '03 Audiovisual and Voice/WUWA_PHOEBE_SPEECH_AND_MACHINE_VOICE_PROFILE_PRE_AV.md', 'WUWA_PHOEBE_VAULT_CRISIS_AND_POSTWAR_WORKLOAD_PROFILE.md': '01 Evidence and Source-Facing/WUWA_PHOEBE_VAULT_CRISIS_AND_POSTWAR_WORKLOAD_PROFILE.md', 'reproduce_validation.py': '04 Validation and Readiness/reproduce_validation.py'}

def packet_artifact(root: Path, name: str) -> Path:
    return root / PACKET_ARTIFACT_PATHS.get(name, name)

def jsonl(path: Path) -> list[dict]:
    with path.open(encoding="utf-8") as handle:
        return [json.loads(line) for line in handle if line.strip()]


def require(condition: bool, message: str, checks: list[str]) -> None:
    if not condition:
        raise AssertionError(message)
    checks.append(message)


def validate(source_root: Path | None) -> dict:
    checks: list[str] = []
    matrix = (packet_artifact(HERE, "WUWA_PHOEBE_EVIDENCE_AND_FALSIFICATION_MATRIX.md")).read_text(encoding="utf-8")
    evidence_ids = set(re.findall(r"\| (PHO-E\d{2}) \|", matrix))
    claim_ids = set(re.findall(r"\| (PHO-C\d{2}) —", matrix))
    require(evidence_ids == {f"PHO-E{index:02d}" for index in range(1, 43)},
            "42 contiguous evidence bundles", checks)
    require(claim_ids == {f"PHO-C{index:02d}" for index in range(1, 40)},
            "39 contiguous claim rows", checks)
    vault_profile = (packet_artifact(HERE, "WUWA_PHOEBE_VAULT_CRISIS_AND_POSTWAR_WORKLOAD_PROFILE.md")).read_text(
        encoding="utf-8")
    require(all(token in vault_profile for token in
                ("QuestTree_Summary_230301", "QuestTree_Summary_240002",
                 "PHO-E36", "PHO-E37", "EN", "device")),
            "vault and recovery specialist retains source and localization anchors", checks)
    guide_profile = (packet_artifact(HERE, "WUWA_PHOEBE_EARLY_CITY_GUIDE_COMMON_ECHO_AUTHORITY_AND_CARNEVALE_PROFILE.md")).read_text(
        encoding="utf-8")
    require(all(token in guide_profile for token in
                ("4203", "114000027_24", "La Guardia", "PHO-E38", "PHO-C35",
                 "English", "Carnival")),
            "early city-guide specialist retains graph, quest and localization anchors", checks)
    sea_profile = (packet_artifact(HERE, "WUWA_PHOEBE_SIREN_TIDEBREAKER_ECOLOGY_AND_DIALOGUE_PROFILE.md")).read_text(
        encoding="utf-8")
    require(all(token in sea_profile for token in
                ("6587/3", "880000038_56", "PHO-E39", "PHO-C36", "Abby", "Japanese")),
            "sea-ecology specialist retains source and uncertainty anchors", checks)
    civic_profile = (packet_artifact(HERE, "WUWA_PHOEBE_CIVIC_FAITH_VAULT_TRANSFER_AND_REBUILDING_PROFILE.md")).read_text(
        encoding="utf-8")
    require(all(token in civic_profile for token in
                ("5601/3", "10451/7", "9930/4", "PHO-E40", "PHO-E41", "PHO-E42",
                 "PHO-C37", "PHO-C38", "PHO-C39", "Cartethyia", "Zani", "Korean")),
            "civic-faith specialist retains three sources and speaker/language limits", checks)
    require(
        not any(path.suffix.lower() in MEDIA_SUFFIXES for path in HERE.rglob("*") if path.is_file()),
        "no raw media in Git packet",
        checks,
    )
    for path in HERE.rglob("WUWA_PHOEBE_*.md"):
        body = path.read_text(encoding="utf-8")
        require(
            body.startswith("---\n") and "\nstatus: draft_noncurrent\n" in body,
            f"draft authority: {path.name}", checks,
        )
        require(
            "\ndo_not_use_as_current_authority: true\n" in body,
            f"noncurrent flag: {path.name}", checks,
        )
        require(
            f"\nsource_commit: {COMMIT}\n" in body,
            f"source pin: {path.name}", checks,
        )
    model = json.loads((packet_artifact(HERE, "WUWA_PHOEBE_CHARACTER_MODEL_PACKAGE.json")).read_text(encoding="utf-8"))
    require(
        model["authority"] == "draft_noncurrent" and model["source_commit"] == COMMIT,
        "model authority and source pin", checks,
    )
    rules = model["rules"]
    require(len(rules) == 20 and len({rule["id"] for rule in rules}) == 20, "20 distinct model rules", checks)
    require(all(set(rule["evidence_ids"]) <= evidence_ids for rule in rules), "all rule evidence IDs resolve", checks)
    require(all(rule["probability"] is None for rule in rules), "no fabricated numerical probabilities", checks)
    probes = (packet_artifact(HERE, "WUWA_PHOEBE_MODEL_FIDELITY_AND_STRESS_TEST_PRE_AV.md")).read_text(encoding="utf-8")
    require(set(re.findall(r"\| (PHO-P\d{2}) \|", probes)) ==
            {f"PHO-P{index:02d}" for index in range(1, 42)},
            "41 contiguous non-blind probes", checks)
    interaction_block = probes.split("## Nine interaction tests", 1)[1].split("\nTogether these cases", 1)[0]
    require(len(re.findall(r"(?m)^\*\*[^\n]+\*\* ", interaction_block)) == 9,
            "nine constructed interaction tests", checks)
    archive_profile = (packet_artifact(HERE, "WUWA_PHOEBE_ARCHIVE_SKILL_KEY_SHARED_TEXT_AND_COMBAT_FAITH_PROFILE.md")).read_text(
        encoding="utf-8"
    )
    require("FavorWord_160719_Content" in archive_profile and "Cantarella" in archive_profile,
            "shared-key archive specialist is present", checks)
    cases = json.loads((packet_artifact(HERE, "AUDIO_MATCHED_SEMANTIC_CASES.json")).read_text(encoding="utf-8"))
    require(cases["semantic_cases"] == 12 and len(cases["cases"]) == 12, "12 matched semantic cases", checks)
    crosswalk = (packet_artifact(HERE, "WUWA_PHOEBE_AV_HUMAN_RETRIEVAL_CROSSWALK.md")).read_text(encoding="utf-8")
    require(all(f"`{case['text_key']}`" in crosswalk for case in cases["cases"]),
            "all 12 exact sound cases occur in AV crosswalk", checks)
    require("11779/2/4" in crosswalk and "precedes" in crosswalk,
            "ambiguous reform referent remains explicit in AV crosswalk", checks)
    require("PHO-R09" in crosswalk and "6587/3" in crosswalk,
            "sea-ecology runtime retrieval target remains explicit", checks)
    require(all(f"PHO-R{index:02d}" in crosswalk for index in (10, 11, 12)) and
            all(f"{state}/" in crosswalk for state in (5601, 10451, 9930)),
            "three civic-faith runtime retrieval targets remain explicit", checks)
    archive_target_events = (3013562366, 3013562365, 2324455528, 2324455531,
                             189042748, 1923856019, 1503895814, 1168224278, 3321153489)
    require(all(str(event_id) in crosswalk for event_id in archive_target_events),
            "archive nominations and Cantarella negative-control event IDs are in AV crosswalk", checks)
    require(sum(len(case["renders"]) for case in cases["cases"]) == 48, "48 selected render records", checks)
    require(
        all({render["language"] for render in case["renders"]} == LANGUAGES for case in cases["cases"]),
        "all cases have four languages", checks,
    )
    require(
        all(len(render[name]) == 64 for case in cases["cases"] for render in case["renders"]
            for name in ("wem_sha256", "canonical_pcm_sha256", "flac_sha256")),
        "all selected render hashes present", checks,
    )
    result = {
        "packet": "Phoebe", "scope": "PHOEBE_PINNED_3_6_0_TEXT_AUDIO_PRE_AV",
        "checks": checks, "source_crosscheck": "not_requested",
    }
    if source_root is not None:
        source = source_root / "ANALYSIS" / "Characters" / "Phoebe"
        voice = source_root / "_voice_media" / "character" / "complete_voice_corpus" / "Phoebe" / "v0_1"
        summary = source_root / "_research" / "character_packets" / "Phoebe" / "audio_work" / "AUDIO_MEASUREMENT_SUMMARY.json"
        audit = json.loads((source / "COLLECTION_AUDIT.json").read_text(encoding="utf-8"))
        quest_nodes = {
            node["Id"]: node for node in json.loads(
                (source_root / "_sources" / "Arikatsu_WutheringWaves_Data" /
                 "BinData" / "QuestTree" / "questtreenode.json").read_text(encoding="utf-8"))
        }
        require(quest_nodes[230301]["QuestArray"] ==
                [122000008, 122000009, 122000010, 122000011]
                and quest_nodes[230301]["MainQuestNode"] == 210030
                and quest_nodes[230301]["Summary"] == "QuestTree_Summary_230301"
                and quest_nodes[240002]["QuestArray"] == [189800000]
                and quest_nodes[240002]["MainQuestNode"] == 212000
                and quest_nodes[240002]["Summary"] == "QuestTree_Summary_240002",
                "vault and recovery synopsis nodes attach to pinned quests", checks)
        mentions = {row["text_key"]: row for row in jsonl(source / "source_mentions.jsonl")}
        require(all(key in mentions and
                    all(mentions[key]["localizations"][language]["status"] == "resolved"
                        for language in ("zh-Hans", "en", "ja", "ko"))
                    for key in ("QuestTree_Summary_230301", "QuestTree_Summary_240002")),
                "four resolved locale witnesses for vault and recovery", checks)
        vault_text = mentions["QuestTree_Summary_230301"]["localizations"]
        require("修会试图抹除罪证的装置" in vault_text["zh-Hans"]["content"]
                and "菲比用她的力量解除了危机" in vault_text["zh-Hans"]["content"]
                and "bomb" in vault_text["en"]["content"]
                and "Phoebe uses her power" in vault_text["en"]["content"]
                and "装置" in vault_text["ja"]["content"]
                and "장치" in vault_text["ko"]["content"],
                "shared vault device/action and EN bomb-specific wording", checks)
        recovery_text = mentions["QuestTree_Summary_240002"]["localizations"]
        require("菲比分身乏术" in recovery_text["zh-Hans"]["content"]
                and "overwhelmed" in recovery_text["en"]["content"]
                and "あなた" in recovery_text["ja"]["content"]
                and "당신" in recovery_text["ko"]["content"],
                "four-locale workload and Rover-help synopsis", checks)
        direct = audit["scopes"]["direct_character"]
        require(audit["valid"] and direct["voice_completeness_valid"], "selected collection audit valid", checks)
        require(
            (direct["candidate_occurrences"], direct["accepted_occurrences"], direct["source_voiced"], direct["source_unvoiced"]) ==
            (674, 672, 416, 256),
            "direct occurrence denominator", checks,
        )
        require(
            (direct["semantic_voice_lines"], direct["render_associations"], direct["unique_flac_objects"]) ==
            (476, 1906, 1818),
            "voice line, association, object denominators", checks,
        )
        decisions = jsonl(source / "occurrence_identity_crosswalk.jsonl")
        require(
            Counter(row["character_attribution"] for row in decisions) ==
            {"accepted_solo": 672, "rejected": 1, "unresolved": 1},
            "identity crosswalk counts", checks,
        )
        guide_occurrences = [row for row in decisions
                             if row["flow_state_row_index"] == 4203 and
                             row["action_index"] == 2]
        require(len(guide_occurrences) == 26 and
                {row["talk_index"] for row in guide_occurrences} == set(range(26)) and
                all(row["character_attribution"] == "accepted_solo" and
                    row["technical_speaker_id"] == 1475 and row["play_voice"] and
                    row["resolved_media_association_count"] == 4
                    for row in guide_occurrences),
                "early guide has 26 accepted voiced Phoebe turns and 104 render associations", checks)
        sea_occurrences = [row for row in decisions
                           if row["flow_state_row_index"] == 6587 and
                           row["action_index"] == 3]
        require(len(sea_occurrences) == 11 and
                {row["talk_index"] for row in sea_occurrences} ==
                {0, 1, 2, 3, 4, 5, 7, 8, 9, 10, 11} and
                all(row["character_attribution"] == "accepted_solo" and
                    row["technical_speaker_id"] == 1475 and row["play_voice"] and
                    row["resolved_media_association_count"] == 4
                    for row in sea_occurrences),
                "sea action has eleven accepted voiced Phoebe turns and 44 render associations",
                checks)
        civic_specs = {
            5601: (3, {0, 1, 3, 7, 9, 10, 12, 14}, 18),
            10451: (7, {2, 9, 10, 13, 14, 16}, 20),
            9930: (4, {0, 1, 5, 6, 7}, 8),
        }
        for state, (action_index, talk_indices, _) in civic_specs.items():
            rows = [row for row in decisions
                    if row["flow_state_row_index"] == state and
                    row["action_index"] == action_index]
            require(len(rows) == len(talk_indices) and
                    {row["talk_index"] for row in rows} == talk_indices and
                    all(row["character_attribution"] == "accepted_solo" and
                        row["technical_speaker_id"] == 1475 and row["play_voice"] and
                        row["resolved_media_association_count"] == 4 for row in rows),
                    f"{state} civic action has exact accepted Phoebe turns and four render joins",
                    checks)
        holiday = {row_index: [r for r in decisions
                               if r["flow_state_row_index"] == row_index and
                               r["character_attribution"] == "accepted_solo"]
                   for row_index in (4798, 4807)}
        require(len(holiday[4798]) == 26 and len(holiday[4807]) == 23 and
                all(not r["play_voice"] and r["resolved_media_association_count"] == 0
                    for rows in holiday.values() for r in rows),
                "holiday invitation and Echo repair are source-unvoiced, not failed decodes", checks)
        raw = {int(row["source_locator"].rsplit("/", 1)[1]): row["raw"]
               for row in jsonl(source / "RAW_RELEVANT_FLOW_STATES.jsonl")}
        sea_action = json.loads(raw[6587]["Actions"])[3]
        sea_items = sea_action["Params"]["TalkItems"]
        require(sea_action["Name"] == "ShowTalk" and len(sea_items) == 12 and
                sea_action["Params"]["TalkSequence"] == [list(range(1, 13))] and
                not sea_action["Params"]["SequenceTransitions"] and
                sea_items[6]["Options"][0]["TidTalkOption"] == "DYHD_2502_7" and
                sea_items[9]["Options"][0]["TidTalkOption"] == "DYHD_2502_11" and
                all(sea_items[index]["WhoId"] == 1475 and
                    sea_items[index]["PlayVoice"]
                    for index in (0, 1, 2, 3, 4, 5, 7, 8, 9, 10, 11)),
                "sea inquiry retains one sequence and two single player option surfaces",
                checks)
        for state, (action_index, talk_indices, item_count) in civic_specs.items():
            action = json.loads(raw[state]["Actions"])[action_index]
            params = action["Params"]
            items = params["TalkItems"]
            require(action["Name"] == "ShowTalk" and len(items) == item_count and
                    {index for index, item in enumerate(items)
                     if item.get("WhoId") == 1475} == talk_indices and
                    all(items[index].get("PlayVoice") is True for index in talk_indices),
                    f"{state} raw speaker and voice flags match accepted civic occurrences", checks)
        vault_transfer = json.loads(raw[5601]["Actions"])[3]["Params"]
        future_exchange = json.loads(raw[10451]["Actions"])[7]["Params"]
        damage_survey = json.loads(raw[9930]["Actions"])[4]["Params"]
        require(vault_transfer["TalkSequence"] == [list(range(1, 19))] and
                future_exchange["TalkSequence"] == [list(range(1, 21))] and
                not vault_transfer["SequenceTransitions"] and
                not future_exchange["SequenceTransitions"] and
                all(not option["Actions"] for index in (1, 13)
                    for option in vault_transfer["TalkItems"][index]["Options"]) and
                not future_exchange["TalkItems"][0]["Options"][0]["Actions"],
                "transfer and future exchanges have linear source sequences with non-jumping Rover captions",
                checks)
        require("TalkSequence" not in damage_survey and
                "SequenceTransitions" not in damage_survey and
                damage_survey["TalkItems"][4].get("WhoId") is None and
                all(not option["Actions"] for item in damage_survey["TalkItems"]
                    for option in item.get("Options", [])),
                "damage survey has no encoded sequence/transition and only empty-action Rover captions",
                checks)
        invitation = json.loads(raw[4798]["Actions"])[3]["Params"]["TalkItems"]

        def choices(item: dict) -> list[tuple[str, int]]:
            return [(option["TidTalkOption"], option["Actions"][0]["Params"]["TalkId"])
                    for option in item.get("Options", [])]

        def jump(item: dict) -> int | None:
            targets = [action["Params"]["TalkId"] for action in item.get("Actions", [])
                       if action["Name"] == "JumpTalk"]
            return targets[0] if targets else None

        guide_action = json.loads(raw[4203]["Actions"])[2]
        guide = guide_action["Params"]["TalkItems"]
        require(guide_action["Name"] == "ShowTalk" and len(guide) == 26 and
                [item["Id"] for item in guide] == list(range(1, 27)) and
                all(item["WhoId"] == 1475 and item["PlayVoice"] for item in guide),
                "early guide raw talk items and speaker match crosswalk", checks)
        require(choices(guide[0]) ==
                [("Main_Linaxita_2_1_11_2", 2),
                 ("Main_Linaxita_2_1_11_3", 9),
                 ("Main_Linaxita_2_1_11_4", 14),
                 ("Main_Linaxita_2_1_11_5", 22),
                 ("Main_Linaxita_2_1_11_33", 26)] and
                [jump(guide[index]) for index in (7, 12, 20, 24)] ==
                [1, 1, 1, 1] and
                guide[25]["Actions"][0]["Name"] == "FinishTalk",
                "four guide topics return to menu and fifth option finishes", checks)
        require([option["TidTalkOption"] for option in guide[16]["Options"]] ==
                ["Main_Linaxita_2_1_11_22", "Main_Linaxita_2_1_11_23"] and
                all(not option["Actions"] for option in guide[16]["Options"]),
                "Carnival inner choices have no explicit JumpTalk targets", checks)
        quest_refs = jsonl(source / "QUEST_CONTEXT_REFERENCES.jsonl")
        require(any(row["quest_id"] == "880000038" and
                    row["raw"].get("Key") == "880000038_56" and
                    any(match["state_key"] == "剧情_V2.1航海活动主线_16_1"
                        for match in row["matching_references"])
                    for row in quest_refs),
                "sea-inquiry action has exact quest-node state match", checks)
        require(any(row["quest_id"] == "114000027" and
                    row["raw"]["Key"] == "114000027_24" and
                    row["raw"]["Data"]["Condition"]["Flow"]["FlowListName"] ==
                    "剧情_2_0_黎那汐塔主线_第一幕" and
                    row["raw"]["Data"]["Condition"]["Flow"]["FlowId"] == 11 and
                    row["raw"]["Data"]["Condition"]["Flow"]["StateId"] == 1
                    for row in quest_refs),
                "city-guide exact-state quest candidate joins flow 11 state 1", checks)
        civic_quest_states = {
            "122000009": "剧情_2_1_世界_埃弗拉德金库_POI任务_12_1",
            "158800019": "剧情_2_7_黎那汐塔主线_上半_2_33_1",
            "175000000": "剧情_2_7_黎那汐塔主线_下半_5_2",
        }
        for quest_id, state_key in civic_quest_states.items():
            require(any(str(row["quest_id"]) == quest_id and
                        any(match["state_key"] == state_key for match in row["matching_references"])
                        for row in quest_refs),
                    f"{quest_id} exact-state civic quest reference", checks)

        require(choices(invitation[2]) == [("POI_LGNJR_1_5", 4),
                                           ("POI_LGNJR_1_6", 5),
                                           ("POI_LGNJR_1_7", 8)] and
                [jump(invitation[i]) for i in (3, 6, 9)] == [11, 11, 11],
                "three compliment-response routes rejoin once", checks)
        require(choices(invitation[11]) == [("POI_LGNJR_1_17", 13),
                                            ("POI_LGNJR_1_18", 15),
                                            ("POI_LGNJR_1_19", 18)] and
                [jump(invitation[i]) for i in (13, 16)] == [22, 22] and
                choices(invitation[20]) == [("POI_LGNJR_1_29", 22)] and
                invitation[21]["TidTalk"] == "POI_LGNJR_1_30",
                "tour, Sentinel and opponent invitations converge without recorded refusal", checks)
        echo = json.loads(raw[4807]["Actions"])[5]["Params"]["TalkItems"]
        require([echo[i]["TidTalk"] for i in (21, 23, 27, 29, 30)] ==
                ["POI_LGNJR_11_23", "POI_LGNJR_11_25", "POI_LGNJR_11_29",
                 "POI_LGNJR_11_31", "POI_LGNJR_11_32"],
                "Echo treatment nod precedes later headshake and Ragunna question", checks)
        witnesses = {row["text_key"]: row["values"]
                     for row in jsonl(source / "CONTEXT_TEXT_WITNESSES.jsonl")}
        require(all(all(witnesses[key][lang]["status"] == "resolved"
                        for lang in ("en", "ja", "ko", "zh-Hans"))
                    for key in ("DYHD_2502_1", "DYHD_2502_3", "DYHD_2502_4",
                                "DYHD_2502_5", "DYHD_2502_6", "DYHD_2502_8",
                                "DYHD_2502_10", "DYHD_2502_12")),
                "sea inquiry's critical text keys resolve in four languages", checks)
        require("应该" in witnesses["DYHD_2502_3"]["zh-Hans"]["content"] and
                "may even" in witnesses["DYHD_2502_3"]["en"]["content"] and
                "近しい" in witnesses["DYHD_2502_3"]["ja"]["content"] and
                "本来であれば" in witnesses["DYHD_2502_6"]["ja"]["content"] and
                "会和鲸鱼说话吗" in witnesses["DYHD_2502_10"]["zh-Hans"]["content"] and
                "once this is all over" in witnesses["DYHD_2502_12"]["en"]["content"],
                "sea species/healing uncertainty and future conversation remain localized",
                checks)
        guide_keys = ("Main_Linaxita_2_1_11_13", "Main_Linaxita_2_1_11_16",
                      "Main_Linaxita_2_1_11_21", "Main_Linaxita_2_1_11_25",
                      "Main_Linaxita_2_1_11_31", "Main_Linaxita_2_1_11_32")
        require(all(all(witnesses[key][lang]["status"] == "resolved"
                        for lang in ("en", "ja", "ko", "zh-Hans"))
                    for key in guide_keys),
                "four-language guide witnesses resolve at civic and Carnival hinges", checks)
        require("使用权分享" in witnesses["Main_Linaxita_2_1_11_16"]["zh-Hans"]["content"] and
                "all citizens" in witnesses["Main_Linaxita_2_1_11_16"]["en"]["content"] and
                "只属于修会管辖的武装力量" in
                witnesses["Main_Linaxita_2_1_11_31"]["zh-Hans"]["content"] and
                "members" in witnesses["Main_Linaxita_2_1_11_32"]["en"]["content"] and
                "神职人员" in witnesses["Main_Linaxita_2_1_11_32"]["zh-Hans"]["content"],
                "guide source retains broad access, armed exception and clergy/member divergence", checks)
        civic_keys = ("POI_JINKU_2_10", "POI_JINKU_2_13", "POI_JINKU_2_15",
                      "POI_JINKU_2_19", "Main_Rinascita_2_12_7401_6",
                      "Main_Rinascita_2_12_7401_11", "Main_Rinascita_2_12_7401_16",
                      "Main_Rinascita_2_12_7401_18", "HRT_Rinascita_Interludes_601_2",
                      "HRT_Rinascita_Interludes_601_5", "HRT_Rinascita_Interludes_601_10")
        require(all(all(witnesses[key][lang]["status"] == "resolved"
                        for lang in ("en", "ja", "ko", "zh-Hans"))
                    for key in civic_keys),
                "four-language civic-faith hinge witnesses resolve", checks)
        require("接受训诫" in witnesses["POI_JINKU_2_10"]["zh-Hans"]["content"] and
                "訓戒" in witnesses["POI_JINKU_2_10"]["ja"]["content"] and
                "교육" in witnesses["POI_JINKU_2_10"]["ko"]["content"] and
                "Order's work" in witnesses["POI_JINKU_2_10"]["en"]["content"] and
                "没有被告知具体的内容" in witnesses["POI_JINKU_2_19"]["zh-Hans"]["content"],
                "vault transfer retains disciplinary localization and explicit non-disclosure", checks)
        require("并非盲信愚从" in witnesses["Main_Rinascita_2_12_7401_6"]["zh-Hans"]["content"] and
                "这里面是空的" in witnesses["Main_Rinascita_2_12_7401_16"]["zh-Hans"]["content"] and
                "我明白了" in witnesses["Main_Rinascita_2_12_7401_18"]["zh-Hans"]["content"],
                "Cartethyia counsel is distinct from Phoebe's question and acknowledgment", checks)
        require("清查" in witnesses["HRT_Rinascita_Interludes_601_2"]["zh-Hans"]["content"] and
                "居民们的安全" in witnesses["HRT_Rinascita_Interludes_601_5"]["zh-Hans"]["content"] and
                "商讨重建" in witnesses["HRT_Rinascita_Interludes_601_10"]["zh-Hans"]["content"] and
                "무역 협상" in witnesses["HRT_Rinascita_Interludes_601_10"]["ko"]["content"],
                "damage survey and KO trade/rebuilding divergence remain distinct", checks)
        selected_text_keys = ("POI_LGNJR_1_17", "POI_LGNJR_1_18", "POI_LGNJR_1_19",
                              "POI_LGNJR_1_21", "POI_LGNJR_1_24", "POI_LGNJR_1_28",
                              "POI_LGNJR_11_23", "POI_LGNJR_11_25", "POI_LGNJR_11_29",
                              "POI_LGNJR_11_31")
        require(all(all(witnesses[key][lang]["status"] == "resolved"
                        for lang in ("en", "ja", "ko", "zh-Hans"))
                    for key in selected_text_keys),
                "four-language holiday invitation and Echo response witnesses resolve", checks)
        require("worthy opponents" in witnesses["POI_LGNJR_1_19"]["en"]["content"] and
                "ruins and ancient buildings" in witnesses["POI_LGNJR_1_28"]["en"]["content"] and
                "nods in agreement" in witnesses["POI_LGNJR_11_25"]["en"]["content"] and
                "shakes its head" in witnesses["POI_LGNJR_11_29"]["en"]["content"] and
                "You want to return to Ragunna" in witnesses["POI_LGNJR_11_31"]["en"]["content"],
                "opponent redirection and two distinct Echo response signals retained", checks)
        cetus_action = json.loads(raw[5606]["Actions"])[3]
        cetus = cetus_action["Params"]
        require(cetus_action["Name"] == "ShowTalk" and
                len(cetus["TalkSequence"]) == 1 and len(cetus["TalkSequence"][0]) == 30 and
                not cetus["SequenceTransitions"],
                "Cetus exchange is one continuous source sequence", checks)
        require(all(cetus["TalkItems"][index]["WhoId"] == 1475 and
                    cetus["TalkItems"][index]["PlayVoice"]
                    for index in (11, 12, 20)) and
                all(cetus["TalkItems"][index]["WhoId"] == 1316 and
                    cetus["TalkItems"][index]["PlayVoice"]
                    for index in (16, 17, 19)) and
                [cetus["TalkItems"][i]["TidTalk"] for i in (11, 12, 16, 17, 19, 20)] ==
                ["DYHD_29_29", "DYHD_29_30", "DYHD_29_32", "DYHD_29_33",
                 "DYHD_29_35", "DYHD_29_36"],
                "Phoebe apology and acknowledgment are distinct from Abby's relay", checks)
        require("接受着大海的馈赠" in witnesses["DYHD_29_32"]["zh-Hans"]["content"] and
                "receiving gifts of the sea" in witnesses["DYHD_29_32"]["en"]["content"] and
                "바다의 선물을 받았" in witnesses["DYHD_29_32"]["ko"]["content"],
                "sea-gift receipt is grounded in three explicit language witnesses", checks)
        require("付出还是收获" in witnesses["DYHD_29_35"]["zh-Hans"]["content"] and
                "giving or receiving" in witnesses["DYHD_29_35"]["en"]["content"] and
                "捧げる時も、他人から受け取る時も" in witnesses["DYHD_29_35"]["ja"]["content"] and
                "주는 것이든 베푸는 것이든" in witnesses["DYHD_29_35"]["ko"]["content"],
                "giving-receiving contrast is localization-sensitive", checks)
        require("没办法代替修会" in witnesses["DYHD_29_29"]["zh-Hans"]["content"] and
                "no position to represent the Order" in witnesses["DYHD_29_29"]["en"]["content"] and
                "私一人の謝罪では償いにはなり得ません" in witnesses["DYHD_29_29"]["ja"]["content"],
                "personal apology retains Japanese recompense distinction", checks)
        line_rows = jsonl(voice / "COMPLETE_VOICE_LINE_ANALYSIS.jsonl")
        require(len(line_rows) == 476, "476 selected semantic voice rows", checks)
        sea_lines = [row for row in line_rows if
                     "/6587/Actions!/3/Params/TalkItems/" in row["source_locator"]]
        sea_renders = [render for row in sea_lines for render in row["renders"]]
        require(len(sea_lines) == 11 and len(sea_renders) == 44 and
                len({render["canonical_pcm_sha256"] for render in sea_renders}) == 44 and
                all({render["voice_language"] for render in row["renders"]} == LANGUAGES
                    for row in sea_lines) and
                all(render["materialization_status"] == "flac_roundtrip_pcm_identical" and
                    render.get("event_id") is None and
                    render.get("numeric_media_id") is None
                    for render in sea_renders),
                "sea inquiry has 11 source-joined lines and 44 distinct PCM-valid renders without invented numeric Wwise IDs",
                checks)
        civic_lines = [row for row in line_rows
                       if any(f"/{state}/Actions!/{action_index}/Params/TalkItems/" in row["source_locator"]
                              for state, (action_index, _, _) in civic_specs.items())]
        civic_renders = [render for row in civic_lines for render in row["renders"]]
        require(len(civic_lines) == 19 and len(civic_renders) == 76 and
                len({render["canonical_pcm_sha256"] for render in civic_renders}) == 76 and
                all({render["voice_language"] for render in row["renders"]} == LANGUAGES
                    for row in civic_lines) and
                all(render["materialization_status"] == "flac_roundtrip_pcm_identical" and
                    render.get("event_id") is None and render.get("bank_id") is None and
                    render.get("numeric_media_id") is None for render in civic_renders),
                "nineteen civic source lines join 76 distinct PCM-valid renders with null numeric Wwise IDs",
                checks)
        package = json.loads((source / "character_source_package.json").read_text(encoding="utf-8"))
        favor_words = package["favor_words"]
        archive_rows = [row for row in line_rows if row["record_class"] == "character_favor_archive"]
        archive_by_locator = {row["source_locator"]: row for row in archive_rows}
        require(len(favor_words) == len(archive_rows) == len(archive_by_locator) == 60,
                "60 distinct Phoebe source and voice archive locators", checks)
        language_map = {"en": "en", "ja": "ja", "ko": "ko", "zh-Hans": "zh"}
        require(all(
            word["raw"]["RoleId"] == 1506 and
            word["source_locator"] in archive_by_locator and
            word["raw"]["Content"] == archive_by_locator[word["source_locator"]]["text_key"] and
            word["raw"]["Voice"] and
            all(word["content"]["values"][source_lang]["content"] ==
                archive_by_locator[word["source_locator"]]["text_witnesses"][voice_lang]["content"]
                for source_lang, voice_lang in language_map.items())
            for word in favor_words
        ), "all 60 Phoebe rows join actual Content keys and four text witnesses", checks)
        require(all(
            row["technical_render_coverage_status"] == "complete" and
            {render["voice_language"] for render in row["renders"]} == LANGUAGES and
            len(row["renders"]) == 4 and
            all(render["event_path"] == word["raw"]["Voice"] and
                render["event_id"] is not None and render["bank_id"] is not None and
                render["numeric_media_id"] is not None and render["source_wem_exists"] and
                render["source_wem_sha256_verified"] and
                render["materialization_status"] == "flac_roundtrip_pcm_identical" and
                len(render["canonical_pcm_sha256"]) == 64
                for render in row["renders"])
            for word in favor_words
            for row in [archive_by_locator[word["source_locator"]]]
        ), "all 60 Phoebe events and 240 four-dub render chains resolve", checks)
        require(len({row["semantic_voice_occurrence_id"] for row in archive_rows}) == 60 and
                len({render["canonical_pcm_sha256"] for row in archive_rows
                     for render in row["renders"]}) == 240,
                "60 semantic archive occurrences and 240 distinct PCM hashes", checks)
        expected_mismatches = {
            150632: ("FavorWord_150634_Content", 1929, 2953016277),
            150633: ("FavorWord_150635_Content", 1930, 2953016278),
            150634: ("FavorWord_150636_Content", 1931, 3013562366),
            150635: ("FavorWord_150637_Content", 1932, 3013562365),
            150636: ("FavorWord_150632_Content", 1933, 2324455528),
            150637: ("FavorWord_150633_Content", 1934, 2324455531),
            150660: ("FavorWord_160719_Content", 2235, 1168224278),
        }
        mismatches = {
            word["raw"]["Id"]: word
            for word in favor_words
            if word["raw"]["Id"] != int(word["raw"]["Content"].split("_")[1])
        }
        require(set(mismatches) == set(expected_mismatches) and all(
            word["raw"]["Content"] == expected_mismatches[raw_id][0] and
            word["source_locator"].endswith(f"#/{expected_mismatches[raw_id][1]}") and
            {render["event_id"] for render in
             archive_by_locator[word["source_locator"]]["renders"]} ==
            {expected_mismatches[raw_id][2]}
            for raw_id, word in mismatches.items()
        ), "exact seven Phoebe raw-ID/Content-key permutations and event IDs", checks)
        combat_words = [word for word in favor_words
                        if 1927 <= int(word["source_locator"].rsplit("/", 1)[1]) <= 1956]
        require(len(combat_words) == 30 and
                len({render["canonical_pcm_sha256"] for word in combat_words
                     for render in archive_by_locator[word["source_locator"]]["renders"]}) == 120,
                "30 combat/system archive rows yield 120 distinct PCM objects inside full corpus", checks)
        by_index = {int(word["source_locator"].rsplit("/", 1)[1]):
                    archive_by_locator[word["source_locator"]] for word in favor_words}
        require(
            by_index[1931]["text_witnesses"]["en"]["content"] == "To the Sentinel." and
            by_index[1931]["text_witnesses"]["zh"]["content"] == "风的方向。" and
            by_index[1932]["text_witnesses"]["ko"]["content"] == "마법진으로!" and
            by_index[1936]["text_witnesses"]["en"]["content"] == "Bluebird, be my salvation." and
            by_index[1936]["text_witnesses"]["zh"]["content"] == "光明，予以祝颂！" and
            by_index[1945]["text_witnesses"]["en"]["content"] == "Pain is my penitence..." and
            "拯救" in by_index[1945]["text_witnesses"]["zh"]["content"] and
            by_index[1948]["text_witnesses"]["en"]["content"] == "I see the light... farewell." and
            "与你同在" in by_index[1948]["text_witnesses"]["zh"]["content"],
            "skill, liberation, injury and fall localization forks match pinned text", checks,
        )
        cantarella_source = source_root / "ANALYSIS" / "Characters" / "Cantarella"
        cantarella_voice = (source_root / "_voice_media" / "character" /
                           "complete_voice_corpus" / "Cantarella" / "v0_1")
        cantarella_package = json.loads(
            (cantarella_source / "character_source_package.json").read_text(encoding="utf-8")
        )
        cantarella_word = next(word for word in cantarella_package["favor_words"]
                               if word["source_locator"].endswith("favorword.json#/1976"))
        cantarella_row = next(row for row in jsonl(cantarella_voice / "COMPLETE_VOICE_LINE_ANALYSIS.jsonl")
                              if row["source_locator"] == cantarella_word["source_locator"])
        phoebe_greeting = by_index[2235]
        require(
            cantarella_word["raw"]["Id"] == 160719 and
            cantarella_word["raw"]["RoleId"] == 1607 and
            cantarella_word["raw"]["Content"] == phoebe_greeting["text_key"] ==
            "FavorWord_160719_Content" and
            cantarella_row["text_key"] == phoebe_greeting["text_key"] and
            cantarella_row["source_locator"] != phoebe_greeting["source_locator"] and
            cantarella_row["semantic_voice_occurrence_id"] !=
            phoebe_greeting["semantic_voice_occurrence_id"] and
            {render["event_id"] for render in cantarella_row["renders"]} == {3321153489} and
            {render["event_id"] for render in phoebe_greeting["renders"]} == {1168224278} and
            {render["canonical_pcm_sha256"] for render in cantarella_row["renders"]}.isdisjoint(
                {render["canonical_pcm_sha256"] for render in phoebe_greeting["renders"]}
            ),
            "Cantarella shared nonlexical key is a different role/event/occurrence/PCM", checks,
        )
        index = {(row["text_key"], row["semantic_voice_occurrence_id"]): row for row in line_rows}
        for case in cases["cases"]:
            row = index[(case["text_key"], case["semantic_voice_occurrence_id"])]
            require(case["source_locator"] == row["source_locator"], f"source locator: {case['text_key']}", checks)
            expected = {
                (render["runtime_render_variant_id"], render["canonical_pcm_sha256"], render["flac_sha256"])
                for render in row["renders"]
            }
            observed = {
                (render["render_variant_id"], render["canonical_pcm_sha256"], render["flac_sha256"])
                for render in case["renders"]
            }
            require(expected == observed, f"exact render join: {case['text_key']}", checks)
        outlier_targets = {
            "Main_Linaxita_2_1_8_4": ("5a126335d884b415f2432ebdecfa81726851280eed1c040f1136ac54acb9c4f6", "/4237/Actions!/3/Params/TalkItems/3"),
            "Main_Linaxita_2_1_8_7": ("b3c440253f3ef1cdd7377234ccfaf0a70ebdac475d854613b2399e5911ced583", "/4237/Actions!/3/Params/TalkItems/6"),
            "POI_JINKU_81_1": ("eb3ef8c3a09486a89b707d3512f99a872ceaa0d9d2b74210539b8569bf9c1379", "/5751/Actions!/1/Params/TalkItems/0"),
        }
        for key, (occurrence_hash, source_suffix) in outlier_targets.items():
            row = index[(key, f"voice-occurrence:{occurrence_hash}")]
            require(row["source_locator"].endswith(source_suffix)
                    and row["technical_speaker_id"] == 1475
                    and row["occurrence_identity_state"] == "solo_resolved_technical_id"
                    and len(row["renders"]) == 4
                    and {render["voice_language"] for render in row["renders"]} == LANGUAGES,
                    f"outlier nomination has exact Phoebe occurrence and four renders: {key}", checks)
        measurement_path = (source_root / "_research" / "character_packets" / "Phoebe" /
                            "audio_work" / "AUDIO_OBJECT_MEASUREMENTS.jsonl")
        require(hashlib.sha256(measurement_path.read_bytes()).hexdigest() ==
                "a98142724297161fa22cb22bde959d0c5195ba2fef6268816f113daaf74a5d29",
                "within-dub outlier screen retains pinned measurement table", checks)
        story_by_language: dict[str, list[dict]] = {language: [] for language in LANGUAGES}
        for measured in jsonl(measurement_path):
            if len(measured["voice_languages"]) != 1:
                continue
            language = measured["voice_languages"][0]
            if {proxy["record_class"] for proxy in measured["source_linked_rate_proxies"]} != {"story_dialogue"}:
                continue
            proxies = [proxy for proxy in measured["source_linked_rate_proxies"]
                       if proxy["voice_language"] == language]
            if len(proxies) == 1:
                story_by_language[language].append(measured)
        expected_story = {"en": (387, 5.520, -23.129), "ja": (387, 6.063, -21.957),
                          "ko": (386, 5.536, -23.822), "zh": (386, 5.235, -22.810)}
        for language, (count, duration, energy) in expected_story.items():
            rows = story_by_language[language]
            require(len(rows) == count
                    and abs(median(row["duration_seconds"] for row in rows) - duration) < 0.001
                    and abs(median(row["gates"]["-45"]["active_frame_energy_dbfs"]["median"]
                                   for row in rows) - energy) < 0.001,
                    f"within-dub story-only baseline: {language}", checks)
        audio = json.loads(summary.read_text(encoding="utf-8"))
        require(
            (audio["manifest_objects"], audio["measured_objects"], audio["repeated_pcm_manifest_rows"]) ==
            (1818, 1818, 4),
            "full local audio measurement counts", checks,
        )
        require(not audio["failed_objects"], "no local audio measurement failures", checks)
        result["source_crosscheck"] = "passed"
    result["result"] = "pass"
    result["check_count"] = len(checks)
    return result


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-root", type=Path, help="Extraction workspace for deeper local evidence crosscheck")
    parser.add_argument("--write-report", action="store_true")
    args = parser.parse_args()
    report = validate(args.source_root)
    if args.write_report:
        (packet_artifact(HERE, "VALIDATION_REPORT.json")).write_text(
            json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8", newline="\n"
        )
    print(json.dumps({key: report[key] for key in ("packet", "source_crosscheck", "result", "check_count")}, indent=2))


if __name__ == "__main__":
    main()
