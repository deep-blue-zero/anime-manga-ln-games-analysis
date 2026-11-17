---
series: WUWA
character: Aemeath
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

# Aemeath — Visual Design and Appearance Profile

Status: `active_provisional`
Generation: `character_visual_v0_2`
Visual evidence manifest: `CHARACTER_VISUAL_REFERENCE_MANIFEST.json`

## Individualized summary

Aemeath is built around a buoyant, performance-ready silhouette: a very long pink high ponytail, bright white fitted costume, deep navy structural layers, and cyan light accents. Iridescent translucent panels and wing-like shapes make the outfit read as both stagewear and advanced optical technology.

## Evidence boundary

This first-pass profile is grounded in three decoded official-client UI textures: the large head icon, formation pile art, and activity portrait. Those images are authoritative as client-derived raw visual evidence for their own pixels, not as proof of unseen rear construction, exact physical materials, runtime animation, alternate skins/forms, or developer intent. The normalized role/profile record supplies semantic context but remains a separate authority layer.

Semantic role context is summarized only in the design–narrative claim below; the exact normalized source locator is retained in the JSON profile rather than reproducing the source text here.

## Structured observations

| Dimension | Observation | Basis | Confidence |
|---|---|---|---|
| silhouette | A long high ponytail and multiple trailing skirt, sash, and sleeve elements create a broad, airborne silhouette; the activity pose keeps the body on a light diagonal rather than a grounded vertical. | `direct_visual` | `high` |
| palette | Saturated pink hair dominates a white-and-navy base, with cyan emissive lines, small gold fittings, and rainbow-iridescent fabric as high-energy accents. | `direct_visual` | `high` |
| hair and face | Pink hair is gathered into an oversized high ponytail with loose curls; amber-gold eyes and a smiling, forward-facing expression keep the face warm and performative. | `direct_visual` | `high` |
| costume construction | The costume combines a fitted asymmetric white bodice, long detached sleeves, short layered skirt panels, thigh straps, and high-heeled boots; navy underlayers give the pale outer shapes a clear graphic frame. | `direct_visual` | `high` |
| materials | Rendered cues contrast matte white fabric, dark structured panels, polished gold hardware, cyan luminous bands, and translucent holographic-looking inserts. | `direct_visual` | `medium` |
| motifs | Wing/feather shapes, angular light traces, and prismatic surfaces repeat across the hair ornament, sleeves, hips, and trailing panels. | `direct_visual` | `high` |
| weapon and role signaling | No held weapon is visible in the three bounded UI images; their strongest signal is singer/performer energy rather than a specific combat discipline. | `direct_visual` | `medium` |
| pose and body language | Open hands, a lifted knee, and a smile give the static art a dance-like, welcoming sense of motion. | `direct_visual` | `high` |
| design narrative relationship | The stage-like pose, luminous accents, and starward/prismatic styling visually support the semantic profile of a former Synchronist who now persists as a singing digital ghost, but that relationship is interpretive rather than an explicit design note. | `direct_visual_and_semantic` | `medium` |

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
| head_icon | `RoleHeadIconLarge` | `decoded_exported` | `/Game/Aki/UI/UIResources/Common/Image/IconRoleHead256/T_IconRoleHead256_53_UI.T_IconRoleHead256_53_UI` | `restricted://_visual_media/character_visual_v0_2/client_textures/Aki/UI/UIResources/Common/Image/IconRoleHead256/T_IconRoleHead256_53_UI.png` |
| formation_pile_art | `FormationRoleCard` | `decoded_exported` | `/Game/Aki/UI/UIResources/Common/Image/IconRolePile/T_IconRole_Pile_Aimisi_UI.T_IconRole_Pile_Aimisi_UI` | `restricted://_visual_media/character_visual_v0_2/client_textures/Aki/UI/UIResources/Common/Image/IconRolePile/T_IconRole_Pile_Aimisi_UI.png` |
| activity_portrait | `RolePortrait` | `decoded_exported` | `/Game/Aki/UI/UIResources/Common/Image/PixActivity/T_ActivityRoleAimisi.T_ActivityRoleAimisi` | `restricted://_visual_media/character_visual_v0_2/client_textures/Aki/UI/UIResources/Common/Image/PixActivity/T_ActivityRoleAimisi.png` |
| head_icon | `RoleHeadIconCircle` | `reference_only` | `/Game/Aki/UI/UIResources/Common/Image/IconRoleHeadCircle256/T_IconRoleHeadCircle256_53_UI.T_IconRoleHeadCircle256_53_UI` | `—` |
| head_icon | `RoleHeadIconBig` | `reference_only` | `/Game/Aki/UI/UIResources/Common/Image/IconRoleHead150/T_IconRoleHead150_53_UI.T_IconRoleHead150_53_UI` | `—` |
| head_icon | `Card` | `reference_only` | `/Game/Aki/UI/UIResources/Common/Image/IconRoleHead175/T_IconRoleHead175_53_UI.T_IconRoleHead175_53_UI` | `—` |
| head_icon | `RoleHeadIcon` | `reference_only` | `/Game/Aki/UI/UIResources/Common/Image/IconRoleHead80/T_IconRoleHead80_53_UI.T_IconRoleHead80_53_UI` | `—` |
| quest_stand | `RoleStand` | `ambiguous` | `/Game/Aki/UI/UIResources/UiQuest/Image/ChuanShuo/T_IconChuanShuo1_UI.T_IconChuanShuo1_UI` | `—` |
| spine_portrait | `FormationSpineAtlas` | `ambiguous` | `/Game/Aki/UI/UIResources/Common/Spine/Portraits/Portraits_Anke/Portraits_Anke.Portraits_Anke-atlas` | `—` |
| spine_portrait | `FormationSpineSkeletonData` | `ambiguous` | `/Game/Aki/UI/UIResources/Common/Spine/Portraits/Portraits_Anke/Portraits_Anke.Portraits_Anke-data` | `—` |
| performance_animation | `UiScenePerformanceABP` | `reference_only` | `/Game/Aki/Character/Role/FemaleM/Aimisi/R2T1AimisiMd10011/ABP_Performance_Aimisi_PC.ABP_Performance_Aimisi_PC_C` | `—` |

The exported PNGs remain local/restricted copyrighted evidence. The repository-facing profile and manifest carry hashes and provenance, not a grant to redistribute the artwork.
