---
series: OREGAIRU
artifact_type: locator_index
scope: V01-V14.5
generation: V2
status: canonical
lifecycle: phase4_frozen
canonical_name: OREGAIRU_V2_PRIMARY_SOURCE_LOCATOR_LEDGER.md
source_boundary: Canonical Japanese-primary Oregairu V2 corpus through Volume 14.5, including chronology-routed Watari-authored supplementary material already admitted by the corpus map; excludes Shin, Ketsu, unaudited anthology story content, and adaptation-only evidence
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
created: '2026-08-16'
next_artifact: OREGAIRU_V2_V1_TO_V2_REVISION_LEDGER.md
---

# OREGAIRU V2 — Primary Source Locator Ledger

## 0. Purpose, authority, and non-duplication rule

This document is the canonical **retrieval graph** for the Oregairu V2 corpus. Its job is not to repeat the 1,780 individual source rows already frozen inside the sequential deep readings, and it is not a substitute for reopening the Japanese sources when exact wording matters. Its job is to make the mature analytical corpus recoverable in a deterministic direction:

> **mature claim → canonical Phase-4 ledger → checkpoint / longitudinal state → volume deep reading → primary-source locator → Japanese witness**

The complete sequential corpus currently contains **1,780 source-locator rows** across the canonical deep readings and the chronology-routed Volume-6.5 Christmas drama-CD/prose crosswalk. Recopying those rows here would create a second source of truth and guarantee drift. This ledger therefore normalizes locator grammar, records source-witness boundaries, indexes high-value locator families, identifies stale or invalid routes, and supplies a compact claim-to-source crosswalk for every mature Phase-4 domain.

Authority order remains:

1. Japanese primary witness at the cited locus;
2. canonical V2 volume deep reading and its §17 primary-source locator ledger;
3. relevant prospective checkpoint for what could be concluded at that historical boundary;
4. relevant Phase-4 longitudinal ledger for mature series-level formulation;
5. later specialist synthesis and continuous synthesis;
6. V1/legacy conversation only as provenance.

A locator proves where evidence can be recovered. It does **not** by itself prove the interpretation attached to that evidence. Evidence class, speaker attribution, chronology, competing passages, and the difference between textual fact and analytical inference remain mandatory.

---

# 1. Locator semantics and evidence hierarchy

## 1.1 What counts as a primary-source locator

A locator is a stable recovery key sufficient to find the governing source act again. Depending on the witness, this may be:

- EPUB XHTML/spine part plus paragraph or element ID;
- synthetic EPUB `partXXXX ¶N` paragraph numbering generated during the reread;
- chapter plus a short distinctive Japanese anchor when an edition lacks reliable element IDs;
- fixed printed page or physical PDF page when page-image/layout verification is materially relevant;
- audio timestamp for performance evidence when the audio itself is the evidentiary object;
- illustration/page-image locator for paratextual or visual claims.

The locator convention is **witness-specific**. Normalization means knowing how to route each form, not pretending all editions expose identical coordinates.

## 1.2 Text, page image, audio, and paratext are different evidence classes

The corpus keeps source functions separated:

- **EPUB/prose text** governs wording, lexical search, syntax, speaker-language analysis, and paragraph recovery where a clean publisher-derived text is available.
- **Fixed-page Japanese scan/PDF** governs printed pagination, page composition, illustration placement, colophon verification, and visual layout.
- **Audio** governs performed delivery, pause, emphasis, timing, and prosody; it does not silently overwrite the wording/attribution of a Watari prose rewrite.
- **Illustrations and packaging** are paratextual evidence. They can establish framing, publication identity, or visual emphasis but cannot override prose characterization by themselves.

## 1.3 Exact quotation rule

When later work needs an exact Japanese quotation, the correct route is:

1. find the claim here;
2. open the named deep reading;
3. recover its §17 locator row or locator family;
4. reopen the governing Japanese witness at that locus;
5. quote from the primary witness, not from this consolidation document;
6. if punctuation, orthography, or edition variance matters, collate the EPUB against the fixed-page witness locally at that locus.

This ledger deliberately avoids becoming a quote anthology.

---

# 2. Canonical source-witness and locator inventory

