---
title: "IDOLY PRIDE V2 Source Cutoff and Project Decisions"
project: "IDOLY PRIDE"
document_id: "IDOLY_PRIDE_V2_SOURCE_CUTOFF_AND_PROJECT_DECISIONS"
version: "1.1"
status: "phase-0-governing-decisions"
source_snapshot_id: "IP-V2-SNAPSHOT-2026-08-13-A"
source_cutoff: "2026-08-13"
created: "2026-08-13"
updated: "2026-08-13"
framework_version: "2.1"
canonical_framework_set: "IP-V2-FRAMEWORK-2026-08-13-AV"
---

# IDOLY PRIDE V2 SOURCE CUTOFF AND PROJECT DECISIONS

## 1. Governing snapshot

The initial V2 source lock is:

`IP-V2-SNAPSHOT-2026-08-13-A`

Game-data frontier:

`2026-08-13T20:13:01+00:00`

Ingest generated:

`2026-08-13T20:24:41+00:00`

Anime frontier:

complete TV anime Episodes 01-12, represented by the exact analysis ZIPs hashed during Phase 0.

4koma frontier:

archive manifest dated 2026-08-09.

This snapshot is a baseline for a live service, not an assertion that later canon does not exist.

## 2. Governing source model

The V2 project adopts the following source transformation model for game narrative text:

`game data -> extracted/normalized corpus -> idoly-ingest -> analysis_bundles`

The majority of Japanese narrative text in the derived corpora is treated as game-extracted source text with transformation provenance, not as fan-authored paraphrase.

## 3. Default reading layer

Decision:

`analysis_bundles` is the preferred first-pass analytical interface.

Reason:

It consolidates the large fragmented corpus into character-, source-, and chronology-oriented bundles while preserving granular source paths.

This is an interface decision, not a downgrade of evidentiary rigor.

## 4. Context-descent rule

Decision:

Descend from `analysis_bundles` to `idoly-ingest` for exact context, quotations, canonical locators, ambiguity, source-order questions, contradictions, and other load-bearing evidentiary needs.

Do not repeatedly reread lower-level raw material when the source-preserving bundle already answers the question adequately.

## 5. Historical selected-events folder

Decision:

`idoly-ingest-selected-events-core-important` is advisory only.

It may accelerate discovery and preserve why earlier analyses focused on particular events. It does not determine V2 importance.

The V2 Corpus Coverage and Priority Ledger is authoritative.

## 6. Manager identity and continuity

Decision:

For V2 analysis, the customizable game manager is treated as the narrative continuation of Makino Kouhei from the anime unless primary evidence in a specific context creates a material contradiction.

Player-choice branches remain part of the source corpus. They should be analyzed as a constrained range of Makino-compatible responses rather than as proof that he has no stable characterization.

## 7. Anime status

Decision:

The 12-episode TV anime is a governing narrative source, not merely promotional background for the game.

It is especially important for:

- Mana and Makino;
- Sakura and Kotono;
- the original Hoshimi group formation;
- SUNNY PEACE and Tsuki no Tempest formation;
- Nagisa/Kotono;
- Rio/Aoi/LizNoir;
- Mana's ghostly presence;
- vocal performance, blocking, camera, editing, music, and stage form.

The anime must be used as audiovisual evidence where presentation matters. Subtitle text alone is insufficient for claims about delivery or cinematic form.

Sequencing correction:

The canonical framework set inserts **Phase 0.5: prospective complete anime deep reading** immediately after this source lock and before Phase 1 game-corpus reconnaissance. All twelve episodes are reviewed as a bounded audiovisual work under the information conditions of the anime itself, producing a frozen anime-endpoint state. Later game material may trigger targeted retrospective anime review in Phase 5, but must not erase the prospective baseline.

Game audiovisual material is not ingested exhaustively. The dedicated audiovisual protocol governs selective escalation using AV-A/B/C/D priorities, representative voice sampling, and dramaturgical selection of songs, MVs, live sequences, and voiced story/card scenes.

## 8. Anime bundle identity and minor repacking differences

Decision:

The exact Episode 01-12 ZIPs supplied in the current project conversation are the Phase 0 anime snapshot.

Their SHA-256 hashes govern exact archive identity.

Minor byte-size mismatches against an earlier extraction manifest are accepted as non-substantive where internal episode identity, screenshots/contact-sheet counts, source paths, subtitle provenance, audio presence, and episode duration remain coherent. The user has identified screenshot deduplication as a plausible source of such repacking differences.

