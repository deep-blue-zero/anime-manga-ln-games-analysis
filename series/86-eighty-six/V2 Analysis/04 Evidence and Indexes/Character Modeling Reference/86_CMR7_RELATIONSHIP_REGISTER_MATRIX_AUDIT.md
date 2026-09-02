---
series: 86-Eighty-Six
series_id: '86'
artifact_type: audit
artifact_role: RELATIONSHIP_REGISTER_MATRIX_AUDIT
phase: CMR-7
scope: V01-V14+ALTER1; sixteen-profile Character Modeling Reference roster
generation: V2
version: '1.0'
status: canonical
date: '2026-08-19'
source_boundary: Locked original-Japanese V01-V14; Alter.1 audited supplemental; Alter.2 excluded
governing_method: 86_CHARACTER_MODELING_REFERENCE_METHOD.md
governing_architecture: 86_MULTI_DOCUMENT_SYNTHESIS_ARCHITECTURE_V2.md v2.1
audited_matrix: 86_CHARACTER_RELATIONSHIP_REGISTER_MATRIX.md
diagnostic_index: 86_CHARACTER_DIALOGUE_AND_BEHAVIOR_LOCATOR_INDEX.tsv
coverage_audit: 86_CMR7_DIRECTED_RELATIONSHIP_COVERAGE_AUDIT.tsv
validation: 86_CMR7_RELATIONSHIP_REGISTER_MATRIX_VALIDATION.json
promotes_matrix_to_canonical: false
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
---

# 86-Eighty-Six V2 - CMR-7 Relationship/Register Matrix Audit
## Full directed completion, structural repair, asymmetry adjudication, coverage accounting and phase-closure record

# I. Verdict

**Result: `PASS_WITH_CMR7_CORRECTIONS_APPLIED`.**

CMR-7 is complete. The matrix was updated **in place** rather than forked. It now contains **318 unique directed register-state rows**, all with twelve fields and controlled confidence values. The matrix remains `active_provisional`; this audit is the canonical closure record for CMR-7, not a CMR-9 promotion of the profiles or matrix.

The audit covered all **16** profiles, all **2,372** diagnostic controls, the pre-audit **298-row** matrix and all **240** possible profile-to-profile directions.

# II. Governing rule

> **A reverse row is added only when the reverse speaker has independent source support for a stable or analytically decisive register/behavior state.**

Mutual affection, co-presence, shared group membership or the existence of `A → B` does not establish `B → A`.

# III. Corrections applied

## 1. Structural repair

The starting matrix contained eleven malformed rows. Ten received the missing command/request-style field. The Fido-to-Rito/Marcel composite was removed and replaced with two pair-addressable ordinary-cohort rows. The split preserves the shared V08 fishing evidence while explicitly refusing to infer differentiated private registers.

## 2. Confidence normalization

**25** rows used noncontrolled labels such as `MODERATE-HIGH` or confidence-plus-caveat phrases. Every row now uses only `HIGH`, `MODERATE`, `LOW` or `OPEN`. Substantive qualifications were moved into the significant-shift/boundary field rather than discarded.

## 3. Directed completion

CMR-7 added **19** independently warranted speaker-side states, plus the two Fido split rows. The completion set includes reverse-direction evidence that the profile-building sequence had not yet placed in the matrix, but no row was created merely for symmetry.

The most consequential additions are:

- Shin toward Shiden, Vika, Lerche, Rito and Marcel;
- Lena toward Theo, Vika and Rito;
- Raiden and Vika in both directions;
- Vika and Theo in both directions;
- Shiden toward Vika, Theo and Fido;
- Anju toward Grethe and Rito;
- Frederica toward Fido;
- Rito toward Lena.

## 4. Retrieval normalization

Roster aliases were normalized, and bare Rito/Marcel diagnostic identifiers were expanded to stable `86-CMR-*` IDs. Every diagnostic identifier used in the matrix resolves to the shared index.

# IV. Directed coverage result

The final matrix contains **119** distinct directed profile-roster relations. Across the **120** unordered profile pairs:

- **46** have independently evidenced rows in both directions;
- **27** have one evidenced direction only;
- **47** have no independent dyadic row at the locked boundary.

The complete 240-direction disposition is recorded in `86_CMR7_DIRECTED_RELATIONSHIP_COVERAGE_AUDIT.tsv`. Absence means that the current evidence remains collective, incidental, role-level, focalized through another subject or insufficiently stable; it does not mean the characters never interact.

# V. Retained open direction

**Raiden Shuga → Anju Emma** remains `OPEN_UNDERDETERMINED`. Raiden's profile names the relation and the corpus establishes long co-presence and collective co-regulation, but the current source-routed spine does not stabilize a distinct Raiden-to-Anju register. Filling it from Anju-side behavior or generic Spearhead familiarity would violate the directionality rule.

# VI. Duplicate and state-split audit

No exact duplicate content remains. Similar rows were retained only where time, role, emotional state or analytical function differs. Two explicitly reviewed examples are Theo-to-Anju V01 correction versus V14 ordinary return, and Vika-to-Lerche privacy/refusal versus particularity/finality.

# VII. Source and projection controls

- No synthetic dialogue was admitted.
- All exact EPUB anchors introduced outside the diagnostic index were reverified.
- Fido signal/posture rows retain the distinction between direct interiority and human interpretation.
- Lerche remains distinct from Lercheritt.
- Rito's posthumous reception does not manufacture living-person register states.
- Vika's insight remains diagnosis/hypothesis rather than omniscience.
- No reverse emotional symmetry was inferred.

# VIII. Integrity result

- Starting matrix SHA-256: `d83402dc2e8a184c2d4e9513f93648e40fc0aa6506306f1a0ccd2eb0a516a0af`
- Final matrix SHA-256: `9d5e0937048268f3c0c040a4b5fa1faa929ca7c9fc1638dc06e41138886f69b9`
- Final row count: **318**
- Unique row IDs: **318**
- Required fields: **12/12 on every row**
- Controlled-confidence defects: **0**
- Missing diagnostic references: **0**
- Duplicate row IDs: **0**
- Empty evidence routes: **0**
- Failed new-source anchor checks: **0**
- Synthetic evidence rows: **0**

Machine validation: `86_CMR7_RELATIONSHIP_REGISTER_MATRIX_VALIDATION.json`.

# IX. Authority transition and next step

CMR-7 does not alter Documents 01-18, the Phase-5 locator lock, Phase-8 Japanese verification or the 2,372-row diagnostic index. All profiles and the matrix remain `active_provisional` until CMR-9.

The architecture-defined next artifact is **CMR-8 - `86_CHARACTER_MODELING_CROSSWALK.md`**.
