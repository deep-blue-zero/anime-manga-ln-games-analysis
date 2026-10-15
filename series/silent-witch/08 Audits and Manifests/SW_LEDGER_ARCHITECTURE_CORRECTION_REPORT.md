---
title: "Silent Witch — Ledger Architecture Correction Report"
artifact_id: SW_LEDGER_ARCHITECTURE_CORRECTION_REPORT
artifact_type: audit_report
series: "Silent Witch: Secrets of the Silent Witch"
series_id: silent-witch
generation: V1
version: "1.0"
last_updated: "2026-10-14"
status: canonical
scope: "Record of the 2026-10-14 longitudinal-ledger architecture correction: responsibility inventory, extraction of claims and revisions into a dedicated ledger, revision-event and claim-metadata audit, character-state schema and causal-fidelity audit with repairs, decisions on the remaining ledger responsibilities, integrity checks and publication"
source_boundary: "The master longitudinal ledger at branch commit ee2f068 (version 1.19) and the sixteen closed deep readings it cites; no new source reading"
created: "2026-10-14"
canonical_home: "series/silent-witch/08 Audits and Manifests/SW_LEDGER_ARCHITECTURE_CORRECTION_REPORT.md"
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
do_not_use_as_literary_evidence: true
---

# Silent Witch — ledger architecture correction report

## 1. Task, authority and state

The owner commissioned a targeted architectural correction and fidelity audit of the longitudinal infrastructure on 2026-10-14. The brief was written at the V09 and IX -extra- boundary and asked for every figure to be recomputed against the live branch. This correction was carried out after the run had closed every supplied unit and every synthesis product. It authorizes:

- the extraction of claims and revisions;
- corrections to revision-event production and claim metadata;
- a character-state schema and causal-fidelity audit with justified repairs;
- decisions on the remaining sections.

It authorizes no new literary reading, character reconstruction or synthesis. Any further split is a recommendation unless it is needed to prevent an integrity failure.

| Field | State |
|---|---|
| Base | Branch `series/silent-witch`, local head `ee2f068`; master ledger blob `d36c4fb4618b77644f5c2f7d1bc20341cce2e324`. |
| Concurrency | The session that ran the sequential readings was the only writer, and no other worktree held the branch. The two character-state auditors worked from a read-only snapshot of `ee2f068` and wrote only scratch reports. Tranches up to V12 were being published in order while the correction was prepared; none of them touches the ledger content changed here. |
| Governance read | `AGENTS.md`; the change-integration checklist, including the maintained-documents rules; the branch-lifecycle and publication sequence; the initiation policy's architecture lifecycle; the handoff contract; the project-initiation gate control. |
| High-water mark and lock | Unchanged: ANOTHER-LOWER; `SEQUENTIAL_ANALYSIS_LOCK` OPEN, as recorded. |
| Main | Not merged. |

## 2. Responsibility inventory, before and after

| Responsibility | Records | Section size before (characters) | Owner after | Section size after |
|---|---|---|---|---|
| Character state and speech, `SW-S` | 254 | 62,550 | Master | 113,905, after repairs, schema extension and audit register |
| Directional relationships, `SW-R` | 214 | 33,835 | Master | unchanged |
| Chronology and epistemic state, `SW-K` | 160 | 27,294 | Master | unchanged |
| Institutions, world and magic, `SW-W` | 162 | 33,464 | Master | unchanged |
| Claims and revisions, `SW-C` / `SW-CR` | 104 claims, 916 events | 437,596 | [Claims and revisions ledger](../03%20Longitudinal%20Ledgers/SW_CLAIMS_AND_REVISIONS_LEDGER.md) | 654 in the master as a routing statement |
| Prospective questions, `SW-P` | 73 questions in 161 rows | 30,369 | Master | 30,944, with an open-question index |
| Literary form, `SW-F` | 68 | 19,498 | Master | unchanged |
| Readiness, `SW-RD` | 66 | 22,862 | Master | unchanged |
| Unit closure, `SW-U` | 16 unit records | 25,697 | Master | 26,295, with the review-receipt rule |

