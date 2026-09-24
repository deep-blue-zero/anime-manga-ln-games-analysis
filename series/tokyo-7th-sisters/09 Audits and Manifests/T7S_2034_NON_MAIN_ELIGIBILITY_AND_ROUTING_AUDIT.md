---
title: "Tokyo 7th Sisters — 2034 Non-Main Eligibility and Routing Audit"
artifact_id: T7S_2034_NON_MAIN_ELIGIBILITY_AND_ROUTING_AUDIT
artifact_type: eligibility_and_routing_audit
series: Tokyo 7th Sisters
generation: V1
version: "11.0"
status: passed
source_lock: "../01 Sources and Chronology/T7S_SOURCE_LOCK.json"
coverage_ledger: "../01 Sources and Chronology/T7S_COVERAGE_AND_ROUTING.jsonl"
portfolio_index: "../02 Readings/T7S_2034_NON_MAIN_PORTFOLIO_INDEX.md"
corpus_alias: c20260909-r484
witness_id: T7S_GAME_OFFLINE_JA_R484
operation: T7S_2034_NON_MAIN_ELIGIBILITY_AND_ROUTING_AUDIT
completed: 2026-09-24
do_not_use_as_literary_evidence: true
---

# Tokyo 7th Sisters — 2034 non-Main eligibility and routing audit

## Decision

**PASS.** The complete declared non-Main inventory is now eligibility-partitioned and routed without crossing the 2053 semantic gate. All **755 Sub** and **231 Event** episodes, all **228 non-catalog scenario resources**, and all **30,991 supplemental records** have an exact ledger home. The 2034 analytical portfolio phase may begin. This audit does not claim narrative reconstruction, close analysis, chronology, static-visual review, or performed-audio review for the newly routed material.

The eligible story horizon is **974 episodes**: **743 Sub** plus all **231 Event** episodes. Eleven Sub birthday episodes are metadata-only 2053 holdings and remain unconsumed. One Hololive collaboration episode was fully screened as an explicit crossover and is retained as context outside the 2034 game-continuity release.

## Authority and reproducibility

The operation used the immutable database at `H:\T7S\corpus\extracted\evidence.sqlite`, expected SHA-256 `1bc0bf5d140e675554cf38ed4e3108be3c8c932c375c494bd29d3e4bb7b2ed87`, opened read-only with `mode=ro&immutable=1` and `PRAGMA query_only=ON`.

The deterministic screening manifest is `H:\T7S\work\analysis_continuation\non_main_audit_v1\manifest.json`, 155,587 bytes, SHA-256 `fff84f8a0e0a5fa185df0782139a9ccb61a9ce1c23a65696ce3894e1aee257bc`. It binds 269 routing packets totaling 11,417,645 bytes. The work packets are reproducibility aids, not repository authority; the canonical per-record decisions are in the coverage ledger.

The screen was deliberately conservative. Complete native-family packets supplied the routing envelope for every admitted episode; substantive families were never dismissed on an absence-of-keyword inference. `TARGETED_CASE` is the minimum for i-n-g and Legend Boss stories, and every Event family receives `DEEP_BLOCK`. Intimacy, birthday, short-message, card-message, character-voice, and solo-stage material receives an occurrence-aware ordinary-life route rather than being treated as literal chronological event evidence.

## Episode partition

| Scope | Count | Membership SHA-256 | Result |
| --- | ---: | --- | --- |
| 2034 eligible | 974 | `afce2d28c27baa949bde41088be50720e4aa53874166946d9da032e191689c5c` | admitted for portfolio reconstruction |
| 2053 blocked | 11 | `4f74c9c6fd33d37d49ef0af4eb4ee1f0d72d1f745067e0ed43b193919d4948c8` | metadata only; semantic text quarantined |
| explicit crossover | 1 | `a3129428958e3333d4015dca7ec73ac7a49e3efd27557858e01be7d0547fd3a5` | `CONTEXT_ONLY`; outside the 2034 continuity release |

The 974 admitted episodes receive these depth floors:

| Native envelope | Episodes | Disposition | Portfolio rule |
| --- | ---: | --- | --- |
| i-n-g | 280 | `TARGETED_CASE` | one factual mini-case per native chapter, grouped under character-family routes |
| intimacy | 349 | `ORDINARY_LIFE_CASE` | bounded character ordinary-life portfolios; no automatic chronology |
| SHORT MESSAGE | 45 | `ORDINARY_LIFE_CASE` | compact occurrence-aware portfolio |
| Legend Boss | 12 | `TARGETED_CASE` | institution, Seven Sisters memory, Coney/Nicole identity, and successor framing |
| NANASUTA L-I-V-E!! — Many merry party | 9 | `DEEP_BLOCK` | standalone event-scale reconstruction |
| 2034-side birthday memories | 48 | `ORDINARY_LIFE_CASE` | bounded birthday portfolio; represented occasion, not free chronology |
| Event, 58 complete native families | 231 | `DEEP_BLOCK` | one deep family envelope with internal episode mini-cases |

This yields **240 `DEEP_BLOCK`**, **292 `TARGETED_CASE`**, and **442 `ORDINARY_LIFE_CASE`** episodes. The exact route key for every episode is stored in `portfolio_route_key` in the coverage ledger.

### Held and external episode scope

The eleven held birthday families are layers `201530`–`201620` for Mai, Nanahoshi Ai, Yu, Flana, Shione, Karen, Siyoung, Hoshikage Ai, Miori, and Alina. Their dialogue was not emitted to the screening packets. The separate layer `201520` Hololive collaboration is a 119-page, 102-text-record crossover involving later-state characters and named external collaborators; it was screened only to establish that exclusion and cannot support 2034 game-continuity claims.

