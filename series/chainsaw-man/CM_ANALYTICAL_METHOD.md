---
title: "Chainsaw Man — Analytical Method"
artifact_id: CM_ANALYTICAL_METHOD
artifact_type: analytical_method
version: "1.1"
status: canonical
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
authority_generation: CM-INITIAL
authority_scope: "INITIAL bootstrap rules and attributed source metadata only; no literary findings"
source_boundary: "Metadata only: Japanese main manga V01–24; no narrative admitted"
created: 2026-11-07
last_updated: 2026-11-13
recommended_reasoning_class: DEEP_SYNTHESIS
---

# Chainsaw Man analytical method

## 1. Source-bounded purpose

Adapt the [generic manga method](../../governance/analytical-methods/GENERIC_MANGA_ANALYTICAL_METHOD.md) to the supplied Japanese V01–24 inventory, with the [architecture](CM_SYNTHESIS_ARCHITECTURE.md) governing accumulation. This method preserves what a reader and each source-established subject can know at a particular disclosure frontier. It does not import a remembered cast, adaptation, plot division or final interpretation.

The design must accommodate changing states and later recontextualization without treating every earlier uncertainty as error. It also requires ordinary routines, relationships, Japanese expression and page form so that dramatic events cannot consume the entire analytical account. These are responsibilities, not asserted features of unread scenes.

Before reading, disclose prior franchise exposure and quarantine it. A new session is not automatically blind. Numeric volume order is a candidate source order, verified before a bounded run; publication chronology, story time, disclosure and subject knowledge are separate.

## 2. Admission, source identity and complete page accounting

No narrative is authorized now. A future run requires both the OPEN precondition and explicit start/terminal authorization. Use `CM-JP-Vnn` keys bound to immutable byte digest, edition/language receipt and versioned spine-to-image map. Presence, transport, verification, admission, inspection and closure are different states. A changed digest is a new witness until demonstrated otherwise.

Map actual chapters and all image occurrences, including cover, front matter, inserts, main narrative, bonus/omake, author note, colophon and preview. Do not derive chapter numbers from arithmetic or infer pagination from image count. Extras can contain later information and require explicit admission/exclusion.

Inspect all selected pages in STILL_IMAGE, including silent, visually dense and OCR-resistant pages. Record REVIEWED_MATERIAL, NO_MATERIAL_ADDITION, DUPLICATE, EXCLUDED or UNRESOLVED_READABILITY per mapped page/range. Container integrity does not prove legibility or completeness. An OCR search, contact sheet or selected sample cannot certify a full reading.

## 3. Evidence coordinates and language

Pair a human locator with deterministic identity: witness/version, verified chapter, one-based image occurrence `iNNNN` including covers, visible printed label if any, panel and balloon ordinal. The machine route adds immutable digest, spine/member image identity and mapping version. State panel reading-order conventions and ambiguity; retain crop coordinates and full-page context.

Verify facing-page layout before claiming page-turn effects, and keep a spread's pair as one relational evidence object. Reflow/digital counters are not printed labels. Reopen the actual image for contested wording or visual interpretation. Exact quotations require image verification; mark EXACT_VERIFIED, WORKING_TRANSCRIPTION or PARAPHRASE and label English glosses.

Preserve consequential Japanese address, self-reference, modality, ellipsis, politeness, sentence endings and ruby/base distinctions. Distinguish speech, thought, narration, editorial caption, handwritten aside and diegetic text; attribute speaker/thinker/recipient by source evidence, not expectation. OCR is a retrieval aid, never independent confirmation.

Central claims receive a retrieval test against locked pages. A failed or pending locator stays RETRIEVAL_UNRESOLVED. Public Git carries short eligible quotations and sanitized routes, not source pages, OCR dumps, private IDs or extensive dialogue.

## 4. Prospective knowledge and causal reconstruction

Within a volume, preserve chapter/movement disclosure frontiers: an end reveal cannot explain an earlier scene's motive as if already known. Record event account, narrator/focalizer presentation, each subject's belief/knowledge, reader information and analyst inference separately.

Segment movements by source-established changes of goal, configuration, location, information or form. Develop conditions → perception → appraisal → affect → options/constraints → choice/non-action → consequence. Mark missing links. Surprise, temporal succession and visual juxtaposition do not by themselves prove causation or deception.

