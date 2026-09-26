---
title: "Mushoku Tensei - Relationship and agency ledger"
artifact_id: MT_RELATIONSHIP_AND_AGENCY_LEDGER
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

# Relationship and agency ledger

## Responsibility

Owns directional relationships, independent goals, initiative, refusal, constraints, trust, obligation, dependency, power and repair. Neither reciprocal feeling nor romance is presumed.

## Record format

`relationship event ID | A | B/group | direction | observation refs | goals | knowledge | choices/constraints | initiative/refusal/repair | prior state/change | reciprocity evidence | uncertainty`

Every future record needs a stable local ID, source/witness and volume boundary, a link to the canonical volume observation, claim class, and explicit uncertainty. No sample rows are treated as evidence.

## Update and ownership rule

Record A-to-B and B-to-A separately when supported. Append events and update current states with links; preserve prior directional history and distinguish choice from pressure. The analytical integrator synchronizes this ledger with each closed volume transaction; a reviewed no-material-update is recorded in the volume closure without padding this ledger.

## Initial state — 2026-09-25

`NOT_STARTED`: zero narrative observations and zero substantive records. V01 is only structurally inspected for source usability. No absent phenomenon or character trait is inferred from the empty ledger. First update requires a separately authorized V01 reading.

## V01 accepted records — read 2026-09-25; closure prepared 2026-09-26 UTC

The owner approved the V01 reading after its synopsis revision. Its hash-only locator map is durably retained and byte-verified as recorded in the [source lock](../01%20Source%20Lock%20and%20Inventory/MT_SOURCE_LOCK_AND_INVENTORY.md). The records below are accepted within V01; their interpretations and uncertainties are unchanged. The [current map](../CURRENT_STATE_AND_CORPUS_MAP.md) distinguishes this local closure candidate from pending branch publication and exact-head audit. The bootstrap zero state above remains historical.

`MT-LNJP-V01` only. Observation numbers below resolve in the [V01 reading](../02%20Sequential%20Readings/MT_V01_DEEP_READING.md). These are directional relations, not reciprocal labels or global registry entries.

| Event ID / direction | Initiative, goal, constraints, and change | Basis / uncertainty |
| --- | --- | --- |
| `MT-R-001` `Roxy → Rudeus` | Accepts paid teaching, adapts instruction, accompanies him outside and offers a limited protective keepsake; leaves for her own advancement. | `006–008,015`; she does not claim to know his trauma or promise indefinite availability. |
| `MT-R-002` `Rudeus → Roxy` | Learns and respects her; also objectifies and steals intimate property. Gratitude and boundary violation coexist. | `006–008,015`; her later letter notices theft, but does not establish prior consent. |
| `MT-R-003` `Rudeus → Sylphie` | Intervenes in bullying and shares literacy/magic, then overrides refusal, tries to manage her response and imagines shaping her future; both care and control are observed. | `009,011–012,015–016`; his romance reading is not her reported goal. |
| `MT-R-004` `Sylphie → Rudeus` | Seeks friendship and instruction, refuses physical exposure, resumes some shared activity while retaining distance, voices desire for ordinary treatment, opposes separation. | `009,011–012,016`; no direct adult preference or consent to future partnership is established. |
| `MT-R-005` `Paul → Rudeus` | Provides training, errs and apologizes after a one-sided accusation; later forcibly arranges paid tutoring and a five-year no-contact term to break perceived dependency. | `006,010,012,016`; good intentions and job benefit do not equal advance consent. |
| `MT-R-006` `Rudeus → Paul` | Seeks approval and instruction, challenges unfair punishment, admires sword competence but criticizes sexual/family conduct; accepts some reasoning only after removal. | `006,010,015–016`; partial post hoc understanding is not agreement to the method. |
| `MT-R-007` `Lilia → household` | Chooses rural employment for pay/safety, supplies professional/daily care, reports her pregnancy and offers to leave, later commits to continued service. | `004,013–014`; employer power, limited money and earlier harm constrain available choices. |
| `MT-R-008` `Zenith → Lilia/Aisha` | Anger and threatened rupture coexist with concern for travel/child; permits Lilia to stay and chooses to feed Aisha when needed. | `013–014`; her faith-related conflict remains explicit. |
| `MT-R-009` `Lilia → Zenith/Rudeus` | Feels she betrayed Zenith, credits Rudeus with protecting her and resolves to bind the unborn child to his service. | `013`; her debt narrative is her own appraisal, not a fair contract on Aisha's behalf. |
| `MT-R-010` `Rudeus → Lilia/Zenith` | Values Lilia's understated care and fears her dangerous departure; fabricates a coercion claim to influence Zenith and later admits the fabrication to her. | `013–014`; need to distinguish care for them from taking control of their information. |
| `MT-R-011` `Rolls/Paul → Sylphie` | Rolls discusses her isolation with Paul; Paul chooses separation to expand her independence; at departure Rolls speaks to her, exact counsel not reported. | `009,016`; Sylphie's protest and her own alternatives are not fully represented. |
| `MT-R-012` `Ghislaine ↔ Rudeus` | Proposed reciprocal instruction: sword teaching for reading and arithmetic; at the V01 ending only the arrangement and her request are known. | `016`; neither party's later teaching is observed. |

