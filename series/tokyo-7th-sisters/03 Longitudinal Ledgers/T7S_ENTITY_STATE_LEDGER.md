---
title: "Tokyo 7th Sisters — Entity State Ledger"
artifact_id: T7S_ENTITY_STATE_LEDGER
artifact_type: entity_state_ledger
series: Tokyo 7th Sisters
generation: V1
version: "1.1"
status: canonical
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
do_not_use_as_literary_evidence: false
source_boundary: "c20260909-r484; through T7S_B0001 / episode 201000001 / primary pages 0–194 including both authored branches"
architecture_lifecycle: INITIAL
created: 2026-09-09
last_updated: 2026-09-09
---

# Tokyo 7th Sisters entity state ledger

Current route: [CURRENT_STATE_AND_CORPUS_MAP.md](../CURRENT_STATE_AND_CORPUS_MAP.md). Governing pair: [T7S_ANALYTICAL_METHOD.md](../00%20Frameworks%20and%20Methods/T7S_ANALYTICAL_METHOD.md) and [T7S_SYNTHESIS_ARCHITECTURE.md](../00%20Frameworks%20and%20Methods/T7S_SYNTHESIS_ARCHITECTURE.md). Source recovery: [T7S_EVIDENCE_SUBSTRATE_AND_LOCATOR_PROTOCOL.md](../00%20Frameworks%20and%20Methods/T7S_EVIDENCE_SUBSTRATE_AND_LOCATOR_PROTOCOL.md).

This ledger began as initialized schema rather than placeholder findings. `INIT-20260909` contained zero analytical records and no seeded fictional psychology, chronology, theme, or identity resolution; that historical fact is retained below. Current literary records begin only with the admitted B0001 horizon. Administrative authority metadata is not literary evidence.

Read the complete current ledger before editing; append stable history and patch current rows without changing unaffected bytes or IDs. Every non-administrative assertion requires an admitted witness/horizon, source locator and a reading/event/claim route. `UNKNOWN`, missing and explicit negative evidence are different. Stable IDs are never recycled. Retractions retain their old formulation and successor decision. Entry/current counts advance only after source verification and all linked responsibilities close together.

## Current state

`identity_routes = 3`; `character_states = 3`; `epistemic_states = 4`; `directional_relationship_states = 6`; `unit_states = 2`; `readiness_decisions = 0`. All routes and states are bounded to B0001. Machine identity resolution remains `unresolved` for every source line; none of the local subject routes below alters the corpus record or resolves Connie's concealed identity. There are no character monographs/models and no R0–R5 promotion.

## Typed record contract

All records have stable ID, record type, witness/horizon, native and analytical identity references, supported interval, establishing event/reading, exact locators, confidence, current formulation, transition history and unresolved obligations.

| Record type / ID prefix | Owned state |
| --- | --- |
| `IDENTITY_ROUTE` / `IDENTITY-0001` | Evidence-backed mapping between witness/master/native ID, literal alias and stable local subject; ambiguity, provenance and correction history |
| `CHARACTER_STATE` / `CHAR-0001` | Development, goals/values, agency, coping, habits, constraints/resources, professional and public/private/stage roles; each conditioned by horizon |
| `EPISTEMIC_STATE` / `KNOW-0001` | Proposition, knower, known/believed/misunderstood/unknown status, acquisition route/time, remembered history, reliability and uncertainty; reader knowledge separate |
| `RELATIONSHIP_STATE` / `REL-0001` | Ordered subject→recipient, reciprocal counterpart link, roles, expectations, trust/dependence, information asymmetry, obligations, rupture/repair |
| `UNIT_STATE` / `UNIT-0001` | Membership and roles by interval, coordination, leadership/authority, resources, shared identity, public image, internal tensions and inter-unit links |
| `READINESS` / `READY-0001` | Subject/model/monograph version and horizon; independently recorded reconstruction readiness, monograph maturity, capabilities, decision evidence, audit and transition history |

