---
title: "Kamakura Police Station — character reconstruction specification"
series: "Kamakura Police Station: The Case Files of Asumi Ogasawara / 鎌倉署・小笠原亜澄の事件簿"
series_id: kamakura-sho
artifact_id: KSOA_CHARACTER_RECONSTRUCTION_SPEC
artifact_type: character_reconstruction_specification
generation: KSOA-G1
version: "1.0"
created: "2026-11-12"
status: canonical
scope: "Evidence requirements and validation design for future character and dialogue reconstruction."
source_boundary: "Japanese publisher EPUBs V01–V07. Bibliography, bytes and package structure reconciled. Narrative admission and inspection are pending."
canonical_home: series/kamakura-sho/KSOA_CHARACTER_RECONSTRUCTION_SPEC.md
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
do_not_use_as_literary_evidence: true
recommended_reasoning_class: DEEP_SYNTHESIS
---

# Character reconstruction specification

Use the [generic reconstruction method](../../governance/analytical-methods/GENERIC_CHARACTER_RECONSTRUCTION_METHOD.md) for derived work on recurring or case-local characters. The [literary method](KSOA_ANALYTICAL_METHOD.md) and [claim revision ledger](KSOA_CLAIM_REVISION_LEDGER.md) retain authority over interpretations. A reconstruction supports a scoped account of how a character appraises a situation and chooses among plausible responses. Its intended uses include monographs, conditional behavior and dialogue, directed interpersonal interaction, professional decisions, and clearly qualified counterfactual or cross-series scenarios. No subject has been assessed at bootstrap.

## Scope and evidence

Bind each candidate to an exact subject and continuity, witness set, admitted source boundary, basis commit, generation, model version, story-time state, reader evidence horizon, and the character's own knowledge and access at that point. Name excluded witnesses, evidence the author has already seen and missing evidence channels. If a later disclosure supports a revised account of the earlier person, label that evidence basis retrospective. A model at that earlier story time can act only on information available to that person then. Preserve earlier, more limited reconstructions as distinct versions with their own evidence horizons.

Build a model evidence map using stable source and state anchors in the [character and relationship ledger](KSOA_CHARACTER_AND_RELATIONSHIP_LEDGER.md), [case evidence ledger](KSOA_CASE_EVIDENCE_LEDGER.md), [disclosure ledger](KSOA_DISCLOSURE_AND_HYPOTHESIS_LEDGER.md) and accepted volume readings. Each input records the exact locator, evidence class, situation, interlocutor/audience, institutional role, subject state, and basis for its permitted use.

| Evidence route | Application |
|---|---|
| Observed conduct | Acts, choices and consequences, with opportunity, pressures, and actual options |
| Narrated interiority | Explicit access, focalizer, thought or affect, and what the character expresses or withholds |
| Dialogue and linguistic register | Japanese speaker and addressee, scene and speech act, address and self-reference, honorifics, politeness, sentence endings, indirectness and register shifts |
| Reports and institutional claims | Who attributes the conduct, role or duty, their access and possible interest, and independent corroboration |
| Context and relationships | Professional authority, duty, resources, social pressure, relative knowledge and directed history with the interlocutor |
| Stable and contingent tendencies | Recurrence across credible opportunities, role or stress alternatives, valid intervals and whether a change occurred or an earlier condition was revealed |
| Conflict, limits and uncertainty | Disconfirming observations, rivals, evidence-backed limitations, gaps and conditions for abstention |
| Character knowledge | Subject-specific disclosures, belief/error, transmission and event time, with the reader's confirmation horizon recorded independently |

Sample ordinary scenes, professional routine, asymmetric interpersonal situations and pressure where available. The source may support a narrow decision or interaction for a case-local character and leave private motivation, ordinary behavior or voice largely open. Mark the limits for each intended use. A missing opportunity is a coverage gap. A negative constraint needs affirmative evidence or a genuinely diagnostic opportunity.

## Model and uses

Keep the literary monograph, evidence crosswalk, operational model and test records distinct in responsibility. State any proposed policy as trigger, perceived stakes and options, relevant role and relationship, response family, inhibitors, alternatives, counterevidence and failure condition. Give the rule a scoped confidence (high, moderate, low or open) and an attested, close-variant, novel in-world or cross-scenario distance. Confidence ordinarily decreases with distance. Preserve reasons for declining a prediction.

