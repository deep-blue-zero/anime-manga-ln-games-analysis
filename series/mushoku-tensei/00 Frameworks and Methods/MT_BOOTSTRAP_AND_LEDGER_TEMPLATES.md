---
title: "Mushoku Tensei - Bootstrap and Ledger Templates"
artifact_id: "MT_BOOTSTRAP_AND_LEDGER_TEMPLATES"
artifact_type: "bootstrap_template_collection"
series: "Mushoku Tensei"
generation: "V1"
version: "1.0"
status: canonical
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
do_not_use_as_literary_evidence: true
created: "2026-09-25"
design_reference_commit: "a2a1ab9a5ecd0512a5ac460c1b79655af1bca0bd"
adopted_on: "2026-09-25"
adoption_basis_commit: "a2a1ab9a5ecd0512a5ac460c1b79655af1bca0bd"
canonical_home: "series/mushoku-tensei/00 Frameworks and Methods/MT_BOOTSTRAP_AND_LEDGER_TEMPLATES.md"
source_boundary: "Accepted bootstrap method or template; no sequential novel readings or validated character models as of adoption."
recommended_reasoning_class: "BOUNDED_STANDARD"
---

# Bootstrap and ledger templates

## 1. Purpose and validation boundary

These examples implement the architecture's local documentation contract. They do not constitute a new repository schema, completed state, or source evidence. Before generating real files, inspect the current machine policies and an eligible maintained example. Use the exact supported gate keys and routing conventions; never modify a global validator to make a local template pass.

Actual operational files were initialized at bootstrap after checking for an existing root and reconciling current main. Unknown values remain explicit. Intentional template nulls must not be presented as successful initialization in the live entrypoint.

## 2. Entrypoint content

Proposed target: `series/mushoku-tensei/CURRENT_STATE_AND_CORPUS_MAP.md`.

Use `artifact_id: MT_CURRENT_STATE_AND_CORPUS_MAP`, `artifact_type: corpus_map`, and the complete live authority quartet. The published root must route to a current-eligible entrypoint; an accepted canonical entrypoint may truthfully report CLOSED initialization. Give it an exact source boundary describing bootstrap-only work and no completed sequential readings, unless existing work proves otherwise.

Its body needs: role and root; project initialization; current authorization; source/admission route; accepted framework links; required infrastructure; progress by lane; current blockers; next permitted action; execution owners; and a compact corpus map of **actual** artifacts.

A gate block following the inspected RAG pattern is:

```yaml
project_initialization:
  status: canonical
  architecture_lifecycle: INITIAL
  analytical_phase: BOOTSTRAP
  source_reconnaissance_complete: false
  governing_method: "00 Frameworks and Methods/MT_ANALYTICAL_METHOD.md"
  method_status: draft_noncurrent
  synthesis_architecture: "00 Frameworks and Methods/MT_SERIES_ARCHITECTURE.md"
  architecture_status: draft_noncurrent
  reconstruction_specification: "00 Frameworks and Methods/MT_CHARACTER_RECONSTRUCTION_SPEC.md"
  reconstruction_specification_status: draft_noncurrent
  required_day_one_infrastructure_initialized: false
  required_day_one_infrastructure:
    - "03 Longitudinal Ledgers/MT_CLAIMS_AND_REVISIONS_LEDGER.md"
    - "03 Longitudinal Ledgers/MT_CHARACTER_STATE_AND_READINESS_LEDGER.md"
    - "03 Longitudinal Ledgers/MT_RELATIONSHIP_AND_AGENCY_LEDGER.md"
    - "03 Longitudinal Ledgers/MT_CHRONOLOGY_AND_KNOWLEDGE_LEDGER.md"
    - "03 Longitudinal Ledgers/MT_NORMATIVE_FRAMING_LEDGER.md"
    - "03 Longitudinal Ledgers/MT_FORM_THEMES_AND_WORLD_LEDGER.md"
  sequential_analysis_lock: CLOSED
```

Replace draft statuses and booleans only after actual adoption/verification. Keep a literal human-readable `SEQUENTIAL_ANALYSIS_LOCK = CLOSED` or `OPEN` synchronized with the block. The bootstrap can end OPEN only if the real gate passes; **OPEN still does not authorize a V01 reading**.