Reports, self-descriptions and declared motives are evidence of assertions; compare them with actions, knowledge and alternatives. A successful consequence does not establish intention. An apparently inconsistent act may reflect temporary condition, new information, coercion, role, audience or an earlier misreading; do not select one cause without evidence.

If identity, memory, physical condition, role or continuity becomes uncertain, assign boundary-specific states and competing mappings. Do not flatten them into one timeless biography or presume instability from title familiarity. Later identification adds a disclosure/revision link and preserves earlier anonymity or uncertainty.

## 5. Character, ordinary life and relationships

Subject records start only when admitted pages establish names/identities. Separate behavior, speech, represented thought, others' reports and public role. A facial expression is not a unique emotion or clinical diagnosis. Narration and formal framing can complicate interpretation without licensing arbitrary speculation.

Distinguish stable disposition from affect, fatigue, resources, role constraint, knowledge and relationship conditions. Use explicit change causes: DISPOSITION, KNOWLEDGE, RELATIONSHIP, CONTEXT, ROLE, RESOURCE, REVEALED_NOT_NEW, UNRESOLVED. Preserve a rival explanation and a disconfirming case.

Read ordinary interactions, practical needs, work, waiting, humor and low-stakes choices wherever present. They are evidence about baseline and context, not decorative paragraphs to cut for dramatic efficiency. Negative evidence requires an actual opportunity; lack of depiction is not refusal or absence of capacity.

Directed relationships A→B and B→A have separate knowledge, expectation, dependence, access, pressure, desire, trust/conflict and source-earned dimensions. Preserve power and information asymmetry without assuming reciprocal feeling. An institution's asserted rule, observed custom and enforcement are distinct. Later affection cannot retroactively settle earlier consent or intention.

## 6. Page grammar, tone and Japanese graphic voice

Analyze panel/page/spread organization, gutters, pacing, framing, gaze, isolated reactions, silence, withheld information, background presence/absence, rendering shifts and lettering. Explain feature → effect → plausible alternative. Still panels omit movement; do not claim the exact trajectory or performance in the gaps.

A tone claim needs page evidence and contextual variation. Stylization, exaggeration, comic distance, symbolism and literal event are separate possibilities. A rendering shift does not automatically change diegetic bodies or consequences. Recurrence requires meaningful relation and counterinstances, not a striking image alone.

Written voice traces appraisal → communicative objective → speech act → recipient/audience filter → register → wording/graphic presentation. Compare ordinary and pressured contexts. Sound effects are drawn Japanese forms with sound/state/manner functions, placement and scale; they are not measured audio. No anime performance can fill the source lane.

Themes emerge from recurring conflicts and formal relations. Preserve the distinction between depicting behavior, explaining it, evaluating it and endorsing it. Describe sensitive material only as needed for a sourced argument; neither moral prefiltering nor retrospective justification should replace analysis.

## 7. Counterreadings and changing claims

Every governing unit thesis has a substantial rival and a condition that would weaken it. Preserve the strongest counterevidence in the full reading. Assertion labels are OBSERVATION, SELF_REPORT, NARRATOR_PRESENTATION, INFERENCE, HYPOTHESIS, CONTRADICTION, EXTERNAL_REFERENCE, EVALUATION and UNRESOLVED, with confidence and reasons.

Use PRESERVE, STRENGTHEN, REVISE, DOWNGRADE, REJECT and OPEN. Store old/new formulations, exact source/knowledge boundary, evidence, alternative disposition and downstream effects. A later stronger interpretation need not invalidate the earlier prospective reading; record the distinction.

Classify apparent contradictions as witness/page-map issues, chronology, perspective, misinformation, role/audience, altered context/state, rendering convention, missing evidence, analyst disagreement or possible textual inconsistency. Leave alternatives open where the source does. Smoothness and brevity are not reasons to collapse them.

## 8. Complete future output and acceptance

Each future reading must contain receipt/coverage; entering state and frozen expectations; developed thesis/rival; movement-by-movement causal/page analysis; subject and directed relationship changes; ordinary-life controls; Japanese language and graphic voice; form/recurrence with counterexamples; earned institutional/domain questions; claim transitions; full ledger manifest; exit freeze; limitations and completion decision.

