---
title: "Watayuri — Consequential proposition and information asymmetry"
artifact_id: WATAYURI_INFORMATION_DISCLOSURE_AND_MISREADING_LEDGER
artifact_type: longitudinal_ledger
series: "Yuri Is My Job! / 私の百合はお仕事です！"
generation: WATAYURI_BOOTSTRAP_V1
version: "0.1"
status: active_provisional
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
do_not_use_as_literary_evidence: true
created: "2026-09-28"
source_boundary: "Japanese manga inventory V01–V14; no narrative volume inspected"
canonical_home: series/watayuri/03 Longitudinal Ledgers/WATAYURI_INFORMATION_DISCLOSURE_AND_MISREADING_LEDGER.md
---

# Consequential proposition and information asymmetry

**Canonical responsibility.** Maintain one record per material proposition whose distribution or misreading changes behavior. Distinguish represented truth from character beliefs, suspicion, false beliefs, belief-about-belief, deliberate lie, omission, ambiguity, mistake and in-role speech.

**Record schema.** Proposition ID; VNN and event time; proposition wording; represented truth/status; each material knower/suspector/false believer; relevant higher-order belief; discloser/withholder; audience; timing; evidenced motive versus analyst inference; resulting behavior; later correction; confidence; source locator; linked relationship/claim IDs.

**Boundary and exclusions.** Do not enumerate trivial facts or duplicate whole dyadic summaries. A claim about reader interpretation belongs to the claims ledger; past-event temporal placement belongs to chronology.

**Evidence convention.** Each future entry references a source-map key and exact Drive witness ID, volume, verified chapter and image/print-page scheme, and panel/balloon where relevant. Cite the associated frozen `WATAYURI_VNN_DEEP_READING.md` observation and claim ID when one exists. Separate depicted fact, character report, and analyst inference. Do not insert raw page images or long source passages into Git.

**Update and revision rule.** Update when disclosure, false belief, correction or materially altered higher-order belief affects behavior. Append a new dated epistemic state; preserve what each party and reader could know at the earlier VNN. Make targeted edits to mutable current-state rows while preserving dated prior states, IDs and frozen prospective readings. Use the claim ledger's explicit transitions for changed interpretations; an artifact-wide supersession requires the global authority procedure. The [architecture](../00%20Frameworks%20and%20Methods/WATAYURI_SYNTHESIS_ARCHITECTURE.md) owns cross-ledger routing.

**Coverage:** `NO_NARRATIVE_EVIDENCE_INSPECTED_AT_BOOTSTRAP`. Evidence rows: **zero**. The schema lists prospective fields, not findings. Next update is conditional on owner approval, an OPEN sequential-analysis lock, and a completed source-unit transaction.
