---
title: "Mushoku Tensei - Character state and readiness ledger"
artifact_id: MT_CHARACTER_STATE_AND_READINESS_LEDGER
artifact_type: longitudinal_ledger
series: "Mushoku Tensei"
generation: "V1"
version: "1.2"
status: canonical
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
do_not_use_as_literary_evidence: true
created: "2026-09-25"
adoption_basis_commit: "a2a1ab9a5ecd0512a5ac460c1b79655af1bca0bd"
source_boundary: "Japanese LN V01–V02 observations; V01 published and audited, V02 analytical/evidence closure prepared with retained map; publication/audit separately tracked."
---

# Character state and readiness ledger

## Responsibility

Owns observed state changes, local character keys, evidence coverage and bounded model readiness by domain. It does not create global entity IDs or duplicate the operational reconstruction model.

## Record format

`state event ID | local key | source observation refs | prior state | observed change | change kind | new information versus disposition | persistent features | uncertainty; readiness: local key | state/source boundary | contexts | supported domains | missing contexts | counterexamples | validation | model path`

Every future record needs a stable local ID, source/witness and volume boundary, a link to the canonical volume observation, claim class, and explicit uncertainty. No sample rows are treated as evidence.

## Update and ownership rule

Append source-bearing state events; revise current readiness only when an evidence review warrants it, preserving the prior state and reasoning. Leave global IDs null until curation establishes them. The analytical integrator synchronizes this ledger with each closed volume transaction; a reviewed no-material-update is recorded in the volume closure without padding this ledger.

## Initial state — 2026-09-25

`NOT_STARTED`: zero narrative observations and zero substantive records. V01 is only structurally inspected for source usability. No absent phenomenon or character trait is inferred from the empty ledger. First update requires a separately authorized V01 reading.

## V01 accepted records — read 2026-09-25; closure prepared 2026-09-26 UTC

The owner approved the V01 reading after its synopsis revision. Its hash-only locator map is durably retained and byte-verified as recorded in the [source lock](../01%20Source%20Lock%20and%20Inventory/MT_SOURCE_LOCK_AND_INVENTORY.md). The records below are accepted within V01; their interpretations and uncertainties are unchanged. The [current map](../CURRENT_STATE_AND_CORPUS_MAP.md) distinguishes this local closure candidate from pending branch publication and exact-head audit. The bootstrap zero state above remains historical.

All events are bounded to `MT-LNJP-V01` and cite observations in the [accepted V01 reading](../02%20Sequential%20Readings/MT_V01_DEEP_READING.md). Local keys are **not** global character IDs. Each current assessment retains its stated V01 evidential limits; prior zero state above remains historical.

| State event ID / local key | Prior → observed change and kind | Basis / uncertainty |
| --- | --- | --- |
| `MT-S-001` / `Rudeus` | Reported isolation and fear → daily magic practice and ability; changed activity/skill, not demonstrated global ethical reform. | `001,003,005`; self-reported prior biography and short experimental series limit causal and population inference. |
| `MT-S-002` / `Rudeus` | Home/garden limit → accompanied trip, then voluntarily steps beyond gate; situational avoidance reduced. | `008`; no clinical diagnosis or proof that every social setting is now safe. |
| `MT-S-003` / `Rudeus` | Protector/teacher role → overrides Sylphie's refusal, recognizes wrong, apologizes, then later imagines shaping her future; conflicting boundary responses. | `009,011–012,015`; recognition and temporary restraint observed, durability untested. |
| `MT-S-004` / `Lilia` | Suspicion/aversion of infant → respect and extreme debt framing after family meeting; belief/relationship revision. | `004,013`; her own earlier employment history and self-blame matter. The proposed future service by Aisha is not Aisha's consent. |
| `MT-S-005` / `Roxy` | Teacher with limited local prospects → recognized village worker, departure for further practice, later reports higher rank and another teaching post. | `006–008,015`; letter is her report, not independently observed offstage experience. |
| `MT-S-006` / `Paul` | Headstrong teacher initially acts on accusation → apologizes and in a later case asks about Sylphie's refusal; partial parenting practice change. | `010–012`; later forced removal `016` is substantial contrary evidence to a generalized noncoercion rule. |
| `MT-S-007` / `Zenith` | Betrayal and contemplated departure → chooses Lilia's continued place and feeds Aisha; chosen care with unresolved religious tension. | `013–014`; her first-person extra supplies reasons but not a durable harmony guarantee. |
| `MT-S-008` / `Sylphie` | Isolated target → initiates friendship/learning, practices silent magic, asserts refusal, remains cautious, protests separation. | `009,011–012,016`; strong observable action, little direct interior narration. |
| `MT-S-009` / `Ghislaine` | New arrival as a sword expert → requests literacy/number instruction as part of exchange. | `016`; her self-account and full instructional practice are not yet present. |