## Additional-resource partition

| Scope | Count | Membership SHA-256 | Result |
| --- | ---: | --- | --- |
| audited 2034-side resources | 133 | `2f686c1d33472cab07cacb2ec4766ea6b0c5764057eb4f95d9cd066bec4098cf` | 131 system/presentation; 2 duplicate opening occurrences |
| 2053 blocked resources | 9 | `5239bd325ebffcffd162327d9784d9b3da7a26922068f4c6e5b1882176f2ed28` | metadata only; semantic text quarantined |
| already-consumed Main attachments | 86 | `7ed9ea60d21240ee26cec58c86b706c09d84fb0e94c0e0840cc70cf784d6f0f1` | reconciled to their existing 87 Main occurrences; not counted twice |

The 131 `SYSTEM_OR_PRESENTATION` resources comprise the `adv` (1), `first` (57), `jack` (6), `m` (1), `news` (1), tutorial (61), and non-duplicate `scout`/blank helper (4) resources. `scout_000_00_02.json` and `v9_scout_000_00_01.json` preserve opening-story duplicate occurrences and are `CONTEXT_ONLY`; neither creates a second narrative event. The nine `ep2053`/`exepisode_ep2053` resources remain `DEFERRED_PENDING_FOUNDATION`.

## Supplemental partition

The original five parent tranches remain in the ledger. The two mixed-character parents are inactive historical nodes with exact active children; the three single-route parents remain active leaves.

| Namespace / active route | Count | Membership SHA-256 | Disposition and remaining work |
| --- | ---: | --- | --- |
| `card_message / 2034` | 22,813 | `42ecc733901565847e02cde5913fb7156bf04c897f6f26dd54a2fbe96f83ced7` | `ORDINARY_LIFE_CASE`; character-portfolio integration |
| `card_message / 2053_BLOCKED` | 2,835 | `debb066bcd8033a7eb9f1d37478dc2f5dabfe6e9c03e0d5aebcb09412d291429` | deferred; text not emitted |
| `card_message / CROSSOVER` | 42 | `ea2dcda056ca3ff165fba197ba9d7e511bfa2b0cb8fd0f8939ecb3138f5d42c1` | context outside 2034 release |
| `card_message / UNRESOLVED` | 21 | `d6089b22a3ba64c1878e0a834a5d7db90c7f0ca8de80ac843d0a5d37cf82dfef` | context only; excluded from load-bearing identity claims |
| `character_voice / 2034` | 3,802 | `822ca812d496b50db65cafb00e601d9ea888f9d3c0c6dd54987a9cad285caf1f` | `ORDINARY_LIFE_CASE`; text screened, audio not listened |
| `character_voice / 2053_BLOCKED` | 1,189 | `3a894cec2595b26b4932a30336d96273a41da338e2f53ec784d13afeea36ed9d` | deferred; text not emitted |
| `character_voice / CROSSOVER` | 81 | `541b84c19b23e1a3c124cf8832ab95a0399899a3bc3fedbaf2395f2f55536b26` | context outside 2034 release |
| `eplive_navigation / 2034_PRESENTATION` | 7 | `46bad0dab6001391c29b4392594f2fa8057ac0716973c132fc835197e97a0dac` | system/presentation; attach only as event interface context |
| `solo_stage_message / 2034` | 196 | `654fa6ec270c3baf262e6beb23c72f43762c751bad5de9217226aad8a63de0a3` | ordinary-life/performance-context portfolio integration |
| `tutorial_ui_message / SYSTEM_OR_PRESENTATION` | 5 | `d78d0fa1753c75bed104422cff5246cb9d97fb66c94459b675bf85dd2eaeaa15` | closed as system/presentation |

For `card_message` and `character_voice`, membership uses the union of the denormalized `character_id`, `raw.character.character_id`, and every `raw.characters[].character_id`, classified against locked character-route sets. Each split passed a disjoint-union check against its parent count: 25,711 card messages and 5,072 character-voice messages respectively.

Card and voice messages are conditional presentation utterances, not proof that a narrated event happened at a particular time. No voice asset was auditioned. The 21 unresolved card messages contain blanks/placeholders plus two self-labeled Coney lines without a reliable structural identity binding; they cannot bear a character claim unless independently resolved.

## Gate checks

| Check | Result |
| --- | --- |
| Every Sub/Event episode has one eligibility route | PASS — 986 / 986 |
| Every 2034-eligible substantive episode has a factual portfolio home | PASS — 974 / 974 |
| Additional resources reconcile without double-counting Main attachments | PASS — 228 / 228 |
| Supplemental active leaves form exact parent memberships | PASS — 30,991 / 30,991 |
| 2053 episode/additional/supplemental semantic text remains quarantined | PASS |
| Crossover material is separated from 2034 game continuity | PASS |
| Screening is distinguished from reconstruction, integration, visuals, and audio | PASS |

## Authorized continuation

The routing gate is closed. The next operation is the 2034 non-Main portfolio program defined in [T7S_2034_NON_MAIN_PORTFOLIO_INDEX.md](../02%20Readings/T7S_2034_NON_MAIN_PORTFOLIO_INDEX.md). The first queued bounded case is i-n-g layer `300520`, episodes `202001101` and `202001102`, under character-family route `NM-ING-200130`. Portfolio work may reconstruct and integrate admitted 2034 sources only. The complete 2053 semantic horizon remains `BLOCKED_PENDING_2034_ERA_RELEASE`.

