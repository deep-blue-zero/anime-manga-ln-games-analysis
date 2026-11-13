---
title: "Kamakura Police Station — claim revision ledger"
series: "Kamakura Police Station: The Case Files of Asumi Ogasawara / 鎌倉署・小笠原亜澄の事件簿"
series_id: kamakura-sho
artifact_id: KSOA_CLAIM_REVISION_LEDGER
artifact_type: claim_revision_ledger
generation: KSOA-G1
version: "1.0"
created: "2026-11-12"
status: canonical
scope: "Cross-unit interpretation, contradictory evidence and recoverable claim versions."
source_boundary: "Japanese publisher EPUBs V01–V07. Bibliography, bytes and package structure reconciled. Narrative admission and inspection are pending."
canonical_home: series/kamakura-sho/KSOA_CLAIM_REVISION_LEDGER.md
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
do_not_use_as_literary_evidence: true
---

# Claim revision ledger

**Analytical rows at initialization: 0.** This is the canonical home for versioned, material interpretive propositions, including disputed readings of character, prose form, clue placement, institutional practice, setting and theme. Case hypothesis history lives in the [disclosure ledger](KSOA_DISCLOSURE_AND_HYPOTHESIS_LEDGER.md), and local observations keep their source homes.

| Record | Required fields |
|---|---|
| Original claim | Stable claim ID, first version, generation, originating artifact/anchor, exact proposition, scope/continuity, story time where material, evidence horizon, claim type, confidence, supporting evidence IDs, counterevidence or plausible alternatives and outstanding diagnostic question |
| Revision | Stable revision ID and predecessor claim/version, revision author/date, new evidence horizon, new supporting and conflicting evidence, reason/transition, revised proposition and confidence, current disposition, and affected downstream paths/anchors |
| Open conflict | Competing claim IDs and evidence, suspected conflict class and its basis, unresolved point, effect on synthesis, and a specific way to resolve or bound it |

Use `KSOA-Vnn-CL-NNNN` for a claim that begins in a volume and `KSOA-SER-CL-NNNN` for a synthesis-origin claim. Append `-RNN` for versioned revisions and use a stable heading or anchor for each version. Retain formulation and evidence horizon. Link to a successor explicitly and keep the current pointer recoverable from the revision sequence. Simultaneous competing interpretations retain distinct IDs and remain visible until adjudicated. Changing a current claim requires meaningful evidence, correction of provenance, or explicit reasoning about the scope of the earlier claim.

| Archive transition | Use |
|---|---|
| `PRESERVE` | The tested formulation and bounds still hold |
| `STRENGTHEN` | New evidence adds support within the stated scope |
| `REVISE` | Wording, scope, mechanism or causal account changes |
| `DOWNGRADE` | Support narrows or confidence falls |
| `REJECT` | The evidence defeats the recorded formulation |
| `OPEN` | A material issue remains underdetermined or disputed |

Attach exact locators through the evidence IDs in the [case ledger](KSOA_CASE_EVIDENCE_LEDGER.md) or owning reading. Anchor any Japanese wording to the native witness. Record what later evidence changes in the current interpretation while preserving the earlier freeze and what it was reasonable to infer then. Review dependent arguments when a load-bearing premise changes. If an immutable reading contains a defect, point to an attributable erratum or superseding artifact and preserve its historical contents. If correction is blocked, make the defect and its impact visible under the [repository correction route](../../governance/policies/CHANGE_INTEGRATION_CHECKLIST.md#analytical-corrections-and-procedural-conflicts).
