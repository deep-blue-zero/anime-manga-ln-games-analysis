---
title: Generic Source-Bounded Novel Analytical Method
artifact_id: GENERIC_NOVEL_ANALYTICAL_METHOD
artifact_type: generic_novel_analytical_method_reference
artifact_role: reusable_corpus_level_analytical_reference_method
version: "1.0"
status: canonical
scope: source-bounded reading of light novels, novels, web novels, and branching prose, and new-project method bootstrap
authority_scope: this_reusable_reference_only
adoption: opt_in
project_local_authority: false
created: 2026-10-24
maintainer: Claude + user
source_boundary: "Methodological reference only; no series findings or primary-source evidence"
do_not_use_as_current_authority: false
do_not_use_as_literary_evidence: true
canonical_home: governance/analytical-methods/GENERIC_NOVEL_ANALYTICAL_METHOD.md
drafted_against_commit: 6a3afaaf1bb61e0993db379ab4074c46e9ea98dd
supersedes: []
superseded_by: []
---

# Generic Source-Bounded Novel Analytical Method

## Adoption and authority boundary

This artifact is a reusable, corpus-level analytical reference for source-bounded, blind-compatible reading of prose fiction: light novels, novels, and web novels. It also supports new-project method design. Games, including visual novels, live-service games, and extracted game data, use the [generic game method](GENERIC_GAME_ANALYTICAL_METHOD.md), which builds on this method's prose-reading discipline. It is canonical only for this reference responsibility, and adoption is opt-in. It is not a repository policy, a project-local governing method, a synthesis architecture, a current-state entrypoint, or literary evidence.

1. It does not govern an existing series merely by residing in Git.
2. It does not by itself satisfy a project's governing-method requirement or open a `SEQUENTIAL_ANALYSIS_LOCK`.
3. A new project adapts or authors its own method after source reconnaissance, pairs it with a synthesis architecture (see the [architecture template](GENERIC_MULTI_DOCUMENT_SYNTHESIS_ARCHITECTURE_TEMPLATE.md)), and exposes both through its entrypoint.
4. Mature projects remain governed by their current methods.
5. Optional modules are activated only when the source earns them.

Prose is inspected in the `TEXT` lane, with `STILL_IMAGE` for illustrations ([routing policy](../source-policies/MANGA_ANIME_MEDIUM_AND_INSPECTION_LANE_ROUTING_POLICY.md)). Comparing a novel with its adaptation is a separate method, outside this one.

## 0. Purpose

This method governs the close reading of a prose volume or part when no series-specific framework exists. It reconstructs what the text establishes through:

- narration and its mode, focalization, and reliability;
- dialogue and source-language wording;
- represented interiority;
- character behavior, decisions, and relationships;
- institutions, world state, and information;
- the order in which the text discloses what it knows;
- recurrence, causality, and counterevidence.

The governing principle is:

> **Explain what this unit makes available to an attentive reader at this point in the work, through whose perception and in what order it is disclosed, and what remains genuinely unresolved.**

---

# I. Epistemic boundary

## 1. Sequential seal

For a unit designated `U`, the semantic evidence boundary is all authorized source material up to and including `U`, and nothing later. If the reading is unit-isolated, the boundary is `U` alone.

Later knowledge may not explain current behavior, identify foreshadowing as such, resolve ambiguity, assign eventual motives, or rank details by later importance.

The default is **prospective**. A retrospective reading is permitted only when explicitly designated, is written in a separately labeled section or artifact, and is never used in blind mode.

## 2. Exposure disclosure and quarantine

A fresh session is not a clean reader. Before reading, record what the analyst already knows about the work and exclude it. Distinguish source-established fact, source-supported inference, interpretive hypothesis, open question, and external knowledge. Never silently convert remembered knowledge into source-derived inference.

## 3. Disclosure frontier within a unit

The default unit is the volume, or the work's natural part. Within it, keep chapter-level disclosure frontiers: a late-chapter revelation does not explain an earlier chapter's scene in the prospective reading of that scene. Never use file or processing splits as boundaries.

## 4. Separate orders

Keep these orders distinct and say which one a claim depends on:

- **publication order**: when each part was released;
- **disclosure order**: the order in which the text reveals information;
- **story chronology**: when events occur in the story world;
- **character knowledge**: when each character learns what;
- **admission order**: when the project admitted each source.

Side stories and extras carry both a release position and a story position.

---

# II. Source witnesses

