---
series: BLUE_ARCHIVE
artifact_type: corpus_map
scope: Current analytical authority, accepted state, and next-operation routing
generation: V1
status: canonical
source_boundary: Active audited Japanese corpus pinned to electricgoat/ba-data@jp a038020f1f5ac02dcfe76962426d38f86414cdd8; V1 source lock cbe3fd623c2aab9e781ba0ce0483bc77c68bff86 retained as historical witness
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
created: 2026-08-15
updated: 2026-10-03
canonical_home: series/blue-archive/CURRENT_STATE_AND_CORPUS_MAP.md
---

# BLUE ARCHIVE — CURRENT STATE AND CORPUS MAP

## 1. Read this first

This is the **single canonical current entrypoint** for the Japanese-primary Blue Archive analytical project in `deep-blue-zero/anime-manga-ln-games-analysis`, branch **`series/blue-archive`**, root **`series/blue-archive/`**. It routes literary analysis from complete source units through longitudinal state and checkpoints toward later specialist synthesis. Repository authority and publication remain governed by [AGENTS.md](../../AGENTS.md) and the [live integration checklist](../../governance/policies/CHANGE_INTEGRATION_CHECKLIST.md).

**Phase 1 is complete at 480 / 480 canonical main units and 26 chapter checkpoints. Architecture Phase 2 — Arc contextualization is IN_PROGRESS through cycle 006: 213 supplemental objects admitted with limits. All 12 arc-completion rows remain incomplete. No standalone character model exists.**

