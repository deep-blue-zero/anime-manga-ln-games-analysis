---
series: TOMOZAKI
artifact_type: current_state_and_corpus_map
scope: GIT_NATIVE_ANALYTICAL_ROOT
source_boundary: "Audited Japanese light-novel EPUB corpus: numbered main Volumes 01-11 plus side-story Volumes 06.5 and 08.5; source audit dated 2026-08-29"
source_audit_date: 2026-08-29
generation: V0.3
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

**Volumes 01 and 02 have been read, analyzed, and prospectively frozen. Volume 03 remains unread.**

Current completed responsibilities:

- analytical methodology: established;
- source inventory and source lock: established;
- V01 sequential deep reading: completed and frozen;
- V02 sequential deep reading: completed and frozen;
- first longitudinal ledger: instantiated for effort, competition, goal ownership, stopping conditions, and comparative self-worth;
- character-analysis home: established, with no character monograph yet instantiated;
- audit/manifest home: established.

V01 was read from audited witness `Bottom-Tier Character Tomozaki - Volume 01.epub`, Drive file ID `1B7r3rf0bIZ1gnFg88NTeDa5K6C4LVlF0`, SHA-256 `49d1577da47a22e0838b8430a52bfe24639effcfb519786149cba7ed1d0bc0c4`.

V02 was read from audited witness `Bottom-Tier Character Tomozaki - Volume 02.epub`, Drive file ID `1kCgzfriuHOjBmDOqsgR0MpLEz3aTqI25`, SHA-256 `9eac14b30b4192e41c901e8194e7ab99e306ef8b6226cf8fa18ee71b75a57c5c`.

The bounded V02 state strengthens the V01 finding that Tomozaki's `良ゲー` revision is resilient to failure: Mimimi's 456–131 election defeat produces causal analysis rather than renewed fatalism. V02 also differentiates Tomozaki's mastery-centered effort ethic from Hinami's stronger first-place orientation; activates the risk that Tomozaki can overapply respect for effort when he ignores goal ownership, moving comparison targets, health, and relational costs; reconstructs Mimimi's crisis around comparative self-worth rather than simple jealousy; and establishes Tama's relationship-specific valuation as the decisive non-comparative identity anchor in that crisis. Tomozaki's agency also becomes more bounded: he increasingly recognizes when the correct action is to create conditions for another person's relationship-specific intervention rather than personally control the outcome. The exact claim revisions, counterevidence, abstentions, and V03 predictions are frozen in `02 Sequential Readings/TOMOZAKI_V02_DEEP_READING.md`.

No Tomozaki character is currently enrolled in the canonical character registry. Character discovery is maintained independently by the designated curation agent through `characters/registry.jsonl` and generated `CHARACTER_ANALYSIS_INDEX.md`. This analytical branch does not create character upsert inputs or independently edit either character output. Eligible V01/V02 distributed character analysis may be discovered after merge by the curation agent, provided no existing character reference is invalidated.

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
- `TOMOZAKI_V02_DEEP_READING.md` — V02 closed/frozen

Next expected artifact:

- `TOMOZAKI_V03_DEEP_READING.md`

### `03 Longitudinal Ledgers/`
Canonical home for recurring cross-volume questions once repetition creates a real retrieval/revision need.

Current artifacts:

- `README.md`
- `TOMOZAKI_EFFORT_COMPETITION_AND_GOAL_OWNERSHIP_LEDGER.md` — current through V02

The first ledger is deliberately narrow: it tracks effort regimes, competition, goal origin/ownership, comparison targets, stopping conditions, self-worth coupling, collateral costs, and revision state. It is not a general character ledger.

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

## 6. Current analytical questions after V02

The following questions are frozen for testing against V03 rather than treated as conclusions:

