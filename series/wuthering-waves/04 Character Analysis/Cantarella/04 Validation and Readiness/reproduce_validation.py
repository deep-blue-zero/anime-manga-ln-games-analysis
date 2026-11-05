#!/usr/bin/env python3
"""Validate Cantarella's draft packet and optionally crosscheck private evidence.

Structural, identity and exact media joins only. This is not a literary-truth,
full graph, generative-fidelity or human listening test. Only --write-report writes.
"""

from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import re


HERE = Path(__file__).resolve().parent.parent
COMMIT = "353f2eaed119bc9f680eab92807d20ac75a79b40"
LANGUAGES = {"en", "ja", "ko", "zh"}
MEDIA_SUFFIXES = {".wav", ".flac", ".wem", ".mp3", ".mp4", ".png", ".webp", ".pak"}




# Exact character-root-relative paths after the artifact-class migration.
PACKET_ARTIFACT_PATHS = {'AUDIO_MATCHED_SEMANTIC_CASES.json': '03 Audiovisual and Voice/AUDIO_MATCHED_SEMANTIC_CASES.json', 'CHARACTER_VISUAL_DESIGN_PROFILE.json': '03 Audiovisual and Voice/CHARACTER_VISUAL_DESIGN_PROFILE.json', 'CHARACTER_VISUAL_DESIGN_PROFILE.md': '03 Audiovisual and Voice/CHARACTER_VISUAL_DESIGN_PROFILE.md', 'CHARACTER_VISUAL_REFERENCE_MANIFEST.json': '03 Audiovisual and Voice/CHARACTER_VISUAL_REFERENCE_MANIFEST.json', 'VALIDATION_REPORT.json': '04 Validation and Readiness/VALIDATION_REPORT.json', 'WUWA_CANTARELLA_ANALYSIS_PACKET_README.md': 'WUWA_CANTARELLA_ANALYSIS_PACKET_README.md', 'WUWA_CANTARELLA_ASCENSION_SEA_SANCTUARY_AND_DISCLOSURE_PROFILE.md': '01 Evidence and Source-Facing/WUWA_CANTARELLA_ASCENSION_SEA_SANCTUARY_AND_DISCLOSURE_PROFILE.md', 'WUWA_CANTARELLA_AV_AND_HUMAN_RETRIEVAL_PLAN.md': '03 Audiovisual and Voice/WUWA_CANTARELLA_AV_AND_HUMAN_RETRIEVAL_PLAN.md', 'WUWA_CANTARELLA_AV_HUMAN_RETRIEVAL_CROSSWALK.md': '03 Audiovisual and Voice/WUWA_CANTARELLA_AV_HUMAN_RETRIEVAL_CROSSWALK.md', 'WUWA_CANTARELLA_CHARACTER_DEEP_DIVE_PRE_AV.md': '01 Evidence and Source-Facing/WUWA_CANTARELLA_CHARACTER_DEEP_DIVE_PRE_AV.md', 'WUWA_CANTARELLA_CHARACTER_MODEL_PACKAGE.json': '02 Reconstruction/WUWA_CANTARELLA_CHARACTER_MODEL_PACKAGE.json', 'WUWA_CANTARELLA_CHERI_HEADSHIP_AND_CONTESTABLE_PROTECTION_PROFILE.md': '01 Evidence and Source-Facing/WUWA_CANTARELLA_CHERI_HEADSHIP_AND_CONTESTABLE_PROTECTION_PROFILE.md', 'WUWA_CANTARELLA_CLAIM_REVISION_LEDGER.md': '04 Validation and Readiness/WUWA_CANTARELLA_CLAIM_REVISION_LEDGER.md', 'WUWA_CANTARELLA_DREAM_TESTIMONY_AND_ACCOUNTABILITY_PROFILE.md': '01 Evidence and Source-Facing/WUWA_CANTARELLA_DREAM_TESTIMONY_AND_ACCOUNTABILITY_PROFILE.md', 'WUWA_CANTARELLA_EVIDENCE_AND_FALSIFICATION_MATRIX.md': '01 Evidence and Source-Facing/WUWA_CANTARELLA_EVIDENCE_AND_FALSIFICATION_MATRIX.md', 'WUWA_CANTARELLA_FIRST_AUDIENCE_APOLOGY_MEDIATION_AND_TEA_REFUSAL_PROFILE.md': '01 Evidence and Source-Facing/WUWA_CANTARELLA_FIRST_AUDIENCE_APOLOGY_MEDIATION_AND_TEA_REFUSAL_PROFILE.md', 'WUWA_CANTARELLA_GHOST_GAME_DESIRE_BARGAIN_AND_REVIVAL_STORY_PROFILE.md': '01 Evidence and Source-Facing/WUWA_CANTARELLA_GHOST_GAME_DESIRE_BARGAIN_AND_REVIVAL_STORY_PROFILE.md', 'WUWA_CANTARELLA_LATER_LEVIATHAN_RECORDS_HARBINGER_AND_COALITION_PROFILE.md': '01 Evidence and Source-Facing/WUWA_CANTARELLA_LATER_LEVIATHAN_RECORDS_HARBINGER_AND_COALITION_PROFILE.md', 'WUWA_CANTARELLA_MODEL_FIDELITY_AND_STRESS_TEST_PRE_AV.md': '04 Validation and Readiness/WUWA_CANTARELLA_MODEL_FIDELITY_AND_STRESS_TEST_PRE_AV.md', 'WUWA_CANTARELLA_ORDINARY_HOSPITALITY_SENSORY_FREEDOM_PROFILE.md': '01 Evidence and Source-Facing/WUWA_CANTARELLA_ORDINARY_HOSPITALITY_SENSORY_FREEDOM_PROFILE.md', 'WUWA_CANTARELLA_RECONSTRUCTIVE_PROFILE_PRE_AV.md': '02 Reconstruction/WUWA_CANTARELLA_RECONSTRUCTIVE_PROFILE_PRE_AV.md', 'WUWA_CANTARELLA_RELATIONSHIP_STATE_AND_ORDINARY_LIFE_PROFILE.md': '01 Evidence and Source-Facing/WUWA_CANTARELLA_RELATIONSHIP_STATE_AND_ORDINARY_LIFE_PROFILE.md', 'WUWA_CANTARELLA_SOURCE_CENSUS_CHRONOLOGY_AND_IDENTITY_AUDIT.md': '04 Validation and Readiness/WUWA_CANTARELLA_SOURCE_CENSUS_CHRONOLOGY_AND_IDENTITY_AUDIT.md', 'WUWA_CANTARELLA_SPEECH_AND_MACHINE_VOICE_PROFILE_PRE_AV.md': '03 Audiovisual and Voice/WUWA_CANTARELLA_SPEECH_AND_MACHINE_VOICE_PROFILE_PRE_AV.md', 'WUWA_CANTARELLA_TOWER_MEMORY_CHILDREN_AND_UNFINISHED_REFORM_PROFILE.md': '01 Evidence and Source-Facing/WUWA_CANTARELLA_TOWER_MEMORY_CHILDREN_AND_UNFINISHED_REFORM_PROFILE.md', 'WUWA_CANTARELLA_TYRVINE_PLEDGE_AND_STAGED_RETURN_PROFILE.md': '01 Evidence and Source-Facing/WUWA_CANTARELLA_TYRVINE_PLEDGE_AND_STAGED_RETURN_PROFILE.md', 'reproduce_validation.py': '04 Validation and Readiness/reproduce_validation.py'}

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
    matrix = (packet_artifact(HERE, "WUWA_CANTARELLA_EVIDENCE_AND_FALSIFICATION_MATRIX.md")).read_text(encoding="utf-8")
    evidence_ids = set(re.findall(r"\| (CAN-E\d{2}) \|", matrix))
    claim_ids = set(re.findall(r"\| (CAN-C\d{2}) —", matrix))
    require(evidence_ids == {f"CAN-E{index:02d}" for index in range(1, 47)},
            "46 contiguous evidence bundles", checks)
    require(claim_ids == {f"CAN-C{index:02d}" for index in range(1, 44)},
            "43 contiguous claim rows", checks)
    choice_profile = (packet_artifact(HERE, "WUWA_CANTARELLA_TYRVINE_PLEDGE_AND_STAGED_RETURN_PROFILE.md")).read_text(
        encoding="utf-8")
    require(all(token in choice_profile for token in
                ("flow#/6811/2", "flow#/5775/5", "flow#/7315/7",
                 "Main_Linaxita_2_4_128_14", "Main_Linaxita_2_4_143_21",
                 "Character_Cantarella_123_30", "330 distinct", "CAN-E42–E44")),
            "Tyrvine/Pledge/return specialist retains three distinct source and media boundaries", checks)
    audience_profile = (packet_artifact(HERE, "WUWA_CANTARELLA_FIRST_AUDIENCE_APOLOGY_MEDIATION_AND_TEA_REFUSAL_PROFILE.md")).read_text(
        encoding="utf-8")
    require(all(token in audience_profile for token in
                ("flow#/6799/4", "flow#/6800/9", "QuestNodeData#/10625",
                 "Main_Linaxita_2_4_8_2", "Main_Linaxita_2_4_8_9",
                 "21", "84 distinct", "CAN-E45", "CAN-C42")),
            "first-audience specialist retains apology, branch, quest and media boundaries", checks)
    ghost_profile = (packet_artifact(HERE, "WUWA_CANTARELLA_GHOST_GAME_DESIRE_BARGAIN_AND_REVIVAL_STORY_PROFILE.md")
                     ).read_text(encoding="utf-8")
    require(all(token in ghost_profile for token in
                ("flow#/6701/6", "PlotHandBook#/37", "Character_Cantarella_134_15",
                 "Character_Cantarella_134_23", "20 authored", "80 distinct",
                 "CAN-E46/C43")),
            "ghost-game specialist retains four-route, staged-prize and media boundaries", checks)
    require(not any(path.suffix.lower() in MEDIA_SUFFIXES for path in HERE.rglob("*") if path.is_file()),
            "no raw media in Git packet", checks)
    for path in HERE.rglob("WUWA_CANTARELLA_*.md"):
        body = path.read_text(encoding="utf-8")
        require(body.startswith("---\n") and "\nstatus: draft_noncurrent\n" in body,
                f"draft authority: {path.name}", checks)
        require("\ndo_not_use_as_current_authority: true\n" in body,
                f"noncurrent flag: {path.name}", checks)
        require(f"\nsource_commit: {COMMIT}\n" in body,
                f"source pin: {path.name}", checks)
    model = json.loads((packet_artifact(HERE, "WUWA_CANTARELLA_CHARACTER_MODEL_PACKAGE.json")).read_text(encoding="utf-8"))
    require(model["authority"] == "draft_noncurrent" and model["source_commit"] == COMMIT,
            "model authority and source pin", checks)
    rules = model["rules"]
    require(len(rules) == 21 and {rule["id"] for rule in rules} ==
            {f"CAN-R{index:02d}" for index in range(1, 22)},
            "21 contiguous model rules", checks)
    require(all(set(rule["evidence_ids"]) <= evidence_ids for rule in rules),
            "all model evidence IDs resolve", checks)
    require(all(rule["probability"] is None for rule in rules),
            "no fabricated numerical probabilities", checks)
    probes = (packet_artifact(HERE, "WUWA_CANTARELLA_MODEL_FIDELITY_AND_STRESS_TEST_PRE_AV.md")).read_text(encoding="utf-8")
    require(set(re.findall(r"\| (CAN-P\d{2}) \|", probes)) ==
            {f"CAN-P{index:02d}" for index in range(1, 49)},
            "48 contiguous non-blind probes", checks)
    require("## Ten interaction tests" in probes and
            all(f"R{number:02d} by" in probes for number in range(1, 22)),
            "ten interacting challenges and explicit coverage of twenty-one rules", checks)
    require("The first cup and the later account" in probes and
            "CAN-E19, E32, E44–E45" in probes,
            "constructed first-audience interaction is explicitly unrun", checks)
    cases = json.loads((packet_artifact(HERE, "AUDIO_MATCHED_SEMANTIC_CASES.json")).read_text(encoding="utf-8"))
    require(cases["semantic_cases"] == 23 and len(cases["cases"]) == 23,
            "23 matched semantic cases", checks)
    crosswalk = (packet_artifact(HERE, "WUWA_CANTARELLA_AV_HUMAN_RETRIEVAL_CROSSWALK.md")).read_text(encoding="utf-8")
    require(all(f"`{case['text_key']}`" in crosswalk for case in cases["cases"]),
            "all 23 exact sound cases occur in AV crosswalk", checks)
    require("Sonoro" in crosswalk and "not literal" in crosswalk,
            "mediated-memory caution in AV crosswalk", checks)
    require(all(token in crosswalk for token in
                ("CAN-R09", "CAN-R10", "CAN-R11", "Main_Linaxita_2_4_128_14",
                 "Main_Linaxita_2_4_143_21", "Character_Cantarella_123_38",
                 "44 of those objects")),
            "new runtime controls and ten exact-key sound nominations retain variant caution", checks)
    require(all(token in crosswalk for token in
                ("CAN-R12", "Main_Linaxita_2_4_8_2", "Main_Linaxita_2_4_8_3",
                 "Main_Linaxita_2_4_8_4", "Main_Linaxita_2_4_8_8",
                 "Main_Linaxita_2_4_8_9", "Main_Linaxita_2_4_8_27")),
            "first-audience exact-line nominations and runtime route control present", checks)
    ghost_nominations = (2, 6, 11, 13, 15, 18, 24, 25)
    require("CAN-R13" in crosswalk and all(
                f"`Character_Cantarella_134_{suffix}`" in crosswalk
                for suffix in ghost_nominations),
            "ghost-game runtime control and eight exact-line nominations present", checks)
    require(sum(len(case["renders"]) for case in cases["cases"]) == 92,
            "92 selected render variants", checks)
    require(sum(render["event_id"] is None and render["numeric_media_id"] is None
                for case in cases["cases"] for render in case["renders"]) == 48,
            "48 paired-null event and numeric-media mappings", checks)
    require(all({render["language"] for render in case["renders"]} == LANGUAGES
                for case in cases["cases"]), "each case has four dubs", checks)
    require(all(len(render[name]) == 64 for case in cases["cases"] for render in case["renders"]
                for name in ("wem_sha256", "canonical_pcm_sha256", "flac_sha256")),
            "selected render hashes present", checks)
    result = {"packet": "Cantarella", "scope": "CANTARELLA_PINNED_3_6_0_TEXT_AUDIO_PRE_AV",
              "checks": checks, "source_crosscheck": "not_requested"}
    if source_root is not None:
        source = source_root / "ANALYSIS" / "Characters" / "Cantarella"
        voice = source_root / "_voice_media" / "character" / "complete_voice_corpus" / "Cantarella" / "v0_1"
        summary = source_root / "_research" / "character_packets" / "Cantarella" / "audio_work" / "AUDIO_MEASUREMENT_SUMMARY.json"
        audit = json.loads((source / "COLLECTION_AUDIT.json").read_text(encoding="utf-8"))
        direct = audit["scopes"]["direct_character"]
        require(audit["valid"] and direct["voice_completeness_valid"],
                "selected collection audit valid", checks)
        require((audit["raw_flow_states"], audit["context_text_keys"],
                 audit["quest_references"], audit["distinct_quest_ids"]) ==
                (200, 2649, 65, 16), "contextual collection denominator", checks)
        require((direct["candidate_occurrences"], direct["accepted_occurrences"],
                 direct["source_voiced"], direct["source_unvoiced"]) ==
                (901, 885, 780, 105), "direct occurrence denominator", checks)
        require((direct["semantic_voice_lines"], direct["render_associations"],
                 direct["unique_flac_objects"]) ==
                (845, 3389, 3237), "voice line, association, object denominators", checks)
        decisions = jsonl(source / "occurrence_identity_crosswalk.jsonl")
        require(Counter(row["character_attribution"] for row in decisions) ==
                {"accepted_solo": 885, "rejected": 9, "unresolved": 7},
                "identity crosswalk counts", checks)
        unvoiced_actions = {(7472, 6): 9, (7088, 8): 3, (7089, 6): 8,
                            (7344, 6): 6, (7345, 5): 7}
        require(all(
            len(rows := [row for row in decisions
                         if row["flow_state_row_index"] == state and
                         row["action_index"] == action]) == count and
            all(row["character_attribution"] == "accepted_solo" and
                row["play_voice"] is False for row in rows)
            for (state, action), count in unvoiced_actions.items()),
            "tower, mixed-power and ordinary-tea actions are accepted but source-unvoiced",
            checks)
        witnesses = {row["text_key"]: row["values"] for row in
                     jsonl(source / "CONTEXT_TEXT_WITNESSES.jsonl")}
        package = json.loads((source / "character_source_package.json").read_text(encoding="utf-8"))
        ascensions = {row["content"]["text_key"]: row for row in package["favor_words"]
                      if 160727 <= row["id"] <= 160731}
        require(len(ascensions) == 5, "five source-package ascension rows", checks)
        for offset in range(5):
            key = f"FavorWord_{160726 + offset}_Content"
            row = ascensions[key]
            require((row["id"], row["raw"]["Id"], row["sort"]) ==
                    (160727 + offset, 160727 + offset, 27 + offset),
                    f"ascension key/raw-row offset and sort: {key}", checks)
            require(row["source_locator"].endswith(f"favorword.json#/{1984 + offset}")
                    and row["title"]["values"]["en"]["content"] ==
                    f"Ascension: {['I', 'II', 'III', 'IV', 'V'][offset]}",
                    f"ascension locator and title: {key}", checks)
            require(row["voice_asset"].endswith(
                f"play_favor_word_kanteleila_sys_rankup0{offset + 1}"),
                    f"ascension source event path: {key}", checks)
            require(all(row["content"]["values"][lang]["status"] == "resolved"
                        for lang in ("en", "ja", "ko", "zh-Hans")),
                    f"four resolved ascension witnesses: {key}", checks)
        fourth = ascensions["FavorWord_160729_Content"]["content"]["values"]
        require("无人可以知晓大海的心意" in fourth["zh-Hans"]["content"]
                and "deepest secret" in fourth["en"]["content"]
                and "宝が眠る在処" in fourth["ja"]["content"]
                and "가장 깊은 비밀" in fourth["ko"]["content"],
                "Ascension IV epistemic limit and secret/treasure fork", checks)
        fifth = ascensions["FavorWord_160730_Content"]["content"]["values"]
        require("纯净之地" in fifth["zh-Hans"]["content"]
                and "place for you here" in fifth["en"]["content"]
                and "いつか必ず光を掴む" in fifth["ja"]["content"]
                and "가장 순수한 곳" in fifth["ko"]["content"],
                "Ascension V reserved refuge versus JA eventual-light fork", checks)
        inquiry = witnesses["Character_Cantarella_124_6"]
        require("难以追究" in inquiry["zh-Hans"]["content"] and
                "remains buried" in inquiry["en"]["content"] and
                "誰にも深堀り" in inquiry["ja"]["content"] and
                "수도회가" in inquiry["ko"]["content"],
                "four-language inquiry-audience divergence", checks)
        cheri = witnesses["Character_Cantarella_124_4"]
        require("试炼的时候" in cheri["zh-Hans"]["content"] and
                "during the trials" in cheri["en"]["content"] and
                "試練の時" in cheri["ja"]["content"] and
                "같이 시련을 겪었을 때" in cheri["ko"]["content"],
                "Cheri's four-language trial-era recollection", checks)
        require("吉尔贝" in witnesses["Main_Linaxita_2_4_8_2"]["zh-Hans"]["content"]
                and "Gilberto" in witnesses["Main_Linaxita_2_4_8_2"]["en"]["content"]
                and "墨渍" in witnesses["Main_Linaxita_2_4_8_3"]["zh-Hans"]["content"]
                and "過去の過ち" in witnesses["Main_Linaxita_2_4_8_3"]["ja"]["content"]
                and "sorrow" in witnesses["Main_Linaxita_2_4_8_3"]["en"]["content"],
                "four-locale first-audience apology and metaphor fork", checks)
        require("饮茶" in witnesses["Main_Linaxita_2_4_8_5"]["zh-Hans"]["content"]
                and "推开茶杯" in witnesses["Main_Linaxita_2_4_8_6"]["zh-Hans"]["content"]
                and "先像这样放到一边" in witnesses["Main_Linaxita_2_4_8_8"]["zh-Hans"]["content"]
                and "serve as a mediator" in witnesses["Main_Linaxita_2_4_8_9"]["en"]["content"]
                and "once you learn everything" in witnesses["Main_Linaxita_2_4_8_29"]["en"]["content"],
                "tea refusal, temporary set-aside, common request and staged disclosure wording", checks)
        ghost_text = lambda suffix, lang: witnesses[
            f"Character_Cantarella_134_{suffix}"][lang]["content"]
        require(all(witnesses[f"Character_Cantarella_134_{suffix}"][lang]["status"] ==
                    "resolved" for suffix in range(1, 26)
                    for lang in ("zh-Hans", "en", "ja", "ko")) and
                "并没有恶魔" in ghost_text(2, "zh-Hans") and
                "向「举办者」求得" in ghost_text(5, "zh-Hans") and
                "this potion is here to make it real" in ghost_text(6, "en") and
                "已经被深深牵扯" in ghost_text(15, "zh-Hans") and
                "too late to withdraw" in ghost_text(15, "en") and
                "按信上所言" in ghost_text(16, "zh-Hans") and
                "秘药" in ghost_text(25, "zh-Hans") and
                "毒药" in ghost_text(25, "zh-Hans") and
                all(ghost_text(a, lang) == ghost_text(a + 2, lang)
                    for a in (11, 12) for lang in ("zh-Hans", "en", "ja", "ko")),
                "ghost-game four-language promise, letter leverage and same-written route pairs",
                checks)
        flow = {int(row["source_locator"].rsplit("/", 1)[1]): row["raw"]
                for row in jsonl(source / "RAW_RELEVANT_FLOW_STATES.jsonl")}
        audience_states = {
            6799: "剧情_2_2_阿维纽林主线_3_9",
            6800: "剧情_2_2_阿维纽林主线_3_10",
            6801: "剧情_2_2_阿维纽林主线_3_11",
        }
        require(all(flow[index]["StateKey"] == state
                    for index, state in audience_states.items()),
                "first-audience introduction, tea and following request are distinct numbered states", checks)
        late_keys = {
            8876: "剧情_2_7_黎那汐塔主线_上半_1_34_1",
            8877: "剧情_2_7_黎那汐塔主线_上半_1_35_1",
        }
        require(all(flow[index]["StateKey"] == key for index, key in late_keys.items()),
                "two consecutive Chapter 2.7 state identities", checks)
        quest_refs = jsonl(source / "QUEST_CONTEXT_REFERENCES.jsonl")
        ghost_state = "剧情_2_2_角色_坎特蕾拉线_1_14"
        require(flow[6701]["StateKey"] == ghost_state and
                any(str(row["quest_id"]) == "880000033" and
                    row["source_locator"].endswith("plothandbookconfig.json#/37") and
                    any(ref["state_key"] == ghost_state and
                        ref["pointer"] == "/9/Flow"
                        for ref in row["matching_references"])
                    for row in quest_refs) and
                not any("QuestNodeData/" in row["source_locator"] and
                        any(ref["state_key"] == ghost_state
                            for ref in row["matching_references"])
                        for row in quest_refs),
                "ghost-game exact handbook pointer without selected quest-node match", checks)
        ghost_action = json.loads(flow[6701]["Actions"])[6]
        ghost_params = ghost_action["Params"]
        ghost_items = ghost_params["TalkItems"]
        ghost_options = ghost_items[5]["Options"]
        require(ghost_action["Name"] == "ShowTalk" and len(ghost_items) == 20 and
                not ghost_params.get("TalkSequence") and
                not ghost_params.get("SequenceTransitions") and
                all(item.get("WhoId") == 150009 and item.get("PlayVoice") is True
                    for item in ghost_items) and
                [option["PlotLineKey"] for option in ghost_options] ==
                    [f"Character_Cantarella_134_{suffix}" for suffix in (7, 8, 9, 10)] and
                [option["Actions"][0]["Params"]["TalkId"]
                 for option in ghost_options] == [7, 9, 11, 14] and
                [ghost_items[index]["Id"] for index in (6, 8, 10, 13)] ==
                    [7, 9, 11, 14] and ghost_items[9]["Id"] == 0 and
                [ghost_items[index]["Actions"][0]["Params"]["TalkId"]
                 for index in (7, 9, 12)] == [18, 18, 18] and
                [option["Actions"][0]["Params"]["TalkId"]
                 for option in ghost_items[16]["Options"]] == [18] and
                [ghost_items[index]["Id"] for index in (17, 18, 19)] == [18, 19, 20],
                "ghost-game four option targets, distinct middles and common ID-18 rejoin",
                checks)
        require(any(str(row["quest_id"]) == "145000005"
                    and row["source_locator"].endswith("questnodedata.json#/10625")
                    and row["raw"]["Key"] == "145000005_414"
                    and any(ref["pointer"] == "/Condition/Flow"
                            and ref["state_key"] == audience_states[6800]
                            for ref in row["matching_references"])
                    for row in quest_refs)
                and any(str(row["quest_id"]) == "145000005"
                        and row["source_locator"].endswith("plothandbookconfig.json#/36")
                        and any(ref["state_key"] == audience_states[6800]
                                for ref in row["matching_references"])
                        for row in quest_refs),
                "first-audience tea state has direct quest-node and handbook pointers", checks)
        audience = json.loads(flow[6800]["Actions"])[9]
        audience_items = audience["Params"]["TalkItems"]
        audience_sequences = audience["Params"]["TalkSequence"]
        audience_transitions = audience["Params"]["SequenceTransitions"]
        require(audience["Name"] == "ShowTalk" and len(audience_items) == 26
                and audience_sequences == [list(range(1, 5)), [5], [6], list(range(7, 27))]
                and [(option["OptionTextKey"], option["NextSequenceIndex"])
                     for option in audience_transitions["0"]] == [
                         ("Main_Linaxita_2_4_8_5", 1),
                         ("Main_Linaxita_2_4_8_6", 2)]
                and audience_transitions["1"][0]["NextSequenceIndex"] == 3
                and audience_transitions["2"][0]["NextSequenceIndex"] == 3,
                "first-audience four-sequence drink/refusal fork reconverges before mediation", checks)
        require(Counter(item.get("WhoId") for item in audience_items) ==
                {150009: 21, 750088: 3, None: 2}
                and all(item.get("PlayVoice") is True for item in audience_items
                        if item.get("WhoId") == 150009)
                and audience_items[4]["WhoId"] == 750088
                and audience_items[4]["TidTalk"] == "Main_Linaxita_2_4_8_7"
                and audience_items[5]["WhoId"] == 150009
                and audience_items[5]["TidTalk"] == "Main_Linaxita_2_4_8_8"
                and audience_items[6]["TidTalk"] == "Main_Linaxita_2_4_8_9"
                and all(audience_items[index]["Type"] == "Option"
                        and audience_items[index]["Options"][0]["Actions"] == []
                        for index in (19, 20)),
                "audience speaker, branch-specific replies, common request and later one-caption prompts", checks)
        require(all(any(
            str(row["quest_id"]) == "158800019" and
            any(ref["state_key"] == key for ref in row["matching_references"])
            for row in quest_refs) for key in late_keys.values()),
            "both late states directly join quest 158800019", checks)
        choice_specs = (
            (6811, 2, 145000005, "剧情_2_2_阿维纽林主线_11_24", "questnodedata.json#/10698"),
            (5775, 5, 145000005, "剧情_2_2_阿维纽林主线_12_2", "questnodedata.json#/11062"),
            (7315, 7, 880000033, "剧情_2_2_角色_坎特蕾拉线_副本_14_1", "plothandbookconfig.json#/37"),
        )
        for row_index, action_index, quest_id, state_key, locator_suffix in choice_specs:
            require(flow[row_index]["StateKey"] == state_key and
                    any(str(row["quest_id"]) == str(quest_id) and
                        row["source_locator"].endswith(locator_suffix) and
                        any(ref["state_key"] == state_key
                            for ref in row["matching_references"])
                        for row in quest_refs),
                    f"exact state and quest reference for choice scene {row_index}/{action_index}",
                    checks)
        tyrvine = json.loads(flow[6811]["Actions"])[2]["Params"]
        sword_items = tyrvine["TalkItems"]
        require(len(sword_items) == 34 and
                tyrvine["TalkSequence"] == [list(range(1, 35))] and
                sum(item.get("WhoId") == 150009 and item.get("PlayVoice") is True
                    for item in sword_items) == 28 and
                sword_items[13]["TidTalk"] == "Main_Linaxita_2_4_128_14" and
                sword_items[13]["WhoId"] == 150009 and
                sword_items[14]["WhoId"] == 50074 and
                sword_items[25]["TidTalk"] == "Main_Linaxita_2_4_128_26",
                "Tyrvine argument has one ordered speaker-specific source sequence", checks)
        pledge_items = json.loads(flow[5775]["Actions"])[5]["Params"]["TalkItems"]
        require(len(pledge_items) == 32 and
                sum(item.get("WhoId") == 150009 and item.get("PlayVoice") is True
                    for item in pledge_items) == 25 and
                pledge_items[12]["TidTalk"] == "Main_Linaxita_2_4_143_15" and
                [option["Actions"][0]["Params"]["TalkId"]
                 for option in pledge_items[12]["Options"]] == [14, 17, 23] and
                all(pledge_items[index]["Actions"][0]["Params"]["TalkId"] == 25
                    for index in (21, 23)) and
                pledge_items[14]["TidTalk"] == "Main_Linaxita_2_4_143_21" and
                pledge_items[29]["TidTalk"] == "Main_Linaxita_2_4_143_40",
                "Bloodpact gift has three exclusive initial requests and common later message", checks)
        return_items = json.loads(flow[7315]["Actions"])[7]["Params"]["TalkItems"]
        require(len(return_items) == 34 and
                sum(item.get("WhoId") == 150009 and item.get("PlayVoice") is True
                    for item in return_items) == 28 and
                all(return_items[index]["WhoId"] == 50135 for index in (0, 1, 2, 3, 4, 24)) and
                return_items[14]["TidTalk"] == "Character_Cantarella_123_17" and
                return_items[29]["TidTalk"] == "Character_Cantarella_123_34" and
                [option["Actions"][0]["Params"]["TalkId"]
                 for option in return_items[29]["Options"]] == [31, 32] and
                return_items[30]["Actions"][0]["Params"]["TalkId"] == 34 and
                return_items[32]["Actions"][0]["Params"]["TalkId"] == 34 and
                return_items[33]["TidTalk"] == "Character_Cantarella_123_40",
                "Cheri testimony, staged return and optional reputation reply have distinct source edges", checks)
        require("选择拿起" in witnesses["Main_Linaxita_2_4_128_14"]["zh-Hans"]["content"] and
                "choose to wield" in witnesses["Main_Linaxita_2_4_128_14"]["en"]["content"] and
                "为何不能" in witnesses["Main_Linaxita_2_4_128_26"]["zh-Hans"]["content"] and
                "ほかない" in witnesses["Main_Linaxita_2_4_128_26"]["ja"]["content"],
                "Tyrvine choice and real/false Maiden wording retain ZH/EN/JA distinction", checks)
        require(all("Male=" in witnesses["Main_Linaxita_2_4_143_21"][lang]["content"] and
                    "Female=" in witnesses["Main_Linaxita_2_4_143_21"][lang]["content"]
                    for lang in ("zh-Hans", "en", "ja", "ko")) and
                "愛し合って" in witnesses["Main_Linaxita_2_4_143_21"]["ja"]["content"] and
                "两天" in witnesses["Main_Linaxita_2_4_143_40"]["zh-Hans"]["content"] and
                "二、三日" in witnesses["Main_Linaxita_2_4_143_40"]["ja"]["content"] and
                "A few more" in witnesses["Main_Linaxita_2_4_143_40"]["en"]["content"],
                "Bloodpact gender and two-versus-two-or-three-day locale forks retained", checks)
        require("声称" in witnesses["Character_Cantarella_123_17"]["zh-Hans"]["content"] and
                "claim that" in witnesses["Character_Cantarella_123_17"]["en"]["content"] and
                "あの子" in witnesses["Character_Cantarella_123_21"]["ja"]["content"] and
                "이야기" in witnesses["Character_Cantarella_123_34"]["ko"]["content"] and
                "保持警惕" in witnesses["Character_Cantarella_123_38"]["zh-Hans"]["content"],
                "staged elixir, tentative sender and warranted family wariness have locale witnesses", checks)
        pinned_base = source_root / "_sources" / "Arikatsu_WutheringWaves_Data"
        quest_nodes = json.loads((pinned_base / "BinData" / "QuestTree" /
                                  "questtreenode.json").read_text(encoding="utf-8"))
        for index, node_id, quest_array, summary_key, quest_type in (
                (46, 220040, [880000033], "QuestTree_Summary_220040", 2),
                (67, 230401, [161750000, 161750001, 161750002],
                 "QuestTree_Summary_230401", 3)):
            node = quest_nodes[index]
            require(node["Id"] == node_id and node["QuestArray"] == quest_array and
                    node["Summary"] == summary_key and node["QuestType"] == quest_type and
                    node["PreNode"] == [210040],
                    f"Cantarella quest node {node_id} direct source link", checks)
        quest_summaries = {
            key: {
                lang: textmap_content(pinned_base / "Textmaps" / lang /
                                      "multi_text" / "MultiText.json", key)
                for lang in ("zh-Hans", "en", "ja", "ko")
            }
            for key in ("QuestTree_Summary_220040", "QuestTree_Summary_230401")
        }
        returned = quest_summaries["QuestTree_Summary_220040"]
        fragments = quest_summaries["QuestTree_Summary_230401"]
        require("救下的少女们送还" in returned["zh-Hans"] and
                "returns the girls she once saved" in returned["en"] and
                "救い出した少女たち" in returned["ja"] and
                "구한 소녀들을 돌려보냈고" in returned["ko"],
                "character-quest synopsis reports returned girls", checks)
        require("历任圣女试炼候选人的记忆碎片" in fragments["zh-Hans"] and
                "memory fragments left behind by past candidates" in fragments["en"] and
                "歴代候補者たちの記憶の断片" in fragments["ja"] and
                "역대 성녀의 시련 후보자의 기억 조각" in fragments["ko"] and
                "终有一天" in fragments["zh-Hans"] and
                "one day" in fragments["en"],
                "side-quest synopsis separates past fragments from future wish", checks)
        sparks = json.loads(flow[7088]["Actions"])[8]["Params"]["TalkItems"]
        require(len(sparks) == 5 and sparks[0]["WhoId"] == 83 and
                [sparks[index]["PlotLineKey"] for index in (1, 2, 4)] == [
                    "ZX_SHZZ_12_14", "ZX_SHZZ_12_15", "ZX_SHZZ_12_17"] and
                all(sparks[index]["WhoId"] == 150009 and
                    not sparks[index].get("PlayVoice", False)
                    for index in (1, 2, 4)),
                "spark comfort is Cantarella text with separate narration and no voice", checks)
        meteor = json.loads(flow[7089]["Actions"])[6]["Params"]["TalkItems"]
        require(len(meteor) == 11 and
                [meteor[index]["PlotLineKey"] for index in (5, 6, 8)] == [
                    "ZX_SHZZ_14_8", "ZX_SHZZ_14_9", "ZX_SHZZ_14_13"] and
                all(meteor[index]["WhoId"] == 150009 and
                    not meteor[index].get("PlayVoice", False)
                    for index in (1, 2, 4, 5, 6, 8, 9, 10)),
                "meteor wish and past correction are Cantarella source-unvoiced turns", checks)
        require("无法感知到它们的情绪" in
                witnesses["ZX_SHZZ_12_13"]["zh-Hans"]["content"] and
                "不远的将来" in witnesses["ZX_SHZZ_14_8"]["zh-Hans"]["content"] and
                "past mistakes" in witnesses["ZX_SHZZ_14_13"]["en"]["content"] and
                "過去を正し" in witnesses["ZX_SHZZ_14_13"]["ja"]["content"] and
                "과거는 바로잡아야" in witnesses["ZX_SHZZ_14_13"]["ko"]["content"],
                "spark emotion uncertainty, future wish and four-witness correction", checks)
        require("尽可能地降低了伤亡" in
                witnesses["ZX_SHZZ_15_3"]["zh-Hans"]["content"] and
                "minimize the loss of life" in
                witnesses["ZX_SHZZ_15_3"]["en"]["content"],
                "Imperator account claims harm reduction, not zero casualties", checks)
        farewell = json.loads(flow[6607]["Actions"])[6]["Params"]["TalkItems"]
        require(farewell[3]["WhoId"] == 50135 and
                farewell[3]["TidTalk"] == "Character_Cantarella_124_4" and
                farewell[5]["TidTalk"] == "Character_Cantarella_124_6",
                "Cheri distinct speaker precedes headship bargain", checks)
        postquest = json.loads(flow[6620]["Actions"])[3]["Params"]
        talk = postquest["TalkItems"]
        require(talk[25]["TidTalk"] == "Character_Cantarella_127_32" and
                {item["Actions"][0]["Params"]["TalkId"] for item in
                 talk[25]["Options"]} == {27, 28} and
                [talk[i]["TidTalk"] for i in (26, 27)] ==
                ["Character_Cantarella_127_35", "Character_Cantarella_127_36"] and
                all(talk[i]["Actions"][0]["Params"]["TalkId"] == 29
                    for i in (26, 27)),
                "common secrets offer branches to exclusive replies then rejoins", checks)
        mixed = json.loads(flow[7472]["Actions"])[6]["Params"]["TalkItems"]
        require([mixed[index]["TidTalk"] for index in (7, 8, 9, 10, 11)] ==
                [f"ZX_SHZZ_15_{number}" for number in range(8, 13)] and
                all(mixed[index]["WhoId"] == 150009 and
                    not mixed[index].get("PlayVoice", False)
                    for index in (7, 8, 9, 10, 11)),
                "mixed-frequency refusal and children's choice are Cantarella's source-unvoiced turns", checks)
        require("孩子们" in witnesses["ZX_SHZZ_15_10"]["zh-Hans"]["content"] and
                "not mine alone" in witnesses["ZX_SHZZ_15_10"]["en"]["content"] and
                "daughters of the Fisalia family" in
                witnesses["ZX_SHZZ_15_9"]["en"]["content"] and
                all(witnesses["ZX_SHZZ_15_12"][lang]["status"] == "resolved"
                    for lang in ("zh-Hans", "en", "ja", "ko")),
                "children's mixed-frequency claim has four resolved textual witnesses", checks)
        late_voiced = json.loads(flow[8876]["Actions"])[6]["Params"]["TalkItems"]
        late_menu = json.loads(flow[8877]["Actions"])[4]["Params"]["TalkItems"]
        cantarella_indices = (0, 1, 2, 9, 21, 22, 23, 24, 25, 31)
        require(len(late_voiced) == 43 and
                tuple(index for index, item in enumerate(late_voiced)
                      if item.get("WhoId") == 150009) == cantarella_indices and
                all(late_voiced[index].get("PlayVoice") is True
                    for index in cantarella_indices),
                "ten Cantarella turns are source-voiced within late multi-speaker action", checks)
        require(len(late_menu) == 34 and
                all(item.get("WhoId") == 150009 and "PlayVoice" not in item
                    for item in late_menu),
                "all 34 menu turns belong to Cantarella and omit raw PlayVoice", checks)
        require(len(late_menu[3]["Options"]) == 3 and
                not late_menu[3]["Options"][0]["Actions"] and
                [option["Actions"][0]["Params"]["TalkId"]
                 for option in late_menu[3]["Options"][1:]] == [32, 32] and
                [option["Actions"][0]["Params"]["TalkId"]
                 for option in late_menu[4]["Options"]] == [6, 12, 19, 25, 32, 32] and
                [late_menu[index]["Actions"][0]["Params"]["TalkId"]
                 for index in (10, 17, 23, 30)] == [5, 5, 5, 5],
                "optional records topics and departure edges remain distinct", checks)
        late_text = lambda suffix, lang: witnesses[
            f"Main_Rinascita_2_11_{suffix}"][lang]["content"]
        require("秘药" in late_text("431_1", "zh-Hans") and
                "antidote" in late_text("431_1", "en") and
                "重新还原" in late_text("431_24", "zh-Hans") and
                "begin to make sense again" in late_text("431_24", "en"),
                "medicine and restored-record four-witness distinctions", checks)
        require("未" in late_text("44_8", "zh-Hans") and
                "what I can" in late_text("44_8", "en") and
                "해독이 끝난 후" in late_text("44_8", "ko") and
                "希望与转机" in late_text("44_34", "zh-Hans") and
                "another way" in late_text("44_34", "en") and
                "目前" in late_text("44_35", "zh-Hans") and
                "For now" in late_text("44_35", "en") and
                "商议解决" in late_text("44_43", "zh-Hans") and
                "stand with" in late_text("44_43", "en"),
                "partial disclosure, present hope/status and coalition witness limits", checks)
        line_rows = jsonl(voice / "COMPLETE_VOICE_LINE_ANALYSIS.jsonl")
        require(len(line_rows) == 845, "845 selected semantic voice rows", checks)
        index = {(row["text_key"], row["semantic_voice_occurrence_id"]): row for row in line_rows}
        by_locator = {row["source_locator"]: row for row in line_rows}
        ghost_cohort = [row for row in line_rows if
                        "/6701/Actions!/6/Params/TalkItems/" in row["source_locator"]]
        ghost_renders = [render for row in ghost_cohort for render in row["renders"]]
        require(len(ghost_cohort) == 20 and len(ghost_renders) == 80 and
                {row["source_locator"].rsplit("/", 1)[1] for row in ghost_cohort} ==
                    {str(index) for index in range(20)} and
                all(row["technical_speaker_id"] == 150009 and
                    row["text_key"] == ghost_items[
                        int(row["source_locator"].rsplit("/", 1)[1])]["TidTalk"] and
                    len(row["renders"]) == 4 and
                    {render["voice_language"] for render in row["renders"]} == LANGUAGES
                    for row in ghost_cohort),
                "ghost-game twenty authored Cantarella occurrence/text joins retain four dubs", checks)
        require(len({render["canonical_pcm_sha256"] for render in ghost_renders}) == 80 and
                all(render.get("event_id") is None and
                    render.get("bank_id") is None and
                    render.get("numeric_media_id") is None and
                    render["source_wem_exists"] and render["source_wem_sha256_verified"] and
                    render["materialization_status"] == "flac_roundtrip_pcm_identical" and
                    (source_root / render["flac_relative_path"]).is_file()
                    for render in ghost_renders),
                "ghost-game eighty distinct source-WEM-verified, roundtrip-valid paired-null renders",
                checks)
        ghost_by_key = {row["text_key"]: row for row in ghost_cohort}
        require(sum(len(ghost_by_key[f"Character_Cantarella_134_{suffix}"]["renders"])
                    for suffix in ghost_nominations) == 32 and
                all(ghost_by_key[f"Character_Cantarella_134_{suffix}"]["source_locator"] ==
                    f"wuwa://{COMMIT}/BinData/flowState/flowstate.json#/6701/Actions!/6/Params/TalkItems/{item_index}"
                    for suffix, item_index in ((2, 1), (6, 5), (11, 6), (13, 8),
                                               (15, 10), (18, 13), (24, 18), (25, 19))),
                "eight exact ghost-game nominations join thirty-two source-positioned renders",
                checks)
        audience_cohort = [row for row in line_rows if
                           "/6800/Actions!/9/Params/TalkItems/" in row["source_locator"]]
        audience_renders = [render for row in audience_cohort for render in row["renders"]]
        require(len(audience_cohort) == 21 and len(audience_renders) == 84
                and all(row["technical_speaker_id"] == 150009
                        and row["text_key"] == audience_items[
                            int(row["source_locator"].rsplit("/", 1)[1])]["TidTalk"]
                        and {render["voice_language"] for render in row["renders"]} == LANGUAGES
                        for row in audience_cohort),
                "first audience has 21 exact Cantarella occurrence/text joins across two routes", checks)
        require(len({render["canonical_pcm_sha256"] for render in audience_renders}) == 84
                and all(render.get("event_id") is None
                        and render.get("numeric_media_id") is None
                        and render["source_wem_exists"]
                        and render["source_wem_sha256_verified"]
                        and render["materialization_status"] == "flac_roundtrip_pcm_identical"
                        and (source_root / render["flac_relative_path"]).is_file()
                        for render in audience_renders),
                "first audience has 84 distinct PCM-valid renders with paired-null numeric IDs", checks)
        audience_nominations = {
            1: "Main_Linaxita_2_4_8_2", 2: "Main_Linaxita_2_4_8_3",
            3: "Main_Linaxita_2_4_8_4", 5: "Main_Linaxita_2_4_8_8",
            6: "Main_Linaxita_2_4_8_9", 23: "Main_Linaxita_2_4_8_27",
        }
        require(all((row := by_locator[
                    f"wuwa://{COMMIT}/BinData/flowState/flowstate.json#/"
                    f"6800/Actions!/9/Params/TalkItems/{item_index}"])["text_key"] == key
                    and len(row["renders"]) == 4 and f"`{key}`" in crosswalk
                    for item_index, key in audience_nominations.items()),
                "six exact first-audience nominations join 24 selected render variants", checks)
        choice_renders = []
        for row_index, action_index, _quest_id, _state, _locator in choice_specs:
            expected_lines, expected_renders = {
                6811: (28, 112), 5775: (25, 104), 7315: (28, 114)
            }[row_index]
            prefix = f"/{row_index}/Actions!/{action_index}/Params/TalkItems/"
            cohort = [row for row in line_rows if prefix in row["source_locator"]]
            source_items = json.loads(flow[row_index]["Actions"])[action_index]["Params"]["TalkItems"]
            renders = [render for row in cohort for render in row["renders"]]
            require(len(cohort) == expected_lines and len(renders) == expected_renders and
                    all(row["technical_speaker_id"] == 150009 and
                        row["text_key"] == source_items[
                            int(row["source_locator"].rsplit("/", 1)[1])]["TidTalk"] and
                        {render["voice_language"] for render in row["renders"]} == LANGUAGES
                        for row in cohort),
                    f"choice scene {row_index} exact source speaker/text and selected line count", checks)
            require(len({render["canonical_pcm_sha256"] for render in renders}) == len(renders) and
                    all(render.get("event_id") is None and
                        render.get("numeric_media_id") is None and
                        render["materialization_status"] == "flac_roundtrip_pcm_identical" and
                        render["source_wem_exists"] and
                        render["source_wem_sha256_verified"] and
                        (source_root / render["flac_relative_path"]).is_file()
                        for render in renders),
                    f"choice scene {row_index} distinct PCM-valid paired-null render joins", checks)
            choice_renders.extend(renders)
        require(len(choice_renders) == 330 and
                len({render["canonical_pcm_sha256"] for render in choice_renders}) == 330 and
                len({render["flac_sha256"] for render in choice_renders}) == 330,
                "81 choice-scene semantic lines have 330 distinct local PCM/FLAC objects", checks)
        pledge_variant = by_locator[
            f"wuwa://{COMMIT}/BinData/flowState/flowstate.json#/5775/Actions!/5/Params/TalkItems/14"]
        return_variant = by_locator[
            f"wuwa://{COMMIT}/BinData/flowState/flowstate.json#/7315/Actions!/7/Params/TalkItems/6"]
        require(pledge_variant["text_key"] == "Main_Linaxita_2_4_143_21" and
                len(pledge_variant["renders"]) == 8 and
                Counter(render["voice_language"] for render in pledge_variant["renders"]) ==
                {"en": 2, "ja": 2, "ko": 2, "zh": 2} and
                return_variant["text_key"] == "Character_Cantarella_123_7" and
                len(return_variant["renders"]) == 6 and
                Counter(render["voice_language"] for render in return_variant["renders"]) ==
                {"en": 2, "ja": 2, "ko": 1, "zh": 1},
                "six additional objects are render variants of two semantic lines", checks)
        choice_nominations = (
            (6811, 2, 13, "Main_Linaxita_2_4_128_14"),
            (6811, 2, 25, "Main_Linaxita_2_4_128_26"),
            (5775, 5, 14, "Main_Linaxita_2_4_143_21"),
            (5775, 5, 18, "Main_Linaxita_2_4_143_28"),
            (5775, 5, 29, "Main_Linaxita_2_4_143_40"),
            (7315, 7, 14, "Character_Cantarella_123_17"),
            (7315, 7, 16, "Character_Cantarella_123_21"),
            (7315, 7, 25, "Character_Cantarella_123_30"),
            (7315, 7, 29, "Character_Cantarella_123_34"),
            (7315, 7, 31, "Character_Cantarella_123_38"),
        )
        nomination_rows = [by_locator[
            f"wuwa://{COMMIT}/BinData/flowState/flowstate.json#/"
            f"{row_index}/Actions!/{action_index}/Params/TalkItems/{item_index}"]
            for row_index, action_index, item_index, _key in choice_nominations]
        require(all(row["text_key"] == key and f"`{key}`" in crosswalk
                    for row, (*_indices, key) in zip(nomination_rows, choice_nominations)) and
                sum(len(row["renders"]) for row in nomination_rows) == 44,
                "ten exact nominated semantic keys have forty-four selected render variants", checks)
        late_voice = [by_locator[
            f"wuwa://{COMMIT}/BinData/flowState/flowstate.json#/8876/Actions!/6/Params/TalkItems/{index}"]
            for index in cantarella_indices]
        require(all(row["text_key"] == late_voiced[index]["TidTalk"] and
                    {render["voice_language"] for render in row["renders"]} == LANGUAGES and
                    all(render["materialization_status"] == "flac_roundtrip_pcm_identical" and
                        render.get("event_id") is None and
                        render.get("numeric_media_id") is None and
                        (source_root / render["flac_relative_path"]).is_file()
                        for render in row["renders"])
                    for index, row in zip(cantarella_indices, late_voice)),
                "ten late voiced turns have forty selected PCM-valid renders without explicit event/media IDs", checks)
        require(not any("#/8877/Actions!/4/Params/TalkItems/" in row["source_locator"]
                        for row in line_rows),
                "unvoiced records menu has no selected decoded voice row", checks)
        late_nominations = ((0, "431_1"), (1, "431_47"), (21, "431_24"),
                            (22, "431_25"), (24, "431_27"), (31, "431_34"))
        require(all(late_voiced[index]["TidTalk"] ==
                    f"Main_Rinascita_2_11_{suffix}" and
                    len(by_locator[f"wuwa://{COMMIT}/BinData/flowState/flowstate.json#/8876/Actions!/6/Params/TalkItems/{index}"]["renders"]) == 4 and
                    f"Main_Rinascita_2_11_{suffix}" in crosswalk
                    for index, suffix in late_nominations),
                "six exact late-story retrieval nominations carry twenty-four render joins", checks)
        trigger_rows = sorted((row for row in package["favor_words"]
                               if 160732 <= row["id"] <= 160765),
                              key=lambda row: row["id"])
        require(len(trigger_rows) == 34 and all(
            row["content"]["text_key"] == f"FavorWord_{row['id'] - 1}_Content" and
            row["source_locator"].endswith(
                f"favorword.json#/{2234 if row['id'] == 160765 else 1989 + offset}")
            for offset, row in enumerate(trigger_rows)),
            "34 trigger raw IDs, actual text keys and exact source locators", checks)
        trigger_voice = [by_locator[row["source_locator"]] for row in trigger_rows]
        require(all(
            voice_row["text_key"] == source_row["content"]["text_key"] and
            all(voice_row["text_witnesses"][language]["content"] ==
                source_row["content"]["values"][source_language]["content"]
                for language, source_language in (("zh", "zh-Hans"), ("en", "en"),
                                                  ("ja", "ja"), ("ko", "ko"))) and
            {render["voice_language"] for render in voice_row["renders"]} == LANGUAGES and
            all(render["event_path"] == source_row["voice_asset"] and
                render["event_id"] == render["bank_id"] and
                render["numeric_media_id"] is not None and
                render["materialization_status"] == "flac_roundtrip_pcm_identical" and
                render["machine_acoustic_observations"]["channels"] == 1 and
                (source_root / render["flac_relative_path"]).is_file()
                for render in voice_row["renders"])
            for source_row, voice_row in zip(trigger_rows, trigger_voice)),
            "trigger text, event/bank/media, four-dub PCM and file joins", checks)
        trigger_renders = [render for row in trigger_voice for render in row["renders"]]
        require(len(trigger_renders) == 136 and
                len({render["canonical_pcm_sha256"] for render in trigger_renders}) == 136 and
                len({render["flac_sha256"] for render in trigger_renders}) == 136 and
                len({render["event_id"] for render in trigger_renders}) == 34,
                "136 distinct trigger PCM/FLAC objects from 34 event IDs with bank fields", checks)
        trigger_by_id = {row["id"]: row for row in trigger_rows}
        thought_two = next(row for row in package["favor_words"] if row["id"] == 160702)
        require("别眨眼哦" in thought_two["content"]["values"]["zh-Hans"]["content"] and
                "别眨眼哦" in trigger_by_id[160734]["content"]["values"]["zh-Hans"]["content"] and
                "捉えられるかしら" in trigger_by_id[160734]["content"]["values"]["ja"]["content"] and
                "一起遨游吧" in trigger_by_id[160736]["content"]["values"]["zh-Hans"]["content"] and
                "一緒に泳ぎましょう" in trigger_by_id[160736]["content"]["values"]["ja"]["content"] and
                "함께 헤엄칠까" in trigger_by_id[160736]["content"]["values"]["ko"]["content"] and
                "Feel the tide pull" in trigger_by_id[160736]["content"]["values"]["en"]["content"] and
                "海の慈悲" in trigger_by_id[160738]["content"]["values"]["ja"]["content"] and
                "Sleep, in the whispers of sirens" in
                trigger_by_id[160747]["content"]["values"]["en"]["content"] and
                "海的呢喃" in trigger_by_id[160747]["content"]["values"]["zh-Hans"]["content"] and
                "海の囁き" in trigger_by_id[160747]["content"]["values"]["ja"]["content"] and
                "바다의 축복" in trigger_by_id[160747]["content"]["values"]["ko"]["content"],
                "trigger/favor lexical echo and four-witness localization forks", checks)
        nominated_ids = (160734, 160736, 160738, 160742, 160747, 160748, 160754)
        require(all(
            f"CAN-TR-{number:02d}" in crosswalk and
            f"favorword#/{int(row['source_locator'].rsplit('/', 1)[1])}" in crosswalk and
            str(by_locator[row["source_locator"]]["renders"][0]["event_id"]) in crosswalk and
            all(str(render["numeric_media_id"]) in crosswalk
                for render in by_locator[row["source_locator"]]["renders"])
            for number, row in enumerate((trigger_by_id[item] for item in nominated_ids), 1)),
            "seven trigger nominations preserve exact source, event and four media IDs", checks)
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
                 audio["repeated_pcm_manifest_rows"]) == (3237, 3237, 3),
                "full local audio measurement counts", checks)
        require(not audio["failed_objects"], "no local audio measurement failures", checks)
        cohort_path = source_root / "_research" / "character_packets" / "Cantarella" / \
            "audio_work" / "CANTARELLA_SOURCE_COHORT_AUDIT.json"
        cohort_bytes = cohort_path.read_bytes()
        cohorts = json.loads(cohort_bytes)
        expected_cohorts = {
            ("garden_invitation", ("6596/3",), 31, 124),
            ("sonoro_caution", ("6862/4", "6863/1"), 9, 36),
            ("main_crisis_exposition", ("6801/3", "6811/2"), 64, 256),
            ("trial_recollections", ("6909/3", "6915/2"), 18, 72),
            ("poison_handling", ("6916/1",), 8, 32),
            ("escape_hint", ("6924/1",), 11, 44),
            ("headship_accountability", ("6607/6", "6620/3"), 34, 136),
        }
        require(hashlib.sha256(cohort_bytes).hexdigest() ==
                "474420975796e9bb746c72f10735f91f7a1d305bd9fda1ef69039ba6461dbe56" and
                cohorts["source_commit"] == COMMIT and
                cohorts["line_analysis_sha256"] == audio["line_analysis_sha256"],
                "source-cohort audit hash and line-generation pin", checks)
        require({(row["name"], tuple(row["source_actions"]), row["semantic_lines"],
                  row["render_associations"]) for row in cohorts["cohorts"]} ==
                expected_cohorts,
                "seven disjoint source-defined audio cohorts and denominators", checks)
        cohort_members = [member for cohort in cohorts["cohorts"]
                          for member in cohort["members"]]
        require(len(cohort_members) == 700 and
                len({member["semantic_voice_occurrence_id"] for member in cohort_members}) == 175 and
                len({member["canonical_pcm_sha256"] for member in cohort_members}) == 700 and
                all(stat["measured_objects"] == stat["integrity_pass_objects"] ==
                    stat["channel_counts"].get("1", 0)
                    for cohort in cohorts["cohorts"]
                    for stat in cohort["language_statistics"].values()) and
                cohorts["human_perceptual_review_performed"] is False,
                "700 distinct integrity-valid mono renders without claimed listening", checks)
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
