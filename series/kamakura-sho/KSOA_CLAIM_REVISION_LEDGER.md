---
title: "Kamakura Police Station — claim revision ledger"
series: "Kamakura Police Station: The Case Files of Asumi Ogasawara / 鎌倉署・小笠原亜澄の事件簿"
series_id: kamakura-sho
artifact_id: KSOA_CLAIM_REVISION_LEDGER
artifact_type: claim_revision_ledger
generation: KSOA-G1
version: "1.0"
created: "2026-11-12"
status: canonical
scope: "Cross-unit interpretation, contradictory evidence and recoverable claim versions."
source_boundary: "Japanese publisher EPUBs V01–V07. Bibliography, bytes and package structure reconciled. Narrative admission and inspection are pending."
canonical_home: series/kamakura-sho/KSOA_CLAIM_REVISION_LEDGER.md
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
do_not_use_as_literary_evidence: true
---

# Claim revision ledger

**Analytical rows at initialization: 0.** This is the canonical home for versioned, material interpretive propositions, including disputed readings of character, prose form, clue placement, institutional practice, setting and theme. Case hypothesis history lives in the [disclosure ledger](KSOA_DISCLOSURE_AND_HYPOTHESIS_LEDGER.md), and local observations keep their source homes.

| Record | Required fields |
|---|---|
| Original claim | Stable claim ID, first version, generation, originating artifact/anchor, exact proposition, scope/continuity, story time where material, evidence horizon, claim type, confidence, supporting evidence IDs, counterevidence or plausible alternatives and outstanding diagnostic question |
| Revision | Stable revision ID and predecessor claim/version, revision author/date, new evidence horizon, new supporting and conflicting evidence, reason/transition, revised proposition and confidence, current disposition, and affected downstream paths/anchors |
| Open conflict | Competing claim IDs and evidence, suspected conflict class and its basis, unresolved point, effect on synthesis, and a specific way to resolve or bound it |

Use `KSOA-Vnn-CL-NNNN` for a claim that begins in a volume and `KSOA-SER-CL-NNNN` for a synthesis-origin claim. Append `-RNN` for versioned revisions and use a stable heading or anchor for each version. Retain formulation and evidence horizon. Link to a successor explicitly and keep the current pointer recoverable from the revision sequence. Simultaneous competing interpretations retain distinct IDs and remain visible until adjudicated. Changing a current claim requires meaningful evidence, correction of provenance, or explicit reasoning about the scope of the earlier claim.

| Archive transition | Use |
|---|---|
| `PRESERVE` | The tested formulation and bounds still hold |
| `STRENGTHEN` | New evidence adds support within the stated scope |
| `REVISE` | Wording, scope, mechanism or causal account changes |
| `DOWNGRADE` | Support narrows or confidence falls |
| `REJECT` | The evidence defeats the recorded formulation |
| `OPEN` | A material issue remains underdetermined or disputed |