| Scope | Canonical deep reading | Governing linguistic witness | Fixed-page / visual witness | Locator rows |
|---|---|---|---|---:|
| V01 | `OREGAIRU_V2_V01_DEEP_READING.md` | `Oregairu - Volume 01 [Japanese].epub` | `see source-identity section` | 22 |
| V02 | `OREGAIRU_V2_V02_DEEP_READING.md` | `Oregairu - Volume 02 [Japanese].epub` | `see source-identity section` | 35 |
| V03 | `OREGAIRU_V2_V03_DEEP_READING.md` | `Oregairu - Volume 03 [Japanese].epub` | `(一般小説) やはり俺の青春ラブコメはまちがっている。第03巻.pdf` | 45 |
| V04 | `OREGAIRU_V2_V04_DEEP_READING.md` | `Oregairu - Volume 04 [Japanese].epub` | `(一般小説) やはり俺の青春ラブコメはまちがっている。第04巻.pdf` | 49 |
| V05 | `OREGAIRU_V2_V05_DEEP_READING.md` | `Oregairu - Volume 05 [Japanese].epub` | `(一般小説) やはり俺の青春ラブコメはまちがっている。第05巻.pdf` | 42 |
| V06 | `OREGAIRU_V2_V06_DEEP_READING.md` | `Oregairu - Volume 06 [Japanese].epub` | `(一般小説) やはり俺の青春ラブコメはまちがっている。第06巻.pdf` | 61 |
| V06.5 | `OREGAIRU_V2_V06_5_DEEP_READING.md` | `see source-identity section` | `see source-identity section` | 64 |
| V06.5 CD (post-V09) | `OREGAIRU_V2_V06_5_DRAMA_CD_DEEP_READING.md` | `see source-identity section` | `see source-identity section` | 48 |
| V07 | `OREGAIRU_V2_V07_DEEP_READING.md` | `Oregairu - Volume 07 [Japanese].epub` | `(一般小説) やはり俺の青春ラブコメはまちがっている。第07巻.pdf` | 84 |
| V07.5 | `OREGAIRU_V2_V07_5_DEEP_READING.md` | `Oregairu - Volume 07.5 [Japanese].epub` | `(一般小説) やはり俺の青春ラブコメはまちがっている。第07.5巻.pdf` | 92 |
| V08 | `OREGAIRU_V2_V08_DEEP_READING.md` | `Oregairu - Volume 08 [Japanese].epub` | `(一般小説) やはり俺の青春ラブコメはまちがっている。第08巻.pdf` | 81 |
| V09 | `OREGAIRU_V2_V09_DEEP_READING.md` | `Oregairu - Volume 09 [Japanese].epub` | `(一般小説) やはり俺の青春ラブコメはまちがっている。第09巻.pdf` | 128 |
| V10 | `OREGAIRU_V2_V10_DEEP_READING.md` | `Oregairu - Volume 10 [Japanese].epub` | `(一般小説) やはり俺の青春ラブコメはまちがっている。第10巻.pdf` | 98 |
| V10.5 | `OREGAIRU_V2_V10_5_DEEP_READING.md` | `Oregairu - Volume 10.5 [Japanese].epub` | `(一般小説) やはり俺の青春ラブコメはまちがっている。第10.5巻.pdf` | 98 |
| V11 | `OREGAIRU_V2_V11_DEEP_READING.md` | `Oregairu - Volume 11 [Japanese].epub` | `(一般小説) やはり俺の青春ラブコメはまちがっている。第11巻.pdf` | 162 |
| V12 | `OREGAIRU_V2_V12_DEEP_READING.md` | `Oregairu - Volume 12 [Japanese].epub` | `(一般小説) やはり俺の青春ラブコメはまちがっている。第12巻.pdf` | 204 |
| V13 | `OREGAIRU_V2_V13_DEEP_READING.md` | `Oregairu - Volume 13 [Japanese].epub` | `(一般小説) やはり俺の青春ラブコメはまちがっている。第13巻.pdf` | 130 |
| V14 | `OREGAIRU_V2_V14_DEEP_READING.md` | `Oregairu - Volume 14 [Japanese].epub` | `(一般小説) やはり俺の青春ラブコメはまちがっている。第14巻.pdf` | 217 |
| V14.5 | `OREGAIRU_V2_V14_5_DEEP_READING.md` | `Oregairu - Volume 14.5 [Japanese].epub` | `none in locked corpus` | 120 |
| **Total** | — | — | — | **1780** |

The count above is an **infrastructure count**, not a claim of 1,780 independent conclusions. Many rows exist to preserve counterevidence, chronology, lexical negatives, institutional procedure, mundane continuity, or alternative interpretations so later synthesis does not retrieve only confirming evidence.

## 2.1 Source-witness identity is preserved upstream

Every row in the table routes to the source-identity section and YAML/front matter of the named deep reading. Those volume artifacts preserve source filenames, hashes, edition notes, and—where available—Drive IDs. This locator index therefore does not replicate every SHA-256 value into a second manifest. Hash-level archival verification belongs to the source inventories/manifests and eventual Phase-9 release package.

---

# 3. Normalized locator grammar

The reread developed several locator syntaxes as source editions changed. All remain valid when interpreted through their source artifact.

| Locator form | Typical scopes | Meaning | Retrieval rule |
|---|---|---|---|
| `p-00xx.xhtml#pNNN` | early/mid volumes | EPUB element ID | open named XHTML spine item, recover paragraph ID |
| `part00xx.html#NN` / `#pNNNN` | several volumes | unpacked EPUB synthetic paragraph/element | recover from the volume's extracted EPUB text |
| `p-00xx.xhtml§NNN` | later synthetic extraction | stable paragraph/section index | recover in that deep reading's extraction convention |
| `part00xx ¶N` | V14.5 and some supplements | synthetic paragraph record | recover paragraph N in part file |
| chapter + distinctive Japanese anchor | volumes where element IDs were not treated as stable | human-readable search key | search exact/diagnostic Japanese string inside governing EPUB chapter |
| printed page / physical PDF page | fixed-page witnesses | visual/fixed-layout confirmation | open rendered or original fixed-page witness |
| audio timestamp / track | drama CD | performed delivery | use only for audio-specific claims; crosswalk wording to prose where required |

**No later synthesis should silently convert one locator grammar into another.** The named deep reading is part of the locator.

---

# 4. Chronology and source-routing exceptions

## 4.1 Volume 7.5 is publication-order material with multiple story chronologies

`OREGAIRU_V2_V07_5_DEEP_READING.md` is not a single post-V7 state. Its pieces route into multiple earlier chronology points. Any locator taken from V7.5 must carry both **publication position** and **story-time position**. In particular, its B.T. is explicitly immediately after the V3 birthday material, SIDE-B is pre-V4, and SIDE-A/S.S. pieces occupy autumn positions around the V6→V7 boundary.

A V7.5 locator may strengthen an earlier state without updating the state at publication order.

## 4.2 Volume 6.5 has two analytically distinct canonical homes

`OREGAIRU_V2_V06_5_DEEP_READING.md` governs the Volume-6.5 prose collection and its sports-festival aftermath / related material under the chronology established there.

