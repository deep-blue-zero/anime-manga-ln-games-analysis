---
title: "Three Days of Happiness — Cumulative state, claim history and readiness"
artifact_id: TDH_TDH_LONGITUDINAL_NOTEBOOK
artifact_type: longitudinal_state_and_claim_notebook
series: three-days-of-happiness
version: "1.1"
generation: INITIAL_BOOTSTRAP
status: canonical
scope: "Cumulative state, claim history and readiness"
authority_scope: cumulative_retrieval_layer_for_TDH-RUN-20261116-U01-U15
source_boundary: "TDH-JP-01 through the latest accepted unit recorded in Transaction and history"
last_updated: 2026-11-17
canonical_home: series/three-days-of-happiness/TDH_LONGITUDINAL_NOTEBOOK.md
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
---

# Three Days of Happiness — longitudinal notebook

This notebook provides distinct cumulative homes appropriate to one novel. It holds source-linked retrieval records; full reasoning stays in full readings and later studies. No narrative has been read, so all analytical record sections begin at **zero observations**. The schema definitions below are operational contracts, not observations or fictional examples.

## State

**Row unit:** one change or bounded stability claim about a named actor, directional relation, knowledge item, contextual constraint or narrative frame. Fields: `state_id`, `kind`, named subject(s), directional target where applicable, entering state ID, exiting formulation, source disclosure frontier, depicted-time interval/uncertainty, continuity/frame, speaker/focalizer, evidence class, exact locators, reading heading, causal account, counterevidence, confidence limits and validity end/successor.

For knowledge rows include `knower`, `proposition`, `knows/believes/suspects/misunderstands/unknown`, acquisition route and distinction from reader knowledge. For character rows distinguish action, self-report, inferred motive, ordinary behavior, stress and performance. For relationships identify A→B separately from B→A; unsupported reciprocity remains unknown. Context rows concern the work's represented constraints, not analyst biography or presumed themes.

**Update trigger:** a completed reading exposes a change, a diagnostic stability case or a material counterexample. Append transitions; never rewrite a prior time slice. If no supported change occurred, record that in the unit transaction without fabricating empty character rows. Claims about absence need a defined opportunity and inspected range. A current-state pointer may be updated only after preserving the prior row and linking the transition.

At bootstrap (2026-11-07) there were no state rows and no named subjects. Rows below are appended per accepted unit. Compact columns: `state_id` | kind | subject → target | entering | exiting formulation | frontier / depicted time | voice and evidence class | locators | reading heading | counterevidence and limits | successor.

