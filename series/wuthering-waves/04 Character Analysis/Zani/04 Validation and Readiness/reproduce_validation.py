#!/usr/bin/env python3
"""Validate Zani's draft packet and optional private evidence joins.

Checks structure, authority, source identity and media retrieval—not literary
truth, story-graph exhaustiveness or human perceptual performance. Read-only
unless --write-report is supplied.
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
PACKET_ARTIFACT_PATHS = {'AUDIO_MATCHED_SEMANTIC_CASES.json': '03 Audiovisual and Voice/AUDIO_MATCHED_SEMANTIC_CASES.json', 'CHARACTER_VISUAL_DESIGN_PROFILE.json': '03 Audiovisual and Voice/CHARACTER_VISUAL_DESIGN_PROFILE.json', 'CHARACTER_VISUAL_DESIGN_PROFILE.md': '03 Audiovisual and Voice/CHARACTER_VISUAL_DESIGN_PROFILE.md', 'CHARACTER_VISUAL_REFERENCE_MANIFEST.json': '03 Audiovisual and Voice/CHARACTER_VISUAL_REFERENCE_MANIFEST.json', 'VALIDATION_REPORT.json': '04 Validation and Readiness/VALIDATION_REPORT.json', 'WUWA_ZANI_ANALYSIS_PACKET_README.md': 'WUWA_ZANI_ANALYSIS_PACKET_README.md', 'WUWA_ZANI_ARCHIVE_SKILL_KEY_AND_COMBAT_LABOR_PROFILE.md': '01 Evidence and Source-Facing/WUWA_ZANI_ARCHIVE_SKILL_KEY_AND_COMBAT_LABOR_PROFILE.md', 'WUWA_ZANI_AV_AND_HUMAN_RETRIEVAL_PLAN.md': '03 Audiovisual and Voice/WUWA_ZANI_AV_AND_HUMAN_RETRIEVAL_PLAN.md', 'WUWA_ZANI_AV_HUMAN_RETRIEVAL_CROSSWALK.md': '03 Audiovisual and Voice/WUWA_ZANI_AV_HUMAN_RETRIEVAL_CROSSWALK.md', 'WUWA_ZANI_CHARACTER_DEEP_DIVE_PRE_AV.md': '01 Evidence and Source-Facing/WUWA_ZANI_CHARACTER_DEEP_DIVE_PRE_AV.md', 'WUWA_ZANI_CHARACTER_MODEL_PACKAGE.json': '02 Reconstruction/WUWA_ZANI_CHARACTER_MODEL_PACKAGE.json', 'WUWA_ZANI_CLAIM_REVISION_LEDGER.md': '04 Validation and Readiness/WUWA_ZANI_CLAIM_REVISION_LEDGER.md', 'WUWA_ZANI_COLLEEN_DANGER_SHARED_BURDEN_AND_CONSENT_PROFILE.md': '01 Evidence and Source-Facing/WUWA_ZANI_COLLEEN_DANGER_SHARED_BURDEN_AND_CONSENT_PROFILE.md', 'WUWA_ZANI_EFFICIENCY_TRAP_SWORD_SHIELD_AND_PROTECTIVE_FORCE_PROFILE.md': '01 Evidence and Source-Facing/WUWA_ZANI_EFFICIENCY_TRAP_SWORD_SHIELD_AND_PROTECTIVE_FORCE_PROFILE.md', 'WUWA_ZANI_EVIDENCE_AND_FALSIFICATION_MATRIX.md': '01 Evidence and Source-Facing/WUWA_ZANI_EVIDENCE_AND_FALSIFICATION_MATRIX.md', 'WUWA_ZANI_FOOD_HOSTING_AND_THE_COST_OF_REST_PROFILE.md': '01 Evidence and Source-Facing/WUWA_ZANI_FOOD_HOSTING_AND_THE_COST_OF_REST_PROFILE.md', 'WUWA_ZANI_FULMINE_MASK_INQUIRY_AND_EVIDENCE_LIMITS_PROFILE.md': '01 Evidence and Source-Facing/WUWA_ZANI_FULMINE_MASK_INQUIRY_AND_EVIDENCE_LIMITS_PROFILE.md', 'WUWA_ZANI_LABOR_RULES_FORCE_AND_REST_PROFILE.md': '01 Evidence and Source-Facing/WUWA_ZANI_LABOR_RULES_FORCE_AND_REST_PROFILE.md', 'WUWA_ZANI_MODEL_FIDELITY_AND_STRESS_TEST_PRE_AV.md': '04 Validation and Readiness/WUWA_ZANI_MODEL_FIDELITY_AND_STRESS_TEST_PRE_AV.md', 'WUWA_ZANI_RECONSTRUCTIVE_PROFILE_PRE_AV.md': '02 Reconstruction/WUWA_ZANI_RECONSTRUCTIVE_PROFILE_PRE_AV.md', 'WUWA_ZANI_RELATIONSHIP_STATE_AND_ORDINARY_LIFE_PROFILE.md': '01 Evidence and Source-Facing/WUWA_ZANI_RELATIONSHIP_STATE_AND_ORDINARY_LIFE_PROFILE.md', 'WUWA_ZANI_SOURCE_CENSUS_CHRONOLOGY_AND_IDENTITY_AUDIT.md': '04 Validation and Readiness/WUWA_ZANI_SOURCE_CENSUS_CHRONOLOGY_AND_IDENTITY_AUDIT.md', 'WUWA_ZANI_SOURCE_DEFINED_AUDIO_COHORT_AUDIT.md': '04 Validation and Readiness/WUWA_ZANI_SOURCE_DEFINED_AUDIO_COHORT_AUDIT.md', 'WUWA_ZANI_SPEECH_AND_MACHINE_VOICE_PROFILE_PRE_AV.md': '03 Audiovisual and Voice/WUWA_ZANI_SPEECH_AND_MACHINE_VOICE_PROFILE_PRE_AV.md', 'WUWA_ZANI_SURVIVOR_DISTRUST_EMPLOYER_DUTY_AND_LEAVE_PROFILE.md': '01 Evidence and Source-Facing/WUWA_ZANI_SURVIVOR_DISTRUST_EMPLOYER_DUTY_AND_LEAVE_PROFILE.md', 'reproduce_validation.py': '04 Validation and Readiness/reproduce_validation.py'}

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
    matrix = (packet_artifact(HERE, "WUWA_ZANI_EVIDENCE_AND_FALSIFICATION_MATRIX.md")).read_text(encoding="utf-8")
    evidence_ids = set(re.findall(r"\| (ZAN-E\d{2}) \|", matrix))
    claim_ids = set(re.findall(r"\| (ZAN-C\d{2}) —", matrix))
    require(evidence_ids == {f"ZAN-E{index:02d}" for index in range(1, 45)},
            "44 contiguous evidence bundles", checks)
    require(claim_ids == {f"ZAN-C{index:02d}" for index in range(1, 44)},
            "43 contiguous claim rows", checks)
    distrust_profile = (packet_artifact(HERE, "WUWA_ZANI_SURVIVOR_DISTRUST_EMPLOYER_DUTY_AND_LEAVE_PROFILE.md")).read_text(
        encoding="utf-8")
    require(all(token in distrust_profile for token in
                ("7411/7", "158800014_25", "ZAN-E41", "ZAN-C39",
                 "ZAN-C40", "Colleen", "Rover")),
            "survivor-distrust specialist retains source, quest and speaker anchors", checks)
    danger_profile = (packet_artifact(HERE, "WUWA_ZANI_COLLEEN_DANGER_SHARED_BURDEN_AND_CONSENT_PROFILE.md")).read_text(
        encoding="utf-8")
    require(all(token in danger_profile for token in
                ("7552/2", "ZAN-E42", "ZAN-E43", "ZAN-C41", "ZAN-C42",
                 "Character_Zani_51_30", "Character_Zani_51_32")),
            "Colleen danger specialist retains exact source, options and claim anchors", checks)
    inquiry_profile = (packet_artifact(HERE, "WUWA_ZANI_FULMINE_MASK_INQUIRY_AND_EVIDENCE_LIMITS_PROFILE.md")).read_text(
        encoding="utf-8")
    require(all(token in inquiry_profile for token in
                ("4245", "114000027", "ZAN-E44", "ZAN-C43",
                 "Fulmine", "60", "Rover")),
            "Fulmine inquiry specialist retains quest, graph, media and speaker anchors", checks)
    require(
        not any(path.suffix.lower() in MEDIA_SUFFIXES for path in HERE.rglob("*") if path.is_file()),
        "no raw media in Git packet", checks,
    )
    for path in HERE.rglob("WUWA_ZANI_*.md"):
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
    model = json.loads((packet_artifact(HERE, "WUWA_ZANI_CHARACTER_MODEL_PACKAGE.json")).read_text(encoding="utf-8"))
    require(
        model["authority"] == "draft_noncurrent" and model["source_commit"] == COMMIT,
        "model authority and source pin", checks,
    )
    rules = model["rules"]
    require(len(rules) == 21 and len({rule["id"] for rule in rules}) == 21,
            "21 distinct model rules", checks)
    require(all(set(rule["evidence_ids"]) <= evidence_ids for rule in rules),
            "all rule evidence IDs resolve", checks)
    require(all(rule["probability"] is None for rule in rules),
            "no fabricated numerical probabilities", checks)
    probes = (packet_artifact(HERE, "WUWA_ZANI_MODEL_FIDELITY_AND_STRESS_TEST_PRE_AV.md")).read_text(encoding="utf-8")
    require(set(re.findall(r"\| (ZAN-P\d{2}) \|", probes)) ==
            {f"ZAN-P{index:02d}" for index in range(1, 46)},
            "45 contiguous non-blind probes", checks)
    interaction_block = probes.split("## Ten interaction tests", 1)[1].split(
        "\nThese remain proposed", 1
    )[0]
    require(len(re.findall(r"(?m)^\*\*[^\n]+\*\* ", interaction_block)) == 10 and
            all(f"R{number:02d}" in probes for number in range(1, 22)),
            "ten interaction tests and twenty-one-rule challenge map", checks)
    archive_profile = (packet_artifact(HERE, "WUWA_ZANI_ARCHIVE_SKILL_KEY_AND_COMBAT_LABOR_PROFILE.md")).read_text(
        encoding="utf-8"
    )
    require("FavorWord_150750_Content" in archive_profile and
            "FavorWord_150748_Content" in archive_profile,
            "rotated-key and labor-trigger specialist is present", checks)
    cases = json.loads((packet_artifact(HERE, "AUDIO_MATCHED_SEMANTIC_CASES.json")).read_text(encoding="utf-8"))
    require(cases["semantic_cases"] == 15 and len(cases["cases"]) == 15,
            "15 matched semantic cases", checks)
    crosswalk = (packet_artifact(HERE, "WUWA_ZANI_AV_HUMAN_RETRIEVAL_CROSSWALK.md")).read_text(encoding="utf-8")
    require(all(f"`{case['text_key']}`" in crosswalk for case in cases["cases"]),
            "all 15 exact sound cases occur in AV crosswalk", checks)
    require(all(f"**ZAN-S{number:02d} —" in crosswalk for number in (1, 2, 3, 4, 13, 14, 15)),
            "seven archive sound cases have individual retrieval capsules", checks)
    archive_target_events = (2045981504, 2217898941, 3387598988, 2452822987,
                             2452822985, 2371488700, 2371488703, 3570649760,
                             397104489, 397104491, 3132207817, 4228212925)
    require(all(str(event_id) in crosswalk for event_id in archive_target_events),
            "exact combat/shift nominations and wrong-key controls in AV crosswalk", checks)
    require(set(re.findall(r"\| (ZAN-R\d{2}) \|", crosswalk)) == {f"ZAN-R{number:02d}" for number in range(1, 13)},
            "twelve runtime/variant retrieval controls", checks)
    require("player-variable" in crosswalk and "textless" in crosswalk and "threat is not an observed killing" in crosswalk,
            "variant, missing-text, and action/outcome controls in AV crosswalk", checks)
    require(sum(len(case["renders"]) for case in cases["cases"]) == 63,
            "63 selected render variants", checks)
    require(sum(render["event_id"] is None and render["numeric_media_id"] is None
                for case in cases["cases"] for render in case["renders"]) == 35,
            "35 paired null event/media-ID render variants", checks)
    require(all({render["language"] for render in case["renders"]} == LANGUAGES
                for case in cases["cases"]), "every case spans four languages", checks)
    require(all(len(render[name]) == 64 for case in cases["cases"] for render in case["renders"]
                for name in ("wem_sha256", "canonical_pcm_sha256", "flac_sha256")),
            "selected render hashes present", checks)
    result = {
        "packet": "Zani",
        "scope": "ZANI_PINNED_3_6_0_TEXT_AUDIO_PRE_AV",
        "checks": checks,
        "source_crosscheck": "not_requested",
    }
    if source_root is not None:
        source = source_root / "ANALYSIS" / "Characters" / "Zani"
        voice = source_root / "_voice_media" / "character" / "complete_voice_corpus" / "Zani" / "v0_1"
        summary = source_root / "_research" / "character_packets" / "Zani" / "audio_work" / "AUDIO_MEASUREMENT_SUMMARY.json"
        audit = json.loads((source / "COLLECTION_AUDIT.json").read_text(encoding="utf-8"))
        quest_nodes = {
            node["Id"]: node for node in json.loads(
                (source_root / "_sources" / "Arikatsu_WutheringWaves_Data" /
                 "BinData" / "QuestTree" / "questtreenode.json").read_text(encoding="utf-8"))
        }
        require(quest_nodes[230301]["QuestArray"] ==
                [122000008, 122000009, 122000010, 122000011]
                and quest_nodes[230301]["Summary"] == "QuestTree_Summary_230301",
                "Zani's shared vault synopsis linked to four pinned quests", checks)
        vault_summary = next(row for row in jsonl(source / "source_mentions.jsonl")
                             if row["text_key"] == "QuestTree_Summary_230301")
        locales = vault_summary["localizations"]
        require(all(locales[language]["status"] == "resolved"
                    for language in ("zh-Hans", "en", "ja", "ko"))
                and "菲比用她的力量解除了危机" in locales["zh-Hans"]["content"]
                and "Phoebe uses her power" in locales["en"]["content"]
                and "bomb" in locales["en"]["content"]
                and "装置" in locales["ja"]["content"]
                and "장치" in locales["ko"]["content"],
                "four-locale vault outcome attributes action to Phoebe, EN bomb only", checks)
        direct = audit["scopes"]["direct_character"]
        require(audit["valid"] and direct["voice_completeness_valid"],
                "selected collection audit valid", checks)
        require((audit["raw_flow_states"], audit["context_text_keys"],
                 audit["quest_references"], audit["distinct_quest_ids"]) ==
                (225, 2954, 123, 21), "contextual collection denominators", checks)
        require((direct["candidate_occurrences"], direct["accepted_occurrences"],
                 direct["source_voiced"], direct["source_unvoiced"]) ==
                (960, 938, 840, 98), "direct occurrence denominator", checks)
        require((direct["semantic_voice_lines"], direct["render_associations"],
                 direct["unique_flac_objects"]) ==
                (912, 3653, 3517), "voice line, association, object denominators", checks)
        decisions = jsonl(source / "occurrence_identity_crosswalk.jsonl")
        require(Counter(row["character_attribution"] for row in decisions) ==
                {"accepted_solo": 938, "rejected": 18, "unresolved": 4},
                "identity crosswalk counts", checks)
        distrust_occurrences = [row for row in decisions
                               if row["flow_state_row_index"] == 7411 and
                               row["action_index"] == 7]
        require(len(distrust_occurrences) == 17 and
                all(row["character_attribution"] == "accepted_solo" and
                    row["technical_speaker_id"] == 1477 and row["play_voice"] and
                    row["resolved_media_association_count"] == 4
                    for row in distrust_occurrences),
                "Colleen action has 17 accepted voiced Zani turns and 68 associations", checks)
        missing = json.loads((source / "UNRESOLVED_TEXT_WITNESSES.json").read_text(encoding="utf-8"))
        require(len(missing["rows"]) == 8 and
                {row["text_key"] for row in missing["rows"]} ==
                {"Main_Linaxita_2_2_91_1", "Main_Linaxita_2_2_91_2"},
                "two semantic lines/eight missing language witnesses", checks)
        line_rows = jsonl(voice / "COMPLETE_VOICE_LINE_ANALYSIS.jsonl")
        require(len(line_rows) == 912, "912 selected semantic voice rows", checks)
        distrust_lines = [row for row in line_rows
                          if "/7411/Actions!/7/Params/TalkItems/" in row["source_locator"]]
        distrust_renders = [render for row in distrust_lines for render in row["renders"]]
        require(len(distrust_lines) == 17 and len(distrust_renders) == 68 and
                len({render["canonical_pcm_sha256"] for render in distrust_renders}) == 68 and
                all(render["materialization_status"] == "flac_roundtrip_pcm_identical" and
                    render.get("event_id") is None and render.get("bank_id") is None and
                    render.get("numeric_media_id") is None
                    for render in distrust_renders),
                "Colleen action has 68 distinct PCM-valid renders with unresolved event/bank/media IDs", checks)
        inquiry_occurrences = [row for row in decisions
                               if row["flow_state_row_index"] == 4245 and row["action_index"] == 2]
        require(len(inquiry_occurrences) == 16 and
                all(row["character_attribution"] == "accepted_solo" and
                    row["technical_speaker_id"] == 1477 and row["play_voice"] and
                    row["resolved_media_association_count"] == 4
                    for row in inquiry_occurrences),
                "4245 inquiry has sixteen accepted voiced Zani occurrences", checks)
        inquiry_lines = [row for row in line_rows
                         if "/4245/Actions!/2/Params/TalkItems/" in row["source_locator"]]
        inquiry_renders = [render for row in inquiry_lines for render in row["renders"]]
        require(len(inquiry_lines) == 16 and len(inquiry_renders) == 64 and
                len({render["canonical_pcm_sha256"] for render in inquiry_renders}) == 60 and
                all(render["source_wem_sha256_verified"] and
                    render["materialization_status"] == "flac_roundtrip_pcm_identical" and
                    render.get("event_id") is None and render.get("bank_id") is None and
                    render.get("numeric_media_id") is None for render in inquiry_renders),
                "4245 inquiry has 64 four-dub joins, 60 distinct PCM-valid objects and null numeric IDs", checks)
        inquiry_by_key = {row["text_key"]: row for row in inquiry_lines}
        require(all(
                    next(render for render in inquiry_by_key["Main_Linaxita_2_1_26_45"]["renders"]
                         if render["voice_language"] == lang)["canonical_pcm_sha256"] ==
                    next(render for render in inquiry_by_key["Main_Linaxita_2_1_26_13"]["renders"]
                         if render["voice_language"] == lang)["canonical_pcm_sha256"] and
                    next(render for render in inquiry_by_key["Main_Linaxita_2_1_26_45"]["renders"]
                         if render["voice_language"] == lang)["expected_wem_sha256"] ==
                    next(render for render in inquiry_by_key["Main_Linaxita_2_1_26_13"]["renders"]
                         if render["voice_language"] == lang)["expected_wem_sha256"]
                    for lang in LANGUAGES),
                "alternative 4245 request keys reuse the same WEM and PCM per language", checks)
        danger_occurrences = [row for row in decisions
                              if row["flow_state_row_index"] == 7552 and row["action_index"] == 2]
        require(len(danger_occurrences) == 15 and
                all(row["character_attribution"] == "accepted_solo" and
                    row["technical_speaker_id"] == 1477 and row["play_voice"] and
                    row["resolved_media_association_count"] == 4
                    for row in danger_occurrences),
                "7552 danger action has fifteen accepted voiced Zani occurrences", checks)
        danger_lines = [row for row in line_rows
                        if "/7552/Actions!/2/Params/TalkItems/" in row["source_locator"]]
        danger_renders = [render for row in danger_lines for render in row["renders"]]
        require(len(danger_lines) == 15 and len(danger_renders) == 60 and
                len({render["canonical_pcm_sha256"] for render in danger_renders}) == 60 and
                all(render["source_wem_sha256_verified"] and
                    render["materialization_status"] == "flac_roundtrip_pcm_identical" and
                    render.get("event_id") is None and render.get("bank_id") is None and
                    render.get("numeric_media_id") is None for render in danger_renders),
                "7552 action has sixty distinct PCM-valid renders with null event/bank/media IDs", checks)
        cohort_path = (source_root / "_research" / "character_packets" / "Zani" /
                       "audio_work" / "ZANI_SOURCE_COHORT_AUDIT.json")
        require(hashlib.sha256(cohort_path.read_bytes()).hexdigest() ==
                "2df1ed9251a80c27d474dd5ff7c538798d8ca745b0361adfcea2f0f0090cd288",
                "pinned source-defined cohort audit hash", checks)
        cohorts = json.loads(cohort_path.read_text(encoding="utf-8"))["cohorts"]
        expected_cohorts = {
            "front_desk": ("4204/2", 28, 115),
            "guest_sweets": ("7297/7@0-4", 5, 20),
            "minor_offenders": ("7297/7@14-27", 14, 56),
            "nightwalker_disclosure": ("7298/7", 28, 112),
            "old_routine_error": ("7301/4@0-16", 17, 68),
            "safer_city": ("7301/4@20-39", 20, 80),
            "talos_confrontation": ("7556/3@11-12+14-15+17-24+26", 13, 52),
            "paid_leave": ("12439/7", 17, 68),
        }
        require({cohort["name"] for cohort in cohorts} == set(expected_cohorts),
                "eight expected source-defined cohort names", checks)
        require(all((cohort["source_actions"][0], cohort["semantic_lines"],
                     cohort["render_associations"]) == expected_cohorts[cohort["name"]]
                    for cohort in cohorts), "eight exact selectors and counts", checks)
        members = [member for cohort in cohorts for member in cohort["members"]]
        require(len(members) == 571 and
                len({member["semantic_voice_occurrence_id"] for member in members}) == 142 and
                len({member["render_analysis_id"] for member in members}) == 571 and
                len({member["canonical_pcm_sha256"] for member in members}) == 571,
                "disjoint 142-line/571-render/571-PCM cohort membership", checks)
        source_render_index = {
            (row["semantic_voice_occurrence_id"], render["render_analysis_id"]):
            (row, render)
            for row in line_rows for render in row["renders"]
        }
        require(all(
            (member["semantic_voice_occurrence_id"], member["render_analysis_id"])
            in source_render_index and
            member["source_locator"] == source_render_index[
                (member["semantic_voice_occurrence_id"], member["render_analysis_id"])
            ][0]["source_locator"] and
            member["text_key"] == source_render_index[
                (member["semantic_voice_occurrence_id"], member["render_analysis_id"])
            ][0]["text_key"] and
            all(member[left] == source_render_index[
                (member["semantic_voice_occurrence_id"], member["render_analysis_id"])
            ][1][right] for left, right in (
                ("voice_language", "voice_language"),
                ("canonical_pcm_sha256", "canonical_pcm_sha256"),
                ("flac_sha256", "flac_sha256")))
            for member in members), "all cohort members match exact selected source/render/hash joins", checks)
        bank_first = [member for member in members if "/4204/Actions!/2/Params/TalkItems/0" in
                      member["source_locator"]]
        require(len(bank_first) == 7 and
                Counter(member["voice_language"] for member in bank_first) ==
                {"zh": 2, "en": 2, "ja": 2, "ko": 1},
                "hidden-speaker bank greeting preserves seven runtime variants", checks)
        negative_rows = [row for row in decisions if
                         (row["flow_state_row_index"], row["action_index"]) in
                         {(8585, 5), (8586, 10)}]
        require(Counter((row["flow_state_row_index"], row["action_index"])
                        for row in negative_rows) == {(8585, 5): 10, (8586, 10): 13} and
                all(row["character_attribution"] == "accepted_solo" and
                    row["play_voice"] is False for row in negative_rows) and
                not any("/8585/Actions!/5/Params/TalkItems/" in row["source_locator"] or
                        "/8586/Actions!/10/Params/TalkItems/" in row["source_locator"]
                        for row in line_rows),
                "23 accepted restitution/night-city turns are source-unvoiced", checks)
        package = json.loads((source / "character_source_package.json").read_text(encoding="utf-8"))
        favor_words = package["favor_words"]
        archive_rows = [row for row in line_rows
                        if row["record_class"] == "character_favor_archive"]
        archive_by_locator = {row["source_locator"]: row for row in archive_rows}
        require(len(favor_words) == len(archive_rows) == len(archive_by_locator) == 72,
                "72 distinct Zani archive source and voice locators", checks)
        language_map = {"en": "en", "ja": "ja", "ko": "ko", "zh-Hans": "zh"}
        require(all(
            word["raw"]["RoleId"] == 1507 and
            word["source_locator"] in archive_by_locator and
            word["raw"]["Content"] == archive_by_locator[word["source_locator"]]["text_key"] and
            all(word["content"]["values"][source_lang]["content"] ==
                archive_by_locator[word["source_locator"]]["text_witnesses"][voice_lang]["content"]
                for source_lang, voice_lang in language_map.items())
            for word in favor_words
        ), "all 72 Zani rows join actual Content keys and four text witnesses", checks)
        require(all(
            row["technical_render_coverage_status"] == "complete" and
            len(row["renders"]) == 4 and
            {render["voice_language"] for render in row["renders"]} == LANGUAGES and
            all(render["event_path"] == word["raw"]["Voice"] and
                render["event_id"] is not None and
                render["bank_id"] is not None and
                render["numeric_media_id"] is not None and
                render["source_wem_exists"] and
                render["source_wem_sha256_verified"] and
                render["materialization_status"] == "flac_roundtrip_pcm_identical" and
                len(render["canonical_pcm_sha256"]) == 64
                for render in row["renders"])
            for word in favor_words
            for row in [archive_by_locator[word["source_locator"]]]
        ), "all 72 Zani event/bank/media and 288 four-dub render chains resolve", checks)
        require(len({row["semantic_voice_occurrence_id"] for row in archive_rows}) == 72 and
                len({row["renders"][0]["event_id"] for row in archive_rows}) == 72 and
                len({render["canonical_pcm_sha256"] for row in archive_rows
                     for render in row["renders"]}) == 288,
                "72 distinct semantic archive occurrences/events and 288 PCM hashes", checks)
        expected_mismatches = {
            150737: (150739, 2198, 2045981504),
            150738: (150740, 2199, 1196901668),
            150739: (150741, 2200, 1196901671),
            150740: (150742, 2201, 1196901670),
            150741: (150743, 2202, 908924405),
            150742: (150744, 2203, 908924406),
            150743: (150745, 2204, 908924407),
            150744: (150746, 2205, 3387598989),
            150745: (150747, 2206, 3387598988),
            150746: (150748, 2207, 2452822985),
            150747: (150749, 2208, 2452822986),
            150748: (150750, 2209, 2452822987),
            150749: (150751, 2210, 2371488700),
            150750: (150752, 2211, 2371488703),
            150751: (150753, 2212, 2371488702),
            150752: (150737, 2213, 2217898941),
            150753: (150738, 2214, 2217898942),
        }
        by_raw_id = {word["raw"]["Id"]: word for word in favor_words}
        require(len(by_raw_id) == 72 and
                {raw_id for raw_id, word in by_raw_id.items()
                 if raw_id != int(word["raw"]["Content"].split("_")[1])} ==
                set(expected_mismatches),
                "exactly seventeen Zani raw-ID/Content-key mismatches", checks)
        for raw_id, (key_id, row_index, event_id) in expected_mismatches.items():
            word = by_raw_id[raw_id]
            row = archive_by_locator[word["source_locator"]]
            require(word["raw"]["Content"] == f"FavorWord_{key_id}_Content" and
                    word["source_locator"].endswith(f"favorword.json#/{row_index}") and
                    {render["event_id"] for render in row["renders"]} == {event_id},
                    f"rotated key/locator/event: raw {raw_id}", checks)
        combat_words = [word for word in favor_words
                        if 150732 <= word["raw"]["Id"] <= 150772]
        require(len(combat_words) == 41 and
                {int(word["source_locator"].rsplit("/", 1)[1]) for word in combat_words} ==
                set(range(2193, 2234)) and
                len({archive_by_locator[word["source_locator"]]["renders"][0]["event_id"]
                     for word in combat_words}) == 41 and
                len({render["canonical_pcm_sha256"] for word in combat_words
                     for render in archive_by_locator[word["source_locator"]]["renders"]}) == 164,
                "41 combat/system rows, 41 events and 164 distinct PCM objects within archive", checks)
        values = {raw_id: word["content"]["values"] for raw_id, word in by_raw_id.items()}
        require(
            values[150748]["en"]["content"] == "All of you at once. I don't do overtime." and
            values[150748]["zh-Hans"]["content"] == "一起上吧，别耽误我下班。" and
            "退勤時間" in values[150748]["ja"]["content"] and
            "퇴근 시간" in values[150748]["ko"]["content"] and
            values[150745]["en"]["content"] == "Reduced to dust." and
            values[150758]["en"]["content"] == "My shield can withstand more than that." and
            values[150763]["en"]["content"] == "Justice... shall be served." and
            values[150765]["en"]["content"] == "I'm off duty, it's your turn." and
            "少し交代" in values[150765]["ja"]["content"] and
            values[150769]["en"]["content"] == "Efficiency above all." and
            "迅速に動こう" in values[150769]["ja"]["content"],
            "combat labor/force/defeat/efficiency localization forks match pinned witnesses", checks,
        )
        require(by_raw_id[150748]["raw"]["Content"] !=
                by_raw_id[150746]["raw"]["Content"] and
                by_raw_id[150746]["raw"]["Content"] == "FavorWord_150748_Content" and
                archive_by_locator[by_raw_id[150748]["source_locator"]]["renders"][0]["event_id"] ==
                2452822987 and
                archive_by_locator[by_raw_id[150746]["source_locator"]]["renders"][0]["event_id"] ==
                2452822985,
                "ID-derived Liberation III key would silently select valid Liberation I event", checks)
        rest_advice = next(row for row in package["favor_words"]
                           if row["content"]["text_key"] == "FavorWord_150704_Content")
        require(rest_advice["source_locator"].endswith("favorword.json#/2165") and
                all(rest_advice["content"]["values"][language]["status"] == "resolved"
                    for language in ("en", "ja", "ko", "zh-Hans")),
                "four-language rest-advice archive identity", checks)
        rest_values = rest_advice["content"]["values"]
        require("拯救世界什么的应该也差不多吧" in rest_values["zh-Hans"]["content"] and
                "saving the world can wait" in rest_values["en"]["content"] and
                "世界を救う時も一緒" in rest_values["ja"]["content"] and
                "세상을 구하는 것도 비슷" in rest_values["ko"]["content"],
                "EN categorical rest wording versus ZH/JA/KO endless-duty analogy", checks)
        context = {row["text_key"]: row for row in jsonl(source / "CONTEXT_TEXT_WITNESSES.jsonl")}
        inquiry_state = next(row for row in jsonl(source / "RAW_RELEVANT_FLOW_STATES.jsonl")
                             if row["source_locator"].endswith("/flowstate.json#/4245"))
        inquiry_action = json.loads(inquiry_state["raw"]["Actions"])[2]
        inquiry_items = inquiry_action["Params"]["TalkItems"]
        inquiry_sequences = inquiry_action["Params"]["TalkSequence"]
        inquiry_transitions = inquiry_action["Params"]["SequenceTransitions"]
        require(inquiry_state["raw"]["StateKey"] == "剧情_2_0_黎那汐塔主线_第一幕_20_1" and
                inquiry_action["Name"] == "ShowTalk" and len(inquiry_items) == 35 and
                len(inquiry_sequences) == 7 and
                [[entry["NextSequenceIndex"] for entry in inquiry_transitions[str(index)]]
                 for index in (0, 1, 2, 3, 4, 5)] ==
                [[1, 2], [3], [3], [4, 5], [6], [6]],
                "4245 preserves two two-way forks and shared rejoins across seven sequences", checks)
        require([(inquiry_items[index]["WhoId"], inquiry_items[index]["TidTalk"])
                 for index in (6, 9, 10, 26, 27, 28, 29, 31)] ==
                [(1477, "Main_Linaxita_2_1_26_10"),
                 (1477, "Main_Linaxita_2_1_26_45"),
                 (1477, "Main_Linaxita_2_1_26_13"),
                 (50068, "Main_Linaxita_2_1_26_31"),
                 (1477, "Main_Linaxita_2_1_26_34"),
                 (1477, "Main_Linaxita_2_1_26_35"),
                 (1477, "Main_Linaxita_2_1_26_36"),
                 (1477, "Main_Linaxita_2_1_26_38")] and
                [option["TidTalkOption"] for option in inquiry_items[5]["Options"]] ==
                ["Main_Linaxita_2_1_26_8", "Main_Linaxita_2_1_26_9"] and
                [option["TidTalkOption"] for option in inquiry_items[26]["Options"]] ==
                ["Main_Linaxita_2_1_26_32", "Main_Linaxita_2_1_26_33"] and
                inquiry_items[29]["Options"][0]["TidTalkOption"] ==
                "Main_Linaxita_2_1_26_46" and
                all(not option["Actions"] for option in inquiry_items[31]["Options"]),
                "4245 speaker, duplicate request, mask alternatives and Rover captions are distinct", checks)
        require("就好像" in context["Main_Linaxita_2_1_26_34"]["values"]["zh-Hans"]["content"] and
                "must have" in context["Main_Linaxita_2_1_26_34"]["values"]["en"]["content"] and
                "如果" in context["Main_Linaxita_2_1_26_36"]["values"]["zh-Hans"]["content"] and
                all(context[key]["values"][lang]["status"] == "resolved"
                    for key in ("Main_Linaxita_2_1_26_34", "Main_Linaxita_2_1_26_35",
                                "Main_Linaxita_2_1_26_36", "Main_Linaxita_2_1_26_46")
                    for lang in ("zh-Hans", "en", "ja", "ko")),
                "four-locale mask and conditional-involvement witnesses retain certainty boundary", checks)
        danger_state = next(row for row in jsonl(source / "RAW_RELEVANT_FLOW_STATES.jsonl")
                            if row["source_locator"].endswith("/flowstate.json#/7552"))
        danger_action = json.loads(danger_state["raw"]["Actions"])[2]
        danger_items = danger_action["Params"]["TalkItems"]
        require(danger_state["raw"]["StateKey"] == "剧情_2_3_角色_赞妮副本_26_1" and
                danger_action["Name"] == "ShowTalk" and len(danger_items) == 32 and
                danger_action["Params"]["TalkSequence"] == [list(range(1, 33))] and
                danger_action["Params"]["SequenceTransitions"] == {} and
                Counter(item["WhoId"] for item in danger_items) ==
                {1477: 15, 200124: 8, 200001: 6, 750088: 3},
                "7552 action is one 32-item mixed-speaker sequence", checks)
        require({index: item["Options"][0]["TidTalkOption"]
                 for index, item in enumerate(danger_items) if item.get("Options")} ==
                {28: "Character_Zani_51_30", 29: "Character_Zani_51_32"} and
                all(not danger_items[index]["Options"][0]["Actions"] for index in (28, 29)) and
                [(danger_items[index]["WhoId"], danger_items[index]["TidTalk"])
                 for index in (15, 19, 21, 24, 25, 28, 29, 30, 31)] ==
                [(1477, "Character_Zani_51_16"), (1477, "Character_Zani_51_20"),
                 (750088, "Character_Zani_51_22"), (200001, "Character_Zani_51_25"),
                 (1477, "Character_Zani_51_26"), (200001, "Character_Zani_51_29"),
                 (1477, "Character_Zani_51_31"), (1477, "Character_Zani_51_33"),
                 (1477, "Character_Zani_51_34")],
                "7552 sequence separates Zani, Rover, Colleen, and two single player prompts", checks)
        danger_values = {key: context[key]["values"] for key in
                         ("Character_Zani_51_16", "Character_Zani_51_20",
                          "Character_Zani_51_26", "Character_Zani_51_30",
                          "Character_Zani_51_31", "Character_Zani_51_32",
                          "Character_Zani_51_33", "Character_Zani_51_34")}
        require("撞晕自己" in danger_values["Character_Zani_51_16"]["zh-Hans"]["content"] and
                "你留在这里" in danger_values["Character_Zani_51_20"]["zh-Hans"]["content"] and
                "程度并不对等" in danger_values["Character_Zani_51_26"]["zh-Hans"]["content"] and
                "stakes" in danger_values["Character_Zani_51_26"]["en"]["content"] and
                "必要はない" in danger_values["Character_Zani_51_26"]["ja"]["content"] and
                "I'll keep her safe" in danger_values["Character_Zani_51_30"]["en"]["content"] and
                "迟早会累垮" in danger_values["Character_Zani_51_31"]["zh-Hans"]["content"] and
                "not today" in danger_values["Character_Zani_51_32"]["en"]["content"] and
                "说了也没用" in danger_values["Character_Zani_51_33"]["zh-Hans"]["content"] and
                "那就拜托了" in danger_values["Character_Zani_51_34"]["zh-Hans"]["content"],
                "four-locale risk wording and speaker-specific safeguard/concession witnesses", checks)
        distrust_state = next(row for row in jsonl(source / "RAW_RELEVANT_FLOW_STATES.jsonl")
                              if row["source_locator"].endswith("/flowstate.json#/7411"))
        distrust_action = json.loads(distrust_state["raw"]["Actions"])[7]
        distrust_items = distrust_action["Params"]["TalkItems"]
        require(distrust_action["Name"] == "ShowTalk" and len(distrust_items) == 36 and
                Counter(item["WhoId"] for item in distrust_items) ==
                {1477: 17, 200001: 14, 750088: 2, 200121: 2, 83: 1},
                "mixed-speaker Colleen action preserves Zani, victim, Rover, operative and narration", checks)
        require([distrust_items[index]["TidTalk"] for index in
                 (15, 17, 18, 20, 22, 25, 26, 27, 28, 29, 30, 32, 33, 34)] ==
                ["Character_Zani_23_21", "Character_Zani_23_24",
                 "Character_Zani_23_25", "Character_Zani_23_27",
                 "Character_Zani_23_29", "Character_Zani_23_32",
                 "Character_Zani_23_33", "Character_Zani_23_34",
                 "Character_Zani_23_35", "Character_Zani_23_36",
                 "Character_Zani_23_37", "Character_Zani_23_42",
                 "Character_Zani_23_43", "Character_Zani_23_45"] and
                len(distrust_items[30]["Options"]) == 3 and
                all(not option["Actions"] for option in distrust_items[30]["Options"]),
                "Colleen trust, report, disclosure, duty and leave order; three options lack targets", checks)
        quest_refs = jsonl(source / "QUEST_CONTEXT_REFERENCES.jsonl")
        require(any(str(row["quest_id"]) == "114000027" and
                    any(ref["state_key"] == "剧情_2_0_黎那汐塔主线_第一幕_20_1"
                        for ref in row["matching_references"])
                    for row in quest_refs),
                "quest 114000027 points to the 4245 investigation state", checks)
        require(any(row["quest_id"] == "158800014" and
                    row["raw"]["Key"] == "158800014_25" and
                    row["raw"]["Data"]["Condition"]["Type"] == "PlayFlow" and
                    row["raw"]["Data"]["Condition"]["Flow"] ==
                    {"FlowListName": "剧情_2_3_角色_赞妮线",
                     "FlowId": 32, "StateId": 1}
                    for row in quest_refs),
                "Colleen action has exact-state character-quest candidate", checks)
        require(all(all(context[key]["values"][lang]["status"] == "resolved"
                        for lang in ("zh-Hans", "en", "ja", "ko"))
                    for key in ("Character_Zani_23_25", "Character_Zani_23_36",
                                "Character_Zani_23_42", "Character_Zani_23_43",
                                "Character_Zani_23_44")) and
                "holding a knife" in context["Character_Zani_23_25"]["values"]["en"]["content"] and
                "被害者" in context["Character_Zani_23_36"]["values"]["zh-Hans"]["content"] and
                "兑现了吗" in context["Character_Zani_23_44"]["values"]["zh-Hans"]["content"] and
                "vacation you got last time" in
                context["Character_Zani_23_44"]["values"]["en"]["content"],
                "four-language victim-right and prior-leave witnesses retain EN-specific imagery", checks)
        touch_state = next(row for row in jsonl(source / "RAW_RELEVANT_FLOW_STATES.jsonl")
                           if row["source_locator"].endswith("/flowstate.json#/7301"))
        touch_items = json.loads(touch_state["raw"]["Actions"])[4]["Params"]["TalkItems"]
        first_options = touch_items[39]["Options"]
        second_options = touch_items[40]["Options"]
        require([option["PlotLineKey"] for option in first_options] ==
                    ["Character_Zani_67_46", "Character_Zani_67_47"] and
                [option["Actions"][0]["Params"]["TalkId"] for option in first_options] ==
                    [44, 41] and
                [option["PlotLineKey"] for option in second_options] ==
                    ["Character_Zani_67_49", "Character_Zani_67_50"] and
                [option["Actions"][0]["Params"]["TalkId"] for option in second_options] ==
                    [42, 43] and
                [touch_items[index]["Actions"][0]["Params"]["TalkId"]
                    for index in (41, 42)] == [44, 44],
                "touch exchange preserves no-touch, hair and horn routes with common rejoin", checks)
        require([touch_items[index]["PlotLineKey"] for index in range(39, 43)] ==
                    ["Character_Zani_67_45", "Character_Zani_67_48",
                     "Character_Zani_67_51", "Character_Zani_67_52"] and
                all(touch_items[index]["WhoId"] == 1477 and
                    touch_items[index]["PlayVoice"] is True for index in range(39, 43)),
                "four exact Zani voiced TalkItems on optional touch paths", checks)
        require(all(context[f"Character_Zani_67_{suffix}"]["values"][lang]["status"] ==
                    "resolved" for suffix in range(45, 53)
                    for lang in ("zh-Hans", "en", "ja", "ko")) and
                "that's enough" in context["Character_Zani_67_51"]["values"]["en"]["content"] and
                "没提前说" in context["Character_Zani_67_52"]["values"]["zh-Hans"]["content"] and
                "話が違う" in context["Character_Zani_67_52"]["values"]["ja"]["content"] and
                "거길 만진다곤" in context["Character_Zani_67_52"]["values"]["ko"]["content"],
                "four-language hair stop and unannounced horn-touch witnesses", checks)
        require(all(
            len(rows := [row for row in line_rows
                         if row["text_key"] == f"Character_Zani_67_{suffix}"]) == 1 and
            rows[0]["source_locator"].endswith(
                f"/7301/Actions!/4/Params/TalkItems/{index}") and
            {render["voice_language"] for render in rows[0]["renders"]} == LANGUAGES and
            all(render["materialization_status"] == "flac_roundtrip_pcm_identical"
                for render in rows[0]["renders"])
            for index, suffix in ((39, 45), (40, 48), (41, 51), (42, 52))),
            "four optional-touch Zani lines each have exact four-dub PCM-valid render joins", checks)
        overtime_rows = [row for row in decisions if row["flow_state_row_index"] == 9968
                         and row["action_index"] == 2]
        overtime_by_talk = {row["talk_index"]: row for row in overtime_rows}
        require(set(overtime_by_talk) == {3, 4, 5, 6}
                and all(row["character_attribution"] == "accepted_solo" and row["play_voice"] is False
                        for row in overtime_rows)
                and all("甘愿在这熬上几天几夜" in context[overtime_by_talk[talk]["text_key"]]["values"]["zh-Hans"]["content"]
                        for talk in (4, 5))
                and "珂莱塔小姐" in context[overtime_by_talk[6]["text_key"]]["values"]["zh-Hans"]["content"],
                "9968/2 is a repeated offer to work longer for Carlotta, not a completed shift", checks)
        evacuation_rows = [row for row in decisions if row["flow_state_row_index"] == 8863
                           and row["action_index"] == 7]
        evacuation_by_talk = {row["talk_index"]: row for row in evacuation_rows}
        require(set(evacuation_by_talk) == {1, 2, 9, 10, 14}
                and "已完成转移" in context[evacuation_by_talk[1]["text_key"]]["values"]["zh-Hans"]["content"]
                and "有序进行" in context[evacuation_by_talk[9]["text_key"]]["values"]["zh-Hans"]["content"],
                "8863/7 reports evacuation progress without proving every physical rescue", checks)
        ascension = {row["content"]["text_key"]: row for row in package["favor_words"]
                     if row["content"]["text_key"] in
                     {f"FavorWord_1507{suffix}_Content" for suffix in (27, 28, 29, 30, 31)}}
        require(len(ascension) == 5, "five pinned ascension archive entries", checks)
        for suffix, locator in ((27, 2188), (28, 2189), (29, 2190), (30, 2191), (31, 2192)):
            key = f"FavorWord_1507{suffix}_Content"
            row = ascension[key]
            require(row["source_locator"].endswith(f"favorword.json#/{locator}") and
                    row["id"] == 150700 + suffix,
                    f"archive ID/source locator: {key}", checks)
            require(all(row["content"]["values"][lang]["status"] == "resolved"
                        for lang in ("en", "ja", "ko", "zh-Hans")),
                    f"four resolved archive witnesses: {key}", checks)
        efficiency = ascension["FavorWord_150728_Content"]["content"]["values"]
        require("摸鱼" in efficiency["zh-Hans"]["content"] and
                "act busy" in efficiency["en"]["content"] and
                "余計な仕事" in efficiency["ja"]["content"] and
                "게으름" in efficiency["ko"]["content"],
                "ascension-II labor-language contrast", checks)
        protection = ascension["FavorWord_150730_Content"]["content"]["values"]
        require("shield" in protection["en"]["content"] and
                "盾" not in protection["zh-Hans"]["content"] and
                "盾" not in protection["ja"]["content"] and
                "방패" not in protection["ko"]["content"],
                "ascension-IV English shield insertion", checks)
        offer = ascension["FavorWord_150731_Content"]["content"]["values"]
        require("无坚不摧" in offer["zh-Hans"]["content"] and
                "unbreakable sword" in offer["en"]["content"] and
                "強力な剣" in offer["ja"]["content"] and
                "무엇이든 벨 수 있는 검" in offer["ko"]["content"],
                "ascension-V sword-language contrast", checks)
        index = {(row["text_key"], row["semantic_voice_occurrence_id"]): row
                 for row in line_rows}
        for case in cases["cases"]:
            row = index[(case["text_key"], case["semantic_voice_occurrence_id"])]
            require(case["source_locator"] == row["source_locator"],
                    f"source locator: {case['text_key']}", checks)
            require(all(row["text_witnesses"][lang]["status"] == "resolved"
                        for lang in LANGUAGES),
                    f"selected text witnesses resolved: {case['text_key']}", checks)
            expected = {(render["runtime_render_variant_id"],
                         render["canonical_pcm_sha256"], render["flac_sha256"])
                        for render in row["renders"]}
            observed = {(render["render_variant_id"],
                         render["canonical_pcm_sha256"], render["flac_sha256"])
                        for render in case["renders"]}
            require(expected == observed, f"exact render join: {case['text_key']}", checks)
            source_by_variant = {render["runtime_render_variant_id"]: render
                                 for render in row["renders"]}
            require(all(render["event_id"] == source_by_variant[render["render_variant_id"]].get("event_id") and
                        render["numeric_media_id"] == source_by_variant[render["render_variant_id"]].get("numeric_media_id") and
                        render["source_virtual_path"] == source_by_variant[render["render_variant_id"]]["source_virtual_path"] and
                        render["wem_sha256"] == source_by_variant[render["render_variant_id"]]["expected_wem_sha256"]
                        for render in case["renders"]),
                    f"event/media/path/WEM join: {case['text_key']}", checks)
        for key in ("FavorWord_150728_Content", "FavorWord_150730_Content", "FavorWord_150731_Content"):
            case = next(case for case in cases["cases"] if case["text_key"] == key)
            require(len(case["renders"]) == 4 and
                    all(render["event_id"] is not None and render["numeric_media_id"] is not None
                        and not render["qc_flags"] for render in case["renders"]),
                    f"four explicit event/media and clean-QC renders: {key}", checks)
        audio = json.loads(summary.read_text(encoding="utf-8"))
        require((audio["manifest_objects"], audio["measured_objects"],
                 audio["repeated_pcm_manifest_rows"]) == (3517, 3517, 4),
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
