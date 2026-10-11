---
series: WUWA
character: Chisa
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

# Chisa — Visual Design and Appearance Profile

Status: `active_provisional`
Generation: `character_visual_v0_2`
Visual evidence manifest: `CHARACTER_VISUAL_REFERENCE_MANIFEST.json`

## Individualized summary

Chisa pairs an ordinary school-uniform silhouette with surgical threat: long black hair, red eyes and ribbons, a gray-black sailor-style outfit, visible stitch motifs, and an enormous red-black pair of shears. The design's power comes from keeping the figure visually quiet while making the tool impossible to ignore.

## Evidence boundary

This first-pass profile is grounded in three decoded official-client UI textures: the large head icon, formation pile art, and activity portrait. Those images are authoritative as client-derived raw visual evidence for their own pixels, not as proof of unseen rear construction, exact physical materials, runtime animation, alternate skins/forms, or developer intent. The normalized role/profile record supplies semantic context but remains a separate authority layer.

Semantic role context is summarized only in the design–narrative claim below; the exact normalized source locator is retained in the JSON profile rather than reproducing the source text here.

## Structured observations

| Dimension | Observation | Basis | Confidence |
|---|---|---|---|
| silhouette | A simple straight-haired, pleated-skirt silhouette is cut diagonally by the oversized open shears, whose length exceeds her height. | `direct_visual` | `high` |
| palette | Black, charcoal, gray, and white dominate; concentrated red in the eyes, ribbons, tie, and weapon acts as a danger code. | `direct_visual` | `high` |
| hair and face | Glossy black hair falls well past the waist with blunt bangs and a small red side ribbon; red eyes and a reserved expression keep the face controlled. | `direct_visual` | `high` |
| costume construction | The outfit adapts a sailor-style school uniform with a white back collar, cropped dark top, pleated skirt, choker, knee socks, loafers, sleeve cutouts, lacing, and raw or torn edges. | `direct_visual` | `high` |
| materials | Soft uniform cloth and ribbon contrast with the hard lacquered red-black weapon, exposed gold mechanisms, and small glossy straps. | `direct_visual` | `medium` |
| motifs | Cuts, seams, stitches, lacing, sharp red triangles, and black-red division repeat across clothing and weapon. | `direct_visual` | `high` |
| weapon and role signaling | The giant articulated shears make cutting, separation, and precision the unambiguous combat and conceptual center of the design. | `direct_visual` | `medium` |
| pose and body language | Her half-turned posture, level gaze, closed mouth, and low-effort grip make the oversized weapon feel controlled rather than burdensome. | `direct_visual` | `high` |
| design narrative relationship | The 'ordinary student' uniform is directly complicated by cut/stitch imagery and the shears, fitting the semantic profile of someone who sees the world's structures and isolates the thread that tugs at life. | `direct_visual_and_semantic` | `medium` |

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
| head_icon | `RoleHeadIconLarge` | `decoded_exported` | `/Game/Aki/UI/UIResources/Common/Image/IconRoleHead256/T_IconRoleHead256_57_UI.T_IconRoleHead256_57_UI` | `restricted://_visual_media/character_visual_v0_2/client_textures/Aki/UI/UIResources/Common/Image/IconRoleHead256/T_IconRoleHead256_57_UI.png` |
| formation_pile_art | `FormationRoleCard` | `decoded_exported` | `/Game/Aki/UI/UIResources/Common/Image/IconRolePile/T_IconRole_Pile_Qianxiao_UI.T_IconRole_Pile_Qianxiao_UI` | `restricted://_visual_media/character_visual_v0_2/client_textures/Aki/UI/UIResources/Common/Image/IconRolePile/T_IconRole_Pile_Qianxiao_UI.png` |
| activity_portrait | `RolePortrait` | `decoded_exported` | `/Game/Aki/UI/UIResources/Common/Image/PixActivity/T_ActivityRoleQianxiao.T_ActivityRoleQianxiao` | `restricted://_visual_media/character_visual_v0_2/client_textures/Aki/UI/UIResources/Common/Image/PixActivity/T_ActivityRoleQianxiao.png` |
| head_icon | `RoleHeadIconCircle` | `reference_only` | `/Game/Aki/UI/UIResources/Common/Image/IconRoleHeadCircle256/T_IconRoleHeadCircle256_57_UI.T_IconRoleHeadCircle256_57_UI` | `—` |
| head_icon | `RoleHeadIconBig` | `reference_only` | `/Game/Aki/UI/UIResources/Common/Image/IconRoleHead150/T_IconRoleHead150_57_UI.T_IconRoleHead150_57_UI` | `—` |
| head_icon | `Card` | `reference_only` | `/Game/Aki/UI/UIResources/Common/Image/IconRoleHead175/T_IconRoleHead175_57_UI.T_IconRoleHead175_57_UI` | `—` |
| head_icon | `RoleHeadIcon` | `reference_only` | `/Game/Aki/UI/UIResources/Common/Image/IconRoleHead80/T_IconRoleHead80_57_UI.T_IconRoleHead80_57_UI` | `—` |
| quest_stand | `RoleStand` | `ambiguous` | `/Game/Aki/UI/UIResources/UiQuest/Image/ChuanShuo/T_IconChuanShuo1_UI.T_IconChuanShuo1_UI` | `—` |
| spine_portrait | `FormationSpineAtlas` | `ambiguous` | `/Game/Aki/UI/UIResources/Common/Spine/Portraits/Portraits_Anke/Portraits_Anke.Portraits_Anke-atlas` | `—` |
| spine_portrait | `FormationSpineSkeletonData` | `ambiguous` | `/Game/Aki/UI/UIResources/Common/Spine/Portraits/Portraits_Anke/Portraits_Anke.Portraits_Anke-data` | `—` |
| performance_animation | `UiScenePerformanceABP` | `reference_only` | `/Game/Aki/Character/Role/FemaleM/Qianxia/R2T1QianXiaMd10011/ABP_Performance_QianXia_PC.ABP_Performance_QianXia_PC_C` | `—` |

The exported PNGs remain local/restricted copyrighted evidence. The repository-facing profile and manifest carry hashes and provenance, not a grant to redistribute the artwork.