Evidence-backed local subject IDs use stable ASCII tokens selected after identity review, not guessed English names or resource hashes. Identity is separate from state, costume, era label or franchise witness. Group membership is time-indexed; publicity grouping is not automatically diegetic membership. Preserve literal `PLAYER`, compound speakers, role labels and unresolved names. A card's owner is not automatically a dialogue speaker.

## Readiness and capability schema

`reconstruction_readiness` uses only R0–R5 from the reconstruction protocol. `monograph_maturity` uses only `MONOGRAPH_NOT_READY`, `MONOGRAPH_READY_TEXTUAL`, `MONOGRAPH_MATURE` from the synthesis architecture. They are independent: neither advances the other, repository authority or the sequential gate. No readiness record is instantiated at bootstrap.

Every readiness decision requires `subject_id`, `witness_id`, `state_horizon`, `artifact_version`, the two separate readiness/maturity values, `capabilities`, `evidence_locators`, `counterexamples`, `review_refs`, `unresolved_obligations`, `decision_reason`, `decision_date`, `previous_decision_id`, and `transition_scope`. If no monograph is justified, use `MONOGRAPH_NOT_READY`; no arbitrary maturity score or second registry is created.

The capability fields are `textual_characterization`, `japanese_linguistic_voice`, `performed_voice`, `visual_identity`, `embodied_presentation`, `stage_identity`, `relationship_coverage`, `ordinary_life_coverage`, `chronology_coverage`. Each is an object with `scope`, `review_status`, `evidence_routes`, `limits`, `review_ref`. Status is `UNREVIEWED`, `PARTIAL`, `REVIEWED_WITH_BOUNDS`, `INSUFFICIENT_SOURCE`, or `NOT_APPLICABLE_WITH_REASON`. A capability score/sum cannot substitute for evidence. An available, unexamined visual/voice modality cannot be waived as non-applicable to monograph maturity.

The current monograph declaration must match its ledger decision and scope. At textual readiness mark its integrated multimodal identity responsibility `PENDING_MULTIMODAL_MATURITY`. Mature status requires both representative visual and actual listened-to voice review, integration, counterexamples and passing audit under the architecture. Broadening scope reopens affected checks while retaining the prior bounded decision.

## Current identity routes

Witness for every row is `T7S_GAME_OFFLINE_JA_R484`, alias `c20260909-r484`; current horizon is the end of T7S_B0001. The canonical source reconstruction is [T7S_B0001_DEEP_READING.md](../02%20Readings/T7S_B0001_DEEP_READING.md), and event routes are in the story ledger.

| ID / local subject | Literal source identity and bounded route | Confidence, evidence, and unresolved obligation |
| --- | --- | --- |
| `IDENTITY-0001` / `player-protagonist` | Literal label `PLAYER`; self-reference `僕`; Nanasta employee who is designated second manager. This route exists only to join B0001 states and does not assign a master-character ID. | High for document-local continuity; machine status `unresolved`. `EV-B0001-002`–`006`; `t7s://c20260909-r484/v1/script/scout_000_00_01.json__8df3fd723276f650?doc=primary&log=15#/Pages/15/TextArea/Dialogue` through `...&log=194#/Pages/194/TextArea/Dialogue`. Preserve literal label in citations. |
| `IDENTITY-0002` / `nanasta-first-manager` | Literal label `支配人`; self-identifies as the first manager of Three Seven/Nanasta. No personal name is supplied in the admitted source. | High for role-local continuity; machine status `unresolved`. `EV-B0001-002`–`006`; self-identification at `...&log=32#/Pages/32/TextArea/Dialogue` through `...&log=33#/Pages/33/TextArea/Dialogue`. Personal identity remains unknown. |
| `IDENTITY-0003` / `rokusaki-connie-presented` | Literal label `六咲コニー`; presented with reading `六咲（ろくさき）コニー` and repeats that introduction herself. This route records the presented name only. | High for the presented document-local identity; machine status `unresolved`. `EV-B0001-004`–`006`; `...&log=116#/Pages/116/TextArea/Dialogue` and `...&log=117#/Pages/117/TextArea/Dialogue`. **Do not equate this route with the interrupted `ナナサ…` clue.** |

