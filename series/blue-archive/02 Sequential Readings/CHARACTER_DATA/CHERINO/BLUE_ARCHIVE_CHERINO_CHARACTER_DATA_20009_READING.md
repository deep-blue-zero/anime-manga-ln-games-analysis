---
series: BLUE_ARCHIVE
artifact_type: character_data_reading
scope: CHERINO_WRITTEN_DATA_VARIANT_20009
generation: V1
status: draft_noncurrent
source_story_ids:
  - "BA:character_data:20009:profile_and_dialog"
source_boundary: "Complete canonical Japanese source objects named in source_story_ids at BA_REFRESH_20260928T032248159554Z; source-facing contextualization proposed pending integrator admission; written text only"
source_generation: BA_REFRESH_20260928T032248159554Z
source_commit: a038020f1f5ac02dcfe76962426d38f86414cdd8
supersedes: []
superseded_by: []
do_not_use_as_current_authority: true
created: 2026-10-01
updated: 2026-10-02
source_admission: UNADMITTED
publication_review_state: COMPLETE_WITH_LIMITS
publication_snapshot: BA_PHASE2_REVIEW_DRAFTS_20261003
---

> Review draft — UNADMITTED. The reviewed argument is preserved with its authoring-stage descriptions; current review and publication status are routed through the draft snapshot manifest. Shared admission effects remain pending.


# Cherino — resort wishes, particular bathing contexts and private appearance concerns

Complete hot-spring profile and all 57 dialog/context records. Exact shared-name identity preserves the variant route and unknown age; quiet food, hospitality, fear and embarrassment remain material. The profile’s event summary and contextual milk repeats do not substitute for complete event readings or add historical episodes.

## 1. Complete source witness

Pinned source root is `blue-archive-corpus-pipeline/corpus/GENERATIONS/BA_REFRESH_20260928T032248159554Z`; upstream `electricgoat/ba-data@jp a038020f1f5ac02dcfe76962426d38f86414cdd8`, game `v1.73.459696-r96_3cpn8ebtdjiqi6y9qtn1`, parser `0.2.0`. Raw acquisition remains outside analytical Git. Each named canonical object, complete structured witness and consequential primary controls were inspected. Source-unit completion is contributor inspection; admission and shared reconciliation remain the parent integrator’s responsibility.

| Exact complete object | Generation-relative canonical path | Extent and canonical SHA-256 |
|---|---|---|
| `BA:character_data:20009:profile_and_dialog` | `02_CANONICAL_STORIES/CHARACTER_DATA/CHERINO/VARIANT_20009.md` | 1 profile records plus 57 written dialog/context records; `3139da1cfef77cea5dd18b62bbde7cee38e639208316af15a87313bd333ce8c3`. |

Raw table provenance, actual file SHA-256:

- `DB/CharacterDialogExcelTable.json`: `dbba21ca2bcdd856498e9eae0c3319309a829e3d0a4ee8d206e9366c28a24b20`.
- `DB/LocalizeCharProfileExcelTable.json`: `f7039fb2bbf78535d4f5aa926cc43a74ddece835d2bea7edc2e46c4bc57b6fe4`.

Canonical anchors preserve `utterance_id`, scene, mode and selection groups; `choices.jsonl` preserves every option and `branch_effect_known=false`; `momotalk_messages.jsonl` preserves complete message IDs, `Answer` alternatives, conditions and schedule links; written data preserve record IDs, categories, conditions, unlocks and source offsets. `DataList` locators are array offsets, not upstream `Id` values. Numeric source IDs, rank unlocks and documentary release are retrieval/provenance, not dates of acts against main chapters.

## 2. Full profile, fallback locator and all runtime records

Complete profile `BA:character_data:20009:profile` is `LocalizeCharProfileExcelTable.json:DataList[81]`. Exact `連河チェリノ`, third year, `??歳`, October 27 and 128cm match the base nominal family; this is positively routed `BA_VARIANT_20009`, not a second Cherino. Raw `Club=None`, gacha `レッドウィンター事務局` and registry RedwinterSecretary remain distinct fields.

The profile contextualizes enjoyment of `227号温泉郷`, a reported initial intention to remove an unauthorized spring, and a change through Nodoka and others' accommodation. It qualifies bathing aversion with `どうやら` / `様子` while distinguishing facility/food satisfaction. This compressed profile history is not a substitute for complete event text or admission of the referenced event. Nodoka gains a source-local profile mention, not a newly read private scene.

