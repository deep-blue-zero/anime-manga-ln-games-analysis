---
series: WUWA
character: Brant
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

# Brant — Visual Design and Appearance Profile

Status: `active_provisional`
Generation: `character_visual_v0_2`
Visual evidence manifest: `CHARACTER_VISUAL_REFERENCE_MANIFEST.json`

## Individualized summary

Brant is a theatrical swashbuckler: a plumed tricorn, tousled blue hair, open-collared pirate coat, magenta lining, white trousers, and an ornate blade. His costume deliberately merges ship-captain authority with stage-performer flamboyance.

## Evidence boundary

This first-pass profile is grounded in three decoded official-client UI textures: the large head icon, formation pile art, and activity portrait. Those images are authoritative as client-derived raw visual evidence for their own pixels, not as proof of unseen rear construction, exact physical materials, runtime animation, alternate skins/forms, or developer intent. The normalized role/profile record supplies semantic context but remains a separate authority layer.

Semantic role context is summarized only in the design–narrative claim below; the exact normalized source locator is retained in the JSON profile rather than reproducing the source text here.

## Structured observations

| Dimension | Observation | Basis | Confidence |
|---|---|---|---|
| silhouette | The wide tricorn, raised coat collar, flared cape tails, ribbons, and long fitted boots create an animated hourglass silhouette with many directional points. | `direct_visual` | `high` |
| palette | Navy, white, cyan-blue, and black form the base, while hot magenta lining and feathers supply the theatrical focal color; gold and silver details punctuate the costume. | `direct_visual` | `high` |
| hair and face | Short tousled blue hair, magenta eyes, a broad smile, and a visible chest scar make the portrait simultaneously playful and battle-worn. | `direct_visual` | `high` |
| costume construction | A cropped, open naval coat sits over a loose dark shirt and fitted white trousers, with ruffled cuffs, belts, buckles, ribbons, gloves, and tall asymmetrically colored boots. | `direct_visual` | `high` |
| materials | Glossy black glove and boot surfaces contrast with patterned blue cloth, crisp white tailoring, metallic fasteners, and feathers. | `direct_visual` | `medium` |
| motifs | Maritime insignia, roses/spirals, crossed or star-like metal marks, feathers, cords, and theatrical ruffles repeat across the hat and coat. | `direct_visual` | `high` |
| weapon and role signaling | An ornate one-handed blade at the hip and naval styling clearly signal a mobile duelist/captain rather than a heavy frontline fighter. | `direct_visual` | `medium` |
| pose and body language | The hand tipping his hat, open grin, loose shoulders, and crossed forearms read as practiced showmanship. | `direct_visual` | `high` |
| design narrative relationship | The captain's silhouette and costume-as-performance align closely with the semantic profile of a free-spirited Troupe of Fools leader who adopts roles on stage but remains sincere offstage. | `direct_visual_and_semantic` | `medium` |

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
| head_icon | `RoleHeadIconLarge` | `decoded_exported` | `/Game/Aki/UI/UIResources/Common/Image/IconRoleHead256/T_IconRoleHead256_44_UI.T_IconRoleHead256_44_UI` | `restricted://_visual_media/character_visual_v0_2/client_textures/Aki/UI/UIResources/Common/Image/IconRoleHead256/T_IconRoleHead256_44_UI.png` |
| formation_pile_art | `FormationRoleCard` | `decoded_exported` | `/Game/Aki/UI/UIResources/Common/Image/IconRolePile/T_IconRole_Pile_Bulante_UI.T_IconRole_Pile_Bulante_UI` | `restricted://_visual_media/character_visual_v0_2/client_textures/Aki/UI/UIResources/Common/Image/IconRolePile/T_IconRole_Pile_Bulante_UI.png` |
| activity_portrait | `RolePortrait` | `decoded_exported` | `/Game/Aki/UI/UIResources/Common/Image/PixActivity/T_ActivityRoleBulante.T_ActivityRoleBulante` | `restricted://_visual_media/character_visual_v0_2/client_textures/Aki/UI/UIResources/Common/Image/PixActivity/T_ActivityRoleBulante.png` |
| head_icon | `RoleHeadIconCircle` | `reference_only` | `/Game/Aki/UI/UIResources/Common/Image/IconRoleHeadCircle256/T_IconRoleHeadCircle256_44_UI.T_IconRoleHeadCircle256_44_UI` | `—` |
| head_icon | `RoleHeadIconBig` | `reference_only` | `/Game/Aki/UI/UIResources/Common/Image/IconRoleHead150/T_IconRoleHead150_44_UI.T_IconRoleHead150_44_UI` | `—` |
| head_icon | `Card` | `reference_only` | `/Game/Aki/UI/UIResources/Common/Image/IconRoleHead175/T_IconRoleHead175_44_UI.T_IconRoleHead175_44_UI` | `—` |
| head_icon | `RoleHeadIcon` | `reference_only` | `/Game/Aki/UI/UIResources/Common/Image/IconRoleHead80/T_IconRoleHead80_44_UI.T_IconRoleHead80_44_UI` | `—` |
| quest_stand | `RoleStand` | `ambiguous` | `/Game/Aki/UI/UIResources/UiQuest/Image/ChuanShuo/T_IconChuanShuo1_UI.T_IconChuanShuo1_UI` | `—` |
| spine_portrait | `FormationSpineAtlas` | `ambiguous` | `/Game/Aki/UI/UIResources/Common/Spine/Portraits/Portraits_Anke/Portraits_Anke.Portraits_Anke-atlas` | `—` |
| spine_portrait | `FormationSpineSkeletonData` | `ambiguous` | `/Game/Aki/UI/UIResources/Common/Spine/Portraits/Portraits_Anke/Portraits_Anke.Portraits_Anke-data` | `—` |
| performance_animation | `UiScenePerformanceABP` | `reference_only` | `/Game/Aki/Character/Role/MaleXL/Bulante/R2T1BulanteMd10011/ABP_Performance_Bulante_PC.ABP_Performance_Bulante_PC_C` | `—` |

The exported PNGs remain local/restricted copyrighted evidence. The repository-facing profile and manifest carry hashes and provenance, not a grant to redistribute the artwork.
