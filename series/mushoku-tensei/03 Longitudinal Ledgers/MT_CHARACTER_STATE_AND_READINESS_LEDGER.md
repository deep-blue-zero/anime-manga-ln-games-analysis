---
title: "Mushoku Tensei - Character state and readiness ledger"
artifact_id: MT_CHARACTER_STATE_AND_READINESS_LEDGER
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
