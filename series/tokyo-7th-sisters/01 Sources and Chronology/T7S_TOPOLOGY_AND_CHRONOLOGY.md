---
title: "Tokyo 7th Sisters — Topology And Chronology"
artifact_id: T7S_TOPOLOGY_AND_CHRONOLOGY
artifact_type: source_topology_and_chronology
series: Tokyo 7th Sisters
generation: V1
version: "1.0"
status: canonical
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
do_not_use_as_literary_evidence: true
source_boundary: "c20260909-r484; preserved offline Japanese game; no sequential analysis consumed"
architecture_lifecycle: INITIAL
created: 2026-09-09
last_updated: 2026-09-09
---

# Tokyo 7th Sisters source topology and chronology

Current route: [CURRENT_STATE_AND_CORPUS_MAP.md](../CURRENT_STATE_AND_CORPUS_MAP.md). Governing pair: [T7S_ANALYTICAL_METHOD.md](../00%20Frameworks%20and%20Methods/T7S_ANALYTICAL_METHOD.md) and [T7S_SYNTHESIS_ARCHITECTURE.md](../00%20Frameworks%20and%20Methods/T7S_SYNTHESIS_ARCHITECTURE.md). Source recovery: [T7S_EVIDENCE_SUBSTRATE_AND_LOCATOR_PROTOCOL.md](../00%20Frameworks%20and%20Methods/T7S_EVIDENCE_SUBSTRATE_AND_LOCATOR_PROTOCOL.md).

## F. Story topology and chronology model

### Observed native hierarchy

The catalog has **two top-level Main menu groupings**, `2034年` (235 episodes) and `2053年` (129). It has **19 second-level Main families**. Rows below are grouped for readability, not proposed chronology.

| Native Main group | Family layer ID | Native family title | Episodes |
| --- | --- | --- | ---: |
| 2034年 | 200010 | EPISODE 0.0 | 6 |
| 2034年 | 200030 | EPISODE 1.0 | 91 |
| 2034年 | 200040 | EPISODE.4U | 22 |
| 2034年 | 200050 | EPISODE.KARAKURI | 18 |
| 2034年 | 200060 | EPISODE 2.0 | 10 |
| 2034年 | 200070 | EPISODE 3.0 | 42 |
| 2034年 | 200080 | EPISODE 4.0 AXiS | 13 |
| 2034年 | 200020 | EPISODE 0.7 -Melt in the Snow- | 3 |
| 2034年 | 200090 | EPISODE 5.0 -Fall in Love- | 6 |
| 2034年 | 200100 | EPISODE 6.0 FINAL -Someday, I'll walk on the Rainbow...- | 7 |
| 2034年 | 200120 | EPISODE NANASUTA | 17 |
| 2053年 | 200110 | EPISODE 2053 SEASON1 | 35 |
| 2053年 | 200130 | EPISODE 2053 Roots. SEASON1 | 11 |
| 2053年 | 200140 | EPISODE 2053 SEASON2 | 30 |
| 2053年 | 200150 | EPISODE 2053 Roots. SEASON2 | 14 |
| 2053年 | 200160 | EPISODE 2053 SEASON3 | 15 |
| 2053年 | 200170 | EPISODE 2053 SEASON4 | 8 |
| 2053年 | 200180 | EPISODE 2053 SEASON5 | 11 |
| 2053年 | 200190 | EPISODE 2053 SEASON6 | 5 |

Sub contains `i-n-g` 280, `親密度` 349, `OTHER` 67, and `BIRTHDAY` 59. Event contains 231 episodes in 58 second-level native families, with one to seven episodes per family. These families supply useful initial envelopes; special editions and related families still need explicit cross-links. The locked episode catalog and category-qualified master rows preserve the full hierarchy; see [T7S_SOURCE_LOCK.json](T7S_SOURCE_LOCK.json) and the exact-membership query contract in [T7S_EVIDENCE_SUBSTRATE_AND_LOCATOR_PROTOCOL.md](../00%20Frameworks%20and%20Methods/T7S_EVIDENCE_SUBSTRATE_AND_LOCATOR_PROTOCOL.md).

**Native layer IDs are not globally unique.** `200130` is a Main Roots. family and a Sub character family; root IDs also repeat by category. Key hierarchy nodes by witness/master revision + table + native category + layer ID, with source row/hash verification. Preserve native category values (`0` for Main in the inspected records) alongside readable labels.

### Established labels versus chronological placement

