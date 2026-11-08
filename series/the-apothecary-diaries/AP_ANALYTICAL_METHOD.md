---
title: "The Apothecary Diaries — Analytical Method"
artifact_id: AP_ANALYTICAL_METHOD
artifact_type: analytical_method
version: "1.0"
status: canonical
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
authority_generation: AP-INITIAL
authority_scope: "INITIAL bootstrap method, architecture, and administrative metadata only; no literary findings"
source_boundary: "Metadata reconnaissance: Japanese volumes 01–16 and separate simplified Chinese volume 15; no narrative admitted"
created: 2026-11-07
last_updated: 2026-11-07
recommended_reasoning_class: DEEP_SYNTHESIS
---

# The Apothecary Diaries analytical method

## 1. Scope, evidence and prospective responsibility

This method governs a future Japanese prose sequence selected from the supplied V01–16 inventory. The Chinese V15 is a separate, currently unadmitted comparison witness. Numbered inventory order is the proposed default, subject to metadata verification and explicit run scope; it is not proof of publication chronology, story chronology or an officially complete collection.

The [architecture](AP_SYNTHESIS_ARCHITECTURE.md) determines accumulation and synthesis responsibilities. The [generic novel method](../../governance/analytical-methods/GENERIC_NOVEL_ANALYTICAL_METHOD.md) supplies the prose baseline; source admission, archive authority and repository controls take precedence. This adaptation concentrates on serial causal explanation, changing access to information, ordinary practice and relationship-conditioned Japanese expression. These are questions the corpus must be capable of preserving, **not findings about unread characters or episodes**.

A reading must retain the full reasoning behind a claim: what happened in the bounded passage, whose perception or testimony supplies it, how the language constructs it, what alternative explains it, and what remains unavailable. An elegant synopsis, a disposition label or a ledger row cannot discharge that work. No fixed word limit authorizes dropping qualifications, mundane interactions or counterreadings.

## 2. Admission and witness identity

A run needs an OPEN architecture gate **and** explicit bounded authorization. Neither exists now. Before each future admitted unit, confirm the authorized run, selected witness, admitted high-water mark and permitted within-volume segmentation. Do not peek ahead to solve an uncertainty. If reliable chapter boundaries are not yet established, map them as a separate authorized preparatory operation rather than inventing them.

Use project-local keys `AP-JP-Vnn` and `AP-ZH-HANS-V15`, then bind each to the exact immutable byte digest and versioned spine map in the governed source receipt. The local key alone is not an identity proof. Distinguish metadata-reported presence, byte-verified receipt, admitted source, inspected components and accepted analytical closure. New bytes, even under the same filename or UUID, reopen identity verification; they do not overwrite the old witness.

For the V15 collision, compare hashes, language and member/spine identity before any content equivalence claim. Chinese packaging repairs reported by the historical audit do not make its prose Japanese or establish translation fidelity. Japanese V12–16 packaging warnings require actual extraction/render-route verification when used; they do not prove missing prose or permission to repair originals silently.

Classify every spine component as narrative, illustration, front matter, afterword, bonus, preview/advertisement, or unresolved. Preserve the supplied reading order and exclusions with reasons. A keyword search, metadata scan or a few screenshots cannot establish full chapter coverage. Paratext that reveals later material belongs beyond the prospective frontier until separately admitted.

## 3. Locators and source inspection

Each load-bearing evidence item has both a human locator and a deterministic route:

- Human: witness key, numbered volume, exact verified chapter/section heading, scene/movement and an economical contextual cue.
- Deterministic: immutable witness digest, versioned extraction/spine-map identity, spine index, member path, paragraph/block identity and a short verified text anchor or character range. Record normalization rules and both original and normalized anchors when transformation affects retrieval.
- Image: the same witness identity, manifest/member identity, local ordinal, relation to the narrative frontier, and inspection method. A prose caption does not prove image content.

The source receipt retains private object resolution. Public analytical prose uses stable local references and allowed short quotations, not private IDs, full copyrighted text or acquisition paths. Reflow page numbers are display coordinates unless a print-page mapping is proven. Record a retrieval test for central claims: a second pass must reach the same bounded evidence in the locked witness. Failure leaves `RETRIEVAL_UNRESOLVED`; it cannot be fixed by a more confident paraphrase.

Japanese is the anchor language for this lane. Preserve consequential original wording, orthography, address terms, ellipsis, modal endings, agency, politeness shifts and ruby/base distinctions. An English gloss is an interpretation and must expose consequential ambiguity. Use `EXACT_VERIFIED`, `WORKING_TRANSCRIPTION` or `PARAPHRASE` honestly. Verify exact quotations against the admitted witness. Normalization improves search only and never silently replaces evidence.