`OREGAIRU_V2_V06_5_DRAMA_CD_DEEP_READING.md` governs the **limited-edition Christmas drama CD plus Watari prose rewrite crosswalk**, whose story chronology is immediate post-V09. Exact quoted Japanese is routed through the Watari prose rewrite; audio governs performed delivery.

These must not be collapsed merely because both originate from Volume 6.5 publication material.

## 4.3 The proposed `V06_75` filename is not a canonical corpus artifact

Older method/ledger routing lists contain the proposed form:

`OREGAIRU_V2_V06_75_DEEP_READING.md`

No canonical file of that name exists in the synchronized corpus, and the current corpus map does not list one. **Do not invent or resolve this filename by guess.** For current retrieval, use the actual canonical artifacts above. If a distinct 6.75 source is later identified and admitted, it must receive its own source audit and authority metadata rather than inheriting this stale placeholder.

## 4.4 Volume 14.5 has no fixed-page Japanese scan in the current lock

V14.5 uses its EPUB as the sole fixed linguistic witness and records locations as `partXXXX ¶N`. No print/PDF pagination should be manufactured. Embedded illustrations are paratextual witnesses only.

## 4.5 Anthology 02 is admitted only at source-control level

The scan-backed OCR package is a provisional navigation/search witness. Embedded page images govern exact text. Watari-authored material may later become supplementary evidence after story-level chronology audit; guest-author stories remain derivative/official comparative witnesses. No unaudited anthology story is allowed to update the current mainline locator graph.

## 4.6 Shin and Ketsu remain outside this ledger's governing boundary

*Shin* may later become a separately marked post-ending annex. *Ketsu* is alternate-continuity comparative material. Neither is permitted to rewrite the V01–V14.5 mainline locator structure by default.

---

# 5. Retrieval graph: canonical operating procedure

For any important claim, use the following graph rather than keyword-searching the whole corpus without authority control.

### Step A — identify semantic responsibility

Choose the canonical Phase-4 home:

- narrator/reliability → Hachiman Epistemic/Narratorial Ledger;
- person-level state → Character State Ledger;
- dyad/triad state → Relationship State Ledger;
- helping/authorization → Request/Intervention Ethics Ledger;
- `本物`/falsity/sincerity → Authenticity Ledger;
- reliance/authorship/`共依存` → Dependency/Autonomy Ledger;
- roles/reputation/performance → Social Role/Performance Ledger;
- language/register/voice → Japanese Voice Ledger.

### Step B — recover historical boundary

Use the relevant checkpoint when the question is **what the text had earned at that point**, not merely what the completed series permits retrospectively.

### Step C — recover the volume-level source route

Open the named sequential deep reading and its §17 locator ledger. Use the locator ID/range given below or in the Phase-4 ledger's source-routing crosswalk.

### Step D — reopen the primary witness

For exact quotation or philology, verify against the Japanese EPUB/page image/audio at the locator. The deep reading is a map, not the final textual authority.

### Step E — seek contrary evidence

Before promoting a source act to a series-level proposition, search the same volume and later/earlier relevant states for counterevidence, changed attribution, changed chronology, or an explicit self-correction.

---

# 6. Hachiman epistemic / narratorial retrieval routes

The Hachiman ledger contains HEN-001 through HEN-126. Rather than reproduce all 126 rows, this index freezes the volume-to-locator route needed to recover them.

| HEN range / state | Governing source route | High-value locator family | Retrieval function |
|---|---|---|---|
| HEN-001–008 | V01 | V01-E01–E22 | defensive solitude, preemptive rejection, early reliance, future-assumption seeds |
| HEN-009–014 | V02 | V02-L01–L35 | group-network inference, Yui evidence, dog-origin overreach, comic camouflage |
| HEN-015–020 | V03 | V3-L01–L45 | reset/debt grammar, safe affection, strict authenticity testing |
| HEN-021–026 | V04 | V4-L01–L49 | Rumi system inference, solitude rationalization, fear of irreplaceability, information control |
| HEN-027–031 | V05 | V05-L001–L042 | provisional interpretation, idealization, `知る`, `勝手に期待して` |
| HEN-032–039 | V06 | V06 locator ledger | cultural-festival systems reading, exclusive cost policy, villain role, `虚像` |
| HEN-040–044 | V06.5 | V06.5 locator ledger | self-harm minimization, procedural cages, mask/real-self simplification |
| HEN-045–050 | post-V09 Christmas coda | coda locator ledger; especially `part0032 ¶674–689`, `part0034 ¶1–36` | `また明日`, indefinite reciprocity, heavy gifts, action without complete explanation |
| HEN-051–058 | V07 | V07 locator ledger | Kyoto stakeholder compression, false necessity, essence-preservation belief |
| HEN-059–064 | V07.5 | chronology-tagged V07.5 ledger | systems strength, invitation underweighting, emotional accounting, known collateral cost |
| HEN-065–069 | V08 | V08-E families | election choice architecture, private understanding replacing shared process, `理性の化け物` self-indictment |
| HEN-070–077 | V09 | V09-E027–E079 | `心理` vs `感情`, restraint, request ownership, anti-total-understanding transition |
| HEN-078–085 | V10 | V10 locator ledger | wanting to know more, reliance openness, privacy, Miura/Hayama jurisdiction error |
| HEN-086–090 | V10.5 | V10.5 locator ledger | ordinary uncertainty, Iroha inference, anti-reliance residue |
| HEN-091–097 | V11 | V11-E001–E096 | direct asking, favorable-evidence denial, `勝手に決めつけていた`, immediate autonomy correction |
| HEN-098–105 | V12 | V12-E001–E204 | `解消` self-reading, authored request, codependency mechanism/feeling distinction, promise motive |
| HEN-106–112 | V13 | V13 locator ledger | sophisticated institutional inference, authored failure, collaborator ethics, failed anti-codependency proof |
| HEN-113–120 | V14 | V14 locator ledger | `思考停止`, `関わり続けたい`, bridge coercion→answerability, anti-certification |
| HEN-121–126 | V14.5 | V14_5-E001–E120 | ordinary participation, post-choice complexity, `神聖視`, anti-sanctification |