Attach exact locators through the evidence IDs in the [case ledger](KSOA_CASE_EVIDENCE_LEDGER.md) or owning reading. Anchor any Japanese wording to the native witness. Record what later evidence changes in the current interpretation while preserving the earlier freeze and what it was reasonable to infer then. Review dependent arguments when a load-bearing premise changes. If an immutable reading contains a defect, point to an attributable erratum or superseding artifact and preserve its historical contents. If correction is blocked, make the defect and its impact visible under the [repository correction route](../../governance/policies/CHANGE_INTEGRATION_CHECKLIST.md#analytical-corrections-and-procedural-conflicts).

## V01 claim history

The [frozen V01 reading](readings/KSOA_V01_DEEP_READING.md) defines the exact witness, full paragraph addresses and disclosure checkpoints. All rows are in generation KSOA-G1 and resolve through that reading's section/member table. The evidence horizon bounds what can be inferred from each row.

| ID | Horizon | Native locators | Record |
|---|---|---|---|
| <a id="ksoa-v01-cl-0001"></a> KSOA-V01-CL-0001 | [H-0004](readings/KSOA_V01_DEEP_READING.md#ksoa-v01-h-0004) | C01 0629–0630, 0697–0749 | Official decision uses the available medical cause, notebook and illness evidence. It leaves the source of the substance and the manuscript unexplained. Original argument remains H-0004. |
| <a id="ksoa-v01-cl-0001-r01"></a> KSOA-V01-CL-0001-R01 | [H-0012](readings/KSOA_V01_DEEP_READING.md#ksoa-v01-h-0012) | C03 0669–0717, 0879–0879 | PRESERVE the represented official disposition and REVISE the explanation for agency. The prospective ambiguity survives historically. Affected V01 interpretation and future institutional study. |
| <a id="ksoa-v01-cl-0002"></a> KSOA-V01-CL-0002 | [H-0003](readings/KSOA_V01_DEEP_READING.md#ksoa-v01-h-0003) | PRO 0010–0019; C01 0455–0527 | An explicit title lets reader connect the two accounts before investigators have an independent handoff witness. Physical document and recipient still open. |
| <a id="ksoa-v01-cl-0002-r01"></a> KSOA-V01-CL-0002-R01 | [H-0012](readings/KSOA_V01_DEEP_READING.md#ksoa-v01-h-0012) | C03 0689–0692, 0752–0819, 1007–1042 | STRENGTHEN through nested account and recovery. Actual transfer and later withholding defeat an explanatory collapse of absence into nonexistence or initial theft. |
| <a id="ksoa-v01-cl-0003"></a> KSOA-V01-CL-0003 | [H-0007](readings/KSOA_V01_DEEP_READING.md#ksoa-v01-h-0007) | C02 0248–0292, 0351–0446 | Local knowledge moves the inquiry by turning an opaque sign into physical geography and a historical trace. Actual meaning to 上原 unresolved. |
| <a id="ksoa-v01-cl-0003-r01"></a> KSOA-V01-CL-0003-R01 | [H-0012](readings/KSOA_V01_DEEP_READING.md#ksoa-v01-h-0012) | C03 0428–0434, 0933–1006 | REVISE single referent. Geographic lead retains its causal value for discovering the relation; late wordplay and phone testimony limit reader-side fairness of exact homicide solution. |
| <a id="ksoa-v01-cl-0004"></a> KSOA-V01-CL-0004 | [H-0010](readings/KSOA_V01_DEEP_READING.md#ksoa-v01-h-0010) | C03 0243–0375, 0492–0527 | The book dramatizes differences among literary, sacramental and investigative disclosure. The priest acts on perceived permission, and later test contents are currently withheld from the reader. |
| <a id="ksoa-v01-cl-0004-r01"></a> KSOA-V01-CL-0004-R01 | [H-0012](readings/KSOA_V01_DEEP_READING.md#ksoa-v01-h-0012) | C03 0565–0667, 0933–1017, 1021–1138 | STRENGTHEN with false voice, separate evidence retrieval, public confrontation and represented publication consent. Keep ethical counterreading and no inferred legal validation. |
| <a id="ksoa-v01-cl-0005"></a> KSOA-V01-CL-0005 | [H-0005](readings/KSOA_V01_DEEP_READING.md#ksoa-v01-h-0005) | C01 0055–0079, 0580–0589, 0811–0843, 0975–1017 | Long familiarity enables professional cooperation, coercion and repair. The direction and meaning of each response differ. |
| <a id="ksoa-v01-cl-0005-r01"></a> KSOA-V01-CL-0005-R01 | [H-0013](readings/KSOA_V01_DEEP_READING.md#ksoa-v01-h-0013) | C02 0719–0738; EPI 0025–0075 | STRENGTHEN operational respect. OPEN on durable mutual romantic intention. The epilogue's private focalization and intoxication limit projection to later volumes. |
| <a id="ksoa-v01-cl-0006"></a> KSOA-V01-CL-0006 | [H-0012](readings/KSOA_V01_DEEP_READING.md#ksoa-v01-h-0012) | C03 0783–0835, 1042–1108, 1113–1138 | The ending distinguishes valued work, social kinship and biological history after the hidden inheritance becomes known. The legal disposition and other affected voices remain outside the portrayed agreement. |

## V02 claim history

The [frozen V02 reading](readings/KSOA_V02_DEEP_READING.md) defines the exact witness, full paragraph addresses and disclosure checkpoints. All rows are in generation KSOA-G1 and resolve through that reading's section/member table. The evidence horizon bounds what can be inferred from each row.

| ID | Horizon | Native locators | Record |
|---|---|---|---|
| <a id="ksoa-v02-cl-0001"></a> KSOA-V02-CL-0001 | [H-0006](readings/KSOA_V02_DEEP_READING.md#ksoa-v02-h-0006) | C01 0994–0998 | OPEN. An extra recorded interval supports multiple plausible causal histories. Tie the unresolved condition to EV-0004 and future mystery and procedure studies. |
| <a id="ksoa-v02-cl-0001-r01"></a> KSOA-V02-CL-0001-R01 | [H-0013](readings/KSOA_V02_DEEP_READING.md#ksoa-v02-h-0013) | C03 0721–0789 | STRENGTHEN the significance of the anomaly. The first confession fits the outer interval and disputes the inner interval. The team closes on a one-actor inference. See EV-0013 and RES-0001. |
| <a id="ksoa-v02-cl-0001-r02"></a> KSOA-V02-CL-0001-R02 | [H-0014](readings/KSOA_V02_DEEP_READING.md#ksoa-v02-h-0014) | C03 1004–1026 | REVISE attribution after EV-0014 and EV-0015. Independent actions with distinct targets explain RES-0002. Retain the original information limits. |
| <a id="ksoa-v02-cl-0001-r03"></a> KSOA-V02-CL-0001-R03 | [H-0015](readings/KSOA_V02_DEEP_READING.md#ksoa-v02-h-0015) | C03 0772–0792, 1004–1059; EPI 0019–0025 | PRESERVE institutional closure as a real action and distinguish it from the later causal resolution. Extend V01 CL-0001-R01's claim across two structurally different cases. |
| <a id="ksoa-v02-cl-0002"></a> KSOA-V02-CL-0002 | [H-0011](readings/KSOA_V02_DEEP_READING.md#ksoa-v02-h-0011) | C03 0122–0164, 0212–0258 | OPEN. Sustained support admits both solidarity and a possible unreported cause. Motoya's doubt supplies a counterreading, not evidence of specific wrongdoing. See EV-0009. |
| <a id="ksoa-v02-cl-0002-r01"></a> KSOA-V02-CL-0002-R01 | [H-0014](readings/KSOA_V02_DEEP_READING.md#ksoa-v02-h-0014) | C03 0972–1002, 1046–1055 | REVISE the account of Michiyasu's death and Satomi's possible involvement in the earlier dismissal. Distinguish reported actions from Satomi's intentions and Motoya's atonement inference. See EV-0015. |
| <a id="ksoa-v02-cl-0003"></a> KSOA-V02-CL-0003 | [H-0010](readings/KSOA_V02_DEEP_READING.md#ksoa-v02-h-0010) | C02 0852–0900 | OPEN. Shiina's responses show a strongly avowed professional and personal attachment, and interest in prestige. No homicide implication at this cutoff. See EV-0008. |
| <a id="ksoa-v02-cl-0003-r01"></a> KSOA-V02-CL-0003-R01 | [H-0014](readings/KSOA_V02_DEEP_READING.md#ksoa-v02-h-0014) | C03 0956–1002 | REVISE. Shiina's professed protective motive now accompanies direct admission of redirection. See EV-0015. |
| <a id="ksoa-v02-cl-0003-r02"></a> KSOA-V02-CL-0003-R02 | [H-0014](readings/KSOA_V02_DEEP_READING.md#ksoa-v02-h-0014) | C03 1028–1055 | OPEN the weighting of loyalty, status and self-interest. Ayane names a concrete incentive but is a participant with incomplete access. See EV-0016. |
| <a id="ksoa-v02-cl-0004"></a> KSOA-V02-CL-0004 | [H-0009](readings/KSOA_V02_DEEP_READING.md#ksoa-v02-h-0009) | C01 0249–0355; C02 0642–0714 | PRESERVE V01 CL-0005-R01's bounded baseline. Familiarity and mutual observation support professional coordination and teasing without proving durable romance. |
| <a id="ksoa-v02-cl-0004-r01"></a> KSOA-V02-CL-0004-R01 | [H-0013](readings/KSOA_V02_DEEP_READING.md#ksoa-v02-h-0013) | C03 0787–0839 | STRENGTHEN evidence of directed reliance and asymmetrical leverage. Asumi recruits Motoya through remembered childhood aid after he has accepted closure. |
| <a id="ksoa-v02-cl-0004-r02"></a> KSOA-V02-CL-0004-R02 | [H-0015](readings/KSOA_V02_DEEP_READING.md#ksoa-v02-h-0015) | EPI 0019–0087 | PRESERVE the open relationship classification. Ordinary vulnerability and an outsider's label have different evidential weight. Follow this into the partnership specialist. |
| <a id="ksoa-v02-cl-0005"></a> KSOA-V02-CL-0005 | [H-0014](readings/KSOA_V02_DEEP_READING.md#ksoa-v02-h-0014) | C01 0533–0578, 0643–0649, 0994–0998; C03 1004–1026 | OPEN early precise identification while STRENGTHENING reader-side detectability of a causal gap. The stage and security evidence precedes the reveal. Confirmation of the anomalous routine, spare access and redirection is late. |
| <a id="ksoa-v02-cl-0006"></a> KSOA-V02-CL-0006 | [H-0012](readings/KSOA_V02_DEEP_READING.md#ksoa-v02-h-0012) | C02 0115–0249, 0467–0646; C03 0309–0435 | STRENGTHEN that division of labor and mediation sustain authority. Yura's practical witness and Satomi's own description corroborate only overlapping aspects. Compare Ayane's private support. |
| <a id="ksoa-v02-cl-0006-r01"></a> KSOA-V02-CL-0006-R01 | [H-0014](readings/KSOA_V02_DEEP_READING.md#ksoa-v02-h-0014) | C03 0902–0938, 1046–1059 | PRESERVE the theme across the final performance and changed succession. Avoid equating musical co-work, mediated testimony and uncoordinated causal contribution. |

## V03 claim history

The [frozen V03 reading](readings/KSOA_V03_DEEP_READING.md) defines the exact witness, full paragraph addresses and disclosure checkpoints. All rows are in generation KSOA-G1 and resolve through that reading's section/member table. The evidence horizon bounds what can be inferred from each row.

| ID | Horizon | Native locators | Record |
|---|---|---|---|
| <a id="ksoa-v03-cl-0001"></a> KSOA-V03-CL-0001 | [H-0004](readings/KSOA_V03_DEEP_READING.md#ksoa-v03-h-0004) | C01 0902–0987 | OPEN. The pictured woman and site may connect the unnamed prologue to a historical event. Visual attribution is distinct from literal reportage. See EV-0003. |
| <a id="ksoa-v03-cl-0001-r01"></a> KSOA-V03-CL-0001-R01 | [H-0011](readings/KSOA_V03_DEEP_READING.md#ksoa-v03-h-0011) | PRO 0004–0035; C03 0083–0135, 0337–0358, 0399–0417 | STRENGTHEN Mariko identification and REVISE the old accident account toward probable homicide. One reported letter and the attributed painted confession give two transmission routes. Preserve the cause and agency limits of the prologue itself. |
| <a id="ksoa-v03-cl-0002"></a> KSOA-V03-CL-0002 | [H-0008](readings/KSOA_V03_DEEP_READING.md#ksoa-v03-h-0008) | C01 0864–0899, 0961–0987; C02 0250–0268, 0345–0412 | OPEN. Art, market, inheritance and prestige make overlapping hypotheses. A dealer's prospective price and an heir's spending are clues to incentives without actions. |
| <a id="ksoa-v03-cl-0002-r01"></a> KSOA-V03-CL-0002-R01 | [H-0011](readings/KSOA_V03_DEEP_READING.md#ksoa-v03-h-0011) | C03 0239–0245, 0261–0313 | REVISE a merely speculative market into admitted contingent transactions. Verified alibi defeats direct physical agency for Haruto. A sale incentive survives as a separate state. |
| <a id="ksoa-v03-cl-0003"></a> KSOA-V03-CL-0003 | [H-0002](readings/KSOA_V03_DEEP_READING.md#ksoa-v03-h-0002) | C01 0123–0185 | OPEN. A known-contact meeting and multiple injuries are provisional descriptions. The inferred motive and number of actors are unresolved. |
| <a id="ksoa-v03-cl-0003-r01"></a> KSOA-V03-CL-0003-R01 | [H-0011](readings/KSOA_V03_DEEP_READING.md#ksoa-v03-h-0011) | C03 0373–0433 | REVISE with independent call attribution and the first admission. The encounter and initial attack are strongly supported. Exact conversation and planning still depend on the speaker. |
| <a id="ksoa-v03-cl-0003-r02"></a> KSOA-V03-CL-0003-R02 | [H-0012](readings/KSOA_V03_DEEP_READING.md#ksoa-v03-h-0012) | C03 0436–0539 | REVISE the causal account through medical discrepancy, stone, travel witness and second admission. Strengthen the cross-volume distinction between causal contribution and joint intent. V02 redirection precedes the event. V03 intervention follows a first assault. |
| <a id="ksoa-v03-cl-0004"></a> KSOA-V03-CL-0004 | [H-0012](readings/KSOA_V03_DEEP_READING.md#ksoa-v03-h-0012) | C02 0651–0668; C03 0399–0418, 0487–0533 | OPEN relative motive weights. Both women describe career interest. Keiko also invokes care and shared stigma. Maya's acknowledgment and claims about the victim have different evidential status from her admission. |
| <a id="ksoa-v03-cl-0005"></a> KSOA-V03-CL-0005 | [H-0010](readings/KSOA_V03_DEEP_READING.md#ksoa-v03-h-0010) | C03 0141–0229 | STRENGTHEN V02's evidence for learned color perception. Asumi's observation is corroborated by a painter while the buried-material hypothesis still requires examination. Affected character and sensory-form studies. |
| <a id="ksoa-v03-cl-0006"></a> KSOA-V03-CL-0006 | [H-0012](readings/KSOA_V03_DEEP_READING.md#ksoa-v03-h-0012) | C02 0164–0177; C03 0186–0229, 0245–0258, 0467–0486 | STRENGTHEN the role of consent and discretion as separate variables. Owner consent, breach of a witness assurance, bounded circulation and deception each make a different claim to legitimacy. |
| <a id="ksoa-v03-cl-0007"></a> KSOA-V03-CL-0007 | [H-0013](readings/KSOA_V03_DEEP_READING.md#ksoa-v03-h-0013) | EPI 0024–0128 | REVISE the care component of V02 CL-0004-R02 by adding Asumi's stated history of assumed self-sufficiency. PRESERVE uncertainty about directed romantic intention and assign distinct reasons to each act of remaining. |

## V04 claim history

The [frozen V04 reading](readings/KSOA_V04_DEEP_READING.md) defines the exact witness, full paragraph addresses and disclosure checkpoints. All rows are in generation KSOA-G1 and resolve through that reading's section/member table. The evidence horizon bounds what can be inferred from each row.

| ID | Horizon | Native locators | Record |
|---|---|---|---|
| <a id="ksoa-v04-cl-0001"></a> KSOA-V04-CL-0001 | [H-0004](readings/KSOA_V04_DEEP_READING.md#ksoa-v04-h-0004) | PRO 0034–0051; C01 0511–0557, 0623–0645 | OPEN. The victim's selective viewing and observable wrist attention support a material clue. His conclusion, medium comparison and precise object remain unverified. |
| <a id="ksoa-v04-cl-0001-r01"></a> KSOA-V04-CL-0001-R01 | [H-0005](readings/KSOA_V04_DEEP_READING.md#ksoa-v04-h-0005) | C01 0795–0825, 0898–0936 | STRENGTHEN the role of the film in the research route while preserving limited playback fidelity. Two unsuccessful stream viewings do not show that all versions are evidentially equivalent. |
| <a id="ksoa-v04-cl-0001-r02"></a> KSOA-V04-CL-0001-R02 | [H-0013](readings/KSOA_V04_DEEP_READING.md#ksoa-v04-h-0013) | C03 0875–0926 | REVISE with the attributed bracelet transfer and recognition. An image can license investigation without independently establishing parentage, blackmail or a motive. |
| <a id="ksoa-v04-cl-0002"></a> KSOA-V04-CL-0002 | [H-0011](readings/KSOA_V04_DEEP_READING.md#ksoa-v04-h-0011) | C03 0175–0229, 0262–0342 | OPEN. Long service and gatekeeping make a protection hypothesis testable. The analogy with devotional love comes first from Yamashina. |
| <a id="ksoa-v04-cl-0002-r01"></a> KSOA-V04-CL-0002-R01 | [H-0012](readings/KSOA_V04_DEEP_READING.md#ksoa-v04-h-0012) | C03 0519–0587 | OPEN alongside a rival money explanation. Passbook evidence concerns the withdrawal, independent of its stated purpose. |
| <a id="ksoa-v04-cl-0002-r02"></a> KSOA-V04-CL-0002-R02 | [H-0013](readings/KSOA_V04_DEEP_READING.md#ksoa-v04-h-0013) | C03 0700–0823, 0875–0955 | REVISE motive attribution after Shichijō discloses and Miyazaki supplies first-person reasoning. His account preserves devotion and anger at a demand with different sources of support. |
| <a id="ksoa-v04-cl-0003"></a> KSOA-V04-CL-0003 | [H-0003](readings/KSOA_V04_DEEP_READING.md#ksoa-v04-h-0003) | C01 0324–0371 | OPEN route through the locked memorial. The discovery party's reported actions do not cover every key. |
| <a id="ksoa-v04-cl-0003-r01"></a> KSOA-V04-CL-0003-R01 | [H-0013](readings/KSOA_V04_DEEP_READING.md#ksoa-v04-h-0013) | C03 0956–0988 | STRENGTHEN access as unresolved after direct attribution. Police hear a source segment withheld from the reader. |
| <a id="ksoa-v04-cl-0003-r02"></a> KSOA-V04-CL-0003-R02 | [H-0014](readings/KSOA_V04_DEEP_READING.md#ksoa-v04-h-0014) | C03 1030–1126 | REVISE with legal marriage, verified absence, reported debt and admitted transfer. Differentiate this linked facilitation from V02 redirection and V03 sequential assault. Instigation remains the represented investigative theory. |
| <a id="ksoa-v04-cl-0004"></a> KSOA-V04-CL-0004 | [H-0014](readings/KSOA_V04_DEEP_READING.md#ksoa-v04-h-0014) | C01 0260–0294, 0745–0775; C03 0692–0756, 0991–1132 | STRENGTHEN secrecy and legacy as distinct actions. Preserve competing responsibilities to accurate account, family privacy, public reputation and credit. |
| <a id="ksoa-v04-cl-0005"></a> KSOA-V04-CL-0005 | [H-0015](readings/KSOA_V04_DEEP_READING.md#ksoa-v04-h-0015) | C03 0362–0486; EPI 0017–0055, 0080–0137 | STRENGTHEN observable field reliance and Asumi's bids for company. OPEN directed intent and what Motoya's begrudging care signifies. Continue V03 CL-0007. |