| File | Before | After |
|---|---|---|
| Master longitudinal ledger | 3,634 lines; 755,572 characters | 2,610 lines; 367,038 characters |
| Claims and revisions ledger | — | 1,367 lines; 474,392 characters |

The brief's V09 figures, 78 claims and 472 events, had grown to 104 and 916 at the live head. The claims section was 58 per cent of the master.

## 3. Claims and revisions extraction

### 3.1 Why the split was justified

Length alone was not the reason. The architecture's split rule asks for independent retrieval or revision pressure, a separate specialist dependency, or conflicting ownership. Two of these held:

- **Independent revision pressure.** Every claim was reviewed, and given an event, at every unit. No other section has that cadence.
- **A separate dependency.** The claims are the primary retrieval route of all eight synthesis arguments, the integrated synthesis and the reconciliation.

### 3.2 What moved and how

- Master section 5, lines 1514 to 2631 at `ee2f068`, moved verbatim as section 5 of the new ledger, under the same heading.
- The master keeps that heading with a routing statement. A reference to "section 5 of the master ledger" therefore finds the route, and the same heading in the new file.
- The new ledger has its own frontmatter, authority, scope, version and canonical home. It adds:
  - field semantics;
  - the claim-review contract;
  - a derived current-view index;
  - review receipts by unit;
  - a corrections register;
  - write and audit rules.
- The master's frontmatter, introduction, initialization block, split record, unit-closure rule and write rules record the split. The master is not described as superseded.

### 3.3 Integrity checks

All checks were run by script against the before-image.

| Check | Result |
|---|---|
| Every pre-migration `SW-C` ID resolves to exactly one claim row in the new ledger | 104 of 104; none missing, none extra, no duplicate. |
| Every pre-migration `SW-CR` ID resolves to exactly one event row | 916 of 916; none missing, none extra, no duplicate. |
| No `SW-C` or `SW-CR` row remains in the master | 0 rows. |
| Moved block preserved | 1,118 lines, of which 1,103 are byte-identical. The other 15 are corrections CX-01 to CX-15, each listed with its original text in the new ledger's section 7. |
| Other families unchanged by the extraction | `SW-R`, `SW-K`, `SW-W`, `SW-P`, `SW-F` and `SW-RD` rows byte-identical. `SW-S` changes are the audit repairs of section 6 only. |
| References from the master to claims and events | 97 distinct `SW-C`/`SW-CR` IDs cited in the master, all resolved in the new ledger. |
| References from the new ledger to other families | 135 distinct IDs, all resolved in the master. |
| Links into the master | No file in the repository links to a heading anchor inside the master ledger. Every file that refers to it refers to the whole file, so no fragment route broke. |
| Frozen readings | Untouched. |

### 3.4 Routing updated

| File | Change |
|---|---|
| Synthesis architecture | Responsibility table, section 4 split record, revision-vocabulary rule, section 10 note. |
| Current-state corpus map | Route key, artifact table rows, a note on the next operation. |
| Analytical method | Revision events and the claim-review contract routed to the new ledger. |
| Volume reading template | Section 9.1 now records a review receipt plus material results. |
| Character reconstruction method | Claim history routed to the new ledger. |
| Longitudinal reconciliation and integrated synthesis | Routing notes; findings unaffected. |
| Cyril Ashley monograph | Amendment where it cited two rows as DEVELOPMENT. |

## 4. Revision-event inflation

### 4.1 What the stream contains

| Transition | Events | Character of the events |
|---|---|---|
| PRESERVE, routine | 574 | "Unchanged (unit)" repeating the full prior formulation, with "see the reading, section 9.1" and no stated reason. |
| PRESERVE, with reason | 12 | A stated reason, for example "no recurrence of the kiss", or "untested". |
| STRENGTHEN | 256 | 220 read "wording unchanged; support extended". The rest change wording within the same claim. 114 cite no observation in the event itself and route to the reading's section 9.1. |
| REVISE | 74 | Including three compound "strengthen and partly revise" events. |
| DOWNGRADE, REJECT, OPEN as transition | 0 | — |

### 4.2 Defects found