## 5. Witness identity

Identify the exact edition read: language, publisher, format (print, EPUB, PDF, web page capture), revision, and a hash of the file. A different hash is a different witness until shown otherwise. A web page that can change is a dated witness: record when it was captured. Package metadata never overrides the visible text.

Keep separate states: present, transported, verified, admitted, inspected, closed.

## 6. Witness roles

| Witness | Role |
|---|---|
| Original-language text | Governs wording, register, and narration claims |
| Translation | Navigation aid; never silently fills a gap |
| Web-novel or earlier edition | Separate witness; textual-history evidence (Section 30) |
| Revised or collected edition | Governs its own text |
| Illustrations | Paratext that never overrides the prose (Section 13) |
| Afterwords, author notes, interviews | Creator statements: intent evidence only, never character testimony |
| Official companion books | Classified by component |
| Adaptations, prior analyses, reception | Excluded or hypothesis indexes only |

## 7. Coverage

Classify every item in the witness (each spine member of an EPUB, each section of a document) before reading: narrative, illustration, afterword, preview, advertisement, bonus, front or back matter. Keep a coverage table recording each narrative section's focalizer, admission class, and inspection state.

Search is not coverage. A keyword hit is not a reading. Choose close-read scenes for their literary centrality, not only because they bear on a current hypothesis.

---

# III. Narration

## 8. Narrative mode

Identify the narrative mode, and watch for changes within a work: first person (present or retrospective); close third person, which absorbs a character's diction; free indirect discourse; omniscient, essayistic, or historiographic narration; frame narration and embedded narrators; epistolary or documentary forms.

## 9. Focalization

For each claim, distinguish:

- what the narrator asserts;
- what the focal character knows or perceives;
- what another character reports;
- what the reader can establish from the text as a whole;
- what the analyst infers.

Record the focalizer for each section in the coverage table. A detail filtered through a focal character is evidence of that character's perception before it is evidence of the world.

## 10. Reliability

Audit reliability per epistemic act, not as a global label on the narrator. A narrator can report events accurately and misjudge motives, or perceive others sharply and themselves poorly. Ask: what does the narrator have access to here, what do they want to be true, and does the text supply evidence that diverges from their account? A narrator is not omniscient, not necessarily sincere, and not the author.

## 11. Interiority

Represented thought is the richest evidence prose offers and the easiest to over-read. Trace the chain where the text supports it: circumstance, evidence perceived, appraisal, affect, options considered, choice, consequence, later revision. Mark each link as explicit, inferred, or not shown. Where the text grants less interior access, make narrower claims.

## 12. Source-language wording

The original language governs claims about register, address, self-reference, sentence endings, politeness, and shifts from a character's baseline. A voice claim needs repetition, not a single line. Quote briefly with a labeled gloss.

Keep ruby base text distinct from its reading, and treat deliberate glosses (a word read as another) as meaning-bearing. Do not apply compatibility normalization to quoted text; if normalization is used for search, record the normalizer and its version.

---

# IV. Illustrations and paratext

## 13. Illustrations

Covers, color inserts, chapter illustrations, maps, and diagrams are paratext: they can corroborate, frame, or anticipate, but they never override the prose. Inventory them, record which were actually inspected, and declare partial modality honestly ("prose complete; illustrations not inspected"). An illustration placed before the scene it depicts can disclose later information; treat it as spoiler-bearing within the unit.

## 14. Paratext

Afterwords and author notes are creator statements, not character testimony. Publisher previews of the next volume and advertisements are excluded from the narrative projection. Retailer or edition bonuses are classified separately and admitted only by explicit decision.

---

# V. First-pass reconstruction

## 15. Entering state

Before reading a unit after the first, record:

- **prior-unit developments**: what is established entering this unit, written before reading it;
- **entering freeze**: character, relationship, and open-question state at entry.

## 16. Segmentation and causality

Divide the unit into dramatic movements by goal, location, configuration, revelation, or narrative-mode shift. For each, record the active characters, the entering state, the change, and the leaving state. Build a causal map, not a synopsis: distinguish coincidence, explicit causation, decision, institutional constraint, misunderstanding, information asymmetry, and interruption.

## 17. Characters

For each materially active character, distinguish stable disposition from current state, and record trigger, perceived stakes, decision rule, relationship-conditioned mode, self-description versus observed behavior, and counterevidence. Treat low-stakes everyday scenes as first-class evidence. A crisis response is not a trait. A performed or learned behavior is not therefore fake. Describe before diagnosing; avoid clinical labels the work does not establish.

