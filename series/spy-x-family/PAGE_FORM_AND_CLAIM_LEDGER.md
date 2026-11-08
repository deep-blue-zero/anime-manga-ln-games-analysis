---
title: "SPY x FAMILY — Page Form and Claim Ledger"
artifact_id: SXF_CLAIM_LEDGER
artifact_type: page_form_claim_ledger
version: "1.0"
status: canonical
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
authority_generation: SXF-INITIAL
authority_scope: "INITIAL bootstrap rules and attributed metadata only; no literary findings"
source_boundary: "Metadata only: Japanese main manga V01–18 plus separate EYES ONLY fanbook; no narrative admitted"
created: 2026-11-07
last_updated: 2026-11-07
---

# Page form and claim ledger

## Responsibility

This ledger holds distinct evidence/form, claim, dispute and revision registers in one retrieval home. It cannot replace developed page, causal, linguistic or relationship analysis. No primary evidence, literary claim or forecast exists at INITIAL.

## Operational schemas

| Register / key | Required fields |
|---|---|
| Evidence `SXF-E-nnnn` | Exact witness/version/digest; human chapter/image/panel/balloon; spine/member/map version; source class and STILL_IMAGE/TEXT lane; observation/brief quote/paraphrase and status; admitted frontier; retrieval result; full argument; limits |
| Page/form `SXF-V-nnnn` | Exact page/spread and facing basis; layout/gutters/framing/reaction/silence/rendering/lettering; observed feature; proposed effect and rival; image/text interaction; counterexample; full close-reading route |
| Claim `SXF-C-nnnn.vN` | Proposition; source/knowledge/audience boundary; warrant class; confidence/reason; support; counterevidence; strongest rival; discriminator; current full home; dependencies |
| Revision `SXF-R-nnnn` | Prior/new formulation/version/frontier; transition; decisive evidence; rival disposition; affected knowledge/tie/voice/form/study/model; propagation and reviewer |
| Dispute `SXF-D-nnnn` | Conflicting routes/statements; source class; suspected causes; live alternatives; needed evidence; unresolved limits; resolution history |
| Forecast `SXF-F-nnnn` | Prediction/rival; known evidence/exposure; exact pre-test freeze; target heldout; later outcome/evidence; independent evaluator; opportunities/confounds |

Warrant classes: OBSERVATION, SELF_REPORT, NARRATOR_PRESENTATION, INFERENCE, HYPOTHESIS, CONTRADICTION, EXTERNAL_REFERENCE, EVALUATION, UNRESOLVED. Quote states: EXACT_VERIFIED, WORKING_TRANSCRIPTION, PARAPHRASE. Confidence needs a reason. Revision: PRESERVE, STRENGTHEN, REVISE, DOWNGRADE, REJECT, OPEN.

Disputes distinguish source/component, chronology, knowledge asymmetry, sincere error, role/audience, reliability, rendering convention, interpretation, missing evidence and possible textual inconsistency. A fanbook assertion and a main observation retain their layers even if a current interpretation agrees.

## Update and depth rules

Write and retain the full argument first. Explain how page form directs information and response, with counterexamples and serious alternatives. A genre/tone label or a matrix cell is not proof. Silent pages and ordinary transitions receive actual inspection.

Test central routes against locked source images. A failed locator stays unresolved; OCR alone cannot verify quotations. A mapping correction preserves old/new identity and tests equivalence; changed evidence requires substantive revision.

Append claim versions and preserve prior formulations, source/knowledge boundaries and full counterarguments. Propagate material changes to all named dependencies. Frozen prose/predictions are never silently rewritten. Forecasts freeze before exposure; exposed exercises are RETROSPECTIVE_CONSISTENCY_TEST. Synthetic results never count as primary or independent evidence.

| Administrative ID | Initial condition | State | Required evidence |
|---|---|---|---|
| SXF-EA-001 | No inspected pages or deterministic literary routes | OPEN | Authorized actual inspection and retrieval tests |
| SXF-EA-002 | Page tone, information effects and Japanese claims unassessed | NOT_ASSESSED | Full page/text arguments with contextual controls and rivals |
| SXF-EA-003 | No prospective tests or independent outcomes | NOT_STARTED | Genuine pre-exposure freeze or retrospective classification |

| History ID | Date | Operation | Result |
|---|---|---|---|
| SXF-EH-001 | 2026-11-07 | Initialized distinct evidence/form/claim/revision schemas | No narrative claim, tone inference or source quote |
