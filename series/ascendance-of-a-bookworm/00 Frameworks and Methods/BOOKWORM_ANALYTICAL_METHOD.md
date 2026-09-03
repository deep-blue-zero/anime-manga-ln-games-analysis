---
series: ASCENDANCE_OF_A_BOOKWORM
artifact_type: analytical_method
scope: JP_LIGHT_NOVEL_SEQUENTIAL_AND_LONGITUDINAL_ANALYSIS
generation: V0.1
status: canonical
release_state: mutable_active
---

# Ascendance of a Bookworm — analytical method

## 1. Responsibility

This document governs source-facing analysis of the locked Japanese light-novel corpus for *Ascendance of a Bookworm*. Its job is methodological: it defines how evidence becomes claims, how later volumes may revise earlier models without rewriting historical analytical state, and when a recurring question deserves its own canonical artifact.

It is **not** a character profile, plot summary, world guide, or thematic synthesis. Those responsibilities belong downstream and must be earned by source evidence.

## 2. Current source and authority boundary

The current semantic anchor is the Japanese-language EPUB set audited on 2026-08-30: numbered main Volumes 01-33 plus the acquired side-story volume *Royal Academy Stories: First Year*.

- Git stores interpretation and analytical routing.
- The governed Drive source folder stores the primary EPUBs and audit manifest.
- The normalized English filenames are locators, not translations and not semantic authority.
- Anime, manga, translations, web-publication versions, fanbooks/reference works, interviews, and other supplements are separate witnesses unless a later source-lock revision explicitly integrates them.

Never fill a gap in the locked source with remembered canon, a wiki, adaptation knowledge, or general model knowledge while presenting the result as source-derived.

## 3. Evidence classes

Every durable claim should be recoverable to one or more source-bearing observations. Use these working classes:

- **DIRECT** — explicitly stated or unambiguously shown by the current source boundary.
- **CORROBORATED INFERENCE** — not stated verbatim, but supported by multiple independent observations or perspectives with weak counterevidence.
- **INTERPRETIVE HYPOTHESIS** — a plausible model that organizes evidence but remains meaningfully contestable.
- **OPEN / UNRESOLVED** — evidence is insufficient, contradictory, viewpoint-bound, or dependent on unread material.

A high-confidence interpretation is not promoted to DIRECT simply because it feels obvious. Conversely, a focal character's explicit statement is DIRECT evidence that the character said/thought it, not necessarily DIRECT evidence that the proposition is objectively true.

Record counterevidence when it is analytically material. Do not hide it inside prose smoothing.

## 4. Prospective sequential reading

The numbered main volumes use a **prospective freeze**.

For each VNN:

1. begin from the frozen analytical state after VNN-1;
2. record material open questions, expectations, and uncertainty before consulting VNN;
3. read VNN as the new source increment;
4. separate confirmation, extension, complication, revision, and falsification of earlier claims;
5. write the VNN deep reading;
6. freeze its bounded state before advancing to VNN+1.

Later evidence may revise the current model. It may not silently rewrite what an earlier reader reasonably knew. This protects against hindsight collapse across a very long series.

A volume deep reading is not a chapter transcript. It should select evidence because it changes the state of an analytical question.

## 5. Parts and global volume identity

The locked Japanese filenames organize the numbered main series into five parts while the normalized corpus uses global Volume 01-33 numbering.

Preserve **both** identities in each deep reading:

- global volume number (`V01` ... `V33`);
- Japanese part label and within-part volume label as encoded by the source metadata.

Do not restart repository filenames at each part. Global numbering keeps deterministic routing stable; part metadata preserves the work's own macrostructure.

A part-boundary synthesis may be created after its final volume freezes when it has a real retrieval responsibility. It summarizes the state reached at that boundary; it does not replace the underlying volume freezes.

## 6. Focalization and viewpoint discipline

Book-length evidence can include different narrators or viewpoint-bearing sections. Treat **focalizer identity as evidence metadata** whenever it matters.

For each claim, ask:

