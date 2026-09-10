---
title: "Tokyo 7th Sisters — Topology And Chronology"
artifact_id: T7S_TOPOLOGY_AND_CHRONOLOGY
artifact_type: source_topology_and_chronology
series: Tokyo 7th Sisters
generation: V1
version: "1.9"
status: canonical
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
do_not_use_as_literary_evidence: true
source_boundary: "c20260909-r484; through complete T7S_B0007 / category-qualified Main chapter 300070 / episodes 201000601–201000609 / all primary pages and both authored branches; later story unconsumed"
architecture_lifecycle: INITIAL
created: 2026-09-09
last_updated: 2026-09-10
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

The audited opening, EPISODE 1.0 → アバンタイトル → 始まりの日 (第0話), episode `201000001`, script `scout_000_00_01.json__8df3fd723276f650`, category `0`, qualified layers `100020 / 200030 / 300010`, remains closed as `T7S_B0001`. Native source-order index is 6 and priority is 1; neither field makes it the universally first story. The canonical reading is [T7S_B0001_DEEP_READING.md](../02%20Readings/T7S_B0001_DEEP_READING.md).

The next complete native chapter layer, `300020` / ノッキン・オン・セブンス・ドア, is closed as `T7S_B0002`. Its exact, hole-free membership is episodes `201000101`, `201000102`, `201000103`, `201000104`, `201000105`, `201000106`, `201000107`, `201000108`, and `201000109`, with respective scripts and complete ranges recorded in the source lock and coverage ledger. These nine documents contain 515 pages and 488 text records; episode `201000109` contains the chapter's one choice group and both authored branches were consumed. The canonical reading is [T7S_B0002_DEEP_READING.md](../02%20Readings/T7S_B0002_DEEP_READING.md).

The following chapter layer, `300030` / スクール・オブ・アイドル, is closed as complete `T7S_B0003`. Its exact, hole-free membership is episodes `201000201`–`201000209`, with respective scripts and complete ranges recorded in the source lock and coverage ledger. The nine primary documents contain 401 pages and 384 text records; episode `201000207` contains one choice group and both authored branches were consumed. The canonical reading is [T7S_B0003_DEEP_READING.md](../02%20Readings/T7S_B0003_DEEP_READING.md). It preserves Musubi's opening refusal as a historical state, then records voluntary lessons, a chosen public test, and her later acceptance of Haru's Nanasta invitation without retroactively authorizing earlier pressure.

The next chapter layer, `300040` / オール・アバウト・マイ・アイドル, is closed as complete `T7S_B0004`. Its exact, hole-free membership is episodes `201000301`–`201000309`, with respective scripts and complete ranges recorded in the source lock and coverage ledger. The nine primary documents contain 371 pages and 342 text records; episode `201000308` contains one choice group and both authored branches were consumed. The canonical reading is [T7S_B0004_DEEP_READING.md](../02%20Readings/T7S_B0004_DEEP_READING.md). It preserves Nicole imitation as Rona's historically useful scaffold, records the point where likeness becomes identity foreclosure, and distinguishes her later self-authored membership from still-unstable error tolerance and Connie's unresolved concealment.

The next chapter layer, `300050` / プリンセス・シタマチ, is closed as complete `T7S_B0005`. Its exact, hole-free membership is episodes `201000401`–`201000409`, with respective scripts and complete ranges recorded in the source lock and coverage ledger. The nine primary documents contain 330 pages and 312 text records; episode `201000407` contains one choice group and both authored branches were consumed. The canonical reading is [T7S_B0005_DEEP_READING.md](../02%20Readings/T7S_B0005_DEEP_READING.md). It preserves Hime's shop/family labor and rough register as genuine, shows care redistributed enough for her to add idol work, and keeps the imposed shop test, agreed river song, chosen entry, public-live assent, streamed debut, and costume refusal as separate decisions.

The next chapter layer, `300060` / モモカ・ゴー・ホーム！, is closed as complete `T7S_B0006`. Its exact, category-qualified Main membership is episodes `201000501`–`201000509`, with respective scripts and complete ranges recorded in the source lock and coverage ledger. The identically numbered Sub layer `300060` is excluded. The nine primary documents contain 370 pages and 349 text records; episode `201000504` contains one choice group and both authored branches were consumed. The canonical reading is [T7S_B0006_DEEP_READING.md](../02%20Readings/T7S_B0006_DEEP_READING.md). It distinguishes Momoka's skill and intense selective interest from sustained obligation, records each role entry and withdrawal separately, and preserves the final five-person admission alongside immediate lesson resistance and Nanasta's deceptive media-based motivation system.

