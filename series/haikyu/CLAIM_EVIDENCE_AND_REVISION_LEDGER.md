---
title: "Haikyu!! — Claim, Evidence and Revision Ledger"
artifact_id: HQ_CLAIM_LEDGER
artifact_type: claim_evidence_revision_ledger
version: "1.0"
status: canonical
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
authority_generation: HQ-INITIAL
authority_scope: "INITIAL bootstrap rules and attributed metadata only; no narrative findings"
source_boundary: "Metadata only: Japanese colour-edition main V01–45 plus separate 10th Chronicle and Final Guidebook; no narrative admitted"
created: 2026-11-07
last_updated: 2026-11-07
---

# Claim, evidence and revision ledger

## Responsibility

Route exact evidence to full arguments, retain counterreadings and record changing interpretations. This register has zero narrative evidence, claims or forecasts at INITIAL. Source inventory rows are administrative provenance, not literary findings.

## Schemas and revision vocabulary

| Record / prefix | Required fields |
|---|---|
| Evidence `HQ-E-nnnn` | Witness/version/digest route; human chapter/page/panel/balloon; deterministic image/member mapping; crop/spread identity if used; channel and inspection lane; observation/short quote/paraphrase; quotation status; frontier; retrieval result/date; full argument; limits |
| Claim `HQ-C-nnnn.vN` | Proposition; warrant class; source/epistemic boundary; confidence/reason; support; counterevidence; strongest rival; falsifier/discriminator; current analytical home; action/character/visual/specialist/model dependencies |
| Revision `HQ-R-nnnn` | Old/new versions and formulations; PRESERVE/STRENGTHEN/REVISE/DOWNGRADE/REJECT/OPEN; decisive evidence; alternative disposition; propagation status; reviewer/date |
| Dispute `HQ-D-nnnn` | Incompatible claims/routes; witness/edition; suspected cause(s); live explanations; needed evidence; current limit; resolution history |
| Forecast `HQ-F-nnnn` | Prospective prediction/rival; known boundary/exposure; frozen exact input/output; target unexposed source; later evidence/outcome; independent evaluator; diagnostic opportunity and confounds |

Warrant classes: OBSERVATION, SELF_REPORT, NARRATOR_PRESENTATION, INFERENCE, HYPOTHESIS, CONTRADICTION, EXTERNAL_REFERENCE, EVALUATION, UNRESOLVED. Confidence: high/moderate/low/unresolved with reason. Quote states: EXACT_VERIFIED, WORKING_TRANSCRIPTION, PARAPHRASE; OCR alone cannot earn EXACT_VERIFIED.

Dispute types distinguish witness/edition, page mapping, chronology/timing, knowledge asymmetry, report reliability, role/audience, rendering convention, interpretation, missing evidence and possible textual inconsistency. Keep unresolved alternatives rather than harmonize them.

## Update and preservation

Write the developed source-facing argument first, including causal links, ordinary contexts, Japanese ambiguity and serious alternatives. The ledger records its route; it never replaces the argument. Test retrieval for central evidence in the locked witness.

Append claim versions and revisions, preserving former formulations and full routes. A meaningful change reviews every named downstream dependency, not just the current summary. Correcting a locator preserves old/new mapping and tests equivalence; changed evidence requires substantive revision.

Freeze prospective forecasts before exposure; otherwise label RETROSPECTIVE_CONSISTENCY_TEST. Synthetic outputs stay separate and never count as primary observations or independent support. Current-view pointers can move after acceptance; frozen readings and predictions cannot be silently edited.

| Administrative obligation | Current state | Closure criterion |
|---|---|---|
| HQ-EA-001 No literary evidence or claims admitted | OPEN | Actual authorized inspection and accepted full reading with retrieval routes |
| HQ-EA-002 Colour/companion source layers can be conflated | OPEN | Every claim names exact witness/source class and admitted boundary |
| HQ-EA-003 No forecasts or independent tests exist | NOT_STARTED | Genuine prospective freeze/evaluation or explicit retrospective label |

| History ID | Date | Operation | Result |
|---|---|---|---|
| HQ-EH-001 | 2026-11-07 | Initialized evidence, claims, disputes and forecast schemas | Administrative baseline only; no invented literary argument |
