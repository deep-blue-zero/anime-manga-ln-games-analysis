---
title: Generic Source-Bounded Manga Analytical Method
artifact_id: GENERIC_MANGA_ANALYTICAL_METHOD
artifact_type: generic_manga_analytical_method_reference
artifact_role: reusable_corpus_level_analytical_reference_method
version: "1.0"
status: canonical
scope: source-bounded manga, manhwa, and manhua reading, and new-project method bootstrap
authority_scope: this_reusable_reference_only
adoption: opt_in
project_local_authority: false
created: 2026-10-24
maintainer: Claude + user
source_boundary: "Methodological reference only; no series findings or primary-source evidence"
do_not_use_as_current_authority: false
do_not_use_as_literary_evidence: true
canonical_home: governance/analytical-methods/GENERIC_MANGA_ANALYTICAL_METHOD.md
drafted_against_commit: 6a3afaaf1bb61e0993db379ab4074c46e9ea98dd
supersedes: []
superseded_by: []
---

# Generic Source-Bounded Manga Analytical Method

## Adoption and authority boundary

This artifact is a reusable, corpus-level analytical reference for source-bounded, blind-compatible reading of manga and other sequential art (manhwa, manhua, webtoons), and for new-project method design. It is canonical only for this reference responsibility, and adoption is opt-in. It is not a repository policy, a project-local governing method, a synthesis architecture, a current-state entrypoint, or literary evidence.

1. It does not govern an existing series merely by residing in Git.
2. It does not by itself satisfy a project's governing-method requirement or open a `SEQUENTIAL_ANALYSIS_LOCK`.
3. A new project adapts or authors its own method after source reconnaissance, pairs it with a synthesis architecture (see the [architecture template](GENERIC_MULTI_DOCUMENT_SYNTHESIS_ARCHITECTURE_TEMPLATE.md)), and exposes both through its entrypoint.
4. Mature projects remain governed by their current methods.
5. Optional modules are activated only when the source earns them.

Manga is inspected in the `STILL_IMAGE` lane, with `TEXT` for lettering transcripts and translations ([routing policy](../source-policies/MANGA_ANIME_MEDIUM_AND_INSPECTION_LANE_ROUTING_POLICY.md)). An anime adaptation is a different source; comparing the two is a separate method, outside this one.

## 0. Purpose

This method governs the close reading of a manga volume or chapter when no series-specific framework exists. It reconstructs what the source establishes through:

- dialogue, narration, and other lettered text in the source language;
- drawn action, expression, and composition;
- panel, page, and spread design, and the reading rhythm they impose;
- character behavior, decisions, and relationships;
- institutions and social organization;
- recurrence, causality, and counterevidence.

The governing principle is:

> **Explain what this unit makes available to an attentive reader at this point in the work, how its pages make that meaning available, and what remains genuinely unresolved.**

---

# I. Epistemic boundary

## 1. Sequential seal

For a unit designated `U`, the semantic evidence boundary is all authorized source material up to and including `U`, and nothing later. If the reading is unit-isolated, the boundary is `U` alone.

Later knowledge may not explain current behavior, identify foreshadowing as such, resolve ambiguity, assign eventual motives, or rank details by later importance.

The default is **prospective**. A retrospective reading is permitted only when explicitly designated, is written in a separately labeled section or artifact, and is never used in blind mode.

## 2. Exposure disclosure and quarantine

A fresh session is not a clean reader. Before reading, record what the analyst already knows about the work (franchise exposure, adaptations seen, remembered events) and exclude it.

Distinguish:

- **source-established fact**;
- **source-supported inference**;
- **interpretive hypothesis**;
- **open question**;
- **external or prior knowledge**, excluded unless explicitly admitted.

Never silently convert remembered knowledge into source-derived inference.

## 3. Disclosure frontier within a unit

The default unit is the volume. Within it, keep chapter-level disclosure frontiers: an end-of-volume reveal does not explain an earlier chapter's scene in the prospective reading of that scene. Use the work's natural parts, never file or processing splits, as boundaries.

---

# II. Source witnesses

## 4. Witness identity

Identify the exact edition read: language, publisher, format (print scan, digital volume, magazine or web chapter), and a hash of the file or package. A different hash is a different witness until shown otherwise. Package metadata never overrides what the pages visibly show.

Keep separate states for each witness: present, transported, verified, admitted, inspected, closed. A file that is present has not thereby been read.

## 5. Witness roles

Decide which witness answers which question:

