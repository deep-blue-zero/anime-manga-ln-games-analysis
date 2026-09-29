---
series: WUWA
character: Qiuyuan
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

# Qiuyuan — Visual Design and Appearance Profile

Status: `active_provisional`
Generation: `character_visual_v0_2`
Visual evidence manifest: `CHARACTER_VISUAL_REFERENCE_MANIFEST.json`

## Individualized summary

Qiuyuan is a weathered wandering swordsman rendered in ink-wash tones. Long black hair tied by a green ribbon, layered white-black robes, gray feathered or torn outer cloth, metal bracers, subdued green trim, and a long carried weapon/case produce a restrained, travel-worn silhouette.

## Evidence boundary

This first-pass profile is grounded in three decoded official-client UI textures: the large head icon, formation pile art, and activity portrait. Those images are authoritative as client-derived raw visual evidence for their own pixels, not as proof of unseen rear construction, exact physical materials, runtime animation, alternate skins/forms, or developer intent. The normalized role/profile record supplies semantic context but remains a separate authority layer.

Semantic role context is summarized only in the design–narrative claim below; the exact normalized source locator is retained in the JSON profile rather than reproducing the source text here.

## Structured observations

| Dimension | Observation | Basis | Confidence |
|---|---|---|---|
| silhouette | A large tied mane, long scarf and robe tails, broad ragged outer layers, crossed arms, and the diagonal carried weapon/case create a closed, wind-beaten silhouette. | `direct_visual` | `high` |
| palette | Black, charcoal, white, gray, and earth-brown dominate; dark green ribbons and lining provide the only sustained color, with sparse red marks on the cloth. | `direct_visual` | `high` |
| hair and face | Long black hair falls over part of the face and is gathered high with a green band; the lowered gaze and sharp profile keep the expression distant. | `direct_visual` | `high` |
| costume construction | Layered robes and scarves sit over a belted dark undergarment, metal forearm guard, practical trousers, boots, and multiple worn outer panels with irregular hems. | `direct_visual` | `high` |
| materials | Soft layered cloth, weathered or ink-stained edges, leather straps, dark metal armor, and a cylindrical hard case/weapon housing create a deliberately used rather than pristine finish. | `direct_visual` | `medium` |
| motifs | Ink wash, torn feathers or brushlike hems, green ties, sparse red strokes, an animal-face chest clasp, and scroll/case forms repeat across the outfit. | `direct_visual` | `high` |
| weapon and role signaling | A long weapon or sheathed implement is carried over the shoulder, while the metal bracer and layered travel gear support the semantic identification as a wandering swordsman; the exact weapon construction is not fully visible. | `direct_visual` | `medium` |
| pose and body language | Crossed arms, lowered chin, and a side-on stance read as guarded, self-contained, and observant. | `direct_visual` | `high` |
| design narrative relationship | The worn monochrome robes and solitary posture strongly align with the profile of a scapegoated former agent and blind swordsman wandering alone; the subdued green prevents the design from becoming entirely funereal. | `direct_visual_and_semantic` | `medium` |

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
| head_icon | `RoleHeadIconLarge` | `decoded_exported` | `/Game/Aki/UI/UIResources/Common/Image/IconRoleHead256/T_IconRoleHead256_56_UI.T_IconRoleHead256_56_UI` | `restricted://_visual_media/character_visual_v0_2/client_textures/Aki/UI/UIResources/Common/Image/IconRoleHead256/T_IconRoleHead256_56_UI.png` |
| formation_pile_art | `FormationRoleCard` | `decoded_exported` | `/Game/Aki/UI/UIResources/Common/Image/IconRolePile/T_IconRole_Pile_qiuyuan_UI.T_IconRole_Pile_qiuyuan_UI` | `restricted://_visual_media/character_visual_v0_2/client_textures/Aki/UI/UIResources/Common/Image/IconRolePile/T_IconRole_Pile_qiuyuan_UI.png` |
| activity_portrait | `RolePortrait` | `decoded_exported` | `/Game/Aki/UI/UIResources/Common/Image/PixActivity/T_ActivityRoleQiuyuan.T_ActivityRoleQiuyuan` | `restricted://_visual_media/character_visual_v0_2/client_textures/Aki/UI/UIResources/Common/Image/PixActivity/T_ActivityRoleQiuyuan.png` |
| head_icon | `RoleHeadIconCircle` | `reference_only` | `/Game/Aki/UI/UIResources/Common/Image/IconRoleHeadCircle256/T_IconRoleHeadCircle256_56_UI.T_IconRoleHeadCircle256_56_UI` | `—` |
| head_icon | `RoleHeadIconBig` | `reference_only` | `/Game/Aki/UI/UIResources/Common/Image/IconRoleHead150/T_IconRoleHead150_56_UI.T_IconRoleHead150_56_UI` | `—` |
| head_icon | `Card` | `reference_only` | `/Game/Aki/UI/UIResources/Common/Image/IconRoleHead175/T_IconRoleHead175_56_UI.T_IconRoleHead175_56_UI` | `—` |
| head_icon | `RoleHeadIcon` | `reference_only` | `/Game/Aki/UI/UIResources/Common/Image/IconRoleHead80/T_IconRoleHead80_56_UI.T_IconRoleHead80_56_UI` | `—` |
| quest_stand | `RoleStand` | `ambiguous` | `/Game/Aki/UI/UIResources/UiQuest/Image/ChuanShuo/T_IconChuanShuo1_UI.T_IconChuanShuo1_UI` | `—` |
| spine_portrait | `FormationSpineAtlas` | `ambiguous` | `/Game/Aki/UI/UIResources/Common/Spine/Portraits/Portraits_Anke/Portraits_Anke.Portraits_Anke-atlas` | `—` |
| spine_portrait | `FormationSpineSkeletonData` | `ambiguous` | `/Game/Aki/UI/UIResources/Common/Spine/Portraits/Portraits_Anke/Portraits_Anke.Portraits_Anke-data` | `—` |
| performance_animation | `UiScenePerformanceABP` | `reference_only` | `/Game/Aki/Character/Role/MaleXL/Qiuyuan/R2T1QiuyuanMd10011/ABP_Performance_Qiuyuan_PC.ABP_Performance_Qiuyuan_PC_C` | `—` |

The exported PNGs remain local/restricted copyrighted evidence. The repository-facing profile and manifest carry hashes and provenance, not a grant to redistribute the artwork.
