---
corpus: AOT_JP_DEEP_READING
document: project_decisions
version: "2.1"
date: "2026-08-23"
---

# Attack on Titan Project Decisions and Checkpoint Policy

## Canonical reading unit

The default analytical unit is **one Japanese tankōbon volume per deep reading**.

This preserves:

- chapter-title architecture;
- local ambiguity;
- page-turn and volume-ending design;
- changes in what characters and readers know;
- volume-specific Japanese lexical clusters;
- visual/formal continuity;
- precise cumulative deltas.

Two- or three-volume passes may be used for later arc synthesis, but not as a replacement for the canonical per-volume artifact.

## Canonical source

The original Japanese manga page governs.

Anime, translations, guidebooks, interviews, and external criticism are separate evidence layers and must be labeled when activated.

## Spoiler policy

Strict publication-order first pass.

Later revelations may generate retrospective corrections, but may not be silently imported into earlier artifacts.

## Checkpoints

### 25% checkpoint

Completed through Volumes 1–9.

Canonical artifact:

```text
AOT_CHECKPOINT_25P_V01-V09_SYNTHESIS.md
```

### 50% checkpoint

Planned around Volumes 18–19, according to the user's chosen stopping point and the natural shape of the ongoing Shiganshina movement.

### 75% checkpoint

To be selected near the three-quarter point of the 34-volume sequence, preferably at a natural structural boundary.

### Full-series synthesis

After Volume 34.

The final phase should include:

- multi-document thematic synthesis;
- character and relationship studies;
- political/institutional analysis;
- human/Titan ontology;
- freedom/personhood/inheritance;
- Japanese-language and visual-form analysis;
- volume-by-volume evidence ledger;
- primary-source locator index;
- translation audit if an English comparison corpus is supplied;
- final manifest and checksum package;
- full-series character reconstruction models where evidence warrants them;
- character-model validation and cross-model consistency audit.

## Character-modeling extension

Character reconstruction is a **downstream derived layer** governed by:

- `AOT_CHARACTER_MODELING_AND_SIMULATION_ARCHITECTURE_V1.md`;
- `AOT_CHARACTER_RECONSTRUCTION_AND_VALIDATION_METHOD_V1.md`;
- `AOT_CHARACTER_MODEL_SCHEMA_V1.md`.

From Volume 19 onward, each deep reading should update the simulation-relevant ledgers when evidence exists:

- `AOT_CHARACTER_BEHAVIOR_AND_DECISION_LEDGER.md`;
- `AOT_RELATIONSHIP_CONDITIONED_BEHAVIOR_LEDGER.md`;
- `AOT_EVERYDAY_LIFE_PREFERENCES_AND_LOW_STAKES_BEHAVIOR_LEDGER.md`;
- `AOT_JAPANESE_VOICE_AND_VOCABULARY_LEDGER.md`;
- `AOT_CHARACTER_MODEL_READINESS_AND_COVERAGE_LEDGER.md`.

The project should exploit its current prospective boundary. After Volume 19 and the approximately 50% checkpoint, but **before Volume 20 is analyzed**, freeze:

```text
AOT_CHARACTER_MODEL_PROSPECTIVE_PREDICTION_REGISTER_V01-V19.md
```

Later volumes may adjudicate but may not rewrite those predictions. This provides genuine prospective evidence of predictive warrant.

Boundary-specific provisional models may be useful before V34, but they must remain `active_provisional`, identify their exact source boundary, and must not be represented as mature full-series character authorities.

After V34, full-series character reconstruction and validation may proceed. Any anime voice/performance reconstruction remains a separate adaptation layer and may not be inferred from manga punctuation or typography.

## Canonical artifact policy

Every future volume response should be accompanied by:

```text
AOT_VXX_DEEP_READING.md
```

The saved file—not chat chronology—is the durable research record.

## Raw-source rotation

Once a volume has a complete canonical artifact and usable locators, its CBZ may move to cold storage. It should be selectively restored when a final claim requires exact quotation, visual verification, or disputed interpretation.