- Who perceives, remembers, narrates, or asserts this?
- Is the claim about the speaker's internal model, another person's behavior, an institution, or the world itself?
- Does another viewpoint independently corroborate it?
- Is the narrator positioned to know?
- Could status, culture, emotion, self-interest, limited information, or rhetorical purpose explain the account?

Do not flatten multiple viewpoints into an omniscient composite voice. Alternate perspectives are especially valuable when they expose a gap between self-conception and social effect.

When translation is later used as a convenience witness, return to Japanese for wording-sensitive claims involving register, titles, kinship/role terms, religious/legal terminology, evaluative language, or ambiguity.

## 7. Identity, names, titles, and role transitions

Long serial fiction can change how a person is named, addressed, classified, affiliated, or legally/socially positioned. Preserve those changes longitudinally rather than collapsing them into a single timeless label.

For identity-sensitive evidence, distinguish:

- personal continuity and self-identification;
- names and forms of address;
- titles, ranks, offices, affiliations, or institutional classifications;
- public identity versus private knowledge;
- legal/social status versus felt identity;
- role expectations versus actual agency;
- what each other character knows at that source boundary.

Use the name/title appropriate to the evidence locus where practical. A later canonical label may be used for retrieval, but it must not erase earlier state.

## 8. Institutions, status, class, and practical agency

Do not treat formal rules as the whole social system. Track separately:

- written or stated rules;
- customary practice;
- enforcement capacity;
- patronage and personal discretion;
- class/status barriers;
- material resources;
- information access;
- coercive leverage;
- exceptions and workarounds;
- the difference between nominal permission and practical freedom.

When a character changes social position, do not assume the same action has the same cost, meaning, or moral valence before and after the change. Re-evaluate available options and constraints at each state.

Political or ethical judgment should therefore follow reconstruction of the actual institutional choice set, not precede it.

## 9. Knowledge transfer, technology, and production

Claims about imported knowledge or practical innovation require more than identifying a modern-looking idea.

Separate at least four layers:

1. **remembered/claimed knowledge** — what a character believes they know;
2. **local translation** — how that knowledge is adapted to available materials, skills, institutions, vocabulary, and labor;
3. **demonstrated result** — what actually works or fails in the source;
4. **systemic consequence** — diffusion, resistance, economic effects, social effects, institutional capture, unintended consequences, or downstream dependency.

Avoid retroactively assuming that a successful result was inevitable. Record failed attempts, missing prerequisites, collaborators, and local expertise when the text makes them material.

Credit should follow causal contribution rather than protagonist-centered narrative salience.

## 10. World-model and system inference

Maintain a distinction between **character model** and **world model**.

For institutions, religion, magic/system mechanics, law, history, economics, education, or political structure, classify evidence by source position:

- character belief or explanation;
- institutional teaching/doctrine;
- observed regularity;
- demonstrated exception;
- independent corroboration;
- unresolved contradiction.

A doctrine can be socially real even if its metaphysical claim remains unproven. A repeated mechanism can be operationally reliable without the characters' theory of it being complete.

When later volumes provide a deeper explanation, revise the current world model while preserving earlier explanatory states and identifying what changed.

## 11. Relationships and recipient-conditioned behavior

Relationship analysis must be dyadic or network-aware rather than a list of isolated traits.

Track, as evidence warrants:

- what each party wants from the relationship;
- dependence and reciprocity;
- trust, disclosure, secrecy, and information asymmetry;
- affection, duty, contract, patronage, service, mentorship, rivalry, or coercion;
- status and power differences;
- forms of address and register;
- conflict and repair patterns;
- what changes when the recipient changes.

Do not infer identical motives from superficially similar behavior toward different people.

## 12. Ordinary life as evidence

Small-scale behavior is often necessary to reconstruct a character without reducing them to plot function.

Record mundane evidence when it bears on the model: food, clothing, comfort, hobbies, work rhythm, study, gifts, shopping, etiquette, humor, rest, annoyance, avoidance, habits, sensory preferences, domestic routines, and treatment of low-status or low-stakes interactions.

Ordinary-life evidence should not become trivia accumulation. Promote it only when it clarifies values, competence, attachment, self-presentation, recipient effects, or state transitions.

## 13. Long-range character development

