---
series: WUWA
artifact_type: character_visual_profile_import_record
scope: EIGHTEEN_CHARACTER_STATIC_VISUAL_PROFILE_V0_2
source_boundary: "Pinned normalized 3.6.0 role semantics plus read-only decoded official-client UI rasters; raw visual media remains restricted outside Git"
generation: V0.2
status: active_provisional
release_state: owner_authorized_publication
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
---

# WUWA character visual-profile V0.2 publication

The owner requested individualized appearance/design profiles for every character currently represented in the extraction workspace. This publication adds a bounded static visual layer for 18 characters: Aemeath, Augusta, Brant, Cantarella, Cartethyia, Changli, Chisa, Denia, Iuno, Jinhsi, Luuk Herssen, Lynae, Phoebe, Qiuyuan, Shorekeeper, Sigrika, Yinlin, and Zani.

## Published analytical set

Each character directory receives three Git artifacts:

- `CHARACTER_VISUAL_DESIGN_PROFILE.md` — an individualized human-readable summary and dimensional analysis;
- `CHARACTER_VISUAL_DESIGN_PROFILE.json` — stable visual-claim IDs, evidence bases, confidence, uncertainty, counterreadings, and form/state limits;
- `CHARACTER_VISUAL_REFERENCE_MANIFEST.json` — stable visual IDs, semantic role fields, client object/package/container identities, hashes, output dimensions, and a reverse provenance index.

The resulting publication set is 54 text/JSON artifacts. Existing reconstruction packets retain their routers and interpretive authority. Twelve new character directories are visual-profile-only and must not be mistaken for completed literary, speech, behavior, relationship, or romance models.

## Evidence and extraction method

The selected denominator is exact and uniform: `RoleHeadIconLarge`, `FormationRoleCard`, and `RolePortrait` for each normalized role record. The 54 referenced textures were decoded from the installed Wuthering Waves client through the headless CUE4Parse adapter in read-only mode. The receipt reports all 54 requested objects exported, no failures, exact GUID-to-key resolution, no raw key material in the receipt, outputs confined to the restricted media root, and identical selected-container metadata and bytes before and after extraction.

The extraction receipt is retained outside Git at `_visual_media/character_visual_v0_2/TEXTURE_EXPORT_RECEIPT.json`: 103,894 bytes, SHA-256 `12538c643a83b0d49adb3c509c8a970e4102fd1b471a411d3d48df448ff999dc`, deterministic projection `0252c43f83fbff812a9ddcc4f2ca4b77efc5c9d4ddd4930e64b96c6832bcfe71`. It records adapter runtime 10.0.11, CUE4Parse commit `b4e95441bcf0c975eb3adb68c0fb44c740c2cf62`, the `GAME_WutheringWaves` profile, and the exact installed-client provenance for each export.

Every one of the three rasters per character was directly inspected while authoring the individualized description. Machine-readable claims distinguish `direct_visual` observations from `direct_visual_and_semantic` interpretation and `open` form/state assertions. Material terms describe rendered cues, not physical-material measurements.

## Authority and limits

Official-client files are raw visual evidence authority. The pinned Arikatsu role record is canonical normalized semantic authority. Neither silently replaces the other. The Git profile is current `active_provisional` analysis within the bounded three-image denominator.

This layer does **not** claim:

- 3D model or topology reconstruction;
- neutral or rear runtime views;
- animation, expression, gesture, or scene-blocking coverage;
- a complete alternate-skin, transformation, damage-state, or form survey;
- promotional-art completeness;
- unique authorial meanings for visual motifs;
- completion of any packet's nominated scene-level audiovisual or human-listening work.

Counterreadings and open questions remain in every profile rather than being normalized away.

## Distribution boundary

No PNG, texture payload, package member, client archive, decryption material, audio, video, or other raw game media is committed. The Git manifests retain only provenance metadata and hashes. The 54 decoded PNGs remain local/restricted or privately shareable under the owner's evidence-plane controls.

The machine-readable [publication manifest](WUWA_CHARACTER_VISUAL_PROFILE_V0_2_IMPORT_MANIFEST.json) hashes every published profile artifact and records the source-to-destination mapping. Global `characters/registry.jsonl` and `CHARACTER_ANALYSIS_INDEX.md` remain curation-agent-owned and are not modified by this series-branch publication.

## Validation

Before publication:

- both V0.2 JSON schemas validated all 36 structured character artifacts;
- all 54 referenced decoded image hashes matched the restricted files;
- every exported reference had a matching reverse-provenance row;
- all 18 profiles used distinct individualized summaries and included the required observation dimensions, uncertainty, counterreadings, and open questions;
- no raw media or absolute private filesystem path entered the Git candidate;
- title-local character, claim, corpus-map, open-question, manifest, and existing-character-router routes were updated in the same change.

Repository author preflight, exact staged-diff review, remote-head recheck, non-forced publication, and exact-head GitHub audit remain the governing publication gates.
