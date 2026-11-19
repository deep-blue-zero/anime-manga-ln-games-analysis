---
title: "Re:Creators — Evidence and Claim Ledger"
artifact_id: RC_EVIDENCE_AND_CLAIM_LEDGER
artifact_type: evidence_claim_and_forecast_ledger
series: re-creators
version: "1.0"
status: canonical
authority_generation: RC-INITIAL
authority_scope: "Source observations, testable interpretations, forecasts and preserved review history"
source_boundary: "NONE admitted; foundation metadata only"
created: 2026-11-18
last_updated: 2026-11-18
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
do_not_use_as_literary_evidence: true
---

# Re:Creators — Evidence and Claim Ledger

## Current state

Admitted source boundary is **NONE**. There are no narrative evidence records, interpretive claims, forecasts, audiovisual findings or review transitions. Inventory hashes belong in the [source register](RC_SOURCE_REGISTER.md) and do not count as narrative inspection.

This combined ledger owns observations and the history of conclusions drawn from them. [Character and world state](RC_CHARACTER_AND_WORLD_LEDGER.md) links to these records. Future episode readings retain their full arguments, and unit checkpoints preserve independent contributions and semantic acceptance.

## Evidence contract

Assign immutable identities `RC-EV-####` and record the source ID, edition, episode, relevant component, exact start/end interval, clock identity, cue/frame anchors where available, evidence lane, inspected object/derivative ID and source hash relationship. Record observer role, actual access, inspection date, effective visual sampling/temporal precision, re-view status and calibration residual. A precision limit cannot be repaired by printing more timestamp digits.

Separate the observed image/sound/event from transcription, translation, speaker testimony and analytical interpretation. Use the continuous-AV method's evidence classes, including `TXT` for primary-language text, `FRM` for sampled-frame evidence, `AM` for deterministic measurement, `AO`/`CAV` for model auditory/continuous audiovisual observation, `HL` for human listening/viewing and `INF`/`INT` for inference/interpretation. A listening transcription remains auditory or human observation, never `TXT`. An observer's report is `REPORTED` until the reconciliation protocol's full conditions justify `ANCHORED`.

Every load-bearing observation must be recoverable in the private source environment through public-safe stable identities and calibrated locators. Do not publish private absolute paths, credentials, Drive IDs, raw media or transcript dumps. Preserve enough analytical description to explain the inference without copying restricted raw evidence into Git.

## Claim contract

Assign `RC-CL-####`. Record a bounded formulation, admitted horizon, responsible episode/section, evidence IDs, provenance lane, reasoning chain, principal rival explanations, strongest counterexample, confidence/limitations and downstream state or synthesis dependencies. A character's assertion is evidence of an assertion unless independently corroborated.

New claims start as proposed. On review, retain the prior formulation and use the governing transition vocabulary `PRESERVE`, `STRENGTHEN`, `REVISE`, `DOWNGRADE`, `REJECT` or `OPEN`. Each transition names source observations, reviewer objection or new evidence, reasoning, resulting bounded formulation and affected artifacts. Record PRESERVE outcomes as well as corrections. A REJECT disposition concerns a specified formulation, not the erasure of evidence.

Maintain competing explanations where evidence cannot discriminate. A later source may revise a current claim without making the earlier bounded reading erroneous. Distinguish a demonstrated mistake within the old boundary from a legitimate update after new disclosure. Frozen-artifact corrections follow the archive policy.

## Forecast and prospective-horizon contract

Assign `RC-FC-####`. Before the next unit is inspected, freeze the current admitted boundary, available evidence, hypothesis, expected diagnostic observation, plausible alternatives and uncertainty. Record the exact freeze artifact/version in the unit transaction. Never reconstruct a supposedly prospective forecast after seeing its outcome.

Adjudication records the newly admitted evidence, whether it supports, pressures, defeats or leaves the forecast undecided, and what changes in the underlying claim. Preserve the original formulation and its rationale. Forecast quality is assessed through discriminating evidence and honest uncertainty, not retrospective success counts.

## Audiovisual findings and review contract

Use evidence IDs for interval observations and claim IDs for their interpretation. New independent findings record source, interval, channel, observation, proposed relevance and disposition. A formal recurrence or motif is a claim supported by individually located occurrences, relevant contrasts and unresolved alternatives.

The unit checkpoint stores an observation freeze and the actual exposure record for each contributor, including prior narrative familiarity. It preserves the full material specialist findings, principal response, critical-review objections, source checks and integrator dispositions. Condensed public records must retain every analytically distinct material finding, supporting evidence, rival explanation and unresolved disagreement. A statement that the agents agreed is not a substitute.

Track required versus optional evidence-channel completion, clock confidence, sampling limitations and unresolved load-bearing disputes. Required unresolved items block their dependent acceptance. An optional unresolved detail remains explicitly provisional and cannot support a firm conclusion.

## Independent audit and propagation

Reviewers inspect decisive sources directly and test unsupported conclusions, omitted significant observations, false state transitions, chronology leakage and weak counterexample testing. The integrator follows the bounded return/verification process in the [plan](RC_AV_EXECUTION_AND_RECONCILIATION_PLAN.md). No provider, principal or majority has automatic interpretive authority.

For each accepted correction, identify affected character/world state, readings, qualification outcomes, monographs and syntheses. Update mutable current records and route frozen corrections legitimately. Preserve the source-supported distinctions from independent analysis even when the final prose is shorter.

A later handoff includes the complete accepted records necessary for its scope, frozen artifact hashes, source boundary, disagreements and open dependencies. Transfer summaries orient the receiver; they cannot replace those underlying records.