**Governing caution:** a HEN row may classify an inference as strong, weak, rationalized, contradicted, or corrected. Recovering the passage without recovering the evidence-class judgment is insufficient.

---

# 7. Character-state retrieval routes

## 7.1 Yukino

| Character-state issue | Primary locator route |
|---|---|
| early reformism / belonging | V01-E05–E15; V3-L10–L25 |
| self-authored reliance and overfunctioning | V06-L19–L22, L36–L40 |
| trust and election rupture | V07-E050, E060–E061; V08-E027–E029, E053–E055 |
| post-V9 request grammar | V09-E047–E079 |
| V11 jurisdictional boundary | V11-E040–E070, E093–E096 |
| V12 authorship-before-certainty | V12-E018–E039, E092–E108, E117–E123 |
| V13 right to choose/fail + triadic closure limits | V13 early Hiratsuka/Hachiman route and late closure route |
| V14 reciprocal future claim / capability-aware support | V14 bridge and post-bridge locator families |
| V14.5 separate trajectories / ordinary future | V14_5-E057–E106 |

## 7.2 Yui

| Character-state issue | Primary locator route |
|---|---|
| atmosphere sensitivity as agency | V01-E08, E12–E13; V02-L02, L05, L17, L23–L25 |
| early particularity / friendship work | V3-L24, L33–L40 |
| Kyoto ethical boundary | V07-E013–E016, E062–E067 |
| V9 explicit answerability | V09-E019–E024, E048–E052, E069–E080 |
| V11 preservation proposal / direct claim | V11 late-chapter locator families |
| V12 self-implication and refusal of rescue identity | V12 Yui interludes + E064–E108 |
| V13 refusal of Yukino self-removal | V13 Yui/triad locator families |
| V14 receives nonmatching answer without subjecthood erasure | V14 Yui request/answer/final-club families |
| V14.5 post-loss ordinary agency | V14_5-E057–E106 |

## 7.3 Iroha

- imposed candidacy / strategic junior: V08-E006–E009;
- office becomes self-owned: V08-E044–E050, V09 institutional routes;
- mixed motive normalized: V10.5 Iroha story locator ledger;
- owns prom for herself: V12-E091–E105, E115–E116;
- procedural observer / continuing possibility: V13–V14 Iroha locator families;
- transparent pretext and epistemic humility: V14_5 Story 4 and Story 5 locator families.

## 7.4 Haruno

- performed warmth and counter-gaze: V03–V05 Haruno locator families;
- diagnostic but non-sovereign position: V11-E040–E054, E064–E070, E093–E096; V12-E045–E061;
- interior longing and limit on diagnostic sovereignty: V13 Haruno interlude / V14 family routes.

## 7.5 Hayama, Hiratsuka, Komachi, and Yukino's mother

- Hayama group centrality: V02-L09–L16;
- Hayama expectation saturation / role ownership: V10 Hayama locator family;
- Hayama refuses proxy guilt: V13 Hayama chapter/interlude routes;
- Hiratsuka's epistemic method: V09-E027–E041; V11-E017–E018, E040–E061; V13 early chapter route; V14 final guidance;
- Komachi secure reliance / differentiation: V02–V05 family routes; V08-E037–E047; V12-E077–E078, E111–E113;
- Komachi succession: V14_5-E057–E068, E079–E106;
- Yukino's mother gentle/formal coercion: V11 family confrontation locators; V12–V14 family-politics routes.

The Character State Ledger remains the authority for whether a given route supports textual fact, self-description, another character's claim, behavioral evidence, or interpretation.

---

# 8. Relationship-state retrieval routes

## 8.1 Hachiman / Yukino

Primary longitudinal chain:

`V01-E14–E15 → V3-L13/L21/L25 → V06-L19–L22/L36–L40/L55 → V07-E050/E060–E061 → V08-E027–E029/E053–E055 → V09-E047–E079 → Christmas coda part0032/part0034 → V11-E040–E070/E093–E096 → V12-E018–E039/E092–E108/E117–E123 → V13 choice/jurisdiction families → V14 bridge/future-claim families → V14_5-E057–E106`.

This chain supports development from adversarial competence-trust through idealization, conflict, answerable request, autonomy/jurisdiction disputes, and finally chosen involvement under recognized capability. It does not support a retrospective claim that the dyad was always destined or always uniquely genuine.

## 8.2 Hachiman / Yui

Use V01–V03 early particularity, V04 distance/`勘違い`, V07 Kyoto boundary, V09 answerability, V11 preservation proposal, V12 Yui interludes, V13 refusal of self-erasure, V14 wish/answer routes, and V14.5 ordinary continuation. Romantic nonreciprocity is a late answer; it is not permission to delete earlier dyadic evidence.

## 8.3 Yukino / Yui

Route through V01–V03 birthday/club friendship locators, V06 cooperative/competitive work, V07–V09 conflict-with-continuity, V11 incompatible proposals, V12–V13 decision displacement/self-removal, V14 explicit rivalry plus friendship, and V14.5 ordinary ongoing friendship.

## 8.4 Service Club triad

The triad should be recovered through all six checkpoints, not one romantic scene. The key route is:

- Checkpoint A: institutional pretext becomes relationship infrastructure;
- Checkpoint B: distributed competence becomes cost-bearing;
- Checkpoint C: preservation-through-control fails;
- Checkpoint D: reopened relation can carry more explicit incompatibility;
- Checkpoint E: diagnosis and final choice remove protected equivalence;
- Final V14.5 checkpoint: continuity survives by transmission/revision rather than identical preservation.

