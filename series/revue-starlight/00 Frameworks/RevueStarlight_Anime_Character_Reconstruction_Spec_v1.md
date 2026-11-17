---
title: "Revue Starlight Anime Character Reconstruction Specification"
artifact_id: REVUE_STARLIGHT_ANIME_CHARACTER_RECONSTRUCTION_SPEC
artifact_type: character_reconstruction_specification
series_id: revue-starlight
version: "1.0"
status: canonical
authority_scope: project_local_anime_character_reconstruction_method
scope: "Evidence, state, conditional behavior, Japanese voice, and validation for animated-continuity reconstruction"
canonical_home: "series/revue-starlight/00 Frameworks/RevueStarlight_Anime_Character_Reconstruction_Spec_v1.md"
source_boundary: "TV01–TV12, OVA01–OVA03, and the complete 2021 sequel film, including narrative credits and post-credit material"
governing_reference: governance/analytical-methods/GENERIC_CHARACTER_RECONSTRUCTION_METHOD.md
governing_reference_version: "1.0"
drafted_against_commit: 46c341663e7e0b78d75fe9e2b3dc6e83859f85db
created: "2026-11-11"
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
do_not_use_as_literary_evidence: true
---

# Revue Starlight Anime Character Reconstruction Specification

## 1. Responsibility and route

Use this specification to predict what a specified character at a specified narrative state is likely to notice, choose, say, do, or avoid, given the character's information, relationships, and situation. Every prediction must identify its supporting evidence, its alternatives and limits, and the conditions under which it can be tested.

This project-local specification adopts the [Generic Character Reconstruction Method, v1.0](../../../governance/analytical-methods/GENERIC_CHARACTER_RECONSTRUCTION_METHOD.md). Enter through the [registered corpus guide](../05%20Full-Series%20Synthesis/00_README_AND_CORPUS_MAP.md). The [synthesis architecture](RevueStarlight_Multi_Document_Synthesis_Architecture_v1.md) and [full-series analytical method](RevueStarlight_Full_Series_Analytical_Method_v1.md) govern literary interpretation and its primary homes. Use the [musical-dramaturgy method](RevueStarlightAnalyticalMethod_MusicalDramaturgy_v2.md) and [film method](RevueStarlightMovieAnalyticalMethod_v1.md) for the underlying audiovisual evidence. The final release's [manifest](../07%20Audits%20and%20Manifests/CORPUS_MANIFEST.md) records the checksum-bound guide and architecture. A forward pointer from project routing to this addendum requires separate review under the [frozen-release routing rules](../../../governance/AGENT_ROUTING.md#84-frozen-release-administrative-maintenance).

A character or relationship synthesis supplies literary interpretations, contradictions, and retrieval routes. A reconstruction policy is a new, testable claim derived from admitted observations. Route a dispute about the underlying interpretation through the project's claim-revision or erratum process. Record the model's dependency on that claim and narrow its use while a material dispute remains open. Generated dialogue, simulated behavior, and predictions may be test inputs or outputs. Only admitted source evidence can ground claims about the character.

## 2. Admitted sources and witness limits

The [source inventory](../01%20Source%20Lock%20and%20Inventory/SOURCE_INVENTORY.md) governs the source boundary and records the available witnesses for the published synthesis.

| Source | Eligible evidence and limits |
|---|---|
| Television `TV01`–`TV12` | The Japanese-original episodes. The inventory records complete Japanese audio, corrected Japanese subtitle/dialogue layers, and retained visual material. Use the audio for delivery and timing, the checked Japanese text for wording, and the inspected visual channel at its actual resolution. |
| `OVA01`–`OVA03` | Supplementary character and social evidence. The inventory records complete Japanese audio and dense visual material with **English subtitles only**. Retain that limitation until an eligible local Japanese witness is verified and recorded. Use the audio-recovery procedure in Section 6 for any exact wording derived from listening. |
| 2021 theatrical sequel | The complete Japanese-original film, including narratively relevant credits and post-credit material. The recorded Japanese ASS/dialogue layer is an analysis-oriented transcription and retrieval aid. Verify load-bearing language against the Japanese source. Use `MOV-PRO`, `MOV-M01`–`MOV-M08`, and `MOV-EPI` as analytical locator codes. Pair each code with the actual film interval or cue and identify whether it is in the credits or post-credit material when relevant. |

