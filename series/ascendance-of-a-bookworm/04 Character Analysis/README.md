---
series: ASCENDANCE_OF_A_BOOKWORM
artifact_type: character_analysis_router
scope: CHARACTER_ANALYSIS
generation: V0.4
status: canonical
release_state: mutable_active
architecture_lifecycle: INITIAL
current_source_boundary: V03_PART_1_COMPLETE
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
---

# Ascendance of a Bookworm character-analysis router

This directory is the canonical future home for Bookworm character-specific analysis. At the completed V03 / Part 1 boundary, the first mandatory promotion review has identified **Myne and Lutz as evidence-earned character-monograph responsibilities**, but those monographs are not instantiated by the V03 source-unit transaction itself. Promotion should create a substantive analytical object when a later operation actually needs the independent retrieval surface, not an empty or shallow placeholder.

Global character discovery remains separate. The designated character curation agent, not this analytical authoring session, owns enrollment in `characters/registry.jsonl` and maintenance of `CHARACTER_ANALYSIS_INDEX.md`.

Do not create a character directory merely because a person appears in the source, an adaptation, a cast list, a synopsis, model memory, or general franchise knowledge.

## Promotion path

Character evidence normally develops through this route:

```text
numbered-volume deep reading
        |
        v
master longitudinal ledger
        |
        v
sufficient multi-state / multi-context evidence?
        |
       yes
        v
04 Character Analysis/<Character>/
        |
        v
reviewed substantial current analysis
        |
        v
separate global discovery review by the designated curation agent
```

Local character analysis and global character discovery are distinct decisions.

## When a character earns an independent canonical home

Create `04 Character Analysis/<Character>/` only when source-grounded longitudinal evidence gives the character an independent retrieval/revision responsibility. Useful triggers include several of the following:

- meaningful evidence across multiple volumes or developmental states;
- a need to separate stable tendencies from role effects, recipient effects, situational effects, or genuine development;
- identity/name/title/status or information-state transitions too complex for master-ledger-only retrieval;
- contradictions, unreliable self-report, or self-conception/social-effect gaps requiring independent adjudication;
- relationships or network position that materially alter behavior and agency;
- ordinary-life evidence that changes the model rather than merely adding trivia;
- speech/register, forms of address, rhetoric, or focalized narration that require independent treatment;
- dependence by multiple specialist syntheses;
- repeated reconstruction cost for simulation/modeling or cross-series work.

Narrative prominence alone is not a promotion criterion.

## Part 1 promotion review

The mandatory V03 checkpoint is recorded in `../05 Specialist Synthesis/BOOKWORM_PART1_BOUNDARY_SYNTHESIS.md`.

### Myne — `WARRANTED_NOT_INSTANTIATED`

Part 1 now supplies independent character-model responsibility across:

- Urano/Myne identity and unresolved ontology;
- genuine value development from book-dominant attachment toward family/self-authorship constraints;
- chronic physical frailty versus mana/`身食い` state;
- household, commercial, workshop, and temple role transitions;
- self-conception versus external valuation;
- recipient-conditioned disclosure and behavior;
- dangerous mana control and practical agency;
- multiple downstream specialist dependencies.

A future substantive Myne monograph is therefore warranted when requested or when a downstream synthesis needs it.

### Lutz — `WARRANTED_NOT_INSTANTIATED`

Part 1 now supplies independent character-model responsibility across:

- self-authored merchant aspiration;
- family opposition and emerging maternal alliance;
- paid labor and personal resource accumulation;
- formal apprenticeship and cross-class occupational acculturation;
- independent focalization;
- literacy/merchant competence development;
- privileged Urano identity knowledge;
- changing but durable Myne relationship.

A future substantive Lutz monograph is therefore warranted when requested or required by downstream synthesis.

### Benno — `MONITOR`

Benno has substantial evidence across commercial mentorship, protection, extraction, family/business history, risk control, and revived ambition. Part 1 is sufficient to make him a strong promotion candidate, but the current checkpoint can still retrieve his model without forcing an immediate monograph.

### Frieda — `MONITOR`

Frieda has significant evidence as a `身食い` comparison, friend/competitor, commercial actor, and person preparing for constrained noble entry. More multi-state evidence is desirable before treating a dedicated monograph as mandatory.

