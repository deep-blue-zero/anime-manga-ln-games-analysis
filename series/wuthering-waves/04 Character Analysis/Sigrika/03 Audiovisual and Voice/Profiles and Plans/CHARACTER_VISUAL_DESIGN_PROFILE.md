---
series: WUWA
character: Sigrika
artifact_type: character_visual_design_profile
scope: DEFAULT_PLAYABLE_OFFICIAL_CLIENT_UI_VISUALS
source_boundary: "Pinned normalized 3.6.0 role semantics plus three decoded official-client UI rasters; raw media remains local/private evidence"
generation: V0.2
status: active_provisional
release_state: mutable_active
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
---

# Sigrika — Visual Design and Appearance Profile

Status: `active_provisional`
Generation: `character_visual_v0_2`
Visual evidence manifest: `CHARACTER_VISUAL_REFERENCE_MANIFEST.json`

## Individualized summary

Sigrika is a bright academy-adventurer design centered on massed orange hair and open movement. Multiple braided, segmented ponytail clusters surround a white-and-lavender asymmetric outfit, dark shorts, gold fittings, crystalline ornaments, and luminous rune-like markings on the legs.

## Evidence boundary

This first-pass profile is grounded in three decoded official-client UI textures: the large head icon, formation pile art, and activity portrait. Those images are authoritative as client-derived raw visual evidence for their own pixels, not as proof of unseen rear construction, exact physical materials, runtime animation, alternate skins/forms, or developer intent. The normalized role/profile record supplies semantic context but remains a separate authority layer.

Semantic role context is summarized only in the design–narrative claim below; the exact normalized source locator is retained in the JSON profile rather than reproducing the source text here.

## Structured observations

| Dimension | Observation | Basis | Confidence |
|---|---|---|---|
| silhouette | Huge orange braided hair masses expand sideways and downward around a compact shorts-and-tunic body; open shoulders, split panels, and sandals keep the center light. | `direct_visual` | `high` |
| palette | Orange hair is the dominant field, balanced by white, pale lavender, deep violet, and black, with gold trim, green eyes, and softly glowing coral-red markings. | `direct_visual` | `high` |
| hair and face | Bright orange hair is divided into many braids and bubble-like tied sections beneath a pale angular headpiece; green eyes and an open smile make the face immediately energetic. | `direct_visual` | `high` |
| costume construction | An off-shoulder white outer tunic with lavender sleeves and asymmetric hanging panels is layered over a dark fitted top and shorts, then finished with arm wraps, thigh straps, ribbons, tassels, and open sandals. | `direct_visual` | `high` |
| materials | Light cloth, woven braids and cords, polished gold fittings, faceted pale crystals, soft pouches, and luminous skin markings provide varied surfaces. | `direct_visual` | `medium` |
| motifs | Runic lines, triangles, angular crystals, braids, tassels, woven cords, and compact utility pouches recur across body and costume. | `direct_visual` | `high` |
| weapon and role signaling | No held weapon appears in the bounded images; runic marks, crystals, and travel-ready accessories signal magical or ritual capability without establishing a weapon class. | `direct_visual` | `medium` |
| pose and body language | The open smile, extended arm, shifted hip, and outward-splaying hair create an eager, socially forward presentation. | `direct_visual` | `high` |
| design narrative relationship | The visible rune markings and challenge-ready pose align with the semantic profile of a Royan Runes Resonator striving to become a Solsworn, but the exact cultural meaning of each geometric ornament is not established. | `direct_visual_and_semantic` | `medium` |

## Form / skin / state distinctions

- The three decoded images are treated as the role record's default playable presentation. Alternate skins, transformation states, damage states, and rear views were not established in this generation. (`open`)

## Counterreadings

- A single costume feature may support several readings; the profile records plausible visual functions rather than claiming unique authorial intent.
- UI key art can exaggerate color, pose, scale, transparency, and fabric motion relative to the runtime model.

## Open questions

- How does the silhouette and garment construction read from the back and in neutral runtime lighting?
- Which pose, gesture, idle, facial-expression, and movement habits persist across authored scenes and gameplay?
- Which alternate skins, forms, combat states, or story states materially change this design grammar?
- Do official promotional sheets or model turnarounds contradict details inferred from these three UI rasters?

## Visual references

| Category | Semantic field | Status | Asset object | Local export |
|---|---|---|---|---|
| head_icon | `RoleHeadIconLarge` | `decoded_exported` | `/Game/Aki/UI/UIResources/Common/Image/IconRoleHead256/T_IconRoleHead256_65_UI.T_IconRoleHead256_65_UI` | `restricted://_visual_media/character_visual_v0_2/client_textures/Aki/UI/UIResources/Common/Image/IconRoleHead256/T_IconRoleHead256_65_UI.png` |
| formation_pile_art | `FormationRoleCard` | `decoded_exported` | `/Game/Aki/UI/UIResources/Common/Image/IconRolePile/T_IconRole_Pile_Xigelika_UI.T_IconRole_Pile_Xigelika_UI` | `restricted://_visual_media/character_visual_v0_2/client_textures/Aki/UI/UIResources/Common/Image/IconRolePile/T_IconRole_Pile_Xigelika_UI.png` |
| activity_portrait | `RolePortrait` | `decoded_exported` | `/Game/Aki/UI/UIResources/Common/Image/PixActivity/T_ActivityRoleXigelika.T_ActivityRoleXigelika` | `restricted://_visual_media/character_visual_v0_2/client_textures/Aki/UI/UIResources/Common/Image/PixActivity/T_ActivityRoleXigelika.png` |
| head_icon | `RoleHeadIconCircle` | `reference_only` | `/Game/Aki/UI/UIResources/Common/Image/IconRoleHeadCircle256/T_IconRoleHeadCircle256_65_UI.T_IconRoleHeadCircle256_65_UI` | `—` |
| head_icon | `RoleHeadIconBig` | `reference_only` | `/Game/Aki/UI/UIResources/Common/Image/IconRoleHead150/T_IconRoleHead150_65_UI.T_IconRoleHead150_65_UI` | `—` |
| head_icon | `Card` | `reference_only` | `/Game/Aki/UI/UIResources/Common/Image/IconRoleHead175/T_IconRoleHead175_65_UI.T_IconRoleHead175_65_UI` | `—` |
| head_icon | `RoleHeadIcon` | `reference_only` | `/Game/Aki/UI/UIResources/Common/Image/IconRoleHead80/T_IconRoleHead80_65_UI.T_IconRoleHead80_65_UI` | `—` |
| quest_stand | `RoleStand` | `ambiguous` | `/Game/Aki/UI/UIResources/UiQuest/Image/ChuanShuo/T_IconChuanShuo1_UI.T_IconChuanShuo1_UI` | `—` |
| spine_portrait | `FormationSpineAtlas` | `ambiguous` | `/Game/Aki/UI/UIResources/Common/Spine/Portraits/Portraits_Anke/Portraits_Anke.Portraits_Anke-atlas` | `—` |
| spine_portrait | `FormationSpineSkeletonData` | `ambiguous` | `/Game/Aki/UI/UIResources/Common/Spine/Portraits/Portraits_Anke/Portraits_Anke.Portraits_Anke-data` | `—` |
| performance_animation | `UiScenePerformanceABP` | `reference_only` | `/Game/Aki/Character/Role/FemaleMS/Xigelika/R2T1XigelikaMd10011/ABP_Performance_Xigelika_PC.ABP_Performance_Xigelika_PC_C` | `—` |

The exported PNGs remain local/restricted copyrighted evidence. The repository-facing profile and manifest carry hashes and provenance, not a grant to redistribute the artwork.
