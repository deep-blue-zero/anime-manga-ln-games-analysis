---
title: "Kamakura Police Station — case evidence ledger"
series: "Kamakura Police Station: The Case Files of Asumi Ogasawara / 鎌倉署・小笠原亜澄の事件簿"
series_id: kamakura-sho
artifact_id: KSOA_CASE_EVIDENCE_LEDGER
artifact_type: case_evidence_ledger
generation: KSOA-G1
version: "1.0"
created: "2026-11-12"
status: canonical
scope: "Case-local fictional events, evidence, investigative actions and causal reconstruction."
source_boundary: "Japanese publisher EPUBs V01–V07. Bibliography, bytes and package structure reconciled. Narrative admission and inspection are pending."
canonical_home: series/kamakura-sho/KSOA_CASE_EVIDENCE_LEDGER.md
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
do_not_use_as_literary_evidence: true
---

# Case evidence ledger

**Analytical rows at initialization: 0.** Create a case key when the authorized text establishes a distinct investigative question. Multiple inquiries can coexist, change scope or cross volume boundaries. Reuse shared evidence by reference. Record actual literary significance and uncertainty when a field is inapplicable or unknown.

All rows carry generation, stable row ID, case ID, first available disclosure horizon, evidence locator or supporting evidence IDs, and the author's certainty or observed status. Use append-only revisions with predecessor IDs and their own horizons. Use `KSOA-Vnn-{kind}-NNNN` IDs, with Vnn keyed to first observation and a case row carrying its own ID as case ID. Retain the original ID if scope or interpretation changes. Use Markdown anchors with the same lowercased IDs for stable retrieval.

| Record and key | Required fields beyond the shared fields |
|---|---|
| Case `CASE` | Inciting incident as disclosed, investigative question, scope start/end, investigator or institution IDs, linked case IDs, open/closed boundary and source-supported remaining ambiguities |
| Event `EVT` | Participants and their roles at the time, location, earliest/latest or relative story time, asserted versus established status, dependencies, alternate chronology and source basis |
| Evidence `EV` | Object, observation, testimony or record type, exact witness locator, material statement or description, observer/speaker/focalizer, reported event/time, provenance and custody if shown, known reliability limits and competing accounts |
| Lead `LEAD` | Trigger and information source, investigator or proposed recipient, question or avenue opened, actions and evidence that test it, status changes, and any evidenced misdirection |
| Action `ACT` | Investigative sequence, investigator and unit, immediate goal, trigger or lead, claimed or portrayed authority, recipient, action taken, result and new evidence/transfer IDs, limits or omissions |
| Causal link `CAUSE` | Linked events, evidence for or against the relation, enabling means/opportunity/motive where established, competing causes, confidence and what would discriminate |
| Resolution `RES` | Assessment horizon, solution asserted by whom, reconstructed chronology and causal links, supporting and conflicting evidence, any rejected or live alternatives, independently unresolved questions and reveal IDs |

Record acquisition, access and transfer as separate facts. An artifact's discovery or a witness's account can establish an investigative action while leaving its significance contested. Use separate time fields for the event, elicitation, analyst-visible disclosure and any later authentication. If the narration supplies only a report of a chain of custody or a gap in it, retain the relevant attribution and uncertainty.

Keep retrospective case-resolution rows at their own horizon and link the [disclosure ledger](KSOA_DISCLOSURE_AND_HYPOTHESIS_LEDGER.md) for hypothesis history and reveal mechanics. For an earlier query, retrieve only versions whose required evidence and disclosure precede the cutoff. The endpoint reconstruction may cite later clarification if its horizon is explicit. Use the [witness locator](KSOA_SOURCE_AND_WITNESS_MAP.md#witness-bound-locator) and the [evidence rules](KSOA_ANALYTICAL_METHOD.md#assess-evidence-and-hypotheses). Claims about the form or meaning of a case use the [claim revision ledger](KSOA_CLAIM_REVISION_LEDGER.md).
