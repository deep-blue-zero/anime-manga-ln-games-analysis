---
title: "IDOLY PRIDE V2 Corpus Coverage and Priority Ledger"
project: "IDOLY PRIDE"
document_id: "IDOLY_PRIDE_V2_CORPUS_COVERAGE_AND_PRIORITY_LEDGER"
version: "1.29-phase-1"
status: "phase-1-card-c1b-frozen-working-ledger"
source_snapshot_id: "IP-V2-SNAPSHOT-2026-08-13-A"
source_cutoff: "2026-08-13"
created: "2026-08-13"
updated: "2026-08-16"
supersedes_working_version: "1.28-phase-1"
immutable_pass_a_snapshot_preserved: true
anime_endpoint_baseline: "IDOLY_PRIDE_V2_ANIME_ENDPOINT_LEDGER_EP01-12"
next_operation: "Phase 1 closure audit and Phase 2 readiness decision"
---

# IDOLY PRIDE V2 CORPUS COVERAGE AND PRIORITY LEDGER

## 1. Status and governing caution

This is the **Pass-A reconnaissance ledger**, not the final stabilized priority map. Every current priority is explicit and revisable. The purpose of this first pass is to make selection visible across the whole corpus before close reading can confirm, split, escalate, or downgrade individual sources.

The authoritative unit of analytical triage is the **ingestion bundle**; the authoritative unit of provenance remains the **granular source story ID**. The companion provenance CSV maps every game story ID to exactly one bundle.

Historical `idoly-ingest-selected-events-core-important` labels are retained only as V1 hypotheses to retest. They do **not** automatically determine V2 priority.

**Event rerank status (2026-08-15):** all 60 raw event bundles have now been independently rescored against the frozen Tier-A main-narrative baseline. The governing event routing map is `IDOLY_PRIDE_V2_PHASE1B_EVENT_RERANK_AUDIT.md`; historical `H` labels in the event table are preserved only for comparison. Event findings themselves remain unadmitted until close-read tranche freezes.

**Event E1-A close-read status (2026-08-15):** the first mandatory E1 tranche is complete and frozen. `event_2021_004`, `event_2022_007`, `event_2022_010`, and `event_2023_006` are now admitted through `IDOLY_PRIDE_V2_PHASE1B_EVENT_E1A_CLOSE_READ_AUDIT.md` and `IDOLY_PRIDE_V2_PHASE1B_POST_EVENT_E1A_BASELINE.md`. Later E1 events remain pending and may not backfill this state.

**Event E1-B close-read status (2026-08-15):** the second mandatory E1 tranche is complete and frozen. `event_2023_009`, `event_2023_011`, `event_2024_005`, and `event_2024_006` are now admitted through `IDOLY_PRIDE_V2_PHASE1B_EVENT_E1B_CLOSE_READ_AUDIT.md` and `IDOLY_PRIDE_V2_PHASE1B_POST_EVENT_E1B_BASELINE.md`. Later E1 events remain pending and may not backfill this state.

**Event E1-C close-read status (2026-08-15):** the third mandatory E1 tranche is complete and frozen. `event_2024_008`, `event_2024_010`, and `event_2024_011` are now admitted through `IDOLY_PRIDE_V2_PHASE1B_EVENT_E1C_CLOSE_READ_AUDIT.md` and `IDOLY_PRIDE_V2_PHASE1B_POST_EVENT_E1C_BASELINE.md`. E1-D/E1-E remain pending and may not backfill the pre-US/persona/public-memory state.

**Event E1-D close-read status (2026-08-15):** the fourth mandatory E1 tranche is complete and frozen as one inseparable United States dependency chain. `event_2025_005` and `event_2025_007` are now admitted through `IDOLY_PRIDE_V2_PHASE1B_EVENT_E1D_CLOSE_READ_AUDIT.md` and `IDOLY_PRIDE_V2_PHASE1B_POST_EVENT_E1D_BASELINE.md`. E1-E remains pending and may not backfill late maturation into the United States dissolution/re-authorization state.

**Event E1-E close-read status (2026-08-15):** the fifth and final mandatory E1 tranche is complete and frozen. `event_2026_002`, `event_2026_003`, and `event_2026_007` are now admitted through `IDOLY_PRIDE_V2_PHASE1B_EVENT_E1E_CLOSE_READ_AUDIT.md` and `IDOLY_PRIDE_V2_PHASE1B_POST_EVENT_E1E_BASELINE.md`. All **16/16 mandatory E1 events** are now close-read and admitted. Per the frozen routing rule, E2 must now be reassessed against the complete post-E1 state before E2 close reading begins.

**Post-E1 E2 reassessment status (2026-08-15):** all **26 original E2 events** have now been rescored for execution order against the complete post-E1-E baseline. The governing reading-order artifacts are `IDOLY_PRIDE_V2_PHASE1B_POST_E1_E2_REASSESSMENT_AUDIT.md` and `IDOLY_PRIDE_V2_PHASE1B_E2_CLOSE_READ_QUEUE.md`. This is routing-only: no E2 event claim has yet been admitted, and `IDOLY_PRIDE_V2_PHASE1B_POST_EVENT_E1E_BASELINE.md` remains the governing analytical checkpoint.

**Event E2-A1 close-read status (2026-08-15):** the first post-E1 E2 tranche is complete and frozen. `event_2021_005`, `event_2022_003`, `event_2024_007`, and `event_2026_004` are admitted through `IDOLY_PRIDE_V2_PHASE1B_EVENT_E2A1_CLOSE_READ_AUDIT.md` and `IDOLY_PRIDE_V2_PHASE1B_POST_EVENT_E2A1_BASELINE.md`. The tranche adds bounded evaluative jurisdiction, non-disposable standing, coauthored mentorship, safeguard-enabled agency, plural idol institutionality, and a split of long-career viability into age legitimacy versus mainstream material sustainability.

**Event E2-A2 close-read status (2026-08-15):** the second post-E1 E2 tranche is complete and frozen. `event_2021_003`, `event_2021_006`, `event_2025_010`, and `event_2026_006` are now admitted through `IDOLY_PRIDE_V2_PHASE1B_EVENT_E2A2_CLOSE_READ_AUDIT.md` and `IDOLY_PRIDE_V2_PHASE1B_POST_EVENT_E2A2_BASELINE.md`. The tranche adds constitutive succession, emergent unit identity, distributed creative authority, influence without derivativeness, non-performative recognition, reciprocal gratitude with an answerability limit, protected leisure as professional infrastructure, stewardship through waiting, and rival infrastructure without assimilation. E2-A3 and later sources remain unadmitted.

**Event E2-A3 close-read status (2026-08-16):** the third post-E1 E2 tranche is complete and frozen. `event_2023_008`, `event_2024_009`, `event_2025_006`, and `event_2025_009` are now admitted through `IDOLY_PRIDE_V2_PHASE1B_EVENT_E2A3_CLOSE_READ_AUDIT.md` and `IDOLY_PRIDE_V2_PHASE1B_POST_EVENT_E2A3_BASELINE.md`. The tranche adds non-totalizing vocation, plural-role authorship, selective disclosure without shame, lineage without vocational predestination, pedigree non-transferability, transformative fidelity, representative creative governance, reciprocal managerial support, non-sovereign leadership, plural protagonism, time-bounded life domains, ordinary-life recovery, fame distance, cross-role fertilization, and role-accumulation risk. `OPEN-04` is resolved at the ontological level: Hoshimi is a professional institution; family/home remains a relational metaphor. E2-B1 and later sources remain unadmitted.

**Event E2-B1 close-read status (2026-08-16):** the first E2-B material-extension tranche is complete and frozen. `event_2022_002`, `event_2023_001`, `event_2025_004`, and `event_2026_001` are now admitted through `IDOLY_PRIDE_V2_PHASE1B_EVENT_E2B1_CLOSE_READ_AUDIT.md` and `IDOLY_PRIDE_V2_PHASE1B_POST_EVENT_E2B1_BASELINE.md`. The tranche adds answerable role constitution, repair without debt ownership, guilt-causal overreach, reparative overwork, a contestable/delegable LizNoir center office, plural role-fit, form adaptation to performers, role-mediated relational truth, scaffolded professional experimentation, strategic/curated IIIX authenticity, trust without friendship label, and audience relational reframing. `OPEN-15` is now resolved for Tsuki and LizNoir while universal generalization remains open; `OPEN-16` is strengthened around answerable construction. E2-B2 and later sources remain unadmitted.

**Event E2-B2 close-read status (2026-08-16):** the second E2-B material-extension tranche is complete and frozen. `event_2022_005`, `event_2023_010`, `event_2024_003`, and `event_2025_001` are now admitted through `IDOLY_PRIDE_V2_PHASE1B_EVENT_E2B2_CLOSE_READ_AUDIT.md` and `IDOLY_PRIDE_V2_PHASE1B_POST_EVENT_E2B2_BASELINE.md`. The tranche adds `RECIPROCAL_STANDING`, reciprocal self-erasure, sibling-role detotalization, support competence without support destiny, trusted conflict capacity, mutuality over unilateral optimization, reciprocal audience coauthorship, fame-scale externalities, intergenerational idol modeling, age-aware equal standing, proportional care intervention, meaningful success beyond rank, and reciprocal care reversibility. `OPEN-03`, `OPEN-07`, and `OPEN-14` are materially advanced; `OPEN-01` gains a present-tense continuation commitment without closing future authorship. E2-C1 and support-deferred sources remain unadmitted.


**Event E2-C1 close-read status (2026-08-16):** the precursor-overlap tranche is complete and frozen. `event_2023_004` and `event_2024_004` are now admitted through `IDOLY_PRIDE_V2_PHASE1B_EVENT_E2C1_CLOSE_READ_AUDIT.md` and `IDOLY_PRIDE_V2_PHASE1B_POST_EVENT_E2C1_BASELINE.md`. The tranche adds `PRECURSOR_AUTHORITY_WITHOUT_MATURE_SUPREMACY`, comparative-status distance, non-extractive reconnection, relational repair without comparative cure, outcome-dependence recursion, deferred participation in inheritance, early Hoshimi contractual scaffolding for IIIX, nonportable prestige, immediate-victory justification, preexisting global ambition, strategic status misrepresentation, and performance-backed reputation bootstrapping. Later E1 remains the stronger mature authority for rivalry, IIIX reauthorization, and mature authenticity. Support-deferred sources remain unadmitted.

**Event SUPPORT-DEFERRED close-read status (2026-08-16):** the final post-E1 E2 execution tranche is complete and frozen. `event_2022_004`, `event_2022_012`, `event_2022_011`, and `event_2023_007` are admitted through `IDOLY_PRIDE_V2_PHASE1B_EVENT_SUPPORT_DEFERRED_CLOSE_READ_AUDIT.md` and `IDOLY_PRIDE_V2_PHASE1B_POST_EVENT_SUPPORT_DEFERRED_BASELINE.md`. All **26/26 sources in the post-E1 E2 execution queue** have now been close-read. The tranche adds `SUPPORTING_AUTHORITY_WITHOUT_THESIS_OWNERSHIP`, affinity-based inheritance, multiperspectival legacy knowledge, admiration-to-peerhood, anniversary re-authoring without erasure, analogical experiential inheritance, IIIX real-friction/maintenance-labor evidence, post-fall media rebuild, selective deliberate practice, live-media leverage, and `AUTHENTICITY_WITHOUT_ETHICAL_EXONERATION`. All four sources remain `SUPPORT`, not `REDUNDANT`; mature thesis ownership remains routed to stronger E1/E2 evidence where specified. E3 and E4 remain pending.

**Event E3 close-read status (2026-08-16):** the seven-source support-mining tranche is complete and frozen. `event_2023_003`, `event_2023_002`, `event_2025_002`, `event_2021_001`, `event_2022_006`, `event_2022_008`, and `event_2022_001` are admitted through `IDOLY_PRIDE_V2_PHASE1B_EVENT_E3_CLOSE_READ_AUDIT.md` and `IDOLY_PRIDE_V2_PHASE1B_POST_EVENT_E3_BASELINE.md`. The tranche adds `SUPPORT_MINING_WITHOUT_CONCEPT_INFLATION`, `EMULATION_WITHOUT_SELF_ERASURE`, ordinary-self professional curation, performed intimacy without private claim, private-life jurisdiction restraint, comparative insecurity as peer recognition, place re-authoring without erasure, participatory production as performance knowledge, rest as creative infrastructure, origin-community reciprocity, non-work LizNoir integration, and genre-expectation refusal. All seven remain `SUPPORT`; mature thesis ownership remains with stronger E1/E2 evidence. E4 remains pending.

**Event E4 close-read status (2026-08-16):** the final eleven-event indexed/selective/caveated tranche is complete and frozen. `event_2022_009`, `event_2023_012`, `event_2024_002`, `event_2025_008`, `event_2021_002`, `event_2024_001`, `event_2023_005`, `event_2024_012`, `event_2025_003`, `event_2025_011`, and `event_2026_005` are routed through `IDOLY_PRIDE_V2_PHASE1B_EVENT_E4_CLOSE_READ_AUDIT.md` and `IDOLY_PRIDE_V2_PHASE1B_POST_EVENT_E4_BASELINE.md`. All **60/60 event bundles** have now received explicit semantic close-read/routing treatment. E4 formalizes `INTERPRETIVE_VALUE_WITHOUT_CONTINUITY_AUTHORITY` and `CROSSOVER_CORROBORATION_REQUIRES_MAINLINE_HOME`; the nine crossover stories remain canon-caveated, while the two uncaveated Tsuki stories are admitted at support-level authority. The event layer is complete, but Phase 1 remains open pending bond/special/card/message sampling and routing.

**Bond priority and sampling status (2026-08-16):** all **20/20 raw bond bundles / 160 granular bond stories** have now received independent Phase-1 sampling/rerank treatment against the complete Tier-A + 60-event model. `IDOLY_PRIDE_V2_PHASE1_BOND_PRIORITY_AND_SAMPLING_AUDIT.md` and `IDOLY_PRIDE_V2_PHASE1_BOND_CLOSE_READ_QUEUE.md` replace the uniform Pass-A assumption that all bonds are equally `IMPORTANT`. Routing result: **3 CORE / B1**, **9 IMPORTANT / B2**, **5 SUPPORT / B3**, **3 TEXTURE / B4**. This operation is routing-only: no bond proposition is admitted, and `IDOLY_PRIDE_V2_PHASE1B_POST_EVENT_E4_BASELINE.md` remains the governing analytical checkpoint until the first bond close-read freeze.

**Bond B1-A close-read status (2026-08-16):** the first mandatory bond tranche is complete and frozen. `bond_kan_001_kan`, `bond_ktn_001_ktn`, and `bond_kor_001_kor` are admitted through `IDOLY_PRIDE_V2_PHASE1_BOND_B1A_CLOSE_READ_AUDIT.md` and `IDOLY_PRIDE_V2_PHASE1_POST_BOND_B1A_BASELINE.md`. The tranche adds `SELECTIVE_PERSONAL_JURISDICTION`, private-self non-monopoly over authenticity, family contact jurisdiction, Saegusa informal protective counterpower with procedural-accountability caution, differentiation-enabled reappropriation of Mana, and active vocational optionality. B2-A/B2-B/B3/B4 bond material remains unadmitted.

**Bond B2-A close-read status (2026-08-16):** the manager/public-private/professional-self bond tranche is complete and frozen. `bond_rui_001_rui`, `bond_skr_001_skr`, `bond_szk_001_szk`, and `bond_mhk_001_mhk` are admitted through `IDOLY_PRIDE_V2_PHASE1_BOND_B2A_CLOSE_READ_AUDIT.md` and `IDOLY_PRIDE_V2_PHASE1_POST_BOND_B2A_BASELINE.md`. The tranche adds `BIDIRECTIONAL_PROFESSIONAL_CARE`, manager-as-care-recipient, managerial affirmation as a relational resource, affective self-consciousness without romantic settlement, fan identity persisting after peerhood, direct relationship superseding parasocial extraction, self-authored devotion overload, unsentimental audience reciprocity, and multiregister authenticity. `OPEN-05` and `OPEN-16` advance; 7/20 bond bundles are now admitted. B2-B/B3/B4 material remains unadmitted.
**Bond B2-B close-read status (2026-08-16):** the family/role/developmental-continuity bond tranche is complete and frozen. `bond_hrk_001_hrk`, `bond_ski_001_ski`, `bond_rei_001_rei`, `bond_smr_001_smr`, and `bond_rio_001_rio` are admitted through `IDOLY_PRIDE_V2_PHASE1_BOND_B2B_CLOSE_READ_AUDIT.md` and `IDOLY_PRIDE_V2_PHASE1_POST_BOND_B2B_BASELINE.md`. The tranche adds `ROLE_CONTINUITY_WITHOUT_ROLE_CAPTIVITY`, Haruko's material vocational opportunity cost and ordinary-life option-space, reversible Saki/Chisa sibling care, assimilated influence becoming self-authored judgment, Rei parental concern/trust friction, Sumire's family model of parallel labor and creative aspiration, and internally anchored pre-debut Rio/Aoi reciprocity. `OPEN-14` materially advances; 12/20 bond bundles are now admitted. All mandatory B1/B2 bond bundles are complete. B3/B4 remain unadmitted.

## 2. Coverage summary

- Game ingestion bundles catalogued: **665 / 665**
- Granular game source stories mapped: **3879 / 3,879**
- Anime episodes catalogued: **12 / 12**
- Total analytical triage units in this ledger: **677**
- Historical curated event bundles present: **53 / 60 current events**
- Game bundles carrying missing/formal asset flags: **32**

### By corpus layer
| Layer | Items | Pass-A role |
|---|---:|---|
| `main_story` | 63 | Tier-A governing narrative |
| `unit_origins` | 33 | Tier-A formative/unit history |
| `events` | 60 | substantial developmental events |
| `bond_stories` | 20 | bond/manager relational development |
| `cards` | 363 | character micro-development/texture |
| `messages` | 99 | voice/ordinary-life texture |
| `specials_misc` | 27 | requires semantic classification |
| `anime` | 12 | Tier-A narrative + audiovisual form |

### Pass-A priority distribution
| Priority | Items | Meaning at this stage |
|---|---:|---|
| `FOUNDATIONAL` | 3 | provisional triage |
| `CORE` | 106 | provisional triage |
| `IMPORTANT` | 79 | provisional triage |
| `TEXTURE` | 462 | provisional triage |
| `UNRESOLVED` | 27 | provisional triage |
| `CONFLICTING` | 0 | none assigned yet |
| `FORMAL-DEPENDENT` | 0 | none assigned yet |
| `REDUNDANT` | 0 | none assigned yet |

## 3. Pass-A assignment rules

- `main_story` -> `CORE`: governing narrative must enter every mature longitudinal reconstruction.
- `unit_origins` -> `CORE`; Mana origin bundles -> `FOUNDATIONAL`: formative history is structural rather than optional background.
- `events` -> `IMPORTANT` pending individual semantic review. An event can move to `CORE`, `TEXTURE`, `CONFLICTING`, or another category after close reading.
- `bond_stories` -> `IMPORTANT` pending character-by-character review.
- `cards` and `messages` -> `TEXTURE` **as a starting assumption only**; either can be escalated when it changes a stable model or resolves an ambiguity.
- `specials_misc` -> `UNRESOLVED` until its narrative function is classified.
- anime E01-E12 -> `CORE` and `requires_av_review=YES` because the anime is both governing narrative and formal evidence.

## 4. Immediate correction to the historical selection layer

The historical curated event folder contains **53 of the 60 current event bundles**. It is therefore useful as a V1 discovery artifact but cannot serve as the V2 coverage boundary. The seven current event bundles outside it are:
- `event_2023_005_st-eve-2305-race` — **きょうえん！HTT＆HMA～放課後ティータイム＆星見アンバサダー～**
- `event_2024_001_st-eve-2401-race` — **にゃんか不思議なお正月！？**
- `event_2024_012_st-eve-2412-contest` — **心跳ねるクリスマスパーティー**
- `event_2025_003_st-eve-2503-dice` — **SOS！星見プロダクションの転送～ただのアイドルには興味ありません！？～**
- `event_2025_011_st-eve-2512-dice` — **ドタバタ！？トラブルクリスマス！**
- `event_2026_006_st-eve-2606-dice` — **羽ばたけ！恩返しのAile**
- `event_2026_007_st-eve-2607-marathon-raid` — **PRIDE貫く頂点への道標**

The July 2026 event `event_2026_007_st-eve-2607-marathon-raid` received a direct Phase-1 spot check and is already promoted to **CORE**. It explicitly presents SUNNY PEACE after becoming BIG4 as still seeking further growth, and uses DoriKyun as an adversarial developmental benchmark. This is precisely the kind of late evidence that an older hand-curated list can miss.

## 5. Close-reading order generated by Pass A

1. **63 main-story bundles** — stabilize governing chronology and arc architecture.
2. **33 unit-origin bundles** — stabilize formative histories, with Mana first.
3. **60 event bundles** — independently re-evaluate all 53 historically selected events plus the seven outside the old selection.
4. **20 bond bundles** — identify manager/idol and longitudinal character claims that cannot be reconstructed from events alone.
5. **27 specials/misc bundles** — classify whether they are canonical development, supplemental context, comedy, formal material, or low-weight special content.
6. **363 card bundles and 99 message bundles** — use character/relationship coverage, contradiction signals, and voice/register needs to choose close-reading samples; escalate consequential items.
7. **12 anime episodes** — maintain complete coverage now, while detailed audiovisual audit remains routed to the dedicated formal phase.

## 5A. Phase 1B semantic audit progress — 2026-08-14

The immutable Pass-A package and its SHA-256 manifest remain preserved. This v1.2 file is the **active working ledger** and begins semantic Pass B after completion of the prospective TV-anime baseline.

### Tranche 01 completed

Reviewed against the frozen anime endpoint:

- all **23 `st-original-cmn` / Hoshimi anime-era game blocks** (122 granular scenes);
- all **three Mana unit-origin bundles** (15 granular scenes);
- anime E01–E12 status updated from provisional Pass-A routing to **`PHASE_0_5_CLOSE_READ_FROZEN`**.

The detailed audit is stored separately as `IDOLY_PRIDE_V2_PHASE1B_TIER_A_AUDIT_TRANCHE_01.md`.

### Priority result

- `hoshimi_001`–`hoshimi_023`: **CORE confirmed**; no block is demoted to REDUNDANT. The game retelling repeatedly adds **Makino** first-person interiority, branch-parameterized Makino expression, and explicit professional reasoning that the anime cannot supply in equivalent form.
- `origin_mna_001`–`origin_mna_003`: **FOUNDATIONAL confirmed**. These are indispensable for Mana, Makino, LizNoir historical ecology, miracle/labor, and manager-ethics reconstruction.
- `st-original-cmn` must therefore be treated as a **cross-media retelling/expansion layer**, not as a disposable duplicate of the anime.

### Makino identity rule and branch-canon handling

The game manager is treated as **Makino Kouhei continuity by default**, not as an unresolved player/Makino equivalence problem. The editable name and `{user}` placeholder are interface parameterization layered onto Makino's continuing Hoshimi role, visual identity, voiced presentation, and history. Only explicit primary-source contradiction can reopen the identity question.

Phase 2 therefore requires a **Makino Player-Branch Canon Ledger** whose job is narrower and more precise:

- preserve identity-invariant and branch-invariant Makino facts as ordinary canon;
- preserve mutually exclusive selectable responses as Makino-compatible authored possibility space without pretending they all co-occurred;
- record branch IDs for load-bearing optional lines;
- distinguish interface customization from diegetic identity evidence.

### Tranche 02 completed — Hoshimi anime/game expansion audit

The dedicated 23-block / 122-scene cross-media audit is complete and archived as:

- `IDOLY_PRIDE_V2_HOSHIMI_ANIME_GAME_EXPANSION_AUDIT.md`;
- `IDOLY_PRIDE_V2_HOSHIMI_ANIME_GAME_EXPANSION_MATRIX.csv`.

The frozen anime endpoint remained the prospective baseline. The audit classified direct retelling, Makino POV expansion, explicitated professional reasoning, game-original character arcs, information-order shifts, anime-only audiovisual evidence, and genuine continuity variants.

Key results:

- all 23 Hoshimi blocks remain **CORE** and are now `PASS_B_CROSS_MEDIA_AUDITED`;
- the Hoshimi slice contains 10,709 dialogue/narration lines, including 2,844 Manager/Makino lines and 1,178 explicit internal/parenthetical Makino lines;
- the game front-loads Sakura's heart-transplant fact relative to the anime and therefore must not be allowed to collapse the anime's prospective medical mystery;
- Haruko, Rei, Nagisa, Suzu, Mei, Saki/Chisa, and Shizuku receive main-story developmental material that the anime either omits or compresses;
- later Hoshimi chronology materially resequences some Rui/Asakura, Kotono/Rio, Mana-disappearance, and semifinal/final material;
- `Pray for you` is a genuine finale continuity variant: the game uses a planned ten-person `サヨナラから始まる物語` final followed by a `First Step` encore, whereas the anime uses separate unit final performances, a tie, and then the ten-person stage.

These differences are not to be silently harmonized. Phase 2 will maintain explicit information-order and continuity-variant routing.

### Tranche 03 completed — SUNNY PEACE origins

The five SUNNY PEACE origin bundles have now received full Phase-1B close reading against the frozen anime endpoint and completed Hoshimi anime/game expansion audit. The primary-source finding set was frozen before historical SUNNY PEACE analytical prose was retrieved.

Canonical tranche artifacts:

- `IDOLY_PRIDE_V2_PHASE1B_SUNNY_PEACE_ORIGIN_PRIMARY_FINDINGS_FREEZE.md`;
- `IDOLY_PRIDE_V2_PHASE1B_SUNNY_PEACE_ORIGIN_AUDIT.md`;
- `IDOLY_PRIDE_V2_HOSHIMI_ANIME_GAME_EXPANSION_AUDIT_ADDENDUM_SUNNY_PEACE_ORIGINS.md`.

Priority/status result:

- `origin_sun_001_chisa_s_memories` -> **CORE / `PASS_B_ORIGIN_AUDITED`**;
- `origin_sun_002_rei_s_memories` -> **CORE / `PASS_B_ORIGIN_AUDITED`**;
- `origin_sun_003_shizuku_s_memories` -> **CORE / `PASS_B_ORIGIN_AUDITED`**;
- `origin_sun_004_haruko_s_memories` -> **CORE / `PASS_B_ORIGIN_AUDITED`**;
- `origin_sun_005_sakura_s_memories` -> **CORE / `PASS_B_ORIGIN_AUDITED`**.

Major tranche findings:

- SUNNY PEACE's explicit formation logic is complementary non-self-sufficiency: Makino wants to assemble people with potential who cannot shine alone, not simply sort bright personalities into a sun unit.
- Chisa's reserve is causally tied to a burden-avoidance ethic created by the near-drowning/Saki guilt loop; Makino tests whether her idol desire survives separation before scouting her.
- Rei's result orientation is better modeled as a response to paternal invalidation than as generic perfectionism; fan recognition restores the audience-facing purpose of performance and converts idolhood from instrument to chosen vocation.
- Shizuku's barrier is punitive visibility rather than simple introversion; fandom first provides a safe participatory public, and Makino reframes fan knowledge as idol competence.
- Haruko is literally Hoshimi Production's **first idol**. Saegusa selects her partly for the future value of kindness plus persistence, and Makino later states that SUNNY PEACE cannot exist without her experience/care/endurance.
- Sakura's smiling begins partly as protective emotional labor for her family, Tomo gives her permission to cry, the `やってみたかったリスト` originates under mortality, and Tomo later explicitly rejects survivor substitution.
- Sakura's trust in heartbeat intuition predates her later Mana identity crisis; this strengthens rather than overturns the frozen anime endpoint that the heart has provenance without retaining jurisdiction.

### Hoshimi expansion-audit addendum status

**REQUIRED and completed.** The origin tranche materially changes provenance for Chisa recruitment/separation, Makino's explicit group-design rationale, Haruko's founding institutional status and SUNNY necessity, and Sakura's pre-Hoshimi heartbeat/Haruko/Tomo trajectory. These revisions are stored in a separate addendum and do not rewrite the parent cross-media audit or frozen anime prospective state.

### Tranche 04 completed — Tsuki no Tempest origins

The five Tsuki no Tempest origin bundles have now received full Phase-1B close reading against the frozen anime endpoint, completed Hoshimi anime/game expansion audit, and completed SUNNY PEACE origin tranche. The source-native findings were frozen before historical Tsuki analytical prose was retrieved.

Canonical tranche artifacts:

- `IDOLY_PRIDE_V2_PHASE1B_TSUKI_NO_TEMPEST_ORIGIN_PRIMARY_FINDINGS_FREEZE.md`;
- `IDOLY_PRIDE_V2_PHASE1B_TSUKI_NO_TEMPEST_ORIGIN_AUDIT.md`;
- `IDOLY_PRIDE_V2_HOSHIMI_ANIME_GAME_EXPANSION_AUDIT_ADDENDUM_TSUKI_NO_TEMPEST_ORIGINS.md`;
- `IDOLY_PRIDE_V2_PHASE1B_SUNNY_PEACE_ORIGIN_AUDIT_ADDENDUM_TSUKI_SAKI.md`.

Priority/status result:

- `origin_moon_001_saki_s_memories` -> **CORE / `PASS_B_ORIGIN_AUDITED`**;
- `origin_moon_002_suzu_s_memories` -> **CORE / `PASS_B_ORIGIN_AUDITED`**;
- `origin_moon_003_mei_s_memories` -> **CORE / `PASS_B_ORIGIN_AUDITED`**;
- `origin_moon_004_nagisa_s_memories` -> **CORE / `PASS_B_ORIGIN_AUDITED`**;
- `origin_moon_005_kotono_s_memories` -> **CORE / `PASS_B_ORIGIN_AUDITED`**.

Major tranche findings:

