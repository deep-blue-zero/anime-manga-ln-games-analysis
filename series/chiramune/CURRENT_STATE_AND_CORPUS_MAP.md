---
series: CHIRAMUNE
artifact_type: corpus_map
scope: JP_LIGHT_NOVEL_OPEN_ENDED_ANALYSIS
source_boundary: "Japanese-language light-novel EPUB corpus through main Volume 09 plus acquired V03/V05/V08 supplements, Volume 06.5, Days of Endless Summer, and Volume 09.5; source audit dated 2026-08-29 and official publisher catalog rechecked 2026-09-07; main analysis frozen through Volume 03 with its bundled pre-main bonus classified separately"
generation: V0.3
status: canonical
release_state: mutable_active
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
---

# Chitose Is in the Ramune Bottle — current state and corpus map

This is the canonical first read for the Git-side *Chitose Is in the Ramune Bottle* (`Chiramune`; Japanese: `千歳くんはラムネ瓶のなか`) analytical corpus.

## Authority split

- **GitHub `main` is the analytical authority.** Interpretive claims, methods, deep readings, longitudinal ledgers, character work, syntheses, and analytical audits belong under `series/chiramune/`.
- **Google Drive is the primary-source authority.** The Japanese EPUBs and their integrity/audit manifest remain in the governed primary-source Drive plane and are not copied into Git.
- **Local/Codex workspaces are working environments**, not authority unless an artifact is promoted through the governed Drive-evidence or Git-analysis route.

Primary-source Drive root: `1tNJvglC-ri_AEGTkJupZ78WddyiCqQMy`  
Chiramune source folder: `1bI8p0tRpD7_u6Xi3vubqydl-jR7gJFxx`  
Source audit manifest: `1Oq8MhiuNApwg-qv9PxEfJG9YTzLuZy52`  
Audited manifest SHA-256: `e4d302d662997ae67be9368d45dd2dc7fefd5918f5c8540cbe82a897c00a8231`

See `01 Source Lock and Inventory/CHIRAMUNE_SOURCE_LOCK_AND_INVENTORY.md` before any source-facing analysis.

## Current analytical state

**The full-series architecture and prospective V01–V03 analytical corpus are established on the continuing Chiramune branch. The latest numbered prospective freeze is V03; the separate V03 illustration/short-story booklet is the next safe source.**

The corpus contains distinct V01, V02, and V03 deep readings and freezes, five rolling longitudinal responsibilities, and active-provisional Saku Chitose, Yuzuki Nanase, and Asuka Nishino monographs. The Volume 03 EPUB's own pre-main birthday story is integrated under the explicit class `BONUS_FICTION`; no separately packaged supplemental witness or V04+ narrative has been opened. Earlier prospective artifacts remain separate epistemic states rather than being rewritten with V03 knowledge.

`00 Frameworks and Methods/CHIRAMUNE_FULL_SERIES_ARCHITECTURE.md` governs the open-ended corpus, atomic closeout, horizon tracking, revision route, synthesis layers, and adaptation boundary.

## Horizon vector

| Horizon | Current state | Evidence / limit |
|---|---|---|
| latest known publication (`H_pub`) | Volume 09.5 | official Shogakukan series catalog rechecked 2026-09-07: 14 listed releases, ending with Volume 09.5; retailer-exclusive completeness is not claimed |
| latest source acquired (`H_acq`) | main V09; supplemental V09.5 | 14 locked EPUB objects; all live local hashes reverified against the source lock before the V01–V02 baseline |
| latest main volume analyzed (`H_main`) | V03 | V01–V03 deep readings and prospective freezes present |
| supplemental analysis (`H_supp`) | V03 in-EPUB birthday bonus | `王様とバースデー` integrated only as `BONUS_FICTION`; no separately packaged supplement opened |
| next safe reading (`H_next`) | separate V03 illustration/SS booklet | V03 main is frozen; classify the booklet's contents and dependency before integration |

Unresolved acquisition scope is limited to unclaimed retailer-exclusive or ephemeral bonuses and future publications. There is no missing numbered main volume through V09 in the locked inventory. Regular-edition V08 is not separately held, but its complete narrative is present in the special-edition witness.

```yaml
sequential_execution:
  mode: continuous_sequential
  unit_type: volume_then_safe_supplement
  authorized_start: V03
  terminal_boundary: ALL_ADMITTED_SOURCES_IN_LIVE_INVENTORY_AT_RUN_START
  committed_high_water_mark: V03_MAIN
  next_candidate_operation: V03_BOOKLET_CLASSIFICATION_AND_READING
  confirmation_between_units: false
  run_state: active
```

## Source boundary

The current locked source set contains 14 Japanese EPUB objects representing:

- main narrative Volumes 01–09;
- the separate Volume 03 illustration/short-story booklet;
- the Volume 05 special edition/SS material in addition to the regular Volume 05 witness;
- Volume 06.5;
- *Days of Endless Summer*;
- Volume 08 as the special edition containing the complete Volume 08 novel plus the rough-illustration supplement;
- Volume 09.5.

The audit found no missing main numbered volume through Volume 09 and no exact duplicate file groups. The current lock does **not** claim exhaustive possession of every retailer-exclusive purchase bonus ever distributed. Such bonuses remain outside the source boundary until separately acquired and audited.