Weapon `チーストカ` is said to have been modified by Tomoe for hot, humid conditions, with `模様`. Preserve that qualified profile attribution; no observed engineering work, corrosion test, actual purge, weapon deployment or outcome audit follows. `粛清君1号` in the gacha introduction is a named object/authority address, not a newly joined person.

All **57** complete dialog/context records at `CharacterDialogExcelTable.json:DataList[3017–3073]` were inspected. Categories: one title, one acquisition, five cafe, 22 lobby, 20 lobby2, one weapon and seven special records. All use raw costume `2000901`; `UILobby2` is a contextual category, not another costume or dated later identity. There are 45 nonempty VoiceId arrays and 12 empty arrays. Production action/animation/duration/CV metadata and performer credit were read, not heard or played.

Actual record blocks, with abbreviations expanded to `BA:character_data:20009:<category>:<ID>`:

| Complete record block | Raw offsets / controls |
|---|---|
| `UITitle:2978` / `CharacterGet:2979` | `[3017–3018]`, favor rank 1 |
| `Cafe:2980–2984` | `[3019–3023]`, favor rank 15; `2983–2984` are `Think` |
| `UILobby:2985–3006` | `[3024–3045]`, segmented runtime utterances |
| `UILobby2:3007–3026` | `[3046–3065]`, repeats in actual alternate UI context |
| `WeaponGet:3027` | `[3066]`, favor rank 25 / `UnlockEquipWeapon=true` |
| `UILobbySpecial:3028,3029,line:000001,3031–3034` | `[3067–3073]`; preserve exact fallback `line:000001`, **do not invent `3030`** |

The fallback record `BA:character_data:20009:UILobbySpecial:line:000001` at `[3069]` prints `おいらの顔に何かついてるか？`, `DisplayOrder=530` / `GroupId=2` / `CVGroup_UILobbySpecial_Idle2` / empty VoiceId. It is present and complete, not a lost unit or unnamed human.

`UserBDay` rows are `[3037–3038]` / `[3057–3058]`; `StudentBDay` rows `[3039–3040]` / `[3059–3060]`. New Year uses January 1–3 at `[3041],[3061]`, Christmas December 24–25 at `[3042],[3062]`, and Halloween October 30–31 at `[3043–3045],[3063–3065]`. These are activation controls, not calendar dates of any narrative episode or one consecutive holiday itinerary.

## 3. Resort enjoyment includes particular food, clothes and embarrassment

Acquisition repeats cold resistance through office pride. Cafe text moves between sleepiness, a threat against idlers, a question about resort development and two private thoughts: that everyone is watching her dignity, and whether more medals would have helped (`CharacterGet2979;Cafe2980–2984`). The two `Think` records do not make other people actually admire her or hear these thoughts; the resort project question does not verify construction.

Lobby welcome invites a winter feast, while the other arrival calls lateness sabotage (`UILobby2985–2986`). Idle material desires springs like Gehenna's and briefly imagines acquiring that school (`2988–2990`). It is a thought/wish in contextual speech, not a completed annexation, inter-school diplomacy, visited Gehenna site or researched public standard.

She recalls enjoying old-school hot-spring buns (`2991`; repeated `UILobby2:3013`). That is affirmative remembered food pleasure, independently useful without proving every event meal. Asked about clothing, she calls wearing a school swimsuit under a yukata normal when bathing and labels the comrade unfamiliar with custom (`2992–2994`; repeated `3014–3016`). This is her own norm, not a verified universal Kivotos practice or instruction for real bathing.

Base lobby `2995–2996` asks whether a wet mustache must be removed; `2997` reports embarrassment at being stared at. Lobby2 repeats the embarrassment at `3017` but omits the removal segment in its actual record set. Do not fabricate absent repeated text or infer a later confidence stage from this category difference. These give a recipient's appearance/boundary context; they do not independently show Sensei staring, touching, complying or engaging in reciprocal romance.

## 4. Conditional hospitality, celebration and fear preserve different recipient contexts

User-birthday text says she has rented a spring for Sensei to rest and will enter too (`UILobby2998–2999;UILobby2:3018–3019`). As owned contextual hospitality this is material, but no rental record, payment, actually completed shared bath or independent consent is observed in this data object.

Student-birthday records call it another step toward adulthood and invite a grand celebration (`3000–3001;3020–3021`). They do not resolve `??歳` or authenticate maturity. New Year says the school's safety is assured if they stay together (`3002;3022`), a pledge/expectation rather than safety audit. Christmas asks whether Santa's beard is real (`3003;3023`), without proving an encounter.

