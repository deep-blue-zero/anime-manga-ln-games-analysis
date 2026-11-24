---
title: "Psycho-Pass — Franchise state and portrait qualification"
artifact_id: PP_FRANCHISE_STATE_LEDGER
artifact_type: franchise_state_ledger
series: psycho-pass
version: "1.1"
status: canonical
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
do_not_use_as_literary_evidence: true
authority_generation: PP-INITIAL
source_boundary: "PP-S01NE-E01 admitted and reconciled"
canonical_home: series/psycho-pass/franchise/ledgers/PP_FRANCHISE_STATE_LEDGER.md
created: 2026-11-18
last_updated: 2026-11-23
---

# Franchise state and portrait qualification

This is the single current canonical home for reconciled character, directed relationship and institution/world state across admitted installments. It also owns individual portrait qualification and the route to each current full portrait. **Current reconciled records through `PP-S01NE-E01`: 18 entities (`PP-ENT-0001`–`0018`), 8 materialized states (`PP-FSTATE-0001`–`0008`), 14 individual qualification assessments (all `DEFERRED_EVIDENCE` at single-episode horizon; 1 `NOT_APPLICABLE` non-human AI), 0 pending monograph obligations, 0 completed portraits.**

## Materialized state contract

Give each person/institution a stable `PP-ENT-####` ID once evidence supports identity. Preserve source-language name, transliteration and meaningful aliases with their legitimate knowledge boundaries. Unknown/provisional identities remain distinct until evidenced equivalence. Record continuity and any source-scoped identity uncertainty.

A state record `PP-FSTATE-####` includes subject and domain, current reconciled conclusion in explanatory prose, boundary through which it is current, contributing installment/edition/unit/local state and claim IDs, decisive locators, contrary cases, confidence and transition history. Explain the mechanism behind a claimed change; a stack of trait labels or links is insufficient. Local observations remain in their source ledger. The master stores only material synthesis and its lineage.

For a person, preserve stable tendencies, changing circumstances, goals, beliefs/knowledge, competencies/limits, self-presentation and meaningful ordinary behavior separately. Do not merge a later identity revelation with what another character knew earlier. For relationships, the canonical key includes A → B and dimension; reciprocity requires separate evidence. For institutions, distinguish professed authority, implemented behavior, constraints, exceptions and consequences. A measurement output remains different from a validated description of a person.

## Qualification register contract

At the first accepted episode, each new differentiated individual is considered; reassess on substantive new evidence and at every declared tranche/installment synthesis boundary. The qualification record carries subject ID/name, continuity, assessed boundary, evidence distribution, rationale, gaps, next review trigger and the actual canonical portrait path once it exists. No name-only roster or fixed lead-character quota controls this decision.

Use `QUALIFIED_PENDING` when sufficient differentiated evidence creates a portrait production obligation, `DEFERRED_EVIDENCE` with a concrete gap/review trigger, `COMPLETE_AT_BOUNDARY` only after both required reviews, and `REASSESS_AFTER_REVISION` when material evidence or correction changes the portrait's basis. An unavailable portrait path is stated as absent rather than linked as if it exists. Counts of pending obligations remain visible in the current handoff.

