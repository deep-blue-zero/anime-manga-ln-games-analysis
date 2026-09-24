---
series: WUWA
character: Cantarella
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

# Cantarella — Visual Design and Appearance Profile

Status: `active_provisional`
Generation: `character_visual_v0_2`
Visual evidence manifest: `CHARACTER_VISUAL_REFERENCE_MANIFEST.json`

## Individualized summary

Cantarella's design is an elegant, perilous bloom. Long lavender hair and a white fitted dress dissolve into blue-violet petal layers, iridescent membranes, floral ornaments, and cool jewel tones, giving her a fluid silhouette that can read as flower, fin, or deep-sea creature.

## Evidence boundary

This first-pass profile is grounded in three decoded official-client UI textures: the large head icon, formation pile art, and activity portrait. Those images are authoritative as client-derived raw visual evidence for their own pixels, not as proof of unseen rear construction, exact physical materials, runtime animation, alternate skins/forms, or developer intent. The normalized role/profile record supplies semantic context but remains a separate authority layer.

Semantic role context is summarized only in the design–narrative claim below; the exact normalized source locator is retained in the JSON profile rather than reproducing the source text here.

## Structured observations

| Dimension | Observation | Basis | Confidence |
|---|---|---|---|
| silhouette | Very long hair, flared hip petals, detached sleeve structures, and a cascading fish-tail-like skirt create a soft but expansive silhouette with little hard geometry. | `direct_visual` | `high` |
| palette | White and pale lavender dominate, deepening through cobalt and violet into near-black, with cyan iridescence and small gold settings. | `direct_visual` | `high` |
| hair and face | Layered lavender hair frames narrowed pink-blue eyes; a dark luminous flower and white ruffled headpiece create an asymmetric crown. | `direct_visual` | `high` |
| costume construction | A fitted white dress is opened at the sides and layered with ruffles, translucent petal panels, a large blue hip bow, lace-edged hosiery, and white heeled boots. | `direct_visual` | `high` |
| materials | Opaque pale fabric, lace, polished jewelry, translucent fins/petals, and rainbow-reflective inserts create a deliberately unstable boundary between dress and organic form. | `direct_visual` | `medium` |
| motifs | Flowers, petals, droplets, fins, and softly curling tendrils recur throughout the hair, jewelry, sleeves, and hem. | `direct_visual` | `high` |
| weapon and role signaling | No held weapon is visible in the bounded UI art; the design signals controlled allure and potentially hazardous, dreamlike power rather than a specific weapon class. | `direct_visual` | `medium` |
| pose and body language | A tilted head, fingertips near the cheek and lips, and a contained smile read as intimate, self-possessed, and knowingly theatrical. | `direct_visual` | `high` |
| design narrative relationship | The beautiful but uncanny floral-aquatic construction supports the profile of a captivating and perilous noblewoman who spins illusory dreams, though flower-versus-sea readings are not mutually exclusive. | `direct_visual_and_semantic` | `medium` |

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
| head_icon | `RoleHeadIconLarge` | `decoded_exported` | `/Game/Aki/UI/UIResources/Common/Image/IconRoleHead256/T_IconRoleHead256_34_UI.T_IconRoleHead256_34_UI` | `restricted://_visual_media/character_visual_v0_2/client_textures/Aki/UI/UIResources/Common/Image/IconRoleHead256/T_IconRoleHead256_34_UI.png` |
| formation_pile_art | `FormationRoleCard` | `decoded_exported` | `/Game/Aki/UI/UIResources/Common/Image/IconRolePile/T_IconRole_Pile_kanteleila_UI.T_IconRole_Pile_kanteleila_UI` | `restricted://_visual_media/character_visual_v0_2/client_textures/Aki/UI/UIResources/Common/Image/IconRolePile/T_IconRole_Pile_kanteleila_UI.png` |
| activity_portrait | `RolePortrait` | `decoded_exported` | `/Game/Aki/UI/UIResources/Common/Image/PixActivity/T_ActivityRoleKanteleila.T_ActivityRoleKanteleila` | `restricted://_visual_media/character_visual_v0_2/client_textures/Aki/UI/UIResources/Common/Image/PixActivity/T_ActivityRoleKanteleila.png` |
| head_icon | `RoleHeadIconCircle` | `reference_only` | `/Game/Aki/UI/UIResources/Common/Image/IconRoleHeadCircle256/T_IconRoleHeadCircle256_34_UI.T_IconRoleHeadCircle256_34_UI` | `—` |
| head_icon | `RoleHeadIconBig` | `reference_only` | `/Game/Aki/UI/UIResources/Common/Image/IconRoleHead150/T_IconRoleHead150_34_UI.T_IconRoleHead150_34_UI` | `—` |
| head_icon | `Card` | `reference_only` | `/Game/Aki/UI/UIResources/Common/Image/IconRoleHead175/T_IconRoleHead175_34_UI.T_IconRoleHead175_34_UI` | `—` |
| head_icon | `RoleHeadIcon` | `reference_only` | `/Game/Aki/UI/UIResources/Common/Image/IconRoleHead80/T_IconRoleHead80_34_UI.T_IconRoleHead80_34_UI` | `—` |
| quest_stand | `RoleStand` | `ambiguous` | `/Game/Aki/UI/UIResources/UiQuest/Image/ChuanShuo/T_IconChuanShuo1_UI.T_IconChuanShuo1_UI` | `—` |
| spine_portrait | `FormationSpineAtlas` | `ambiguous` | `/Game/Aki/UI/UIResources/Common/Spine/Portraits/Portraits_Anke/Portraits_Anke.Portraits_Anke-atlas` | `—` |
| spine_portrait | `FormationSpineSkeletonData` | `ambiguous` | `/Game/Aki/UI/UIResources/Common/Spine/Portraits/Portraits_Anke/Portraits_Anke.Portraits_Anke-data` | `—` |
| performance_animation | `UiScenePerformanceABP` | `reference_only` | `/Game/Aki/Character/Role/FemaleXL/Kanteleila/R2T1KanteleilaMd10011/ABP_Performance_Kanteleila_PC.ABP_Performance_Kanteleila_PC_C` | `—` |

The exported PNGs remain local/restricted copyrighted evidence. The repository-facing profile and manifest carry hashes and provenance, not a grant to redistribute the artwork.
