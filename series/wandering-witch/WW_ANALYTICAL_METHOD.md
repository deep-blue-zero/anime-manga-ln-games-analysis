---
title: "Wandering Witch — Analytical Method"
artifact_id: WW_ANALYTICAL_METHOD
artifact_type: analytical_method
version: "1.1"
status: canonical
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
authority_generation: WW-INITIAL
authority_scope: "INITIAL bootstrap rules and attributed source metadata only; no literary findings"
source_boundary: "Metadata reconnaissance: Japanese main volumes 01–25 plus separate 2014 Upper and Lower editions; no narrative admitted"
created: 2026-11-07
last_updated: 2026-11-13
recommended_reasoning_class: DEEP_SYNTHESIS
---

# Wandering Witch analytical method

## 1. The question this method keeps open

This project must be able to analyze a local narrative on its own terms while also testing how a long numbered sequence accumulates traveler/persona, relationship, formal and ethical meaning. It must not decide in advance that every chapter is an isolated tale, that every encounter proves the same trait, or that the sequence is a single continuous chronology. Those are hypotheses to be tested from admitted prose.

The supplied metadata establishes main Japanese volumes 01–25 and separate 2014 Upper/Lower witnesses. It does not establish chapter contents, narrator identity in each section, continuity across editions, or a roster of characters. The title's reference to Elaina is bibliographic identity, not permission to invent characterization.

The [generic novel method](../../governance/analytical-methods/GENERIC_NOVEL_ANALYTICAL_METHOD.md) governs prose fundamentals; this method adapts it to local-unit integrity, disclosure order, recurring-persona claims, and separate edition history. The [architecture](WW_SYNTHESIS_ARCHITECTURE.md) owns accumulation and convergence. Current source, initiation, handoff and authority policies take precedence. No narrative work is authorized now.

## 2. Source lock, order and segmentation

Use `WW-MAIN-Vnn` for the supplied main sequence and `WW-ORIG2014-UPPER` / `WW-ORIG2014-LOWER` for the earlier editions. Bind each to immutable bytes and a versioned spine map before admission. Historical manifest digests and claims can aid reconciliation but must not be presented as freshly verified remote bytes. Five archived alternatives remain provenance witnesses rather than extra installments.

The default candidate main order is numeric V01→V25, subject to actual edition/order verification and the owner's run scope. A run specifies exact start/terminal units, allowable chapter/section frontiers and exclusions. Original editions have no automatic place before V01 or after V25: comparison requires separate authorization and source alignment. Do not conflate publication ancestry with fictional chronology.

Map verified chapters and section breaks faithfully. Assign an analytical local-unit ID only after inspecting enough authorized material to establish its boundary. A chapter might contain multiple movements, or several chapters might sustain one question; record the rationale instead of forcing one table row per chapter. Preserve the difference between volume completion and local-story closure. An unresolved ending is a possible formal result, not an instruction to search later or external sources.

For every admitted component, record narrative, illustration, front matter, afterword, bonus, preview/advertisement or unresolved. Keep paratext beyond the prospective frontier if it reveals later content. Search hits and random sample checks cannot certify all components. Do not use the stale nineteen-file audit notes to delete present inventory, nor silently rewrite their historical claims into a clean audit.

## 3. Deterministic evidence and Japanese language

A public evidence route comprises witness/version, human volume/chapter/section, local-unit/movement, and a concise contextual anchor. Its deterministic counterpart is the immutable witness digest plus extraction/spine-map version, spine index, member path, paragraph/block identifier and a verified short anchor or character range. Record normalization rules; retain original Japanese when a search form changes orthography, ruby or punctuation.

Image evidence adds manifest/member identity, ordinal, placement, inspection route and admitted frontier. Reflow pages are not print pages without a proven mapping. The private receipt resolves public keys to restricted source objects; no private ID or copyrighted bulk extraction belongs in Git.