Thirteen V04 STRENGTHEN events, SW-CR-0049 to SW-CR-0074, carried the kind "Review, not change." with no evidence. The V04 reading's section 9.1 records STRENGTHEN for each claim, with observations. These events are corrected as CX-01 to CX-13; the original text is kept.

No other event was found to contradict its reading. The 114 STRENGTHEN events that route to the reading were not checked one by one. Whether each strengthened the warrant, rather than adding a similar instance, is not established here.

### 4.3 Correction

The historical stream is kept in full as provenance. The new ledger's section 3 separates claim review from revision events:

- Every applicable claim is reviewed at each unit, and the review is recorded as a receipt in `SW-U` and in the reading's section 9.1.
- A routine no-change review writes no event.
- An event is written only for material strengthening with new observations cited; for REVISE, DOWNGRADE, REJECT or OPEN; for a significant PRESERVE with its reason; or for a correction.

Historical states stay reconstructible, because no routine review ever changed a formulation. The ledger's section 6 gives a review receipt for each closed unit, derived from the stream.

## 5. Claim metadata and the current view

| Field | Finding | Remedy |
|---|---|---|
| Formulation | Current: all 104 match the new formulation of the last wording-changing event. | None needed. |
| Range; class | Ambiguous. For claims registered at V01 to V03 it was widened at the V04 review and then frozen; from V04 on it records only the registering unit. | Kept as written, with the heading clarified (CX-15). The index adds origin, last formulation change, current evidence boundary and last review. |
| Support | Registration support only; later support lives in events. | Heading clarified; the index gives the current evidence boundary and its event. |
| State; confidence | Opens with the state at registration or V02, then indexes the events. Its opening state was stale for twelve claims. Examples: SW-C-0013 still read OPEN after V05's disclosure; SW-C-0022, 0050 and 0058 read "no hypothesis registered" after V08's explanation. | The index gives the current state of every claim. For each stale opening it cites the revision event that resolved it. One component, the alliance in SW-C-0031, is not carried by the current wording, and it is flagged rather than resolved. |
| Claim-records paragraph | Listed registrations only to V04 and said rows were current "after V04 review". | Corrected (CX-14). |

No conclusion was drawn from revision history beyond what the recorded events state.

## 6. Character-state schema and causal-fidelity audit

### 6.1 Method

Two fresh-context analysts each audited a risk-targeted sample against the deep readings, from a read-only snapshot.

- **Records 0001 to 0188.** 26 sampled, 21 of them from V05 to V09.
- **Records 0189 to 0254, plus the change-kind vocabulary.** 25 sampled.

Each proposed repair quoted the current field exactly. A script applied a repair only if that quotation matched the ledger, and all 155 did. Every observation number in the repairs was checked against its unit's register. Two repairs were checked again by the integrator against the V07 and V08 registers (SW-S-0142 and SW-S-0158).

### 6.2 Results

| Classification | V01–V09 sample | Later sample | Total |
|---|---|---|---|
| ADEQUATE | 5 | 1 | 6 |
| PRESENT_ELSEWHERE | 13 | 12 | 25 |
| GENUINELY_UNRESOLVED | 1 | 1 | 2 |
| MATERIAL_DEFECT | 7 | 11 | 18 |
| Sampled | 26 | 25 | 51 |

Because the sample was chosen by risk, these counts are not population rates.

### 6.3 Causes

**The source registers changed form.** From IV -after- on, the readings' observation registers dropped the focalizer and per-row interpretation columns that V01 to V04 carried. The ledger's Process, Persona and Rival fields collapsed at the same unit. The causal material still exists in the readings' close-reading, character and alternative-readings sections, but it was not projected into the ledger. Most defects are therefore projection gaps that the readings fill, not losses of evidence.

**REVEALED_NOT_NEW became a "no process" switch.**

- In V01 to V04, 28 of 49 such rows carry a process chain. In V05 to V09, none of 56 does.
- It was applied to events that are new in their unit, for example Isaac's recognition of the Witch at V09 and Cyril's recognition and sacrifice.

**DEVELOPMENT was a section heading.** The readings' §7 heading was copied into the Kind column. In 25 rows checked, it carried ten senses, and only one was a change measured across units.

