---
title: Character monographs — Binding amendment to the COTE synthesis architecture
series: Classroom of the Elite
artifact_type: synthesis_architecture
version: '1.0'
status: canonical
authority_state: canonical
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
incorporated_document: COTE_Multi_Document_Synthesis_Architecture_v1.md
incorporated_version: '1.1'
incorporated_sha256: 9fc0acd1b11d03a590e40db1a1d8d6a90f738787894b081d7dfc0f3a711347e0
content_amendment: true
amendment_scope: Mandatory individual monographs for characters with sufficient evidence
adoption_boundary: Y3V01
applies_to: Existing completed corpus and subsequent authorized analysis
created_at: '2026-09-12'
---

# Character monographs — Binding architectural amendment

## 1. Requirement and authority

**Every character with sufficient evidence must receive a substantial individual monograph integrating personal history, personality, behavior, written speech, and preferences, with an operational profile that supports bounded modeling of that person.** This requirement applies to supporting characters and adults as well as protagonists and class leaders. Narrative prominence, popularity, and membership in an existing specialist chapter do not determine eligibility.

This amendment adopts the **complete** [synthesis architecture v1.1](COTE_Multi_Document_Synthesis_Architecture_v1.md), at the hash recorded above, and adds the monograph responsibility to its ledger, specialist, primary-home, evidence, and behavioral-reconstruction provisions. The complete base architecture governs wherever this amendment is silent. Where its existing allocation of a character's primary home would leave the integrated personal portrait optional or dispersed, this amendment governs that responsibility. It does not displace source-local evidence, year-boundary judgments, or specialist arguments about relationships, ethics, institutions, and class polities.

The [current series map](../COTE_CURRENT_STATE_AND_CORPUS_MAP.md) binds the base architecture and this amendment together. The [Year 3 analytical method](COTE_Y3_ANALYTICAL_METHOD_V2.md), through its [typed adoption](../04%20Year%203%20Rolling%20Second%20Pass/00%20Corpus%20Administration/COTE_Y3_ANALYTICAL_METHOD_ADOPTION.md), continues to govern reading. This addition is effective from the completed Y3V01 boundary. It creates a new corpus responsibility using existing evidence; it does not retroactively invalidate completed Year 1, Year 2, or Y3V01 releases, reopen their frozen files, or authorize reading another source unit.

## 2. What counts as sufficient evidence

Qualification asks whether the completed corpus supports a coherent, individualized account of the person, their known formation or trajectory, and the conditions under which their behavior varies. It requires more than a role description, a memorable scene, a trait attributed by another character, or a collection of isolated facts. The assessment must identify convergent evidence, meaningful contextual or relational variation, and constraints or counterexamples that prevent a generic personality sketch.

There is no fixed quota of pages, appearances, volumes, or quotations. Repeated appearances can remain shallow; a concentrated sequence may establish a supporting character deeply. Direct interior access is valuable but not compulsory when behavior and context strongly constrain interpretation. A claimed motive remains an inference unless the evidence warrants stronger wording, and an unreliable self-report is evidence about self-presentation as well as possible motive.

Use the evidence-envelope vocabulary already defined by the [behavioral reconstruction protocol](COTE_BEHAVIORAL_RECONSTRUCTION_PROTOCOL_THROUGH_Y2.md). Record a brief source-grounded rationale for the assessment, rather than converting these dimensions into a numerical personality score:

| Evidence dimension | Existing vocabulary |
|---|---|
| Behavioral breadth | `robust`, `narrow_diagnostic`, `role_limited`, `trace` |
| Temporal continuity | `robust`, `present`, `local_only`, `absent` |
| Relationship coverage | `diverse`, `specific_deep`, `specific_thin`, `absent` |
| Motive access | `direct`, `strongly_inferred`, `role_inferred`, `absent` |
| Ordinary-life coverage | `robust`, `present`, `trace`, `absent` |
| Stress coverage | `robust`, `present`, `singular`, `absent` |
| Written-voice coverage | `A`, `A_B`, `B`, `C`, `unprofiled` |
| Negative constraints | `strong`, `some`, `weak` |

The rationale must explain why the combination supports an individual monograph, including its largest gaps. No single label automatically qualifies a character. Role-limited action and role-inferred motives alone are insufficient. A narrow diagnostic sequence may support a bounded reconstruction case without yet supporting a substantial monograph.

Qualification does **not** require a complete childhood biography, exhaustive preferences, or equally rich speech evidence. A well-supported account of known history and behavior can qualify while voice, early life, or ordinary tastes remain sparsely documented. Each required domain must still be addressed: state what is known, what can be inferred, and what remains unknown. Never fill missing life periods or preferences to make the document appear complete. A preference inferred from one situational choice must retain that limitation.