The next chapter layer, `300070` / ギャル・ライク・イット・ホット, is closed as complete `T7S_B0007`. Its exact, category-qualified Main membership is episodes `201000601`–`201000609`, with respective scripts and complete ranges recorded in the source lock and coverage ledger. The identically numbered Sub layer `300070` contributes episode `402000201` and is excluded. The nine primary documents contain 401 pages and 378 text records; episode `201000606` contains one choice group and both authored branches were consumed. The canonical reading is [T7S_B0007_DEEP_READING.md](../02%20Readings/T7S_B0007_DEEP_READING.md). It preserves Sumire's opening enjoyment and unexplained weight, then identifies a recurring currentness-based self-disqualification across name, cooking, earnestness, and idol work; distinguishes each refusal, visit, pushed song, immediate-live assent, membership declaration, name permission, and costume decision; and records “shining” as decision-changing evidence against her half-finished self-judgment without treating it as a stable talent essence.

The **next candidate within the owner-authorized EPISODE 1.0 continuation** is episode `201000701`, script `scout_007_01_01.json__6dd916ae293fdd45`, title 今度は王子さま？ / 第1話, in chapter layer `300080` / マイ・プリンス・フォーエバー. Only its catalog metadata identifies this boundary; its story document has not been opened. Continue only after the B0007 chapter-close transaction is validated and recoverably published; any source outside EPISODE 1.0 requires separate authorization.

The EPISODE 1.0 frontier is exact and hole-free for 55 episodes: `{201000001, 201000101–201000109, 201000201–201000209, 201000301–201000309, 201000401–201000409, 201000501–201000509, 201000601–201000609}`. Within that set all 2,583 primary pages/logs and 2,443 text records are consumed, and all seven choice-bearing episodes retain both authored branches. The remaining 36 EPISODE 1.0 memberships, beginning with `201000701`, remain `NOT_STARTED`. Every other 2034 family and every 2053 season/Roots. line remains `NOT_STARTED`; Sub/Event/additional and supplemental obligations remain wholly unscreened. The exact coverage ledger, not a numeric high-water alone, is authoritative for holes. Prequels, NANASUTA, and later-era crossings still require prospective dependency review. An unknown chronology remains unknown; resolve it only when a claim or reading boundary depends on it.

At event level, B0001 retains the recorded last-live `BEFORE` 2034 office edge. B0002 adds an explicitly recounted prior-idol interval before Haru's present arrival plus causal and recontextualizing edges inside her recruitment arc. Complete B0003 adds a causal chain from public persona through coerced exposure, voluntary training, disclosed desire, public test, friendship-based consent, and an unresolved privacy breach; its later account recontextualizes rather than overwrites the opening state. B0004 adds the prior Nicole-imitation scaffold, present recruitment by misrecognition, public confrontation, relational repair, chosen return, reciprocal debut, and immediate error-triggered relapse; later repair recontextualizes rather than erases imitation's earlier benefit or continuing fragility. B0005 adds Hime's childhood/present plurality, shop and household labor, grief disclosure, private agreed rehearsal, material burden-sharing, public entry, debut, and costume-boundary coda; later consent never overwrites earlier refusal or force. B0006 adds Momoka's selective-interest baseline, repeated stage/band/audition entries and exits, explicit coercive capture, deliberately planted media, prepared return, successful stream, formal fifth-performer admission, and immediate lesson-resistance counterexample. Complete B0007 adds Sumire's pleasure/weight tension, care-led discovery, explicit offer and refusal, name boundary, voluntary visit, hidden cooking competence, pushed songs, adequacy-based refusal, recognized shining, immediate-stream assent, explicit membership, exclusive name permission, and a pressured costume coda; later decisions recontextualize rather than overwrite earlier states. Native sequential consumption is not silently converted into a complete diegetic timeline, and no cross-family ordering or exact calendar date is added. All typed event edges are owned by the story ledger.

