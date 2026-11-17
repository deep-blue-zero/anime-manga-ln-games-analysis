---
title: "Blue Box — Evidence, Comparison and Revision Ledger"
artifact_id: BB_CLAIM_LEDGER
artifact_type: evidence_comparison_revision_ledger
version: "1.0"
status: canonical
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
authority_generation: BB-INITIAL
authority_scope: "INITIAL bootstrap rules and attributed metadata only; no literary findings"
source_boundary: "Metadata only: Japanese main manga V01–27 and separate prose Interlude/Prologue; no narrative admitted"
created: 2026-11-07
last_updated: 2026-11-07
---

# Evidence, comparison and revision ledger

## Responsibility and schemas

This register holds evidence, independent arguments, comparison and history as distinct records. No source passage, literary claim, alignment or forecast exists now.

| Record / key | Required fields |
|---|---|
| Evidence `BB-E-nnnn` | Lane/witness/version/digest; human unit; image/panel/balloon or spine/member/paragraph deterministic route; map/extraction version; inspection/channel; observation/short quote/paraphrase and status; frontier; retrieval result; full argument; limits |
| Claim `BB-C-nnnn.vN` | Proposition; lane/knowledge/state boundary; warrant class; confidence/reason; support/counterevidence; strongest rival/falsifier; complete analytical home; dependencies |
| Comparison `BB-X-nnnn` | Independently accepted source-reading routes; exact paired/unmatched evidence; relation type; chronology/continuity assumption and warrant; authorized comparison scope; agreement/divergence; unresolved limits |
| Revision `BB-R-nnnn` | Old/new formulation/version/boundary; transition; decisive evidence; rival disposition; affected lane states/forms/studies/models; propagation/reviewer |
| Dispute `BB-D-nnnn` | Incompatible statements; exact source/knowledge layers; possible causes; alternatives; required evidence; retained resolution history |
| Forecast `BB-FC-nnnn` | Prediction/rival; author known lane/source/exposure; exact pre-source freeze; target holdout; later result; independent evaluator/opportunities/confounds |

Comparison relation types: VERIFIED_OVERLAP, COMPATIBLE_ADDITION, CHANGED_FOCALIZATION, CHANGED_WORDING, CHANGED_CAUSAL_OR_EVENT_ACCOUNT, CONTRADICTION, UNMATCHED, UNRESOLVED. No type automatically merges continuity.

Warrant classes: OBSERVATION, SELF_REPORT, NARRATOR_PRESENTATION, INFERENCE, HYPOTHESIS, CONTRADICTION, EXTERNAL_REFERENCE, EVALUATION, UNRESOLVED. Revision: PRESERVE, STRENGTHEN, REVISE, DOWNGRADE, REJECT, OPEN. Confidence needs a reason.

## Update and anti-compression rules

Develop and retain each full source-facing argument before comparison. Test exact locators in the locked witnesses. A pending route stays unresolved. Preserve narration/interiority and visual evidence as different channels even where a comparative thesis finds compatibility.

Append claim versions and comparison changes, preserving former wording, source limits and complete counterarguments. A later comparative claim cannot rewrite earlier prospective knowledge. A corrected map retains old/new identity and tests equivalence; changed evidence is a substantive revision.

Forecasts freeze before exposure; exposed tests are RETROSPECTIVE_CONSISTENCY_TEST. Synthetic output never becomes primary evidence, canonical dialogue or independent corroboration. Current pointers can change after acceptance; frozen readings/predictions remain intact.

| Administrative ID | Initial condition | State | Closure |
|---|---|---|---|
| BB-EA-001 | No admitted evidence/claims or tested routes | OPEN | Actual authorized independent source readings |
| BB-EA-002 | No verified overlap/divergence/continuity alignment | OPEN | Exact admitted paired sources and explicit comparison scope |
| BB-EA-003 | No forecasts or independent tests | NOT_STARTED | Genuine freeze/evaluation or explicit retrospective classification |

| History ID | Date | Operation | Result |
|---|---|---|---|
| BB-EH-001 | 2026-11-07 | Initialized evidence/comparison/claim/revision schemas | No composite canon or literary findings |