## 4. Five clocks and several knowledge positions

Keep numbered source/disclosure order, publication or edition history, inferred story time, a subject's information-acquisition order, and the analyst's admitted-source order distinct. The serial ledger stores explicit sequence constraints rather than manufactured dates. A flashback can supply old events newly available to the reader; it does not retroactively give those events to a character who did not know them.

At each consequential passage distinguish:

1. Textually represented event or condition.
2. Narrator presentation, focalization and access.
3. Named subject's perception, memory, testimony, belief or uncertainty.
4. Other participants' information and plausible misconceptions.
5. Reader knowledge at that disclosure frontier.
6. Analyst inference at the authorized boundary.

Names and identities must follow the admitted text. Preserve an intentional disguise or withheld identity without using later knowledge to “correct” the original reading. When a name is established, use it rather than repetitive generic role substitutions. Reliability is evaluated for a particular act of testimony or focalization, not assigned globally to a narrator or character because one claim failed.

Record alternative chronologies or knowledge states where the text permits them. A retrospective reassessment links to the earlier frozen reading and explains the later evidence; it does not rewrite what a prospective reader could have known.

## 5. Causal explanation, inference and institutions

A future analytical movement should connect condition → perception → appraisal → affect → available options → choice or non-action → consequence. Label any unsupported link; temporal succession and narrative juxtaposition are not causation. Separate an explanation proposed by a character from the mechanism the analyst thinks the text supports. Record evidence that would discriminate rival explanations and whether the source actually supplies it.

If specialized practical, medical, household, legal, political or institutional knowledge becomes consequential, distinguish rules stated by an authority, observed procedure, testimony, rumor, sanctioned exceptions and analyst generalization. These domains are architectural possibilities suggested by the project's identity and prose form, not established subject matter at bootstrap. No external technical fact can silently validate the fictional mechanism. External context, when expressly relevant and sourced, is `EXTERNAL_REFERENCE` and remains separate from the primary text's claims.

Track who can act, who controls resources, what information is inaccessible, and what consequences follow refusal as well as compliance. A successful outcome does not prove an actor intended it; a failed outcome does not prove incompetence without an opportunity/resource analysis. Distinguish deliberate action, coerced action, habit, mistake, presentation for an audience and retrospective rationalization.

Preserve competing causal models in full prose when stakes are substantial. The cumulative ledger can route those arguments but cannot reduce them to a winner column.

## 6. Character development and ordinary life

Character analysis accumulates from actual named subjects encountered in admitted prose. Do not import a roster, biography, psychology or relationship from title familiarity, an adaptation or secondary summary. Record separate evidence channels: direct speech, represented behavior, narrated interiority, others' reports and role/public presentation. Reports about a subject are not the subject's own motives.

Sample ordinary routines, low-stakes choices, professional or domestic practice, pauses, humor, boredom, fatigue and unremarked interactions where they occur. Crisis evidence alone cannot establish baseline disposition. “Never does X” requires a meaningful opportunity denominator; absence of a scene is not refusal.

Distinguish a stable tendency, a temporary emotional/physical condition, a role constraint, newly acquired knowledge, an audience-dependent mask and development over time. A revised reading may be `REVEALED_NOT_NEW` rather than a change in the subject. Record the proposed change cause and evidence. Retain exceptions and recovery periods instead of flattening a subject into a final-state personality.

Use full argument for motivation, including rival motives and what the prose withholds. Diagnosis, moral evaluation and causal explanation have different warrant. Distinguish depiction, explanation, evaluation and endorsement without moral prefiltering or unsupported exculpation.

## 7. Directed relationships and linguistic action

An A→B state need not match B→A. Track access, trust, dependence, obligation, fear, intimacy, status, misunderstanding and audience effects only where supported, with source-specific vocabulary rather than compulsory numeric scores. Record the setting and alternatives available. A courtesy form, teasing utterance or withheld response cannot by itself settle an entire relationship.

Analyze utterances as situated actions: appraisal → conversational objective → speech act → recipient/audience filter → register → words. Preserve who hears the utterance, private thought versus spoken line, narrative framing, interruptions, repairs, indirect reference and what remains unsaid. Register can enact distance, concealment, role or play; require competing explanations and contextual controls before declaring psychological change.

The register ledger routes exact Japanese anchors to close analysis. It must retain mundane comparable examples and not become a catchphrase catalog. Translation observations attach to `AP-ZH-HANS-V15` and a verified aligned Japanese passage only after a separate authorized comparison. A translated wording is evidence of that witness's wording; it is not a replacement for Japanese voice, narrator stance or uncertainty.

