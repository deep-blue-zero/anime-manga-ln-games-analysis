---
series: ASCENDANCE_OF_A_BOOKWORM
artifact_type: longitudinal_ledger_router
scope: CROSS_VOLUME_ANALYSIS
generation: V0.2
status: canonical
release_state: mutable_active
architecture_lifecycle: INITIAL
master_ledger: BOOKWORM_MASTER_LONGITUDINAL_LEDGER.md
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
---

# Ascendance of a Bookworm longitudinal-ledger router

This directory is the canonical home for cumulative cross-volume state.

The day-one architecture initializes **one master pre-split longitudinal ledger**:

- `BOOKWORM_MASTER_LONGITUDINAL_LEDGER.md`

That file is the current cumulative home before V01. It prevents the first sequential readings from accumulating important state only inside isolated volume prose while avoiding a premature forest of empty ledgers.

## Current responsibility map

The master ledger initially owns cumulative state for:

- character identity, developmental state, role/status, bodily limits, competence, resources, and practical agency;
- relationships, reciprocity, dependence, disclosure, patronage, obligation, conflict, and recipient-conditioned behavior;
- institutions, class/status, law/custom, enforcement, coercive leverage, and nominal versus practical freedom;
- knowledge transfer, literacy, education, production, labor, commerce, diffusion, and unintended consequences;
- religion, magic/system mechanics, history, politics, economics, and other world-model claims, with belief/doctrine separated from observed or corroborated mechanism;
- focalization, information asymmetry, secrecy, character knowledge, and reader knowledge;
- ordinary-life evidence when it materially improves reconstruction;
- major claims, counterevidence, revision state, and prospective predictions/open questions.

These are cumulative responsibilities, not predetermined findings.

## Split rule

A responsibility earns its own canonical ledger when one or more of the following become true:

- entries are numerous enough that independent retrieval is materially safer or faster;
- the dimension has an independent revision cadence or evidence schema;
- multiple character or specialist artifacts depend on it directly;
- keeping it in the master file causes repeated reconstruction or duplication;
- it requires an independent audit, locator index, or high-water mark.

Do not split for cosmetic symmetry or because another series has a similarly named ledger.

If a responsibility is split, update:

1. `BOOKWORM_MASTER_LONGITUDINAL_LEDGER.md` with a routing note rather than duplicate current detail;
2. `../CURRENT_STATE_AND_CORPUS_MAP.md` with the new canonical home;
3. `../00 Frameworks and Methods/BOOKWORM_SYNTHESIS_ARCHITECTURE.md` if the split materially changes dependencies or completion gates.

## Part-boundary reconciliation

At V03, V07, V12, V21, and V33, reconcile cumulative state and ask:

- which claims were preserved, strengthened, revised, downgraded, rejected, or remain open;
- whether contradictions remain unresolved;
- whether any master-ledger responsibility should split or merge;
- whether a character/relationship now merits independent analysis;
- whether a specialist synthesis responsibility has become real rather than merely anticipated;
- whether the architecture needs amendment or backfill.

The first mandatory review is after V03 unless a material gap appears earlier.

## Retrieval order

For current cumulative state, read:

1. `../CURRENT_STATE_AND_CORPUS_MAP.md`
2. `../00 Frameworks and Methods/BOOKWORM_SYNTHESIS_ARCHITECTURE.md`
3. `BOOKWORM_MASTER_LONGITUDINAL_LEDGER.md`
4. any dedicated split ledger named by those current surfaces.

Frozen volume readings remain the historical record of prospective source boundaries; current ledgers may revise the mature model without rewriting those freezes.
