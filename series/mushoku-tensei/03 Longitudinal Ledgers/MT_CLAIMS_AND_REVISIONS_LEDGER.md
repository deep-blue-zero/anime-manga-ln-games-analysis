---
title: "Mushoku Tensei - Claims and revisions ledger"
artifact_id: MT_CLAIMS_AND_REVISIONS_LEDGER
artifact_type: longitudinal_ledger
series: "Mushoku Tensei"
generation: "V1"
version: "1.1"
status: canonical
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
do_not_use_as_literary_evidence: true
created: "2026-09-25"
adoption_basis_commit: "a2a1ab9a5ecd0512a5ac460c1b79655af1bca0bd"
source_boundary: "Accepted Japanese LN V01 observations only; locator map retained and byte-verified; local closure publication pending; no V02 evidence."
---

# Claims and revisions ledger

## Responsibility

Owns load-bearing analytical propositions, alternatives, prospective tests, and dated revision history. A volume reading owns its underlying observations; this ledger links them and records change of assessment.

## Record format

`claim ID | formulation | witness/range | class | support | counterevidence | alternatives | confidence basis | current assessment | revision events | affected homes`

Every future record needs a stable local ID, source/witness and volume boundary, a link to the canonical volume observation, claim class, and explicit uncertainty. No sample rows are treated as evidence.

## Update and ownership rule

Append revisions with prior and new formulation, evidence, input boundary, and dependent homes. Never overwrite a historical freeze. A test needs an opportunity and a disconfirming observation; absent opportunity means UNTESTED. The analytical integrator synchronizes this ledger with each closed volume transaction; a reviewed no-material-update is recorded in the volume closure without padding this ledger.

## Initial state — 2026-09-25

`NOT_STARTED`: zero narrative observations and zero substantive records. V01 is only structurally inspected for source usability. No absent phenomenon or character trait is inferred from the empty ledger. First update requires a separately authorized V01 reading.

## V01 accepted records — read 2026-09-25; closure prepared 2026-09-26 UTC

The owner approved the V01 reading after its synopsis revision. Its hash-only locator map is durably retained and byte-verified as recorded in the [source lock](../01%20Source%20Lock%20and%20Inventory/MT_SOURCE_LOCK_AND_INVENTORY.md). The records below are accepted within V01; their interpretations and uncertainties are unchanged. The [current map](../CURRENT_STATE_AND_CORPUS_MAP.md) distinguishes this local closure candidate from pending branch publication and exact-head audit. The bootstrap zero state above remains historical.

The historical initial state above is preserved. Current scope is **MT-LNJP-V01 only**, the [accepted V01 reading](../02%20Sequential%20Readings/MT_V01_DEEP_READING.md), observations `MT-E-LNJP-V01-001`–`016`. No V02 or later witness contributes. These are new bounded formulations, not revisions of nonexistent pre-V01 claims. Confidence concerns the stated V01 scope, not the series. `OPEN` means insufficient discriminating evidence, not a prediction of later outcomes.

| Claim ID | Current V01 formulation / class | Support; significant contrary or limiting evidence | Assessment and next test |
| --- | --- | --- | --- |
| `MT-C-001` | Rudeus's learning progress is produced through repeated experiment **and** material/relational support, not solely innate genius. `STRONG_INFERENCE` | `005–008,015`: books, parental reading, paid tutor, village practice, correction after failed trials. His unusual early silent casting is real, but its population-wide cause is not determined. | `OPEN` to developmental and individual alternatives; do not infer unlimited mana growth from a few trials. Reassess with separately verified later instruction/constraints. |
| `MT-C-002` | Ability and movement improve while consent-sensitive restraint remains uneven in V01. `STRONG_INFERENCE` | `005,008,011–013,016`: gate crossing and care; violation of Sylphie's refusal, theft, manipulation, possessive fantasy. He apologizes and temporarily self-interrupts, so “no recognition at all” is false. | Preserve dimensional formulation; comparable later refusals and costly restraint would discriminate durable change. No whole-series trajectory declared. |
| `MT-C-003` | V01's other focalizers materially qualify Rudeus's self-account. `STRONG_INFERENCE` | `004,010,013,014,016`: Lilia's fear and work, Paul's defensive motive and error, Lilia's self-blame, Zenith's independent reason for care. These viewpoints can themselves rationalize and are not omniscient. | Preserve as a formal claim; compare later viewpoints without flattening disagreement. |
| `MT-C-004` | The Sylphie boundary scene combines a clear refusal and persistent distress with a comic reveal frame. `STRONG_INFERENCE` | `011` and image `text/part0019.html`: explicit protest, further override, apology and later avoidance; comedic surprise and Paul's partial normalization. Later play does not settle the injury. | V01 conclusion is mixed, with a definite wrongful override under the stated consent criterion; reception/creator intent unavailable. |
| `MT-C-005` | The family meeting achieves immediate protection by a knowingly fabricated allegation and Zenith's choice; its means and consequence remain ethically distinct. `STRONG_INFERENCE` | `013–014`: risk of departure, Rudeus's lie and subsequent disclosure, Lilia's distinct past assault and recent invitation, Zenith's extra on what changed her mind. No external verification of all backstory. | A local protective outcome cannot certify a general truthfulness or victim-centered rule; examine later consequences only if authorized. |
| `MT-C-006` | Paul's stated concern about dependency has evidence, but V01 does not validate his forced five-year separation as necessary or effective. `STRONG_INFERENCE` for concern and coercion; `UNRESOLVED` for outcome | `012,015–016`: Sylphie's pleas, Rudeus's possessive fantasy, Paul's ambush/no-contact order and doubt. Sylphie's own future opportunity is not observed. | Keep justification and outcome separate; no V02 inference. |
| `MT-C-007` | Roxy, Lilia, Zenith and Sylphie each have choices, labor and/or constraints not reducible to Rudeus's improvement. `STRONG_INFERENCE` | `004,006–009,011–016`: employment, self-education, domestic care, refusal and protest. Access remains uneven, especially Sylphie's interiority. | Preserve plurality without inventing offstage agency. |

**Revision register:** V01 was the first narrative unit, so earlier analytical claims were absent. During V01, provisional character reports were corrected rather than promoted: Lilia's aversion is not simply dislike of children (`004`); the supposed fabricated injury of the bullying child is withdrawn after later information (`010`); a manual's fixed-capacity assertion is contradicted by Rudeus's observed short-term trials without establishing a universal replacement rule (`005`). Future material revises these IDs with a dated prior formulation and dependent-home review; the V01 entering freeze remains intact.