- Tsuki no Tempest's origin architecture is best modeled as **attachment -> vow -> testing -> chosen commitment**. Relationships remain causally central, but character growth repeatedly changes who has jurisdiction over what the attachment means.
- The preferred unit thesis is: **Tsuki no Tempest is an ecology for turning attachment into authorship.**
- Saki's central problem is internalized responsibility functioning as a permission structure. Her resolution preserves competence, family care and education by making their relationship to idol desire authored rather than compulsory.
- Saki's origin and Chisa's already-audited origin jointly establish a **reciprocal sacrifice loop**: each sister interpreted self-limitation as evidence of love. A controlled SUNNY cross-tranche addendum records this bilateral model.
- Suzu's Mana inheritance begins not with idol imitation but with Mana teaching truthful self-disclosure; Suzu first uses that lesson to tell her parents she is lonely. After Mana's death, idolhood becomes a desire to give someone else the courage Suzu once received.
- Suzu's parental conflict tests durable commitment more than the legitimacy of idolhood itself; her family questions whether admiration can survive the labor behind the image.
- Mei's `本気` problem establishes a professional dialectic between sustained effort and serious enjoyment. Her later lightness should not be reduced to unserious comic relief.
- Mei's choice of idolhood is also a movement from generalized social usefulness toward particular durable belonging: Suzu is the first person whose promise of togetherness gives Mei a reason to organize continuity around one group.
- Nagisa's origin strongly confirms yuri-adjacent coding with Kotono while preserving the guardrail that explicit romance is not established. Her best early care follows an **accompaniment** model: persistence without confiscating Kotono's choice.
- The Mana/Kotono/Nagisa notebook is a load-bearing object of relational succession: Nagisa renews the proposition that Kotono is not alone without becoming Mana's replacement.
- Kotono's diary discovery is the precise causal source of her proxy-completion mission. Mana's diary gives evidence of love and unfinished work; **Kotono herself converts those facts into a commission Mana never explicitly issues**. This materially strengthens the frozen anime self-authorship arc.
- Tsuki's origin causal topology is polycentric even if Kotono later becomes a major unit center: Saki originates in Chisa/family responsibility, Suzu in Mana/family, Mei in cheer/Suzu, Nagisa in Kotono, and Kotono in Mana/Nagisa.

### Historical V1 stress-test result

The earlier Tsuki work was strong at character-level pattern recognition and is mostly confirmed. V2's main corrections are causal and source-order precision. The historical phrase **"attachments become destinies"** is retained only as an evocative shorthand and is superseded for governing analysis by **"attachments supply vectors; the characters must decide whether to choose those vectors again as their own."** Later BIG4/event moonlight philosophy must not be silently projected backward as an origin-stage conscious doctrine.

### Addendum status

Two controlled addenda were required and completed:

1. **Hoshimi expansion-audit addendum:** routes Saki expectation provenance, Suzu/Mana causal sequence, Mei `本気`/belonging history, Nagisa's Mana promise/notebook role, and Kotono's diary-to-proxy-mission mechanism.
2. **SUNNY cross-tranche addendum:** joins Chisa and Saki's independent origin evidence into the bilateral Shiraishi reciprocal-sacrifice model without rewriting either frozen tranche.

### Next output and recommended model

**Next output:** `IDOLY_PRIDE_V2_PHASE1B_TSUKI_NO_TEMPEST_ORIGIN_TRANCHE_SHA256SUMS.txt`

**Recommended model:** GPT-5.6 Sol  
**Recommended reasoning level:** **Low**

**Reason:** the analytical decisions are already stabilized. The next artifact is an integrity manifest whose job is exact filename/hash recording rather than interpretation. After the manifest, the next analytical tranche is LizNoir origins and returns to High reasoning.

### Tranche 05 completed — LizNoir origins

All ten LizNoir origin bundles have now received full Phase-1B close reading across **43 granular stories / 4,333 utterances / 131,936 corpus characters**. The source-native findings were frozen and SHA-256 hashed before any historical LizNoir analytical prose was consulted.

Canonical tranche artifacts:

- `IDOLY_PRIDE_V2_PHASE1B_LIZNOIR_ORIGIN_PRIMARY_FINDINGS_FREEZE.md` v1.0 — immutable pre-historical freeze;
- `IDOLY_PRIDE_V2_PHASE1B_LIZNOIR_ORIGIN_PRIMARY_FINDINGS_FREEZE_v1.1.md` — pronoun-only editorial correction for Igawa Aoi; no substantive analytical change;
- `IDOLY_PRIDE_V2_PHASE1B_LIZNOIR_ORIGIN_AUDIT.md`;
- `IDOLY_PRIDE_V2_HOSHIMI_ANIME_GAME_EXPANSION_AUDIT_ADDENDUM_LIZNOIR_ORIGINS.md`;
- `IDOLY_PRIDE_V2_PHASE1B_TIER_A_AUDIT_TRANCHE_01_ADDENDUM_LIZNOIR_SAEGUSA_VENUS.md`.

Priority/status result:

- `origin_liz_001_a_budding_lily` -> **CORE / `PASS_B_ORIGIN_AUDITED`**;
- `origin_liz_002_one_more_dream` -> **CORE / `PASS_B_ORIGIN_AUDITED`**;
- `origin_liz_003_impatience_of_hollyhock` -> **CORE / `PASS_B_ORIGIN_AUDITED`**;
- `origin_liz_004_love_heart` -> **CORE / `PASS_B_ORIGIN_AUDITED`**;
- `origin_liz_005_smile_or_perfect_performance` -> **CORE / `PASS_B_ORIGIN_AUDITED`**;
- `origin_liz_006_brand-new_liznoir` -> **CORE / `PASS_B_ORIGIN_AUDITED`**;
- `origin_liz_007_black_lily_in_the_storm` -> **CORE / `PASS_B_ORIGIN_AUDITED`**;
- `origin_liz_008_the_road_of_battle` -> **CORE / `PASS_B_ORIGIN_AUDITED`**;
- `origin_liz_009_the_beginning_venus` -> **CORE / `PASS_B_ORIGIN_AUDITED`**;
- `origin_liz_010_kokoro_ai_s_memories` -> **CORE / `PASS_B_ORIGIN_AUDITED`**.

Major tranche findings:

- LizNoir's governing origin question is **what excellence is for**, not whether excellence itself is desirable. The preferred tranche thesis is: **excellence remains meaningful only while it serves human desire and communication rather than replacing them.**
- Rio's idol vocation develops from family/economic instrumentality into personally non-substitutable desire. Her professional severity has material/familial provenance.
- Aoi's original role is to restore felt/embodied expression to Rio's technically correct but emotionally disconnected performance. Aoi's later major failure mode is **protection-through-secrecy**: care that edits what a partner is allowed to know.
- Mana did **not** cause Saegusa to leave BanPro. Saegusa's industry/VENUS disillusionment predates Mana; Rio's heat delays his departure long enough for him to debut LizNoir. Rio's abandonment account is psychologically operative but historically misattributed.
- Mana becomes a vocation catalyst and then a **frozen rival benchmark** after death removes the possibility of future reciprocal contest.
- Losing to Tsuki is a major hinge because Rio can lose without treating defeat as retroactive invalidation of LizNoir, her career, or the Rio/Aoi partnership.
- Kokoro's `可愛いこころ` persona begins as an authored survival/visibility strategy under repeated rejection and becomes lived identity; it should not be classified as wholly fake or wholly innate.
- Ai and Kokoro are explicitly recruited together and must mature from disciples/fans into co-authors of LizNoir. Their pair is a second inheritance dyad distinct from Rio/Aoi.
- The initial `smile` conflict is only a local proxy. New York reveals the deeper missing quality as **communicative affect**: correct motion/voice must express a felt intention to an audience.
- The mature quartet's strongest invariant is not fixed form but **prideful authored participation and continued struggle**. Four-person LizNoir does not invalidate the original duo; it widens ownership of the name.
- `The Beginning Venus` makes the institutional argument explicitly dialectical. Saegusa identifies the damage of ranking/AI winner-loser logic; Rio insists meaningful competition can sharpen skill, desire, and pride. The current V2 institutional hypothesis is therefore **critique of metric colonization, not blanket rejection of competition**.

### Editorial-freeze note

The original LizNoir primary freeze v1.0 remains the immutable proof that source-native findings were locked before historical analysis. After that freeze, historical project material surfaced the standing correction that Igawa Aoi is a woman. A v1.1 human-readable copy corrects only mistaken English pronouns/gendered wording; it does **not** modify any claim, locator, evidence class, counterevidence, or interpretation.

### Cross-media / prior-tranche addenda status

**REQUIRED and completed.** Two controlled addenda were emitted:

1. the Hoshimi anime/game expansion addendum, routing Rio/Aoi/Mana rivalry provenance, the Tsuki defeat, and the no-backfill rule for later four-person LizNoir;
2. the Tranche-01 Saegusa/VENUS addendum, routing VENUS authorship, Saegusa's pre-Mana disillusionment, Hoshimi as counter-practice to victory-only value, and Rio's explicit defense of meaningful competition.

No frozen anime or prior origin finding was silently rewritten.

### Tranche 06 completed — TRINITYAiLE origins

All six TRINITYAiLE origin bundles have now received full Phase-1B close reading across **30 granular stories / 2,948 utterances / 90,097 corpus characters**. The source-native findings were frozen and SHA-256 hashed before any historical TRINITYAiLE analytical prose was consulted.

Canonical tranche artifacts:

- `IDOLY_PRIDE_V2_PHASE1B_TRINITYAILE_ORIGIN_PRIMARY_FINDINGS_FREEZE.md` — pristine pre-historical freeze;
- `IDOLY_PRIDE_V2_PHASE1B_TRINITYAILE_ORIGIN_AUDIT.md`;
- `IDOLY_PRIDE_V2_HOSHIMI_ANIME_GAME_EXPANSION_AUDIT_ADDENDUM_TRINITYAILE_ORIGINS.md`.

Priority/status result:

- `origin_tri_001_white_resolve` -> **CORE / `PASS_B_ORIGIN_AUDITED`**;
- `origin_tri_002_shoot_for_the_sky` -> **CORE / `PASS_B_ORIGIN_AUDITED`**;
- `origin_tri_003_light_my_fire` -> **CORE / `PASS_B_ORIGIN_AUDITED`**;
- `origin_tri_004_r_aliser` -> **CORE / `PASS_B_ORIGIN_AUDITED`**;
- `origin_tri_005_because_sisters` -> **CORE / `PASS_B_ORIGIN_AUDITED`**;
- `origin_tri_006_violette_blooming_proudly` -> **CORE / `PASS_B_ORIGIN_AUDITED`**.

Major tranche findings:

- The preferred unit thesis is: **TRINITYAiLE permits asymmetry of role without asymmetry of personhood.** Rui may remain center, Yu strategist/second position, and Sumire youngest expressive member without any role authorizing one person to suppress her full agency or ability.
- Rui's idol dream **predates** discovery of Asakura's paternity. Paternal abandonment does not originate the vocation; it hardens the criterion of success into an evidentiary demand to become an `絶対的なアイドル` whom even Asakura cannot ignore.
- Rui's early formation ethic explicitly rejects instrumental partnership: `「利用する」って考え方は好きじゃない` / `組むのなら真剣に、対等でいたい`. Visible center hierarchy therefore coexists from the beginning with an equality-of-persons norm.
- Yu's second-position identity is both sincerely chosen and defensively conditioned. Her growth is not "stop supporting Rui" but **stop assuming support requires becoming smaller**.
- In the controlled performance contest, Rui narrowly wins two of three songs but **Yu wins the aggregate score**. This directly prohibits interpreting Rui's center/`absolute` language as universal superiority across every measurable performance dimension.
- Sumire's absence during a record-setting Rui/Yu performance establishes a crucial distinction: **competitive sufficiency is not the same thing as constitutive group identity**. `三人でトリエル` is a chosen/normative identity, not a false claim that the duo cannot win.
- Sumire's entertainment history has a dual genealogy: it begins partly as family-support labor tied to her brother's piano dream and later becomes a self-authored desire to become a top idol with Rui and Yu.
- The Sumire/brother family crisis forms a reciprocal-sacrifice structure comparable to, but causally distinct from, the Shiraishi sisters. The comparative Phase-2 claim is that care becomes recursively zero-sum when both people use self-denial to protect the other's future.
- `全部欲しい` is not magical optimism. TRINITYAiLE uses research, management, commerce, celebrity reach, sponsorship, labor, and local institutions to expand a seemingly zero-sum choice-space. Sumire's decisive authored act is asking the others to help her keep both idolhood and family care.
- Asakura's producer competence and paternal adequacy must remain separate analytical axes. His exact motive for early paternal non-recognition remains unresolved.
- Mana becomes TRINITYAiLE's professional benchmark partly through Asakura's mediation. Grand Prix defeat against SUNNY PEACE opens a future `長瀬麻奈に縛られることのない` without abolishing competitive ambition.
- `Réaliser` origin placement strengthens the frozen anime post-defeat interpretation but does not substitute for the later dedicated lyric/music/voice audit.
- Himeno Kiriko's Yamagata assistance shows that useful institutional support and instrumental motive can coexist; this is an early bridge toward later industry/autonomy analysis without importing Tokyo evidence prematurely.

### Historical V1 stress-test result

The historical TRINITYAiLE origin analysis was unusually strong and is mostly confirmed. V2's principal corrections are precision upgrades rather than reversals:

- "exceptional girls learn not to amputate attachments" is retained but governed by the more exact **full-strength interdependence** model;
- "Yu's self-erasure" is qualified because second place is partly a genuine authored preference; the unstable part is equating support with suppressed ability;
- "full-power competition as proof of love" is narrowed to **trust/full-strength reciprocity**;
- Sumire's three-person indispensability is relational/normative rather than proof that Rui/Yu cannot succeed technically without her;
- `全部欲しい` is strengthened by material/institutional execution and qualified against wishful non-zero-sum optimism;
- global claims such as TRINITYAiLE being the franchise's "most professional" unit remain deferred until comparative full-corpus synthesis.

No major historical V1 claim is overturned.

### Hoshimi expansion-audit addendum status

**REQUIRED and completed.** The controlled TRINITYAiLE addendum routes Rui's vocation chronology, Yu's aggregate win and self-suppression history, the founding `対等` ethic, Sumire's competitive-sufficiency/constitutive-identity distinction, Asakura-mediated Mana benchmarking, Grand Prix release from Mana's jurisdiction, and the no-backfill rule for post-Grand-Prix sisterhood/Yamagata material.

No frozen anime finding or prior origin finding was silently rewritten.

### Cross-tranche comparison status

No separate SUNNY/Tsuki rewrite addendum is required. The resemblance between Sumire/brother and the Shiraishi sisters is registered as a **Phase-2 comparative care claim** with an explicit non-equivalence guardrail rather than used to mutate either prior source-native freeze.

### Next output and recommended model

**Next output:** `IDOLY_PRIDE_V2_PHASE1B_TRINITYAILE_ORIGIN_TRANCHE_SHA256SUMS.txt`

**Recommended model:** GPT-5.6 Sol  
**Recommended reasoning level:** **Low**

**Reason:** the substantive TRINITYAiLE work is complete; this artifact is integrity bookkeeping. The manifest is now frozen and the architecture has advanced to IIIX.

### Tranche 07 completed — IIIX origins

All four IIIX origin bundles have now received full Phase-1B close reading across **20 granular stories / 2,214 utterances / 71,438 corpus characters**. The source-native finding set was frozen and SHA-256 hashed before historical IIIX prose or historical Tokyo interpretation was consulted.

Canonical tranche artifacts:

- `IDOLY_PRIDE_V2_PHASE1B_IIIX_ORIGIN_PRIMARY_FINDINGS_FREEZE.md`;
- `IDOLY_PRIDE_V2_PHASE1B_IIIX_ORIGIN_AUDIT.md`;
- preserved historical `IDOLY_PRIDE_V2_PHASE1B_IIIX_PRE_TOKYO_BASELINE.md` v1.0;
- `IDOLY_PRIDE_V2_PHASE1B_IIIX_ORIGIN_CHRONOLOGY_CORRECTION_AND_TOKYO_GATE_REVISION.md`;
- governing `IDOLY_PRIDE_V2_PHASE1B_IIIX_PRE_TOKYO_BASELINE_v1.1.md`.

Priority/status result:

- `origin_thrx_001_diamond_mining` -> **CORE / `PASS_B_ORIGIN_AUDITED`**;
- `origin_thrx_002_house_of_cards` -> **CORE / `PASS_B_ORIGIN_AUDITED`**;
- `origin_thrx_003_gears_go_awry` -> **CORE / `PASS_B_ORIGIN_AUDITED`**;
- `origin_thrx_004_re-polished` -> **CORE / `PASS_B_ORIGIN_AUDITED`**.

Major tranche findings:

- The origins establish **two IIIXs**: a first corporate product assembled by Preta Porte and a second, self-authorized freelance unit chosen after defeat, Himeno's collapse, and the disappearance of institutional guarantees.
- The preferred longitudinal thesis is **authenticity through re-authorization**: IIIX does not become legitimate by discovering pure motives; the same three people receive a real opportunity to stop and choose the unit again under materially worse conditions.
- The preferred relationship model is **adversarial interdependence / deliberately non-sentimental loyalty**. The members reject friendship vocabulary but exceed pure utility through disclosure, professional trust, defense of shared work, and voluntary re-selection.
- miho's idol vocation originates with Yō in an audience-facing wish to make people happy. Mana's death becomes bound to a grievance about **unequal public mourning**, and miho converts that grievance into a retaliatory memory project.
- The small-live fan who remembers Yō destabilizes miho's belief that Yō has vanished from public memory but does **not** resolve the anti-Mana project; at the origin endpoint miho still says she will continue until Mana's memory is overwritten. Tokyo therefore inherits an unresolved contradiction rather than a completed redemption.
- fran's instrumentalism contains an aesthetic/self-authorship floor. Fashion remains first vocation, while idolhood becomes a genuine secondary vocation.
- kana's visibility motive combines vanity, skilled self-branding, competitive status, and an explicit search signal toward her missing father. Her suspicion of Himeno is informed by prior family exploitation rather than being generic antagonism.
- Himeno exploits rather than creates IIIX's instrumental motives. The group nevertheless bears responsibility for **motivated toleration** because warning signs are recognized before the final break.
- The key ethical distinction is not competition versus care, but **rules-aware performance optimization versus externally contaminated victory**. IIIX continues to value scores, rankings, and technical control after rejecting sabotage/manipulation.
- The strongest current institutional reading is **critique of metric colonization rather than rejection of measurement or competition**.
- The reduced live adds audience encounter to IIIX's value model without converting the group into SUNNY PEACE or erasing its technical identity.
- The full origin endpoint eventually exits Preta Porte and continues freelance, taking on office/legal/work-acquisition functions itself. **This is post-I-UNITY state and must not be projected backward into the IIIX that Tokyo initially encounters.** Tokyo inherits only the securely pre-Tokyo IIIX baseline; the freelance/self-managed endpoint becomes admissible only through the post-I-UNITY -> BIG4 entry bridge.
- miho recognizes Makino as the same young man associated with Mana, independently corroborating the project's Makino-continuity rule. This confirms an existing source rule and does not require a Hoshimi parent-audit addendum.

### Historical V1 stress-test result

The historical IIIX origin reading is strong on motive specificity and the unit's unsentimental texture. V2 makes several precision corrections:

- `weaponized selfhood` is retained for the first formation but replaced as the mature unit thesis by **re-authorization**;
- `anti-SUNNY PEACE` is qualified as a contrast in formation/relational grammar rather than pure philosophical negation;
- “miho's revenge premise collapses” is weakened to **destabilized but explicitly unresolved**;
- “not friendship, not love” is qualified to preserve self-description while recognizing durable non-sentimental loyalty;
- “toxic/corrosive partnership” is replaced by the less pathologizing **adversarial interdependence**;
- “strongest critique of VENUS” is split into a more precise critique of metric colonization;
- `earned indispensability` is retained in a narrower form as **earned non-substitutability**.

Historical V1 Tokyo conclusions were quarantined through the Tokyo source-native freeze. They were consulted only after that freeze was SHA-256 locked.

### Hoshimi addendum status

**NOT REQUIRED.** The IIIX origins corroborate Makino identity continuity and provide Hoshimi-era impressions, but do not revise any frozen anime/Hoshimi retelling classification or prospective anime-state claim.

### IIIX chronology and Tokyo-gate correction

The earlier v1.0 IIIX pre-Tokyo gate incorrectly treated the endpoint of all four IIIX origin bundles as anterior to Tokyo. `origin_thrx_003` and `origin_thrx_004` cross into I-UNITY and post-I-UNITY chronology. The original v1.0 gate remains preserved as an archival record; `IDOLY_PRIDE_V2_PHASE1B_IIIX_PRE_TOKYO_BASELINE_v1.1.md` supersedes it for prospective use.

**IIIX source prerequisite: SATISFIED.**

**Tokyo opening gate: CORRECTED AND SATISFIED by v1.1.**

The Tokyo audit therefore carries `CONTROLLED_RECONSTRUCTION_WITH_DISCLOSED_PRIMARY_SOURCE_HINDSIGHT` rather than a pristine label.

### IIIX post-I-UNITY -> BIG4 entry gate repair — completed 2026-08-15

The frozen post-Tokyo baseline deliberately left the exact admission point for the later `Re-Polished` endpoint open. A pre-BIG4 chronology audit has now resolved that question without rewriting either the Tokyo freeze or the v1.1 Tokyo-entry gate.

Canonical prospective artifacts:

- `IDOLY_PRIDE_V2_PHASE1B_IIIX_POST_IUNITY_TO_BIG4_ENTRY_BRIDGE.md`;
- `IDOLY_PRIDE_V2_PHASE1B_BIG4_ENTRY_GOVERNING_BASELINE.md`.

Gate result:

- `st-group-thrx-01-01-17` remains the I-UNITY boundary anchor;
- `st-group-thrx-01-01-18 -> 20` are newly admitted after Tokyo and before BIG4;
- the factual endpoint is voluntary IIIX continuation followed by freelance/self-managed operation;
- `second founding` / `authenticity through re-authorization` remains a high-confidence interpretive formulation rather than bare textual fact;
- `big4_001` opening transition evidence confirms that freelance IIIX is already past history when BIG4 begins.

This repair also corrects a prospective-state defect in ledger v1.1, whose IIIX tranche summary mistakenly said that the IIIX *Tokyo encounters* is already increasingly self-managed. That wording conflated the full longitudinal origin endpoint with Tokyo-entry state. v1.1 remains preserved as the historical working ledger; v1.2 is the corrected prospective ledger.

Because a limited portion of the `big4_001` primary opening was inspected to resolve the boundary, BIG4 now carries `CONTROLLED_RECONSTRUCTION_WITH_DISCLOSED_HISTORICAL_AND_PRIMARY_SOURCE_HINDSIGHT`.

### Tranche 08 completed — Tokyo main story

The fourteen Tokyo main-story bundles (69 granular stories / 7,067 utterances) have received full sequential Phase-1B audit.

Canonical artifacts:

- `IDOLY_PRIDE_V2_PHASE1B_IIIX_ORIGIN_CHRONOLOGY_CORRECTION_AND_TOKYO_GATE_REVISION.md`;
- `IDOLY_PRIDE_V2_PHASE1B_IIIX_PRE_TOKYO_BASELINE_v1.1.md`;
- `IDOLY_PRIDE_V2_PHASE1B_TOKYO_MAIN_STORY_PRIMARY_FINDINGS_FREEZE.md`;
- `IDOLY_PRIDE_V2_PHASE1B_TOKYO_MAIN_STORY_AUDIT.md`;
- `IDOLY_PRIDE_V2_PHASE1B_POST_TOKYO_BASELINE.md`.

#### Integrity status

The Tokyo source-native freeze is `CONTROLLED_RECONSTRUCTION_WITH_DISCLOSED_PRIMARY_SOURCE_HINDSIGHT`, not pristine. The earlier IIIX origin pass had exposed concurrent/post-I-UNITY primary material before the IIIX chronology defect was discovered. The corrected v1.1 Tokyo-entry baseline admits only securely pre-Tokyo IIIX stories 01–10. Historical V1 Tokyo analysis remained sealed until after the Tokyo primary-source findings were SHA-256 frozen.

#### Priority/status result

- `tokyo_001_new_wind` through `tokyo_014_with_beyond_the_miracle` -> **CORE / `PASS_B_MAIN_STORY_AUDITED`**.
- No Tokyo bundle is demoted to REDUNDANT.

#### Major tranche findings

- Tokyo scales the franchise problem of self-authorship into institutional governance: legitimate structure enlarges authored choice; illegitimate structure converts people into instruments of externally authored outcomes.
- Makino develops fiduciary authority and explicitly states that idols are not agency tools; the agency should be infrastructure idols can use to shine.
- Hoshimi is better modeled as a relational institution organized around standing, consent, and authored choice than as a simple `family` metaphor.
- Competition remains positively valued when results retain evidentiary meaning; the target of critique is metric sovereignty and institutional capture, not ranking itself.
- SUNNY PEACE develops reciprocal fan/idol recognition as its mature Tokyo philosophy and operationalizes it during the I-UNITY sabotage.
- Tsuki no Tempest converts defeat into moral/professional knowledge; Kotono explicitly states that her idol activity is no longer principally Mana-directed.
- LizNoir regains living rivalry as reciprocal futurity and remains at Hoshimi by choice.
- TRINITYAiLE extends its origin ethic into anti-unilateral-sacrifice and shared standing in collective risk.
- IIIX is neither Himeno puppet nor ethically clean: its core Tokyo failure is responsibility compartmentalization, demanding a fair direct stage while tolerating corruption of the surrounding conditions.
- SUNNY PEACE is explicitly described as going beyond Mana; Mana becomes history and possible supernatural residue rather than terminal horizon.

#### BIG4 integrity warning

During the historical Tokyo stress test, a broad historical-transcript search accidentally surfaced limited high-level V1 BIG4 snippets. During the subsequent chronology-gate repair, a limited opening portion of `big4_001_dark_of_the_moon` was also inspected solely to determine whether IIIX's freelance transition was already past history when BIG4 begins.

The future BIG4 primary-source pass must therefore use `CONTROLLED_RECONSTRUCTION_WITH_DISCLOSED_HISTORICAL_AND_PRIMARY_SOURCE_HINDSIGHT`, restart from the beginning of `big4_001`, and quarantine all further historical BIG4 analysis until its primary findings are frozen.

### Tranche 09 completed — BIG4 main story

The fourteen BIG4 main-story bundles (66 granular stories) have now received full sequential Phase-1B audit from the frozen BIG4-entry baseline.

Canonical artifacts:

- `IDOLY_PRIDE_V2_PHASE1B_BIG4_MAIN_STORY_PRIMARY_FINDINGS_FREEZE.md`;
- `IDOLY_PRIDE_V2_PHASE1B_BIG4_MAIN_STORY_AUDIT.md`;
- `IDOLY_PRIDE_V2_PHASE1B_POST_BIG4_BASELINE.md`.

#### Integrity status

The BIG4 source-native freeze is `CONTROLLED_RECONSTRUCTION_WITH_DISCLOSED_HISTORICAL_AND_PRIMARY_SOURCE_HINDSIGHT`. Limited high-level historical BIG4 material had been exposed during the prior Tokyo stress test, and a localized `big4_001` opening passage had been inspected during the IIIX chronology-gate repair. The formal pass therefore restarted at the first line of `big4_001`, proceeded sequentially through `big4_014`, and SHA-256 froze the source-native findings before any deliberate historical BIG4 comparison.

Primary freeze SHA-256:

`7271a4c1f72b89f196e469ea0dd8adfd0589ad530d68c742d3630acbd3d46317`

#### Priority/status result

- `big4_001_dark_of_the_moon` through `big4_014_epilogue` -> **CORE / `PASS_B_MAIN_STORY_AUDITED`**.
- No BIG4 bundle is demoted to REDUNDANT.
- `big4_013_the_moonlight` retains `AV=Y`; its textual narrative result is frozen, while exact staging/choreography/vocal/music/camera/lighting claims remain routed to the later audiovisual/formal phase.

#### Major tranche findings

- BIG4 is best modeled as **Tsuki no Tempest's constitutional refoundation through distributed personhood**, not merely its promotion to the BIG4 tier.
- Kotono correctly identifies a need for individual growth but overcorrects by equating individuation with severance; her departure produces real gains without being retroactively justified as necessary.
- Nagisa's refusal to follow Kotono turns care into reciprocal equality: she remains attached precisely by becoming capable of saying no and pursuing her own idolhood.
- Four-person Tsuki is a genuine developmental constitution, not a waiting room. It develops Suzu as center, individual member visibility, and a four-storm performance identity.
- Suzu's center arc is explicitly two-stage: she remains formal center during the five-member comeback and lends Kotono one song; only before the decisive DoriKyun battle does she strategically entrust the full center role to Kotono based on tested performance fit. Center becomes a contestable professional office rather than Kotono's permanent property.
- Saki becomes a procedural-care voice; Mei articulates resilience as recoverability after defeat.
- DoriKyun are **adversarial teachers whose diagnosis must be separated from their ethic**. Their critique of industry disposability, agency failure, and the need for strength is partly correct; their elimination doctrine is rejected.
- Tsuki's final moral counterclaim is not anti-competition. It is **competition without ontological erasure**: the winner defeats the rival and then refuses to make losing equivalent to disappearance.
- IIIX's Hoshimi integration advances without sentimental domestication. Miho explicitly begins evaluating Kotono as Kotono rather than only as Mana's sister.
- Makino/Hoshimi again instantiate structured autonomy: real managerial infrastructure and risk governance without producer-authored life choices.
- Mana inheritance is further refracted rather than reproduced: SUNNY's sun and Tsuki's moon become distinct living forms rather than copies of Mana.

#### Historical stress-test corrections

- The older `埋もれたセンター` / "buried center" reading is retained, but explicitly as an interpretation of Kotono's external-evaluation spiral rather than an essentialist textual fact.
- Older wording that Suzu simply "returns the center" to Kotono is split and corrected by the primary chronology.
- "Kotono restored" is replaced by **five-member Tsuki reconstituted**; membership returns, but the internal constitution does not revert.
- Miho's account of DoriKyun's early industry betrayal remains meaningful but preserves its in-world hearsay/inference qualifiers.

#### Post-BIG4 freeze

`IDOLY_PRIDE_V2_PHASE1B_POST_BIG4_BASELINE.md` now governs the next main-story tranche. Stellar may inherit Tsuki's BIG4 status and refounded internal state, SUNNY's existing BIG4 status, IIIX's trial Hoshimi integration, DoriKyun's post-defeat continuation, and the broader Hoshimi structured-autonomy model. It may not import later event/card/message conclusions prospectively.

### Tranche 10 completed — Stellar main story

The eleven Stellar main-story bundles have now received full sequential Phase-1B audit from the frozen post-BIG4 baseline, covering **56 granular stories / 6,301 utterances**. The source-native finding set was written and SHA-256 frozen before the historical Stellar analysis was deliberately opened.

Canonical artifacts:

- `IDOLY_PRIDE_V2_PHASE1B_STELLAR_MAIN_STORY_PRIMARY_FINDINGS_FREEZE.md`;
- `IDOLY_PRIDE_V2_PHASE1B_STELLAR_MAIN_STORY_AUDIT.md`;
- `IDOLY_PRIDE_V2_PHASE1B_POST_STELLAR_BASELINE.md`.

