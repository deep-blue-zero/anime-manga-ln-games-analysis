#!/usr/bin/env python3
"""Check Changli draft packet structure, media joins and optional private source pin."""

from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import re

HERE = Path(__file__).resolve().parent
PREFIX = "WUWA_CHANGLI_"
COMMIT = "353f2eaed119bc9f680eab92807d20ac75a79b40"
LANGUAGES = {"en", "ja", "ko", "zh"}
MEDIA_SUFFIXES = {".wav", ".flac", ".wem", ".mp3", ".mp4", ".png", ".webp", ".pak"}


def jsonl(path: Path) -> list[dict]:
    with path.open(encoding="utf-8") as handle:
        return [json.loads(line) for line in handle if line.strip()]


def require(ok: bool, note: str, checks: list[str]) -> None:
    if not ok:
        raise AssertionError(note)
    checks.append(note)


def validate(source_root: Path | None) -> dict:
    checks: list[str] = []
    matrix = (HERE / f"{PREFIX}EVIDENCE_AND_FALSIFICATION_MATRIX.md").read_text(encoding="utf-8")
    evidence = set(re.findall(r"\| (CHL-E\d{2}) \|", matrix))
    claims = set(re.findall(r"\| (CHL-C\d{2}) —", matrix))
    require(evidence == {f"CHL-E{i:02d}" for i in range(1, 44)},
            "43 contiguous evidence bundles", checks)
    require(claims == {f"CHL-C{i:02d}" for i in range(1, 39)},
            "38 contiguous claim rows", checks)
    require(not any(p.suffix.lower() in MEDIA_SUFFIXES for p in HERE.rglob("*") if p.is_file()),
            "no raw media in Git packet", checks)
    expected = (
        "ANALYSIS_PACKET_README.md", "AV_AND_HUMAN_RETRIEVAL_PLAN.md",
        "AV_HUMAN_RETRIEVAL_CROSSWALK.md",
        "CHARACTER_DEEP_DIVE_PRE_AV.md", "EVIDENCE_AND_FALSIFICATION_MATRIX.md",
        "STRATEGY_CARE_AND_MORTAL_TIME_PROFILE.md",
        "WEIQI_INVITATION_BRANCH_AND_DISCLOSURE_PROFILE.md",
        "CHRONOSORTER_HYPOTHESIS_EVIDENCE_AND_RISK_PROFILE.md",
        "GUIDANCE_INTERCESSION_AND_COMPANION_PERSPECTIVE_PROFILE.md",
        "TIME_DEVICE_AND_DREAM_HYPOTHESIS_BOUNDARY_PROFILE.md",
        "SELF_PRESERVATION_SHARED_SEARCH_AND_JINHSI_BURDEN_PROFILE.md",
        "CLAIM_REVISION_LEDGER.md",
        "MODEL_FIDELITY_AND_STRESS_TEST_PRE_AV.md",
        "RELATIONSHIP_STATE_AND_ORDINARY_LIFE_PROFILE.md",
        "ORDINARY_LIFE_AND_RECIPROCITY_PROFILE.md",
        "SOURCE_DEFINED_AUDIO_COHORT_AUDIT.md",
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
    require(len(model["rules"]) == 19 and
            {r["id"] for r in model["rules"]} ==
            {f"CHL-R{i:02d}" for i in range(1, 20)},
            "19 contiguous distinct model rules", checks)
    require(all(set(r["evidence_ids"]) <= evidence and r["probability"] is None
                for r in model["rules"]), "evidence-linked nonnumeric rules", checks)
    probes = (HERE / f"{PREFIX}MODEL_FIDELITY_AND_STRESS_TEST_PRE_AV.md").read_text(encoding="utf-8")
    require(set(re.findall(r"\| (CHL-P\d{2}) \|", probes)) ==
            {f"CHL-P{i:02d}" for i in range(1, 45)},
            "44 contiguous non-blind probes", checks)
    cases = json.loads((HERE / "AUDIO_MATCHED_SEMANTIC_CASES.json").read_text(encoding="utf-8"))
    require(cases["semantic_cases"] == 18 and len(cases["cases"]) == 18,
            "18 matched semantic cases", checks)
    crosswalk = (HERE / f"{PREFIX}AV_HUMAN_RETRIEVAL_CROSSWALK.md").read_text(encoding="utf-8")
    require(all(f"`{case['text_key']}`" in crosswalk for case in cases["cases"]),
            "all 18 exact sound cases occur in AV crosswalk", checks)
    require("flow#/3688/0/0–17" in crosswalk and "runtime_dispatch_unsupported" in crosswalk,
            "unresolved poetic narration is an explicit negative AV target", checks)
    require(set(re.findall(r"\| (CHL-R\d{2}) \|", crosswalk)) ==
            {f"CHL-R{i:02d}" for i in range(1, 22)},
            "twenty-one exact runtime/negative retrieval controls", checks)
    require(sum(len(c["renders"]) for c in cases["cases"]) == 72,
            "72 selected render variants", checks)
    require(sum(r["event_id"] is None and r["numeric_media_id"] is None
                for c in cases["cases"] for r in c["renders"]) == 44,
            "44 selected renders retain paired null event/media IDs", checks)
    require(all({r["language"] for r in c["renders"]} == LANGUAGES for c in cases["cases"]),
            "all selected cases have four dubs", checks)
    require(all(len(r[f]) == 64 for c in cases["cases"] for r in c["renders"]
                for f in ("wem_sha256", "canonical_pcm_sha256", "flac_sha256")),
            "selected media hashes present", checks)
    result = {"packet": "Changli", "scope": "CHANGLI_PINNED_3_6_0_TEXT_AUDIO_PRE_AV",
              "checks": checks, "source_crosscheck": "not_requested"}
    if source_root is not None:
        source = source_root / "ANALYSIS" / "Characters" / "Changli"
        voice = source_root / "_voice_media" / "character" / "complete_voice_corpus" / "Changli" / "v0_1"
        summary = source_root / "_research" / "character_packets" / "Changli" / "audio_work" / "AUDIO_MEASUREMENT_SUMMARY.json"
        audit = json.loads((source / "COLLECTION_AUDIT.json").read_text(encoding="utf-8"))
        direct = audit["scopes"]["direct_character"]
        require(audit["valid"] and not direct["voice_completeness_valid"],
                "collection valid, selected voice incomplete", checks)
        require((audit["raw_flow_states"], audit["context_text_keys"],
                 audit["quest_references"], audit["distinct_quest_ids"]) ==
                (154, 2657, 142, 24), "context collection denominator", checks)
        require((direct["candidate_occurrences"], direct["accepted_occurrences"],
                 direct["source_voiced"], direct["source_unvoiced"]) ==
                (661, 657, 545, 112), "direct occurrence denominator", checks)
        require((direct["semantic_voice_lines"], direct["complete_voice_lines"],
                 direct["missing_voice_lines"], direct["unresolved_reason_rows"]) ==
                (610, 592, 18, 72), "explicit eighteen-line/72-render gap", checks)
        require((direct["render_associations"], direct["runtime_object_rows"],
                 direct["unique_flac_objects"], direct["unique_flac_bytes"]) ==
                (2440, 2234, 2230, 605221588), "media denominators and bytes", checks)
        require(direct["unresolved_statuses"] == {"runtime_dispatch_unsupported": 72},
                "unresolved dispatch not relabelled decode failure", checks)
        crosswalk = jsonl(source / "occurrence_identity_crosswalk.jsonl")
        require(Counter(r["character_attribution"] for r in crosswalk) ==
                {"accepted_solo": 657, "unresolved": 4}, "identity crosswalk counts", checks)
        hidden = [r for r in crosswalk if r["flow_state_row_index"] == 2516 and
                  r["talk_index"] in (13, 16, 17, 18, 20, 22, 24, 26, 28, 33)]
        require(len(hidden) == 10 and all(r["character_attribution"] == "accepted_solo" for r in hidden),
                "ten exact hidden Changli turns accepted", checks)
        remote = [r for r in crosswalk if r["flow_state_row_index"] == 17636 and
                  r["talk_index"] in (31, 32, 33, 34)]
        require(len(remote) == 4 and all(r["character_attribution"] == "unresolved" for r in remote),
                "four remote voices remain unresolved", checks)
        raw_meeting = next(r for r in jsonl(source / "RAW_RELEVANT_FLOW_STATES.jsonl")
                           if r["source_locator"].endswith("#/3296"))
        meeting = json.loads(raw_meeting["raw"]["Actions"])[4]["Params"]
        sequences = meeting["TalkSequence"]
        transitions = meeting["SequenceTransitions"]

        def routes(index: int) -> list[tuple[str, int]]:
            return [(r["OptionTextKey"], r["NextSequenceIndex"])
                    for r in transitions[str(index)]]

        require(sequences[2] == [3, 4] and sequences[3] == list(range(5, 13)),
                "optional watchful opening rejoins common apology and personal motive", checks)
        require(routes(0) == [("Character_ChangLi_8_4", 1),
                              ("Character_ChangLi_8_5", 2)] and
                routes(1) == [("", 3)] and routes(2) == [("", 3)],
                "both opening alternatives rejoin the apology", checks)
        require(sequences[14:19] == [[35, 36, 37], [38], [39, 40, 41, 42],
                                     [43, 44], [45, 46, 47]],
                "invitation, three exclusive replies and common departure sequences", checks)
        require(routes(14) == [("Character_ChangLi_8_50", 15),
                               ("Character_ChangLi_8_51", 16),
                               ("Character_ChangLi_8_52", 17)],
                "final choice is accept, why-me or reward, not categorical refusal", checks)
        require(routes(15) == [("Character_ChangLi_8_65", 18)] and
                routes(16) == [("Character_ChangLi_8_71", 18)] and
                routes(17) == [("Character_ChangLi_8_66", 18),
                               ("Character_ChangLi_8_76", 18)],
                "all three invitation routes accept and rejoin departure", checks)
        witnesses = {r["text_key"]: r["values"]
                     for r in jsonl(source / "CONTEXT_TEXT_WITNESSES.jsonl")}

        def witness(key: str, lang: str) -> str:
            return witnesses[key][lang]["content"]

        require("your idea" in witness("Character_ChangLi_8_10", "en") and
                "guessed" in witness("Character_ChangLi_8_69", "en") and
                "apology" in witness("Character_ChangLi_8_70", "en"),
                "token proposal is challenged, acknowledged and apologized for", checks)
        require("adorable" in witness("Character_ChangLi_8_78", "en") and
                "看得认真" in witness("Character_ChangLi_8_78", "zh-Hans") and
                "真剣" in witness("Character_ChangLi_8_78", "ja") and
                "열심히" in witness("Character_ChangLi_8_78", "ko"),
                "optional adorable is English-specific against attentive source witnesses", checks)
        require("wanted to see you" in witness("Character_ChangLi_8_15", "en") and
                "私心" in witness("Character_ChangLi_8_15", "zh-Hans") and
                "面倒事" in witness("Character_ChangLi_8_15", "ja") and
                "사심" in witness("Character_ChangLi_8_15", "ko"),
                "personal motive is localized with distinct emphasis", checks)
        require("special to me" in witness("Character_ChangLi_8_55", "en") and
                "任由你差遣" in witness("Character_ChangLi_8_56", "zh-Hans") and
                "any way I can" in witness("Character_ChangLi_8_56", "en") and
                "借り" in witness("Character_ChangLi_8_56", "ja") and
                "부름에 따르" in witness("Character_ChangLi_8_56", "ko"),
                "why-me affection and reward-only service wording retain four witnesses", checks)
        flow = {int(row["source_locator"].rsplit("/", 1)[1]): row["raw"]
                for row in jsonl(source / "RAW_RELEVANT_FLOW_STATES.jsonl")}
        quest_tree = json.loads((source_root / "_sources" / "Arikatsu_WutheringWaves_Data" /
                                 "BinData" / "QuestTree" / "questtreenode.json")
                                .read_text(encoding="utf-8"))
        summary_node = quest_tree[39]
        require(summary_node["Id"] == 120040 and
                summary_node["QuestArray"] == [121000035] and
                summary_node["Summary"] == "QuestTree_Summary_120040",
                "personal-quest synopsis is pinned to exact quest-tree node and quest ID",
                checks)
        mentions = {r["text_key"]: r for r in jsonl(source / "source_mentions.jsonl")}
        localized_summary = mentions["QuestTree_Summary_120040"]["localizations"]
        require(set(localized_summary) == {"zh-Hans", "en", "ja", "ko"} and
                all(localized_summary[lang]["status"] == "resolved" and
                    localized_summary[lang]["source_locator"].endswith(
                        "/MultiText.json#/293833")
                    for lang in ("zh-Hans", "en", "ja", "ko")),
                "four exact multilingual quest-summary witnesses retained", checks)
        require("下完了最后的棋局" in localized_summary["zh-Hans"]["content"] and
                "play out the final moves" in localized_summary["en"]["content"] and
                "最後の対局を終えた" in localized_summary["ja"]["content"] and
                "마지막 바둑을 끝냈다" in localized_summary["ko"]["content"] and
                "继续探索风景" in localized_summary["zh-Hans"]["content"] and
                "keep chasing distant horizons" in localized_summary["en"]["content"] and
                "探索を続ける" in localized_summary["ja"]["content"] and
                "계속 찾아다니기로" in localized_summary["ko"]["content"],
                "completed game and continued exploration are explicit in four summary texts",
                checks)
        final_game = json.loads(flow[3323]["Actions"])[6]["Params"]["TalkItems"][37]
        require(final_game["TidTalk"] == "Character_ChangLi_62_61" and
                final_game["WhoId"] == 999 and
                "可愿意" in witness("Character_ChangLi_62_61", "zh-Hans") and
                "Would you be willing" in witness("Character_ChangLi_62_61", "en"),
                "direct ending is a question, not the retrospective completed-game report",
                checks)
        handoff = json.loads(flow[3149]["Actions"])[5]
        handoff_items = handoff["Params"]["TalkItems"]
        require(handoff["Name"] == "ShowTalk" and
                handoff["Params"]["TalkSequence"] == [list(range(1, 13))] and
                len(handoff_items) == 12 and
                all(item["WhoId"] == 999 for item in handoff_items) and
                {i: handoff_items[i]["TidTalk"] for i in (0, 5, 7, 10)} ==
                {0: "Chengxiaoshan_main_1_1_245_2",
                 5: "Chengxiaoshan_main_1_1_245_8",
                 7: "Chengxiaoshan_main_1_1_245_10",
                 10: "Chengxiaoshan_main_1_1_245_14"},
                "3149 handoff is one Changli sequence with exact choice/defense keys", checks)
        require("引路，而非干涉" in witness("Chengxiaoshan_main_1_1_245_8", "zh-Hans") and
                "guide, not intervene" in witness("Chengxiaoshan_main_1_1_245_8", "en") and
                "案内は干渉ではない" in witness("Chengxiaoshan_main_1_1_245_8", "ja") and
                "간섭이 아닌" in witness("Chengxiaoshan_main_1_1_245_8", "ko") and
                "keep them at bay" in witness("Chengxiaoshan_main_1_1_245_10", "en"),
                "four witnesses bound noninterference to a final choice while defense continues",
                checks)
        companion = json.loads(flow[3301]["Actions"])[2]
        companion_items = companion["Params"]["TalkItems"]
        require(companion["Name"] == "ShowTalk" and
                companion["Params"]["TalkSequence"] == [list(range(1, 11))] and
                len(companion_items) == 10 and
                [item["WhoId"] for item in companion_items] ==
                [999, 999, 999, 999, 1316, 1316, 1316, 1316, 999, 999] and
                companion_items[2]["TidTalk"] == "Character_ChangLi_12_3" and
                companion_items[3]["TidTalk"] == "Character_ChangLi_12_6",
                "3301 changed-view sequence is interrupted by Abby, not a reply route",
                checks)
        require("同行的旅伴令人心安" in witness("Character_ChangLi_12_6", "zh-Hans") and
                "Your presence makes me feel at ease" in
                witness("Character_ChangLi_12_6", "en") and
                "頼もしい仲間" in witness("Character_ChangLi_12_6", "ja") and
                "동행자의 든든함" in witness("Character_ChangLi_12_6", "ko"),
                "EN direct address is distinct from ZH/JA/KO companion wording", checks)
        for state, expected_keys in (
            (3175, {6: "Chengxiaoshan_main_1_1_176_9",
                    7: "Chengxiaoshan_main_1_1_176_12"}),
            (3176, {1: "Chengxiaoshan_main_1_1_179_2",
                    7: "Chengxiaoshan_main_1_1_179_9",
                    12: "Chengxiaoshan_main_1_1_179_17"}),
            (3177, {6: "Chengxiaoshan_main_1_1_205_10",
                    9: "Chengxiaoshan_main_1_1_205_16",
                    10: "Chengxiaoshan_main_1_1_205_19",
                    11: "Chengxiaoshan_main_1_1_205_32",
                    14: "Chengxiaoshan_main_1_1_205_22",
                    15: "Chengxiaoshan_main_1_1_205_24",
                    17: "Chengxiaoshan_main_1_1_205_26",
                    18: "Chengxiaoshan_main_1_1_205_27",
                    19: "Chengxiaoshan_main_1_1_205_35"}),
        ):
            action = json.loads(flow[state]["Actions"])[5]
            items = action["Params"]["TalkItems"]
            require(action["Name"] == "ShowTalk" and
                    all(items[i]["TidTalk"] == key and items[i]["WhoId"] == 999
                        for i, key in expected_keys.items()),
                    f"Chronosorter scene {state} retains Changli speaker and exact keys", checks)
            owned = [r for r in crosswalk if r["flow_state_row_index"] == state and
                     r["action_index"] == 5 and r["character_attribution"] == "accepted_solo"]
            require(len(owned) == {3175: 9, 3176: 13, 3177: 21}[state] and
                    all(r["play_voice"] for r in owned),
                    f"Chronosorter scene {state} accepted source-voiced count", checks)
        require("更有可能" in witness("Chengxiaoshan_main_1_1_176_12", "zh-Hans") and
                "likely" in witness("Chengxiaoshan_main_1_1_176_12", "en") and
                "가능성" in witness("Chengxiaoshan_main_1_1_176_12", "ko"),
                "physical clue supports probable not diagnosed Overclocking", checks)
        require("起码在卷宗" in witness("Chengxiaoshan_main_1_1_179_9", "zh-Hans") and
                "At least that's what it says in these records" in
                witness("Chengxiaoshan_main_1_1_179_9", "en") and
                "至少验证" in witness("Chengxiaoshan_main_1_1_205_32", "zh-Hans") and
                "只有一例例外" in witness("Chengxiaoshan_main_1_1_205_19", "zh-Hans"),
                "documentary verdict and one destroyed exception stay bounded", checks)
        require("或许是二次共鸣的前提条件" in
                witness("Chengxiaoshan_main_1_1_205_22", "zh-Hans") and
                "过度消耗自身，只会走向灭亡" in
                witness("Chengxiaoshan_main_1_1_205_24", "zh-Hans") and
                "It doesn't sound like a good thing" in
                witness("Chengxiaoshan_main_1_1_205_23", "en"),
                "researcher hypothesis is not Changli's safe overclocking prescription", checks)
        require("似对祂下达" in witness("Chengxiaoshan_main_1_1_205_27", "zh-Hans") and
                "似乎因此" in witness("Chengxiaoshan_main_1_1_205_35", "zh-Hans") and
                "thanks to that order" in witness("Chengxiaoshan_main_1_1_205_35", "en") and
                "듯하고요" in witness("Chengxiaoshan_main_1_1_205_35", "ko"),
                "localization strength of apparent command/energy transfer retained", checks)
        unresolved = json.loads((source / "UNRESOLVED_VOICE_MEDIA.json").read_text(encoding="utf-8"))
        require(len(unresolved["source_locators"]) == 18 and
                all("#/3688/Actions!/0/Params/TalkItems/" in loc for loc in unresolved["source_locators"]),
                "eighteen text-known poetic lines in gap", checks)
        require(len(unresolved["installed_membership_rows"]) == 72,
                "72 installed memberships not counted as decoded", checks)
        lines = jsonl(voice / "COMPLETE_VOICE_LINE_ANALYSIS.jsonl")
        require(len(lines) == 610, "610 selected semantic voice rows", checks)
        new_scene_rows = []
        for state, action_index, item_count, owned_count, render_count, pcm_count, speakers in (
            (3345, 2, 16, 8, 36, 33, {0: 1328, 1: 1327, 13: 999, 15: 999}),
            (3134, 1, 6, 4, 16, 16, {0: 354, 2: 999, 5: 999}),
            (3297, 5, 8, 8, 32, 32, {0: 999, 5: 999, 7: 999}),
            (3146, 1, 5, 4, 16, 16, {0: 354, 1: 999, 4: 999}),
        ):
            action = json.loads(flow[state]["Actions"])[action_index]
            items = action["Params"]["TalkItems"]
            require(action["Name"] == "ShowTalk" and len(items) == item_count and
                    all(items[index]["WhoId"] == who for index, who in speakers.items()) and
                    not action["Params"].get("TalkSequence") and
                    not action["Params"].get("SequenceTransitions"),
                    f"context scene {state}/{action_index} raw speaker/action boundary", checks)
            owned = [row for row in crosswalk if row["flow_state_row_index"] == state and
                     row["action_index"] == action_index and
                     row["character_attribution"] == "accepted_solo"]
            require(len(owned) == owned_count and all(row["play_voice"] for row in owned),
                    f"context scene {state}/{action_index} accepted voiced ownership", checks)
            locators = {row["source_locator"] for row in owned}
            linked = [row for row in lines if row["source_locator"] in locators]
            require(len(linked) == owned_count and
                    {row["source_locator"] for row in linked} == locators,
                    f"context scene {state}/{action_index} semantic occurrence join", checks)
            renders = [render for row in linked for render in row["renders"]]
            require(len(renders) == render_count and
                    len({render["canonical_pcm_sha256"] for render in renders}) == pcm_count and
                    all({render["voice_language"] for render in row["renders"]} ==
                        LANGUAGES for row in linked) and
                    all(render["materialization_status"] == "flac_roundtrip_pcm_identical" and
                        render["source_wem_sha256_verified"] and
                        "/WwiseExternalSource/" in render["source_virtual_path"] and
                        render.get("event_id") is None and render.get("bank_id") is None and
                        render.get("numeric_media_id") is None for render in renders),
                    f"context scene {state}/{action_index} four-dub PCM joins and explicit Wwise gaps", checks)
            new_scene_rows.extend(linked)
        require(len(new_scene_rows) == 24 and
                len({row["semantic_voice_occurrence_id"] for row in new_scene_rows}) == 24 and
                sum(len(row["renders"]) for row in new_scene_rows) == 100 and
                len({render["canonical_pcm_sha256"] for row in new_scene_rows
                     for render in row["renders"]}) == 97,
                "four new readings reuse 24 selected lines, 100 associations and 97 PCM objects",
                checks)
        sonoro_intro = json.loads(flow[3343]["Actions"])[5]["Params"]["TalkItems"]
        require([item["TidTalk"] for item in sonoro_intro] ==
                ["Character_ChangLi_51_1", "Character_ChangLi_51_2"] and
                "混杂" in witness("Character_ChangLi_51_2", "zh-Hans") and
                "jumbled" in witness("Character_ChangLi_51_2", "en") and
                "独善其身" in witness("Character_ChangLi_53_7", "zh-Hans") and
                "네 자신을 잘 챙기고" in witness("Character_ChangLi_53_7", "ko"),
                "Sonoro framing and projected self-preservation counsel retain source limits",
                checks)
        require("无法确定" in witness("Chengxiaoshan_main_1_1_65_5", "zh-Hans") and
                "如果我不幸" in witness("Chengxiaoshan_main_1_1_65_6", "zh-Hans") and
                "想做的事" in witness("Chengxiaoshan_main_1_1_65_7", "zh-Hans") and
                "have to do" in witness("Chengxiaoshan_main_1_1_65_7", "en") and
                "需要你相助" in witness("Character_ChangLi_10_8", "zh-Hans") and
                "need your help" in witness("Character_ChangLi_10_8", "en"),
                "conditional time-flow directive and later help request retain distinct contexts",
                checks)
        search_items = json.loads(flow[3297]["Actions"])[5]["Params"]["TalkItems"]
        require([(i, len(item.get("Options", []))) for i, item in enumerate(search_items)
                 if item.get("Options")] == [(0, 1), (1, 2), (3, 2), (5, 3)] and
                all(not option.get("Actions") for item in search_items
                    for option in item.get("Options", [])) and
                "供职于边庭的各个仕宦" in
                witness("Chengxiaoshan_main_1_1_163_3", "zh-Hans") and
                "不过才十几岁" in witness("Chengxiaoshan_main_1_1_163_4", "zh-Hans") and
                "suppress her true nature" in
                witness("Chengxiaoshan_main_1_1_163_4", "en"),
                "Rover caption alternatives and Changli-attributed Jinhsi childhood account",
                checks)
        mountain_rows = []
        for state, expected_items, named_count, keys in (
            (3133, 15, 12, {5: "Chengxiaoshan_main_1_1_60_6",
                            9: "Chengxiaoshan_main_1_1_60_10",
                            10: "Chengxiaoshan_main_1_1_60_11",
                            13: "Chengxiaoshan_main_1_1_60_16"}),
            (3135, 17, 14, {7: "Chengxiaoshan_main_1_1_70_11",
                            8: "Chengxiaoshan_main_1_1_70_12",
                            13: "Chengxiaoshan_main_1_1_70_18",
                            14: "Chengxiaoshan_main_1_1_70_19"}),
        ):
            action = json.loads(flow[state]["Actions"])[4]
            items = action["Params"]["TalkItems"]
            require(action["Name"] == "ShowTalk" and len(items) == expected_items and
                    all(items[i]["WhoId"] == 999 and items[i]["TidTalk"] == key
                        for i, key in keys.items()),
                    f"mountain emergency {state}/4 exact raw action and speaker keys", checks)
            owned = [r for r in crosswalk if r["flow_state_row_index"] == state and
                     r["action_index"] == 4 and r["character_attribution"] == "accepted_solo"]
            require(len(owned) == named_count and all(r["play_voice"] for r in owned),
                    f"mountain emergency {state}/4 accepted source-voiced ownership",
                    checks)
            linked = [r for r in lines if r["source_locator"] in
                      {o["source_locator"] for o in owned}]
            require(len(linked) == named_count and
                    {r["source_locator"] for r in linked} ==
                    {o["source_locator"] for o in owned},
                    f"mountain emergency {state}/4 exact selected voice joins", checks)
            mountain_rows.extend(linked)
        require(len(json.loads(flow[3135]["Actions"])[4]["Params"]["TalkItems"][3]["Options"]) == 2,
                "dream dialogue has two alternate Rover options", checks)
        mountain_renders = [r for line in mountain_rows for r in line["renders"]]
        require(len(mountain_rows) == 26 and len(mountain_renders) == 104 and
                len({r["canonical_pcm_sha256"] for r in mountain_renders}) == 104 and
                all({r["voice_language"] for r in line["renders"]} == LANGUAGES
                    for line in mountain_rows) and
                all(r["materialization_status"] == "flac_roundtrip_pcm_identical" and
                    r.get("event_id") is None and r.get("numeric_media_id") is None
                    for r in mountain_renders),
                "two mountain actions: 26 named lines and 104 distinct four-dub PCM-valid renders without invented Wwise IDs",
                checks)
        require("倒退" in witness("Chengxiaoshan_main_1_1_60_6", "zh-Hans") and
                "slow down" in witness("Chengxiaoshan_main_1_1_60_6", "en") and
                "逆行" in witness("Chengxiaoshan_main_1_1_60_6", "ja") and
                "후퇴" in witness("Chengxiaoshan_main_1_1_60_6", "ko") and
                "推论是错" in witness("Chengxiaoshan_main_1_1_60_11", "zh-Hans") and
                "乡民" in witness("Chengxiaoshan_main_1_1_60_16", "zh-Hans"),
                "reversal localization, fallible theory and resident welfare anchors",
                checks)
        require("或许" in witness("Chengxiaoshan_main_1_1_70_11", "zh-Hans") and
                "could be" in witness("Chengxiaoshan_main_1_1_70_12", "en") and
                "かつての記憶" in witness("Chengxiaoshan_main_1_1_70_12", "ja") and
                "是今汐" in witness("Chengxiaoshan_main_1_1_70_18", "zh-Hans") and
                "有关吗" in witness("Chengxiaoshan_main_1_1_70_19", "zh-Hans"),
                "dream modality and Jinhsi-trace/question anchors", checks)
        new_context_rows = []
        for state, action_index, expected_count, expected_prefix, key_at in (
            (3147, 10, 9, "Chengxiaoshan_main_1_1_165_", {
                6: "Chengxiaoshan_main_1_1_165_8",
                8: "Chengxiaoshan_main_1_1_165_10",
                9: "Chengxiaoshan_main_1_1_165_11"}),
            (4682, 6, 10, "Event_AYKXBRZM_112_", {
                1: "Event_AYKXBRZM_112_5",
                4: "Event_AYKXBRZM_112_9",
                9: "Event_AYKXBRZM_112_15"}),
        ):
            action = json.loads(flow[state]["Actions"])[action_index]
            items = action["Params"]["TalkItems"]
            require(action["Name"] == "ShowTalk" and len(items) == 10 and
                    all(items[i]["WhoId"] == 999 and items[i]["TidTalk"] == key
                        for i, key in key_at.items()),
                    f"hypothesis scene {state}/{action_index} raw keys and speaker",
                    checks)
            owned = [row for row in crosswalk
                     if row["flow_state_row_index"] == state and
                     row["action_index"] == action_index and
                     row["character_attribution"] == "accepted_solo"]
            require(len(owned) == expected_count and all(row["play_voice"] for row in owned),
                    f"hypothesis scene {state}/{action_index} accepted voiced ownership",
                    checks)
            linked = [row for row in lines
                      if row["source_locator"] in
                      {occ["source_locator"] for occ in owned}]
            require(len(linked) == expected_count and
                    all(row["text_key"].startswith(expected_prefix) for row in linked),
                    f"hypothesis scene {state}/{action_index} selected source joins",
                    checks)
            render_set = [render for row in linked for render in row["renders"]]
            require(len(render_set) == expected_count * 4 and
                    len({render["canonical_pcm_sha256"] for render in render_set}) ==
                    expected_count * 4 and
                    all({render["voice_language"] for render in row["renders"]} ==
                        LANGUAGES for row in linked) and
                    all(render["materialization_status"] == "flac_roundtrip_pcm_identical" and
                        render["source_wem_sha256_verified"] and
                        render["source_virtual_path"].endswith(
                            f"/{render['voice_language']}_vo_{row['text_key']}.wem")
                        for row in linked for render in row["renders"]),
                    f"hypothesis scene {state}/{action_index} four distinct key-matched PCM-valid dubs",
                    checks)
            new_context_rows.extend(linked)
        require(len(items[0]["Options"]) == 3 and
                len(items[3]["Options"]) == 1 and
                len(items[7]["Options"]) == 1,
                "dream interaction retains three opening and two later Rover choices",
                checks)
        require("快速理解并利用" in
                witness("Chengxiaoshan_main_1_1_165_8", "zh-Hans") and
                "aren't supposed to be able to comprehend" in
                witness("Chengxiaoshan_main_1_1_165_8", "en") and
                "왜" in witness("Chengxiaoshan_main_1_1_165_10", "ko") and
                "线索" in witness("Chengxiaoshan_main_1_1_165_11", "zh-Hans"),
                "time-device hypothesis, language qualifier and clue-seeking intact",
                checks)
        require("推测" in witness("Event_AYKXBRZM_112_9", "zh-Hans") and
                "could be mistaken" in witness("Event_AYKXBRZM_112_9", "en") and
                "仮定" in witness("Event_AYKXBRZM_112_9", "ja") and
                "추측" in witness("Event_AYKXBRZM_112_9", "ko") and
                "索拉里斯" in witness("Event_AYKXBRZM_112_8", "zh-Hans"),
                "dream-world conjecture remains explicit across four witnesses",
                checks)
        quest_refs = jsonl(source / "QUEST_CONTEXT_REFERENCES.jsonl")
        for state_key, exact_keys in (
            ("剧情_1_1_乘宵山主线_2_15", {"125000121_40", "121800001_40"}),
            ("剧情_1_4_肉鸽主线剧情_8_7", {"139000039_50"}),
        ):
            candidates = [row for row in quest_refs if
                          any(m["state_key"] == state_key
                              for m in row["matching_references"])]
            require(exact_keys <= {row["raw"].get("Key") for row in candidates},
                    f"hypothesis scene {state_key} exact quest-reference candidates",
                    checks)
        for suffix, quest_keys in (
            ("_1_6", {"125000121_15", "121800001_15"}),
            ("_1_8", {"125000121_19", "121800001_19"}),
        ):
            relevant = [r for r in quest_refs
                        if any(m["state_key"].endswith(suffix)
                               for m in r["matching_references"])]
            require(quest_keys <= {r["raw"].get("Key") for r in relevant},
                    f"two exact quest-node state-match candidates for {suffix}",
                    checks)
        new_nominations = {
            "Chengxiaoshan_main_1_1_176_12", "Chengxiaoshan_main_1_1_179_9",
            "Chengxiaoshan_main_1_1_179_17", "Chengxiaoshan_main_1_1_205_16",
            "Chengxiaoshan_main_1_1_205_19", "Chengxiaoshan_main_1_1_205_24",
            "Chengxiaoshan_main_1_1_205_27", "Chengxiaoshan_main_1_1_205_35",
        }
        nominated = [line for line in lines if line["text_key"] in new_nominations]
        require(len(nominated) == len(new_nominations) and
                {line["text_key"] for line in nominated} == new_nominations and
                all(len(line["renders"]) == 4 for line in nominated),
                "Chronosorter AV nominations have exact four-dub voice joins", checks)
        handoff_companion_keys = {
            "Chengxiaoshan_main_1_1_245_8": "/3149/Actions!/5/Params/TalkItems/5",
            "Chengxiaoshan_main_1_1_245_10": "/3149/Actions!/5/Params/TalkItems/7",
            "Character_ChangLi_12_3": "/3301/Actions!/2/Params/TalkItems/2",
            "Character_ChangLi_12_6": "/3301/Actions!/2/Params/TalkItems/3",
        }
        new_rows = [line for line in lines if line["text_key"] in handoff_companion_keys]
        require(len(new_rows) == 4 and
                all(line["source_locator"].endswith(
                    handoff_companion_keys[line["text_key"]]) and
                    len(line["renders"]) == 4 and
                    all(render["source_wem_sha256_verified"] and
                        render["materialization_status"] ==
                        "flac_roundtrip_pcm_identical"
                        for render in line["renders"])
                    for line in new_rows),
                "four new exact keys join to sixteen PCM-valid four-dub renders", checks)
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
        audio = json.loads(summary.read_text(encoding="utf-8"))
        require((audio["manifest_objects"], audio["measured_objects"],
                 audio["repeated_pcm_manifest_rows"]) == (2230, 2230, 4),
                "measured-object counts", checks)
        require(not audio["failed_objects"] and not audio["human_perceptual_review_performed"],
                "no local measurement failures; human listening not implied", checks)
        cohort_path = summary.parent / "CHANGLI_SOURCE_COHORT_AUDIT.json"
        cohort_bytes = cohort_path.read_bytes()
        cohort = json.loads(cohort_bytes)
        require(hashlib.sha256(cohort_bytes).hexdigest() ==
                "1336d0cc9009f65ea9d1981ffafcf9db027a3df045c2b0b8177b9fc975d408bd",
                "source cohort matches documented frozen hash", checks)
        require(cohort["character"] == "Changli"
                and len(cohort["cohorts"]) == 11
                and sum(group["semantic_lines"] for group in cohort["cohorts"]) == 242
                and sum(group["render_associations"] for group in cohort["cohorts"]) == 964,
                "eleven source cohorts retain 242/964 denominators", checks)
        poem = next(group for group in cohort["cohorts"]
                    if group["name"] == "poetic_no_dispatch")
        require(poem["semantic_lines"] == 18
                and len(poem["semantic_lines_without_renders"]) == 18
                and poem["render_associations"] == 0,
                "poetic cohort retains eighteen unrendered text lines", checks)
        members = [member for group in cohort["cohorts"] for member in group["members"]]
        require(len({member["semantic_voice_occurrence_id"] for member in members}) == 224
                and len({member["canonical_pcm_sha256"] for member in members}) == 902
                and all(group["language_statistics"][lang]["integrity_pass_objects"] ==
                        group["language_statistics"][lang]["measured_objects"]
                        for group in cohort["cohorts"] for lang in LANGUAGES),
                "rendered cohort has 224 semantic lines, 902 integrity-valid PCM", checks)
        source_by_occurrence = {row["semantic_voice_occurrence_id"]: row for row in lines}
        require(all(member["semantic_voice_occurrence_id"] in source_by_occurrence
                    and member["source_locator"] == source_by_occurrence[
                        member["semantic_voice_occurrence_id"]]["source_locator"]
                    and any(render["render_analysis_id"] == member["render_analysis_id"]
                            and render["canonical_pcm_sha256"] == member["canonical_pcm_sha256"]
                            for render in source_by_occurrence[
                                member["semantic_voice_occurrence_id"]]["renders"])
                    for member in members),
                "cohort members retain exact source/render/PCM joins", checks)
        supplement_path = summary.parent / "CHANGLI_CHRONOSORTER_SOURCE_COHORT_AUDIT.json"
        supplement_bytes = supplement_path.read_bytes()
        supplement = json.loads(supplement_bytes)
        require(hashlib.sha256(supplement_bytes).hexdigest() ==
                "2f18f33d51af2891057892d195fe1e13b094651d432fac3e4262572231e725ae",
                "Chronosorter supplement matches documented hash", checks)
        require(supplement["character"] == "Changli" and
                [(group["name"], group["semantic_lines"], group["render_associations"])
                 for group in supplement["cohorts"]] ==
                [("physical_clue", 9, 36), ("first_record", 13, 52),
                 ("exceptional_device", 21, 84)],
                "three technical cohorts retain 43/172 denominators", checks)
        supplement_members = [member for group in supplement["cohorts"]
                              for member in group["members"]]
        require(len({member["semantic_voice_occurrence_id"] for member in supplement_members}) == 43
                and len({member["canonical_pcm_sha256"] for member in supplement_members}) == 172
                and all(group["language_statistics"][lang]["integrity_pass_objects"] ==
                        group["language_statistics"][lang]["measured_objects"]
                        for group in supplement["cohorts"] for lang in LANGUAGES),
                "technical supplement has 43 semantic lines and 172 integrity-valid PCM", checks)
        require(not {member["semantic_voice_occurrence_id"] for member in supplement_members} &
                {member["semantic_voice_occurrence_id"] for member in members},
                "technical supplement is disjoint from frozen eleven cohorts", checks)
        require(all(member["semantic_voice_occurrence_id"] in source_by_occurrence
                    and member["source_locator"] == source_by_occurrence[
                        member["semantic_voice_occurrence_id"]]["source_locator"]
                    and any(render["render_analysis_id"] == member["render_analysis_id"]
                            and render["canonical_pcm_sha256"] == member["canonical_pcm_sha256"]
                            for render in source_by_occurrence[
                                member["semantic_voice_occurrence_id"]]["renders"])
                    for member in supplement_members),
                "technical supplement retains exact source/render/PCM joins", checks)
        require(supplement["cohorts"][1]["language_statistics"]["zh"]["pitch_qualified_objects"] == 12,
                "first-record ZH pitch exclusion remains explicit", checks)
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
