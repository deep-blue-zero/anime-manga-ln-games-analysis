---
series: WUWA
character: Iuno
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

# Iuno — Visual Design and Appearance Profile

Status: `active_provisional`
Generation: `character_visual_v0_2`
Visual evidence manifest: `CHARACTER_VISUAL_REFERENCE_MANIFEST.json`

## Individualized summary

Iuno reads as a celestial priestess in motion. Deep-blue twin tails, a white-and-gold draped costume, laurel and wing ornaments, blue crystals, and a monumental jeweled ring frame her as an astronomical or fate-reading figure rather than a conventional cleric.

## Evidence boundary

This first-pass profile is grounded in three decoded official-client UI textures: the large head icon, formation pile art, and activity portrait. Those images are authoritative as client-derived raw visual evidence for their own pixels, not as proof of unseen rear construction, exact physical materials, runtime animation, alternate skins/forms, or developer intent. The normalized role/profile record supplies semantic context but remains a separate authority layer.

Semantic role context is summarized only in the design–narrative claim below; the exact normalized source locator is retained in the JSON profile rather than reproducing the source text here.

## Structured observations

| Dimension | Observation | Basis | Confidence |
|---|---|---|---|
| silhouette | Two enormous ponytails, long trailing sashes, asymmetric drapery, and the large crescent/ring device create a circular, orbiting silhouette. | `direct_visual` | `high` |
| palette | Deep midnight blue grading to pale blue is balanced by white and warm gold, with clear sapphire focal points and small black structural accents. | `direct_visual` | `high` |
| hair and face | Long blue hair is split into high twin tails with gold-edged bands and laurel/wing ornaments; gold-blue eyes and a slight smile keep the face confident. | `direct_visual` | `high` |
| costume construction | A one-shoulder white drape, gold collar, strapped bodice, short layered skirt, arm wraps, broad bracelets, pendant hardware, and wrapped sandals combine classical and fantasy construction. | `direct_visual` | `high` |
| materials | Flowing white cloth and star-speckled hair contrast with rigid gold framework and large glassy blue stones. | `direct_visual` | `medium` |
| motifs | Laurel leaves, wings, stars, circles, crescents, pendants, and orbit-like rings repeat from headpiece to weapon/device. | `direct_visual` | `high` |
| weapon and role signaling | The enormous jeweled circular device reads as ritual instrument, celestial chart, shield, or weapon; the images prove its prominence but not its exact operation. | `direct_visual` | `medium` |
| pose and body language | Open palms, lifted foot, curved limbs, and hair flowing around the ring give the art a weightless, guiding rhythm. | `direct_visual` | `high` |
| design narrative relationship | Circular fate imagery and priestess regalia align closely with the semantic profile's defiant Priestess walking a web of destiny, while the device's precise symbolism remains interpretive. | `direct_visual_and_semantic` | `medium` |

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
| head_icon | `RoleHeadIconLarge` | `decoded_exported` | `/Game/Aki/UI/UIResources/Common/Image/IconRoleHead256/T_IconRoleHead256_48_UI.T_IconRoleHead256_48_UI` | `restricted://_visual_media/character_visual_v0_2/client_textures/Aki/UI/UIResources/Common/Image/IconRoleHead256/T_IconRoleHead256_48_UI.png` |
| formation_pile_art | `FormationRoleCard` | `decoded_exported` | `/Game/Aki/UI/UIResources/Common/Image/IconRolePile/T_IconRole_Pile_younuo_UI.T_IconRole_Pile_younuo_UI` | `restricted://_visual_media/character_visual_v0_2/client_textures/Aki/UI/UIResources/Common/Image/IconRolePile/T_IconRole_Pile_younuo_UI.png` |
| activity_portrait | `RolePortrait` | `decoded_exported` | `/Game/Aki/UI/UIResources/Common/Image/PixActivity/T_ActivityRoleYounuo.T_ActivityRoleYounuo` | `restricted://_visual_media/character_visual_v0_2/client_textures/Aki/UI/UIResources/Common/Image/PixActivity/T_ActivityRoleYounuo.png` |
| head_icon | `RoleHeadIconCircle` | `reference_only` | `/Game/Aki/UI/UIResources/Common/Image/IconRoleHeadCircle256/T_IconRoleHeadCircle256_48_UI.T_IconRoleHeadCircle256_48_UI` | `—` |
| head_icon | `RoleHeadIconBig` | `reference_only` | `/Game/Aki/UI/UIResources/Common/Image/IconRoleHead150/T_IconRoleHead150_48_UI.T_IconRoleHead150_48_UI` | `—` |
| head_icon | `Card` | `reference_only` | `/Game/Aki/UI/UIResources/Common/Image/IconRoleHead175/T_IconRoleHead175_48_UI.T_IconRoleHead175_48_UI` | `—` |
| head_icon | `RoleHeadIcon` | `reference_only` | `/Game/Aki/UI/UIResources/Common/Image/IconRoleHead80/T_IconRoleHead80_48_UI.T_IconRoleHead80_48_UI` | `—` |
| quest_stand | `RoleStand` | `ambiguous` | `/Game/Aki/UI/UIResources/UiQuest/Image/ChuanShuo/T_IconChuanShuo1_UI.T_IconChuanShuo1_UI` | `—` |
| spine_portrait | `FormationSpineAtlas` | `ambiguous` | `/Game/Aki/UI/UIResources/Common/Spine/Portraits/Portraits_Anke/Portraits_Anke.Portraits_Anke-atlas` | `—` |
| spine_portrait | `FormationSpineSkeletonData` | `ambiguous` | `/Game/Aki/UI/UIResources/Common/Spine/Portraits/Portraits_Anke/Portraits_Anke.Portraits_Anke-data` | `—` |
| performance_animation | `UiScenePerformanceABP` | `reference_only` | `/Game/Aki/Character/Role/FemaleM/Younuo/R2T1YounuoMd10011/ABP_Performance_Younuo_PC.ABP_Performance_Younuo_PC_C` | `—` |

The exported PNGs remain local/restricted copyrighted evidence. The repository-facing profile and manifest carry hashes and provenance, not a grant to redistribute the artwork.
