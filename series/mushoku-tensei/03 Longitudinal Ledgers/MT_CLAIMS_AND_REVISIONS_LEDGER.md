---
title: "Mushoku Tensei - Claims and revisions ledger"
artifact_id: MT_CLAIMS_AND_REVISIONS_LEDGER
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