## 8.5 Secondary relationship controls

Use the Relationship State Ledger for Hachiman/Hayama, Hachiman/Iroha, Yukino/Haruno-family, Hachiman/Komachi, Hachiman/Hiratsuka, Saki/Taishi, Sagami/Meguri, and Komachi/Iroha. These are controls against making the central triangle explain every relational mechanism in the series.

---

# 9. Request / intervention ethics retrieval routes

The Request/Intervention Ethics Ledger contains RIE-001 through RIE-086. The efficient source route is volume-based because authorization, cost allocation, and externalities are scene-bound.

| Ethical field | Source route | Locator emphasis |
|---|---|---|
| founding Service Club paternalism / early request grammar | V01–V03 | V01-E07–E13; V02-L13 and related Hayama request rows; V3 request/autonomy rows |
| Rumi intervention | V04 | V4-L06–L13 plus later Rumi resolution rows |
| epistemic noninterference / speech blocking | V05 | V05-L001–L013 and associated later rows |
| cultural festival substitution / villain method | V06 | cultural-festival locator family |
| sports-festival aftermath / Sagami rehabilitation | V06.5 | V06.5 locator ledger |
| ordinary post-V9 answerability | Christmas coda | `part0032 ¶674–689`, `part0034 ¶1–36`, plus gift/scheduling rows |
| Kyoto multi-owner intervention | V07 | Tobe/Ebina/Hayama/Yui/Yukino locator families |
| frame recognition / ordinary indirectness | V07.5 | chronology-tagged routes only |
| election choice architecture | V08 | Iroha candidacy and Yukino/Yui option-foreclosure locator families |
| requester reversal | V09 | V09-E027–E079 |
| privacy/refusal/information ownership | V10 | Miura/Hayama/Hachiman locator family |
| capacity before commitment / shared failure | V10.5 | Iroha + Komachi story routes |
| Valentine event / recipient-authored request | V11 | V11-E001–E096, especially event and final-request families |
| witness request / explicit nonintervention boundary | V12 | V12-E018–E039, E064–E108, E117–E123 |
| direct aid refused / rivalry authorized / dummy prom | V13 | early Hiratsuka route; rivalry; collaborator; dummy-prom rows |
| helper becomes claimant / bridge / reciprocal request | V14 | wish, second prom, bridge, support, final-club routes |
| advice without jurisdiction / succession | V14.5 | V14_5-E057–E106 |

**Ethical interpretation rule:** having a locator for care, competence, prediction, promise, sacrifice, or success does not establish authorization. Always recover the recipient's answer/refusal route as well.

---

# 10. Authenticity / `本物` retrieval routes

The Authenticity Ledger freezes AH-001–AH-030. The source graph should preserve its historical development rather than search only for literal `本物`.

| AH family | Primary source route | Locator principle |
|---|---|---|
| AH-001–004: pre-`本物`, performance ≠ falsity | V01–V03 | use early honesty, role, Zaimokuza, Yui-group, Haruno-performance rows; absence/presence audits matter |
| AH-005–006: sincerity/pain not sufficient | V04–V07 | intervention-cost and harsh-truth routes; do not equate suffering with genuineness |
| AH-007–008: projection is not genuine understanding | V08 | exact V8 `本物` negative-criterion locator family |
| AH-009–010: `俺は、本物が欲しい` as owned request | V09 | V09 climactic request and surrounding `心理`/`感情`/answerability rows |
| AH-011: ordinary post-V9 continuity | Christmas coda | ordinary scheduling/gifts/`終わらなくても` routes |
| AH-012–014: post-honmono fallibility | V10–V11 | privacy overreach, ordinary performance, V11 chapter-title / continued-error routes |
| AH-015–018: valuable relation can become evasive; pain/separation not tests; Haruno non-sovereign | V11–V12 | final-proposal, opening/closing interlude, Haruno diagnosis, Yui/Yukino self-authorship routes |
| AH-019–020: `紛い物` / `贋作`, compromised origin and real consequence | V13 | Hayama/role/counterfeit locator family |
| AH-021–025: romantic choice without retroactive falsification or certification | V14 | Yui wish/answer, bridge, `好き`, late `偽物` paradox, family/social integration routes |
| AH-026–030: post-ending anti-certification | V14.5 | lexical zero audit, `神聖視`, relation-imperfection, succession/ordinary-future routes |

Literal-keyword retrieval must preserve speaker and grammatical function. `本物`, `偽物`, `紛い物`, `贋作`, `欺瞞`, `信実`, and `真実` are not interchangeable tokens in one English binary.

---

# 11. Dependency / autonomy retrieval routes

| Canonical proposition | Primary source route | Retrieval note |
|---|---|---|
| DA-01 reliance ≠ incapacity | V01–V03 early request/reliance; V14 `一人で立てるのに` / `知ってる` | compare ordinary reliance with explicit capability recognition |
| DA-02 capability ≠ sufficient autonomy | V06 Yukino overfunctioning; V12–V13 self-authorship | competence can coexist with substituted choice |
| DA-03 formal freedom can coexist with weak authorship practice | V11–V13 family/future-choice routes | recover family expectation and Yukino self-definition passages |
| DA-04 `共依存` identifies real reinforcement mechanisms | V12 | Haruno diagnosis + Hachiman neededness self-reading |
| DA-05 `共依存` does not determine feeling | V12 | exact `共依存は仕組みだ。気持ちじゃない` route |
| DA-06 no unique cure follows from diagnosis | V12–V14 | separation experiment, V13 failed proof, V14 renewed involvement |
| DA-07 direct-help refusal ≠ global relational refusal | V12–V13 | `あなたの力はもう借りない` / `お願い。私にやらせて` versus later rivalry authorization |
| DA-08 authored choices can still overreach | V13 | Yukino closure request and Hachiman/Yui triadic jurisdiction response |
| DA-09 neededness is one Hachiman mechanism, not whole attachment | V12–V14 | codependency self-reading → `関わり続けたい` without need/inability justification |
| DA-10 Yui dependence best specified as decision displacement | V12 | Yui closing-interlude self-implication |
| DA-11 noninterference ≠ autonomy | V05 noninterference doctrine; V13 `大事なのは関わり方`; V14.5 advice/succession | compare withdrawal, procedure, and accountable influence |
| DA-12 terminal model is chosen interdependence | V14–V14.5 | bridge/support/future assumptions/separate trajectories/succession |

