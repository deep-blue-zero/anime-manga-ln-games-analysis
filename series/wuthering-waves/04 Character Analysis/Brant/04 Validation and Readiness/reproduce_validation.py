#!/usr/bin/env python3
"""Validate Brant's draft packet; optionally crosscheck private primary evidence.

Structural/identity/media joins only: not literary truth, exhaustive graph paths,
generative fidelity, or human listening. Only --write-report writes.
"""

from __future__ import annotations

import argparse
from collections import Counter
import json
from pathlib import Path
import re


HERE = Path(__file__).resolve().parent.parent
COMMIT = "353f2eaed119bc9f680eab92807d20ac75a79b40"
LANGUAGES = {"en", "ja", "ko", "zh"}
MEDIA_SUFFIXES = {".wav", ".flac", ".wem", ".mp3", ".mp4", ".png", ".webp", ".pak"}




# Exact character-root-relative paths after the artifact-class migration.
PACKET_ARTIFACT_PATHS = {'AUDIO_MATCHED_SEMANTIC_CASES.json': '03 Audiovisual and Voice/AUDIO_MATCHED_SEMANTIC_CASES.json', 'CHARACTER_VISUAL_DESIGN_PROFILE.json': '03 Audiovisual and Voice/CHARACTER_VISUAL_DESIGN_PROFILE.json', 'CHARACTER_VISUAL_DESIGN_PROFILE.md': '03 Audiovisual and Voice/CHARACTER_VISUAL_DESIGN_PROFILE.md', 'CHARACTER_VISUAL_REFERENCE_MANIFEST.json': '03 Audiovisual and Voice/CHARACTER_VISUAL_REFERENCE_MANIFEST.json', 'VALIDATION_REPORT.json': '04 Validation and Readiness/VALIDATION_REPORT.json', 'WUWA_BRANT_ANALYSIS_PACKET_README.md': 'WUWA_BRANT_ANALYSIS_PACKET_README.md', 'WUWA_BRANT_ASCENSION_RISK_AND_INVITATION_PROFILE.md': '01 Evidence and Source-Facing/WUWA_BRANT_ASCENSION_RISK_AND_INVITATION_PROFILE.md', 'WUWA_BRANT_AV_AND_HUMAN_RETRIEVAL_PLAN.md': '03 Audiovisual and Voice/WUWA_BRANT_AV_AND_HUMAN_RETRIEVAL_PLAN.md', 'WUWA_BRANT_AV_HUMAN_RETRIEVAL_CROSSWALK.md': '03 Audiovisual and Voice/WUWA_BRANT_AV_HUMAN_RETRIEVAL_CROSSWALK.md', 'WUWA_BRANT_CHARACTER_DEEP_DIVE_PRE_AV.md': '01 Evidence and Source-Facing/WUWA_BRANT_CHARACTER_DEEP_DIVE_PRE_AV.md', 'WUWA_BRANT_CHARACTER_MODEL_PACKAGE.json': '02 Reconstruction/WUWA_BRANT_CHARACTER_MODEL_PACKAGE.json', 'WUWA_BRANT_CLAIM_REVISION_LEDGER.md': '04 Validation and Readiness/WUWA_BRANT_CLAIM_REVISION_LEDGER.md', 'WUWA_BRANT_DRAKE_ALDRIC_COST_AND_FATE_PROFILE.md': '01 Evidence and Source-Facing/WUWA_BRANT_DRAKE_ALDRIC_COST_AND_FATE_PROFILE.md', 'WUWA_BRANT_ECHO_TRANSLATION_PUPPET_TROUPE_AND_ALDRIC_INTERVENTION_PROFILE.md': '01 Evidence and Source-Facing/WUWA_BRANT_ECHO_TRANSLATION_PUPPET_TROUPE_AND_ALDRIC_INTERVENTION_PROFILE.md', 'WUWA_BRANT_EVIDENCE_AND_FALSIFICATION_MATRIX.md': '01 Evidence and Source-Facing/WUWA_BRANT_EVIDENCE_AND_FALSIFICATION_MATRIX.md', 'WUWA_BRANT_FESTIVAL_FREEDOM_THEOLOGY_AND_LOCALIZATION_PROFILE.md': '01 Evidence and Source-Facing/WUWA_BRANT_FESTIVAL_FREEDOM_THEOLOGY_AND_LOCALIZATION_PROFILE.md', 'WUWA_BRANT_MODEL_FIDELITY_AND_STRESS_TEST_PRE_AV.md': '04 Validation and Readiness/WUWA_BRANT_MODEL_FIDELITY_AND_STRESS_TEST_PRE_AV.md', 'WUWA_BRANT_NIGHTMARE_PERFORMANCE_REBIRTH_AND_COLLECTIVE_MOURNING_PROFILE.md': '01 Evidence and Source-Facing/WUWA_BRANT_NIGHTMARE_PERFORMANCE_REBIRTH_AND_COLLECTIVE_MOURNING_PROFILE.md', 'WUWA_BRANT_ORDINARY_LIFE_HOME_AND_CREW_LABOR_PROFILE.md': '01 Evidence and Source-Facing/WUWA_BRANT_ORDINARY_LIFE_HOME_AND_CREW_LABOR_PROFILE.md', 'WUWA_BRANT_PERFORMANCE_PERSONHOOD_AND_COMMAND_PROFILE.md': '01 Evidence and Source-Facing/WUWA_BRANT_PERFORMANCE_PERSONHOOD_AND_COMMAND_PROFILE.md', 'WUWA_BRANT_PLUSHIE_INFILTRATION_ROLE_AND_COMPANION_CHOICE_PROFILE.md': '01 Evidence and Source-Facing/WUWA_BRANT_PLUSHIE_INFILTRATION_ROLE_AND_COMPANION_CHOICE_PROFILE.md', 'WUWA_BRANT_RECONSTRUCTIVE_PROFILE_PRE_AV.md': '02 Reconstruction/WUWA_BRANT_RECONSTRUCTIVE_PROFILE_PRE_AV.md', 'WUWA_BRANT_RELATIONSHIP_STATE_AND_ORDINARY_LIFE_PROFILE.md': '01 Evidence and Source-Facing/WUWA_BRANT_RELATIONSHIP_STATE_AND_ORDINARY_LIFE_PROFILE.md', 'WUWA_BRANT_SOURCE_CENSUS_CHRONOLOGY_AND_IDENTITY_AUDIT.md': '04 Validation and Readiness/WUWA_BRANT_SOURCE_CENSUS_CHRONOLOGY_AND_IDENTITY_AUDIT.md', 'WUWA_BRANT_SPEECH_AND_MACHINE_VOICE_PROFILE_PRE_AV.md': '03 Audiovisual and Voice/WUWA_BRANT_SPEECH_AND_MACHINE_VOICE_PROFILE_PRE_AV.md', 'WUWA_BRANT_TEMPORARY_HELM_BRANCH_AND_CREW_VALUE_PROFILE.md': '01 Evidence and Source-Facing/WUWA_BRANT_TEMPORARY_HELM_BRANCH_AND_CREW_VALUE_PROFILE.md', 'WUWA_BRANT_WAGER_EXCHANGE_AND_HONORARY_HELM_PROFILE.md': '01 Evidence and Source-Facing/WUWA_BRANT_WAGER_EXCHANGE_AND_HONORARY_HELM_PROFILE.md', 'reproduce_validation.py': '04 Validation and Readiness/reproduce_validation.py'}