## 18. Relationships

Model relationships directionally: A toward B is not B toward A. Record knowledge, desire, and power asymmetries, trust, dependency, conflict, recognition, pressure, and reciprocity, and ask what becomes possible between the characters after this unit.

## 19. Information and knowledge

Track who knows what, when, and how they learned it. Many prose works turn on information asymmetry; a knowledge-state record separates what the reader knows from what each character knows.

## 20. Institutions and world state

Activate when material. Separate what an institution formally requires from what a character says it requires, what custom expects, and what characters assume. For speculative settings, separate world rules the text establishes from rules characters believe.

## 21. Theme

Derive theme from recurring conflict, not by assigning abstractions. Depiction, sympathy, and narrative success are not endorsement; explanation is not justification.

## 22. Sensitive content

For sexual or violent content, give the minimum description that supports the claim, with locators; do not reproduce it. Keep comic, erotic, relational, and ethical functions separate. Later affection does not establish earlier consent.

---

# VI. Evidence

## 23. Evidence labels

| Label | Meaning |
|---|---|
| `OBSERVATION` | Directly stated or shown by the text |
| `SELF_REPORT` | A character's own account of themselves |
| `NARRATOR_PRESENTATION` | The narrator's assertion or framing |
| `INFERENCE` | Supported by multiple observations |
| `HYPOTHESIS` | Fits the evidence but remains contestable |
| `CONTRADICTION` | The text supports incompatible readings |
| `EXTERNAL_REFERENCE` | Outside the boundary; excluded unless admitted |
| `EVALUATION` | The analyst's value judgment |
| `UNRESOLVED` | The unit does not settle it |

Pair a label with a confidence (`HIGH`, `MODERATE`, `LOW`, `UNRESOLVED`) and, where it matters, a source layer (original text, translation, illustration, paratext). Series vocabularies remain valid when they preserve these distinctions.

## 24. Quotation states

Mark each quotation: `EXACT_VERIFIED` (checked against the witness), `WORKING_TRANSCRIPTION` (not yet checked), or `PARAPHRASE`. Only `EXACT_VERIFIED` quotations support load-bearing wording claims.

## 25. Locator grammar

Pair a deterministic locator with a human-readable one:

```text
human:          <SERIES> V07 Ch.3 ¶42
deterministic:  <WITNESS-KEY>@sha256:<digest>::spine:9::member:<path>::p:0042::chars:118-164
```

- Spine and member identify the EPUB section; a paragraph index or anchor identifies the passage; a character range and, optionally, a hash of the selected text pin it exactly.
- Reflowed pages are not print pages. Cite printed page numbers only from a fixed-layout witness.
- Retrieval-test load-bearing locators: confirm that the locator actually returns the cited text.

A missing locator is better than a false one. A locator marked `pending_backfill` cannot support a benchmark claim.

## 26. Retrieval aids and the public boundary

Search results and extracts are retrieval aids, not reading. Reopen the passage before a contested or quoted claim. Source text in bulk stays in the evidence plane, outside Git; readings carry locators and brief quotations. Prior analyses are hypothesis indexes, not evidence.

---

# VII. Counterevidence and closure

## 27. Counterreading

Every governing interpretation answers: what evidence would make this weaker? Generate at least one plausible counterreading for the unit's thesis, including one that takes the narrator's account less on trust. Classify major claims: strongly supported, supported but contestable, provisional, open, contradicted. `OPEN` is a valid result.

## 28. Claim transitions

When later units pressure earlier claims, use `PRESERVE`, `STRENGTHEN`, `REVISE`, `DOWNGRADE`, `REJECT`, or `OPEN`, recorded as dated revisions. Never rewrite an entering or exit freeze.

---

# VIII. Unit output

## 29. Required structure

- **A. Receipt and witness**: edition, hash, admission, coverage table.
- **B. Entering state**: prior-unit developments and entering freeze.
- **C. Governing thesis**, with a competing thesis where one is live.
- **D. Movement-by-movement causal reading**, noting disclosure order.
- **E. Narration**: mode, focalization, reliability findings.
- **F. Character changes**, with interiority evidence marked.
- **G. Relationship changes.**
- **H. Information and knowledge changes.**
- **I. Optional domain modules**, only as earned.
- **J. Language and register.**
- **K. Illustrations and paratext**, with inspection status.
- **L. Motifs and recurrence** inside the boundary.
- **M. Counterreadings.** Mandatory.
- **N. Claim transitions and forecast dispositions.**
- **O. Ledger manifest**: the updates made, with an explicit "no material change" where none applies.
- **P. Exit freeze.**
- **Q. Limitations and completion decision.**