The inventory describes working witnesses. For any new inspection, bind the particular edition or cut, tracks, derivative and parent relationship, and citation clock to a recoverable source identity, using a governed alias or digest and a safe provenance reference. Where edition identifiers are unavailable, record the gap. Verify equivalence and clock offsets before transferring a locator between copies. Record material divergences and obtain separate source authorization if a different cut or source unit would expand the boundary. Keep media, bulk transcripts, and private source paths in governed evidence storage.

Direct Japanese audiovisual observations and checked Japanese textual witnesses carry authority on the channels they support. The narrative portions of the film epilogue are part of the primary source. Contact sheets, indices, and previous analytical observations guide retrieval. Measurements of the final mix can corroborate specific sound claims. Recheck load-bearing observations against the governing witness where recoverable. If the necessary source or inspection channel is unavailable, retain the report as a lead and bound or withhold the affected policy.

Eligibility is confined to the listed animated corpus. Mobile-game stories, stage plays, manga and other adaptations, promotional dialogue, interviews, guidebooks, fan interpretations, and secondary summaries require separate admission. A registry media tag alone grants no source admission.

## 3. Subject, time, and character knowledge

Identify the character by the canonical anime name and bind the anime continuity and any evidenced incarnation. Use the existing discovery entity and subject IDs only when their scope matches. Leave unresolved or uncurated IDs null and use a stable project-local subject and state identifier. A compact label such as `Character@Unit` is a display label. Disambiguate it with a scene or interval when the unit contains more than one material state.

Record these boundaries separately for each model and each material observation.

- **Admitted source boundary and evidence horizon.** Identify the allowed units, the latest source unit or within-unit point used in presentation order, the basis commit, and any excluded witnesses or channels. Record the analyst's actual exposure, including prior analyses and previews, for validation.
- **Diegetic validity.** Give the state a `valid_from` and `valid_until` with source anchors or explicitly uncertain bounds. State whether the transition anchor is before or after the event. Map flashbacks, retellings, hypothetical sequences, and theatrical time separately from their presentation order.
- **Character knowledge.** For each fact relevant to prediction, record what the character perceived, was told, remembered, believed, suspected, or could reasonably infer. Cite how and when the character acquired access and distinguish belief from established world state. Preserve mistaken beliefs and unknowns. Track the same facts independently for relevant interlocutors and the audience.
- **Frame and relationship.** Identify the active role, frame, addressee or audience, and any directional relationship state that changes the predicted response. Keep temporary emotion, bodily condition, and pressure as situational changes within the state where appropriate.

Use this scheme for early TV, episode-bounded transitions, the TV12 endpoint, chronologically established OVA material, the film opening, changes within film movements, and the film ending including evidenced epilogue changes. Split states at an anchored change in knowledge, goals, relationships, role, resources, or behavior when the change affects prediction. An episode boundary alone is insufficient. Establish OVA placement per scene using in-story markers and the corpus chronology. When placement is uncertain, preserve the plausible range or leave it open. Use floating observations only for context-bound claims that hold across the supported placements.

Tag changes with the generic causes `DISPOSITION`, `KNOWLEDGE`, `RELATIONSHIP`, `CONTEXT`, `ROLE`, `RESOURCE`, `REVEALED_NOT_NEW`, or `UNRESOLVED`. A newly acquired disposition needs evidence of a transition. A late disclosure can support an earlier disposition or memory if the source places it there. Record both the earlier event and the later disclosure, explain the evidence for earlier operation or possession, and label the inference retrospective. Earlier knowledge is assessed from the character's access at that time. A later revelation to the audience is never itself an acquisition by the character. If acquisition and revelation remain competing explanations, retain both. Use earlier evidence in later states as labeled history and check its continued applicability.

Preserve any genuinely prospective snapshots at their original exposure boundaries. Put retrospective updates in a later version or linked adjudication with the earlier formulation and new evidence recoverable. Whole-film reconnaissance establishes prior exposure to the material seen during that pass even if the close reading proceeds in movement order.

## 4. Evidence map and context