Distinguish:

- **stable tendency** — recurs across states and recipients;
- **developmental state** — characteristic of a bounded period;
- **role effect** — produced by office/status/duty;
- **recipient effect** — specific to a relationship;
- **situational effect** — crisis, illness, exhaustion, danger, public performance, etc.;
- **genuine revision** — prior model no longer adequately predicts later behavior.

Do not force every contradiction into hidden consistency. Some contradictions are development; some are hypocrisy; some are competing values; some are narrator error; some remain open.

## 14. Supplemental and side-story control

*Royal Academy Stories: First Year* is inside the acquired source inventory but **outside the numbered prospective main-volume chain**.

Before analytical integration:

1. verify publication and diegetic placement from source-grounded evidence;
2. identify its focalizers and the main-volume states it can legitimately inform;
3. decide whether it is best read after a specific frozen volume/part boundary;
4. record whether its evidence confirms, extends, complicates, or revises the current model;
5. do not rewrite predictions that were frozen before the supplement was consulted.

Apply the same rule to any later-acquired side story, bonus, fanbook, adaptation, or alternate-version witness.

## 15. Claim revision vocabulary

When a later volume or witness tests a prior claim, prefer explicit revision states:

- **PRESERVE** — materially unchanged;
- **STRENGTHEN** — same claim, stronger evidence or wider support;
- **REVISE** — core model survives but wording/scope/causal account changes;
- **DOWNGRADE** — claim remains possible but confidence or scope falls;
- **REJECT** — evidence now materially contradicts the claim;
- **OPEN** — adjudication remains insufficient.

This vocabulary describes analytical state, not moral approval.

## 16. Minimum numbered-volume deep-reading responsibilities

Each numbered deep reading should cover, as evidence warrants:

- volume/part identity and exact source witness;
- event/scene structure and focalization;
- character-state changes and contradictions;
- relationship and network changes;
- institutional/status constraints and practical agency;
- knowledge transfer, work, production, economic, or educational changes where material;
- ordinary-life evidence;
- names/titles/roles and information-state changes;
- world-model claims separated from viewpoint-bound belief;
- distinctive Japanese wording/register when interpretation depends on it;
- direct facts versus inference;
- rival readings and counterevidence;
- revision status of important prior claims;
- bounded expectations/open questions for the next unread numbered volume.

## 17. Promotion thresholds for new artifacts

Create a new canonical artifact only when it owns a recurring retrieval/revision responsibility that the existing files no longer serve reliably.

Examples:

- a longitudinal ledger after the same question recurs across multiple volume freezes;
- a character monograph after enough longitudinal evidence exists to model stable tendencies, state effects, contradictions, relationships, and abstentions;
- a specialist institutional/economic/religious/formal synthesis when the question spans many volumes and cannot be maintained cleanly inside general ledgers;
- a part or full-series synthesis only after its source boundary is actually covered.

Do not create directories merely to advertise future ambitions.

## 18. Comparative and ethical frameworks

PACTRIH, cross-series character comparison, genre comparison, adaptation judgment, and similar higher-order frameworks are **downstream**.

Before applying them:

- establish the relevant source boundary;
- build the character/institutional model from Bookworm evidence first;
- distinguish descriptive reconstruction from normative judgment;
- preserve uncertainty and state dependence;
- avoid treating protagonist status, antagonist status, popularity, or narrative reward as moral evidence.

A comparative framework may expose new questions, but it must not become a substitute for reading the source.

## 19. Falsification and rival-reading rule

For any thesis important enough to recur, ask what evidence would make it weaker.

A durable analysis should be able to name:

- supporting evidence;
- counterevidence;
- alternative causal explanations;
- missing evidence;
- source boundaries that could change the result.

When evidence supports multiple readings, keep them live until one becomes materially stronger. Precision about uncertainty is preferable to premature closure.

## 20. Bootstrap prohibition

This method establishes how analysis will be done. It does not authorize substantive conclusions by itself.

The first canonical interpretive artifact under this root should be the Volume 01 deep reading. No whole-series character model, world guide, ethical score, or thematic conclusion is established merely by creating this scaffold.