**"Keep." replaced the readings' explicit guards.** Examples:

- the V11 reading's "registers no change of disposition" for Isaac's potion refusal;
- the V12 reading's refusal to name Monica's and Cyril's feelings.

**Material misstatements.** Examples:

- Two V08 reveals were merged, losing Porter's mechanism (SW-S-0158).
- The order of causes was reversed in V07's infiltration decision (SW-S-0142).
- At EXTRA09, Cyril calling Monica by name was recorded as unsettling her, when the reading has it unsettling her pleasantly (SW-S-0192).
- At V12, the marriage talk was recorded as unanswered, when Cyril in fact asks Aurelia to decline (SW-S-0228).
- The prequel's amnesia record dropped Adolf's push, Glen's sealing and Louis's unsealing (SW-S-0247).
- EXTRA09 school-year scenes were filed as developments of the later frame (SW-S-0191, 0196).

### 6.4 Repairs

- **Fields.** 155 field repairs in 45 records: Process 45, Rival; uncertainty 45, Obs. 35, Kind 14, State 10, Persona 6.
- **Kinds.** 22 kind edits under the schema extension, eight of them in rows otherwise unchanged. This totals 53 corrected records.
- **Records kept.** Each corrected row ends with an audit note. The master's SW-S section ends with an audit register, SA-01 to SA-53, which keeps the original value of every changed field.
- **No invented causality.** Repairs write "not shown" or "mechanism not shown" wherever the reading gives no link. No unit boundary or ID changed.

### 6.5 Schema extension

The original change-kind paragraph is kept, and the extension follows it in the master's section 1:

- **Kinds.** Each row takes one primary kind. GOAL_CHANGE is adopted, as a real distinction found in V05 and V08 rows. CAPACITY_CHANGE and PERSISTENCE are added. CONTEXT_CHANGE is a synonym of ROLE_CONTEXT_CHANGE.
- **Qualifiers.** Provisional, partial, cumulative, unaware and "internal: KIND". The last lets prequel and collection rows remain REVEALED_NOT_NEW while recording a decision inside their own time.
- **DEVELOPMENT** is retired. Nineteen unsampled rows keep it and are read as "listed among the reading's developments; kind not analysed".
- **Process and uncertainty.** "—" is banned for change rows, and "Keep." is not a value.

### 6.6 Residual issues

- **Unsampled rows.** Of the 254 rows, 201 were not sampled, so further projection gaps of the same kind are likely, especially in AFTER04 to ANOTHER-LOWER rows with "—" or "Keep.". The legacy-reading rule warns users of this.
- **V08 reading inconsistency.** The V08 reading is inconsistent about what Isaac learns when Nero visits him: compare its sections 6.6 and 7.1 with 7.8 and SW-K-0106. SW-S-0158 records the inconsistency as an uncertainty and does not resolve it.
- **Unresolved kinds.** SW-S-0184, a mixed V09 row, was flagged and not re-kinded.
- **Class codes.** "SI" means strong inference in V01 to V04 and structural inference from AFTER04, and NP and UQ disappear after V04. This was not corrected, because a correction would require re-auditing every row's class.
- **Japanese in Process fields.** A few early Process fields contain Japanese wording (SW-S-0085, 0086, 0089). They were not changed.
- **SW-R and SW-K.** These rows were not audited. The same register-column loss probably affects SW-R.

## 7. Decisions on the remaining ledger responsibilities

| Section | Decision | Basis |
|---|---|---|
| `SW-S` | RETAIN; MONITOR | It is the main dependency of monographs and any future reconstruction, and its fidelity problem is projection, not location. Splitting would not repair a "—". If reconstruction models are authorized, a per-subject read-only projection should be tried before a split. |
| `SW-K` | RETAIN | 160 records and 27,294 characters, retrieved together with SW-S and SW-C. The withheld-identity rules live in the readings, the checkpoint and the reconciliation. An index of identity and concealment states would be the smaller remedy if retrieval pressure appears. |
| `SW-RD` | MONITOR; PROPOSE SPLIT only if models are authorized | Evidence reviews only, 66 records, no tests. A separate validation cadence begins only with models, rules and test histories; at that point a readiness-and-validation home is justified. |
| `SW-P` | RETAIN, with index | Retrieval required scanning 161 status rows to find 27 open questions. The open-question index added at the section's head is the smaller remedy. |
| `SW-R` | RETAIN; MONITOR | Not in the brief's list. It probably shares SW-S's projection drift and should be audited by the same method before any monograph revision relies on it. |
| `SW-W`, `SW-F`, `SW-U` | RETAIN | No pressure found. |