Use the [episode, movement, and Revue ledger](../06%20Evidence%20and%20Indexes/14_EPISODE_MOVEMENT_AND_REVUE_EVIDENCE_LEDGER.md) for chronology and the [Japanese dialogue, lyric, and motif index](../06%20Evidence%20and%20Indexes/15_JAPANESE_DIALOGUE_LYRIC_AND_MOTIF_INDEX.md) for language retrieval. Follow the synthesis architecture to the relevant character, relationship, or specialist analysis. Cite the exact repository path and stable heading or record ID at the pinned commit. Also cite the underlying source unit and locator. When the existing corpus has no corresponding entry, record that fact. Treat multiple analyses, transcriptions, and channels of one event as traceable perspectives on the same event. Independent behavioral corroboration requires distinct opportunities.

Each material observation gets a stable ID and the following fields. Use an explicit unknown or unavailable value with its reason wherever a field cannot be resolved.

| Field | Required content |
|---|---|
| Source and provenance | Unit code, witness and track, calibrated interval and precision, and nearest stable cue, scene, or frame anchor where available. Record the clock mapping when the witness or derivative differs. If alignment is unresolved, use a reproducible same-object locator for claims independent of the mapping and queue claims that require aligned timing. |
| Attribution and state | Character and state, actor or speaker, depicted role, interlocutor or action target, witnesses or audience, and attribution confidence. Distinguish who said, knew, saw, or inferred what. |
| Situation and frame | Ordinary life or exceptional situation, social context, stakes and options observable at the time, frame and role, and any mixed or uncertain boundary. |
| Evidence and inspection | Descriptive observation, evidence class, channel and actual inspection lane, language witness and transcription status where applicable, and any resolution or access limits. |
| Interpretation and challenge | Separate inference with its supporting observation IDs, qualitative confidence and rationale, strongest counterevidence or an explicit search gap, plausible alternatives, and links to relevant corpus entries. |

Use the generic evidence classes at the claim level. `DS` is directly presented speech. `DB` is directly presented behavior. `NI` is presented interiority with the focalizer and access mode recorded. `RB` is reported behavior and `OS` is an observer, institution, or role statement. `PF` records performed voice or body within the lane's permissions. `INF` marks an inference linked to its observations. A spoken report can establish that the speaker made the report while the reported event remains `RB`. Self-report establishes an expression or self-understanding under its viewpoint and context. Record a motive as inference when the source supplies behavior, framing, or delivery alone. Retain the published corpus's labels on citations, including `AF`, `JT`, `PF`, `MF`, `FR`, `SI`, `IT`, and `SP`. They describe the cited analysis. For instance, a musical fact or formal recurrence can ground an inference while the character's intention remains open.

Record social context independently of narrative frame. Use applicable tags for ordinary conversation, routine school and social life, friendly interaction or humor, cooperation or support, competition or evaluation, conflict or confrontation, vulnerability, performance preparation, onstage performance, exceptional Revue or other heightened theater, and post-crisis recovery or changed relationship. Keep audience, privacy, and stakes visible when tags overlap. A spoken exchange inside a performance retains its frame even when it sounds conversational.

Deliberately sample routine, low-stakes scenes where available, including eligible OVAs, before proposing ordinary behavior or speech. Compare similar interlocutors and situations across frames and seek counterexamples in ordinary life as well as onstage. Record what ordinary-life coverage was examined and what was unavailable. When a pattern rests on exceptional scenes, restrict it to the evidenced circumstances until a suitable comparison supports transfer.

## 5. Roles and theatrical evidence

Record the enclosing scene, the actor or focalizer, the depicted identity, who controls the act, and what the scene establishes about their correspondence. Use the following decisions for each claim. A scene may sustain several levels at once.

| Reading of the role | Evidence needed and permitted use |
|---|---|
| Behavioral context of the same subject | The enclosing scene establishes continuity of the acting person and the activity is a social or occupational role. Use the evidence within its role conditions. |
| Deliberately performed persona | Evidence of self-presentation, acting choices, staging, or an intended audience identifies the performance. Attribute the choice to perform to the subject where agency is supported. Condition persona diction and gesture on that performance. |
| Fictional character in an embedded performance | Casting, scripting, or scene framing establishes an embedded character. Track the performer and the role separately. The role's acts and biography belong to the embedded story. Choices about playing, changing, or responding to the role may be evidence about the performer. |
| Subjective or metaphorical self | Focalization, memory, dream, metaphor, or audiovisual framing suggests a representation. Record whose viewpoint and what is depicted. Keep its significance conditional on the frame and its proposed reading. |
| Separate narrative identity | The anime establishes an independently acting person or entity with distinct agency or continuity. Cite the distinguishing evidence before assigning a separate subject. |

