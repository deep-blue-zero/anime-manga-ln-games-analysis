---
title: "Medalist — Source-Unit Reading and Closure Specification"
artifact_id: "MEDALIST_SOURCE_UNIT_READING_SPEC"
artifact_type: "source_unit_reading_specification"
series: "Medalist / メダリスト"
series_id: "medalist"
generation: "MEDALIST_BOOTSTRAP_V1"
version: "0.1"
status: "active_provisional"
scope: "Reusable prospective source-unit transaction and completion contract"
canonical_home: "series/medalist/00 Frameworks and Methods/MEDALIST_SOURCE_UNIT_READING_SPEC.md"
source_boundary: "Architecture and metadata reconnaissance only; zero primary narrative units admitted or inspected"
created: "2026-10-11"
review_status: "OWNER_REVIEW_PENDING"
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
do_not_use_as_literary_evidence: true
recommended_reasoning_class: "DEEP_SYNTHESIS"
---

# Source-unit reading specification

This specification defines future transaction outputs under the [method](MEDALIST_ANALYTICAL_METHOD.md) and [architecture](MEDALIST_SYNTHESIS_ARCHITECTURE.md). It is not a V01 reading or a populated template. No sequential artifact exists at bootstrap.

## Identity and admission

Future collected-volume readings use `02 Sequential Readings/MEDALIST_VNN_DEEP_READING.md` with stable artifact ID `MEDALIST_VNN_DEEP_READING` and structured `artifact_type: manga_deep_reading`. A magazine-only chapter uses `MEDALIST_SCORE_NNN_SERIAL_DEEP_READING` and its own source identity. Create these paths only after admission and authorization. Explicitly mark authority, exact continuity/edition/language, generation, source boundary, canonical home and supersession quartet.

Before substantive inspection, record the current Git base, owner authorization, source key/Drive ID, independently reproduced hash if available, edition identity, chapter range, locator version, admitted components and exclusions. Structural verification checks ZIP/container integrity, OPF metadata, every relevant manifest/spine reference, image order/resolution and sampled locator round trips without describing narrative. Metadata verification alone is not narrative inspection. Admission requires complete retrievable primary evidence, usable Japanese/page inspection, declared limitations and appropriate authorization.

## Mandatory section contract

| Section | Required content and acceptance test |
| --- | --- |
| Source/provenance and coverage | Exact witness and locator convention; complete admitted page/Score coverage; separately labeled cover, bonus and paratext; gaps and processing limitations. |
| Entering knowledge state | Prior frozen reading/checkpoint IDs and versions; established developments, current scoped claims, unresolved questions and predictions. V01 explicitly has none. |
| Developments and chronological account | What changes in this unit, in source order; represented time distinguished from disclosure order; no later-unit explanation. |
| Narrative and formal close reading | Significant causal/framing patterns plus diagnostic manga pages/panels; description separated from inference and competing readings. |
| Character and directional relationships | Self-report/action/inference, state transitions, agency, mentorship/rivalry, knowledge differences, counterexamples and readiness implications. |
| Skating/competitive state | Technical statements, depicted execution, calls/results and external verification separately labeled; training/physical limits, risk and artistry where material. |
| Evidence and material claims | Stable observation IDs, exact locators, claim IDs/versions, confidence/basis, counterevidence and falsification criteria. |
| Open questions and prospective register | New hypotheses only where useful; predictions frozen before eligible later evidence with trigger, test window and adjudication rule. |
| Cumulative updates | Exact affected ledger paths and row IDs/versions; explain material changes; certify other ledgers reviewed with no update needed. |
| Frozen exit state | Source endpoint, knowledge frontier, accepted/open/rejected claims, participant state and unresolved debts recoverable as of this unit. |
| Verification and transaction closure | Coverage/locator checks, cross-reference/authority review, staged paths, commit recovery route, publication/audit state and next candidate without implied authorization. |

## Observation and freeze schema

Each canonical observation has `MD-EV-VNN-####` (or `MD-EV-SNNN-####` for serial units), plus: source key, locator, component/continuity, inspected feature, speaker/observer, story-time certainty, evidence class, identification confidence, limits and linked claims. Short Japanese text/gloss/ambiguity appears here when needed. Ledgers reference this row rather than owning a second observation. Material claims have stable `MD-CL-####` IDs and exact versions.

An exit freeze `MD-FR-VNN` records: entering freeze, admitted witness set, coverage endpoint, claim-version list, affected ledger row/version references, unresolved questions/prediction IDs, actual inspection limitations and next candidate. The reading contains a compact state snapshot, not merely links to mutable current rows. Preserve earlier versions and qualifiers even when subsequent ledger views advance. A source-unit's completed receipt is recovered from the Git commit containing it; no commit claims to contain its own SHA.

## Closeout and interruption

Close one unit atomically: write the reading, update every materially affected ledger, source status and entrypoint, verify all named claims/locators, then validate and persist under the integration checklist. Partial inspection records the exact high-water mark within the unit but cannot advance the completed sequential boundary. Publication remains subject to source audit, housekeeping and final exact-head integration audit.

Default future execution is `single_operation`. A continuous run requires a recoverable owner-authorized terminal boundary and independently closed/frozen units. After interruption, retrieve actual branch/head, entrypoint, last closed freeze, pending candidate and audit state before resuming. Later-source access is never evidence that an unfinished earlier unit completed. Current bootstrap: zero completed readings; no narrative admission; `SEQUENTIAL_ANALYSIS_LOCK = CLOSED`.