No other Part 1 character earns an immediate local monograph solely by prominence.

## Potential artifact responsibilities

Instantiate only what the character actually needs:

- `<CHARACTER>_CURRENT_STATE.md` — router when a character has multiple active artifacts or a changing source boundary;
- `<CHARACTER>_CHARACTER_MONOGRAPH.md` — canonical integrated character interpretation;
- `<CHARACTER>_IDENTITY_AND_STATE_LEDGER.md` — names, titles, roles, developmental states, institutional status, bodily state, or information state;
- `<CHARACTER>_RELATIONSHIP_AND_NETWORK_PROFILE.md` — recipient-conditioned behavior and changing network position;
- `<CHARACTER>_ORDINARY_LIFE_AND_PREFERENCES_PROFILE.md` — mundane behavioral evidence that materially improves reconstruction;
- `<CHARACTER>_SPEECH_AND_REGISTER_PROFILE.md` — diction, terms of address, title use, social register, rhetoric, or focalized narration;
- claim/counterevidence, fidelity, ethical, or reconstructive-model artifacts — only when the character-modeling problem is dense enough to justify an independent home.

Do not create the full menu for every character.

## Minimum monograph contract

A mature monograph should, as evidence permits:

- declare its exact source boundary;
- distinguish stable tendency from developmental state, role effect, recipient effect, situational effect, and genuine revision;
- preserve identity/name/title/status transitions without flattening earlier states into a final label;
- integrate contradictory evidence and meaningful rival readings;
- separate self-description from observed behavior and social effect;
- reconstruct practical agency from real options, constraints, information, resources, and coercive leverage;
- integrate relationship-conditioned behavior rather than infer one context-free personality;
- use ordinary-life evidence where it materially constrains the model;
- preserve wording/register evidence when Japanese language is interpretively load-bearing;
- state abstention boundaries and unresolved questions;
- route major evidence back through deep readings, the longitudinal layer, or promoted indexes.

A monograph is not a wiki biography, trait list, or compilation of flattering/condemning moments.

## Relationship specialization

A relationship does not automatically need its own file because it is important. Keep dyadic/network evidence in the master ledger or relevant character monographs until the relationship itself has recurring state, independent revision needs, or multiple downstream consumers that justify a specialist synthesis.

The V03 Part 1 review finds one current relationship that has crossed that threshold:

- **Myne ↔ Lutz — `WARRANTED_NOT_INSTANTIATED`**.

The relationship now carries independent longitudinal state across identity disclosure, bodily care, production, commercial rights, occupational development, future-separation risk, and explicit mutual commitments. A future relationship synthesis should remain source-boundary explicit and must not promote romance beyond what the covered evidence supports.

## Global character discovery boundary

Enrollment in `characters/registry.jsonl` and maintenance of the generated `CHARACTER_ANALYSIS_INDEX.md` belong solely to the repository's designated character curation agent under `governance/policies/CHARACTER_DISCOVERY_MAINTENANCE.md`. Analytical authoring sessions do not independently curate either global character output and do not create or maintain series-local character-upsert files to drive enrollment.

A Bookworm subject should not be enrolled merely because:

- the character appears frequently;
- a local folder exists;
- a deep reading contains several observations;
- a future monograph is planned;
- the character is prominent in adaptations or fandom.

Qualifying new Bookworm analysis may merge before global enrollment when existing character references and the generated index remain valid. The curation agent may then discover eligible additions from `main` and independently verify identity, dimensions, anchors, and coverage against the merged evidence.

If a future Bookworm edit changes evidence already referenced by an existing curated character record and invalidates a path, anchor, authority relationship, coverage claim, or generated output, integration must wait for a coordinated curation-agent repair against the exact proposed source branch and commit. Do not weaken validation or assume a later routine curation run will repair an invalid merge.

At the V03 / Part 1 boundary, this analytical session makes **no global character-registry or generated-index write**.

## PACTRIH and comparative modeling

PACTRIH scoring, cross-series comparison, behavioral simulation, and other higher-order character modeling are downstream. They require a source-grounded Bookworm character model first and must preserve state dependence, uncertainty, and the distinction between descriptive reconstruction and normative judgment.