---
series: WUWA
artifact_type: synthesis_architecture
scope: LONGITUDINAL_STORY
source_boundary: "Versioned Wuthering Waves releases and source-bounded analytical generations"
generation: V0.1
status: canonical
release_state: mutable_active
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
---

# WUWA longitudinal story-analysis architecture

## Problem

*Wuthering Waves* is a continuing game. Patch order, fictional chronology, character memory, archive unlock order, retellings, and later revelations can diverge. A single static synthesis will quickly become misleading unless state transitions and claim revisions remain independently retrievable.

## Analytical layers

### Sequential readings

Bounded readings preserve local sequence, scene context, branch structure, and contemporaneous interpretation.

### Longitudinal ledgers

Ledgers accumulate cross-reading state without replacing the readings:

- character-state crosswalk;
- relationship network;
- world/faction state;
- chronology;
- open questions.

### Character analysis

Character monographs synthesize state-bounded evidence and may be revised as later releases add material. Earlier source-bounded generations remain recoverable through Git history and explicit revision ledgers.

### Specialist synthesis

Create only after a recurring analytical dimension spans multiple readings or characters—for example Sentinel-human relations, institutional legitimacy, Resonator identity, memory/personhood, regional political economy, or music/performance systems.

### Full-series/release synthesis

For a live-service work, "full-series" means a declared release boundary, not completion of the franchise. Use versioned scope such as `THROUGH_3_6_0` and never silently roll later material backward.

## Chronology dimensions

The chronology ledger should distinguish:

- `release_order`;
- `diegetic_order`;
- `player_epistemic_order`;
- `character_epistemic_state`;
- `retrospective_or_reenacted`;
- `uncertain_or_conflicting`.

## Update transaction

A substantive reading or character update should atomically update the relevant:

- canonical artifact;
- claim-revision ledger;
- longitudinal ledgers;
- character/claim indexes;
- current-state map;
- corpus manifest/audit.

## Claim persistence

Later evidence may preserve, strengthen, revise, downgrade, reject, or reopen a claim. Do not rewrite the historical analytical situation as though the later revelation was always available to the player or character.

## Version transition

When a new game/source release becomes analytically active:

1. freeze or identify the prior evidence generation;
2. create a source/release delta and update source boundary;
3. identify affected story units and characters;
4. test earlier claims rather than assuming continuity;
5. record claim transitions;
6. update current authority pointers;
7. preserve the earlier source-bounded analytical state.
