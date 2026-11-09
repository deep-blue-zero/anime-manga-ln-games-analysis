---
title: "Blue Box — Manga Analytical Method"
artifact_id: BB_MANGA_METHOD
artifact_type: analytical_method
version: "1.0"
status: canonical
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
authority_generation: BB-INITIAL
authority_scope: "INITIAL bootstrap rules and attributed metadata only; no literary findings"
source_boundary: "Metadata only: Japanese main manga V01–27 and separate prose Interlude/Prologue; no narrative admitted"
created: 2026-11-07
last_updated: 2026-11-07
recommended_reasoning_class: DEEP_SYNTHESIS
---

# Blue Box manga analytical method

## 1. Main-lane scope

This method adapts the [generic manga method](../../governance/analytical-methods/GENERIC_MANGA_ANALYTICAL_METHOD.md) for reported Japanese main V01–27. The [prose method](BB_PROSE_SUPPLEMENT_METHOD.md) independently governs Interlude/Prologue; the [architecture](BB_SYNTHESIS_ARCHITECTURE.md) coordinates them. No narrative is admitted now.

Do not import a cast, relationship, event or genre conclusion from familiarity or another medium. Record prior exposure before a future run and quarantine it. A fresh session is not automatically blind. The method must preserve ordinary behavior, changing knowledge, directed relationships, causal choices, Japanese expression and page construction at the admitted frontier.

## 2. Admission and page coverage

An OPEN gate and explicit bounded authorization are both required. Use `BB-MANGA-Vnn` keys bound to immutable bytes, edition/language receipt and versioned spine/image occurrence map. Presence, transport, verification, admission, inspection and analytical closure are separate. A changed digest creates a distinct witness until equivalence is established.

Verify numeric order and actual chapters rather than infer them. Map all image occurrences including covers, inserts, main pages, bonus, notes, colophon and previews. Classify/exclude spoiler-bearing components explicitly. Page states: REVIEWED_MATERIAL, NO_MATERIAL_ADDITION, DUPLICATE, EXCLUDED, UNRESOLVED_READABILITY.

Inspect actual readable STILL_IMAGE pages, including silence and small lettering. OCR/search/contact sheets aid retrieval but do not certify coverage. Container validity is not page completeness or legibility.

## 3. Deterministic locators and Japanese text

Use witness/version, verified chapter, one-based image occurrence including covers, visible printed label if any, panel/balloon ordinal; bind them to digest, spine/member and map version. State reading-order conventions and uncertainty. Preserve crop coordinates/full-page context and exact spread pairing. Verify facing-page layout before page-turn claims.

Reopen source images for central interpretation and exact quotations. Mark EXACT_VERIFIED, WORKING_TRANSCRIPTION or PARAPHRASE; label glosses. Preserve consequential Japanese address, self-reference, ellipsis, modality, politeness, endings and ruby/base. Attribute speaker, thinker, narrator and recipient from tails, placement and context.

Test central retrieval; a failed/pending locator stays RETRIEVAL_UNRESOLVED. Private source IDs, primary pages and bulk OCR stay outside Git.

## 4. Causality and prospective knowledge

Keep chapter/movement disclosure frontiers within a volume. Record event account, narrator/focalizer presentation, each subject's knowledge/belief, reader information and analyst inference separately. Later manga or prose information cannot enter earlier states.

Develop movements as conditions → perception → appraisal → affect → options/constraints → choice/non-action → consequence, with unsupported links and serious rival causes. A silent reaction, successful outcome or adjacent panel does not uniquely establish motive or causation. Preserve what the page omits.

Source-established chronology uses evidence-based constraints, not assumed dates. Page succession may depict simultaneity, recall or reaction; still images do not certify exact omitted motion. Prose supplement titles cannot supply chronology.

## 5. Character, ordinary routine and directed relationships

Create names/identities only from admitted manga pages. Separate behavior, speech, thought text, others' reports and public role. A drawn expression supports bounded interpretation, not certain internal narration. Prose interiority is not a missing caption to insert into manga.

Treat low-stakes routine, practical arrangements, work/practice, rest, waiting, humor and mundane interaction as first-class evidence where present. Dramatic choices alone do not establish disposition. Negative evidence requires a meaningful opportunity and clear limits.

