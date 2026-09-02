---
series: AOT
artifact_type: character_model_schema
scope: per_character_template
status: canonical
generation: V2
version: '1.0'
date: '2026-08-23'
source_boundary: Schema only; no character-specific claims
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
architecture: AOT_CHARACTER_MODELING_AND_SIMULATION_ARCHITECTURE_V1.md
validation_method: AOT_CHARACTER_RECONSTRUCTION_AND_VALIDATION_METHOD_V1.md
---

# Attack on Titan — Character Reconstruction Model Schema v1.0

## Purpose

This is the canonical template for future per-character reconstruction models. It standardizes semantic responsibilities without requiring identical prose length for every character.

## Required front matter

```yaml
---
series: AOT
artifact_type: character_reconstruction_model
character: "Eren Jaeger / エレン・イェーガー"
scope: V01-V34
generation: V2
status: active_provisional
source_boundary: "Japanese manga V01-V34"
model_time_slices:
  - V01
  - V04
  - V18
  - V34
construction_set: "..."
prospective_validation_register: "..."
validation_status: pending
supersedes: null
superseded_by: null
do_not_use_as_current_authority: false
---
```

## Required model sections

### 1. Scope, authority, and use boundary

State what version(s) of the character the model can represent and what it cannot.

### 2. Reconstruction summary

A compact account of the character's recognizable behavioral organization. Avoid thematic slogans as the sole summary.

### 3. Stable dispositional core

Traits/tendencies that survive multiple states, each with evidence and counterevidence.

### 4. Developmental state map

For each major boundary record:

`boundary | knowledge | self-conception | role | dominant conflict | available repertoire | suppressed/unavailable repertoire | evidence`

### 5. Attention and epistemic style

What the character notices, verifies, ignores, assumes, asks, updates, or refuses to know.

### 6. Value hierarchy and override conditions

Do not merely list values. State when one value overrides another.

### 7. Decision grammar

Use conditional rules:

`trigger/condition -> likely response family -> inhibitors/overrides -> confidence -> evidence`

### 8. Threat, conflict, and coercion

Separate immediate violence, strategic threat, interpersonal threat, humiliation, authority pressure, and existential danger.

### 9. Failure, guilt, regret, and repair

Track attribution style, self-blame, blame of others, counterfactual thinking, apology, learning, withdrawal, escalation, and repair.

### 10. Care, attachment, and help

Distinguish giving, asking, accepting, rejecting, and controlling forms of care.

### 11. Directed relationship matrix

`character -> interlocutor | boundary | trust/attachment | role | speech register | behavioral tendencies | fault line | evidence | confidence`

### 12. Ordinary life, preferences, and material habits

Include only attested evidence. Mark unknowns rather than extrapolating from personality.

### 13. Japanese voice fingerprint

Cover self-reference, address, register, turn shape, speech acts, lexical habits, relationship variation, and state deltas.

### 14. Emotional and bodily state deltas

At minimum distinguish ordinary/resting, fear, anger, grief/guilt, acute command/combat, injury/exhaustion, and intimacy/vulnerability where evidenced.

### 15. Institutional and role performance

How military rank, captivity, public symbolism, royal status, infiltrator role, or other institutions alter behavior and speech.

### 16. Mischaracterization traps

List tempting reductive readings and the evidence that limits them.

### 17. "Would sound/act wrong if..." constraints

Operational negative constraints for QA.

### 18. Bounded hypothetical-response rules

For major scenario classes, give top response families and confidence rather than deterministic scripts.

### 19. Scenario-distance limits

List domains that are D0/D1-friendly and domains where only D2/D3 inference is possible.

### 20. Evidence crosswalk

Route each major model claim to ledger entries, canonical volume evidence IDs, and source locators.

### 21. Validation record

Include frozen prediction IDs and `PASS/PARTIAL/FAIL/NOT_TESTED/CONFOUNDED` outcomes.

### 22. Open uncertainties

State what would require more source, anime performance evidence, guidebook material, or simply cannot be known.

## Required tables

### Conditional behavior rule table

| Rule ID | Boundary | Condition | Relationship/role | Likely response family | Override/inhibitor | Confidence | Evidence |
|---|---|---|---|---|---|---|---|

### Voice/register matrix

| Boundary | Interlocutor/role | Baseline register | Speech acts | State delta | Confidence | Evidence |
|---|---|---|---|---|---|---|

### Model limitations table

| Domain | Coverage | Maximum warranted confidence | Main limitation |
|---|---|---|---|

## Promotion rule

A model may be useful while `active_provisional`. `canonical` means the evidence, temporal boundaries, ordinary-life gaps, voice model, negative constraints, and validation results have all been audited. It does not mean every novel scenario becomes predictable.