A Stage Girl identity, costume, voice shift, or title alone cannot decide among these readings. If attribution or ontology is materially ambiguous, retain the supported readings and their limits and abstain from conclusions that require choosing one.

For each theatrical observation, distinguish the demonstrated choice, deliberate self-presentation, enacted relationship, metaphor, and explicitly established diegetic mechanism. Where relevant, record mechanical, emotional, epistemic, relational, symbolic, and musical outcomes as separate evidence routes. Credit character knowledge only when the character has access. A score cue, camera angle, lyric, or visible transformation can establish form and support an interpretation of it. Claims about literal consequences, motivation, or everyday capacity need evidence specific to that claim.

Any policy using theatrical material must give the inferential bridge. Name the observed act, who had agency and what options were available, any script or stage constraints, the proposed mechanism, the target context, and the evidence permitting transfer. For a load-bearing transfer to ordinary life, seek independent ordinary or mainline corroboration under comparable stakes and relationships, and test an explanation based on staging or script. Without that bridge, keep the prediction within the demonstrated frame or mark transfer open. A rhyme, reprise, or repeated line requires separate evidence of causal, relational, or mnemonic continuity.

## 6. Japanese language, body, and inspection lanes

Evaluate **decision fidelity** by asking whether the character would choose this speech act given the state, goal, and audience. Evaluate **surface fidelity** by checking the Japanese register, wording, and delivery supported for that choice. Build a register matrix by state, addressee, public or private audience, and mode. Track self-reference, names and address forms, honorifics, politeness, sentence endings, discourse markers, vocabulary and recurring expressions, ellipsis, humor, support, and confrontation. Record a range of attested forms and evidence-backed traps for forms that would sound wrong. Habitual speech needs conversational evidence. Mark sung, quoted, scripted, and Revue speech separately and verify speaker or singer attribution before using it. A signature line or a lyric can support a use in its own setting.

For a load-bearing wording claim, cite the exact Japanese cue or a checked Japanese transcription and verify attribution and text against the governing source where available. A listening transcription is a derived text witness. Record its method, listening interval, verifier or checking pass, and uncertain syllables or competing readings. With Japanese audio but no Japanese transcript, preserve confidently recovered wording in a short, checked transcription anchored to the audio. Seek independent Japanese-language verification of any audio-only wording on which a policy depends. Keep unresolved lexical detail open. If the wording is unclear but delivery is audible, use only the supported delivery or independently supported semantic content. English subtitles can guide retrieval. Exact Japanese wording, grammar, or register requires Japanese evidence. Where the audio and the primary Japanese text diverge, preserve both, flag the discrepancy for text-lane review, and defer dependent claims until resolved.

For the performed layer, track directly heard delivery such as tempo, stress, pauses, overlap, breath, laughter, and silence, and visible posture, gaze and orientation, hesitation, gesture, physical approach or withdrawal, and interactional distance. Record the interlocutor, frame, what was visible or audible, and precision. A cut or a missing channel can end the observation window. Withholding a response is an inference requiring an opportunity, adequate coverage, and a basis for distinguishing withholding from other explanations.

Apply the [inspection-lane policy](../../../governance/source-policies/MANGA_ANIME_MEDIUM_AND_INSPECTION_LANE_ROUTING_POLICY.md) and the [continuous audiovisual method](../../../governance/analytical-methods/GENERIC_CONTINUOUS_AUDIOVISUAL_ANALYTICAL_METHOD.md) to every claim.

- `TEXT` supports wording and text-layer claims. `STILL_IMAGE` and visual evidence from `BUNDLE_MEDIATED` inspection support positions or expressions at inspected frames and bounded endpoint claims. Use contact sheets to locate individual frames. A sparse sequence leaves the path, micro-expression, and exact gesture timing unresolved. Listening in the bundle lane requires verified auditory inspection. Acoustic measurement can establish the measured feature within its precision.
- `CONTINUOUS_AV` requires verified synchronized audio and picture perception. Record the effective visual sampling rate or `UNKNOWN`, the clock and its calibration, and coverage gaps. Bound movement, gaze, timing, and synchronization to what the effective sampling and alignment can resolve. Re-view load-bearing observations. Corroborate unmarked attribution, exact duration, or fine synchronization through an appropriate independent channel or measurement. Route unresolved fine detail to targeted higher-resolution inspection or leave it open. Audio continuity cannot establish an unseen visual event. Score and performance can support inference about emotion, intention, or attention when the inferential steps are explicit.

