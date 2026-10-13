---
title: "Silent Witch — SW Analytical Method"
artifact_id: SW_ANALYTICAL_METHOD
artifact_type: analytical_method
series: "Silent Witch: Secrets of the Silent Witch"
series_id: silent-witch
generation: V1
version: "1.1"
last_updated: "2026-10-13"
status: canonical
scope: "Japanese-primary published-LN prospective reading and evidence discipline"
source_boundary: "Accepted pre-reading foundation and Japanese LN V01 technical source lock; no narrative source unit analyzed."
created: "2026-10-12"
canonical_home: "series/silent-witch/00 Frameworks and Methods/SW_ANALYTICAL_METHOD.md"
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
do_not_use_as_literary_evidence: true
recommended_reasoning_class: DEEP_SYNTHESIS
---

# Silent Witch analytical method

## Responsibility and governing boundary

Read the published Japanese light novels as literature, preserving the mechanisms by which a scene produces action, knowledge, feeling, and reader response. This method governs source inspection and inference. The [synthesis architecture](SW_SYNTHESIS_ARCHITECTURE.md) owns cumulative destinations and completion gates; the [character method](SW_CHARACTER_RECONSTRUCTION_METHOD.md) owns future operational reconstruction. The [template](SW_VOLUME_READING_TEMPLATE.md) implements these responsibilities without proving a reading occurred.

The canonical route is [the current corpus map](../CURRENT_STATE_AND_CORPUS_MAP.md). Live repository authority and [initiation policy](../../../governance/source-policies/MANGA_ANIME_PROJECT_INITIATION_AND_ARCHITECTURE_POLICY.md) govern execution. The owner has accepted this current-eligible method and its paired architecture. V01 has a technical source lock; the current entrypoint records the owner’s subsequent decision to keep its locator package local and leave SEQUENTIAL_ANALYSIS_LOCK = CLOSED. Gate readiness and an explicit source-unit reading instruction remain distinct; no narrative findings exist.

## 1. Japanese primary evidence and source fidelity

The intended primary track is numbered Japanese commercial LN I–XII in the supplied collection, one individually admitted volume per transaction. The [source map](../01%20Source%20Lock%20and%20Inventory/SW_SOURCE_AND_CONTINUITY_MAP.md) distinguishes verified folder identities from retained audit findings. Folder presence, a filename, a script statistic, and an OPF label are each narrower than a source lock or completed reading.

Before an authorized VNN reading, verify the exact EPUB bytes and SHA-256, Japanese title/volume, credits, colophon/edition and revision where available, OPF/spine, navigation, language, and resource usability. Preserve discrepancies instead of supplying a guessed edition. Compare the retrieved bytes with the retained manifest; an unexplained change must be reconciled. Source locking may inspect structure and limited fidelity samples while CLOSED, but may not become a disguised deep reading.

Deterministic extraction must preserve paragraph and scene order, punctuation, Japanese orthography, indentation or typographic cues where meaningful, emphasis, line breaks, and relevant ruby/gaiji information. Keep ruby base text distinct from its reading annotation; document any omission in the reading projection. Do not perform silent NFKC conversion, punctuation simplification, translation, OCR substitution, or correction of apparent authorial errors. A searchable projection may differ from the fidelity projection only with a reversible, versioned mapping.

A locator records witness ID, source hash, exact chapter label, spine member, and paragraph/element anchor. Prefer native anchors where stable; otherwise define a one-based deterministic element rule, including handling of empty elements and scene separators. Round-trip ordinary dialogue, ruby-bearing text, a chapter boundary, and the final narrative passage to original XHTML. Record the normalizer version and projection/map hashes in the evidence plane. Reader-app reflow pages are not printed pagination. Printed page numbers may be cited only when genuinely established.

Use witness grammar `SW-LNJP-V<NN>` and observation grammar `SW-E-LNJP-V<NN>-<sequence>`; supplements and web snapshots get separate witness IDs. These are prospective identifier patterns, not existing observations. The volume reading owns compact analytical observation records and recoverable locators. Raw text, paragraph maps, alignment tables, full image sets, and extraction databases remain governed Drive evidence.

Quote only wording necessary to test an interpretation, reproduce it exactly, identify speaker/focalizer and locator, and label any analyst translation. A translation is an aid, not an independent Japanese witness. Keep public excerpts brief and proportionate. Illustrations, captions, design material, author notes, and prose are different evidence channels. Record actual visual inspection; never infer voice-actor delivery, acoustic prosody, or uninspected visual detail from prose.

