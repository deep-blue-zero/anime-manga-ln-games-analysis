---
series: ASCENDANCE_OF_A_BOOKWORM
artifact_type: master_longitudinal_ledger
scope: PRE_SPLIT_CROSS_VOLUME_STATE
generation: V0.2
status: canonical
release_state: mutable_active
source_boundary: "Japanese-language light-novel EPUB corpus; no numbered volume analyzed yet"
committed_high_water_mark: PRE_V01
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
---

# Ascendance of a Bookworm — master longitudinal ledger

This file is the canonical **pre-split cumulative state** for the Japanese-primary numbered-volume analysis. It begins before V01 so that the first source-unit transaction has a durable place to propagate evidence instead of allowing important cross-volume observations to remain scattered in standalone deep readings.

It is deliberately one ledger rather than a collection of empty specialist ledgers. A responsibility is split into its own file only after recurring evidence creates independent retrieval or revision pressure.

## Current state

```yaml
longitudinal_state:
  architecture_lifecycle: INITIAL
  committed_high_water_mark: PRE_V01
  numbered_volumes_completed: []
  source_derived_claims_present: false
  dedicated_ledgers_split_from_master: []
  next_source_unit: V01
```

There are **no source-derived Bookworm findings in this ledger yet**. The sections below are active schemas and routing homes, not assertions about the story.

## Update contract

After each numbered volume, add only observations that deserve cumulative retrieval beyond the local deep reading. Every durable entry should preserve enough metadata to recover:

- source unit and Japanese part identity;
- focalizer or asserting source position when material;
- evidence class (`DIRECT`, `CORROBORATED INFERENCE`, `INTERPRETIVE HYPOTHESIS`, or `OPEN / UNRESOLVED`);
- current formulation;
- prior formulation when revised;
- revision state (`PRESERVE`, `STRENGTHEN`, `REVISE`, `DOWNGRADE`, `REJECT`, or `OPEN`) where applicable;
- evidence locator or route back to the deep reading/source;
- counterevidence or rival reading when material;
- temporal, identity, institutional, or information state needed to prevent hindsight collapse.

Do not duplicate scene summaries merely because they exist. Promote an observation when it changes or constrains a longitudinal model.

## 1. Character identity, state, and practical agency

**Responsibility:** preserve changes in self-concept, names/titles/roles, developmental state, bodily constraint, competence, resources, institutional position, and the actual options available to a character.

Current entries: **none — pre-V01**.

Suggested entry shape:

| Source boundary | Subject | State / transition | Evidence class | Current interpretation | Constraint / counterevidence | Evidence route |
|---|---|---|---|---|---|---|

A later state must not overwrite an earlier one merely because the mature series provides a more convenient final label.

## 2. Relationships and recipient-conditioned behavior

**Responsibility:** preserve dependence, reciprocity, trust, disclosure, secrecy, affection, obligation, contract, service, mentorship, patronage, rivalry, coercion, conflict/repair, and behavior that changes with the recipient.

Current entries: **none — pre-V01**.

Suggested entry shape:

| Source boundary | Parties / network | Relationship state | Power / information asymmetry | Change | Evidence class | Evidence route |
|---|---|---|---|---|---|---|

Do not infer one timeless relationship from later closeness, hostility, status, or knowledge.

## 3. Institutions, status, law/custom, and coercive structure

**Responsibility:** distinguish stated rules from custom, enforcement, patronage, exceptions, material resources, class barriers, information access, coercive leverage, nominal permission, and practical freedom.

Current entries: **none — pre-V01**.

Suggested entry shape:

| Source boundary | Institution / rule | Stated rule or doctrine | Observed practice | Enforcement / exception | Agency consequence | Evidence route |
|---|---|---|---|---|---|---|

Political or ethical judgment should follow reconstruction of the actual choice set rather than substitute for it.

## 4. Knowledge transfer, literacy, production, education, labor, and commerce

**Responsibility:** preserve the chain from remembered/claimed knowledge through local translation, demonstrated result, collaborators/prerequisites, and systemic consequence.

Current entries: **none — pre-V01**.

Suggested entry shape:

| Source boundary | Knowledge / process | Claimed knowledge | Local translation / collaborators | Result | Systemic consequence | Evidence route |
|---|---|---|---|---|---|---|

Credit causal contribution rather than protagonist-centered narrative salience.

## 5. World-model evidence: religion, magic/system mechanics, history, politics, economics

**Responsibility:** keep character belief, institutional doctrine, observed regularity, demonstrated exception, independent corroboration, and unresolved contradiction distinct.

Current entries: **none — pre-V01**.

Suggested entry shape:

