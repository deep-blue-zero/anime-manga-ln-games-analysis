---
title: ROAD TO THE TOP Character and Relationship State Ledger
artifact_id: UM_RTTT_CHARACTER_AND_RELATIONSHIP_STATE_LEDGER
artifact_type: character_relationship_state_ledger
series: uma-musume
installment: road-to-the-top
generation: V1
status: canonical
scope: Evidence-bounded character states and directed interpersonal changes
source_boundary: "2023 original four-episode anime; no narrative sources admitted at bootstrap"
created: 2026-11-22
last_updated: 2026-11-22
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
do_not_use_as_literary_evidence: true
---

# Character and relationship state ledger

This ledger preserves what changes, for whom, under which conditions, and when that change becomes knowable. It implements the [analytical method](../00_Method/UM_RTTT_ANALYTICAL_METHOD.md) and routes interpretations through the [claim ledger](UM_RTTT_CLAIM_INTERPRETATION_LEDGER.md). **Accepted character states: 0. Accepted relationship states: 0.** A name in the roster is an identity reservation, not an observed trait or a monograph qualification.

## Reserved identities

| Local key | Canonical Latin-script name | Japanese name | Narrative-state boundary |
|---|---|---|---|
| `NTR` | Narita Top Road | ナリタトップロード | Unobserved |
| `ADV` | Admire Vega | アドマイヤベガ | Unobserved |
| `TMO` | T.M. Opera O | テイエムオペラオー | Unobserved |

Add other characters only after identity and source appearance are established; retain the authoritative Japanese spelling and record aliases without conflating historical horse and fictional character. Trainer, teammate, supporter and rival are roles to investigate, not preloaded states. Do not infer anyone's behavior from a franchise profile or real horse biography.

## Character-state schema

Allocate `RTTT-E01-CS0001` only after observing a source interval. The following is an **unallocated template**.

```yaml
character_state_id: TEMPLATE_UNALLOCATED
character_key: TEMPLATE
episode: TEMPLATE
source_id: TEMPLATE_MANIFEST_ID
source_interval: {start: TEMPLATE, end: TEMPLATE}
scene_id: TEMPLATE
observation_ids: []
entering_state_ref: TEMPLATE_OR_FIRST_OBSERVED
dramatic_time: TEMPLATE
disclosure_time: TEMPLATE
knowledge_boundary: TEMPLATE_EPISODE_AND_INTERVAL
explicit_self_report: TEMPLATE_OR_NOT_EXPRESSED
other_character_attribution: TEMPLATE_OR_NONE
observed_actions_and_decisions: TEMPLATE
observed_expression_gesture_and_delivery: TEMPLATE_WITH_CHANNEL_LIMITS
stated_goal_or_obligation: TEMPLATE_OR_UNAVAILABLE
interpreted_emotional_psychological_motivational_state: TEMPLATE_OR_OPEN
public_presentation_vs_private_witness: TEMPLATE_OR_UNTESTED
trigger_and_response: TEMPLATE
consequence_and_exit_state: TEMPLATE_OR_UNRESOLVED
constraints_or_counterexamples: []
state_change_or_later_disclosure: TEMPLATE_CHANGE_DISCLOSURE_UNCERTAIN
claim_ids: []
alternative_explanations: []
evidentiary_strength: TEMPLATE_HIGH_MODERATE_LOW_UNASSESSABLE
critical_review_and_reconciliation_ref: TEMPLATE
record_state: DRAFT
```

Keep observation and interpretation visibly separate. A character saying she is confident supports a self-report; it does not by itself establish confidence. Distinguish outward performance, observed choices, interior speech and another character's attribution. Psychological descriptions remain evidence-bounded interpretations, never clinical diagnoses. A goal, fear or obligation not expressed or tested remains unknown.

## Directed relationship schema

Allocate `RTTT-E01-RS0001`. A relationship state is directional: A's conduct toward B does not establish B's reciprocal feeling. Link two records when mutuality is actually supported. Use named participants rather than pronouns whose referent is unclear.

```yaml
relationship_state_id: TEMPLATE_UNALLOCATED
episode: TEMPLATE
source_id: TEMPLATE_MANIFEST_ID
source_interval: {start: TEMPLATE, end: TEMPLATE}
from_character: TEMPLATE
to_character_or_group: TEMPLATE
scene_id: TEMPLATE
observation_ids: []
entering_relationship_ref: TEMPLATE_OR_FIRST_OBSERVED
interaction_and_context: TEMPLATE
verbal_address_and_register: TEMPLATE_OR_UNAVAILABLE
gesture_proximity_shared_activity: TEMPLATE_OR_NOT_OBSERVED
support_competition_disclosure_or_boundary: TEMPLATE
response_and_reciprocity: TEMPLATE_OR_UNKNOWN
interpreted_relationship_change: TEMPLATE_OR_OPEN
alternative_readings: []
counterevidence_and_asymmetry: []
knowledge_boundary: TEMPLATE
related_character_state_ids: []
claim_ids: []
evidentiary_strength: TEMPLATE
critical_review_and_reconciliation_ref: TEMPLATE
record_state: DRAFT
```

Consider friendship, admiration, rivalry, recognition, intimacy and romantic subtext as potentially different readings. Preserve alternatives when the source does not decide between them. Emotional intensity, physical closeness or a supportive gesture alone does not establish romantic intent. Negative evidence requires a real opportunity in the inspected source; a relationship dimension not tested is `UNTESTED`, not absent.

## Prospective and longitudinal discipline

At each episode's entering boundary, reference only already admitted earlier-episode states. Record current-unit events before adding an episode-end retrospective interpretation. Preserve a pre-disclosure reading even if later evidence changes it. Historical knowledge, later episodes, theatrical additions, games and other anime are excluded from the character's knowledge state unless this installment itself establishes the information.

Track situational variation: conduct under pressure versus ordinary interaction, speech versus action, effort versus self-presentation, response to another's success versus one's own result, and what remains unknown. These are questions, not required traits for the three leads. A single action cannot establish a durable behavioral rule without a bounded rationale and a counterexample search.

## Qualification and portrait responsibility

This ledger supplies evidence for later character and relationship synthesis; it is not a substitute for a self-contained portrait. At specialist-synthesis readiness, assess every character for whom admitted evidence supports differentiation, including supporting characters. Record the decision in the project's readiness audit home with identity, boundary, evidence-based rationale, largest gaps, next trigger and a real monograph path once one exists. Outcomes follow the initiation policy: `QUALIFIED_PENDING`, `COMPLETE_AT_BOUNDARY`, `DEFERRED_EVIDENCE`, `REASSESS_AFTER_REVISION`. No outcomes are assigned at bootstrap, and no placeholder monographs are created.

## Append and revision rules

New observations create new state records; they do not silently replace an earlier state. Keep each record's episode, source interval and knowledge boundary immutable. An interpretation correction adds a dated entry referencing prior/new claim states and affected records. Use `DRAFT`, `ACCEPTED`, `DISPUTED`, `CORRECTED` or `WITHDRAWN`; retain withdrawn IDs. Preserve independent specialist contributions and the integrator's critical-review dispositions through the episode transaction record. A claim revision may change the current interpretation of a state without rewriting the historical observation.

## Accepted states

None. State comparisons across E01–E04 remain unavailable until source-grounded records exist.