## 7. Conditional model and directed relationships

Represent stable dispositions, developmental state, and situational emotion or bodily constraints as distinct layers. For each behavior domain, start with what the character can perceive and the available actions, infer appraisal and competing values with citations, and identify when a value overrides another. Keep conflicting desires and indecision available where the source supports them.

For every rule use the following structure.

> Trigger + perceived stakes and available information + subject state + directed relationship + frame → ranked response families, with inhibitors, overrides, exceptions, and abstention conditions.

Give the rule a stable ID, scope and validity interval, linked support and counterexample IDs, confidence, evidence distance, and a plausible rival explanation. State what should be less likely or ruled out within the stated bounds, and an observable result that would favor the rival or disconfirm the rule. If a rule merely fits any result, revise it until it discriminates or record the question as open.

| Status | Rule for use |
|---|---|
| `OBSERVED` | A source instance or pattern confined to one observed context. Cite it as attestation. |
| `CANDIDATE_POLICY` | Recurs across diagnostic opportunities or has explicit support for a bounded policy. State what remains to be tested. A character's own stated intention warrants checking how behavior follows it. |
| `PROMOTED_POLICY` | Recurrence and validation support the particular scope being promoted. Link the fidelity audit, discriminating tests, failures, and final bounds. A retrospective result supports only the scope it tested and carries less weight than a prospective result. Reopen the policy if a material counterexample or source revision undermines it. |

Keep a directed record for each material `A → B` inference. Record A's expectations and knowledge of B, trust or distrust, cooperation and competition, dependence, care, obligation, and speech or behavior changes with evidence and time bounds. Keep B's own record for `B → A`. Derive reciprocity from both directions and track asymmetry, differences between private and public audiences, and changes after new knowledge or relationship events. Compare behavior toward B with comparable interactions toward others. State under what supported conditions the difference disappears or reverses. A familiar pairing or a shared performance establishes neither direction by itself.

Use the generic confidence scale `HIGH`, `MODERATE`, `LOW`, `OPEN` with the basis and limiting uncertainty. Mark each prediction `D0` for attestation, `D1` for a close variant, `D2` for a novel in-world scenario within state, or `D3` for a counterfactual or substantially different setting. Confidence normally declines with distance. For `D3`, give the assumed chronology, relationships, and setting, and identify the promoted support for any retained confidence. Report plausible alternatives qualitatively.

Evidence of absence needs a real opportunity or expectation, access and available options for the character, an observable response window, and adequate lane coverage. Record a witnessed absence, contradictory behavior, a missed or unexamined opportunity, an unavailable channel, and an incompatible horizon distinctly. Give each evidence-backed limit its observation IDs. Mark unexamined or unobservable domains as gaps. If identity, continuity, a relevant relationship, knowledge, or domain support is unresolved and decisive, abstain and name the missing condition. If only surface voice is unsupported, give the bounded decision or speech act and abstain from exact Japanese wording or delivery.

## 8. Future artifacts and validation

When character modeling is separately authorized, use `series/revue-starlight/reconstruction/` as the proposed home for actual subject-state work, with stable paths or heading anchors. Resolve the subject against the single registered project entrypoint and keep the following responsibilities distinct.

| Artifact | Required content |
|---|---|
| Evidence map | Section 4 observation IDs, source locators and corpus references, ordinary and exceptional coverage, competing interpretations, counterevidence, and access gaps. Reference existing analyses at their primary homes. |
| Operational model | Subject and state IDs, version, continuity, source and temporal boundaries, exact basis commit, inspection lanes, exclusions, rules, voice features, relationship conditions, and known limits. Give every material claim links back to observation IDs and forward to relevant tests. Use the generic method's dimension and scenario crosswalk to indicate where coverage can be inspected. |
| Validation record | Exact model version and evidence basis, exposure and prediction freeze when applicable, test scenarios and expected boundaries, reviewer and method, source adjudication, disagreements, corrective action, and retests. Keep predictions recoverable independently of subsequent results. |
| Literary monograph or specialist synthesis | The existing interpretive homes in the synthesis architecture. Add new literary work only through its own authorized route. |

