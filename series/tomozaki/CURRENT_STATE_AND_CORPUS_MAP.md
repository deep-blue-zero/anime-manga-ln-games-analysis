---
series: TOMOZAKI
artifact_type: current_state_and_corpus_map
scope: GIT_NATIVE_ANALYTICAL_ROOT
source_audit_date: 2026-08-29
generation: V0.1
status: canonical
release_state: mutable_active
---

# Bottom-Tier Character Tomozaki — current state and corpus map

## 1. Responsibility

This is the **canonical current entrypoint** for the Tomozaki analytical root. It answers four questions:

1. What source/evidence boundary is currently available and authoritative?
2. What analytical work has actually been completed?
3. Where does each analytical responsibility live?
4. What is the next source-facing action?

This file is a router and state record. It is not itself a substitute for deep readings, ledgers, monographs, or synthesis.

## 2. Repository and evidence authority

Analytical root: `series/tomozaki/`  
Primary medium: Japanese light novel  
Repository authority: Git for owner-reviewed analytical artifacts under the active repository authority epoch  
Primary/evidence plane: governed Google Drive evidence root  
Series evidence folder ID: `1YldXgz3sglS1CLD_CvUieUM_GOr-VElg` (`Tomozaki`)

The Japanese EPUBs remain outside Git. Git stores analytical interpretation, routing, source-lock metadata, and future derived analytical artifacts.

## 3. Current source boundary

Source lock: [`01 Source Lock and Inventory/TOMOZAKI_SOURCE_LOCK_AND_INVENTORY.md`](01%20Source%20Lock%20and%20Inventory/TOMOZAKI_SOURCE_LOCK_AND_INVENTORY.md)

Current audited inventory, dated 2026-08-29:

- main numbered light novels V01-V11, with no gaps;
- side-story volumes V06.5 and V08.5;
- V07 represented by the acquired Special Edition witness;
- 13 EPUB objects total;
- 13/13 ZIP CRC checks passed;
- 13/13 EPUB container checks passed;
- 11 packaging-conformant under the audit;
- V04 and V11 carry non-blocking `mimetype`-ordering warnings;
- no exact duplicate groups.

This source inventory is **verified**. It does not establish availability or authority for V12+, adaptations, translations, retailer bonuses outside the audited EPUBs, interviews, or reception material.

## 4. Current analytical state

**Bootstrap state only. No substantive source-facing literary analysis has yet been established under this root.**

Current completed responsibilities:

- analytical methodology: established;
- source inventory and source lock: established;
- sequential-reading home: established;
- longitudinal-ledger home: established, with no ledger yet instantiated;
- character-analysis home: established, with no character monograph yet instantiated;
- audit/manifest home: established.

No character is globally enrolled by this bootstrap. Character discovery is maintained independently by the designated curation agent through the canonical `characters/registry.jsonl` and generated `CHARACTER_ANALYSIS_INDEX.md`. This analytical branch does not create character upsert inputs or independently edit either character output. Future eligible Tomozaki character analysis may merge first and be discovered by the curation agent afterward, provided no existing character reference is invalidated.

## 5. Architecture

### `00 Frameworks and Methods/`
Canonical methodological rules for source-facing analysis.

Current artifact:

- `TOMOZAKI_ANALYTICAL_METHOD.md`

### `01 Source Lock and Inventory/`
Exact primary-source boundary, audited witness identity, source integrity, exclusions, and future source-lock revision rules.

Current artifact:

- `TOMOZAKI_SOURCE_LOCK_AND_INVENTORY.md`

### `02 Sequential Readings/`
Canonical home for volume-by-volume source-facing deep readings and bounded prospective freezes.

Current artifact:

- `README.md`

Expected first analytical artifact:

- `TOMOZAKI_V01_DEEP_READING.md`

### `03 Longitudinal Ledgers/`
Canonical home for recurring cross-volume questions once repetition creates a real retrieval/revision need.

Current artifact:

- `README.md`

No substantive ledger exists yet.

### `04 Character Analysis/`
Canonical home for source-grounded character modeling after sufficient longitudinal evidence accumulates.

Current artifact:

- `README.md`

No character monograph or character subdirectory exists yet.

### `08 Audits and Manifests/`
Canonical home for title-local audit and manifest artifacts whose responsibility is provenance, path/state closure, or validation rather than interpretation.

Current artifact:

- `TOMOZAKI_BOOTSTRAP_PATH_MANIFEST.json`

### `.repository/`
Declarative routing inputs consumed by the bounded global-index housekeeping workflow.

Current artifact:

- `series-registry.json`

Directories `05`, `06`, `07`, and `90` are intentionally absent. They should be created only when an actual analytical responsibility requires them.

## 6. Initial analytical questions — not findings

The following are **questions to track**, not conclusions about the series:

- How do explicit social techniques relate to habit, internalization, self-authorship, and authenticity over time?
- When characters state theories about society, games, status, optimization, popularity, romance, or human behavior, which parts are corroborated and which remain viewpoint-bound?
- How independently do competence, confidence, social status, self-concept, agency, and value change move?
- Under what conditions does guidance function as teaching, pressure, dependency, manipulation, overreach, or negotiated mentorship?
- How do friendship, rivalry, mentorship, attraction, romance, family relations, and peer-group positioning affect one another?
- Where do game/rank/optimization metaphors illuminate behavior, and where do they fail?
- What does ordinary-life evidence reveal that explicit self-theory does not?
- How often does focalized self-description diverge from independent behavioral or relational evidence?
- When a learned behavior becomes fluent, does the source support describing it as internalized competence, strategic presentation, value adoption, masking, or some combination?
- How do refusal, disagreement, and self-authored goal-setting change across the series?

These questions are deliberately framed so they can be falsified, revised, or abandoned.

## 7. Main reading order and side-story control

The default prospective main chain is:

`V01 → V02 → V03 → V04 → V05 → V06 → V07 → V08 → V09 → V10 → V11`

Volumes V06.5 and V08.5 are inside the source lock but outside that simple integer-numbered chain. Before either is consulted, establish and record its publication/diegetic placement and the main-volume frozen state it is allowed to inform.

Do not use side-story evidence retroactively to rewrite earlier predictions.

## 8. Work order

1. Treat the 2026-08-29 source lock as the current source boundary.
2. Begin `TOMOZAKI_V01_DEEP_READING.md` from a clean pre-V01 state.
3. Record prospective questions/predictions before advancing to each next unread main volume.
4. Promote recurring questions into longitudinal ledgers only when repeated evidence makes retrieval difficult inside volume readings.
5. Create character monographs only after enough longitudinal evidence exists to support stable/state/recipient distinctions and meaningful abstentions.
6. Create specialist or whole-series synthesis only after its source coverage and analytical responsibility are explicit.

## 9. Bootstrap abstentions

This scaffold deliberately does **not** claim:

- a definitive interpretation of Tomozaki, Hinami, or any other character;
- a romance outcome or ranking;
- a judgment about whether any character's social philosophy is correct;
- a PACTRIH score or comparative-ethics placement;
- an authenticity verdict;
- an adaptation comparison;
- a complete series source boundary beyond V11;
- qualifying global character-registry evidence.

Those claims require later source-grounded work.

## 10. Current next action

**Read and analyze Volume 01 from the audited Japanese EPUB witness, then freeze the first bounded analytical state before consulting Volume 02.**
