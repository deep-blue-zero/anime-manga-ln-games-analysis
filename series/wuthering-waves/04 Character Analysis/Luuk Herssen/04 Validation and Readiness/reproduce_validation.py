#!/usr/bin/env python3
"""Validate Luuk Herssen's noncurrent draft and optional private-source joins.

This verifies structure, attribution denominators, selected multilingual/media
joins and a known localization conflict. It cannot score literary truth,
runtime branch reachability, visual acting or human-heard voice quality.
"""

from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import re


HERE = Path(__file__).resolve().parent.parent
NAME = "Luuk Herssen"
PREFIX = "WUWA_LUUK_HERSSEN_"
COMMIT = "353f2eaed119bc9f680eab92807d20ac75a79b40"
LANGUAGES = {"en", "ja", "ko", "zh"}
MEDIA_SUFFIXES = {".wav", ".flac", ".wem", ".mp3", ".mp4", ".png", ".webp", ".pak"}




# Exact character-root-relative paths after the artifact-class migration.
PACKET_ARTIFACT_PATHS = {'AUDIO_MATCHED_SEMANTIC_CASES.json': '03 Audiovisual and Voice/AUDIO_MATCHED_SEMANTIC_CASES.json', 'CHARACTER_VISUAL_DESIGN_PROFILE.json': '03 Audiovisual and Voice/CHARACTER_VISUAL_DESIGN_PROFILE.json', 'CHARACTER_VISUAL_DESIGN_PROFILE.md': '03 Audiovisual and Voice/CHARACTER_VISUAL_DESIGN_PROFILE.md', 'CHARACTER_VISUAL_REFERENCE_MANIFEST.json': '03 Audiovisual and Voice/CHARACTER_VISUAL_REFERENCE_MANIFEST.json', 'VALIDATION_REPORT.json': '04 Validation and Readiness/VALIDATION_REPORT.json', 'WUWA_LUUK_HERSSEN_ANALYSIS_PACKET_README.md': 'WUWA_LUUK_HERSSEN_ANALYSIS_PACKET_README.md', 'WUWA_LUUK_HERSSEN_ASCENSION_PAIN_DUTY_AND_ALLIANCE_PROFILE.md': '01 Evidence and Source-Facing/WUWA_LUUK_HERSSEN_ASCENSION_PAIN_DUTY_AND_ALLIANCE_PROFILE.md', 'WUWA_LUUK_HERSSEN_AUDIO_QC_AND_COMPARABILITY_AUDIT.md': '04 Validation and Readiness/WUWA_LUUK_HERSSEN_AUDIO_QC_AND_COMPARABILITY_AUDIT.md', 'WUWA_LUUK_HERSSEN_AV_AND_HUMAN_RETRIEVAL_PLAN.md': '03 Audiovisual and Voice/WUWA_LUUK_HERSSEN_AV_AND_HUMAN_RETRIEVAL_PLAN.md', 'WUWA_LUUK_HERSSEN_AV_HUMAN_RETRIEVAL_CROSSWALK.md': '03 Audiovisual and Voice/WUWA_LUUK_HERSSEN_AV_HUMAN_RETRIEVAL_CROSSWALK.md', 'WUWA_LUUK_HERSSEN_BESIDE_NOT_OBSERVER_CAT_ADOPTION_AND_RECIPROCAL_REST_PROFILE.md': '01 Evidence and Source-Facing/WUWA_LUUK_HERSSEN_BESIDE_NOT_OBSERVER_CAT_ADOPTION_AND_RECIPROCAL_REST_PROFILE.md', 'WUWA_LUUK_HERSSEN_CHARACTER_DEEP_DIVE_PRE_AV.md': '01 Evidence and Source-Facing/WUWA_LUUK_HERSSEN_CHARACTER_DEEP_DIVE_PRE_AV.md', 'WUWA_LUUK_HERSSEN_CHARACTER_MODEL_PACKAGE.json': '02 Reconstruction/WUWA_LUUK_HERSSEN_CHARACTER_MODEL_PACKAGE.json', 'WUWA_LUUK_HERSSEN_CLAIM_REVISION_LEDGER.md': '04 Validation and Readiness/WUWA_LUUK_HERSSEN_CLAIM_REVISION_LEDGER.md', 'WUWA_LUUK_HERSSEN_COMBAT_SURGICAL_LANGUAGE_AND_ARCHIVE_KEY_PROFILE.md': '01 Evidence and Source-Facing/WUWA_LUUK_HERSSEN_COMBAT_SURGICAL_LANGUAGE_AND_ARCHIVE_KEY_PROFILE.md', 'WUWA_LUUK_HERSSEN_EVIDENCE_AND_FALSIFICATION_MATRIX.md': '01 Evidence and Source-Facing/WUWA_LUUK_HERSSEN_EVIDENCE_AND_FALSIFICATION_MATRIX.md', 'WUWA_LUUK_HERSSEN_EXOSTRIDER_AUTHORIZATION_SECURE_CONTACT_AND_RISK_COUNSEL_PROFILE.md': '01 Evidence and Source-Facing/WUWA_LUUK_HERSSEN_EXOSTRIDER_AUTHORIZATION_SECURE_CONTACT_AND_RISK_COUNSEL_PROFILE.md', 'WUWA_LUUK_HERSSEN_INHERITED_HARM_RHEIN_AND_REPAIR_PROFILE.md': '01 Evidence and Source-Facing/WUWA_LUUK_HERSSEN_INHERITED_HARM_RHEIN_AND_REPAIR_PROFILE.md', 'WUWA_LUUK_HERSSEN_LUCILLA_ACADEMY_TRUST_STUDENT_HOPE_AND_NIVORA_PURSUIT_PROFILE.md': '01 Evidence and Source-Facing/WUWA_LUUK_HERSSEN_LUCILLA_ACADEMY_TRUST_STUDENT_HOPE_AND_NIVORA_PURSUIT_PROFILE.md', 'WUWA_LUUK_HERSSEN_MEDICAL_INFERENCE_SECRECY_AND_AUTONOMY_PROFILE.md': '01 Evidence and Source-Facing/WUWA_LUUK_HERSSEN_MEDICAL_INFERENCE_SECRECY_AND_AUTONOMY_PROFILE.md', 'WUWA_LUUK_HERSSEN_MODEL_FIDELITY_AND_STRESS_TEST_PRE_AV.md': '04 Validation and Readiness/WUWA_LUUK_HERSSEN_MODEL_FIDELITY_AND_STRESS_TEST_PRE_AV.md', 'WUWA_LUUK_HERSSEN_ORDINARY_LIFE_FOOD_REST_AND_MUTUAL_LIMITS_PROFILE.md': '01 Evidence and Source-Facing/WUWA_LUUK_HERSSEN_ORDINARY_LIFE_FOOD_REST_AND_MUTUAL_LIMITS_PROFILE.md', 'WUWA_LUUK_HERSSEN_RECONSTRUCTIVE_PROFILE_PRE_AV.md': '02 Reconstruction/WUWA_LUUK_HERSSEN_RECONSTRUCTIVE_PROFILE_PRE_AV.md', 'WUWA_LUUK_HERSSEN_RELATIONSHIP_STATE_AND_ORDINARY_LIFE_PROFILE.md': '01 Evidence and Source-Facing/WUWA_LUUK_HERSSEN_RELATIONSHIP_STATE_AND_ORDINARY_LIFE_PROFILE.md', 'WUWA_LUUK_HERSSEN_SOURCE_CENSUS_CHRONOLOGY_AND_IDENTITY_AUDIT.md': '04 Validation and Readiness/WUWA_LUUK_HERSSEN_SOURCE_CENSUS_CHRONOLOGY_AND_IDENTITY_AUDIT.md', 'WUWA_LUUK_HERSSEN_SOURCE_DEFINED_AUDIO_COHORT_AUDIT.md': '04 Validation and Readiness/WUWA_LUUK_HERSSEN_SOURCE_DEFINED_AUDIO_COHORT_AUDIT.md', 'WUWA_LUUK_HERSSEN_SPEECH_AND_MACHINE_VOICE_PROFILE_PRE_AV.md': '03 Audiovisual and Voice/WUWA_LUUK_HERSSEN_SPEECH_AND_MACHINE_VOICE_PROFILE_PRE_AV.md', 'reproduce_validation.py': '04 Validation and Readiness/reproduce_validation.py'}

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
    matrix = (packet_artifact(HERE, f"{PREFIX}EVIDENCE_AND_FALSIFICATION_MATRIX.md")).read_text(encoding="utf-8")
    evidence_ids = set(re.findall(r"\| (LUK-E\d{2}) \|", matrix))
    claim_ids = set(re.findall(r"\| (LUK-C\d{2}) —", matrix))
    require(len(evidence_ids) == 41, "41 unique evidence bundles", checks)
    require(len(claim_ids) == 40, "40 unique claim rows", checks)
    require(not any(path.suffix.lower() in MEDIA_SUFFIXES for path in HERE.rglob("*") if path.is_file()),
            "no raw media in Git packet", checks)
    expected_files = {
        "ANALYSIS_PACKET_README.md", "AV_AND_HUMAN_RETRIEVAL_PLAN.md",
        "AUDIO_QC_AND_COMPARABILITY_AUDIT.md",
        "SOURCE_DEFINED_AUDIO_COHORT_AUDIT.md",
        "CLAIM_REVISION_LEDGER.md",
        "ASCENSION_PAIN_DUTY_AND_ALLIANCE_PROFILE.md",
        "COMBAT_SURGICAL_LANGUAGE_AND_ARCHIVE_KEY_PROFILE.md",
        "LUCILLA_ACADEMY_TRUST_STUDENT_HOPE_AND_NIVORA_PURSUIT_PROFILE.md",
        "EXOSTRIDER_AUTHORIZATION_SECURE_CONTACT_AND_RISK_COUNSEL_PROFILE.md",
        "BESIDE_NOT_OBSERVER_CAT_ADOPTION_AND_RECIPROCAL_REST_PROFILE.md",
        "CHARACTER_DEEP_DIVE_PRE_AV.md", "EVIDENCE_AND_FALSIFICATION_MATRIX.md",
        "INHERITED_HARM_RHEIN_AND_REPAIR_PROFILE.md",
        "MEDICAL_INFERENCE_SECRECY_AND_AUTONOMY_PROFILE.md",
        "MODEL_FIDELITY_AND_STRESS_TEST_PRE_AV.md",
        "ORDINARY_LIFE_FOOD_REST_AND_MUTUAL_LIMITS_PROFILE.md",
        "RECONSTRUCTIVE_PROFILE_PRE_AV.md",
        "RELATIONSHIP_STATE_AND_ORDINARY_LIFE_PROFILE.md",
        "SOURCE_CENSUS_CHRONOLOGY_AND_IDENTITY_AUDIT.md",
        "SPEECH_AND_MACHINE_VOICE_PROFILE_PRE_AV.md",
    }
    for suffix in expected_files:
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
    rules = model["rules"]
    require(len(rules) == 19 and len({rule["id"] for rule in rules}) == 19,
            "19 distinct model rules", checks)
    require(all(set(rule["evidence_ids"]) <= evidence_ids for rule in rules),
            "all model evidence IDs resolve", checks)
    require(all(rule["probability"] is None for rule in rules),
            "no fabricated numerical probabilities", checks)
    probes = (packet_artifact(HERE, f"{PREFIX}MODEL_FIDELITY_AND_STRESS_TEST_PRE_AV.md")).read_text(encoding="utf-8")
    require(len(set(re.findall(r"\| (LUK-P\d{2}) \|", probes))) == 48,
            "48 non-blind probes", checks)
    require("## Ten interaction tests" in probes and
            "**A combat bark beside a real patient" in probes and all(
                f"R{number:02d}" in probes for number in range(1, 20)),
            "ten interaction tests and nineteen-rule challenge map", checks)
    cases = json.loads((packet_artifact(HERE, "AUDIO_MATCHED_SEMANTIC_CASES.json")).read_text(encoding="utf-8"))
    require(cases["semantic_cases"] == 20 and len(cases["cases"]) == 20,
            "20 matched semantic cases", checks)
    crosswalk = (packet_artifact(HERE, "WUWA_LUUK_HERSSEN_AV_HUMAN_RETRIEVAL_CROSSWALK.md")).read_text(encoding="utf-8")
    require(all(f"`{case['text_key']}`" in crosswalk for case in cases["cases"]),
            "all 20 exact sound cases occur in AV crosswalk", checks)
    require("generic-ID" in crosswalk and "message text" in crosswalk,
            "identity and message-medium controls in AV crosswalk", checks)
    require("LUK-R08" in crosswalk and "MAIN_RGLC_40_41" in crosswalk,
            "exact Academy audience and emergency retrieval control", checks)
    require(set(re.findall(r"\| (LUK-R\d{2}) \|", crosswalk)) ==
            {f"LUK-R{number:02d}" for number in range(1, 12)} and
            "Zuoyequnxing_50_19" in crosswalk and "Zuoyequnxing_52_41" in crosswalk,
            "eleven exact runtime controls include both Chapter 3.3 actions and companion scene", checks)
    require(sum(len(case["renders"]) for case in cases["cases"]) == 80,
            "80 selected render variants", checks)
    require(all({render["language"] for render in case["renders"]} == LANGUAGES
                for case in cases["cases"]), "each case has four dubs", checks)
    require(all(len(render[name]) == 64 for case in cases["cases"] for render in case["renders"]
                for name in ("wem_sha256", "canonical_pcm_sha256", "flac_sha256")),
            "selected render hashes present", checks)
    render_rows = [render for case in cases["cases"] for render in case["renders"]]
    require(sum(render["event_id"] is None and render["numeric_media_id"] is None
                for render in render_rows) == 40
            and all((render["event_id"] is None) == (render["numeric_media_id"] is None)
                    for render in render_rows),
            "40/80 paired null event and numeric-media IDs preserved", checks)
    waffle_cases = {case["text_key"]: case for case in cases["cases"]
                    if case["text_key"].startswith("Side_LHSCP_2_")}
    require(set(waffle_cases) == {f"Side_LHSCP_2_{suffix}" for suffix in range(9, 15)}
            and all(waffle_cases[f"Side_LHSCP_2_{suffix}"]["source_locator"].endswith(
                f"/15461/Actions!/5/Params/TalkItems/{suffix - 3}")
                    for suffix in range(9, 15)),
            "six waffle cases retain exact mutually exclusive source positions", checks)
    result = {"packet": NAME, "scope": "LUUK_HERSSEN_PINNED_3_6_0_TEXT_AUDIO_PRE_AV",
              "checks": checks, "source_crosscheck": "not_requested"}
    if source_root is not None:
        source = source_root / "ANALYSIS" / "Characters" / NAME
        voice = source_root / "_voice_media" / "character" / "complete_voice_corpus" / NAME / "v0_1"
        summary = source_root / "_research" / "character_packets" / NAME / "audio_work" / "AUDIO_MEASUREMENT_SUMMARY.json"
        audit = json.loads((source / "COLLECTION_AUDIT.json").read_text(encoding="utf-8"))
        direct = audit["scopes"]["direct_character"]
        require(audit["valid"] and direct["voice_completeness_valid"],
                "selected collection audit valid", checks)
        require((audit["raw_flow_states"], audit["context_text_keys"],
                 audit["quest_references"], audit["distinct_quest_ids"]) ==
                (179, 2429, 68, 21), "contextual collection denominator", checks)
        require((direct["candidate_occurrences"], direct["accepted_occurrences"],
                 direct["source_voiced"], direct["source_unvoiced"]) ==
                (834, 830, 642, 188), "direct occurrence denominator", checks)
        require((direct["semantic_voice_lines"], direct["render_associations"],
                 direct["runtime_object_rows"], direct["unique_flac_objects"]) ==
                (719, 2889, 2863, 2855), "voice line, association, object denominators", checks)
        decisions = jsonl(source / "occurrence_identity_crosswalk.jsonl")
        require(Counter(row["character_attribution"] for row in decisions) ==
                {"accepted_solo": 830, "unresolved": 4}, "identity crosswalk counts", checks)
        generic = [row for row in decisions if row["flow_state_row_index"] == 10719
                   and row["talk_index"] in (1, 2)]
        require(len(generic) == 2 and all(row["character_attribution"] == "accepted_solo"
                                           for row in generic),
                "two exact unnamed doctor occurrences accepted", checks)
        unknown = [row for row in decisions if row["flow_state_row_index"] == 15064
                   and row["talk_index"] in (14, 15, 16, 17)]
        require(len(unknown) == 4 and all(row["character_attribution"] == "unresolved"
                                           for row in unknown),
                "four anonymous adjacent narration occurrences unresolved", checks)
        messages = jsonl(source / "WAVESLINE_MESSAGES.jsonl")
        require(len(messages) == 11 and all(row["content_extraction_status"] == "metadata_only_scope"
                                             and row["state_found"] for row in messages),
                "eleven message metadata pointers target linked flow states", checks)
        package = json.loads((source / "character_source_package.json").read_text(encoding="utf-8"))
        story = next(row for row in package["favor_stories"]
                     if row["content"]["text_key"] == "FavorStory_151004_Content")
        values = story["content"]["values"]
        require("绝大部分" in values["zh-Hans"]["content"]
                and "Without exception" in values["en"]["content"],
                "Chinese/English Ichor-outcome scope conflict preserved", checks)
        ascension = [row for row in package["favor_words"]
                     if row["content"]["text_key"] in
                     {f"FavorWord_1510{suffix}_Content" for suffix in range(27, 32)}]
        require(len(ascension) == 5 and [row["id"] for row in ascension] ==
                list(range(151027, 151032)),
                "five source-ordered Luuk ascension entries", checks)
        require(all(row["source_locator"].endswith(f"/favorword.json#/{3179 + offset}")
                    and row["voice_asset"].endswith(
                        f"rankup0{offset + 1}.play_favor_word_luhesi_sys_rankup0{offset + 1}")
                    for offset, row in enumerate(ascension)),
                "five exact rank-up source rows and event paths", checks)
        require("力量并非只属于厮杀" in ascension[1]["content"]["values"]["zh-Hans"]["content"]
                and "殺す" in ascension[1]["content"]["values"]["ja"]["content"],
                "rank-up II Chinese force and Japanese killing/healing contrast", checks)
        require("尚在能够忍受的范畴" in ascension[2]["content"]["values"]["zh-Hans"]["content"]
                and "还在稳稳地握住刀" in ascension[3]["content"]["values"]["zh-Hans"]["content"]
                and "never falters" in ascension[3]["content"]["values"]["en"]["content"],
                "rank-up III/IV present pain tolerance and EN technical intensification", checks)
        require("我们是盟友" in ascension[4]["content"]["values"]["zh-Hans"]["content"]
                and "sworn friends" in ascension[4]["content"]["values"]["en"]["content"]
                and "until then and beyond" in ascension[4]["content"]["values"]["en"]["content"],
                "rank-up V ally versus English relationship/duration intensification", checks)
        raw_states = jsonl(source / "RAW_RELEVANT_FLOW_STATES.jsonl")
        academy_state = next(row for row in raw_states if row["source_locator"].endswith(
            "/flowstate.json#/12327"))
        require(academy_state["raw"]["StateKey"] == "剧情_3_1_拉海洛主线_下半_21_1",
                "Academy audience exact Chapter 3.1 state identity", checks)
        academy_params = json.loads(academy_state["raw"]["Actions"])[3]["Params"]
        academy_items = academy_params["TalkItems"]
        luuk_indices = (2, 9, 10, 11, 16, 18, 19, 20, 21, 22, 23,
                        25, 26, 29, 31, 32, 34, 35, 36, 38, 40)
        require(len(academy_items) == 42 and
                academy_params["TalkSequence"] == [list(range(1, 43))] and
                not any(item.get("Options") for item in academy_items) and
                tuple(index for index, item in enumerate(academy_items)
                      if item.get("WhoId") == 150065) == luuk_indices and
                all(academy_items[index].get("PlayVoice") is True
                    for index in luuk_indices) and
                academy_items[39]["WhoId"] == academy_items[41]["WhoId"] == 150057 and
                academy_items[27]["WhoId"] == 750539,
                "continuous 42-item audience has 21 voiced Luuk turns and distinct Lucilla/N.A.N.A. speakers", checks)
        academy_decisions = [row for row in decisions
                             if row["flow_state_row_index"] == 12327 and
                             row["action_index"] == 3]
        require(len(academy_decisions) == 21 and
                {row["talk_index"] for row in academy_decisions} == set(luuk_indices) and
                all(row["character_attribution"] == "accepted_solo" and
                    row["play_voice"] is True for row in academy_decisions),
                "identity crosswalk retains all twenty-one Academy Luuk occurrences", checks)
        quest_refs = jsonl(source / "QUEST_CONTEXT_REFERENCES.jsonl")
        require({row["source_locator"].split("/BinData/")[1].split("#/")[0]
                 for row in quest_refs
                 if str(row["quest_id"]) == "189000000" and
                 any(ref["state_key"] == academy_state["raw"]["StateKey"]
                     for ref in row["matching_references"])} ==
                {"QuestNodeData/questnodedata.json",
                 "PlotHandBook/plothandbookconfig.json"},
                "Academy state directly joins quest 189000000 in node and handbook", checks)
        waffle_state = next(row for row in raw_states if row["source_locator"].endswith(
            "/flowstate.json#/15461"))
        talk_items = json.loads(waffle_state["raw"]["Actions"])[5]["Params"]["TalkItems"]
        options = talk_items[5]["Options"]
        targets = [option["Actions"][0]["Params"]["TalkId"] for option in options]
        require(targets == [7, 10]
                and [item["TidTalk"] for item in talk_items[6:9]] ==
                [f"Side_LHSCP_2_{suffix}" for suffix in range(9, 12)]
                and [item["TidTalk"] for item in talk_items[9:12]] ==
                [f"Side_LHSCP_2_{suffix}" for suffix in range(12, 15)]
                and all(talk_items[index]["Actions"][0]["Params"]["TalkId"] == 13
                        for index in (8, 11)),
                "raw graph forks to alternate three-line waffle runs and rejoins at TalkId 13",
                checks)
        leave_state = next(row for row in raw_states if row["source_locator"].endswith(
            "/flowstate.json#/15475"))
        leave_actions = json.loads(leave_state["raw"]["Actions"])
        leave_items = next(action["Params"]["TalkItems"] for action in leave_actions
                           if action["Name"] == "ShowTalk")
        fatigue_offer = leave_items[21]
        require(fatigue_offer["PlotLineKey"] == "Side_LHSCP_15_27" and
                fatigue_offer["WhoId"] == 150065 and fatigue_offer["PlayVoice"] and
                [option["PlotLineKey"] for option in fatigue_offer["Options"]] ==
                    ["Side_LHSCP_15_28", "Side_LHSCP_15_29"],
                "fatigue-notice wish has two distinct Rover reply options", checks)
        witnesses = {row["text_key"]: row["values"] for row in
                     jsonl(source / "CONTEXT_TEXT_WITNESSES.jsonl")}
        require(all(witnesses[key][lang]["status"] == "resolved"
                    for key in ("Side_LHSCP_15_27", "Side_LHSCP_15_28",
                                "Side_LHSCP_15_29")
                    for lang in ("zh-Hans", "en", "ja", "ko")) and
                "希望我能第一时间看出来" in
                    witnesses["Side_LHSCP_15_27"]["zh-Hans"]["content"] and
                "I hope" in witnesses["Side_LHSCP_15_27"]["en"]["content"] and
                witnesses["Side_LHSCP_15_28"]["en"]["content"] ==
                    "You already have." and
                witnesses["Side_LHSCP_15_29"]["en"]["content"] ==
                    "I look forward to it.",
                "four-language fatigue wish and alternate retrospective/prospective replies", checks)
        require("十个校工里八个" in witnesses["MAIN_RGLC_40_20"]["zh-Hans"]["content"] and
                "スパイ" in witnesses["MAIN_RGLC_40_20"]["ja"]["content"] and
                "planted" in witnesses["MAIN_RGLC_40_20"]["en"]["content"] and
                "全封闭管理" in witnesses["MAIN_RGLC_40_21"]["zh-Hans"]["content"] and
                "gilded cage" in witnesses["MAIN_RGLC_40_21"]["en"]["content"] and
                "学生们并不愚蠢" in witnesses["MAIN_RGLC_40_22"]["zh-Hans"]["content"],
                "Academy staffing, management and student-agency localization limits", checks)
        require("早就吃腻了" in witnesses["MAIN_RGLC_40_13"]["zh-Hans"]["content"] and
                "细作" in witnesses["MAIN_RGLC_40_15"]["zh-Hans"]["content"] and
                "优先处理损伤" in witnesses["MAIN_RGLC_40_32"]["zh-Hans"]["content"] and
                "围" in witnesses["MAIN_RGLC_40_39"]["zh-Hans"]["content"] and
                "单独验证" in witnesses["MAIN_RGLC_40_41"]["zh-Hans"]["content"] and
                "一人のほうが動きやすい" in
                    witnesses["MAIN_RGLC_40_41"]["ja"]["content"] and
                "track record" in witnesses["MAIN_RGLC_40_42"]["en"]["content"],
                "declined candy, earned trust and conditional solo emergency witnesses", checks)
        require(all(witnesses[f"Side_LHSCP_10_{suffix}"][language]["status"] == "resolved"
                    for suffix in (14, 16, 17, 22, 26, 27, 28, 32, 33)
                    for language in ("zh-Hans", "en", "ja", "ko")) and
                "并肩走过" in witnesses["Side_LHSCP_10_14"]["zh-Hans"]["content"] and
                "more than just an observer" in
                    witnesses["Side_LHSCP_10_16"]["en"]["content"] and
                "调查残星会" in witnesses["Side_LHSCP_10_17"]["zh-Hans"]["content"] and
                "朋友的建议" in witnesses["Side_LHSCP_10_22"]["zh-Hans"]["content"] and
                "Once it's adopted" in witnesses["Side_LHSCP_10_32"]["en"]["content"] and
                "再次邀请你" in witnesses["Side_LHSCP_10_33"]["zh-Hans"]["content"],
                "four-language direct presence, friend and conditional invitation witnesses", checks)
        line_rows = jsonl(voice / "COMPLETE_VOICE_LINE_ANALYSIS.jsonl")
        require(len(line_rows) == 719, "719 selected semantic voice rows", checks)
        line_by_locator = {row["source_locator"]: row for row in line_rows}
        academy_voice = [line_by_locator[
            f"wuwa://{COMMIT}/BinData/flowState/flowstate.json#/12327/Actions!/3/Params/TalkItems/{index}"]
            for index in luuk_indices]
        extra_english_indices = {2, 19, 34}
        require(all(row["text_key"] == academy_items[index]["TidTalk"] and
                    len(row["renders"]) == (5 if index in extra_english_indices else 4) and
                    {render["voice_language"] for render in row["renders"]} == LANGUAGES and
                    all(render["materialization_status"] == "flac_roundtrip_pcm_identical" and
                        render["source_wem_exists"] and
                        render["source_wem_sha256_verified"] and
                        render.get("event_id") is None and
                        render.get("numeric_media_id") is None and
                        (source_root / render["flac_relative_path"]).is_file()
                        for render in row["renders"])
                    for index, row in zip(luuk_indices, academy_voice)),
                "21 Academy Luuk turns preserve three second-EN variants and valid source/PCM joins", checks)
        academy_renders = [render for row in academy_voice for render in row["renders"]]
        require(len(academy_renders) == 87 and
                Counter(render["voice_language"] for render in academy_renders) ==
                {"en": 24, "ja": 21, "ko": 21, "zh": 21} and
                len({render["canonical_pcm_sha256"] for render in academy_renders}) == 87 and
                all(len({render["runtime_render_variant_id"] for render in row["renders"]
                         if render["voice_language"] == "en"}) == 2
                    for index, row in zip(luuk_indices, academy_voice)
                    if index in extra_english_indices),
                "87 distinct Academy PCM associations include three extra English runtime variants", checks)
        academy_nominations = ((2, "40_3"), (19, "40_20"), (20, "40_21"),
                               (22, "40_23"), (31, "40_32"), (34, "40_35"),
                               (38, "40_39"), (40, "40_41"))
        academy_by_index = dict(zip(luuk_indices, academy_voice))
        require(all(academy_items[index]["TidTalk"] == f"MAIN_RGLC_{suffix}" and
                    f"MAIN_RGLC_{suffix}" in crosswalk
                    for index, suffix in academy_nominations) and
                sum(len(academy_by_index[index]["renders"])
                    for index, _ in academy_nominations) == 35,
                "eight exact Academy nominations retain thirty-five selected sound associations", checks)
        exostrider_specs = (
            (15731, 3, 21, (0, 2, 3, 4, 5, 6, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 20),
             "剧情_3_3_拉海洛主线_上半新_2_1", 20332, 0,
             ("Zuoyequnxing_50_2", "Zuoyequnxing_50_3")),
            (15733, 2, 40, (0, 1, 2, 3, 4, 5, 8, 10, 28, 36, 38, 39),
             "剧情_3_3_拉海洛主线_上半新_2_3", 20335, 12,
             ("Zuoyequnxing_52_14", "Zuoyequnxing_52_15")),
        )
        exostrider_renders = []
        for (state_row, action_index, item_count, indices, state_key,
             node_index, option_index, option_keys) in exostrider_specs:
            state = next(row for row in raw_states if row["source_locator"].endswith(
                f"/flowstate.json#/{state_row}"))
            actions = json.loads(state["raw"]["Actions"])
            params = actions[action_index]["Params"]
            items = params["TalkItems"]
            require(state["raw"]["StateKey"] == state_key and
                    actions[action_index]["Name"] == "ShowTalk" and
                    len(items) == item_count and
                    params["TalkSequence"] == [list(range(1, item_count + 1))] and
                    not params["SequenceTransitions"] and
                    [index for index, item in enumerate(items) if item.get("Options")] ==
                    [option_index] and
                    tuple(option["PlotLineKey"] for option in
                          items[option_index]["Options"]) == option_keys and
                    all(not option.get("Actions") for option in
                        items[option_index]["Options"]) and
                    tuple(index for index, item in enumerate(items)
                          if item.get("WhoId") == 150065) == indices,
                    f"Exostrider {state_row}/{action_index}: linear graph, two-caption menu and exact Luuk turns",
                    checks)
            require(all(witnesses[key][language]["status"] == "resolved"
                        for key in option_keys
                        for language in ("zh-Hans", "en", "ja", "ko")),
                    f"Exostrider {state_row}/{action_index}: both Rover captions have four text witnesses",
                    checks)
            source_decisions = [row for row in decisions
                                if row["flow_state_row_index"] == state_row and
                                row["action_index"] == action_index]
            require(len(source_decisions) == len(indices) and
                    {row["talk_index"] for row in source_decisions} == set(indices) and
                    all(row["character_attribution"] == "accepted_solo" and
                        row["play_voice"] for row in source_decisions),
                    f"Exostrider {state_row}/{action_index}: accepted exact speaker occurrences",
                    checks)
            source_lines = [line_by_locator[
                f"wuwa://{COMMIT}/BinData/flowState/flowstate.json#/{state_row}"
                f"/Actions!/{action_index}/Params/TalkItems/{index}"]
                for index in indices]
            require(all(row["text_key"] == items[index]["TidTalk"] and
                        len(row["renders"]) == 4 and
                        {r["voice_language"] for r in row["renders"]} == LANGUAGES and
                        all(r["materialization_status"] == "flac_roundtrip_pcm_identical" and
                            r["source_wem_exists"] and r["source_wem_sha256_verified"] and
                            all(len(r[field]) == 64 for field in
                                ("canonical_pcm_sha256", "flac_sha256", "expected_wem_sha256")) and
                            r.get("event_id") is None and r.get("bank_id") is None and
                            r.get("numeric_media_id") is None and
                            (source_root / r["flac_relative_path"]).is_file()
                            for r in row["renders"])
                        for index, row in zip(indices, source_lines)),
                    f"Exostrider {state_row}/{action_index}: four-dub PCM and null Wwise-ID joins",
                    checks)
            exostrider_renders.extend(r for row in source_lines for r in row["renders"])
            require(any(str(row["quest_id"]) == "121000040" and
                        row["source_locator"].endswith(f"/questnodedata.json#/{node_index}") and
                        any(ref["state_key"] == state_key
                            for ref in row["matching_references"])
                        for row in quest_refs) and
                    any(str(row["quest_id"]) == "121000040" and
                        row["source_locator"].endswith("/plothandbookconfig.json#/77") and
                        any(ref["state_key"] == state_key
                            for ref in row["matching_references"])
                        for row in quest_refs),
                    f"Exostrider {state_row}/{action_index}: exact node and handbook quest join",
                    checks)
        require(len(exostrider_renders) == 116 and
                len({r["canonical_pcm_sha256"] for r in exostrider_renders}) == 116 and
                Counter(r["voice_language"] for r in exostrider_renders) ==
                {language: 29 for language in LANGUAGES},
                "two Exostrider actions: twenty-nine lines and 116 distinct four-dub PCM objects",
                checks)
        companion_state = next(row for row in raw_states if row["source_locator"].endswith(
            "/flowstate.json#/15470"))
        companion_actions = json.loads(companion_state["raw"]["Actions"])
        companion_params = companion_actions[4]["Params"]
        companion_items = companion_params["TalkItems"]
        companion_indices = (1, 3, 4, 6, 7, 9, 10, 11, 14, 15, 16, 17,
                             19, 20, 21, 23, 24, 26, 28, 30, 31, 32, 33)
        choice = companion_items[24]["Options"]
        require(companion_state["raw"]["StateKey"] == "剧情_3.2_陆赫斯coop_11_1" and
                companion_actions[4]["Name"] == "ShowTalk" and
                len(companion_items) == 34 and
                not companion_params.get("TalkSequence") and
                not companion_params.get("SequenceTransitions") and
                tuple(index for index, item in enumerate(companion_items)
                      if item.get("WhoId") == 150065) == companion_indices and
                sum(item.get("WhoId") == 750088 for item in companion_items) == 7 and
                all(companion_items[index].get("PlayVoice") is True
                    for index in companion_indices) and
                [option["PlotLineKey"] for option in choice] ==
                    [f"Side_LHSCP_10_{suffix}" for suffix in (26, 27, 28)] and
                [[action["Params"]["TalkId"] for action in option["Actions"]
                  if action["Name"] == "JumpTalk"] for option in choice] ==
                    [[0], [32], [33]] and
                [companion_items[index]["Id"] for index in (25, 27, 29)] ==
                    [0, 32, 33] and
                [companion_items[index]["TidTalk"] for index in (26, 28, 30)] ==
                    [f"Side_LHSCP_10_{suffix}" for suffix in (29, 30, 31)] and
                all(companion_items[index]["Actions"][0]["Params"]["TalkId"] == 29
                    for index in (26, 28, 30)) and
                [companion_items[index]["TidTalk"] for index in (31, 32, 33)] ==
                    [f"Side_LHSCP_10_{suffix}" for suffix in (32, 33, 34)],
                "companion 34-item graph preserves three JumpTalk answers and common conditional rejoin",
                checks)
        require(any(str(row["quest_id"]) == "165800021" and
                    row["source_locator"].endswith("/questnodedata.json#/19182") and
                    any(ref["state_key"] == companion_state["raw"]["StateKey"] and
                        ref["pointer"] == "/FinishActions/0/Params"
                        for ref in row["matching_references"])
                    for row in quest_refs),
                "companion state joins quest 165800021 through exact finish-action pointer",
                checks)
        companion_decisions = [row for row in decisions
                               if row["flow_state_row_index"] == 15470 and
                               row["action_index"] == 4]
        require(len(companion_decisions) == 23 and
                {row["talk_index"] for row in companion_decisions} == set(companion_indices) and
                all(row["character_attribution"] == "accepted_solo" and
                    row["play_voice"] is True for row in companion_decisions),
                "23 exact Luuk companion occurrences accepted and source-voiced", checks)
        companion_lines = [line_by_locator[
            f"wuwa://{COMMIT}/BinData/flowState/flowstate.json#/15470"
            f"/Actions!/4/Params/TalkItems/{index}"] for index in companion_indices]
        companion_renders = [render for row in companion_lines for render in row["renders"]]
        require(all(row["text_key"] == companion_items[index]["TidTalk"] and
                    len(row["renders"]) == 4 and
                    {render["voice_language"] for render in row["renders"]} == LANGUAGES
                    for index, row in zip(companion_indices, companion_lines)) and
                len(companion_renders) == 92 and
                len({render["canonical_pcm_sha256"] for render in companion_renders}) == 92 and
                all(render["materialization_status"] == "flac_roundtrip_pcm_identical" and
                    render["source_wem_exists"] and render["source_wem_sha256_verified"] and
                    render.get("event_id") is None and render.get("bank_id") is None and
                    render.get("numeric_media_id") is None and
                    (source_root / render["flac_relative_path"]).is_file()
                    for render in companion_renders),
                "23 companion authored-union lines have 92 distinct four-dub PCM-valid renders",
                checks)
        companion_by_index = dict(zip(companion_indices, companion_lines))
        nominations = ((14, 15), (16, 17), (21, 22), (24, 25), (26, 29),
                       (28, 30), (30, 31), (31, 32), (32, 33))
        require(all(companion_by_index[index]["text_key"] ==
                    f"Side_LHSCP_10_{suffix}" and
                    f"Side_LHSCP_10_{suffix}" in crosswalk
                    for index, suffix in nominations) and
                sum(len(companion_by_index[index]["renders"])
                    for index, _ in nominations) == 36,
                "nine exact companion nominations preserve 36 four-dub sound objects", checks)
        require("没人能确认" in witnesses["Zuoyequnxing_50_19"]["zh-Hans"]["content"] and
                "no one's been able to prove" in
                    witnesses["Zuoyequnxing_50_19"]["en"]["content"] and
                "争取到了商谈机会" in
                    witnesses["Zuoyequnxing_50_11"]["zh-Hans"]["content"] and
                "损失降到最低" in witnesses["Zuoyequnxing_52_7"]["zh-Hans"]["content"] and
                "lowest casualty count" in
                    witnesses["Zuoyequnxing_52_7"]["en"]["content"] and
                "百分百" in witnesses["Zuoyequnxing_52_41"]["zh-Hans"]["content"],
                "meeting, rumor, loss-localization and no-certainty text anchors", checks)
        require(json.loads(next(row for row in raw_states if row["source_locator"].endswith(
                    "/flowstate.json#/15733"))["raw"]["Actions"])[2]["Params"]["TalkItems"][6]["WhoId"] == 750088 and
                json.loads(next(row for row in raw_states if row["source_locator"].endswith(
                    "/flowstate.json#/15733"))["raw"]["Actions"])[2]["Params"]["TalkItems"][11]["WhoId"] == 750019,
                "Rover's risk proposal and Shorekeeper's briefing are not Luuk turns", checks)
        combat_profile = (packet_artifact(HERE, f"{PREFIX}COMBAT_SURGICAL_LANGUAGE_AND_ARCHIVE_KEY_PROFILE.md")
                          ).read_text(encoding="utf-8")
        combat_table = [tuple(map(int, match)) for match in re.findall(
            r"(?m)^\| (1510\d{2}) \| (1510\d{2}) \| `(?:favorword)?#/([0-9]+)` \|",
            combat_profile)]
        expected_combat_table = [(151038 + index,
                                  151039 + index if index < 21 else 151078,
                                  3190 + index)
                                 for index in range(22)]
        require(combat_table == expected_combat_table,
                "22 exact raw favor IDs, actual Content keys and locators", checks)
        archive_by_locator = {row["source_locator"]: row for row in line_rows
                              if "/BinData/favor/favorword.json#/" in row["source_locator"]}
        source_combat = [row for row in package["favor_words"]
                         if 151038 <= row["id"] <= 151059]
        require(len(source_combat) == 22 and len(archive_by_locator) == 77,
                "22 combat source rows among 77 archive voice rows", checks)
        combat_renders = []
        combat_events = set()
        for raw_id, key_suffix, source_index in combat_table:
            raw = next(row for row in source_combat if row["id"] == raw_id)
            locator = raw["source_locator"]
            key = f"FavorWord_{key_suffix}_Content"
            require(locator.endswith(f"/favorword.json#/{source_index}") and
                    raw["content"]["text_key"] == key and locator in archive_by_locator,
                    f"combat raw/key/locator join: {raw_id}", checks)
            voice_row = archive_by_locator[locator]
            require(voice_row["text_key"] == key and
                    voice_row["technical_render_coverage_status"] == "complete" and
                    len(voice_row["renders"]) == 4 and
                    {render["voice_language"] for render in voice_row["renders"]} == LANGUAGES,
                    f"combat semantic/four-dub coverage: {raw_id}", checks)
            require(all(voice_row["text_witnesses"][voice_lang]["content"] ==
                        raw["content"]["values"][text_lang]["content"]
                        for voice_lang, text_lang in
                        (("zh", "zh-Hans"), ("en", "en"), ("ja", "ja"), ("ko", "ko"))),
                    f"combat four-text witness join: {raw_id}", checks)
            require(all(render["event_path"] == raw["voice_asset"] and
                        isinstance(render["event_id"], int) and
                        isinstance(render["bank_id"], int) and
                        isinstance(render["numeric_media_id"], int) and
                        render["source_wem_exists"] and
                        render["source_wem_sha256_verified"] and
                        render["materialization_status"] == "flac_roundtrip_pcm_identical" and
                        render["canonical_pcm_sha256"] ==
                        render["expected_canonical_pcm_sha256"]
                        for render in voice_row["renders"]),
                    f"combat event/media/PCM join: {raw_id}", checks)
            combat_events.update(render["event_id"] for render in voice_row["renders"])
            combat_renders.extend(voice_row["renders"])
        require(len(combat_renders) == 88 and
                len({render["canonical_pcm_sha256"] for render in combat_renders}) == 88 and
                len(combat_events) == 22,
                "22 combat events and 88 distinct four-dub PCM objects", checks)
        require("Intro Skill I" in combat_profile and "Hit I" in combat_profile and
                "FavorWord_151078_Content" in combat_profile,
                "combat trigger/localization/causal limits documented", checks)
        cohort_path = (source_root / "_research" / "character_packets" / NAME /
                       "audio_work" / "LUUK_SOURCE_COHORT_AUDIT.json")
        require(hashlib.sha256(cohort_path.read_bytes()).hexdigest() ==
                "00199988c6959545f6249eb61e62d19f7a4961a73bdbb0d8b9e05f8f25dcd95e",
                "pinned exact-action cohort audit hash", checks)
        cohort_audit = json.loads(cohort_path.read_text(encoding="utf-8"))
        require(cohort_audit["whole_measured_object_count"] == 2855 and
                cohort_audit["whole_measured_integrity_pass_count"] == 2855 and
                not cohort_audit["human_perceptual_review_performed"] and
                not cohort_audit["video_review_performed"],
                "cohort audit measures all objects without claiming human AV", checks)
        expected_cohorts = {
            "clinic_uncertainty": ("10719/5@1-12", 12, 50),
            "sigrika_counsel": ("12313/3@0+2-3+5-6+8-9+11", 8, 32),
            "rover_counsel_and_disclosure":
                ("12313/3@13+15-17+19-20+25-26+28+30-32+34-36+39-41+43+45+47", 21, 86),
            "shock_care": ("12330/4", 6, 24),
            "architect_challenge": ("12331/4", 7, 28),
            "architect_inference": ("12332/3", 9, 36),
            "waffle_praise": ("15461/5@6-8", 3, 12),
            "waffle_critique": ("15461/5@9-11", 3, 12),
            "academy_ordinary": ("15461/5@14-29+31-32", 18, 72),
            "cat_care_planning": ("15473/2", 19, 76),
            "cat_freedom_and_leave": ("15475/5", 21, 84),
        }
        cohorts = cohort_audit["cohorts"]
        require({cohort["name"] for cohort in cohorts} == set(expected_cohorts),
                "eleven exact source-action cohort names", checks)
        require(all((cohort["source_actions"][0], cohort["semantic_lines"],
                     cohort["render_associations"]) == expected_cohorts[cohort["name"]]
                    for cohort in cohorts), "eleven exact selectors and counts", checks)
        members = [member for cohort in cohorts for member in cohort["members"]]
        require(len(members) == 512 and
                len({member["semantic_voice_occurrence_id"] for member in members}) == 127 and
                len({member["render_analysis_id"] for member in members}) == 512 and
                len({member["canonical_pcm_sha256"] for member in members}) == 512,
                "disjoint 127-line/512-render/512-PCM cohort membership", checks)
        source_renders = {
            (row["semantic_voice_occurrence_id"], render["render_analysis_id"]):
            (row, render)
            for row in line_rows for render in row["renders"]
        }
        require(all(
            (member["semantic_voice_occurrence_id"], member["render_analysis_id"])
            in source_renders and
            member["source_locator"] == source_renders[
                (member["semantic_voice_occurrence_id"], member["render_analysis_id"])
            ][0]["source_locator"] and
            member["text_key"] == source_renders[
                (member["semantic_voice_occurrence_id"], member["render_analysis_id"])
            ][0]["text_key"] and
            all(member[left] == source_renders[
                (member["semantic_voice_occurrence_id"], member["render_analysis_id"])
            ][1][right] for left, right in (
                ("voice_language", "voice_language"),
                ("canonical_pcm_sha256", "canonical_pcm_sha256"),
                ("flac_sha256", "flac_sha256")))
            for member in members), "all cohort members match exact selected source/render/hash joins", checks)
        multi = Counter((member["source_locator"], member["voice_language"])
                        for member in members)
        require({(locator.split("TalkItems/")[-1], lang)
                 for (locator, lang), count in multi.items() if count == 2} ==
                {("2", "ja"), ("9", "ja"), ("43", "en"), ("47", "en")} and
                sum(count == 2 for count in multi.values()) == 4,
                "four exact second-PCM semantic-language slots retained", checks)
        negative_rows = [row for row in decisions if
                         (row["flow_state_row_index"], row["action_index"]) in
                         {(15474, 1), (15914, 1)}]
        require(Counter((row["flow_state_row_index"], row["action_index"])
                        for row in negative_rows) == {(15474, 1): 11, (15914, 1): 9} and
                all(row["character_attribution"] == "accepted_solo" and
                    row["play_voice"] is False for row in negative_rows) and
                not any("/15474/Actions!/1/Params/TalkItems/" in row["source_locator"] or
                        "/15914/Actions!/1/Params/TalkItems/" in row["source_locator"]
                        for row in line_rows),
                "twenty accepted message turns are source-unvoiced", checks)
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
        audio = json.loads(summary.read_text(encoding="utf-8"))
        require((audio["manifest_objects"], audio["measured_objects"],
                 audio["repeated_pcm_manifest_rows"]) == (2855, 2855, 8),
                "full local audio measurement counts", checks)
        require(not audio["failed_objects"] and not audio["human_perceptual_review_performed"],
                "zero local audio failures; human listening not implied", checks)
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
        (packet_artifact(HERE, "VALIDATION_REPORT.json")).write_text(
            json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8", newline="\n")
    print(json.dumps({key: report[key] for key in
                      ("packet", "source_crosscheck", "result", "check_count")}, indent=2))


if __name__ == "__main__":
    main()