#### Integrity status

The Stellar pass is `PRIMARY_FINDINGS_FROZEN_BEFORE_HISTORICAL_STELLAR_COMPARISON`. No deliberate historical Stellar prose or later event/card/bond/message material was consulted until the independent primary finding set had been frozen.

Primary freeze SHA-256:

`a5dfbd0f0ca7d5e3c12fa1a22206315c0f4b861914ebbf286d320b474b761cc1`

#### Priority/status result

- `stellar_001_to_soar_high` through `stellar_011_all_my_youth` -> **CORE / `PASS_B_MAIN_STORY_AUDITED`**.
- No Stellar bundle is demoted to REDUNDANT.
- `stellar_011_all_my_youth` retains `AV=Y` because `adv-live-main-cmn-03-01-53` is absent from the processed asset layer; textual outcomes are frozen while detailed final-live formal analysis remains routed to the audiovisual phase.

#### Major tranche findings

- Stellar generalizes BIG4's reciprocal-dependence lesson across the whole Hoshimi competitive system. Its major movement is **protection -> supported risk; technical perfection -> authored purpose; victory as proof -> competition as reciprocal development; inherited miracle -> living continuation**.
- Hoshimi becomes a nationally legible plural professional home/platform. Family-like language is meaningful, but institutional legitimacy comes from making different authored forms of idolhood materially possible rather than from emotional uniformity.
- Makino's current best managerial model is **risk-aware co-authorship**: discover the idol's authored aim, make risks legible, build medical/logistical/staff support, and resist both fear-driven confiscation of choice and laissez-faire abandonment. Sakura's semifinal remains an ethically difficult stress case rather than a solved formula.
- SUNNY PEACE explicitly becomes a five-person burden-sharing constitution. Sakura's Mana inheritance recurs not as identity replacement but as a dangerous professional ethic in which singular audience opportunity can become a claim on bodily availability.
- Sakura's heartbeat/performance surge remains `CONFLICT / AMBIGUITY`; Kotono rejects a simple Mana-rescue account, but the main story does not require a fully non-supernatural explanation. Mana increasingly functions as witness/inheritance rather than causal sovereign.
- TRINITYAiLE's missing `核` becomes source-explicit `恩返し`: reciprocal gratitude converted into propulsion. The unit recognizes `私達は、私達だけじゃ高く飛べない`, distributes leadership responsibility, reconciles Rui's father/president conflict through explicit communication, and wins the VENUS Grand Prix without treating victory as final summit status.
- IIIX deliberately attempts its first `完璧ではないステージ`, converting internal rivalry and controlled imperfection into performance resources while retaining `絶対勝利` and hostile intimacy.
- LizNoir's four-person present is explicitly affirmed as non-substitutable and its horizon expands beyond Mana and one domestic tournament.
- Tsuki no Tempest's BIG4 constitutional refoundation survives new pressure and carries the unit to the Grand Prix final.
- DoriKyun remains external and hostile while expanding from pure elimination toward adversarial cultivation of already-serious opponents.
- The Grand Prix refuses terminal ranking: winners and losers retain rematches, experiments, global horizons and continued futures. Competition remains real without becoming ontological jurisdiction over who deserves to continue.
- `青春全部かけて` must be read with the same ending's explicit **twenty-/thirty-year professional horizon**. Stellar celebrates total commitment while refusing to equate youth with self-annihilation.
- The epilogue's new aspirants and audition convert inheritance into new self-authored desire rather than another attempt to reproduce Mana.

#### Historical stress-test corrections

- The earlier "cost of altitude" and "constellation" readings are retained and strengthened.
- Historical wording that Sakura's semifinal defeat "saved her from burning herself to death" is **WEAKENED / QUALIFIED**. The primary text establishes serious future-career risk and Rui's candle metaphor, but also present medical clearance and safeguards. Defeat creates recovery time; it does not retroactively prove the risky choice was right or establish imminent death.
- Historical wording that mature Makino simply "intervenes when bodies are at risk and otherwise trusts" is **QUALIFIED**. Stellar instead presents a negotiated risk zone in which intervention, clearance, safeguards, and authored desire coexist.
- "Gratitude defeats calculation" is **QUALIFIED**. Both TRINITYAiLE and IIIX are technically elite; IIIX deliberately experiments beyond calculation in the same match.
- `恩返し` is governed as reciprocal gratitude rather than servile debt/obligation.
- Historical language that the final makes TRINITYAiLE the ultimate idol group is rejected by Rui's explicit refusal of finality.
- "Mana's miracle has finally become a sky" is retained as a high-value **INTERPRETATION**, not textual fact.

#### Post-Stellar freeze

`IDOLY_PRIDE_V2_PHASE1B_POST_STELLAR_BASELINE.md` now freezes the endpoint of the complete currently catalogued game main-story spine. Lower-tier sources must not be allowed to retroactively rewrite that endpoint before the Tier-A consolidation audit.

### Main-story completion checkpoint — Tier-A consolidation COMPLETE

All **63 game main-story bundles**, all **33 unit-origin bundles**, and the frozen **12-episode anime endpoint** have now been cross-reconciled in:

`IDOLY_PRIDE_V2_PHASE1B_TIER_A_MAIN_NARRATIVE_CONSOLIDATION_AUDIT.md`

The audit freezes the main-narrative architecture before lower-tier material is permitted to modify it. Its principal cross-arc result is that the historical **inheritance-after-miracle** thesis remains foundational but broadens into a more general problem of **answerable interdependence and authorship**: the narrative repeatedly asks how a life can be shaped by the dead, attachments, institutions, rivals, audiences, gratitude, and professional risk without granting any one of those forces unilateral jurisdiction over what that life is for.

The audit also freezes:

- the anime/game Hoshimi continuity-variant rule;
- the IIIX chronology partition;
- complete Tier-A character, unit, relationship, institution, and thematic endpoint matrices;
- a V1 master-claim revision table;
- a 20-item unresolved/conflict register;
- explicit audiovisual backfill routes;
- lower-tier update classes and anti-backfill rules;
- event-reranking criteria.

The compact implementation baseline is:

`IDOLY_PRIDE_V2_PHASE1B_POST_TIER_A_MAIN_NARRATIVE_BASELINE.md`

**Event rerank gate: OPEN.**

No event priority in the exhaustive table below has been silently rewritten by the consolidation audit. Existing event labels remain Pass-A/provisional until the independent 60-event rerank is performed.

### Next semantic tranches — active Phase 1B dependency sequence

**Tier-A main narrative: COMPLETE AND CONSOLIDATED.**

1. full independent re-ranking of all **60 event bundles** against `IDOLY_PRIDE_V2_PHASE1B_POST_TIER_A_MAIN_NARRATIVE_BASELINE.md`;
2. event close reading in the resulting priority/chronology order;
3. bond/special/card/message sampling and escalation against the updated longitudinal model;
4. later audiovisual/music/visual formal backfill per the dedicated architecture.

## 6. Full bundle ledger

The table below is exhaustive at the bundle/episode level. `H` shows the historical curated-event label, if any. `AV` marks formal/audiovisual review requirements. `Status` distinguishes provisional source-class triage from manually reviewed entries.

### main_story

| Item ID | Title | Priority | Status | H | AV | Stories |
|---|---|---|---|---|:---:|---:|
| `hoshimi_001_shine_purity` | Shine Purity | `CORE` | `PASS_B_CROSS_MEDIA_AUDITED` | — |  | 6 |
| `hoshimi_002_short_goodbye` | Short Goodbye | `CORE` | `PASS_B_CROSS_MEDIA_AUDITED` | — |  | 5 |
| `hoshimi_003_like_the_sun_moon` | like the Sun/Moon | `CORE` | `PASS_B_CROSS_MEDIA_AUDITED` | — |  | 5 |
| `hoshimi_004_strange_one` | Strange One | `CORE` | `PASS_B_CROSS_MEDIA_AUDITED` | — |  | 5 |
| `hoshimi_005_the_sun_moon_and_stars` | The Sun, Moon and Stars | `CORE` | `PASS_B_CROSS_MEDIA_AUDITED` | — |  | 7 |
| `hoshimi_006_to_trust_one` | to Trust One | `CORE` | `PASS_B_CROSS_MEDIA_AUDITED` | — |  | 5 |
| `hoshimi_007_drop_of_smile` | Drop of Smile | `CORE` | `PASS_B_CROSS_MEDIA_AUDITED` | — |  | 5 |
| `hoshimi_008_make_up_her_mind` | Make up her Mind | `CORE` | `PASS_B_CROSS_MEDIA_AUDITED` | — |  | 5 |
| `hoshimi_009_with_a_will` | With a Will | `CORE` | `PASS_B_CROSS_MEDIA_AUDITED` | — |  | 5 |
| `hoshimi_010_proud_lady` | Proud Lady | `CORE` | `PASS_B_CROSS_MEDIA_AUDITED` | — |  | 5 |
| `hoshimi_011_resolution` | Resolution | `CORE` | `PASS_B_CROSS_MEDIA_AUDITED` | — |  | 5 |
| `hoshimi_012_dear_my_sister_part_01` | Dear My Sister (Part 1) | `CORE` | `PASS_B_CROSS_MEDIA_AUDITED` | — |  | 7 |
| `hoshimi_012_dear_my_sister_part_02` | Dear My Sister (Part 2) | `CORE` | `PASS_B_CROSS_MEDIA_AUDITED` | — |  | 2 |
| `hoshimi_013_sunlight` | Sunlight | `CORE` | `PASS_B_CROSS_MEDIA_AUDITED` | — |  | 6 |
| `hoshimi_014_successor_of_miracle` | Successor of Miracle | `CORE` | `PASS_B_CROSS_MEDIA_AUDITED` | — |  | 5 |
| `hoshimi_015_sorrows_of_orpheus` | Sorrows of Orpheus | `CORE` | `PASS_B_CROSS_MEDIA_AUDITED` | — |  | 5 |
| `hoshimi_016_cherry_worry` | Cherry,Worry | `CORE` | `PASS_B_CROSS_MEDIA_AUDITED` | — |  | 5 |
| `hoshimi_017_beat_meets` | Beat Meets | `CORE` | `PASS_B_CROSS_MEDIA_AUDITED` | — |  | 5 |
| `hoshimi_018_idoly_pride` | Idoly Pride | `CORE` | `PASS_B_CROSS_MEDIA_AUDITED` | — |  | 5 |
| `hoshimi_019_still_live` | Still Live | `CORE` | `PASS_B_CROSS_MEDIA_AUDITED` | — |  | 5 |
| `hoshimi_020_on_my_way` | on My Way | `CORE` | `PASS_B_CROSS_MEDIA_AUDITED` | — |  | 5 |
| `hoshimi_021_glory_days` | Glory Days | `CORE` | `PASS_B_CROSS_MEDIA_AUDITED` | — |  | 5 |
| `hoshimi_022_last_step` | Last Step | `CORE` | `PASS_B_CROSS_MEDIA_AUDITED` | — |  | 5 |
| `hoshimi_023_pray_for_you` | Pray for you | `CORE` | `PASS_B_CROSS_MEDIA_AUDITED` | — |  | 4 |
| `tokyo_001_new_wind` | New Wind | `CORE` | `PASS_B_MAIN_STORY_AUDITED` | — |  | 5 |
| `tokyo_002_stray_wings` | Stray Wings | `CORE` | `PASS_B_MAIN_STORY_AUDITED` | — |  | 5 |
| `tokyo_003_shiny_melody` | Shiny Melody | `CORE` | `PASS_B_MAIN_STORY_AUDITED` | — |  | 5 |
| `tokyo_004_wear_feathers` | Wear Feathers | `CORE` | `PASS_B_MAIN_STORY_AUDITED` | — |  | 5 |
| `tokyo_005_black_impact` | Black Impact | `CORE` | `PASS_B_MAIN_STORY_AUDITED` | — |  | 5 |
| `tokyo_006_farewell_and_oath` | Farewell and Oath | `CORE` | `PASS_B_MAIN_STORY_AUDITED` | — |  | 5 |
| `tokyo_007_struggle_for_idols` | Struggle for IDOLs | `CORE` | `PASS_B_MAIN_STORY_AUDITED` | — |  | 5 |
| `tokyo_008_enjoy_just_purely` | Enjoy just purely | `CORE` | `PASS_B_MAIN_STORY_AUDITED` | — |  | 5 |
| `tokyo_009_no_gray` | No Gray | `CORE` | `PASS_B_MAIN_STORY_AUDITED` | — |  | 5 |
| `tokyo_010_cold_diamond` | Cold Diamond | `CORE` | `PASS_B_MAIN_STORY_AUDITED` | — |  | 5 |
| `tokyo_011_moonlight_in_our_hands` | Moonlight In Our Hands | `CORE` | `PASS_B_MAIN_STORY_AUDITED` | — |  | 5 |
| `tokyo_012_what_is_idol` | What is ”IDOL”? | `CORE` | `PASS_B_MAIN_STORY_AUDITED` | — |  | 5 |
| `tokyo_013_may_the_sunshine_be_with_you` | May the Sunshine be with you | `CORE` | `PASS_B_MAIN_STORY_AUDITED` | — |  | 5 |
| `tokyo_014_with_beyond_the_miracle` | [With/Beyond] the Miracle | `CORE` | `PASS_B_MAIN_STORY_AUDITED` | — |  | 4 |
| `big4_001_dark_of_the_moon` | Dark Of the Moon | `CORE` | `PASS_B_MAIN_STORY_AUDITED` | — |  | 5 |
| `big4_002_cloudy_road_ahead` | Cloudy Road Ahead | `CORE` | `PASS_B_MAIN_STORY_AUDITED` | — |  | 5 |
| `big4_003_adventure_of_life` | Adventure Of Life | `CORE` | `PASS_B_MAIN_STORY_AUDITED` | — |  | 5 |
| `big4_004_decision_of_the_underdogs` | Decision Of The Underdogs | `CORE` | `PASS_B_MAIN_STORY_AUDITED` | — |  | 5 |
| `big4_005_goodbye_to_the_moon` | Goodbye To The Moon | `CORE` | `PASS_B_MAIN_STORY_AUDITED` | — |  | 5 |
| `big4_006_choice_of_destiny` | Choice of Destiny | `CORE` | `PASS_B_MAIN_STORY_AUDITED` | — |  | 5 |
| `big4_007_new_moon_new_bright` | New moon, New bright | `CORE` | `PASS_B_MAIN_STORY_AUDITED` | — |  | 5 |
| `big4_008_keep_going` | Keep going | `CORE` | `PASS_B_MAIN_STORY_AUDITED` | — |  | 5 |
| `big4_009_battle_again` | Battle again | `CORE` | `PASS_B_MAIN_STORY_AUDITED` | — |  | 5 |
| `big4_010_goodbye_to_the_darkness` | Goodbye To The Darkness | `CORE` | `PASS_B_MAIN_STORY_AUDITED` | — |  | 5 |
| `big4_011_back_of_entertainment` | Back Of Entertainment | `CORE` | `PASS_B_MAIN_STORY_AUDITED` | — |  | 5 |
| `big4_012_illuminate` | Illuminate | `CORE` | `PASS_B_MAIN_STORY_AUDITED` | — |  | 5 |
| `big4_013_the_moonlight` | The Moonlight | `CORE` | `PASS_B_MAIN_STORY_AUDITED` | — | Y | 5 |
| `big4_014_epilogue` | Epilogue | `CORE` | `PASS_B_MAIN_STORY_AUDITED` | — |  | 1 |
| `stellar_001_to_soar_high` | To Soar High | `CORE` | `PASS_B_MAIN_STORY_AUDITED` | — |  | 5 |
| `stellar_002_nemophila` | Nemophila | `CORE` | `PASS_B_MAIN_STORY_AUDITED` | — |  | 5 |
| `stellar_003_to_fly_higher` | To Fly Higher | `CORE` | `PASS_B_MAIN_STORY_AUDITED` | — |  | 5 |
| `stellar_004_hoshimi_s_festival` | Hoshimi's Festival | `CORE` | `PASS_B_MAIN_STORY_AUDITED` | — |  | 5 |
| `stellar_005_we_are_the_sun` | We Are The Sun | `CORE` | `PASS_B_MAIN_STORY_AUDITED` | — |  | 5 |
| `stellar_006_will_of_the_underdogs` | Will Of The Underdogs | `CORE` | `PASS_B_MAIN_STORY_AUDITED` | — |  | 5 |
| `stellar_007_repaying_kindness` | Repaying Kindness | `CORE` | `PASS_B_MAIN_STORY_AUDITED` | — |  | 5 |
| `stellar_008_opening_of_grand_prix` | Opening of Grand Prix | `CORE` | `PASS_B_MAIN_STORY_AUDITED` | — |  | 5 |
| `stellar_009_challenge_for_friend` | Challenge for Friend | `CORE` | `PASS_B_MAIN_STORY_AUDITED` | — |  | 5 |
| `stellar_010_miraculous_beat` | Miraculous Beat | `CORE` | `PASS_B_MAIN_STORY_AUDITED` | — |  | 5 |
| `stellar_011_all_my_youth` | All My Youth | `CORE` | `PASS_B_MAIN_STORY_AUDITED` | — | Y | 6 |

### unit_origins

| Item ID | Title | Priority | Status | H | AV | Stories |
|---|---|---|---|---|:---:|---:|
| `origin_mna_001_first_step` | Mana: First Step | `FOUNDATIONAL` | `PASS_B_FOUNDATIONAL_REVIEWED` | — |  | 5 |
| `origin_mna_002_trajectory_of_miracle` | Mana: Trajectory of Miracle | `FOUNDATIONAL` | `PASS_B_FOUNDATIONAL_REVIEWED` | — |  | 5 |
| `origin_mna_003_goodbye_to_goodbye` | Mana: Goodbye to Goodbye | `FOUNDATIONAL` | `PASS_B_FOUNDATIONAL_REVIEWED` | — |  | 5 |
| `origin_sun_001_chisa_s_memories` | SUNNY PEACE: Chisa's Memories | `CORE` | `PASS_B_ORIGIN_AUDITED` | — |  | 5 |
| `origin_sun_002_rei_s_memories` | SUNNY PEACE: Rei's Memories | `CORE` | `PASS_B_ORIGIN_AUDITED` | — |  | 5 |
| `origin_sun_003_shizuku_s_memories` | SUNNY PEACE: Shizuku's Memories | `CORE` | `PASS_B_ORIGIN_AUDITED` | — |  | 5 |
| `origin_sun_004_haruko_s_memories` | SUNNY PEACE: Haruko's Memories | `CORE` | `PASS_B_ORIGIN_AUDITED` | — |  | 5 |
| `origin_sun_005_sakura_s_memories` | SUNNY PEACE: Sakura's Memories | `CORE` | `PASS_B_ORIGIN_AUDITED` | — |  | 5 |
| `origin_moon_001_saki_s_memories` | Tsuki no Tempest: Saki's Memories | `CORE` | `PASS_B_ORIGIN_AUDITED` | — |  | 5 |
| `origin_moon_002_suzu_s_memories` | Tsuki no Tempest: Suzu's Memories | `CORE` | `PASS_B_ORIGIN_AUDITED` | — |  | 5 |
| `origin_moon_003_mei_s_memories` | Tsuki no Tempest: Mei's Memories | `CORE` | `PASS_B_ORIGIN_AUDITED` | — |  | 5 |
| `origin_moon_004_nagisa_s_memories` | Tsuki no Tempest: Nagisa's Memories | `CORE` | `PASS_B_ORIGIN_AUDITED` | — |  | 5 |
| `origin_moon_005_kotono_s_memories` | Tsuki no Tempest: Kotono's Memories | `CORE` | `PASS_B_ORIGIN_AUDITED` | — |  | 5 |
| `origin_tri_001_white_resolve` | TRINITYAiLE: White Resolve | `CORE` | `PASS_B_ORIGIN_AUDITED` | — |  | 5 |
| `origin_tri_002_shoot_for_the_sky` | TRINITYAiLE: Shoot for the Sky | `CORE` | `PASS_B_ORIGIN_AUDITED` | — |  | 5 |
| `origin_tri_003_light_my_fire` | TRINITYAiLE: Light My Fire | `CORE` | `PASS_B_ORIGIN_AUDITED` | — |  | 5 |
| `origin_tri_004_r_aliser` | TRINITYAiLE: Réaliser | `CORE` | `PASS_B_ORIGIN_AUDITED` | — |  | 5 |
| `origin_tri_005_because_sisters` | TRINITYAiLE: because  sisters | `CORE` | `PASS_B_ORIGIN_AUDITED` | — |  | 5 |
| `origin_tri_006_violette_blooming_proudly` | TRINITYAiLE: Violette blooming proudly | `CORE` | `PASS_B_ORIGIN_AUDITED` | — |  | 5 |
| `origin_liz_001_a_budding_lily` | LizNoir: a Budding Lily | `CORE` | `PASS_B_ORIGIN_AUDITED` | — |  | 5 |
| `origin_liz_002_one_more_dream` | LizNoir: One more dream | `CORE` | `PASS_B_ORIGIN_AUDITED` | — |  | 5 |
| `origin_liz_003_impatience_of_hollyhock` | LizNoir: Impatience of Hollyhock | `CORE` | `PASS_B_ORIGIN_AUDITED` | — |  | 5 |
| `origin_liz_004_love_heart` | LizNoir: Love & Heart | `CORE` | `PASS_B_ORIGIN_AUDITED` | — |  | 5 |
| `origin_liz_005_smile_or_perfect_performance` | LizNoir: Smile or Perfect performance | `CORE` | `PASS_B_ORIGIN_AUDITED` | — |  | 5 |
| `origin_liz_006_brand-new_liznoir` | LizNoir: Brand-new LizNoir | `CORE` | `PASS_B_ORIGIN_AUDITED` | — |  | 5 |
| `origin_liz_007_black_lily_in_the_storm` | LizNoir: Black Lily in the Storm | `CORE` | `PASS_B_ORIGIN_AUDITED` | — |  | 5 |
| `origin_liz_008_the_road_of_battle` | LizNoir: The Road Of Battle | `CORE` | `PASS_B_ORIGIN_AUDITED` | — |  | 5 |
| `origin_liz_009_the_beginning_venus` | LizNoir: The Beginning Venus | `CORE` | `PASS_B_ORIGIN_AUDITED` | — |  | 1 |
| `origin_liz_010_kokoro_ai_s_memories` | LizNoir: Kokoro & Ai's Memories | `CORE` | `PASS_B_ORIGIN_AUDITED` | — |  | 2 |
| `origin_thrx_001_diamond_mining` | IIIX: Diamond Mining | `CORE` | `PASS_B_ORIGIN_AUDITED` | — |  | 5 |
| `origin_thrx_002_house_of_cards` | IIIX: House Of Cards | `CORE` | `PASS_B_ORIGIN_AUDITED` | — |  | 5 |
| `origin_thrx_003_gears_go_awry` | IIIX: Gears Go Awry | `CORE` | `PASS_B_ORIGIN_AUDITED` | — |  | 5 |
| `origin_thrx_004_re-polished` | IIIX: Re-Polished | `CORE` | `PASS_B_ORIGIN_AUDITED` | — |  | 5 |

### events

| Item ID | Title | Priority | Status | H | AV | Stories |
|---|---|---|---|---|:---:|---:|
| `event_2021_001_st-eve-2107-tour` | 雨上がりの太陽と共に | `SUPPORT` | `PASS_B_EVENT_E3_AUDITED` | IMPORTANT |  | 5 |
| `event_2021_002_st-eve-2108-tour` | 月夜に輝く恋の魔法 | `SUPPORT` | `PASS_B_EVENT_E4_AUDITED` | IMPORTANT |  | 5 |
| `event_2021_003_st-eve-2109-backside` | 芽吹く黒ユリの蕾 | `IMPORTANT` | `PASS_B_EVENT_E2A2_AUDITED` | IMPORTANT |  | 5 |
| `event_2021_004_st-eve-2110-marathon` | 煌めく奇跡をもう一度 | `CORE` | `PASS_B_EVENT_E1A_AUDITED` | IMPORTANT |  | 6 |
| `event_2021_005_st-eve-2111-backside` | 夢踊るステージに架け橋を | `IMPORTANT` | `PASS_B_EVENT_E2A1_AUDITED` | IMPORTANT |  | 5 |
| `event_2021_006_st-eve-2112-marathon` | 羽休む聖夜のサプライズ | `IMPORTANT` | `PASS_B_EVENT_E2A2_AUDITED` | IMPORTANT |  | 5 |
| `event_2022_001_st-eve-2201-contest` | 昇る初陽に咲く笑顔 | `SUPPORT` | `PASS_B_EVENT_E3_AUDITED` | IMPORTANT |  | 5 |
| `event_2022_002_st-eve-2202-marathon` | 心愛溶けるビターチョコレート | `IMPORTANT` | `PASS_B_EVENT_E2B1_AUDITED` | IMPORTANT |  | 5 |
| `event_2022_003_st-eve-2203-race` | 並び立つ歌姫のフルリール | `IMPORTANT` | `PASS_B_EVENT_E2A1_AUDITED` | IMPORTANT |  | 6 |
| `event_2022_004_st-eve-2204-contest` | 愛歌う星の継承者 | `SUPPORT` | `PASS_B_EVENT_SUPPORT_DEFERRED_AUDITED` | CORE |  | 6 |
| `event_2022_005_st-eve-2205-race` | 心紡ぎ合う輝きの競演 | `IMPORTANT` | `PASS_B_EVENT_E2B2_AUDITED` | CORE |  | 5 |
| `event_2022_006_st-eve-2206-marathon` | 導きのファンファーレ | `SUPPORT` | `PASS_B_EVENT_E3_AUDITED` | IMPORTANT |  | 5 |
| `event_2022_007_st-eve-2207-contest` | Happy Smile Selfie | `CORE` | `PASS_B_EVENT_E1A_AUDITED` | CORE |  | 5 |
| `event_2022_008_st-eve-2208-backside` | 熱中☆ハプニングサマー | `SUPPORT` | `PASS_B_EVENT_E3_AUDITED` | IMPORTANT |  | 5 |
| `event_2022_009_st-eve-2209-contest` | 未来とつながるマジカルメロディ | `LOW` | `PASS_B_EVENT_E4_CAVEATED_AUDITED` | IMPORTANT | Y | 5 |
| `event_2022_010_st-eve-2210-race` | 運命繋ぐ流星の軌跡 | `CORE` | `PASS_B_EVENT_E1A_AUDITED` | CORE | Y | 5 |
| `event_2022_011_st-eve-2211-marathon-raid` | 舌戦開幕！賛美の湯 | `SUPPORT` | `PASS_B_EVENT_SUPPORT_DEFERRED_AUDITED` | CORE |  | 5 |
| `event_2022_012_st-eve-2212-race` | 君と願う月灯の祝祭 | `SUPPORT` | `PASS_B_EVENT_SUPPORT_DEFERRED_AUDITED` | CORE | Y | 5 |
| `event_2023_001_st-eve-2301-contest` | 最高優美＊飛躍のカウントダウン | `IMPORTANT` | `PASS_B_EVENT_E2B1_AUDITED` | IMPORTANT | Y | 5 |
| `event_2023_002_st-eve-2302-marathon-raid` | 守れ！純潔のベーゼ～imposition of love～ | `SUPPORT` | `PASS_B_EVENT_E3_AUDITED` | IMPORTANT |  | 5 |
| `event_2023_003_st-eve-2303-race` | ぱじゃまパーティー！～夢見る少女と眠り姫～ | `SUPPORT` | `PASS_B_EVENT_E3_AUDITED` | IMPORTANT | Y | 5 |
| `event_2023_004_st-eve-2304-marathon-raid` | 音色の輝石が紡ぐ未来 | `IMPORTANT` | `PASS_B_EVENT_E2C1_AUDITED` | CORE |  | 5 |
| `event_2023_005_st-eve-2305-race` | きょうえん！HTT＆HMA～放課後ティータイム＆星見アンバサダー～ | `LOW` | `PASS_B_EVENT_E4_CAVEATED_AUDITED` | — |  | 3 |
| `event_2023_006_st-eve-2306-contest` | 星々が奇跡と叶える約束の未来 | `CORE` | `PASS_B_EVENT_E1A_AUDITED` | CORE |  | 5 |
| `event_2023_007_st-eve-2307-race` | 灼熱のBEACH ～イライラMAX ⅢX～ | `SUPPORT` | `PASS_B_EVENT_SUPPORT_DEFERRED_AUDITED` | IMPORTANT | Y | 5 |
| `event_2023_008_st-eve-2308-marathon-raid` | おしごとシークレット | `IMPORTANT` | `PASS_B_EVENT_E2A3_AUDITED` | IMPORTANT | Y | 5 |
| `event_2023_009_st-eve-2309-backside` | 遥か頂に向かう秀麗 | `CORE` | `PASS_B_EVENT_E1B_AUDITED` | CORE | Y | 5 |
| `event_2023_010_st-eve-2310-race` | 迷走ピリオド 涼やかな青春 | `IMPORTANT` | `PASS_B_EVENT_E2B2_AUDITED` | IMPORTANT |  | 5 |
| `event_2023_011_st-eve-2311-marathon-raid` | 翔けぬけるVictoire　誓いのplume | `CORE` | `PASS_B_EVENT_E1B_AUDITED` | CORE | Y | 5 |
| `event_2023_012_st-eve-2312-contest` | 君と輝くサンシャイン!! | `LOW` | `PASS_B_EVENT_E4_CAVEATED_AUDITED` | IMPORTANT | Y | 5 |
| `event_2024_001_st-eve-2401-race` | にゃんか不思議なお正月！？ | `SUPPORT` | `PASS_B_EVENT_E4_AUDITED` | — |  | 5 |
| `event_2024_002_st-eve-2402-contest` | 未来を彩るスノーフェスティバル | `LOW` | `PASS_B_EVENT_E4_CAVEATED_AUDITED` | IMPORTANT | Y | 5 |
| `event_2024_003_st-eve-2403-race` | 笑顔のSUNNY 繋げるPEACE | `IMPORTANT` | `PASS_B_EVENT_E2B2_AUDITED` | CORE | Y | 5 |
| `event_2024_004_st-eve-2404-dice` | 不屈のChallenger～Roll the dice～ | `IMPORTANT` | `PASS_B_EVENT_E2C1_AUDITED` | IMPORTANT | Y | 5 |
| `event_2024_005_st-eve-2405-race` | すれ違いのディソナンス | `CORE` | `PASS_B_EVENT_E1B_AUDITED` | CORE | Y | 5 |
| `event_2024_006_st-eve-2406-contest` | 君を照らすムーンライトロード | `CORE` | `PASS_B_EVENT_E1B_AUDITED` | CORE |  | 5 |
| `event_2024_007_st-eve-2407-dice` | 漕ぎ出せ！アイドル★サバイバーズ | `IMPORTANT` | `PASS_B_EVENT_E2A1_AUDITED` | CORE |  | 5 |
| `event_2024_008_st-eve-2408-race` | 偽りのREALISM ～密着 新曲会議！？～ | `CORE` | `PASS_B_EVENT_E1C_AUDITED` | CORE | Y | 5 |
| `event_2024_009_st-eve-2409-marathon-raid` | 開演！ぷりてぃー★エンジェル | `IMPORTANT` | `PASS_B_EVENT_E2A3_AUDITED` | IMPORTANT |  | 5 |
| `event_2024_010_st-eve-2410-dice` | お待たせしました里帰り～星見凱旋記～ | `CORE` | `PASS_B_EVENT_E1C_AUDITED` | CORE | Y | 5 |
| `event_2024_011_st-eve-2411-race` | 欺瞞の最強TWINkle | `CORE` | `PASS_B_EVENT_E1C_AUDITED` | CORE | Y | 5 |
| `event_2024_012_st-eve-2412-contest` | 心跳ねるクリスマスパーティー | `LOW` | `PASS_B_EVENT_E4_CAVEATED_AUDITED` | — | Y | 5 |
| `event_2025_001_st-eve-2501-race` | 迎春！翼に込める躍進の一念 | `IMPORTANT` | `PASS_B_EVENT_E2B2_AUDITED` | CORE |  | 5 |
| `event_2025_002_st-eve-2502-marathon-raid` | 感謝を伝えるLovely Valentine's Day | `SUPPORT` | `PASS_B_EVENT_E3_AUDITED` | IMPORTANT | Y | 5 |
| `event_2025_003_st-eve-2503-dice` | SOS！星見プロダクションの転送～ただのアイドルには興味ありません！？～ | `LOW` | `PASS_B_EVENT_E4_CAVEATED_AUDITED` | — |  | 3 |
| `event_2025_004_st-eve-2504-marathon-raid` | 旗揚げ！劇団★見～二人のアリスとWONDERLAND～ | `IMPORTANT` | `PASS_B_EVENT_E2B1_AUDITED` | CORE |  | 5 |
| `event_2025_005_st-eve-2507-free` | st-eve-2507-free | `CORE` | `PASS_B_EVENT_E1D_AUDITED` | CORE |  | 5 |
| `event_2025_006_st-eve-2507-race` | 星見プロ全国ツアー　Stars Journey | `IMPORTANT` | `PASS_B_EVENT_E2A3_AUDITED` | CORE |  | 5 |
| `event_2025_007_st-eve-2508-free` | st-eve-2508-free | `CORE` | `PASS_B_EVENT_E1D_AUDITED` | CORE | Y | 5 |
| `event_2025_008_st-eve-2509-contest` | 未来へ続く夏祭り | `LOW` | `PASS_B_EVENT_E4_CAVEATED_AUDITED` | IMPORTANT | Y | 5 |
| `event_2025_009_st-eve-2510-marathon-raid` | 私達の青春謳歌～DOTABATA SCHOOL FESTIVAL～ | `IMPORTANT` | `PASS_B_EVENT_E2A3_AUDITED` | IMPORTANT | Y | 5 |
| `event_2025_010_st-eve-2511-race` | let's 湯けむり dancing！ | `IMPORTANT` | `PASS_B_EVENT_E2A2_AUDITED` | CORE |  | 5 |
| `event_2025_011_st-eve-2512-dice` | ドタバタ！？トラブルクリスマス！ | `LOW` | `PASS_B_EVENT_E4_CAVEATED_AUDITED` | — |  | 3 |
| `event_2026_001_st-eve-2601-race` | 新春万福　素顔の晒し合いGAME | `IMPORTANT` | `PASS_B_EVENT_E2B1_AUDITED` | CORE | Y | 5 |
| `event_2026_002_st-eve-2602-dice` | ぶつかり愛のCenter Battle！ | `CORE` | `PASS_B_EVENT_E1E_AUDITED` | CORE | Y | 5 |
| `event_2026_003_st-eve-2603-race` | あなたに捧ぐWith your songs | `CORE` | `PASS_B_EVENT_E1E_AUDITED` | CORE | Y | 5 |
| `event_2026_004_st-eve-2604-dice` | IDOLY MATCH～地下闘技場への挑戦～ | `IMPORTANT` | `PASS_B_EVENT_E2A1_AUDITED` | IMPORTANT | Y | 5 |
| `event_2026_005_st-eve-2605-marathon-raid` | ハロー！アイドル♪ 夢でつながるミラクルステージ | `LOW` | `PASS_B_EVENT_E4_CAVEATED_AUDITED` | IMPORTANT |  | 3 |
| `event_2026_006_st-eve-2606-dice` | 羽ばたけ！恩返しのAile | `IMPORTANT` | `PASS_B_EVENT_E2A2_AUDITED` | — | Y | 5 |
| `event_2026_007_st-eve-2607-marathon-raid` | PRIDE貫く頂点への道標 | `CORE` | `PASS_B_EVENT_E1E_AUDITED` | — |  | 5 |