Relations A→B and B→A need separate knowledge, expectations, conduct, trust/conflict, dependence, obligation, access and source-earned dimensions. A gesture or address term cannot alone settle an entire tie. Preserve contextual constraints and competing motives. Group/institutional assertions distinguish rules, custom, observed practice and participant assumptions.

Change causes are DISPOSITION, KNOWLEDGE, RELATIONSHIP, CONTEXT, ROLE, RESOURCE, REVEALED_NOT_NEW or UNRESOLVED. Retain temporary conditions, ordinary counterexamples and prior state. Depiction, explanation, evaluation and endorsement remain distinct; later affection cannot settle earlier consent or motive.

## 6. Page form and graphic language

Analyze panel/page/spread arrangement, framing, gaze, gutters, silence, reaction placement, backgrounds, rendering shifts and lettering. Explain observed feature → supported effect → alternative. Tone and symbolism require exact page evidence and counterinstances, not genre familiarity.

Written voice follows appraisal → objective → speech act → recipient/audience filter → register → wording/lettering. Compare ordinary and pressured contexts. Sound effects are drawn sound/state/manner conventions, not measured audio. No adaptation acting or music enters this lane.

Recurrence requires meaningful variation and selection criteria. Preserve quiet transitional pages as well as dramatic compositions. A synopsis or a relationship label cannot discharge a visual/linguistic argument.

## 7. Claims and separate-medium comparison

Use OBSERVATION, SELF_REPORT, NARRATOR_PRESENTATION, INFERENCE, HYPOTHESIS, CONTRADICTION, EXTERNAL_REFERENCE, EVALUATION and UNRESOLVED with confidence/reason. Every unit thesis has a serious rival and disconfirmation condition.

Cross-medium comparison occurs only after independently authorized/inspected manga and prose readings. Pair exact evidence; classify overlap, compatible addition, changed focalization, changed wording/causality, contradiction or unmatched material. Do not assume shared continuity or narrator authority. A prose-only statement remains prose-only even when useful to a comparative interpretation.

Revision uses PRESERVE, STRENGTHEN, REVISE, DOWNGRADE, REJECT or OPEN, keeping old/new formulations, lane/knowledge boundary, evidence, counterevidence and dependencies. Frozen manga readings retain their original prospective state.

## 8. Full output and acceptance

A future reading contains receipt/coverage; entering state/forecasts; developed thesis/rival; movement-level causal/page reading; subjects and directed ties; ordinary controls; Japanese/graphic expression; form/recurrence and counterexamples; source-earned domains; claim transitions; five-register manifest; exit freeze; limitations and completion decision.

Keep full causal, relational, linguistic and formal reasoning at the length needed. A brief summary, trait chart or cross-medium composite cannot replace the source-facing reading. Missing required inspection and genuinely open interpretation are different.

Before semantic acceptance, promotion or integration, sample introduction, substantial middle, conclusion/exit and major relationships/ambiguous actors. Verify names, purposeful roles, pronouns, concealment, speaker/thinker/recipient and knowledge boundary. Classify JUSTIFIED_ROLE_REFERENCE, SOURCE_REQUIRED_ANONYMITY, KNOWLEDGE_BOUNDARY_REQUIRED, UNNECESSARY_GENERICIZATION, AMBIGUOUS_REFERENT or INCORRECT_IDENTITY_OR_ATTRIBUTION. Record sampled scope/material findings and repair supported defects.

Accept complete prose and synchronized registers atomically. Scoped no-change findings state actual inspection. Unreadable required pages, broken central locators or missing updates remain holds.

## 9. Reconstruction and preserved history

Models remain separate from monographs, evidence and independent evaluation. Use lane-qualified subject@frontier/state; manga-derived models cannot silently learn prose-only interiority. Conditional rules need triggers/stakes/state, response families, inhibitors, exceptions, counterevidence, rivals/falsifiers, confidence/evidence distance and abstention/multiple-response criteria. Trace appraisal → decision → recipient-conditioned expression and separate disposition from condition.

Freeze true held-out predictions before exposure; exposed work is RETROSPECTIVE_CONSISTENCY_TEST. Synthetic output is never primary evidence or canonical characterization. [Archive authority](../../governance/source-policies/ARCHIVE_AUTHORITY_AND_SUPERSESSION_POLICY.md) and the [handoff contract](../../governance/source-policies/MANGA_ANIME_ANALYTICAL_HANDOFF_AND_INTEGRATION_CONTRACT.md) preserve frozen source-facing states and full arguments across sessions.
