---
title: "Rent-a-Girlfriend - Analytical Method"
artifact_id: RAG_ANALYTICAL_METHOD
artifact_type: analytical_method
series: Rent-a-Girlfriend
generation: V1
version: "1.0"
status: canonical
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
do_not_use_as_literary_evidence: true
created: "2026-09-19"
canonical_home: "series/rent-a-girlfriend/00 Frameworks and Methods/RAG_ANALYTICAL_METHOD.md"
design_reference_commit: "6d027e55f2eb38ec04ceed16bddc25015dc8a180"
adopted_at: "2026-09-19"
adopted_against_commit: "6d027e55f2eb38ec04ceed16bddc25015dc8a180"
source_boundary: "Method design only; no manga volume was inspected in preparing this document."
recommended_reasoning_class: DEEP_SYNTHESIS
---

# Rent-a-Girlfriend: analytical method

## 1. Purpose and governing commitment

Build a source-grounded, longitudinal account of the manga and operationally useful reconstructions of its characters. Read **one volume at a time, in order**, and close each volume transaction before opening the next. Use ten-volume blocks as synthesis and review boundaries, not as substitutes for individual readings and not as assumed narrative arcs.

Every reading must distinguish:

1. **What happened:** represented events, speech, thoughts, decisions, disclosures, and material changes.
2. **What changed:** knowledge, commitments, behavior, relationship conditions, self-understanding, dependencies, and available choices.
3. **How the manga presents it:** focalization, images, page construction, comedy, erotic or romantic framing, repetition, and reader access.

The goal is neither a defense nor a prosecution of the series. Familiar claims about stagnation, passivity, manipulation, idealization, or authorial provocation begin as questions or quarantined prior opinions. None is an established finding of this project.

This method governs evidence and interpretation. `RAG_SERIES_ARCHITECTURE.md` governs destinations, dependencies, checkpoints, and completion. `RAG_CHARACTER_RECONSTRUCTION_SPEC.md` governs operational character models and their validation. Those responsibilities are complementary, not interchangeable.

## 2. Source boundary and reconnaissance

### 2.1 What is known at design time

The owner reports acquiring all published volumes. The exact inventory, language, publisher, editions, file formats, completeness, source locations, and final volume number have **not** been verified in this package. Do not carry forward an earlier conversational volume count as a source lock. Acquisition does not establish inspection.

Resolve a finite inventory `V001-VNNN` at implementation. Record the inventory date and distinguish:

- available volumes;
- verified intact volumes;
- analytically admitted volumes;
- completed and committed readings;
- the currently authorized terminal volume.

Newly acquired or newly published material does not automatically expand an active run. A partial final block is legitimate; it is not evidence that the series itself has ended.

### 2.2 Witness precedence

The primary project is the acquired **main manga continuity**, not an unmarked franchise composite. Verify what the supplied files actually contain. Map collected volumes to chapters using the edition itself; do not assume uniform chapter counts or unchanged magazine/collected pagination.

Where available, the original-language manga supplies the basis for original-language wording claims. The inspected localization remains its own named witness. When only a translation is available, proceed with bounded analysis and explicitly mark translation-dependent claims. Do not invent Japanese wording, register, or nuance.

Keep these source classes separate:

| Source class | Treatment |
|---|---|
| Main manga narrative pages | Primary narrative evidence within the admitted boundary. |
| Bonus chapters and volume extras | Inventory separately; admit by a declared placement rule and record their narrative/paratext status. |
| Covers, advertisements, next-volume previews | Paratext; not evidence that depicted events occurred. Future-facing material is not admitted prospectively. |
| Alternate printings or translations | Separate witnesses with edition-specific locators and conflict notes. |
| Spin-offs and adaptations | Outside the first pass unless separately authorized and scoped. |
| Interviews, author posts, marketing | Dated external/paratext evidence; never a shortcut to character motives. |
| Fan commentary, memes, reviews | Reception material only when explicitly assigned; not primary character evidence. |