Use the repository's authority quartet and reciprocal supersession links for versioned artifacts. A materially revised model gets a successor with the affected rule IDs, revised evidence, and validation scope traceable. Preserve freezes and issued model versions. Record local coverage and validation status alongside the model. Only the authorized evaluator assigns capability tiers, dimension grades, or registry readiness under the [capability specification](../../../characters/RECONSTRUCTION_CAPABILITY_SPEC.md) and [maintenance policy](../../../governance/policies/CHARACTER_RECONSTRUCTION_MAINTENANCE.md).

Before offering a model for use, run these checks against its declared scope.

1. **Fidelity audit.** Recover evidence for each rule, voice feature, relationship condition, and hard limit. Check actor and audience attribution, state, locator, evidence class, and inspection-lane support. Record `PASS`, `PASS_WITH_BOUND`, `NEEDS_TARGETED_SOURCE_REVIEW`, or `INSUFFICIENT_EVIDENCE` with the reason and scope. Narrow or suspend claims whose support fails.
2. **Discriminating probes.** Give every scenario a continuity, diegetic state, evidence horizon, knowledge state, interlocutor, setting, frame, stakes, and available options. Probe ordinary life, disagreement, cooperation and support, competition, performance, and a novel but plausible situation where eligible. Vary chronology, what the character knows, audience, or interlocutor one at a time. Require a predicted change where the evidence says the difference matters and stability where it does not. Mark unavailable scenario domains explicitly.
3. **Negative controls.** Offer a plausible but disfavored response and a wrong-register decoy. Check for appropriate abstention on unsupported domains and incompatible scenarios. Score choice and surface fidelity independently, including when natural Japanese expresses an implausible choice. Compare the rule's discrimination with a generic personality sketch of the same subject if assessing added predictive value.
4. **Exposure and freeze.** For a prospective test, commit the state and admissible evidence, exact predictions, rule IDs, distance, confidence, expected diagnostic opportunity and disconfirmation conditions before anyone authoring those predictions sees the test material or its outcomes. Record prior exposure and keep later source exposure and adjudication in a separate record. When the author already saw the material or learned the outcome, label the check retrospective even if it was excluded from the model's stated evidence. Independence from a prior interpretation is a separate property from source holdout.
5. **Independent review.** Give reviewers the model, exact evidence locators and scenario contracts. Ask them to check Japanese against eligible witnesses, compare rule predictions to source events, and search for missed alternatives or counterexamples. For multiple models compare decisions, voice constraints, applicability, and failures at matched states and horizons. Adjudicate as `SUPPORTED`, `PARTLY_SUPPORTED`, `CONTRADICTED`, `NO_DIAGNOSTIC_OPPORTUNITY`, `CONFOUNDED`, or `UNRESOLVED`. Preserve disagreements and report counts with denominators and exclusions. Avoid accuracy percentages from purposive probes.

A future modeling run starts by fixing its authorized subject, state, source set, and evidence horizon. Build the evidence map before drafting rules. Inspect the ordinary-life controls and every channel needed for load-bearing claims, or narrow the intended scope. A model can be offered only within the bounds of the recovered evidence and completed validation. Report uncovered domains, tests still needed, and decisions the model must abstain from.

## 9. Independent audiovisual reanalysis

For the planned Gemini 4 Carbon High run, supply only the **Blind-Safe Character Evidence Capture Contract** below as reconstruction guidance, extracted from its heading to the end of this file. The appendix is self-contained. Keep the complete specification, current guide, existing methods, synthesis, ledgers, claim lists, and all source-derived interpretations out of the blind inputs until the independent analysis is frozen. Git publication gives no permission to retrieve these materials during the blind phase. The run's authorized inputs and execution instructions govern its scope.