## 10.8 Event rerank freeze — 2026-08-15

The 60-event rerank is complete. Tier distribution: **E1/CORE 16; E2/IMPORTANT 26; E3/SUPPORT 7; E4/LOW-DELTA OR CAVEATED 11**.

Governing artifacts:

- `IDOLY_PRIDE_V2_PHASE1B_EVENT_RERANK_AUDIT.md`
- `IDOLY_PRIDE_V2_PHASE1B_EVENT_CLOSE_READ_QUEUE.md`
- `IDOLY_PRIDE_V2_PHASE1B_EVENT_RERANK_SHA256SUMS.txt`

The event table below now uses the V2 rerank in `Priority`. The historical `H` column remains frozen provenance and **must not be read as current priority**. No event findings have yet been admitted to the Tier-A baseline.

### bond_stories

| Item ID | Title | Priority | Status | H | AV | Stories |
|---|---|---|---|---|:---:|---:|
| `bond_ai_001_ai` | Bond stories: ai | `TEXTURE` | `PHASE1_BOND_RERANKED_TEXTURE_INDEXED` | — |  | 8 |
| `bond_aoi_001_aoi` | Bond stories: aoi | `SUPPORT` | `PHASE1_BOND_RERANKED_SUPPORT_MINING` | — |  | 8 |
| `bond_chs_001_chs` | Bond stories: chs | `SUPPORT` | `PHASE1_BOND_RERANKED_SUPPORT_MINING` | — |  | 8 |
| `bond_hrk_001_hrk` | Bond stories: hrk | `IMPORTANT` | `PASS_PHASE1_BOND_B2B_AUDITED` | — |  | 8 |
| `bond_kan_001_kan` | Bond stories: kan | `CORE` | `PASS_PHASE1_BOND_B1A_AUDITED` | — |  | 8 |
| `bond_kkr_001_kkr` | Bond stories: kkr | `SUPPORT` | `PHASE1_BOND_RERANKED_SUPPORT_MINING` | — |  | 8 |
| `bond_kor_001_kor` | Bond stories: kor | `CORE` | `PASS_PHASE1_BOND_B1A_AUDITED` | — |  | 8 |
| `bond_ktn_001_ktn` | Bond stories: ktn | `CORE` | `PASS_PHASE1_BOND_B1A_AUDITED` | — |  | 8 |
| `bond_mei_001_mei` | Bond stories: mei | `TEXTURE` | `PHASE1_BOND_RERANKED_TEXTURE_INDEXED` | — |  | 8 |
| `bond_mhk_001_mhk` | Bond stories: mhk | `IMPORTANT` | `PASS_PHASE1_BOND_B2A_AUDITED` | — |  | 8 |
| `bond_ngs_001_ngs` | Bond stories: ngs | `SUPPORT` | `PHASE1_BOND_RERANKED_SUPPORT_MINING` | — |  | 8 |
| `bond_rei_001_rei` | Bond stories: rei | `IMPORTANT` | `PASS_PHASE1_BOND_B2B_AUDITED` | — |  | 8 |
| `bond_rio_001_rio` | Bond stories: rio | `IMPORTANT` | `PASS_PHASE1_BOND_B2B_AUDITED` | — |  | 8 |
| `bond_rui_001_rui` | Bond stories: rui | `IMPORTANT` | `PASS_PHASE1_BOND_B2A_AUDITED` | — |  | 8 |
| `bond_ski_001_ski` | Bond stories: ski | `IMPORTANT` | `PASS_PHASE1_BOND_B2B_AUDITED` | — |  | 8 |
| `bond_skr_001_skr` | Bond stories: skr | `IMPORTANT` | `PASS_PHASE1_BOND_B2A_AUDITED` | — |  | 8 |
| `bond_smr_001_smr` | Bond stories: smr | `IMPORTANT` | `PASS_PHASE1_BOND_B2B_AUDITED` | — |  | 8 |
| `bond_suz_001_suz` | Bond stories: suz | `SUPPORT` | `PHASE1_BOND_RERANKED_SUPPORT_MINING` | — |  | 8 |
| `bond_szk_001_szk` | Bond stories: szk | `IMPORTANT` | `PASS_PHASE1_BOND_B2A_AUDITED` | — |  | 8 |
| `bond_yu_001_yu` | Bond stories: yu | `TEXTURE` | `PHASE1_BOND_RERANKED_TEXTURE_INDEXED` | — |  | 8 |

### specials_misc

| Item ID | Title | Priority | Status | H | AV | Stories |
|---|---|---|---|---|:---:|---:|
| `specials_001_st-ex-story-part-anniversary-01-23-0624` | st-ex-story-part-anniversary-01-23-0624 | `FORMAL-DEPENDENT` | `PHASE1_SPECIAL_FORMAL_INDEX_ONLY` | — | Y | 1 |
| `specials_002_st-ex-story-part-anniversary-01-24-0624` | st-ex-story-part-anniversary-01-24-0624 | `SUPPORT` | `PHASE1_SPECIAL_SUPPORT_RETROSPECTIVE` | — |  | 1 |
| `specials_003_st-ex-story-part-birthday-01-hrk` | st-ex-story-part-birthday-01-hrk | `TEXTURE` | `PHASE1_SPECIAL_TEXTURE_INDEXED` | — |  | 1 |
| `specials_004_st-ex-story-part-birthday-01-mei` | st-ex-story-part-birthday-01-mei | `TEXTURE` | `PHASE1_SPECIAL_TEXTURE_INDEXED` | — |  | 2 |
| `specials_005_st-ex-story-part-birthday-01-ngs` | st-ex-story-part-birthday-01-ngs | `TEXTURE` | `PHASE1_SPECIAL_TEXTURE_INDEXED` | — |  | 2 |
| `specials_006_st-ex-story-part-birthday-01-rei` | st-ex-story-part-birthday-01-rei | `TEXTURE` | `PHASE1_SPECIAL_TEXTURE_INDEXED` | — |  | 2 |
| `specials_007_st-ex-story-part-birthday-01-rio` | st-ex-story-part-birthday-01-rio | `TEXTURE` | `PHASE1_SPECIAL_TEXTURE_INDEXED` | — |  | 1 |
| `specials_008_st-ex-story-part-birthday-01-rui` | st-ex-story-part-birthday-01-rui | `TEXTURE` | `PHASE1_SPECIAL_TEXTURE_INDEXED` | — |  | 1 |
| `specials_009_st-ex-story-part-birthday-01-szk` | st-ex-story-part-birthday-01-szk | `TEXTURE` | `PHASE1_SPECIAL_TEXTURE_INDEXED` | — |  | 1 |
| `specials_010_st-ex-story-part-special-01-21-1224-half-aniv` | st-ex-story-part-special-01-21-1224-half-aniv | `FORMAL-DEPENDENT` | `PHASE1_SPECIAL_FORMAL_INDEX_ONLY` | — |  | 1 |
| `specials_011_st-ex-story-part-special-01-22-0103-newyear` | st-ex-story-part-special-01-22-0103-newyear | `TEXTURE` | `PHASE1_SPECIAL_TEXTURE_INDEXED` | — |  | 1 |
| `specials_012_st-ex-story-part-special-01-22-0401-april` | st-ex-story-part-special-01-22-0401-april | `FORMAL-DEPENDENT` | `PHASE1_SPECIAL_FORMAL_INDEX_ONLY` | — |  | 2 |
| `specials_013_st-ex-story-part-special-01-22-0624-aniv` | st-ex-story-part-special-01-22-0624-aniv | `SUPPORT` | `PHASE1_SPECIAL_SUPPORT_RETROSPECTIVE` | — |  | 2 |
| `specials_014_st-ex-story-part-special-01-23-0101-newyear` | st-ex-story-part-special-01-23-0101-newyear | `TEXTURE` | `PHASE1_SPECIAL_TEXTURE_INDEXED` | — |  | 1 |
| `specials_015_st-ex-story-part-special-01-23-0401-april` | st-ex-story-part-special-01-23-0401-april | `FORMAL-DEPENDENT` | `PHASE1_SPECIAL_FORMAL_INDEX_ONLY` | — |  | 3 |
| `specials_016_st-ex-story-part-special-01-24-0103-newyear` | st-ex-story-part-special-01-24-0103-newyear | `TEXTURE` | `PHASE1_SPECIAL_TEXTURE_INDEXED` | — |  | 1 |
| `specials_017_st-ex-story-part-special-01-24-0401-april` | st-ex-story-part-special-01-24-0401-april | `TEXTURE` | `PHASE1_SPECIAL_COMEDY_CAVEATED` | — | Y | 5 |
| `specials_018_st-ex-story-part-special-01-24-0624-aniv` | st-ex-story-part-special-01-24-0624-aniv | `FORMAL-DEPENDENT` | `PHASE1_SPECIAL_FORMAL_INDEX_ONLY` | — |  | 1 |
| `specials_019_st-ex-story-part-special-01-25-0104-newyear` | st-ex-story-part-special-01-25-0104-newyear | `TEXTURE` | `PHASE1_SPECIAL_TEXTURE_INDEXED` | — |  | 1 |
| `specials_020_st-ex-story-part-special-01-25-0624-aniv` | st-ex-story-part-special-01-25-0624-aniv | `FORMAL-DEPENDENT` | `PHASE1_SPECIAL_FORMAL_INDEX_ONLY` | — |  | 1 |
| `specials_021_st-ex-story-part-special-01-26-0104-newyear` | st-ex-story-part-special-01-26-0104-newyear | `TEXTURE` | `PHASE1_SPECIAL_TEXTURE_INDEXED` | — |  | 1 |
| `specials_022_st-ex-story-part-special-01-26-0401-april` | st-ex-story-part-special-01-26-0401-april | `TEXTURE` | `PHASE1_SPECIAL_COMEDY_CAVEATED` | — |  | 6 |
| `specials_023_st-ex-story-part-special-01-26-0624-aniv` | st-ex-story-part-special-01-26-0624-aniv | `FORMAL-DEPENDENT` | `PHASE1_SPECIAL_FORMAL_INDEX_ONLY` | — |  | 1 |
| `specials_024_st-ex-story-part-special-01-birthday-trip-2024` | st-ex-story-part-special-01-birthday-trip-2024 | `SUPPORT` | `PHASE1_SPECIAL_SUPPORT_ORDINARY_LIFE` | — |  | 4 |
| `specials_025_st-shelf-25-0128-001` | st-shelf-25-0128-001 | `SUPPORT` | `PHASE1_SPECIAL_SUPPORT_MANAGER_RELATIONAL` | — |  | 1 |
| `specials_026_st-shelf-25-0401-001` | st-shelf-25-0401-001 | `TEXTURE` | `PHASE1_SPECIAL_COMEDY_CAVEATED` | — |  | 7 |
| `misc_001_st-love-23-0514-007-bad` | st-love-23-0514-007-bad | `CONFLICTING` | `PHASE1_BRANCH_CAVEATED_NO_CONTINUITY_AUTHORITY` | — |  | 1 |

### cards