Do not use external plot summaries to repair unread or inaccessible manga. A source-access failure remains an access failure.

### 2.3 Three storage planes

Primary volumes, page images, transcripts, extraction products, and deterministic page/chapter crosswalks belong to the approved evidence plane, ordinarily the project Drive evidence surface or an authorized local source location. Temporary renders and processing caches belong to the working/build plane. Interpretive readings, analytical ledgers, character models, and syntheses belong in Git after acceptance.

The analytical `RAG_SOURCE_AND_SCOPE_MAP.md` holds public-safe witness identifiers, source boundaries, inspection status, and retrieval routes. It is not a second raw-source archive. Do not commit manga pages, bulk transcriptions, purchase records, personal filesystem details, credentials, or temporary ZIP packages.

## 3. Initiation and execution gates

Before V001, the exact current entrypoint must identify accepted, current-eligible versions of this method and the architecture; the reconstruction specification must also be accepted as this architecture's required dependency. Verify source reconnaissance, usable page inspection, the required day-one infrastructure, and the applicable repository gate. Only then record `SEQUENTIAL_ANALYSIS_LOCK = OPEN`.

These distributed proposal files remain `draft_noncurrent`. Their existence does not open the gate. A current-eligible bootstrap entrypoint may truthfully record a CLOSED lock while setup is incomplete.

The canonical source unit is one volume. Chapters and scenes are internal working subdivisions. An interruption mid-volume does not advance the completed-volume high-water mark.

Default execution is `single_operation` unless the owner explicitly supplies a bounded `continuous_sequential` instruction. The companion startup prompt proposes V001-V010 as the first continuous tranche. Merely owning later volumes, listing a next operation, or reaching a checkpoint does not authorize additional volumes.

## 4. Prospective knowledge discipline

### 4.1 Before each volume

Recover the committed boundary, prior checkpoint where applicable, current models, active claims, and unresolved questions. Record an entering freeze before substantive inspection of the next volume. It identifies what is established, inferred, disputed, or unknown through the preceding volume and any genuine predictions being tested.

Do not load later plot summaries, later monographs, later character biographies, later-volume previews, or retrospective commentary into the reading context. A filename-only inventory of later sources is acceptable; their narrative content is not.

Prior franchise familiarity cannot literally be erased. Record known exposure where material, exclude it from evidence, and do not call a reading or prediction blind merely because a new session was opened. A fresh session reduces context carryover; it does not guarantee an uncontaminated reader.

### 4.2 During and after the volume

Read chapters in the edition's order. Distinguish an initial encounter with a scene from a volume-end interpretation informed by subsequent chapters **within that same volume**. The completed volume reading may synthesize the entire admitted volume; it must not import the next one.

Freeze the exiting state after all required updates. The prospective reading remains a historical record of what the admitted evidence supported then. Later findings belong in the revision ledger and current interpretive homes, with links back to the old reading.

Do not silently rewrite an early inference to look prescient. Correct an objective transcription or locator error transparently, preserving the correction trail. A changed interpretation is not a typographical correction.

### 4.3 Questions are not predictions

A question asks what the text will establish. A prediction specifies an observable expectation, its conditions, source basis, and a potential disconfirmation before the relevant new evidence is read. Record abstention or lack of a diagnostic opportunity rather than generating a prediction for every volume.

## 5. Evidence grammar and locators

### 5.1 Represented evidence versus inference

Use the following local claim classes. They are analytical labels, not replacements for repository authority metadata.

| Class | Meaning |
|---|---|
| `OBSERVATION` | A recoverable feature of the inspected source. |
| `CHARACTER_REPORT` | What a character says, thinks, remembers, or claims; not automatically objective truth. |
| `STRONG_INFERENCE` | An explanation supported by converging evidence and tested alternatives. |
| `WORKING_HYPOTHESIS` | A useful but insufficiently discriminated explanatory model. |
| `SPECULATION` | An extension beyond the evidence; not promoted into source findings. |
| `VALUE_JUDGMENT` | An explicitly stated evaluative conclusion and its criterion. |
| `UNRESOLVED` | Competing readings or missing evidence prevent adjudication. |