| state_id | Kind | Subject → target | Entering | Exiting formulation | Frontier / depicted time | Voice; class | Locators (Ch01 unless noted) | Reading | Counterevidence, limits | Successor |
|---|---|---|---|---|---|---|---|---|---|---|
| TDH-S001 | character | Narrator (俺, unnamed) | — | As a boy he thought himself exceptional; the narrating self calls this 勘違い and admits arrogance but keeps contempt for classmates (P0035 present assertion). Habitual hedging and did-not→could-not self-correction | U01 / age 10, narrated at ~20 | Narrator self-report; OBS + INF | P0023, P0028, P0035–P0036, P0053–P0054 | [U01 §5, §7](readings/TDH_U01_DEEP_READING.md#5-narration-focalization-and-time) | P0030, P0049 voice-undecidable; self-deprecation may be a pose (P0031 irony) | — |
| TDH-S002 | character | Narrator | — | Values at ten: authenticity (cannot laugh along without "scraping" his core), contempt for false modesty, global dislike of "everything that happens" (P0082); preference for a short intense life (P0020, voice OPEN). Laughs with Himeno, not with the group | U01 / age 10 | Narrated + direct speech; OBS + INF | P0020, P0031, P0053, P0074, P0082, P0092–P0093 | [U01 §7, §9](readings/TDH_U01_DEEP_READING.md#7-characters) | Laughter limitation is group-specific; misanthropy has an exception (Himeno) | — |
| TDH-S003 | character | Himeno (ヒメノ; katakana; surname/given unknown) | — | At ten: equal top scorer; polite public answerer, cutting in private; main initiator of the shrine dialogue (prophecy, horizon, summer, proposal); values rank, wealth, envy, repayment; ようやく implies not glad to be alive (INF) | U01 / age 10 | Narrated through narrator; direct speech; OBS + INF | P0009, P0037–P0038, P0047, P0062–P0092 | [U01 §7](readings/TDH_U01_DEEP_READING.md#7-characters) | All interiority via narrator; whether she believed the prophecy or meant the proposal unknown | — |
| TDH-S004 | relationship | Narrator → Himeno | — | Rival; his only interlocutor (stated as fact); source of authoritative frames (P0075); kept her retracted proposal as a "promise" ~10 years and refused romantic interest at each school stage to show he stayed "unsold"; affection never named | U01 / age 10 → ~20 | Narrator self-report; OBS + INF | P0039–P0041, P0075, P0086, P0094–P0096 | [U01 §8](readings/TDH_U01_DEEP_READING.md#8-directional-relationships-at-u01-exit) | Abstention rivals: misanthropy, social incapacity (TDH-C003); "foolish" self-mockery | — |
| TDH-S005 | relationship | Himeno → narrator (as narrated) | — | Rival; mutual intelligibility only "probably"; includes him in every future (私たち); proposes conditionally, then retracts as a joke; attitude after separation unknown | U01 / age 10 | Narrator inference + her speech; OBS + INF | P0040, P0063–P0092 | [U01 §8](readings/TDH_U01_DEEP_READING.md#8-directional-relationships-at-u01-exit) | Narrator's P0090 claim of contemporaneous insight uncorroborated | — |
| TDH-S006 | knowledge | Lifespan sale | — | Narrating self knows he sold lifespan for payment at twenty; reader knows the fact only; price, quantity, buyer, mechanism, motive unknown; the boy and Himeno knew only the teacher's hypothetical parable | U01 / sale at 20 | Narrator prolepsis; OBS | P0004, P0016–P0021, P0032 | [U01 §10](readings/TDH_U01_DEEP_READING.md#10-epistemic-and-temporal-state) | Per-year/partial terms inferred from the parable, not stated (TDH-C002) | — |
| TDH-S007 | knowledge | Status of the proposal | — | Himeno: retracted as joke. Narrator: construes as 約束 and keeps it. Himeno's knowledge of his fidelity: unknown. Nobody accepted | U01 / age 10 → ~20 | Speech + narrator construal; OBS | P0089–P0095 | [U01 §4](readings/TDH_U01_DEEP_READING.md#4-factual-and-causal-reconstruction) | Title's 約束 may also name the prophecy | — |
| TDH-S008 | frame | Narrative time | — | Three layers: narrating instance after the sale; the unplaced "hearing" (P0004); childhood at ten. Closing present ~20 unfixed relative to the sale. Separation after ten, unplaced (before/during middle school, low confidence) | U01 | Narrator; OBS + INF | P0004, P0032, P0094, P0097–P0098 | [U01 §5](readings/TDH_U01_DEEP_READING.md#5-narration-focalization-and-time) | — | — |

## Claims and questions

**Row unit:** one explicitly bounded claim version or prospective question. Fields: `claim_id`, version, formulation, `OBSERVATION/INFERENCE/HYPOTHESIS/VALUE_JUDGMENT`, asserting voice, source horizon, scope/state IDs, supporting locators, complete argument's reading/study heading, counterevidence, credible alternative, discriminating/falsifying condition, uncertainty, `PRESERVE/STRENGTHEN/REVISE/DOWNGRADE/REJECT/OPEN`, predecessor, reason, revision boundary and dependent artifacts.

**Update trigger:** proposal, retest or change of any load-bearing interpretation; later evidence against a prior prediction; or source correction affecting the assertion. Preserve all formulations and reasons. A prediction is timestamped to the source frontier before later material is read; adjudicate it later with the actual evidence and exposure limit. Do not retroactively improve the original prediction. Distinguish what later became false from what was reasonable at the earlier boundary.

At bootstrap there were no claim or question rows. Source admission questions remain in the source register; they are not literary hypotheses. Rows below are appended per accepted unit; a later transition appends a new version row and never edits the earlier one.

| claim_id | Ver | Formulation | Class | Voice | Horizon | Locators | Reading | Counterevidence / alternative; discriminating condition | Status | Predecessor / reason |
|---|---|---|---|---|---|---|---|---|---|---|
| TDH-C001 | 1 | The narrator sold some lifespan for payment at twenty, disclosed early with no price, quantity, buyer, mechanism or motive | OBSERVATION | Narrator | U01 | Ch01 P0032 | [U01 §11](readings/TDH_U01_DEEP_READING.md#11-competing-interpretations-claims-and-forecasts) | — | OPEN (new) | — |
| TDH-C002 | 1 | The narrator offers the teacher's parable (buyer; price per year of remaining life; partial sale) as the template for his sale via 正解らしきもの; that the real sale follows its per-year pricing and partial scope is likely but unstated | INFERENCE | Analyst | U01 | Ch01 P0016–P0021, P0032 | [U01 §4.2](readings/TDH_U01_DEEP_READING.md#4-factual-and-causal-reconstruction) | Discriminator: disclosure of the real sale's terms | OPEN (new) | Reformulated before registration per D-U01-02 |
| TDH-C003 | 1 | His refusals of romantic interest (middle school–university) are self-attributed to Himeno's proposal; the attribution is his alone | INFERENCE | Analyst on narrator self-report | U01 | Ch01 P0053, P0080–P0082, P0094–P0096 | [U01 §4.8](readings/TDH_U01_DEEP_READING.md#4-factual-and-causal-reconstruction) | Rivals: misanthropy (P0082); incapacity for conformist performance (P0053); display motive (P0095). Discriminator: independent evidence of his conduct or Himeno's view | OPEN (new) | — |
| TDH-C004 | 1 | The narrator revises his self-assessment but not clearly his contempt for others | INFERENCE | Analyst | U01 | Ch01 P0023, P0035, P0053; P0030 and P0049 undecidable | [U01 §5](readings/TDH_U01_DEEP_READING.md#5-narration-focalization-and-time) | Rival: contempt lines are free indirect child view; 勘違い may be a pose | OPEN | — |
| TDH-C005 | 1 | The proposal is surrounded by multiple hesitation markers; the narrator's explicit gloss (embarrassment, recognized "then") covers only the register shift | OBSERVATION | Narrator; Himeno's speech | U01 | Ch01 P0084–P0090 | [U01 §11](readings/TDH_U01_DEEP_READING.md#11-competing-interpretations-claims-and-forecasts) | — | OPEN (new) | — |
| TDH-C006 | 1 | The proposal is conditional, unaccepted and retracted; 約束 is the narrator's construal; the title's 約束 may name the proposal, the prophecy or both | OBSERVATION | Narrator; characters | U01 | Ch01 P0089–P0094; title P0002 | [U01 §4.7–4.8](readings/TDH_U01_DEEP_READING.md#4-factual-and-causal-reconstruction) | — | OPEN (new) | — |
| TDH-C007 | 1 | In the shrine dialogue Himeno is the main initiator and source of frames; the boy introduces the age-twenty arithmetic and marriage | INFERENCE | Analyst | U01 | Ch01 P0062–P0089 | [U01 §11](readings/TDH_U01_DEEP_READING.md#11-competing-interpretations-claims-and-forecasts) | Rival: selective memory foregrounds Himeno | OPEN (new) | — |

**Forecasts** (timestamped to their frontier; adjudication rows are appended, never edited in place):

| forecast_id | Frozen at | Forecast | Basis | Label | Adjudication |
|---|---|---|---|---|---|
| F-U01-a | Entering U01 | "Three days" names a bounded span treated as precious or measured | Title | PRIOR_EXPOSURE_POSSIBLE | Untested at U01 |
| F-U01-b | Entering U01 | Ch. 1 title implies a time-displaced childhood promise recalled or tested | Ch. 1 title | PRIOR_EXPOSURE_POSSIBLE | U01: CONFIRMED_WITH_QUALIFICATION (retracted proposal construed as promise) |
| F-U01-c | Entering U01 | A watcher figure and a childhood friend matter besides the narrator | Ch. 3, ch. 10 titles | PRIOR_EXPOSURE_POSSIBLE | U01: childhood friend = Himeno; watcher untested |
| F-U01-d | U01 exit | Narrative present opens in or near the summer when he is twenty | P0067–P0070, P0097 | PRIOR_EXPOSURE_POSSIBLE | Pending |
| F-U01-e | U01 exit | Price will be disclosed and contrast sharply with the boy's self-valuation | P0028, P0032; ch. 4 title | PRIOR_EXPOSURE_POSSIBLE | Pending |
| F-U01-f | U01 exit | Himeno returns (person or pursuit); the one-sided "promise" is measured against her view | P0092, P0094–P0095; ch. 10 title | PRIOR_EXPOSURE_POSSIBLE | Pending |
| F-U01-g | U01 exit | The young woman on the cover belongs to the narrator's present | Cover vs frontispiece; weakener: uniform-like clothing | PRIOR_EXPOSURE_POSSIBLE | Pending |
| F-U01-C1 | U01 exit (role C) | Next units move to the present at ~20 and narrate the sale; price well below the boy's self-valuation | P0004, P0028, P0032, P0035; ch. 4 title | PRIOR_EXPOSURE_POSSIBLE | Pending |
| F-U01-C2 | U01 exit (role C) | At the present he is neither great nor rich | P0035, P0094, P0098 | PRIOR_EXPOSURE_POSSIBLE | Pending |
| F-U01-C3 | U01 exit (role C) | Himeno not in contact when the present opens; her view of the "joke" will not mirror his | P0092, P0094–P0096; ch. 6 title | PRIOR_EXPOSURE_POSSIBLE | Pending |
| F-U01-C4 | U01 exit (role C) | Ch. 10 centers on a text addressed to an only childhood friend, most economically Himeno to the narrator | P0042; Himeno's 私; ch. 10 title | PRIOR_EXPOSURE_POSSIBLE | Pending |
| F-U01-C5 | U01 exit (role C) | Narration of the present keeps the sardonic, self-correcting, hedged habits; affection not named early | P0023, P0029–P0031, P0053, P0094–P0098 | PRIOR_EXPOSURE_POSSIBLE | Pending |

## Form and register

**Row unit:** an evidence-bearing instance or a justified linked pattern in voice, narration, address, focalization, rhythm, motif or inspected image. Fields: `form_id`, type, speaker/narrator and addressee, context/state, original-language anchor where necessary, working translation and alternatives, source locator(s), disclosure position, observation versus interpretation, recurrence basis, counterinstance, reading heading, affected claims and intended synthesis responsibility.

**Update trigger:** an instance changes or constrains a formal/character argument, or recurrence creates a cumulative question. An isolated local detail can remain in its reading with `LOCAL_ONLY` routing; later recurrence promotes it by linking the original full argument. Preserve original contexts when joining a pattern. A source-language register observation is not performed vocal delivery; no audio is available in this boundary. Record image evidence only after actual inspection.

At bootstrap there were no form/register rows. Rows below are appended per accepted unit.

| form_id | Type | Speaker → addressee | Anchor (short) | Working translation; alternatives | Locators | Observation vs interpretation | Recurrence / counterinstance | Reading | Affected claims; synthesis route |
|---|---|---|---|---|---|---|---|---|---|
| TDH-F001 | Benefactive framing of selling | Narrator (P0004); boy's thought (P0020) | 寿命を買い取ってもらえる; 売ってやってもいい | "have one's lifespan bought off one"; "I'd do it the favor of selling" | Ch01 P0004, P0020 | OBS of forms; candidate motif (rival: bleached trade-in idiom) | Track in sale scenes | [U01 §6](readings/TDH_U01_DEEP_READING.md#6-japanese-language-and-form) | C002; synthesis: exchange language |
| TDH-F002 | Orthographic split なにか / 何か | Teacher (buyer, ぼく/きみ); narration; Himeno | 『なにか』; 「何か」; その『何か』 | "something" ×3 | Ch01 P0016–P0021, P0060, P0070 | OBS of split; any identification HYPOTHESIS | Watch for the buyer's and the awaited event's realizations | [U01 §6](readings/TDH_U01_DEEP_READING.md#6-japanese-language-and-form) | C002; motif |
| TDH-F003 | Sesame-dot emphasis + simile | Narrator | 〔傍点〕ずれて〔/傍点〕いた; 咲く季節を間違えた花 | "out of step"; "flowers that mistook their season" | Ch01 P0054 | OBS; mistiming-not-defect is INF | Only emphasis in ch. 1; track other 傍点 | [U01 §6](readings/TDH_U01_DEEP_READING.md#6-japanese-language-and-form) | Self-conception; prophecy link |
| TDH-F004 | Register shift at proposal | Himeno → boy; boy's mirrored reply | 一緒になりませんか？; なんですか、それは; 忘れてちょうだい | "Shall we marry, as two leftovers?"; "What's that supposed to be?" | Ch01 P0087–P0092 | OBS; reading of reply OPEN | Track register shifts under emotion | [U01 §6](readings/TDH_U01_DEEP_READING.md#6-japanese-language-and-form) | C005, C006 |
| TDH-F005 | Market idiom for persons; 売る link | Himeno; boy; narrator | 生涯賃金; 処分料金; わりにあわない; 売れ残り; 〝売れ残っている〟 | "lifetime earnings"; "disposal fee"; "wouldn't balance out"; "unsold/left on the shelf" | Ch01 P0009, P0028, P0030, P0074, P0089, P0095; P0032 | OBS; irony HYPOTHESIS | Track | [U01 §6](readings/TDH_U01_DEEP_READING.md#6-japanese-language-and-form) | Interpretation C; synthesis |
| TDH-F006 | Distanced 幼馴染 vs warm ch. 10 title | Narrator; ch. 10 title voice (私) | いわゆる『幼馴染』というものに当たるのだろう; 私の、たった一人の幼馴染へ | "what you'd call a 'childhood friend', I suppose"; "To my one and only childhood friend" | Ch01 P0042, P0043, P0049; `text/part0003.html` P0012 | OBS; voice/stance change HYPOTHESIS | Adjudicate at U10 | [U01 §6](readings/TDH_U01_DEEP_READING.md#6-japanese-language-and-form) | F-U01-C4 |

## Reconstruction readiness

**Row unit:** one prospective named subject at one state boundary, only after source evidence identifies an appropriate subject. Fields: subject ID, continuity and valid interval, evidence dossier route, behavior/motivation/ordinary-life/relationship/knowledge/register coverage, missing opportunities versus negative constraints, contradictions, independent context count with source identities, held-out allocation and exposure log, model route if later authorized, evaluated limitations, reviewer, and next permitted operation.

**Update trigger:** a reading adds relevant coverage or contradiction, a state boundary changes, or independent assessment changes the usable scope. This section records evidential sufficiency and gaps; it assigns no capability tier. Preserve previous readiness decisions with their source boundaries. A high volume of citations cannot compensate for missing relationship or ordinary-life contexts. No percentages or universal behavioral guarantees are inferred.

At bootstrap there were no subject rows. Global state: `NOT_ASSESSED`; models: none; held-out source allocation: none; reconstruction operations: not authorized. Reserve genuine evaluation material before future model construction; when prior reading compromises blindness, disclose it and redesign assessment.

**Held-out note (2026-11-17).** The run reads every unit prospectively, so no unconsumed source unit will remain for held-out evaluation, and every participant may carry parametric prior exposure. Any later reconstruction assessment must therefore disclose that it is at most a `RETROSPECTIVE_CONSISTENCY_TEST` unless a genuinely independent evaluation boundary is arranged.

| Subject | Boundary | Coverage at boundary | Gaps | Readiness |
|---|---|---|---|---|
| Narrator (unnamed) | U01 | Childhood behavior, values, speech with Himeno; narrating voice; one relationship (Himeno); classmates and adults as context | No adult present-day conduct, ordinary life, other relationships | `NOT_ASSESSED`; candidate |
| Himeno | U01 | Childhood speech (two registers), initiative, values; one relationship | All via narrator; nothing after age ten | `NOT_ASSESSED`; candidate |

## Transaction and history

Each accepted future unit appends a transaction: unit/witness identity; full reading path; source coverage change; State row IDs; Claims transitions; Form/register changes; Readiness effects; explicit reviewed/no-supported-change entries; gaps; reviewer disposition; and next bounded operation. All linked arguments must survive a handoff in full. A transaction cannot declare completion while a required cumulative update remains deferred.

| Date | Control event | Analytical consequence |
|---|---|---|
| 2026-11-07 | Four independent notebook section contracts initialized for standalone scope | Zero literary observations; no subjects, claims or readiness findings; lock remains closed |
| 2026-11-16 | Witness `TDH-JP-01` bound; run `TDH-RUN-20261116-U01-U15` authorized; lock opened; multi-agent configuration recorded (architecture §8.1) | Still zero literary observations; unit transactions will be appended below as each unit is accepted |
| 2026-11-17 | **U01 accepted** ([reading](readings/TDH_U01_DEEP_READING.md)): S01–S05 and `text/part0004.html` P0001–P0098 | State TDH-S001–S008; Claims TDH-C001–C007 and forecasts F-U01-a–g, F-U01-C1–C5 (a–c adjudicated); Form TDH-F001–F006; Readiness: narrator and Himeno candidates, `NOT_ASSESSED`; held-out note recorded. Participation: A principal; B 37 findings; C 26 findings; D blind phase 1 (56 items) and phase 2 (25 findings, 6 material) → `ACCEPT_WITH_CORRECTIONS`, all material corrections adopted; P0020 voice disagreement preserved OPEN. Gaps: none blocking. Next: U02 |

Split a section into a dedicated file only when its independent retrieval need is demonstrated. Preserve IDs, full rows and bidirectional crosswalks; update the architecture and entrypoint together. Frozen snapshots receive errata or superseding versions, never silent replacement. This notebook remains the current mutable retrieval layer until a recorded architectural amendment changes that responsibility.