Use `EXACT_VERIFIED`, `WORKING_TRANSCRIPTION` or `PARAPHRASE` for quotations. Distinguish exact wording from a working English gloss and explain consequential ambiguity. Preserve narration versus dialogue, politeness, address, tense/aspect, modality, omission of subjects, irony cues, base/ruby and represented thought. A fluent gloss must not erase ambiguity over who speaks, knows, judges or acts.

Retrieve load-bearing evidence a second time from the locked witness. Report `RETRIEVAL_UNRESOLVED` if the route fails. An extract or OCR output is a derivative requiring mapping and error checks, not an independent corroborating witness. No audio, acting or vocal-prosody claim can be inferred from written Japanese.

## 4. First read the local narrative in depth

For each source-established local unit, reconstruct the sequence of conditions, information, actions and consequences. Preserve the setting's concrete rules as presented, who asserts them, who can benefit or refuse, the opportunities available, and what the narrator withholds. Separate the text's event account from a subject's explanation and the analyst's inference.

The causal chain is condition → perception → appraisal → affect → options/constraints → choice or non-action → consequence. Mark missing links. A surprising ending does not prove everything before it was deception; narrative surprise, factual contradiction and reader misprediction are different observations. Consider a rival account of the decisive transition and what evidence would distinguish it.

Do not reduce a local narrative to “an example of the traveler being X” or a one-sentence moral. Supporting subjects, local relationships, routine activities, institutional assumptions and the unit's formal closure may have interpretive importance independent of a recurring figure. Develop that argument where the source supports it. A brief appearance can carry a complete ethical or causal problem.

Distinguish depiction, explanation, evaluation and endorsement. A narrator's judgment, a subject's justification and the work's formal invitation to judge need not coincide. Record uncomfortable or unresolved alternatives without replacing literary interpretation with a moral lesson, and without mistaking explanation for approval.

## 5. Disclosure, narration and knowledge

Track five orders: supplied source/disclosure order, publication/edition history, inferred story or travel chronology, subject information acquisition, and analyst admission. Never sort scenes into a single “true timeline” before the source warrants it. Relative before/after constraints and unknowns are legitimate states.

For each consequential passage identify the speaking/narrating position, focalization, represented thinker, recipient/audience, and the reader's information frontier. Distinguish narrator presentation, self-report, observed behavior, recalled event, rumor, inference and withheld information. Reliability is claim-specific; a playful or unreliable passage does not justify globally distrusting every statement.

A later identification or recurrence can recontextualize an earlier unit without changing what was knowable then. Preserve the earlier name or anonymity required by the source; add a later identity link with its disclosure boundary. A returning name, location or image may suggest recurrence but is not sufficient to prove identical person, place, event or continuity.

In the local-unit atlas, record both resolved and open causal/epistemic endpoints. “The reader is not told” is different from “no outcome occurred”; “the traveler leaves” cannot automatically settle every local consequence. This is an analytical rule for any such evidence encountered, not a claim that a particular departure appears in the unread source.

## 6. From local units to recurrence without flattening

A cross-unit link begins as a candidate with the exact evidence for sameness or variation. Distinguish repeated character, repeated setting, retold event, formal rhyme, thematic analogy, reusable situation and incidental lexical similarity. Preserve incompatible interpretations if identity is unproven.

A pattern claim needs the local arguments it integrates, meaningful variation, counterexamples and an explanation of selection. Do not cherry-pick vivid encounters or impose a universal worldview from one narrator's statement. Track counterinstances and units where an expected opportunity was absent. Similar narrative functions need not imply equivalent motives or ethics.

When a recurring subject appears, ask what actually changes: knowledge, relationship, role, context, resources, affect, disposition or what the reader has only now learned. Maintain `REVEALED_NOT_NEW` and `UNRESOLVED` possibilities. Nonadjacent disclosures can reveal older states; later volume position is not automatically later psychological development.

A checkpoint may propose a motif or formal account, but it must preserve full local readings so that a specialist can challenge the grouping. The recurrence atlas is a router, not a replacement short-story anthology of summaries.