The abbreviated `...` expands without substitution to `t7s://c20260909-r484/v1/script/scout_000_00_01.json__8df3fd723276f650?doc=primary`.

## Current character states

| ID / subject | Supported interval and current formulation | Evidence, limits, and transition |
| --- | --- | --- |
| `CHAR-0001` / `player-protagonist` | **B0001 entry:** devoted to Seven Sisters, employed at idle Nanasta, dreams of raising idols but believes an equivalent group cannot recur. **Exit:** second manager who has accepted a bounded attempt to build new Nanasta and scout girls. Uses `僕` and polite speech while directly challenging contradiction and irresponsibility; this is block-specific agency evidence, not a universal trait. | `EV-B0001-002`, `003`, `005`, `006`. The choice preserves two formulations—confident love or low confidence converted into effort—so neither becomes the sole canonical interior state. Pages 15–27, 68–93, 131–160, 183–194. |
| `CHAR-0002` / `nanasta-first-manager` | **B0001:** incumbent who reports the idol-cultural crisis, uses grandiose/performative rhetoric, unilaterally appoints a successor, arranges Connie's support, transfers the HoloCom, and departs for a self-described wandering trip. He is familiar enough with the Player for specific mutual criticism and shares undisclosed knowledge with Connie. | `EV-B0001-002`–`006`. His society-wide diagnosis and the HoloCom's special status are attributed claims, not automatically reliable world fact. Pages 28–93, 108–130, 161–178. |
| `CHAR-0003` / `rokusaki-connie-presented` | **B0001 entry/exit:** recently returned from abroad; self-styled `ジャーマネ`; presented by the first manager as capable and senior to the Player; becomes the Player's support. She supplies the present-oriented idol model, promises full help in one choice branch, and immediately pushes scouting. She deliberately controls disclosure about her past through register shifts, denial, intimidation, and redirection. | `EV-B0001-004`–`006`. “Excellent” and “industry senior” originate in the first manager's report; exact past and identity remain unresolved. Pages 94–160 and 180–194. Textual register evidence does not establish performed voice. |

## Current epistemic states

| ID | Knower / proposition / status | Acquisition, reliability, and asymmetry |
| --- | --- | --- |
| `KNOW-0001` | `player-protagonist` **knows** the first manager and Nanasta's local operational scarcity; **believes** Seven Sisters-like girls will not appear; then **recognizes** that fixation on Seven Sisters obscured the future. | Existing familiarity is explicit at pages 35–38 and in later criticism; scarcity at 42–49 and 55–56; initial belief at 26; self-correction at 149. The broader “idol culture is dead” proposition is heard from the first manager rather than independently established by the Player. |
| `KNOW-0002` | `player-protagonist` **does not know** Connie's exact past/identity. The Player experiences familiarity, nearly connects her presented name to `ナナサ…`, and then says the shock made an important thought disappear. | Pages 100–107 and 183–192. Preserve “suspected recognition interrupted,” not a resolved remembered identity and not proof of permanent forgetting. |
| `KNOW-0003` | `rokusaki-connie-presented` and `nanasta-first-manager` share **some information** about Connie that the Player lacks; Connie intentionally withholds it. The exact proposition is `UNKNOWN`. | His expectation of her arrival (108–110), two cut-off `ナナサ…` disclosures (113–126), her private `おっちゃん` familiarity (180), and later obstruction (185–193). This supports an information asymmetry, not an exact identity solution. |
| `KNOW-0004` | **Audience presentation differs from Player knowledge.** The blocking movie after the last-live footage visually previews multiple named girls and an ensemble before the office scene establishes no Nanasta idols. Nothing in B0001 establishes that the Player sees or knows this montage as in-world information. | Page 13 movie command and reviewed exact movie asset; `AV-0001`. Current status: `AUDIENCE_PRESENTATION_ONLY`; future character identities are not imported into B0001 state. |

