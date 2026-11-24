---
title: "Psycho-Pass — Franchise state and portrait qualification"
artifact_id: PP_FRANCHISE_STATE_LEDGER
artifact_type: franchise_state_ledger
series: psycho-pass
version: "1.2"
status: canonical
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
do_not_use_as_literary_evidence: true
authority_generation: PP-INITIAL
source_boundary: "PP-S01NE-E01–E02 admitted and reconciled"
canonical_home: series/psycho-pass/franchise/ledgers/PP_FRANCHISE_STATE_LEDGER.md
created: 2026-11-18
last_updated: 2026-11-23
---

# Franchise state and portrait qualification

This is the single current canonical home for reconciled character, directed relationship and institution/world state across admitted installments. It also owns individual portrait qualification and the route to each current full portrait. **Current reconciled records through `PP-S01NE-E02`: 29 entities (`PP-ENT-0001`–`0029`), 12 materialized states (`PP-FSTATE-0001`–`0012`), 23 individual qualification assessments (all `DEFERRED_EVIDENCE` at two-episode horizon; 1 `NOT_APPLICABLE` non-human AI; 1 virtual avatar entity tracked via operators), 0 pending monograph obligations, 0 completed portraits.**

## Materialized state contract

Give each person/institution a stable `PP-ENT-####` ID once evidence supports identity. Preserve source-language name, transliteration and meaningful aliases with their legitimate knowledge boundaries. Unknown/provisional identities remain distinct until evidenced equivalence. Record continuity and any source-scoped identity uncertainty.

A state record `PP-FSTATE-####` includes subject and domain, current reconciled conclusion in explanatory prose, boundary through which it is current, contributing installment/edition/unit/local state and claim IDs, decisive locators, contrary cases, confidence and transition history. Explain the mechanism behind a claimed change; a stack of trait labels or links is insufficient. Local observations remain in their source ledger. The master stores only material synthesis and its lineage.

For a person, preserve stable tendencies, changing circumstances, goals, beliefs/knowledge, competencies/limits, self-presentation and meaningful ordinary behavior separately. Do not merge a later identity revelation with what another character knew earlier. For relationships, the canonical key includes A → B and dimension; reciprocity requires separate evidence. For institutions, distinguish professed authority, implemented behavior, constraints, exceptions and consequences. A measurement output remains different from a validated description of a person.

## Qualification register contract

At the first accepted episode, each new differentiated individual is considered; reassess on substantive new evidence and at every declared tranche/installment synthesis boundary. The qualification record carries subject ID/name, continuity, assessed boundary, evidence distribution, rationale, gaps, next review trigger and the actual canonical portrait path once it exists. No name-only roster or fixed lead-character quota controls this decision.

Use `QUALIFIED_PENDING` when sufficient differentiated evidence creates a portrait production obligation, `DEFERRED_EVIDENCE` with a concrete gap/review trigger, `COMPLETE_AT_BOUNDARY` only after both required reviews, and `REASSESS_AFTER_REVISION` when material evidence or correction changes the portrait's basis. An unavailable portrait path is stated as absent rather than linked as if it exists. Counts of pending obligations remain visible in the current handoff.