| Source boundary | Domain | Proposition | Source position | Evidence class | Corroboration / exception | Current world-model state | Evidence route |
|---|---|---|---|---|---|---|---|

A doctrine can be socially real while its metaphysical proposition remains unproven.

## 6. Focalization, information asymmetry, and epistemic state

**Responsibility:** preserve who knows what, who believes what, what the reader knows, what is concealed or misunderstood, and how information changes available action.

Current entries: **none — pre-V01**.

Suggested entry shape:

| Source boundary | Knower / focalizer | Information state | Reliability / limitation | Disclosure or concealment change | Consequence | Evidence route |
|---|---|---|---|---|---|---|

Do not flatten multiple viewpoints into an omniscient composite narrator.

## 7. Ordinary life, bodily limits, risk, competence, and low-stakes behavior

**Responsibility:** retain mundane evidence only when it materially improves reconstruction of values, attachment, competence, self-presentation, recipient effects, state transitions, or practical agency.

Current entries: **none — pre-V01**.

Possible evidence includes food, clothing, comfort, hobbies, work rhythm, study, gifts, shopping, etiquette, humor, rest, annoyance, avoidance, sensory preference, domestic routine, and treatment of low-status or low-stakes interactions.

Suggested entry shape:

| Source boundary | Subject | Ordinary-life observation | Analytical significance | Stability / state dependence | Evidence route |
|---|---|---|---|---|---|

This section is not a trivia inventory.

## 8. Major claims, counterevidence, and revision state

**Responsibility:** preserve only claims important enough that later evidence could materially strengthen, revise, downgrade, reject, or leave open.

Current source-derived claims: **none — pre-V01**.

Suggested entry shape:

| Claim ID | First source boundary | Earlier formulation | Revision state | Current formulation | Supporting evidence | Counterevidence / rival reading | Current authority |
|---|---|---|---|---|---|---|---|

A claim's historical formulation remains discoverable even after the current model changes.

## 9. Prospective prediction and open-question register

Before V01 there is no prior Bookworm source evidence from which to make canonical predictions. The initial state therefore contains **questions, not forecasts**.

Initial prompts to test without assuming their answers include:

- how priorities and self-conception change under altered resources, roles, obligations, and agency;
- how names, titles, social position, affiliation, and identity continuity interact;
- how knowledge is translated into local practice and constrained by materials, skills, institutions, and collaborators;
- how literacy, production, labor, commerce, education, religion, law, and political authority interact as systems;
- when focalized explanations are reliable, limited, self-serving, culturally bounded, or contradicted;
- how relationships and obligations change across long time horizons;
- how bodily limits, risk, status, resources, and information asymmetry affect practical autonomy;
- how divine, religious, magical, legal, historical, or political claims divide between belief, doctrine, observation, and unresolved proposition;
- where ordinary behavior supplies stronger character evidence than explicit self-description.

After each frozen VNN, replace generic prompts with bounded predictions/open questions derived only from the source state then available.

Suggested entry shape:

| Entering boundary | Question / prediction | Confidence | Basis at entering boundary | Tested by | Outcome | Historical note |
|---|---|---|---|---|---|---|

## 10. Dedicated-ledger split rule

Split a responsibility out of this file when at least one of the following becomes true:

- entries are numerous enough that independent retrieval is materially faster or safer;
- the dimension has its own revision cadence or evidence schema;
- several character/specialist artifacts depend on it directly;
- maintaining it inside the master file causes duplicated reconstruction work;
- the dimension needs an independent audit, locator index, or high-water mark.

Likely—but not guaranteed—future splits include character/state, relationships, institutions/agency, knowledge-production/economy, world-model/religion-magic, information state, ordinary life/body, and claim revision.

Do not split for cosmetic symmetry or because another series uses that ledger.

## 11. Part-boundary reconciliation

At V03, V07, V12, V21, and V33:

1. reconcile all entries through the just-frozen part boundary;
2. adjudicate material predictions and claims;
3. identify unresolved contradictions;
4. check whether a responsibility should split or merge;
5. identify character/relationship promotion candidates without enrolling them automatically;
6. identify specialist responsibilities that have become warranted;
7. record any required architecture amendment in `../CURRENT_STATE_AND_CORPUS_MAP.md`.

The first mandatory review occurs after V03 unless an earlier volume exposes a material architecture gap.

## 12. Freeze and mutability behavior

This ledger is mutable current state. Frozen deep readings preserve their historical source boundaries. Updating this ledger may revise the **current** interpretation but must not rewrite the earlier deep-reading record or pretend later knowledge was available prospectively.

If a responsibility later splits into a dedicated canonical ledger, this file should retain a compact routing note and cease duplicating that responsibility's detailed current state.
