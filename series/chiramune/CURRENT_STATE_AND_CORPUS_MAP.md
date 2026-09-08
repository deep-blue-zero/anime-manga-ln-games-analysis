---
series: CHIRAMUNE
artifact_type: corpus_map
scope: JP_LIGHT_NOVEL_OPEN_ENDED_ANALYSIS
source_boundary: "Japanese-language light-novel EPUB corpus through main Volume 09 plus acquired V03/V05/V08 supplements, Volume 06.5, Days of Endless Summer, and Volume 09.5; source audit dated 2026-08-29 and official publisher catalog rechecked 2026-09-07; regular main analysis frozen through Volume 05; V03 bundled bonus, separate V03 booklet, and component-routed V05 special-edition booklet integrated"
generation: V0.7
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

**The full-series architecture and prospective V01–V05-regular-main analytical corpus are established on the continuing Chiramune branch. The latest numbered prospective freeze is regular main V05; the V03 illustration/short-story booklet and the V05 Special Edition's component-routed 18-story booklet are integrated through separate frozen supplemental checkpoints. Volume 06 main is the next safe source.**

The corpus contains distinct V01–V05 regular-main deep readings and freezes, separate V03 and V05 supplemental readings/checkpoints, five rolling longitudinal responsibilities, six active-provisional character monographs, the first promoted specialist synthesis for Fukui locality/departure/ordinary youth, and a mutable current published-corpus synthesis. The Volume 03 EPUB's own pre-main birthday story is `BONUS_FICTION`; the separate V03 booklet and individually routed V05 booklet stories are `SUPPLEMENTAL_MAINLINE`. The Special Edition's regular-main duplicate is verified but not double-counted. Its revised V03 cap story is two edition witnesses to one event, with variants preserved. All V06+ sources remain unopened. Earlier prospective artifacts remain separate epistemic states rather than being rewritten with later knowledge.

`00 Frameworks and Methods/CHIRAMUNE_FULL_SERIES_ARCHITECTURE.md` governs the open-ended corpus, atomic closeout, horizon tracking, revision route, synthesis layers, and adaptation boundary.

## Horizon vector

| Horizon | Current state | Evidence / limit |
|---|---|---|
| latest known publication (`H_pub`) | Volume 09.5 | official Shogakukan series catalog rechecked 2026-09-07: 14 listed releases, ending with Volume 09.5; retailer-exclusive completeness is not claimed |
| latest source acquired (`H_acq`) | main V09; supplemental V09.5 | 14 locked EPUB objects; all live local hashes reverified against the source lock before the V01–V02 baseline |
| latest main volume analyzed (`H_main`) | V05 regular main | V01–V05 regular-main deep readings and prospective freezes present |
| supplemental analysis (`H_supp`) | V03 in-EPUB birthday bonus, separate V03 illustration/SS booklet, and V05 Special Edition 18-story booklet | V03/V05 supplemental checkpoints preserve individual class, provenance, chronology, and edition-witness routing |
| next safe reading (`H_next`) | Volume 06 main | V05 main and Special Edition are independently frozen; verify the exact locked V06 witness and enter from the V05-main prospective freeze plus current supplemental revision state |

Unresolved acquisition scope is limited to unclaimed retailer-exclusive or ephemeral bonuses and future publications. There is no missing numbered main volume through V09 in the locked inventory. Regular-edition V08 is not separately held, but its complete narrative is present in the special-edition witness.