| Witness | Role |
|---|---|
| Original-language edition | Governs wording, register, and lettering claims |
| Translation | Navigation aid; never silently fills a gap in the original |
| Magazine or web serialization | Separate witness; revision evidence where the collected edition differs |
| Collected (tankobon) edition | Governs that edition's text and art, including revisions |
| Official companion books | Classified by component: data, editorial, fiction, creator statement, technical |
| Creator statements | Evidence of intent only, never of what the work establishes |
| Adaptations, prior analyses, reception | Excluded or hypothesis indexes only |

Never derive collected-edition chapter numbers arithmetically from serialization numbers; use an explicit crosswalk.

## 6. Volume apparatus

Classify collected-edition extras by function: covers, inside covers, joke pages, character profiles, omake strips, author notes, afterwords. A joke page is not a diegetic fact. A character profile is paratext, not narrative evidence, unless the method admits it explicitly. Covers, title pages, colophons, and next-volume previews can carry later information; treat them as spoiler-bearing.

---

# III. Evidence

## 7. Evidence labels

Use labels when a claim's status could blur:

| Label | Meaning |
|---|---|
| `OBSERVATION` | Directly visible on the page: drawn action, composition, lettered text |
| `SELF_REPORT` | A character's own account of themselves |
| `NARRATOR_PRESENTATION` | Narration boxes or framing text |
| `INFERENCE` | Supported by multiple observations |
| `HYPOTHESIS` | Fits the evidence but remains contestable |
| `EXTERNAL_REFERENCE` | Outside the boundary; excluded unless admitted |
| `EVALUATION` | The analyst's value judgment |
| `UNRESOLVED` | The unit does not settle it |

Pair a label with a confidence (`HIGH`, `MODERATE`, `LOW`, `UNRESOLVED`) and, where it matters, a source layer (original text, translation, companion book). Series vocabularies remain valid when they preserve these distinctions.

## 8. Text layers

Distinguish:

- speech balloons, by balloon shape (spoken, shouted, whispered, electronic, shared);
- thought balloons and interior monologue;
- narration boxes, distinguishing a present narrator from a retrospective one, and both from publisher or editorial captions;
- handwritten or small asides outside balloons;
- diegetic text: signs, screens, letters;
- sound effects (Section 11).

Attribute speech by tail, position, and context. Where attribution is uncertain, say so.

## 9. Source-language register

For claims about address, self-reference, sentence endings, politeness, and shifts from a character's baseline, the source language governs. A voice claim needs repetition, not a single line. Quote briefly with a labeled gloss. Furigana and ruby are textual objects: keep the base text distinct from its reading, and treat deliberate glosses (a word read as another) as meaning-bearing.

## 10. What a page cannot establish

Lettering is not acoustic delivery: bold type, size, or a trembling balloon edge is a graphic convention, not a measured voice. One drawn expression does not establish a unique emotion. A sequence of panels suggests a trajectory but does not show its execution; do not infer motion between omitted moments.

## 11. Sound effects and onomatopoeia

Sound effects (giongo for sounds, gitaigo for states or manners, such as silence or a stare) are drawn text with their own evidentiary role:

- record the source-language form, and translate it only as a gloss;
- distinguish sound from state or manner effects; a gitaigo effect can describe atmosphere or interior state rather than any audible event;
- note placement, size, and whether the effect is integrated into the art or overlaid;
- in translated editions, record whether the effect was replaced, subtitled, or left untranslated, since replacement changes the page.

Do not treat a sound effect as evidence of what a scene sounds like beyond the convention it uses.

## 12. Rendering registers

Manga shifts drawing register for effect: detailed hyper-rendering, ordinary style, simplified or super-deformed (chibi) comic register, and symbolic abstractions (sweat drops, anger marks, blank eyes). Treat a register shift as a framing choice, usually signaling comic distance or emotional emphasis, not as a literal event. A character drawn in chibi register has not changed size, and a gag-register beating does not carry the consequences a realistic one would. Note when the work breaks its own register conventions; those breaks are often load-bearing.

---

# IV. Form

## 13. Scales of form

Analyze at the scale that carries the effect: panel, page, spread, chapter, series. For each formal claim, describe the feature, then its effect, then an alternative explanation. Repetition is not a deliberate motif by default; require recurrence with a plausible relation between occurrences.

## 14. Reading order and the page turn

Reading order follows the inspected edition: right-to-left for Japanese manga; left-to-right for most translations and Korean webtoons; top-to-bottom scroll for vertical formats.

Before claiming that a reveal lands on a page turn, check the facing-page layout of the edition read. A single-image display or a reflowed digital edition changes which pages face each other. Keep double-page spreads whole as one evidence object.