An inner monologue establishes that the manga represents a thought. It does not automatically establish that the thought is accurate, stable, sincerely endorsed over time, or equivalent to an action. A facial reaction establishes a depicted reaction, not one uniquely recoverable motive.

Keep narrator, focal character, other characters, and analyst knowledge distinct. Explanation, justification, and narrative endorsement must also remain distinct.

### 5.2 Evidence IDs

Assign local stable IDs such as `RAG-E-V001-001` to analytically diagnostic observations. IDs are not global character-registry IDs. The volume reading owns each observation's primary analytical entry; cumulative ledgers cite that ID rather than reproducing the same observation as independently discovered evidence.

A recoverable evidence record includes:

```yaml
evidence_id: RAG-E-V001-001
witness_id: null          # Resolve from the verified source inventory.
volume: V001
chapter_label: null      # Exact edition label, not a guessed global number.
printed_page: null
file_page_or_image: null
panel_region: null       # Reading-order index or an unambiguous description.
representation: null     # event / spoken / interior / imagined / visual_form / paratext
observation: null
claim_class: OBSERVATION
interpretive_limit: null
```

This is a documentation template, not a populated record or a new global machine schema. Replace nulls only with verified information. At minimum, source identity plus a recoverable chapter/page or image location is required for consequential claims. Printed page and file index must not be silently conflated. For unnumbered pages, record the image index or other stable witness locator.

Where useful, create explicit Markdown anchors such as `rag-e-v001-001`; verify links rather than assuming generated heading anchors will match. Short quotations should be exact, limited to what the analysis needs, and attributed to the inspected language witness. Paraphrases are labeled as paraphrases.

### 5.3 Efficient granularity

Every chapter and narrative scene must be accounted for, but not every panel needs an independent record. Give ordinary continuity a concise scene index. Give diagnostic decisions, contradictions, formal effects, or developmental changes close analysis and exact locators. A volume-sized paraphrase of all dialogue is neither necessary nor desirable.

## 6. Reading manga as manga

Full declared volume coverage requires actual access to and inspection of the narrative pages, in legible order. A transcript-only pass cannot certify a full visual deep reading. Contact sheets are useful for orientation but do not replace readable pages when facial detail, wording, or sequencing matters.

Check page order, missing pages, duplicate images, cropped text, spreads, edition pagination, and any mismatch between extracted text and the page. Use built-in visual inspection when available. OCR is a fallback when necessary, not a default substitute; consequential readings of uncertain text must be checked against the image.

Inspect the relation between text and image: viewpoint, panel size, reaction timing, juxtaposition, silent intervals, imagined scenes, beauty emphasis, comic deformation, framing of bodies, and page-turn information. A large panel may prolong attention without advancing story time. A fantasy panel does not establish an event, intention, or consent in the story world.

Track how the manga gives or withholds access to a person. Do not confuse a focal character's idealization with an objective characterization of its object. Nor should every romantic image be assumed to be an ironic critique: establish the formal basis for the interpretation.

Speech balloons, typography, ellipses, written hesitation, and linguistic register can support a **written speech model**. They do not establish acoustic timbre, performed pitch, breathing, or a voice actor's delivery. Anime performance is a separately scoped evidence channel, not a mandatory condition for this manga project.

## 7. Twelve analytical lenses

These are questions to test, not twelve mandatory essays in every volume. Use depth proportional to the evidence; explicitly mark a reviewed domain with no material update rather than padding it.

### 7.1 Narrative causality

What occurs, what motivates it, which options were available, and what consequences follow? Distinguish coincidence, character initiative, and external pressure. Ask what the scene makes possible or impossible that was not already true.