## 7. Persona, relationships and ordinary life

Create subject identities from admitted source evidence only. Separate a subject's self-description or performed persona from narrated interiority, actual behavior, other people's reports and analyst interpretation. A vivid voice is not transparent access to a stable motive. Avoid flattening a recurring subject to a signature trait or a supporting subject to a plot function.

Capture low-stakes conversation, rest, practical arrangements, work, money/resource choices, habitual conduct and ordinary social exchange where present. These contexts are diagnostic controls for dramatic decisions. A crisis response requires its particular stakes and alternatives; repeated silence or absence is not a policy without actual opportunity evidence.

Relationships are directed and context-dependent. For A→B, preserve A's information about B, behavior, expectation, audience, obligation and constraints. B→A requires separate evidence. A brief encounter can be consequential without a durable mutual bond; recurrence can reveal asymmetry rather than intimacy. Do not infer closeness solely from familiarity of address or repeated co-presence.

Written voice follows appraisal → objective → speech act → recipient filter → register → expression. Preserve irony, distancing, narrative self-fashioning and speech/interiority contrasts when supported, with alternatives. Record comparable ordinary contexts, not only quotable lines. Use verified Japanese excerpts sparingly and retain exact locator paths.

## 8. Edition history, images and external contamination

The 2014 Upper/Lower witnesses occupy a separate editorial-history lane. Only an authorized comparative operation can establish aligned sections, expansion, omission, rewriting, reordered disclosure or unchanged passage. Similar titles and authorship metadata do not prove textual equivalence. The original Lower is never a substitute for main V01.

A future comparison records exact witness pairs, alignment confidence, unmatched material and effect on narration, causality, characterization, form and language. It does not silently repair or reinterpret the main prospective reading with earlier-edition material. Shared and divergent continuities remain explicit hypotheses until evidence supports them.

The manifest's five archived cover variants are historically reported to have matching publication-content entries apart from package metadata and cover images. That assertion remains attributed; present-day equivalence is not independently established. A changed image matters to image claims even where prose bytes match.

Illustrations require actual STILL_IMAGE inspection, with placement and spoiler boundary. A text-only reader can acknowledge the debt but cannot certify appearance, composition or image/prose agreement. Covers, insert art and afterwords have distinct roles and may use different representational conventions. Adaptations and secondary summaries are excluded; they cannot fill unknown local outcomes, identities or performed voices.

## 9. Future output contract and revision

Each accepted volume reading must include detailed source-established local-unit analyses rather than only a volume thesis. Develop the following responsibilities, adapting section lengths to actual complexity:

| Responsibility | Required account |
|---|---|
| Receipt and entry state | Exact witness, authorized frontier, coverage/exclusions, prior claims and frozen expectations |
| Local-unit segmentation | Actual boundaries and rationale; movements and relations within/between units |
| Full local argument | Conditions, characters/roles as known, causal chain, narration, language, relationships, strongest rival and unresolved ending |
| Cross-unit reasoning | Evidenced recurrence/variation, alternative groupings, counterinstances and limits of generalization |
| Subject and voice state | Ordinary versus exceptional behavior, knowledge/disclosure, directed ties, written register and change causes |
| Form and modality | Ordering, pacing, repetition, illustrations/paratext actually inspected and remaining debt |
| Revision/integration | Evidence routes; claim transitions; atlas and persona updates; implications and full argument destinations |
| Exit freeze | Source frontier, known and unresolved states, prospective predictions, owner-authorized next operation or NONE |

Assertion classes are `OBSERVATION / SELF_REPORT / NARRATOR_PRESENTATION / INFERENCE / HYPOTHESIS / CONTRADICTION / EXTERNAL_REFERENCE / EVALUATION / UNRESOLVED`, with high/moderate/low/unresolved confidence and a reason. Revision uses `PRESERVE / STRENGTHEN / REVISE / DOWNGRADE / REJECT / OPEN`. Record former and new formulations, boundaries, evidence, rivals and dependent outputs. Do not harmonize local moral positions or narrator claims simply to obtain a single series thesis.

