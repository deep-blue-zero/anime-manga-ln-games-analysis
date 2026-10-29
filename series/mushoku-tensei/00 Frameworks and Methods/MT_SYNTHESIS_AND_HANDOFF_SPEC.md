---
title: "Mushoku Tensei - Synthesis and Handoff Specification"
artifact_id: "MT_SYNTHESIS_AND_HANDOFF_SPEC"
artifact_type: "synthesis_handoff_specification"
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
canonical_home: "series/mushoku-tensei/00 Frameworks and Methods/MT_SYNTHESIS_AND_HANDOFF_SPEC.md"
source_boundary: "Accepted bootstrap method or template; no sequential novel readings or validated character models as of adoption."
recommended_reasoning_class: "DEEP_SYNTHESIS"
---

# Synthesis and cross-session handoff specification

## 1. Responsibility

This specification defines what substantial downstream outputs must accomplish and what their transfer must preserve. The architecture owns dependency order and gates; the live repository handoff/integration contract governs acceptance and publication. This is not a second series entrypoint.

Prefer fresh, well-grounded synthesis over keeping one conversation alive for the entire series. A summary is a navigation aid, not a replacement for full analytical artifacts and source routes.

## 2. Target-specific acceptance

### Character monograph

Make a sustained account of who the person is, how their commitments and defenses interact, what changes across the admitted boundary, how relationships condition behavior, where self-report misleads or helps, and what the source leaves uncertain. Include ordinary behavior, speech, substantial counterevidence, narrative function, and a real explanation of the operational reconstruction model.

A monograph fails when it is mainly biography, a trait list, a moral label, or a collection of chapter summaries. Length alone is not acceptance; do not impose a universal word ceiling that compresses necessary distinctions.

### Relationship or ensemble study

Explain both directions of important relationships, independent goals, information and power, reciprocity, rupture/repair, and the way one relationship alters others. Separate character desires from narrative function. Avoid treating romantic status as the only meaningful change or Rudeus as the sole measure of every person's significance.

### Literary specialist

State an explanatory thesis appropriate to the assigned domain, develop it through formal and narrative evidence, compare important counterreadings, and show what it explains that a plot recap does not. Define the source boundary, dependencies, and limitations. Do not create specialists merely because their titles sound comprehensive.

### Normative-framing specialist

Distinguish depicted behavior, character judgment, social norms, narrative framing, authorial intention, and reception. Analyze both supporting and countervailing mechanisms, with domain-specific development and matched-case tests. Do not require a binary verdict or use mixedness as an automatic compromise.

### Textual-history specialist

Document exact witness identities, historical order where established, comparison coverage, observed variants, and their possible effects. Separate mitigation from an attributed editor's intention. State whether the study is targeted, sampled, or complete for a range. Current-page evidence is not automatically evidence of the original publication state.

### Reception/discourse specialist

Represent actual arguments faithfully, distinguish languages/platforms/media/reading boundaries, explain sampling limits, and identify where disagreements are factual, interpretive, normative, or aesthetic. Do not infer community prevalence or social effects from selected posts. Return source-grounded claim adjudications, not a list of slogans.

### Integrated literary synthesis

Make a continuous account of the work's major artistic structures and tensions. Reconcile specialists rather than concatenating their summaries. Address what the work makes possible, what it does well or unevenly under explicit criteria, how character development and form interact, and what counterreadings remain strong.

Name whether this is a main-LN-only, supplemented-LN, comparative WN/LN, or broader adaptation-aware synthesis. Do not use 'full series' as an unqualified synonym for all franchise material. A later supplemental result can warrant a new bounded synthesis without invalidating the historical main-LN reading.

## 3. Synthesis input readiness

Before dispatch, identify exact target artifact IDs/paths, output responsibilities, current accepted versions, frozen input commit, source boundary, relevant ledger/checkpoint revisions, evidence gaps, and the integration owner. The package must provide full required analyses or verified retrieval routes; a chat synopsis alone is insufficient.

Classify every missing item as required, optional, or outside scope. Explain which claim depends on it. An optional rare bonus should not block an otherwise sound core-literary synthesis; an unverified central rewrite cannot be hidden inside a definitive revision-history thesis.

Use an architecture/role-gap review after sequential completion and before final synthesis. Newly discovered material may require bounded backfill or a new specialist. Preserve adequate work; do not restart the corpus for cosmetic uniformity.

## 4. Dispatch contract