Halloween begins with a reported frightening demon-like passerby, receives a costume interpretation and responds with a purge threat (`3004–3006;3024–3026`). The runtime dialogue supplies fear as a contrary context to invulnerability. It does not show a supernatural threat, diagnosis, completed purge or whole-school festival. The weapon line worries about retaining authority even at a resort and repeats mustache as the sign (`WeaponGet3027`); no new deployment is printed.

## 5. Milk special lines repeat a positively owned scene without multiplying it

Seven special records repeat the milk montage in [complete bond 20009 E006](../../BOND/CHERINO/BLUE_ARCHIVE_CHERINO_BOND_20009_E006_DEEP_READING.md):

- `3028` ↔ bond `u0031–u0032`; `3029` ↔ `u0033`; exact `line:000001` ↔ `u0034`.
- `3031` ↔ `u0035`; `3032` ↔ `u0036–u0037`.
- `3033` ↔ `u0038–u0039`; `3034` ↔ `u0040–u0041`.

That bond already has explicit `[log=체리노 온천ND]` ownership. Written data corroborate contextual wording; they are not a second historical consumption episode or extra proof of the final upset stomach. The delighted “new mustache” remains a character interpretation of residue, not hair growth or actual restored office authority.

## 6. Counterreading and observed written repertoire

The profile's general aversion to bathing is source-bounded and qualified. [E006](../../BOND/CHERINO/BLUE_ARCHIVE_CHERINO_BOND_20009_E006_DEEP_READING.md) and [E020](../../BOND/CHERINO/BLUE_ARCHIVE_CHERINO_BOND_20009_E020_DEEP_READING.md) provide particular reported/enjoyed baths, so neither “always likes bathing” nor “never enjoys it” holds across these inspected contexts. No release-based personality development is inferred.

The repertoire includes private appearance worry, named food pleasure, hospitality desire, contextual fear, embarrassment and office language. [GROUP1301–1303](../../GROUP/BLUE_ARCHIVE_GROUP_1301_1303_DEEP_READING.md) and [GROUP2801–2802](../../GROUP/BLUE_ARCHIVE_GROUP_2801_2802_DEEP_READING.md) preserve coercion and other students' needs; this private material remains affirmative evidence without exonerating them.

## 7. Proposed seven-ledger reconciliation

| Ledger / affected rows | Material proposal and limit |
|---|---|
| Character state — Cherino | Exact same-name identity/unknown age; private medal/appearance thoughts, remembered buns, embarrassment, hospitality and runtime fear. Profile characterization and conditional utterances are not completed scenes or a diagnosis. |
| Relationship state — Cherino→Sensei / Nodoka/Tomoe report contexts | Owned hospitality/rest invitation and appearance discomfort; profile reports accommodation and qualified modification. No independently observed response, event intervention, romance, rental or weapon engineering. |
| Institution — Red Winter / Class227 spring / Gehenna mentioned | Profile history and wishes provide scoped contexts. No event admission, verified authorization dispute, completed annexation, resort expansion, safety policy or purge. |
| Sensei ethics — C007/C008/C016/C017 | **No new direct teacher act/choice.** Recipient's invitations, requests and embarrassment are comparison conditions, not observed consent/compliance or general care. C005/C006 remain rejected. |
| Japanese voice / address | Owned `Think` records, office/fear/embarrassment registers, exact fallback `line:000001` and segmented/runtime repeats. Same-costume `UILobby2` and VoiceId/performer metadata retain their boundaries; no performance. |
| Motif / theme / callback | Desired spring/food, sign-mediated standing, gifts and conditional company; milk correspondence repeats an owned scene, no new historical episode or definite chronology. |
| Claim revision | QUALIFY fixed bathing preference, actual rental/annexation/weapon-modification result, age certainty, actual teacher stare and guaranteed institutional safety. C008 keeps profile/condition/claim grades; no durable new claim/model or C009/C012/C014/C015/C019 expansion. |

## 8. Proposed admission, coverage and debts

Propose **ADMIT_WITH_LIMITS** for this exact complete written-data ID pending acceptance. **CORE** value is justified by variant-specific desires, qualified profile context, private thoughts and independent boundary evidence. Repetition and quietness do not remove eligibility.

After acceptance, add one variant 20009 written-data object: one profile and 57 complete context records. No additional bond/event/group/MomoTalk/audio object is completed. G01 gains ordinary/private context; G09/G14 exact record, `Think` and activation boundaries. G07 chronology, G10 performance, G12 age/club/variant/role outcomes and G13 scientific/administrative verification remain open. **NO_DIAGNOSTIC_OPPORTUNITY** applies to this retrospective interpretation. Parent controls shared reconciliation and publication.
