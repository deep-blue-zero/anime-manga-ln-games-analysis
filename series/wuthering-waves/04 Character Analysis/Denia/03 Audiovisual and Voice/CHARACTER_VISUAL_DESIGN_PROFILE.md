---
series: WUWA
character: Denia
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

# Denia — Visual Design and Appearance Profile

Status: `active_provisional`
Generation: `character_visual_v0_2`
Visual evidence manifest: `CHARACTER_VISUAL_REFERENCE_MANIFEST.json`

## Individualized summary

Denia is a soft, sleepy academy-fashion design complicated by dark hardware. Very long pastel-pink hair, a layered white-and-pink dress, fur-trimmed sleeves, blue gems, dangling plush figures, chains, rope, and red gloves create a sweet surface with deliberately odd, slightly ominous attachments.

## Evidence boundary

This first-pass profile is grounded in three decoded official-client UI textures: the large head icon, formation pile art, and activity portrait. Those images are authoritative as client-derived raw visual evidence for their own pixels, not as proof of unseen rear construction, exact physical materials, runtime animation, alternate skins/forms, or developer intent. The normalized role/profile record supplies semantic context but remains a separate authority layer.

Semantic role context is summarized only in the design–narrative claim below; the exact normalized source locator is retained in the JSON profile rather than reproducing the source text here.

## Structured observations

| Dimension | Observation | Basis | Confidence |
|---|---|---|---|
| silhouette | Large curled hair masses and voluminous sleeves frame a short layered dress; chains, tassels, plush charms, and long side panels add many small hanging shapes. | `direct_visual` | `high` |
| palette | Powder pink, white, pale blue, and black dominate, with turquoise gems, gold chains, brown rope, and sharp red gloves as accents. | `direct_visual` | `high` |
| hair and face | Long pink hair shifts toward pale blue at the ends and is gathered into an elaborate side coil; pastel irises and a small smile create a gentle expression. | `direct_visual` | `high` |
| costume construction | The dress combines a pale wrapped bodice, layered white outer skirt, black ruffled underskirt, oversized pink sleeves, dark straps, red gloves, and ribboned black shoes. | `direct_visual` | `high` |
| materials | Fine pale fabric and fluffy trim contrast with coarse rope, metal chain, polished blue stones, leather-like straps, and soft plush charms. | `direct_visual` | `medium` |
| motifs | Sleep/toy cues, bundled cords, faceted blue gems, diamond/star cutouts, and asymmetrically suspended ornaments repeat across the outfit. | `direct_visual` | `high` |
| weapon and role signaling | No weapon appears in the bounded UI art; chains, ropes, and the dark toy charms imply an unconventional toolkit but do not prove combat function. | `direct_visual` | `medium` |
| pose and body language | A relaxed raised hand, softened eyes, and a small smile fit a low-energy, socially pleasant presentation. | `direct_visual` | `high` |
| design narrative relationship | The comfortable pastel surface supports the semantic profile's professional-slacker and gentle-smile persona, while the chains and dark charms prevent the reading from becoming purely innocent. | `direct_visual_and_semantic` | `medium` |

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
| head_icon | `RoleHeadIconLarge` | `decoded_exported` | `/Game/Aki/UI/UIResources/Common/Image/IconRoleHead256/T_IconRoleHead256_64_UI.T_IconRoleHead256_64_UI` | `restricted://_visual_media/character_visual_v0_2/client_textures/Aki/UI/UIResources/Common/Image/IconRoleHead256/T_IconRoleHead256_64_UI.png` |
| formation_pile_art | `FormationRoleCard` | `decoded_exported` | `/Game/Aki/UI/UIResources/Common/Image/IconRolePile/T_IconRole_Pile_daniya_UI.T_IconRole_Pile_daniya_UI` | `restricted://_visual_media/character_visual_v0_2/client_textures/Aki/UI/UIResources/Common/Image/IconRolePile/T_IconRole_Pile_daniya_UI.png` |
| activity_portrait | `RolePortrait` | `decoded_exported` | `/Game/Aki/UI/UIResources/Common/Image/PixActivity/T_ActivityRoleDaniya.T_ActivityRoleDaniya` | `restricted://_visual_media/character_visual_v0_2/client_textures/Aki/UI/UIResources/Common/Image/PixActivity/T_ActivityRoleDaniya.png` |
| head_icon | `RoleHeadIconCircle` | `reference_only` | `/Game/Aki/UI/UIResources/Common/Image/IconRoleHeadCircle256/T_IconRoleHeadCircle256_64_UI.T_IconRoleHeadCircle256_64_UI` | `—` |
| head_icon | `RoleHeadIconBig` | `reference_only` | `/Game/Aki/UI/UIResources/Common/Image/IconRoleHead150/T_IconRoleHead150_64_UI.T_IconRoleHead150_64_UI` | `—` |
| head_icon | `Card` | `reference_only` | `/Game/Aki/UI/UIResources/Common/Image/IconRoleHead175/T_IconRoleHead175_64_UI.T_IconRoleHead175_64_UI` | `—` |
| head_icon | `RoleHeadIcon` | `reference_only` | `/Game/Aki/UI/UIResources/Common/Image/IconRoleHead80/T_IconRoleHead80_64_UI.T_IconRoleHead80_64_UI` | `—` |
| quest_stand | `RoleStand` | `ambiguous` | `/Game/Aki/UI/UIResources/UiQuest/Image/ChuanShuo/T_IconChuanShuo1_UI.T_IconChuanShuo1_UI` | `—` |
| spine_portrait | `FormationSpineAtlas` | `ambiguous` | `/Game/Aki/UI/UIResources/Common/Spine/Portraits/Portraits_Anke/Portraits_Anke.Portraits_Anke-atlas` | `—` |
| spine_portrait | `FormationSpineSkeletonData` | `ambiguous` | `/Game/Aki/UI/UIResources/Common/Spine/Portraits/Portraits_Anke/Portraits_Anke.Portraits_Anke-data` | `—` |
| performance_animation | `UiScenePerformanceABP` | `reference_only` | `/Game/Aki/Character/Role/FemaleMS/Daniya/R2T1DaniyaMd10011/ABP_Performance_Daniya_PC.ABP_Performance_Daniya_PC_C` | `—` |

The exported PNGs remain local/restricted copyrighted evidence. The repository-facing profile and manifest carry hashes and provenance, not a grant to redistribute the artwork.
