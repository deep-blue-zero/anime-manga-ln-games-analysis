---
title: ROAD TO THE TOP Claim and Interpretation Ledger
artifact_id: UM_RTTT_CLAIM_INTERPRETATION_LEDGER
artifact_type: claim_interpretation_ledger
series: uma-musume
installment: road-to-the-top
generation: V1
status: canonical
scope: Traceable analytical arguments, alternatives and attributable revisions
source_boundary: "2023 original four-episode anime; no narrative sources admitted at bootstrap"
created: 2026-11-22
last_updated: 2026-11-22
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
do_not_use_as_literary_evidence: true
---

# Claim and interpretation ledger

This is the canonical home for substantive interpretations, distinct from the [scene/evidence ledger](UM_RTTT_SCENE_EVIDENCE_LEDGER.md). **Analytical claims allocated: 0. Accepted interpretations: 0.** Research directions live in the [research register](../04_Research/UM_RTTT_RESEARCH_QUESTIONS.md); a plausible question does not become a conclusion by receiving an ID.

## Claim schema

Allocate stable installment-wide IDs `RTTT-CLM0001`, incrementing without reuse. A claim must name its subject and scope clearly enough to be challenged. Split a compound claim when separate propositions require different evidence. The following is an **unallocated template**, not a first claim.

```yaml
claim_id: TEMPLATE_UNALLOCATED
claim_version: 1
proposition: TEMPLATE_PRECISE_NAMED_SUBJECT
epistemic_state: TEMPLATE_GROUNDED_INTERPRETATION_OR_TENTATIVE_HYPOTHESIS
scope: TEMPLATE_EPISODE_INTERVAL_OR_ADMITTED_BOUNDARY
source_editions: []
supporting_observation_ids: []
reasoning_from_observation_to_interpretation: TEMPLATE
counterevidence_observation_ids: []
strongest_alternative_readings: []
disconfirmation_test: TEMPLATE
missing_evidence_and_channel_obligations: []
confidence: TEMPLATE_HIGH_MODERATE_LOW_UNASSESSABLE
confidence_rationale: TEMPLATE
related_character_state_ids: []
related_relationship_state_ids: []
related_race_ids: []
related_hypothesis_ids: []
external_context_ids: []
depends_on_claim_ids: []
affected_episode_or_synthesis_paths: []
independent_contribution_refs: []
critical_review_ref: TEMPLATE
integrator_disposition_and_reason: TEMPLATE
current_transition: OPEN
record_state: DRAFT
```

`HIGH` requires specific convergent evidence, an adequate inspected channel and a considered alternative; `MODERATE` retains a material plausible competitor; `LOW` has limited support or unresolved ambiguity; `UNASSESSABLE` lacks the needed evidence. State exactly what the confidence evaluates. Agreement between models does not increase confidence without independent source observations.

## Epistemic boundaries

Use these six states consistently: `VERIFIED_PRODUCTION_FACT`, `PRIMARY_SOURCE_OBSERVATION`, `GROUNDED_INTERPRETATION`, `TENTATIVE_HYPOTHESIS`, `EXTERNAL_CONTEXTUAL_FACT`, `UNVERIFIED_UNAVAILABLE`. Production facts belong in the production metadata, observations in their ledger, and external facts in identified context records. The claim ledger links those records without merging their authority.

An interpretation's support must cite observation IDs and recoverable locators, not an episode title alone. Separate what a character says, what she does, another person's attribution and the analyst's explanation. A historical race result can contextualize adaptation but cannot prove that the anime depicts the same outcome, framing or intention. A production interview can support a statement about the interviewee's explanation; it does not replace inspecting the scene. A translation issue stays visible until Japanese wording is checked.

## Revision history

Preserve every formulation and its source/knowledge boundary. Append a revision event rather than erasing the earlier argument. Each event records date, author role, old/new version, transition, triggering observation or correction, counterevidence, rationale and affected downstream artifacts. No transition discards the original evidence trail.

| Transition | Meaning |
|---|---|
| `OPEN` | An explicit unsettled question, evidence gap or unresolved contest |
| `PRESERVE` | Reassessed formulation remains supported within the same bounds |
| `STRENGTHEN` | New evidence increases support without changing the central proposition |
| `REVISE` | Proposition or material scope changes; retain the previous version |
| `DOWNGRADE` | Confidence or permitted scope decreases |
| `REJECT` | Evidence no longer supports the proposition; retain it for audit |

Use `record_state` values `DRAFT`, `ACCEPTED`, `DISPUTED` and `WITHDRAWN` to distinguish review standing from the interpretive transition. Rejection is not deletion. A corrected locator need not change an interpretation, while a stronger argument need not alter the original observation. Mark dependent claims for review whenever a premise changes; update each downstream artifact through targeted edits or a recorded erratum if frozen.

## Independent review and synthesis

The episode transaction record retains the principal, independent source-aware specialist and critical reviewer contributions, their source frontiers, disagreement and the integrator's acceptance/revision/rejection/defer decisions. Reviewers inspect the actual evidence channels their objections concern. A reviewer receiving only the principal's conclusions cannot supply independent source corroboration.

Only accepted claims with satisfied channel obligations may feed final synthesis. Open disputes and unresolved tests remain visible in synthesis readiness. Do not represent a frozen prospective hypothesis as something the analyst already knew before its later adjudication.

## Claim records

None. No claim is implied by the research prompts, character roster, race categories or template wording.