## 2. Whole-volume coverage and segmentation

Construct an inventory of every spine item before reading. Assign each to narrative, in-volume supplemental narrative, illustration, source-identifying paratext, author/production commentary, publisher preview, advertisement/notice, or unresolved class. Resolve narrative-relevant uncertainty before declaring closure.

Read every admitted narrative part in source order: prologue, chapters, interludes, epilogue, and in-volume extras. Account for viewpoint stories separately even when their story time lies earlier. Classify afterwords as paratext rather than character testimony. The retained audit flags unrelated publisher previews in several books; preserve them in the source container and exclude them from the Silent Witch narrative projection. Reverify their boundaries at source lock rather than treating audit entry names as an exhaustive semantic classification.

Maintain a coverage table of chapter/scene range, focalizer, admission class, inspection state, substantive movement, and remaining gap. Counts corroborate a bounded inspection record; they do not establish comprehension. Retrieval, a keyword search, a synopsis, or excerpt screening cannot replace full admitted narrative coverage. Full coverage does not require equal commentary on every paragraph.

Select close-reading scenes for literary centrality as well as relevance to current hypotheses. Include mundane exchanges, failed actions, limits of competence, contradictory behavior, and material not centered on the presumed protagonist. Record why diagnostic selections discriminate among explanations. Search can support retrieval after reading; it cannot silently choose the entire evidence set.

## 3. Prospective knowledge and reader-facing orientation

Before opening VNN narrative, recover the last closed LN-only state. Freeze the entering source boundary, relevant character/world knowledge, load-bearing claims, live questions, alternatives, genuine expectations, and uncertainties. V01 starts at PRE_V01 with no source-derived claims. Do not invent predictions to fill a form.

For V02 onward, write a distinct **prior-volume developments** section before inspecting the new volume. It tells the inherited story situation from already closed units. It is reader orientation, separate from the timed analytical entry freeze. Preserve a timestamp or immutable scratch/commit reference sufficient to establish its preparation boundary.

During reading, distinguish immediate scene impressions from interpretation after completing the volume. At exit, synthesize only that volume and eligible prior LN sources. Later discoveries may revise the current model but may not silently improve earlier predictions, erase reasonable uncertainty, or turn a later explanation into an earlier fact.

Write a connected **current-volume story synopsis** after the complete pass. Explain the starting situation, causal developments, consequential choices, relationship movement, reversals, ending, and placement of admitted extras in readable prose. Qualify reported or uncertain events. Readers should understand what happened without decoding evidence tables. This synopsis is substantial orientation; diagnostic close reading remains a separate sustained argument explaining how and why the novel works.

Record relevant prior franchise exposure honestly. This bootstrap inspected bibliographic descriptions, audit metadata, and web landing/index material; a future reader must not claim a blind first encounter. Keep later LN files, WN/gaiden, supplements, adaptations, commentary, reception, and comparison findings outside the next LN-only working evidence set. A fresh session does not erase model familiarity. If exposure occurs, disclose it, exclude it as evidence, and recheck affected claims.

## 4. Claim grammar and contradiction

Use these distinctions for consequential propositions:

| Class | Meaning and limitation |
|---|---|
| OBSERVABLE_TEXT_EVENT | Recoverable wording, represented action, or source presentation; an assertion's occurrence does not prove its content. |
| CHARACTER_REPORT_BELIEF | Speech, thought, recollection, belief, or self-description attributed to a character; reliability is a further claim. |
| NARRATOR_PRESENTATION | What narration offers and under what focalization/knowledge constraints; omniscience is not assumed. |
| STRONG_INFERENCE | A supported causal/formal explanation with consequential alternatives and counterevidence considered. |
| WORKING_HYPOTHESIS | A useful but incompletely discriminated account. |
| SPECULATION | Extension beyond close source support, visibly bounded. |
| NORMATIVE_EVALUATION | An evaluation with explicit criterion and descriptive premises. |
| CONTRADICTION | Incompatible propositions within specified witness/time/knowledge scopes; cause remains to be investigated. |
| UNRESOLVED_QUESTION | Material ambiguity or missing evidence prevents adjudication. |

Separate what happens, what a participant thinks happened, why someone acts, how narration frames it, authorial intention, and actual reception. Support each with the appropriate source. A character's confidence, institutional doctrine, comic framing, or repeated reader assumption does not promote a belief into narrative truth.