The dated external chronology references above are inherited, attributed reconnaissance claims from approved design 1.1, not fresh primary-story findings. This bootstrap did not conduct new external chronology research. Native confirmation remains required before using 2031/2043 settings as load-bearing character-state or causal assumptions. Metadata labels, small technical dialogue examples, four earlier playback samples and external chronology discussion were previously exposed; no reader may claim an uncontaminated first encounter.

## Opening-prerequisite decision OPA-0001

The [bounded opening-prerequisite audit](../09%20Audits%20and%20Manifests/T7S_OPENING_PREREQUISITE_AUDIT.md) retains the EP1.0 introduction. In revision 484, `m_scenario_recommend` assigns series `100020` rank 1 to episode `201000001`, ranks 155–160 to the six EP0.0 episodes, and ranks 163–165 to the three EP0.7 episodes. The client filters this table by series and sorts ascending by `Order` for its recommendation service. This is a documented **recommendation axis**; it is distinct from native array order, ordinary menu priority, release dates, diegetic time and knowledge prerequisites. Store table/witness/series/scenario/rank and the audit's exact source binding whenever reusing it.

For these three groups, no documented prerequisite requires displacing the proposed opening, and positive recommendation evidence supports retaining it. Historical onboarding requirements and complete narrative independence remain unresolved; no negative `REQUIRES_KNOWLEDGE_OF` claim follows. The official October 2019 EP0.7 release/final-chapter framing is supplementary routing evidence, not a fictional-time assertion. Exact evidence, uncertainty and exposure are in OPA-0001. This follow-up performed new bounded routing research; it does not alter the earlier bootstrap's research/exposure history above.

EP0.0 and EP0.7 remain `NOT_STARTED`. Their ranks do not admit later packets or establish an automatic complete reading order. If a future load-bearing reconstruction requires unadmitted prior knowledge, pause the dependent work and record a prospective boundary correction before proceeding. No event-level temporal or causal edge was added by the scheduling decision itself; the B0001 edge recorded above comes from the subsequently admitted episode.

## Revision history

- 2026-09-09 — Initialize native topology and candidate reading schedule from master revision 484; zero analytical chronology edges or consumed stories.
- 2026-09-09 — V1 / 1.1: record OPA-0001 and the separate native recommendation axis; retain the EP1.0 introduction with explicit prerequisite limits and zero story consumption.
- 2026-09-09 — V1 / 1.2: close T7S_B0001 at episode `201000001`, advance only the exact EPISODE 1.0 frontier, and route the unopened next candidate to chapter `300020` / episode `201000101`.
- 2026-09-10 — V1 / 1.3: close the complete nine-episode chapter `300020` as T7S_B0002 and the single authorized opening episode of `300030` as T7S_B0003; advance the exact hole-free frontier through `201000201` and stop before unopened `201000202`.
- 2026-09-10 — V1 / 1.4: expand T7S_B0003 to the complete nine-episode chapter `300030`, consume every page and both authored branches, advance the exact EPISODE 1.0 frontier to 19 episodes through `201000209`, and route unopened `201000301` as the next candidate.
- 2026-09-10 — V1 / 1.5: close the complete nine-episode chapter `300040` as T7S_B0004, consume every page and both authored branches, advance the exact EPISODE 1.0 frontier to 28 episodes through `201000309`, and route unopened `201000401` as the next candidate.
- 2026-09-10 — V1 / 1.6: close the complete nine-episode chapter `300050` as T7S_B0005, consume every page and both authored branches, advance the exact EPISODE 1.0 frontier to 37 episodes through `201000409`, and route unopened `201000501` as the next candidate.
- 2026-09-10 — V1 / 1.7: close the category-qualified nine-episode Main chapter `300060` as T7S_B0006, consume every page and both authored branches, advance the exact EPISODE 1.0 frontier to 46 episodes through `201000509`, retain the identically numbered Sub layer as unconsumed, and route unopened `201000601` as the next candidate.
- 2026-09-10 — V1 / 1.8: close only episode `201000601`, the opening of chapter `300070`, as T7S_B0007; consume all 73 pages, reconstruct six exact native-offset Sumire composites, advance the exact frontier to 47 episodes, and route unopened `201000602` as the next candidate.
- 2026-09-10 — V1 / 1.9: expand T7S_B0007 to complete category-qualified Main chapter `300070`, consume all nine episodes and both authored branches, advance the exact EPISODE 1.0 frontier to 55 episodes through `201000609`, and route unopened `201000701` as the next candidate.
