---
series: WUWA
character: Phoebe
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

# Phoebe — Visual Design and Appearance Profile

Status: `active_provisional`
Generation: `character_visual_v0_2`
Visual evidence manifest: `CHARACTER_VISUAL_REFERENCE_MANIFEST.json`

## Individualized summary

Phoebe combines acolyte, scholar, and storybook traveler. Long curled blonde hair, a very wide white hat, royal-blue stole-like panels, white tailored layers, black lace, gold devotional motifs, and a long staff produce a gentle but highly formal silhouette.

## Evidence boundary

This first-pass profile is grounded in three decoded official-client UI textures: the large head icon, formation pile art, and activity portrait. Those images are authoritative as client-derived raw visual evidence for their own pixels, not as proof of unseen rear construction, exact physical materials, runtime animation, alternate skins/forms, or developer intent. The normalized role/profile record supplies semantic context but remains a separate authority layer.

Semantic role context is summarized only in the design–narrative claim below; the exact normalized source locator is retained in the JSON profile rather than reproducing the source text here.

## Structured observations

| Dimension | Observation | Basis | Confidence |
|---|---|---|---|
| silhouette | The wide hat brim, long curled hair, broad blue back panels, flared white coat, and vertical staff create a clear cross-shaped silhouette. | `direct_visual` | `high` |
| palette | White and royal blue dominate, framed by black cuffs and underlayers and warmed by gold stars, floral filigree, and blonde hair. | `direct_visual` | `high` |
| hair and face | Blonde curls fall in long loops beneath the hat; straight bangs, blue-violet eyes, and a small smile make the face calm and approachable. | `direct_visual` | `high` |
| costume construction | A short white coat-dress with wide sleeves is layered over black lace and fitted pale legwear, then structured by a blue stole/cape, narrow belt, tassels, gloves, and white ankle boots. | `direct_visual` | `high` |
| materials | Crisp white cloth, rich blue textile, black lace edging, polished gold ornament, ribbon, and the rigid staff are visibly distinct. | `direct_visual` | `medium` |
| motifs | Stars, flowers/roses, devotional tassels, scroll-like white patterning, crosses or four-point marks, and bookish hat styling recur across the costume. | `direct_visual` | `high` |
| weapon and role signaling | The long staff and formal acolyte styling suggest ritual support or spellcasting more than close combat. | `direct_visual` | `medium` |
| pose and body language | One hand tips the broad hat while the staff rests behind her; the relaxed smile and upright posture read as courteous and self-possessed. | `direct_visual` | `high` |
| design narrative relationship | The luminous blue-white vestment, staff, and gentle expression closely support the profile of a diligent Acolyte whose prayers offer comfort and peace. | `direct_visual_and_semantic` | `medium` |

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
| head_icon | `RoleHeadIconLarge` | `decoded_exported` | `/Game/Aki/UI/UIResources/Common/Image/IconRoleHead256/T_IconRoleHead256_45_UI.T_IconRoleHead256_45_UI` | `restricted://_visual_media/character_visual_v0_2/client_textures/Aki/UI/UIResources/Common/Image/IconRoleHead256/T_IconRoleHead256_45_UI.png` |
| formation_pile_art | `FormationRoleCard` | `decoded_exported` | `/Game/Aki/UI/UIResources/Common/Image/IconRolePile/T_IconRole_Pile_Feibi_UI.T_IconRole_Pile_Feibi_UI` | `restricted://_visual_media/character_visual_v0_2/client_textures/Aki/UI/UIResources/Common/Image/IconRolePile/T_IconRole_Pile_Feibi_UI.png` |
| activity_portrait | `RolePortrait` | `decoded_exported` | `/Game/Aki/UI/UIResources/Common/Image/PixActivity/T_ActivityRoleFeibi.T_ActivityRoleFeibi` | `restricted://_visual_media/character_visual_v0_2/client_textures/Aki/UI/UIResources/Common/Image/PixActivity/T_ActivityRoleFeibi.png` |
| head_icon | `RoleHeadIconCircle` | `reference_only` | `/Game/Aki/UI/UIResources/Common/Image/IconRoleHeadCircle256/T_IconRoleHeadCircle256_45_UI.T_IconRoleHeadCircle256_45_UI` | `—` |
| head_icon | `RoleHeadIconBig` | `reference_only` | `/Game/Aki/UI/UIResources/Common/Image/IconRoleHead150/T_IconRoleHead150_45_UI.T_IconRoleHead150_45_UI` | `—` |
| head_icon | `Card` | `reference_only` | `/Game/Aki/UI/UIResources/Common/Image/IconRoleHead175/T_IconRoleHead175_45_UI.T_IconRoleHead175_45_UI` | `—` |
| head_icon | `RoleHeadIcon` | `reference_only` | `/Game/Aki/UI/UIResources/Common/Image/IconRoleHead80/T_IconRoleHead80_45_UI.T_IconRoleHead80_45_UI` | `—` |
| quest_stand | `RoleStand` | `ambiguous` | `/Game/Aki/UI/UIResources/UiQuest/Image/ChuanShuo/T_IconChuanShuo1_UI.T_IconChuanShuo1_UI` | `—` |
| spine_portrait | `FormationSpineAtlas` | `ambiguous` | `/Game/Aki/UI/UIResources/Common/Spine/Portraits/Portraits_Anke/Portraits_Anke.Portraits_Anke-atlas` | `—` |
| spine_portrait | `FormationSpineSkeletonData` | `ambiguous` | `/Game/Aki/UI/UIResources/Common/Spine/Portraits/Portraits_Anke/Portraits_Anke.Portraits_Anke-data` | `—` |
| performance_animation | `UiScenePerformanceABP` | `reference_only` | `/Game/Aki/Character/Role/FemaleMS/Feibi/R2T1FeibiMd10011/ABP_Performance_FeiBi_PC.ABP_Performance_FeiBi_PC_C` | `—` |

The exported PNGs remain local/restricted copyrighted evidence. The repository-facing profile and manifest carry hashes and provenance, not a grant to redistribute the artwork.
