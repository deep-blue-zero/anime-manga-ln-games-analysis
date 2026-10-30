---
title: "Cornered Mouse — Claims, Predictions and Revisions Ledger"
artifact_id: CORNERED_MOUSE_CLAIMS_PREDICTIONS_AND_REVISIONS_LEDGER
artifact_type: claim_revision_ledger
series: "The Cornered Mouse Dreams of Cheese / 窮鼠はチーズの夢を見る"
series_id: cornered-mouse
generation: CORNERED_MOUSE_BOOTSTRAP_V1
version: "0.9"
status: active_provisional
scope: "Interpretive claim lineage, genuine prospective forecasts and revision impact"
source_boundary: "Japanese manga continuity; CM-JP-AIO2020-LOCAL through CM-U06 first-work exit; narrative144–202, frontispiece143 and closing art203/204 separate"
canonical_home: series/cornered-mouse/03 Longitudinal Ledgers/CORNERED_MOUSE_CLAIMS_PREDICTIONS_AND_REVISIONS_LEDGER.md
created: "2026-10-24"
updated: "2026-10-30"
review_status: SOURCE_GROUNDED_AUTHOR_CLOSEOUT
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
do_not_use_as_literary_evidence: true
---

# Claims, predictions and revisions

**Claims: 15. Predictions: 6 (three adjudicated, three prospective model tests pending). Claim revision events: 24. Forecast adjudication events: 3. Source boundary: CM-U06.** U01 formulations and original forecast bytes remain unchanged; the current projection and appended U02 events identify later authority. Follow the [method](../00%20Frameworks%20and%20Methods/CORNERED_MOUSE_ANALYTICAL_METHOD.md) and [architecture](../00%20Frameworks%20and%20Methods/CORNERED_MOUSE_SYNTHESIS_ARCHITECTURE.md).

## Schemas and revision vocabulary

| Claim field | Meaning |
|---|---|
| `claim_id`, `version`, `created_boundary`, `current_authority` | Stable `CM-CL-...` identity, originating freeze and current formulation home |
| `kind`, `formulation`, `witness_scope`, `temporal_scope`, `disclosure_boundary` | Observation/testimony/interpretation/alternative/hypothesis/question/value judgment; avoid scope drift |
| `evidence_refs`, `source_locators`, `counterevidence`, `credible_alternative` | Source retrieval and competing explanations |
| `confidence`, `confidence_reason`, `falsifier`, `unresolved` | Calibrated limits and disconfirmation |
| `revision_history`, `downstream_homes` | Earlier formulations and affected state/specialist/model routes |

Each revision appends `(revision_id, claim_id, old_version/formulation, transition, new_version/formulation, source/disclosure boundary, evidence/counterevidence, reason, downstream dispositions)`. Use `PRESERVE` for retained formulation, `STRENGTHEN` for stronger support, `REVISE` for changed content, `DOWNGRADE` for weaker confidence/scope, `REJECT` for an unsupported claim retained as history, and `OPEN` for unresolved adjudication. Rejection never deletes the prior claim.

| Prediction field | Meaning |
|---|---|
| `prediction_id`, `rule_or_claim_ref`, `recorded_at`, `preoutcome_commit_or_freeze` | Stable `CM-PR-...` and proof it predates inspection |
| `entering_knowledge`, `prior_exposure`, `target`, `predicted_range`, `falsifier` | What could be known, outcome window and discriminating expectation |
| `outcome_ref`, `adjudication`, `non_discrimination_or_abstention_reason`, `rule_revision_ref` | Later support/failure/mixed/non-discriminating/unobserved result, preserving original wording |

## Update contract

Material claims get stable identities and append-only revision events; the current projection may change while every earlier version remains recoverable. Frozen readings, forecasts and genuine preoutcome commits remain unchanged. Later source explanations revise the present claim at the later disclosure point. Retrospectively reconstructed forecasts are labeled RETROSPECTIVE and never counted as genuine predictions or holdout success.

Record downstream changes explicitly so a stale monograph, relationship argument or rule cannot retain a rejected premise silently. A credible unresolved alternative remains visible; no arbitrary confidence score or model agreement replaces evidence. At bootstrap no forecast, character motive or ethical conclusion is created.

## Claims

Common initial fields: version 1; created/disclosure boundary `CM-U01-EXIT`; witness `CM-JP-AIO2020-LOCAL`; current authority is this ledger's source-bounded formulation, with evidence in the immutable [U01 reading](../01%20Sequential%20Readings/CORNERED_MOUSE_U01_DEEP_READING.md). No claim covers later chapters or all editions. Revision history is NONE at creation. Source spines expand to exact members/digests through that reading. Confidence is qualitative and explained, never a fabricated probability.

### CM-CL-001 v1 — responsive and evasive agency

