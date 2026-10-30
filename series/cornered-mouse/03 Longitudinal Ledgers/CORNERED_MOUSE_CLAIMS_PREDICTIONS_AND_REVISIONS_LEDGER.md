---
title: "Cornered Mouse — Claims, Predictions and Revisions Ledger"
artifact_id: CORNERED_MOUSE_CLAIMS_PREDICTIONS_AND_REVISIONS_LEDGER
artifact_type: claim_revision_ledger
series: "The Cornered Mouse Dreams of Cheese / 窮鼠はチーズの夢を見る"
series_id: cornered-mouse
generation: CORNERED_MOUSE_BOOTSTRAP_V1
version: "0.4"
status: active_provisional
scope: "Interpretive claim lineage, genuine prospective forecasts and revision impact"
source_boundary: "Japanese manga continuity; CM-JP-AIO2020-LOCAL admitted through CM-U02; story ends sp0090, closing illustration sp0091 separately classified"
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

**Claims: 9. Predictions: 2 (both adjudicated). Claim revision events: 6. Forecast adjudication events: 2. Source boundary: CM-U02.** U01 formulations and original forecast bytes remain unchanged; the current projection and appended U02 events identify later authority. Follow the [method](../00%20Frameworks%20and%20Methods/CORNERED_MOUSE_ANALYTICAL_METHOD.md) and [architecture](../00%20Frameworks%20and%20Methods/CORNERED_MOUSE_SYNTHESIS_ARCHITECTURE.md).

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

## Current claim projection

| Claim | Current formulation | Authority boundary / disposition |
|---|---|---|
| CM-CL-001 | v2 in CM-CR-001 | U01–U02 contextual agency; REVISE |
| CM-CL-002 | v1 above | U01 hotel mechanism preserved by CM-CR-002 |
| CM-CL-003 | v1 above | Chikako account preserved by CM-CR-003; no U02 new evidence |
| CM-CL-004 | v2 in CM-CR-004 | Actual access routes; STRENGTHEN |
| CM-CL-005 | v2 in CM-CR-005 | Active intimacy/provisional offer; REVISE |
| CM-CL-006 | v2 in CM-CR-006 | Temporal/access/form evidence; STRENGTHEN |
| CM-CL-007 | v1 above | U02 normalcy/self-explanation, identity open |
| CM-CL-008 | v1 above | U02 changing participation and bilateral permission limits |
| CM-CL-009 | v1 above | Nishimura's independent agency/qualified family account |
