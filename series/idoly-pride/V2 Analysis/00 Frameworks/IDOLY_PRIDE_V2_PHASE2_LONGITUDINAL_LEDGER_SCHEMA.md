---
series: IDOLY_PRIDE
artifact_type: analytical_method
artifact_role: ANALYTICAL_METHOD
scope: PHASE2_LONGITUDINAL_LEDGER_SCHEMA
generation: V2
version: "1.0"
status: canonical
phase: "2"
source_snapshot_id: IP-V2-SNAPSHOT-2026-08-13-A
source_boundary: "Operational Phase-2 ledger schema derived from the governing V2 method, synthesis architecture, source/evidence protocol, and frozen Phase-2 execution queue. It creates no literary findings."
inherits:
  - IDOLY_PRIDE_V2_ANALYTICAL_METHOD.md
  - IDOLY_PRIDE_V2_SOURCE_EVIDENCE_AND_LEDGER_PROTOCOL.md
  - IDOLY_PRIDE_V2_MULTI_DOCUMENT_SYNTHESIS_ARCHITECTURE.md
  - IDOLY_PRIDE_V2_PHASE2_LONGITUDINAL_LEDGER_QUEUE.md
supersedes: null
superseded_by: null
do_not_use_as_current_authority: false
integrity_status: PHASE2_OPERATIONAL_SCHEMA
created: "2026-08-16"
updated: "2026-08-16"
next_operation: "Apply to P2-A1 Mana longitudinal ledger after P2-0 infrastructure freeze"
recommended_model: "GPT-5.6 Sol"
recommended_reasoning: "Extra High"
---

# IDOLY PRIDE V2 — PHASE 2 LONGITUDINAL LEDGER SCHEMA

## 0. Responsibility

This file instantiates the shared ledger conventions required by P2-0. It does **not** replace the governing method or evidence protocol. Where this operational schema and a governing framework conflict, the governing framework wins unless explicitly amended.

Phase-2 principle:

> **ledger first, synthesis later; chronology and disclosure boundaries must survive endpoint knowledge.**

The frozen substantive inheritance entering Phase 2 is `IDOLY_PRIDE_V2_PHASE1_FINAL_BASELINE.md`.

---

## 1. Stable identifier grammar

Use stable ASCII identifiers wherever practical.

- character claim: `IP-CHAR-<CODE>-NNN`
- relationship claim: `IP-REL-<PAIR_OR_SLUG>-NNN`
- unit claim: `IP-UNIT-<CODE_OR_SLUG>-NNN`
- theme/institution claim: `IP-THEME-<SLUG>-NNN` / `IP-INST-<SLUG>-NNN`
- formal dependency: `IP-FORM-NNN`
- source delta: `IP-DELTA-YYYYMMDD-NNN`

Existing stable source IDs such as `st-main-*`, `st-eve-*`, `card_*`, `bond_*`, `message-*`, and `tel-*` remain unchanged and should not be wrapped in invented aliases.

Claim IDs are retrieval handles, not assertions of truth. A rejected or revised claim retains its identifier and transition history.

---

## 2. Required claim-entry fields

Every consequential longitudinal entry should carry the following fields when applicable:

```yaml
claim_id:
subject:
claim:
scope:
chronological_position:
disclosure_position:
epistemic_class:
transition_state:
prior_claim_or_authority:
source_bundle_id:
source_story_id:
source_locator:
supporting_evidence:
counterevidence:
formal_dependency:
canonical_destination:
validated_through:
last_retested:
source_snapshot_id:
update_status:
open_questions:
```

Optional but useful fields include `relationship_category`, `confidence`, `branch_semantics`, `voice_register`, and `phase1_provenance`.

---

## 3. Epistemic classes

Preserve the governing method's evidence classes exactly:

1. **TEXTUAL FACT** — directly established by dialogue, narration, metadata, or explicit story events.
2. **AUDIOVISUAL FACT** — directly established by visible or audible presentation.
3. **STRONG INFERENCE** — not directly stated, but supported by converging signals with little meaningful counterevidence.
4. **INTERPRETATION** — defensible explanatory model that organizes evidence but is not uniquely compelled.
5. **SPECULATION / OPEN HYPOTHESIS** — plausible but insufficiently stabilized.
6. **CONFLICT / AMBIGUITY** — materially unresolved competing readings or continuity/source tension.

Do not convert absence of contradiction into TEXTUAL FACT.

---

## 4. Phase-2 transition vocabulary

For longitudinal claim transitions, use the project-standard Phase-2 vocabulary:

- `PRESERVE`
- `STRENGTHEN`
- `REVISE`
- `DOWNGRADE`
- `REJECT`
- `OPEN`

Historical V1-comparison fields may additionally preserve the older audit vocabulary (`CONFIRMED`, `STRENGTHENED`, `QUALIFIED`, `SPLIT`, `WEAKENED`, `OVERTURNED`, `RECONTEXTUALIZED`, `UNRESOLVED`) when that distinction is analytically useful. Do not mix the two vocabularies in one field.

---

## 5. Locator convention

Preferred evidentiary descent:

> **claim → Phase-2 ledger → Phase-1 audit/checkpoint → exact bundle/story locator → extracted source**

A load-bearing locator should identify as much of the following as exists:

