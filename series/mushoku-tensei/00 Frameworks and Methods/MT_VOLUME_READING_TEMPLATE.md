---
title: "Mushoku Tensei - Volume Reading Template"
artifact_id: "MT_VOLUME_READING_TEMPLATE"
artifact_type: "volume_reading_template"
series: "Mushoku Tensei"
generation: "V1"
version: "1.1"
status: canonical
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
do_not_use_as_literary_evidence: true
created: "2026-09-25"
design_reference_commit: "a2a1ab9a5ecd0512a5ac460c1b79655af1bca0bd"
adopted_on: "2026-09-25"
adoption_basis_commit: "a2a1ab9a5ecd0512a5ac460c1b79655af1bca0bd"
canonical_home: "series/mushoku-tensei/00 Frameworks and Methods/MT_VOLUME_READING_TEMPLATE.md"
source_boundary: "Accepted bootstrap method or template; no sequential novel readings or validated character models as of adoption."
recommended_reasoning_class: "SUBSTANTIVE_ANALYSIS"
---

# Volume reading template

## Template status and use

This is a reusable structure, not `MT_V01_DEEP_READING.md` and not evidence that any source has been read. Its own `artifact_type` must remain a template type. Copy and adapt its body only when an actual authorized unit is opened after the initiation gate passes.

Use the method to determine depth. Sections with no material finding can be brief and say so; do not manufacture uniform essays. Maintain a compact coverage map for the whole volume and close-read diagnostic passages. No word count can substitute for coverage and argument.

The actual reading should have a valid first YAML block, a unique artifact ID such as `MT_V01_DEEP_READING`, `artifact_type: deep_reading`, its real source boundary, and truthful authority status. Start an unfinished candidate as `draft_noncurrent`; promote only through the project's acceptance process. A template cannot confer canonical status on an uninspected source.

---

# [Actual volume title and verified edition]

## Reader orientation

### Developments through the previous volume (V02 onward)

Before opening this volume, describe in ordinary prose the causally important story events, relationship and character changes, and unresolved situations inherited from *closed* earlier LN units. State the exact prior-volume boundary and link its reading. Keep character reports and open interpretations qualified; do not import a later revelation or rewrite the prior unit's prospective freeze. For V01, say that there is no previous LN volume or omit this subsection. This reader-facing account is distinct from the entering analytical freeze below.

### Story synopsis of this volume (spoilers)

After inspecting the complete volume, narrate its initial situation, central choices and reversals, important changes in relationships, ending, and the position of consequential interludes or extras. Use connected prose that makes the plot understandable before the reader reaches the technical coverage map. Identify the actors and the stakes rather than listing only chapter topics or evidence IDs. Qualify uncertain or character-reported events, paraphrase sensitive scenes without graphic detail, and route to Sections C and D for exact evidence. The synopsis is a reading aid, not a substitute for source coverage or close analysis.

## A. Scope, input state, and inspection

Record the exact volume/witness ID, admitted main/supplemental items, source hash or revision, language, source-map reference, base input commit, method/architecture versions, and exclusions. Record prose, illustrations, and paratext inspection independently.

```yaml
unit:
  volume: null
  witness_id: null
  source_fingerprint_ref: null
  basis_commit: null
coverage:
  narrative_items_total_verified: null
  narrative_items_inspected: null
  prose_inspection: PENDING
  illustration_inspection: PENDING
  paratext_admission: null
  extraction_limitations: []
  missing_or_duplicate_items: []
knowledge_boundary:
  entering_closed_volume: null
  eligible_witnesses: []
  known_external_exposure: []
```

Report actual exposure, not just intended exclusion. Do not attach a count whose denominator is unverified.

## B. Entering prospective freeze

What is established through the last closed unit? Which character/relationship states and shared claims govern the starting model? What is inferred, disputed, or unknown?

Separate questions from predictions. A real prediction identifies its prior evidence, expected outcome or response range, conditions for a diagnostic opportunity, potential disconfirmation, and the time it was frozen. Abstention is valid.

Do not insert observations made after reading this volume into its entering freeze. Correct an objective starting-state error visibly rather than rewriting the prediction.

## C. Coverage and volume architecture

Provide a concise chapter/scene map with exact edition labels and source ranges. Account for interludes, point-of-view shifts, internal extras, and omitted paratext. Ordinary continuity can be summarized compactly.

Then explain the volume's structure: its initial situation, decisions and reversals, pacing, information releases, contrasts, unresolved movement, and contribution to the developing work. Do not assume the future arc's meaning.

## D. Diagnostic close readings

For each important passage or scene, provide:

- a stable evidence ID and recoverable source locator;
- a concise non-graphic description of what is represented;
- the exact interpretive question;
- close analysis of wording, narrative access, action, and form;
- the strongest consequential alternative reading;
- the minimum warranted conclusion, confidence, and downstream claim/ledger links.

