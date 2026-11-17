---
series: WUWA
character: Augusta
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

# Augusta — Visual Design and Appearance Profile

Status: `active_provisional`
Generation: `character_visual_v0_2`
Visual evidence manifest: `CHARACTER_VISUAL_REFERENCE_MANIFEST.json`

## Individualized summary

Augusta has a tall, commanding solar-warrior design. Flame-orange hair, a radiating crown, white ceremonial drapery, gold armor, and a huge black-gold fan-like weapon turn her into a moving sun-banner rather than a conventional armored soldier.

## Evidence boundary

This first-pass profile is grounded in three decoded official-client UI textures: the large head icon, formation pile art, and activity portrait. Those images are authoritative as client-derived raw visual evidence for their own pixels, not as proof of unseen rear construction, exact physical materials, runtime animation, alternate skins/forms, or developer intent. The normalized role/profile record supplies semantic context but remains a separate authority layer.

Semantic role context is summarized only in the design–narrative claim below; the exact normalized source locator is retained in the JSON profile rather than reproducing the source text here.

## Structured observations

| Dimension | Observation | Basis | Confidence |
|---|---|---|---|
| silhouette | Long flame-shaped hair, a high radial crown, shoulder drapery, and a floor-length split garment produce a tall triangular silhouette; the oversized circular fan/weapon adds a second sun-disc behind her. | `direct_visual` | `high` |
| palette | Fiery orange-red hair is set against white, warm gold, black, and small bronze-brown areas, producing a solar palette with severe dark counterweight. | `direct_visual` | `high` |
| hair and face | Her extremely long orange hair is swept into flame-like waves, while the eyes are partly shadowed by the crown; her neutral expression is restrained and authoritative. | `direct_visual` | `high` |
| costume construction | A fitted gold-toned armored torso is layered under white patterned drapery, asymmetric shoulder pieces, black neck protection, forearm guards, a high-slit skirt, and strapped sandals. | `direct_visual` | `high` |
| materials | The render differentiates polished gold armor and jewelry, bright woven drapery, dark metal or lacquer on the fan, and lighter flexible shoulder cloth. | `direct_visual` | `medium` |
| motifs | Sunbursts, stars, rays, and circular medallions recur in the crown, earrings, chest ornament, belt, and weapon. | `direct_visual` | `high` |
| weapon and role signaling | The enormous radiating fan-like weapon and guarded bracers combine ceremonial authority with credible battlefield weight. | `direct_visual` | `medium` |
| pose and body language | Her square shoulders, level gaze, and relaxed grip communicate control rather than exertion; the hair and cloth provide motion around an otherwise stable center. | `direct_visual` | `high` |
| design narrative relationship | The solar crown, banner-like drapery, and conqueror's stance directly reinforce the profile's language of an 'undying sun' and undefeated Ephor, while the exact symbolic program remains interpretive. | `direct_visual_and_semantic` | `medium` |

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
| head_icon | `RoleHeadIconLarge` | `decoded_exported` | `/Game/Aki/UI/UIResources/Common/Image/IconRoleHead256/T_IconRoleHead256_51_UI.T_IconRoleHead256_51_UI` | `restricted://_visual_media/character_visual_v0_2/client_textures/Aki/UI/UIResources/Common/Image/IconRoleHead256/T_IconRoleHead256_51_UI.png` |
| formation_pile_art | `FormationRoleCard` | `decoded_exported` | `/Game/Aki/UI/UIResources/Common/Image/IconRolePile/T_IconRole_Pile_aogusita_UI.T_IconRole_Pile_aogusita_UI` | `restricted://_visual_media/character_visual_v0_2/client_textures/Aki/UI/UIResources/Common/Image/IconRolePile/T_IconRole_Pile_aogusita_UI.png` |
| activity_portrait | `RolePortrait` | `decoded_exported` | `/Game/Aki/UI/UIResources/Common/Image/PixActivity/T_ActivityRoleAogusita.T_ActivityRoleAogusita` | `restricted://_visual_media/character_visual_v0_2/client_textures/Aki/UI/UIResources/Common/Image/PixActivity/T_ActivityRoleAogusita.png` |
| head_icon | `RoleHeadIconCircle` | `reference_only` | `/Game/Aki/UI/UIResources/Common/Image/IconRoleHeadCircle256/T_IconRoleHeadCircle256_51_UI.T_IconRoleHeadCircle256_51_UI` | `—` |
| head_icon | `RoleHeadIconBig` | `reference_only` | `/Game/Aki/UI/UIResources/Common/Image/IconRoleHead150/T_IconRoleHead150_51_UI.T_IconRoleHead150_51_UI` | `—` |
| head_icon | `Card` | `reference_only` | `/Game/Aki/UI/UIResources/Common/Image/IconRoleHead175/T_IconRoleHead175_51_UI.T_IconRoleHead175_51_UI` | `—` |
| head_icon | `RoleHeadIcon` | `reference_only` | `/Game/Aki/UI/UIResources/Common/Image/IconRoleHead80/T_IconRoleHead80_51_UI.T_IconRoleHead80_51_UI` | `—` |
| quest_stand | `RoleStand` | `ambiguous` | `/Game/Aki/UI/UIResources/UiQuest/Image/ChuanShuo/T_IconChuanShuo1_UI.T_IconChuanShuo1_UI` | `—` |
| spine_portrait | `FormationSpineAtlas` | `ambiguous` | `/Game/Aki/UI/UIResources/Common/Spine/Portraits/Portraits_Anke/Portraits_Anke.Portraits_Anke-atlas` | `—` |
| spine_portrait | `FormationSpineSkeletonData` | `ambiguous` | `/Game/Aki/UI/UIResources/Common/Spine/Portraits/Portraits_Anke/Portraits_Anke.Portraits_Anke-data` | `—` |
| performance_animation | `UiScenePerformanceABP` | `reference_only` | `/Game/Aki/Character/Role/FemaleXL/Aogusita/R2T1AogusitaMd10011/ABP_Performance_Aogusita_PC.ABP_Performance_Aogusita_PC_C` | `—` |

The exported PNGs remain local/restricted copyrighted evidence. The repository-facing profile and manifest carry hashes and provenance, not a grant to redistribute the artwork.