Before semantic acceptance, promotion or integration, sample introduction/synopsis, a substantial middle section, conclusion/exit state, every major relationship and any ambiguous actor passage. Verify known names, purposeful titles, pronouns, concealment, speaker/thinker/recipient and knowledge boundaries. Classify findings as `JUSTIFIED_ROLE_REFERENCE / SOURCE_REQUIRED_ANONYMITY / KNOWLEDGE_BOUNDARY_REQUIRED / UNNECESSARY_GENERICIZATION / AMBIGUOUS_REFERENT / INCORRECT_IDENTITY_OR_ATTRIBUTION`. Record sampled scope and material findings; repair only supported defects.

A completed reading requires the full text and synchronized source, atlas, persona, claim and boundary-register transaction. Inspect central evidence retrieval and modality debt. A word ceiling, convenient summary or populated table cannot excuse missing local causal/linguistic argument. Reasoned uncertainty may remain; unsupported closure may not.

### Current-unit story synopsis

*Prospective amendment, 2026-11-13, under initiation policy v1.11 §5.3.*

Each completed plot-bearing reading includes a clearly labeled **Current-unit story synopsis** near its front, after brief witness/coverage and entering context and before the extended interpretation or ledger inventory. For a canonical volume reading, orient the reader to the actual sequence of source-established local units and their relation or lack of established connection. For a separately authorized canonical local-unit reading, use that declared local boundary. Do not assume every chapter is a self-contained story, force an overarching continuous plot, or turn volume completion into resolution of every local outcome.

Use connected, accessible prose to explain the opening situations, named participants and stakes, consequential actions and decisions, causal turns, disclosures and state at the current boundary. Preserve concrete scene and physical-event mechanics where established, including what remains unresolved when a local narrative ends. Distinguish inherited context from events newly presented here; distinguish narrated or witnessed events from focalized belief, testimony, conjecture and unknown outcomes. Preserve source-required anonymity and the point at which an identity becomes available. Material event claims need retrievable source locators or stable observation references; those references support the prose rather than replacing it with a table. Scale detail to the actual units without a fixed word count.

This is unit-end, spoiler-bearing orientation: compose or finalize it only after all applicable entering and within-unit prospective captures are frozen, and shield it and the completed reading from earlier-horizon analysts. It may recount any outcome disclosed inside the authorized unit, but must not import later unadmitted units or the separate 2014 Upper/Lower witnesses to complete a main-lane account. Publication ancestry does not supply missing fictional chronology. The synopsis supplements every existing full local causal, linguistic, formal, character, ethical, counterreading and synchronized-register obligation in this section. Acceptance requires both; no existing frozen reading is rewritten and the CLOSED analysis lock remains governing.

## 10. Later reconstruction and historical preservation

Reconstruction is a future derived responsibility, not the purpose of every local reading. Its model and independent tests stay distinct from a character monograph and from primary evidence. Freeze predictions before held-out inspection. If the model author has already seen the test source, label the exercise `RETROSPECTIVE_CONSISTENCY_TEST`, not held out.

Never feed synthetic speech or scenario outcomes back as canonical characterization. The architecture defines coverage, conditional policies, exception handling, uncertainty and independent evaluation. No subject dossier, readiness grade or behavioral simulation is authorized now.

Accepted prospective readings and frozen checkpoints retain their historical boundaries. Later evidence produces linked revisions or errata, not quiet rewriting. Follow the [archive authority policy](../../governance/source-policies/ARCHIVE_AUTHORITY_AND_SUPERSESSION_POLICY.md) and [full-output handoff contract](../../governance/source-policies/MANGA_ANIME_ANALYTICAL_HANDOFF_AND_INTEGRATION_CONTRACT.md); preserve complete local analyses, counterarguments and edition distinctions across sessions.
