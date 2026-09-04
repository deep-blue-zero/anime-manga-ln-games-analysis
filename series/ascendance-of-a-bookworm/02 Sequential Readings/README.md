---
series: ASCENDANCE_OF_A_BOOKWORM
artifact_type: sequential_reading_contract
scope: VOLUME_BY_VOLUME_ANALYSIS
generation: V0.2
status: canonical
release_state: mutable_active
architecture_lifecycle: INITIAL
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
---

# Ascendance of a Bookworm sequential readings

This directory is the canonical home for source-bounded numbered-volume deep readings.

## Naming and identity

Use global numbered filenames:

- `BOOKWORM_V01_DEEP_READING.md`
- `BOOKWORM_V02_DEEP_READING.md`
- continuing through `BOOKWORM_V33_DEEP_READING.md` as analysis proceeds.

Each reading should record:

- global volume number;
- Japanese part title/number and within-part Roman-numeral identity from the audited source metadata;
- normalized EPUB filename;
- audited SHA-256 or deterministic manifest locator;
- source boundary/generation used;
- entering committed high-water mark;
- exiting freeze state after closeout.

Do not restart filenames at each part. Do not create placeholder files for unread volumes.

## Prospective rule

Each numbered main volume is read from the frozen analytical state produced by the prior numbered volume. Before opening a new volume for analysis, recover material expectations/open questions from `../03 Longitudinal Ledgers/README.md` and the prior frozen reading. After reading, classify meaningful outcomes as confirmation, extension, complication, revision, falsification, or still open, then freeze the new state before advancing.

Later volumes can revise the current model. They cannot rewrite the historical record of what the earlier source boundary supported.

## Atomic completion contract

A numbered-volume transaction is complete only when all applicable architecture-defined state advances with it.

For VNN, complete the following before VNN+1 is opened:

1. resolve the exact Japanese source witness and part identity;
2. recover the entering prospective boundary;
3. write the VNN deep reading;
4. propagate material cumulative observations into `../03 Longitudinal Ledgers/README.md`;
5. adjudicate any earlier material claim or prediction that VNN tests;
6. preserve new major open claims and bounded next-volume expectations;
7. retain evidence locators in the deep reading or promote them to the evidence/index layer if cross-volume retrieval has become necessary;
8. advance `../CURRENT_STATE_AND_CORPUS_MAP.md` to the new committed high-water mark;
9. freeze the exiting state.

Standalone prose without required cumulative propagation does not close the atomic source-unit transaction.

## Execution scope

The sequential-execution policy is independent of this reading method.

- A request naming one next volume defaults to `single_operation`: close that volume completely, identify the next operation, and stop.
- A bounded multi-volume run requires explicit `continuous_sequential` authorization and a recoverable terminal boundary.
- Continuous authorization does not permit later-volume knowledge to leak backward into earlier prospective freezes.

The durable Git corpus, not conversational memory, defines the committed high-water mark.

## Part boundaries

The locked main sequence is:

- Part 1: V01-V03
- Part 2: V04-V07
- Part 3: V08-V12
- Part 4: V13-V21
- Part 5: V22-V33

After V03, V07, V12, V21, and V33, perform an architecture review. A part-boundary checkpoint synthesis is created only if it owns useful cross-volume retrieval responsibility; it must not substitute for the underlying volume readings.

## Supplemental sequencing

*Royal Academy Stories: First Year* is not part of the numbered V01-V33 prospective chain. Before reading it analytically, verify its publication/diegetic placement and decide which already-frozen main-volume state it may legitimately test or extend.

Do not use supplemental evidence to rewrite predictions made before that evidence was opened.

## Minimum deep-reading responsibilities

A numbered deep reading should cover, as evidence warrants:

- scene/event structure and focalization;
- character-state changes and contradictions;
- relationship/network developments;
- names, titles, roles, affiliations, and information-state changes;
- institutions, status, rules, enforcement, and practical agency;
- work, production, education, knowledge transfer, and economic consequences where material;
- ordinary-life, bodily-limit, risk, and competence evidence when diagnostic;
- world-model claims separated from focalized belief or institutional doctrine;
- Japanese diction/register/terms of address when wording bears on interpretation;
- direct evidence versus inference;
- rival readings and counterevidence;
- revision state of material prior claims;
- prospective expectations/open questions for the next unread numbered volume;
- explicit notes on what was promoted to longitudinal state and why.

The deep reading is an analytical artifact, not a chapter-by-chapter plot transcript.

## Evidence routing

Initially, exact passage locators and wording-sensitive observations may remain local to the deep reading. Promote a dedicated cross-volume locator/terminology structure only when mature claims repeatedly require retrieval across multiple volumes.

Do not duplicate the full source audit or primary-source text in Git.

## Architecture amendment trigger

If a volume exposes a recurring dimension that the current master longitudinal ledger cannot represent responsibly, amend the architecture before continuing indefinitely with a known gap. A new dimension does not automatically require rereading all prior volumes; backfill only when the missing responsibility creates a material evidence deficit.