Start with this file. For active work, descend into the [Phase 2 acceptance audit](08%20Audits%20and%20Manifests/BLUE_ARCHIVE_PHASE2_CONTEXTUALIZATION_AUDIT.md#14-current-accepted-progress--cycle006-2026-10-02) and the exact selected source/reading routes; the [historical map](90%20Legacy%20and%20Superseded/BLUE_ARCHIVE_CURRENT_STATE_HISTORY_THROUGH_CYCLE_005.md) is unnecessary for routine startup. The audit owns acceptance criteria; this summary does not independently admit evidence or change readiness.

## 2. Current source boundary

The [2026-09-28 source reconciliation](01%20Source%20Lock%20and%20Inventory/BLUE_ARCHIVE_SOURCE_RECONCILIATION_20260928.md) fixes:

- Japanese witness: `electricgoat/ba-data@jp a038020f1f5ac02dcfe76962426d38f86414cdd8`.
- Audited generation: `BA_REFRESH_20260928T032248159554Z`; game-data version `v1.73.459696-r96_3cpn8ebtdjiqi6y9qtn1`.
- Source location: `blue-archive-corpus-pipeline/corpus/GENERATIONS/BA_REFRESH_20260928T032248159554Z/` in the separate extraction workspace. `corpus/CURRENT.json` and `ACTIVE_CORPUS.md` provide technical routing; a later selection cannot silently change this analytical lock.
- Latest forward released unit **within this snapshot**: `BA:main:series2:003:001:014`, governed by the [S2 V003 C001 checkpoint](02%20Sequential%20Readings/MAIN/SERIES2_VOLUME_003/BLUE_ARCHIVE_MAIN_S2_V003_C001_CHECKPOINT.md). Final completed backfill: `BA:main:001:003:043`, governed by the [V001 C003 checkpoint](02%20Sequential%20Readings/MAIN/VOLUME_001_%E5%AF%BE%E7%AD%96%E5%A7%94%E5%93%A1%E4%BC%9A%E7%B7%A8/BLUE_ARCHIVE_MAIN_V001_C003_CHECKPOINT.md). Neither is an unread holdout or a universal story-time endpoint.
- Historical V1 witness: `cbe3fd623c2aab9e781ba0ce0483bc77c68bff86`, retained in the [V1 source lock](01%20Source%20Lock%20and%20Inventory/BLUE_ARCHIVE_SOURCE_LOCK_V1.md) for the readings that used it. Its 310-unit denominator does not govern present completion. Independent parser/reference witness: `HePudding/ba-storybook@main 6c4091603ca76d7d8c3cdb9104933f52cd8cab8e`.

The promoted source inventory has **4,864 objects in nine classes**. Availability is not admission. Recover new source-facing claims through the [source-class crosswalk](06%20Evidence%20and%20Indexes/BLUE_ARCHIVE_SOURCE_CLASS_CROSSWALK.md): stable `story_id` → complete object at its generation-relative `canonical_path` → scene/utterance/choice/message → structured record → raw path/hash and pinned commit. The path already begins with `02_CANONICAL_STORIES/`. Source transcripts and generated retrieval packages remain outside analytical Git. Pinned Japanese fields are textual evidence, not an official literary edition.

## 3. Accepted progress and unfinished work

The [cycle 006 checkpoint](02%20Sequential%20Readings/BLUE_ARCHIVE_PHASE2_CONTEXTUALIZATION_CYCLE_006_CHECKPOINT.md) owns the latest accepted transaction; earlier cycles retain their exact scopes and limits.

| Responsibility | Current state | Detailed owner |
|---|---|---|
| Main-story pass | **480 / 480**, 26 checkpoints, no unopened unit in the audited snapshot | [Main crosswalk](06%20Evidence%20and%20Indexes/BLUE_ARCHIVE_MAIN_STORY_TO_ANALYSIS_CROSSWALK.csv) and its readings/checkpoints |
| Supplemental acceptance | **213**: 65 group / 59 event / 37 bond / 37 MomoTalk / 15 written character-data | [Supplemental object crosswalk](06%20Evidence%20and%20Indexes/BLUE_ARCHIVE_SUPPLEMENTAL_SOURCE_TO_ANALYSIS_CROSSWALK.csv), exact IDs, hashes, claims and admission routes |
| Group duty | All **65 / 65** complete objects accepted; P2-R01 **PASS_WITH_LIMITS** for all 12 group-relevance questions | [Group/arc relevance audit](08%20Audits%20and%20Manifests/BLUE_ARCHIVE_PHASE2_GROUP_ARC_RELEVANCE_AUDIT.md) |
| Whole Phase 2 | All **12 arc rows incomplete**; P2-R02–R09 **IN_PROGRESS** | [Completion requirements and arc matrix](08%20Audits%20and%20Manifests/BLUE_ARCHIVE_PHASE2_CONTEXTUALIZATION_AUDIT.md#2-completion-requirements) |
| Remaining required intake | 951 event objects in 56 packages; 1,024 principal bond / 1,024 MomoTalk / 419 written-data objects | [Current acceptance table](08%20Audits%20and%20Manifests/BLUE_ARCHIVE_PHASE2_CONTEXTUALIZATION_AUDIT.md#14-current-accepted-progress--cycle006-2026-10-02) |
| Full tracked scope | 3,631 mandatory + 19 separate Kei identity objects + 32 mini leads = **3,682 tracked**; **3,418 mandatory / 3,469 tracked** still unaccepted | [Scope extension 001](08%20Audits%20and%20Manifests/BLUE_ARCHIVE_PHASE2_PRINCIPAL_SCOPE_EXTENSION_001.md), 125 retrieval families / 128 preserved raw keys |
| Longitudinal integration | Seven ledgers retain all 480-main deltas and accepted cycles 001–006 | Ledger routes in §5 |
| Later analytical layers | No standalone reconstruction model, monograph, adjudicated relationship/institutional synthesis, Sensei full synthesis, current-era synthesis, frozen release or prospective/adjudication register | [Architecture](00%20Frameworks%20and%20Methods/BLUE_ARCHIVE_SYNTHESIS_ARCHITECTURE_V1.md) and [bootstrap audit](08%20Audits%20and%20Manifests/BLUE_ARCHIVE_CHARACTER_RECONSTRUCTION_BOOTSTRAP_AUDIT.md#current-disposition--2026-10-02) |

Serika's complete available 31-object private/written packet remains accepted. Cycle 005 also accepts Reijo/Rei/Ayane available private/written pools, two separately interpreted Tsukuyo/Junko pairs, and complete EVENT807/814. Rei inquiry joins do not establish baseball-Rei appearances. Cycle 006 adds Serina’s complete 17-object private/written pool and all 16 independent EVENT80001 encounters. Accepted event packages are EVENT816, EVENT80000, EVENT807, EVENT814 and EVENT80001. Other delivered drafts remain unadmitted until review and shared reconciliation. Mini, special-operation, unclassified scenario and performed voice remain unadmitted.

These are scoped analytical acceptance states. Historical publication rows in cycle audits record their then-known checks; the repository checklist and exact GitHub commit status govern publication and integration.

## 4. Compact readiness routing

This section is a **manually maintained routing summary**, not another coverage authority or generated database. Detailed canonical truth is the [main coverage index](06%20Evidence%20and%20Indexes/BLUE_ARCHIVE_CHARACTER_ANALYTICAL_COVERAGE_INDEX.md#5-project-local-readiness-and-artifact-state) **plus** the [contextual companion](06%20Evidence%20and%20Indexes/BLUE_ARCHIVE_CONTEXTUAL_CHARACTER_COVERAGE_INDEX.md#4-project-local-readiness-and-artifact-state). Apply the companion's subject overrides first: its 262 rows override 98 of the 352 main-only rows and add 164 analytical subjects; 254 main-only rows inherit unchanged. Count each subject once.

| Readiness | Current count |
|---|---:|
| `PARTIAL_MODEL` | **23** |
| `UNMODELED` | **493** |
| `OPERATIONAL_CANDIDATE` | **0** |
| `BOUNDED_VALIDATED` | **0** |
| Total analytical subjects | **516** |

All 23 `PARTIAL_MODEL` subjects, retaining the owners' identity labels: **Sensei; Reisa; Momoi; Midori; Alice / `AL-1S` (provisional); Yuzu; Yuuka; Ayane; Shiroko; Nonomi; Serika; Hoshino; Aru; Mutsuki; Kayoko; Haruka; Hifumi; Ako; Hina; Black Suit (role actor); Kaiser director (role actor); Shiba Seki master (role actor); Kazusa.** All standalone model fields are `NONE`; partial readiness denotes distributed supported mechanisms, not completed models or whole-person simulation capability.

Latest readiness transitions: **Kazusa and Reisa, `UNMODELED` → distributed `PARTIAL_MODEL` in [cycle 001 §4](02%20Sequential%20Readings/BLUE_ARCHIVE_PHASE2_CONTEXTUALIZATION_CYCLE_001_CHECKPOINT.md#4-readiness-adjudication)**, limited to the accepted event-local domains. Cycles 002–006 add coverage and subjects without further readiness promotions. Source-local role/voice buckets are not certified distinct biographies.

Bounded **design leads**, not active operational models: Yuuka's named Pavane council/club decision contract and Serika's familiar service/reciprocity alternative. The [bootstrap pilot assessment](08%20Audits%20and%20Manifests/BLUE_ARCHIVE_CHARACTER_RECONSTRUCTION_BOOTSTRAP_AUDIT.md#24-pilot-reassessment), qualified by its [cycle 006 reassessment](08%20Audits%20and%20Manifests/BLUE_ARCHIVE_CHARACTER_RECONSTRUCTION_BOOTSTRAP_AUDIT.md#34-current-cycle006-readiness-reassessment--2026-10-02), owns those choices. Hoshino/Hina require substantial state reconciliation; Sensei requires separate choice-space treatment. The [reconstruction specification](00%20Frameworks%20and%20Methods/BLUE_ARCHIVE_CHARACTER_RECONSTRUCTION_SPEC_V1.md) governs construction and validation, not a competing live admission census.

Update this summary only with accepted changes to its owners; reconcile discrepancies there before changing the summary. Do not append detailed coverage rows or sequential history here.

## 5. Responsibility and evidence routes

| Need | Canonical home and responsibility |
|---|---|
| Interpretation and source-class limits | [Analytical method](00%20Frameworks%20and%20Methods/BLUE_ARCHIVE_ANALYTICAL_METHOD_V1.md) |
| Artifact ownership and production phases | [Synthesis architecture](00%20Frameworks%20and%20Methods/BLUE_ARCHIVE_SYNTHESIS_ARCHITECTURE_V1.md); its **Phase 2 — Arc contextualization** labels current production, while older method numbering is retained history |
| Model rules, domain/state and validation gates | [Reconstruction specification](00%20Frameworks%20and%20Methods/BLUE_ARCHIVE_CHARACTER_RECONSTRUCTION_SPEC_V1.md) |
| Detailed subject coverage / supplemental overrides | [Main coverage](06%20Evidence%20and%20Indexes/BLUE_ARCHIVE_CHARACTER_ANALYTICAL_COVERAGE_INDEX.md) + [contextual coverage](06%20Evidence%20and%20Indexes/BLUE_ARCHIVE_CONTEXTUAL_CHARACTER_COVERAGE_INDEX.md), combined as §4 explains |
| Admission, provenance and chronology | [Source-class crosswalk](06%20Evidence%20and%20Indexes/BLUE_ARCHIVE_SOURCE_CLASS_CROSSWALK.md) + [exact supplemental object crosswalk](06%20Evidence%20and%20Indexes/BLUE_ARCHIVE_SUPPLEMENTAL_SOURCE_TO_ANALYSIS_CROSSWALK.csv) |
| Event review selection | [Event priority index](06%20Evidence%20and%20Indexes/BLUE_ARCHIVE_EVENT_ANALYTICAL_PRIORITY_INDEX.md); intake cues schedule inquiry, while reviewed rows own priority and accepted state |
| Claim-specific missing evidence | [Source-gap impact register](01%20Source%20Lock%20and%20Inventory/BLUE_ARCHIVE_SOURCE_GAP_IMPACT_REGISTER.md) |
| Whole-phase and per-arc completion | [Phase 2 audit](08%20Audits%20and%20Manifests/BLUE_ARCHIVE_PHASE2_CONTEXTUALIZATION_AUDIT.md), [principal scope extension](08%20Audits%20and%20Manifests/BLUE_ARCHIVE_PHASE2_PRINCIPAL_SCOPE_EXTENSION_001.md), and [group relevance audit](08%20Audits%20and%20Manifests/BLUE_ARCHIVE_PHASE2_GROUP_ARC_RELEVANCE_AUDIT.md) |
| Display/text-actor seams | [Supplemental attribution review](08%20Audits%20and%20Manifests/BLUE_ARCHIVE_SUPPLEMENTAL_ATTRIBUTION_REVIEW_20261001.md); diagnostic excerpts do not admit their whole event |

The seven cumulative ledgers retain their separate analytical responsibilities and historical information boundaries:

| Responsibility | Ledger |
|---|---|
| Character state, goals and material transitions | [Character state](03%20Longitudinal%20Ledgers/BLUE_ARCHIVE_CHARACTER_STATE_LEDGER.md) |
| Directed relationships and ensembles | [Relationship state](03%20Longitudinal%20Ledgers/BLUE_ARCHIVE_RELATIONSHIP_STATE_LEDGER.md) |
| Institutional roles, power and legitimacy | [School / club / institution](03%20Longitudinal%20Ledgers/BLUE_ARCHIVE_SCHOOL_CLUB_INSTITUTION_LEDGER.md) |
| Structural actions, choice-space and adult responsibility | [Sensei role and ethics](03%20Longitudinal%20Ledgers/BLUE_ARCHIVE_SENSEI_ROLE_AND_ETHICS_LEDGER.md) |
| Written Japanese register, address and attribution limits | [Japanese voice and address](03%20Longitudinal%20Ledgers/BLUE_ARCHIVE_JAPANESE_VOICE_AND_ADDRESS_LEDGER.md) |
| Motifs, themes and callbacks with local chronology | [Motif / theme / callback](03%20Longitudinal%20Ledgers/BLUE_ARCHIVE_MOTIF_THEME_AND_CALLBACK_LEDGER.md) |
| Claim status, revisions, counterevidence and reasons | [Claim revision](03%20Longitudinal%20Ledgers/BLUE_ARCHIVE_CLAIM_REVISION_LEDGER.md) |

For a substantive question: this map → coverage or relevant checkpoint → applicable ledger → source-facing reading → complete pinned Japanese source. Choose chapter authority for the represented state; later backfill does not replace earlier information boundaries. Source-side character/relationship/institution bundles and LLM chunks aid retrieval but do not replace complete scenes or analytical adjudication.

## 6. Active gaps and next valid operation

Continue **Phase 2 contextualization**: select the next unaccepted complete event or private/written family packet under the [Phase 2 audit](08%20Audits%20and%20Manifests/BLUE_ARCHIVE_PHASE2_CONTEXTUALIZATION_AUDIT.md) and [object crosswalk](06%20Evidence%20and%20Indexes/BLUE_ARCHIVE_SUPPLEMENTAL_SOURCE_TO_ANALYSIS_CROSSWALK.csv), review the complete argument and consequential source evidence, then accept only its supported scope and reconcile affected ledgers, coverage and controls. Preserve full-source event rotation alongside inquiry-led selection. Existing drafts are review candidates, not accepted progress. The [2026-10-03 review-draft snapshot](08%20Audits%20and%20Manifests/BLUE_ARCHIVE_PHASE2_REVIEW_DRAFT_PUBLICATION_20261003.md) routes completed unadmitted arguments and their pending checks; publication of those drafts does not change this accepted-state summary. The [PR135 terminal-LF transformation record](08%20Audits%20and%20Manifests/BLUE_ARCHIVE_PR135_TERMINAL_LF_TRANSFORMATION_V1.json) binds the seventy normalized derivatives and their exact inverse; the dated publication manifest retains its original historical tuples. The event index currently routes EVENT801 as the next independent rotation packet and EVENT806 as a Yuuka/C&C inquiry; neither is admitted. This queue order is distinct from a literary priority judgment on unread material.

Major unresolved responsibilities are the remaining event/private/written and per-arc duties in §3; [G01–G06](01%20Source%20Lock%20and%20Inventory/BLUE_ARCHIVE_SOURCE_GAP_IMPACT_REGISTER.md#1-current-material-gaps-and-claim-effects) distinguish ordinary/private breadth, Yuuka transfer, Serika's remaining event range, Hina accountability, Arius/PS68 aftermath, and cross-school contexts. G11 retains Hoshino's Yume-record and office-state limits; G07–G10 and G12 retain chronology, naming, attribution, performance and identity constraints. Kaguya's private route remains unresolved; the [scope extension](08%20Audits%20and%20Manifests/BLUE_ARCHIVE_PHASE2_PRINCIPAL_SCOPE_EXTENSION_001.md#3-exact-identity-and-overlap-decisions) owns that inquiry. Unprinted legal, medical or technical outcomes cannot be closed by unrelated ordinary scenes.

Do not extend main-story dialogue until release status, source provenance and added IDs are reconciled. Broader Phase 3 packages and any separately assigned reconstruction pilot must pass their distinct evidence and state/domain gates. A prospective test requires a committed freeze before genuinely unexposed diagnostic material; the completed main run supports exposed retrospective checks, not retroactively prospective validation.

## 7. Authority limits and historical recovery

- Availability ≠ admission; source bundles ≠ literary monographs; metadata overlap ≠ secure appearance or identity.
- Release order, event number, packet order and corpus Part 2 numbering ≠ story chronology. Do not renumber stable IDs or backdate later evidence and knowledge.
- Written Japanese ≠ performed voice. Preserve uncertain labels, raw attribution receipts, quote/report modes, private audiences and mutually exclusive Sensei choices.
- Source-local identity buckets ≠ canonical biographies; `PARTIAL_MODEL` ≠ a standalone model; exposed retrospective evidence ≠ prospective validation.
- Generated hypothetical output cannot become evidence for an upstream analytical claim.

The [historical current-state archive through cycle 005](90%20Legacy%20and%20Superseded/BLUE_ARCHIVE_CURRENT_STATE_HISTORY_THROUGH_CYCLE_005.md) preserves the complete former map, including earlier rollups, V1 build/retrieval counts, Drive provenance IDs, unit-level cautions, historical readiness and obsolete next-unit instructions. It is **historical_legacy**, never a second current entrypoint. Detailed readings, checkpoints and ledgers remain in their existing canonical homes. The [maintenance audit](08%20Audits%20and%20Manifests/BLUE_ARCHIVE_ROUTING_RESPONSIBILITY_AUDIT_20261001.md) records the responsibility assessment, preservation proof and cold-start check.

Keep future updates here limited to current routing and accepted state. Preserve detailed historical developments in their existing analytical owners. Continue substantive Phase 2 work through the accepted-state owners and source-facing routes above.


## External conditional MAIN S2 V002 integration component — 2026-10-04

A partial mini/G01 contextual extension is prepared for review, with existing histories preserved and source admission unchanged. It is not current authority and does not settle the remaining family, main-only or EVENT reconciliation. The authority frontier remains 480 MAIN, 213 admissions, 516 subjects, 23 PARTIAL_MODEL, 493 UNMODELED and no standalone model.


## External conditional selected-arc integration candidate

A concrete external MAIN S2 V002 candidate now composes preserved original/mini/G01 history with accepted private-family, G06/G26 and D02 scene functions. It broadens the analytical repertoire while retaining source-specific admission, actor/mode/locale distinctions, ordinary pleasure/care/refusals and unresolved outcomes. This is a prepared analytical afterimage, not installed authority, a new model or complete Phase2. Event functions remain a separate overlay; final measured capacity and reasoned admission controls remain necessary before shared application.


## Additional external conditional event functions: CF08 and CF10

The earlier pending-event wording is historical candidate scope. This successor incorporates only the accepted precise CF08 and CF10 functions; other event payloads are not inferred. All original history, source-specific 397 UNADMITTED/two existing ADMITTED Junko statuses and authority codes remain unchanged.

Every changed output above 1 MiB requires a fresh named path/bytes/SHA256 storage review of these final bytes. Earlier storage tuples cover only their own candidates; this candidate remains external pending governed whole-effect review and application.

## Completed review draft published 2026-10-06

Event 820 Episode 13 has a [completed author and sole distinct independent review package](02%20Sequential%20Readings/EVENTS/EVENT_820/REVIEW_DRAFT_20261006_EPISODE_013/README.md), with a [byte-bound publication manifest](02%20Sequential%20Readings/EVENTS/EVENT_820/REVIEW_DRAFT_20261006_EPISODE_013/PUBLICATION_MANIFEST.json). Its publication status is `draft_noncurrent`; its source admission remains `UNADMITTED`. Publication metadata preserves all analytical bodies, with each exact precision delta ordered after its four immutable bases. Accepted intake remains 213; coverage remains 516 subjects, 23 partial models and 493 unmodeled subjects, with no standalone model. All 12 arc rows and all five architectural duties remain incomplete.