### 7.2 Character state

Capture desires, beliefs, self-conceptions, competencies, fears, commitments, and regulation strategies. Separate stable tendencies, temporary states, learning, changed circumstances, and new access to previously hidden information.

### 7.3 Directed relationship state

Model A's understanding of B separately from B's understanding of A. Separate public label, private acknowledgment, demonstrated conduct, and each party's beliefs. A change in one person's understanding is not automatically a jointly acknowledged transition.

### 7.4 Agency and initiative

Who initiates, refuses, delays, repairs, takes a risk, incurs a cost, or creates an option? Record the available opportunity and competing constraints. Interior intensity does not equal external action; reserved presentation does not prove passivity. Help received and agency exercised can coexist.

### 7.5 Transaction and intimacy

Distinguish contractual service, payment, gifts, uncompensated favors, professional boundaries, family obligations, emotional labor, and voluntary care. Record what was agreed, what was assumed, and what remains ambiguous. Payment does not buy unlimited access; a favor does not by itself create romantic entitlement. Conversely, commercial form alone does not settle whether a particular feeling is authentic.

### 7.6 Information and deception

For each significant proposition, distinguish truth as represented, what each person knows, what they believe, what they falsely believe another person knows, and what they disclose. Distinguish fabrication, omission, uncorrected misunderstanding, strategic ambiguity, and genuine ignorance. Record the costs and incentives of maintaining a false account.

### 7.7 Progress and regression

Measure change by a named dimension and baseline, not by a general impression that the relationship is closer to an ending. Capture informational, behavioral, emotional, relational, material, and social changes. An intention is not implementation; a private recognition is not a public agreement.

### 7.8 Chronology

Record explicit dates, relative intervals, holidays, birthdays, semesters, seasons, and continuity constraints. Distinguish hard anchors, bounded inferences, loose seasonal cues, and unknown durations. Record event order independently of exact dating. Do not turn art, clothing, or a publication date into a certain story date.

### 7.9 Kazuya's cognition

Use `represented thought -> interpretation -> emotion -> options -> inhibition -> action -> consequence -> self-account`. Test whether negative self-evaluation, fantasy, and anxious interpretations accurately describe what he actually does. Both flattering and unflattering counterevidence matter. Do not presume that his self-criticism is either entirely reliable or entirely misleading.

### 7.10 Chizuru's observable and reported states

Use `observable conduct -> verbal account -> private conduct where shown -> formal/affective cues -> alternatives -> minimum warranted inference`. Ask what the evidence establishes without assigning a complete hidden motive. Track differences between professional presentation, personal disclosure, voluntary behavior, and others' readings of her. Opacity can remain unresolved.

These are evidence-access strategies, not permanent stereotypes: if later volumes change access to either character's interiority, update the observation method prospectively.

### 7.11 Repetition and callbacks

Index repeated situations by their concrete mechanism: interruption, proximity, embarrassment, misunderstanding, boundary negotiation, reassurance, or another discovered pattern. Compare entering state, available information, choices, and consequences. Distinguish a callback, altered recurrence, reversal, reset, and genuinely redundant recurrence. Do not assume all similar scenes perform the same work.

### 7.12 Formal framing and reader position

Track visual rhetoric, comedic targets, romantic attention, discomfort, dramatic irony, the distribution of interior access, and the management of uncertainty. Separate the analyst's reading experience from claims about audiences generally. A theory of reader frustration is not evidence of how actual readers responded.

## 8. Operational progress, repetition, and time analysis

A progress record should contain an event ID, domain, prior state, observed change, agents who know or acknowledge it, immediate consequence, durability **as of the current boundary**, and later revision links. Use `GAIN`, `LOSS`, `RECONFIGURATION`, `NO_DEMONSTRATED_CHANGE`, or `UNRESOLVED` relative to the named construct. Do not add different domains into one romance score.