This route preserves the decisive V2 distinction: **diagnosis is a system map, not an ontology of feeling and not a uniquely prescribed remedy.**

---

# 12. Social role / performance retrieval routes

| Proposition | Primary source route |
|---|---|
| SRP-01 performance ≠ falsity | V01–V03 Zaimokuza/Yui-group/Haruno; V10.5 Iroha |
| SRP-02 spontaneity ≠ authenticity | recurring early social-performance cases + late owned-role evidence |
| SRP-03 externally shaped roles can become self-owned | V08–V10 Iroha presidency |
| SRP-04 self-owned roles can remain performative | V10.5–V14.5 Iroha |
| SRP-05 prediction does not authorize role assignment | V07–V08 Hachiman solutions; V11 Yukino correction |
| SRP-06 reputation is causal but not sovereign | V02 Hayama network; V06 festival; V08 election |
| SRP-07 atmosphere is a field of agency | Yui routes V01–V14.5 |
| SRP-08 pretext is ethically graded | V10.5, V11 Valentine, V14 second prom, V14.5 Iroha gift pretext |
| SRP-09 performed continuity can become relationally false | V08–V09 club/election crisis |
| SRP-10 institutional office does not require sovereign competence | Meguri / Iroha / Komachi routes |
| SRP-11 socially rewarded competence can produce role capture | Yukino cultural-festival/family routes |
| SRP-12 role may be partly imposed and partly owned | Hayama, Iroha, Yukino family position |
| SRP-13 mixed motive does not disqualify ownership | Iroha; Yui relational labor; Hachiman late involvement |
| SRP-14 social labels change risk | loner / nice guy / student-council / Service Club / family-role routes |
| SRP-15 mature continuity requires revisability | V14–V14.5 final club and succession |
| SRP-16 `神聖視` is a social-form failure | V14_5 succession/anti-sanctification locator family |

The final social-role failure test is not “is someone performing?” It is whether the role can be owned, refused, revised, and answered without acquiring silent jurisdiction over other people.

---

# 13. Japanese voice retrieval routes

The Voice Ledger freezes JV-001–JV-035. Because linguistic evidence is particularly easy to flatten in translation, retrieval must recover local grammar and speaker context.

| Voice domain | Primary route | What must be preserved |
|---|---|---|
| Hachiman narration vs spoken voice | HEN ledger + representative V01/V05/V09/V12/V14 locators | narration, self-description, joke, inference, and direct request are distinct acts |
| abstraction / comic camouflage | V01–V14 representative Hachiman rows | abstraction can be humor, cognition, coordination, defense, or concealment |
| `わからない` / epistemic limit | V09–V14.5 | speaker, object of not-knowing, whether uncertainty blocks or enables action |
| `勝手に` | V05 idealization; V11 `勝手に決めつけていた`; V11 Yukino correction; V14.5 self-authored gift | unilateral authorship and self-directed initiative have different pragmatic force |
| Yukino controlled feminine register | representative early/late Yukino dialogue | development occurs inside stable register, not by “becoming blunt” |
| Yui softness + firmness | V03, V07, V11–V14.5 | hedging/ellipsis/colloquial softness can carry explicit desire and refusal |
| Iroha strategic/cute register | V08–V14.5 | performed register can be owned and transparent |
| Haruno interrogatives | V03–V14 | diagnostic pressure does not equal narrator authority |
| Hayama role-inclusive self | V10 locator family | `それも含めて、俺だよ` resists mask/essence simplification |
| Hiratsuka answer-preserving guidance | V05/V09/V13/V14 | advice often supplies procedure rather than final answer |
| Komachi meta-performance | recurring family + V14.5 succession | acknowledged performance can coexist with affection |
| institutional formulae | festival/election/prom/succession scenes | conventional wording can carry real changes in authority |
| address terms | representative early/late pairs only | change can matter; stability cannot prove relational stasis |
| politeness | family/institutional confrontations | politeness does not map directly to softness, equality, or sincerity |
| ellipsis | Yui/Yukino/Hayama/Haruno local scenes | classify pragmatic function locally |
| `と思う` | representative desire/stance passages | can mark accountable ownership rather than weak conviction |
| benefactive grammar | request/help scenes | track giver/receiver, agency, obligation, standpoint |
| `ちゃんと` | V04 Rumi will; later request/autonomy scenes | procedural adequacy term; standard remains context-dependent |
| authenticity lexicon | Authenticity ledger | preserve lexical distinctions rather than translation collapse |
| `終わる` vs `終わらせる` | V11–V14.5 | distinguish event/state from authored termination |
| interludes/preludes | V12–V14 | formal redistribution of voice limits Hachiman-centered inference |
| unattributed text | especially V13 closing interlude | preserve attribution uncertainty in metadata |
| drama-CD prosody | V06.5 Christmas CD deep reading | separate prose wording from performance evidence |

**Series-level voice rule:** maturity is increased linguistic responsibility inside persistent idiolect, not convergence toward one supposedly honest way of speaking.

