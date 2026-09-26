---
title: "Mushoku Tensei - Normative framing ledger"
artifact_id: MT_NORMATIVE_FRAMING_LEDGER
artifact_type: longitudinal_ledger
series: "Mushoku Tensei"
generation: "V1"
version: "1.0"
status: canonical
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
do_not_use_as_literary_evidence: true
created: "2026-09-25"
adoption_basis_commit: "a2a1ab9a5ecd0512a5ac460c1b79655af1bca0bd"
source_boundary: "Bootstrap only; V01 not narratively inspected, no source observations admitted."
---

# Normative framing ledger

## Responsibility

Owns diagnostic non-graphic framing records and comparisons across conduct, affected-person access, consent, power, narrative tone, consequences, and later opportunities. It does not own a total morality score or infer creator intent from a scene alone.

## Record format

`normative event ID | observation refs | represented event | ages/uncertainty | knowledge/capacity | power/alternatives | consent/boundaries | focalizer/affected-person access | formal cues | consequences | strongest readings and counterreadings | scope/criterion | claim refs; comparison ID | related event IDs | matched issue | differences | change/continuity | limits`

Every future record needs a stable local ID, source/witness and volume boundary, a link to the canonical volume observation, claim class, and explicit uncertainty. No sample rows are treated as evidence.

## Update and ownership rule

Append diagnostic event records under MT_NORMATIVE_FRAMING_PROTOCOL; compare only warranted cases. Update shared proposition changes in the claims ledger, keeping normative events linked rather than duplicated. The analytical integrator synchronizes this ledger with each closed volume transaction; a reviewed no-material-update is recorded in the volume closure without padding this ledger.

## Initial state — 2026-09-25

`NOT_STARTED`: zero narrative observations and zero substantive records. V01 is only structurally inspected for source usability. No absent phenomenon or character trait is inferred from the empty ledger. First update requires a separately authorized V01 reading.

## V01 pilot candidate — 2026-09-25 (pending durable locator map)

The observations below are provisional and the LN high-water mark remains `null`; the hash-only locator map has not been durably placed in the evidence plane.

The source is `MT-LNJP-V01`; IDs link the [canonical reading](../02%20Sequential%20Readings/MT_V01_DEEP_READING.md). This ledger uses non-graphic descriptions. “Wrong” identifies an analyst **value judgment** under the named criterion, not an asserted universal audience response or author intention. Narrator, focal person, other-character response and implied pattern are separate.

| Event ID / evidence | Conditions, access, tone, consequence | Strongest reading / counterreading / bounded judgment |
| --- | --- | --- |
| `MT-N-001` `001–002` | An adult reports trauma, family neglect and sexualized fantasy; he makes a costly rescue after anticipating regret. Only his account of prior family/school is available. | Rescue warrants credit for the actual intervention; his own stated motive complicates pure-altruism rhetoric without invalidating aid. Suffering explains but does not absolve unrelated misconduct. |
| `MT-N-002` `004,008` | Infant with retained adult memories behaves in ways that Lilia experiences as sexually intrusive; Roxy's property is later stolen and disclosed as a farewell punch line. Lilia receives focalized aversion; Roxy's direct response to the original theft is limited, though her letter later mentions it. | Lilia's reaction supplies meaningful affected-person access. The cut from sincere gratitude to a theft gag can distance readers from his reverence, but also treats the violation lightly. Under a bodily/property-boundary criterion, gratitude does not authorize appropriation. No global endorsement conclusion. |
| `MT-N-003` `006–008` | Roxy and Rudeus each damage valued property/put others at risk through magic. Zenith corrects Roxy over her tree; Roxy repairs it; Rudeus's indoor damage leads to instruction rather than expulsion. Roxy's storm briefly harms the horse before healing. | Comic errors are accompanied by material consequences and repair; the scenes do not establish that high ability licenses careless practice. Rudeus's parental protection and a paid teacher's responsibility differ, so strict penalty symmetry is an inadequate test. |
| `MT-N-004` `009–010` | Bullying targeted at a child for ancestry/appearance; Rudeus intervenes, then Paul strikes him on an inaccurate account and apologizes after hearing him. Sylph's immediate fear and Paul's interior failure are visible. | V01 criticizes prejudicial targeting and unhearing discipline through action and corrective focalization. Rudeus's own “fight back” advice initially overlooks larger threats. The apology establishes local recognition, not guaranteed nonviolence. |
| `MT-N-005` `011–012` | Sylphie, approximately Rudeus's peer in bodily childhood, explicitly resists undressing; he overrides her, briefly pauses, then overrides again. She cries, remains wary of touch and asks for ordinary interaction; Paul names her refusal and instructs apology. The image at `text/part0019.html` emphasizes comic surprise. | **Value judgment:** the override is wrong under a clear-refusal/bodily-autonomy criterion, independent of his claimed aim to prevent cold or later shock at her sex. **Formal inference:** distress and continuing distance criticize the act, while the gender-reveal joke and quick reconciliation accommodate its comic treatment. She does not grant retroactive consent by remaining a friend. No explicit passage is reproduced. |
| `MT-N-006` `012,015` | He fantasizes about directing Sylphie's future affection after her abandonment fear, recognizes a disturbing implication and checks himself; no completed grooming plan is represented. Her independent preference is for normal treatment and presence, not future partnership terms. | Present self-interruption is evidence of awareness, not proof of lasting restraint. Her isolation increases asymmetry and makes promises of care consequential. **Working hypothesis:** romantic-game framing risks reducing her agency; later comparable decisions would test whether he respects her independent alternatives. |
| `MT-N-007` `013–014` | Paul's affair breaches Zenith's explicit exclusivity expectation. Lilia risks losing income and a safe home. Rudeus knowingly makes a false specific coercion accusation, then retracts it privately; Lilia reports recent initiative and earlier forced conduct. Zenith states her own fear and eventual choice to care for both infants. | Under a truthful, consent-sensitive deliberation criterion, inventing coercion is wrong even when the immediate protective aim is legitimate. The earlier forced act deserves separate scrutiny; Lilia's self-blame for the recent affair does not ratify it. Zenith's mercy has her own reasons and costs; “case solved” is an incomplete ethical closure. |
| `MT-N-008` `014–015` | Lilia, midwife, Zenith and Rudeus supply birth/infant care; Zenith feeds Aisha when Lilia is absent despite unresolved faith and hurt. Ordinary labor is shown, not merely a reward for the protagonist's intervention. | Particular chosen care can be affirmed without assuming the family hierarchy is freely negotiated or all future conflict settled. Aisha's future service is Lilia's plan, not the child's agreement. |
| `MT-N-009` `010,016` | Paul fears dependency and arranges employment/education; he strikes, binds and removes his seven-year-old son without hearing him, imposes five years without Sylphie contact, while she tries to stop it. His motive and reservations get a later viewpoint. | Concern about dependence is supported; necessity/proportionality of this force and absolute duration is **unresolved**. His earlier lesson about listening and apology creates a visible contradictory paternal practice, not automatic proof of either hypocrisy as stable essence or justified exceptionalism. Outcomes unavailable at V01. |

**Matched-case comparison `MT-NC-001`:** `MT-N-004` versus `MT-N-009` tests Paul's principle that the strong should listen and not use force casually; his first error is admitted, his later force is deliberated but still unconsented. Difference in purpose and duration matters; the shared asymmetry does too. **Comparison `MT-NC-002`:** `MT-N-005` versus `MT-N-006` separates completed physical override from subsequent fantasy and restraint, avoiding an invented equivalence. V01 supports scene/volume-level findings only. No percentage, morality score, reader effect or creator intention is claimed.
