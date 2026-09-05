---
series: TOMOZAKI
artifact_type: current_state_and_corpus_map
scope: GIT_NATIVE_ANALYTICAL_ROOT
source_boundary: "Audited Japanese light-novel EPUB corpus: numbered main Volumes 01-11 plus side-story Volumes 06.5 and 08.5; source audit dated 2026-08-29"
source_audit_date: 2026-08-29
generation: V0.2
status: canonical
release_state: mutable_active
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
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

**Volume 01 has been read, analyzed, and prospectively frozen. Volume 02 remains unread.**

Current completed responsibilities:

- analytical methodology: established;
- source inventory and source lock: established;
- V01 sequential deep reading: completed and frozen;
- longitudinal-ledger home: established, with no ledger yet instantiated;
- character-analysis home: established, with no character monograph yet instantiated;
- audit/manifest home: established.

V01 was read from audited witness `Bottom-Tier Character Tomozaki - Volume 01.epub`, Drive file ID `1B7r3rf0bIZ1gnFg88NTeDa5K6C4LVlF0`, SHA-256 `49d1577da47a22e0838b8430a52bfe24639effcfb519786149cba7ed1d0bc0c4`.

The bounded V01 state establishes, at high confidence, that Tomozaki begins with a pre-existing effort ethic and disciplined learning capacity; that his social fatalism is a domain-specific exemption rather than generalized passivity; that multiple social subskills improve through practice without proving Hinami's universal `神ゲー` claim; that competence improves faster than global confidence or self-concept; that learned technique begins to become owned competence; and that agency increases through unassigned, value-driven actions. The exact claim states, counterevidence, abstentions, and V02 predictions are frozen in `02 Sequential Readings/TOMOZAKI_V01_DEEP_READING.md`.

No character is globally enrolled by this V01 analysis. Character discovery is maintained independently by the designated curation agent through the canonical `characters/registry.jsonl` and generated `CHARACTER_ANALYSIS_INDEX.md`. This analytical branch does not create character upsert inputs or independently edit either character output. Future eligible Tomozaki character analysis may merge first and be discovered by the curation agent afterward, provided no existing character reference is invalidated.

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

Current artifacts:

- `README.md`
- `TOMOZAKI_V01_DEEP_READING.md` — V01 closed/frozen

Next expected artifact:

- `TOMOZAKI_V02_DEEP_READING.md`

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

## 6. Current analytical questions after V01

The following questions are frozen for testing against V02 rather than treated as conclusions:

- Does Tomozaki's `良ゲー` revision survive meaningful negative evidence, or does confidence collapse faster than competence?
- Will the main disagreement with Hinami increasingly concern **ends and values** rather than whether her techniques work?
- Can Tomozaki integrate learned technique with his direct considered-expression style without one erasing the other?
- How broadly does `空気` generalize across different groups, and who can resist or rewrite it at what cost?
- What mixture of gamer respect, mentorship, project investment, friendship, control, and possible affection explains Hinami's investment in Tomozaki?
- Does Nakamura's newly demonstrated effort produce a more reciprocal rivalry?
- Does Yuzu's costly resistance to group pressure recur outside the exact V01 confrontation?
- Can the Kikuchi relationship develop on an honest basis after the false shared-interest reset?
- Does Tomozaki eventually overgeneralize the opposite lesson and begin treating structural constraints or other people's agency as controllable through sufficient correct effort?
- Which dimensions move next: competence, confidence, status, self-concept, agency, or values?

The V01 deep reading contains the controlling confidence bounds, falsifiers, and explicit predictions. These questions may be falsified, revised, or abandoned by later evidence.

## 7. Main reading order and side-story control

The default prospective main chain is:

`V01 → V02 → V03 → V04 → V05 → V06 → V07 → V08 → V09 → V10 → V11`

Current position: **V01 complete; V02 unread.** Preserve the V01 freeze before opening V02.

Volumes V06.5 and V08.5 are inside the source lock but outside that simple integer-numbered chain. Before either is consulted, establish and record its publication/diegetic placement and the main-volume frozen state it is allowed to inform.

Do not use side-story evidence retroactively to rewrite earlier predictions.

## 8. Work order

1. Preserve `TOMOZAKI_V01_DEEP_READING.md` as the bounded V01 historical analytical state.
2. Admit the exact audited V02 witness from the source lock.
3. Before opening V02, record any genuinely new pre-read prediction only if it arises independently of V02 evidence.
4. Read V02 as a new evidence increment and classify important V01 claims as PRESERVE, STRENGTHEN, REVISE, DOWNGRADE, REJECT, or OPEN.
5. Promote recurring questions into longitudinal ledgers only when repeated cross-volume evidence makes retrieval difficult inside sequential readings.
6. Create character monographs only after enough longitudinal evidence exists to support stable/state/recipient distinctions and meaningful abstentions.
7. Create specialist or whole-series synthesis only after its source coverage and analytical responsibility are explicit.

## 9. Current abstentions

At the V01 boundary this project deliberately does **not** claim:

- a definitive whole-series interpretation of Tomozaki, Hinami, or any other character;
- that Hinami's public persona is fake or her private presentation is the singular true self;
- that Hinami is benevolent, manipulative, romantic, or emotionally detached in any final sense;
- a romance outcome or ranking;
- that Tomozaki has become broadly confident or high-status;
- that learned social behavior is inherently authentic or inherently fake;
- that `空気` explains all group behavior;
- that life is objectively fair or a `神ゲー`;
- a PACTRIH score or comparative-ethics placement;
- an adaptation comparison;
- a complete series source boundary beyond V11;
- a dedicated character monograph or global character-enrollment decision.

Those claims require later source-grounded work.

## 10. Current next action

**Begin the prospective Volume 02 deep reading from the frozen V01 state, using the exact audited Japanese V02 witness and without consulting later volumes first.**
