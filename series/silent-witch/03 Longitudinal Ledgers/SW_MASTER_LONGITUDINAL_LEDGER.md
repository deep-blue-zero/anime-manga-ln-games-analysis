---
title: "Silent Witch — SW Master Longitudinal Ledger"
artifact_id: SW_MASTER_LONGITUDINAL_LEDGER
artifact_type: master_longitudinal_ledger
series: "Silent Witch: Secrets of the Silent Witch"
series_id: silent-witch
generation: V1
version: "1.0"
status: canonical
scope: "Exclusive pre-split cumulative state; initialized schemas with zero literary records"
source_boundary: "Architecture bootstrap and source reconnaissance only; no narrative source unit analyzed."
created: "2026-10-12"
canonical_home: "series/silent-witch/03 Longitudinal Ledgers/SW_MASTER_LONGITUDINAL_LEDGER.md"
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
do_not_use_as_literary_evidence: true
---

# Master longitudinal ledger

This is the single pre-split cumulative analytical home specified by [the architecture](../00%20Frameworks%20and%20Methods/SW_SYNTHESIS_ARCHITECTURE.md). The current entrypoint is [the corpus map](../CURRENT_STATE_AND_CORPUS_MAP.md). This file preserves cumulative meaning and revision history; volume readings own underlying diagnostic observations, and Drive owns raw source/locator derivatives.

## Actual initialization state

```yaml
longitudinal_state:
  state: NO_SOURCE_UNIT_ANALYZED
  committed_high_water_mark: PRE_V01
  analyzed_units: []
  frozen_units: []
  literary_observations: 0
  local_character_identities: 0
  character_models: 0
  readiness_assessments: 0
  claim_records: 0
  revision_records: 0
  prediction_records: 0
  split_ledger_paths: []
  sequential_analysis_lock: OPEN
  sequential_analysis_lock_scope: JAPANESE_LN_V01_ONLY
```

Zero records are truthful absence of analysis, not findings about the novel. The schemas below contain no fabricated scene rows, sample characters or simulated dialogue.

## Common record contract

Every source-bearing record carries: stable typed ID; continuity/witness/source unit; applicable diegetic interval and disclosure boundary; evidence class; canonical observation reference; exact evidence route; formulation; support; material counterevidence/rival explanation; uncertainty; created/updated boundary; and supersession/revision references where relevant.

Stable IDs are never renumbered. Source observation grammar is `SW-E-LNJP-V<NN>-<sequence>` for numbered LN units; the volume reading owns those IDs. Supplement/web IDs are separate. Local entity keys resolve only inspected identity evidence and are not global character enrollments.

The common fields apply to all sections. The following field lists define each section's additional exclusive responsibility; they are schemas, not populated rows.

## 1. Character state and speech — SW-S

Owns source-bearing character changes, role constraints, ordinary behavior, self-conception and written-speech conditioning.

Fields: local key; name/title/address alias and scope; state before; represented perception/appraisal/affect; options; action/speech; consequence; state after; change kind; persistent feature; persona/private distinction; audience/recipient; register/address/silence feature; diagnostic ordinary-life basis.

Change kinds: DISPOSITION_CHANGE, KNOWLEDGE_CHANGE, ROLE_CONTEXT_CHANGE, RELATIONSHIP_CHANGE, REVEALED_NOT_NEW, UNRESOLVED. A knowledge-change summary links to SW-K for proposition ownership. A relational effect links to SW-R.

Records: none.

## 2. Directional relationships and obligations — SW-R

Owns A-to-B relationship change; B-to-A is separate even within a shared episode.

Fields: actor; recipient; relation/role; actor's aim; trust/disclosure state before/after; obligation origin/terms; initiative/refusal; dependency/resources/power; concealment or disclosure act; conflict/repair; independent goals; reciprocity assessment; linked knowledge/state IDs.

Attraction, affection, loyalty, duty, dependence and understanding are separate variables. No romance score or assumed mutuality is stored.

Records: none.

## 3. Chronology and epistemic state — SW-K

Owns proposition-specific participant/reader knowledge and event/revelation order.

Fields: proposition ID/formulation; event and disclosure anchors; order/date certainty; knower/attributing observer; knowledge/belief/suspicion/ignorance status; evidence available to that knower; truth assessment separately; prior/current state; source of change; withheld/false information; continuity conflict.

One character's known proposition cannot be inherited by all participants. Uncertain dates remain uncertain. Event order may be partial; no invented complete calendar is required.

Records: none.

## 4. Institutions, world and magic — SW-W

Owns cumulative operational world/institution claims and their exceptions.

Fields: domain; stated rule/doctrine; asserting source position; demonstrated operation; conditions/costs/resources; exception/failure; enforcement versus nominal rule; role/political/material constraint; mathematical or magical reasoning basis; current formulation; competing causal model; linked chronology/claim IDs.