| Finding | Basis and permitted interpretation |
| --- | --- |
| 2034 / 2053 | Native menu labels establish organizing groups, not the year of every contained scene |
| EPISODE 0.7 → winter 2031; EPISODE 5.0 → autumn 2043 | A contemporary 2020-05-20 report explicitly supplies those settings. Record `basis=SECONDARY_REFERENCE`, `confidence=DOCUMENTED_PENDING_PRIMARY_CONFIRMATION`; do not silently upgrade to native chronology. [Gamer report](https://www.gamer.ne.jp/news/202005200001/) |
| 2043 is an official franchise grouping | The official unit page contains a 2043 section; that alone does not date every associated scene. [Official unit page](https://t7s.jp/character/unit.html) |
| 2053 includes multiple units/lines | Native Roots. families are explicit. DONUTS names Stella MiNE, Asterline, Roots., and RiPoP within EPISODE 2053. This supports distinct group routing, not a chapter-by-chapter interleaving. [DONUTS, 2023-12-19](https://www.donuts.ne.jp/news/2023/1219_7th_10th_anniversary/) |

Neither 2031 nor 2043 appears in the examined native family titles. EPISODE 0.7 and 5.0 sit under the `2034年` menu group despite the documented settings above. Therefore **menu-group inheritance must never populate a scene's diegetic year as established fact**. No exact Asterline/Roots. total reading order has been established by this inspection.

### Multi-axis record contract

| Axis | Required representation |
| --- | --- |
| Native identity | `episode_id`, `script_id`, `native_category`, full qualified `native_hierarchy` |
| Native presentation | `native_source_order`, `native_priority`, observed menu position if separately captured; never treat them as interchangeable |
| Publication | Exact date/interval/ordinal only with release evidence; record original release versus later inclusion separately |
| Diegetic time | Year/era/interval, narrated time versus framing time, flashback/retelling mode, evidence and confidence; permit unknown and overlapping ranges |
| Narrative line | Native family and independently justified `narrative_spine`; units may cross spines |
| Dependencies | Typed edges: `REQUIRES_KNOWLEDGE_OF`, `CAUSES`, `BEFORE`, `OVERLAPS`, `RECOUNTS`, `RECONTEXTUALIZES`; include provenance and confidence |
| Reading schedule | Planned analytical block order and reason; this is an execution choice, not a source assertion |
| Character horizon | Character-state IDs and permissible knowledge boundary per subject/recipient |
| Witness | Continuity, edition, source lock, and retrospective/prospective exposure boundary |

Maintain a **partial-order graph**, not one chronology integer. Only asserted `BEFORE` edges participate in temporal cycle checks; causal, retelling, and interpretive edges remain different types. Unknown ordering is valid. Contradictory order constraints open a chronology issue rather than force a convenient sort.

`T7S_TOPOLOGY_AND_CHRONOLOGY.md` owns source-family placement and reading dependencies. The story ledger owns event-level temporal/causal assertions. Prequels are scheduled by exposure/prerequisite safety, not earliest year. Parallel lines have separate frontiers until an evidenced crossing warrants integration. Birthday dates, affinity unlock order, card IDs, filenames, and system availability dates are not automatically diegetic dates.

## Bootstrap topology, chronology and exposure state

The exact source membership comes from the locked episode catalog and coverage ledger. All 19 Main families, all four Sub top groups and all 58 Event families are inventoried. Native parent links are topology edges; they are not temporal `BEFORE` assertions. No event-level chronology or inferred cross-line dependency is asserted at bootstrap. The temporal dependency graph has zero analytical edges, so there is no fabricated total order to validate. Add edges with type, exact source basis, witness, endpoints and confidence; reject cycles among established `BEFORE` edges and retain incompatible alternatives as issues.

The first candidate is EPISODE 1.0 → アバンタイトル → 始まりの日 (第0話), episode `201000001`, script `scout_000_00_01.json__8df3fd723276f650`, category `0`, qualified layers `100020 / 200030 / 300010`. Native source-order index is 6 and priority is 1; neither field makes this the universally first story. The complete source has 195 pages and 190 text records. Selection follows the approved introductory reading plan. The next candidate is chapter `300020`, ノッキン・オン・セブンス・ドア, with causal subdivision determined during authorized reading.

2034 family frontiers and every 2053 season/Roots. line frontier are `NOT_STARTED`. Sub/Event/additional and supplemental obligations are wholly unscreened. Maintain explicit episode/script/range sets per line and eligible supplemental envelope; a high-water number cannot hide holes. Prequels, NANASUTA and later-era crossings require prospective dependency review before admission. An unknown chronology remains unknown; resolve it only when a claim or reading boundary depends on it.

The dated external chronology references above are inherited, attributed reconnaissance claims from approved design 1.1, not fresh primary-story findings. This bootstrap did not conduct new external chronology research. Native confirmation remains required before using 2031/2043 settings as load-bearing character-state or causal assumptions. Metadata labels, small technical dialogue examples, four earlier playback samples and external chronology discussion were previously exposed; no reader may claim an uncontaminated first encounter.

## Revision history

- 2026-09-09 — Initialize native topology and candidate reading schedule from master revision 484; zero analytical chronology edges or consumed stories.
