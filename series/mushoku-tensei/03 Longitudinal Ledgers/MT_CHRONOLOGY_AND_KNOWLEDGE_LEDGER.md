---
title: "Mushoku Tensei - Chronology and knowledge ledger"
artifact_id: MT_CHRONOLOGY_AND_KNOWLEDGE_LEDGER
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

# Chronology and knowledge ledger

## Responsibility

Owns story-event ordering and who knows, believes, suspects or misbelieves a proposition at a particular point. It preserves uncertain age and interval claims by witness/continuity.

## Record format

`chronology ID | event/observation | witness | anchor | inferred interval | age claims | certainty/conflicts; knowledge ID | proposition | holder | epistemic state | disclosure/concealment | story state | reader access | source basis | uncertainty`

Every future record needs a stable local ID, source/witness and volume boundary, a link to the canonical volume observation, claim class, and explicit uncertainty. No sample rows are treated as evidence.

## Update and ownership rule

Append anchored events and proposition changes; reconcile conflicts visibly. Never backfill a character’s earlier knowledge from a later disclosure or force an unsupported exact calendar. The analytical integrator synchronizes this ledger with each closed volume transaction; a reviewed no-material-update is recorded in the volume closure without padding this ledger.

## Initial state — 2026-09-25

`NOT_STARTED`: zero narrative observations and zero substantive records. V01 is only structurally inspected for source usability. No absent phenomenon or character trait is inferred from the empty ledger. First update requires a separately authorized V01 reading.

## V01 pilot candidate — 2026-09-25 (pending durable locator map)

The observations below are provisional and the LN high-water mark remains `null`; the hash-only locator map has not been durably placed in the evidence plane.

Witness `MT-LNJP-V01`; observation IDs resolve in the [V01 reading](../02%20Sequential%20Readings/MT_V01_DEEP_READING.md). Ages are reported anchors in this volume, not a formula for subjective or moral age. Exact elapsed months and calendar dates are not inferred beyond the text.

| Chronology ID | Story order and age/interval anchor | Evidence and certainty |
| --- | --- | --- |
| `MT-T-001` | First-life narrator reports age 34, years of isolation, an eviction after the parents' funeral, then the rescue attempt/death. | `001–002`, **character report** for biography and motive; accident as represented event. Other students' ultimate fate is not certified. |
| `MT-T-002` | Reborn infant discovers language and household over months; healing is observed before the vow to live seriously. | `003`, order explicit; the reincarnation mechanism and prior subjective continuity are unresolved. |
| `MT-T-003` | Roughly two years after rebirth he reads and practices; at age three the damaging indoor magic attempt triggers the hiring of Roxy. | `005–006`, explicit rounded anchor. Capacity increases over practice days, but the exact growth law is unknown. |
| `MT-T-004` | At age five he receives gifts, graduates after a roughly two-year teaching period, first crosses the village boundary and then becomes Sylphie's friend. | `007–010`, age and general order explicit; the exact birthdays of the other children are not given here. |
| `MT-T-005` | At age six he has taught Sylphie for about a year; the bathroom violation, apology, wary friendship, Zenith and Lilia pregnancies and births follow. | `011–014`; pregnancy/birth interval is narrated in compressed months, not converted into a date. |
| `MT-T-006` | At age seven he confronts a training plateau and asks about university; one month after a request for work, Paul sends him to Roa. | `015–016`; Paul's letter specifies five years apart, which is a planned interval, **not** a completed interval at V01 exit. |
| `MT-T-007` | The Zenith extra appears after the separation ending but recounts her youth, past marriage and domestic period before the departure. | `014`, publication/spine order differs from story time; do not read it as a later event after departure. |

| Knowledge ID / proposition | Holder and epistemic state at the V01 boundary | Basis / limit |
| --- | --- | --- |
| `MT-K-001` Prior-life memory and reincarnation | Rudeus has represented memories and infers rebirth; family, Roxy and Sylphie are not shown knowing their content. Reader has first-person access. | `001–003`; no omniscient mechanism or universal subjective-age rule. |
| `MT-K-002` Magic/manual capacity | The textbook asserts near-fixed initial mana; Rudeus observes his own changing endurance, offers multiple hypotheses; Sylphie later also improves. | `005,011`; observation narrows the manual's simple rule, not proof of unbounded capacities for all. |
| `MT-K-003` Rudeus's fear of crossing gate | Rudeus reports fear linked to past injury. Roxy believes he fears a horse; his parents do not receive a full explanation in V01. | `008`; his later gate test establishes local change only. |
| `MT-K-004` Sylphie's identity and wishes | Rudeus misclassifies Sylphie's sex until the boundary violation; she had communicated refusal. Later she asks for ordinary treatment and opposes his leaving. | `009,011–012,016`; his error about sex does not cancel her known refusal. Romance is his inference, not her declared future agreement. |
| `MT-K-005` Pregnancy and allegation | Paul admits likely paternity; Rudeus knowingly invents the coercion allegation; Zenith hears it, then Rudeus privately tells her it was a lie. Lilia's later focalized account attributes initiation of the recent encounter to herself while recalling earlier force. | `013–014`; participant reports are distinguished; the precise earlier conduct is not excused by later feelings. |
| `MT-K-006` Separation plan | Paul and Rolls discuss Sylphie's dependency; Rudeus learns the five-year terms only after waking in the carriage. Sylphie sees the removal and protests; her father's precise explanation is withheld. | `016`; adult prediction and future effect remain unverified. |
| `MT-K-007` Roxy's later progress | Rudeus and reader learn from her letter that she reports Shiron court work and water-king level after leaving. | `015`; no direct inspection of her offstage life or later LN. |

The age claims “34” and later self-characterization as mentally over 40 belong to Rudeus's own arithmetic and rhetoric (`001,006,013`); age at this volume's close is seven in his new life (`MT-T-006`). Physical development, remembered experience, social treatment and demonstrated judgment remain separate variables. Do not enter a sum as a world fact.