The [architecture](../../framework/PP_SYNTHESIS_ARCHITECTURE.md#individuals-and-one-canonical-full-portrait) defines the full portrait standard and intended home `franchise/characters/PP_<SUBJECT>_CHARACTER_MONOGRAPH.md`. There is one current full portrait per person/continuity/boundary. Installment states and historical snapshots are scoped evidence, not competing current portraits.

A completion decision names the exact portrait bytes and declared boundary, independent self-containment review and independent source-fidelity review, actual source sample/coverage, required revisions and their disposition, and residual limits. Both reviews must pass for the declared scope; a complete checklist with missing causal/ordinary-life/relationship substance fails. Unknown domains remain stated, not fabricated. Portrait completion does not certify operational reconstruction or simulation readiness.

## Incremental integration and dependencies

The integrator applies accepted local deltas to affected state and qualification records, preserving the previous conclusion and reason for change. A new state with cross-installment consequences also links the [continuity/claim ledger](PP_CONTINUITY_AND_CLAIM_LEDGER.md). If not yet reconciled, keep the older materialized boundary visible with the pending delta ID; do not silently borrow the latest local wording.

A changed psychological, relationship or institutional conclusion identifies dependent portraits, specialist studies and syntheses. Update affected living portraits through dated sourced additions or mark them for reassessment. Frozen prior versions retain their authority boundary and supersession route. At a synthesis boundary, reconcile pending changes and qualification obligations or accurately state that the affected layer is incomplete.

The master never adjudicates a fact solely by citing itself. Reopen decisive source evidence through installment/edition/unit locators under the [integration protocol](../../integration/PP_RECONCILIATION_PROTOCOL.md).

---

## Reconciled Entity & Portrait Qualification Register (Through `PP-S01NE-E01`)

| Entity ID | Canonical Name (`JA` / Transliteration) | Category | Qualification (`PP-S01NE-E01`) | Rationale, Gaps & Next Review Trigger | Canonical Portrait Path |
| --- | --- | --- | --- | --- | --- |
| `PP-ENT-0001` | `常守 朱` / Akane Tsunemori | Person | `DEFERRED_EVIDENCE` | Highest E01 multi-domain breadth (domestic, friends, paperwork, crisis, poise); single-episode horizon only; `Powder Blue` mechanism & multi-case arc unseen. **Trigger:** Reassess at E03–E04 / Tranche 1. | Absent |
| `PP-ENT-0002` | `狡噛 慎也` / Shinya Kōgami | Person | `DEFERRED_EVIDENCE` | Strong crisis/infirmary/lexical split, but core past `"abnormal"` death & `yakume` undisclosed. **Trigger:** Reassess upon disclosure of `"that incident"` or Tranche 1. | Absent |
| `PP-ENT-0003` | `征陸 智己` / Tomomi Masaoka | Person | `DEFERRED_EVIDENCE` | Distinct veteran/mentor contradiction (`127.4`, prosthetic hand, Dominator decoy, `"Sibyl's eye"`), personal history unseen. **Trigger:** Reassess at Tranche 1. | Absent |
| `PP-ENT-0004` | `縢 秀星` / Shūsei Kagari | Person | `DEFERRED_EVIDENCE` | Desk-toy banter vs. explosive cafeteria rupture (`age-5` uncorroborated self-report); needs multi-episode development. **Trigger:** Reassess at Tranche 1. | Absent |
| `PP-ENT-0005` | `宜野座 伸元` / Nobuchika Ginoza | Person | `DEFERRED_EVIDENCE` | Sharp public authority + minor pragmatic gestures; zero private/interior access at E01. **Trigger:** Reassess upon private/history disclosure. | Absent |
| `PP-ENT-0006` | `六合塚 弥生` / Yayoi Kunizuka | Person | `DEFERRED_EVIDENCE` | Minimal dialogue; strong silent solidarity cues (tablet, guitar, off-shift offer) but interiority absent. **Trigger:** Reassess upon focal episode. | Absent |
| `PP-ENT-0007` | `唐之杜 志恩` / Shion Karanomori | Person | `DEFERRED_EVIDENCE` | Single lab scene only (`Latent Criminal` doctor + emotional tact). **Trigger:** Reassess after multi-episode presence. | Absent |
| `PP-ENT-0008` | `槙島 聖護` / Shōgo Makishima | Person | `DEFERRED_EVIDENCE` | Cold-open flashforward monologue & standoff only; absent from main timeline. **Trigger:** Reassess upon main-timeline entry. | Absent |
| `PP-ENT-0009` | `大倉 信夫` / Nobuo Okura | Person (Episodic) | `DEFERRED_EVIDENCE` | Complete tragic/predatory arc ending in death (`00:18:15`); sufficient at local-reading scale. **Trigger:** Reassess only if posthumously referenced. | Absent |
| `PP-ENT-0010` | `島津 千香` / Chika Shimazu | Person (Episodic) | `DEFERRED_EVIDENCE` | Complete hostage-to-therapy arc (`56.3`). **Trigger:** Reassess only if recurring. | Absent |
| `PP-ENT-0011` | `船原 ゆき` / Yuki Funahara | Person | `DEFERRED_EVIDENCE` | Single café scene (`C`-rank friend, mock Sibyl creed). **Trigger:** Reassess upon recurrence. | Absent |
| `PP-ENT-0012` | `水無瀬 佳織` / Kaori Minase | Person | `DEFERRED_EVIDENCE` | Single café scene (`SE` friend, `"intuition as a friend"`). **Trigger:** Reassess upon recurrence. | Absent |
| `PP-ENT-0013` | `少年潜在犯` / Youth Latent Criminal | Person (Episodic) | `DEFERRED_EVIDENCE` | Single mall pre-crime vignette (`俺はまだ何も…`). **Trigger:** Reassess only if recurring. | Absent |
| `PP-ENT-0014` | `キャンディ` / Candy | Non-Human AI | `NOT_APPLICABLE` | Akane's apartment holographic concierge AI (`SC-09`). | Absent |
| `PP-ENT-0015` | `UNNAMED-COLLEAGUE-E01` (`あいつ`) | Provisional Person | `DEFERRED_EVIDENCE` | Smoking officer beside Ginoza (`00:23:50`) & `"abnormal"` death (`00:24:00`); link upon future identity disclosure without backfilling E01. | Absent |
| `PP-ENT-0016` | `シビュラシステム` / Sibyl System | Institution | Tracked via `PP-FSTATE-0006` | Assessed under `H3c` ambivalence at E01. | N/A |
| `PP-ENT-0017` | `公安局刑事課` / PSB CID (Division 1) | Institution | Tracked via `PP-FSTATE-0007` | Hierarchy, Dominator discretion (`任意執行対象`), staffing strain, Commissa-chan policing. | N/A |
| `PP-ENT-0018` | `ドミネーター` / Dominator System | Institutional Artifact | Tracked via `PP-FSTATE-0008` | Biometric lock, directional audio, Paralyzer / Lethal Eliminator modes. | N/A |

## Reconciled Materialized States (`PP-FSTATE-0001` – `PP-FSTATE-0008`, Current Through `PP-S01NE-E01`)

- **`PP-FSTATE-0001` (`PP-ENT-0001` Akane Tsunemori — Character/Agency):** Enters CID Division 1 as an uncertain valedictorian (`700` pts, solitary `A`) who, under warehouse pressure, overrides Kōgami's lethal Dominator shot (`00:21:07`) to protect Chika, endures Ginoza's catwalk override (`00:22:15`), maintains a clear `Powder Blue` Hue despite sleepless guilt, and defends her decision clinically (`一過性`, `00:44:00`). *Lineage:* `PP-S01NE-STATE-0001`, `CLM-0001/0003/0012`. *Confidence:* High (E01-scoped).
- **`PP-FSTATE-0002` (`PP-ENT-0002` Shinya Kōgami — Character/Agency):** Tactical Enforcer haunted by an unnamed colleague's `"abnormal"` death (`00:23:50–00:24:18`). Internally split between `デカ` idealism (`正義 > 役目`) and compulsive survival `始末をつけなきゃならない役目`, yet publicly shields Akane before Ginoza via formal `"義務を果たした"` (`00:44:16`). *Lineage:* `PP-S01NE-STATE-0002`, `CLM-0004/0008`. *Confidence:* High (past cause `OPEN`).
- **`PP-FSTATE-0003` (`PP-ENT-0003` Tomomi Masaoka — Character/Agency):** Veteran Enforcer (`127.4`, articulated metallic prosthetic left hand) fusing tactical craft (biometric-lock decoy, `00:17:45`) and gentle mentorship with fierce field enforcement (`シビュラの目`, `00:19:41`) and internalized hound-fatalism (`犯罪に関わる才能`). *Lineage:* `PP-S01NE-STATE-0003`, `CLM-0006`.
- **`PP-FSTATE-0004` (`PP-ENT-0004` Shūsei Kagari — Character/Agency):** Masks Enforcer captivity (`捕らわれの身`) under playful banter and hostage-rescue urgency (`00:14:48`), erupting over Akane's solitary `A` and his uncorroborated age-5 Latent Criminal classification (`00:39:22–00:40:37`) before silently reassessing her poised CID defense (`00:44:05`). *Lineage:* `PP-S01NE-STATE-0004`, `CLM-0005`.
- **`PP-FSTATE-0005` (`PP-ENT-0005` Nobuchika Ginoza — Character/Authority):** Enforces strict Inspector/Enforcer hierarchy (`飼い主`/`貴様ら`) and overrides Akane's de-escalation from the warehouse catwalk (`00:22:15`), tempered by pragmatic operational support (`00:06:02`) and formal consultation of Kōgami (`00:44:12`); private interiority unseen. *Lineage:* `PP-S01NE-STATE-0005`, `CLM-0011/0012`.
- **`PP-FSTATE-0006` (`PP-ENT-0016` Sibyl System — Institution):** Adjudicated under `H3c` unresolved ambivalence: demonstrates real-time biometric safety, live threat downgrade, and effective therapy (`56.3`), yet enables near-fatal transient misclassification, pre-crime juvenile detention (`00:36:44`), and theological-deontic legitimation (`恩寵`/`ご託宣`/`成す`). Material constitution `OPEN`. *Lineage:* `PP-S01NE-STATE-0014`, `PP-DELTA-0001`, `CLM-0001/0002`.
- **`PP-FSTATE-0007` (`PP-ENT-0017` PSB CID Division 1 — Institution):** Structured around Inspector authority over carceral Enforcers (`任意執行対象`), visible staffing strain, and holographic Commissa-chan surface concealment over forceful street arrests. *Lineage:* `PP-S01NE-STATE-0014`, `PP-DELTA-0002`, `CLM-0007/0011`.
- **`PP-FSTATE-0008` (`PP-ENT-0018` Dominator System — Institutional Artifact):** Biometric-locked, directional-audio enforcement weapon cycling dynamically across locked (`<100`), Non-Lethal Paralyzer (`100–299`), and Lethal Eliminator (`≥300`) modes, acting simultaneously as diagnostic eye and execution arm. *Lineage:* `PP-S01NE-STATE-0014`, `OBS-0005/0007/0011–0014`.