### Current bounded readiness

| Local key | Supported domains through V01 | Missing contexts / standalone model decision |
| --- | --- | --- |
| `Rudeus` | Study/experimental response, failure management, selected family care, conflict rhetoric, fear at gate, some ethical self-correction. | No stable response model across independent contexts, sustained consent practice, employment, equal-power intimacy, or later consequences. **Standalone operational model deferred.** His claim to a numerical mental age is self-description only. |
| `Lilia` | Safety/pay decision, household labor, changed judgment of Rudeus, self-blame in crisis. | Thin access to life outside house and later motherhood. Model deferred. |
| `Roxy` | Adaptive pedagogy, paid work, treatment of error, chosen continued education. | Offstage new post is only letter report; broader relational contexts absent. Model deferred. |
| `Paul` | Sword teaching, mistaken discipline and apology, expressed dependence concern, coercive separation. | Competing motives and untested consequences prevent a general parenting rule. Model deferred. |
| `Zenith` | Faith, family boundary, practical healing/care, response to betrayal, chosen feeding of Aisha. | Extra is a first-person self-account; future stability and work outside house sparsely observed. Model deferred. |
| `Sylphie` | Independent learning request, repeated practice, refusal and avoidance, abandonment protest. | Her developing goals and peer world beyond Rudeus are not sufficiently accessible. Model deferred. |
| `Ghislaine`, `Norn`, `Aisha`, `Rolls` | Limited encounter or represented need/choice only. | No standalone reconstruction warranted; retain local keys without global enrollment. |

## V02 state events and current readiness — 2026-09-26 UTC

