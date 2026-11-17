---
title: "Medalist — Source-Unit Reading and Closure Specification"
artifact_id: "MEDALIST_SOURCE_UNIT_READING_SPEC"
artifact_type: "source_unit_reading_specification"
series: "Medalist / メダリスト"
series_id: "medalist"
generation: "MEDALIST_BOOTSTRAP_V1"
version: "0.6"
status: "canonical"
scope: "Reusable prospective source-unit transaction and completion contract"
canonical_home: "series/medalist/00 Frameworks and Methods/MEDALIST_SOURCE_UNIT_READING_SPEC.md"
source_boundary: "Reading contract; the closed manga boundary and admitted sources are those recorded in CURRENT_STATE_AND_CORPUS_MAP.md"
created: "2026-10-11"
updated: "2026-10-13"
review_status: "AUTHOR_REVIEWED_NAMING_RULE_UPDATE"
foundation_owner_approval: "I approve the revised foundation. Begin analysis/deep reading of Volume 1."
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
do_not_use_as_literary_evidence: true
recommended_reasoning_class: "DEEP_SYNTHESIS"
---

# Source-unit reading specification

This owner-approved specification defines transaction outputs under the [method](MEDALIST_ANALYTICAL_METHOD.md) and [architecture](MEDALIST_SYNTHESIS_ARCHITECTURE.md). It is not a V01 reading or a populated template. No sequential artifact exists at bootstrap.

## Identity and admission

Future collected-volume readings use `02 Sequential Readings/MEDALIST_VNN_DEEP_READING.md` with stable artifact ID `MEDALIST_VNN_DEEP_READING` and structured `artifact_type: manga_deep_reading`. A magazine-only chapter uses `MEDALIST_SCORE_NNN_SERIAL_DEEP_READING` and its own source identity. Create these paths only after admission and authorization. Explicitly mark authority, exact continuity/edition/language, generation, source boundary, canonical home and supersession quartet.

Before substantive inspection, record the current Git base, owner authorization, source key/Drive ID, independently reproduced hash if available, edition identity, chapter range, locator version, admitted components and exclusions. Structural verification checks ZIP/container integrity, OPF metadata, every relevant manifest/spine reference, image order/resolution and sampled locator round trips without describing narrative. Metadata verification alone is not narrative inspection. Admission requires complete retrievable primary evidence, usable Japanese/page inspection, declared limitations and appropriate authorization.

## Mandatory section contract

A reading or audit opened after 2026-10-13 names characters under the method's [entity naming and referential clarity](MEDALIST_ANALYTICAL_METHOD.md#entity-naming-and-referential-clarity) rule. Readings closed before that date are frozen and are not rewritten for it.

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

## Fanbook paratext-audit transaction

Future full-book artifacts use `02 Sequential Readings/MEDALIST_FB01_PARATEXT_AUDIT.md` and `MEDALIST_FB02_PARATEXT_AUDIT.md`, matching stable artifact IDs and structured `artifact_type: guidebook_paratext_audit`. They are governed substantive source readings: the CLOSED lock and authorization rules apply. Create them only for actual admitted work, not as bootstrap placeholders or numbered manga volumes. A deliberately bounded component audit states its narrower identity/scope and cannot claim whole-book completion.

Apply the mandatory contract with these supplemental acceptance tests:

1. Verify source/hash/edition, component inventory, coverage basis, `admit_after` and actual documentary/fiction inspection capabilities. Inventory excluded reprints, teasers or unknown-continuity material; do not imply that inventoried means read/admitted.
2. Enter from the completed manga-only freeze at the verified checkpoint, plus any already admitted supplements. Name prior claim/ledger versions, exposure and exclusions. The book's analytical position differs from the story date of any event it describes.
3. Audit every admitted component under the method's `FB-DATA / FB-RATING / FB-EDITORIAL / FB-FICTION / FB-CREATOR / FB-TECHNICAL` layers. Preserve attribution, exact image/paragraph/panel locators and confidence; OCR alone cannot authenticate a documentary claim. New bonus fiction receives narrative/form/character analysis where verified; reprinted scenes do not count as independent evidence.
4. Produce an explicit retrospective delta register: `later observation/locator + source layer + prior claim/version + earlier best inference + new evidence + PRESERVE/STRENGTHEN/REVISE/DOWNGRADE/REJECT/OPEN + affected homes/versions + unresolved limits`. Distinguish new facts, corroboration, summary, changed framing and surviving conflict; separate story time, disclosure and character knowledge.
5. Reconcile materially affected ledgers/readiness, review dependent arguments and certify no-change homes. Keep manga-only freezes and original predictions intact. Source observations remain solely in the fanbook audit; domain ledgers link them.
6. Freeze the combined state and close source/entrypoint/publication records. An admitted subset with excluded later components does not certify excluded content covered. Partial inspection preserves the high-water mark but cannot claim full audit completion.

Fanbook observations use `MD-EV-FB01-####` or `MD-EV-FB02-####`; completed full-book freezes use `MD-FR-FB01` or `MD-FR-FB02`. Component-scoped records append their declared component scope to avoid colliding with full-book IDs. Record entering freeze, unchanged completed mainline manga endpoint, admitted component/witness set, supplemental endpoint, exact active claim/ledger versions, unresolved debts and next candidate. Later manga transactions identify this combined entering state while retaining the earlier manga-only freeze as historical truth. Completion increments supplemental progress separately from completed manga readings.

## Closeout and interruption

Close one unit atomically: write the reading, update every materially affected ledger, source status and entrypoint, verify all named claims/locators, then validate and persist under the integration checklist. Partial inspection records the exact high-water mark within the unit but cannot advance the completed sequential boundary. Publication remains subject to source audit, housekeeping and final exact-head integration audit.

Default future execution is `single_operation`. A continuous run requires a recoverable owner-authorized terminal boundary and independently closed/frozen units. After interruption, retrieve actual branch/head, entrypoint, last closed freeze, pending candidate and audit state before resuming. Later-source access is never evidence that an unfinished earlier unit completed. Historical bootstrap: zero completed readings and CLOSED lock. Historical activation: owner-authorized V01 witness admitted, zero completed readings, OPEN initiation gate and single-operation V01 scope. Current closure: one complete [V01 reading and MD-FR-V01](../02%20Sequential%20Readings/MEDALIST_V01_DEEP_READING.md), seven reconciled ledgers, completed V01 operation and no later authorization; the entrypoint owns live progress. From 2026-10-12 an owner-authorized continuous run covers V02–V15 under this unchanged contract; each volume still closes and freezes separately.
