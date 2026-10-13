---
series: IMOSAE
artifact_type: primary_source_locator_index
scope: V01-V14_evidence_retrieval
generation: V1
status: canonical
source_boundary: Locked original Japanese numbered EPUBs and immutable normalized/visual releases; no narrative-source payloads in Git
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
version: '1.0'
date: '2026-10-13'
---

# Primary source locator index

## 1. One route from an analytical claim to its source

Use an `IM-VNN-E###` identifier to find the prospective reading register and the primary coordinate. The [machine-readable route index](machine_readable/IMOSAE_EVIDENCE_ROUTE_INDEX.jsonl) contains all **3,666** units: 3,579 in V01–V13 plus V14's 87 text/paratext/visual units. It contains metadata, classes and coordinates, not extracted paragraphs. Evidence numbers are local to each volume and immutable; their size is not a literary-quality score.

The unit's source reading remains the home of its caption and original interpretation. Current interpretation may revise that caption through the claim ledger, later checkpoint, specialist or [identity/normalization errata](IMOSAE_PRIMARY_IDENTITY_AND_NORMALIZATION_ERRATA.md). Most notably, E023's old “Itsuki response” caption does not print an explicit reply. The route index exposes the corrected speaker ceiling rather than silently rebuilding the frozen reading.

For a contested claim: read the analytical sentence, retrieve its E unit, open the relevant scene with context, verify narrator/speaker and level, inspect original ruby/gaiji or artwork if material, then apply the stated inference. A resolved identifier alone does not prove the inference. Endpoints define a registered unit; decisive adjacent context is named explicitly in the analytical document.

## 2. Source hierarchy and retrieval surfaces

| Layer | Role | Authoritative route |
|---|---|---|
| IMOSAE-JP-LN-RAW-1.0 | Fourteen locked original Japanese EPUBs; ultimate authority for exact text, ruby, glyphs and assets | [Raw source manifest](../01%20Source%20Lock%20and%20Inventory/machine_readable/source_manifest.json), [source inventory](../01%20Source%20Lock%20and%20Inventory/IMOSAE_SOURCE_INVENTORY.md) and source lock |
| IMOSAE-JP-LN-NORM-1.0 | Frozen reading/retrieval derivative with paragraph/source-member coordinates | Normalized text folder (Drive ID `1621QxO9x3GpR2wh7bpXtSUB9zgA4AaDX`); sidecar folder (Drive ID `18yvch7xMrvPS3XobOoS7a4QIpevOEuil`) |
| Normalized release manifest | File identities and immutable payload boundary | Drive manifest (Drive ID `1IYRwvKtKcHWEIK-rQN_wF73h9qyjquht`), ID `1IYRwvKtKcHWEIK-rQN_wF73h9qyjquht` |
| IMOSAE-VISUAL-INDEX-1.0 | Classed raster assets and prose/paratext routes | [Frozen visual index](../01%20Source%20Lock%20and%20Inventory/machine_readable/illustration_paratext_index.jsonl), [illustration guide](IMOSAE_ILLUSTRATION_LOCATOR_INDEX.md) |
| IMOSAE-GAIJI-MAP-1.0 | Preserved inline graphic tokens and frozen replacement choices | [Gaiji register](../01%20Source%20Lock%20and%20Inventory/IMOSAE_GAIJI_AND_TEXT_NORMALIZATION_REGISTER.md), with explicit current analytical exceptions |
| Git analysis | Method, prospective readings, checkpoints, ledgers, specialists, models, terminals, indexes and audits | [Current corpus map](../CURRENT_STATE_AND_CORPUS_MAP.md) and the release manifest |

Working copies are execution material, not another source release. Original EPUBs, full normalized volumes, source images and private extraction scripts do not belong in this Git release. The source register and audit retain the immutable release identities and the exact payload scope actually checked.

## 3. Coordinate grammar and interpretation

A text coordinate has the form `VNN|chapter:…|spine:…|xhtml:…|p:…|fp:…`. The chapter is a source label, the spine/member route identifies the EPUB document, and p/fp identify a normalized paragraph. The sidecar also carries a source-block XPath and original/source/normalized hashes. A fingerprint alone cannot identify an edition or a speaker.

A visual coordinate has the form `VNN|ILL:…|member:…`. Legacy registers sometimes append a role annotation. That annotation is metadata on the same asset, not a different image. The frozen visual index supplies the asset hash and class. Inline gaiji images must not be mistaken for narrative illustrations merely because both are JPEGs.

TF and LF establish represented facts/language; PF concerns publication and creator framing; SF requires separately admitted supplemental evidence. FR, SI, IT and SP describe recurrence, inference, interpretation and speculation. An analytical rule is usually derived SI/IT, not an additional fact created by the index.

## 4. Diagnostic retrieval starts