The [architecture](../../framework/PP_SYNTHESIS_ARCHITECTURE.md#individuals-and-one-canonical-full-portrait) defines the full portrait standard and intended home `franchise/characters/PP_<SUBJECT>_CHARACTER_MONOGRAPH.md`. There is one current full portrait per person/continuity/boundary. Installment states and historical snapshots are scoped evidence, not competing current portraits.

A completion decision names the exact portrait bytes and declared boundary, independent self-containment review and independent source-fidelity review, actual source sample/coverage, required revisions and their disposition, and residual limits. Both reviews must pass for the declared scope; a complete checklist with missing causal/ordinary-life/relationship substance fails. Unknown domains remain stated, not fabricated. Portrait completion does not certify operational reconstruction or simulation readiness.

## Incremental integration and dependencies

The integrator applies accepted local deltas to affected state and qualification records, preserving the previous conclusion and reason for change. A new state with cross-installment consequences also links the [continuity/claim ledger](PP_CONTINUITY_AND_CLAIM_LEDGER.md). If not yet reconciled, keep the older materialized boundary visible with the pending delta ID; do not silently borrow the latest local wording.

A changed psychological, relationship or institutional conclusion identifies dependent portraits, specialist studies and syntheses. Update affected living portraits through dated sourced additions or mark them for reassessment. Frozen prior versions retain their authority boundary and supersession route. At a synthesis boundary, reconcile pending changes and qualification obligations or accurately state that the affected layer is incomplete.

The master never adjudicates a fact solely by citing itself. Reopen decisive source evidence through installment/edition/unit locators under the [integration protocol](../../integration/PP_RECONCILIATION_PROTOCOL.md).

---

## Reconciled Entity & Portrait Qualification Register (Through `PP-S01NE-E02`)

| Entity ID | Canonical Name (`JA` / Transliteration) | Category | Qualification (`PP-S01NE-E02`) | Rationale, Gaps & Next Review Trigger | Canonical Portrait Path |
| --- | --- | --- | --- | --- | --- |
| `PP-ENT-0001` | `常守 朱` / Akane Tsunemori | Person | `DEFERRED_EVIDENCE` | Expanding multi-domain breadth (E02 defiance of Ginoza, `内在化したシビュラシステムの思想`, CommuField/Exocet infiltration, unintended classmate exposure); 2/11 horizon. **Trigger:** Reassess at Tranche 1 (`E03–E04`). | Absent |
| `PP-ENT-0002` | `狡噛 慎也` / Shinya Kōgami | Person | `DEFERRED_EVIDENCE` | Deepened E02 contrast (solitary Pencak Silat/wall archive, anti-bullying hand vs. cruel restroom baiting, forensic mastery, candid `正論だ`), yet past incident & wall photo identity remain undisclosed. **Trigger:** Reassess at Tranche 1 (`E03–E04`). | Absent |
| `PP-ENT-0003` | `征陸 智己` / Tomomi Masaoka | Person | `DEFERRED_EVIDENCE` | Major E02 interior/ordinary-life expansion (`伸元`, sunlit painting studio, prosthetic left hand, Nietzsche warning + `"コウのときもそうだった"`, Exocet apology); Ginoza rift origin still undisclosed. **Trigger:** Reassess at Tranche 1 (`E03–E04`). | Absent |
| `PP-ENT-0004` | `縢 秀星` / Shūsei Kagari | Person | `DEFERRED_EVIDENCE` | E02 adds tactical/ordinary color (cafeteria, `POLICE` cart cable rescue, PC crack, urban cynicism); age-5 claim & interiority remain unexpanded. **Trigger:** Reassess at Tranche 1 (`E03–E04`). | Absent |
| `PP-ENT-0005` | `宜野座 伸元` / Nobuchika Ginoza | Person | `DEFERRED_EVIDENCE` | Major E02 deepening (Bismarckian rigidity, volcanic Masaoka eruption, `LIVERTY` coin humor, disciplined `分かった` physical-evidence compliance); rift origin still undisclosed. **Trigger:** Reassess at Tranche 1 (`E03–E04`). | Absent |
| `PP-ENT-0006` | `六合塚 弥生` / Yayoi Kunizuka | Person | `DEFERRED_EVIDENCE` | E02 adds crisp competence (holo-autopsy, `"地雷"`, mid-sprint Dominator toss); interiority still deferred & Yayoi↔Shion open (`00:32:23` wink). **Trigger:** Reassess upon focal episode. | Absent |
| `PP-ENT-0007` | `唐之杜 志恩` / Shion Karanomori | Person | `DEFERRED_EVIDENCE` | Two lab appearances (`はーい拍手`, proxy counter-trace, `00:32:23` wink); private history absent. **Trigger:** Reassess after multi-episode presence. | Absent |
| `PP-ENT-0008` | `槙島 聖護` / Shōgo Makishima | Person | `DEFERRED_EVIDENCE` | Major E02 main-timeline debut (#2 cast billing, Clausewitz + Orwell *1984* bookends, active sponsorship of Kanehara/Midō, unspoken `LSM LIBRARY` tablet seed); long-term motive & status undisclosed. **Trigger:** Reassess at Tranche 1 (`E03–E04`). | Absent |
| `PP-ENT-0009` | `大倉 信夫` / Nobuo Okura | Person (Episodic) | `DEFERRED_EVIDENCE` | Complete tragic/predatory arc ending in death (`E01 00:18:15`); sufficient at local-reading scale. **Trigger:** Reassess only if posthumously referenced. | Absent |
| `PP-ENT-0010` | `島津 千香` / Chika Shimazu | Person (Episodic) | `DEFERRED_EVIDENCE` | Complete hostage-to-therapy arc (`56.3`, E01). **Trigger:** Reassess only if recurring. | Absent |
| `PP-ENT-0011` | `船原 ゆき` / Yuki Funahara | Person | `DEFERRED_EVIDENCE` | Single E01 café scene (`C`-rank friend). **Trigger:** Reassess upon recurrence. | Absent |
| `PP-ENT-0012` | `水無瀬 佳織` / Kaori Minase | Person | `DEFERRED_EVIDENCE` | Single E01 café scene (`SE` friend). **Trigger:** Reassess upon recurrence. | Absent |
| `PP-ENT-0013` | `少年潜在犯` / Youth Latent Criminal | Person (Episodic) | `DEFERRED_EVIDENCE` | Single E01 mall pre-crime vignette. **Trigger:** Reassess only if recurring. | Absent |
| `PP-ENT-0014` | `キャンディ` / Candy | Non-Human AI | `NOT_APPLICABLE` | Akane's apartment holographic concierge AI. | Absent |
| `PP-ENT-0015` | `UNNAMED-COLLEAGUE-E01` (`あいつ`) | Provisional Person | `DEFERRED_EVIDENCE` | Smoking officer beside Ginoza (`E01 00:23:50`) & `"abnormal"` death; still unnamed through E02. | Absent |
| `PP-ENT-0016` | `シビュラシステム` / Sibyl System | Institution | Tracked via `PP-FSTATE-0006` | Sharpened from `H3c` to `H2c` at E02. | N/A |
| `PP-ENT-0017` | `公安局刑事課` / PSB CID (Division 1) | Institution | Tracked via `PP-FSTATE-0007` | Jurisdiction friction (`経済省`), Dominator RF exposure, Exocet bust. | N/A |
| `PP-ENT-0018` | `ドミネーター` / Dominator System | Institutional Artifact | Tracked via `PP-FSTATE-0008` | `割り込み処理`, `電波暗室` `通信エラー`/`文鎮`, `Destroy Decomposer` debut. | N/A |
| `PP-ENT-0019` | `チェ・グソン` / Choi Gu-sung | Person | `DEFERRED_EVIDENCE` | E02 debut as Makishima's smooth operative fixer (conservatory sounding board, Exocet RF counter-surveillance & mass holo-hack); background undisclosed. **Trigger:** Reassess upon multi-episode recurrence. | Absent |
| `PP-ENT-0020` | `郷田 蔵人` / Kurōdo Gōda *(unspoken credit kanji; spoken `郷田主任`)* | Person (Episodic) | `DEFERRED_EVIDENCE` | Complete E02 Economy Ministry technocrat portrait (opaque glasses, scapegoat `メンタル管理`, silent CCTV collapse). **Trigger:** Reassess only if recurring. | Absent |
| `PP-ENT-0021` | `金原 祐治` / Yūji Kanehara | Person (Episodic) | `DEFERRED_EVIDENCE` | Complete E02 arc (bullied `YellowGreen` scapegoat → `Johnny Mnemonic` triple killer whose Hue cleared → paralyzed alive at `CC 265`). **Trigger:** Reassess only if recurring. | Absent |
| `PP-ENT-0022` | `塩山 大輔` / Daisuke Shioyama *(+ prior victims `浅見` / `郡山`)* | Person (Episodic Victim) | `DEFERRED_EVIDENCE` | E02 factory victim #3 (`27`, laser-amputated & crushed). **Trigger:** Reassess only if posthumously expanded. | Absent |
| `PP-ENT-0023` | `葉山 公彦` / Kimihiko Hayama | Person (Episodic Victim) | `DEFERRED_EVIDENCE` | Reconstructed in absentia (`32`, original Talisman, murdered & flushed down drains 2 months prior). **Trigger:** Reassess only if posthumously expanded. | Absent |
| `PP-ENT-0024` | `菅原 昭子` / Shōko Sugawara (`すがわら しょうこ` — lossless audio) / `スプーキーブーギー` | Person (Episodic) | `DEFERRED_EVIDENCE` | Akane's former classmate (`竹達彩奈`, `本音と建前` pact); strangled by Midō at `E02 00:43:35`, murder undiscovered by CID. **Trigger:** Reassess upon E03 investigation fallout. | Absent |
| `PP-ENT-0025` | `御堂 将剛` / Masatake Midō *(unspoken credit kanji; spoken `御堂さん`)* | Person (Active Threat) | `DEFERRED_EVIDENCE` | Vivid E02 behavioral reveal (monotone avatar-purist `水島大宙`, Hayama/Shōko murderer, Orwellian erasure, still at large at `00:45:52`). **Trigger:** Reassess after arc resolution (`E03`). | Absent |
| `PP-ENT-0026` | `タリスマン` / Talisman *(Avatar Persona, `子安武人`)* | Virtual Avatar / Artifact | `NOT_APPLICABLE` | CommuField celebrity persona originally run by Hayama and usurped via voice synthesis by Midō. | Absent |
| `PP-ENT-0027` | `経済省・八王子ドローン工場` / Ministry of Economy & Hachiōji Drone Factory | Institution | Tracked via `PP-FSTATE-0011` | Air-gapped `電波暗室`, ministerial turf (`縦割り行政`), institutionalized scapegoating. | N/A |
| `PP-ENT-0028` | `コミュフィールド` / CommuField & Home Holography | Socio-Technical Platform | Tracked via `PP-FSTATE-0012` | Avatar sociality, `Biometrics` login UI, affiliate income, offline `ホロコス` vulnerability. | N/A |
| `PP-ENT-0029` | `BLURRED-WALL-PHOTO-E02` (`f05`) | Provisional Visual Subject | `DEFERRED_EVIDENCE` | Creased surveillance photo of a pale-haired figure on Kōgami's cell wall (`E02 00:02:21`); visually resembles Makishima but verbally unconfirmed through E02. | Absent |

## Reconciled Materialized States (`PP-FSTATE-0001` – `PP-FSTATE-0012`, Current Through `PP-S01NE-E02`)

- **`PP-FSTATE-0001` (`PP-ENT-0001` Akane Tsunemori — Character/Agency):** E01 poised rookie challenger advances in E02 by defying Ginoza's passivity (`私、みんなに賛成です`), confronting Kōgami's terrifying brutality (`肉食獣`), interrogating her own `内在化したシビュラシステムの思想` (`00:23:23`), and proactively leading CommuField/Exocet infiltration — while inadvertently exposing schoolmate Shōko Sugawara to Midō. *Lineage:* `STATE-0001/0015`, `CLM-0001/0003/0012/0015/0019`. *Confidence:* High.
- **`PP-FSTATE-0002` (`PP-ENT-0002` Shinya Kōgami — Character/Agency):** E01's three-register split deepens in E02: solitary Pencak Silat ascetic staring at a creased pale-haired wall photo (`f05`, verbally unconfirmed); genuinely repulsed by factory bullying (`シビュラシステムさまさまだな`) and brilliant at physical-world deduction (`ホログラフの椅子には座れない`), yet willing to breach Akane's informed consent (`話をするだけなんですよね？`) with sadistic provocation and feral combat glee, while accepting her accidental rebuke without defensiveness (`まったくの正論だ`, `00:39:53`). Prior insider status inferred (`INF`: `00:23:41` + `00:28:24`; past case `OPEN`). *Lineage:* `STATE-0002/0016`, `CLM-0004/0008/0016/0019`. *Confidence:* High.
- **`PP-FSTATE-0003` (`PP-ENT-0003` Tomomi Masaoka — Character/Agency):** Veteran Enforcer (`127.4`, prosthetic left hand) expands markedly in E02: calls Ginoza `伸元` (`00:09:52`), absorbs Ginoza's `社会のくず` tirade with weathered grace, paints tulips off-duty (`非番`) in a sunlit studio, smears cobalt over crimson while warning Akane via Nietzsche (`コウのときもそうだった`), and displays warm humanity after accidentally tackling Akane at Exocet. *Lineage:* `STATE-0003/0018`, `CLM-0006/0017/0020`. *Confidence:* High.
- **`PP-FSTATE-0004` (`PP-ENT-0004` Shūsei Kagari — Character/Agency):** E01's desk-toy humor over carceral resentment (`捕らわれの身`) gains street-cynical breadth (`陸の孤島`, `殺される方が消えるより簡単`), cafeteria levity, `POLICE` cart cable rescue, and Hayama PC forensics; age-5 self-report untouched in E02. *Lineage:* `STATE-0004/0019`, `CLM-0005`. *Confidence:* High.
- **`PP-FSTATE-0005` (`PP-ENT-0005` Nobuchika Ginoza — Character/Authority):** E01's rigid hierarchy reveals defensive personal trauma in E02: Bismarckian dogma (`同僚` vs. `調教師`, `愚か者の道`) cracks into volcanic rage at Masaoka (`貴様` / `社会のくず`) and lens-reflected fury over Akane's `"landmine"` question (`00:16:29`), yet is counterbalanced by his stiff comedic `LIVERTY` coin avatar and disciplined professionalism conceding **`分かった`** upon physical proof (`00:31:35`). Rift origin strictly `OPEN`. *Lineage:* `STATE-0005/0017`, `CLM-0011/0012/0017`. *Confidence:* High.
- **`PP-FSTATE-0006` (`PP-ENT-0016` Sibyl System — Institution):** Adjudicated **`H2c CONFIRMED`** (sharpening E01's `H3c`): E02 exposes acute physical (`電波暗室`), inter-ministerial (`経済省`), psychometric (murder clearing Kanehara's local Hue; `内在化したシビュラシステムの思想` vs. realistic threat perception), and digital (`NO DATA` 2-month avatar usurpation) blind spots — balanced directly against genuine non-lethal **`CC 265`** capture of an active triple murderer, live `Destroy Decomposer` targeting of lethal machinery, functional smart-home/forensic detection, and ordinary civic/off-duty life (`非番`). Material constitution `OPEN`. *Lineage:* `STATE-0014`, `PP-DELTA-0001/0005`, `CLM-0001/0002/0018/0019`. *Confidence:* High.
- **`PP-FSTATE-0007` (`PP-ENT-0017` PSB CID Division 1 — Institution):** Constrained by `縦割り行政` (`経済省` turf) and vulnerable to Dominator RF counter-surveillance (Club Exocet hack), yet capable of improvised field engineering (200 m cable relay) and physical-evidence forensics when Inspectors heed Enforcers. *Lineage:* `STATE-0014`, `PP-DELTA-0002/0005`, `CLM-0007/0011/0018`.
- **`PP-FSTATE-0008` (`PP-ENT-0018` Dominator System — Institutional Artifact):** Uses top-priority **`割り込み処理`** over Sibyl's queue; fails locally inside RF shielding (`通信エラー` → `文鎮`); emits detectable RF signatures when powered online (Exocet `CAUTION`); adds **`Destroy Decomposer`** (`完全排除`) against heavy mechanized threats alongside locked, Paralyzer (`100–299`, e.g. Kanehara `265`), and Lethal Eliminator (`≥300`) modes. *Lineage:* `STATE-0014`, `E02-OBS-0006/0012/0020`, `PP-DELTA-0005`.
- **`PP-FSTATE-0009` (`PP-ENT-0008` Shōgo Makishima & `PP-ENT-0019` Choi Gu-sung — Active Facilitators):** Enter the main timeline as a serene philosophical orchestrator (#2 billing; Clausewitz `戦場の摩擦`/`犯罪の摩擦`, analog `Johnny Mnemonic` disk, Orwell *1984*, unspoken `LSM LIBRARY` / `ハイパーオーツ` / `ウイルス` tablet seed) and smooth technical fixer (Exocet RF alert & mass holo-hack), actively arming/shielding both Kanehara and Midō while 100% undetected by CID at `00:45:52`. *Lineage:* `STATE-0022/0023`, `PP-DELTA-0006`, `CLM-0013/0014/0021`.
- **`PP-FSTATE-0010` (`PP-ENT-0025` Masatake Midō — Active Threat):** Monotone, dead-eyed avatar purist (`水島大宙`; credit kanji `御堂将剛`) who murdered Hayama, usurped Talisman (`子安武人` voice synthesis), escaped Exocet via Gu-sung's hack, and strangled Shōko Sugawara (`君`→`この女`) to erase her flesh (`跡形もなく、完全に`) while preserving Spooky Boogie; still at large at `00:45:52`. *Lineage:* `STATE-0027/0028/0029`, `PP-DELTA-0008`, `CLM-0021/0022`.
- **`PP-FSTATE-0011` (`PP-ENT-0027` Ministry of Economy & Hachiōji Drone Factory — Institution):** Demonstrates how state-owned industrial bunkers (`官営`, `電波暗室`, ~50 debuggers / 1,000+ drones/mo) weaponize public Hue boards and Sibyl aptitude rhetoric (`役回り`) to institutionalize scapegoat bullying while suppressing triple-murder inquiry. *Lineage:* `STATE-0024/0025/0026`, `PP-DELTA-0005`, `CLM-0018`.
- **`PP-FSTATE-0012` (`PP-ENT-0028` CommuField & Home Holography — Socio-Technical Platform):** Masks stark concrete living behind Baroque holograms and enables rich virtual celebrity/affiliate economies (`Biometrics` login UI — bypass mechanism `OPEN`), creating both `NO DATA` urban isolation blind spots and vulnerable offline `ホロコス` masquerades harboring uncaptured latent criminals (`>110`, `>140`). *Lineage:* `STATE-0027/0028/0029`, `PP-DELTA-0008`, `CLM-0021/0022`.