## 15. Panel grammar

For high-value pages ask:

- How do panel size, shape, and count control pacing?
- What do gutters elide, and how much time do they imply?
- Where are borderless, bleeding, or broken-frame panels used, and why?
- Whose gaze or point of view organizes the sequence?
- When does a page withhold a face, a reaction, or a background?
- When does a silent panel or silent page carry the scene?

Read silent and OCR-resistant pages as fully as text-heavy ones.

## 16. Composition and visual grammar

Track framing, distance, height, center and periphery, grouping and isolation, barriers, screentone and shading, line weight, and backgrounds dropped away for emphasis. Color pages, where present, are part of the edition: never strip them, and note when color is used for effect rather than as a magazine convention.

Do not assign symbolism merely because an image is striking; require recurrence or clear dramatic alignment.

---

# V. First-pass reconstruction

## 17. Entering state

Before reading a unit after the first, record:

- **prior-unit developments**: what is established entering this unit, written before reading it;
- **entering freeze**: the character, relationship, and open-question state at entry.

## 18. Segmentation and causality

Divide the unit into dramatic movements by goal, location, configuration, revelation, or formal shift. For each, record the active characters, the entering state, the change, and the leaving state. Build a causal map, not a synopsis: distinguish coincidence, explicit causation, decision, institutional constraint, misunderstanding, information asymmetry, and interruption.

## 19. Characters

For each materially active character, distinguish stable disposition from current state, and record trigger, perceived stakes, decision rule, relationship-conditioned mode, self-description versus observed behavior, and counterevidence. Treat low-stakes everyday scenes as first-class evidence. A crisis response is not a trait. A performed or learned behavior is not therefore fake. Describe before diagnosing; avoid clinical labels the work does not establish.

## 20. Relationships

Model relationships directionally: A toward B is not B toward A. Record knowledge, desire, and power asymmetries, trust, dependency, conflict, recognition, pressure, and reciprocity, and ask what becomes possible between the characters after this unit that was not possible before.

## 21. Institutions and groups

Activate when material. Separate what an institution formally requires from what a character says it requires, what custom expects, and what characters assume. A confident gatekeeper does not automatically speak for the institution.

## 22. Theme

Derive theme from recurring conflict, not by assigning abstractions. Depiction, sympathy, and narrative success are not endorsement; explanation is not justification.

## 23. Sensitive content

For sexual or violent content, give the minimum description that supports the claim, with locators; do not reproduce it. Keep comic, erotic, relational, and ethical functions separate. Later affection does not establish earlier consent.

---

# VI. Counterevidence and closure

## 24. Counterreading

Every governing interpretation answers: what evidence would make this weaker? Generate at least one plausible counterreading for the unit's thesis. Classify major claims: strongly supported, supported but contestable, provisional, open, contradicted. `OPEN` is a valid result.

## 25. Claim transitions

When later units pressure earlier claims, use `PRESERVE`, `STRENGTHEN`, `REVISE`, `DOWNGRADE`, `REJECT`, or `OPEN`, recorded as dated revisions. Never rewrite an entering or exit freeze.

---

# VII. Locators and evidence handling

## 26. Locator grammar

Pair a deterministic locator with a human-readable one:

```text
<WITNESS-KEY> / V05 / Ch.38 / i0112 / p<printed label, if visible> / panel 3 / balloon 2
```

- `iNNNN` is the one-based image occurrence in the witness's reading order, including covers; it is stable for that witness.
- The printed page label is recorded only if visible on the page; digital page indexes are not print pages.
- Panel and balloon numbers are analyst-assigned in reading order; state the convention.
- Crops record their region coordinates.

A missing locator is better than a false one. A locator marked `pending_backfill` cannot support a benchmark claim.

## 27. Page review states

Record each page's review state: `REVIEWED_MATERIAL`, `NO_MATERIAL_ADDITION`, `DUPLICATE`, `EXCLUDED`, `UNRESOLVED_READABILITY`. Log legibility problems separately from archive validity.

## 28. Retrieval aids are not reading

OCR output, search hits, and keyword lists are retrieval aids. They are not quotation-grade text and not evidence that a page was read. Reopen the page image before a contested, visual, or quoted claim.

## 29. Public-repository boundary

Page images, OCR dumps, and bulk dialogue stay in the evidence plane, outside Git. The reading carries locators and brief quotations. Prior analyses are hypothesis indexes, not evidence.

---

# VIII. Unit output