| Question / risk | Start with | Current boundary |
|---|---|---|
| Was the extravagant opening actual life? | `IM-V01-E001` | Authored scenario and actual life differ |
| What happens in the first editorial meeting? | `IM-V01-E002` | Toki owns the meeting; E017 is Haruto's peer critique |
| What does the protagonist self-correction do? | `IM-V03-E114` | Private 僕→俺 act, not universal pronoun semantics |
| What is Nayuta's private gift? | `IM-V03-E034` | Particular audience/circulation, not automatic market duty |
| Does protective TRPG conviction make a miracle? | `IM-V04-E134`, `IM-V04-E135` | Displayed cost/outcome survives later PF qualifications |
| Does caretaking satisfaction prove fairness? | `IM-V09-E021` | Narrated imbalance and satisfaction coexist |
| Who participates in the concealment plan? | `IM-V10-E012`, `IM-V10-E029` | Distributed adult/child responsibility and dated knowledge |
| Is functional craft fake? | `IM-V11-E320`, `IM-V12-E323` | Functional recovery and personal integration differ |
| Did the V12 alternate route happen? | `IM-V12-E064`, `IM-V12-E065`, `IM-V12-E068` | Dream boundary and awake refusal separated |
| Is meeting always better than email? | `IM-V13-E379`, `IM-V13-E380` | Particular diagnosis with explicit channel exceptions |
| What is Miyako's actual dating gate? | `IM-V14-E008` | Next Itsuki book she edits; publication regardless of surpassing |
| Who receives Haruto's false report? | `IM-V14-E009` | LINE to Itsuki and Chihiro, not a changed promise to Miyako |
| Did Nayuta dislike every moment before return? | `IM-V14-E019` plus original p0021–0065 | Actual contentment and later new desire |
| Did Itsuki explicitly answer her care request? | `IM-V14-E023` | Spoken request/desire, no explicit reply |
| What did “stepping aside” concern? | `IM-V14-E024` p0066 | Miyako reports Ui/Chihiro romantic withdrawal, not retirement |
| Is Nayuta's sequel actual? | `IM-V14-E024` p0118–0125 | Actual work/publication assent; fourteen-year future is inside that work |
| Is the adolescent future actual biography? | `IM-V14-E042` | Explicit dream-based manuscript frame |
| Who can criticize the acclaimed author? | `IM-V14-E043`–`IM-V14-E047` | Living-person permission, craft criticism and a private separate goal |
| Does the astronaut picture prove a career? | `IM-V14-E076` | PF possibility, not actual achievement |

These are high-use entry routes, not replacements for context. The [Japanese index](IMOSAE_JAPANESE_PASSAGE_AND_TERMINOLOGY_INDEX.md) handles names/voice/gaiji; the [volume guide](IMOSAE_VOLUME_BY_VOLUME_EVIDENCE_LEDGER.md) handles chronological retrieval; the [supplement crosswalk](IMOSAE_SUPPLEMENT_CROSSWALK.md) prevents alternate/adaptation leakage.

## 5. Integrity and correction ceiling

The release source audit checks raw identity/ZIP integrity, fourteen sidecar identities/invariants, original block routes, all indexed raster hashes and evidence coordinate resolution. Semantic speaker/level checks are separately reported. It does not claim every old interpretation was freshly reread or every normalized payload re-fetched. V01–V13 and earlier checkpoints remain protected bytes.

The G005 exception applies to exactly two original-asset occurrences in V01 and V14. Their shared hash and original しか ruby establish scolding, while the frozen replacement 吐 remains untouched. Ordinary Unicode 吐 is unaffected. Use [the exact exception metadata](machine_readable/IMOSAE_G005_ANALYTICAL_EXCEPTION.json) rather than global text substitution.


## Source anchor index

Stable E identifiers route to the prospective reading registers and frozen source releases. Exact anchor/range endpoints are reproduced below; adjacent scene context is identified in the argument where needed. Coordinate resolution does not by itself certify attribution or inference. Original Japanese governs name, register and gaiji exceptions.