After the freeze and with authorization, retain the independent output and exposure record at their exact revision. Compare recoverable locators and claims through the [audiovisual reconciliation protocol](../../../governance/source-policies/MANGA_ANIME_AUDIOVISUAL_RECONCILIATION_PROTOCOL.md). Re-view and anchor load-bearing observations before relying on them. Record differences in witnesses, sampling, and clocks before adjudicating disagreements. Place post-exposure interpretation and comparison in separate records, with proposals for the existing primary homes. Preserve disputed items as open when verification cannot settle them.

## 10. Future Re LIVE comparison

*Revue Starlight -Re LIVE-* requires a separately authorized source inventory and project-specific analytical foundation under the [Generic Source-Bounded Game Analytical Method](../../../governance/analytical-methods/GENERIC_GAME_ANALYTICAL_METHOD.md). That foundation must admit and weight source classes explicitly. These include main story, school and everyday stories, character stories, events, hypothetical or stylized scenarios, costumes and other variants, and roles within performances. It must account for interactions across schools and ensembles and bind Japanese text and performed voice to the relevant build, route, variant, unlock conditions, witness, and scene. Record release order, diegetic placement, knowledge, and incompatible or floating event chronologies independently.

For a future comparison, align two explicitly identified subject-state records. Record each continuity, incarnation or role, witness and version, time and knowledge horizon, scenario, directed relationship, evidence channel, and the basis and uncertainty of the correspondence. Compare a bounded feature or conditional rule under matched premises and preserve disagreements and uncertain alignment. Each medium retains its own model and chronology. A game event requires affirmative evidence for any proposed correspondence with a film state.

## Blind-Safe Character Evidence Capture Contract

Collect character evidence from the assigned Japanese-original audiovisual material. Use only the run's authorized inputs, including any supplied neutral manifest or clock references. Work within the assigned source horizon. Identify people by what the source has established so far, using a temporary identifier when a name or correspondence is uncertain. Quarantine prior familiarity and report any exposure to earlier interpretations or later material.

**Record once per source object.** Give the unit and witness identifier, streams and language, inspected intervals, clock and calibration (anchors, offset, drift, precision), verified inspection route, and effective visual sampling or `UNKNOWN`. State what could actually be seen, heard, or read. Keep same-object observations with recoverable content anchors if a cross-object clock cannot be calibrated.

**Record once per material observation.**

| Field | Capture |
|---|---|
| ID and locator | Stable observation ID, unit, interval in the declared clock, and nearest available cue, frame, or neutral content anchor. Mark approximate timings. |
| Identity and state | Observed actor or speaker, depicted role or viewpoint if relevant, current state and story-time placement where established, and identification uncertainty. Record the disclosure point separately if the event may have occurred earlier. |
| Interaction | Addressee, action target, witnesses or audience, available options, and what each participant appears to know at that point. Cite the evidence of access or mark it unknown. |
| Context | Ordinary or heightened situation, immediate circumstances, social stakes and frame, including preparation, scripted performance, sung or spoken exchange, recollection, or uncertain staging where observed. Deliberately sample low-stakes routine and friendly exchanges as well as exceptional ones where available. |
| Description and class | What happened or was expressed, by inspected channel. Label direct speech, observed action, presented interiority, reported behavior, observer or role statement, performed delivery, or inference. Describe observable action and delivery before attributing intent. |
| Japanese status | Record spoken, sung, written, or unavailable, with speaker or singer certainty. Mark wording as verified Japanese text, checked or tentative listening transcription, translation-only, or unavailable. Treat translation as a navigation aid. Preserve uncertain wording without guessing. |
| Limits and interpretation | Confidence with a reason, limits of access or sampling, and any plausible alternative. Link counterevidence by observation ID or state the search gap. Put any conditional interpretation after the observation and cite its support. Record a missing action as possible evidence of absence only when opportunity and coverage are established. |

Re-view observations that will carry a conclusion. Record discrepancies between passes. Bound movement, micro-expression, and synchronization claims by the actual sampling and clock precision. Use a qualified, anchored observation or mark the issue unresolved when a channel is inadequate.

Freeze the observation log and independent analysis before receiving prior interpretations or comparison material. Record the exact frozen revision or digest, covered and unexamined intervals and channels, the last source boundary inspected, and any prior knowledge or accidental exposure with its affected scope. Preserve any earlier sequential freezes. Label later additions and comparisons by their exposure and keep them outside the frozen record. If earlier conclusions were seen before the freeze, record that the affected work cannot be claimed as independent.