No further split is executed.

## 8. Changed paths

| Path | Change |
|---|---|
| `03 Longitudinal Ledgers/SW_CLAIMS_AND_REVISIONS_LEDGER.md` | New, version 1.0. |
| `03 Longitudinal Ledgers/SW_MASTER_LONGITUDINAL_LEDGER.md` | 1.19 to 1.20: claims routed out; SW-S repairs, schema extension and register; SW-P index; SW-U receipt rule; split record. |
| `00 Frameworks and Methods/SW_SYNTHESIS_ARCHITECTURE.md` | 1.25 to 1.26. |
| `00 Frameworks and Methods/SW_ANALYTICAL_METHOD.md` | 1.4 to 1.5. |
| `00 Frameworks and Methods/SW_VOLUME_READING_TEMPLATE.md` | 1.1 to 1.2. |
| `00 Frameworks and Methods/SW_CHARACTER_RECONSTRUCTION_METHOD.md` | 1.2 to 1.3. |
| `03 Longitudinal Ledgers/SW_LONGITUDINAL_RECONCILIATION.md` | 1.0 to 1.1, routing note. |
| `07 Integrated Synthesis/SW_INTEGRATED_SYNTHESIS.md` | 1.0 to 1.1, routing note. |
| `06 Character and Relationship Arguments/SW_CHARACTER_CYRIL_ASHLEY.md` | 1.0 to 1.1, amendment. |
| `CURRENT_STATE_AND_CORPUS_MAP.md` | 1.23 to 1.24. |
| `08 Audits and Manifests/SW_LEDGER_ARCHITECTURE_CORRECTION_REPORT.md` | This report. |

No global registry, housekeeping-owned index, character file, governance file, workflow or source material is changed.

## 9. Publication

The correction is one commit on `series/silent-witch`, after the integrated-synthesis commit. It is published in order after the tranches queued before it, under the stable-branch sequence:

- fetch, then reconcile with the current remote head;
- author preflight;
- recheck the heads, then a non-forced push;
- wait for the exact-head audit.

The commit and audit receipts belong to Git and CI history. This report cannot record its own containing commit.

## 10. Evaluation

| Property | Effect |
|---|---|
| Evidence retrieval | Better. Claims and their history are now one file with an index, and the master's other sections are a third of the old file size. For the 53 corrected character records, the causal chain now names its observations rather than "—". |
| Current-state accuracy | Materially better for claims. Twelve stale states and the misleading range and support fields are now explained by a current view, and all formulations were verified current. Better for the corrected SW-S rows. Unchanged for the 201 unsampled rows, which are flagged. |
| Preservation of historical reasoning | Kept. No event was deleted, and every changed field's original value is in a register. |
| Efficiency of future updates | Better. A unit no longer writes about a hundred unchanged formulations, and the review receipt records the review in one place. |
| Specialist synthesis readiness | Somewhat better. Claims and boundaries are easier to cite, but the existing products already worked from the readings. |
| Character reconstruction readiness | Better in kind for the corrected rows: restored chains, rivals and "not shown" guards are what a model needs. No readiness state changes, because no tier depended on the ledger rows alone. |
| Resistance to compression and schema drift | Better. The kind vocabulary is defined, "—" and "Keep." are ruled out as values, the template asks for receipts, and the claims ledger has a mechanical audit rule. The root cause sat in the reading registers. That cause is named here, but it is not structurally prevented: a later reading could again drop its interpretation columns. |

The result is a smaller master ledger with defined responsibilities, plus a separately maintained claims subsystem, with no accepted evidence or historical state lost. The largest remaining weakness is the 201 character-state rows that were not audited.
