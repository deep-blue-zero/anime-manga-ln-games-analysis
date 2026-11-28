---
title: Manga / Anime MACRP Execution Runbook
artifact_id: MANGA_ANIME_MACRP_EXECUTION_RUNBOOK
artifact_type: macrp_execution_runbook
version: "1.0"
status: canonical
scope: concise reusable execution checklist for a Multi-Agent Character Reconstruction Pass run
created: 2026-11-24
last_updated: 2026-11-24
do_not_use_as_current_authority: false
do_not_use_as_literary_evidence: true
canonical_home: governance/source-policies/templates/MANGA_ANIME_MACRP_EXECUTION_RUNBOOK.md
supersedes: null
superseded_by: null
---

# MACRP Execution Runbook

This checklist sequences a run under the [MACRP protocol](../MANGA_ANIME_MULTI_AGENT_CHARACTER_RECONSTRUCTION_PASS_PROTOCOL.md). The protocol governs; a step here adds no requirement and waives none. Record each step in the run's [run record](MANGA_ANIME_MACRP_RUN_RECORD_TEMPLATE.md). **Stop** marks a point where the run waits for owner direction.

## 0. Before anything

1. Read `AGENTS.md` and routing Sections 2-4, 6-7 and 12, then the routing row for this pass and the protocol in full.
2. Recover the owner instruction. Confirm it names the project, the mode for each subject and the subjects or selection rule, and whether it authorizes configuration only or execution. **Stop** if it does not authorize the mode you would need.
3. Resolve the project's registry row, require `PRESENT_VERIFIED`, and read the canonical entrypoint in full. Read the governing method, architecture, admitted source boundary and reconstruction method.
4. Start from current `main` and the project's continuing branch, as the checklist's publication sequence requires.

## 1. Configure

1. Create the run record from the template at the path the project names. Record the instruction.
2. Freeze `baseline_commit` at a full SHA on `main`, and list the baseline artifacts with their frozen-release, byte-lock or recorded-hash state (Protocol Sections 2.1 and 9.5).
3. Assess eligibility at the baseline (Section 2.2). **Stop** at `NOT_ELIGIBLE` and report the route that applies instead.
4. Complete the baseline assessment, including current-state consistency findings (Section 2.3).
5. Diagnose each deficiency (Section 2.4). For MACRP-T, record the selection rule, or derive one when the instruction names none, and apply the reread test (Sections 3.1 and 4.2). If the diagnosis needs a mode or scope the instruction does not cover, record the proposal and **stop**.
6. Declare the scope, held artifacts and run-specific acceptance criteria (Section 3.2). Declare the source inventory and lanes (Section 6.1), the selection and uncited-source search (Section 6.2), the configuration, roster and workstream owners (Section 5), the planned outputs, successor and draft paths (Section 9) and the test strategy (Section 10.2).
7. Verify the capabilities: independent contexts and every lane the workstreams need. **Stop** on a missing required capability (Protocol Section 5.4).
8. For MACRP-F, confirm the gate route: material restart with `project_initiation_gate: REQUIRED`, a current-eligible method for the generation and its rule on retrospective material, the generation's own entrypoint and the reroute, the closure record's `canonical_entrypoint` update, the lock, run-stop reopening or closure amendment, and the run declaration (Section 4.3). **Stop** until each owner step is done.
9. If the instruction authorized configuration only, set `pass_state: blocked`, publish the run record alone, wait for its exact-head audit and **stop**. Otherwise set the run record's `pass_state: active` and record the run in the entrypoint under its own key: ID, modes, `pass_state: active`, run record path, held artifacts and next action (Section 13.2). Keep the two in step from then on. Never write `sequential_execution` or `project_initialization` fields for an R or T run. Publish this tranche and wait for its exact-head audit.

## 2. Independent work