For a load-bearing inference preserve support, strongest rival explanation, disconfirming evidence, uncertainty, and the observation that could change it. Absence becomes negative evidence only when the declared inspected range and expected opportunity make absence meaningful. Missing access is an evidence gap, not proof that a trait or event is absent. An untested expectation remains UNTESTED.

Use the master ledger's PRESERVE, STRENGTHEN, REVISE, DOWNGRADE, REJECT, and OPEN revision events. Preserve the earlier formulation and its evidence boundary. A contradiction may result from ignorance, deception, chronology, focalization, witness revision, translation, paratext, or genuine inconsistency; retain alternatives until inspection supports adjudication.

## 5. Close reading as prose and social action

Attend to Japanese wording when it changes the argument: dialogue acts, requests/refusals, repair, address terms, honorifics, pronouns, register shifts, hedging, hesitations, omitted responses, and silence. Establish who speaks to whom, who is present, what each can know, and what the utterance attempts. Written hesitation does not certify a clinical symptom or acoustic delivery.

Analyze narrative voice, focalization, distance, withholding, imagery, humor, scene/summary rhythm, pacing, repetition, and asymmetry of reader access. Show the textual mechanism instead of naming a device without explanation. Silence can be avoidance, deliberation, concealment, refusal, inability, deference, or simply narratorial omission; compare evidence rather than choosing the title's most convenient interpretation.

For character observation use a recoverable process:

`circumstance -> perceived evidence -> appraisal/belief -> affect -> available options -> choice -> action/speech -> consequences -> later revision`

Mark which links are explicit and which are inferred. Preserve outward persona, private state, third-party attribution, and reader knowledge separately. Distinguish changed disposition from new knowledge, role/context change, relationship conditioning, newly revealed traits, and unresolved differences. Demonstrated expertise does not prove authority in every domain.

Relationships are directional: A toward B can differ from B toward A. Track initiative, trust, information, dependence, duty, resources, refusal, conflict, repair, and independent aims. Attraction, loyalty, care, and obligation may overlap without being equivalent. Less interior access warrants narrower claims, not invented motives.

Normative reading must identify affected people, viable alternatives, consequences, recurrence, tone, and counterreadings. Depiction, sympathy, success, comedy, or lack of punishment alone establishes neither approval nor critique. Explain motives separately from evaluating means. Everyday interaction must be allowed to complicate crisis-based models.

## 6. Investigative lenses, not prewritten conclusions

Test concealed identity and disclosure; withdrawal and coping without ungrounded diagnosis; expertise, mathematics and constraints on magic; the distribution of knowledge among focalizers; school/social and aristocratic/institutional pressures; loyalty, obligation, deception, self-authorship and agency; romantic/affiliative ambiguity; reputation versus demonstrated competence; and the relation of comedy, seriousness, and ethical treatment.

For each recurring lens ask what concrete mechanism the current volume supplies and what would weaken the proposed reading. Combine, reject, or extend lenses when evidence warrants it. Do not label a specialist mandatory merely because the prompt names its topic. The work may disclose an unanticipated central responsibility.

## 7. Atomic closeout and quality

A volume closes only after complete declared coverage, a readable causal synopsis, sustained diagnostic analysis, verified consequential wording/locators, entry and exit freezes, claim/prediction adjudication, and material updates to every required cumulative responsibility. Record an explained no-material-update where appropriate. Preserve unresolved mandatory evidence as a blocker to the corresponding completion claim.

The [master ledger](../03%20Longitudinal%20Ledgers/SW_MASTER_LONGITUDINAL_LEDGER.md) preserves cumulative changes; the entrypoint advances only after coherent durable closure. Distinguish inspection, semantic acceptance, transaction persistence/commit, branch publication, housekeeping, exact-head audit, and main integration.

Evaluate explanatory depth, evidence specificity, temporal/epistemic discipline, meaningful counterinterpretations, and literary readability. Sparse plot bullets or generic character lists cannot satisfy a deep reading. No arbitrary word quota or maximum imposes compression, and length alone proves nothing. Preserve enough connected prose to develop significant arguments.

A future single-unit instruction defaults to single_operation. Continuous execution needs an explicit recoverable terminal boundary under the [continuation policy](../../../governance/source-policies/MANGA_ANIME_SEQUENTIAL_EXECUTION_SCOPE_AND_CONTINUATION_POLICY.md). Listing the next volume supplies a route, not permission. On interruption recover actual files and high-water mark before resuming; never infer closure from conversation memory.
