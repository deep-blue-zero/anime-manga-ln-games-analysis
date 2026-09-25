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