```yaml
sequential_execution:
  mode: continuous_sequential
  unit_type: volume_then_safe_supplement
  authorized_start: V03
  terminal_boundary: ALL_ADMITTED_SOURCES_IN_LIVE_INVENTORY_AT_RUN_START
  committed_high_water_mark: V05_SPECIAL_EDITION_SUPPLEMENTAL_CHECKPOINT
  next_candidate_operation: V06_MAIN_VERIFICATION_AND_PROSPECTIVE_READING
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
| `00 Frameworks and Methods` | Governing source-reading, inference, prospective-freeze, multi-document full-series accumulation, comparison, and synthesis rules | populated; analytical method V0.2 and full-series architecture V0.7, including compilation/edition-witness routing |
| `01 Source Lock and Inventory` | Exact acquired-source boundary, integrity state, and Drive routing | populated; canonical V0.5 |
| `02 Sequential Readings` | Volume-by-volume prospective deep readings, immutable freezes, and warranted supplemental checkpoints | V01–V05 regular main frozen; V03 and V05 supplemental checkpoints integrated; V06 main next |
| `03 Longitudinal Ledgers` | Claim revision plus recurring cross-volume state/relationship/theme tracking | five ledgers active through V05 main and integrated V03/V05 supplements; earlier frozen boundary states preserved |
| `04 Character Analysis` | Character syntheses created only after evidence warrants them | six active-provisional monographs updated through the V05 booklet |
| `05 Specialist Synthesis` | Dense recurring thematic/relationship/form and future adaptation/performance questions | Fukui locality/departure/ordinary youth promoted at V05 main and updated with V05 booklet evidence; other domains deferred |
| `06 Full-Series Synthesis` | Router for the multi-document portfolio and rolling analyzed-to-date integration, conceptually separate from terminal full-series synthesis | router plus mutable current published-corpus synthesis through V05 main and Special Edition; terminal synthesis ineligible |
| `07 Evidence and Indexes` | Git-side cross-volume claim/evidence routing if later needed | not instantiated; source lock plus reading-local locators are sufficient through V05 main |
| `08 Audits and Manifests` | Bootstrap inventory, package reconciliation, and later analytical/source-integrity records | bootstrap manifest plus V01–V02 reconciliation audit |
| `90 Legacy and Superseded` | Materially distinct superseded analysis | not instantiated; no legacy analytical corpus is being imported |

The absence of a directory is intentional. Do not create empty categories merely to make Chiramune resemble another project.

## Post-V05-Special-Edition frozen state for Volume 06

The exact regular V05 claim boundary and integrated special-edition revisions live in:

- `02 Sequential Readings/CHIRAMUNE_V05_DEEP_READING.md`;
- `02 Sequential Readings/CHIRAMUNE_V05_PROSPECTIVE_FREEZE.md`;
- `02 Sequential Readings/CHIRAMUNE_V05_SPECIAL_EDITION_SUPPLEMENTAL_READING.md`;
- `03 Longitudinal Ledgers/CHIRAMUNE_REVISION_LEDGER.md`;
- the four thematic/relationship ledgers;
- the Saku, Yuzuki, Asuka, Haru, Yuko, and Yua monographs;
- `05 Specialist Synthesis/CHIRAMUNE_FUKUI_LOCALITY_DEPARTURE_AND_ORDINARY_YOUTH_SYNTHESIS.md`;
- `06 Full-Series Synthesis/CHIRAMUNE_CURRENT_PUBLISHED_CORPUS_SYNTHESIS.md`.

The required high-level guardrails are:

- Saku explicitly refuses Yuko and names one other girl, but regular V05 does not identify her and establishes no couple;
- preserve Yuko's request, grief, ordinary importance, and independent friendships without adopting personal-insufficiency language;
- preserve Yua's chosen priority and non-extractive care without identifying her as the unnamed girl;
- preserve Haru's future consent protocol and Yuzuki's bounded present requests without inventing reciprocal love;
- treat Saku's self-injury as worsened moralized punishment, not accountability or repaired safety practice;
- preserve Fujishi institutional closure while keeping chosen future baseball open;
- classify group fracture as enacted but not proven terminal;
- route locality/departure/ordinary youth through the promoted specialist synthesis;
- treat eight Ramune bottles and the finite-object system as collective scale and reconstructed retrieval, not terminal motif resolution;
- preserve the V05 Special Edition as a component graph: its main duplicate is counted once, each of 18 stories retains its own route, and the revised V03 cap story remains two witnesses to one event;
- carry the booklet's historicizing evidence into the current model without back-projecting it into V01–V05 prospective freezes;
- enter Volume 06 with Saku's unnamed girl still unidentified and no couple established.

Comparisons to *Oregairu*, *AoButa*, *Classroom of the Elite*, PACTRIH, or other corpus frameworks remain downstream operations. Reconstruct Chiramune on its own evidence first.

## Continuous work order after the V05-Special-Edition checkpoint

1. Preserve the published V01–V05 regular-main freezes and independently classified V03/V05 supplemental checkpoints as distinct source-boundary records.
2. Open Volume 06 main only after the complete V05-special transaction is committed, pushed, audited, and independently validated.
3. Enter Volume 06 from `CHIRAMUNE_V05_PROSPECTIVE_FREEZE.md` plus the current rolling revisions produced by the V05 booklet; do not rewrite the prospective freeze itself.
4. Keep committing and pushing coherent validated checkpoints to `series/chiramune` until every currently admitted source reaches its safe chronological boundary.
5. Do not merge to `main`; integration remains owner-controlled and separately governed.

## Standing abstentions

- No character personality claim is current merely because it appeared in a synopsis, marketing copy, fandom discussion, or an earlier ChatGPT conversation.
- No kanji name reading is inferred by generic CJK transliteration when an official/furigana reading is available or required.
- No retailer-exclusive SS is treated as present unless it is actually acquired and audited.
- No PACTRIH score or other comparative ethical placement is assigned before source-grounded character evidence is sufficient.
- No later source is allowed to rewrite the record of what an earlier prospective reading reasonably inferred at the time.