1. If execution starts after a configure-only stop, compare `main` with the baseline for every governing input in the run record: targets, method, architecture, admitted boundary, entrypoint, authority and freeze states, held-artifact ownership and the governance documents applied. On a material change, refreeze and rerun the affected configuration steps before executing (Section 2.1). Then record the run in the entrypoint as step 1.9 describes.
2. Have the probe designer, an independent context that will not revise any model, write and seal the probe set. Include untargeted regression probes and control arms. Name the custodian that keeps the full set from the revisers, and record only its digest in the run record. If custody cannot be shown, record the set as `REVISERS_EXPOSED` (Section 10.4).
3. Dispatch each specialist and reviewer with an assignment packet, including the source-handling limits, in a separate context (Section 5.4). Participants return findings; only the principal commits. For MACRP-F, run every unit under topology Section 4.1 and the continuation policy, reconciling each unit against the preceding generation's reading of it.
4. Collect each participant's own findings, with locators, local occurrence IDs and per-proposition epistemic statuses (Section 7). Commit them unaltered, apart from source-text sanitization, as `draft_noncurrent` finding records before reconciling. Record each receipt, including auto-loaded instructions and latent knowledge.
5. Rerun any participant whose findings were lost or cannot be recovered. Never reconstruct them from memory or from a digest. Disclose any contamination.
6. Publish the frozen-findings tranche and wait for its audit.

## 3. Reconcile and draft

1. Build the occurrence register: map local IDs, baseline citations and re-presentations to canonical occurrences (Section 7.1).
2. Record each material finding's disposition and claim transition (Section 8). Count confirmation only where the source occurrence was inspected directly.
3. Resolve disagreements from the source; keep rival readings that remain supported.
4. Draft the revisions, canonical homes first (ledgers, claim registers, errata, monographs) and then the models that follow (Section 9.3). Build the mechanisms with priority arbitration (Section 7.3) and the state selectors (Section 7.4); mark what the evidence does not support as unknown.
5. Publish every draft as `draft_noncurrent` at its own path. Never edit a current, frozen or byte-locked artifact in this tranche (Section 9.2). Keep generated material out of evidence and source text out of Git (Section 6.6). Publish and wait for the audit.

## 4. Review and test

1. Reviewer A checks that every source-facing record lies inside the admitted boundary and the selection, then audits rule by rule against source, including its own sample. Reviewer B challenges for rival readings, counterexamples in uncited source, omissions, caricature and over-hedging (Section 10.1).
2. Once the drafts are frozen, commit the probe set and check it against its digest. Administer it through respondents and judges in separate contexts. Respondents use exactly the recorded inputs and state confidence and distance. Present normalized outputs under neutral labels. Record all three exposure facts and calibration (Sections 10.2-10.4).
3. Run the self-containment and fidelity reviews for every new or generally revised monograph, and the name-and-reference check on substantial prose.
4. Compare the drafts with the baseline using the sealed probes and control arms (Section 11). Report each change at its evidence level: source-verified correction, retrospective consistency gain, targeted-fix confirmation, or improvement on unseen probes.
5. Fix supported defects through the same routes. Rerunning the probe that exposed a defect only confirms the fix on that probe; a claim that the fix generalizes needs a fresh sealed probe (Section 10.4).

## 5. Accept, publish and refer

1. Check the fifteen acceptance criteria and the run-specific criteria (Section 12.1), and record each result.
2. Write the completion statement, the remaining items, typed as evidence-backed limitations, evidence gaps or deferred work, and the leads (Sections 12.2 and 14). Leads never mention tiers or grades.
3. In an acceptance tranche, apply the in-place revisions, promote the drafts of each accepted subject, add their supersession links, and update the qualification record and the entrypoint's run summary. Promote only subjects whose in-scope `REQUIRED` items are all met and accepted (Section 12.2).
   - Set `pass_state: completed` in the run record and the entrypoint only when the whole declared scope is accepted.
   - Otherwise record `blocked` or `interrupted_pending_recovery`, with each unmet item, its blocker, the affected artifacts and the next action. A declared item counts as dropped only with an explicit owner decision (Section 3.3).
   - In a shared ledger, relationship record or claim register, promote only separable reviewed changes that concern accepted subjects. Keep an indivisible joint change noncurrent until every subject it affects is accepted. Batch shared-artifact promotions where practicable, since each one makes every assessment citing that file stale (Section 12.2).
   - A frozen-release successor stays a draft on this branch. Its promotion and the predecessor's supersession metadata land together in one owner-reviewed governance change (Section 9.5).
4. Run author preflight, publish, put the leads in the PR description, and wait for the exact-head audit. If a supersession breaks a character reference, the discovery agent's separately identifiable repair commit on the branch resolves it (or the CI agent's, if mechanical); never touch discovery or capability outputs yourself. The CI agent merges.

## If interrupted

Recover from the run record's last verified checkpoint, the branch and `main` before writing anything (Protocol Section 15). Resume at the first stage not verified complete. Never infer completion from a draft or a conversation.