## Current directional relationship states

Every pair is stored in both directions because role, obligation, trust, and knowledge are asymmetric.

| ID | Ordered relation at B0001 exit | Current state and evidence |
| --- | --- | --- |
| `REL-0001` | `player-protagonist → nanasta-first-manager` | Familiar employee/successor toward former incumbent: knows his patterns, contests his authority claims and irresponsibility, but accepts the inherited office and device. Reciprocal: `REL-0002`. Pages 35–38, 68–93, 163–179. |
| `REL-0002` | `nanasta-first-manager → player-protagonist` | Incumbent toward chosen successor: identifies the Player's love/dream, imposes the role, delegates Nanasta, provides support through Connie, and entrusts the HoloCom. Trust and burden coexist; consent was not obtained before appointment. Reciprocal: `REL-0001`. |
| `REL-0003` | `player-protagonist → rokusaki-connie-presented` | Formally senior by title but practically uncertain: initial distrust of her presentation shifts toward accepting her argument/support; suspicion about her past remains interrupted and unresolved. Reciprocal: `REL-0004`. Pages 94–107, 131–160, 183–193. |
| `REL-0004` | `rokusaki-connie-presented → player-protagonist` | Assigned right hand/support toward new manager in all paths: challenges defeatism, reframes the mission, and directs first action while controlling information about herself. In the low-confidence branch she additionally promises full assistance. Reciprocal: `REL-0003`. |
| `REL-0005` | `rokusaki-connie-presented → nanasta-first-manager` | Prior familiarity and operational confidence: criticizes his scouting, polices what he may reveal, calls him `おっちゃん` after departure, and promises to handle new Nanasta. Exact prior role is unknown. Reciprocal: `REL-0006`. |
| `REL-0006` | `nanasta-first-manager → rokusaki-connie-presented` | Expects her return, treats her as trusted support and industry senior, and knows information she forbids him to disclose. He yields to her intimidation without resolving their exact history. Reciprocal: `REL-0005`. |

## Current unit and institution states

| ID | Interval and current formulation | Membership/role limits and evidence |
| --- | --- | --- |
| `UNIT-0001` / Seven Sisters | Historical unit presented through last-live footage and the Player's recollection; reported dissolved two years before the 2034 office scene. It functions at B0001 as the Player's beloved but immobilizing standard and as the source of the episode's “begin from ending” proposition. | Literal names supplied in this block: 羽生田ミト, 御園尾マナ, 寿クルト, 若王子ルイ, 遊佐メモル, 七咲ニコル. This list records only what pages 16–22 enumerate and does not claim corpus-wide exhaustiveness or master-ID resolution. |
| `UNIT-0002` / Nanasta institution | **Entry:** first manager plus employee `PLAYER`, no affiliated idols, poor viewership/content. **Exit:** first manager departed; Player is second manager; Connie is support/manager; scouting mission active. “Nanasta Sisters” is a proposed future idol form/name, not a unit with established membership. | `EV-B0001-002`–`006`; `WORLD-0001`; pages 32–64, 74–86, 116–160, 178–194. No performer membership is admitted at this horizon. |

## Readiness and transition history

No `READINESS` row is created. One introductory episode supports bounded state records but is insufficient for an independent character reconstruction model or monograph, and performed voice has not been reviewed. `reconstruction_readiness` and `monograph_maturity` therefore remain uninstantiated rather than receiving a token score.

`INIT-20260909` establishes schemas and an explicit unknown initial state. `T7S_B0001-20260909` adds the three local identity routes, three character states, four epistemic states, six reconciled directional relationship states, and two unit/institution states above. Later knowledge must never become an earlier state's remembered history; future evidence may extend or revise these rows only with an explicit transition.

## Character discovery boundary

The local ledger routes analytical identity/state; it is not a parallel global character registry. Eligible reviewed monographs/models may later support discovery by the curation agent. That process alone writes the global character registry and generated index. No character-upsert file or repository-wide reconstruction score is created by this bootstrap.