Use stable claim and evidence IDs; never renumber them. The reading owns its observations; ledgers cite them.

---

# IX. Optional modules

Activate only when the source earns them.

## 30. Textual history

Where a work exists in several versions (web novel and light novel; serialized and revised editions; platform revisions), keep a textual-history lane separate from the main reading:

- treat each version as a dated witness;
- record variants by type (addition, deletion, substitution, relocation, restructuring) without assuming why they were made;
- distinguish author, publisher, and platform as possible agents of change;
- state which version governs which claims.

A variant's operation is not its explanation.

## 31. Branching prose

Where a prose work itself branches (gamebooks, multiple-ending novels, interactive fiction published as text), keep state per branch: what is true on one branch is not true on another. Locate by branch and section. For games, including visual novels, use the [generic game method](GENERIC_GAME_ANALYTICAL_METHOD.md), which covers routes, variants, live-service intake, and extracted data.

## 32. Multiple states of one character

Where a work has loops, resets, dreams, possession, alternate selves, or similar devices, keep explicit state bookkeeping: which instance of the character, in which state, knows and has done what.

## 33. Names, puns, and wordplay

Where names, ruby glosses, puns, or invented terms carry meaning, treat them as textual objects with their own entries, quoting the source form.

---

# X. Blind-analysis mode

## 34. Identity minimization

Where practical, remove from the analyst's package: series titles in filenames and EPUB metadata, covers, title and copyright pages, colophons, afterwords, author notes, next-volume previews, and advertisements. Character names in the prose cannot be removed; pseudonymization is optional and applies only to the analyst's prose and supplied materials. When pseudonymization is in use, it overrides the repository's named-subject standard for that run.

Record what the analyst recognized. Blind mode is procedurally prospective, not a guarantee of epistemic blindness.

## 35. Generic-framework restriction

The analyst receives this method, the source text, technical provenance, and translations if used. It does not receive series-specific theses, ledgers, future information, character monographs, or other analyses.

## 36. Modality-ablation benchmark

Run independent passes:

- **Pass A, prose only.**
- **Pass B, prose with illustrations.**
- **Pass C, translation only**, compared with a source-language pass, where testing translation dependence.

For each added condition record new claims, revised claims, confidence changes, false claims, and claims correctly left open. Measure epistemic improvement, not prose length.

---

# XI. Governing rules

1. **Observation precedes interpretation.**
2. **A focalized detail is evidence of perception before it is evidence of the world.**
3. **Reliability is judged per act, not per narrator.**
4. **Character belief is not world fact; a narrator is not the author.**
5. **Disclosure order is not chronology.**
6. **Later outcomes cannot solve earlier uncertainty.**
7. **Illustrations and paratext never override the prose.**
8. **Search is not coverage, and a hit is not a reading.**
9. **The source language governs wording claims.**
10. **Relationships are directional and conditional.**
11. **Counterevidence belongs inside the analysis.**
12. **A missing locator is better than a false one.**
13. **Use only the modules the unit earns.**

---

# Repository context

- [Medium and inspection-lane routing policy](../source-policies/MANGA_ANIME_MEDIUM_AND_INSPECTION_LANE_ROUTING_POLICY.md): lanes and reference methods by medium.
- [Project initiation and architecture policy](../source-policies/MANGA_ANIME_PROJECT_INITIATION_AND_ARCHITECTURE_POLICY.md): project-local method and architecture requirements; Sections 12.3–12.4 on novels and branching narratives.
- [Generic multi-document synthesis architecture template](GENERIC_MULTI_DOCUMENT_SYNTHESIS_ARCHITECTURE_TEMPLATE.md): the paired architecture.
- [Generic character reconstruction method](GENERIC_CHARACTER_RECONSTRUCTION_METHOD.md): optional downstream modeling.
- [Analytical handoff contract](../source-policies/MANGA_ANIME_ANALYTICAL_HANDOFF_AND_INTEGRATION_CONTRACT.md): Section 15, named subjects and referential clarity.
- [Change-integration checklist](../policies/CHANGE_INTEGRATION_CHECKLIST.md): authorized paths, validation, and publication.