```yaml
bundle_id:
story_id:
scene_or_section:
utterance_or_line_range:
message_id:
telephone_id:
asset_id:
source_path:
```

Use exact Japanese quotation only when it is necessary and verified against the appropriate textual/audio source. Do not quote approximate telephone ASR as if it were an official transcript.

---

## 6. Chronology versus disclosure

Every longitudinal ledger must distinguish:

- **story chronology** — when an event occurs in the fictional timeline;
- **release/disclosure order** — when the audience/analysis first receives the information;
- **analytical validation frontier** — the newest source snapshot against which a claim has actually been retested.

Later revelation may recontextualize an earlier event without erasing what was genuinely unknown at the earlier disclosure frontier.

Default unresolved rule:

> **`BOND_TEMPORAL_PLACEMENT_UNFIXED` remains in force unless the source itself supplies enough evidence to place the bond more precisely.**

---

## 7. Freshness semantics

`source_snapshot_id` records the source set available to the ledger.

`validated_through` means the claim/entity has actually been longitudinally checked through that source frontier. It must **not** advance merely because the snapshot exists or because an unrelated source was analyzed.

At P2-0 initialization:

> all character/unit registry entries retain `validated_through: null` until their relevant Phase-2 ledger is completed.

`CHARACTER_UNIT_UPDATE_STATUS.md` is the authoritative freshness registry.

---

## 8. Source-delta semantics

Every later extraction snapshot is compared against `IP-V2-SNAPSHOT-2026-08-13-A` or its audited successor through `SOURCE_DELTA_LEDGER.md`.

Change types:

- `added`
- `modified`
- `removed`
- `replaced`
- `asset-added`
- `upstream-correction`

Impact classes:

- `CLASS-1 ADDITIVE-TEXTURE`
- `CLASS-2 SIGNIFICANT-DEVELOPMENT`
- `CLASS-3 ARCHITECTURAL`

Class is determined by semantic impact, not prestige or source class.

---

## 9. Formal-dependency semantics

Use `IDOLY_PRIDE_V2_FORMAL_DEPENDENCY_LEDGER.md` for formal evidence state.

Telephone states:

- `PHONE-AUDIO-VERIFIED` — source audio has actually been reviewed for the claim at issue.
- `PHONE-ASR-SUPPORTED` — cached source audio and approximate ASR exist, but the exact formal claim has not necessarily been manually audio-verified.
- `PHONE-GAP` — upstream source audio is unavailable; no audio/ASR content may be reconstructed.

Formal-effect states:

- `NONBLOCKING_TEXT_ONLY_GAP`
- `FORMAL_NUANCE_UNAVAILABLE`
- `LOAD_BEARING_FORMAL_CLAIM_BLOCKED`
- `PHASE5_REVIEW_REQUIRED`
- `RECOVERED`

A textual claim may remain valid when an unrelated formal asset is missing. A vocal/staging/music claim may not.

---

## 10. Makino branch semantics

The customizable game manager remains the continuation of **Makino Kouhei**.

Use:

- `IDENTITY-INVARIANT MAKINO FACT` for branch-independent facts/history/actions;
- `PLAYER_SELECTED_MAKINO_EXPRESSION` for mutually exclusive selectable lines;
- repeated cross-branch traits may strengthen stable characterization;
- impossible co-occurrence must remain explicit;
- custom `{user}` naming is interface parameterization, not a different person.

The mandatory `IDOLY_PRIDE_V2_MAKINO_PLAYER_BRANCH_CANON_LEDGER.md` owns this distinction during P2-A.

---

## 11. Counterevidence rule

Every major ledger section should actively search for:

- contrary dialogue/action;
- source-class limitations;
- chronology conflicts;
- alternative relationship category evidence;
- branch-specific exceptions;
- formal evidence not available in transcript;
- later material that narrows rather than merely strengthens a claim.

A ledger with no counterevidence field is not evidence of uncontested truth.

---

## 12. Canonical topical homes

Do not duplicate the same claim across many ledgers without routing ownership.

Default ownership:

- character change → character longitudinal ledger;
- relationship-state change → relationship ledger, with character ledgers linking to it;
- unit constitution/governance → unit ledger;
- recurrent cross-unit mechanism → theme/institution ledger;
- source freshness → `SOURCE_DELTA_LEDGER.md` / `CHARACTER_UNIT_UPDATE_STATUS.md`;
- missing audio/visual/formal evidence → formal-dependency ledger;
- polished interpretive argument → Phase 3+ synthesis, downstream of ledgers.

---

## 13. Relationship-category safeguard

Relationship evidence must separate:

- textual relationship fact;
- culturally legible romantic/yuri coding;
- unusually intimate friendship;
- interpretive possibility;
- unsupported shipping.

A one-sided romantic state is not automatically reciprocal. Public/audience pairing recognition is not private relationship-status proof.

---

## 14. Update transaction

When a ledger changes materially:

1. identify the exact new or newly promoted source;
2. retest the prior claim;
3. assign transition state;
4. record counterevidence and formal limits;
5. update `validated_through` only for the affected entity/claim;
6. route any Class-2/3 downstream work into `PENDING_REANALYSIS_QUEUE.md`;
7. update `CURRENT_STATE_AND_CORPUS_MAP.md` only when project state materially changes.

No silent endpoint rewriting.