def packet_artifact(root: Path, name: str) -> Path:
    return root / PACKET_ARTIFACT_PATHS.get(name, name)

def jsonl(path: Path) -> list[dict]:
    with path.open(encoding="utf-8") as handle:
        return [json.loads(line) for line in handle if line.strip()]


def textmap_content(path: Path, key: str) -> str:
    """Read one pinned textmap entry without loading the large file into memory."""
    marker = f'"Id": "{key}"'
    with path.open(encoding="utf-8") as handle:
        for line in handle:
            if marker in line:
                content_line = next(handle)
                if '"Content":' not in content_line:
                    raise AssertionError(f"missing Content after {key} in {path}")
                return json.loads(content_line.split(":", 1)[1].strip().removesuffix(","))
    raise AssertionError(f"missing {key} in {path}")


def require(condition: bool, message: str, checks: list[str]) -> None:
    if not condition:
        raise AssertionError(message)
    checks.append(message)


def validate(source_root: Path | None) -> dict:
    checks: list[str] = []
    matrix = (packet_artifact(HERE, "WUWA_BRANT_EVIDENCE_AND_FALSIFICATION_MATRIX.md")).read_text(encoding="utf-8")
    evidence_ids = set(re.findall(r"\| (BRA-E\d{2}) \|", matrix))
    claim_ids = set(re.findall(r"\| (BRA-C\d{2}) —", matrix))
    require(evidence_ids == {f"BRA-E{n:02d}" for n in range(1, 47)},
            "46 contiguous evidence bundles", checks)
    require(claim_ids == {f"BRA-C{n:02d}" for n in range(1, 43)},
            "42 contiguous claim rows", checks)
    require(not any(path.suffix.lower() in MEDIA_SUFFIXES for path in HERE.rglob("*") if path.is_file()),
            "no raw media in Git packet", checks)
    for path in HERE.rglob("WUWA_BRANT_*.md"):
        body = path.read_text(encoding="utf-8")
        require(body.startswith("---\n") and "\nstatus: draft_noncurrent\n" in body,
                f"draft authority: {path.name}", checks)
        require("\ndo_not_use_as_current_authority: true\n" in body,
                f"noncurrent flag: {path.name}", checks)
        require(f"\nsource_commit: {COMMIT}\n" in body,
                f"source pin: {path.name}", checks)
    model = json.loads((packet_artifact(HERE, "WUWA_BRANT_CHARACTER_MODEL_PACKAGE.json")).read_text(encoding="utf-8"))
    require(model["authority"] == "draft_noncurrent" and model["source_commit"] == COMMIT,
            "model authority and source pin", checks)
    rules = model["rules"]
    require({rule["id"] for rule in rules} ==
            {f"BRA-R{n:02d}" for n in range(1, 22)},
            "21 contiguous model rules", checks)
    require(all(set(rule["evidence_ids"]) <= evidence_ids for rule in rules),
            "all model evidence IDs resolve", checks)
    require(all(rule["probability"] is None for rule in rules),
            "no fabricated numerical probabilities", checks)
    probes = (packet_artifact(HERE, "WUWA_BRANT_MODEL_FIDELITY_AND_STRESS_TEST_PRE_AV.md")).read_text(encoding="utf-8")
    require(set(re.findall(r"\| (BRA-P\d{2}) \|", probes)) ==
            {f"BRA-P{n:02d}" for n in range(1, 47)},
            "46 contiguous non-blind probes", checks)
    require("## Nine interaction tests" in probes,
            "nine interacting constraint tests", checks)
    cases = json.loads((packet_artifact(HERE, "AUDIO_MATCHED_SEMANTIC_CASES.json")).read_text(encoding="utf-8"))
    require(cases["semantic_cases"] == 23 and len(cases["cases"]) == 23,
            "23 matched semantic cases", checks)
    crosswalk = (packet_artifact(HERE, "WUWA_BRANT_AV_HUMAN_RETRIEVAL_CROSSWALK.md")).read_text(encoding="utf-8")
    require(all(f"`{case['text_key']}`" in crosswalk for case in cases["cases"]),
            "all 23 exact sound cases occur in AV crosswalk", checks)
    require("stage fiction" in crosswalk and "near-duplicate" in crosswalk,
            "stage-fiction and duplicate-route controls in AV crosswalk", checks)
    require("Main_Linaxita_2_3_39_57" in crosswalk and
            "additional retrieval nomination" in crosswalk,
            "middle Carnival line remains an explicit extra retrieval candidate", checks)
    require(all(f"BRA-R{n:02d}" in crosswalk for n in range(9, 13)) and
            all(key in crosswalk for key in
                ("Character_Brant_3_31", "Character_Brant_61_3",
                 "Character_Brant_65_10", "Character_Brant_71_11")),
            "wager/exchange/honorary-helm AV retrieval controls retained", checks)
    require(set(re.findall(r"\| (BRA-R\d{2}) \|", crosswalk)) ==
            {f"BRA-R{n:02d}" for n in range(1, 16)} and
            all(key in crosswalk for key in
                ("Main_Rinascita_2_11_9_9–13", "Main_Rinascita_2_12_741_3–13")),
            "fifteen runtime/negative controls include civic performance and Egla disguise",
            checks)
    require(sum(len(case["renders"]) for case in cases["cases"]) == 92,
            "92 selected render variants", checks)
    require(all({render["language"] for render in case["renders"]} == LANGUAGES
                for case in cases["cases"]), "each case has four dubs", checks)
    selected_renders = [render for case in cases["cases"] for render in case["renders"]]
    require(sum(render["event_id"] is None and render["numeric_media_id"] is None
                for render in selected_renders) == 48,
            "48 selected renders preserve paired null event/media IDs", checks)
    require(all((render["event_id"] is None) == (render["numeric_media_id"] is None)
                for render in selected_renders), "selected event/media nulls remain paired", checks)
    require(all(len(render[name]) == 64 for case in cases["cases"] for render in case["renders"]
                for name in ("wem_sha256", "canonical_pcm_sha256", "flac_sha256")),
            "selected render hashes present", checks)
    result = {"packet": "Brant", "scope": "BRANT_PINNED_3_6_0_TEXT_AUDIO_PRE_AV",
              "checks": checks, "source_crosscheck": "not_requested"}
    if source_root is not None:
        source = source_root / "ANALYSIS" / "Characters" / "Brant"
        voice = source_root / "_voice_media" / "character" / "complete_voice_corpus" / "Brant" / "v0_1"
        summary = source_root / "_research" / "character_packets" / "Brant" / "audio_work" / "AUDIO_MEASUREMENT_SUMMARY.json"
        audit = json.loads((source / "COLLECTION_AUDIT.json").read_text(encoding="utf-8"))
        direct = audit["scopes"]["direct_character"]
        require(audit["valid"] and direct["voice_completeness_valid"],
                "selected collection audit valid", checks)
        require((audit["raw_flow_states"], audit["context_text_keys"],
                 audit["quest_references"], audit["distinct_quest_ids"]) ==
                (219, 3163, 127, 28), "contextual collection denominator", checks)
        require((direct["candidate_occurrences"], direct["accepted_occurrences"],
                 direct["source_voiced"], direct["source_unvoiced"]) ==
                (662, 636, 544, 92), "direct occurrence denominator", checks)
        require((direct["semantic_voice_lines"], direct["render_associations"],
                 direct["unique_flac_objects"]) ==
                (606, 2432, 2324), "voice line, association, object denominators", checks)
        decisions = jsonl(source / "occurrence_identity_crosswalk.jsonl")
        require(Counter(row["character_attribution"] for row in decisions) ==
                {"accepted_solo": 636, "rejected": 18, "unresolved": 8},
                "identity crosswalk counts", checks)
        witnesses = {row["text_key"]: row["values"]
                     for row in jsonl(source / "CONTEXT_TEXT_WITNESSES.jsonl")}
        carnival_row = next(row for row in jsonl(source / "RAW_RELEVANT_FLOW_STATES.jsonl")
                            if row["source_locator"].endswith("#/4384"))
        carnival_action = json.loads(carnival_row["raw"]["Actions"])[2]
        carnival = carnival_action["Params"]
        require(carnival_action["Name"] == "ShowTalk" and
                len(carnival["TalkSequence"]) == 7 and
                all(index in carnival["TalkSequence"][6] for index in (34, 35, 36, 37)) and
                len(carnival["TalkSequence"][6]) == 21,
                "Carnival speech follows optional clue loops in one common final unit", checks)
        require(all(carnival["TalkItems"][index]["WhoId"] == 1462 and
                    carnival["TalkItems"][index]["PlayVoice"] and
                    carnival["TalkItems"][index]["TidTalk"] ==
                    f"Main_Linaxita_2_3_39_{index + 21}"
                    for index in (34, 35, 36, 37)),
                "four common-path festival speech turns are source-voiced Brant", checks)
        require("夺魁" in witnesses["Main_Linaxita_2_3_39_57"]["zh-Hans"]["content"] and
                "기적" in witnesses["Main_Linaxita_2_3_39_57"]["ko"]["content"] and
                "win the Laurel" in witnesses["Main_Linaxita_2_3_39_57"]["en"]["content"] and
                "悪しき者が罰せられない" in witnesses["Main_Linaxita_2_3_39_57"]["ja"]["content"] and
                "神がいようといなかろうと" in
                witnesses["Main_Linaxita_2_3_39_58"]["ja"]["content"],
                "JA unpunished-evil premise differs while final freedom claim remains", checks)
        package = json.loads((source / "character_source_package.json").read_text(encoding="utf-8"))
        ascensions = {row["content"]["text_key"]: row for row in package["favor_words"]
                      if 120626 <= row["id"] <= 120630}
        require(len(ascensions) == 5, "five source-package ascension rows", checks)
        for number in range(120626, 120631):
            key = f"FavorWord_{number}_Content"
            row = ascensions[key]
            require((row["id"], row["raw"]["Id"], row["sort"]) ==
                    (number, number, number - 120600),
                    f"ascension row and sort identity: {key}", checks)
            require(row["source_locator"].endswith(f"favorword.json#/{1861 + number - 120626}")
                    and row["title"]["values"]["en"]["content"] ==
                    f"Ascension: {['I', 'II', 'III', 'IV', 'V'][number - 120626]}",
                    f"ascension locator and title: {key}", checks)
            require(row["voice_asset"].endswith(
                f"play_favor_word_bulante_sys_rankup0{number - 120625}"),
                    f"ascension source event path: {key}", checks)
            require(all(row["content"]["values"][lang]["status"] == "resolved"
                        for lang in ("en", "ja", "ko", "zh-Hans")),
                    f"four resolved ascension text witnesses: {key}", checks)
        require("无惧风浪" in ascensions["FavorWord_120627_Content"]["content"]["values"]["zh-Hans"]["content"]
                and "storm-proof and unstoppable" in ascensions["FavorWord_120627_Content"]["content"]["values"]["en"]["content"]
                and "動じない" in ascensions["FavorWord_120627_Content"]["content"]["values"]["ja"]["content"]
                and "굴복하지" in ascensions["FavorWord_120627_Content"]["content"]["values"]["ko"]["content"],
                "Ascension II four-witness resolve versus EN immunity fork", checks)
        require("更高一点" in ascensions["FavorWord_120629_Content"]["content"]["values"]["zh-Hans"]["content"]
                and "乗り越えた" in ascensions["FavorWord_120629_Content"]["content"]["values"]["ja"]["content"]
                and "더 높게" in ascensions["FavorWord_120629_Content"]["content"]["values"]["ko"]["content"],
                "Ascension IV prospective versus JA completed-wave fork", checks)
        require("朋友" in ascensions["FavorWord_120630_Content"]["content"]["values"]["zh-Hans"]["content"]
                and "friend" in ascensions["FavorWord_120630_Content"]["content"]["values"]["en"]["content"]
                and "天空海" in ascensions["FavorWord_120630_Content"]["content"]["values"]["ja"]["content"],
                "Ascension V friend invitation and JA sky-sea image", checks)
        require("回去捡钱" in witnesses["Character_Brant_70_2"]["zh-Hans"]["content"]
                and "over his own life" in witnesses["Character_Brant_70_2"]["en"]["content"]
                and "金に囚われ" in witnesses["Character_Brant_70_2"]["ja"]["content"]
                and "돈을 주우러" in witnesses["Character_Brant_70_2"]["ko"]["content"],
                "Aldric aftermath has bounded four-language fate wording", checks)
        require("愚人船" in witnesses["Character_Brant_66_22"]["zh-Hans"]["content"]
                and "Pilgrim's Sail" in witnesses["Character_Brant_66_22"]["en"]["content"]
                and "巡礼船" in witnesses["Character_Brant_66_22"]["ja"]["content"]
                and "우인선" in witnesses["Character_Brant_66_22"]["ko"]["content"],
                "Aldric ship departure label is a documented localization divergence", checks)
        require("加工了一下" in witnesses["Character_Brant_30_9"]["zh-Hans"]["content"] and
                "embellished" in witnesses["Character_Brant_30_9"]["en"]["content"] and
                "人形劇団" in witnesses["Character_Brant_30_11"]["ja"]["content"] and
                "Echoes" in witnesses["Character_Brant_30_11"]["en"]["content"] and
                "人の尊厳" in witnesses["Character_Brant_33_15"]["ja"]["content"],
                "Echo translation, puppet-troupe scope and dignity localization bounds", checks)
        require("流血牺牲" in witnesses["Character_Brant_36_14"]["zh-Hans"]["content"]
                and "tricking" in witnesses["Character_Brant_36_14"]["en"]["content"]
                and "逃了出去" in witnesses["Character_Brant_70_20"]["zh-Hans"]["content"],
                "cost-shifting and Drake escape witness distinctions", checks)
        pinned_flow = json.loads((source_root / "_sources" / "Arikatsu_WutheringWaves_Data"
                                  / "BinData" / "flowState" / "flowstate.json").read_text(encoding="utf-8"))
        egla_action = json.loads(pinned_flow[5245]["Actions"])[3]
        egla = egla_action["Params"]
        egla_items = egla["TalkItems"]
        require(pinned_flow[5245]["StateKey"] == "剧情_2_1_角色_布兰特线_1_13" and
                egla_action["Name"] == "ShowTalk" and len(egla_items) == 13 and
                [item["WhoId"] for item in egla_items] ==
                [1462] * 4 + [750088] + [1462] * 8 and
                all(item["PlayVoice"] is True for item in egla_items),
                "Egla action separates Brant's twelve voice turns from Rover's stealth turn",
                checks)
        require(egla["TalkSequence"] == [list(range(1, 11)), [11], [12], [13]] and
                [(option["OptionTextKey"], option["NextSequenceIndex"])
                 for option in egla["SequenceTransitions"]["0"]] ==
                [("Character_Brant_27_13", 1), ("Character_Brant_27_14", 2)] and
                [egla["SequenceTransitions"][str(index)][0]["NextSequenceIndex"]
                 for index in (1, 2)] == [3, 3] and
                [egla_items[index]["TidTalk"] for index in (10, 11, 12)] ==
                ["Character_Brant_27_15", "Character_Brant_27_16", "Character_Brant_27_17"],
                "Egla two exclusive Rover role replies reach distinct Brant turns then rejoin",
                checks)
        require("打草惊蛇" in witnesses["Character_Brant_27_4"]["zh-Hans"]["content"] and
                "潜行" in witnesses["Character_Brant_27_5"]["zh-Hans"]["content"] and
                "布偶剧团" in witnesses["Character_Brant_27_10"]["zh-Hans"]["content"] and
                "人形劇団" in witnesses["Character_Brant_27_10"]["ja"]["content"] and
                "인형 극단" in witnesses["Character_Brant_27_10"]["ko"]["content"] and
                "plushie" in witnesses["Character_Brant_27_10"]["en"]["content"] and
                "把「什么东西」给你套上" in
                witnesses["Character_Brant_27_18"]["zh-Hans"]["content"],
                "Egla danger, stealth, troupe localization and unspecified costume synopsis",
                checks)
        egla_owned = [row for row in decisions
                      if row["flow_state_row_index"] == 5245 and
                      row["action_index"] == 3 and
                      row["character_attribution"] == "accepted_solo"]
        require(len(egla_owned) == 12 and
                {row["talk_index"] for row in egla_owned} ==
                set(range(4)) | set(range(5, 13)) and
                all(row["technical_speaker_id"] == 1462 and
                    row["play_voice"] is True for row in egla_owned),
                "Egla identity crosswalk retains only twelve Brant-owned turns", checks)
        nightmare_action = json.loads(pinned_flow[8850]["Actions"])[5]
        nightmare = nightmare_action["Params"]
        nightmare_items = nightmare["TalkItems"]
        require(pinned_flow[8850]["StateKey"] ==
                "剧情_2_7_黎那汐塔主线_上半_1_7_1" and
                nightmare_action["Name"] == "ShowTalk" and
                len(nightmare_items) == 21 and
                nightmare["TalkSequence"] ==
                [list(range(1, 13)), [13], [14], [15], list(range(16, 22))] and
                {index: nightmare_items[index]["WhoId"] for index in (0, 9, 10, 11, 13, 14)} ==
                {0: 1462, 9: 1533, 10: 1533, 11: 1462, 13: 1533, 14: 1462},
                "nightmare scene raw action, speakers and source sequence retained", checks)
        require(len(nightmare_items[1]["Options"]) == 3 and
                all(not option["Actions"] for option in nightmare_items[1]["Options"]) and
                [option["Actions"][0]["Params"]["TalkId"]
                 for option in nightmare_items[12]["Options"]] == [14, 15, 16] and
                [(row["OptionTextKey"], row["NextSequenceIndex"])
                 for row in nightmare["SequenceTransitions"]["1"]] ==
                [("Main_Rinascita_2_11_9_17", 2),
                 ("Main_Rinascita_2_11_9_18", 3),
                 ("Main_Rinascita_2_11_9_19", 4)] and
                all(nightmare["SequenceTransitions"][str(n)][0]["NextSequenceIndex"] == 1
                    for n in (2, 3)),
                "opening captions differ from alternative nightmare question paths", checks)
        memorial_action = json.loads(pinned_flow[11777]["Actions"])[2]
        memorial = memorial_action["Params"]
        memorial_items = memorial["TalkItems"]
        brant_memorial_indices = (0, 2, 3, 6, 9, 10, 11, 12)
        require(pinned_flow[11777]["StateKey"] ==
                "剧情_2_7_黎那汐塔主线_上半_2_50_1" and
                memorial_action["Name"] == "ShowTalk" and
                len(memorial_items) == 14 and
                not memorial.get("TalkSequence") and
                all(memorial_items[index]["WhoId"] == 1462 and
                    not memorial_items[index].get("PlayVoice")
                    for index in brant_memorial_indices) and
                memorial_items[4]["WhoId"] == 1533 and
                memorial_items[13]["WhoId"] == 702,
                "memorial template separates eight unvoiced Brant texts from Roccia and toast repeat",
                checks)
        require("布兰特提议编排" in
                witnesses["Main_Rinascita_2_11_9_15"]["zh-Hans"]["content"] and
                "洛可可和布兰特都还没有" in
                witnesses["Main_Rinascita_2_11_9_20"]["zh-Hans"]["content"] and
                "似乎只有" in
                witnesses["Main_Rinascita_2_11_9_16"]["zh-Hans"]["content"] and
                "似乎都改换" in
                witnesses["Main_Rinascita_2_11_9_21"]["zh-Hans"]["content"] and
                "sounding an awful lot like" in
                witnesses["Main_Rinascita_2_11_9_21"]["en"]["content"],
                "Roccia-attributed play, non-dreamer boundary and qualified anomaly reports",
                checks)
        require("建立之时" in
                witnesses["Main_Rinascita_2_12_741_4"]["zh-Hans"]["content"] and
                "세워지기 전에" in
                witnesses["Main_Rinascita_2_12_741_4"]["ko"]["content"] and
                "too young" in
                witnesses["Main_Rinascita_2_12_741_10"]["en"]["content"] and
                "もう少し先" in
                witnesses["Main_Rinascita_2_12_741_10"]["ja"]["content"] and
                "敬逝者，也敬明天" in
                witnesses["Main_Rinascita_2_12_741_13"]["zh-Hans"]["content"],
                "recipe-dating and Roccia age localization forks retained with dual toast",
                checks)
        wager = json.loads(pinned_flow[5236]["Actions"])[3]["Params"]
        wager_items = wager["TalkItems"]
        require(pinned_flow[5236]["StateKey"] == "剧情_2_1_角色_布兰特线_1_2"
                and len(wager_items) == 38
                and wager["TalkSequence"][0] == [1, 2, 3, 4]
                and [(r["OptionTextKey"], r["NextSequenceIndex"])
                     for r in wager["SequenceTransitions"]["0"]] ==
                [("Character_Brant_3_6", 1), ("Character_Brant_3_7", 2)]
                and wager["TalkSequence"][1:3] == [[5], [6]]
                and all(wager["SequenceTransitions"][str(n)][0]["NextSequenceIndex"] == 3
                        for n in (1, 2)),
                "fish-wager opening alternatives reconverge before crew stake", checks)
        require([(r["OptionTextKey"], r["NextSequenceIndex"])
                 for r in wager["SequenceTransitions"]["3"]] ==
                [("Character_Brant_3_35", 4), ("Character_Brant_3_36", 5)]
                and wager["TalkSequence"][4:6] == [[30], [31]]
                and all(wager["SequenceTransitions"][str(n)][0]["NextSequenceIndex"] == 6
                        for n in (4, 5))
                and [wager_items[n]["PlotLineKey"] for n in (25, 29, 30, 31, 36)] ==
                ["Character_Brant_3_31", "Character_Brant_3_37",
                 "Character_Brant_3_38", "Character_Brant_3_39",
                 "Character_Brant_3_44"]
                and all(wager_items[n]["WhoId"] == 1462
                        for n in (25, 29, 30, 31, 36)),
                "Brant accepts crew-adjudicated labor; distinct title replies rejoin at consent", checks)
        require(wager_items[11]["WhoId"] == 50098
                and wager_items[12]["WhoId"] == 50098
                and "值日" in witnesses["Character_Brant_3_15"]["zh-Hans"]["content"]
                and "愿赌服输" in witnesses["Character_Brant_3_31"]["zh-Hans"]["content"]
                and "entirely up to you" in
                witnesses["Character_Brant_3_39"]["en"]["content"],
                "Battier owns day-off stakes while Brant accepts result and keeps helm optional",
                checks)
        painting = json.loads(pinned_flow[6281]["Actions"])[6]["Params"]
        painting_items = painting["TalkItems"]
        require(pinned_flow[6281]["StateKey"] == "剧情_2_1_角色_布兰特线_1_50"
                and len(painting_items) == 9
                and painting.get("TalkSequence") is None
                and [o["Actions"][0]["Params"]["TalkId"]
                     for o in painting_items[2]["Options"]] == [4, 5, 6]
                and [painting_items[n]["Actions"][0]["Params"]["TalkId"]
                     for n in (3, 4, 5)] == [7, 7, 7]
                and all(item["WhoId"] == 1462 for item in painting_items),
                "three painted-scale readings receive exclusive replies then rejoin", checks)
        require("破碎的心" in witnesses["Character_Brant_61_3"]["zh-Hans"]["content"]
                and "或许" in witnesses["Character_Brant_61_12"]["zh-Hans"]["content"]
                and "Maybe" in witnesses["Character_Brant_61_12"]["en"]["content"],
                "broken-heart symbol and Drake fairness remain hypotheses", checks)
        inscription = json.loads(pinned_flow[6282]["Actions"])[1]["Params"]
        inscription_items = inscription["TalkItems"]
        require(pinned_flow[6282]["StateKey"] == "剧情_2_1_角色_布兰特线_1_51"
                and len(inscription_items) == 9
                and inscription.get("TalkSequence") is None
                and [len(inscription_items[n]["Options"]) for n in (2, 4, 7)] ==
                [2, 2, 2]
                and all(not option["Actions"]
                        for n in (2, 4, 7)
                        for option in inscription_items[n]["Options"])
                and all(item["WhoId"] == 1462 for item in inscription_items),
                "inscription has three option surfaces without explicit jump actions", checks)
        require("诅咒" in witnesses["Character_Brant_65_2"]["zh-Hans"]["content"]
                and "等价交换" in witnesses["Character_Brant_65_3"]["zh-Hans"]["content"]
                and "或许" in witnesses["Character_Brant_65_6"]["zh-Hans"]["content"]
                and "洋流" in witnesses["Character_Brant_65_10"]["zh-Hans"]["content"]
                and "波と風" in witnesses["Character_Brant_65_10"]["ja"]["content"]
                and "해류" in witnesses["Character_Brant_65_10"]["ko"]["content"]
                and "offer something in return" in
                witnesses["Character_Brant_65_10"]["en"]["content"],
                "quoted curse, hedged price and EN sea-offering localization fork", checks)
        honor = json.loads(pinned_flow[6283]["Actions"])[2]["Params"]
        honor_items = honor["TalkItems"]
        require(pinned_flow[6283]["StateKey"] == "剧情_2_1_角色_布兰特线_1_52"
                and len(honor_items) == 9
                and [o["Actions"][0]["Params"]["TalkId"]
                     for o in honor_items[0]["Options"]] == [2, 3]
                and [honor_items[n]["Actions"][0]["Params"]["TalkId"]
                     for n in (1, 3)] == [5, 5]
                and honor_items[5]["WhoId"] == 750088
                and honor_items[7]["WhoId"] == 1462
                and honor_items[7]["PlotLineKey"] == "Character_Brant_71_11",
                "day-end versus paperwork replies rejoin before honorary conferral", checks)
        require("荣誉船长" in witnesses["Character_Brant_71_11"]["zh-Hans"]["content"]
                and "Honorary Captain" in witnesses["Character_Brant_71_11"]["en"]["content"]
                and "名誉キャプテン" in witnesses["Character_Brant_71_11"]["ja"]["content"]
                and "명예 선장" in witnesses["Character_Brant_71_11"]["ko"]["content"]
                and "scroll" in witnesses["Character_Brant_71_8"]["en"]["content"]
                and "海图" in witnesses["Character_Brant_71_8"]["zh-Hans"]["content"],
                "four-language honorary title with bounded EN scroll/map object fork", checks)
        aldric_interlude = json.loads(pinned_flow[5356]["Actions"])[2]["Params"]["TalkItems"]
        require([item["WhoId"] for item in aldric_interlude] == [100023, 100023]
                and [item["PlotLineKey"] for item in aldric_interlude] == [
                    "Character_Brant_68_1", "Character_Brant_68_3"],
                "intervening full-source row 5356 is Aldric-only, not a Brant death declaration", checks)
        echo_talk = json.loads(pinned_flow[6820]["Actions"])[2]["Params"]["TalkItems"]
        pirate_talk = json.loads(pinned_flow[6823]["Actions"])[5]["Params"]["TalkItems"]
        def targets(item: dict) -> list[int]:
            return [option["Actions"][0]["Params"]["TalkId"]
                    for option in item.get("Options", []) if option.get("Actions")]
        require(pinned_flow[6820]["StateKey"] == "剧情_2_1_角色_布兰特线_6_2" and
                len(echo_talk) == 10 and
                [echo_talk[i]["WhoId"] for i in (0, 1, 5, 6, 7, 8)] ==
                [100016, 1462, 100016, 1462, 100016, 1462] and
                targets(echo_talk[2]) == [4, 5] and
                [echo_talk[i]["Actions"][0]["Params"]["TalkId"] for i in (3, 4)] ==
                [6, 6],
                "short Echo speech and two translation-question replies reconverge", checks)
        require(pinned_flow[6823]["StateKey"] == "剧情_2_1_角色_布兰特线_6_5" and
                len(pirate_talk) == 33 and
                [pirate_talk[i]["WhoId"] for i in (0, 11, 12, 13, 21, 23, 24, 27)] ==
                [100023, 100013, 1462, 1462, 100023, 100016, 1462, 1462] and
                targets(pirate_talk[11]) == [13, 14] and
                targets(pirate_talk[27]) == [29, 30] and
                [pirate_talk[i]["Actions"][0]["Params"]["TalkId"]
                 for i in (12, 13, 28, 29)] == [15, 15, 31, 31],
                "pirate chant ownership, moral reply fork and optional introduction reconverge",
                checks)
        require(pirate_talk[31]["WhoId"] == 100023 and
                pirate_talk[31]["PlotLineKey"] == "Character_Brant_33_40" and
                "not the real Lottie Lost" in
                witnesses["Character_Brant_33_40"]["en"]["content"],
                "pirates identify the intruders as disguised humans, not the original Echoes",
                checks)
        quest_context = jsonl(source / "QUEST_CONTEXT_REFERENCES.jsonl")
        expected_quest_states = {
            "剧情_2_1_角色_布兰特线_1_2": "155000000_8",
            "剧情_2_1_角色_布兰特线_1_50": "155000000_120",
            "剧情_2_1_角色_布兰特线_1_51": "155000000_123",
            "剧情_2_1_角色_布兰特线_1_52": "155000000_115",
        }
        quest_state_joins = {
            (ref["state_key"], node["raw"].get("Key"))
            for node in quest_context
            if "/QuestNodeData/" in node["source_locator"]
            for ref in node["matching_references"]
        }
        require(all((state, key) in quest_state_joins
                    for state, key in expected_quest_states.items()),
                "four exact quest-node joins for wager, painting, inscription and honor", checks)
        handbook_state_pointers = {
            (ref["state_key"], ref["pointer"])
            for node in quest_context
            if node["source_locator"].endswith("plothandbookconfig.json#/35")
            for ref in node["matching_references"]
        }
        require(all((state, f"/{pointer}/Flow") in handbook_state_pointers
                    for state, pointer in zip(expected_quest_states, (1, 72, 73, 81))),
                "handbook order differs from quest-node numeric order", checks)
        require(not any(ref["state_key"] in {
            "剧情_2_1_角色_布兰特线_6_2", "剧情_2_1_角色_布兰特线_6_5"}
            for node in quest_context for ref in node["matching_references"]),
            "no exact-state quest-node join for the two Echo actions", checks)
        temporary_helm = json.loads(pinned_flow[5238]["Actions"])[2]["Params"]["TalkItems"]
        require(pinned_flow[5238]["StateKey"] == "剧情_2_1_角色_布兰特线_1_5" and
                temporary_helm[5]["Id"] == 6 and
                temporary_helm[5]["PlotLineKey"] == "Character_Brant_11_8" and
                temporary_helm[5]["WhoId"] == 1462,
                "temporary helm option source row, talk ID and Brant speaker", checks)
        option_jumps = {
            option["PlotLineKey"]: option["Actions"][0]["Params"]["TalkId"]
            for option in temporary_helm[5]["Options"]
        }
        require(option_jumps == {
            "Character_Brant_11_9": 9,
            "Character_Brant_11_10": 7,
            "Character_Brant_11_11": 8,
        } and
                [temporary_helm[i]["Actions"][0]["Params"]["TalkId"]
                 for i in (6, 7)] == [9, 9] and
                temporary_helm[8]["Id"] == 9 and
                temporary_helm[8]["PlotLineKey"] == "Character_Brant_11_14",
                "three Rover answers converge through two optional Brant replies", checks)
        require(all(item["WhoId"] == 1462 for item in temporary_helm[8:13]) and
                temporary_helm[11]["PlotLineKey"] == "Character_Brant_11_17",
                "common branch names crew talents then returns Brant to deck labor", checks)
        captain_text = witnesses["Character_Brant_11_14"]
        require("最有意思的" in captain_text["zh-Hans"]["content"] and
                "without a captain" in captain_text["en"]["content"] and
                "一番の宝物" in captain_text["ja"]["content"] and
                "극단 사람들이지" in captain_text["ko"]["content"] and
                "失うわけにはいかない" in
                witnesses["Character_Brant_11_16"]["ja"]["content"],
                "shared crew-value line has bounded EN captain and JA no-loss additions", checks)
        require("<ano=带来欢笑>掠夺</ano>" in
                witnesses["Character_Brant_11_8"]["zh-Hans"]["content"] and
                "lives of leisure and luxury" in
                witnesses["Character_Brant_13_29"]["en"]["content"] and
                "风吹雨淋" in
                witnesses["Character_Brant_13_29"]["zh-Hans"]["content"],
                "annotated pirate wording and non-Brant wealth localization fork", checks)
        half_coin = json.loads(pinned_flow[5239]["Actions"])[3]["Params"]
        first_coin_options = half_coin["SequenceTransitions"]["0"]
        require(half_coin["TalkSequence"][0] == list(range(1, 23)) and
                [(row["OptionTextKey"], row["NextSequenceIndex"])
                 for row in first_coin_options] == [
                    ("Character_Brant_13_27", 1),
                    ("Character_Brant_13_28", 2)] and
                half_coin["TalkSequence"][1:3] == [[23], [24]] and
                half_coin["TalkSequence"][3] == list(range(25, 35)) and
                all(half_coin["SequenceTransitions"][str(index)][0]["NextSequenceIndex"] == 3
                    for index in (1, 2)),
                "half-coin and treasure question branches rejoin common sequence", checks)
        require(half_coin["TalkItems"][21]["WhoId"] == 50098 and
                half_coin["TalkItems"][21]["PlotLineKey"] == "Character_Brant_13_26" and
                [half_coin["TalkItems"][index]["WhoId"] for index in (22, 23)] == [1545, 1545] and
                [half_coin["TalkItems"][index]["PlotLineKey"] for index in (22, 23)] == [
                    "Character_Brant_13_29", "Character_Brant_13_30"],
                "treasure and luxury speculation is not voiced by Brant", checks)
        bet = json.loads(pinned_flow[5241]["Actions"])[3]["Params"]
        require([(row["OptionTextKey"], row["NextSequenceIndex"])
                 for row in bet["SequenceTransitions"]["0"]] == [
                    ("Character_Brant_16_8", 2),
                    ("Character_Brant_16_9", 1)] and
                bet["TalkSequence"][1] == [8] and
                bet["SequenceTransitions"]["1"][0]["NextSequenceIndex"] == 2 and
                bet["TalkItems"][7]["PlotLineKey"] == "Character_Brant_16_10",
                "one-day bet explanation is conditional then rejoins common path", checks)
        performance = json.loads(pinned_flow[5244]["Actions"])[3]["Params"]
        require([(row["OptionTextKey"], row["NextSequenceIndex"])
                 for row in performance["SequenceTransitions"]["0"]] == [
                    ("Character_Brant_26_2", 1),
                    ("Character_Brant_26_3", 2)] and
                performance["TalkSequence"][1:3] == [[2, 3], [4, 5]] and
                all(performance["SequenceTransitions"][str(index)][0]["NextSequenceIndex"] == 3
                    for index in (1, 2)) and
                performance["TalkSequence"][3] == list(range(6, 28)),
                "applause and drunkenness response branches rejoin coin inquiry", checks)
        pinned_base = source_root / "_sources" / "Arikatsu_WutheringWaves_Data"
        quest_nodes = json.loads((pinned_base / "BinData" / "QuestTree" /
                                  "questtreenode.json").read_text(encoding="utf-8"))
        quest_node = quest_nodes[45]
        require(quest_node["Id"] == 220030 and
                quest_node["QuestArray"] == [155000000] and
                quest_node["Summary"] == "QuestTree_Summary_220030",
                "Brant quest node links character quest to retrospective summary", checks)
        synopsis = {
            lang: textmap_content(pinned_base / "Textmaps" / lang /
                                  "multi_text" / "MultiText.json",
                                  "QuestTree_Summary_220030")
            for lang in ("zh-Hans", "en", "ja", "ko")
        }
        require("爱蒂奇因为贪婪葬身于此" in synopsis["zh-Hans"] and
                "meets his end" in synopsis["en"] and
                "その場所に埋まってしまい" in synopsis["ja"] and
                "죽음을 맞이하게 되었고" in synopsis["ko"],
                "linked four-language quest synopsis reports Aldric end with JA wording limit",
                checks)
        line_rows = jsonl(voice / "COMPLETE_VOICE_LINE_ANALYSIS.jsonl")
        require(len(line_rows) == 606, "606 selected semantic voice rows", checks)
        egla_locators = {row["source_locator"] for row in egla_owned}
        egla_lines = [row for row in line_rows
                      if row["source_locator"] in egla_locators]
        egla_renders = [render for row in egla_lines for render in row["renders"]]
        require(len(egla_lines) == 12 and
                {row["source_locator"] for row in egla_lines} == egla_locators and
                len(egla_renders) == 48 and
                len({render["canonical_pcm_sha256"] for render in egla_renders}) == 48 and
                all({render["voice_language"] for render in row["renders"]} == LANGUAGES
                    for row in egla_lines),
                "Egla twelve authored-union Brant voice rows join 48 distinct four-dub PCM objects",
                checks)
        require(all(render["materialization_status"] ==
                    "flac_roundtrip_pcm_identical" and
                    render["source_wem_sha256_verified"] and
                    render.get("event_id") is None and
                    render.get("bank_id") is None and
                    render.get("numeric_media_id") is None and
                    len(render["canonical_pcm_sha256"]) == 64
                    for render in egla_renders),
                "Egla media are verified without invented Wwise numeric IDs or listening",
                checks)
        nightmare_owned = [row for row in decisions
                           if row["flow_state_row_index"] == 8850 and
                           row["action_index"] == 5 and
                           row["character_attribution"] == "accepted_solo"]
        memorial_owned = [row for row in decisions
                          if row["flow_state_row_index"] == 11777 and
                          row["action_index"] == 2 and
                          row["character_attribution"] == "accepted_solo"]
        require(len(nightmare_owned) == 10 and
                all(row["play_voice"] and row["technical_speaker_id"] == 1462
                    for row in nightmare_owned) and
                len(memorial_owned) == 8 and
                all(not row["play_voice"] and row["technical_speaker_id"] == 1462
                    for row in memorial_owned),
                "nightmare ten voiced versus memorial eight unvoiced Brant occurrences",
                checks)
        nightmare_locators = {row["source_locator"] for row in nightmare_owned}
        memorial_locators = {row["source_locator"] for row in memorial_owned}
        nightmare_lines = [row for row in line_rows
                           if row["source_locator"] in nightmare_locators]
        require(len(nightmare_lines) == 10 and
                {row["source_locator"] for row in nightmare_lines} ==
                nightmare_locators and
                not any(row["source_locator"] in memorial_locators for row in line_rows),
                "only exact nightmare locators enter selected voice corpus", checks)
        nightmare_renders = [render for row in nightmare_lines
                             for render in row["renders"]]
        require(len(nightmare_renders) == 40 and
                len({render["canonical_pcm_sha256"] for render in nightmare_renders}) == 40 and
                all({render["voice_language"] for render in row["renders"]} ==
                    LANGUAGES for row in nightmare_lines) and
                all(render["materialization_status"] == "flac_roundtrip_pcm_identical" and
                    render["source_wem_sha256_verified"] and
                    render.get("event_id") is None and render.get("bank_id") is None and
                    render.get("numeric_media_id") is None
                    for render in nightmare_renders),
                "nightmare action has forty distinct PCM-valid four-dub joins and null Wwise IDs",
                checks)
        quest_references = jsonl(source / "QUEST_CONTEXT_REFERENCES.jsonl")
        egla_node = next(row for row in quest_references
                          if row["source_locator"].endswith("/questnodedata.json#/9273"))
        egla_handbook = next(row for row in quest_references
                              if row["source_locator"].endswith("/plothandbookconfig.json#/35"))
        require(egla_node["raw"]["Key"] == "155000000_34" and
                any(match["state_key"] == pinned_flow[5245]["StateKey"] and
                    match["pointer"] == "/Condition/Flow"
                    for match in egla_node["matching_references"]) and
                any(match["state_key"] == pinned_flow[5245]["StateKey"] and
                    match["pointer"] == "/27/Flow"
                    for match in egla_handbook["matching_references"]),
                "Egla exact quest-condition and handbook state pointers", checks)
        nightmare_refs = [row for row in quest_references
                          if any(match["state_key"] == pinned_flow[8850]["StateKey"]
                                 for match in row["matching_references"])]
        require(any(row["raw"].get("Key") == "168000001_49"
                    for row in nightmare_refs) and
                any(row["source_locator"].endswith("/plothandbookconfig.json#/56")
                    for row in nightmare_refs) and
                not any(any(match["state_key"] == pinned_flow[11777]["StateKey"]
                            for match in row["matching_references"])
                        for row in quest_references),
                "nightmare exact-state quest leads and absent memorial wrapper are explicit",
                checks)
        for state, action, expected_lines in (
            (5236, 3, 16), (6281, 6, 9), (6282, 1, 9), (6283, 2, 8)
        ):
            owned = [row for row in decisions
                     if row["flow_state_row_index"] == state
                     and row["action_index"] == action
                     and row["character_attribution"] == "accepted_solo"
                     and row["play_voice"]]
            scene_lines = [row for row in line_rows
                           if f"#/{state}/Actions!/{action}/Params/TalkItems/"
                           in row["source_locator"]]
            scene_renders = [render for row in scene_lines for render in row["renders"]]
            require(len(owned) == len(scene_lines) == expected_lines
                    and len(scene_renders) == 4 * expected_lines
                    and len({r["canonical_pcm_sha256"] for r in scene_renders}) ==
                    4 * expected_lines
                    and all({r["voice_language"] for r in row["renders"]} == LANGUAGES
                            for row in scene_lines),
                    f"Brant source ownership and 4-distinct-PCM cohort: {state}/{action}",
                    checks)
            require(all(r.get("event_id") is None and r.get("numeric_media_id") is None
                        and r["source_wem_sha256_verified"]
                        and r["materialization_status"] == "flac_roundtrip_pcm_identical"
                        and r["source_virtual_path"].endswith(
                            f"/{r['voice_language']}_vo_{row['text_key']}.wem")
                        for row in scene_lines for r in row["renders"]),
                    f"key-matching external source and paired-null IDs: {state}/{action}",
                    checks)
        echo_keys = {
            "Character_Brant_30_2": (6820, 2, 1),
            "Character_Brant_30_9": (6820, 2, 6),
            "Character_Brant_30_11": (6820, 2, 8),
            "Character_Brant_33_15": (6823, 5, 12),
            "Character_Brant_33_31": (6823, 5, 24),
        }
        require(all(
            len(rows := [row for row in line_rows if row["text_key"] == key]) == 1 and
            rows[0]["source_locator"].endswith(
                f"#/{where[0]}/Actions!/{where[1]}/Params/TalkItems/{where[2]}") and
            {render["voice_language"] for render in rows[0]["renders"]} == LANGUAGES and
            all(render["materialization_status"] == "flac_roundtrip_pcm_identical" and
                render.get("event_id") is None and render.get("numeric_media_id") is None and
                len(render["canonical_pcm_sha256"]) == 64 and
                len(render["flac_sha256"]) == 64 for render in rows[0]["renders"])
            for key, where in echo_keys.items()),
            "five extra Echo/pirate turns have twenty PCM-valid four-dub joins with null event/media IDs",
            checks)
        carnival_nomination = [row for row in line_rows
                               if row["text_key"] == "Main_Linaxita_2_3_39_57"]
        require(len(carnival_nomination) == 1 and
                carnival_nomination[0]["source_locator"].endswith(
                    "#/4384/Actions!/2/Params/TalkItems/36") and
                {render["voice_language"] for render in carnival_nomination[0]["renders"]} ==
                LANGUAGES and
                all(render["source_wem_exists"] and render["source_wem_sha256_verified"]
                    and render["materialization_status"] == "flac_roundtrip_pcm_identical"
                    and len(render["canonical_pcm_sha256"]) == 64
                    for render in carnival_nomination[0]["renders"]),
                "extra Carnival nomination has four exact verified WEM/PCM/FLAC joins", checks)
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
        for case in cases["cases"][-5:]:
            require(case["text_key"] in ascensions and len(case["renders"]) == 4
                    and all(render["event_id"] is not None
                            and render["numeric_media_id"] is not None
                            for render in case["renders"]),
                    f"rank-up case has exact four-dub render IDs: {case['text_key']}", checks)
        audio = json.loads(summary.read_text(encoding="utf-8"))
        require((audio["manifest_objects"], audio["measured_objects"],
                 audio["repeated_pcm_manifest_rows"]) == (2324, 2324, 4),
                "full local audio measurement counts", checks)
        require(not audio["failed_objects"], "no local audio measurement failures", checks)
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