The preceding table is the preserved **V01** readiness snapshot, not the latest assessment. V02 source observations are in [the complete V02 reading](../02%20Sequential%20Readings/MT_V02_DEEP_READING.md#d-diagnostic-close-readings); numbers below resolve as `MT-E-LNJP-V02-NNN`. Input is audited V01 commit `eaf159559c6fc76ddd820178d7588545f08c351d`.

| State event / local key | Prior → represented change / kind | Evidence, persistent feature and limit |
| --- | --- | --- |
| `MT-S-010` / Rudeus | Prospective employee → practicing tutor, coordinator and language learner. COMPETENCE / CONTEXT_CHANGE. | `001–003,006–012`: preparation, adapting instruction, using others' expertise, social access; manipulation persists. No global maturation score. |
| `MT-S-011` / Rudeus | V01 uneven self-restraint → one gift-related restraint, later violation, recognition/apology, commitment framed as future reward. UNRESOLVED persistence. | `006,009,014`: recognition is real, transfer failed at least once; renewed promise has no subsequent comparable opportunity here. |
| `MT-S-012` / Eris | Resists younger tutor → chooses learning, develops distinct skills, initiates gifts and celebration, asserts boundaries. RELATIONSHIP / COMPETENCE_CHANGE. | `002–009,012,014`: voice and force persist; defensive blows distinguished from arbitrary aggression. No direct complete interior account. |
| `MT-S-013` / Ghislaine | V01 rank/request only → demonstrated protector, effective teacher and learner with ordinary thought and ambitions. REVEALED_NOT_NEW plus COMPETENCE_CHANGE. | `001,003,006–011`: patient study changes practical options; rank did not prevent fraud/hunger. Own biased judgments remain. |
| `MT-S-014` / Ghislaine | Household protective routine → displaced, disoriented combat and urgent search. CONTEXT_CHANGE. | `017,019`: survives initial displacement; berserk violence interrupts a generic controlled-protector rule. Eventual homecoming unestablished. |
| `MT-S-015` / Roxy | Distant reported teacher → authored guide, observed refusal/exit, then self-chosen search. REVEALED_NOT_NEW / KNOWLEDGE / CONTEXT_CHANGE. | `010,015,018`: independent goals, teaching doubt, revised assumptions about camp grief. Hope is not successful recovery. |
| `MT-S-016` / Hilda | Apparent hostility → protective embrace; Philip supplies an explanation in separation from sons. RELATIONSHIP_CHANGE / REVEALED_NOT_NEW. | `012–013`; behavior direct, motive/backstory mediated. Do not diagnose or equate marriage pressure with freely granted choice. |
| `MT-S-017` / Philip, Sauros | Kinship employers → differentiated political and affective roles. REVEALED_NOT_NEW. | `004–005,008,012–013`: gratitude, violence, succession strategy and care overlap; outcomes after disaster unknown. |
| `MT-S-018` / Paul, Norn, Zenith, Lilia, Aisha | Stable household at prior boundary → Paul reports Norn with him, others missing, organizes search. KNOWLEDGE / CONTEXT_CHANGE. | `018`; public message read by Roxy, not shown received by Rudy. No observation of all persons' current states. |
| `MT-S-019` / Vigo | Mercenary identifies acquired homeland as worth dying for → survives intervention and memorializes rescuer. CONTEXT / SELF-APPRAISAL_CHANGE. | `019`; independent extra narrative, no invented knowledge of Ghislaine's eventual fate. |

| Local key / domain | Current readiness through V02 | Counterevidence / validation debt / operational home |
| --- | --- | --- |
| Rudeus: ordinary study, tutoring, coordination | BOUNDED_PROVISIONAL; multiple tasks and relationships now represented. | Retrospective fit only; severe context change at ending. Sexual restraint, politics and post-disaster adaptation not DOMAIN_READY. No standalone model promoted; V02 K/L names the next calibration review. |
| Ghislaine: teaching/learning, protective household work | BOUNDED_PROVISIONAL; action, dialogue, interiority and ordinary preferences available. | Accurate advice coexists with biased appraisals; disorientation/indiscriminate combat limits transfer. No tested operational model. |
| Eris: task-specific learning and chosen reciprocity | BOUNDED_PROVISIONAL for observed household contexts. | Limited interior access; performance, consent, cooperation and dependence must remain separate. Novel situations INSUFFICIENT_EVIDENCE. |
| Roxy: instruction, workplace refusal, route deliberation | BOUNDED_PROVISIONAL. | Relationship idealization and fallible assumptions; no successful-search evidence or out-of-domain validation. |
| Hilda, Philip, Sauros, Paul | Supported local actions and reported constraints; broad reconstruction INSUFFICIENT_EVIDENCE. | Uneven focalization and missing aftermath. |
| Sylphie, Zenith, Lilia, Norn, Aisha | V01 readiness limits preserved; new availability/knowledge statuses only where sourced. | No current inner states inferred from absence, missing-person status or Rudy's recollection. |
| Orsted, Perugius, Gal, Kishirika, Arumanfi, Vigo and other new figures | Encounter-specific actions only. | No generic persona, prophecy or unshown future imported. Global IDs remain null; no registry enrollment. |