Retain causal steps, exact linguistic ambiguities, competing motives and quiet scenes at whatever length their analytical responsibility requires. A synopsis, state adjective or row cannot replace sustained reasoning. Separate interpretive openness from incomplete source inspection.

Before semantic acceptance, promotion or integration, sample introduction, a substantial middle section, conclusion/exit and major relationships/ambiguous actor passages. Check known names, purposeful roles, pronouns, concealment, speaker/thinker/recipient and frontier. Classify JUSTIFIED_ROLE_REFERENCE, SOURCE_REQUIRED_ANONYMITY, KNOWLEDGE_BOUNDARY_REQUIRED, UNNECESSARY_GENERICIZATION, AMBIGUOUS_REFERENT or INCORRECT_IDENTITY_OR_ATTRIBUTION. Record sample/findings and repair only supported defects.

Close the complete reading and five registers atomically. Scoped no-change records state actual inspected dimensions. Missing visual coverage, unreadable central evidence, broken locators or absent required updates remain holds.

<a id="current-unit-story-synopsis"></a>

### Current-unit story synopsis (initiation policy §5.3)

Each authorized main-volume reading must contain a clearly labeled **Current-unit story synopsis** near the front of its canonical artifact, after the receipt/coverage and entering context, before the thesis/rival, extended interpretation and ledger inventories. Identify inherited events briefly and distinguish them from what newly happens or is newly disclosed in the current volume.

Write coherent, accessible prose showing the opening situation, source-established participants and stakes, consequential actions and decisions, causal turning points, major disclosures and the ending state. Preserve meaningful physical and scene mechanics: who acts, how an act or interruption proceeds where established, and its consequences. Follow actual chapter/movement and panel presentation; inferred gutter transitions, replay or stylized rendering must not become invented continuous motion or literal events. Detail follows narrative density without a fixed length or required chapter template; unresolved outcomes remain unresolved.

Use only the current admitted Japanese unit and clearly distinguished inherited context. Separate depicted actions from speech/thought, narrator or focalizer presentation, testimony, conjecture, disputed identities/attributions and unresolved causes. Newly disclosed earlier events are not new story-time events. An end-of-unit reveal may appear here as unit-end knowledge but cannot be written back into an earlier actor's or prospective reader's state. Material event claims need retrievable witness/chapter/image/panel locators under §3 or stable evidence references resolving to them, without converting the synopsis into ledger rows. Remembered cast, arc divisions, later revelations, adaptations and unrelated works by the creator cannot complete the account.

Compose or finalize this unit-end, spoiler-bearing orientation only after the applicable prospective captures are frozen. Shield analysts assigned an earlier chapter, movement or volume horizon from the full spoiler-bearing reading. It is neither a prospective freeze nor independent evidence. The complete causal, visual/formal, Japanese, character, relationship, ordinary-life and counterreading arguments, five-register transaction and exit freeze remain required. Only a genuinely non-narrative separately scoped pass may state inapplicability with a reason.

_Prospective amendment — 2026-11-13, method v1.1: implements initiation policy §5.3 for future eligible readings; no narrative synopsis, admission, run authorization or frozen-history rewrite is made._

## 9. Reconstruction, frozen history and handoff

Later reconstruction separates evidence, a conditional operational model, independent tests and any literary monograph. Policies require triggers/stakes/state, response families, inhibitors, exceptions, counterevidence, rivals and falsifiers. Distinguish disposition and temporary condition; trace appraisal → decision → recipient-conditioned expression. Record confidence, distance from observed contexts and an abstention/multiple-response rule when evidence is inadequate.

Freeze genuine held-out predictions before exposure; label exposed work RETROSPECTIVE_CONSISTENCY_TEST. Independent evaluators own outcomes/readiness. Synthetic speech or scenario outcomes never become primary evidence or canon.

Accepted readings and checkpoint freezes preserve historical knowledge states. Later revisions use linked errata or superseding syntheses under [archive authority](../../governance/source-policies/ARCHIVE_AUTHORITY_AND_SUPERSESSION_POLICY.md). The [handoff contract](../../governance/source-policies/MANGA_ANIME_ANALYTICAL_HANDOFF_AND_INTEGRATION_CONTRACT.md) requires full files, evidence routes and unresolved obligations, not compressed substitutes.
