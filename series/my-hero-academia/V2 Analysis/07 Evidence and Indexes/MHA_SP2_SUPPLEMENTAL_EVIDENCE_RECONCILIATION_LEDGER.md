---
series: MHA
artifact_type: supplemental_evidence_reconciliation_ledger
scope: V01-V42_PLUS_UA_UAN_UAG
generation: V2
status: canonical
source_boundary: Owner-selected Japanese UA, UAN and UAG EPUBs; reconciliation against the preserved completed V01-V42 corpus
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
recommended_reasoning_class: DEEP_SYNTHESIS
---

# MHA SP2 — Supplemental evidence reconciliation ledger

## Current state and responsibility

**Initialized; substantive evidence review is pending. No character claim has yet been admitted by this ledger.** The source-lock transaction establishes retrieval and the adjudication contract; it does not pre-judge what the books add. See the [current map](../00%20Frameworks%20and%20Methods/CURRENT_STATE_AND_CORPUS_MAP.md#current-supplemental-reconciliation) and [source lock](../01%20Source%20Lock%20and%20Inventory/MHA_SP2_OFFICIAL_SUPPLEMENTAL_SOURCE_LOCK.md).

This selective ledger owns consequential claim reconciliation. Page-complete accounting belongs to each book audit and coverage CSV; absence of a ledger record is not evidence that its page was unread. Stable IDs use `SUP-UA-001`, `SUP-UAN-001`, `SUP-UAG-001`, with stable subclaims when a record contains different effects. Cross-book revisions link the original ID rather than deleting a prior checkpoint. A record may have several destinations without becoming multiple independent observations.

## Required record contract

Each admitted record states: original code/spine locator and exact source-map member; verified printed page when available; brief Japanese anchor and bounded gloss; attributable author/editor/character speaker and audience; subjects/relationships/domain; evidence class; book print/digital dates, original/reprint provenance, editorial cutoff, depicted state and final applicability; authority/confidence and any conflict; manga and later-book comparators; dependency status; analytical outcome; temporal outcome; modeling effect; literary consequence; and exact affected current homes or a reason for no propagation.

Recurring book-level metadata may be inherited by an explicit link to the book audit, with claim-specific exceptions and unknowns stated. The original-member field may use the deterministic source-map lookup rather than reproduce a long member path in every paragraph. Record IDs, locators, source dependence and downstream homes must remain explicit. Short Japanese anchors support verification; this is not a transcription of the books.

Evidence classes are `NARRATIVE`, `BONUS_FICTION`, `PROFILE_FACT`, `AUTHOR_COMMENT`, `EDITORIAL_SUMMARY`, `SELF_REPORT`, `OTHER_CHARACTER_JUDGMENT`, `RATING`, `DESIGN`, and `GAG`. Analytical outcome is independently `CONFIRM`, `STRENGTHEN`, `COMPLICATE`, `NARROW`, `CONTRADICT`, `NEW`, or `INSUFFICIENT`. Temporal use is independently `EARLIER_ONLY`, `CONTINUING_WITH_SUPPORT`, `SUPERSEDED`, `ENDPOINT`, or `UNRESOLVED`. Modeling effect is independently `NONE`, `FACTUAL_TEXTURE`, `RELATIONSHIP`, `CONDITIONAL_COVERAGE`, `MOTIVE`, `REVISION`, or `CONFIDENCE_REDUCTION`. Explain any compound outcome rather than collapsing it into an uninformative verdict.

Readiness promotions require the existing schema and named evidence, not a count of new atoms. Preferences are admissible factual texture but do not by themselves establish conduct in an unobserved setting. A sourced author statement may change a character interpretation without repairing a missing dramatic scene. Source disagreement can remain unresolved where attribution, chronology or evidence cannot adjudicate it. Historical manga-only freezes and formal validation remain intact.

## Records

No substantive records yet. Next: UA page-complete visual review and its first verified checkpoint.