Use a durable-change test: does subsequent eligible evidence continue to constrain choices, preserve acquired knowledge, maintain a commitment, alter a practice, or produce an irreversible consequence? At the moment a change occurs, its future durability may be unknown. A later reversal is a new row or revision event, not evidence the original change never happened.

At checkpoints, discriminate among:

- slow accumulation;
- cyclical development with retained changes;
- escalation followed by reversal;
- changed states expressed through familiar situations;
- genuine restoration of the earlier conditions;
- insufficient evidence to distinguish those possibilities.

Page counts, chapters devoted to an event, and elapsed story time can provide descriptive comparisons. Explain the counting convention, coverage, and uncertain dates. Do not claim objective literary quality from those counts or infer publication strategy from length alone.

Chronology must preserve incompatible anchors as conflicts rather than forcing one neat calendar. A single exact elapsed-time total is not required when the source supports only a range.

## 9. Character reconstruction begins during reading

Begin bounded reconstruction as soon as meaningful evidence permits it; do not wait until the final block. Capture ordinary conduct as carefully as crisis behavior: conversational openings, listening, small preferences, humor, politeness, apologies, work habits, use of money and time, and giving or receiving help.

For each active substantial character, maintain the evidence/state ledger and working operational model defined by the reconstruction specification. Minor figures can remain in the cast router with links to local evidence until a separate artifact has a real responsibility. Do not manufacture a monograph for every name.

Every consequential model rule must state its applicable source state and relationship conditions, supporting observations, counterevidence or an explicit coverage gap, likely alternatives, and confidence. The model should explain behavior under specified pressures, not reduce the person to adjectives or a clinical label.

At each completed volume, inspect the existing models for material updates. No-change judgments are legitimate. Do not rewrite every model in full, manufacture psychometric numbers, or invent a preference merely to fill a schema.

## 10. Per-volume transaction and required reading contents

### 10.1 The transaction

1. Verify the current project state, source witness, unit order, authorization, and entering freeze.
2. Inspect all in-scope pages; maintain chapter/scene coverage and exact diagnostic locators.
3. Write the deep reading and classify observations, reports, interpretations, and remaining uncertainties.
4. Update the applicable cumulative ledgers, character evidence/models, claims, and prior predictions.
5. Freeze the exiting state; verify links, names, chronology, source boundary, and completion claims.
6. Update the single current entrypoint and record any interrupted subwork or evidence debts.
7. Perform the required repository checks and authorized atomic persistence. Verify the committed high-water mark before beginning another volume.

A standalone essay without synchronized state is not a closed volume. A drafted or locally saved volume is not automatically a committed volume. Repository publication, main integration, and analytical completion are separately recorded.

### 10.2 Deep-reading template

Each `RAG_VNNN_DEEP_READING.md` contains:

- complete authority metadata, exact source witness/coverage, entering and exiting boundaries;
- a substantive volume thesis, proportional to the material, not a verdict imposed from reputation;
- an ordered chapter/scene map accounting for the whole narrative volume;
- close readings of diagnostic scenes with stable evidence IDs;
- causal, character, directed-relationship, information, agency, transaction, and temporal deltas;
- manga-form and written-speech analysis where supported;
- progress/repetition findings and the strongest alternative readings;
- a character-model change log or explicit reviewed/no-material-change results;
- prediction adjudication, open questions, and consequential claim revisions;
- exact ledger/model destinations updated, coverage debts, exiting freeze, and next eligible operation.

These are semantic responsibilities, not a demand for an identical wall of headings. The prose must explain mechanisms and integrate evidence. No fixed word ceiling or floor substitutes for that obligation.

## 11. Ten-volume checkpoint method

Stop before admitting the next block's narrative content. Close V010, V020, and subsequent ten-volume boundaries with one checkpoint containing two clearly separated views: **the new block's contribution** and **the cumulative interpretation through this endpoint**. A terminal residual checkpoint uses its actual final volume and is explicitly partial.