**V01 directional limit:** The house calls Lilia “family” while her wage and servant history persist; the word does not erase employment dependency. Sylphie's closeness is not evidence of unrestricted access to her body or her future. The five-year separation is Paul's decision, with its effectiveness and consent unresolved. Later evidence must be linked as new events rather than silently converted into current V01 motives.

## V02 directed events — 2026-09-26 UTC

The V01 events remain historical. New evidence numbers below refer to [V02 canonical observations](../02%20Sequential%20Readings/MT_V02_DEEP_READING.md#d-diagnostic-close-readings), prefix `MT-E-LNJP-V02-`. Current scope V01–V02; input audited commit `eaf159559c6fc76ddd820178d7588545f08c351d`.

| Event / direction | Initiative, constraints and changed options | Evidence / reciprocity and limit |
| --- | --- | --- |
| `MT-R-013` Rudeus → Eris | Engineers fear to obtain employment/cooperation, rescues and teaches, later coordinates rest and adaptive practice. | `001–008`; helpful outcomes do not prove the staged scheme necessary. Financial/class asymmetry is complex: pupil's household employs him, he controls practical knowledge. |
| `MT-R-014` Eris → Rudeus | Rejects teacher, later grants familiar address, returns to practice, wants to give a book, initiates birthdays and staff gift. | `004,007–009,012`; choices establish reciprocity beyond obedience, not unrestricted physical permission. |
| `MT-R-015` Rudeus → Eris | Particular restraint while she cherishes gifts; later exceeds limited permission, recognizes disregard and apologizes. | `009,014`; regained hope becomes entitlement to a future prize in his account. No demonstrated transfer of new vow yet. |
| `MT-R-016` Eris → Rudeus | Stops a violation, leaves, returns to forgive on this occasion and sets a five-year limit. | `014`; no irrevocable contract over future intimacy; her return does not ratify the violation. |
| `MT-R-017` Ghislaine → Rudeus | Protects life, cautions against overconfidence, adapts sword instruction and considers another teacher conditional on his wishes. | `003,006–007,011,017`; gratitude and fallible appraisal both present. |
| `MT-R-018` Rudeus → Ghislaine | Patient literacy/magic instruction, formal learner recognition, food reserved while she works; also sexualizes her and exploits her distraction role. | `006–012`; her artistic wish to record herself differs from his intention. Respect is not complete mutual understanding. |
| `MT-R-019` Ghislaine → Eris | Longstanding teaching/protection, personal ring, later urgent search. | `006–009,011,017,019`; duty persists on holiday; disorientation produces harmful force beyond controlled rescue. |
| `MT-R-020` Eris → Ghislaine | Admires expertise, listens to experience, treasures ring, seeks additional practice. | `006–009,011`; relationship predates Rudy and retains independent significance. |
| `MT-R-021` Roxy → Rudeus | Creates substantial guide, maintains correspondence, independently chooses search for him. | `010,015,018`; he is a respected pupil, not her declared lover. Idealization can obscure his limits. |
| `MT-R-022` Rudeus → Roxy | Gratitude and study depend on her labor; likeness made and sold without demonstrated permission disturbs her on arrival. | `010`; narrator's comedy does not settle her experience. |
| `MT-R-023` Philip/Sauros/Hilda → Rudeus/Eris | Resources, belonging and gratitude coexist with violence, gendered performance and proposed marital/political recruitment. | `004–005,008,012–013`; Hilda's grief is Philip-reported, her embrace observed. Affection need not be fictitious for constraints to be real. |
| `MT-R-024` Roxy → prince/court | Refuses coercion, uses contract/relative status, leaves at term end and repels attack. | `015`; court's judgment protects its interests as recorded; no broad equality guarantee. |
| `MT-R-025` Paul → scattered family/Rudeus | Protects Norn per message, requests assistance, prioritizes missing wives/Aisha and assigns Rudy a northern search. | `018`; Rudy not shown reading message. Trust and delegated burden coexist; necessity remains untested. |
| `MT-R-026` Ghislaine → Vigo / Vigo → Ghislaine | Her search-driven intervention enables his survival; he recognizes a protective purpose, accompanies her and later memorializes her. | `019`; their immediate directions partly coincide, their goals and later knowledge differ. Cult does not establish her endorsement. |

**Reviewed limits:** no new direct Sylphie→Rudeus event; his recollection is not her choice. No missing-person listing proves death. Relationship states after displacement are not simply household states moved intact to a new place.