```yaml
evidence_id: null
witness_id: null
chapter_label: null
spine_item_path: null
source_element_or_paragraph_range: null
normalization_map_ref: null
printed_page_if_verified: null
representation: null  # event / speech / interior / memory / fantasy / paratext / illustration
observation_non_graphic: null
short_quote_if_necessary: null
analyst_translation_if_used: null
interpretation_class: WORKING_HYPOTHESIS
interpretation_and_alternatives: null
claim_refs: []
```

Do not use a quote merely for atmosphere. Do not reproduce explicit sexual material involving children. A restrained paraphrase plus source locator is generally enough for ethical analysis.

## E. Character deep readings and state changes

For materially affected characters, analyze appraisal, motives, emotional regulation, self-account, decisions, competencies, responsibility, contradictions, and ordinary behavior. State what changed and whether it reflects disposition, knowledge, relationship, circumstance, or newly revealed information.

Include independent goals and scenes of secondary people when relevant. Do not let a protagonist-centered narrative become an excuse for a protagonist-only analysis.

Record what the current volume does **not** establish. Distinguish an inferred motive from reported interiority and a stable trait from one contextual response.

## F. Relationships, agency, and family/social structures

Track A->B and B->A separately. Who initiates, refuses, interprets, withholds, repairs, provides care, incurs costs, or changes available options? What information/power asymmetries matter? Does a public relationship label match private belief or demonstrated practice?

Connect social institutions and material constraints to choices where supported. Do not import unverified cultural generalizations.

## G. Focalization, voice, and form

Analyze narrator/experiencing-self distance, reliability, irony, diction, temporal presentation, scene/summary balance, tone, chapter arrangement, and attention distribution. Note representative Japanese wording where the interpretation depends on it.

Where illustrations were inspected, distinguish their visual framing from prose narration. Do not infer performed voice or camera behavior from a novel.

## H. Normative-framing findings

Use the narrower protocol, not an automatic endorsement/condemnation label. Include precise conduct, knowledge/consent/power conditions where material, affected-person access, character judgment, narrative register, consequences, recurrence, and alternative readings.

Acknowledge where the volume provides a clear result and where it only supplies one element of a later longitudinal test. Moral-learning claims must name the domain and evidence rather than use a general 'better person' score.

## I. Themes, motifs, world, and chronology

Explain emerging themes through concrete recurrences and formal structure. Record world rules, institutional effects, important age/date anchors, knowledge transfers, and unresolved contradictions. Do not pad this with an encyclopedia of setting facts.

Distinguish thematic importance from page frequency. A theme need not be one of the planning catalogue's expected topics.

## J. Claims, counterevidence, and revisions

| Claim ID | Earlier bounded formulation | New evidence | Transition | Current formulation/limit | Downstream home |
|---|---|---|---|---|---|

Use `PRESERVE`, `STRENGTHEN`, `REVISE`, `DOWNGRADE`, `REJECT`, or `OPEN`. An empty table means no material revisions were found after review, not that the review was skipped. Refer to independent source units, not a count of citations to the same passage.

Do not adjudicate a spoiler-bearing discourse claim from later information. A neutral analytical claim can be updated now and connected to reception later.

## K. Reconstruction implications

Which new behavioral rules or state distinctions are supportable? Which existing rules require qualification? What ordinary/relationship contexts are now better represented? What remains too thin for simulation?

Link exact model revisions or record that a standalone model is not yet warranted. State readiness by domain and source state. Generated demonstrations are labeled extrapolations and do not become source evidence.

## L. Exit freeze and next questions

Record current source-bounded conclusions, surviving alternatives, open source questions, disproven expectations, and genuinely prospective tests for later eligible material. Do not pretend that a later possibility is a prediction when prior external exposure already revealed it.

## M. Transaction closure and verification

| Obligation | Actual result | Evidence/path | Remaining blocker |
|---|---|---|---|
| Declared prose coverage | | | |
| Consequential locators/wording checked | | | |
| Illustrations/paratext scope stated | | | |
| Claims/revisions reviewed | | | |
| Character/state/readiness reviewed | | | |
| Relationships/agency reviewed | | | |
| Chronology/knowledge reviewed | | | |
| Normative framing reviewed | | | |
| Form/themes/world reviewed | | | |
| Affected models and indexes synchronized | | | |
| Entering/exiting freezes preserved | | | |
| Semantic review and current-state update | | | |
| Applicable repository checks/persistence | | | |

Use actual results: updated, reviewed-no-material-change, partial, pending, or blocked. No fictitious PASS rows. State separately whether the unit is draft, semantically closed, committed, branch-published, or main-integrated. Never advance beyond the authorized terminal boundary.

## N. Later correction history

Leave the original prospective interpretation intact. Record objective corrections and links to subsequent reinterpretations with dates and reasons. This section is not permission to inject future knowledge into earlier conclusions.