## 8. Form, recurring structures and images

For each admitted unit, ask how focalization, interiority, reported speech, ellipsis, ordering, pacing, chapter breaks and repeated details distribute attention and uncertainty. Motifs and symbols require recurrence plus variation, context and plausible alternatives; repetition alone is not a settled thesis. Retain quiet transitional passages as potential structural evidence.

Inspect included illustrations only through an actually verified STILL_IMAGE route. Record placement and whether an image precedes, accompanies or follows the event it appears to depict. Treat visual claims as bounded observations; do not silently promote an illustration into an authoritative account of an ambiguous prose event. Record visual debt if an image was not inspected, and narrow any dependent claim. No performed vocal, musical or audiovisual assertion can arise from this text-and-image lane.

## 9. Claim handling and future reading acceptance

Classify assertions as `OBSERVATION`, `SELF_REPORT`, `NARRATOR_PRESENTATION`, `INFERENCE`, `HYPOTHESIS`, `CONTRADICTION`, `EXTERNAL_REFERENCE`, `EVALUATION` or `UNRESOLVED`, with high/moderate/low/unresolved confidence and its reason. Classification describes warrant, not prestige. A contradiction stays open until its type is determined: source identity, translation, chronology, perspective, strategic presentation, revised interpretation or possible textual inconsistency.

The minimum completed future reading contains the following developed responsibilities; headings may adapt to the unit:

| Responsibility | Required work |
|---|---|
| Receipt and boundary | Exact witness, authorized unit, components inspected/excluded, entry high-water mark and access limits |
| Entering state and expectation | Prior knowledge, active competing claims, frozen predictions and source-specific uncertainties |
| Unit argument | A developed central reading and credible rival, with discriminating evidence and scope limits |
| Movement-level analysis | Full sequence of material transitions; causality, narration, focalization and unresolved links, not a chapter synopsis |
| Subject and relationship development | Named evidence, ordinary-life controls, directed states, motive alternatives and change causes |
| Language and form | Consequential Japanese phrasing, voice/register, ordering, motifs and counterexamples |
| Specialist and modality debts | Earned domains, institutional claims, images and paratext; inspected versus unresolved clearly separated |
| Revision and integration | Claims preserved/strengthened/revised/downgraded/rejected/opened; linked evidence, ledger deltas and affected destinations |
| Exit freeze | Accepted source frontier, unresolved questions, preserved prospective forecasts and exact next authorized operation or none |

At closeout, synchronize the source coverage, evidence/revision, serial state, character/register and checkpoint surfaces as one reviewed transaction. Each substantive delta links to its full argument. Before semantic acceptance, promotion or integration, sample the introduction, a substantial middle section, conclusion and every major relationship where actors could be confused. Check known names, purposeful titles, pronouns, concealment, speaker/thinker/recipient attribution and knowledge boundaries. Classify findings as `JUSTIFIED_ROLE_REFERENCE`, `SOURCE_REQUIRED_ANONYMITY`, `KNOWLEDGE_BOUNDARY_REQUIRED`, `UNNECESSARY_GENERICIZATION`, `AMBIGUOUS_REFERENT` or `INCORRECT_IDENTITY_OR_ATTRIBUTION`; repair supported defects and record sampled scope/material findings in closeout. No automatic name substitution is permitted.

A reading is incomplete if a needed source or modality remains uninspected, an important claim cannot be retrieved, required ledger updates are missing, or a thesis suppresses strong counterevidence. Explicitly bounded unresolved interpretation can remain after completion; false certainty is not an acceptance requirement.

## 10. Reconstruction and preserved history

The architecture defines a later reconstruction pathway separate from monographs. Evidence collected here may support it, but no behavioral policy, synthetic dialogue, prediction score or readiness grade exists now. Freeze prospective predictions before opening later evidence. Synthetic outputs remain labeled derived tests and never become source quotations or independent support.

Frozen accepted readings preserve their historical boundary. Later discoveries produce claim transitions and linked errata or new syntheses, not silent retroactive rewrites. The [archive authority policy](../../governance/source-policies/ARCHIVE_AUTHORITY_AND_SUPERSESSION_POLICY.md), [handoff contract](../../governance/source-policies/MANGA_ANIME_ANALYTICAL_HANDOFF_AND_INTEGRATION_CONTRACT.md) and [long-series protocol](../../governance/source-policies/MANGA_ANIME_LONG_SERIES_HYBRID_EXECUTION_PROTOCOL.md) govern retention and transfer. A fresh session must receive the full analytical files and evidence routes, including counterarguments, not just their conclusions.
