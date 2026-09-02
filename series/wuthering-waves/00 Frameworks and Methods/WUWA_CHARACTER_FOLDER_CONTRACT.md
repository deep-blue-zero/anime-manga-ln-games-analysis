---
series: WUWA
artifact_type: character_folder_contract
scope: CHARACTER_ANALYSIS
source_boundary: "Applies to WUWA Git analytical character packages; evidence remains in the canonical Drive plane"
generation: V0.1
status: canonical
release_state: mutable_active
supersedes: null
superseded_by: null
do_not_use_as_current_authority: false
---

# WUWA character-folder contract

## Governing rule

The contract standardizes **analytical responsibilities**, not an identical mandatory file count. A minor character may need one monograph. A major reconstruction project may warrant the complete package below.

No empty monograph, model, or ledger may be created merely to instantiate a filename.

## Canonical responsibilities

### `WUWA_<CHARACTER>_CURRENT_STATE.md`

Recommended when a character has more than one substantive artifact or a live evidence/analysis mismatch. It must identify:

- current analytical authority and generation;
- source generation and Drive evidence route;
- completed artifacts;
- open modalities and unresolved evidence;
- default/current state only when justified;
- recommended first-read order;
- next authorized operation.

### `WUWA_<CHARACTER>_CHARACTER_MONOGRAPH.md`

The canonical interpretive synthesis. It should integrate:

- identity and source boundary;
- developmental/state architecture;
- values, goals, fears, vulnerabilities, contradictions;
- ordinary personality;
- relationships;
- speech and interaction;
- narrative/thematic function;
- rival readings;
- bounded predictions and abstentions.

The monograph should explain how facts cohere. It is not a list of traits.

### `WUWA_<CHARACTER>_RELATIONSHIP_AND_STATE_LEDGER.md`

Create when state or relationship changes are too complex for reliable monograph-only retrieval. It distinguishes:

- developmental state;
- persona/form;
- operational context;
- relationship state;
- evidence density;
- transition evidence;
- unresolved continuity.

### `WUWA_<CHARACTER>_ORDINARY_LIFE_AND_PREFERENCES_PROFILE.md`

Create when mundane evidence is dense enough to materially improve reconstruction. Potential domains:

- food and drink;
- leisure, play, hobbies, art, music, travel, celebration;
- crowds, solitude, rest, sleep, sensory attention;
- gifting and preferred shared activities;
- practical skills and competence bids;
- disliked tasks, boredom, frustration, embarrassment;
- money/shopping/haggling where supported;
- clothing/material/aesthetic taste where supported;
- low-stakes social behavior.

Every entry should separate:

1. source fact;
2. analytical implication;
3. extrapolation limit.

### `WUWA_<CHARACTER>_SPEECH_VOICE_AND_PERFORMANCE_PROFILE.md`

Create when speech or voice is analytically material. It has three authority tiers:

1. **Textual speech findings** — diction, register, disclosure style, terms of address, rhetorical moves, relationship/state conditioning, localization differences.
2. **Machine voice findings** — comprehensive measurements, normalized distributions, clusters, contrasts, outliers, and cohort selection.
3. **Human performance interpretation** — direct listening observations that preserve, revise, or reject machine-generated hypotheses.

The machine tier is a required baseline whenever a sufficiently complete usable voice corpus exists. Human review may remain selectively incomplete, but strong acting claims remain open until heard.

### `WUWA_<CHARACTER>_CLAIM_AND_COUNTEREVIDENCE_LEDGER.json`

Recommended for high-confidence reconstruction. Every material claim should carry stable ID, wording, epistemic status, state/situation/relationship scope, supporting evidence, counterevidence, alternative reading, and extrapolation limit.

### `WUWA_<CHARACTER>_CLAIM_REVISION_LEDGER.md`

Create when a major reread, source update, or multimodal pass materially changes claims. Use the controlled transition vocabulary.

### `WUWA_<CHARACTER>_CHARACTER_MODEL_PACKAGE.json`

A compact machine-consumption view derived from the analysis. It is subordinate to primary evidence, monograph, claim ledger, and specialist analysis. It should normally include:

- identity and state slices;
- core thesis;
- values, goals, fears, vulnerabilities;
- ordinary personality and preferences;
- behavior rules with exceptions;
- relationship models;
- speech/performance model;
- bounded unfamiliar-situation predictions;
- mandatory abstentions;
- evidence artifact references.

Generated scenarios never feed back into canon.

### `WUWA_<CHARACTER>_MODEL_FIDELITY_CHECK.md`

An adversarial smoke test, not a statistical benchmark. It should test:

- state selection;
- ordinary low-stakes behavior;
- relationship sensitivity;
- speech/register fit;
- contradiction retention;
- romance and archetype leakage;
- dub leakage;
- abstention where source evidence is insufficient.

## Minimal and expanded packages

A legitimate minimal package may be:

```text
<Character>/
└── WUWA_<CHARACTER>_CHARACTER_MONOGRAPH.md
```

A reconstruction-oriented package may contain every role above. Split only when the independent document will be maintained as a canonical topical home.

## Evidence boundary

Do not copy into the character folder:

- large scene/evidence JSONL;
- raw or normalized dialogue corpora;
- full text maps or flow states;
- audio files or FLAC shards;
- runtime package trees;
- contact sheets or video clips;
- machine line-level measurement tables too large for public analytical Git.

Store those in Drive. The Git profile synthesizes them and preserves stable pointers.

## Required same-change updates

When a character package is created or materially revised, update as applicable:

- character current state;
- `07 Evidence and Indexes/WUWA_CHARACTER_INDEX.md`;
- `WUWA_CLAIM_EVIDENCE_INDEX.md`;
- title-wide state/relationship/open-question ledgers;
- `CURRENT_STATE_AND_CORPUS_MAP.md`;
- revision ledger;
- corpus manifest/audit.