The checkpoint must answer what earlier interpretation survives, strengthens, changes, loses support, or remains unresolved; what is durable versus momentary; which narrative systems and emergent arcs now explain the sequence; and how character-reconstruction coverage changed.

Use the revision vocabulary `PRESERVE`, `STRENGTHEN`, `REVISE`, `DOWNGRADE`, `REJECT`, and `OPEN`. Keep historical interpretations recoverable. Include difficult counterexamples, not just confirming highlights.

Run the local reconstruction audit specified in the companion document. Dispatch substantial monographs or specialist synthesis when evidence is ready, not only at an arbitrary late volume. A sparse character remains bounded even if the overall corpus is large.

## 12. Ethics, reception, and comparison

Record consent, refusal, obligations, deception, vulnerability, objectification, and recognition of others as interpretive questions where relevant. Do not turn embarrassing thoughts into a completed action, or sympathetic intent into evidence that harm did not occur.

PACTRIH is an optional separately governed specialist layer, not the default organizing axis of this romance study. Read its current foundational specification and canonical data before any formal use. Keep its dimensions separate; do not infer a single morality score or invent a calibration from this method.

External comparisons and the owner's social-counterfactual experiments should use the admitted, state-specific model. Generated dialogue and hypothetical outcomes are validation or illustrative material, never manga evidence. Formal reception analysis or claims about author intent require separately retrieved, attributed sources and a declared post-freeze research boundary.

## 13. Quality and failure controls

Material blockers include missing narrative pages, unreadable load-bearing text, an unavailable required visual inspection route, unresolved source identity, a contradictory high-water mark, and an unsatisfied initiation gate. Preserve valid work and record the affected requirement; do not silently downgrade full-volume analysis to a summary-only pass.

An ambiguity in a character's motive is ordinarily an analytical result, not a reason to halt a run. A genuine contradiction can remain open. Distinguish missing evidence from affirmative disconfirming evidence, and partial coverage from a demonstrated absence.

When a session becomes unreliable, close the current coherent unit where feasible and externalize state. A handoff must contain the actual analytical artifacts or verified retrieval routes, not only a synopsis. Do not promise that one chat or agent invocation will finish all ten volumes without interruption.

## 14. Governance references and adoption

The design uses the owner's decisions in this conversation, the supplied project source map, and live repository rules inspected on 2026-09-19. It adds implementation detail, not manga findings. Re-read the live versions before adoption; the repository was not modified by preparing this file.

Relevant repository paths:

- `AGENTS.md`
- `governance/policies/CHANGE_INTEGRATION_CHECKLIST.md`
- `governance/source-policies/MANGA_ANIME_PROJECT_INITIATION_AND_ARCHITECTURE_POLICY.md`
- `governance/source-policies/MANGA_ANIME_SEQUENTIAL_EXECUTION_SCOPE_AND_CONTINUATION_POLICY.md`
- `governance/source-policies/MANGA_ANIME_LONG_SERIES_HYBRID_EXECUTION_PROTOCOL.md`
- `governance/source-policies/MANGA_ANIME_EXECUTION_TOPOLOGY_AND_CAPABILITY_ROUTING_POLICY.md`
- `governance/source-policies/MANGA_ANIME_ANALYTICAL_HANDOFF_AND_INTEGRATION_CONTRACT.md`

Repository reference: https://github.com/deep-blue-zero/anime-manga-ln-games-analysis/tree/6d027e55f2eb38ec04ceed16bddc25015dc8a180

### Revision note

This formalization preserves the agreed sequential method and ten-volume cadence. It replaces the earlier illustrative Volume 30/40 monograph thresholds with evidence-based readiness; separates operational models from literary monographs; and replaces mutable "Current" endpoint names with exact bounded identities. None of those refinements grants repository write authority or asserts that source analysis has begun.