Monograph eligibility and reconstruction permission are separate decisions. Rich biography does not establish voice fidelity; extensive dialogue does not establish behavior outside the depicted situation. Domain readiness must therefore remain visible within the monograph and in any downstream modeling use.

## 3. Qualification creates a production obligation

The initial eligibility review must consider the existing completed corpus, including qualifying secondary characters, rather than wait for the series to finish. Later reviews occur when new analysis materially changes a character's history, behavior, relations, speech evidence, or prior qualification judgment. Use existing character and voice ledgers to find candidates, but do not treat absence from a dedicated ledger as disqualification.

At the first substantive eligibility review, create a local monograph index with one concise record per assessed character: stable identity, assessment boundary, outcome, supporting evidence and rationale, domain gaps, next review trigger, and the monograph path when a real document exists. Do not create an empty index or placeholder portraits to simulate progress. An unassessed character is neither qualified nor rejected.

| Recorded outcome | Meaning and required action |
|---|---|
| `QUALIFIED_PENDING` | Evidence supports a monograph; production is required and remains outstanding. |
| `COMPLETE_AT_BOUNDARY` | The substantive monograph meets this amendment at its declared boundary and has been reviewed. |
| `DEFERRED_EVIDENCE` | Current evidence does not support a substantial portrait; record the specific deficiency and reassessment trigger. |
| `REASSESS_AFTER_REVISION` | A material new finding challenges eligibility, coverage, or the current portrait; retain the prior assessment and resolve the change. |

Qualifying monographs are mandatory work in the applicable character/synthesis production tranche, not optional enrichment. A bounded task may leave explicitly recorded pending work, but the monograph layer cannot be declared complete while any qualifying character remains without the required document. Review scheduling must not silently restrict the guarantee to leads. Qualification is an analytical judgment with stated evidence, not an additional human approval gate.

This adoption establishes the responsibility; it does not claim that the eligibility sweep or the monographs have already been completed. Actual population is a subsequent substantive operation using authorized source boundaries. Repository publication and further sequential reading retain their separate authorization boundaries.

## 4. Required monograph coverage

The result must be a readable, detailed portrait with an integrated argument about the person. Tables, timelines, compact profiles, and retrieval links support that account. They do not replace it. Length follows the evidence and complexity; avoid padding with repeated plot summaries or substituting a personality card for sustained analysis.

Each monograph must cover the following responsibilities. Closely related sections may be combined when their distinctions remain recoverable.

1. **Identity and portrait.** Names and aliases, stable character identity, source/spoiler boundary, current situation, a concise account of the person, and the principal evidence strengths and limits.
2. **Known personal history.** Family and background, formative experiences, pre-school history where known, entry conditions, and the sequence of relevant school events and relationships. Distinguish when an event happened, when the reader learned it, and what the character knew at a particular time. Mark undocumented periods explicitly.
3. **Development and revelation.** Explain continuity and change across the available chronology: learned capacities, revised goals, attachments, losses, compromises, and setbacks. Separate a new fact about an earlier self from actual development. Preserve earlier-boundary interpretations alongside later revisions where that history matters.
4. **Personality organization.** Self-conception, values, recurrent motives, fears, vulnerabilities, coping and defensive strategies, aspirations, tensions, and contradictions. Separate self-description, others' interpretations, narrator framing, and demonstrated choices. Prefer explanatory patterns to unsupported diagnostic or typological labels.
5. **Behavior and decisions.** What the character notices, prioritizes, attempts, withholds, refuses, and repairs under different conditions. Include ordinary interaction, cooperation, conflict, uncertainty, stress, failure, and recovery where evidenced. State mechanisms, exceptions, costs, and counterconditions rather than absolute trait rules.
6. **Preferences and ordinary life.** Supported likes, dislikes, tastes, hobbies, habits, routines, comforts, aversions, and preferred social conditions. Distinguish stable preference, temporary desire, instrumental choice, situational accommodation, and attachment to a particular person. Include negative evidence and unknowns without extrapolating a complete lifestyle.
7. **Relationships.** Explain directed differences in trust, attachment, disclosure, dependency, rivalry, obligation, consent, and power. State what changes with the interlocutor and shared history. Do not generalize an intimate dyad into behavior toward everyone, or treat affection as proof of informed consent.
8. **Abilities and constraints.** Demonstrated capabilities, development, limits, withholding, incentives, institutional position, and gaps between public reputation and private competence. A capacity is not evidence of willingness to use it in every setting.
9. **Written speech and interior voice.** Japanese pronouns and address forms, register, sentence patterns where diagnostic, politeness, directness, humor, evasion, silence, audience effects, and shifts under pressure. Distinguish internal narration from outward speech and originals from translation choices. Use the existing language keys and evidence tiers; prose does not establish acoustic delivery or an actor's performance.
10. **Embodied presentation.** Relevant movement, expression, appearance, bodily habits, and visual framing, with distinctions between narrated action, illustration, and interpretation. Include only what contributes to the personal portrait or grounded reconstruction.
11. **Operational model.** A compact, evidence-linked account of attention, goals, beliefs and knowledge, protected interests, concealment, decision tendencies, relational modifiers, likely response families, and refusal limits. For each major tendency, state the triggering conditions, alternative outcomes or counterconditions, support level, and uncertainty. Select behavior before rendering speech.
12. **Limits and competing readings.** The strongest plausible alternative interpretation, disconfirming evidence, unresolved questions, and contexts where the model should abstain. No psychological portrait is exhaustive simply because all headings are filled.
13. **Evidence and navigation.** Reproducible source locators for substantive claims and links to the relevant volume readings, ledger entries, language/visual keys, and specialist homes. A locator router supplements the portrait; it must not defer the portrait itself to other files.