For dialogue, work from objective and speech act to interlocutor-conditioned register and wording. Include Japanese coverage across relevant interlocutors and contexts, with samples that test what would sound wrong, and judge the decision to speak separately from fidelity of expression. Preserve ruby, punctuation and context where meaningful. Where the source presents thought and speech separately, require independent grounds for making an internal judgment audible. A cross-scenario contract states assumed chronology, setting, interlocutor relationship, authority, facts available to the character and which novel conditions are altered. Carry source-bounded role constraints into professional scenarios. Generated dialogue, scenes and predicted choices remain synthetic records outside the literary evidence set.

## Interpretive readiness and operational validation

A future interpretive readiness review tests whether the source coverage and counterevidence can support a specified reconstruction purpose and state. It checks locators, stability versus contingency, uncertainty, ordinary and pressured behavior, interpersonal direction and sufficient original-language dialogue for the claimed range. A credible monograph or well-supported hypothesis may inform this decision. Operational validation requires a distinct authorized test and result. This specification records neither a readiness judgment nor a capability tier.

1. **Freeze the basis and test plan.** Pin candidate model version, exact evidence, temporal/state boundary, intended scenario and qualitative acceptance criteria. An independent custodian withholds genuinely unexposed passages or units with diagnostic opportunities, including routine and pressure contexts and relevant dialogue or relationships. Freeze rules, predicted response families, alternatives, confidence, disconfirmers and expected abstentions at the permitted knowledge horizon before releasing the test material. Record exposure and input boundaries for the producer and reviewer. Reserve further held-out material for any later retest.
2. **Run scoped tests.** Compare the frozen predictions with verified Japanese passages and the exact information available to the subject. Include perturbations of role, available evidence or interlocutor, plausible decoys, abstention controls and a generic-profile baseline where they can discriminate. Treat already seen passages as retrospective replay. Label noncanonical probes and use them to test consistency and bounds. Their outcomes carry no new canon facts.
3. **Adjudicate independently.** Preserve the original predictions. Record diagnostic opportunity, source locator, supported/partly supported/contradicted/confounded/unresolved outcome or absence of opportunity, and reviewer rationale. Evaluate action and appraisal, factual knowledge, context/relationship fit, and speech-act and Japanese register fidelity separately. Report the number of opportunities and exclusions by context, and calibrate confidence against disconfirmations. Avoid percentages from small or selected samples. Compare the candidate with simple baselines and credit meaningful abstention.
4. **Narrow or fail unsupported uses.** Later-knowledge leakage, invented evidence or interiority, unsupported role powers, untraceable or materially misquoted evidence, systematic register or interlocutor mismatch, and a rule compatible with any outcome require correction or a narrower boundary. Lack of independent diagnostic material leaves operational validation pending for that use. A retrospective fit or fluent output can support further review. Reserve promotion for evidence-supported rules that survive the applicable tests. Save new versions and their retest results with the original failures.

## Evaluator handoff

Provide evidence routes for the twelve controlled dimensions. Appraisal and decision rules support `PSYCHOLOGICAL_MODEL`. Dated states and their causes support `LONGITUDINAL_STATE` and `TEMPORAL_SPECIFICITY`. Japanese samples support `VOICE_REGISTER`. Ordinary scenes and directed edges support `MUNDANE_BEHAVIOR` and `RELATIONSHIP_CONDITIONING`. Explicit thought routes support `INTERIORITY`. Diagnostic choices supply `CONFLICT_BEHAVIOR`, `ETHICAL_DELIBERATION` and `HUMOR_PLAY` where evidenced. Coverage and opportunity records support `SOURCE_COMPLETENESS` and `NEGATIVE_EVIDENCE`.

For `DIALOGUE`, `CROSS_SCENARIO`, `MUNDANE_SOCIAL`, `ETHICAL_DELIBERATION`, `ROMANCE_RELATIONSHIP` and `PROFESSIONAL_CONTEXT`, report purpose-specific evidence, limits and test results where authorized. Romantic or other relationship scenarios require evidence appropriate to that specific directed relationship and time. Use stable path/heading anchors and current-eligible artifacts with complete authority metadata. The designated discovery agent owns reviewed evidence enrollment. The designated evaluator uses exact reviewed discovery references for the same subject and a commit-bound evidence set, and maintains any global candidate assessments under its own policy. Human review and effective currentness are governed there. Bootstrap adds no character models, simulations, monographs or assessment records. See the [capability specification](../../characters/RECONSTRUCTION_CAPABILITY_SPEC.md) and [evaluator policy](../../governance/policies/CHARACTER_RECONSTRUCTION_MAINTENANCE.md).