---

# 14. Checkpoint routing and temporal control

The primary locator graph must preserve the prospective/retrospective distinction. Later wording cannot be used to pretend earlier ambiguity never existed.

| Checkpoint | Evidence boundary | Locator role |
|---|---|---|
| A — Early Service Club Formation | V01–V03 | freezes pre-`本物` formation, early subjecthood, request/relation baseline |
| B — Cultural Festival / Self-Sacrifice Consolidation | V04–V06.5 | freezes self-sacrifice/jurisdiction/cost externality and role-overfunctioning field |
| C — Kyoto / Election / Christmas Crisis | V07–V09 + chronology-routed coda | freezes failure of preservation-through-control and procedural turn toward answerability |
| D — Post-Honmono Restructuring | V10–V11 + V10.5 | tests fallibility after the `本物` request, privacy, role, ordinary performance, future choice |
| E — Prom / Final Choice Movement | V12–V14 | mainline ending freeze: diagnosis, authorship, romantic non-equivalence, chosen involvement |
| Final Post-14.5 Ordinary-Life Stabilization | positive update from V14.5 Stories 4–5; earlier stories chronology-routed | durability test only; preserves Checkpoint E while adding anti-sanctification and transmissive continuity |

When an analytical claim asks “what does the ending mean?”, Checkpoint E controls the meaning **at the ending**. When it asks “what does the ending prove capable of sustaining afterward?”, the Final V14.5 checkpoint is the correct additional authority.

---

# 15. Counterevidence and contradiction routing

A primary-source locator system becomes misleading if it only retrieves confirmation. The following contrary-evidence classes must remain first-class:

1. **narrator correction** — Hachiman later rejects or narrows an earlier theory;
2. **behavior/self-description conflict** — a character's actions contradict a global self-account;
3. **speaker disagreement** — Haruno, Hiratsuka, Yui, Yukino, Hayama, and Hachiman may offer competing models without one automatically becoming doctrine;
4. **chronology conflict** — publication position and story time diverge in supplements;
5. **formal attribution uncertainty** — an interlude may be strongly inferable but not textually named;
6. **lexical absence** — absence of `本物`, `依存`, etc. can be meaningful negative evidence but is never by itself proof a concept has disappeared;
7. **method/outcome split** — an intervention can succeed instrumentally while remaining ethically defective;
8. **origin/current-state split** — an imposed or compromised beginning does not settle later ownership or value;
9. **romantic answer/relationship-history split** — final romantic choice does not rewrite all previous dyadic/triadic evidence;
10. **paratext/prose split** — image, package, chapter title, or song can frame interpretation without replacing prose evidence.

Later Phase 6 must deliberately use this ledger to search for the strongest contrary locator before approving any load-bearing specialist-synthesis claim.

---

# 16. Confidence and locator completeness

Use four practical locator-confidence states:

- **direct / very high** — exact source location and evidence act are stable; attribution/chronology clear;
- **high** — source location stable, interpretive use requires modest inference;
- **moderate** — exact placement or attribution has a bounded uncertainty recorded in the deep reading;
- **OPEN / audit required** — source route exists but the claim requires adversarial rereading, edition collation, audio verification, or additional context before publication-level certainty.

A locator may be direct while the analytical claim remains OPEN. The confidence of the address is not the confidence of the interpretation.

---

# 17. Exact-source recovery protocol for later specialist synthesis

When drafting Documents 01–12:

1. state the intended claim in provisional language;
2. identify its Phase-4 semantic home;
3. use this ledger to select the relevant volume/locator family;
4. recover at least one **positive** source act and, for consequential claims, one plausible **counterexample** route;
5. confirm evidence class and speaker;
6. confirm prospective/retrospective boundary;
7. quote Japanese only after reopening the primary witness;
8. record the recovered locator in the specialist document's working notes;
9. if the claim changes under rereading, revise the claim rather than force the source into the previous wording.

For final publication-like synthesis, a chain should be reconstructable as:

`full-series claim → specialist section → Phase-4 claim/ledger → deep-reading locator ID → EPUB/PDF/audio locus`.

This is the traceability target that Phase 7 will formalize after adversarial audit.

---

# 18. Known infrastructure gaps and normalization notes

## 18.1 No canonical V06.75 artifact

As noted above, older planning documents contain `OREGAIRU_V2_V06_75_DEEP_READING.md`. The synchronized corpus does not. Current retrieval must use actual files; this ledger supersedes the stale route for retrieval purposes without rewriting historical planning documents.

## 18.2 Some early-volume locators use distinctive anchors instead of exact EPUB paragraph IDs

This is acceptable where the deep reading explicitly froze that convention. Do not fabricate element IDs later. Exact-string search in the governing EPUB plus printed-page confirmation is the correct recovery method.

## 18.3 V14.5 fixed-page pagination remains unavailable

No page numbers are to be inferred from EPUB flow. If a fixed-page Japanese print witness is later acquired and source-audited, it may extend the locator row metadata without superseding the current EPUB wording authority.

## 18.4 Audio-specific locator completeness is narrower than prose completeness

The Christmas CD has been analytically audited, but audio timestamps/prosody are not to be generalized across the whole series. The novels remain the main literary corpus; adaptation voice acting is outside this Phase-4 source boundary.

## 18.5 Anthology OCR is not quote authority

OCR text can locate a page; page image verifies the exact text. Until story chronology is audited, anthology material does not update the mainline longitudinal graph.

---

# 19. Phase-4 locator exit test

This ledger satisfies the locator-layer objective if the following are true:

