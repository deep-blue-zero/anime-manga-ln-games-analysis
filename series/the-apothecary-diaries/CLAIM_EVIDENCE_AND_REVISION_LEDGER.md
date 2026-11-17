---
title: "The Apothecary Diaries — Claim, Evidence and Revision Ledger"
artifact_id: AP_CLAIM_LEDGER
artifact_type: claim_evidence_revision_ledger
version: "1.0"
status: canonical
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
authority_generation: AP-INITIAL
authority_scope: "INITIAL bootstrap method, architecture, and administrative metadata only; no literary findings"
source_boundary: "Metadata reconnaissance: Japanese volumes 01–16 and separate simplified Chinese volume 15; no narrative admitted"
created: 2026-11-07
last_updated: 2026-11-07
---

# Claim, evidence and revision ledger

## Responsibility and current state

This ledger routes evidence, rival interpretations and revisions. It is mandatory from the first authorized reading because later information can change explanations of earlier events. It contains **zero literary claims and zero primary evidence excerpts** at INITIAL. The administrative obligations below are not character findings.

The full argument remains in the reading or study named by each row. Never condense a disputed motive, a causal mechanism, Japanese ambiguity or an ordinary-life counterexample into a claim label and discard its reasoning.

## Typed registers and stable identifiers

| Register / prefix | Required fields |
|---|---|
| Evidence `AP-E-nnnn` | Witness version/digest route; human locator; deterministic spine/member/block anchor; component and inspection lane; evidence channel; observation or short exact quotation/paraphrase; quotation status; subject/relationship if source-established; admitted frontier; source/derived/synthetic class; retrieval test result/date; full analytical home; limits |
| Claim version `AP-C-nnnn.vN` | Proposition; claim class; source and epistemic boundary; confidence with reason; supporting evidence; counterevidence; strongest rival; discriminator/falsifier; full argument; current authority; dependent state/studies; unresolved obligations |
| Revision `AP-R-nnnn` | Earlier claim version/formulation/boundary; transition; new version/formulation; new evidence; reasoning and rival disposition; affected outputs; propagation state; author/reviewer and date |
| Forecast `AP-P-nnnn` | Frozen predicted outcome or discriminating expectation; basis; competing prediction; explicit future test boundary; freeze identity/time; author exposure declaration; later outcome/evidence; adjudicator; diagnostic limits |
| Dispute `AP-D-nnnn` | Incompatible statements; exact routes/boundaries; suspected cause; viable explanations; evidence needed; responsible home; status and resolution history |

Evidence channels distinguish direct speech, behavior, narrated interiority, narrated event, report, role/observer presentation, image, paratext and external context. They are not interchangeable proof of intention. Quotation states are `EXACT_VERIFIED / WORKING_TRANSCRIPTION / PARAPHRASE`. Claim classes and confidence follow method §9. Synthetic test output is never admissible primary evidence and must route to its separate future test record.

The transition enum is `PRESERVE / STRENGTHEN / REVISE / DOWNGRADE / REJECT / OPEN`. A new claim starts OPEN; this is not an instruction to treat all supported later claims as uncertain. A preserved claim still records why new evidence did not change it.

Dispute causes may be `WITNESS_IDENTITY / TRANSLATION / CHRONOLOGY / KNOWLEDGE_ASYMMETRY / NARRATOR_OR_REPORT_RELIABILITY / PERFORMANCE_OR_ROLE / INTERPRETIVE_DIFFERENCE / MISSING_EVIDENCE / POSSIBLE_TEXTUAL_INCONSISTENCY / UNRESOLVED`. Several may remain live. No forced single explanation.

## Update transaction

1. In the full reading, develop the evidence and interpretation at the permitted frontier; preserve consequential wording and alternative accounts.
2. Create evidence routes and test retrieval for load-bearing uses. Do not manufacture paragraph IDs from an unavailable extraction.
3. Add a claim or append a version. Keep prior formulations and the full route even when rejected.
4. Register serial, subject, relationship, register and synthesis dependencies. A consequential revision triggers review of each dependency; unresolved propagation is visible in the integration ledger.
5. Freeze predictions before admitting the test source. Record no prediction as prospective if its author already saw that material.
6. An independent reviewer checks central revision/dispute closure. Current pointers can update after acceptance; frozen prose cannot be silently rewritten.

For a purely clerical locator repair, preserve the old route and the reason, verify equivalence and re-test retrieval. If repaired identity changes the evidence, it is an analytical revision, not a cosmetic fix.

## Initialized administrative obligations

| Administrative ID | Boundary fact / gap | State | Closure criterion |
|---|---|---|---|
| AP-CA-001 | No narrative admitted and no deterministic literary evidence routes exist | OPEN; not a literary claim | First authorized, inspected and accepted source transaction creates actual evidence/claim records |
| AP-CA-002 | V15 witness collision can contaminate support if keys are merged | OPEN; linked AP-SG-002 | Separate locked witnesses; every V15 claim names language/version; any alignment independently verified |
| AP-CA-003 | No forecasts or held-out tests have been run | NOT_STARTED | Explicit future test design, freeze and independent adjudication; retrospective fit labeled separately |

There is deliberately no invented claim row, evidence quotation, prediction or character name. Once real records exist, retain these administrative baseline rows as history rather than reusing their identifiers.

| History ID | Date | Change | Authority effect |
|---|---|---|---|
| AP-CH-001 | 2026-11-07 | Initialized operational schemas and admission/identity gaps | Administrative foundation only; no literary claim promotion |