These differences do not block Phase 0.

## 9. Episode 1 subtitle discrepancy

Decision:

The small mismatch between the Episode 1 bundled subtitle snapshot and the separate timing-audit record is logged as a known provenance discrepancy.

It does not block the anime source lock because:

- episode identity is established independently;
- the bundle remains analytically usable;
- the current exact archive is hashed;
- the separate timing audit is retained as provenance rather than silently treated as byte-identical to the ZIP's embedded subtitle copy.

For a quote-sensitive Episode 1 claim, verify against the subtitle file actually present in the locked bundle and, when necessary, against audio.

## 10. Telephone evidence

Decision:

Telephone source audio is primary evidence when present.

Telephone ASR is classified as provisional derived evidence.

Use status labels:

- `PHONE-AUDIO-VERIFIED`;
- `PHONE-ASR-SUPPORTED`;
- `PHONE-GAP`.

Unverified ASR cannot solely establish subtle linguistic claims or exact quotations.

## 11. Missing processed transcript assets

Decision:

The 32 missing processed asset references are explicit known gaps, not evidence of general corpus unreliability.

Most are `adv-live-*` formal/live assets. One recorded gap is a card visual. These items should be routed to audiovisual/formal follow-up when relevant.

Narrative transcripts around those source stories remain usable unless a specific missing asset is necessary for the claim.

## 12. 4koma status

Decision:

Official 4koma is supplementary canon-adjacent characterization/social-texture evidence.

It may support:

- ordinary-life characterization;
- recurring comic behavior;
- relationship texture;
- visual motifs;
- editorial emphasis.

It should not automatically outweigh main story, unit origins, or major developmental events.

## 13. Visual assets

Decision:

Card art, photos, key visuals, anime frames, 3DMVs, and live sequences can establish audiovisual facts.

Every visual argument must distinguish:

1. visible fact;
2. interpretation of that fact;
3. cross-source inference.

Do not derive visual conclusions from prose-only sources.

## 14. Japanese-language priority

Decision:

Original Japanese is the governing linguistic evidence where available.

When wording matters, preserve:

- original Japanese;
- literal sense;
- natural English gloss;
- source locator;
- explanation of the relevant nuance.

Do not make a language-based argument from an English paraphrase when the Japanese distinction is the actual evidence.

## 15. Historical analysis treatment

Decision:

Prior chats and V1 documents are historical analytical sources only.

Allowed uses:

- recover hypotheses;
- locate previously identified evidence;
- reconstruct why an interpretation emerged;
- compare V1 and V2 conclusions.

They may be CONFIRMED, STRENGTHENED, QUALIFIED, SPLIT, WEAKENED, OVERTURNED, RECONTEXTUALIZED, or UNRESOLVED.

They never override primary-source review.

## 16. Live-service update model

Decision:

The active V2 workspace is rolling and mutable. Frozen releases are immutable.

New source snapshots after `IP-V2-SNAPSHOT-2026-08-13-A` must be delta-audited and assigned semantic impact:

- Class 1: additive texture;
- Class 2: significant development;
- Class 3: architectural material.

New material updates only the claims and documents it actually affects. It does not force a complete reread from zero.

## 17. Temporal claim provenance

Decision:

Consequential claims should ultimately record:

```yaml
validated_through:
last_retested:
source_snapshot_id:
update_status:
```

A claim's validation frontier must not advance merely because unrelated new content was released.

## 18. New characters and units

Decision:

Newly introduced live-service characters or units begin with provisional ledgers.

Definitive synthesis is delayed until sufficient longitudinal evidence exists to test introductory characterization.

## 19. Source gaps and uncertainty

Decision:

Known gaps are preserved explicitly.

Do not silently fill them from memory, fan wikis, translation sites, or general franchise knowledge.

External research may be used only when separately requested or when required to resolve provenance, and must remain clearly distinguished from the locked primary-source corpus.

## 20. Phase 0 completion criterion

Phase 0 is complete when:

- source roots are identified;
- current source snapshot is dated and named;
- major source classes are inventoried;
- exact anime bundles are hashed;
- corpus validation is recorded;
- known gaps are recorded;
- governing source decisions are frozen;
- a future delta-update path exists.

The present Phase 0 package satisfies those criteria. Under canonical framework set `IP-V2-FRAMEWORK-2026-08-13-AV`, the next analytical step is **Phase 0.5: prospective complete anime deep reading**. After the anime-endpoint baseline is frozen, proceed to Phase 1: Corpus Coverage and Priority Ledger.