- every canonical Phase-4 domain has a deterministic route back to primary-source locator families;
- all canonical sequential readings expose their own locator ledgers;
- source-witness type and chronology are not silently collapsed;
- exact Japanese quotation can be recovered without quoting this consolidation artifact as if it were primary evidence;
- V7.5 chronology, Christmas-CD chronology, V14.5 pagination limits, and attribution uncertainty are explicit;
- stale `V06_75` routing is flagged rather than guessed;
- counterevidence is part of retrieval design;
- later specialist synthesis can reconstruct a claim chain without conversation memory.

**Assessment: PASS for Phase-4 locator infrastructure.**

This does **not** mean every final synthesis claim has already been adversarially reverified. That is the purpose of Phase 6 and the later Document 13 evidence/revision audit.

---

# 20. Phase-4 status after this artifact

1. `OREGAIRU_V2_HACHIMAN_EPISTEMIC_NARRATORIAL_LEDGER.md` — complete
2. `OREGAIRU_V2_CHARACTER_STATE_LEDGER.md` — complete
3. `OREGAIRU_V2_RELATIONSHIP_STATE_LEDGER.md` — complete
4. `OREGAIRU_V2_REQUEST_INTERVENTION_ETHICS_LEDGER.md` — complete
5. `OREGAIRU_V2_AUTHENTICITY_HONMONO_LEDGER.md` — complete
6. `OREGAIRU_V2_DEPENDENCY_AUTONOMY_LEDGER.md` — complete
7. `OREGAIRU_V2_SOCIAL_ROLE_PERFORMANCE_LEDGER.md` — complete
8. `OREGAIRU_V2_JAPANESE_VOICE_LEDGER.md` — complete
9. `OREGAIRU_V2_PRIMARY_SOURCE_LOCATOR_LEDGER.md` — **complete**
10. `OREGAIRU_V2_V1_TO_V2_REVISION_LEDGER.md` — **next**

Phase 4 exits only after item 10 is complete and the major V1 claims have been routed to PRESERVE / STRENGTHEN / REVISE / DOWNGRADE / REJECT / OPEN with current authority and evidence homes.

---

# 21. Remaining architecture-defined roadmap

After the V1→V2 Revision Ledger closes Phase 4, the governing architecture proceeds as follows.

## Phase 5 — Specialist synthesis production

Recommended drafting order:

1. `01_SERIES_ARCHITECTURE_AND_VOLUME_PROGRESSION.md`
2. `02_HIKIGAYA_HACHIMAN_NARRATION_SELF_DECEPTION_AND_GROWTH.md`
3. `03_YUKINOSHITA_YUKINO_SELFHOOD_COMPETENCE_FAMILY_AND_DESIRE.md`
4. `04_YUIGAHAMA_YUI_ATMOSPHERE_ACCOMMODATION_DESIRE_AND_LOSS.md`
5. `05_THE_SERVICE_CLUB_TRIAD_RELATIONSHIP_AND_ROMANTIC_CHOICE.md`
6. `06_THE_GENUINE_AUTHENTICITY_PERFORMANCE_AND_MIXED_MOTIVES.md`
7. `07_HELPING_SELF_SACRIFICE_DEPENDENCY_AND_AUTONOMY.md`
8. `08_SOCIAL_SYSTEMS_REPUTATION_GROUPS_AND_SCHOOL_POLITICS.md`
9. `09_HARUNO_HAYAMA_HIRATSUKA_KOMACHI_AND_COUNTER_GAZES.md`
10. `10_FAMILY_ADULTHOOD_FUTURITY_AND_THE_PROBLEM_OF_CHOICE.md`
11. `11_JAPANESE_VOICE_NARRATIVE_STYLE_COMEDY_AND_INTERTEXTUALITY.md`
12. `12_SUPPLEMENTARY_VOLUMES_DRAMA_CDS_AND_ORDINARY_LIFE.md`

## Phase 6 — Adversarial Japanese-source audit

Stress-test the strongest claims from Documents 01–12 by reopening Japanese passages, hunting counterexamples, auditing narrator inference, and narrowing or downgrading claims that fail.

## Phase 7 — Evidence locator and first-pass revision document

Produce:

`13_EVIDENCE_LOCATOR_AND_FIRST_PASS_REVISION_LEDGER.md`

This is distinct from the present Phase-4 locator infrastructure. Document 13 is the **post-specialist, post-adversarial curated publication bridge**: mature claim → specialist document → Japanese locator → counterevidence → V1 status → V2 revision reason.

## Phase 8 — Full-series synthesis

Produce:

`14_OREGAIRU_FULL_SERIES_SYNTHESIS.md`

This is the continuous reader-facing argument written from Documents 01–13 plus the canonical readings/ledgers. It should not merely concatenate specialist sections.

An optional `15_HACHIMAN_AND_YUKINO_RELATIONSHIP_DEEP_DIVE.md` is warranted only if the triad/relationship specialist cannot carry that material without distortion or overload.

## Phase 9 — Archival release

- write final frozen `00_README_AND_CORPUS_MAP.md`;
- update corpus manifest;
- validate links, YAML, names, and locators;
- duplicate-prose audit;
- separate working from release artifacts;
- compute artifact/source checksums;
- verify no copyrighted primary-source payloads are redistributed;
- package and freeze the V2 release.

The architecture's recommended release name is:

`Oregairu_Definitive_V2_Multi_Document_Synthesis_v1.0.zip`

Future corrections should become a later release/version rather than silently mutating the frozen package.

---

# 22. Terminal locator formulation

The locator layer freezes one methodological proposition for all later Oregairu work:

> **No mature claim should depend on remembering what a prior analysis “said.” It should be possible to recover why the claim exists, which authority currently owns it, what historical boundary limits it, where the Japanese evidence sits, what kind of evidence that source act is, and what counterevidence could still force revision.**

This is the distinction between a large archive of insightful prose and a traceable analytical corpus.
