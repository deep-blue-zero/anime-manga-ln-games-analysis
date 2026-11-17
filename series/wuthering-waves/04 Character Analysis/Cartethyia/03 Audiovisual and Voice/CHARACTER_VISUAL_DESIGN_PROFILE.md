---
series: WUWA
character: Cartethyia
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

# Cartethyia — Visual Design and Appearance Profile

Status: `active_provisional`
Generation: `character_visual_v0_2`
Visual evidence manifest: `CHARACTER_VISUAL_REFERENCE_MANIFEST.json`

## Individualized summary

Cartethyia's bounded base-form art presents a gentle wandering saint/knight: long blonde hair, pointed ears, a thorn-like blue circlet, and a white-black dress extended by deep-blue star-flecked panels. The design balances ecclesiastical restraint with airy movement and a quiet, approachable expression.

## Evidence boundary

This first-pass profile is grounded in three decoded official-client UI textures: the large head icon, formation pile art, and activity portrait. Those images are authoritative as client-derived raw visual evidence for their own pixels, not as proof of unseen rear construction, exact physical materials, runtime animation, alternate skins/forms, or developer intent. The normalized role/profile record supplies semantic context but remains a separate authority layer.

Semantic role context is summarized only in the design–narrative claim below; the exact normalized source locator is retained in the JSON profile rather than reproducing the source text here.

## Structured observations

| Dimension | Observation | Basis | Confidence |
|---|---|---|---|
| silhouette | Long straight hair, pointed ears, a branching thorn circlet, shoulder drapes, and extremely long ribbon-like side panels create a slender, wind-swept silhouette. | `direct_visual` | `high` |
| palette | Warm blonde hair and pale skin sit against white, black, navy, and vivid gradient blues, with restrained gold and blue crystal accents. | `direct_visual` | `high` |
| hair and face | Waist-length blonde hair frames blue eyes and visibly pointed ears; the crown crosses the forehead asymmetrically and small blue drops hang beside the ears. | `direct_visual` | `high` |
| costume construction | A high black collar and dark central underdress are layered beneath white split panels, exposed shoulders, delicate straps, short inner hem, long trailing side cloth, and light heeled sandals. | `direct_visual` | `high` |
| materials | Soft pale cloth and dark structured trim contrast with branch-like metal, crystal drops, gold filigree, and blue panels rendered with starry translucent texture. | `direct_visual` | `medium` |
| motifs | Thorns/branches, droplets, wind-swept ribbons, blue crystal, and small ecclesiastical or fleur-like ornaments repeat across the crown, ears, chest, and hem. | `direct_visual` | `high` |
| weapon and role signaling | No weapon is visible in this bounded base-form UI set; the crown and vestment-like layering signal saintly or ceremonial history more strongly than an explicit knight's armament. | `direct_visual` | `medium` |
| pose and body language | The open hands, slight smile, crossed-leg stance, and lightly drifting panels convey gentleness and newly found ease rather than formal martial severity. | `direct_visual` | `high` |
| design narrative relationship | The thorned ceremonial frame and dark center preserve traces of the Blessed Maiden/Fleurdelys history, while the light pose and wind-blue panels fit the dossier's wandering-knight freedom reading. The selected images do not establish the visual transformation into Fleurdelys. | `direct_visual_and_semantic` | `medium` |

## Form / skin / state distinctions

- The three decoded images represent Cartethyia's default playable/base presentation. Fleurdelys, spirit-body, combat transformation, damage states, and any other skins are not visually covered by this generation. (`open`)

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
| head_icon | `RoleHeadIconLarge` | `decoded_exported` | `/Game/Aki/UI/UIResources/Common/Image/IconRoleHead256/T_IconRoleHead256_40_UI.T_IconRoleHead256_40_UI` | `restricted://_visual_media/character_visual_v0_2/client_textures/Aki/UI/UIResources/Common/Image/IconRoleHead256/T_IconRoleHead256_40_UI.png` |
| formation_pile_art | `FormationRoleCard` | `decoded_exported` | `/Game/Aki/UI/UIResources/Common/Image/IconRolePile/T_IconRole_Pile_katixiya_UI.T_IconRole_Pile_katixiya_UI` | `restricted://_visual_media/character_visual_v0_2/client_textures/Aki/UI/UIResources/Common/Image/IconRolePile/T_IconRole_Pile_katixiya_UI.png` |
| activity_portrait | `RolePortrait` | `decoded_exported` | `/Game/Aki/UI/UIResources/Common/Image/PixActivity/T_ActivityRoleKatixiya.T_ActivityRoleKatixiya` | `restricted://_visual_media/character_visual_v0_2/client_textures/Aki/UI/UIResources/Common/Image/PixActivity/T_ActivityRoleKatixiya.png` |
| head_icon | `RoleHeadIconCircle` | `reference_only` | `/Game/Aki/UI/UIResources/Common/Image/IconRoleHeadCircle256/T_IconRoleHeadCircle256_40_UI.T_IconRoleHeadCircle256_40_UI` | `—` |
| head_icon | `RoleHeadIconBig` | `reference_only` | `/Game/Aki/UI/UIResources/Common/Image/IconRoleHead150/T_IconRoleHead150_40_UI.T_IconRoleHead150_40_UI` | `—` |
| head_icon | `Card` | `reference_only` | `/Game/Aki/UI/UIResources/Common/Image/IconRoleHead175/T_IconRoleHead175_40_UI.T_IconRoleHead175_40_UI` | `—` |
| head_icon | `RoleHeadIcon` | `reference_only` | `/Game/Aki/UI/UIResources/Common/Image/IconRoleHead80/T_IconRoleHead80_40_UI.T_IconRoleHead80_40_UI` | `—` |
| quest_stand | `RoleStand` | `ambiguous` | `/Game/Aki/UI/UIResources/UiQuest/Image/ChuanShuo/T_IconChuanShuo1_UI.T_IconChuanShuo1_UI` | `—` |
| spine_portrait | `FormationSpineAtlas` | `ambiguous` | `/Game/Aki/UI/UIResources/Common/Spine/Portraits/Portraits_Anke/Portraits_Anke.Portraits_Anke-atlas` | `—` |
| spine_portrait | `FormationSpineSkeletonData` | `ambiguous` | `/Game/Aki/UI/UIResources/Common/Spine/Portraits/Portraits_Anke/Portraits_Anke.Portraits_Anke-data` | `—` |
| performance_animation | `UiScenePerformanceABP` | `reference_only` | `/Game/Aki/Character/Role/FemaleMS/Feibi/R2T1FeibiMd10011/ABP_Performance_FeiBi_PC.ABP_Performance_FeiBi_PC_C` | `—` |

The exported PNGs remain local/restricted copyrighted evidence. The repository-facing profile and manifest carry hashes and provenance, not a grant to redistribute the artwork.