| Evidence | Primary route |
|---|---|
| IM-V01-E001 | V01\|chapter:小説家は妹キチ●イ\|spine:009\|xhtml:OEBPS/Text/p-0009.xhtml.xhtml\|p:0034\|fp:51c0ca64acf6 |
| IM-V01-E002 | V01\|chapter:小説家は妹キチ●イ\|spine:009\|xhtml:OEBPS/Text/p-0009.xhtml.xhtml\|p:0045\|fp:182da08e174a |
| IM-V03-E034 | V03\|chapter:２１歳\|spine:023\|xhtml:OEBPS/Text/p-0023.xhtml\|p:0126\|fp:03cced1e85e6 |
| IM-V03-E114 | V03\|chapter:番外編 羽島伊月の誕生\|spine:051\|xhtml:OEBPS/Text/p-0051.xhtml\|p:0125\|fp:2f7f2c4ce9a7 |
| IM-V04-E134 | V04\|chapter:クロニカクロニクル③\|spine:040\|xhtml:text/part0039.html\|p:0151\|fp:b771cc62d1de |
| IM-V04-E135 | V04\|chapter:クロニカクロニクル③\|spine:042\|xhtml:text/part0041.html\|p:0078\|fp:3f9181469670 |
| IM-V09-E021 | V09\|chapter:クリエイター２人とルームシェアすることになった女子大生の悩み\|spine:013\|xhtml:OEBPS/Text/p-0013.xhtml.xhtml\|p:0065\|fp:a2abe1f7afae |
| IM-V10-E012 | V10\|chapter:番外編 羽島千尋の誕生\|spine:011\|xhtml:OEBPS/Text/p-0011.xhtml.xhtml\|p:0161\|fp:695eb7793003 |
| IM-V10-E029 | V10\|chapter:番外編 羽島千尋の誕生\|spine:011\|xhtml:OEBPS/Text/p-0011.xhtml.xhtml\|p:0269\|fp:7c1dea5b3ad7 |
| IM-V11-E320 | V11\|chapter:他の誰が許そうとも、彼女だけはそれを許しはしない\|spine:051\|xhtml:OEBPS/Text/p-0052.xhtml.xhtml\|p:0095\|fp:f143d0efc507 |
| IM-V12-E064 | V12\|chapter:笠松青葉ルート（罠）\|spine:011\|xhtml:text/part0010.html\|p:0087\|fp:a22f3a66e9f7 |
| IM-V12-E065 | V12\|chapter:笠松青葉ルート（罠）\|spine:011\|xhtml:text/part0010.html\|p:0117\|fp:c3dd34790797 |
| IM-V12-E068 | V12\|chapter:笠松青葉ルート（罠）\|spine:011\|xhtml:text/part0010.html\|p:0120\|fp:59def94b752a |
| IM-V12-E323 | V12\|chapter:正解のない道\|spine:034\|xhtml:text/part0033.html\|p:0044\|fp:ad1c0469b02d |
| IM-V13-E379 | V13\|chapter:暗黒騎士\|spine:031\|xhtml:text/part0030.html\|p:0122\|fp:659dfb56463b |
| IM-V13-E380 | V13\|chapter:暗黒騎士\|spine:031\|xhtml:text/part0030.html\|p:0130\|fp:957df08e6d2d |
| IM-V14-E008 | V14\|chapter:北へ。\|spine:018\|xhtml:text/part0017.html\|p:0131\|fp:21fb8e2067df<br>V14\|chapter:北へ。\|spine:018\|xhtml:text/part0017.html\|p:0148\|fp:30ca6579b769 |
| IM-V14-E009 | V14\|chapter:北へ。\|spine:018\|xhtml:text/part0017.html\|p:0149\|fp:3df2c63e6f22<br>V14\|chapter:北へ。\|spine:018\|xhtml:text/part0017.html\|p:0162\|fp:b75ced6522be |
| IM-V14-E019 | V14\|chapter:シリウス\|spine:032\|xhtml:text/part0031.html\|p:0033\|fp:96aacf461ab3<br>V14\|chapter:シリウス\|spine:032\|xhtml:text/part0031.html\|p:0081\|fp:7a086195fea4 |
| IM-V14-E023 | V14\|chapter:報いの虹\|spine:036\|xhtml:text/part0035.html\|p:0035\|fp:1f6988b28f1d<br>V14\|chapter:報いの虹\|spine:036\|xhtml:text/part0035.html\|p:0039\|fp:2ebde1f8319d |
| IM-V14-E024 | V14\|chapter:報いの虹\|spine:036\|xhtml:text/part0035.html\|p:0040\|fp:3df2c63e6f22<br>V14\|chapter:報いの虹\|spine:036\|xhtml:text/part0035.html\|p:0127\|fp:77e434a84031 |
| IM-V14-E042 | V14\|chapter:青い小鳥たち\|spine:045\|xhtml:text/part0044.html\|p:0001\|fp:3df2c63e6f22<br>V14\|chapter:青い小鳥たち\|spine:045\|xhtml:text/part0044.html\|p:0009\|fp:863c59f341d6 |
| IM-V14-E043 | V14\|chapter:青い小鳥たち\|spine:045\|xhtml:text/part0044.html\|p:0010\|fp:b672901d8572<br>V14\|chapter:青い小鳥たち\|spine:045\|xhtml:text/part0044.html\|p:0029\|fp:4848713b23af |
| IM-V14-E047 | V14\|chapter:青い小鳥たち\|spine:045\|xhtml:text/part0044.html\|p:0081\|fp:abb071673c19<br>V14\|chapter:青い小鳥たち\|spine:045\|xhtml:text/part0044.html\|p:0092\|fp:29211d3ff670 |
| IM-V14-E076 | V14\|ILL:024\|member:images/00030.jpeg |
