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

## Standing team for a narrative unit

For a newly authorized quest, event or substantive reread, the principal reads the entire admitted flow and owns the interpretation, [reading closeout](WUWA_NARRATIVE_DEEP_READING_PROTOCOL.md#closeout) and updates to the five longitudinal ledgers. Establish the game version, quest and TalkSequence IDs, option conditions and entering player and character knowledge before distributing evidence. Freeze prospective judgments before opening later states.

A source-aware specialist independently follows an occurrence through its branch conditions, speaker crosswalk and official text witnesses. Test which choices change an outcome, what a particular interlocutor could know, and whether an apparent trait survives a different relationship or low-stakes exchange. Use the pinned flowState when the selected-quest projection omits the path. Separate ambiguous identity or runtime dispatch from an observed delivery. Where a conclusion depends on tone or staging, assign a listener or viewer with direct access to the matched language render or bounded scene. The zh-Hans text anchor, each dubbed performance, acoustic measurements and selected stills each carry their own evidentiary limits.

A separate critical reviewer directly checks the decisive option, utterance or scene and a material counterexample. Working from the admitted evidence before the principal’s interpretation where practicable, challenge branch conflation, retrospective knowledge, localization overrides and details lost between the source and cumulative account. The principal reconciles both accounts with locators and reasons in the unit closeout. An unresolved path or conflicting account stays open in the existing claim and open-question routes.

Apply [topology §4.1](../../../governance/source-policies/MANGA_ANIME_EXECUTION_TOPOLOGY_AND_CAPABILITY_ROUTING_POLICY.md#multi-agent-source-reading) in independent, frontier-limited contexts. Each reading role starts at `SUBSTANTIVE_ANALYSIS`; escalate a disputed flow, identity or consequential revision in the affected role. For an unusually bounded unit the principal may use one independent contributor/reviewer with a recorded reason and adequate direct inspection. Missing independent access holds acceptance and high-water advance. Retrospective character reconstruction and scene/voice completion follow their specialized protocols and existing authority routes.

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