| Item ID | Title | Priority | Status | H | AV | Stories |
|---|---|---|---|---|:---:|---:|
| `card_ai_001_st-card-ai-05-arab-00` | 世界の お祭り 突撃GO！ | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_ai_002_st-card-ai-05-birt-00` | 父の力に なりたくて | `SUPPORT` | `PHASE1_CARD_C2_SELECTIVE` | — |  | 3 |
| `card_ai_003_st-card-ai-05-birt-01` | 慰安旅行 in山梨 | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_ai_004_st-card-ai-05-birt-02` | 熊さーーー ーーーん | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_ai_005_st-card-ai-05-casl-04` | お出掛けしま しょうよ～ | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_ai_006_st-card-ai-05-chna-01` | 私がリングに 立つなんて！ | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_ai_007_st-card-ai-05-fest-00` | 前を向き 駆け抜けろ ですよ！ | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_ai_008_st-card-ai-05-fest-03` | 最高のMVを 作って みせます | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_ai_009_st-card-ai-05-idol-00` | いなくても いい？ | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_ai_010_st-card-ai-05-kait-00` | 合宿を終えて | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_ai_011_st-card-ai-05-miku-01` | そーっと、 そーっと | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_ai_012_st-card-ai-05-mizg-01` | 一人だけ ゼロ回 | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_ai_013_st-card-ai-05-mizg-02` | 泣くつもり なんて 全然ないのに | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_ai_014_st-card-ai-05-rock-00` | やりとげて みせます！ | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_ai_015_st-card-ai-05-tact-00` | 端っこ アイドル | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_ai_016_st-card-ai-05-vlnt-00` | 親友の本音 | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_ai_017_st-card-ai-05-wedd-00` | 結婚式を プロデュース | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_ai_018_st-card-ai-05-yukt-00` | 私もBIG4 ですからね | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_aoi_001_st-card-aoi-05-arab-00` | もう一人の 恩人 | `SUPPORT` | `PHASE1_CARD_C2_SELECTIVE` | — |  | 3 |
| `card_aoi_002_st-card-aoi-05-birt-00` | 莉央と愛への ドッキリ企画 | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_aoi_003_st-card-aoi-05-birt-01` | 慰安旅行 in沖縄 | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_aoi_004_st-card-aoi-05-birt-02` | mihoは AIの達人 だね | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_aoi_005_st-card-aoi-05-casl-04` | さすが僕の マネージャー | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_aoi_006_st-card-aoi-05-circ-00` | 一人のファン としての意見 | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_aoi_007_st-card-aoi-05-fest-00` | 力を 貸してほしい | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_aoi_008_st-card-aoi-05-fest-03` | 「そばに いる」 | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_aoi_009_st-card-aoi-05-idol-00` | 僕は僕 | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_aoi_010_st-card-aoi-05-kait-00` | 隠し事とカニカマ | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_aoi_011_st-card-aoi-05-miku-01` | ミクは凄いね | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_aoi_012_st-card-aoi-05-mizg-01` | この夏一番 熱い場所 | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_aoi_013_st-card-aoi-05-past-00` | 莉央の お世話で 大変だ | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_aoi_014_st-card-aoi-05-vlnt-00` | 二月のチョコ だけが違う | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_aoi_015_st-card-aoi-05-wdnc-00` | 彼女が 怪我を？ | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_aoi_016_st-card-aoi-05-wedd-00` | ドラマの中の ことなのに | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_aoi_017_st-card-aoi-05-yukt-00` | 歌とダンスで生きていく | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_cca_001_st-card-cca-05-goch-00` | いろいろ案内 したいな～ | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_chk_001_st-card-chk-05-sush-00` | 旅館 『十千万』 へようこそ！ | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_chn_001_st-card-chn-05-goch-00` | 私の 好きな場所 | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_chs_001_st-card-chs-05-alic-00` | ラヴラビに 関われる なんて | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_chs_002_st-card-chs-05-birt-00` | 日頃の感謝を 歌に乗せて | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_chs_003_st-card-chs-05-birt-01` | 慰安旅行 in京都 | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_chs_004_st-card-chs-05-birt-02` | 10カワだよ | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_chs_005_st-card-chs-05-chia-00` | 物持ちが いいんですね | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_chs_006_st-card-chs-05-chsk-00` | 最高の 衣装デザイン | `SUPPORT` | `PHASE1_CARD_C2_SELECTIVE` | — |  | 3 |
| `card_chs_007_st-card-chs-05-fest-00` | 凄い衣装が 出来ちゃう かも | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_chs_008_st-card-chs-05-fest-03` | 逆襲の ドッキリ企画 | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_chs_009_st-card-chs-05-flow-00` | ここが噂の スタジオ ですね！ | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_chs_010_st-card-chs-05-hruh-00` | 宇宙人は 本当にいます | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_chs_011_st-card-chs-05-idol-00` | オススメの 映画 | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_chs_012_st-card-chs-05-maid-00` | すみれちゃん が出演した 作品 | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_chs_013_st-card-chs-05-mizg-04` | 略して 生磯かな | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_chs_014_st-card-chs-05-pajm-00` | 目指せ スリクスさん | `SUPPORT` | `PHASE1_CARD_C2_SELECTIVE` | — |  | 3 |
| `card_chs_015_st-card-chs-05-rock-00` | ソロパートに 挑戦 | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_chs_016_st-card-chs-05-seik-00` | お姉さんらしい振る舞い | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_chs_017_st-card-chs-05-yukt-00` | 思い出の 夏祭り | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_hrk_001_st-card-hrk-05-adlt-00` | 養成所の 先生 | `SUPPORT` | `PHASE1_CARD_C2_SELECTIVE` | — |  | 3 |
| `card_hrk_002_st-card-hrk-05-birt-00` | 星見プロの お姉さん枠 | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_hrk_003_st-card-hrk-05-birt-01` | 慰安旅行 in山梨 | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_hrk_004_st-card-hrk-05-birt-02` | 工具セット どうするのよ | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_hrk_005_st-card-hrk-05-chna-00` | 羞恥心克服 | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_hrk_006_st-card-hrk-05-fest-00` | 一週間 マネージャー | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_hrk_007_st-card-hrk-05-idol-00` | ソロキャンが 趣味 | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_hrk_008_st-card-hrk-05-idol-03` | 新曲のジャケット撮影 | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_hrk_009_st-card-hrk-05-link-00` | ミュージカル のオーディ ション | `IMPORTANT` | `PHASE1_CARD_C1A_ADMITTED` | — |  | 3 |
| `card_hrk_010_st-card-hrk-05-mizg-01` | 苦い思い出 | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_hrk_011_st-card-hrk-05-mnab-00` | そんな光景を 見てみたい | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_hrk_012_st-card-hrk-05-onep-00` | ドキドキ 温泉旅行 | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_hrk_013_st-card-hrk-05-pair-00` | 一緒に頑張ろうって言ったでしょ？ | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_hrk_014_st-card-hrk-05-pajm-00` | 私をデートに 連れてって | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_hrk_015_st-card-hrk-05-sail-00` | むちっとは してるけど | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_hrk_016_st-card-hrk-05-vlnt-00` | ちょっと意識していた人 | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_hrk_017_st-card-hrk-05-wedd-00` | デート ってこと！？ | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_hrk_018_st-card-hrk-05-xmas-00` | 複雑な気持ち | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_kan_001_st-card-kan-05-birt-00` | ちょうどいい 引き立て役 | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_kan_002_st-card-kan-05-birt-01` | 慰安旅行 in北海道 | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_kan_003_st-card-kan-05-birt-02` | 巨大珍魚を 一本釣り | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_kan_004_st-card-kan-05-buny-00` | セレブという 名の獲物 | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_kan_005_st-card-kan-05-chia-00` | 殊勝な 心がけ じゃん | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_kan_006_st-card-kan-05-chna-00` | kanaの映画デビュー | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_kan_007_st-card-kan-05-fest-02` | クソ記事を ぶっ潰して やんのよ | `IMPORTANT` | `PHASE1_CARD_C1A_ADMITTED` | — |  | 3 |
| `card_kan_008_st-card-kan-05-idol-00` | どいつを ボコれば いいわけ？ | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_kan_009_st-card-kan-05-idol-03` | 恋愛解禁 ってこと？ | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_kan_010_st-card-kan-05-link-00` | こいつの 実家は 実家で | `SUPPORT` | `PHASE1_CARD_C2_SELECTIVE` | — |  | 3 |
| `card_kan_011_st-card-kan-05-mizg-02` | もっと 気合いを 入れろー！！ | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_kan_012_st-card-kan-05-pair-00` | こころの やつ、 絶対泣かす | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_kan_013_st-card-kan-05-poli-00` | 二日酔いでも パッキパキ | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_kan_014_st-card-kan-05-snro-00` | はい、 kanaと 握手！ | `IMPORTANT` | `PHASE1_CARD_C1A_ADMITTED` | — |  | 3 |
| `card_kkr_001_st-card-kkr-05-birt-00` | こころが 主役の こころの ための日 | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_kkr_002_st-card-kkr-05-birt-01` | 慰安旅行 in山梨 | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_kkr_003_st-card-kkr-05-birt-02` | 祝いたまへー | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_kkr_004_st-card-kkr-05-casl-04` | 涙腺 どうなって るんですか | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — | Y | 3 |
| `card_kkr_005_st-card-kkr-05-fest-00` | こころは絶対 歌います！ | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_kkr_006_st-card-kkr-05-fest-03` | 最終形態 鬼モード | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_kkr_007_st-card-kkr-05-flow-00` | 角が折れた！ | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_kkr_008_st-card-kkr-05-idol-00` | 大きな仕事 | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_kkr_009_st-card-kkr-05-kion-00` | 声が似てる なんて | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_kkr_010_st-card-kkr-05-link-00` | 二人で存分に 鍛えて きなさい | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_kkr_011_st-card-kkr-05-miku-01` | あまりにも 寒過ぎて | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_kkr_012_st-card-kkr-05-mizg-01` | こっそり ストーキング | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_kkr_013_st-card-kkr-05-mizg-02` | いざ出陣じゃー！ | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_kkr_014_st-card-kkr-05-newy-00` | 一人だけの オフなので | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_kkr_015_st-card-kkr-05-pair-00` | こ、こころの プリンが！ | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_kkr_016_st-card-kkr-05-seik-00` | 研究中のアイドルさん | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_kkr_017_st-card-kkr-05-snro-00` | マネージャー さん、 おねがい♪ | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_kkr_018_st-card-kkr-05-trbl-00` | 邪な視線を 察知っ！ | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_kkr_019_st-card-kkr-05-vlnt-00` | 零れる弱音 | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_kor_001_st-card-kor-05-birt-00` | クソガキに 鉄槌を | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_kor_002_st-card-kor-05-birt-01` | 慰安旅行 in沖縄 | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_kor_003_st-card-kor-05-birt-02` | なんで 莉央が 不機嫌に | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_kor_004_st-card-kor-05-buny-00` | 嘘、嘘でしょ ……！？ | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_kor_005_st-card-kor-05-fest-02` | 契約取れない で終わる！！ | `IMPORTANT` | `PHASE1_CARD_C1A_ADMITTED` | — |  | 3 |
| `card_kor_006_st-card-kor-05-idol-00` | お金を 稼ぎたい | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_kor_007_st-card-kor-05-idol-03` | franの 興味 | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_kor_008_st-card-kor-05-mizg-01` | そうなん ですか？ | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_kor_009_st-card-kor-05-mizg-02` | 優雅な休憩も 必要 | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_kor_010_st-card-kor-05-newy-00` | う、うーん ……ぐぅ…… | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_kor_011_st-card-kor-05-nurs-00` | 私が ネクロ！？ | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_kor_012_st-card-kor-05-poli-00` | この旅館 なんですか？ | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_kor_013_st-card-kor-05-xmas-00` | ああ、お金が ほしいわ | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_ktn_001_st-card-ktn-05-birt-00` | サプライズ・ サンタ計画 | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_ktn_002_st-card-ktn-05-birt-01` | 慰安旅行 in山梨 | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_ktn_003_st-card-ktn-05-birt-02` | メリー クリスマス、 渚 | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_ktn_004_st-card-ktn-05-circ-00` | 新しい扉 | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_ktn_005_st-card-ktn-05-fest-00` | 懐古と焦燥 | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_ktn_006_st-card-ktn-05-fest-01` | どんな想いも 燃料に | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_ktn_007_st-card-ktn-05-fest-02` | 想いに 応えたい | `IMPORTANT` | `PHASE1_CARD_C1B_ADMITTED` | — |  | 3 |
| `card_ktn_008_st-card-ktn-05-idol-00` | 焦りは禁物 | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_ktn_009_st-card-ktn-05-kiok-00` | ゲストには あの人を | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_ktn_010_st-card-ktn-05-mizg-01` | 恥ずかしいです | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_ktn_011_st-card-ktn-05-mizg-03` | 今度は 水上バイク かぁ | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_ktn_012_st-card-ktn-05-mnab-00` | 思い出の プレゼント | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_ktn_013_st-card-ktn-05-msic-00` | ど、努力 します | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_ktn_014_st-card-ktn-05-newy-00` | 言いそびれ ちゃった | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_ktn_015_st-card-ktn-05-poli-00` | 絶対に 見返して みせます | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_ktn_016_st-card-ktn-05-wedd-00` | 気付いてほしい | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_ktn_017_st-card-ktn-05-yukt-00` | どーん どーん | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_mei_001_st-card-mei-05-birt-00` | 夢のような 企画 | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_mei_002_st-card-mei-05-birt-01` | 慰安旅行 in沖縄 | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_mei_003_st-card-mei-05-birt-02` | はっぴー ばーすでー だにゃ | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_mei_004_st-card-mei-05-birt-03` | にゃん がとう！ | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_mei_005_st-card-mei-05-casl-02` | 恋する少女、早坂芽衣 | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_mei_006_st-card-mei-05-fest-00` | 仲間から刺激を受けて | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_mei_007_st-card-mei-05-fest-02` | アイドルの お手本に | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_mei_008_st-card-mei-05-hruh-00` | 今の芽衣とは 違う芽衣 | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_mei_009_st-card-mei-05-idol-00` | 芽衣の ポテンシャル | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_mei_010_st-card-mei-05-miku-05` | プールを 遊び尽くす よ～！！ | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_mei_011_st-card-mei-05-mizg-01` | ライブ前のひと時 | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_mei_012_st-card-mei-05-mizg-02` | セクシーな アレンジ | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_mei_013_st-card-mei-05-pair-00` | すっごい 嬉しい ニュース | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_mei_014_st-card-mei-05-rock-00` | 楽しく踊ってる方がいい | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_mei_015_st-card-mei-05-vlnt-00` | 面白いよね、 『本命 チョコ』 | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_mei_016_st-card-mei-05-wdnc-00` | どっかーー ーーん | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_mei_017_st-card-mei-05-wedd-00` | 水が垂れてる いい男？ | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_mei_018_st-card-mei-05-xmas-00` | 街中すっかり クリスマス | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_mhk_001_st-card-mhk-05-birt-00` | mihoの やってみたい こと | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_mhk_002_st-card-mhk-05-birt-01` | 慰安旅行 in山梨 | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_mhk_003_st-card-mhk-05-birt-02` | それは それで 撮れ高が | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_mhk_004_st-card-mhk-05-chna-00` | 願ってもない 好条件です | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_mhk_005_st-card-mhk-05-circ-00` | 免許証です | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_mhk_006_st-card-mhk-05-fest-02` | 『Friend  Glass』 | `IMPORTANT` | `PHASE1_CARD_C1A_ADMITTED` | — |  | 3 |
| `card_mhk_007_st-card-mhk-05-idol-00` | 名目上は マネージャー | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_mhk_008_st-card-mhk-05-idol-03` | もうひとりの 優勝者 | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_mhk_009_st-card-mhk-05-mizg-01` | あ、ヤドカリ | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_mhk_010_st-card-mhk-05-newy-00` | 自分の車を 買うつもり なんです | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_mhk_011_st-card-mhk-05-pajm-00` | 容赦なく 刈りますから | `IMPORTANT` | `PHASE1_CARD_C1A_ADMITTED` | — |  | 3 |
| `card_mhk_012_st-card-mhk-05-poli-00` | 今後は 気をつけます | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_mhk_013_st-card-mhk-05-wedd-00` | なんて 不気味な | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_mhk_014_st-card-mhk-05-xmas-00` | もうすぐ クリスマス | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_mku_001_st-card-mku-05-miku-00` | 教えて、 マネージャーさん | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_mku_002_st-card-mku-05-miku-05` | 夏休みの 宿題？ | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_mku_003_st-card-mku-05-miku-06` | アクシデント も思い出？ | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_mna_001_st-card-mna-05-birt-01` | 普段と 違ーう！ | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_mna_002_st-card-mna-05-birt-02` | アンサー ソング | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_mna_003_st-card-mna-05-fest-00` | 突然のプレゼント | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_mna_004_st-card-mna-05-fest-01` | 内緒の準備 | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_mna_005_st-card-mna-05-fest-02` | 麻奈への 密着 インタビュー | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_mna_006_st-card-mna-05-idol-00` | 新人アイドルとマネージャー | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_mna_007_st-card-mna-05-link-00` | くすぐったい ってば | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_mna_008_st-card-mna-05-mizg-01` | ホテルに 缶詰だよ！ | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_mna_009_st-card-mna-05-msic-00` | カレーを 食べようよ～ | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_mna_010_st-card-mna-05-snro-00` | それじゃあ、 紹介するね | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_mna_011_st-card-mna-05-vlnt-00` | 経験ないのに | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_mna_012_st-card-mna-05-wedd-00` | うち、来る？ | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_ngs_001_st-card-ngs-05-akma-00` | 小悪魔 といえば？ | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_ngs_002_st-card-ngs-05-birt-00` | 大好きで 絶対に 喜ぶもの | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_ngs_003_st-card-ngs-05-birt-01` | 慰安旅行 in沖縄 | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_ngs_004_st-card-ngs-05-birt-02` | 聞いて 驚きたまえ | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_ngs_005_st-card-ngs-05-birt-03` | 企画を 考えたのは？ | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_ngs_006_st-card-ngs-05-casl-02` | 恋する少女、伊吹渚 | `SUPPORT` | `PHASE1_CARD_C2_SELECTIVE` | — |  | 3 |
| `card_ngs_007_st-card-ngs-05-fest-02` | 二人の関係 | `IMPORTANT` | `PHASE1_CARD_C1B_ADMITTED` | — |  | 3 |
| `card_ngs_008_st-card-ngs-05-flow-00` | 渚のスケジュール | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_ngs_009_st-card-ngs-05-frut-00` | 桃が 美味しくて、 つい | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_ngs_010_st-card-ngs-05-idol-00` | 尾行の理由 | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_ngs_011_st-card-ngs-05-link-00` | 甘えん坊さん だなぁ | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_ngs_012_st-card-ngs-05-maid-01` | お給仕 します！ | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_ngs_013_st-card-ngs-05-mizg-01` | 大役のプレッシャー | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_ngs_014_st-card-ngs-05-mizg-02` | 心と体の 準備期間 | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_ngs_015_st-card-ngs-05-vlnt-00` | 最高の ライバルで あり仲間 | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_ngs_016_st-card-ngs-05-wedd-00` | 普通の子 じゃなくて | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_ngs_017_st-card-ngs-05-xmas-00` | 理想の クリスマス デート | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_ngs_018_st-card-ngs-05-yukt-00` | つむじで 分かるんです | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_rei_001_st-card-rei-05-birt-00` | 楽しさ三倍の 誕生日企画 | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_rei_002_st-card-rei-05-birt-01` | 慰安旅行 in北海道 | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_rei_003_st-card-rei-05-birt-02` | うー…… あと五分…… | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_rei_004_st-card-rei-05-casl-02` | 恋する少女、 一ノ瀬怜 | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_rei_005_st-card-rei-05-chia-00` | 恋愛相談が あるんです けど | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_rei_006_st-card-rei-05-fest-00` | 怜のライバル | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_rei_007_st-card-rei-05-fest-01` | どういたし まして | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_rei_008_st-card-rei-05-hruh-00` | 不思議な力で 行きたい 場所へ | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_rei_009_st-card-rei-05-idol-00` | 認められたい 気持ち | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_rei_010_st-card-rei-05-mizg-02` | じろじろ 見ないで | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_rei_011_st-card-rei-05-mizg-03` | 怜の ジャングル 探検 | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_rei_012_st-card-rei-05-newy-00` | わんこそば 早食い競争 | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_rei_013_st-card-rei-05-onep-00` | 私って怖い んでしょうか？ | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_rei_014_st-card-rei-05-pair-00` | 粗茶ですが、 どうぞ | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_rei_015_st-card-rei-05-rock-00` | 休息を知らない怜 | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_rei_016_st-card-rei-05-sail-00` | 眩しく輝いて みせます | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_rei_017_st-card-rei-05-trbl-00` | ハレンチは 起こさせ ません | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_rei_018_st-card-rei-05-wdnc-00` | アングラな 名前ですね | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_rei_019_st-card-rei-05-wedd-00` | 結婚 おめでとう | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_rik_001_st-card-rik-05-sush-00` | なんだか 後ろに気配が | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_rio_001_st-card-rio-05-birt-00` | 莉央の わがまま | `SUPPORT` | `PHASE1_CARD_C2_SELECTIVE` | — |  | 3 |
| `card_rio_002_st-card-rio-05-birt-01` | 慰安旅行 in沖縄 | `SUPPORT` | `PHASE1_CARD_C2_SELECTIVE` | — |  | 3 |
| `card_rio_003_st-card-rio-05-birt-02` | 空き巣に 入られてる じゃない | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_rio_004_st-card-rio-05-casl-02` | 敗北を 味わわせて あげる | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_rio_005_st-card-rio-05-casl-04` | 私がお店に 立つわ | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_rio_006_st-card-rio-05-fest-00` | 大人げない 自分 | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_rio_007_st-card-rio-05-fest-01` | 莉央への 密着 インタビュー | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_rio_008_st-card-rio-05-fest-03` | 負けられない 理由 | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_rio_009_st-card-rio-05-halw-00` | プライドの塊 | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_rio_010_st-card-rio-05-idol-00` | トップを取る のは私達 | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_rio_011_st-card-rio-05-kait-00` | 宣戦布告 | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_rio_012_st-card-rio-05-kiok-00` | 思い出を 巡れば | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_rio_013_st-card-rio-05-mizg-02` | じっと 見ないで ちょうだい | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_rio_014_st-card-rio-05-newy-00` | 実家に来る？ | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_rio_015_st-card-rio-05-pajm-00` | コスメの CM？ | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_rio_016_st-card-rio-05-past-00` | 葵と私の話 | `SUPPORT` | `PHASE1_CARD_C2_SELECTIVE` | — |  | 3 |
| `card_rio_017_st-card-rio-05-trbl-00` | そんなに じろじろ 見ないで | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_rio_018_st-card-rio-05-wedd-00` | 私の プライドは ズタズタよ | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_rui_001_st-card-rui-05-birt-00` | 瑠依の疑問 | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_rui_002_st-card-rui-05-birt-01` | 慰安旅行 in京都 | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_rui_003_st-card-rui-05-birt-02` | 黒魔術 でも やってんの | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_rui_004_st-card-rui-05-date-00` | 未知の体験 | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_rui_005_st-card-rui-05-fest-01` | 私一人だけ ですか？ | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_rui_006_st-card-rui-05-fest-03` | わわわ私 なんてことを | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_rui_007_st-card-rui-05-fest-04` | こ、こ ……恋！？ | `IMPORTANT` | `PHASE1_CARD_C1B_ADMITTED` | — |  | 3 |
| `card_rui_008_st-card-rui-05-idol-00` | 財布がない | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_rui_009_st-card-rui-05-idol-04` | 差を埋める 方法 | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_rui_010_st-card-rui-05-miku-00` | 同じステージ に立って | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_rui_011_st-card-rui-05-mizg-01` | 瑠依の恩返し | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_rui_012_st-card-rui-05-newy-00` | CMでも 食べたお揚げ | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_rui_013_st-card-rui-05-sucu-00` | サキュバス ってなんで すか！？ | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_rui_014_st-card-rui-05-trbl-01` | 入れ 替わってる ーー！？ | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_rui_015_st-card-rui-05-vlnt-00` | 掴めない感覚 | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_rui_016_st-card-rui-05-xmas-00` | 内緒で相談 | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_rui_017_st-card-rui-05-yukt-00` | か、か、間接 | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_ski_001_st-card-ski-05-birt-00` | 千紗からの プレゼント | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_ski_002_st-card-ski-05-birt-01` | 慰安旅行in 京都 | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_ski_003_st-card-ski-05-birt-02` | 可愛い お洋服とか 良さそうね | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_ski_004_st-card-ski-05-chsk-00` | 確かな成長と 違和感 | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_ski_005_st-card-ski-05-fest-02` | 我慢するのは もったいない | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_ski_006_st-card-ski-05-idol-00` | 整理整頓 | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_ski_007_st-card-ski-05-kifj-00` | オーディション結果 | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_ski_008_st-card-ski-05-link-00` | それぞれの 『ソロ曲』 | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_ski_009_st-card-ski-05-miku-05` | ミクさんと 共演っ！？ | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_ski_010_st-card-ski-05-mizg-02` | 意外な一面を 探して | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_ski_011_st-card-ski-05-newy-00` | 中身だけ なくなってる | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_ski_012_st-card-ski-05-onep-00` | 恋愛について の勉強 | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_ski_013_st-card-ski-05-poli-00` | 目指せ スリクス | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_ski_014_st-card-ski-05-ster-00` | うぅ、 意地悪です | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_ski_015_st-card-ski-05-waso-00` | 自分を さらけ出す | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_ski_016_st-card-ski-05-xmas-00` | 何をあげたら いいんでしょう | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_skr_001_st-card-skr-05-adlt-00` | 友ちゃんの リスト | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_skr_002_st-card-skr-05-anml-00` | 味わってあげ たいんです！ | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_skr_003_st-card-skr-05-birt-00` | 家族は大事に しないと | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_skr_004_st-card-skr-05-birt-01` | 慰安旅行 in北海道 | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_skr_005_st-card-skr-05-birt-02` | ナイス セレブ リティ！ | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_skr_006_st-card-skr-05-chia-00` | 頑張ります、 コーチ！ | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_skr_007_st-card-skr-05-chna-00` | 美味しくて 美味しいです | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_skr_008_st-card-skr-05-fest-00` | 大き過ぎる期待 | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_skr_009_st-card-skr-05-fest-01` | ニュース 見ましたか？ | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_skr_010_st-card-skr-05-fest-03` | 地元ファンが 喜ぶ企画 | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_skr_011_st-card-skr-05-idol-00` | デビューと 同じ場所 | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_skr_012_st-card-skr-05-idol-03` | 新曲リリース | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_skr_013_st-card-skr-05-mizg-04` | ぎょぎょ っとしてて 格好いい | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_skr_014_st-card-skr-05-newy-00` | 羽根つき対決 | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_skr_015_st-card-skr-05-sail-00` | 瀕死の 遊園地を 救います！ | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_skr_016_st-card-skr-05-vlnt-00` | 想いよ 届け～！ | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_skr_017_st-card-skr-05-wedd-00` | 川咲さくら流 銀河一の お嫁さん | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_smr_001_st-card-smr-05-birt-00` | サプライズ 過ぎるっ ちゃ～！ | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_smr_002_st-card-smr-05-birt-01` | 慰安旅行 in北海道 | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_smr_003_st-card-smr-05-birt-02` | 千紗 お姉ちゃん！ | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_smr_004_st-card-smr-05-fest-00` | 全部忘れて きちゃい ました！？ | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_smr_005_st-card-smr-05-fest-03` | 本当は 遊びたい ですよね | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_smr_006_st-card-smr-05-fest-04` | 大好きな 地元からの オファー | `SUPPORT` | `PHASE1_CARD_C2_SELECTIVE` | — |  | 3 |
| `card_smr_007_st-card-smr-05-frut-00` | アイドルと 学生の狭間で | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_smr_008_st-card-smr-05-idol-00` | 自販機の前で | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_smr_009_st-card-smr-05-idol-04` | おもてなし するっちゃ！ | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_smr_010_st-card-smr-05-jwel-00` | 私が署長 なんですから | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_smr_011_st-card-smr-05-magi-00` | 最高の作品に してみせます | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_smr_012_st-card-smr-05-maid-00` | 今の私は 挑戦者 | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_smr_013_st-card-smr-05-mizg-01` | ドキドキさせてみせます | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_smr_014_st-card-smr-05-mizg-02` | 海に 行きたいっ ちゃ！ | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_smr_015_st-card-smr-05-newy-00` | 星見プロ、 天下御免！ | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_smr_016_st-card-smr-05-nurs-00` | 風邪 引きますよー | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_smr_017_st-card-smr-05-pajm-00` | すみれの 武者修行 | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_smr_018_st-card-smr-05-seik-00` | ゆーびきーり げんまんっ♪ | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_smr_019_st-card-smr-05-xmas-00` | あんぽんたん！ | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_suz_001_st-card-suz-05-alic-00` | あんなの ぴょーん ですわ | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_suz_002_st-card-suz-05-angl-00` | 念願のCM | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_suz_003_st-card-suz-05-anml-00` | アメリカ留学 | `IMPORTANT` | `PHASE1_CARD_C1A_ADMITTED` | — |  | 3 |
| `card_suz_004_st-card-suz-05-birt-00` | そわそわの 理由 | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_suz_005_st-card-suz-05-birt-01` | 慰安旅行 in京都 | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_suz_006_st-card-suz-05-birt-02` | めちゃくちゃ ですわー | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_suz_007_st-card-suz-05-fest-02` | 思い入れの ある曲 | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_suz_008_st-card-suz-05-goch-00` | 旅におやつは 必需品！ | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_suz_009_st-card-suz-05-idol-00` | 背伸び してる？ | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_suz_010_st-card-suz-05-kion-00` | 部活動って 素敵ですわ | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_suz_011_st-card-suz-05-link-00` | 背後に 気配が ……！？ | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_suz_012_st-card-suz-05-mizg-01` | すず宛ての荷物 | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_suz_013_st-card-suz-05-msic-00` | 全制覇して やりますわ | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_suz_014_st-card-suz-05-onep-00` | 二代目星降る奇しぇき | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_suz_015_st-card-suz-05-pair-00` | 芽衣に 負けない 最高の提案 | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_suz_016_st-card-suz-05-seik-00` | ついに女優 デビュー！ | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_suz_017_st-card-suz-05-wedd-00` | これは 禁断の愛 | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_suz_018_st-card-suz-05-xmas-00` | きっと 驚きますわよ | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_szk_001_st-card-szk-05-alic-00` | 主役の アリスだよ | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_szk_002_st-card-szk-05-angl-00` | あの頃の 私の名前 | `IMPORTANT` | `PHASE1_CARD_C1B_ADMITTED` | — |  | 3 |
| `card_szk_003_st-card-szk-05-birt-00` | 大胆過ぎる 企画 | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_szk_004_st-card-szk-05-birt-01` | 慰安旅行 in京都 | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_szk_005_st-card-szk-05-birt-02` | これは 家宝に しなきゃ | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_szk_006_st-card-szk-05-chna-00` | SNSの声 | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_szk_007_st-card-szk-05-goch-00` | お友達に なったから | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_szk_008_st-card-szk-05-idol-00` | アイドル文化 の先生 | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_szk_009_st-card-szk-05-link-00` | 私が 『一緒に歌い たい』のは | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_szk_010_st-card-szk-05-mizg-03` | 野生に 目覚めた アイドル | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_szk_011_st-card-szk-05-pajm-00` | お姉さんに なりたい | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_szk_012_st-card-szk-05-rock-00` | かっこ良く なりたい…！ | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_szk_013_st-card-szk-05-sail-00` | アイドルだ って 分かるもの | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_szk_014_st-card-szk-05-snro-00` | シナモン くん達との 思い出 | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_szk_015_st-card-szk-05-yukt-00` | 憧れの浴衣 デビュー | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_szk_016_st-card-szk-05-yuru-00` | 意外な選択 | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_ymk_001_st-card-ymk-05-miku-01` | 共演のお礼に | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_yo_001_st-card-yo-05-sush-00` | 曜ちゃんの おうちに | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_yu_001_st-card-yu-05-birt-00` | めんどくさい オタク心理 | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_yu_002_st-card-yu-05-birt-01` | 慰安旅行 in北海道 | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_yu_003_st-card-yu-05-birt-02` | もしもし かめよ | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_yu_004_st-card-yu-05-casl-02` | 全人類キュン 死間違い なしや！ | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_yu_005_st-card-yu-05-chna-00` | ぴったり 過ぎて 恐ろしい | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_yu_006_st-card-yu-05-fest-00` | 風邪 ちゃいます | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_yu_007_st-card-yu-05-fest-01` | 教えて くれへんくて | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_yu_008_st-card-yu-05-fest-04` | 最強最高 の曲で | `SUPPORT` | `PHASE1_CARD_C2_SELECTIVE` | — |  | 3 |
| `card_yu_009_st-card-yu-05-idol-00` | トリエルを 見学 | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_yu_010_st-card-yu-05-idol-04` | ゆで卵 みたいに ぷるぷるや | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_yu_011_st-card-yu-05-jwel-00` | 西の血が 騒いで抑え きれません | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_yu_012_st-card-yu-05-link-00` | 生徒会長に なります！ | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_yu_013_st-card-yu-05-mizg-01` | 二人だけの 秘密 | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_yu_014_st-card-yu-05-mizg-02` | 予想外の反応 | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_yu_015_st-card-yu-05-nurs-00` | 優が大変 お世話に なってます | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_yu_016_st-card-yu-05-ster-00` | 校門から 入れば ええんです | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_yu_017_st-card-yu-05-vlnt-00` | 口説いてみせ ましょか？ | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_yu_018_st-card-yu-05-wedd-01` | うち 話早い人 好きよ | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |
| `card_yu_019_st-card-yu-05-xmas-00` | ライブの後は…？ | `TEXTURE` | `PHASE1_CARD_C3_INDEXED_TEXTURE` | — |  | 3 |

### messages

| Item ID | Title | Priority | Status | H | AV | Stories |
|---|---|---|---|---|:---:|---:|
| `message_message_group_ai_001_message_group_ai_part_01` | Messages: 愛 (Part 1) | `TEXTURE` | `PHASE1_MESSAGE_ROUTED_STORY_LEVEL` | — |  | 22 |
| `message_message_group_ai_001_message_group_ai_part_02` | Messages: 愛 (Part 2) | `TEXTURE` | `PHASE1_MESSAGE_ROUTED_STORY_LEVEL` | — |  | 25 |
| `message_message_group_ai_001_message_group_ai_part_03` | Messages: 愛 (Part 3) | `TEXTURE` | `PHASE1_MESSAGE_ROUTED_STORY_LEVEL` | — |  | 23 |
| `message_message_group_ai_001_message_group_ai_part_04` | Messages: 愛 (Part 4) | `TEXTURE` | `PHASE1_MESSAGE_ROUTED_STORY_LEVEL` | — |  | 18 |
| `message_message_group_aoi_001_message_group_aoi_part_01` | Messages: 葵 (Part 1) | `TEXTURE` | `PHASE1_MESSAGE_ROUTED_STORY_LEVEL` | — |  | 22 |
| `message_message_group_aoi_001_message_group_aoi_part_02` | Messages: 葵 (Part 2) | `TEXTURE` | `PHASE1_MESSAGE_ROUTED_STORY_LEVEL` | — |  | 26 |
| `message_message_group_aoi_001_message_group_aoi_part_03` | Messages: 葵 (Part 3) | `TEXTURE` | `PHASE1_MESSAGE_ROUTED_STORY_LEVEL` | — |  | 24 |
| `message_message_group_aoi_001_message_group_aoi_part_04` | Messages: 葵 (Part 4) | `TEXTURE` | `PHASE1_MESSAGE_ROUTED_STORY_LEVEL` | — |  | 14 |
| `message_message_group_chs_001_message_group_chs_part_01` | Messages: 千紗 (Part 1) | `TEXTURE` | `PHASE1_MESSAGE_ROUTED_STORY_LEVEL` | — |  | 21 |
| `message_message_group_chs_001_message_group_chs_part_02` | Messages: 千紗 (Part 2) | `TEXTURE` | `PHASE1_MESSAGE_ROUTED_STORY_LEVEL` | — |  | 26 |
| `message_message_group_chs_001_message_group_chs_part_03` | Messages: 千紗 (Part 3) | `TEXTURE` | `PHASE1_MESSAGE_ROUTED_STORY_LEVEL` | — |  | 24 |
| `message_message_group_chs_001_message_group_chs_part_04` | Messages: 千紗 (Part 4) | `TEXTURE` | `PHASE1_MESSAGE_ROUTED_STORY_LEVEL` | — |  | 16 |
| `message_message_group_hrk_001_message_group_hrk_part_01` | Messages: 遙子 (Part 1) | `TEXTURE` | `PHASE1_MESSAGE_ROUTED_STORY_LEVEL` | — |  | 21 |
| `message_message_group_hrk_001_message_group_hrk_part_02` | Messages: 遙子 (Part 2) | `TEXTURE` | `PHASE1_MESSAGE_ROUTED_STORY_LEVEL` | — |  | 26 |
| `message_message_group_hrk_001_message_group_hrk_part_03` | Messages: 遙子 (Part 3) | `TEXTURE` | `PHASE1_MESSAGE_ROUTED_STORY_LEVEL` | — |  | 24 |
| `message_message_group_hrk_001_message_group_hrk_part_04` | Messages: 遙子 (Part 4) | `TEXTURE` | `PHASE1_MESSAGE_ROUTED_STORY_LEVEL` | — |  | 16 |
| `message_message_group_kan_001_message_group_kan_part_01` | Messages: kana (Part 1) | `TEXTURE` | `PHASE1_MESSAGE_ROUTED_STORY_LEVEL` | — |  | 22 |
| `message_message_group_kan_001_message_group_kan_part_02` | Messages: kana (Part 2) | `TEXTURE` | `PHASE1_MESSAGE_ROUTED_STORY_LEVEL` | — |  | 25 |
| `message_message_group_kan_001_message_group_kan_part_03` | Messages: kana (Part 3) | `TEXTURE` | `PHASE1_MESSAGE_ROUTED_STORY_LEVEL` | — |  | 8 |
| `message_message_group_kkr_001_message_group_kkr_part_01` | Messages: こころ (Part 1) | `TEXTURE` | `PHASE1_MESSAGE_ROUTED_STORY_LEVEL` | — |  | 19 |
| `message_message_group_kkr_001_message_group_kkr_part_02` | Messages: こころ (Part 2) | `TEXTURE` | `PHASE1_MESSAGE_ROUTED_STORY_LEVEL` | — |  | 24 |
| `message_message_group_kkr_001_message_group_kkr_part_03` | Messages: こころ (Part 3) | `TEXTURE` | `PHASE1_MESSAGE_ROUTED_STORY_LEVEL` | — |  | 22 |
| `message_message_group_kkr_001_message_group_kkr_part_04` | Messages: こころ (Part 4) | `TEXTURE` | `PHASE1_MESSAGE_ROUTED_STORY_LEVEL` | — |  | 22 |
| `message_message_group_kkr_001_message_group_kkr_part_05` | Messages: こころ (Part 5) | `TEXTURE` | `PHASE1_MESSAGE_ROUTED_STORY_LEVEL` | — |  | 1 |
| `message_message_group_kor_001_message_group_kor_part_01` | Messages: fran (Part 1) | `TEXTURE` | `PHASE1_MESSAGE_ROUTED_STORY_LEVEL` | — |  | 21 |
| `message_message_group_kor_001_message_group_kor_part_02` | Messages: fran (Part 2) | `TEXTURE` | `PHASE1_MESSAGE_ROUTED_STORY_LEVEL` | — |  | 25 |
| `message_message_group_kor_001_message_group_kor_part_03` | Messages: fran (Part 3) | `TEXTURE` | `PHASE1_MESSAGE_ROUTED_STORY_LEVEL` | — |  | 8 |
| `message_message_group_ktn_001_message_group_ktn_part_01` | Messages: 琴乃 (Part 1) | `TEXTURE` | `PHASE1_MESSAGE_ROUTED_STORY_LEVEL` | — |  | 23 |
| `message_message_group_ktn_001_message_group_ktn_part_02` | Messages: 琴乃 (Part 2) | `TEXTURE` | `PHASE1_MESSAGE_ROUTED_STORY_LEVEL` | — |  | 28 |
| `message_message_group_ktn_001_message_group_ktn_part_03` | Messages: 琴乃 (Part 3) | `TEXTURE` | `PHASE1_MESSAGE_ROUTED_STORY_LEVEL` | — |  | 24 |
| `message_message_group_ktn_001_message_group_ktn_part_04` | Messages: 琴乃 (Part 4) | `TEXTURE` | `PHASE1_MESSAGE_ROUTED_STORY_LEVEL` | — |  | 11 |
| `message_message_group_ladder-22-0513_001_message_group_ladder-22-0513` | Messages: 白石SISTERS | `TEXTURE` | `PHASE1_MESSAGE_ROUTED_STORY_LEVEL` | — |  | 4 |
| `message_message_group_ladder-22-0610_001_message_group_ladder-22-0610` | Messages: マネ＆さにぴっぴ | `TEXTURE` | `PHASE1_MESSAGE_ROUTED_STORY_LEVEL` | — |  | 9 |
| `message_message_group_ladder-22-0812_001_message_group_ladder-22-0812` | Messages: LizNoir業務連絡 | `TEXTURE` | `PHASE1_MESSAGE_ROUTED_STORY_LEVEL` | — |  | 8 |
| `message_message_group_ladder-22-0916_001_message_group_ladder-22-0916` | Messages: トリトリトリエル | `TEXTURE` | `PHASE1_MESSAGE_ROUTED_STORY_LEVEL` | — |  | 4 |
| `message_message_group_ladder-22-1109_001_message_group_ladder-22-1109_part_01` | Messages: ⅢX-announce- (Part 1) | `TEXTURE` | `PHASE1_MESSAGE_ROUTED_STORY_LEVEL` | — |  | 10 |
| `message_message_group_ladder-22-1109_001_message_group_ladder-22-1109_part_02` | Messages: ⅢX-announce- (Part 2) | `TEXTURE` | `PHASE1_MESSAGE_ROUTED_STORY_LEVEL` | — |  | 2 |
| `message_message_group_ladder-23-0912_001_message_group_ladder-23-0912` | Messages: REI♡HARU | `TEXTURE` | `PHASE1_MESSAGE_ROUTED_STORY_LEVEL` | — |  | 4 |
| `message_message_group_ladder-23-1014_001_message_group_ladder-23-1014` | Messages: わんにゃんツインズ | `TEXTURE` | `PHASE1_MESSAGE_ROUTED_STORY_LEVEL` | — |  | 4 |
| `message_message_group_ladder-24-0811_001_message_group_ladder-24-0811` | Messages: 8/11.12ライブ連絡用 | `TEXTURE` | `PHASE1_MESSAGE_ROUTED_STORY_LEVEL` | — |  | 8 |
| `message_message_group_ladder-24-1108_001_message_group_ladder-24-1108` | Messages: 仲良しkana×こころ | `TEXTURE` | `PHASE1_MESSAGE_ROUTED_STORY_LEVEL` | — |  | 4 |
| `message_message_group_ladder-24-1208_001_message_group_ladder-24-1208` | Messages: ぱじゃパ！＆さとみさん達 | `TEXTURE` | `PHASE1_MESSAGE_ROUTED_STORY_LEVEL` | — |  | 4 |
| `message_message_group_ladder-25-0512_001_message_group_ladder-25-0512` | Messages: Sweet Rouge | `TEXTURE` | `PHASE1_MESSAGE_ROUTED_STORY_LEVEL` | — |  | 4 |
| `message_message_group_ladder-25-1205_001_message_group_ladder-25-1205` | Messages: クリスマスイベント連絡用 | `TEXTURE` | `PHASE1_MESSAGE_ROUTED_STORY_LEVEL` | — |  | 4 |
| `message_message_group_ladder-26-0214_001_message_group_ladder-26-0214` | Messages: 月スト＆マネおしゃべり | `TEXTURE` | `PHASE1_MESSAGE_ROUTED_STORY_LEVEL` | — |  | 4 |
| `message_message_group_ladder-26-0515_001_message_group_ladder-26-0515` | Messages: 遊園地コラボ連絡用 | `TEXTURE` | `PHASE1_MESSAGE_ROUTED_STORY_LEVEL` | — |  | 4 |
| `message_message_group_mei_001_message_group_mei_part_01` | Messages: 芽衣 (Part 1) | `TEXTURE` | `PHASE1_MESSAGE_ROUTED_STORY_LEVEL` | — |  | 23 |
| `message_message_group_mei_001_message_group_mei_part_02` | Messages: 芽衣 (Part 2) | `TEXTURE` | `PHASE1_MESSAGE_ROUTED_STORY_LEVEL` | — |  | 29 |
| `message_message_group_mei_001_message_group_mei_part_03` | Messages: 芽衣 (Part 3) | `TEXTURE` | `PHASE1_MESSAGE_ROUTED_STORY_LEVEL` | — |  | 24 |
| `message_message_group_mei_001_message_group_mei_part_04` | Messages: 芽衣 (Part 4) | `TEXTURE` | `PHASE1_MESSAGE_ROUTED_STORY_LEVEL` | — |  | 12 |
| `message_message_group_mhk_001_message_group_mhk_part_01` | Messages: miho (Part 1) | `TEXTURE` | `PHASE1_MESSAGE_ROUTED_STORY_LEVEL` | — |  | 21 |
| `message_message_group_mhk_001_message_group_mhk_part_02` | Messages: miho (Part 2) | `TEXTURE` | `PHASE1_MESSAGE_ROUTED_STORY_LEVEL` | — |  | 25 |
| `message_message_group_mhk_001_message_group_mhk_part_03` | Messages: miho (Part 3) | `TEXTURE` | `PHASE1_MESSAGE_ROUTED_STORY_LEVEL` | — |  | 9 |
| `message_message_group_mna_001_message_group_mna_part_01` | Messages: 麻奈 (Part 1) | `TEXTURE` | `PHASE1_MESSAGE_ROUTED_STORY_LEVEL` | — |  | 20 |
| `message_message_group_mna_001_message_group_mna_part_02` | Messages: 麻奈 (Part 2) | `TEXTURE` | `PHASE1_MESSAGE_ROUTED_STORY_LEVEL` | — |  | 20 |
| `message_message_group_mna_001_message_group_mna_part_03` | Messages: 麻奈 (Part 3) | `TEXTURE` | `PHASE1_MESSAGE_ROUTED_STORY_LEVEL` | — |  | 23 |
| `message_message_group_mna_001_message_group_mna_part_04` | Messages: 麻奈 (Part 4) | `TEXTURE` | `PHASE1_MESSAGE_ROUTED_STORY_LEVEL` | — |  | 2 |
| `message_message_group_ngs_001_message_group_ngs_part_01` | Messages: 渚 (Part 1) | `TEXTURE` | `PHASE1_MESSAGE_ROUTED_STORY_LEVEL` | — |  | 22 |
| `message_message_group_ngs_001_message_group_ngs_part_02` | Messages: 渚 (Part 2) | `TEXTURE` | `PHASE1_MESSAGE_ROUTED_STORY_LEVEL` | — |  | 28 |
| `message_message_group_ngs_001_message_group_ngs_part_03` | Messages: 渚 (Part 3) | `TEXTURE` | `PHASE1_MESSAGE_ROUTED_STORY_LEVEL` | — |  | 23 |
| `message_message_group_ngs_001_message_group_ngs_part_04` | Messages: 渚 (Part 4) | `TEXTURE` | `PHASE1_MESSAGE_ROUTED_STORY_LEVEL` | — |  | 15 |
| `message_message_group_rei_001_message_group_rei_part_01` | Messages: 怜 (Part 1) | `TEXTURE` | `PHASE1_MESSAGE_ROUTED_STORY_LEVEL` | — |  | 21 |
| `message_message_group_rei_001_message_group_rei_part_02` | Messages: 怜 (Part 2) | `TEXTURE` | `PHASE1_MESSAGE_ROUTED_STORY_LEVEL` | — |  | 27 |
| `message_message_group_rei_001_message_group_rei_part_03` | Messages: 怜 (Part 3) | `TEXTURE` | `PHASE1_MESSAGE_ROUTED_STORY_LEVEL` | — |  | 23 |
| `message_message_group_rei_001_message_group_rei_part_04` | Messages: 怜 (Part 4) | `TEXTURE` | `PHASE1_MESSAGE_ROUTED_STORY_LEVEL` | — |  | 19 |
| `message_message_group_rio_001_message_group_rio_part_01` | Messages: 莉央 (Part 1) | `TEXTURE` | `PHASE1_MESSAGE_ROUTED_STORY_LEVEL` | — |  | 21 |
| `message_message_group_rio_001_message_group_rio_part_02` | Messages: 莉央 (Part 2) | `TEXTURE` | `PHASE1_MESSAGE_ROUTED_STORY_LEVEL` | — |  | 26 |
| `message_message_group_rio_001_message_group_rio_part_03` | Messages: 莉央 (Part 3) | `TEXTURE` | `PHASE1_MESSAGE_ROUTED_STORY_LEVEL` | — |  | 24 |
| `message_message_group_rio_001_message_group_rio_part_04` | Messages: 莉央 (Part 4) | `TEXTURE` | `PHASE1_MESSAGE_ROUTED_STORY_LEVEL` | — |  | 17 |
| `message_message_group_rui_001_message_group_rui_part_01` | Messages: 瑠依 (Part 1) | `TEXTURE` | `PHASE1_MESSAGE_ROUTED_STORY_LEVEL` | — |  | 22 |
| `message_message_group_rui_001_message_group_rui_part_02` | Messages: 瑠依 (Part 2) | `TEXTURE` | `PHASE1_MESSAGE_ROUTED_STORY_LEVEL` | — |  | 25 |
| `message_message_group_rui_001_message_group_rui_part_03` | Messages: 瑠依 (Part 3) | `TEXTURE` | `PHASE1_MESSAGE_ROUTED_STORY_LEVEL` | — |  | 23 |
| `message_message_group_rui_001_message_group_rui_part_04` | Messages: 瑠依 (Part 4) | `TEXTURE` | `PHASE1_MESSAGE_ROUTED_STORY_LEVEL` | — |  | 16 |
| `message_message_group_seaparalive_001_message_group_seaparalive` | Messages: 里帰りライブ業務連絡 | `TEXTURE` | `PHASE1_MESSAGE_ROUTED_STORY_LEVEL` | — |  | 4 |
| `message_message_group_ski_001_message_group_ski_part_01` | Messages: 沙季 (Part 1) | `TEXTURE` | `PHASE1_MESSAGE_ROUTED_STORY_LEVEL` | — |  | 22 |
| `message_message_group_ski_001_message_group_ski_part_02` | Messages: 沙季 (Part 2) | `TEXTURE` | `PHASE1_MESSAGE_ROUTED_STORY_LEVEL` | — |  | 25 |
| `message_message_group_ski_001_message_group_ski_part_03` | Messages: 沙季 (Part 3) | `TEXTURE` | `PHASE1_MESSAGE_ROUTED_STORY_LEVEL` | — |  | 25 |
| `message_message_group_ski_001_message_group_ski_part_04` | Messages: 沙季 (Part 4) | `TEXTURE` | `PHASE1_MESSAGE_ROUTED_STORY_LEVEL` | — |  | 13 |
| `message_message_group_skr_001_message_group_skr_part_01` | Messages: さくら (Part 1) | `TEXTURE` | `PHASE1_MESSAGE_ROUTED_STORY_LEVEL` | — |  | 20 |
| `message_message_group_skr_001_message_group_skr_part_02` | Messages: さくら (Part 2) | `TEXTURE` | `PHASE1_MESSAGE_ROUTED_STORY_LEVEL` | — |  | 26 |
| `message_message_group_skr_001_message_group_skr_part_03` | Messages: さくら (Part 3) | `TEXTURE` | `PHASE1_MESSAGE_ROUTED_STORY_LEVEL` | — |  | 24 |
| `message_message_group_skr_001_message_group_skr_part_04` | Messages: さくら (Part 4) | `TEXTURE` | `PHASE1_MESSAGE_ROUTED_STORY_LEVEL` | — |  | 17 |
| `message_message_group_smr_001_message_group_smr_part_01` | Messages: すみれ (Part 1) | `TEXTURE` | `PHASE1_MESSAGE_ROUTED_STORY_LEVEL` | — |  | 21 |
| `message_message_group_smr_001_message_group_smr_part_02` | Messages: すみれ (Part 2) | `TEXTURE` | `PHASE1_MESSAGE_ROUTED_STORY_LEVEL` | — |  | 30 |
| `message_message_group_smr_001_message_group_smr_part_03` | Messages: すみれ (Part 3) | `TEXTURE` | `PHASE1_MESSAGE_ROUTED_STORY_LEVEL` | — |  | 23 |
| `message_message_group_smr_001_message_group_smr_part_04` | Messages: すみれ (Part 4) | `TEXTURE` | `PHASE1_MESSAGE_ROUTED_STORY_LEVEL` | — |  | 14 |
| `message_message_group_suz_001_message_group_suz_part_01` | Messages: すず (Part 1) | `TEXTURE` | `PHASE1_MESSAGE_ROUTED_STORY_LEVEL` | — |  | 22 |
| `message_message_group_suz_001_message_group_suz_part_02` | Messages: すず (Part 2) | `TEXTURE` | `PHASE1_MESSAGE_ROUTED_STORY_LEVEL` | — |  | 28 |
| `message_message_group_suz_001_message_group_suz_part_03` | Messages: すず (Part 3) | `TEXTURE` | `PHASE1_MESSAGE_ROUTED_STORY_LEVEL` | — |  | 22 |
| `message_message_group_suz_001_message_group_suz_part_04` | Messages: すず (Part 4) | `TEXTURE` | `PHASE1_MESSAGE_ROUTED_STORY_LEVEL` | — |  | 16 |
| `message_message_group_szk_001_message_group_szk_part_01` | Messages: 雫 (Part 1) | `TEXTURE` | `PHASE1_MESSAGE_ROUTED_STORY_LEVEL` | — |  | 23 |
| `message_message_group_szk_001_message_group_szk_part_02` | Messages: 雫 (Part 2) | `TEXTURE` | `PHASE1_MESSAGE_ROUTED_STORY_LEVEL` | — |  | 27 |
| `message_message_group_szk_001_message_group_szk_part_03` | Messages: 雫 (Part 3) | `TEXTURE` | `PHASE1_MESSAGE_ROUTED_STORY_LEVEL` | — |  | 24 |
| `message_message_group_szk_001_message_group_szk_part_04` | Messages: 雫 (Part 4) | `TEXTURE` | `PHASE1_MESSAGE_ROUTED_STORY_LEVEL` | — |  | 12 |
| `message_message_group_vns_001_message_group_vns` | Messages: VENUS事務局 | `TEXTURE` | `PHASE1_MESSAGE_ROUTED_STORY_LEVEL` | — |  | 17 |
| `message_message_group_yu_001_message_group_yu_part_01` | Messages: 優 (Part 1) | `TEXTURE` | `PHASE1_MESSAGE_ROUTED_STORY_LEVEL` | — |  | 21 |
| `message_message_group_yu_001_message_group_yu_part_02` | Messages: 優 (Part 2) | `TEXTURE` | `PHASE1_MESSAGE_ROUTED_STORY_LEVEL` | — |  | 23 |
| `message_message_group_yu_001_message_group_yu_part_03` | Messages: 優 (Part 3) | `TEXTURE` | `PHASE1_MESSAGE_ROUTED_STORY_LEVEL` | — |  | 25 |
| `message_message_group_yu_001_message_group_yu_part_04` | Messages: 優 (Part 4) | `TEXTURE` | `PHASE1_MESSAGE_ROUTED_STORY_LEVEL` | — |  | 20 |

### anime

| Item ID | Title | Priority | Status | H | AV | Stories |
|---|---|---|---|---|:---:|---:|
| `ANIME_E01` | IDOLY PRIDE TV Episode 01 | `CORE` | `PHASE_0_5_CLOSE_READ_FROZEN` | — | Y | — |
| `ANIME_E02` | IDOLY PRIDE TV Episode 02 | `CORE` | `PHASE_0_5_CLOSE_READ_FROZEN` | — | Y | — |
| `ANIME_E03` | IDOLY PRIDE TV Episode 03 | `CORE` | `PHASE_0_5_CLOSE_READ_FROZEN` | — | Y | — |
| `ANIME_E04` | IDOLY PRIDE TV Episode 04 | `CORE` | `PHASE_0_5_CLOSE_READ_FROZEN` | — | Y | — |
| `ANIME_E05` | IDOLY PRIDE TV Episode 05 | `CORE` | `PHASE_0_5_CLOSE_READ_FROZEN` | — | Y | — |
| `ANIME_E06` | IDOLY PRIDE TV Episode 06 | `CORE` | `PHASE_0_5_CLOSE_READ_FROZEN` | — | Y | — |
| `ANIME_E07` | IDOLY PRIDE TV Episode 07 | `CORE` | `PHASE_0_5_CLOSE_READ_FROZEN` | — | Y | — |
| `ANIME_E08` | IDOLY PRIDE TV Episode 08 | `CORE` | `PHASE_0_5_CLOSE_READ_FROZEN` | — | Y | — |
| `ANIME_E09` | IDOLY PRIDE TV Episode 09 | `CORE` | `PHASE_0_5_CLOSE_READ_FROZEN` | — | Y | — |
| `ANIME_E10` | IDOLY PRIDE TV Episode 10 | `CORE` | `PHASE_0_5_CLOSE_READ_FROZEN` | — | Y | — |
| `ANIME_E11` | IDOLY PRIDE TV Episode 11 | `CORE` | `PHASE_0_5_CLOSE_READ_FROZEN` | — | Y | — |
| `ANIME_E12` | IDOLY PRIDE TV Episode 12 | `CORE` | `PHASE_0_5_CLOSE_READ_FROZEN` | — | Y | — |

## 7. What this ledger does not yet claim

- It does not claim that every `TEXTURE` item is analytically minor; that is only the safest broad-pass starting position.
- It does not inherit the V1 `core`/`important` event rankings as truth.
- It does not yet assign relationship axes, themes, contradiction outcomes, or definitive V1 revision labels to every item.
- It does not conflate missing `adv-live-*` assets with missing narrative text.
- It does not yet treat release order as identical to in-universe chronology.

## 8. Phase-1 completion condition

Phase 1 completes only when the governing narrative and event layers have been semantically reviewed, the card/message/bond/special layers have been sampled across every major character and relationship axis, historical priority claims have been independently retested, and every remaining `UNRESOLVED`/`CONFLICTING`/formal-dependent source has an explicit routing decision.

## 9. Next output and recommended model

**Tier-A consolidation bookkeeping:** `IDOLY_PRIDE_V2_PHASE1B_TIER_A_MAIN_NARRATIVE_CONSOLIDATION_AUDIT.md` and `IDOLY_PRIDE_V2_PHASE1B_POST_TIER_A_MAIN_NARRATIVE_BASELINE.md` freeze the complete main-narrative reference model without mutating the prior anime/origin/Tokyo/BIG4/Stellar locks.

**Tier-A status:** **COMPLETE AND CONSOLIDATED — 63/63 game main-story bundles, 33/33 origin bundles, 12/12 anime episodes.**

**Event rerank:** **COMPLETE AND FROZEN — 60/60 event bundles independently rescored.**

**E1-A:** **COMPLETE AND AUDITED — 4/4 tranche events admitted.**

**E1-B:** **COMPLETE AND AUDITED — 4/4 tranche events admitted.**

**E1-C:** **COMPLETE AND AUDITED — 3/3 tranche events admitted.**

**E1-D:** **COMPLETE AND AUDITED — 2/2 tranche events admitted as one United States dissolution/re-authorization chain.**

**E1-E:** **COMPLETE AND AUDITED — 3/3 late-maturation events admitted.**

**E1 mandatory-event progress:** **16/16 E1 events admitted through frozen tranche audits.**

**Event semantic review:** **COMPLETE — 60/60 event bundles explicitly audited/routed through E4.**

**Next analytical operation:** **Phase 1 — Bond Story Priority and Sampling Audit (20 bond bundles).**

Rerank the 20 bond-story bundles against the complete Tier-A + 60-event model before selective close reading. The bond layer is especially important for Makino/idol relationships and may verify or revise claims that events only establish indirectly.

**Recommended model:** GPT-5.6 Sol  
**Recommended reasoning level:** **Extra High**

**Governing inherited state:** `IDOLY_PRIDE_V2_PHASE1B_POST_EVENT_E4_BASELINE.md`.

**Lower-tier rule:** bond/card/message/special material may extend, stabilize, recur, revise, contradict, temporally mature, add texture, require formal review, or correct chronology. It may not silently backfill mature states into earlier Tier-A/event chronology.

**Phase-1 caution:** event completion is not Phase-1 completion. The bond/special/card/message layers still require the sampling and routing specified by the governing analytical method; remaining formal dependencies retain their existing audit routes.

## 10.14 Post-E1 E2 reassessment freeze — 2026-08-15

All **26 events that entered the first event rerank as E2/IMPORTANT** have now been re-evaluated against the complete admitted E1 state. The original event rerank remains immutable provenance; the post-E1 audit now governs E2 reading order.

Governing artifacts:

- `IDOLY_PRIDE_V2_PHASE1B_POST_E1_E2_REASSESSMENT_AUDIT.md`
- `IDOLY_PRIDE_V2_PHASE1B_E2_CLOSE_READ_QUEUE.md`
- `IDOLY_PRIDE_V2_PHASE1B_POST_E1_E2_REASSESSMENT_SHA256SUMS.txt`

Execution result:

- **E2-A / priority close read:** 11
- **E2-B / material extension:** 9
- **E2-C / late important:** 2
- **Support-deferred from the original E2 pool:** 4

This reassessment does **not** admit E2 claims. `IDOLY_PRIDE_V2_PHASE1B_POST_EVENT_E1E_BASELINE.md` remains current governing authority.

The next tranche is **E2-A1**:

1. `event_2021_005_st-eve-2111-backside`
2. `event_2022_003_st-eve-2203-race`
3. `event_2024_007_st-eve-2407-dice`
4. `event_2026_004_st-eve-2604-dice`

**Recommended model:** GPT-5.6 Sol  
**Recommended reasoning:** Extra High

## 10.15 Event E2-A1 close-read freeze — 2026-08-15

The first E2 close-read tranche is complete, prospectively frozen before historical comparison, adversarially audited, and admitted through a successor baseline.

Audited sources:

1. `event_2021_005_st-eve-2111-backside` — **夢踊るステージに架け橋を**
2. `event_2022_003_st-eve-2203-race` — **並び立つ歌姫のフルリール**
3. `event_2024_007_st-eve-2407-dice` — **漕ぎ出せ！アイドル★サバイバーズ**
4. `event_2026_004_st-eve-2604-dice` — **IDOLY MATCH～地下闘技場への挑戦～**

Governing artifacts:

- `IDOLY_PRIDE_V2_PHASE1B_EVENT_E2A1_PRIMARY_FINDINGS_FREEZE.md`
- `IDOLY_PRIDE_V2_PHASE1B_EVENT_E2A1_CLOSE_READ_AUDIT.md`
- `IDOLY_PRIDE_V2_PHASE1B_POST_EVENT_E2A1_BASELINE.md`
- `IDOLY_PRIDE_V2_PHASE1B_EVENT_E2A1_SHA256SUMS.txt`

Principal admitted additions:

- `NON_DISPOSABLE_STANDING`
- `EVALUATIVE_JURISDICTION`
- `BOUNDED_PARENTAL_AUTHORITY`
- `COAUTHORED_MENTORSHIP`
- `SAFEGUARD_ENABLED_AGENCY`
- `PLURAL_IDOL_INSTITUTIONALITY`
- `EVALUATIVE_REGIME_PLURALISM`
- `NON_EXCLUSIVE_INSTITUTIONAL_LEGITIMACY`

Open-register changes:

- `OPEN-03`: advanced, still open.
- `OPEN-05`: advanced, still open.
- `OPEN-07`: strongly advanced.
- old `OPEN-08` split:
  - `OPEN-08A`: age compatibility with genuine idolhood — **strongly resolved yes**;
  - `OPEN-08B`: mainstream material/professional longevity across a very long adult lifespan — **open**.
- `OPEN-14`: open; conceptual age ceiling weakened.
- `OPEN-20`: E2-A1 chronology advanced.

Formal caveat:

- `event_2026_004` remains missing `adv-live-eve-2604-dice-05`; exact final-live choreography/camera/blocking/lighting/arrangement claims remain deferred.

The next tranche is **E2-A2**:

1. `event_2021_003_st-eve-2109-backside`
2. `event_2021_006_st-eve-2112-marathon`
3. `event_2025_010_st-eve-2511-race`
4. `event_2026_006_st-eve-2606-dice`

**Recommended model:** GPT-5.6 Sol  
**Recommended reasoning:** Extra High
## 10.16 Event E2-A2 close-read freeze — 2026-08-15

The second E2 close-read tranche is complete, prospectively frozen before historical comparison, adversarially audited, and admitted through a successor baseline.

Audited sources:

1. `event_2021_003_st-eve-2109-backside` — **芽吹く黒ユリの蕾**
2. `event_2021_006_st-eve-2112-marathon` — **羽休む聖夜のサプライズ**
3. `event_2025_010_st-eve-2511-race` — **let's 湯けむり dancing！**
4. `event_2026_006_st-eve-2606-dice` — **羽ばたけ！恩返しのAile**

Governing artifacts:

- `IDOLY_PRIDE_V2_PHASE1B_EVENT_E2A2_PRIMARY_FINDINGS_FREEZE.md`
- `IDOLY_PRIDE_V2_PHASE1B_EVENT_E2A2_CLOSE_READ_AUDIT.md`
- `IDOLY_PRIDE_V2_PHASE1B_POST_EVENT_E2A2_BASELINE.md`
- `IDOLY_PRIDE_V2_PHASE1B_EVENT_E2A2_SHA256SUMS.txt`

Principal admitted additions:

- `EMERGENT_UNIT_IDENTITY`
- `CONSTITUTIVE_SUCCESSION`
- `DISTRIBUTED_CREATIVE_AUTHORITY`
- `INFLUENCE_WITHOUT_DERIVATIVENESS`
- `NON_PERFORMATIVE_RECOGNITION`
- `RECIPROCAL_GRATITUDE_CYCLE`
- `BENEVOLENT_RECIPROCITY_PRESSURE`
- `PROTECTED_LEISURE_AS_PROFESSIONAL_INFRASTRUCTURE`
- `STEWARDSHIP_THROUGH_WAITING`
- `RIVAL_INFRASTRUCTURE_WITHOUT_ASSIMILATION`

Principal constitutional result:

> **A mature unit remains itself by making change answerable to the people who constitute it.**

LizNoir result:

- Rio/Aoi remain the privileged founding dyad;
- Ai/Kokoro are fully constitutive members;
- successor legitimacy includes standing to reinterpret inherited work;
- later members can alter the founders as well as inherit from them;
- `LizNoir-like` identity is relationally emergent from the four members rather than a fixed external style template.

TRINITYAiLE result:

- Sumire's value does not need to be re-earned through successful proof displays;
- Hoshimi/BanPro workload contrast adds direct evidence to institutional-care analysis;
- gratitude is repeatable rather than a debt discharged once;
- gratitude can itself become overbearing when the giver tries to control how it is received;
- self-authorship remains compatible with composers, venues, management, and rival infrastructure;
- influence from other artists does not negate originality when consciously authored into the unit's own work.

Open-register effects:

- `OPEN-03`: advanced via `STEWARDSHIP_THROUGH_WAITING`; acute intervention remains open.
- `OPEN-05`: advanced via workload/rest evidence; remains open.
- `OPEN-06`: remains `USEFUL_BUT_NOT_NECESSARY`; DoriKyun rival infrastructure added.
- `OPEN-12`: BanPro ethics materially advanced; remains open.
- `OPEN-13`: mature four-person LizNoir continuity strengthened; aging remains open.
- `OPEN-16`: major conceptual advance through emergent identity and influence-without-derivativeness.
- `OPEN-20`: E2-A2 chronology advanced.

Formal caveat:

- `event_2026_006` remains missing `adv-live-eve-2606-dice-05`; exact final-live choreography/camera/blocking/lighting/arrangement claims remain deferred.

The next tranche is **E2-A3 — Multiple vocations, family lineage, and institutional scale**:

1. `event_2023_008_st-eve-2308-marathon-raid` — **おしごとシークレット**
2. `event_2024_009_st-eve-2409-marathon-raid` — **開演！ぷりてぃー★エンジェル**
3. `event_2025_006_st-eve-2507-race` — **星見プロ全国ツアー　Stars Journey**
4. `event_2025_009_st-eve-2510-marathon-raid` — **私達の青春謳歌～DOTABATA SCHOOL FESTIVAL～**

**Recommended model:** GPT-5.6 Sol  
**Recommended reasoning:** Extra High

## 10.17 Event E2-A3 close-read freeze — 2026-08-16

The third post-E1 E2 tranche is complete and frozen through:

- `IDOLY_PRIDE_V2_PHASE1B_EVENT_E2A3_PRIMARY_FINDINGS_FREEZE.md`
- `IDOLY_PRIDE_V2_PHASE1B_EVENT_E2A3_CLOSE_READ_AUDIT.md`
- `IDOLY_PRIDE_V2_PHASE1B_POST_EVENT_E2A3_BASELINE.md`

Admitted events:

1. `event_2023_008_st-eve-2308-marathon-raid` — **おしごとシークレット**
2. `event_2024_009_st-eve-2409-marathon-raid` — **開演！ぷりてぃー★エンジェル**
3. `event_2025_006_st-eve-2507-race` — **星見プロ全国ツアー　Stars Journey**
4. `event_2025_009_st-eve-2510-marathon-raid` — **私達の青春謳歌～DOTABATA SCHOOL FESTIVAL～**

Principal admitted additions:

- `NON_TOTALIZING_VOCATION`
- `PLURAL_ROLE_AUTHORSHIP`
- `PRIVATE_CREATIVE_VOCATION`
- `SELECTIVE_DISCLOSURE_WITHOUT_SHAME`
- `ANTICIPATORY_SELF_DISQUALIFICATION`
- `INHERITED_CAPACITY_WITHOUT_INHERITED_VOCATION`
- `PEDIGREE_NON_TRANSFERABILITY`
- `TRANSFORMATIVE_FIDELITY`
- `VOLUNTARY_REENTRY_INTO_LINEAGE`
- `SCALABLE_PLURAL_INSTITUTION`
- `RECIPROCAL_MANAGERIAL_SUPPORT`
- `REPRESENTATIVE_CREATIVE_GOVERNANCE`
- `NON_SOVEREIGN_LEADERSHIP`
- `PLURAL_PROTAGONISM`
- `TIME_BOUNDED_LIFE_DOMAIN`
- `CIVIC_PROTAGONISM`
- `ROLE_ACCUMULATION_RISK`
- `ORDINARY_LIFE_RECOVERY`
- `FAME_DISTANCE`
- `CROSS_ROLE_FERTILIZATION`

Principal tranche result:

> **Idolhood can be a central chosen vocation without acquiring total jurisdiction over the person.**

Institutional result:

> `OPEN-04` is **RESOLVED AT THE ONTOLOGICAL LEVEL**: Hoshimi is a professional institution. Home/family language remains relational metaphor, not a complete governance description.

Authenticity result:

> **Authenticity does not require compulsory transparency.** Yu may cease treating fandom/doujin work as shameful while retaining authority over whether the doujin practice becomes public identity.

Family-lineage result:

> **Inheritance may transmit resources and capacities without predetermining vocation or transferring competence.** Voluntary re-entry into parental expertise is compatible with self-authorship.

Hoshimi-scale result:

> **Pluralism at national scale is sustained by representative procedure, distributed expertise, reciprocal support, and material logistics—not affection alone.**

Ordinary-life result:

> **Professional seriousness does not automatically outrank time-bounded student life.** Kotono and Nagisa treat school participation as a real domain of belonging; Yu extends this into civic leadership.

Workload result:

> **Chosen work can still become unsustainable work.** `ROLE_ACCUMULATION_RISK` is now a longitudinal subproblem under `OPEN-05`.

Historical comparison produced one notable precision correction: prior shorthand that Yu's doujin identity becomes something she can stand “openly” with is revised. The mature endpoint is **shame reduction plus selective disclosure**, not total publicity.

Formal dependencies carried forward:

- `event_2023_008` → missing `adv-live-eve-2308-marathon-raid-05`
- `event_2025_009` → missing `adv-live-eve-2510-marathon-05`

The next tranche is **E2-B1 — Guilt, center extension, performed role, and late IIIX media**:

1. `event_2022_002_st-eve-2202-marathon` — **心愛溶けるビターチョコレート**
2. `event_2023_001_st-eve-2301-contest` — **最高優美＊飛躍のカウントダウン**
3. `event_2025_004_st-eve-2504-marathon-raid` — **旗揚げ！劇団★見～二人のアリスとWONDERLAND～**
4. `event_2026_001_st-eve-2601-race` — **新春万福　素顔の晒し合いGAME**

**Recommended model:** GPT-5.6 Sol  
**Recommended reasoning:** Extra High

## 10.18 Event E2-B1 close-read freeze — 2026-08-16

The first E2-B material-extension tranche is complete, prospectively frozen before historical comparison, adversarially audited, and admitted through a successor baseline.

Audited sources:

1. `event_2022_002_st-eve-2202-marathon` — **心愛溶けるビターチョコレート**
2. `event_2023_001_st-eve-2301-contest` — **最高優美＊飛躍のカウントダウン**
3. `event_2025_004_st-eve-2504-marathon-raid` — **旗揚げ！劇団★見～二人のアリスとWONDERLAND～**
4. `event_2026_001_st-eve-2601-race` — **新春万福　素顔の晒し合いGAME**

Governing artifacts:

- `IDOLY_PRIDE_V2_PHASE1B_EVENT_E2B1_PRIMARY_FINDINGS_FREEZE.md`
- `IDOLY_PRIDE_V2_PHASE1B_EVENT_E2B1_CLOSE_READ_AUDIT.md`
- `IDOLY_PRIDE_V2_PHASE1B_POST_EVENT_E2B1_BASELINE.md`
- `IDOLY_PRIDE_V2_PHASE1B_EVENT_E2B1_SHA256SUMS.txt`

Principal admitted additions:

- `ANSWERABLE_ROLE_CONSTITUTION`
- `GUILT_CAUSAL_OVERREACH`
- `UNILATERAL_REPARATIVE_OVERWORK`
- `PROTECTIVE_GUILT_MONOPOLIZATION`
- `FUTURE_FACING_REPAIR`
- `REPAIR_WITHOUT_DEBT_OWNERSHIP`
- `CONTESTABLE_CENTER_OFFICE_LIZNOIR`
- `SENIORITY_NON_OWNERSHIP`
- `CONTINGENT_CENTER_DELEGATION`
- `CENTER_AS_BURDENED_RESPONSIBILITY`
- `SCAFFOLDED_PROFESSIONAL_EXPERIMENTATION`
- `PLURAL_ROLE_FIT`
- `RECIPROCAL_ABILITY_RECOGNITION`
- `COMPARATIVE_SELF_DISQUALIFICATION`
- `FORM_ADAPTATION_TO_PERFORMERS`
- `DUAL_PROTAGONISM`
- `NON_ZERO_SUM_CASTING`
- `ROLE_MEDIATED_RELATIONAL_TRUTH`
- `CO_PRODUCED_LIVENESS`
- `STRATEGIC_AUTHENTICITY`
- `CURATED_ADVERSARIAL_AUTHENTICITY`
- `TRUST_WITHOUT_FRIENDSHIP_LABEL`
- `AUDIENCE_RELATIONAL_REFRAMING`

Principal tranche result:

> **A role is not made ethical by disappearing. It is made ethical by losing the power to become unquestionable ownership of the person.**

Kokoro result:

> **A real mistake can warrant apology and changed practice without becoming an unlimited debt over future labor.** Her old collision with Rio contributed to Aoi's ankle injury, but Aoi explicitly rejects the injury as the cause of LizNoir's defeat. Kokoro's later overwork is therefore read as `GUILT_CAUSAL_OVERREACH` and `UNILATERAL_REPARATIVE_OVERWORK`, not as repayment the seniors demand.

Center result:

> **LizNoir joins Tsuki in treating center as a contestable professional office.** Aoi explicitly rejects seniority ownership; Rio allows challenges and accepts performance-based testing of her continued legitimacy; Kokoro can receive contingent delegation. `OPEN-15` is resolved for Tsuki + LizNoir, while universal cross-unit generalization remains open.

Role/form result:

> **Not all competition needs a single winner.** Shizuku and Suzu remain distinct performers, but the Alice production changes form to preserve both valid interpretations. The ledger therefore distinguishes `CONTESTABLE_SINGULAR_OFFICE` from `ADAPTABLE_PLURAL_ROLE`.

Authenticity result:

> **IIIX's mature authenticity remains constructed and strategic.** The unit stops imitating Hoshimi-style ordinary warmth and publicly curates its own adversarial relational grammar while preserving editing and privacy boundaries. miho explicitly names `信頼` while denying `友情`, supporting `TRUST_WITHOUT_FRIENDSHIP_LABEL`. Audience interpretation remains co-produced rather than wholly controlled by performers.

Open-register effects:

- `OPEN-03`: advanced through `SCAFFOLDED_PROFESSIONAL_EXPERIMENTATION`; remains open.
- `OPEN-05`: strongly advanced through guilt-driven overwork and IIIX self-authored media/live overwork; remains open.
- `OPEN-15`: resolved for Tsuki and LizNoir; universal claim open.
- `OPEN-16`: major advance through role-mediated truth, strategic authenticity, curated adversarial authenticity, and answerable construction; remains open at full-series scale.
- `OPEN-20`: E2-B1 chronology advanced.

Formal dependencies:

- `event_2023_001` → missing `adv-live-eve-2301-contest-005`
- `event_2026_001` → missing `adv-live-eve-2601-race-05`

Exact choreography/camera/blocking/lighting/unstated arrangement claims remain deferred for those sequences.

The duplicate working-ledger section label previously attached to E2-A3 (`10.14`) is normalized to `10.17` in v1.16; this is a numbering correction only and does not change frozen E2-A3 analytical content.

The next tranche is **E2-B2 — Limited-unit identity and secondary mature-professional tests**:

1. `event_2022_005_st-eve-2205-race` — **心紡ぎ合う輝きの競演**
2. `event_2023_010_st-eve-2310-race` — **迷走ピリオド 涼やかな青春**
3. `event_2024_003_st-eve-2403-race` — **笑顔のSUNNY 繋げるPEACE**
4. `event_2025_001_st-eve-2501-race` — **迎春！翼に込める躍進の一念**

**Recommended model:** GPT-5.6 Sol  
**Recommended reasoning:** Extra High

## 10.19 Event E2-B2 close-read freeze — 2026-08-16

The second E2-B material-extension tranche is complete, prospectively frozen before historical comparison, adversarially audited, and admitted through a successor baseline.

Audited sources:

1. `event_2022_005_st-eve-2205-race` — **心紡ぎ合う輝きの競演**
2. `event_2023_010_st-eve-2310-race` — **迷走ピリオド 涼やかな青春**
3. `event_2024_003_st-eve-2403-race` — **笑顔のSUNNY 繋げるPEACE**
4. `event_2025_001_st-eve-2501-race` — **迎春！翼に込める躍進の一念**

Governing artifacts:

- `IDOLY_PRIDE_V2_PHASE1B_EVENT_E2B2_PRIMARY_FINDINGS_FREEZE.md`
- `IDOLY_PRIDE_V2_PHASE1B_EVENT_E2B2_CLOSE_READ_AUDIT.md`
- `IDOLY_PRIDE_V2_PHASE1B_POST_EVENT_E2B2_BASELINE.md`
- `IDOLY_PRIDE_V2_PHASE1B_EVENT_E2B2_SHA256SUMS.txt`

Principal admitted additions:

- `RECIPROCAL_STANDING`
- `RECIPROCAL_SELF_ERASURE`
- `SIBLING_ROLE_DETOTALIZATION`
- `RECIPROCAL_SISTER_SUPPORT`
- `SUPPORT_COMPETENCE_WITHOUT_SUPPORT_DESTINY`
- `ASSERTIVE_MUTUALITY`
- `NON_ZERO_SUM_SIBLING_AMBITION`
- `CONFLICT_TOLERANT_AFFECTION`
- `REVISION_WHILE_RELATIONSHIP_IS_LIVE`
- `SHARED_LABEL_DIVERGENT_MEANING`
- `UNILATERAL_OTHER_OPTIMIZATION`
- `JEALOUSY_AS_AUTHORSHIP_SIGNAL`
- `KINDNESS_ACCUMULATION_RISK`
- `TRUSTED_CONFLICT_CAPACITY`
- `RECIPROCAL_VULNERABILITY_DISCLOSURE`
- `COAUTHORED_UNIT_SYNTHESIS`
- `MUTUALITY_OVER_OPTIMIZATION`
- `RECIPROCAL_AUDIENCE_COAUTHORSHIP`
- `CIRCULATING_DREAM_RECIPROCITY`
- `FAME_SCALE_EXTERNALITY`
- `INTERGENERATIONAL_IDOL_MODELING`
- `PRESENTLY_AUTHORED_CONTINUATION_COMMITMENT`
- `GENERATIVE_AUDIENCE_CIRCULATION`
- `CARE_RECEPTION_GAP`
- `DEVELOPMENTAL_ASYMMETRY_WITHOUT_STATUS_SUBORDINATION`
- `AGE_AWARE_EQUAL_STANDING`
- `STATUS_PROVING_RISK_TAKING`
- `REFLEXIVE_CARE_REVISION`
- `ACCOMPANIMENT_WITHOUT_GOAL_SEIZURE`
- `PROPORTIONAL_CARE_INTERVENTION`
- `MEANINGFUL_SUCCESS_BEYOND_RANK`
- `RETURN_CAPABLE_EQUALITY`
- `RECIPROCAL_CARE_REVERSIBILITY`

Principal tranche result:

> **Mature interdependence requires reciprocal standing: asymmetries can remain real while all affected parties retain standing to want, answer, contest, contribute care, and alter the shared form.**

Shiraishi-sister result:

> **Support competence is not support destiny.** Saki and Chisa initially erase both performers through mutual accommodation; the repaired sisterhood lets both claim visibility and ambition without making affection conditional on yielding.

Mei/Suzu result:

> **The limited unit becomes shared when neither member is merely the optimized object of the other's care.** Historical “effort versus intuition” remains useful as Suzu's experienced wound but is revised as a complete narrator-level account. Their durable gain is conflict-capable co-authorship.

Sunny Peace result:

> **Sunny's warmth is reciprocal and generative at national scale, but fame also creates externalities.** Fan dreams become structured inputs to professional activity; fan encounters can generate new aspirations; popularity changes public space and ordinary anonymity. Audience coauthorship is therefore meaningful but bounded.

TRINITYAiLE result:

> **Equal membership does not require identical risk assumptions.** E2-B2 distinguishes age-aware safeguards from status subordination and adds `PROPORTIONAL_CARE_INTERVENTION`: intervention intensity should rise with credible risk, impairment, and loss of decision capacity rather than caregiver anxiety alone.

Open-register effects:

- `OPEN-01`: advanced by Sakura's present continuation commitment; future authorship remains open.
- `OPEN-03`: strongly advanced by the Mana-collapse/Sumire-marathon contrast; universal threshold remains open.
- `OPEN-05`: advanced by reciprocal self-erasure and status-proving risk; open.
- `OPEN-07`: strongly advanced through `MEANINGFUL_SUCCESS_BEYOND_RANK`.
- `OPEN-14`: advanced by Haruko as an intergenerational professional model; long-horizon economics remain open.
- `OPEN-15`: no constitutional change; Saki's explicit center desire strengthens Tsuki psychology.
- `OPEN-16`: minor role-detotalization advance; open at full-series scale.
- `OPEN-20`: E2-B2 chronology advanced.

Formal dependency:

- `event_2024_003` → missing `adv-live-eve-2403-race-05`

Exact Sunny live choreography/camera/blocking/lighting/costume-motion/unstated-arrangement claims remain deferred.

The next tranche is **E2-C1 — Important precursors now heavily overlapped by E1**:

1. `event_2023_004_st-eve-2304-marathon-raid` — **音色の輝石が紡ぐ未来**
2. `event_2024_004_st-eve-2404-dice` — **不屈のChallenger～Roll the dice～**

Use primarily for comparative-distance relapse and early IIIX overseas/Hoshimi-contract chronology. Explicitly distinguish unique precursor evidence from propositions now better established by E1.

**Recommended model:** GPT-5.6 Sol  
**Recommended reasoning:** Extra High

## 10.20 Event E2-C1 close-read freeze — 2026-08-16

The precursor-overlap E2-C1 tranche is complete, prospectively frozen before historical comparison, adversarially audited, and admitted through a successor baseline.

Audited sources:

1. `event_2023_004_st-eve-2304-marathon-raid` — **音色の輝石が紡ぐ未来**
2. `event_2024_004_st-eve-2404-dice` — **不屈のChallenger～Roll the dice～**

Governing artifacts:

- `IDOLY_PRIDE_V2_PHASE1B_EVENT_E2C1_PRIMARY_FINDINGS_FREEZE.md`
- `IDOLY_PRIDE_V2_PHASE1B_EVENT_E2C1_CLOSE_READ_AUDIT.md`
- `IDOLY_PRIDE_V2_PHASE1B_POST_EVENT_E2C1_BASELINE.md`
- `IDOLY_PRIDE_V2_PHASE1B_EVENT_E2C1_SHA256SUMS.txt`

Principal admitted additions:

- `PRECURSOR_AUTHORITY_WITHOUT_MATURE_SUPREMACY`
- `COMPARATIVE_STATUS_DISTANCE`
- `COMPETITIVE_PROXIMITY_INHIBITED_DISCLOSURE`
- `INTERGENERATIONAL_COMPARATIVE_DISTANCE_PATTERN`
- `INTERGENERATIONAL_REPAIR_TECHNIQUE_TRANSMISSION`
- `NON_EXTRACTIVE_RECONNECTION`
- `COMPARATIVE_AVOIDANCE`
- `RECIPROCAL_RIVAL_ANXIETY`
- `RELATIONAL_REPAIR_WITHOUT_COMPARATIVE_CURE`
- `OUTCOME_DEPENDENCE_RECURSION`
- `DEFERRED_PARTICIPATION_IN_INHERITANCE`
- `HOSHIMI_CONTRACTUAL_SCAFFOLD_WITH_UNIT_AUTONOMY`
- `UNIT_PRESERVING_OPPORTUNITY_EXPANSION`
- `NONPORTABLE_PRESTIGE`
- `IMMEDIATE_VICTORY_JUSTIFICATION`
- `TALENT_JUSTIFIED_ADVERSARIAL_COALITION`
- `PREEXISTING_GLOBAL_AMBITION`
- `STRATEGIC_STATUS_MISREPRESENTATION`
- `PERFORMANCE_BACKED_STATUS_BOOTSTRAPPING`
- `TRANSNATIONAL_REPUTATION_FEEDBACK_LOOP`
- `SUCCESS_CONDITIONED_RELATIONAL_SECURITY`

Principal tranche result:

> **Earlier sources remain authoritative for chronology and developmental mechanism even when later E1 evidence provides the stronger mature formulation.** E2-C1 is therefore retained as precursor authority rather than promoted to mature-thesis supremacy or demoted to redundancy.

Sakura/Kotono result:

> **Relational repair does not automatically cure comparative outcome-dependence.** Kotono can restore normal communication with Sakura, make jealousy speakable, and reauthorize rivalry while still ending the event convinced that she needs more results because the Sunny/Tsuki professional gap remains.

Intergenerational repair result:

> **Mana's earlier low-pressure curry reconnection with Haruko becomes a care technique transmitted Haruko → Sakura.** Sakura's tonkatsu outing is significant because disclosure is not made the price of the care; the outing would still matter if Kotono never confessed. Haruko's later participation in Mana's future-facing song intention also supports `DEFERRED_PARTICIPATION_IN_INHERITANCE`.

Early IIIX result:

> **IIIX already has Hoshimi contractual/negotiating scaffolding and global ambition before the later U.S. crisis, but its own reason for togetherness is still victory-conditioned.** miho's `今勝たなくては、私達が一緒にいる意味はない` is preserved as `IMMEDIATE_VICTORY_JUSTIFICATION`, an earlier constitution later transformed by E1-D/E1-E rather than a timeless IIIX doctrine.

Authenticity result:

> **Effective strategic construction is not automatically authentic.** The Las Vegas “Japan's top idols” tactic begins from a knowingly misleading status claim and planted hype; the ensuing performance success and real opportunity do not retroactively make the original claim true. This counterexample strengthens the later `answerable construction` model by showing why strategy, editing, commerce, and successful reception are insufficient on their own.

Open-register effects:

- `OPEN-05`: advanced through persistent internal comparative/result pressure; remains open.
- `OPEN-07`: minor cross-market advance through `NONPORTABLE_PRESTIGE`; strongly advanced overall.
- `OPEN-10`: IIIX/Hoshimi chronology strengthened; mature autonomy state unchanged.
- `OPEN-16`: advanced by a deceptive-strategy counterexample; answerable construction remains the preferred mature formulation.
- `OPEN-20`: chronology advanced through E2-C1.

Priority result:

- `event_2023_004` — retain `IMPORTANT`; not redundant; preferred for comparative-distance rupture/repair chronology and residual outcome-dependence.
- `event_2024_004` — retain `IMPORTANT`; not redundant; preferred for early IIIX overseas/Hoshimi-contract chronology, nonportable prestige, and pre-crisis unit constitution.

Formal dependency:

- `event_2024_004` → missing `adv-live-eve-2404-dice-05`

Exact Las Vegas live choreography/camera/blocking/lighting/costume-motion/unstated-arrangement claims remain deferred.

SUPPORT-DEFERRED is now complete. Final routing result:

- all four sources remain `SUPPORT` and independently retrievable;
- none is `REDUNDANT`;
- mature thesis ownership remains with stronger E1/E2 evidence where routed;
- unique retained mechanisms include `AFFINITY_BASED_INHERITANCE`, `ANNIVERSARY_REAUTHORING_WITHOUT_ERASURE`, `ADVERSARIAL_GRAMMAR_WITH_REAL_FRICTION`, `INVISIBLE_UNIT_MAINTENANCE_LABOR`, `LIVE_MEDIA_LEVERAGE`, and `AUTHENTICITY_WITHOUT_ETHICAL_EXONERATION`.

The next architecture-defined operation is **Phase 1B Event Close Read — E3: SUPPORT MINING**, in frozen queue order:

1. `event_2023_003_st-eve-2303-race` — **ぱじゃまパーティー！～夢見る少女と眠り姫～**
2. `event_2023_002_st-eve-2302-marathon-raid` — **守れ！純潔のベーゼ～imposition of love～**
3. `event_2025_002_st-eve-2502-marathon-raid` — **感謝を伝えるLovely Valentine's Day**
4. `event_2021_001_st-eve-2107-tour` — **雨上がりの太陽と共に**
5. `event_2022_006_st-eve-2206-marathon` — **導きのファンファーレ**
6. `event_2022_008_st-eve-2208-backside` — **熱中☆ハプニングサマー**
7. `event_2022_001_st-eve-2201-contest` — **昇る初陽に咲く笑顔**

Use E3 for bounded support mining rather than mature-thesis inflation. Freeze source-native findings before historical comparison.

**Recommended model:** GPT-5.6 Sol  
**Recommended reasoning:** Extra High


## 10.21 Event E3 support-mining freeze — 2026-08-16

The seven-source E3 support-mining tranche is complete, prospectively frozen before historical comparison, adversarially audited, and admitted through a successor baseline.

Audited sources, in the frozen routing order:

1. `event_2023_003_st-eve-2303-race` — **ぱじゃまパーティー！～夢見る少女と眠り姫～**
2. `event_2023_002_st-eve-2302-marathon-raid` — **守れ！純潔のベーゼ～imposition of love～**
3. `event_2025_002_st-eve-2502-marathon-raid` — **感謝を伝えるLovely Valentine's Day**
4. `event_2021_001_st-eve-2107-tour` — **雨上がりの太陽と共に**
5. `event_2022_006_st-eve-2206-marathon` — **導きのファンファーレ**
6. `event_2022_008_st-eve-2208-backside` — **熱中☆ハプニングサマー**
7. `event_2022_001_st-eve-2201-contest` — **昇る初陽に咲く笑顔**

Governing artifacts:

- `IDOLY_PRIDE_V2_PHASE1B_EVENT_E3_PRIMARY_FINDINGS_FREEZE.md`
- `IDOLY_PRIDE_V2_PHASE1B_EVENT_E3_CLOSE_READ_AUDIT.md`
- `IDOLY_PRIDE_V2_PHASE1B_POST_EVENT_E3_BASELINE.md`
- `IDOLY_PRIDE_V2_PHASE1B_EVENT_E3_SHA256SUMS.txt`

Principal archival rule:

> **`SUPPORT_MINING_WITHOUT_CONCEPT_INFLATION`** — lower-priority evidence remains canonical when it sharpens chronology, mechanism, counterexample, or texture, but does not take mature-thesis ownership away from stronger sources without a genuine model-changing result.

Principal admitted additions:

- `EMULATION_WITHOUT_SELF_ERASURE`
- `ORDINARY_SELF_AS_PROFESSIONAL_RESOURCE`
- `PERFORMED_INTIMACY_WITHOUT_PRIVATE_CLAIM`
- `PRIVATE_LIFE_JURISDICTION_RESTRAINT`
- `COMPARATIVE_INSECURITY_AS_PEER_RECOGNITION`
- `PLACE_REAUTHORING_WITHOUT_ERASURE`
- `PARTICIPATORY_PRODUCTION_AS_PERFORMANCE_KNOWLEDGE`
- `REST_AS_CREATIVE_INFRASTRUCTURE`
- `ORIGIN_COMMUNITY_RECIPROCITY`
- `NON_WORK_RELATIONAL_INTEGRATION`
- `GENRE_EXPECTATION_REFUSAL`

Priority result:

- all seven E3 sources remain `SUPPORT`;
- none is `REDUNDANT`;
- none is promoted above the mature E1/E2 source that already owns the relevant broad thesis;
- historical transitions are predominantly `PRESERVE`, `STRENGTHEN`, and `REVISE_BY_PRECISION`.

Formal dependencies:

- `event_2023_003` → missing `adv-live-eve-2303-race-005`
- `event_2025_002` → missing `adv-live-eve-2502-marathon-05`

The next architecture-defined operation is **Phase 1B Event Close Read — E4: INDEXED / SELECTIVE / CAVEATED**. The E4 tranche must preserve explicit crossover/canon caveats and should not assume equal evidentiary weight across all eleven sources.

**Recommended model:** GPT-5.6 Sol  
**Recommended reasoning:** Extra High

## 10.22 Event E4 indexed/selective/caveated freeze — 2026-08-16

The final eleven-event E4 tranche is complete, prospectively frozen before historical comparison, adversarially audited, canon-weighted, and admitted/routed through a successor baseline.

Audited sources, in frozen order:

1. `event_2022_009_st-eve-2209-contest` — **未来とつながるマジカルメロディ** — crossover caveated
2. `event_2023_012_st-eve-2312-contest` — **君と輝くサンシャイン!!** — crossover caveated
3. `event_2024_002_st-eve-2402-contest` — **未来を彩るスノーフェスティバル** — crossover caveated
4. `event_2025_008_st-eve-2509-contest` — **未来へ続く夏祭り** — crossover caveated
5. `event_2021_002_st-eve-2108-tour` — **月夜に輝く恋の魔法** — mainline support
6. `event_2024_001_st-eve-2401-race` — **にゃんか不思議なお正月！？** — mainline support/texture
7. `event_2023_005_st-eve-2305-race` — **きょうえん！HTT＆HMA～放課後ティータイム＆星見アンバサダー～** — crossover caveated
8. `event_2024_012_st-eve-2412-contest` — **心跳ねるクリスマスパーティー** — crossover caveated
9. `event_2025_003_st-eve-2503-dice` — **SOS！星見プロダクションの転送～ただのアイドルには興味ありません！？～** — crossover caveated
10. `event_2025_011_st-eve-2512-dice` — **ドタバタ！？トラブルクリスマス！** — crossover caveated
11. `event_2026_005_st-eve-2605-marathon-raid` — **ハロー！アイドル♪ 夢でつながるミラクルステージ** — crossover caveated

Governing artifacts:

- `IDOLY_PRIDE_V2_PHASE1B_EVENT_E4_PRIMARY_FINDINGS_FREEZE.md`
- `IDOLY_PRIDE_V2_PHASE1B_EVENT_E4_CLOSE_READ_AUDIT.md`
- `IDOLY_PRIDE_V2_PHASE1B_POST_EVENT_E4_BASELINE.md`
- `IDOLY_PRIDE_V2_PHASE1B_EVENT_E4_SHA256SUMS.txt`

Principal archival rules:

> **`INTERPRETIVE_VALUE_WITHOUT_CONTINUITY_AUTHORITY`** — a caveated source may be analytically rich without possessing authority to establish ordinary mainline chronology, ontology, relationships, institutions, or developmental state.

> **`CROSSOVER_CORROBORATION_REQUIRES_MAINLINE_HOME`** — crossover material can corroborate a proposition when a non-crossover source owns it; otherwise the proposition remains event-local or analogical.

Principal uncaveated additions:

- `AESTHETIC_SELF_DIFFERENTIATION`
- `IMAGINED_INTIMACY_AS_PERFORMANCE_MATERIAL`
- `ROMANTIC_LANGUAGE_WITHOUT_ROMANTIC_IDENTITY`
- additional support for Tsuki five-person non-disposable standing

Authority result:

- **2 E4 sources** are admitted as ordinary `SUPPORT`;
- **9 E4 crossover sources** are indexed with explicit corroborative/analogical/event-local/non-transferable routes;
- no crossover supernatural mechanism is admitted into mainline ontology;
- all **60/60 event bundles** now have explicit semantic audit/routing treatment.

Historical-priority correction:

Strong crossover interpretations such as Snow Miku/LizNoir and Miku/Tsuki are preserved where persuasive, but thematic richness no longer implies ordinary continuity authority. Earlier historical prose that already called Haruhi, Rabbit House, or Sanrio lighter canon is formalized rather than discarded.

A Tier-H kana-card analysis appears to independently reuse the Sanrio amusement-park memory. Because cards have not yet been V2-audited, this remains `OPEN_VERIFY_KANA_CARD_CORROBORATION` and may not backfill the current event checkpoint.

Formal dependencies:

- `event_2022_009` → missing `adv-live-eve-2209-contest-005`
- `event_2023_012` → missing `adv-live-eve-2312-contest-05`
- `event_2024_002` → missing `adv-live-eve-2402-contest-05`
- `event_2025_008` → missing `adv-live-eve-2509-contest-05`
- `event_2024_012` → missing `adv-live-eve-2412-contest-05`

Exact live choreography/camera/blocking/lighting/costume-motion/visual-composition/unstated-arrangement claims remain deferred.

The next method-defined Phase-1 source operation is **Bond Story Priority and Sampling Audit (20 bond bundles)**. Event-layer completion does not waive the method's requirement to sample/rerank bond, special, card, and message layers before Phase 1 closes.

**Recommended model:** GPT-5.6 Sol  
**Recommended reasoning:** Extra High

## 10.23 Bond priority and sampling audit — 2026-08-16

All **20 raw bond bundles / 160 granular bond stories** have been sampled and reranked against the complete post-E4 Tier-A + event model. This is a **routing-only** operation. No bond claim is admitted into the governing analytical state.

Governing routing artifacts:

- `IDOLY_PRIDE_V2_PHASE1_BOND_PRIORITY_AND_SAMPLING_AUDIT.md`
- `IDOLY_PRIDE_V2_PHASE1_BOND_CLOSE_READ_QUEUE.md`
- `IDOLY_PRIDE_V2_PHASE1_BOND_PRIORITY_AND_SAMPLING_SHA256SUMS.txt`

Priority correction from uniform Pass-A `IMPORTANT`:

- `CORE / B1`: `bond_kan_001_kan`, `bond_ktn_001_ktn`, `bond_kor_001_kor`;
- `IMPORTANT / B2`: `bond_szk_001_szk`, `bond_rui_001_rui`, `bond_mhk_001_mhk`, `bond_hrk_001_hrk`, `bond_smr_001_smr`, `bond_rio_001_rio`, `bond_ski_001_ski`, `bond_skr_001_skr`, `bond_rei_001_rei`;
- `SUPPORT / B3`: `bond_aoi_001_aoi`, `bond_chs_001_chs`, `bond_kkr_001_kkr`, `bond_ngs_001_ngs`, `bond_suz_001_suz`;
- `TEXTURE / B4`: `bond_ai_001_ai`, `bond_mei_001_mei`, `bond_yu_001_yu`.

Routing principle:

> **`PRIVATE_SCALE_DOES_NOT_EQUAL_LOW_IMPACT`** — private/low-pressure material can deserve early close reading when it uniquely exposes family memory, private aspiration, manager–idol reciprocity, relationship asymmetry, professional future planning, or persistence of a wound after public resolution. Ordinary comedy remains searchable without automatic promotion.

The current analytical baseline remains `IDOLY_PRIDE_V2_PHASE1B_POST_EVENT_E4_BASELINE.md`.

Next operation:

> **Phase 1 Bond Close Read — B1-A: Private identity, inheritance, and future vocation**
> `bond_kan_001_kan` → `bond_ktn_001_ktn` → `bond_kor_001_kor`

**Recommended model:** GPT-5.6 Sol  
**Recommended reasoning:** Extra High

## 10.24 Bond B1-A close-read freeze — 2026-08-16

The first mandatory bond close-read tranche is complete and frozen in routing order:

1. `bond_kan_001_kan` — kana;
2. `bond_ktn_001_ktn` — 長瀬琴乃;
3. `bond_kor_001_kor` — fran.

Governing artifacts:

- `IDOLY_PRIDE_V2_PHASE1_BOND_B1A_PRIMARY_FINDINGS_FREEZE.md`;
- `IDOLY_PRIDE_V2_PHASE1_BOND_B1A_CLOSE_READ_AUDIT.md`;
- `IDOLY_PRIDE_V2_PHASE1_POST_BOND_B1A_BASELINE.md`;
- `IDOLY_PRIDE_V2_PHASE1_BOND_B1A_SHA256SUMS.txt`.

Source volume: **24 granular bond stories / 1,000 utterances**. No B1-A bond bundle declares a missing audiovisual/formal asset.

Primary private-scale additions:

- `SELECTIVE_PERSONAL_JURISDICTION`;
- `PRIVATE_SELF_IS_NOT_AUTHENTICITY_MONOPOLY`;
- `KINSHIP_WITHOUT_CONTACT_ENTITLEMENT`;
- `SELECTIVE_FAMILY_VISIBILITY_LONGING`;
- `INFORMAL_PROTECTIVE_COUNTERPOWER`;
- `PROTECTIVE_OUTCOME_DOES_NOT_RESOLVE_PROCEDURAL_ACCOUNTABILITY`;
- `DIFFERENTIATION_ENABLES_REAPPROPRIATION`;
- `POST_DIFFERENTIATION_FANDOM_RECOVERY`;
- `ORDINARY_MEMORY_REHUMANIZES_LEGACY`;
- `VOCATIONAL_OPTIONALITY_BUILDING`;
- `CROSS_ROLE_CAPITAL_CONVERSION`;
- `PRESENT_FAME_AS_FUTURE_OPTIONALITY_INFRASTRUCTURE`;
- `OPTIONALITY_IS_AN_ACTIVE_PRACTICE`;
- `LEGACY_RECEPTION_WITHOUT_DEVOTION`.

Historical correction:

- historical prose that placed kana's grandfather-contact bond **after** the U.S. father arc is downgraded to an unverified chronology inference; the raw bond provides no reliable diegetic date;
- Kotono's self-authorship is refined from movement away from Mana into differentiation that can enable freer attachment to Mana;
- fran's historical “authored persona = true persona” shorthand is revised: authorship matters, but authenticity remains constrained by answerability;
- B1-A thrift/financial calculation is not sufficient by itself to diagnose fran's current economic state.

Open-register effects:

- `OPEN-16` advanced through public/private-register evidence;
- `OPEN-18` advanced through kana's attribution of consequential behind-the-scenes protective power to Saegusa, with mechanism and legitimacy still open;
- `OPEN_VERIFY_KANA_CARD_CORROBORATION` remains open;
- new guardrail `BOND_TEMPORAL_PLACEMENT_UNFIXED` prohibits silent placement of undated bond states into event chronology.

The current lower-tier governing checkpoint is now `IDOLY_PRIDE_V2_PHASE1_POST_BOND_B1A_BASELINE.md`.

Next operation:

> **Phase 1 Bond Close Read — B2-A: Manager, public/private, and professional self**
> `bond_rui_001_rui` → `bond_skr_001_skr` → `bond_szk_001_szk` → `bond_mhk_001_mhk`

**Recommended model:** GPT-5.6 Sol  
**Recommended reasoning:** Extra High


## 10.25 Bond B2-A close-read freeze — 2026-08-16

The manager/public-private/professional-self bond tranche is complete and frozen in routing order:

1. `bond_rui_001_rui` — 天動瑠依;
2. `bond_skr_001_skr` — 川咲さくら;
3. `bond_szk_001_szk` — 兵藤雫;
4. `bond_mhk_001_mhk` — miho.

Governing artifacts:

- `IDOLY_PRIDE_V2_PHASE1_BOND_B2A_PRIMARY_FINDINGS_FREEZE.md`;
- `IDOLY_PRIDE_V2_PHASE1_BOND_B2A_CLOSE_READ_AUDIT.md`;
- `IDOLY_PRIDE_V2_PHASE1_POST_BOND_B2A_BASELINE.md`;
- `IDOLY_PRIDE_V2_PHASE1_BOND_B2A_SHA256SUMS.txt`.

Source volume: **32 granular bond stories / 1,257 utterances**. Cumulative admitted bond layer: **7/20 bundles / 56 stories / 2,257 utterances**. No B2-A bond bundle declares a missing audiovisual/formal asset. `BOND_TEMPORAL_PLACEMENT_UNFIXED` remains in force.

Primary additions:

- `BIDIRECTIONAL_PROFESSIONAL_CARE`;
- `CARE_FLOWS_ACROSS_ROLE_HIERARCHY`;
- `MANAGER_AS_CARE_RECIPIENT`;
- `MANAGERIAL_AFFIRMATION_AS_RELATIONAL_RESOURCE`;
- `RECIPROCAL_MANAGERIAL_PREPARATION`;
- `AFFECTIVE_SELF_CONSCIOUSNESS_WITHOUT_ROMANTIC_SETTLEMENT`;
- `RECIPROCAL_NUTRITIONAL_CARE`;
- `FAN_IDENTITY_PERSISTS_AFTER_PEERHOOD`;
- `DIRECT_RELATIONSHIP_SUPERSEDES_PARASOCIAL_EXTRACTION`;
- `SELF_AUTHORED_DEVOTION_OVERLOAD`;
- `UNSENTIMENTAL_AUDIENCE_RECIPROCITY`;
- `MULTIREGISTER_AUTHENTICITY`;
- `MULTIYEAR_PROFESSIONAL_CONTINUITY_MIHO`.

Historical-transition summary:

- Makino's protector/witness model is **preserved and strengthened, revised by reciprocity**: idols may care back toward him without role collapse;
- Rui's maturation toward human attachment is **preserved and strengthened**; manager-specific emotional salience is admitted, while romance remains **OPEN / DO NOT PROMOTE**;
- Sakura's reciprocal-radiance model is **preserved and specified** through bodily care for Makino;
- Shizuku's fan-to-idol thesis is **strongly strengthened**, with a new direct-access boundary around parasocial knowledge practices;
- Shizuku's workload supplies **new V2 risk evidence** that self-authored roles can accumulate beyond sustainable limits;
- miho's adult-mentor, professionalism, and public/private-register theses are **preserved and strengthened**;
- miho's private acknowledgment of long-term fans adds `UNSENTIMENTAL_AUDIENCE_RECIPROCITY`;
- 5+ years of miho career continuity is admitted only as bounded evidence and does not close long-horizon viability questions.

Open-register effects:

- `OPEN-05` materially advanced;
- `OPEN-16` advanced;
- `OPEN-08B` gains minor bounded support only;
- `OPEN-20` advances to **7/20 admitted bond bundles**.

The current lower-tier governing checkpoint is now `IDOLY_PRIDE_V2_PHASE1_POST_BOND_B2A_BASELINE.md`.

Next operation:

> **Phase 1 Bond Close Read — B2-B: Family, role, and developmental continuity**
> `bond_hrk_001_hrk` → `bond_ski_001_ski` → `bond_rei_001_rei` → `bond_smr_001_smr` → `bond_rio_001_rio`

**Recommended model:** GPT-5.6 Sol  
**Recommended reasoning:** Extra High

## 10.26 Bond B2-B close-read freeze — 2026-08-16

The family/role/developmental-continuity bond tranche is complete and frozen in routing order:

1. `bond_hrk_001_hrk` — 佐伯遙子;
2. `bond_ski_001_ski` — 白石沙季;
3. `bond_rei_001_rei` — 一ノ瀬怜;
4. `bond_smr_001_smr` — 奥山すみれ;
5. `bond_rio_001_rio` — 神崎莉央.

Governing artifacts:

- `IDOLY_PRIDE_V2_PHASE1_BOND_B2B_PRIMARY_FINDINGS_FREEZE.md`;
- `IDOLY_PRIDE_V2_PHASE1_BOND_B2B_CLOSE_READ_AUDIT.md`;
- `IDOLY_PRIDE_V2_PHASE1_POST_BOND_B2B_BASELINE.md`;
- `IDOLY_PRIDE_V2_PHASE1_BOND_B2B_SHA256SUMS.txt`.

Source volume: **40 granular bond stories / 1,572 utterances**. Cumulative admitted bond layer: **12/20 bundles / 96 stories / 3,829 utterances**. All mandatory `CORE / B1` and `IMPORTANT / B2` bond bundles are now close-read and admitted. No B2-B bundle declares a missing audiovisual/formal asset. `BOND_TEMPORAL_PLACEMENT_UNFIXED` remains the default, with `st-company-bond-rio-01-01` admitted as a local chronology exception because it explicitly states `LizNoirデビューの少し前`.

Primary additions:

- `ROLE_CONTINUITY_WITHOUT_ROLE_CAPTIVITY`;
- `CARE_FORM_CAN_CHANGE_WITHOUT_RELATIONAL_WITHDRAWAL`;
- `RELATIONAL_INFLUENCE_WITHOUT_VOCATIONAL_OWNERSHIP`;
- `ORDINARY_LIFE_AS_OPTION_SPACE`;
- `VOCATIONAL_OPPORTUNITY_COST_WITHOUT_TOTALIZATION`;
- `COUNTERFACTUAL_ORDINARY_LIFE_IMAGINATION`;
- `SIBLING_CARE_ROLE_REVERSIBILITY`;
- `ASSIMILATED_INFLUENCE_BECOMES_OWN_JUDGMENT`;
- `CROSS_ROLE_SKILL_TRANSFER_REQUIRES_CONTEXTUAL_FIT`;
- `PARENTAL_CONCERN_TRUST_FRICTION`;
- `SUPPORT_WITHOUT_PERMANENT_DEPENDENCE`;
- `FAMILY_MODEL_OF_PLURAL_VOCATION`;
- `PARALLEL_LABOR_AND_CREATIVE_ASPIRATION`;
- `PREDEBUT_SELF_ASSIGNED_SENIOR_CARETAKER_ROLE`;
- `RECIPROCITY_PRECEDES_ROLE_EQUALIZATION`;
- `DEPENDENCE_WITHIN_SENIORITY`;
- `RECIPROCAL_DEPENDENCE_WITHOUT_SENIORITY_ERASURE`;
- `FOUNDING_DYAD_PERSISTS_WITHOUT_UNIT_EXCLUSIVITY`.

Historical-transition summary:

- Haruko's delayed-blooming/ordinary-adulthood thesis is **preserved and strengthened**, with real university/work opportunity cost added without an exit inference;
- Saki/Chisa's protector/dependent shorthand is **preserved and revised by reciprocity**;
- Saki's borrowed advice supplies new V2 evidence that provenance does not permanently own later practiced judgment;
- Rei's paternal-proof thesis is **preserved and refined** as concern/trust friction;
- Sumire's brother/piano bond is routed as **stabilization / temporal maturation**, with the stronger TRINITYAiLE origin retaining mature thesis ownership;
- Rio/Aoi mature reciprocity is **preserved and strongly strengthened by chronology**, because reciprocal concern is already visible explicitly before LizNoir's debut;
- Rio/Aoi founding specialness is retained without reducing Ai/Kokoro's equal standing in mature four-person LizNoir.

Open-register effects:

- `OPEN-14` materially advanced;
- `OPEN-05`, `OPEN-08B`, `OPEN-15`, and `OPEN-16` gain bounded support only;
- `OPEN-20` advances to **12/20 admitted bond bundles**.

The current lower-tier governing checkpoint is now `IDOLY_PRIDE_V2_PHASE1_POST_BOND_B2B_BASELINE.md`.

Next operation:

> **Phase 1 Bond Close Read — B3: Support mining**
> `bond_aoi_001_aoi` → `bond_chs_001_chs` → `bond_kkr_001_kkr` → `bond_ngs_001_ngs` → `bond_suz_001_suz`

Use `SUPPORT_MINING_WITHOUT_CONCEPT_INFLATION`.

**Recommended model:** GPT-5.6 Sol  
**Recommended reasoning:** Extra High



## 10.28 Bond B3 support-mining freeze — 2026-08-16

The mandatory B3 support tranche is complete and frozen in routing order:

1. `bond_aoi_001_aoi`;
2. `bond_chs_001_chs`;
3. `bond_kkr_001_kkr`;
4. `bond_ngs_001_ngs`;
5. `bond_suz_001_suz`.

Governing artifacts:

- `IDOLY_PRIDE_V2_PHASE1_BOND_B3_PRIMARY_FINDINGS_FREEZE.md`;
- `IDOLY_PRIDE_V2_PHASE1_BOND_B3_CLOSE_READ_AUDIT.md`;
- `IDOLY_PRIDE_V2_PHASE1_POST_BOND_B3_BASELINE.md`;
- `IDOLY_PRIDE_V2_PHASE1_BOND_B3_SHA256SUMS.txt`.

B3 admits **40 stories / 1,563 utterances**, taking the cumulative admitted bond layer to **17/20 bundles / 136 stories / 5,392 utterances**. The tranche deliberately follows `SUPPORT_MINING_WITHOUT_CONCEPT_INFLATION`: it adds no new universal constitutional thesis.

Key admitted support includes:

- Aoi: `EMBODIED_MENTORING_WITHOUT_DEFICIT_FIXATION`, reversible protection, and coexistence of recovery need with self-directed dance practice;
- Chisa: performer choice/uncertainty around adultized presentation, private craft competence, self-authored feedback calibration, and ordinary-world agency through small risk;
- Kokoro: school/work opportunity cost, self-directed persona/scoring analysis, and `STATUS_AWARE_BEHAVIORAL_RESTRAINT` where peer prank grammar would become inappropriate across a child/status asymmetry;
- Nagisa: Kotono-focused private archiving and `NAGISA_KOTONO_DOMESTIC_ROMANTIC_FANTASY`; Nagisa-side yuri/romantic coding is materially strengthened, while Kotono reciprocity/dating/exclusivity remain open;
- Suzu: ordinary-setting confirmation that the ojou-sama register is persistent personal voice, affectionate but explicitly nonliteral `お姉さま` language toward Rei, fan-recognition converting into genuine audience reciprocity, and active Mana re-performance.

Historical transition:

- existing Aoi, Chisa, Kokoro, and Suzu models are principally **PRESERVED + STRENGTHENED**;
- Nagisa/Kotono's historical classification as strongly yuri-coded but not confirmed mutual romance is **PRESERVED + STRENGTHENED ON THE NAGISA SIDE**;
- treating Suzu's ojou-sama speech as an occasional flourish is **REJECTED**;
- treating peer-tolerated teasing as automatically portable across unequal workplace relations is **REJECTED AS A UNIVERSAL RULE**.

The three B4 bond bundles remain `TEXTURE / B4` and do not require a standalone close-read tranche unless a later claim-specific ambiguity promotes an exact story. Mandatory bond close reading is therefore complete, but Phase 1 remains open because special/misc, card, and message layers still require sampling/routing.

Current lower-tier authority:

`IDOLY_PRIDE_V2_PHASE1_POST_BOND_B3_BASELINE.md`

Next operation:

> **Phase 1 lower-tier sampling/routing beyond mandatory bonds**
> Preserve B4 as indexed texture; continue method-required specials/misc, card, and message sampling/routing before Phase 1 closure.

**Recommended model:** GPT-5.6 Sol  
**Recommended reasoning:** Extra High


## 10.29 Lower-tier sampling/routing freeze — 2026-08-16

Phase-1 reconnaissance for the remaining lower-tier layers is complete and frozen as a **routing-only** operation. No card, message, special, or B4-bond proposition is newly admitted by this update; `IDOLY_PRIDE_V2_PHASE1_POST_BOND_B3_BASELINE.md` remains current analytical authority until the first C1 card tranche freezes.

Governing artifacts:

- `IDOLY_PRIDE_V2_PHASE1_LOWER_TIER_SAMPLING_AND_ROUTING_AUDIT.md`;
- `IDOLY_PRIDE_V2_PHASE1_LOWER_TIER_CLOSE_READ_QUEUE.md`;
- `IDOLY_PRIDE_V2_PHASE1_LOWER_TIER_ROUTING_SHA256SUMS.txt`.

### Specials/misc

All **27 bundles / 52 stories** now have an explicit Phase-1 route:

- supporting retrospective/ordinary-life/manager-relational material;
- indexed birthday/seasonal texture;
- formal-only items whose meaningful audiovisual payload is absent from text;
- caveated April/parody material without ordinary continuity authority;
- one explicit bad/alternate branch retained as authored possibility rather than mainline fact.

No specials-only mandatory close-read tranche is required.

### Cards

All **363 ledger-enumerated card bundles** now route as:

- **11 `C1_MANDATORY`** sources;
- **12 currently identified `C2_SELECTIVE`** support sources;
- all remaining cards as **`C3_INDEXED_TEXTURE`** unless a later exact claim promotes them.

The C1 set is split into two tranches:

**C1-A — family, memory, vocation, and legacy**

1. `card_kan_007_st-card-kan-05-fest-02`;
2. `card_kan_014_st-card-kan-05-snro-00`;
3. `card_suz_003_st-card-suz-05-anml-00`;
4. `card_kor_005_st-card-kor-05-fest-02`;
5. `card_hrk_009_st-card-hrk-05-link-00`;
6. `card_mhk_011_st-card-mhk-05-pajm-00`;
7. `card_mhk_006_st-card-mhk-05-fest-02`.

**C1-B — relationship and late-state authorship**

1. `card_ngs_007_st-card-ngs-05-fest-02`;
2. `card_ktn_007_st-card-ktn-05-fest-02`;
3. `card_szk_002_st-card-szk-05-angl-00`;
4. `card_rui_007_st-card-rui-05-fest-04`.

A formatting-only defect in the v1.26 card table was corrected here: `card_chs_009_st-card-chs-05-flow-00` had literal newlines embedded inside its title cell. Source identity, priority logic, and story count are unchanged; the repaired row now permits correct line-based enumeration of 363 card bundles.

### Messages

All **99 bundles / 1,812 granular messages** are now explicitly routed at the bundle level as story-selective indexed material (`PHASE1_MESSAGE_ROUTED_STORY_LEVEL`). Exact messages may be promoted without elevating their whole containing bundle.

Current M1 claim-bearing companion set:

- `message-card-kan-05-fest-02`;
- `message-card-kor-05-fest-02`;
- `message-card-hrk-05-link-00`;
- `message-card-mhk-05-pajm-00`;
- `message-card-ngs-05-fest-02`;
- `message-card-ktn-05-fest-02`;
- `message-card-rui-05-fest-04`.

Representative M2 sources include Nagisa/Kotono back-to-back intimacy, Rio romance/cohabitation inexperience, Rio/Aoi founding-dyad privacy, Rio's all-youth commitment language, Yu-side Rui possessive/yuri coding, and unit/group-chat maintenance labor.

Player-selectable manager replies remain `PLAYER_SELECTED_MAKINO_EXPRESSION`; mutually exclusive options may not be accumulated into a single literal Makino history.

### B4 bonds

Remain indexed without a mandatory tranche:

- `bond_ai_001_ai`;
- `bond_mei_001_mei`;
- `bond_yu_001_yu`.

### Open-register routing

- `OPEN_VERIFY_KANA_CARD_CORROBORATION` is routed to C1-A via `card_kan_014_st-card-kan-05-snro-00`; it remains open until close-read admission.
- Nagisa/Kotono reciprocity is routed to paired C1-B cards; Nagisa-side intensity may not substitute for Kotono-side romantic fact.
- Rui/Makino affect is routed to `card_rui_007` plus `message-card-rui-05-fest-04`; the referenced telephone continuation is unavailable and may not be reconstructed.
- `OPEN-14` Haruko gains a mandatory performance/vocational-horizon test through `card_hrk_009`; economic/material long-career viability remains separate.

Current next operation:

> **Phase 1 Card Close Read — C1-A: family, memory, vocation, and legacy**
>
> `card_kan_007_st-card-kan-05-fest-02` → `card_kan_014_st-card-kan-05-snro-00` → `card_suz_003_st-card-suz-05-anml-00` → `card_kor_005_st-card-kor-05-fest-02` → `card_hrk_009_st-card-hrk-05-link-00` → `card_mhk_011_st-card-mhk-05-pajm-00` → `card_mhk_006_st-card-mhk-05-fest-02`

Use the lower-tier gate:

> **raw cards → card-only prospective freeze → exact primary companion messages → Tier-H comparison if useful → close-read audit → successor baseline → ledger → SHA manifest**

**Recommended model:** GPT-5.6 Sol  
**Recommended reasoning:** Extra High

## 10.30 Card C1-A close-read freeze — 2026-08-16

The first mandatory card tranche is complete, audited, and admitted.

Governing artifacts:

- `IDOLY_PRIDE_V2_PHASE1_CARD_C1A_PRIMARY_FINDINGS_FREEZE.md`;
- `IDOLY_PRIDE_V2_PHASE1_CARD_C1A_CLOSE_READ_AUDIT.md`;
- `IDOLY_PRIDE_V2_PHASE1_POST_CARD_C1A_BASELINE.md`;
- `IDOLY_PRIDE_V2_PHASE1_CARD_C1A_SHA256SUMS.txt`.

Primary card coverage:

- **7 / 11 C1 mandatory cards admitted**;
- **21 granular card stories**;
- **1,797 card-story utterances**;
- **4 / 11 C1 mandatory cards remain**, all in C1-B.

Admitted C1-A cards:

1. `card_kan_007_st-card-kan-05-fest-02`;
2. `card_kan_014_st-card-kan-05-snro-00`;
3. `card_suz_003_st-card-suz-05-anml-00`;
4. `card_kor_005_st-card-kor-05-fest-02`;
5. `card_hrk_009_st-card-hrk-05-link-00`;
6. `card_mhk_011_st-card-mhk-05-pajm-00`;
7. `card_mhk_006_st-card-mhk-05-fest-02`.

Exact companion-message evidence admitted after the card-only prospective freeze:

- `message-card-kan-05-fest-02`;
- `message-card-suz-05-anml-00`;
- `message-card-kor-05-fest-02`;
- `message-card-hrk-05-link-00`;
- `message-card-mhk-05-pajm-00`;
- claim-specific `message-card-mhk-05-fest-02`.

### Main transition results

**kana**

- categorical `paternal abandonment` shorthand is **REVISED** to `CONTACT_WITHOUT_FAMILY_RECONSTITUTION` while retaining severe deprivation and non-co-residence;
- `PATERNAL_VISIBILITY_AS_ORIGINAL_VOCATIONAL_MOTIVE` is strengthened;
- `PUBLIC_SELF_NARRATION_AS_DEFENSIVE_AUTHORSHIP` is admitted as a concrete `ANSWERABLE_CONSTRUCTION` / `SELECTIVE_PERSONAL_JURISDICTION` mechanism;
- `VOCATIONAL_MEANING_CAN_OUTLIVE_FAILED_ORIGINAL_PURPOSE` is admitted;
- `MEMORY_AS_TRANSFERABLE_RESILIENCE` and `CARE_WITHOUT_FALSE_RESCUE_PROMISE` are admitted;
- `OPEN_VERIFY_KANA_CARD_CORROBORATION` is **RESOLVED** narrowly: the later ordinary card explicitly remembers meeting Kuromi at the dream amusement park. This does not settle blanket crossover ontology.

**Suzu**

- family authorization is split: father supportive, mother conditional;
- rebellion-to-vocation transition is strengthened as `DEFENSIVE_ENTRY_TO_SELF_AUTHORED_VOCATION`;
- `PROOF_SEEKING_OVERWORK_UNDER_CONDITIONAL_AUTHORIZATION` is admitted;
- `SMALL_WORK_AS_PROFESSIONAL_LEGITIMACY` is strengthened;
- maternal study-abroad pressure remains open because acceptance is explicitly only provisional.

**fran**

- failed authorship remains governing wound;
- `PLURAL_VOCATION_WITHOUT_HIERARCHY_FRAN` is admitted: idol and fashion work are concurrent serious vocations at this endpoint;
- `CROSS_DOMAIN_STATUS_RESET`, `MARKET_DISCIPLINE_WITHOUT_ARTISTIC_SURRENDER`, and `FAILURE_REVISES_STRATEGY_NOT_VOCATIONAL_COMMITMENT` are admitted;
- `CROSS_ROLE_COMPETENCE_TRANSFER_WITH_CONTEXTUAL_ADAPTATION` becomes the cleanest positive card-level instance of the existing transfer rule.

**Haruko**

- delayed-flowering / delayed-fulfillment thesis is strengthened;
- literalized “stand beside Mana” fulfillment shorthand is revised to `PROMISE_FULFILLMENT_THROUGH_ROLE_INHERITANCE_NOT_COPRESENCE`;
- `DEFERRED_PERFORMANCE_SUCCESSION` and `SUCCESSION_WITHOUT_IMPERSONATION` are admitted;
- `PLURAL_PERFORMANCE_VOCATION_WITHOUT_IDOL_EXIT_HARUKO` advances `OPEN-14` without closing the economic/long-career endpoint.

**miho**

- Yō's recognition is sharpened into `RELATIONAL_RECOGNITION_BECOMES_SELF_AUTHORED_EMBODIED_VALUE`;
- `PRIVATE_MEMORY_WITHIN_PUBLIC_IMAGE_LABOR` and `MEMORIAL_PRACTICE_WITHOUT_STATIC_RELIC` are admitted;
- historical `Friend Glass` memory model is preserved and strengthened as `MEMORIAL_REPERFORMANCE_WITHOUT_REPLICATION`, `LEGACY_TRANSMISSION_THROUGH_PRESENT_REAUTHORSHIP`, and `NEW_COMPANIONSHIP_WITHOUT_REPLACEMENT`;
- `GUILT_OVER_PROFESSIONAL_ABSENCE_DURING_IRREVERSIBLE_LOSS` is admitted with an explicit safeguard against inventing knowing career-over-deathbed culpability.

### Tranche-level refinement

Admit:

> **`LEGACY_CONTINUITY_WITHOUT_RESTORATION`**
>
> A lost, unavailable, failed, or superseded relational configuration may remain constitutive without literal restoration; its meaning can continue through re-authored work, embodied practice, later vocation, public transmission, or care for another person.

This remains subordinate to the existing series-level architecture and should not be universalized beyond supported cases.

Current lower-tier authority:

`IDOLY_PRIDE_V2_PHASE1_POST_CARD_C1A_BASELINE.md`

Next operation:

> **Phase 1 Card Close Read — C1-B: relationship and late-state authorship**
>
> `card_ngs_007_st-card-ngs-05-fest-02` → `card_ktn_007_st-card-ktn-05-fest-02` → `card_szk_002_st-card-szk-05-angl-00` → `card_rui_007_st-card-rui-05-fest-04`

Use the unchanged prospective gate:

> **raw cards → card-only freeze → exact routed companion messages → Tier-H comparison → transitions → successor baseline → ledger → SHA manifest**

For Rui, `tel-card-rui-05-fest-04` remains unavailable and may not be reconstructed.

**Recommended model:** GPT-5.6 Sol  
**Recommended reasoning:** Extra High


## 10.31 Card C1-B close-read freeze — 2026-08-16

The second and final mandatory card tranche is complete, audited, and admitted.

Governing artifacts:

- `IDOLY_PRIDE_V2_PHASE1_CARD_C1B_PRIMARY_FINDINGS_FREEZE.md`;
- `IDOLY_PRIDE_V2_PHASE1_CARD_C1B_CLOSE_READ_AUDIT.md`;
- `IDOLY_PRIDE_V2_PHASE1_POST_CARD_C1B_BASELINE.md`;
- `IDOLY_PRIDE_V2_PHASE1_CARD_C1B_SHA256SUMS.txt`.

Primary C1-B card coverage:

- **4 bundles**;
- **12 granular stories**;
- **1,005 card-story utterances**.

Mandatory-card program after C1-B:

- **11 / 11 C1 cards admitted**;
- **33 granular C1 stories**;
- **2,802 C1 card-story utterances**.

Admitted C1-B cards:

1. `card_ngs_007_st-card-ngs-05-fest-02`;
2. `card_ktn_007_st-card-ktn-05-fest-02`;
3. `card_szk_002_st-card-szk-05-angl-00`;
4. `card_rui_007_st-card-rui-05-fest-04`.

Exact companion-message evidence admitted after the card-only prospective freeze:

- `message-card-ngs-05-fest-02`;
- `message-card-ngs-05-idol-00` as M2 recurring relational support only;
- `message-card-ktn-05-fest-02`;
- `message-card-rui-05-fest-04`.

No mandatory Shizuku companion was routed.

### Main transition results

**Nagisa / Kotono**

- historical “strongly yuri-coded but not textually confirmed lovers” is **PRESERVED + STRONGLY STRENGTHENED WITH BOUNDARY**;
- Nagisa explicitly names Kotono `親友` while also using romantic reconciliation analogy, marriage imagination, mutual-need language, closest-adjacency illumination, and a durable non-separation vow;
- `INDEPENDENT_SELF_EXPANSION_WITHIN_RELATIONAL_COMMITMENT_NAGISA`, `SUPPORT_DESIRE_PERSISTS_AFTER_SELF_DIFFERENTIATION_NAGISA`, `ROMANTIC_ANALOGY_WITH_EXPLICIT_FRIENDSHIP_CATEGORY`, `AUDIENCE_RECOGNIZED_DYAD_KOTONAGI`, and `EQUAL_ADJACENCY_WITHOUT_SUPPORT_ERASURE_NAGISA` are admitted;
- Kotono independently proves solo capacity while defining her chosen future through the five-member Moon Tempest: `SOLO_CAPACITY_WITHOUT_SOLO_IDEAL_KOTONO`, `FIVE_MEMBER_RELIANCE_AFTER_INDIVIDUALIZATION_KOTONO`, and `GROUP_COMPLETENESS_WITHOUT_PERSONAL_INCAPACITY` are admitted;
- paired Kotono authority **does not** establish Kotono-side romantic reciprocity toward Nagisa;
- mutual romantic intent/dating/exclusivity remain open.

**Kotono**

- `FAN_ANSWERABILITY_AS_SELF_AUTHORED_RESPONSIBILITY_KOTONO` and `WORKLOAD_CONSENT_WITHOUT_INFINITE_CAPACITY_KOTONO` are admitted;
- `MEMORIAL_ADDRESS_WITHOUT_VOCATIONAL_SUBORDINATION_KOTONO` strengthens the anti-replication / legacy-continuity architecture;
- the routed companion message adds support-level `MANAGERIAL_STANDING_WITHIN_FAMILY_TRUST_NETWORK_KOTONO`.

**Shizuku**

- historical fan-memory/fan-translator thesis is **PRESERVED + STRONGLY STRENGTHENED**;
- `MULTILAYER_CREATIVE_AUTHORSHIP_SHIZUKU`, `PAST_FAN_SELF_AS_CREATIVE_MATERIAL_SHIZUKU`, `IDENTITY_INTEGRATION_WITHOUT_ROLE_FIXATION_SHIZUKU`, `FAN_EXPERIENCE_AS_AUDIENCE_RELATIONAL_COMPETENCE_SHIZUKU`, `RECIPROCAL_FAN_IDOL_SUPPORT_WITH_ROLE_DIFFERENCE`, and `AUDIENCE_RECIPROCITY_AS_CREATIVE_GOVERNANCE_SHIZUKU` are admitted;
- the deleted `ぷにもちどろっぷ` identity is reincorporated through `drop` rather than restored as a role she must return to;
- former fanhood becomes present creative authority rather than a phase that must be discarded.

**Rui**

- current late-state `AFFECTIVE_SELF_CONSCIOUSNESS_WITHOUT_ROMANTIC_SETTLEMENT` is **REVISED** to `RUI_TO_MAKINO_ROMANTIC_ATTRACTION_STRONGLY_ESTABLISHED`;
- the earlier B2-A formulation remains valid at its own information frontier;
- `ROMANTIC_SELF_RECOGNITION_RESISTANCE_RUI`, `DISCOVERED_CREATIVE_AUTHORSHIP_RUI`, and `PRIVATE_DESIRE_EMERGES_WITHIN_PROFESSIONAL_GRATITUDE_RUI` are admitted;
- the routed message adds `RETROSPECTIVE_ROMANTIC_RECLASSIFICATION_RUI`: Rui now understands her former kiss-rehearsal request as careless after acquiring stronger romantic literacy;
- Rui-side romantic attraction is strongly established, but exact confession wording, Makino reciprocity, dating, and relationship status remain open;
- `tel-card-rui-05-fest-04` remains unavailable and may not be reconstructed.

### Tranche-level refinements

Admit as subordinate, source-bounded refinements:

> **`SELF_AUTHORSHIP_AS_REFLEXIVE_SELF_KNOWLEDGE`** — authorship can help a person discover or accept an inner state rather than merely express one already fully known.

> **`DIFFERENTIATED_RECIPROCITY`** — mutual standing does not require identical roles, histories, or functions; independent agents can choose reciprocal reliance without role collapse.

### Open-register state after C1-B

- Nagisa/Kotono mutual romantic reciprocity — **OPEN / NOT ESTABLISHED**;
- `OPEN_RUI_MAKINO_POST_RECOGNITION_OUTCOME` — **OPEN FORMAL DEPENDENCY** because `tel-card-rui-05-fest-04` is unavailable;
- `OPEN_VERIFY_KANA_CARD_CORROBORATION` remains **RESOLVED** in the narrow C1-A form;
- `OPEN-14` remains materially advanced but economically open;
- `OPEN-20` bond coverage remains **17/20 bundles / 136 stories / 5,392 utterances admitted** because B4 remains indexed texture.

### Escalation decision

C1-B triggers **no mandatory C2/C3 card, B4 bond, special, or unrelated-message escalation**.

The Rui telephone is a routed formal dependency but does not block the current Rui-side attraction claim. The Nagisa/Kotono result is a legitimate evidentiary boundary rather than a contradiction requiring lower-priority rescue.

Current lower-tier authority:

`IDOLY_PRIDE_V2_PHASE1_POST_CARD_C1B_BASELINE.md`

Next operation:

> **Phase 1 closure audit and Phase 2 readiness decision**

If closure criteria are met, proceed to the method-defined:

> **Phase 2 — Longitudinal ledgers**

**Recommended model:** GPT-5.6 Sol  
**Recommended reasoning:** Extra High