Record bootstrap authorization separately, for example:

```yaml
bootstrap_execution:
  authorized_operation: BOOTSTRAP_ONLY
  new_sequential_analysis_authorized: false
  completed_new_sequential_units: []
  next_candidate: V01
  next_permitted_action: REPORT_BOOTSTRAP_STATE_AND_AWAIT_READING_SCOPE
lane_progress:
  ln_sequential_closed_through: null
  wn_comparison_closed_scope: null
  supplemental_readings_closed_scope: null
  adaptation_scope: OUT_OF_SCOPE
  reception_scope: NOT_STARTED
```

These additional fields are local documentation. They must not overwrite a real existing progress state or bypass the current continuation policy. Use the repository's actual execution fields when an authorized sequential run later starts.

## 3. Series routing descriptor

Target only after root identity is approved: `.repository/series-registry.json` inside the series root. Derive it from live controls and an existing valid new-root descriptor. Required semantics include stable ID/slug, canonical title, media, repository path, verified current entrypoint, materialization, migration/adoption scope, authority, `project_initiation_gate: REQUIRED`, and a truthful catalog note.

Do not set `PRESENT_VERIFIED` before the entrypoint exists and has been checked. Do not claim literary coverage in the catalog note. A suitable **meaning**, after actual acceptance, is: 'Japanese LN analysis framework bootstrapped; no sequential readings completed; source gap/verification state recorded; next reading requires explicit authorization.'

Do not directly edit housekeeping-owned `series/registry.json`, `series/README.md`, or `governance/MANGA_ANIME_CORPUS_INDEX.md` on the stable analytical branch. Do not create character-upsert payloads; the current curation policy owns character discovery.

## 4. Source-lock record

Proposed target: `01 Source Lock and Inventory/MT_SOURCE_LOCK_AND_INVENTORY.md`.

Record verified evidence folder/manifest identity and date, primary source family, exact inspected source metadata, available versus admitted units, missing/corrupt units, first-unit retrieval round trip, representation limits, and per-lane exclusions. Link the evidence inventory rather than reproduce it as another authoritative byte manifest.

Minimal admission row:

`witness ID | source family | verified title/edition/language | immutable identity/hash reference | available | integrity/coverage check | narrative inspection | admitted scope | limitation`

A source can be available and verified readable while narrative inspection remains NOT_STARTED. An inventory row is not an analytical claim. At bootstrap, inspect only metadata and the bounded structural samples required to establish usability; log any actual content exposure.

## 5. Shared ledger envelope

Each of the six required ledgers receives an accepted operational header, a distinctive `artifact_id`, a suitable non-sequential `artifact_type`, source boundary, responsibility, update/ownership rule, and initial state:

> No narrative observations have been admitted by this bootstrap. Record count zero means NOT_STARTED, not that the relevant phenomenon is absent.

Do not populate dummy findings. Use explicit stable row IDs when real records arrive. Retain history, patch current views, and link the original volume evidence observation. All records must distinguish source range, claim class, and uncertainty.

## 6. Claims and revisions ledger

Owns shared analytical claims and genuine prospective tests.

```yaml
claim_id: null
formulation: null
scope_and_witness: null
claim_class: WORKING_HYPOTHESIS
supporting_evidence: []
counterevidence: []
competing_explanations: []
current_assessment: OPEN
confidence_basis: null
revision_events: []
affected_artifacts: []
```

Revision event:

`revision ID | claim ID | prior formulation | PRESERVE/STRENGTHEN/REVISE/DOWNGRADE/REJECT/OPEN | new formulation | evidence | input/output boundary | affected homes`

Prospective test:

`test ID | frozen date/input boundary | observable expectation | diagnostic opportunity | disconfirmation | actual later observation | outcome | known exposure`

No opportunity is UNTESTED. A question without a discriminating expectation is not a prediction. Discourse hypotheses link these claims rather than duplicating their evidence history.

## 7. Character state and readiness ledger

Owns state-change observations, evidence coverage, and local model routing.