## Governing method

Read in this order for new Chiramune analytical work:

1. `CURRENT_STATE_AND_CORPUS_MAP.md`
2. `00 Frameworks and Methods/CHIRAMUNE_ANALYTICAL_METHOD.md`
3. `00 Frameworks and Methods/CHIRAMUNE_FULL_SERIES_ARCHITECTURE.md`
4. `01 Source Lock and Inventory/CHIRAMUNE_SOURCE_LOCK_AND_INVENTORY.md`
5. the latest prospective freeze and `03 Longitudinal Ledgers/CHIRAMUNE_REVISION_LEDGER.md`;
6. only the rolling ledger, character model, or earlier source-bound reading needed for the task.

The Japanese prose is the current semantic anchor. Later anime material, official interviews, reception research, translations, or other adaptations may become separate witnesses, but they do not silently alter this source boundary.

## Corpus architecture

| Layer | Analytical responsibility | Current state |
|---|---|---|
| `00 Frameworks and Methods` | Governing source-reading, inference, prospective-freeze, multi-document full-series accumulation, comparison, and synthesis rules | populated; analytical method V0.2 and full-series architecture V0.3 |
| `01 Source Lock and Inventory` | Exact acquired-source boundary, integrity state, and Drive routing | populated; canonical V0.1 |
| `02 Sequential Readings` | Volume-by-volume prospective deep readings and immutable freezes | V01–V03 frozen; V03 booklet next |
| `03 Longitudinal Ledgers` | Claim revision plus recurring cross-volume state/relationship/theme tracking | revision, self-authorship, agency, social-status, and relationship ledgers active through V03 |
| `04 Character Analysis` | Character syntheses created only after evidence warrants them | Saku, Yuzuki, and Asuka active-provisional monographs through V03 |
| `05 Specialist Synthesis` | Dense recurring thematic/relationship/form and future adaptation/performance questions | not instantiated; responsibilities defined by architecture |
| `06 Full-Series Synthesis` | Router for the multi-document portfolio and rolling analyzed-to-date integration, conceptually separate from terminal full-series synthesis | router present; no synthesis promoted at V02 |
| `07 Evidence and Indexes` | Git-side cross-volume claim/evidence routing if later needed | not instantiated; source lock plus reading-local locators are sufficient through V03 |
| `08 Audits and Manifests` | Bootstrap inventory, package reconciliation, and later analytical/source-integrity records | bootstrap manifest plus V01–V02 reconciliation audit |
| `90 Legacy and Superseded` | Materially distinct superseded analysis | not instantiated; no legacy analytical corpus is being imported |

The absence of a directory is intentional. Do not create empty categories merely to make Chiramune resemble another project.

## V03 frozen state for the booklet and V04

The exact V03 claim boundary and V04 questions live in:

- `02 Sequential Readings/CHIRAMUNE_V03_DEEP_READING.md`;
- `02 Sequential Readings/CHIRAMUNE_V03_PROSPECTIVE_FREEZE.md`;
- `03 Longitudinal Ledgers/CHIRAMUNE_REVISION_LEDGER.md`;
- the four thematic/relationship ledgers;
- the Saku and Yuzuki monographs.

The required high-level guardrails are:

- preserve Saku/Asuka mutual love without silently converting it into an exclusive couple;
- preserve Yuzuki's named, costly support without inventing reciprocal naming from Saku;
- distinguish Saku's improved respect for another person's final choice from his continuing procedural violations;
- treat Asuka's Tokyo decision as an informed choice between rival goods, not proof of vocational success or a city hierarchy;
- preserve Kenta's ordinary membership and the reopened but unresolved baseball trajectory;
- treat the Ramune image as enclosure, lens, divergent co-authored perception, and many-moons relation without freezing it to a terminal meaning;
- keep the separate V03 booklet outside the V03 main freeze until it is independently classified and read.

Comparisons to *Oregairu*, *AoButa*, *Classroom of the Elite*, PACTRIH, or other corpus frameworks remain downstream operations. Reconstruct Chiramune on its own evidence first.

## Continuous work order after the V03 main freeze

1. Publish and independently verify the complete V03 main transaction before opening the separate booklet.
2. Verify the V03 booklet object, classify its internal visual/fiction components and diegetic dependencies, and integrate it through a separate supplemental checkpoint.
3. Begin main V04 only after the booklet disposition is frozen and published.
4. Continue main numbered volumes in order, following the V05, V06.5, V08, *Days of Endless Summer*, and V09.5 handling rules in the architecture and source lock.
5. Keep committing and pushing coherent validated checkpoints to `series/chiramune` until every currently admitted source reaches its safe chronological boundary.
6. Do not merge to `main`; integration remains owner-controlled and separately governed.

## Standing abstentions

- No character personality claim is current merely because it appeared in a synopsis, marketing copy, fandom discussion, or an earlier ChatGPT conversation.
- No kanji name reading is inferred by generic CJK transliteration when an official/furigana reading is available or required.
- No retailer-exclusive SS is treated as present unless it is actually acquired and audited.
- No PACTRIH score or other comparative ethical placement is assigned before source-grounded character evidence is sufficient.
- No later source is allowed to rewrite the record of what an earlier prospective reading reasonably inferred at the time.