A substantial transfer should make these groups recoverable:

```yaml
transfer:
  transfer_id: null
  stage_state: PLANNED
  project_root: null
  canonical_entrypoint: null
  producer_role: null
  receiver_role: null
  current_owner_instruction: null
  authorized_operation_and_source_scope: null
  allowed_target_paths: []
base:
  repository: null
  branch: null
  input_commit: null
  existing_target_blob_ids: []
  governing_method_and_architecture: []
evidence:
  admitted_witnesses: []
  inspected_boundary: null
  required_inputs_and_access_state: []
  optional_inputs: []
  excluded_or_spoiler_sources: []
outputs:
  artifact_ids_and_targets: []
  delivered_files_and_sha256: []
  acceptance_criteria: []
state:
  central_claims_and_counterreadings: []
  proposed_claim_revisions: []
  unresolved_requirements: []
  preservation_requirements: []
  next_action: null
receipt:
  integrity_check: PENDING
  base_drift_check: PENDING
  semantic_review: PENDING
  accepted_rejected_deferred: []
  repository_validation: NOT_RUN
  published_commit: null
  main_integration: NOT_PERFORMED
```

This is local documentation, not a replacement for global metadata. Operational stage states and authority statuses are different. A transferred candidate remains noncurrent until accepted; `READY_FOR_HANDOFF` is not a literary-quality certificate.

## 5. Source and knowledge integrity

A receiver must use the dispatched source boundary, even if the live branch has advanced. If expansion is authorized, state it explicitly and review affected dependencies. A new source cannot quietly enter a through-V10 monograph because V11 happens to be nearby.

Preserve uncertainty, alternative interpretations, unresolved translation issues, and failed predictions. Do not let the handoff convert a disputed hypothesis into a fact by dropping its qualification. Keep exact names and local IDs, and separate canonical spelling from unverified aliases.

The synopsis must identify what it omits and which original artifacts need recovery. Never claim every detail was preserved. Where context pressure threatens continuity, finish a coherent unit when practical, save the actual state, and hand off before beginning another large task.

## 6. Parallel specialists and convergence

Assign unique output paths and one frozen evidence snapshot. Specialists may challenge shared claims but return proposed deltas rather than concurrently patching the same ledger. One integrator compares overlaps and contradictions and updates canonical shared state.

Where specialists disagree, identify whether the issue is a source fact, scope mismatch, chronology, focalization, inference, or value criterion. Do not average incompatible conclusions into vague prose. Retrieve decisive evidence where available; preserve a real unresolved dispute otherwise.

A material new finding that changes a central premise reopens the affected argument and dependent specialists. Appending a footnote without revising the argument is insufficient. Unaffected work and prospective freezes remain intact.

## 7. Receiver workflow

Verify actual authorization, repository/root identity, hashes, complete delivered files, input coverage, and current target contents. Compare the source base, candidate, and current target before any replacement. Distinguish harmless drift, mechanical reconciliation, semantic conflict, and unresolved provenance.

Patch maintained documents through exact changes against complete current content. Do not rebuild a large artifact from excerpts or memory. Preserve substantive incoming prose unless evidence, a real defect, or an authorized structural change warrants revision; integration is not a license to compress everything into generic summaries.

Review high-impact new claims and suspect locators against sources, plus a declared representative sample. State the review extent rather than calling it exhaustive. Treat generated tests/scenarios as tests, not evidence.

## 8. Publication and release receipt

Follow the live checklist, approved branch lifecycle, exact-path staging, designated housekeeping/curation ownership, concurrency checks, and successful exact-head audit. No tool success message replaces remote content verification.

Report semantic acceptance, branch publication, housekeeping, final audit, and main integration separately. A file may be accepted but unpublished; a branch may be published but not integration-ready. Do not fabricate a commit or test result.

A frozen release identifies admitted source scope, actual completed lanes, artifact versions/hashes or immutable commit, required debts resolved, optional omissions, and the one current entrypoint. It is not a promise of future monitoring or an assertion of exhaustive franchise coverage.

## 9. Recovery handoff ending

End a substantial recovery handoff with a section titled **Instructions to the New Chat**. It must tell the receiver which live governance/entrypoint to read, what sources and scope control the work, what is already complete, what must not be redone, what remains uncertain or missing, and the next authorized concrete operation.

Files available in one chat may require re-upload or reconnection. Name those dependencies explicitly. A sandbox path is a transport reference, not a promise that another session has the bytes.