## 30. Required structure

- **A. Receipt and witness**: edition, hash, admission, inspection coverage.
- **B. Entering state**: prior-unit developments and entering freeze.
- **C. Governing thesis**, with a competing thesis where one is live.
- **D. Movement-by-movement causal reading.**
- **E. Character changes.**
- **F. Relationship changes.**
- **G. Optional domain modules**, only as earned.
- **H. Language and register.**
- **I. Page form**: panel grammar, page turns, composition, sound effects, rendering registers, as consequential.
- **J. Motifs and recurrence** inside the boundary.
- **K. Counterreadings.** Mandatory.
- **L. Claim transitions and forecast dispositions.**
- **M. Ledger manifest**: the updates made, with an explicit "no material change" where none applies.
- **N. Exit freeze**: character, relationship, and open-question state at unit end.
- **O. Limitations and completion decision.**

## 31. Claim ledger

```text
Claim ID
Claim
Evidence and locators
Evidence label and confidence
Source layer
Counterevidence
Alternative explanation
Status
```

Use stable claim and evidence IDs; never renumber them. The reading owns its observations; ledgers cite them.

---

# IX. Optional modules

Activate only when the source earns them.

## 32. Vertical-scroll formats (webtoons, manhwa)

Vertical spacing replaces the page turn as the main pacing device: long gaps are elapsed time or suspense, and a panel's position in the scroll replaces its position on the page. Full-color art makes color and lighting primary channels. Locate by episode and scroll segment rather than by page.

## 33. Serialization and revision

Where magazine or web chapters and the collected edition differ, keep a crosswalk and treat superseded serialization text and art as revision evidence. Claims about a still-running work are provisional at the latest admitted chapter.

---

# X. Blind-analysis mode

## 34. Identity minimization

Where practical, remove from the analyst's package: series titles in filenames and metadata, covers, title pages, colophons, publisher logos, afterwords, author notes, next-volume previews, and advertisements. Character names in the art and lettering cannot be removed; pseudonymization is optional and applies only to the analyst's prose and supplied materials. When pseudonymization is in use, it overrides the repository's named-subject standard for that run.

Record what the analyst recognized. Blind mode is procedurally prospective, not a guarantee of epistemic blindness.

## 35. Generic-framework restriction

The analyst receives this method, the source pages, technical provenance, and translations if used. It does not receive series-specific theses, ledgers, future information, character monographs, or other analyses.

## 36. Modality-ablation benchmark

Run independent passes:

- **Pass A, text only**: lettering transcript or OCR text with page order.
- **Pass B, page images**: the full pages.
- **Pass C, page images with translation**, where the analyst does not read the source language.

For each added condition record new claims, revised claims, confidence changes, false claims, and claims correctly left open. Measure epistemic improvement, not prose length.

---

# XI. Governing rules

1. **Observation precedes interpretation.**
2. **Lettering is not acoustic delivery.**
3. **Panels suggest a trajectory; they do not show its execution.**
4. **A rendering-register shift is framing, not event.**
5. **Character belief is not world fact; a narrator is not the author.**
6. **Later outcomes cannot solve earlier uncertainty.**
7. **A striking image is not automatically a symbol.**
8. **OCR and search are not reading.**
9. **The edition read decides reading order and page turns.**
10. **Relationships are directional and conditional.**
11. **Counterevidence belongs inside the analysis.**
12. **A missing locator is better than a false one.**
13. **Use only the modules the unit earns.**

---

# Repository context

- [Medium and inspection-lane routing policy](../source-policies/MANGA_ANIME_MEDIUM_AND_INSPECTION_LANE_ROUTING_POLICY.md): lanes and reference methods by medium.
- [Project initiation and architecture policy](../source-policies/MANGA_ANIME_PROJECT_INITIATION_AND_ARCHITECTURE_POLICY.md): project-local method and architecture requirements; Section 12.1 on manga.
- [Generic multi-document synthesis architecture template](GENERIC_MULTI_DOCUMENT_SYNTHESIS_ARCHITECTURE_TEMPLATE.md): the paired architecture.
- [Generic character reconstruction method](GENERIC_CHARACTER_RECONSTRUCTION_METHOD.md): optional downstream modeling.
- [Analytical handoff contract](../source-policies/MANGA_ANIME_ANALYTICAL_HANDOFF_AND_INTEGRATION_CONTRACT.md): Section 15, named subjects and referential clarity.
- [Change-integration checklist](../policies/CHANGE_INTEGRATION_CHECKLIST.md): authorized paths, validation, and publication.