```yaml
state_event_id: null
local_character_key: null
source_evidence_refs: []
prior_state_ref: null
observed_change: null
change_kind: null
new_information_vs_new_disposition: null
persistent_features: []
uncertainty: null
model_path_if_present: null
```

Readiness row:

`character key | source boundary | observed contexts | missing contexts | local readiness by domain | model revision | validation evidence | constraints`

Do not enroll characters merely because they appear. Global entity/subject IDs remain null until an existing reviewed mapping is retrieved or curation establishes one. Optional per-character state histories are linked views, not competing state-event authorities.

## 8. Relationship and agency ledger

Owns directed relationship state and independently evidenced initiative/constraints.

```yaml
relationship_event_id: null
agent_a: null
agent_b_or_group: null
direction: null
source_evidence_refs: []
goal_or_desired_relationship: null
knowledge_and_assumptions: null
available_choices_and_constraints: null
initiative_refusal_or_repair: null
trust_obligation_dependency_power: null
prior_state_and_change: null
reciprocity_evidence: null
uncertainty: null
```

A group event may need several directional records linked to one source observation. Caring or compliance can be chosen, pressured, strategic, or ambiguous; record the basis. Include non-romantic relationships and goals when the source makes them significant.

## 9. Chronology and knowledge ledger

Owns event ordering, age/date claims, source-relative certainty, and proposition access.

Chronology row:

`chronology ID | event/evidence ID | witness/continuity | explicit anchor | inferred interval | physical age if known | other age claims | certainty | conflicts`

Knowledge row:

`knowledge ID | proposition | observer/holder | knows/believes/suspects/misbelieves/unknown | source basis | disclosure/concealment | effective story state | reader access | uncertainty`

Separate narrator report from independently established world fact. Do not backfill an earlier character's knowledge from later revelation. Do not force contradictory chronology into a false exact calendar.

## 10. Normative framing ledger

Use the full local record in [MT_NORMATIVE_FRAMING_PROTOCOL.md](MT_NORMATIVE_FRAMING_PROTOCOL.md). The ledger also needs a compact longitudinal comparison table:

`comparison ID | related event IDs | matched issue/opportunity | relevant differences | continuity/change | competing interpretation | present limit | shared claim IDs`

It owns no single cumulative morality score. Keep sexual preferences, conduct, consent, framing, and learning distinct. Nonsexual care, violence, exploitation, and responsibility belong here when diagnostic.

## 11. Form, themes, and world ledger

```yaml
pattern_id: null
kind: null  # form / motif / thematic_question / world_constraint / institution
proposed_pattern_or_rule: null
source_evidence_refs: []
recurrences_and_variations: []
formal_or_causal_mechanism: null
character_report_vs_world_fact: null
counterexamples: []
current_scope_and_confidence: null
specialist_destination_if_earned: null
```

Keep this concise and argument-bearing. If world facts or prose-form records become substantial independent bodies, split through an explicit architecture amendment with ownership transfer. Do not create a ledger for every possible theme in advance.

## 12. Deferred lanes

The textual-variant record belongs in the textual-history method; initialize its ledger only for actual authorized comparisons. The discourse hypothesis record belongs in the discourse method; the initial catalogue can be seeded as questions with no reception/prevalence claims. Neither is a required empirical finding at bootstrap.

Do not create anime episode bundles, voice ledgers, translation alignment, or extraction tooling without a separately bounded evidence task and sufficient capability.

## 13. Bootstrap report

Proposed target: `10 Audits and Handoffs/MT_BOOTSTRAP_REPORT.md`.

Record actual base/main/source-branch SHAs, collision search, existing work preserved, proposal hashes, accepted/rejected/amended files, source reconnaissance scope, gate state and reasons, required infrastructure state, exact changed paths, tests and actual results, publication/readback state, remaining blockers, and next permitted operation.

Include `substantive_sequential_findings_created: false` when that is true. Do not claim a containing commit SHA before it exists; use a later receipt or the verified Git record. Separate branch publication from integration into main and distinguish pending housekeeping from success.

Only retain sanitized provenance. Keep the transport package and its spoiler-bearing quarantine outside the analytical root unless an explicit reviewed transformation assigns them a legitimate public home.