Character explanation, institutional belief, observed mechanism and universal law remain distinguishable. A single successful demonstration does not prove an unlimited rule.

Records: none.

## 5. Load-bearing claims and revision history — SW-C / SW-CR

SW-C owns the current bounded formulation and its retrieval route. Fields: claim ID; question/domain; formulation; source/knowledge range; class; support; counterevidence; alternatives; confidence and reason; current transition/state; discriminating observation; dependent artifacts/IDs; revision references.

SW-CR owns append-only change events. Fields: revision ID; claim ID; earlier formulation and boundary; transition; new formulation and boundary; new support/counterevidence; reason; affected homes; correction versus later reinterpretation; date/reviewer. Allowed transitions:

| Transition | Meaning |
|---|---|
| PRESERVE | Material formulation retained after review. |
| STRENGTHEN | Same formulation receives stronger independent support. |
| REVISE | Wording, scope or mechanism materially changes. |
| DOWNGRADE | Confidence or warranted scope decreases. |
| REJECT | Claim is contradicted sufficiently to cease being accepted. |
| OPEN | Discriminating evidence remains insufficient or conflicting. |

An initial claim has no invented predecessor. It may begin OPEN or another justified initial assessment; a revision event requires an actual previous formulation. Preserve rejected claims for provenance rather than deleting their IDs. Normative criteria are explicit and separate from evidence confidence.

Claim records: none. Revision records: none.

## 6. Prospective questions and predictions — SW-P

Owns genuine prospective tests and open questions across source-unit boundaries.

Fields: ID; frozen wording; preparation boundary/reference; basis observations/claims; target opportunity; expected outcome if any; falsifying/weakening outcome; confidence basis; test status; eligible adjudicating observations; result/revision route.

Statuses: OPEN, TESTED_SUPPORTED, TESTED_COMPLICATED, TESTED_DISCONFIRMED, UNTESTED, or RETIRED_WITH_REASON. An open question needs no predicted answer. An absent opportunity is UNTESTED; a remembered later event is never a newly frozen prediction.

Records: none.

## 7. Literary form, motifs and evaluation — SW-F

Owns recurring prose/form and ethical-framing patterns that warrant cumulative retrieval.

Fields: feature/domain; textual/formal mechanism; focalization/withholding/reader alignment; Japanese wording/register evidence; recurrence and changed function; affected-person access; evaluative criterion; consequences/tone; strongest rival interpretation; one-off versus promoted reason; linked claims/observations.

A scene's comic tone is distinct from its represented act and normative assessment. Avoid compulsory ethical scoring of every passage. Isolated details without cumulative significance remain in their volume reading.

Records: none.

## 8. Reconstruction readiness — SW-RD

Owns local, domain-specific readiness decisions, not operational model rules or global grades.

Fields: local identity; continuity/state/source boundary; requested output tier/domain; readiness state; evidence variety/ordinary/recipient coverage; affirmative limitations; missing evidence; held-out/prospective test route; actual results; restrictions/abstentions; reviewer/date; existing model/evidence path only when created; prior decision/revision route.

Readiness vocabulary and tier criteria come from [the character method](../00%20Frameworks%20and%20Methods/SW_CHARACTER_RECONSTRUCTION_METHOD.md). Absence of evidence and affirmative negative evidence are separately recorded. No character is assessed in this bootstrap.

Records: none.

## 9. Unit closure and acceptance — SW-U

Owns cumulative transaction bookkeeping separately from claims.

Fields: witness/unit; source lock and locator fidelity state; admitted prose/image/paratext coverage independently; inspection completed; semantic review/acceptance state; each typed responsibility's update IDs or no-material-update rationale; exit freeze; durable/committed closure reference; remaining mandatory/optional evidence; publication/audit routes.

No numbered volume, supplement, or web unit is closed. Repository-wide publication facts belong to the entrypoint/actual Git workflow; this ledger links their receipts without guessing.

Records: none.

## Write, amend, and split rules

The authorized sequential integrator appends source-bearing state and revision events after full unit inspection. Patch current claim/readiness views only with preserved prior events. Record every affected responsibility's material delta or explained no-update in the unit closeout. Coverage completion never mechanically promotes an inference or readiness level.

Correct an objective error through an explicit correction event retaining old/new evidence routes and affected homes. Later reinterpretation is a source-bounded revision, not a rewrite of the historical freeze. If a record cannot be supported, defer or mark uncertainty rather than padding a table.

Split a typed responsibility only after recurring evidence establishes independent retrieval/revision pressure or a separate specialist dependency. Record exact transferred IDs, ownership, new path and necessary bounded backfill in architecture/entrypoint. Preserve historical routes and prohibit duplicate live datasets. Architecture-defined split decisions, not arbitrary row counts, govern this transition.