- Does Tomozaki retain the V02 correction that serious effort is not self-validating when the goal, comparison structure, or collateral costs are misaligned?
- Does the main Tomozaki/Hinami disagreement move further from technique toward ends, people as ends rather than pieces, and acceptable optimization?
- What source-grounded motive, stopping condition, or self-worth structure explains Hinami's uncompromising perfectionism?
- Does Mimimi remain ambitious without returning to first-place-dependent identity collapse?
- Can Tomozaki act as strategist without overclaiming control over other people's goals and agency?
- Does Tomozaki's self-concept continue catching up with his improved competence and ordinary social belonging?
- Does the Kikuchi relationship remain genuinely owned rather than primarily serving a Hinami-defined girlfriend objective?
- Does Hinami increasingly treat Tomozaki as a source of surprise and reciprocal competition outside explicitly staged contests?
- How modifiable is `空気` when there is no campaign-style preparation or obvious reframing device?
- Does Tomozaki's new bounded-agency model generalize: recognizing when the right move is to involve another person rather than personally solve the event?

The V02 deep reading contains the controlling confidence bounds, falsifiers, and explicit predictions. The effort/competition/goal-ownership ledger retains the cross-volume state for that promoted responsibility.

## 7. Main reading order and side-story control

The default prospective main chain is:

`V01 → V02 → V03 → V04 → V05 → V06 → V07 → V08 → V09 → V10 → V11`

Current position: **V01-V02 complete; V03 unread.** Preserve both frozen volume states before opening V03.

Volumes V06.5 and V08.5 are inside the source lock but outside that simple integer-numbered chain. Before either is consulted, establish and record its publication/diegetic placement and the main-volume frozen state it is allowed to inform.

Do not use side-story evidence retroactively to rewrite earlier predictions.

## 8. Work order

1. Preserve `TOMOZAKI_V01_DEEP_READING.md` and `TOMOZAKI_V02_DEEP_READING.md` as bounded historical analytical states.
2. Carry the V02 post-state and frozen V03 questions forward without consulting later volumes.
3. Admit the exact audited V03 witness from the source lock.
4. Read V03 as a new evidence increment and classify important V02 claims as PRESERVE, STRENGTHEN, REVISE, DOWNGRADE, REJECT, or OPEN.
5. Update `TOMOZAKI_EFFORT_COMPETITION_AND_GOAL_OWNERSHIP_LEDGER.md` only where V03 materially changes its maintained longitudinal state.
6. Promote other recurring questions into ledgers only when multiple frozen source states make retrieval/revision cumbersome.
7. Create character monographs only after enough longitudinal evidence exists to support stable/state/recipient distinctions and meaningful abstentions.
8. Create specialist or whole-series synthesis only after its source coverage and analytical responsibility are explicit.

## 9. Current abstentions

At the V02 boundary this project deliberately does **not** claim:

- a definitive whole-series interpretation of Tomozaki, Hinami, Mimimi, Tama, Kikuchi, or any other character;
- the full motive, history, or psychological structure behind Hinami's perfectionism;
- that Hinami's public persona is fake or her private presentation is the singular true self;
- that extreme effort, first-place orientation, self-improvement, or competition is inherently healthy or unhealthy;
- that Mimimi has permanently resolved comparative self-worth or envy;
- that Tomozaki's effort ethic is now fully corrected;
- that Tomozaki and Hinami, Tomozaki and Kikuchi, or any other pair has a settled romantic trajectory;
- that Tomozaki has become broadly confident or high-status;
- that learned social behavior is inherently authentic or inherently fake;
- that `空気` explains all group behavior;
- that Tama's relationship-specific valuation will remain sufficient under every future stressor;
- that life is objectively fair or a `神ゲー`;
- a PACTRIH score or comparative-ethics placement;
- an adaptation comparison;
- a complete series source boundary beyond V11;
- a dedicated character monograph or global character-enrollment decision.

Those claims require later source-grounded work.

## 10. Current next action

**Begin the prospective Volume 03 deep reading from the frozen V02 state, using the exact audited Japanese V03 witness and without consulting later volumes first.**
