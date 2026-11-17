---
title: "Domestic Girlfriend — expression and ordinary-life evidence"
series: domestic-girlfriend
artifact_id: DG_REGISTER_AND_ORDINARY_LIFE_LEDGER
artifact_type: expression_evidence_ledger
generation: DG-G1
version: "1.0"
status: canonical
authority_scope: "Contextual expression/behavior retrieval schema; zero source observations"
source_boundary: "Metadata reconnaissance of Japanese manga volumes 01-03 only; no narrative units admitted or inspected"
canonical_home: series/domestic-girlfriend/DG_REGISTER_AND_ORDINARY_LIFE_LEDGER.md
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
---

# Expression and ordinary-life evidence

## Why this home exists

An opening-only corpus can overfit striking confrontations and then mistake them for a person's baseline. This ledger preserves low-stakes behavior and Japanese expression by situation and interlocutor so later interpretation can test that risk. It makes no claim that any particular routine or register has appeared.

| Control | Current state | Required consequence |
|---|---|---|
| Ordinary-life samples | 0 | Stable-behavior/reconstruction claims unsupported |
| Source-verified Japanese expression samples | 0 | No written-register model |
| Performance evidence | OUT_OF_SCOPE | No acoustic voice, acting or timing inference |
| Coverage opportunity | UNASSESSED | Lack of samples is a gap, not negative evidence |

## Ordinary-life sample schema

One DG-O0001-style record denotes a bounded diagnostic situation, including exceptions and failed opportunities.

| Sample ID | Subject / interlocutors | Unit / event time / horizon | Situation and stakes | Opportunity to act | Observed action / inaction | Source presentation or reported behavior | State / relationship event links | Counterexample or alternative | Reading anchor / exact locators |
|---|---|---|---|---|---|---|---|---|---|

`situation` may be routine, humor/play, work/study, care, idle interaction or another sourced category; these are field choices, not asserted scenes. Classify stakes as ORDINARY, CRISIS or MIXED with a source-based reason. Negative evidence requires a real opportunity and an inspected response; an unseen situation is GAP. Record contextual alternatives, including a different audience or constraint, before proposing a trait.

## Japanese expression schema

One DG-X0001-style record denotes a relevant attested form in context.

| Expression ID | Speaker/thinker | Addressee / audience | Unit / state / horizon | Layer and attribution confidence | Brief Japanese form / labeled gloss | Register feature and pragmatic purpose | Comparable baseline / exception | Claim ID / reading anchor / locators |
|---|---|---|---|---|---|---|---|---|

Layer is SPEECH, THOUGHT, NARRATION, DIEGETIC_TEXT, ASIDE or EFFECT. Attribute thought/narration only as securely as the source allows. Record address, self-reference, politeness, endings, omission or ruby where relevant. The pragmatic purpose remains an INFERENCE unless explicitly established. A translation is labeled as a gloss, never independent Japanese voice evidence. Keep quotations minimal; bulk text remains outside Git.

Both analytical tables currently contain zero rows.

## Update and history

Append material samples during the same transaction as the reading; stable IDs never change. A recurring form needs multiple situated examples and counterexamples before it becomes a register claim. Link claims to the source samples, character states and directed relationships. Correct transcription or attribution by an append-preserving correction record `correction_id | prior_sample_id | date | old | new | source_basis | affected_claim_ids`; keep the mistaken historical form identifiable without retaining it as current evidence.

At each checkpoint summarize coverage by `subject | sampled_situations | interlocutors | observed_horizon | gaps | claim_ids`. A sample count is not a quality score. Check whether low-stakes and exception evidence actually tests proposed generalizations. A subject with no diagnostic ordinary-life material stays explicitly bounded.

Page-form observations supporting an expression remain in the full reading and FORM-tagged claims. A separate visual-form ledger is deferred until recurrence demands independent retrieval; do not stretch this expression home into an all-purpose motif catalog.