Primary evidence route: [CM-U01-O015](../01%20Sequential%20Readings/CORNERED_MOUSE_U01_DEEP_READING.md#cm-u01-o015); `CM-JP-AIO2020-LOCAL::sp0025::xhtml=item/xhtml/p-0023.xhtml::image=item/image/i-0023.jpg::panel=P00`.

**Kind:** SUPPORTED_INTERPRETATION. **Formulation:** Across U01, Otomo often prefers responsive accommodation and explains unwanted consequences through others' initiative; literal absence of agency is contradicted by his own initiated acts and exits. **Scope:** U01 event trajectory, not lifelong personality. **Evidence:** O003,O011–O012,O014–O015,O019–O026,O029,O031,O038–O040; sp0013,0021–0025,0029–0036,0039,0041,0048–0050. **Counterevidence/alternative:** shopping, suit request, calls and refusal are genuine choices; care or situational caution can explain some accommodation. Imagase/Chikako are interested critics. **Confidence:** moderate for recurring pattern, high against total passivity. **Falsifier:** a source/attribution correction removing the recurring self-exculpatory/ease evidence would defeat this formulation; later independent initiative should restrict its predictive scope rather than erase U01 observations. **Unresolved:** stable disposition versus marriage-specific strategy. **Downstream:** CM-CS-001/003, CM-RS-001–005, CM-DEC-001/002/004/006; no monograph/model yet.

### CM-CL-002 v1 — pressure and permission remain distinct from pleasure

Primary evidence route: [CM-U01-O009](../01%20Sequential%20Readings/CORNERED_MOUSE_U01_DEEP_READING.md#cm-u01-o009); `CM-JP-AIO2020-LOCAL::sp0019::xhtml=item/xhtml/p-0017.xhtml::image=item/image/i-0017.jpg::panel=P00`.

**Kind:** SUPPORTED_INTERPRETATION and explicitly supported VALUE_JUDGMENT. **Formulation:** Report-based pressure and the overriding of stated bodily limits make the hotel contact coercive in its shown mechanism; Otomo's later stated pleasure does not constitute authorization of those overridden limits. **Evidence:** O002–O004,O009–O018; sp0012–0014,0019–0028. **Counterevidence/alternative:** narrowed bargain and pleasure are real, and desire may coexist with coercion; neither demonstrates a renewed agreement at the contested moments. **Confidence:** high for explicit pressure/refusals and the distinction, open for every private feeling. **Falsifier:** evidence that the refusal/pressure speech was misattributed or that a contemporaneous unpressured agreement actually precedes the specific contested act would require revision of that act's assessment. Later love cannot be that evidence. **Scope/unresolved:** hotel sequences only; reunion assessed separately. **Downstream:** CM-CS-001/002, CM-RS-001, CM-INF-001/002, CM-DEC-001; future ethics/intimacy work.

### CM-CL-003 v1 — Chikako's disclosed exit changes the causal account

Primary evidence route: [CM-U01-O029](../01%20Sequential%20Readings/CORNERED_MOUSE_U01_DEEP_READING.md#cm-u01-o029); `CM-JP-AIO2020-LOCAL::sp0039::xhtml=item/xhtml/p-0037.xhtml::image=item/image/i-0037.jpg::panel=P00`.

**Kind:** SUPPORTED_INTERPRETATION. **Formulation:** Chikako's direct divorce/compensation/new-partner account displaces Otomo's assumption that report delivery caused the request and gives her an independent critique of the marriage's responsive pattern. **Evidence:** O007,O014–O015,O019–O020,O027–O030; sp0017,0024–0025,0029–0030,0037–0040. **Counterevidence/alternative:** she may give a selective, self-serving account; no independent full history proves it exhaustive. Material self-interest and relational dissatisfaction can coexist. **Confidence:** high for disclosure and correction of what is warranted, moderate for her whole marital explanation. **Falsifier:** direct evidence of delivery actually motivating the request would revise causality; absence of that evidence prevents treating Otomo's assumption as fact. **Unresolved:** private chronology, knowledge of men's encounters, new partner's perspective. **Downstream:** CM-CS-003/001, CM-RS-005, CM-INF-003/004, CM-DEC-003; secondary-agency responsibility.

### CM-CL-004 v1 — psychology is interested speech; knowledge is unequal

Primary evidence route: [CM-U01-O034](../01%20Sequential%20Readings/CORNERED_MOUSE_U01_DEEP_READING.md#cm-u01-o034); `CM-JP-AIO2020-LOCAL::sp0044::xhtml=item/xhtml/p-0042.xhtml::image=item/image/i-0042.jpg::panel=P00`.

**Kind:** SUPPORTED_INTERPRETATION. **Formulation:** Imagase's confident readings of Otomo have partial local support but are not omniscient; his own prior knowledge and exclusive-care claim remain unconfirmed, while the phone scene gives readers visual knowledge Otomo lacks. **Evidence:** O012–O013,O023–O025,O031–O035; sp0022–0023,0033–0035,0041–0045. **Counterevidence/alternative:** acknowledged affairs, ease language and loss support some of his insight; manipulation alone is insufficient as an exhaustive explanation. **Confidence:** high for source/access distinction, moderate for mixed insight and interest, low for exact hidden motives. **Falsifier:** an actual focal shift into his interior or explicit prior-knowledge disclosure could settle particular uncertainties; it would not retroactively give Otomo sight of the kitchen. **Unresolved:** assignment design, prior divorce knowledge, motives of companion. **Downstream:** CM-CS-001/002/004, CM-RS-002/003/006, CM-INF-004/005/006; form/agency responsibilities.

### CM-CL-005 v1 — renewed contact leaves terms open

Primary evidence route: [CM-U01-O040](../01%20Sequential%20Readings/CORNERED_MOUSE_U01_DEEP_READING.md#cm-u01-o040); `CM-JP-AIO2020-LOCAL::sp0050::xhtml=item/xhtml/p-0048.xhtml::image=item/image/i-0048.jpg::panel=P00`.

**Kind:** SUPPORTED_INTERPRETATION. **Formulation:** The reunion reopens contact after loss and withdrawal, with dating explicitly refused and a trip welcomed in principle; the closing kiss does not establish stable couplehood, exclusivity or repair of earlier coercion. **Evidence:** O035–O040; sp0045–0050. **Counterevidence/alternative:** no report threat is restated and no fresh protest is depicted; attraction/attachment is plausible. The activity invitation may be a genuine accommodating step or strategic reframing. **Confidence:** high for explicit terms/action, moderate for reengagement, unknown for durable agreement. **Falsifier:** contemporaneous explicit dating/exclusivity/repair speech omitted from this inspected range would require correction; later new agreements establish a later state rather than rewrite this one. **Unresolved:** love, orientation, durable permission, future conduct. **Downstream:** CM-CS-001/002, CM-RS-004, CM-DEC-006; CM-PR-001/002.

### CM-CL-006 v1 — formal delay and unequal access shape interpretation

Primary evidence route: [CM-U01-O008](../01%20Sequential%20Readings/CORNERED_MOUSE_U01_DEEP_READING.md#cm-u01-o008); `CM-JP-AIO2020-LOCAL::sp0018::xhtml=item/xhtml/p-0016.xhtml::image=item/image/i-0016.jpg::panel=P00`.

**Kind:** SUPPORTED_INTERPRETATION. **Formulation:** Reordered hotel/home recollection, slowed wordless contact, late direct spousal speech, compositional separation and reader-only kitchen action make explanations provisional and distinguish speech from visible surplus. **Evidence:** O001–O010,O020–O021,O027–O036,O040; sp0011–0020,0030–0031,0037–0046,0050. **Counterevidence/alternative:** some imagery also serves pacing or decoration; fish metaphor is suggestive rather than a proven single symbolic code. A cup echo does not prove the earlier attributed impulse. **Confidence:** high for layout/order/access, moderate for thematic function. **Falsifier:** corrected page ordering or focal attribution could revise the mechanism; species identification and measured duration are not premises. **Unresolved:** cross-unit recurrence and ending significance. **Downstream:** originating U01 reading and later form/literary synthesis; no separate visual ledger warranted yet.


## U02 new claims

CM-CL-007–009 originate at CM-U02-EXIT, version 1, witness `CM-JP-AIO2020-LOCAL`, disclosure/temporal scope through U02. They do not inherit U01's creation boundary. All are SUPPORTED_INTERPRETATION; ethical distinctions are explicitly identified where used. The U02 reading owns evidence, and the coverage table expands its exact source members/digests.

### CM-CL-007 v1 — gendered normalcy is a self-explanation

Primary route: [CM-U02-O011](../01%20Sequential%20Readings/CORNERED_MOUSE_U02_DEEP_READING.md#cm-u02-o011); `CM-JP-AIO2020-LOCAL::sp0061::xhtml=item/xhtml/p-0059.xhtml::image=item/image/i-0059.jpg::panel=P00`. **Formulation:** Kyoichi's distinction between normal heterosexual manhood and intimacy with Imagase organizes his self-explanations without fully containing his pleasure, attention, felt loss or active reengagement; it does not by itself settle orientation or ethical responsibility. **Evidence:** O003–O011,O018–O023,O029–O040, sp0053–0061,0068–0073,0079–0090. **Counterevidence/alternative:** his stated resistance/not-gay description is real and cannot be dismissed as merely false; heterosexual desire is also shown. Social identity, specific-person attachment, anxiety and exploration may coexist. **Confidence:** high for wording/contradiction, moderate for explanatory pattern, open for enduring identity. **Falsifier:** corrected speaker/thought attribution removing these classifications would revise the claim; later identity statements establish later states, not a retrospective universal. **Unresolved:** how desire, labels and commitment develop. **Downstream:** CM-CS-005/006, CM-RS-007–012, CM-INF-008/012; intimacy/literary responsibilities. No model claim.

### CM-CL-008 v1 — active participation changes the encounter without certifying every limit

Primary route: [CM-U02-O033](../01%20Sequential%20Readings/CORNERED_MOUSE_U02_DEEP_READING.md#cm-u02-o033); `CM-JP-AIO2020-LOCAL::sp0083::xhtml=item/xhtml/p-0081.xhtml::image=item/image/i-0081.jpg::panel=P00`. **Formulation:** U02 shifts from contested routine to active initiative and an explicit demand for participation, while pressure, Imagase's own protest and withheld permission answers prevent a blanket claim that every act/relationship term is consensually settled. **Evidence:** O004–O006,O029–O033,O037–O040, sp0054–0056,0079–0083,0087–0090. **Counterevidence/alternative:** Kyoichi's initiative is a substantial change; Imagase says he cannot accept ambiguous passive YES and asks specific permissions. These facts resist a static one-direction/no-change account. Yet compensation demands, cornering and intercepted exit remain constraints. **Confidence:** high for actions/utterances and equal-direction permission standard; open for off-panel agreement and unique motives. **Falsifier:** contemporaneous source evidence of an explicit answer/agreement would settle that particular gap; it could not retroactively authorize U01 limits. **Unresolved:** affection versus fear of loss/exploration/provocation, durable mutual understanding. **Downstream:** CM-CS-005/006, CM-RS-007/010/011, CM-INF-007/012, CM-DEC-010/011; ethics/relationship responsibilities. No broad ethical reform or orientation verdict.

### CM-CL-009 v1 — Nishimura has agency and an incomplete family account

Primary route: [CM-U02-O024](../01%20Sequential%20Readings/CORNERED_MOUSE_U02_DEEP_READING.md#cm-u02-o024); `CM-JP-AIO2020-LOCAL::sp0074::xhtml=item/xhtml/p-0072.xhtml::image=item/image/i-0072.jpg::panel=P00`. **Formulation:** Nishimura's invitations, reassurance-seeking, family complaints and alibi establish an independently acting person in an affair; her difficulties and Kyoichi's normalcy narrative do not erase either participant's choices or certify every family fault. The men's clean-ending account is not her complete aftermath. **Evidence:** O002–O003,O009–O014,O024–O029, sp0052–0053,0059–0064,0074–0079. **Counterevidence/alternative:** her testimony can be selective; husband/child/mother-in-law are unvoiced. The affair may seek validation, attraction, respite or several aims. Kyoichi's reassurance/convenience are not a complete motive either. **Confidence:** high for requests/actions, qualified for household history and ending. **Falsifier:** an independent household view or later direct account could revise fault/aftermath; no unshown abuse/divorce plan is assumed. **Unresolved:** her later understanding and choices. **Downstream:** CM-CS-007, CM-RS-012, CM-INF-008/011, CM-DEC-007/013; secondary-agency responsibility.

## Predictions

These original formulations freeze with `CM-U01-EXIT` and the atomic U01 transaction commit, recorded at `2026-10-30T04:09:20+00:00`. Git history binds this exact version before U02 narrative inspection. Entering knowledge is the complete U01 endpoint; prior exposure includes bibliography/contents and the explicitly declared U02 frontispiece crops, not U02 scenes. They are not blind/model-validation tests. Later outcomes append adjudication events; this original text stays fixed.

### CM-PR-001 — contact with classification resistance

- **Rule/claim refs:** CM-CL-001/005, not an operational behavior rule.
- **Target:** complete CM-U02, first future component only.
- **Predicted range:** Otomo will explicitly resist a male-romantic/couple classification while also voluntarily accepting or initiating at least one private social encounter with Imagase within U02. Both conditions are required for support.
- **Falsifier/adjudication:** unqualified explicit acceptance of dating before any resistance, or refusal of all such encounters throughout an otherwise observable U02, defeats the conjunction. One condition alone is MIXED; neither with no relevant opportunity is NON_DISCRIMINATING, not success. Coerced bodily access alone does not satisfy voluntary social contact.
- **Outcome/adjudication:** UNOBSERVED. Rule revision ref NONE. No predictive credit yet.

### CM-PR-002 — first renewed request's mechanism

- **Rule/claim refs:** CM-CL-002/005; changed marital context from CM-INF-004.
- **Target:** Imagase's first consequential request for greater contact/relationship access in CM-U02, with the whole unit checked to identify it correctly.
- **Predicted range:** that first request will be presented as an invitation or through emotional/relational pressure rather than being enforced by threatened delivery of an infidelity report. This is a mechanism forecast, not a forecast of ethical improvement or success.
- **Falsifier/adjudication:** a report-disclosure threat enforcing that first request is FAILURE. Multiple simultaneous mechanisms including such a threat are MIXED. No new consequential request is NON_DISCRIMINATING. A broad range of emotional mechanisms limits this forecast's discriminating strength even if supported.
- **Outcome/adjudication:** UNOBSERVED. Rule revision ref NONE. No predictive credit yet.


## Revision events

The original v1 claim formulations above remain unchanged. Each event binds CM-U02-EXIT and witness `CM-JP-AIO2020-LOCAL`. Later current formulations below do not rewrite U01's frozen reading. Old source-state/limits remain retrievable by claim/version; these are source-based revisions rather than owner approval.

### CM-CR-001 — CM-CL-001, v1 → v2, REVISE

**Old:** U01-bounded responsive/evasive preference with active counterexamples. **New v2:** Across U01–U02, Otomo repeatedly prefers responsive accommodation and externalized explanations, yet can initiate forcefully when absence or perceived replaceability matters; this is a contextual pattern rather than absence of agency. **Reason/evidence:** active pursuit, assault, home invitation and intimate initiative materially extend the counterexamples (U02 O018–O033; sp0068–0083); ease/alibi/normalcy and passive life-page language preserve the candidate pattern. Primary route: [CM-U02-O027](../01%20Sequential%20Readings/CORNERED_MOUSE_U02_DEEP_READING.md#cm-u02-o027); `CM-JP-AIO2020-LOCAL::sp0077::xhtml=item/xhtml/p-0075.xhtml::image=item/image/i-0075.jpg::panel=P00`. **Counterevidence/alternative:** these acts may reflect situational jealousy/care/fear rather than a stable global disposition; confidence moderate. **Falsifier/limits:** missing or corrected agency/self-explanation evidence would revise it; no work/stranger portability claimed. **Downstream:** CM-CS-005/006, CM-RS-008–011, CM-DEC-007/009/011 updated; no existing monograph/model to backfill.

### CM-CR-002 — CM-CL-002 v1, PRESERVE

**Old/new:** the U01 hotel pressure and overridden limits remain as formulated. **Reason:** U02's initiative and changed stated standards are later states, not contemporaneous permission for U01. Primary route: [CM-U02-O006](../01%20Sequential%20Readings/CORNERED_MOUSE_U02_DEEP_READING.md#cm-u02-o006); `CM-JP-AIO2020-LOCAL::sp0056::xhtml=item/xhtml/p-0054.xhtml::image=item/image/i-0054.jpg::panel=P00`. U02 O004–O006/O029–O038 supplies new disputes; CM-CL-008 owns their present analysis rather than widening the old claim silently. **Confidence/falsifier:** original high-confidence mechanism and original attribution/agreement falsifier preserved. **Downstream:** CM-RS-001/CM-DEC-001 remain historical; current central records link CM-CL-008. No retrospective repair or deleted harm.

### CM-CR-003 — CM-CL-003 v1, PRESERVE

**Old/new:** Chikako's U01 direct account changes what is warranted about the divorce cause and preserves her independent critique. **Reason:** no new Chikako evidence appears in U02. Nishimura is another person; generalizing the wives/affair partners would be a scope error. **Evidence:** U01 references unchanged; U02 identity guard CM-CS-007/008 and O014–O016 distinguish the student woman. Primary new guard route: [CM-U02-O016](../01%20Sequential%20Readings/CORNERED_MOUSE_U02_DEEP_READING.md#cm-u02-o016); `CM-JP-AIO2020-LOCAL::sp0066::xhtml=item/xhtml/p-0064.xhtml::image=item/image/i-0064.jpg::panel=P00`. **Confidence/falsifier:** original qualified causal account and independent-delivery test unchanged. **Downstream:** CM-CS-003/CM-RS-005 no-new-evidence disposition; CM-CL-009 separately owns Nishimura. No new motive invented.

### CM-CR-004 — CM-CL-004, v1 → v2, STRENGTHEN

**Old:** interested psychological speech, incomplete prior knowledge and unequal phone access. **New v2:** Interpretive confidence must follow each actual access route: Imagase's partial predictive insight and represented suspicion are distinct from phone-derived knowledge; Otomo's apparent-rival inference is corrected by the client explanation. New represented interior settles some present perceptions, not earlier omniscience. **Evidence:** U02 O003,O014–O018,O025–O029, sp0053,0064–0068,0075–0079. Primary route: [CM-U02-O028](../01%20Sequential%20Readings/CORNERED_MOUSE_U02_DEEP_READING.md#cm-u02-o028); `CM-JP-AIO2020-LOCAL::sp0078::xhtml=item/xhtml/p-0076.xhtml::image=item/image/i-0076.jpg::panel=P00`. **Counterevidence/alternative:** Imagase's accurate reunion expectation supports genuine local insight; job details remain testimony. **Confidence:** high for access distinctions, qualified for whole motives/history. **Falsifier:** direct corroboration/corrected focal attribution can settle particular knowledge claims, not grant hindsight to past people. **Downstream:** CM-CS-005/006/009, CM-RS-008/009, CM-INF-009/010/011 updated. U01 kitchen asymmetry unchanged.

### CM-CR-005 — CM-CL-005, v1 → v2, REVISE

**Old:** U01 reopened contact with dating refused and terms unresolved. **New v2:** U02 develops active pursuit/intimacy and a voiced provisional-companionship offer; permanent couplehood, exclusivity, identity conversion and comprehensive boundary repair remain unestablished. **Evidence:** U02 O018–O040, sp0068–0090. Primary route: [CM-U02-O039](../01%20Sequential%20Readings/CORNERED_MOUSE_U02_DEEP_READING.md#cm-u02-o039); `CM-JP-AIO2020-LOCAL::sp0089::xhtml=item/xhtml/p-0087.xhtml::image=item/image/i-0087.jpg::panel=P00`. **Counterevidence/alternative:** tender proximity and initiative are real development; the offered withdrawal may be generous, defensive or strategic and is not yet tested. **Confidence:** high for action/offer, open for durable mutual terms. **Falsifier:** explicit agreement would establish that scoped term at its time; later new commitments do not rewrite U01's endpoint. **Downstream:** CM-CS-005/006, CM-RS-007–011, CM-INF-012, CM-DEC-010–012 updated; no premature relationship-finality claim.

### CM-CR-006 — CM-CL-006, v1 → v2, STRENGTHEN

**Old:** formal delay and unequal access shape provisional explanations. **New v2:** U01–U02 use temporally ambiguous cuts, later dream/context reveals, repeated absence imagery and corrected visual inferences to expose the limits of self-explanation; symbolic garden/fruit imagery remains mediated by Kyoichi's metaphor. **Evidence:** U02 O008–O016,O022–O028,O034–O040, sp0058–0066,0072–0078,0084–0090. Primary route: [CM-U02-O016](../01%20Sequential%20Readings/CORNERED_MOUSE_U02_DEEP_READING.md#cm-u02-o016); `CM-JP-AIO2020-LOCAL::sp0066::xhtml=item/xhtml/p-0064.xhtml::image=item/image/i-0064.jpg::panel=P00`. **Counterevidence/alternative:** decorative/pacing functions coexist; no single symbol code or biological species identification follows. **Confidence:** high for order/access, moderate for thematic function. **Falsifier:** corrected ordering/focal attribution could revise the mechanism. **Downstream:** U02 reading and future form/literary synthesis; no extra ledger warranted.

## Forecast adjudications at CM-U02-EXIT

Original CM-PR-001/002 text, timestamps, prior exposure and UNOBSERVED-at-creation fields above remain byte-for-byte unchanged. These appended events own their current outcomes. Both forecasts predate full U02 access and the declared U03 boundary-crop exposure; no prediction is fabricated for a within-U02 event.

| Event / original forecast | Outcome and exact evidence | Adjudication / practical limit |
|---|---|---|
| **CM-PA-001 / CM-PR-001** | Explicit not-dating claim sp0068 and resistance at sp0080 coexist with voluntary home invitation sp0079 and reengagement. [CM-U02-O029](../01%20Sequential%20Readings/CORNERED_MOUSE_U02_DEEP_READING.md#cm-u02-o029); `CM-JP-AIO2020-LOCAL::sp0079::xhtml=item/xhtml/p-0077.xhtml::image=item/image/i-0077.jpg::panel=P00` | **SUPPORTED** for the stated conjunction. Coerced bodily access alone is not counted as voluntary social contact. No general love/orientation/model-readiness result follows; rule revision NONE |
| **CM-PA-002 / CM-PR-002** | Earliest explicit renewed access demand sp0056 uses gendered/emotional pressure, with no report-disclosure enforcement. Earlier intrusive action sp0054–0055 was not a request. [CM-U02-O006](../01%20Sequential%20Readings/CORNERED_MOUSE_U02_DEEP_READING.md#cm-u02-o006); `CM-JP-AIO2020-LOCAL::sp0056::xhtml=item/xhtml/p-0054.xhtml::image=item/image/i-0054.jpg::panel=P00` | **SUPPORTED, LOW_DISCRIMINATION** under the original broad mechanism criterion. The unrequested action exposes a coverage limitation; later compensation pressure is not ethical improvement. No operational rule validation; rule revision NONE |

**U03 abstention:** no new forecast is issued. The source-boundary title probe exposed two captions about returning before one's senior/checking the PC. Repackaging that premise as a prediction would be retrospective. U03 remains unread in full; its actual role and consequences will be inspected after the U02 commit.

## U03 claim and revision events

### CM-CL-010 v1 — care, monitoring and self-restraint coexist

Created at CM-U03-EXIT; kind SUPPORTED_INTERPRETATION; witness `CM-JP-AIO2020-LOCAL`, temporal/disclosure scope this short. Primary route: [CM-U03-O003](../01%20Sequential%20Readings/CORNERED_MOUSE_U03_DEEP_READING.md#cm-u03-o003); `CM-JP-AIO2020-LOCAL::sp0094::xhtml=item/xhtml/p-0092.xhtml::image=item/image/i-0092.jpg::panel=P00`. **Formulation:** Imagase's represented interior joins domestic care, covert monitoring and an effort to regulate hope; the trace that prompts his hope does not establish Otomo's motive, and perceived moon-like distance is not mutual knowledge. **Evidence:** U03 O001–O004, sp0092–0095. **Counterevidence/alternative:** earlier actual withdrawals show capacity to leave; concern/self-protection can coexist with surveillance, which has no new shown permission. The query may express curiosity, concern, alarm or desire. **Confidence:** high for represented coexistence, moderate for its broader explanatory use, unknown for query motive/future promise. **Falsifier:** corrected focalization or direct Otomo explanation would revise the relevant inference; no single motive/diagnosis is claimed. **Unresolved:** enduring self-regulation and actual response to a terminating condition. **Downstream:** CM-CS-010/011, CM-RS-014, CM-INF-013, CM-DEC-014; future attachment/privacy work. No monograph/model promotion.

### CM-CR-007 — CM-CL-004, v2 → v3, STRENGTHEN

**Old v2:** actual access routes distinguish suspicion, phone knowledge and corrected rival inference. **New v3:** through U03, direct Imagase interior, visible digital trace and unverified Otomo motive remain distinct planes; a confident or emotionally plausible interpretation is not automatically shared knowledge. **Evidence:** U03 O001–O004, sp0092–0095. Primary route: [CM-U03-O002](../01%20Sequential%20Readings/CORNERED_MOUSE_U03_DEEP_READING.md#cm-u03-o002); `CM-JP-AIO2020-LOCAL::sp0093::xhtml=item/xhtml/p-0091.xhtml::image=item/image/i-0091.jpg::panel=P00`. **Counterevidence/alternative:** the query is strongly attributable to the PC owner, but no typing/motive scene independently establishes its purpose. **Confidence:** high for access distinctions, qualified for attribution, open for motive. **Falsifier:** direct explanation/corrected attribution can settle the specific gap without rewriting earlier knowledge. **Downstream:** CM-CS-010/011, CM-RS-014, CM-INF-013 updated; prior source records unchanged.

### CM-CR-008 — CM-CL-005 v2, PRESERVE

**Old/new:** U02 active intimacy and provisional offer leave permanence, exclusivity, identity conversion and full repair unestablished. **Reason:** U03's private hope makes the emotional cost of disappearance legible, but no qualifying future choice/request tests the promise. Primary route: [CM-U03-O004](../01%20Sequential%20Readings/CORNERED_MOUSE_U03_DEEP_READING.md#cm-u03-o004); `CM-JP-AIO2020-LOCAL::sp0095::xhtml=item/xhtml/p-0093.xhtml::image=item/image/i-0093.jpg::panel=P00`. O001–O004 supplies interior context, not an actual breach. **Counterevidence:** both earlier withdrawals were enacted; current self-restraint may support keeping a difficult promise. **Confidence/falsifier:** v2 limits and scoped agreement test retained. **Downstream:** CM-RS-014/CM-CS-011 add context; original offer in CM-INF-012/CM-RS-011 remains intact. CM-PR-003 is a new future test, not retroactive proof.

### CM-CR-009 — CM-CL-006, v2 → v3, STRENGTHEN

**Old v2:** temporal reveals, corrected inferences, absence imagery and mediated symbols shape understanding. **New v3:** U03's focal shift and imagined monitor scene grant access to one person's reasoning while marking the other's unknowability; repeated moon/apartment framing makes distance explicitly subjective. **Evidence:** U03 O001–O005, sp0092–0096. Primary route: [CM-U03-O001](../01%20Sequential%20Readings/CORNERED_MOUSE_U03_DEEP_READING.md#cm-u03-o001); `CM-JP-AIO2020-LOCAL::sp0092::xhtml=item/xhtml/p-0090.xhtml::image=item/image/i-0090.jpg::panel=P00`. **Counterevidence/alternative:** visual ornament/pacing coexist, and the closing illustration supplies no narrated agreement. **Confidence:** high for access/frame/explicit metaphor, moderate for thematic integration across units. **Falsifier:** corrected focal/order evidence could revise mechanism; no species/folklore or universal-symbol claim. **Downstream:** U03 reading, later form/integrated synthesis; no extra ledger.

**Other claims:** CM-CL-001 v2 retains its U01–U02 contextual formulation; the recalled chore is recorded with its uncertainty in CM-CS-010, not silently promoted to a new general trait. CM-CL-002/003/007/008/009 receive PRESERVE/no-new-adjudicative-evidence dispositions at U03: no new hotel consent, Chikako/Nishimura account, identity declaration or embodied permission negotiation is shown. Closing art is excluded from such claims. CM-PA-001/002 remain the only completed forecast outcomes.

## New prospective forecast at CM-U03-EXIT

### CM-PR-003 — response to an explicit female-choice withdrawal request

- **Rule/claim refs:** CM-CL-005 v2/010; literary forecast, no operational rule/model.
- **Recorded at:** `2026-10-30T05:22:26+00:00`; preoutcome freeze CM-U03-EXIT, bound by the complete U03 transaction commit before U04 narrative access.
- **Entering knowledge:** U01–U03 only, including two enacted withdrawals, the provisional disappearance offer and newly represented hope/self-restraint. Prior bibliography and the declared U04 frontispiece bands (most art/title, no scene/dialogue) are exposure; no blind benchmark claim.
- **Target/eligibility:** the first scene within CM-U04–CM-U06 in which Otomo explicitly chooses a woman for a romantic relationship and asks Imagase to end/withdraw their arrangement. A mere affair, presumed rival or analyst-inferred preference is not eligible. This observable declaration/request is a proxy; it cannot establish the subjective truth of destined/real love.
- **Predicted response:** Imagase will voice an objection to ending the arrangement or offer a modified way to remain, before any withdrawal. The test concerns an observable response and cost, not a guaranteed promise breach or ethical verdict.
- **Falsifier/scoring:** acceptance and departure/termination of the interaction without such objection/counteroffer is FAILURE, even if sadness is voiced. A voiced objection followed by eventual compliance supports the specified response but does not prove inability to honor departure. If the scene ends before a response, UNOBSERVED. If no eligible trigger occurs by U06 end, NON_DISCRIMINATING; do not substitute a later/cherry-picked case.
- **Confidence/counterevidence:** tentative, moderate-low. Persistent hope supports hesitation; actual prior withdrawals and present self-restraint favor compliance. No numerical probability or broad portability claim.
- **Outcome/adjudication:** UNOBSERVED. Rule revision ref NONE. No predictive credit yet.

## U04 new claims and revision events

All new claims/events bind `CM-JP-AIO2020-LOCAL`, disclosure and contemporary authority boundary CM-U04-EXIT. Former formulations remain unchanged above; listed spines resolve through U04's exact coverage table.

### CM-CL-011 v1 — Natsuki's critique has an independent history

**Kind:** SUPPORTED_INTERPRETATION of testimony/actions. **Formulation:** Natsuki's account distinguishes being treated kindly from feeling desired and shows the cost of Kyoichi's easy accommodation from a former partner's perspective; her current choices and affection prevent reduction to an interchangeable female alternative. Takasugi's parallel rejection request comes from another person with his own reunion wish, not an omniscient chorus. **Evidence:** U04 O005,O008–O011,O018–O026, sp0101,0104–0107,0114–0122. Primary route: [CM-U04-O021](../01%20Sequential%20Readings/CORNERED_MOUSE_U04_DEEP_READING.md#cm-u04-o021); `CM-JP-AIO2020-LOCAL::sp0117::xhtml=item/xhtml/p-0115.xhtml::image=item/image/i-0115.jpg::panel=P00`. **Counterevidence/alternative:** Natsuki's account may be selective, and Kyoichi's concern about unilateral sex is ethically meaningful; Takasugi wants the relationship himself. Her wish for a forced kiss is not general permission. **Confidence:** high for independent speech/choices, qualified for past relational explanation. **Falsifier:** source/identity correction or independent contradictory past evidence would revise the scoped account. **Unresolved/downstream:** present final understanding and future choice unknown; CM-CS-014/015, CM-RS-017/018, CM-INF-015, secondary/ethics synthesis.

### CM-CL-012 v1 — the repeated gift changes shared knowledge

**Kind:** SUPPORTED_INTERPRETATION. **Formulation:** Repeating the lighter transfer after Imagase explains its meaning makes Kyoichi's second offer knowingly particular care; the visual hand echo holds the old action steady while changing its available relational meaning. **Evidence:** U04 O019–O020,O028–O029,O039–O040, sp0115–0116,0124–0125,0135–0136. Primary route: [CM-U04-O039](../01%20Sequential%20Readings/CORNERED_MOUSE_U04_DEEP_READING.md#cm-u04-o039); `CM-JP-AIO2020-LOCAL::sp0135::xhtml=item/xhtml/p-0133.xhtml::image=item/image/i-0133.jpg::panel=P00`. **Counterevidence/alternative:** immediate hurt repair, kindness and desire may coexist; Imagase's old private motive is testimony. The gift is not an explicit romance/exclusivity contract. **Confidence:** high for repeated action/knowledge change, moderate for care interpretation. **Falsifier:** a source correction removing explanation-before-second-offer or showing a different object would defeat this precise mechanism. **Unresolved/downstream:** lasting effect/intent remain open; CM-CS-012/013, CM-RS-016, CM-INF-016, CM-DEC-021; form/relationship synthesis. No model readiness follows.

### CM-CR-010 — CM-CL-001, v2 → v3, STRENGTHEN

**Old v2:** U01–U02 responsive/evasive pattern with forceful initiative in particular contexts. **New v3:** Through U04, Kyoichi's agency remains contextual: externalized/ease accounts coexist with defended others, self-correction, a deliberate-avoidance account, a proposed ending, intimate initiative and knowingly particular giving. Literal passivity is increasingly untenable; no global autonomous transformation is established. **Evidence:** U04 O013,O016,O022,O028,O031,O034,O039, sp0109,0112,0118,0124,0127,0130,0135. Primary route: [CM-U04-O039](../01%20Sequential%20Readings/CORNERED_MOUSE_U04_DEEP_READING.md#cm-u04-o039); `CM-JP-AIO2020-LOCAL::sp0135::xhtml=item/xhtml/p-0133.xhtml::image=item/image/i-0133.jpg::panel=P00`. **Counterevidence/alternative:** intoxication, pressure, response to counsel and hurt repair limit assigning one self-directed motive. **Confidence:** moderate contextual pattern, high against total helplessness. **Falsifier:** corrected attributions or removal of recurring accommodation/initiative would revise scope; no work/stranger portability. **Downstream:** CM-CS-012, CM-RS-015–017, CM-DEC-015/019/021; later monograph/model assessment only.

### CM-CR-011 — CM-CL-004, v3 → v4, STRENGTHEN

**Old v3:** actual routes distinguish interior, trace and unknown motive. **New v4:** Through U04, public cover/private message, simultaneous conversation, interested memories, imagined former intimacy and selective asserted memory continue to produce unequal knowledge. Later responsiveness does not prove an earlier complaint was heard; morning jokes require act-specific correction. **Evidence:** U04 O006–O011,O014–O018,O027–O039, sp0102–0107,0110–0114,0123–0135. Primary route: [CM-U04-O038](../01%20Sequential%20Readings/CORNERED_MOUSE_U04_DEEP_READING.md#cm-u04-o038); `CM-JP-AIO2020-LOCAL::sp0134::xhtml=item/xhtml/p-0132.xhtml::image=item/image/i-0132.jpg::panel=P00`. **Counterevidence/alternative:** reliable local disclosures settle particular questions; epistemic caution must not deny visible action. **Confidence:** high for channels/order, qualified for whole histories/memory. **Falsifier:** direct corroboration or corrected attribution may settle each gap without granting past hindsight. **Downstream:** CM-CS-012–015, CM-RS-015–018, CM-INF-014–017; prior kitchen/PC gaps preserved.

### CM-CR-012 — CM-CL-005, v2 → v3, REVISE

**Old v2:** active intimacy/provisional offer with permanence, exclusivity and full repair unestablished. **New v3:** U04 adds an explicitly resisted general ending and a knowingly repeated gift, strengthening particular attachment and renewal without establishing permanent mutual terms. The disappearance promise remains untested under the chosen-woman condition. **Evidence:** U04 O031–O040, sp0127–0136. Primary route: [CM-U04-O031](../01%20Sequential%20Readings/CORNERED_MOUSE_U04_DEEP_READING.md#cm-u04-o031); `CM-JP-AIO2020-LOCAL::sp0127::xhtml=item/xhtml/p-0125.xhtml::image=item/image/i-0125.jpg::panel=P00`. **Counterevidence/alternative:** resistance to ending shows emotional cost but could coexist with later compliance with the narrower promise; earlier withdrawals are real. Gift may repair immediate hurt rather than declare romance. **Confidence:** high for objection/renewal, open for durable terms. **Falsifier:** a contemporaneous explicit shared agreement would establish that term at its own time; the forecast's exact trigger remains fixed. **Downstream:** CM-RS-016/CM-CS-012/013/CM-DEC-019–021, CM-PR-003 eligibility log. No retroactive promise-breach verdict.

### CM-CR-013 — CM-CL-006, v3 → v4, STRENGTHEN

**Old v3:** temporal/focal disclosure and subjective metaphors shape provisional interpretation. **New v4:** U04's explicitly transformed dream, interleaved table conversations, recalled hands and repeated gift stage differences among desire, available knowledge and acted meaning; semantic qualifications prevent visual/genre expectation from deciding the intimate act. **Evidence:** U04 O002–O004,O006–O011,O019,O029,O034–O040, sp0098–0100,0102–0107,0115,0125,0130–0136. Primary route: [CM-U04-O039](../01%20Sequential%20Readings/CORNERED_MOUSE_U04_DEEP_READING.md#cm-u04-o039); `CM-JP-AIO2020-LOCAL::sp0135::xhtml=item/xhtml/p-0133.xhtml::image=item/image/i-0133.jpg::panel=P00`. **Counterevidence/alternative:** echoes can also serve pacing/romance ornament; frontispiece and closing portrait do not add events. **Confidence:** high for order/repetition/qualifications, moderate for integrated thematic function. **Falsifier:** corrected source order or identity of repeated object would change the mechanism. **Downstream:** U04 argument, CM-INF-016/017 and future form/synthesis; existing four homes remain adequate.

### CM-CR-014 — CM-CL-007, v1 → v2, STRENGTHEN

**Old v1:** U02 normalcy language is self-explanation, distinct from fixed orientation and ethics. **New v2:** U04's female-Imagase dream and voiced not-gay/different-world claims show gendered self-conception in tension with desire for this particular man; neither dream nor embodied initiative settles a permanent identity. **Evidence:** U04 O002–O004,O011,O016,O028,O031–O034, sp0098–0100,0107,0112,0124,0127–0130. Primary route: [CM-U04-O002](../01%20Sequential%20Readings/CORNERED_MOUSE_U04_DEEP_READING.md#cm-u04-o002); `CM-JP-AIO2020-LOCAL::sp0098::xhtml=item/xhtml/p-0096.xhtml::image=item/image/i-0096.jpg::panel=P00`. **Counterevidence/alternative:** the dream can be wish, accommodation of known desire or conflicted fantasy; exclusive motive unknown. Harmful categorical speech and immediate apology remain actions, not identity proof. **Confidence:** high for tension, low for exhaustive identity determination. **Falsifier:** source correction or later direct self-definition changes current knowledge at its later boundary, not the earlier ambiguity. **Downstream:** CM-CS-012, CM-RS-015–017, sexuality/character synthesis.

### CM-CR-015 — CM-CL-008, v1 → v2, STRENGTHEN

**Old v1:** U02 participation changes while bilateral boundaries and withheld answers remain. **New v2:** Through U04, visible initiative and pleasure coexist with intimidation, intoxication, protest/wait and incomplete permission; Natsuki's forceful-kiss wish cannot license others' acts. The morning finger-only correction limits what the source certifies. **Evidence:** U04 O012–O017,O021,O031–O039, sp0108–0113,0117,0127–0135. Primary route: [CM-U04-O038](../01%20Sequential%20Readings/CORNERED_MOUSE_U04_DEEP_READING.md#cm-u04-o038); `CM-JP-AIO2020-LOCAL::sp0134::xhtml=item/xhtml/p-0132.xhtml::image=item/image/i-0132.jpg::panel=P00`. **Counterevidence/alternative:** Kyoichi's active kiss and Imagase's responsive contact are real; these support those acts without deciding every subsequent boundary. No total amnesia or total lack of desire is inferred. **Confidence:** high for explicit signals/correction, open for omitted agreements. **Falsifier:** contemporaneous act-specific agreement or attribution correction could revise a particular assessment; later affection cannot supply earlier permission. **Downstream:** CM-RS-015/016/017, CM-INF-017, CM-DEC-019/020, future ethics/intimacy synthesis. U01 mechanism remains unchanged.

**Other claims:** CM-CL-002 v1 (original hotel mechanism),003 v1 (Chikako),009 v1 (Nishimura) and010 v1 (U03 PC/care/self-restraint) receive PRESERVE at their existing scopes. No new source evidence settles the earlier investigation, women's aftermath or PC motive/privacy. U04 objections qualify future expectations through CM-CL-005 v3 rather than rewrite U03's represented reasoning. All original forecast/outcome formulations remain unchanged.

## CM-PR-003 eligibility checkpoint at U04 exit

**PENDING / no eligible trigger in fully inspected sp0097–sp0137.** The unnamed appointment and encounter with Natsuki do not establish a chosen romantic partner. Takasugi asks Kyoichi to reject Imagase; that is not Kyoichi choosing a woman. The different-world statement and sp0127 general stop suggestion do not state withdrawal in favor of a chosen woman. Imagase's actual objection at sp0128 is therefore retained as relational evidence without forecast credit. Primary route: [CM-U04-O031](../01%20Sequential%20Readings/CORNERED_MOUSE_U04_DEEP_READING.md#cm-u04-o031); `CM-JP-AIO2020-LOCAL::sp0127::xhtml=item/xhtml/p-0125.xhtml::image=item/image/i-0125.jpg::panel=P00`. Remaining window U05–U06; no trigger by U06 means NON_DISCRIMINATING under the original rule. CM-PA-001/002 remain the only completed outcomes. No new forecast or operational model is introduced at this exit.

## U05 claim and revisions

### CM-CL-013 v1 — a distancing plan produces immediate warmth

**Kind:** SUPPORTED_INTERPRETATION; created/disclosed CM-U05-EXIT, witness `CM-JP-AIO2020-LOCAL`. **Formulation:** Kyoichi deliberately tries consideration to make the relation burdensome; the compliment instead produces a warm response he recognizes as contrary to this aim. Initiative, private purpose and relational effect diverge. **Evidence:** U05 O001–O004, sp0138–0141. Primary route: [CM-U05-O004](../01%20Sequential%20Readings/CORNERED_MOUSE_U05_DEEP_READING.md#cm-u05-o004); `CM-JP-AIO2020-LOCAL::sp0141::xhtml=item/xhtml/p-0139.xhtml::image=item/image/i-0139.jpg::panel=P00`. **Counterevidence/alternative:** the result may be a temporary comic misfire, not lasting change; actual appreciation can coexist with instrumental motive. **Confidence:** high for stated aim/action/recognized immediate effect, open for durable attachment or unvoiced Imagase understanding. **Falsifier:** corrected sequence/attribution removing aim-before-compliment or the expressed contrary outcome would defeat this mechanism. **Downstream:** CM-CS-016/017, CM-RS-019, CM-INF-018/CM-DEC-022; later agency/form/relationship synthesis. No model readiness or final love follows.

### CM-CR-016 — CM-CL-001, v3 → v4, STRENGTHEN

**Old v3:** through U04, responsive/evasive accounts coexist with meaningful initiative. **New v4:** through U05, initiative can itself implement avoidance: Kyoichi plans a care experiment to escape drifting, then recognizes its immediate contrary effect. Agency is neither absent nor equivalent to settled purpose/ethical improvement. **Evidence:** U05 O002–O004, sp0139–0141. Primary route: [CM-U05-O003](../01%20Sequential%20Readings/CORNERED_MOUSE_U05_DEEP_READING.md#cm-u05-o003); `CM-JP-AIO2020-LOCAL::sp0140::xhtml=item/xhtml/p-0138.xhtml::image=item/image/i-0138.jpg::panel=P00`. **Counterevidence/alternative:** comic brevity limits stable/global generalization; U04's repeated gift need not share this specific motive. **Confidence:** high for this plan, moderate contextual pattern. **Falsifier/limits:** correction of represented motive or causal sequence revises the addition; no broad portability. **Downstream:** CM-CS-016, CM-RS-019, CM-DEC-022, CM-CL-013; earlier formulations preserved.

### CM-CR-017 — CM-CL-006, v4 → v5, STRENGTHEN

**Old v4:** dream/interleaving/repeated hands and semantic correction shape provisional meaning. **New v5:** U05 stages internal evaluation as black/white doubles, then Gray Kyoichi and paired warm framing undo the simple binary; apartment/danger echoes enclose a changed immediate predicament. **Evidence:** U05 O001–O004, sp0138–0141. Primary route: [CM-U05-O004](../01%20Sequential%20Readings/CORNERED_MOUSE_U05_DEEP_READING.md#cm-u05-o004); `CM-JP-AIO2020-LOCAL::sp0141::xhtml=item/xhtml/p-0139.xhtml::image=item/image/i-0139.jpg::panel=P00`. **Counterevidence/alternative:** comic ornament/pacing coexist; labels are no diagnosis or final moral classification. **Confidence:** high for visible labels/order/echo, moderate for thematic function. **Falsifier:** source attribution/order correction could revise mechanism. **Downstream:** U05 form argument, CM-INF-018/CM-CL-013 and future integration; no fifth ledger.

**Retained claims:** CM-CL-005 v3/007 v2 remain applicable without widening permanent-terms/identity conclusions. All other formulations retain their source scopes with no new adjudicative evidence: no new actual bodily act/permission, PC access/motive, former partners' aftermath or promise outcome appears. The hypothetical gender argument belongs to Kyoichi. U04 gift and U05 exit experiment have different stated knowledge/motive conditions.

## CM-PR-003 eligibility checkpoint at U05 exit

**PENDING / no eligible trigger through sp0142.** Private hypothetical preference for a woman is not a named/explicit chosen romantic relationship, and Kyoichi makes no withdrawal request in her favor. Primary route: [CM-U05-O003](../01%20Sequential%20Readings/CORNERED_MOUSE_U05_DEEP_READING.md#cm-u05-o003); `CM-JP-AIO2020-LOCAL::sp0140::xhtml=item/xhtml/p-0138.xhtml::image=item/image/i-0138.jpg::panel=P00`. U06 is the remaining window; the original NON_DISCRIMINATING disposition applies if no trigger occurs. No outcome/adjudication event or new forecast is invented. CM-PA-001/002 remain the two completed bounded literary outcomes.

## U06 new claims and revisions

All events bind `CM-JP-AIO2020-LOCAL`, disclosure/authority boundary CM-U06-EXIT. Earlier formulations, test wording and historical outcomes remain unchanged. Present conclusions retain actual access and temporal limits.

### CM-CL-014 v1 — enacted withdrawal has cost and does not guarantee permanence

**Kind:** SUPPORTED_INTERPRETATION. **Formulation:** Imagase can accept this explicit rejection and enact withdrawal despite attachment; Kyoichi's expectation of painless continued access is defeated. Later waiting/pain and renewed contact make neither the departure a mere bluff nor its permanence established. **Evidence:** U06 O018–O030,O040–O049, sp0160–0172,0182–0191. Primary route: [CM-U06-O029](../01%20Sequential%20Readings/CORNERED_MOUSE_U06_DEEP_READING.md#cm-u06-o029); `CM-JP-AIO2020-LOCAL::sp0171::xhtml=item/xhtml/p-0169.xhtml::image=item/image/i-0169.jpg::panel=P00`. **Counterevidence/alternative:** a separate final plea follows Kyoichi's recontact, and waiting continues by Imagase's report. This complicates effortless renunciation, not the observed loss of access. **Confidence:** high for acceptance/absence, qualified for whole private cost. **Falsifier:** corrected scene/order or evidence he remained with belongings/active contact would revise enacted withdrawal; no claim of permanent or painless disappearance. **Downstream:** CM-CS-018/019, CM-RS-022/024/025, CM-INF-021–024, CM-PA-003 and later relationship/agency arguments. No full destined-woman promise certification or model result.

### CM-CL-015 v1 — ordinary remains turn absence into shared knowledge

**Kind:** SUPPORTED_INTERPRETATION. **Formulation:** Missing black clothes and retained cigarette butts make absence legible to Kyoichi; delayed disposal and later admission let Imagase learn a particular investment he did not know. Replacing old remnants with current use registers reunion materially without a complete verbal contract. **Evidence:** U06 O005,O028–O030,O036,O042–O043,O058, sp0147,0170–0172,0178,0184–0185,0200. Primary route: [CM-U06-O042](../01%20Sequential%20Readings/CORNERED_MOUSE_U06_DEEP_READING.md#cm-u06-o042); `CM-JP-AIO2020-LOCAL::sp0184::xhtml=item/xhtml/p-0182.xhtml::image=item/image/i-0182.jpg::panel=P00`. **Counterevidence/alternative:** retention may combine grief, habit and avoidance; the precise disposal destination is unshown. It is not the same motive as the U04 gift or U05 experiment. **Confidence:** high for object/knowledge sequence, moderate for relational significance. **Falsifier:** corrected object identity/order or absent retention/admission would defeat the mechanism. **Downstream:** CM-CS-018/019, CM-RS-024/025, CM-INF-023/024, CM-DEC-029, form/relationship synthesis. No biological or magical symbol code.

### CM-CR-018 — CM-CL-001, v4 → v5, STRENGTHEN

**Old v4:** initiative may implement avoidance and produce contrary immediate results. **New v5:** through U06, Kyoichi repeatedly acts decisively at threatened access/loss, while self-explanations of drifting and delayed acknowledgment persist; rejection, retention, pursuit and conditional return are choices with different purposes. No global ethical/autonomy transformation follows. **Evidence:** U06 O018–O022,O024–O036,O038–O046, sp0160–0164,0166–0178,0180–0188. Primary route: [CM-U06-O039](../01%20Sequential%20Readings/CORNERED_MOUSE_U06_DEEP_READING.md#cm-u06-o039); `CM-JP-AIO2020-LOCAL::sp0181::xhtml=item/xhtml/p-0179.xhtml::image=item/image/i-0179.jpg::panel=P00`. **Counterevidence/alternative:** care, fear, jealousy and dependency can overlap; social pressure and limited choices differ by scene. **Confidence:** moderate contextual pattern, high against literal helplessness. **Falsifier/limits:** corrected motive/action or missing recurring contrast revises scope; no professional/stranger portability. **Downstream:** CM-CS-018, CM-RS-022–025, CM-DEC-025/027/029/031/033; earlier choices preserved.

### CM-CR-019 — CM-CL-004, v4 → v5, STRENGTHEN

**Old v4:** public/private channels, interested histories, imagined acts and selective memory produce unequal knowledge. **New v5:** U06 adds concealed proposal, reader-only rival meeting, corrected emergency, material departure, asymmetric noncontact accounts and a one-sided phone call. Each new disclosure settles only its own question; Kyoichi's new-target assumption is not proved fact. **Evidence:** U06 O002–O019,O023–O044,O047, sp0144–0161,0165–0186,0189. Primary route: [CM-U06-O044](../01%20Sequential%20Readings/CORNERED_MOUSE_U06_DEEP_READING.md#cm-u06-o044); `CM-JP-AIO2020-LOCAL::sp0186::xhtml=item/xhtml/p-0184.xhtml::image=item/image/i-0184.jpg::panel=P00`. **Counterevidence/alternative:** direct admission and converging absence cues warrant some strong conclusions; caution cannot erase actual departure. **Confidence:** high for access/order, qualified for private histories/costs. **Falsifier:** direct corroboration or attribution correction settles a scoped gap without past hindsight. **Downstream:** CM-CS-018–020, CM-RS-020–025, CM-INF-019–025; earlier kitchen/PC/memory histories unchanged.

### CM-CR-020 — CM-CL-005, v3 → v4, REVISE

**Old v3:** resisted general ending and knowing gift renew attachment while future disappearance remains untested. **New v4:** U06 enacts contextual choice, initial acceptance and actual withdrawal, then chosen pursuit, a fidelity-like demand and expanded intimacy under acknowledged fear. Particular attachment/sexual access advance; permanent mutual terms, comprehensive repair and Natsuki resolution remain unestablished. **Evidence:** U06 O014–O030,O037–O060, sp0156–0172,0179–0202. Primary route: [CM-U06-O049](../01%20Sequential%20Readings/CORNERED_MOUSE_U06_DEEP_READING.md#cm-u06-o049); `CM-JP-AIO2020-LOCAL::sp0191::xhtml=item/xhtml/p-0189.xhtml::image=item/image/i-0189.jpg::panel=P00`. **Counterevidence/alternative:** the later final plea/waiting reveal cost, but cannot erase the first acceptance/absence; reunion does not prove the earlier departure insincere. **Confidence:** high for transitions, open for durable terms. **Falsifier:** explicit mutual agreements settle particular terms at their time; future events cannot rewrite this boundary. **Downstream:** CM-RS-022–025, CM-CS-018/019, CM-DEC-025–033, CM-PA-003/CM-CL-014. Downgrade the expectation of necessary initial objection; no operational rule existed to revise.

### CM-CR-021 — CM-CL-006, v5 → v6, STRENGTHEN

**Old v5:** internal doubles/gray outcome and prior dream/interleaving/repetition shape meaning. **New v6:** U06 uses forced public choice, absent-person confession, empty domestic frames, an explicit two-month gap, material echoes and a one-sided call to separate appearance, knowledge and motive; rain/drowning closes with a question rather than resolved judgment. **Evidence:** U06 O018–O036,O042–O060, sp0160–0178,0184–0202. Primary route: [CM-U06-O060](../01%20Sequential%20Readings/CORNERED_MOUSE_U06_DEEP_READING.md#cm-u06-o060); `CM-JP-AIO2020-LOCAL::sp0202::xhtml=item/xhtml/p-0200.xhtml::image=item/image/i-0200.jpg::panel=P00`. **Counterevidence/alternative:** objects/rain also serve pacing/atmosphere; no uniquely fixed allegory or literal drowning. **Confidence:** high for order/echo/question, moderate for thematic integration. **Falsifier:** corrected ordering/focalization/object identity revises mechanism. **Downstream:** U06/form synthesis, CM-INF-023–025/CM-CL-015. Adjacent art203/204 supplies no narrative agreement; four homes remain adequate pending review.

### CM-CR-022 — CM-CL-007, v2 → v3, REVISE

**Old v2:** gendered self-conception conflicts with particular desire; dream/action do not settle identity. **New v3:** U06 explicitly connects ordinary-man choice and ordinary-couple relief to Kyoichi's fear of entering an unfamiliar world with only Imagase and being abandoned. Renewed active desire/penetrative sex changes conduct without a final identity declaration or an automatic moral endorsement. **Evidence:** U06 O018–O022,O037–O060, sp0160–0164,0179–0202. Primary route: [CM-U06-O022](../01%20Sequential%20Readings/CORNERED_MOUSE_U06_DEEP_READING.md#cm-u06-o022); `CM-JP-AIO2020-LOCAL::sp0164::xhtml=item/xhtml/p-0162.xhtml::image=item/image/i-0162.jpg::panel=P00`. **Counterevidence/alternative:** self-account may be partial; dependence, shame, social safety and desire overlap differently. Imagase's actual future conduct is not known from Kyoichi's fear. **Confidence:** high for voiced fear/tension, open for exhaustive motives/permanent label. **Falsifier:** later self-definition revises current knowledge at its own boundary, not this earlier uncertainty. **Downstream:** CM-CS-018, CM-RS-022/023/025, sexuality/character integration.

### CM-CR-023 — CM-CL-008, v2 → v3, STRENGTHEN

**Old v2:** initiative/intoxication/bilateral limits and finger-only correction qualify participation. **New v3:** U06 preserves an actual early refusal/interruption, distinguishes caring bath contact and ambiguous request-answer from certified sex, then records a later condition, active return and sustained penetrative encounter. Change in participation cannot retroactively authorize prior acts; shared fear/intensity is not complete permission/repair. **Evidence:** U06 O004–O008,O023–O027,O046–O060, sp0146–0150,0165–0169,0188–0202. Primary route: [CM-U06-O026](../01%20Sequential%20Readings/CORNERED_MOUSE_U06_DEEP_READING.md#cm-u06-o026); `CM-JP-AIO2020-LOCAL::sp0168::xhtml=item/xhtml/p-0166.xhtml::image=item/image/i-0166.jpg::panel=P00`. **Counterevidence/alternative:** present pursuit, condition and response are real agency/desire; lack of a full negotiation transcript does not prove every act unwanted. **Confidence:** high for distinctions/refusals, qualified for unshown agreements. **Falsifier:** contemporaneous act-specific agreement/corrected attribution revises a scoped assessment; later affection never supplies it retroactively. **Downstream:** CM-RS-020/024/025, CM-INF-022/025, CM-DEC-025/027/033; old U01/U02/U04 evidence intact.

### CM-CR-024 — CM-CL-011, v1 → v2, STRENGTHEN

**Old v1:** Natsuki's independent critique/history and Takasugi's own reunion stake are not an omniscient chorus. **New v2:** U06 gives Natsuki independent refusal, proposal/choice pressure, conditional tolerance of a prepared male relationship, criticism of being a substitute listener and tangible holiday care. Her demeaning rivalry language and unresolved final call also remain. Takasugi's U04 scope is unchanged; no new evidence for him. **Evidence:** U06 O002–O003,O009–O022,O031–O035,O037,O058–O060, sp0144–0145,0151–0164,0173–0177,0179,0200–0202. Primary route: [CM-U06-O034](../01%20Sequential%20Readings/CORNERED_MOUSE_U06_DEEP_READING.md#cm-u06-o034); `CM-JP-AIO2020-LOCAL::sp0176::xhtml=item/xhtml/p-0174.xhtml::image=item/image/i-0174.jpg::panel=P00`. **Counterevidence/alternative:** love, competitive hurt and gendered norms overlap; no uniquely certified private motive. **Confidence:** high for agency/words, qualified for whole history/aftermath. **Falsifier:** source/identity correction or later independent account changes scoped interpretation. **Downstream:** CM-CS-020, CM-RS-021/023, CM-DEC-023/030, secondary/ethics synthesis.

**Retained claims:** CM-CL-002 v1 (U01 hotel),003 v1 (Chikako),009 v1 (Nishimura),010 v1 (U03 care/PC),012 v1 (U04 knowing gift) and013 v1 (U05 care experiment) remain at their source scopes. New objects/choices do not rewrite their distinct motives or introduce former partners' unshown aftermath. No global grade or model is created.

## Forecast adjudication at CM-U06-EXIT

### CM-PA-003 — CM-PR-003, FAILURE with eligibility bound

**Frozen basis:** original CM-PR-003 recorded `2026-10-30T05:22:26+00:00`, bound by U03 transaction `0d96bb987da131e4846c2612bace00c8e9a52a1f` before U04/U06 narrative access. Its target and falsifier remain unchanged. **First contextual eligible scene:** sp0160–0161, within U04–U06 window. Direct cannot-choose-you to Imagase operates inside the shared binary romantic choice/unchosen-withdraws frame, followed by Kyoichi leaving with Natsuki. This is explicit contextual selection/rejection, not an inferred private preference or a presumed affair. It does not prove real/fated love. Primary route: [CM-U06-O019](../01%20Sequential%20Readings/CORNERED_MOUSE_U06_DEEP_READING.md#cm-u06-o019); `CM-JP-AIO2020-LOCAL::sp0161::xhtml=item/xhtml/p-0159.xhtml::image=item/image/i-0159.jpg::panel=P00`.

**Observed response/scoring:** Imagase says yes/knows his place, with no voiced objection/counteroffer before the café interaction terminates. The originally specified first response is therefore FAILURE. Later final request sp0168 follows a separate terminated café interaction and Kyoichi-initiated recontact, so it cannot be substituted to rescue the forecast. Actual disappearance cues sp0170–0172 and later pain/waiting accounts qualify cost and permanence separately.

**Eligibility limitation:** demanding a standalone positive declaration I choose Natsuki would exclude this negative-form contextual selection; that stricter reading yields NON_DISCRIMINATING if no later eligible trigger, never support. The primary adjudication follows the declared observable choice frame rather than adding a new exact-phrase requirement. The scene remains adverse counterevidence on either reading. **Confidence/limits:** high for response/interaction end, contextual eligibility explicitly bounded. No universal compliance, painless exit, complete promise-keeping or permanent separation claim. **Propagation:** CM-CL-005 v4/CM-CR-020 and CM-CL-014, CM-RS-022/024/025 and CM-CS-018/019 preserve actual transition; necessary-initial-objection expectation downgraded. Operational rule revision NONE; no model existed. Original UNOBSERVED-at-creation field remains historical, and CM-PA-001/002 outcomes/weak-discrimination limits remain untouched.

| Forecast | Current completed outcome | Exact outcome home / limit |
|---|---|---|
| CM-PR-001 | SUPPORTED | CM-PA-001 at U02; bounded contact/classification test |
| CM-PR-002 | SUPPORTED, LOW_DISCRIMINATION | CM-PA-002 at U02; earliest request test omitted prior unrequested act |
| CM-PR-003 | FAILURE, contextual eligibility bounded | CM-PA-003 at U06; first café response, no later-scene rescue |

These three literary tests are not a sampled accuracy metric or operational-model validation. No new forecast is created from already read U06 outcomes.

## Prospective model tests frozen before CM-U07

**Freeze recorded 2026-10-30T22:09:38.037437+00:00; evidence basis `e4749dea42179e01a417a96171e9cfb035ca919b`, CM-U06-EXIT.** These records and the linked model versions commit before any U07 title probe/image. Prior exposure is the six completed readings, contents/bibliography and colophon; sequel narrative remains uninspected. One canonical prediction register lives here. Later outcome records append separately and never replace the UNOBSERVED-at-creation fields. The [title-work review](../07%20Audits%20and%20Handoffs/CORNERED_MOUSE_TITLE_WORK_ARCHITECTURE_AND_READINESS_REVIEW.md) binds the exact evidence/dimensions/gaps.

### CM-TEST-U06-V1 — common selection and scoring protocol

Window CM-U07–CM-U10, collection disclosure order; CM-S01 is excluded. For each test select the **first eligible complete encounter**, not the best confirming scene. Record candidate triggers and exclusions in each unit closeout, even when no trigger qualifies. Log eligibility from information available at the trigger before using later outcomes where page disclosure permits. A response on the same page is inseparable source exposure; declare that fact rather than pretend a blind within-page eligibility judgment. The forecast remains prospective because its wording was committed before the image.

Trigger information itself is allowed: apparent rival, voluntary offer or disagreement as respectively defined below. Discomfort, anger or a surprising/failing response alone never becomes a state mismatch. Prior explicit abandonment of the attachment, a new exclusive commitment, substantial intervening history/new constraint or changed knowledge that defeats a stated precondition produces a documented TEMPORAL_CONTEXT_MISMATCH/abstention. Specify the new fact and its pre-response locator; do not invent mismatch after seeing failure. No silent model update. A materially changed state can be tested only as an explicitly labeled transfer challenge, not clean validation of U06 state.

Score SUPPORTED only for the entire original response range, FAILURE for its stated counteroutcome, MIXED for partial/contradictory visible response or genuinely ambiguous eligibility, and UNOBSERVED if an eligible interaction's outcome is not supplied. No eligible trigger by U10 yields NON_DISCRIMINATING, or WINDOW_CONFOUNDED if all opportunities were precluded by documented state/context mismatch. Those are not successful predictions. A reported past response is retrospective evidence, not the next depicted encounter. Synthetic/adversarial prompts are noncanonical consistency checks. No sampled accuracy, independent rater agreement or global assessment is claimed.

### CM-PR-004 — Kyoichi initiates at an eligible rival encounter

- **Rule/state:** [CM-RULE-OTOMO-001@v1](../04%20Character%20Studies/CORNERED_MOUSE_OTOMO_U06_PROPOSED_MODEL.md), CM-CH-OTOMO at U06 exit; test protocol CM-TEST-U06-V1.
- **Target:** first unexpected direct encounter after perceived loss/rupture with Imagase and an apparent competing male attachment, where Kyoichi can address him. Exclude an imposed public woman/man choice, incapacity, restraint, emergency or actual danger. Mere discussion without encounter is ineligible.
- **Predicted range:** Kyoichi initiates a personal interaction with Imagase before that encounter terminates; not silent departure/nonaddress. Exact speech, violence, motive, sex and reunion are unpredicted.
- **Falsifier:** the eligible encounter ends with an available opportunity and no such initiation. Alternatives/mismatch/no-trigger score under the common protocol. Only two training episodes fit closely; a supported result remains narrow.
- **Outcome at creation:** UNOBSERVED; no outcome or rule revision yet.

### CM-PR-005 — Imagase responds to a voluntary personal reopening

- **Rule/state:** [CM-RULE-IMAGASE-001@v1](../04%20Character%20Studies/CORNERED_MOUSE_IMAGASE_U06_PROPOSED_MODEL.md), CM-CH-IMAGASE at U06 exit; CM-TEST-U06-V1.
- **Target:** first sober, uncoerced personal invitation or clear meaningful affectionate gesture from Kyoichi after rupture/ending-like exchange. Kyoichi must direct personal access to Imagase, rather than offer instrumental work contact, emergency rescue or an ambiguous accident. Both have the physical opportunity to respond.
- **Predicted range:** Imagase accepts or actively negotiates that offered personal access before the interaction ends, rather than unequivocally refusing and terminating. No automatic forgiveness, permission for further acts or durable reconciliation predicted.
- **Falsifier:** unequivocal refusal followed by termination without negotiation. Changed commitments/knowledge, impairment, coercion or emergency invoke declared exclusions with locators, never post hoc rescue.
- **Outcome at creation:** UNOBSERVED; no outcome or rule revision yet.

### CM-PR-006 — written politeness during direct disagreement

- **Rule/state:** [CM-RULE-IMAGASE-002@v1](../04%20Character%20Studies/CORNERED_MOUSE_IMAGASE_U06_PROPOSED_MODEL.md), same state/protocol. Written-register test only.
- **Target:** first complete sober direct disagreement/pressure exchange addressed by Imagase to Kyoichi with their familiar relationship/hierarchy intact; exclude quotation/dream, emergency, impaired speech, untranslated wording or an unestablished recipient. Anger alone does not exclude it.
- **Predicted range:** the exchange contains at least one senior-address or polite-form segment while expressing disagreement; exact line/voice, every-sentence politeness and ethical respect unpredicted.
- **Falsifier:** the complete eligible exchange contains neither senior address nor polite-form language. A supported outcome is inherently low discrimination because hierarchy/habit can explain the same surface; it cannot validate motive/action fidelity.
- **Outcome at creation:** UNOBSERVED; no outcome or rule revision yet.

The three earlier literary forecasts and CM-PA-001–003 retain their original results and limits. New models do not retroactively claim those as validation. Current forecast totals: six registered, three adjudicated and three pending.

## Current claim projection

| Claim | Current formulation | Authority boundary / disposition |
|---|---|---|
| CM-CL-001 | v5 in CM-CR-018 | Choice/retention/pursuit coexist with drift accounts; STRENGTHEN |
| CM-CL-002 | v1 above | U01 hotel mechanism preserved by CM-CR-002 |
| CM-CL-003 | v1 above | Chikako account preserved by CM-CR-003; no U02 new evidence |
| CM-CL-004 | v5 in CM-CR-019 | Private meetings, corrected fear, absence and one-sided call; STRENGTHEN |
| CM-CL-005 | v4 in CM-CR-020 | Enacted withdrawal and conditional reunion; unresolved mutual/other terms; REVISE |
| CM-CL-006 | v6 in CM-CR-021 | Domestic traces, delayed recognition and open rain/drowning end; STRENGTHEN |
| CM-CL-007 | v3 in CM-CR-022 | Voiced dependence/abandonment fear and particular desire; identity open; REVISE |
| CM-CL-008 | v3 in CM-CR-023 | Early refusal, distinct request gap and later expanded participation; STRENGTHEN |
| CM-CL-009 | v1 above | Nishimura's independent agency/qualified family account |
| CM-CL-010 | v1 above | U03 care/monitoring/self-restrained hope; motives bounded |
| CM-CL-011 | v2 in CM-CR-024 | Natsuki’s independent choices/care/critique and outstanding claim; STRENGTHEN |
| CM-CL-012 | v1 above | Repeated gift after explanation changes shared meaning |
| CM-CL-013 | v1 above | Care as exit experiment yields an immediately warm response |
| CM-CL-014 | v1 above | Withdrawal is enacted and costly; permanence not certified |
| CM-CL-015 | v1 above | Ordinary traces make absence and retained investment legible |
