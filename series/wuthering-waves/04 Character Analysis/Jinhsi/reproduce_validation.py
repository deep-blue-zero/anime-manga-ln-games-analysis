#!/usr/bin/env python3
"""Validate Jinhsi's draft structure and optional exact private-source joins.

This cannot establish literary truth, runtime branch reachability, human-heard
performance, or correctness of the unresolved origin-narration dispatch.
"""

from __future__ import annotations

import argparse
from collections import Counter
import json
from pathlib import Path
import re


HERE = Path(__file__).resolve().parent
PREFIX = "WUWA_JINHSI_"
COMMIT = "353f2eaed119bc9f680eab92807d20ac75a79b40"
LANGUAGES = {"en", "ja", "ko", "zh"}
MEDIA_SUFFIXES = {".wav", ".flac", ".wem", ".mp3", ".mp4", ".png", ".webp", ".pak"}


def read_jsonl(path: Path) -> list[dict]:
    with path.open(encoding="utf-8") as handle:
        return [json.loads(line) for line in handle if line.strip()]


def require(ok: bool, description: str, checks: list[str]) -> None:
    if not ok:
        raise AssertionError(description)
    checks.append(description)


def validate(source_root: Path | None) -> dict:
    checks: list[str] = []
    matrix = (HERE / f"{PREFIX}EVIDENCE_AND_FALSIFICATION_MATRIX.md").read_text(encoding="utf-8")
    evidence_ids = set(re.findall(r"\| (JIN-E\d{2}) \|", matrix))
    claim_ids = set(re.findall(r"\| (JIN-C\d{2}) —", matrix))
    require(evidence_ids == {f"JIN-E{index:02d}" for index in range(1, 44)},
            "43 contiguous evidence bundles", checks)
    require(claim_ids == {f"JIN-C{index:02d}" for index in range(1, 43)},
            "42 contiguous material claims", checks)
    require(not any(p.suffix.lower() in MEDIA_SUFFIXES for p in HERE.rglob("*") if p.is_file()),
            "no raw game media in Git packet", checks)
    expected = (
        "ANALYSIS_PACKET_README.md", "AV_AND_HUMAN_RETRIEVAL_PLAN.md",
        "AV_HUMAN_RETRIEVAL_CROSSWALK.md",
        "CHARACTER_DEEP_DIVE_PRE_AV.md", "EVIDENCE_AND_FALSIFICATION_MATRIX.md",
        "CIVIC_AUTHORITY_AND_HUMAN_SELF_RULE_PROFILE.md",
        "FIRST_ALLIANCE_CHOICE_AND_INFORMATION_ASYMMETRY_PROFILE.md",
        "TEMPORAL_BARGAIN_AND_THREE_PERSON_CHOICE_PROFILE.md",
        "PUBLIC_INVITATION_PRE_FIRMAMENT_AGENCY_AND_BATTLE_CHOICE_PROFILE.md",
        "XUANFANG_JURISDICTION_YANGYANG_CHOICE_AND_TRANSFER_PROFILE.md",
        "DISRUPTOR_AUTHORIZATION_RISK_AND_SHARED_ACTION_PROFILE.md",
        "SIMULATED_ECHO_AND_EXTERNAL_SOURCE_BOUNDARY_PROFILE.md",
        "PROMISE_FIELD_UNCERTAINTY_AND_PRESENCE_BOUNDARY_PROFILE.md",
        "JUE_ORIGIN_INFERENCE_RESEARCH_CARD_AND_DISCLOSURE_PROFILE.md",
        "CLAIM_REVISION_LEDGER.md",
        "MODEL_FIDELITY_AND_STRESS_TEST_PRE_AV.md",
        "RELATIONSHIP_STATE_AND_ORDINARY_LIFE_PROFILE.md",
        "ORDINARY_LIFE_PUBLIC_JOY_AND_REST_PROFILE.md",
        "SOURCE_CENSUS_CHRONOLOGY_AND_IDENTITY_AUDIT.md",
        "SPEECH_AND_MACHINE_VOICE_PROFILE_PRE_AV.md",
    )
    for suffix in expected:
        path = HERE / f"{PREFIX}{suffix}"
        body = path.read_text(encoding="utf-8")
        require(body.startswith("---\n") and "\nstatus: draft_noncurrent\n" in body,
                f"draft authority: {path.name}", checks)
        require("\ndo_not_use_as_current_authority: true\n" in body,
                f"noncurrent flag: {path.name}", checks)
        require(f"\nsource_commit: {COMMIT}\n" in body,
                f"source pin: {path.name}", checks)
    model = json.loads((HERE / f"{PREFIX}CHARACTER_MODEL_PACKAGE.json").read_text(encoding="utf-8"))
    require(model["authority"] == "draft_noncurrent" and model["source_commit"] == COMMIT,
            "model authority and source pin", checks)
    require(len(model["rules"]) == 17 and len({r["id"] for r in model["rules"]}) == 17,
            "17 distinct model rules", checks)
    require(all(set(rule["evidence_ids"]) <= evidence_ids for rule in model["rules"]),
            "all model evidence IDs resolve", checks)
    require(all(rule["probability"] is None for rule in model["rules"]),
            "no fabricated numerical rule probabilities", checks)
    probes = (HERE / f"{PREFIX}MODEL_FIDELITY_AND_STRESS_TEST_PRE_AV.md").read_text(encoding="utf-8")
    require(set(re.findall(r"\| (JIN-P\d{2}) \|", probes)) ==
            {f"JIN-P{index:02d}" for index in range(1, 48)},
            "47 contiguous non-blind probes", checks)
    require("JIN-P46" in probes and "player/piece" in probes and
            "player/piece" in model["rules"][1]["exceptions_and_limits"],
            "Changli/Jinhsi player-piece agency guard retained", checks)
    require("JIN-P47" in probes and "FavorWord_130429_Content" in probes and
            "JIN-E43" in model["rules"][8]["evidence_ids"] and
            "JIN-E43" in model["rules"][11]["evidence_ids"],
            "fate-versus-civic-agency probe and both model guards retained", checks)
    cases = json.loads((HERE / "AUDIO_MATCHED_SEMANTIC_CASES.json").read_text(encoding="utf-8"))
    require(cases["semantic_cases"] == 18 and len(cases["cases"]) == 18,
            "18 matched cases", checks)
    crosswalk = (HERE / f"{PREFIX}AV_HUMAN_RETRIEVAL_CROSSWALK.md").read_text(encoding="utf-8")
    require(all(f"`{case['text_key']}`" in crosswalk for case in cases["cases"]),
            "all 18 exact sound cases occur in AV crosswalk", checks)
    require(all(f"**JIN-AV-{n:02d} —" in crosswalk for n in range(1, 8)),
            "seven archive cases have individual retrieval capsules", checks)
    require("flow#/3722/0/1–8" in crosswalk and "runtime_dispatch_unsupported" in crosswalk,
            "unresolved narration is an explicit negative AV target", checks)
    require("JIN-R13" in crosswalk and "TZZNQ_7_16" in crosswalk
            and "Tethys-simulated" in crosswalk,
            "simulated-Echo and external-source AV target retained", checks)
    require(all(f"JIN-R{n:02d}" in crosswalk for n in range(14, 17))
            and all(key in crosswalk for key in
                    ("Huanglong_main_1_5_82_3", "Chengxiaoshan_main_1_1_290_5",
                     "Side_TZJNSC_2_6")),
            "promise, field uncertainty and replay AV targets retained", checks)
    require("JIN-R17" in crosswalk and "Flow_31000071_188" in crosswalk
            and "source-unvoiced" in crosswalk,
            "origin/card scene retained as negative-audio runtime target", checks)
    require(sum(len(case["renders"]) for case in cases["cases"]) == 72,
            "72 selected render variants", checks)
    require(sum(r["event_id"] is None and r["numeric_media_id"] is None
                for case in cases["cases"] for r in case["renders"]) == 44,
            "44 paired-null event and numeric-media mappings", checks)
    require(all({r["language"] for r in case["renders"]} == LANGUAGES for case in cases["cases"]),
            "each case has four dubs", checks)
    require(all(len(r[field]) == 64 for case in cases["cases"] for r in case["renders"]
                for field in ("wem_sha256", "canonical_pcm_sha256", "flac_sha256")),
            "selected render hashes present", checks)
    result = {"packet": "Jinhsi", "scope": "JINHSI_PINNED_3_6_0_TEXT_AUDIO_PRE_AV",
              "checks": checks, "source_crosscheck": "not_requested"}
    if source_root is not None:
        source = source_root / "ANALYSIS" / "Characters" / "Jinhsi"
        voice = source_root / "_voice_media" / "character" / "complete_voice_corpus" / "Jinhsi" / "v0_1"
        summary = source_root / "_research" / "character_packets" / "Jinhsi" / "audio_work" / "AUDIO_MEASUREMENT_SUMMARY.json"
        audit = json.loads((source / "COLLECTION_AUDIT.json").read_text(encoding="utf-8"))
        direct = audit["scopes"]["direct_character"]
        require(audit["valid"] and not direct["voice_completeness_valid"],
                "collection integrity valid; voice completeness explicitly false", checks)
        require((audit["raw_flow_states"], audit["context_text_keys"],
                 audit["quest_references"], audit["distinct_quest_ids"]) ==
                (185, 3465, 142, 44), "contextual collection denominator", checks)
        require((direct["candidate_occurrences"], direct["accepted_occurrences"],
                 direct["source_voiced"], direct["source_unvoiced"]) ==
                (617, 584, 472, 112), "direct occurrence denominator", checks)
        require((direct["semantic_voice_lines"], direct["complete_voice_lines"],
                 direct["missing_voice_lines"], direct["unresolved_reason_rows"]) ==
                (547, 539, 8, 32), "explicit eight-line/32-render voice gap", checks)
        require((direct["render_associations"], direct["runtime_object_rows"],
                 direct["unique_flac_objects"], direct["unique_flac_bytes"]) ==
                (2209, 2042, 2038, 526464066), "audio denominator and byte counts", checks)
        require(direct["unresolved_statuses"] == {"runtime_dispatch_unsupported": 32},
                "runtime dispatch status not collapsed into decode failure", checks)
        crosswalk = read_jsonl(source / "occurrence_identity_crosswalk.jsonl")
        require(Counter(r["character_attribution"] for r in crosswalk) ==
                {"accepted_solo": 584, "rejected": 33}, "identity crosswalk counts", checks)
        card_owned = [r for r in crosswalk if r["flow_state_row_index"] == 584
                      and r["action_index"] == 5]
        require(len(card_owned) == 15 and
                all(r["character_attribution"] == "accepted_solo" and
                    r["technical_speaker_id"] == 186 and not r["play_voice"]
                    for r in card_owned),
                "584 origin/card action has fifteen accepted source-unvoiced Jinhsi items", checks)
        simulated_owned = [r for r in crosswalk if r["flow_state_row_index"] == 7844
                           and r["action_index"] == 1 and r["character_attribution"] == "accepted_solo"]
        later_image_owned = [r for r in crosswalk if r["flow_state_row_index"] == 8329
                             and r["action_index"] == 1 and r["character_attribution"] == "accepted_solo"]
        require(len(simulated_owned) == 10 and sum(r["play_voice"] for r in simulated_owned) == 9
                and len(later_image_owned) == 7 and all(r["play_voice"] for r in later_image_owned),
                "simulated-image technical identity: ten plus seven accepted turns, one unvoiced", checks)
        hidden_changli_indices = {13, 16, 17, 18, 20, 22, 24, 26, 28, 33}
        interleaved_jinhsi_indices = {12, 14, 15, 19, 21, 23, 25, 27,
                                     29, 30, 31, 32, 34, 35}
        changli = [r for r in crosswalk if r["flow_state_row_index"] == 2516 and
                   r["action_index"] == 3 and r["talk_index"] in hidden_changli_indices]
        require(len(changli) == 10 and all(r["character_attribution"] == "rejected" for r in changli),
                "hidden Changli turns rejected from Jinhsi", checks)
        jinhsi_replies = [r for r in crosswalk if r["flow_state_row_index"] == 2516 and
                          r["action_index"] == 3 and r["talk_index"] in interleaved_jinhsi_indices]
        require(len(jinhsi_replies) == len(interleaved_jinhsi_indices) and
                all(r["character_attribution"] == "accepted_solo" for r in jinhsi_replies),
                "Jinhsi's interleaved replies retained", checks)
        ending_replies = [r for r in crosswalk if r["flow_state_row_index"] == 2516 and
                          r["action_index"] == 3 and r["talk_index"] in {40, 41}]
        require(len(ending_replies) == 2 and
                all(r["character_attribution"] == "accepted_solo" and
                    r["technical_speaker_id"] == 186 for r in ending_replies),
                "Jinhsi owns both closing player-piece replies", checks)
        messages = read_jsonl(source / "WAVESLINE_MESSAGES.jsonl")
        require(len(messages) == 3, "three message pointers inventoried", checks)
        witnesses = {row["text_key"]: row["values"] for row in
                     read_jsonl(source / "CONTEXT_TEXT_WITNESSES.jsonl")}
        player_piece = witnesses["Huanglong_main_1_5_83_41"]
        require("又有谁能分的清明" in player_piece["zh-Hans"]["content"] and
                "no difference" in player_piece["en"]["content"] and
                "誰が打ち手" in player_piece["ja"]["content"] and
                "바둑을 두는 자" in player_piece["ko"]["content"],
                "four-language player-piece uncertainty is not EN's invariant", checks)
        require("泰缇斯模拟" in witnesses["TZZNQ_7_9"]["zh-Hans"]["content"]
                and "记忆也模拟" in witnesses["TZZNQ_7_8"]["zh-Hans"]["content"]
                and witnesses["TZZNQ_7_16"]["zh-Hans"]["content"]
                != witnesses["Side_TZJNSC_2_3"]["zh-Hans"]["content"],
                "event text explicitly marks Tethys simulation and distinguishes stroll from introduction", checks)
        require(witnesses["Huanglong_main_1_5_79_33"]["en"]["content"] == "Count me in." and
                "time to think" in witnesses["Huanglong_main_1_5_79_34"]["en"]["content"] and
                witnesses["Huanglong_main_1_5_79_34"]["zh-Hans"]["content"] == "我考虑考虑。",
                "four-language option set includes join and consider, not refuse", checks)
        require("不想通过让你了解自己的过去" in
                witnesses["Huanglong_main_1_5_79_82"]["zh-Hans"]["content"] and
                "not feel obligated" in
                witnesses["Huanglong_main_1_5_79_82"]["en"]["content"] and
                "尘埃落定后" in
                witnesses["Huanglong_main_1_5_79_88"]["zh-Hans"]["content"],
                "nonbarter and postcrisis departure conditions retained", checks)
        public_choice = witnesses["HuanglongXZ_21_18"]
        require("选择自由" in public_choice["zh-Hans"]["content"] and
                "decide your course" in public_choice["en"]["content"] and
                "あなた自身の選択" in public_choice["ja"]["content"] and
                "선택은 당신의 자유" in public_choice["ko"]["content"],
                "four-language early public freedom promise retained", checks)
        prior_agency = witnesses["Huanglong_main_1_7_21_20"]
        require("不能总是习惯依赖于角的力量" in prior_agency["zh-Hans"]["content"] and
                "cannot sit back and wait" in prior_agency["en"]["content"] and
                "いつまでも" in prior_agency["ja"]["content"] and
                "항상" in prior_agency["ko"]["content"] and
                "实际性的援助" in witnesses["Huanglong_main_1_7_21_21"]["zh-Hans"]["content"],
                "pre-Firmament Jué-reliance wording and practical aid retained", checks)
        flow = {int(row["source_locator"].rsplit("/", 1)[1]): row["raw"]
                for row in read_jsonl(source / "RAW_RELEVANT_FLOW_STATES.jsonl")}
        counsel = json.loads(flow[2516]["Actions"])[3]["Params"]
        require(len(counsel["TalkItems"]) == 42 and
                counsel["TalkSequence"] == [list(range(1, 43))] and
                [counsel["TalkItems"][index]["WhoId"] for index in range(36, 42)] ==
                [999, 999, 999, 999, 186, 186] and
                [counsel["TalkItems"][index]["TidTalk"] for index in range(37, 42)] ==
                [f"Huanglong_main_1_5_83_{number}" for number in range(38, 43)],
                "single counsel sequence yields Changli move to Jinhsi's own response", checks)
        card_actions = json.loads(flow[584]["Actions"])
        card = card_actions[5]["Params"]
        card_items = card["TalkItems"]
        require(flow[584]["StateKey"] == "剧情_第四章_19_1" and
                card_actions[2]["Name"] == "BeginFlowTemplate" and
                card_actions[3]["Name"] == "SetFlowTemplate" and
                card_actions[5]["Name"] == "ShowTalk" and len(card_items) == 15 and
                all(item["WhoId"] == 186 for item in card_items) and
                [item["Id"] for item in card_items[:2]] == [1, 0] and
                not card.get("TalkSequence") and not card.get("SequenceTransitions"),
                "584 template and fifteen-item ShowTalk retain unsequenced source ordering", checks)
        card_options = card_items[12]["Options"]
        require([(option["TidTalkOption"], option["Actions"][0]["Name"],
                  option["Actions"][0]["Params"]["TalkId"])
                 for option in card_options] ==
                [("Flow_31000071_202", "JumpTalk", 13),
                 ("Flow_31000071_203", "JumpTalk", 14)] and
                [card_items[index]["TidTalk"] for index in (12, 13, 14)] ==
                ["Flow_31000071_201", "Flow_31000071_204", "Flow_31000071_205"] and
                all(not option.get("Actions", [])
                    for index in (0, 3, 6, 7)
                    for option in card_items[index]["Options"]),
                "584 explicit card permission/anxiety fork versus untargeted earlier options", checks)
        require("岁光" in witnesses["Flow_31000071_188"]["zh-Hans"]["content"] and
                "a Sentinel" in witnesses["Flow_31000071_188"]["en"]["content"] and
                "会不会" in witnesses["Flow_31000071_192"]["zh-Hans"]["content"] and
                "被破坏" in witnesses["Flow_31000071_199"]["zh-Hans"]["content"] and
                "资料卡" in witnesses["Flow_31000071_201"]["zh-Hans"]["content"] and
                all(witnesses[f"Flow_31000071_{n}"][lang]["status"] == "resolved"
                    for n in (188, 189, 191, 192, 197, 199, 201, 202, 203, 204, 205)
                    for lang in ("zh-Hans", "en", "ja", "ko")),
                "four-locale origin hypothesis and limited card witnesses retain uncertainty", checks)
        require(not any("剧情_第四章_19_1" == ref["state_key"]
                        for row in read_jsonl(source / "QUEST_CONTEXT_REFERENCES.jsonl")
                        for ref in row.get("matching_references", [])),
                "584 has no selected exact-state quest reference", checks)
        promise = json.loads(flow[2515]["Actions"])[3]["Params"]
        promise_items = promise["TalkItems"]
        require(len(promise_items) == 7
                and promise["TalkSequence"] == [list(range(1, 9))]
                and all(item["WhoId"] == 186 for item in promise_items)
                and [item["TidTalk"] for item in promise_items] ==
                [f"Huanglong_main_1_5_82_{n}" for n in (1, 3, 4, 5, 6, 7, 9)],
                "seven owned Jinhsi turns in one Black Shores/Jue promise sequence", checks)
        require("一定" in witnesses["Huanglong_main_1_5_82_3"]["zh-Hans"]["content"]
                and "よう" in witnesses["Huanglong_main_1_5_82_3"]["ja"]["content"]
                and "可能" in witnesses["Huanglong_main_1_5_82_4"]["zh-Hans"]["content"]
                and "所知" in witnesses["Huanglong_main_1_5_82_6"]["zh-Hans"]["content"]
                and "promise" in witnesses["Huanglong_main_1_5_82_7"]["en"]["content"],
                "promise locale witnesses retain inference, surveillance uncertainty and future disclosure", checks)
        chamber = json.loads(flow[3157]["Actions"])[2]["Params"]
        chamber_items = chamber["TalkItems"]
        require(len(chamber_items) == 7
                and chamber["TalkSequence"] == [list(range(1, 8))]
                and [item["WhoId"] for item in chamber_items] == [83] + [186] * 6
                and [item["TidTalk"] for item in chamber_items] ==
                [f"Chengxiaoshan_main_1_1_290_{n}" for n in (1, 2, 3, 5, 6, 7, 8)],
                "chamber approach retains six Jinhsi turns and one narrator ellipsis", checks)
        require("也许" in witnesses["Chengxiaoshan_main_1_1_290_5"]["zh-Hans"]["content"]
                and "or" in witnesses["Chengxiaoshan_main_1_1_290_5"]["en"]["content"]
                and "看不清" in witnesses["Chengxiaoshan_main_1_1_290_7"]["zh-Hans"]["content"]
                and "更多信息" in witnesses["Chengxiaoshan_main_1_1_290_8"]["zh-Hans"]["content"],
                "four-witness chamber text retains competing causes and information threshold", checks)
        reprise = json.loads(flow[7456]["Actions"])[2]["Params"]
        reprise_items = reprise["TalkItems"]
        first_meeting = json.loads(flow[1191]["Actions"])[3]["Params"]
        opening_options = first_meeting["TalkItems"][2]["Options"]
        require(len(reprise_items) == 8
                and reprise["TalkSequence"] == [list(range(1, 9))]
                and [item["WhoId"] for item in reprise_items] ==
                [186, 186, 186, 750088, 750088, 186, 186, 83]
                and [item["TidTalk"] for item in reprise_items] ==
                [f"Side_TZJNSC_2_{n}" for n in range(1, 9)],
                "memory-handbook reprise has five Jinhsi turns, two Rover turns and narration", checks)
        require([opening_options[i]["TidTalkOption"] for i in (0, 3)] ==
                ["Huanglong_main_1_5_79_4", "Huanglong_main_1_5_79_7"]
                and [opening_options[i]["Actions"][0]["Params"]["TalkId"]
                     for i in (0, 3)] == [8, 4]
                and [first_meeting["SequenceTransitions"]["0"][i]["NextSequenceIndex"]
                     for i in (0, 3)] == [2, 1]
                and witnesses["Side_TZJNSC_2_4"]["en"]["content"] == "Hello."
                and "projection" in witnesses["Side_TZJNSC_2_5"]["en"]["content"]
                and "real human in the flesh" in
                witnesses["Side_TZJNSC_2_6"]["en"]["content"],
                "side retelling linearizes mutually exclusive original hello/projection openings", checks)
        simulated_action = json.loads(flow[7844]["Actions"])[1]["Params"]
        require(simulated_action["TalkItems"][6]["WhoId"] == 83
                and simulated_action["TalkItems"][6]["TidTalk"] == "TZZNQ_7_8"
                and simulated_action["TalkItems"][7]["WhoId"] == 83
                and simulated_action["TalkItems"][7]["TidTalk"] == "TZZNQ_7_9"
                and simulated_action["TalkItems"][11]["WhoId"] == 186,
                "simulation claim is contextual narration, not an invented Jinhsi utterance", checks)
        broadcast = json.loads(flow[2948]["Actions"])[1]["Params"]
        require(len(broadcast["TalkSequence"]) == 1 and
                len(broadcast["TalkSequence"][0]) == 16 and
                broadcast["TalkItems"][14]["WhoId"] == 186 and
                broadcast["TalkItems"][14]["TidTalk"] == "HuanglongXZ_21_18" and
                broadcast["TalkItems"][15]["TidTalk"] == "HuanglongXZ_21_19",
                "citywide broadcast is one retained sequence with choice and civic-help lines", checks)
        broadcast_owned = [r for r in crosswalk if r["flow_state_row_index"] == 2948 and
                           r["action_index"] == 1 and r["character_attribution"] == "accepted_solo"]
        require(len(broadcast_owned) == 14 and all(r["play_voice"] for r in broadcast_owned),
                "14 accepted source-voiced Jinhsi broadcast occurrences", checks)
        defense = json.loads(flow[2301]["Actions"])[4]["Params"]
        defense_sequences = defense["TalkSequence"]
        require(len(defense_sequences) == 9 and
                defense_sequences[1:4] == [[17], [18, 19], [20]] and
                defense_sequences[4] == [21, 22, 23, 24, 25, 26] and
                [x["NextSequenceIndex"] for x in defense["SequenceTransitions"]["0"]] == [1, 2, 3] and
                all(defense["SequenceTransitions"][str(i)][0]["NextSequenceIndex"] == 4
                    for i in (1, 2, 3)),
                "Jinzhou defense has three exclusive replies and TalkID 21 rejoin", checks)
        require([defense["TalkItems"][i]["TidTalk"] for i in (11, 12, 17, 18, 19, 20, 21, 22)] ==
                ["Huanglong_main_1_7_21_20", "Huanglong_main_1_7_21_21",
                 "Huanglong_main_1_7_21_29", "Huanglong_main_1_7_21_30",
                 "Huanglong_main_1_7_21_31", "Huanglong_main_1_7_21_32",
                 "Huanglong_main_1_7_21_33", "Huanglong_main_1_7_21_34"] and
                all(defense["TalkItems"][i]["WhoId"] == 1212
                    for i in (11, 12, 17, 18, 19, 20, 21, 22)),
                "defense text keys and local Jinhsi technical speaker retained", checks)
        defense_owned = [r for r in crosswalk if r["flow_state_row_index"] == 2301 and
                         r["action_index"] == 4 and r["character_attribution"] == "accepted_solo"]
        require(len(defense_owned) == 16 and all(r["play_voice"] for r in defense_owned),
                "16 accepted source-voiced Jinhsi defense occurrences", checks)
        emergency = json.loads(flow[17181]["Actions"])[2]["Params"]
        emergency_items = emergency["TalkItems"]
        require(len(emergency["TalkSequence"]) == 1 and
                emergency["TalkSequence"][0] == list(range(1, 42)) and
                [emergency_items[i]["TidTalk"] for i in (19, 20, 31, 32, 39, 40)] ==
                ["Main_HuangLong_SYYLFML_110_28", "Main_HuangLong_SYYLFML_110_29",
                 "Main_HuangLong_SYYLFML_110_31", "Main_HuangLong_SYYLFML_110_67",
                 "Main_HuangLong_SYYLFML_110_53", "Main_HuangLong_SYYLFML_110_66"] and
                all(emergency_items[i]["WhoId"] == 186 for i in (19, 20, 31, 32, 39, 40)),
                "Xuanfang emergency keeps exact Jinhsi inquiry, jurisdiction, key and promise", checks)
        require("试图让夜归精锐再探" in witnesses["Main_HuangLong_SYYLFML_110_29"]["zh-Hans"]["content"] and
                "tried sending elite Midnight Rangers" in witnesses["Main_HuangLong_SYYLFML_110_29"]["en"]["content"] and
                "不得擅自干涉" in witnesses["Main_HuangLong_SYYLFML_110_31"]["zh-Hans"]["content"] and
                "not permitted to interfere" in witnesses["Main_HuangLong_SYYLFML_110_31"]["en"]["content"] and
                "个人身份前往" in witnesses["Main_HuangLong_SYYLFML_110_67"]["zh-Hans"]["content"] and
                "personal basis" in witnesses["Main_HuangLong_SYYLFML_110_67"]["en"]["content"],
                "attempted inquiry is distinct from military intervention and possible personal entry", checks)
        emergency_owned = [r for r in crosswalk if r["flow_state_row_index"] == 17181 and
                           r["action_index"] == 2 and r["character_attribution"] == "accepted_solo"]
        require(len(emergency_owned) == 18 and all(r["play_voice"] for r in emergency_owned),
                "18 accepted source-voiced Jinhsi emergency occurrences", checks)
        transfer = json.loads(flow[17636]["Actions"])[6]["Params"]
        transfer_items = transfer["TalkItems"]
        require(len(transfer["TalkSequence"]) == 1 and
                transfer["TalkSequence"][0] == list(range(1, 36)) and
                [transfer_items[i]["TidTalk"] for i in (6, 7, 13, 14, 15, 16, 17)] ==
                ["Main_HuangLong_XLZHDLY_480_39", "Main_HuangLong_XLZHDLY_480_40",
                 "Main_HuangLong_XLZHDLY_480_47", "Main_HuangLong_XLZHDLY_480_48",
                 "Main_HuangLong_XLZHDLY_480_49", "Main_HuangLong_XLZHDLY_480_50",
                 "Main_HuangLong_XLZHDLY_480_51"] and
                [transfer_items[i]["WhoId"] for i in (6, 7, 13, 14, 15, 16, 17)] ==
                [1212, 108, 1212, 350151, 350151, 108, 1212],
                "later Yangyang request, local Qiuhong assent and future Jiyan step retain speaker ownership", checks)
        require("尊重你的决定" in witnesses["Main_HuangLong_XLZHDLY_480_47"]["zh-Hans"]["content"] and
                "respect your decision" in witnesses["Main_HuangLong_XLZHDLY_480_47"]["en"]["content"] and
                "之后会同忌炎将军商议" in witnesses["Main_HuangLong_XLZHDLY_480_51"]["zh-Hans"]["content"] and
                "will speak with General Jiyan" in witnesses["Main_HuangLong_XLZHDLY_480_51"]["en"]["content"] and
                "相談して" in witnesses["Main_HuangLong_XLZHDLY_480_51"]["ja"]["content"] and
                "상의하여" in witnesses["Main_HuangLong_XLZHDLY_480_51"]["ko"]["content"],
                "four-language requested service and prospective consultation retained", checks)
        transfer_owned = [r for r in crosswalk if r["flow_state_row_index"] == 17636 and
                          r["action_index"] == 6 and r["character_attribution"] == "accepted_solo"]
        require(len(transfer_owned) == 10 and all(r["play_voice"] for r in transfer_owned),
                "10 accepted source-voiced Jinhsi transfer-conversation occurrences", checks)
        disruptor = json.loads(flow[1693]["Actions"])[3]
        disruptor_items = disruptor["Params"]["TalkItems"]
        require(disruptor["Name"] == "ShowTalk" and
                disruptor["Params"]["TalkSequence"] == [list(range(1, 19))] and
                len(disruptor_items) == 18 and
                [(disruptor_items[i]["WhoId"], disruptor_items[i]["TidTalk"])
                 for i in (8, 9, 10, 15)] ==
                [(1212, "Huanglong_main_1_7_49_9"),
                 (1212, "Huanglong_main_1_7_49_12"),
                 (1212, "Huanglong_main_1_7_49_13"),
                 (1212, "Huanglong_main_1_7_49_21")],
                "Disruptor permission, risk, outcome and support in one owned sequence", checks)
        require("争取到了" in witnesses["Huanglong_main_1_7_49_9"]["zh-Hans"]["content"] and
                "obtained the approval" in witnesses["Huanglong_main_1_7_49_9"]["en"]["content"] and
                "許可します" in witnesses["Huanglong_main_1_7_49_9"]["ja"]["content"] and
                "全权负责" in witnesses["Huanglong_main_1_7_49_12"]["zh-Hans"]["content"] and
                "一人承担" in witnesses["Huanglong_main_1_7_49_13"]["zh-Hans"]["content"] and
                "I alone will be accountable" in
                witnesses["Huanglong_main_1_7_49_13"]["en"]["content"] and
                "信じて" in witnesses["Huanglong_main_1_7_49_13"]["ja"]["content"] and
                "혼자" in witnesses["Huanglong_main_1_7_49_13"]["ko"]["content"],
                "four-language permission/accountability alignment retains JA trust split", checks)
        counsel_items = json.loads(flow[2516]["Actions"])[3]["Params"]["TalkItems"]
        require({i for i in range(12, 36) if counsel_items[i]["WhoId"] == 178} ==
                hidden_changli_indices and
                {i for i in range(12, 36) if counsel_items[i]["WhoId"] == 186} ==
                interleaved_jinhsi_indices and
                counsel_items[34]["TidTalk"] == "Huanglong_main_1_5_83_35",
                "mixed counsel scene preserves exact technical speakers and teacher address", checks)
        require("种子发芽" in witnesses[counsel_items[29]["TidTalk"]]["zh-Hans"]["content"] and
                "本心行事" in witnesses[counsel_items[32]["TidTalk"]]["zh-Hans"]["content"] and
                "独自前往" in witnesses[counsel_items[35]["TidTalk"]]["zh-Hans"]["content"] and
                "safest option" in witnesses[counsel_items[35]["TidTalk"]]["en"]["content"],
                "counsel and solo-decision localization hinge retained", checks)
        temporal = json.loads(flow[3160]["Actions"])[5]["Params"]["TalkItems"]
        require([(temporal[i]["WhoId"], temporal[i]["TidTalk"]) for i in
                 (26, 30, 41, 44, 51, 52, 53, 54)] ==
                [(1345, "Chengxiaoshan_main_1_1_380_30"),
                 (186, "Chengxiaoshan_main_1_1_380_34"),
                 (186, "Chengxiaoshan_main_1_1_380_45"),
                 (1345, "Chengxiaoshan_main_1_1_380_50"),
                 (1345, "Chengxiaoshan_main_1_1_380_59"),
                 (1345, "Chengxiaoshan_main_1_1_380_60"),
                 (1345, "Chengxiaoshan_main_1_1_380_61"),
                 (1345, "Chengxiaoshan_main_1_1_380_62")],
                "Jue suspension/warning/help and Jinhsi refusal/awakening ownership", checks)
        require("今州的时间暂停" in witnesses[temporal[26]["TidTalk"]]["zh-Hans"]["content"] and
                "无法遵从" in witnesses[temporal[30]["TidTalk"]]["zh-Hans"]["content"] and
                "二次共鸣" in witnesses[temporal[41]["TidTalk"]]["zh-Hans"]["content"] and
                "空壳" in witnesses[temporal[44]["TidTalk"]]["zh-Hans"]["content"],
                "competing temporal mechanisms and bodily danger stated", checks)
        chance = witnesses["Chengxiaoshan_main_1_1_380_59"]
        require("多上一成" in chance["zh-Hans"]["content"] and
                "by a fraction" in chance["en"]["content"] and
                "십분의 일" in chance["ko"]["content"] and
                chance["ja"]["content"] == "だが、そうでない時が訪れよう。" and
                "或可保下" in witnesses["Chengxiaoshan_main_1_1_380_60"]["zh-Hans"]["content"],
                "locale-specific possible increment, no absolute survival probability", checks)
        survival = json.loads(flow[3161]["Actions"])[3]["Params"]["TalkItems"]
        require(survival[11]["WhoId"] == 186 and
                survival[11]["TidTalk"] == "Chengxiaoshan_main_1_1_383_11" and
                "简简单单一死了之非我所愿" in witnesses[survival[11]["TidTalk"]]["zh-Hans"]["content"],
                "Jinhsi's explicit refusal of mere death retained", checks)
        gate = json.loads(flow[3163]["Actions"])[2]["Params"]
        gate_items = gate["TalkItems"]
        require(gate["TalkSequence"] == [list(range(1, 10)), [10], [11], list(range(12, 18))] and
                {option["Actions"][0]["Params"]["TalkId"]
                 for option in gate_items[8]["Options"]} == {10, 11} and
                [gate_items[i]["TidTalk"] for i in (9, 10, 11)] ==
                ["Chengxiaoshan_main_1_1_395_10",
                 "Chengxiaoshan_main_1_1_395_11",
                 "Chengxiaoshan_main_1_1_395_12"] and
                all(gate_items[i]["Actions"][0]["Params"]["TalkId"] == 12
                    for i in (9, 10)),
                "domain-gate alternatives have exclusive replies and common rejoin", checks)
        meeting = json.loads(flow[1191]["Actions"])[3]["Params"]
        items = meeting["TalkItems"]
        require(items[24]["TidTalk"] == "Huanglong_main_1_5_79_32" and
                {o["Actions"][0]["Params"]["TalkId"] for o in items[24]["Options"]} ==
                {24, 25} and
                [items[i]["TidTalk"] for i in (25, 26)] ==
                ["Huanglong_main_1_5_79_35", "Huanglong_main_1_5_79_36"] and
                all(items[i]["Actions"][0]["Params"]["TalkId"] == 26
                    for i in (25, 26)) and meeting["TalkSequence"][5][0] == 26,
                "first-alliance join/consider replies are exclusive and rejoin", checks)
        require(items[57]["TidTalk"] == "Huanglong_main_1_5_79_82" and
                items[62]["TidTalk"] == "Huanglong_main_1_5_79_88" and
                items[64]["TidTalk"] == "Huanglong_main_1_5_79_90" and
                not items[64].get("Options"),
                "nonbarter, conditioned departure and unanswered secrecy are shared", checks)
        later = json.loads(flow[2514]["Actions"])[6]["Params"]["TalkItems"]
        require(later[18]["TidTalk"] == "Huanglong_main_1_5_81_27" and
                later[26]["TidTalk"] == "Huanglong_main_1_5_81_38",
                "later Black Shores contact and limited-purpose testimony retained", checks)
        changli_meeting = json.loads(flow[3296]["Actions"])[4]["Params"]["TalkItems"]
        require(changli_meeting[6]["TidTalk"] == "Character_ChangLi_8_10" and
                changli_meeting[7]["TidTalk"] == "Character_ChangLi_8_69" and
                changli_meeting[9]["TidTalk"] == "Character_ChangLi_8_70" and
                "your idea" in witnesses["Character_ChangLi_8_10"]["en"]["content"] and
                "guessed" in witnesses["Character_ChangLi_8_69"]["en"]["content"],
                "cross-character token suggestion and apology retained without sole authorship", checks)
        unresolved = json.loads((source / "UNRESOLVED_VOICE_MEDIA.json").read_text(encoding="utf-8"))
        require(len(unresolved["installed_membership_rows"]) == 32,
                "32 installed membership rows retained but not called decoded", checks)
        lines = read_jsonl(voice / "COMPLETE_VOICE_LINE_ANALYSIS.jsonl")
        require(not any("/584/Actions!/5/Params/TalkItems/" in row["source_locator"]
                        for row in lines),
                "584 source-unvoiced action has no selected complete-voice render rows", checks)
        require(len(lines) == 547, "547 selected semantic voice rows", checks)
        alias_rows = [line for line in lines if len(line["renders"]) >= 4
                      and {render["voice_language"] for render in line["renders"]} == LANGUAGES
                      and len({render["canonical_pcm_sha256"] for render in line["renders"]}) == 1]
        require(len(alias_rows) == 31
                and all(len({render["source_virtual_path"] for render in line["renders"]}) == 1
                        and "/WwiseExternalSource/gl_vo_" in line["renders"][0]["source_virtual_path"]
                        for line in alias_rows),
                "31 four-label/single-WEM/PCM external-source lines", checks)
        basename_mismatch = [line for line in alias_rows
                             if line["renders"][0]["source_virtual_path"].rsplit("/", 1)[1]
                             != f"gl_vo_{line['text_key']}.wem"]
        require(len(basename_mismatch) == 4,
                "four event text keys disagree with external-source WEM basename", checks)
        event_pair = [line for line in alias_rows
                      if re.search(r"#/(7844|8329)/Actions!/1/Params/TalkItems/\d+$",
                                   line["source_locator"])]
        event_renders = [render for line in event_pair for render in line["renders"]]
        require(len(event_pair) == 16 and len(event_renders) == 64
                and len({render["canonical_pcm_sha256"] for render in event_renders}) == 14
                and all(render["materialization_status"] == "flac_roundtrip_pcm_identical"
                        for render in event_renders),
                "two event actions: 16 voiced lines, 64 associations, 14 distinct valid PCM", checks)
        event_by_key = {line["text_key"]: line for line in event_pair}
        require(event_by_key["TZZNQ_7_4"]["renders"][0]["source_virtual_path"].endswith(
                    "/gl_vo_TZZNQ_77_3.wem")
                and event_by_key["TZZNQ_7_16"]["renders"][0]["source_virtual_path"].endswith(
                    "/gl_vo_Side_TZJNSC_2_3.wem")
                and event_by_key["TZZNQ_7_17"]["renders"][0]["source_virtual_path"].endswith(
                    "/gl_vo_Side_TZJNSC_2_2.wem")
                and witnesses["TZZNQ_7_4"]["zh-Hans"]["content"]
                != witnesses["TZZNQ_77_3"]["zh-Hans"]["content"],
                "cake-plan/duty and stroll/introduction joins remain unproved", checks)
        for row_index, action_index, line_count, render_count, pcm_count in (
            (2515, 3, 7, 28, 28), (3157, 2, 6, 24, 24), (7456, 2, 5, 20, 5)
        ):
            scene_lines = [line for line in lines
                           if f"#/{row_index}/Actions!/{action_index}/Params/TalkItems/"
                           in line["source_locator"]]
            scene_renders = [render for line in scene_lines for render in line["renders"]]
            require(len(scene_lines) == line_count
                    and len(scene_renders) == render_count
                    and len({render["canonical_pcm_sha256"] for render in scene_renders})
                    == pcm_count
                    and all(render["materialization_status"] ==
                            "flac_roundtrip_pcm_identical" for render in scene_renders),
                    f"source-action voice/PCM denominator: {row_index}/{action_index}", checks)
            if row_index == 7456:
                require(all(len({render["canonical_pcm_sha256"] for render in line["renders"]}) == 1
                            and len({render["source_virtual_path"] for render in line["renders"]}) == 1
                            and line["renders"][0]["source_virtual_path"].endswith(
                                f"/gl_vo_{line['text_key']}.wem")
                            for line in scene_lines),
                        "five recap voice keys are four-label/single-PCM aliases", checks)
            else:
                require(all(len(line["renders"]) == 4
                            and len({render["canonical_pcm_sha256"] for render in line["renders"]}) == 4
                            and all(render["source_virtual_path"].endswith(
                                f"/{render['voice_language']}_vo_{line['text_key']}.wem")
                                for render in line["renders"])
                            for line in scene_lines),
                        f"four distinct localized key-matching objects: {row_index}/{action_index}",
                        checks)
        new_nominations = {
            "HuanglongXZ_21_18", "Huanglong_main_1_7_21_20", "Huanglong_main_1_7_21_21",
            "Huanglong_main_1_7_21_29", "Huanglong_main_1_7_21_30",
            "Huanglong_main_1_7_21_31", "Huanglong_main_1_7_21_32",
            "Main_HuangLong_SYYLFML_110_29", "Main_HuangLong_SYYLFML_110_31",
            "Main_HuangLong_SYYLFML_110_53", "Main_HuangLong_SYYLFML_110_67",
            "Main_HuangLong_XLZHDLY_480_39", "Main_HuangLong_XLZHDLY_480_47",
            "Main_HuangLong_XLZHDLY_480_51",
            "Huanglong_main_1_7_49_9", "Huanglong_main_1_7_49_12",
            "Huanglong_main_1_7_49_13", "Huanglong_main_1_7_49_21",
        }
        nominated_rows = [line for line in lines if line["text_key"] in new_nominations]
        require(len(nominated_rows) == len(new_nominations) and
                {line["text_key"] for line in nominated_rows} == new_nominations and
                all(len(line["renders"]) == 4 for line in nominated_rows),
                "new public/defense/Xuanfang/Disruptor AV nominations have exact four-dub source joins", checks)
        disruptor_rows = [line for line in nominated_rows
                          if line["text_key"].startswith("Huanglong_main_1_7_49_")]
        require(len(disruptor_rows) == 4 and
                all("/1693/Actions!/3/Params/TalkItems/" in line["source_locator"] and
                    all(render.get("event_id") is None and
                        render.get("numeric_media_id") is None and
                        render["source_virtual_path"].endswith(
                            f"/{render['voice_language']}_vo_{line['text_key']}.wem") and
                        render["source_wem_sha256_verified"] and
                        render["materialization_status"] ==
                        "flac_roundtrip_pcm_identical" for render in line["renders"])
                    for line in disruptor_rows),
                "four Disruptor lines retain 16 PCM-valid external-source renders with paired null IDs",
                checks)
        index = {(r["text_key"], r["semantic_voice_occurrence_id"]): r for r in lines}
        package = json.loads((source / "character_source_package.json").read_text(encoding="utf-8"))
        favor_by_id = {word["id"]: word for word in package["favor_words"]}
        archive_positions = {130401: 1224, 130405: 1228, 130408: 1231,
                             130410: 1233, 130414: 1237, 130418: 1241,
                             130428: 1251}
        archive_cases = {case["text_key"]: case for case in cases["cases"]
                         if case["record_class"] == "character_favor_archive"}
        require(set(archive_cases) == {f"FavorWord_{word_id}_Content"
                                       for word_id in archive_positions},
                "seven exact archive text keys selected", checks)
        for word_id, position in archive_positions.items():
            word = favor_by_id[word_id]
            case = archive_cases[f"FavorWord_{word_id}_Content"]
            row = index[(case["text_key"], case["semantic_voice_occurrence_id"])]
            expected_locator = (f"wuwa://{COMMIT}/BinData/favor/favorword.json#/"
                                f"{position}")
            require(word["source_locator"] == case["source_locator"] ==
                    row["source_locator"] == expected_locator and
                    word["raw"]["Content"] == case["text_key"] and
                    word["voice_asset"].startswith("/Game/Aki/WwiseAudio/Events/") and
                    all(r["event_id"] is not None and r["numeric_media_id"] is not None
                        for r in case["renders"]),
                    f"raw archive row, event path and numeric media: {word_id}", checks)
            require(all(word["content"]["values"]["zh-Hans" if lang == "zh" else lang]
                        ["content"] == row["text_witnesses"][lang]["content"] and
                        row["text_witnesses"][lang]["content_sha256"] ==
                        case["text_witness_sha256"][lang] for lang in LANGUAGES),
                    f"four pinned archive text witnesses: {word_id}", checks)
        civic = favor_by_id[130410]["content"]["values"]
        fate_word = favor_by_id[130429]
        fate = fate_word["content"]["values"]
        require("属于人类自己的道路" in civic["zh-Hans"]["content"] and
                "偶尔相信一次命运也不错" in fate["zh-Hans"]["content"] and
                "once believed" in fate["en"]["content"] and
                "power of fate" in fate["en"]["content"] and
                "出会えたこの「運命」" in fate["ja"]["content"] and
                "한 번쯤은" in fate["ko"]["content"],
                "four-language human-road versus encounter-fate wording", checks)
        fate_rows = [line for line in lines if line["text_key"] == "FavorWord_130429_Content"]
        require(len(fate_rows) == 1 and fate_word["id"] == 130429 and
                fate_word["raw"]["Content"] == "FavorWord_130429_Content" and
                fate_word["source_locator"] ==
                f"wuwa://{COMMIT}/BinData/favor/favorword.json#/1252" and
                fate_rows[0]["source_locator"] == fate_word["source_locator"] and
                all(fate["zh-Hans" if language == "zh" else language]["content"] ==
                    fate_rows[0]["text_witnesses"][language]["content"]
                    for language in LANGUAGES),
                "Ascension V exact row and four localized text joins", checks)
        fate_renders = fate_rows[0]["renders"]
        require(len(fate_renders) == 4 and
                {(r["voice_language"], r["numeric_media_id"]) for r in fate_renders} ==
                {("en", 314613510), ("ja", 844083088),
                 ("ko", 537313558), ("zh", 267182053)} and
                {r["event_id"] for r in fate_renders} == {494967523} and
                {r["event_path"] for r in fate_renders} == {fate_word["voice_asset"]} and
                len({r["canonical_pcm_sha256"] for r in fate_renders}) == 4 and
                all(r["materialization_status"] == "flac_roundtrip_pcm_identical"
                    for r in fate_renders),
                "Ascension V event/media and four distinct PCM-valid render joins", checks)
        birthday = archive_cases["FavorWord_130418_Content"]
        birthday_en = next(r for r in birthday["renders"] if r["language"] == "en")
        require("long_object_check_subtitle_extent" in birthday_en["qc_flags"] and
                round(birthday_en["duration_seconds"], 2) == 41.65,
                "EN birthday extent flag retained as unresolved human check", checks)
        for case in cases["cases"]:
            row = index[(case["text_key"], case["semantic_voice_occurrence_id"])]
            require(case["source_locator"] == row["source_locator"],
                    f"source locator: {case['text_key']}", checks)
            require(all(row["text_witnesses"][lang]["status"] == "resolved" for lang in LANGUAGES),
                    f"text witnesses resolved: {case['text_key']}", checks)
            expected_renders = {(r["runtime_render_variant_id"], r["canonical_pcm_sha256"],
                                 r["flac_sha256"]) for r in row["renders"]}
            observed_renders = {(r["render_variant_id"], r["canonical_pcm_sha256"],
                                 r["flac_sha256"]) for r in case["renders"]}
            require(expected_renders == observed_renders,
                    f"exact render join: {case['text_key']}", checks)
        audio = json.loads(summary.read_text(encoding="utf-8"))
        require((audio["manifest_objects"], audio["measured_objects"],
                 audio["repeated_pcm_manifest_rows"]) == (2038, 2038, 4),
                "local measured-object counts", checks)
        require(not audio["failed_objects"] and not audio["human_perceptual_review_performed"],
                "zero local measurement failures; no human listening implied", checks)
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
        (HERE / "VALIDATION_REPORT.json").write_text(
            json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8", newline="\n")
    print(json.dumps({k: report[k] for k in
                      ("packet", "source_crosscheck", "result", "check_count")}, indent=2))


if __name__ == "__main__":
    main()
