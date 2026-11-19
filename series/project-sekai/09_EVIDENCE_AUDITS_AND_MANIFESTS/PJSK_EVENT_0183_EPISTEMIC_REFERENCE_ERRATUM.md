---
series: PJSK
artifact_type: analytical_erratum
scope: EVENT_0183_EPISTEMIC_LEDGER_REFERENCES
status: canonical
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
---

# EVENT_0183 epistemic ledger reference erratum

The [EVENT_0183 section of the epistemic state ledger](../04_LONGITUDINAL_LEDGERS/PJSK_EPISTEMIC_STATE_LEDGER.md#forward-event_0183--successful-cooperation-does-not-settle-private-history) drops the `EPI-` prefix from two existing Stage SEKAI owner IDs. Read those references as follows:

| Printed reference | Correct owner ID | Existing evidence route |
|---|---|---|
| `MMJ-STAGE-FLOWERS-E0130` | `EPI-MMJ-STAGE-FLOWERS-E0130` | [EVENT_0130 deep reading](../03_SEQUENTIAL_EVENT_READINGS/MMJ/PJSK_EVENT_0130_DEEP_READING.md), section 3 |
| `MMJ-STAGE-TREE-E0176` | `EPI-MMJ-STAGE-TREE-E0176` | [EVENT_0176 deep reading](../03_SEQUENTIAL_EVENT_READINGS/MMJ/PJSK_EVENT_0176_DEEP_READING.md), section 8 |

Both references still mean **preserve** the existing owners. This corrects the identifiers only: it changes no evidence, event disposition, or analytical conclusion and makes no new source-verification claim.

The [EVENT_0222 retrospective acceptance manifest](PJSK_RETROSPECTIVE_0222_ACCEPTANCE_MANIFEST.json) binds the ledger to SHA-256 `3e42bce1e6d999e187b5689087264133086e36e413487df355b4f5bf6bce150c` (640,395 bytes). The original ledger and manifest remain unchanged. The current corpus map adds only an inbound retrieval link to this erratum; its historical acceptance snapshot remains preserved at [receipt-producing commit `a7cdfefb`](https://github.com/deep-blue-zero/anime-manga-ln-games-analysis/tree/a7cdfefb4c6c740d80e7991c0c1a661244f95298/series/project-sekai). No historical checkpoint or analytical content is rewritten.