## 5. Primary homes and storage

The monograph becomes the primary home for the **integrated person-level history, portrait, and operational profile**. Existing character ledgers remain the primary chronological and rolling evidence record. Source-local readings retain their local arguments and observations. Relationship, polity, institutional, ethical, and thematic specialists retain their respective questions; a monograph explains their consequences for this person and links to the fuller specialist argument.

This allocation extends the base architecture's primary-home and anti-duplication rules. Reuse evidence to answer distinct questions, but do not reproduce entire scenes or specialist essays in multiple homes. A reader must find a self-contained portrait without having to assemble it from ledgers, while still being able to verify its evidence and explore the other analytical questions.

New standalone monographs belong in `05 Character Monographs/` under the COTE series root. The prospective filename convention is `COTE_CHAR_MONOGRAPH_<CHARACTER_ID>_THROUGH_<BOUNDARY>.md`, using a stable identity token rather than a changing class label or office. Create this directory and its index when substantive assessment or monograph work begins. No empty artifacts are required at adoption.

A future dedicated character study may also fulfill the monograph responsibility if it satisfies every required domain and the local index identifies one canonical portrait path. Do not maintain competing current full portraits for the same character and boundary. Existing frozen studies retain their original responsibilities and bytes; later monographs link to them and declare the distinct integrated scope. Reserve `FINAL` for an actually completed relevant corpus, not the current Year 3 checkpoint.

## 6. Modeling and simulation use

The monograph provides organized inputs for the existing reconstruction protocol. It must distinguish observed behavior from the model's proposed generalization using that protocol's support classes: `DEMONSTRATED`, `STRONG_GENERALIZATION`, `BOUNDED_EXTRAPOLATION`, and `SPECULATIVE`. Scenario permission remains independently assessed as `PORTABLE_BOUNDED`, `CONTEXT_ANCHORED`, `STRUCTURAL_ONLY`, or `ABSTAIN_CHARACTER_SPECIFIC`; a monograph is not a universal permission to simulate the person in arbitrary contexts.

For an admissible scenario, bind the character's knowledge and development to the selected time, identify the relationship and setting, choose a supported action family, and only then apply the independently supported voice profile. Give bounded alternatives when the evidence underdetermines a choice. A generated scene, line, or reaction is a reconstruction and must never enter the canonical evidence ledger as something the character actually did. Avoid false precision in predicted preferences or decisions.

The existing through-Year-2 reconstruction protocol remains frozen at **Y2SL**. A monograph through Y3V01 may summarize later analytical evidence and explain its consequences for the operational profile, but this does not extend the protocol's calibration boundary or validate Year 3 simulations. A later protocol extension must explicitly bind the new boundary and evidence before claiming such calibration. Existing retrospective cases do not become prospective prediction/observation pairs; real prospective validation requires freezing a prediction before the later source is read.

## 7. Metadata, maintenance, and review

Actual monographs use `artifact_type: character_monograph` and the repository's complete authority metadata. Record version, stable identity and aliases, source codes, source/spoiler boundary, governing method and architecture, domain evidence readiness, related primary homes, and predecessor/successor relations when applicable. Distinguish replacement for current lookup from continuing historical authority. This amendment adds no executable schema or new numerical scoring system.

When later evidence materially changes a portrait, preserve the earlier boundary and issue an appropriately bounded successor with a concise change account. New history, revised motive, altered relationships, and speech changes require different explanations; do not flatten them into a generic update. The local index records the actual current home and unresolved production obligations. Global character discovery remains governed by the repository's existing curation policy.

Production proceeds from completed readings and ledgers to an evidence-based qualification assessment, then to the narrative portrait and operational profile. Recheck primary passages where the new synthesis depends on contested history, motive, preference, or Japanese voice. Review contradictions, uncertainty, temporal boundaries, evidence locators, ownership of claims, and links before marking a monograph complete. Apply the repository's required author preflight and proportionate document checks; ordinary monograph authoring does not itself require new validation software or an additional software test suite.
