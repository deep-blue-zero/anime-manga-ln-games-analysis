---
series: WUWA
character: Jinhsi
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

# Jinhsi — Visual Design and Appearance Profile

Status: `active_provisional`
Generation: `character_visual_v0_2`
Visual evidence manifest: `CHARACTER_VISUAL_REFERENCE_MANIFEST.json`

## Individualized summary

Jinhsi is designed as a young civic and ceremonial authority rather than an armored ruler. Silver-white hair, pale blue ribbons, black-and-gold collar pieces, layered white panels, teal trailing cloth, and a poised hands-folded stance make her appear gentle and highly composed while preserving signs of formal office.

## Evidence boundary

This first-pass profile is grounded in three decoded official-client UI textures: the large head icon, formation pile art, and activity portrait. Those images are authoritative as client-derived raw visual evidence for their own pixels, not as proof of unseen rear construction, exact physical materials, runtime animation, alternate skins/forms, or developer intent. The normalized role/profile record supplies semantic context but remains a separate authority layer.

Semantic role context is summarized only in the design–narrative claim below; the exact normalized source locator is retained in the JSON profile rather than reproducing the source text here.

## Structured observations

| Dimension | Observation | Basis | Confidence |
|---|---|---|---|
| silhouette | Paired side locks, extremely long split hair tails, narrow ribbon streamers, layered coat-skirt panels, thigh-high boots, and a long blue-edged implement create a tall, symmetrical silhouette softened by many curved trailing lines. | `direct_visual` | `high` |
| palette | Silver-white and cool pale blue dominate, anchored by black at the bodice and shoulders, muted teal in the long back panels, and restrained antique-gold edging and fittings. | `direct_visual` | `high` |
| hair and face | Silver-white hair is cut in straight bangs and gathered into paired side sections with large blue ribbon clusters and gold loop ornaments; pale gray-gold eyes and a quiet expression keep the face youthful but formal. | `direct_visual` | `high` |
| costume construction | A black fitted high-collar underlayer and short structured shoulder cape sit beneath layered white and pale-blue front panels, teal back drapery, belts, small arm plates, fitted shorts, and tall white boots. | `direct_visual` | `high` |
| materials | Soft ribbon and flowing white-teal cloth contrast with black structured panels, fine gold piping, small metallic fasteners, and pale surfaces patterned like scales, feathers, or woven diamonds. | `direct_visual` | `medium` |
| motifs | Paired loops, ribbons, tassels, cloud-like curves, cool blue gradients, fine geometric lattice, and small gold ceremonial flourishes repeat from the hair ornaments through the garment hems. | `direct_visual` | `high` |
| weapon and role signaling | A long blue-edged, ornamented weapon or ceremonial implement is partly visible behind her; the bounded angle does not establish its complete construction, while the formal collar and layered robes clearly signal public office. | `direct_visual` | `medium` |
| pose and body language | Hands folded at the waist, level shoulders, close-set feet, and a direct but softened gaze communicate restraint, courtesy, and deliberate calm. | `direct_visual` | `high` |
| design narrative relationship | The winter-white palette, modestly folded posture, and ceremonial detailing closely support the semantic profile's image of a humble Magistrate who brightens public hope like winter sunlight; any dragon or Sentinel-specific reading of individual ornaments requires additional evidence. | `direct_visual_and_semantic` | `medium` |

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
| head_icon | `RoleHeadIconLarge` | `decoded_exported` | `/Game/Aki/UI/UIResources/Common/Image/IconRoleHead256/T_IconRoleHead256_24_UI.T_IconRoleHead256_24_UI` | `restricted://_visual_media/character_visual_v0_2/client_textures/Aki/UI/UIResources/Common/Image/IconRoleHead256/T_IconRoleHead256_24_UI.png` |
| formation_pile_art | `FormationRoleCard` | `decoded_exported` | `/Game/Aki/UI/UIResources/Common/Image/IconRolePile/T_IconRole_Pile_jinxi_UI.T_IconRole_Pile_jinxi_UI` | `restricted://_visual_media/character_visual_v0_2/client_textures/Aki/UI/UIResources/Common/Image/IconRolePile/T_IconRole_Pile_jinxi_UI.png` |
| activity_portrait | `RolePortrait` | `decoded_exported` | `/Game/Aki/UI/UIResources/Common/Image/PixActivity/T_ActivityRoleJinxi.T_ActivityRoleJinxi` | `restricted://_visual_media/character_visual_v0_2/client_textures/Aki/UI/UIResources/Common/Image/PixActivity/T_ActivityRoleJinxi.png` |
| head_icon | `RoleHeadIconCircle` | `reference_only` | `/Game/Aki/UI/UIResources/Common/Image/IconRoleHeadCircle256/T_IconRoleHeadCircle256_24_UI.T_IconRoleHeadCircle256_24_UI` | `—` |
| head_icon | `RoleHeadIconBig` | `reference_only` | `/Game/Aki/UI/UIResources/Common/Image/IconRoleHead150/T_IconRoleHead150_24_UI.T_IconRoleHead150_24_UI` | `—` |
| head_icon | `Card` | `reference_only` | `/Game/Aki/UI/UIResources/Common/Image/IconRoleHead175/T_IconRoleHead175_24_UI.T_IconRoleHead175_24_UI` | `—` |
| head_icon | `RoleHeadIcon` | `reference_only` | `/Game/Aki/UI/UIResources/Common/Image/IconRoleHead80/T_IconRoleHead80_24_UI.T_IconRoleHead80_24_UI` | `—` |
| quest_stand | `RoleStand` | `ambiguous` | `/Game/Aki/UI/UIResources/UiQuest/Image/ChuanShuo/T_IconChuanShuo1_UI.T_IconChuanShuo1_UI` | `—` |
| spine_portrait | `FormationSpineAtlas` | `ambiguous` | `/Game/Aki/UI/UIResources/Common/Spine/Portraits/Portraits_Anke/Portraits_Anke.Portraits_Anke-atlas` | `—` |
| spine_portrait | `FormationSpineSkeletonData` | `ambiguous` | `/Game/Aki/UI/UIResources/Common/Spine/Portraits/Portraits_Anke/Portraits_Anke.Portraits_Anke-data` | `—` |
| performance_animation | `UiScenePerformanceABP` | `reference_only` | `/Game/Aki/Character/Role/FemaleM/Jinxi/R2T1JinxiMd10011/ABP_Performance_Jinxi_PC.ABP_Performance_Jinxi_PC_C` | `—` |

The exported PNGs remain local/restricted copyrighted evidence. The repository-facing profile and manifest carry hashes and provenance, not a grant to redistribute the artwork.
