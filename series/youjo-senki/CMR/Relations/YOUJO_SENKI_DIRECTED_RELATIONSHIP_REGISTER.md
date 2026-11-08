---
series: YOUJO_SENKI
artifact_id: YOUJO_SENKI_DIRECTED_RELATIONSHIP_REGISTER
artifact_type: directed_relationship_source_register
scope: "Japanese LN V01-V14; 77 directed source observations across 32 source units; 42 core-seven coverage cells"
generation: V2_CMR
version: "1.0"
status: active_provisional
canonical_home: "series/youjo-senki/CMR/Relations/YOUJO_SENKI_DIRECTED_RELATIONSHIP_REGISTER.md"
snapshot_date: 2026-10-12
promotion_status: PROPOSED_PENDING_VERIFIED_MAIN_INTEGRATION
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
---

# Directed relationship source register

This register and the [77 episode records](YOUJO_SENKI_DIRECTED_RELATIONSHIP_EPISODES.jsonl) preserve source-ready relationship analysis. They do not establish character models, a Tanya QA pass, or ensemble QA clearance. The [CMR entrypoint](../README.md), [governing method](../Methods/YOUJO_SENKI_CHARACTER_MODELING_REFERENCE_METHOD.md), [source-facing character readiness re-audit](../Provenance/YOUJO_SENKI_CHARACTER_READINESS_REAUDIT.md), and [Tanya diagnostic navigation](../Diagnostics/YOUJO_SENKI_TANYA_DIAGNOSTIC_NAVIGATION.md) provide the existing methodological and diagnostic context.

Each direction has its own actor access, speech, information limits, target agency and inference ceiling. A→B never supplies B→A by symmetry. Paired records share a source unit and dependence group. **77 observations / 32 distinct logged units / 2,043 distinct normalized source blocks** are inventory measures, not 77 independent behavioral scenes. The 1,141 supporting paragraph edges retain their original IDs, hashes and order; reuse of one paragraph across directions is evidence dependence.

The source reviewer read contiguous checksum-validated Japanese CMR0 windows. The orchestrating root independently verified original EPUB bytes and deterministic extraction. This port fully read every substantive analytical field of all 77 sealed observations, all 42 coverage cells, the complete source review and the governing source/seal/validation material. Exact routes, member context and all hashes were revalidated for the port; no second independent semantic or original-container reopen is claimed. The inherited `actual_read=true` and `source_container_reopened_here=false` describe that source review, not a newly performed container read.

Seven reserved construction QA ranges have zero shared blocks with the entire 2,043-block relationship read union. Only exclusion coordinates and reserve metadata were used in this port; private expected outcomes were not read. The source reviewer had prepared those outcomes earlier, so this is construction-held-out separation with mature V2/shared-source familiarity limits, not a fully blinded evaluation. No predictions or scores are produced here.

## Direction and identity controls

The 42 core cells concern Tanya, Visha, Lergen, Zettour, Weiss, Grantz and Uger. Rudersdorf, Calandro, Conrad, Gassman, Romel, Drake, Mary, Anson, Tospan, Meybert, Erya, Schugel, Loria, Josef, de Lugo and Ahrens have additional typed episodes outside that core matrix. An unnamed council remains a group target, not a fabricated person.

All original actor tokens and stable episode IDs remain literal. `AHRENS` in the relationship source package resolves to `ELMAR_AHRENS` in the existing focused-candidate identity route. `resolved_actor_id` and `resolved_target_id` expose this same-person crosswalk; they make no new readiness determination. The separately begun focused candidate audit is outside this sealed package. The older tentative “Ruder” label was a withdrawn working abbreviation for Rudersdorf; it is not an eighth established new person.

Speaker attribution and focalizer attribution stay separate. `HIGH_SOURCE_CONTEXT` for a spoken actor does not grant target mind access. Josef’s `HIGH_ROLE_CONTEXT_NOT_NAMED` is retained literally; no personal-name token is invented. Lergen’s memoir has `EXPLICIT_WRITTEN_AUTHOR` and `WRITTEN_SELF_PRESENTATION_ONLY`, not contemporaneous live voice. The two absent-Lergen group appraisals are recognition stances without a target response. Mixed focalization windows remain segmented as recorded.

## Core directed coverage

The sealed coverage ledger has **24 `DIRECT_SOURCE_AVAILABLE_IN_PACKAGE`, 3 `PARTIAL_APPRAISAL_OR_MEMOIR_ONLY`, and 15 `NOT_YET_AUDITED_IN_THIS_PACKAGE`** cells. Direct availability means an admitted observation exists in this package. It does not determine reconstruction class or completeness across eras, audiences and ordinary states. Partial means absent-target appraisal or memoir only; it cannot synthesize face-to-face voice or target private motives. Not-yet-audited makes no finding that a relation is absent or that source is insufficient.

The source ledger’s `independent_source_unit_count` is preserved below as “units”: it counts distinct logged dependence groups for that directed cell, not statistically independent scenes or independent evidence sources. Every cell retains `reciprocity_not_assumed=true`.

| Actor → target | Literal coverage status | Units | Exact episode IDs |
|---|---|---:|---|
| Tanya → Visha | `DIRECT_SOURCE_AVAILABLE_IN_PACKAGE` | 4 | `YS-CMR5-REL-V05-INTERVIEW-B`, `YS-CMR5-REL-V06-MUD-B`, `YS-CMR5-REL-V04-SEARCH-F`, `YS-CMR5-REL-V14-DUTY-A` |
| Tanya → Lergen | `DIRECT_SOURCE_AVAILABLE_IN_PACKAGE` | 1 | `YS-CMR5-REL-V14-CENSURE-B` |
| Tanya → Zettour | `DIRECT_SOURCE_AVAILABLE_IN_PACKAGE` | 1 | `YS-CMR5-REL-V14-GRATITUDE-B` |
| Tanya → Weiss | `DIRECT_SOURCE_AVAILABLE_IN_PACKAGE` | 2 | `YS-CMR5-REL-V04-SEARCH-C`, `YS-CMR5-REL-V06-PEACE-F` |
| Tanya → Grantz | `DIRECT_SOURCE_AVAILABLE_IN_PACKAGE` | 1 | `YS-CMR5-REL-V02-ARENE-B` |
| Tanya → Uger | `DIRECT_SOURCE_AVAILABLE_IN_PACKAGE` | 3 | `YS-CMR5-REL-V06-PEACE-B`, `YS-CMR5-REL-V01-STUDENT-B`, `YS-CMR5-REL-V09-HUMAN-B` |
| Visha → Tanya | `DIRECT_SOURCE_AVAILABLE_IN_PACKAGE` | 4 | `YS-CMR5-REL-V05-INTERVIEW-A`, `YS-CMR5-REL-V06-MUD-A`, `YS-CMR5-REL-V04-SEARCH-E`, `YS-CMR5-REL-V14-DUTY-B` |
| Visha → Lergen | `PARTIAL_APPRAISAL_OR_MEMOIR_ONLY` | 1 | `YS-CMR5-REL-V14-DUTY-D` |
| Visha → Zettour | `NOT_YET_AUDITED_IN_THIS_PACKAGE` | 0 | — |
| Visha → Weiss | `DIRECT_SOURCE_AVAILABLE_IN_PACKAGE` | 1 | `YS-CMR5-REL-V03-PHONE-A` |
| Visha → Grantz | `NOT_YET_AUDITED_IN_THIS_PACKAGE` | 0 | — |
| Visha → Uger | `NOT_YET_AUDITED_IN_THIS_PACKAGE` | 0 | — |
| Lergen → Tanya | `DIRECT_SOURCE_AVAILABLE_IN_PACKAGE` | 1 | `YS-CMR5-REL-V14-CENSURE-A` |
| Lergen → Visha | `NOT_YET_AUDITED_IN_THIS_PACKAGE` | 0 | — |
| Lergen → Zettour | `PARTIAL_APPRAISAL_OR_MEMOIR_ONLY` | 1 | `YS-CMR5-REL-V11-MEMOIR-A` |
| Lergen → Weiss | `NOT_YET_AUDITED_IN_THIS_PACKAGE` | 0 | — |
| Lergen → Grantz | `NOT_YET_AUDITED_IN_THIS_PACKAGE` | 0 | — |
| Lergen → Uger | `DIRECT_SOURCE_AVAILABLE_IN_PACKAGE` | 1 | `YS-CMR5-REL-V10-RAIL-A` |
| Zettour → Tanya | `DIRECT_SOURCE_AVAILABLE_IN_PACKAGE` | 1 | `YS-CMR5-REL-V14-GRATITUDE-A` |
| Zettour → Visha | `NOT_YET_AUDITED_IN_THIS_PACKAGE` | 0 | — |
| Zettour → Lergen | `NOT_YET_AUDITED_IN_THIS_PACKAGE` | 0 | — |
| Zettour → Weiss | `NOT_YET_AUDITED_IN_THIS_PACKAGE` | 0 | — |
| Zettour → Grantz | `DIRECT_SOURCE_AVAILABLE_IN_PACKAGE` | 1 | `YS-CMR5-REL-V14-ADOPTION-C` |
| Zettour → Uger | `DIRECT_SOURCE_AVAILABLE_IN_PACKAGE` | 1 | `YS-CMR5-REL-V14-ADOPTION-A` |
| Weiss → Tanya | `DIRECT_SOURCE_AVAILABLE_IN_PACKAGE` | 3 | `YS-CMR5-REL-V04-SEARCH-D`, `YS-CMR5-REL-V06-PEACE-E`, `YS-CMR5-REL-V14-DUTY-C` |
| Weiss → Visha | `DIRECT_SOURCE_AVAILABLE_IN_PACKAGE` | 1 | `YS-CMR5-REL-V03-PHONE-B` |
| Weiss → Lergen | `PARTIAL_APPRAISAL_OR_MEMOIR_ONLY` | 1 | `YS-CMR5-REL-V14-DUTY-E` |
| Weiss → Zettour | `NOT_YET_AUDITED_IN_THIS_PACKAGE` | 0 | — |
| Weiss → Grantz | `DIRECT_SOURCE_AVAILABLE_IN_PACKAGE` | 1 | `YS-CMR5-REL-V04-SEARCH-A` |
| Weiss → Uger | `DIRECT_SOURCE_AVAILABLE_IN_PACKAGE` | 1 | `YS-CMR5-REL-V06-PEACE-D` |
| Grantz → Tanya | `DIRECT_SOURCE_AVAILABLE_IN_PACKAGE` | 1 | `YS-CMR5-REL-V02-ARENE-A` |
| Grantz → Visha | `NOT_YET_AUDITED_IN_THIS_PACKAGE` | 0 | — |
| Grantz → Lergen | `NOT_YET_AUDITED_IN_THIS_PACKAGE` | 0 | — |
| Grantz → Zettour | `DIRECT_SOURCE_AVAILABLE_IN_PACKAGE` | 1 | `YS-CMR5-REL-V14-ADOPTION-D` |
| Grantz → Weiss | `DIRECT_SOURCE_AVAILABLE_IN_PACKAGE` | 1 | `YS-CMR5-REL-V04-SEARCH-B` |
| Grantz → Uger | `NOT_YET_AUDITED_IN_THIS_PACKAGE` | 0 | — |
| Uger → Tanya | `DIRECT_SOURCE_AVAILABLE_IN_PACKAGE` | 3 | `YS-CMR5-REL-V06-PEACE-A`, `YS-CMR5-REL-V01-STUDENT-A`, `YS-CMR5-REL-V09-HUMAN-A` |
| Uger → Visha | `NOT_YET_AUDITED_IN_THIS_PACKAGE` | 0 | — |
| Uger → Lergen | `DIRECT_SOURCE_AVAILABLE_IN_PACKAGE` | 1 | `YS-CMR5-REL-V10-RAIL-B` |
| Uger → Zettour | `DIRECT_SOURCE_AVAILABLE_IN_PACKAGE` | 1 | `YS-CMR5-REL-V14-ADOPTION-B` |
| Uger → Weiss | `DIRECT_SOURCE_AVAILABLE_IN_PACKAGE` | 1 | `YS-CMR5-REL-V06-PEACE-C` |
| Uger → Grantz | `NOT_YET_AUDITED_IN_THIS_PACKAGE` | 0 | — |

The literal gap notes are preserved by status: direct — “Additional eras/audiences/ordinary contexts remain unaudited; existence of evidence is not a model or QA clearance.”; partial — “Absent-target appraisal/testimony only; do not synthesize face-to-face voice or target private motives.”; not-yet-audited — “No source package determination for this directed cell. This does not assert no relationship exists or insufficient source.”. No missing reverse cell is filled by a target-agency sentence in another record.

## Conditional relationship routes

Each unit below names phase, office/rank, audience and focalization before its separate directed findings. The curated reading concerns trust, obligation, disclosure, refusal, care and misperception only where supported; an unobserved dimension remains bounded by the episode’s limits. Exact source coordinates in the JSONL are the reopening authority. Volume/spine order is not guaranteed chronological order; stated appointments, promised work, forecast outcomes and present authority adoption must not be promoted into earlier realized facts.

Search a full `relationship_episode_id` in the JSONL for every preserved field and supporting tuple. The group names below are human navigation anchors and the original `dependence_group` labels.

### V05-INTERVIEW

**Phase:** V05 Federation campaign; experienced command group. **Roles:** Tanya — Lieutenant Colonel/commander; Visha — Lieutenant/adjutant; Weiss — Major/deputy.

**Authority condition:** Tanya commands; Visha has linguistic/information expertise, not equal command authority. **Audience/setting:** Post-attack staff exchange with Weiss present. **Focalization:** Tanya; Visha actions/speech directly attributed.

**Source unit:** `YS-CMR0-V05-013-00646` through `YS-CMR0-V05-013-00711`; 66 normalized blocks. `OEBPS/Text/part0011.xhtml`, spine 13. Window SHA256 `0e530fca4eec5839604a10ac1c25ee6e9faf017a43805cbd57eb63db25f3f12b`. The shared EPUB/member identity and hashes are in each episode’s `source`. The source unit has earlier sealed character witnesses.

**Conditional reading:** Trust is evidenced by independently prepared linguistic evidence and a commander’s correction of her own premature interpretation. Obligation remains commander/adjutant duty. Visha supplies a correction and prior prisoner-interview material; Tanya’s private ideological misreading is not her public response. Reuse of expertise is operational appreciation, not equal rank or unlimited access to Visha’s mind.

- **Visha → Tanya — `YS-CMR5-REL-V05-INTERVIEW-A`.** `DIRECT_INTERACTION`. Professionally deferential correction and independently prepared evidence.
  - Private access: Unavailable in this directed record. Actor-access category: `NO_DIRECT_ACTOR_PRIVATE_ACCESS_IN_THIS_DIRECTED_RECORD`.
  - Behavior/public speech: Requests reports and supplies prior prisoner-interview notes. Tentative recommendation, permission request, exact ideological correction and qualified unit identification.
  - Communicative objective: Correct an information frame through useful evidence. This remains bounded scene interpretation. Withheld content: Not independently recorded.
  - Written register: 中佐殿 / 失礼ですが / 厳密に申し上げるならば / かと思われます.
  - External reading/consequence: Tanya reads steadiness as specialist confidence. Commander orders wider review and first-hand observation.
  - Target agency: Tanya initially rejects a supposedly duplicate inquiry, then examines the discrepant record.
  - Information/misperception: No source for Visha's entire prisoner-facing conversation or every private motive. Inference ceiling: Expertise and role-bound firmness; neither omniscience nor unrestricted insubordination.

- **Tanya → Visha — `YS-CMR5-REL-V05-INTERVIEW-B`.** `DIRECT_INTERACTION`. Initial skepticism becomes evidence-seeking appreciation and task delegation.
  - Private access: Direct language-barrier appraisal and recognition of her own ideology-led error. Actor-access category: `EXPLICIT_BOUNDED_ACTOR_ACCESS`.
  - Behavior/public speech: Reads notes, checks their provenance, orders a meeting and includes Visha as translator. Initial qualified rejection, verification question and task instruction.
  - Communicative objective: Verify discrepant evidence and exploit actual specialist competence. This remains bounded scene interpretation. Withheld content: Private prior-world/ideological framing is not fully disclosed to the adjutant.
  - Written register: 貴官 / セレブリャコーフ中尉 with questions and direct role assignment.
  - External reading/consequence: Visha corrects the ideological category and specifies a limited evidentiary basis. Information gathering changes; no final prisoner-analysis result in this window.
  - Target agency: Visha had already done work and contributes an independently useful correction.
  - Information/misperception: Tanya initially assumes reports adequately represent ideological soldiers, then sees ordinary human testimony. Inference ceiling: Appreciation does not abolish hierarchy; commander error/repair remains part of the relation.

### V06-MUD

**Phase:** V06 Eastern winter; same commander/adjutant roles. **Roles:** Tanya — Lieutenant Colonel; Visha — Lieutenant.

**Authority condition:** Subordinate may disagree in this trusted professional exchange; command decides report routing. **Audience/setting:** Winter preparation/field logistics discussion. **Focalization:** Tanya; Visha speech/actions, no direct full Visha interiority.

**Source unit:** `YS-CMR0-V06-013-00125` through `YS-CMR0-V06-013-00206`; 82 normalized blocks. `OEBPS/Text/part0011.xhtml`, spine 13. Window SHA256 `852f4280c32a7548846201abf7f80fbfb9a30262525aa616f791ea06d78a6ba8`. The shared EPUB/member identity and hashes are in each episode’s `source`. The source unit has earlier sealed character witnesses.

**Conditional reading:** A trusted subordinate can make a polite substantive refusal and name the mud/mobility mechanism. Tanya questions, revises and permits report routing. This local receptivity neither predicts headquarters acceptance nor proves that all objections can be safely made. Care and trust are shown through evidence reception rather than generic warmth.

- **Visha → Tanya — `YS-CMR5-REL-V06-MUD-A`.** `DIRECT_INTERACTION`. Respectful substantive refusal with a concrete operational mechanism.
  - Private access: Unavailable in this directed record. Actor-access category: `NO_DIRECT_ACTOR_PRIVATE_ACCESS_IN_THIS_DIRECTED_RECORD`.
  - Behavior/public speech: Sustains the objection, then asks whether a report is really permitted. Firm politeness-prefaced disagreement and mobility explanation.
  - Communicative objective: Correct seasonal threat weighting.  This remains bounded scene interpretation. Withheld content: Not independently recorded.
  - Written register: 小官 / 中佐殿 / 失礼ですが / 同意できません.
  - External reading/consequence: Tanya finds her unusually strong rebuttal interesting. Her report is requested for staff consideration.
  - Target agency: Tanya updates her assessment and requests the report.
  - Information/misperception: Expertise is not certainty in every domain; permission surprise remains visible. Inference ceiling: No generalized defiance, no independent statement that headquarters will accept the report.

- **Tanya → Visha — `YS-CMR5-REL-V06-MUD-B`.** `DIRECT_INTERACTION`. Questions the dissent, revises her appraisal and authorizes an external report.
  - Private access: Direct interest, self-correction and recognition of narrowed attention. Actor-access category: `EXPLICIT_BOUNDED_ACTOR_ACCESS`.
  - Behavior/public speech: Nods, orders a report and redirects logistics questions. Requests the mechanism and explains why field experience can challenge doctrine.
  - Communicative objective: Make useful divergent field knowledge actionable. This remains bounded scene interpretation. Withheld content: Self-narrowed attention is narrated privately; not all corporate analogies are spoken.
  - Written register: 貴官 / 中尉 and explicit report request; no punitive reprimand.
  - External reading/consequence: Visha remains deferential while holding the substantive objection. Report enters a possible General Staff route, not guaranteed institutional change.
  - Target agency: Visha's stated countermechanism forces a revision, not merely an approved comfort role.
  - Information/misperception: She is susceptible to prior-world winter emphasis and homogeneous staff doctrine. Inference ceiling: A receptive episode does not prove she never coerces subordinates elsewhere.

### V03-PHONE

**Phase:** V03 leave/Imperial-capital visit. **Roles:** Visha — Second Lieutenant/adjutant; Weiss — Lieutenant/deputy; Grantz — Second Lieutenant.

**Authority condition:** Weiss is senior; Visha can complete a task and withhold an optional inference. **Audience/setting:** Long-distance handover call to a holiday facility; Grantz audible there. **Focalization:** Visha; Weiss state explicitly described as intoxicated, usual baseline different.

**Source unit:** `YS-CMR0-V03-027-00055` through `YS-CMR0-V03-027-00087`; 33 normalized blocks. `text/part0025.html`, spine 27. Window SHA256 `7e75ce7a4b1754448cccb24746914b1a98f52dbe7caa506dcc033dc5f87f90a6`. The shared EPUB/member identity and hashes are in each episode’s `source`. The source unit has earlier sealed character witnesses.

**Conditional reading:** The telephone task permits Visha to give exact formal notice while omitting an optional warning. Her minor irritation remains private. Weiss’s intoxication explains a cheerful invitation joke and a self-chosen decision; his usual quieter baseline is separately described. Neither direction establishes romance, literal false orders or a durable intoxicated voice.

- **Visha → Weiss — `YS-CMR5-REL-V03-PHONE-A`.** `DIRECT_INTERACTION`. Minor irritation becomes exact formal handover and selective omission.
  - Private access: Direct annoyance, awareness that communication probably suffices, playful inward retaliation. Actor-access category: `EXPLICIT_BOUNDED_ACTOR_ACCESS`.
  - Behavior/public speech: Calls, conveys true facts and laughs at the resulting holiday-side response. Polite apology, handover facts and formally bounded refusal to say more.
  - Communicative objective: Complete mandated handover while allowing his unnecessary inconvenience. This remains bounded scene interpretation. Withheld content: Her own view that a phone call would likely suffice.
  - Written register: 中尉殿 / 小官 / 僭越ながら / ご随意に; irritation is not spoken insult.
  - External reading/consequence: She reads his uncharacteristic delayed understanding as drunkenness. Weiss decides to contact/return to the commander; his final action outcome is not shown.
  - Target agency: He makes his own choice; Visha does not utter a false direct return order.
  - Information/misperception: Weiss treats notice as requiring direct adjustment and casts it as a lady's invitation. Inference ceiling: No romance or universal passive sweetness; this particular petty retaliation is state/relationship-bound.

- **Weiss → Visha — `YS-CMR5-REL-V03-PHONE-B`.** `DIRECT_INTERACTION`. Drunken cheerful teasing and self-chosen response to formal notice.
  - Private access: Unavailable in this directed record. Actor-access category: `NO_DIRECT_ACTOR_PRIVATE_ACCESS_IN_THIS_DIRECTED_RECORD`.
  - Behavior/public speech: Answers the call and announces he will ask the commander directly. Familiar holiday tease, practical inference and a playful lady-invitation explanation to Grantz.
  - Communicative objective: Handle notice from the adjutant while enjoying leave.  This remains bounded scene interpretation. Withheld content: Not independently recorded.
  - Written register: ヴィーシャ / 君 versus later formal 少尉; state is explicitly intoxication.
  - External reading/consequence: Visha knows his usual calmer, more thoughtful delivery differs here. Handover produces a decision, not an independently observed completed return.
  - Target agency: Visha delivers a true but selectively incomplete notice rather than agreeing to his holiday framing.
  - Information/misperception: He does not perceive her withheld convenience judgment in this window. Inference ceiling: No independent Weiss private cognition and no generic flirting/romance rule.

### V04-SEARCH

**Phase:** V04 rescue search in enemy territory. **Roles:** Tanya — Major/commander; Weiss — Captain/deputy; Grantz — Lieutenant; Visha — Lieutenant/adjutant.

**Authority condition:** Command divides risk/tasks; subordinate judgment can persist without complete public disclosure. **Audience/setting:** Ground search, airborne cover and radio-linked regrouping. **Focalization:** Tanya early; Weiss search focalization; Tanya again after regrouping.

**Source unit:** `YS-CMR0-V04-029-00099` through `YS-CMR0-V04-029-00143`; 45 normalized blocks. `OEBPS/Text/part0027.xhtml`, spine 29. Window SHA256 `45daadd8bbb6ff47a8dda3e89a32b245e8e53fb26ea515e7921e948cc8a9047a`. The shared EPUB/member identity and hashes are in each episode’s `source`. The source unit has earlier sealed character witnesses.

**Conditional reading:** Six directed records share one search unit. Weiss’s shoulder tap and restrained public response support Grantz while his own feasibility/casualty reasoning stays distinct. Grantz’s qualified report is not a full private monologue. Tanya’s public cover promise coexists with a private airborne escape advantage while allocating grounded danger to Weiss. Visha’s demonstrated independent command responsibility is developmental evidence; it must not be projected into her trainee state.

- **Weiss → Grantz — `YS-CMR5-REL-V04-SEARCH-A`.** `DIRECT_INTERACTION`. Quiet support under a shared infeasible task, with independent casualty-risk assessment.
  - Private access: Direct hope in Tanya and conflicting realism about stopping the search. Actor-access category: `EXPLICIT_BOUNDED_ACTOR_ACCESS`.
  - Behavior/public speech: Taps Grantz's shoulder, continues search and later responds to recall. Task questions and restrained complaint; not every feasibility concern is spoken.
  - Communicative objective: Keep the junior functioning while judging the search limit. This remains bounded scene interpretation. Withheld content: Full internal inclination toward stopping the search.
  - Written register: グランツ中尉 / 大隊長殿; limited public words plus bodily reassurance.
  - External reading/consequence: Weiss infers discomfort from Grantz's unfinished words and look. New police-radio information subsequently changes the task.
  - Target agency: Grantz reports threat and starts an objection; silence is not proof of free assent.
  - Information/misperception: Hope in Tanya's competence conflicts with immediate terrain/time evidence. Inference ceiling: The shoulder tap belongs to Weiss. His reading of Grantz's mind remains inference.

- **Grantz → Weiss — `YS-CMR5-REL-V04-SEARCH-B`.** `DIRECT_INTERACTION`. Qualified field reporting and interrupted feasibility concern.
  - Private access: Unavailable in this directed record. Actor-access category: `NO_DIRECT_ACTOR_PRIVATE_ACCESS_IN_THIS_DIRECTED_RECORD`.
  - Behavior/public speech: Reports worsening enemy approach and falls silent before completing the objection. Factual warnings and a hesitant question about pursuing footprints.
  - Communicative objective: Report danger and raise a limit within subordinate role. This remains bounded scene interpretation. Withheld content: A full objection is not voiced; exact private motive is not directly available.
  - Written register: ヴァイス大尉殿; qualified 見つけられなくはありません / ですが.
  - External reading/consequence: Weiss interprets his silence/look as awareness of excessive risk. Task remains under command until new information/recall.
  - Target agency: Weiss responds with a quiet tap and his own assessment, not a punitive demand for enthusiasm.
  - Information/misperception: Weiss's inference does not supply a transparent Grantz interior monologue. Inference ceiling: No assumed cowardice, no claimed psychological recovery or full consent.

- **Tanya → Weiss — `YS-CMR5-REL-V04-SEARCH-C`.** `DIRECT_INTERACTION`. Promises cover while allocating the grounded risk to the deputy.
  - Private access: Direct preference to retain an airborne escape position, even at risk to the capable deputy. Actor-access category: `EXPLICIT_BOUNDED_ACTOR_ACCESS`.
  - Behavior/public speech: Splits the unit and remains airborne. Affirms she will guard subordinate backs and assigns search.
  - Communicative objective: Complete rescue while preserving her own mobile position. This remains bounded scene interpretation. Withheld content: Her candid comparative risk-to-self appraisal.
  - Written register: Direct task commands and confident cover assurance.
  - External reading/consequence: Weiss treats airborne commander cover as reliable support. Ground/air tasks split, not equal danger or transparent motive.
  - Target agency: Weiss requests Grantz and protects the commander/adjutant pairing instead of passively accepting every composition.
  - Information/misperception: Weiss's trust does not mean he knows the private self-preservation reasoning. Inference ceiling: Public care claim and private self-interest both remain source evidence.

- **Weiss → Tanya — `YS-CMR5-REL-V04-SEARCH-D`.** `DIRECT_INTERACTION`. Respects command while retaining composition and feasibility judgment.
  - Private access: Direct hope in her exceptional capacity and conflicting rescue-risk appraisal. Actor-access category: `EXPLICIT_BOUNDED_ACTOR_ACCESS`.
  - Behavior/public speech: Takes the search, regroups and corrects a police-radio expectation. Requests Grantz, protects existing pairing, and softens the corrective explanation.
  - Communicative objective: Support the task without discarding independent practical knowledge. This remains bounded scene interpretation. Withheld content: Full inclination to stop costly search before the new clue.
  - Written register: 少佐殿 / かとは思いますが; respectful correction is possible.
  - External reading/consequence: Tanya accepts the correction about police practice. A specific intercepted clue changes rescue feasibility.
  - Target agency: Tanya changes the plan using evidence and acknowledges his correction.
  - Information/misperception: He partly overestimates her ability to resolve impossibility; new information actually matters. Inference ceiling: Trust is not a guarantee of every command's practicability.

- **Visha → Tanya — `YS-CMR5-REL-V04-SEARCH-E`.** `DIRECT_INTERACTION`. Concise expert estimate and explicit acceptance of independent command responsibility.
  - Private access: Unavailable in this directed record. Actor-access category: `NO_DIRECT_ACTOR_PRIVATE_ACCESS_IN_THIS_DIRECTED_RECORD`.
  - Behavior/public speech: Takes a company to perform the rescue. Force estimate followed by confident assent.
  - Communicative objective: Estimate required force and execute assigned rescue.  This remains bounded scene interpretation. Withheld content: Not independently recorded.
  - Written register: 少佐殿 / 可能かと / お任せください.
  - External reading/consequence: Tanya privately values her learned capacity to think/act herself. She receives a company command, not unrestricted autonomy everywhere.
  - Target agency: Tanya asks, evaluates and modifies the estimate rather than merely outsourcing a fixed answer.
  - Information/misperception: Her estimate is qualified; Tanya increases the force for transport risk. Inference ceiling: This supports demonstrated growth; not an unbounded strategic skill claim.

- **Tanya → Visha — `YS-CMR5-REL-V04-SEARCH-F`.** `DIRECT_INTERACTION`. Values growing expertise and delegates a meaningful mission with risk correction.
  - Private access: Direct pleased recognition of human learning and self-directed skill, then prioritizes the task. Actor-access category: `EXPLICIT_BOUNDED_ACTOR_ACCESS`.
  - Behavior/public speech: Requests an estimate and assigns a company. Invites field-experience judgment and increases force for transport safety.
  - Communicative objective: Use demonstrated specialist experience for a bounded task. This remains bounded scene interpretation. Withheld content: Her personal satisfaction is not fully disclosed as a private confession.
  - Written register: 貴官 / 中尉, clear operational assignment.
  - External reading/consequence: Visha responds promptly and takes the role. Delegated command gives actual agency within the mission.
  - Target agency: Visha provides her own estimate and accepts control, not mere comfort service.
  - Information/misperception: Recognizing expertise does not eliminate the need to qualify an optimistic force estimate. Inference ceiling: No projection of this later growth into an already perfected early trainee.

### V06-PEACE

**Phase:** V06 settlement discussion. **Roles:** Tanya — Lieutenant Colonel; Uger — Lieutenant Colonel/staff; college contemporary; Weiss — Major/deputy.

**Authority condition:** Tanya/Uger are same-rank former classmates; Weiss answers a senior staff officer after his own commander's permission. **Audience/setting:** Staff exchange with multiple viewpoints. **Focalization:** Tanya; other officers' feelings are self-statements and visible behavior, not transparent interiority.

**Source unit:** `YS-CMR0-V06-027-00105` through `YS-CMR0-V06-027-00160`; 56 normalized blocks. `OEBPS/Text/part0025.xhtml`, spine 27. Window SHA256 `28708d51351eeec1de6ff0f15f7865abfe47f108cce71776b756d6975fdbb77d`. The shared EPUB/member identity and hashes are in each episode’s `source`. The source unit has earlier sealed character witnesses.

**Conditional reading:** Same-rank former classmates disagree over loss-cutting, sacrifice and affect; Uger admits rational force yet refuses emotionally. His separate request to Weiss requires Tanya’s permission and receives a personally qualified answer. Tanya permits speech but discovers a gap in her understanding of her deputy. A correct argument does not erase grief; a respectful objection does not establish every-context refusal rights.

- **Uger → Tanya — `YS-CMR5-REL-V06-PEACE-A`.** `DIRECT_INTERACTION`. Emotionally rejects a proposed settlement while admitting its rational force.
  - Private access: Unavailable in this directed record. Actor-access category: `NO_DIRECT_ACTOR_PRIVATE_ACCESS_IN_THIS_DIRECTED_RECORD`.
  - Behavior/public speech: Visibly restrains anger, seeks another field viewpoint and closes the immediate deputy debate. Calls the proposal surrender, cites lost lives, admits rational assent but emotional resistance.
  - Communicative objective: Make sacrifice/emotional limits part of the decision.  This remains bounded scene interpretation. Withheld content: Not independently recorded.
  - Written register: デグレチャフ中佐, forceful rebuttal and metaphorical emotion report.
  - External reading/consequence: Tanya is surprised by a moderate contemporary's position. A contrasting field answer constrains settlement advocacy; no actual peace result.
  - Target agency: Tanya argues further loss avoidance, then reluctantly acknowledges the objection.
  - Information/misperception: Uger's self-described feelings are not an independently narrated complete motive. Inference ceiling: Fatherhood/humaneness does not mean immediate assent to every peace proposal.

- **Tanya → Uger — `YS-CMR5-REL-V06-PEACE-B`.** `DIRECT_INTERACTION`. Offers frank loss-cutting counsel to a familiar staff contemporary, then confronts unexpected emotional refusal.
  - Private access: Direct hesitation, cost reasoning and disappointed/shaken expectation. Actor-access category: `EXPLICIT_BOUNDED_ACTOR_ACCESS`.
  - Behavior/public speech: States the proposal and later nods reluctantly. Formal reasoned proposal, further-loss reply and qualified acknowledgment.
  - Communicative objective: Prevent further losses through an immediately available settlement. This remains bounded scene interpretation. Withheld content: Corporate precedent and private surprise are not disclosed verbatim.
  - Written register: お言葉ですが / 道理かと / ウーガ中佐殿.
  - External reading/consequence: Uger calls it surrender and insists emotionally on accumulated sacrifice. Her expectation of field support fails inside this exchange.
  - Target agency: Uger asks Weiss rather than accepting Tanya's perspective as representative.
  - Information/misperception: She expects professional logic to determine emotional assent. Inference ceiling: No achieved institutional policy and no objective verdict that emotion is mere stupidity.

- **Uger → Weiss — `YS-CMR5-REL-V06-PEACE-C`.** `DIRECT_INTERACTION`. Seeks a field viewpoint other than Tanya's and accepts its distinction.
  - Private access: Unavailable in this directed record. Actor-access category: `NO_DIRECT_ACTOR_PRIVATE_ACCESS_IN_THIS_DIRECTED_RECORD`.
  - Behavior/public speech: Directly asks the deputy, then interrupts a prolonged commander/deputy challenge. Repeated specific request for his opinion and acknowledgment of a field answer.
  - Communicative objective: Test whether the commander's view represents frontline experience.  This remains bounded scene interpretation. Withheld content: Not independently recorded.
  - Written register: ヴァイス少佐 / 貴官 / どう見る.
  - External reading/consequence: Tanya recognizes the request for a different perspective. The professional discussion gains a distinct testimony.
  - Target agency: Weiss explicitly limits his answer to his own personal view.
  - Information/misperception: No assumption of a personally close Uger/Weiss friendship outside this role. Inference ceiling: A solicited opinion does not establish unquestioned full access to the deputy's thought.

- **Weiss → Uger — `YS-CMR5-REL-V06-PEACE-D`.** `DIRECT_INTERACTION`. Permission-conditioned, personally bounded disclosure of a conflict.
  - Private access: Unavailable in this directed record. Actor-access category: `NO_DIRECT_ACTOR_PRIVATE_ACCESS_IN_THIS_DIRECTED_RECORD`.
  - Behavior/public speech: Looks to his own commander for permission before answering. Prefers avoiding further casualties yet cannot emotionally discard earlier loss; explicitly limits the claim to himself.
  - Communicative objective: Give an honest limited account within authority constraints.  This remains bounded scene interpretation. Withheld content: Not independently recorded.
  - Written register: 結論から申し上げますと / 小官個人 / 考えております.
  - External reading/consequence: Uger reads the answer as a field viewpoint. Provides an independent perspective rather than a simple echo of Tanya.
  - Target agency: Uger asks and listens; Tanya authorizes speech rather than dictating its content.
  - Information/misperception: Self-stated personal conflict is not a universal frontline opinion. Inference ceiling: No unqualified reading of all soldiers' feelings or hidden Weiss motives.

- **Weiss → Tanya — `YS-CMR5-REL-V06-PEACE-E`.** `DIRECT_INTERACTION`. Respectfully challenges the assumption that sound reasoning dissolves grief.
  - Private access: Unavailable in this directed record. Actor-access category: `NO_DIRECT_ACTOR_PRIVATE_ACCESS_IN_THIS_DIRECTED_RECORD`.
  - Behavior/public speech: After permission, turns the commander's question back toward her. Asks why she can discard the feeling and repeats that the answer is logic.
  - Communicative objective: Clarify the emotional residue that her account omits.  This remains bounded scene interpretation. Withheld content: Not independently recorded.
  - Written register: 中佐殿 / 失礼ですが / それは理屈です.
  - External reading/consequence: Tanya's settled expectation of her practical deputy is shaken. Shows disagreement inside a trusted command relationship.
  - Target agency: She grants initial permission and then asks for clarification; not a penalty in this episode.
  - Information/misperception: Her judgment of his common sense did not predict this answer. Inference ceiling: Respectful disagreement here does not imply unrestricted ability to refuse every order.

- **Tanya → Weiss — `YS-CMR5-REL-V06-PEACE-F`.** `DIRECT_INTERACTION`. Authorizes independent speech but discovers the deputy does not share her expected loss-cutting affect.
  - Private access: Direct expectation, shock and uncertainty about the independent emotional response. Actor-access category: `EXPLICIT_BOUNDED_ACTOR_ACCESS`.
  - Behavior/public speech: Nods permission and interrupts to question the unexpected answer. Invites his view, then probes how even he cannot divide feeling from decision.
  - Communicative objective: Use his different field perspective, then understand an unexpected divergence. This remains bounded scene interpretation. Withheld content: She privately compares the adjutant's prolonged exposure and the deputy's reference value.
  - Written register: かまわんぞ / 存念 / 貴官ですら.
  - External reading/consequence: Weiss distinguishes reason from emotional ability to accept it. Broad professional sameness proves a poor predictor of assent.
  - Target agency: He offers a personally qualified reply rather than mechanically copying his commander.
  - Information/misperception: Her estimate of his practicality is not his full interiority. Inference ceiling: Her surprise matters; do not retrofit perfect knowledge of every subordinate.

### V10-RAIL

**Phase:** V10 backup-plan deadline and diplomacy effort. **Roles:** Lergen — Colonel/staff; Uger — Lieutenant Colonel/rail specialist.

**Authority condition:** Same-army senior staff request; specialist limit and family cost can be voiced. **Audience/setting:** Private professional planning exchange. **Focalization:** Lergen; Uger self-statements and visible fatigue.

**Source unit:** `YS-CMR0-V10-040-00018` through `YS-CMR0-V10-040-00052`; 35 normalized blocks. `OEBPS/Text/part0038.xhtml`, spine 40. Window SHA256 `1c49857d93f04da989e8db22879e1f710bfe871cbbffc8175bf96e0e4c42280b`. The shared EPUB/member identity and hashes are in each episode’s `source`. The source unit has earlier sealed character witnesses.

**Conditional reading:** A senior’s deadline imposes excessive work on a specialist. Lergen apologizes sincerely and admits uncertain hope; Uger voices family-cost resentment and independently commits to the shared task. Duty and care coexist with real burden. The promise to finish is not completed railway capacity, and a threatened daughter’s dislike is not her observed response.

- **Lergen → Uger — `YS-CMR5-REL-V10-RAIL-A`.** `DIRECT_INTERACTION`. Duty-driven request with sincere apology, admitting excess and uncertain hope.
  - Private access: Direct dislike of politics, recognition of military-plan reality, scarce hope and commitment. Actor-access category: `EXPLICIT_BOUNDED_ACTOR_ACCESS`.
  - Behavior/public speech: Bows and asks for maximum schedule flexibility. Requests extra effort, allows blame and pleads for time.
  - Communicative objective: Buy time for a less disastrous national route. This remains bounded scene interpretation. Withheld content: His low-confidence hopes for diplomacy are not a guaranteed forecast.
  - Written register: 中佐 / 君 / すまん / 頼む; lower formality accompanies sincere institutional burden.
  - External reading/consequence: Uger reminds him of specialist limits and lost family time. Uger pledges work; actual additional months/success are not established.
  - Target agency: Uger can object and express resentment while choosing cooperation.
  - Information/misperception: He recognizes that the requested margin may be wishful and costly. Inference ceiling: No universal kindness claim or guaranteed railroad flexibility.

- **Uger → Lergen — `YS-CMR5-REL-V10-RAIL-B`.** `DIRECT_INTERACTION`. Explicit family-cost resentment alongside collective duty.
  - Private access: Unavailable in this directed record. Actor-access category: `NO_DIRECT_ACTOR_PRIVATE_ACCESS_IN_THIS_DIRECTED_RECORD`.
  - Behavior/public speech: Shrugs with fatigue and accepts continued effort. States limits, names the daughter's loss and says he will resent him yet work together.
  - Communicative objective: Keep professional cooperation while naming its personal cost. This remains bounded scene interpretation. Withheld content: No independently narrated Uger private resentment beyond his spoken claim.
  - Written register: 大佐殿 / お言葉ですが / 恨みますよ / やりとげましょう.
  - External reading/consequence: Lergen knows he is a husband/father and bows rather than treating the cost as imaginary. Conditional solidarity begins; not a demonstrated completed operational solution.
  - Target agency: Lergen asks and apologizes; this does not erase formal seniority or the imposed work.
  - Information/misperception: Family concern does not make him abandon institutional effort. Inference ceiling: Do not invent daughter's actual reaction or detailed home routines.

### V01-STUDENT

**Phase:** V01 military-college contemporaries; early fatherhood. **Roles:** Uger — Captain/student and new father; Tanya — Lieutenant/student, publicly a child.

**Authority condition:** Uger explicitly invites a contemporary's reply rather than merely demanding a junior officer answer; rank persists in address. **Audience/setting:** Quiet restaurant, waiter asked away; personal talk in a public venue. **Focalization:** Uger throughp197; Tanya private narrationp198-202.

**Source unit:** `YS-CMR0-V01-031-00107` through `YS-CMR0-V01-031-00202`; 96 normalized blocks. `text/part0029.html`, spine 31. Window SHA256 `fd4296810fdee3393267f69f4e6f84fac7162c258eb4f0b07b3253316af5188f`. The shared EPUB/member identity and hashes are in each episode’s `source`. This window is marked new relative to the earlier 95-diagnostic package.

**Conditional reading:** Uger’s new-father concern encourages a personal contemporary exchange but includes an erroneous piety/childhood assumption. Tanya’s formal self-account and forceful career counsel must stay separate from her later private advantage calculation. Rank-aware address does not cancel the invited classmate footing. Fatherly concern is supported; perfect understanding or a transparent confession is not.

- **Uger → Tanya — `YS-CMR5-REL-V01-STUDENT-A`.** `DIRECT_INTERACTION`. New father seeks personal understanding and offers protection, then confronts a role/childhood mismatch.
  - Private access: Direct family affection, protective discomfort, guilt over unintended status insult and resistance to leaving comrades. Actor-access category: `EXPLICIT_BOUNDED_ACTOR_ACCESS`.
  - Behavior/public speech: Asks the waiter to step aside and speaks directly. Asks enlistment reasons as a contemporary, proposes leaving military work, explains his daughter-related fear.
  - Communicative objective: Understand why a talented child serves and reduce her danger. This remains bounded scene interpretation. Withheld content: Not all uncertainty about her selfhood is publicly stated.
  - Written register: 君 / 同期 / 大尉からの問いかけではなく; frank personal framing with rank-aware response.
  - External reading/consequence: He reads Tanya's orphan/church story as piety and her role adherence as deeply formed identity. He agrees to consider a rear move; later consequences require other source.
  - Target agency: Tanya challenges the implied competence judgment and redirects his family concern into advice for his own future.
  - Information/misperception: His piety/inner-self interpretations are his assumptions, not Tanya's actual private beliefs. Inference ceiling: Fatherly concern is source-grounded; a correct understanding of her motives is not.

- **Tanya → Uger — `YS-CMR5-REL-V01-STUDENT-B`.** `DIRECT_INTERACTION`. Formal autobiographical defense and reciprocal career advice with privately strategic advantage.
  - Private access: At scene end she explicitly recognizes persuasion of an emotionally unguarded competitor as securing her own desired college rank. Actor-access category: `EXPLICIT_BOUNDED_ACTOR_ACCESS`.
  - Behavior/public speech: Congratulates him, presses rear/retirement advice and shares lunch paid by him. Orphan-option explanation, challenge to doubts about qualifications, respectful but forceful family-directed counsel.
  - Communicative objective: Protect role/career and use the other person's concerns persuasively. This remains bounded scene interpretation. Withheld content: The competitive rank motive and satisfaction at the paid meal.
  - Written register: 大尉殿 / 小官 / 同期として / 貴方; polite form carries a strong directive.
  - External reading/consequence: Uger reads her as a tragic child and pious military self, without access to her private calculation. A future rear preference could affect rank competition; this is narrated expectation, not complete later outcome here.
  - Target agency: He initially refuses out of comradeship, then agrees only to consider it.
  - Information/misperception: Uger mistakes a performed/partial account for transparent motive. Inference ceiling: Do not transform the stated orphan background into a full verified confession; helpful later effects need separate evidence.

### V09-HUMAN

**Phase:** V09 reunion between college contemporaries. **Roles:** Tanya — Lieutenant Colonel/frontline commander; Uger — Lieutenant Colonel/logistics staff and father.

**Authority condition:** Same-rank contemporary relation; courtesy persists despite personal critique and gratitude. **Audience/setting:** Restaurant with poor tea and other patrons; political/ethical-personal discussion. **Focalization:** Tanya; Uger self-disclosure/actions and Tanya's interpretation of them.

**Source unit:** `YS-CMR0-V09-017-00567` through `YS-CMR0-V09-017-00703`; 137 normalized blocks. `text/part0015.html`, spine 17. Window SHA256 `801da66c42b2547ef3ccf65440bda39daa38bf5a840ce0c9c90ed848bcbd5128`. The shared EPUB/member identity and hashes are in each episode’s `source`. The source unit has earlier sealed character witnesses.

**Conditional reading:** Professional familiarity permits a frank complaint, admissions of limits and gratitude. Tanya feels offense, hears the explanation and offers reassurance, while receiving gratitude with uncertainty. Uger’s self-claims and Tanya’s appraisal remain separate from independently established capability. The exchange supports affective ambiguity rather than a finished emotional conversion or zero emotion.

- **Uger → Tanya — `YS-CMR5-REL-V09-HUMAN-A`.** `DIRECT_INTERACTION`. Frank criticism, confessed limits and sincere-seeming gratitude coexist.
  - Private access: Unavailable in this directed record. Actor-access category: `NO_DIRECT_ACTOR_PRIVATE_ACCESS_IN_THIS_DIRECTED_RECORD`.
  - Behavior/public speech: Shows anger/distress, corrects unintended insult and bows openly. Asks her to include human emotional time, discloses inability to remain the trained monster, thanks her rear advice and requests less formality.
  - Communicative objective: Correct a harmful tendency while acknowledging a beneficial personal history. This remains bounded scene interpretation. Withheld content: No transparent inner testimony beyond his actual self-disclosure.
  - Written register: 私 / デグレチャフ中佐 / 純然たる苦言 / 人間; personal register still professional.
  - External reading/consequence: Tanya reads his public bow as serious and struggles to understand the self-assessment. Personal gratitude reinforces a right to offer criticism, not a formal therapeutic authority.
  - Target agency: Tanya protests but listens, encourages him and retains formal convention.
  - Information/misperception: His claim she is not personally evil is a character judgment, not the narrative's universal moral verdict. Inference ceiling: Do not independently adjudicate all self-described operational incapacity or invent a cure.

- **Tanya → Uger — `YS-CMR5-REL-V09-HUMAN-B`.** `DIRECT_INTERACTION`. Pleasantly formal contemporary talk becomes defensive surprise, encouragement and uncertain receipt of gratitude.
  - Private access: Direct certainty in necessity, offense at apparent dehumanization, shock at shared-training divergence, and ambiguous bodily/civic response to thanks. Actor-access category: `EXPLICIT_BOUNDED_ACTOR_ACCESS`.
  - Behavior/public speech: Briefly rises in anger, sits after clarification, then responds with courtesy. Defends personhood/duty, urges confidence in him and thanks his goodwill while retaining formal phrasing.
  - Communicative objective: Defend her governing principle while keeping a respected contemporary relationship functional. This remains bounded scene interpretation. Withheld content: Prior-world/BeingX grievance and internal response to gratitude.
  - Written register: 小官 / 中佐殿 / 僭越ながら / ご厚意; she explicitly names formality as her disposition.
  - External reading/consequence: Uger distinguishes criticism from personal attack and asks her to reduce formality. The relation permits frank challenge but does not erase disagreement about emotion.
  - Target agency: He states his own limits and gratitude rather than becoming an echo of her reassurance.
  - Information/misperception: She expects common training to make his stated difficulty impossible, and is wrong about that expectation. Inference ceiling: Her inner emotional ambiguity is not an absence of affect or complete conversion to Uger's view.

### V14-CENSURE

**Phase:** V14 aftermath of emergency forged-order intervention. **Roles:** Lergen — Colonel/staff messenger with limited mandate; Tanya — Lieutenant Colonel/commander.

**Authority condition:** Lergen delivers institutional censure and praise inside a circumscribed authority; operational success does not erase the forgery. **Audience/setting:** Frontline visit and ensuing self-directed remarks after departure. **Focalization:** Lergen throughp118; Tanya thereafter. Claimed appointment date in speech is not certified chronology.

**Source unit:** `YS-CMR0-V14-025-00024` through `YS-CMR0-V14-025-00128`; 105 normalized blocks. `item/xhtml/p-016.xhtml`, spine 25. Window SHA256 `aa363c1087181fa5c1151620962878af3818f2fc82c335b8526091345a2c4904`. The shared EPUB/member identity and hashes are in each episode’s `source`. The source unit has earlier sealed character witnesses.

**Conditional reading:** Institutional censure, personal aversion, shame, praise and gratitude coexist. Tanya’s performed appointment account cannot certify a historical 1927 appointment or promotion; Lergen’s speech does not erase the original forgery. The later shift to Tanya’s private analysis occurs after his departure. Recognition is meaningful yet does not imply frictionless agreement or access to every motive.

- **Lergen → Tanya — `YS-CMR5-REL-V14-CENSURE-A`.** `DIRECT_INTERACTION`. Aversion/uncertainty has become censure mixed with recognition, shame and gratitude.
  - Private access: Direct anxiety over hypocrisy in borrowing her merit while condemning her methods; distress at institutional contradiction. Actor-access category: `EXPLICIT_BOUNDED_ACTOR_ACCESS`.
  - Behavior/public speech: Controls his tone, turns away, bows and thanks her. Names fraudulent means, warns sincerely about erasure/further career harm and then expresses respect.
  - Communicative objective: Carry institutional warning without denying the rescue's value or his indebtedness. This remains bounded scene interpretation. Withheld content: Full self-reproach and doubts behind his initially even mouth.
  - Written register: デグレチャフ中佐 / 貴官 with formal questioning, then すまん / 助かった.
  - External reading/consequence: He reads Tanya's homeland-before-career answer as sacrifice, an attributed motive reading. Reports merit erasure and future visits; no new promotion is established.
  - Target agency: Tanya defends necessity, challenges the premise and offers respectful response.
  - Information/misperception: His sacrifice interpretation is not Tanya's independent private motive. Inference ceiling: Praise does not legalize original forgery; gratitude is not frictionless total understanding.

- **Tanya → Lergen — `YS-CMR5-REL-V14-CENSURE-B`.** `DIRECT_INTERACTION`. Performs a formal institutional account, defends necessity and later notices his reordered authority values.
  - Private access: Only after departure direct reflection reads his Zettour-before-Emperor naming as value change. Actor-access category: `EXPLICIT_BOUNDED_ACTOR_ACCESS`.
  - Behavior/public speech: Responds in formal role, receives praise and watches him leave. Uses claimed appointment/authority as a public account, insists homeland makes career possible and respectfully receives esteem.
  - Communicative objective: Defend action through role/necessity while maintaining a respected senior-facing form. This remains bounded scene interpretation. Withheld content: No direct contemporaneous private confession duringp45-117 is licensed by Lergen focalization.
  - Written register: 小官 / 大佐殿 / であります / 深くお詫び申し上げます; performed account distinct from private truth.
  - External reading/consequence: Lergen reads self-sacrifice and is both grateful and condemnatory. Institutional record treatment remains constrained; her claimed authorization is not original truth.
  - Target agency: Lergen refuses to accept results as sufficient justification, then bows and thanks independently.
  - Information/misperception: She later interprets the messenger's phrasing; that interpretation is not omniscient proof of every allegiance. Inference ceiling: Do not score the asserted1927 appointment as certified historical authority or a promotion.

### V14-ADOPTION

**Phase:** V14 emergency headquarters authority adoption. **Roles:** Zettour — General/senior command; Uger — Colonel/senior adjutant; Grantz — Lieutenant/courier.

**Authority condition:** Overwhelming same-army authority; gentle wording can foreclose factual challenge. **Audience/setting:** Staff office; Grantz witnesses Uger exchange, then is directly questioned. **Focalization:** Grantz; Zettour/Uger actions and speech, no full private cognition.

**Source unit:** `YS-CMR0-V14-017-00346` through `YS-CMR0-V14-017-00452`; 107 normalized blocks. `item/xhtml/p-008.xhtml`, spine 17. Window SHA256 `8c13099b7cdd16c451a6b2736846629ca1a03f1e718c7898c3ffd16e31bbe5c6`. The shared EPUB/member identity and hashes are in each episode’s `source`. The source unit has earlier sealed character witnesses.

**Conditional reading:** The general’s current adoption of orders changes present command authority, not the legality of their original fabrication. Gentle closure and coded regret toward Uger coexist with authority that limits challenge. A friendly chair invitation to Grantz becomes an explicit command to stop speaking. Grantz’s competent report under direct fear is not healed trauma or freely disclosed trust; Uger’s stiff compliance is not private assent.

- **Zettour → Uger — `YS-CMR5-REL-V14-ADOPTION-A`.** `DIRECT_INTERACTION`. Publicly adopts the contested orders and combines closure with coded regret.
  - Private access: Unavailable in this directed record. Actor-access category: `NO_DIRECT_ACTOR_PRIVATE_ACCESS_IN_THIS_DIRECTED_RECORD`.
  - Behavior/public speech: Burns documents, sends a fresh instruction and thanks the adjutant. Declares prior authorship, offers an understated communication-error apology and orders retransmission.
  - Communicative objective: Make the emergency operational direction effective and close public contradiction. This remains bounded scene interpretation. Withheld content: His full private motive is not directly narrated.
  - Written register: ウーガ大佐 / 私 / よいかね / すまん; gentleness remains authority-bearing.
  - External reading/consequence: Grantz sees a terrifying reversal of black to white. His adoption produces current official command effect without proving original legality.
  - Target agency: Uger seeks confirmation and then chooses/formally accepts constrained transmission.
  - Information/misperception: Grantz's fear is the focal witness, not Zettour's inner state. Inference ceiling: No omniscient legal vindication or permission to generalize every gentle speech as benign.

- **Uger → Zettour — `YS-CMR5-REL-V14-ADOPTION-B`.** `DIRECT_INTERACTION`. Formal clarification and visibly strained compliance.
  - Private access: Unavailable in this directed record. Actor-access category: `NO_DIRECT_ACTOR_PRIVATE_ACCESS_IN_THIS_DIRECTED_RECORD`.
  - Behavior/public speech: Delivers the telegram, stiffens his expression, nods and leaves to transmit. Asks if the general truly authorizes it, accepts the communication-error frame and promises own retransmission.
  - Communicative objective: Clarify and carry the superior's current directive. This remains bounded scene interpretation. Withheld content: Actual private belief or wholehearted assent is unavailable.
  - Written register: 閣下 / 小官 / 確実に理解 / 今度こそ; controlled professional compliance.
  - External reading/consequence: Grantz witnesses the strain under polite closure. A new message is formally arranged.
  - Target agency: Zettour closes further confirmation and offers indirect acknowledgment of burden.
  - Information/misperception: The official frame must be respected; it does not prove Uger privately believes original authorship. Inference ceiling: No silent assent-as-belief inference.

- **Zettour → Grantz — `YS-CMR5-REL-V14-ADOPTION-C`.** `DIRECT_INTERACTION`. Friendly invitation and information dependence shift to explicit silence command.
  - Private access: Unavailable in this directed record. Actor-access category: `NO_DIRECT_ACTOR_PRIVATE_ACCESS_IN_THIS_DIRECTED_RECORD`.
  - Behavior/public speech: Offers a chair, questions field capacity and thinks aloud. Acknowledges rear information limits, asks the lieutenant, then becomes blunt when indirection fails.
  - Communicative objective: Gather current field capability and obtain uninterrupted thinking time. This remains bounded scene interpretation. Withheld content: His full strategic reasoning remains unavailable despite audible fragments.
  - Written register: 中尉 / 貴官 / くれたまえ to 命令だ / 黙れ; same relation, changed communicative need.
  - External reading/consequence: Grantz experiences the chair as an electric chair and cannot casually relax. Field information feeds senior planning; next completed plan is beyond this bounded unit.
  - Target agency: Grantz supplies qualified reports and asks a clarification that triggers sharper closure.
  - Information/misperception: He admits rear limits, so not timeless omniscience; Grantz fears intent he cannot fully know. Inference ceiling: No universal genial grandfather or universal shouted commander.

- **Grantz → Zettour — `YS-CMR5-REL-V14-ADOPTION-D`.** `DIRECT_INTERACTION`. Competent reporting under direct private fear and forced silence.
  - Private access: Direct fear, comparison to Tanya's more readable affect, distorted time sense and self-suppression. Actor-access category: `EXPLICIT_BOUNDED_ACTOR_ACCESS`.
  - Behavior/public speech: Sits reluctantly, answers precisely and shuts his mouth after the order. Qualified comparison of field maps/capacity and brief clarification.
  - Communicative objective: Fulfill the courier/officer role without attracting dangerous attention. This remains bounded scene interpretation. Withheld content: Fear, electric-chair image and self-command to be an ornament.
  - Written register: 閣下 / 小官 / 自分 / 対応可能かと; private ヤバイ imagery is not public voice.
  - External reading/consequence: He interprets geniality as frightening authority, not assured warmth. Provides needed field information while receiving no complete strategic account.
  - Target agency: Zettour solicits knowledge but imposes silence when thinking.
  - Information/misperception: He cannot infer the full plan from fragments; questions/time guesses remain uncertain. Inference ceiling: Competent speech does not prove healing or fearless trust.

### V02-ARENE

**Phase:** V02 Arene, new-officer moral crisis. **Roles:** Tanya — Major/battalion commander; Grantz — Second Lieutenant.

**Authority condition:** Extreme same-army coercion; command and bodily force restrict the junior's ability to object. **Audience/setting:** Attack orders with civilians behind mage defenses; afterwards a separate train/reflection frame. **Focalization:** Grantz during the exchange; Tanya in the following private reflectionp663 onward.

**Source unit:** `YS-CMR0-V02-033-00570` through `YS-CMR0-V02-033-00674`; 105 normalized blocks. `item/xhtml/p-026.xhtml`, spine 33. Window SHA256 `3f2227db2367d0488b515f39882a8f5b478959d7b2c6c177674516c1664e91d8`. The shared EPUB/member identity and hashes are in each episode’s `source`. The source unit has earlier sealed character witnesses.

**Conditional reading:** A new officer’s moral objection is constrained by rank, threat framing and bodily compulsion. Grantz’s private conflict is narrated in his segment; the commander’s contemporary private cognition is unavailable in that segment. Tanya’s later private disgust must not be borrowed backward as complete motive. Executed orders do not demonstrate ethical consent, moral legitimacy or psychological recovery.

- **Grantz → Tanya — `YS-CMR5-REL-V02-ARENE-A`.** `DIRECT_INTERACTION`. Moral protest breaks through fear of command authority and is then suppressed.
  - Private access: Direct distress, knowledge of the civilian consequence, fear of insubordination and private resentment. Actor-access category: `EXPLICIT_BOUNDED_ACTOR_ACCESS`.
  - Behavior/public speech: Turns pale, interjects, falls to the ground after a sweep and understands he must comply. Repeated conditional appeal for reconsideration and interrupted objection.
  - Communicative objective: Prevent the known killing consequence while addressing the commander. This remains bounded scene interpretation. Withheld content: Full private curse and conflicted emotion.
  - Written register: 大隊長殿 / 御再考 / repeated もし and incomplete protest.
  - External reading/consequence: He expects the commander to be emotionally indifferent; that is his reading. Protest does not change the order; coerced compliance is not voluntary ethical assent.
  - Target agency: Tanya replies with enemy threat/order arguments and applies force.
  - Information/misperception: Belief that correct military form makes the act acceptable does not resolve his own feeling. Inference ceiling: No invented cowardice, categorical recovery or freely embraced brutality.

- **Tanya → Grantz — `YS-CMR5-REL-V02-ARENE-B`.** `DIRECT_INTERACTION`. Closes moral objection through enemy-threat rationale, authority and physical compulsion.
  - Private access: Unavailable in this directed record. Actor-access category: `NO_DIRECT_ACTOR_PRIVATE_ACCESS_IN_THIS_DIRECTED_RECORD`.
  - Behavior/public speech: Uses a sweep and orders him to take the rifle. Says enemies can shoot again, invokes the order and offers to disregard the objection.
  - Communicative objective: Enforce the assigned attack despite junior resistance. This remains bounded scene interpretation. Withheld content: No direct contemporaneous private explanation for the sweep is given in Grantz focalization.
  - Written register: グランツ少尉 / 命令 / 銃をとりたまえ; command form is not civilian/private baseline.
  - External reading/consequence: Grantz reads calm execution as absence of feeling; source itself questions whether she grasps his conflict. Objection is forcibly closed; military form does not supply a narrator-certified moral verdict.
  - Target agency: Grantz voices a genuine alternative and is coerced, not persuaded into complete agreement.
  - Information/misperception: Adjacent Tanya aftermath contains disgust and resource-oriented distress, countering a globally affectless interpretation. Inference ceiling: Do not claim she knows his precise inner conflict or use command success as moral legitimacy.

### V14-GRATITUDE

**Phase:** V14 final senior/field-command conversation. **Roles:** Zettour — General/senior commander; Tanya — Lieutenant Colonel.

**Authority condition:** Senior can express thanks and still impose work; use of his authority remains bounded, promotions not assured. **Audience/setting:** Personal gratitude, cultural talk and next assignment in a military visit. **Focalization:** Tanya with directly attributed Zettour statements and narrated bodily/emotional cues.

**Source unit:** `YS-CMR0-V14-025-00539` through `YS-CMR0-V14-025-00635`; 97 normalized blocks. `item/xhtml/p-016.xhtml`, spine 25. Window SHA256 `ed3f94a4b6649865951d60dbd9b4f17b966df6442d9333700e6751c87865719a`. The shared EPUB/member identity and hashes are in each episode’s `source`. The source unit has earlier sealed character witnesses.

**Conditional reading:** Senior authority allows personal thanks, bodily fatigue and a cultural picture-book aspiration while still imposing work. Tanya’s criticism, qualified respect, reluctance and relief at credible future employment are simultaneous evidence. Promised work or authorship is not realized employment, a completed book or guaranteed promotion. Disclosure is partial; neither total devotion nor mere opportunism explains away the competing motives.

- **Zettour → Tanya — `YS-CMR5-REL-V14-GRATITUDE-A`.** `DIRECT_INTERACTION`. Personal gratitude, cultural desire and continuing institutional demand coexist.
  - Private access: Unavailable in this directed record. Actor-access category: `NO_DIRECT_ACTOR_PRIVATE_ACCESS_IN_THIS_DIRECTED_RECORD`.
  - Behavior/public speech: Bows repeatedly, shows fatigue, offers bounded authority and returns her salute with moist eyes. Admits strategic surprise, thanks her as a person, speaks of picture-book aspiration, apologizes before work demands and promises postwar work.
  - Communicative objective: Acknowledge indebtedness and mobilize an essential field commander for the remaining task. This remains bounded scene interpretation. Withheld content: Full private motive is not transparently available despite sincerely framed statements.
  - Written register: 私 / 貴官 / 貴様 / 中佐; gratitude and familiar irony retain senior authority.
  - External reading/consequence: Tanya reads the task/assignment as responsibility and future safety. A new western assignment and bounded name/authority offer; not a completed postwar job or promotion.
  - Target agency: She challenges religious framing, qualifies the apparent rescue and questions eastern versus western use.
  - Information/misperception: Tanya's relief/escape interpretation does not certify his entire intended future. Inference ceiling: No frictionless benefactor or fulfilled peaceful authorship from stated aspirations.

- **Tanya → Zettour — `YS-CMR5-REL-V14-GRATITUDE-B`.** `DIRECT_INTERACTION`. Familiar critique and qualified respect turn into explicit relief at credible future work.
  - Private access: Direct distaste for more work, performed employee readiness, hope from a western posting and pride/relief at recognition. Actor-access category: `EXPLICIT_BOUNDED_ACTOR_ACCESS`.
  - Behavior/public speech: Salutes, responds dutifully and departs. Rejects gospel language, points out deferred collapse, engages cultural talk and eagerly accepts the postwar-work statement.
  - Communicative objective: Keep the relationship functional and secure a personally viable future. This remains bounded scene interpretation. Withheld content: Private employee reluctance and interpretation of future employment as safety.
  - Written register: 閣下 / 小官 / 何なりと / 光栄です; private corporate vocabulary does not become spoken confession.
  - External reading/consequence: Zettour shows gratitude and responds to her resistance/cultural idea. Receives a prospective assignment and promise, not secured later outcome.
  - Target agency: He acknowledges surprise, grants only bounded authority and refuses promotion guarantees.
  - Information/misperception: She interprets the superior's sacrifice/assignment; this is her appraisal, not omniscient policy assurance. Inference ceiling: Meaningful trust and self-preservation coexist; do not flatten into devotion or mere opportunism.

### V14-DUTY

**Phase:** V14 dangerous operation commitment discussion. **Roles:** Tanya — Lieutenant Colonel; Visha — Lieutenant/adjutant; Weiss — Major/deputy.

**Authority condition:** Hierarchical proposal with repeatedly offered reconsideration; unpunished refusal is Weiss's confident inference, not a universal policy proof. **Audience/setting:** Coffee/chocolate pause before a grave operation; three-person command-group audience. **Focalization:** Weiss until later transition; source-described Tanya care is partly his reading.

**Source unit:** `YS-CMR0-V14-021-00105` through `YS-CMR0-V14-021-00211`; 107 normalized blocks. `item/xhtml/p-012.xhtml`, spine 21. Window SHA256 `f0cded6497abca24ddae070826b007dfbfe55b6224cf7247efcd31c2e3f56f45`. The shared EPUB/member identity and hashes are in each episode’s `source`. The source unit has earlier sealed character witnesses.

**Conditional reading:** Repeated offers to reconsider a dangerous assignment coexist with longstanding command bonds. Visha states an earlier choice and finds renewed questioning puzzling; Weiss reads the questions as care and confidently believes refusal could be unpunished. Those are bounded access claims, not a universal policy or a revision of semi-compulsory initial induction. The familiar group joke recognizes absent Lergen; it creates two partial appraisals, not reciprocal live relations. Coffee and chocolate are scene objects, not established favorites.

- **Tanya → Visha — `YS-CMR5-REL-V14-DUTY-A`.** `DIRECT_INTERACTION`. Repeatedly asks whether a longstanding adjutant chooses a dangerous commitment.
  - Private access: Unavailable in this directed record. Actor-access category: `NO_DIRECT_ACTOR_PRIVATE_ACCESS_IN_THIS_DIRECTED_RECORD`.
  - Behavior/public speech: Looks toward her and asks again despite an earlier confirmation. Invites free expression and reconsideration without promising survival.
  - Communicative objective: Check commitment before accepting a grave shared task. This remains bounded scene interpretation. Withheld content: No transparent Tanya private intention during Weiss focalization.
  - Written register: 貴官 / セレブリャコーフ中尉 / 好きに言いたまえ.
  - External reading/consequence: Weiss interprets the repeated question as awkward care and reluctance to draw her into danger. Choice is confirmed in conversation; danger remains.
  - Target agency: Visha provides her own declared long-standing choice and a familiar joke.
  - Information/misperception: Her answer treats the renewed question as belated rather than necessary reassurance. Inference ceiling: Do not treat courtesy as complete voluntariness across her whole military history.

- **Visha → Tanya — `YS-CMR5-REL-V14-DUTY-B`.** `DIRECT_INTERACTION`. Stated prior choice makes renewed consent-check puzzling; familiar levity remains rank-aware.
  - Private access: Unavailable in this directed record. Actor-access category: `NO_DIRECT_ACTOR_PRIVATE_ACCESS_IN_THIS_DIRECTED_RECORD`.
  - Behavior/public speech: Continues the coffee/chocolate pause and laughs with the group. Says the Rhine decision was long made, questions why she is asked again and names a normal-person exception.
  - Communicative objective: Clarify that commitment is already hers in this relation. This remains bounded scene interpretation. Withheld content: Actual private current motive is not directly narrated here.
  - Written register: 中佐殿 / 自分 / 申し上げた / 今更だなぁ; familiarity is selective.
  - External reading/consequence: Weiss reads long partnership and the commander's awkward human relation-building. Affirms this task commitment.
  - Target agency: Tanya asks repeatedly and is surprised; a statement of choice is not retroactive proof of every prior consent.
  - Information/misperception: Early semi-compulsory recruitment remains a different developmental condition. Inference ceiling: No generic worship, automatic all-context volunteering or favorite chocolate inference.

- **Weiss → Tanya — `YS-CMR5-REL-V14-DUTY-C`.** `DIRECT_INTERACTION`. Freely stated duty and affectionate recognition of the commander's limits.
  - Private access: Direct confidence he could decline, warmth, humor and recognition that even the apparently perfect younger superior is human. Actor-access category: `EXPLICIT_BOUNDED_ACTOR_ACCESS`.
  - Behavior/public speech: Shrugs, laughs, shapes a sober face and accepts the written order. Declares long-settled resolve and agrees with Visha's joke.
  - Communicative objective: Affirm chosen commitment while relieving awkwardness. This remains bounded scene interpretation. Withheld content: The alternate birds-of-a-feather quip is consciously withheld.
  - Written register: 失礼ですが / 中佐殿 / 決め切っております; withheld private quip is not his spoken line.
  - External reading/consequence: He reads Tanya's questions as care; this is not an omniscient motive account. He accepts the command in this state.
  - Target agency: Tanya asks rather than immediately demanding and permits the familiar exchange.
  - Information/misperception: His inference of an available final escape is strong for him, not a proof for every soldier. Inference ceiling: No unconditional warmth or consent inference outside the specified relation/state.

- **Visha → Lergen — `YS-CMR5-REL-V14-DUTY-D`.** `SPOKEN_APPRAISAL_OF_ABSENT_OTHER`. Public familiar-group appraisal of an absent senior as the normal exception.
  - Private access: Unavailable in this directed record. Actor-access category: `NO_DIRECT_ACTOR_PRIVATE_ACCESS_IN_THIS_DIRECTED_RECORD`.
  - Behavior/public speech: Smiles and supplies the joke. Calls Lergen the sensible exception to surrounding warmongers.
  - Communicative objective: Answer Tanya's complaint through a relationship-network joke.  This remains bounded scene interpretation. Withheld content: Not independently recorded.
  - Written register: レルゲン大佐殿 / 常識人; respectful third-person appraisal.
  - External reading/consequence: Weiss openly agrees. Group levity precedes the mission order.
  - Target agency: Lergen is absent and has no recorded reply/agency in this unit.
  - Information/misperception: This is Visha's appraisal, not neutral proof of Lergen's entire character. Inference ceiling: Supports one directed recognition stance, not a live Visha/Lergen conversational model.

- **Weiss → Lergen — `YS-CMR5-REL-V14-DUTY-E`.** `SPOKEN_APPRAISAL_OF_ABSENT_OTHER`. Public assent endorses an absent senior as the sensible exception.
  - Private access: Direct recognition of the joke and desire to relieve awkwardness; not Lergen's interior. Actor-access category: `EXPLICIT_BOUNDED_ACTOR_ACCESS`.
  - Behavior/public speech: Claps in agreement and laughs with the group. Uses a respectful third-person description to agree with Visha.
  - Communicative objective: Support a familiar-group joke without addressing Lergen directly. This remains bounded scene interpretation. Withheld content: His alternative quip remains private.
  - Written register: あの方 / 真っ当 / いらっしゃる; respectful absent-senior appraisal, not direct casual address.
  - External reading/consequence: Visha originated the exception and Tanya shares the laughter. Group levity accompanies a dangerous mission discussion.
  - Target agency: Lergen is absent; reciprocal stance is not supplied.
  - Information/misperception: Their appraisal does not prove a neutral all-context baseline for Lergen. Inference ceiling: Partial recognition cell only, not a live Weiss/Lergen exchange.

### V11-RUPTURE

**Phase:** 10 September1927; Zettour Eastern HQ office. **Roles:** Zettour — General/war-resources authority; Rudersdorf — Rudersdorf/senior staff friend.

**Authority condition:** Longstanding peer intimacy does not erase distinct office duties or the resource conflict. **Audience/setting:** Private discussion of backup plan and possible Ildoa attack. **Focalization:** Zettour; Rudersdorf dialogue/self-description and observable confusion.

**Source unit:** `YS-CMR0-V11-012-00001` through `YS-CMR0-V11-012-00061`; 61 normalized blocks. `OEBPS/Text/part0010.xhtml`, spine 12. Window SHA256 `805485d3ac01aa82f9cb506f3cb477f80652e4b8f2e9cd133ad34ebc51d57e73`. The shared EPUB/member identity and hashes are in each episode’s `source`. The source unit has earlier sealed character witnesses.

**Conditional reading:** Peer intimacy sharpens rather than dissolves conflict over resources, prediction, sacrifice and homeland duty. Zettour’s shaking, hope and anguish are directly available; Rudersdorf’s obligation and private/military distinction are self-statements interpreted by his friend. Familiar address and the spouse/affair metaphor are professional intimacy evidence, not a domestic case. Neither later death nor reconciliation is certified in this unit.

- **Zettour → Rudersdorf — `YS-CMR5-REL-V11-RUPTURE-A`.** `DIRECT_INTERACTION`. Friendship intensifies duty-driven rejection of the friend's wishful plan.
  - Private access: Direct tremor, hope, disappointment, shame over losses and distinction between Reich survival and Heimat future. Actor-access category: `EXPLICIT_BOUNDED_ACTOR_ACCESS`.
  - Behavior/public speech: Masks shaking calm, scrutinizes the friend and momentarily softens at familiar address. Sharp questions, wish-versus-prediction challenge and intimate metaphorical rebuke.
  - Communicative objective: Force a real capability/resource account rather than a must-based wish. This remains bounded scene interpretation. Withheld content: Full anguish over condemning a friend.
  - Written register: 貴様 / 我俺 / named address and mock title; not generic subordinate register.
  - External reading/consequence: He reads Rudersdorf's position as desperate unwillingness to lose all. Conflict persists; later death/resolution are not established by this window.
  - Target agency: Rudersdorf acknowledges error/debt and still defends obligation, then invites frankness.
  - Information/misperception: His characterization of the friend's heart is focal appraisal, not fully narrated Rudersdorf cognition. Inference ceiling: Spouse/affair metaphor does not supply a domestic case or prove complete shared values.

- **Rudersdorf → Zettour — `YS-CMR5-REL-V11-RUPTURE-B`.** `DIRECT_INTERACTION`. Affirmed obligation and sacrifice debt resist a friend's capability objection.
  - Private access: Unavailable in this directed record. Actor-access category: `NO_DIRECT_ACTOR_PRIVATE_ACCESS_IN_THIS_DIRECTED_RECORD`.
  - Behavior/public speech: Shows confusion at the opening challenge and later invites frank talk. Defines avoidance as what must occur, cites lives lost, states separation of private/military self and insists duty.
  - Communicative objective: Avoid imminent collapse while preserving faith in sacrificed lives. This remains bounded scene interpretation. Withheld content: Full private cognition is not independently narrated.
  - Written register: ゼートゥーア / 我俺 and obligation framing; peer intimacy differs from staff-command diction.
  - External reading/consequence: Zettour reads necessity becoming wishfulness and feels despair. No accepted common course is demonstrated here.
  - Target agency: Zettour challenges him as a friend, not merely a rank subordinate; the emotional bond persists amid conflict.
  - Information/misperception: His private/military distinction is a self-claim; Zettour's opposing interpretation remains another channel. Inference ceiling: Do not use his statements as a universal verified psychology or erase earlier practical restraint.

### V10-STAFF

**Phase:** V10 same-day report after Conrad meeting. **Roles:** Lergen — Colonel/staff; Rudersdorf — Lieutenant General/operations senior.

**Authority condition:** Same-army superior authorizes a subordinate's diplomatic coordination and access to a specialist; fatigue does not erase command. **Audience/setting:** Staff deputy office; time-pressure/metaphorical negotiation. **Focalization:** Lergen; Rudersdorf's explicit speech and visible exhaustion.

**Source unit:** `YS-CMR0-V10-014-00166` through `YS-CMR0-V10-014-00217`; 52 normalized blocks. `OEBPS/Text/part0012.xhtml`, spine 14. Window SHA256 `f7b74af67e391adbf46a47def9bfaa8d25c82902a04a00bca66b9b49da355afd`. The shared EPUB/member identity and hashes are in each episode’s `source`. This window is marked new relative to the earlier 95-diagnostic package.

**Conditional reading:** Fatigue changes a superior’s delivery but leaves actual office authority intact. Lergen knowingly coats a limited diplomatic prospect with hope and requests Uger’s help. Rudersdorf tests feasibility and timing, then authorizes coordination/resources. The apparent relief is observed, not a verified private conversion; concrete help also prevents an escalation-only caricature.

- **Lergen → Rudersdorf — `YS-CMR5-REL-V10-STAFF-A`.** `DIRECT_INTERACTION`. Sober professional optimism is consciously made persuasive under a depleted superior.
  - Private access: Direct recognition of Rudersdorf's altered energy, shared burden and intentionally hope-coated diplomatic prospect. Actor-access category: `EXPLICIT_BOUNDED_ACTOR_ACCESS`.
  - Behavior/public speech: Reports, maintains even tone and asks to borrow Uger. Frames a tolerable end as victory, answers the agricultural metaphor and requests concrete authority.
  - Communicative objective: Keep diplomacy viable and obtain time/specialist resources. This remains bounded scene interpretation. Withheld content: The gap between bitter limited ceasefire and the hopeful presentation.
  - Written register: 閣下 / 小官 / 勝利であります / ご命令とあれば; respectful pushback and metaphor use.
  - External reading/consequence: Rudersdorf pressures deadline feasibility but listens and grants resources. Coordination with Conrad and Uger is authorized; no achieved negotiation result.
  - Target agency: Rudersdorf challenges the premise and condition, then authorizes needed help.
  - Information/misperception: Lergen reads fatigue/changed voice from long service; not direct access to all Rudersdorf motive. Inference ceiling: This is a new52-block fit window; no QA-reserve overlap and no blanket private-life claim.

- **Rudersdorf → Lergen — `YS-CMR5-REL-V10-STAFF-B`.** `DIRECT_INTERACTION`. Deadline skepticism and tired irony coexist with concrete diplomatic support.
  - Private access: Unavailable in this directed record. Actor-access category: `NO_DIRECT_ACTOR_PRIVATE_ACCESS_IN_THIS_DIRECTED_RECORD`.
  - Behavior/public speech: Appears depleted but upright, questions and later seems relieved. Challenges hopeful forecasts, uses harvest/time metaphor, orders close civilian coordination and grants authority/help.
  - Communicative objective: Demand a feasible timely route while supporting the best available effort. This remains bounded scene interpretation. Withheld content: Independent private Rudersdorf thought remains unavailable.
  - Written register: 大佐 / 貴官, irony/metaphor and 頼むぞ / 好きにやれ.
  - External reading/consequence: Lergen compares this delivery to the former louder energetic superior. Lergen receives permission to borrow Uger and pursue diplomacy.
  - Target agency: Lergen argues for a different victory framing rather than merely echoing the general.
  - Information/misperception: Hope is repeatedly conditional; observing apparent relief is not proof of a private conversion. Inference ceiling: No timeless escalation-only model or inference that negotiation is now guaranteed.

### V11-MEMOIR

**Phase:** Written retrospective unpublished memoir; narration recounts later-war events. **Roles:** Lergen — Former Imperial soldier/written memoir author; Zettour — Remembered senior commander.

**Authority condition:** No live command exchange; author frames responsibility to later readers. **Audience/setting:** Unpublished written account, not neutral interview transcript or face-to-face speech. **Focalization:** Explicit Lergen authored first-person memoir; claims about Zettour stay testimony.

**Source unit:** `YS-CMR0-V11-014-00001` through `YS-CMR0-V11-014-00045`; 45 normalized blocks. `OEBPS/Text/part0012.xhtml`, spine 14. Window SHA256 `a462ad5bba080d7658c9150c84e0a8b23bfe381fcb669cf4c5fbb6f7954813ba`. The shared EPUB/member identity and hashes are in each episode’s `source`. The source unit has earlier sealed character witnesses.

**Conditional reading:** Lergen addresses later readers through retrospective written self-presentation. He admits shame, failure and consequential silence while defending remembered Zettour intent. This is one partial directed testimony with no live target agency or reverse response. Authorship certainty is distinct from truth of every remembered motive or causal account.

- **Lergen → Zettour — `YS-CMR5-REL-V11-MEMOIR-A`.** `WRITTEN_RETROSPECTIVE_APPRAISAL_OF_ABSENT_OTHER`. Retrospectively defends a superior's intent while admitting failure, shame and meaningful silence.
  - Private access: Explicit authored self-presentation, not contemporaneous independent interiority. Actor-access category: `WRITTEN_SELF_PRESENTATION_ONLY`.
  - Behavior/public speech: Writes an account that directs readers to omission as well as what is said. No live public speech; written argument/testimony instead.
  - Communicative objective: Preserve a responsibility account and defend Zettour's intended duty. This remains bounded scene interpretation. Withheld content: He explicitly warns readers to attend to silence.
  - Written register: Written 私, qualified concession, self-shame and explanatory defense; not casual voice.
  - External reading/consequence: He protests popular army-dominance interpretation while admitting exceptional institutional fusion. Creates contested memory testimony; no independent adjudication of every motive.
  - Target agency: Zettour is absent; no reciprocal response shown.
  - Information/misperception: His assertion that Zettour never intended dictatorship is testimony, not omniscient truth. Inference ceiling: Retrospective professional respect supports a partial directed cell, not a live dyad model.

### V06-DIPLOMACY

**Phase:** V06 Ildoan reception/mediation offer. **Roles:** Lergen — Imperial Colonel; Calandro — Ildoan Colonel/Gassman's special envoy.

**Authority condition:** Foreign peers; each represents a state. No shared-command obedience follows from rank. **Audience/setting:** Hosted coffee/reception and diplomatic probe. **Focalization:** Lergen; Calandro direct speech/actions, no transparent private cognition.

**Source unit:** `YS-CMR0-V06-025-00012` through `YS-CMR0-V06-025-00086`; 75 normalized blocks. `OEBPS/Text/part0023.xhtml`, spine 25. Window SHA256 `cd5aa1797e8daacd342921ec9c972c9b857ff9e4aa29c5f5195bbc57a8e34d4b`. The shared EPUB/member identity and hashes are in each episode’s `source`. The source unit has earlier sealed character witnesses.

**Conditional reading:** Foreign peers have state mandates rather than a shared chain of command. Calandro’s hospitality, qualified apology and agenda control are persuasive acts; Lergen’s courtesy masks surprise, embarrassment and institutional uncertainty. The envoy’s friendly neutrality is a diplomatic claim, not certified impartiality. A personal lack of acceptance authority is real; no accepted treaty follows from the meeting.

- **Calandro → Lergen — `YS-CMR5-REL-V06-DIPLOMACY-A`.** `DIRECT_INTERACTION`. Polished hospitality secures initiative for a serious peace offer.
  - Private access: Unavailable in this directed record. Actor-access category: `NO_DIRECT_ACTOR_PRIVATE_ACCESS_IN_THIS_DIRECTED_RECORD`.
  - Behavior/public speech: Chooses a handshake, serves scarce luxuries, smiles and interrupts the attempted objection. Announces envoy status, qualified apology and neutral-mediator proposal, then tests the counterpart's stated authority limit.
  - Communicative objective: Open a state negotiation and keep its agenda moving. This remains bounded scene interpretation. Withheld content: Full private calculation is not directly narrated.
  - Written register: 小官 / ご気分 / ご提案 / 貴官; polite force differs from staff subordination.
  - External reading/consequence: Lergen experiences courtesy as tactically dangerous and his silence exposes surprise. A mediation offer is made; no treaty acceptance follows in the window.
  - Target agency: Lergen counters, declines personal decision authority and begins reassessing the envoy.
  - Information/misperception: Claims of friendly neutrality/benefit remain diplomatic positions. Inference ceiling: No presumed moral impartiality, generic charm or command over a foreign colonel.

- **Lergen → Calandro — `YS-CMR5-REL-V06-DIPLOMACY-B`.** `DIRECT_INTERACTION`. Courtesy/reciprocal irony gives way to surprise, a constrained answer and recovery.
  - Private access: Direct uncertainty about intelligence work, agenda loss, silence, experience limits and resumed analysis. Actor-access category: `EXPLICIT_BOUNDED_ACTOR_ACCESS`.
  - Behavior/public speech: Smiles, drinks/receives hospitality and reinspects uniform cues. Replies with irony, probes the offer and invokes national decision authority.
  - Communicative objective: Represent the state without disclosing vulnerability or pretending mandate he lacks. This remains bounded scene interpretation. Withheld content: His embarrassment, uncertainty and assessment of institutional strain.
  - Written register: カランドロ大佐殿 / 失礼ですが / ご説; foreign-peer politeness can carry resistance.
  - External reading/consequence: Calandro points out his known access to senior generals. He cannot personally accept the state offer.
  - Target agency: Calandro deliberately brings the offer rather than waiting for the guest's initiative.
  - Information/misperception: Uniform/hand/experience conclusions are his inferences, not a complete identity dossier. Inference ceiling: Public restraint is not evidence of no anxiety or of actual acceptance.

### V10-CONRAD

**Phase:** 26 July1927; Imperial General Staff. **Roles:** Lergen — Colonel/staff; Conrad — Civilian Foreign Ministry counsellor.

**Authority condition:** Different institutional functions; civilian counterpart is not a military subordinate. **Audience/setting:** First coordination meeting, handshake, critique and cigar hospitality. **Focalization:** Lergen; Conrad direct speech, narrated anger and self-claims.

**Source unit:** `YS-CMR0-V10-014-00001` through `YS-CMR0-V10-014-00165`; 165 normalized blocks. `OEBPS/Text/part0012.xhtml`, spine 14. Window SHA256 `449fed7fc7aba8063cb9a49209dbb9373dd466340dda29228ffaba8cd662d965`. The shared EPUB/member identity and hashes are in each episode’s `source`. The source unit has earlier sealed character witnesses.

**Conditional reading:** A civilian counterpart independently criticizes military explanatory habits and admits his own institution’s faults. Lergen initially defends professional legitimacy, then repairs communication and collaborates while preserving private backup-plan anxiety. The handshake and cigar hospitality do not make Conrad a military subordinate. Political subtext remains uncertain; no favorite cigar, actual habitual theft or completed peace is inferred.

- **Lergen → Conrad — `YS-CMR5-REL-V10-CONRAD-A`.** `DIRECT_INTERACTION`. Institutional self-defense gives way to explanation repair, guarded cooperation and uncertainty about political subtext.
  - Private access: Direct handshake discomfort, unintended prejudice restrained, recognition of communication error, political limits and backup-plan anxiety. Actor-access category: `EXPLICIT_BOUNDED_ACTOR_ACCESS`.
  - Behavior/public speech: Lowers a begun salute into handshake, accepts cigar and later offers cooperation. Challenges unfair disrespect/critique, admits selective-audience habits and agrees to coordination.
  - Communicative objective: Make a viable diplomatic exit while defending professional legitimacy. This remains bounded scene interpretation. Withheld content: Backup-plan fear and uncertainty over joke/subtext.
  - Written register: 参事官殿 / 私 / ご批判 / お恥ずかしながら; softened admission after defensive argument.
  - External reading/consequence: Conrad locates the missing explanatory work and asks practical collaboration. A joint work relationship begins; successful peace is not established.
  - Target agency: Conrad critiques and proposes rather than obeying military assumptions.
  - Information/misperception: The diplomat's cigar joke could be joke or truth; Lergen does not know. Inference ceiling: No claim of complete political skill or access to Conrad's private motives.

- **Conrad → Lergen — `YS-CMR5-REL-V10-CONRAD-B`.** `DIRECT_INTERACTION`. Direct institutional criticism, teaching pressure and professional hospitality open cooperation.
  - Private access: Unavailable in this directed record. Actor-access category: `NO_DIRECT_ACTOR_PRIVATE_ACCESS_IN_THIS_DIRECTED_RECORD`.
  - Behavior/public speech: Arrives punctually, shakes hands, makes visible anger/irony and shares cigars. Names both institutions' blame, makes explanation concrete, admits own side's fault and proposes immediate work.
  - Communicative objective: Get usable explanation and a common political/diplomatic effort. This remains bounded scene interpretation. Withheld content: Exact private joke motive and all inner beliefs remain unavailable.
  - Written register: 貴下/貴官 / 大佐, blunt teacher-like challenge, then hospitable irony.
  - External reading/consequence: Lergen initially sees disrespect, then recognizes the case applies to his own habits. Coordination is agreed; authority is not transferred to a military commander.
  - Target agency: Lergen pushes back, admits a fault and then voluntarily collaborates.
  - Information/misperception: A claim of willingness/relief is not independent proof of every political intention. Inference ceiling: No inferred favorite cigar, habitual theft or broad domestic conversational baseline.

### V06-GASSMAN

**Phase:** V06 Ildoan staff mediation. **Roles:** Gassman — General; Calandro — Colonel/staff intelligence officer.

**Authority condition:** Own-army general/colonel hierarchy; politically sensitive staff exchange. **Audience/setting:** Evidence report, cigar and loaded political aside. **Focalization:** Gassman; Calandro explicit reports and selected silence.

**Source unit:** `YS-CMR0-V06-021-00013` through `YS-CMR0-V06-021-00045`; 33 normalized blocks. `OEBPS/Text/part0019.xhtml`, spine 21. Window SHA256 `aa9d25f1784714180a7940a1a337d81174e5a2f665e2af85c234f020f03cdb4f`. The shared EPUB/member identity and hashes are in each episode’s `source`. The source unit has earlier sealed character witnesses.

**Conditional reading:** Own-army hierarchy permits evidence questions but makes political assent costly. Gassman directly calculates bounded national advantage, probes silence and chooses to move on without settling it. Calandro reports confidently yet withholds an explicit loaded political commitment. The missing private position remains unknown; no cross-window unverified voice forms, pure pacifism or endless profiteering is imported.

- **Gassman → Calandro — `YS-CMR5-REL-V06-GASSMAN-A`.** `DIRECT_INTERACTION`. Interested mediation includes evidentiary questioning and sensitivity to a non-answer.
  - Private access: Direct profit calculation, restraint on further gain and noticing silence without resolving it. Actor-access category: `EXPLICIT_BOUNDED_ACTOR_ACCESS`.
  - Behavior/public speech: Reaches for cigar and redirects work. Asks for confirmation/evidence, makes a loaded domestic-politics remark and returns to task.
  - Communicative objective: Validate reports and secure a bounded state advantage. This remains bounded scene interpretation. Withheld content: Interest calculation and uncertainty about the silent response.
  - Written register: 我々 / 大佐 with evidence questions; no unverified forms from another window.
  - External reading/consequence: Calandro avoids explicit political assent. Peace mediation remains a work project; no concluded agreement shown.
  - Target agency: Calandro supplies evidence and controls his own explicit political commitment.
  - Information/misperception: Silence can mean more than one thing; he declines to settle it. Inference ceiling: No pure-pacifist or endless-profiteer model from the ironic narration.

- **Calandro → Gassman — `YS-CMR5-REL-V06-GASSMAN-B`.** `DIRECT_INTERACTION`. Confident limited report and politically disciplined non-answer.
  - Private access: Unavailable in this directed record. Actor-access category: `NO_DIRECT_ACTOR_PRIVATE_ACCESS_IN_THIS_DIRECTED_RECORD`.
  - Behavior/public speech: Reports, then naturally moves his gaze to the clock. Answers requested evidence and a limited comparison, then chooses silence at the loaded claim.
  - Communicative objective: Fulfill information duty without adopting an unnecessary political assertion. This remains bounded scene interpretation. Withheld content: No independently available private opinion behind silence.
  - Written register: 閣下 / でしょう; politeness includes selective silence.
  - External reading/consequence: Gassman notices he neither confirms nor denies. A potentially compromising commitment is not publicly made.
  - Target agency: Gassman probes but ultimately changes subject.
  - Information/misperception: Observer interpretation cannot replace the withheld position. Inference ceiling: No inferred agreement, universal evasiveness or transparent intelligence omniscience.

### V07-GASSMAN

**Phase:** V07 settlement negotiation. **Roles:** Gassman — Ildoan General/mediator; Lergen — Imperial Colonel/mandated negotiator.

**Authority condition:** Foreign-state bargaining licenses resistance to a higher foreign rank. **Audience/setting:** Negotiating priorities/terms under national mandate. **Focalization:** Lergen with Gassman's speech and narrated public fatigue.

**Source unit:** `YS-CMR0-V07-021-00021` through `YS-CMR0-V07-021-00047`; 27 normalized blocks. `OEBPS/Text/part0019.xhtml`, spine 21. Window SHA256 `54b8e134a2745e24fe96bbf03e1c83f0feb335170bb1db6254e9975b76718043`. The shared EPUB/member identity and hashes are in each episode’s `source`. The source unit has earlier sealed character witnesses.

**Conditional reading:** The foreign general’s greater rank does not require a colonel to abandon his state mandate. Gassman’s precise criticism concedes losses while pressing a settlement; Lergen politely resists and argues security needs. Fatigue and smiles are visible cues rather than transparent motive. No agreed terms or neutral benevolence are established.

- **Gassman → Lergen — `YS-CMR5-REL-V07-GASSMAN-A`.** `DIRECT_INTERACTION`. Friendly-looking critique is precise, conceded in part and visibly tired.
  - Private access: Unavailable in this directed record. Actor-access category: `NO_DIRECT_ACTOR_PRIVATE_ACCESS_IN_THIS_DIRECTED_RECORD`.
  - Behavior/public speech: Smiles, sighs and presses the terms. Challenges priority and excessive demands while recognizing real Imperial losses and Federation aggression.
  - Communicative objective: Test whether the proposed offer can actually mediate peace. This remains bounded scene interpretation. Withheld content: Full private national calculation is not independently narrated in this window.
  - Written register: 貴官 / 大佐 / いいかね; seniority does not become shared-army command.
  - External reading/consequence: Lergen experiences the pressure as representing another state's interests. No accepted settlement terms are established.
  - Target agency: Lergen challenges his rationale and preserves his own national mandate.
  - Information/misperception: Claimed objectivity is bargaining posture, not certified impartiality. Inference ceiling: No assumption that smiles mean benevolent intent or fatigue means surrender.

- **Lergen → Gassman — `YS-CMR5-REL-V07-GASSMAN-B`.** `DIRECT_INTERACTION`. Respectful foreign-peer resistance obeys national duty rather than rank alone.
  - Private access: Direct suspicion, desire to read the other state's intent and recognition of mandate. Actor-access category: `EXPLICIT_BOUNDED_ACTOR_ACCESS`.
  - Behavior/public speech: Nods, resists and accepts the tacit bargaining license. Conditionally offers withdrawal, challenges negotiation priority and defends minimal-security claims.
  - Communicative objective: Represent required security space without prematurely conceding it. This remains bounded scene interpretation. Withheld content: Full contempt/assessment of demands is not said in every word.
  - Written register: 閣下 / 失礼な反問 / 道理 / かと存じます.
  - External reading/consequence: Both tacitly permit a colonel to resist a foreign general. Imperial mandate remains constrained; no freely chosen treaty change.
  - Target agency: Gassman grants losses yet criticizes the offer independently.
  - Information/misperception: Different state interests coexist with professed mediation. Inference ceiling: Neither insubordination within his own army nor an equal-free agent unconstrained by home instructions.

### V10-ROMEL

**Phase:** V10 western posting/backup-plan ambiguity. **Roles:** Romel — Lieutenant General/field commander; Rudersdorf — Lieutenant General/operations senior.

**Authority condition:** Peer-grade officers with different offices; allocation and hidden state planning constrain field needs. **Audience/setting:** Staff meeting over Tanya's delayed allocation. **Focalization:** Romel; Rudersdorf explicit dialogue, no complete private intent.

**Source unit:** `YS-CMR0-V10-016-00054` through `YS-CMR0-V10-016-00097`; 44 normalized blocks. `OEBPS/Text/part0014.xhtml`, spine 16. Window SHA256 `adb4119a80e0db670ed453cb3117e0e4e427099f83effbf890c15173b25e40c5`. The shared EPUB/member identity and hashes are in each episode’s `source`. The source unit has earlier sealed character witnesses.

**Conditional reading:** Peer-grade officers hold different offices and information. Romel seeks actual force, probes delay and hopes the overworked Tanya receives rest; he reads a coded limit on further inquiry. Rudersdorf conveys allocation while withholding complete courier/backup-plan meaning. Nominal leave is neither an observed vacation nor proof of pure benevolence; resource promises and delivered force remain distinct.

- **Romel → Rudersdorf — `YS-CMR5-REL-V10-ROMEL-A`.** `DIRECT_INTERACTION`. Practical demand for actual reinforcement reveals distrust of paper promises and concern for an overworked officer.
  - Private access: Direct preference for delivered force, uncertainty about the backup plan, inference about a courier mission and hope Tanya has genuine rest. Actor-access category: `EXPLICIT_BOUNDED_ACTOR_ACCESS`.
  - Behavior/public speech: Questions the delay, accepts an indirect limit and departs with unease. Thanks for allocation, challenges the leave explanation and accepts a coded reply.
  - Communicative objective: Secure operational resources while reading enough institutional context to do his job. This remains bounded scene interpretation. Withheld content: Cynicism about paper reinforcements and pity for the overworked field officer.
  - Written register: 閣下 / 理由をお伺い / 失礼ですが; direct peer probing within office constraints.
  - External reading/consequence: He reads Rudersdorf's closing line as don't ask further. Assignment remains delayed; actual leave or reinforcements are not delivered here.
  - Target agency: Rudersdorf withholds sensitive meaning and still confirms the western task.
  - Information/misperception: The courier/backup-plan connection is his inference, not a disclosed complete plan. Inference ceiling: No favorite leisure, literal finance or fully known political intention.

- **Rudersdorf → Romel — `YS-CMR5-REL-V10-ROMEL-B`.** `DIRECT_INTERACTION`. Conveys a real allocation delay through ironic leave/courier framing and closes deeper inquiry.
  - Private access: Unavailable in this directed record. Actor-access category: `NO_DIRECT_ACTOR_PRIVATE_ACCESS_IN_THIS_DIRECTED_RECORD`.
  - Behavior/public speech: Meets punctually, gives a slight amused gesture and returns to task. Explains delayed arrival, invokes leave plus eastern courier work and uses a parent-like rest pretext.
  - Communicative objective: Manage resources and sensitive routing while retaining field cooperation. This remains bounded scene interpretation. Withheld content: Full courier/backup-plan motive is not independently narrated.
  - Written register: 貴官 / すまん / 違うかね and coded reassurance.
  - External reading/consequence: Romel infers the hidden strategic significance and stops asking. Western task is confirmed without full political disclosure.
  - Target agency: Romel probes and then accepts the boundary independently.
  - Information/misperception: Apparent leave concern may carry political concealment; neither pure benevolence nor a complete lie is certified. Inference ceiling: No claim that the nominal holiday is an actually observed vacation.

### V04-WARNING

**Phase:** V04 early combat briefing in Allied home-air defence. **Roles:** Drake — United Kingdom Lieutenant Colonel/liaison; Mary — Second Lieutenant in the Allied volunteer formation.

**Authority condition:** Foreign liaison in a joint briefing; expertise licenses warning, not unqualified shared-chain command. **Audience/setting:** Volunteer officers and their colonel attend a threat briefing. **Focalization:** Mary novice anxiety and comprehension are narrated; Drake known through spoken warning and action.

**Source unit:** `YS-CMR0-V04-029-00038` through `YS-CMR0-V04-029-00063`; 26 normalized blocks. `OEBPS/Text/part0027.xhtml`, spine 29. Window SHA256 `84f3e4325a6384659dbdbbcb835f93cdfe7d1b181fbf840616739ab00c13f69c`. The shared EPUB/member identity and hashes are in each episode’s `source`. The source unit has earlier sealed character witnesses.

**Conditional reading:** An Allied briefing precedes Mary’s later explicitly British-command dispute. Drake’s threat expertise supports severe survival guidance under friendly-territory recovery conditions; Mary asks an anxious practical question and learns the mechanism. His full private appraisal is unavailable. Early novice comprehension does not certify future obedience or a timeless stubbornness.

- **Drake → Mary — `YS-CMR5-REL-V04-WARNING-A`.** `DIRECT_INTERACTION`. Serious warning gives a junior officer a concrete survival instruction.
  - Private access: Unavailable in this directed record. Actor-access category: `NO_DIRECT_ACTOR_PRIVATE_ACCESS_IN_THIS_DIRECTED_RECORD`.
  - Behavior/public speech: Takes the briefing floor and explains the apparently shocking short answer. Invites the question, praises it and specifies survival by falling over friendly territory when escape fails.
  - Communicative objective: Correct underestimation of a named threat and preserve an officer for another battle. This remains bounded scene interpretation. Withheld content: His complete private appraisal of Mary is unavailable.
  - Written register: 貴官 / 少尉 / たまえ; severe imperative followed by practical explanation.
  - External reading/consequence: Mary initially hesitates, then understands the friendly-recovery mechanism. A joint-defence survival instruction is conveyed; no actual later recovery is shown.
  - Target agency: Mary asks an independent practical question instead of merely receiving generic inspiration.
  - Information/misperception: The imperative to fall is conditional on home defence and available friendly recovery. Inference ceiling: Neither universal retreat advice nor immediate membership of Mary in Drake's own army is established here.

- **Mary → Drake — `YS-CMR5-REL-V04-WARNING-B`.** `DIRECT_INTERACTION`. An anxious novice asks for usable guidance and revises her understanding.
  - Private access: Directly narrated realization of her own nervous heartbeat and later comprehension of the explanation. Actor-access category: `EXPLICIT_BOUNDED_ACTOR_ACCESS`.
  - Behavior/public speech: Requests the floor, identifies herself and listens through initial surprise. Asks respectfully what they should do if escape is impossible.
  - Communicative objective: Find a workable response to an acknowledged combat danger. This remains bounded scene interpretation. Withheld content: The entire emotional background of the question is not spoken.
  - Written register: 中佐殿 / 質問を宜しいでしょうか / であります / 私たち.
  - External reading/consequence: Drake calls the question good and supplies a mechanism. She acquires conditional survival knowledge; future obedience is not shown.
  - Target agency: Drake independently clarifies rather than demanding unquestioning enthusiasm.
  - Information/misperception: Her initial surprise is not refusal or proof that she fully grasps every tactical threat. Inference ceiling: Early second-lieutenant learning is not a timeless stubbornness or a complete later-state ethical model.

### V06-PRISONERS

**Phase:** V06 Christmas dispute over transferred captives. **Roles:** Drake — United Kingdom Lieutenant Colonel; Mary — Lieutenant explicitly holding United Kingdom military membership.

**Authority condition:** Own-army command, military-law obligations and foreign political surveillance constrain speech. **Audience/setting:** A room Drake believes is likely bugged; he wants conversation moved outdoors. **Focalization:** Drake interior; Mary direct speech, hesitation and visibly dissatisfied departure, no independent Mary interior.

**Source unit:** `YS-CMR0-V06-019-00262` through `YS-CMR0-V06-019-00335`; 74 normalized blocks. `OEBPS/Text/part0017.xhtml`, spine 19. Window SHA256 `bcd8c072a0b704db277f28f13e82814157e484442a7ba674cdeae01e430e2dc0`. The shared EPUB/member identity and hashes are in each episode’s `source`. The source unit has earlier sealed character witnesses.

**Conditional reading:** The later lieutenant is explicitly subject to Drake’s own military/legal authority. His direct conscience about guaranteed captives, anger and expected surveillance motivate partial public explanation and refusal of unauthorized transfer. Mary voices a rival apparent-humanitarian rationale but has no independent private monologue here. Her account of Liliya is reported speech; surveillance is Drake’s strong expectation. The officers disagree over what the prisoner issue means, and statutory assurances do not certify humane treatment.

- **Drake → Mary — `YS-CMR5-REL-V06-PRISONERS-A`.** `DIRECT_INTERACTION`. Humanitarian alarm becomes anger, legally constrained public correction and selective political explanation.
  - Private access: Direct conscience about British-guaranteed captives, respect for Mikel, anger, political caution and deliberately partial disclosure. Actor-access category: `EXPLICIT_BOUNDED_ACTOR_ACCESS`.
  - Behavior/public speech: Attempts to move the encounter outdoors, loses patience, restrains more dangerous candid speech and terminates the exchange. Invokes military duty and lack of transfer authority, orders her to stop and offers a political pretext explicitly true but incomplete.
  - Communicative objective: Protect guaranteed captives and avoid surveillance-triggered diplomatic harm while correcting an officer. This remains bounded scene interpretation. Withheld content: Party-prison fears, complete humanitarian rationale and risk to his respected ally Mikel.
  - Written register: 私 / 貴官 / 中尉 / かね / たまえ, sarcasm and clipped legal commands under surveillance.
  - External reading/consequence: Mary hears trophy-seeking where his private reason concerns captive protection. Improper transfer precedent is refused; a prior staged quarrel recovered custody, not a neutral diplomatic success.
  - Target agency: Mary presses a rival rationale rather than automatically accepting rank.
  - Information/misperception: Mary mistakes protected prisoners for trophies; the room's surveillance is his strong expectation, not an independently shown recording. Inference ceiling: Hostility in this case neither excludes humanitarian motivation nor licenses a habitual cruelty or actual prescription-drug routine.

- **Mary → Drake — `YS-CMR5-REL-V06-PRISONERS-B`.** `DIRECT_INTERACTION`. Persistent apparent-humanitarian objection resists her superior's unstated political understanding.
  - Private access: Unavailable in this directed record. Actor-access category: `NO_DIRECT_ACTOR_PRIVATE_ACCESS_IN_THIS_DIRECTED_RECORD`.
  - Behavior/public speech: Insists the matter is urgent, hesitates, then continues despite attempts to change location and close the discussion. Cites abolished execution, proximity to home, Christmas relief and a good precedent, then challenges his insistence on prisoners.
  - Communicative objective: Obtain an explanation and press the stated prisoner-welfare argument. This remains bounded scene interpretation. Withheld content: No independent private Mary monologue is supplied in this exchange.
  - Written register: 中佐殿 / お時間を / お願いいたします / ですが; respectful forms coexist with persistent accusation.
  - External reading/consequence: Drake sees dangerous failure to read the room and an insufficient distinction between a statute and the Party prison system. Her transfer is directly censured; her claim about Federation punishment is not narrator-certified humane treatment.
  - Target agency: Drake refuses the premise, identifies command/legal limits and withholds some reasons.
  - Information/misperception: Liliya's assurance is reported by Mary, not direct Liliya speech; Drake's private political purpose is unavailable to her. Inference ceiling: Do not import Drake's judgments as Mary's self-description, or project this failed exchange onto all later development.

### V02-FATHER

**Phase:** 10 December1924; family evacuation before an Entente sortie. **Roles:** Anson — Entente Colonel/father; Mary — Daughter before her later military role.

**Authority condition:** Family relationship rather than command; war and privileged evacuation access limit options. **Audience/setting:** Wife and daughter at a departure; civilian family intimacy. **Focalization:** Anson private regret and affection; Mary's direct speech and visible laughter only.

**Source unit:** `YS-CMR0-V02-023-00015` through `YS-CMR0-V02-023-00031`; 17 normalized blocks. `item/xhtml/p-016.xhtml`, spine 23. Window SHA256 `54ee81f7cca6465ad339a3502c0cc3de75b4e0b77d08bbbe9d71a46e369644dc`. The shared EPUB/member identity and hashes are in each episode’s `source`. The source unit has earlier sealed character witnesses.

**Conditional reading:** A father/daughter farewell uses civilian family intimacy, not military command. Anson’s love, home-time regret and evacuation privilege guilt are direct; Mary’s supportive speech and grooming joke are observed. His request to deserve future pride is aspiration, not vindication of later conduct. No exact age, later reunion, complete domestic routine or adult lieutenant interior is supplied.

- **Anson → Mary — `YS-CMR5-REL-V02-FATHER-A`.** `DIRECT_INTERACTION`. Duty-limited parting includes protection, regret and a wish to deserve his daughter's pride.
  - Private access: Direct regret for neglected home time, gratitude and guilt about privileged evacuation, love and uncertainty about being a good father. Actor-access category: `EXPLICIT_BOUNDED_ACTOR_ACCESS`.
  - Behavior/public speech: Holds his wife, crouches to meet his daughter's eyes, forces a smile and embraces her. Asks Mary to help her mother and take care, apologizes that work prevents accompanying them, and asks for future pride.
  - Communicative objective: Provide care and a bearable farewell under a genuine duty constraint. This remains bounded scene interpretation. Withheld content: Much of his guilt, home regret and self-questioning.
  - Written register: お母さん / すまんな / んだぞ / 思ってくれ; family imperative and apology differ from officer briefing.
  - External reading/consequence: Mary answers affectionately and teases him about his beard. Family evacuation becomes possible for this family; he must remain for the sortie.
  - Target agency: Mary supplies a spontaneous supportive correction and ordinary grooming joke.
  - Information/misperception: A request for future pride is not proof that his military conduct will deserve it. Inference ceiling: No invented later reunion, favorite domestic routine, or claim that this farewell gives direct access to Mary's adult cognition.

- **Mary → Anson — `YS-CMR5-REL-V02-FATHER-B`.** `DIRECT_INTERACTION`. Daughter's affectionate question and reassurance introduce ordinary intimacy within departure.
  - Private access: Unavailable in this directed record. Actor-access category: `NO_DIRECT_ACTOR_PRIVATE_ACCESS_IN_THIS_DIRECTED_RECORD`.
  - Behavior/public speech: Responds to his farewell and laughs when embraced. Asks why he cannot come, calls him a good father and asks him to shave.
  - Communicative objective: Seek accompaniment and reassure her father in the exchange. This remains bounded scene interpretation. Withheld content: Her independent private appraisal and complete awareness of the war are unavailable.
  - Written register: お父さん / だよ / お髭は剃って; intimate daughter register.
  - External reading/consequence: Anson sees an endearing child and embraces her. No policy or command consequence; the family is being separated by war.
  - Target agency: Anson answers the work constraint and speaks his own self-doubt.
  - Information/misperception: Exact age is not established by this excerpt; later lieutenant register must not be back-projected. Inference ceiling: A grooming joke is not a hobby, adult military judgment or permanently uncomplicated father idealization.

### V09-UNIFORM

**Phase:** V09 garrison rest after eastern field service. **Roles:** Meybert — Artillery Captain; Tospan — Infantry Lieutenant/remaining-unit commander.

**Authority condition:** Senior/junior colleagues permit respectful correction; port garrison rules conflict with field habits. **Audience/setting:** Ordinary uniform complaint and reciprocal professional talk without Tanya present. **Focalization:** Tospan initial discomfort; explicit shift to Meybert's rule intentions and reflections; speech must not collapse the two.

**Source unit:** `YS-CMR0-V09-031-00185` through `YS-CMR0-V09-031-00247`; 63 normalized blocks. `text/part0029.html`, spine 31. Window SHA256 `350cf8c9fdf60d5360c201b7cf968766021674ae4ff2167aa9194a65eab5c1b9`. The shared EPUB/member identity and hashes are in each episode’s `source`. The source unit has earlier sealed character witnesses.

**Conditional reading:** Garrison conditions expose conflict between intended regulations and acquired field habit. Tospan’s cautious cap correction produces Meybert’s embarrassed admission and self-critique. Their focalization shifts must remain segmented. Their accounts of Tanya’s patriotism are observer interpretations; collegial repair does not create an unrestricted correction right or expand recognition-scale Tospan into a full model.

- **Tospan → Meybert — `YS-CMR5-REL-V09-UNIFORM-A`.** `DIRECT_INTERACTION`. Courteous correction makes a senior officer recognize his own rule lapse.
  - Private access: Limited narrated discomfort with a crisp uniform; later bounded spoken self-assessment, not Meybert's interior. Actor-access category: `EXPLICIT_BOUNDED_ACTOR_ACCESS`.
  - Behavior/public speech: Glances at his own uniform and the captain's cap, shrugs and cautiously points out the rule. Complains about formal rest clothing, challenges the cap inconsistency respectfully and qualifies his own limits in the later exchange.
  - Communicative objective: Seek usable rest and consistency while maintaining a colleague's face. This remains bounded scene interpretation. Withheld content: No entire private resentment or theory of Tanya is transparently stated.
  - Written register: 大尉殿 / 失礼ですが / ご指摘 / 自分には; caution and role-aware qualification.
  - External reading/consequence: Meybert admits field habits have changed him. A cap-rule lapse is acknowledged; garrison culture remains awkward.
  - Target agency: Meybert responds with admission and self-critique rather than punishment.
  - Information/misperception: Their comments about Tanya's patriotism are observer interpretations, not Tanya's own motive. Inference ceiling: No borrowed Meybert doctrine, general confidence, romantic intimacy or fully reconstructible off-duty life.

- **Meybert → Tospan — `YS-CMR5-REL-V09-UNIFORM-B`.** `DIRECT_INTERACTION`. Rule assertion changes into embarrassed admission and collegial discussion of field influence.
  - Private access: Direct intention to follow rules strictly, recognition of his drift and feeling of garrison estrangement. Actor-access category: `EXPLICIT_BOUNDED_ACTOR_ACCESS`.
  - Behavior/public speech: Touches his cap, smiles ruefully and talks through the conflict. Initially enforces regulations, then acknowledges lapse and discusses their commander's influence.
  - Communicative objective: Preserve rules and workable collegial understanding after an exposed inconsistency. This remains bounded scene interpretation. Withheld content: Some discomfort and unspoken assumptions about the commander.
  - Written register: 私 / 中尉 / 規則だ followed by admitted uncertainty and reflective peer conversation.
  - External reading/consequence: Tospan can identify the contradiction without antagonism. Strict intended conformity is revised by a concrete correction; broader policy is not changed.
  - Target agency: Tospan observes the cap, challenges it and adds a different qualified self-assessment.
  - Information/misperception: His patriotism explanation for Tanya remains an interpretation, not source-certified private Tanya belief. Inference ceiling: Not an inflexible artillery caricature; no conclusion that all rules are abandoned or every subordinate may correct him without limits.

### V14-HQ-RELIEF

**Phase:** V14 eastern headquarters airborne emergency. **Roles:** Tanya — Lieutenant Colonel/mobile mage commander; Meybert — Artillery Captain/remaining-unit officer.

**Authority condition:** Superior/subordinate emergency command; physical distance imposes a real assistance limit. **Audience/setting:** Urgent radio call while Tanya is deep behind enemy lines. **Focalization:** Tanya interior and decision; Meybert direct voice/report, no direct Meybert private monologue.

**Source unit:** `YS-CMR0-V14-017-00610` through `YS-CMR0-V14-017-00650`; 41 normalized blocks. `item/xhtml/p-008.xhtml`, spine 17. Window SHA256 `7de22ade4e4e55114f3ee584c0290f211f49a6fca9ba0fe6a84a684d0d988ac6`. The shared EPUB/member identity and hashes are in each episode’s `source`. The source unit has earlier sealed character witnesses.

**Conditional reading:** Tanya intentionally welcomes bad news to protect truthful reporting, but the attempt does not calm an unusually alarmed Meybert. Physical distance forces a candid assistance limit and a severe all-unit relief order. Meybert states unknowns and asks practical clarification. Care for reports coexists with potentially terrible sacrifice; neither infinite rescue, normal-state panic nor a completed outcome is inferred.

- **Tanya → Meybert — `YS-CMR5-REL-V14-HQ-RELIEF-A`.** `DIRECT_INTERACTION`. A consciously welcoming response to bad news changes into a severe all-unit rescue order.
  - Private access: Direct concern about punishing bad reports, shock, HQ priority, recognition of time/distance and military cost. Actor-access category: `EXPLICIT_BOUNDED_ACTOR_ACCESS`.
  - Behavior/public speech: Answers slowly to calm him, absorbs failure of that attempt and immediately reallocates the entire available unit. Asks for information, orders headquarters relief even at total battlegroup loss, and refuses to promise timely mage support.
  - Communicative objective: Get enough facts and prevent worse institutional collapse under a geographic constraint. This remains bounded scene interpretation. Withheld content: Her private enemy-cost hypothesis, nausea/escape-from-reality reflection and initial uncertainty.
  - Written register: なんだね / 貴官 / たまえ; calming cadence changes to 明言しておく and clipped commands.
  - External reading/consequence: Meybert remains alarmed and presses the garrison and assistance questions. All available personnel may be risked to preserve institutional command capacity; outcome is outside this window.
  - Target agency: Meybert asks practical clarification rather than mechanically accepting an underspecified order.
  - Information/misperception: Her Federation-cost interpretation remains a hypothesis; no offered response can erase travel time. Inference ceiling: Neither always successful reassurance nor limitless rescue capacity; care for truthful reports can coexist with a terrible order.

- **Meybert → Tanya — `YS-CMR5-REL-V14-HQ-RELIEF-B`.** `DIRECT_INTERACTION`. An experienced officer in an abnormal shock reports limits and demands concrete assistance.
  - Private access: Unavailable in this directed record. Actor-access category: `NO_DIRECT_ACTOR_PRIVATE_ACCESS_IN_THIS_DIRECTED_RECORD`.
  - Behavior/public speech: Calls urgently, repeats the threat and begins the ordered relief. States what is unknown, asks about leaving the base, confirms the sacrifice condition and requests mage return.
  - Communicative objective: Report a critical emergency accurately and clarify available means before execution. This remains bounded scene interpretation. Withheld content: Private reasoning beyond the report and the narrated sound of distress is unavailable.
  - Written register: 中佐殿 / 全てが不明です / できますか; stammered onset is crisis-specific, not a timeless voice tic.
  - External reading/consequence: Tanya treats the panic as unusual for him and recognizes the force of the assistance request. The relief task begins; battlefield result is not yet established.
  - Target agency: Tanya answers the sacrifice question and discloses the time constraint without a comforting false promise.
  - Information/misperception: Honest unknowns are not fabricated knowledge or general artillery incompetence. Inference ceiling: No hidden panic monologue, universal fragility or completed rescue inferred from this call.

### V01-DORMITORY

**Phase:** V01 before the first operational postings. **Roles:** Visha — Cadet-school graduate/junior replacement; Erya — Peer graduate/observation-team posting.

**Authority condition:** Close female peers without a rank barrier; constrained military induction and uncertain assignment. **Audience/setting:** Dormitory wake-up and shared mess meal before separation. **Focalization:** Visha explicit first person; Erya actions and direct speech filtered through her friend.

**Source unit:** `YS-CMR0-V01-023-00180` through `YS-CMR0-V01-023-00224`; 45 normalized blocks. `text/part0021.html`, spine 23. Window SHA256 `a7880f383515b5d4a4b8f5650b531f234c0537349f2c0227b7d68e4a20203873`. The shared EPUB/member identity and hashes are in each episode’s `source`. The source unit has earlier sealed character witnesses.

**Conditional reading:** Early peers exchange sleepy banter, assignment uncertainty, food, safety concern and teasing without rank barriers. Visha’s warmth and night-chat preference coexist with body comparison, exile history, envy and relief; Erya’s mind remains unavailable. Information secrecy and rear-area tea are playful claims, not covert profession or favorite drink. This early friendship does not erase constrained induction or license romance.

- **Visha → Erya — `YS-CMR5-REL-V01-DORMITORY-A`.** `DIRECT_INTERACTION`. Affection and mild envy permit banter, information skepticism and concern for a friend's safety.
  - Private access: Direct warm-bed and night-chat preference, body comparison, gratitude, exile memories and relief mixed with envy at her friend's safer posting. Actor-access category: `EXPLICIT_BOUNDED_ACTOR_ACCESS`.
  - Behavior/public speech: Wakes reluctantly, eats with her friend, reacts visibly to news and notices her missing caramel. Asks skeptical assignment questions, jokingly calls her a ninja and warns against complacency.
  - Communicative objective: Enjoy ordinary companionship and obtain useful posting information while expressing care. This remains bounded scene interpretation. Withheld content: Her mixed envy/relief and broader coerced-induction/private identity reflection.
  - Written register: 貴女 / わ / かしら with familiar エーリャ; different from formal adjutant replies.
  - External reading/consequence: Erya teases her changing facial reactions and answers the posting question. Impending assignment may separate them; outcome of Erya's later posting is not shown.
  - Target agency: Erya has her own information, timing, teasing and food-taking acts.
  - Information/misperception: She is unsure about the intelligence source; a joke about secret information does not establish covert profession. Inference ceiling: No romance, timeless ideal patriotism or broad inference about adult domestic preferences.

- **Erya → Visha — `YS-CMR5-REL-V01-DORMITORY-B`.** `DIRECT_INTERACTION`. Practical care and playful information control enliven a peer farewell morning.
  - Private access: Unavailable in this directed record. Actor-access category: `NO_DIRECT_ACTOR_PRIVATE_ACCESS_IN_THIS_DIRECTED_RECORD`.
  - Behavior/public speech: Wakes Visha, reports overheard staffing news, laughs quietly, urges timely eating and takes a caramel. Teases with exaggerated secrecy, qualifies the posting news and jokes that she will drink tea behind the lines.
  - Communicative objective: Share useful news and sustain familiar play within a shared meal. This remains bounded scene interpretation. Withheld content: No independent private Erya appraisal or guaranteed explanation of her information habits.
  - Written register: 私 / 君 / だよ / もん / ね / よ; the playful セレブリャコーフ君 is her address, not Visha's pronoun baseline.
  - External reading/consequence: Visha regards her as a capable considerate friend and mischievous companion, with envy and relief. A specific observation posting is reported; later survival or career is not known here.
  - Target agency: Visha challenges the information, warns about danger and protests the caramel loss.
  - Information/misperception: Tea is a boast/joke about rear-area safety, not an attested favorite drink. Inference ceiling: Recognition-scale early peer evidence cannot certify a full independent psychology or later military voice.

### V01-TECHNICAL

**Phase:** V01 early Type95 performance test before explicit faith claim. **Roles:** Tanya — Mage Second Lieutenant/chief test officer; Schugel — Chief engineer/technical project authority.

**Authority condition:** Different specialties and constrained test assignment; technical authority and operator experience conflict. **Audience/setting:** Radio exchange between airborne tester and control aircraft. **Focalization:** Tanya private technical/safety assessment; Schugel direct speech and observable radio conduct.

**Source unit:** `YS-CMR0-V01-019-00073` through `YS-CMR0-V01-019-00107`; 35 normalized blocks. `text/part0017.html`, spine 19. Window SHA256 `0f3bb0ade68dc27d2796c3515cca2546f1a3411e7088eea41ac6c062ddaac6c2`. The shared EPUB/member identity and hashes are in each episode’s `source`. The source unit has earlier sealed character witnesses.

**Conditional reading:** Technical and operator authority conflict before Schugel’s explicit new-faith claim. Schugel defends performance and the masterpiece, while Tanya’s private fear/hostility coexists with real appreciation of engineering. Her spoken technical protest withholds harsher management appraisal. Assignment/secrecy limit withdrawal; no clinical diagnosis, safety guarantee or redesigned device follows.

- **Schugel → Tanya — `YS-CMR5-REL-V01-TECHNICAL-A`.** `DIRECT_INTERACTION`. Defends theoretical performance and responds angrily to operator criticism.
  - Private access: Unavailable in this directed record. Actor-access category: `NO_DIRECT_ACTOR_PRIVATE_ACCESS_IN_THIS_DIRECTED_RECORD`.
  - Behavior/public speech: Pushes the altitude test and raises his voice over radio. Invokes available power/loads, calls the device his masterpiece and demands withdrawal of the defect judgment.
  - Communicative objective: Continue testing and defend the project's technical design. This remains bounded scene interpretation. Withheld content: Private motives beyond the observed defense of his work are unavailable.
  - Written register: 私 / 君 / 少尉 / かね / たまえ; argumentative technical authority.
  - External reading/consequence: Tanya respects technical achievement but reads a dangerous mismatch between specialist skill and management. Tester remains assigned and cannot simply discard a secret prototype.
  - Target agency: Tanya argues reliability and human operating limits from direct experience.
  - Information/misperception: Tanya's MAD labels are her hostile perspective, not a neutral diagnosis. Inference ceiling: No divine-confidence register imported before its later explicit claim, and no certainty that performance theory equals safe use.

- **Tanya → Schugel — `YS-CMR5-REL-V01-TECHNICAL-B`.** `DIRECT_INTERACTION`. Private hostility and respect for genuine engineering coexist with formal practical criticism.
  - Private access: Direct fear, fatigue, angry control-aircraft impulse restrained, appreciation of miniaturization and frustration with management. Actor-access category: `EXPLICIT_BOUNDED_ACTOR_ACCESS`.
  - Behavior/public speech: Continues dangerous testing while making repeated operator objections. Requests redundancy/usability, rejects an impractical altitude demand and asks him to lower his radio voice.
  - Communicative objective: Improve practical safety without provoking a worse assignment or confidentiality problem. This remains bounded scene interpretation. Withheld content: Hostile fantasy and detailed corporate-management judgment are not her spoken greeting.
  - Written register: ドクトル / いただきたい / ください with escalating technical protest.
  - External reading/consequence: Schugel receives criticism as an attack on his optimized masterpiece. Prototype secrecy and assignment limit withdrawal; no device redesign results here.
  - Target agency: Schugel defends a competing technical standard and refuses the demanded practical adjustment.
  - Information/misperception: Her hostile labels must remain separate from verified engineering facts and clinical claims. Inference ceiling: No all-purpose irreverent monologue spoken aloud or claim that she finds engineering intrinsically worthless.

### V01-FAITH-TEST

**Phase:** V01 threatened project termination and Schugel's new explicit revelation claim. **Roles:** Tanya — Second Lieutenant/chief test officer; Schugel — Chief engineer/claimed command over test task.

**Authority condition:** Project/command coercion limits a test officer's refusal; Schugel shares the immediate physical exposure. **Audience/setting:** Isolated live test with distant staff and medical preparation. **Focalization:** Tanya direct interior and actions; Schugel spoken belief and visible confidence, no independent inner verification.

**Source unit:** `YS-CMR0-V01-021-00186` through `YS-CMR0-V01-021-00253`; 68 normalized blocks. `text/part0019.html`, spine 21. Window SHA256 `07ceb925fc0804179124fc2140e032241eade03c3b6c19fe2b44cbd09f52e9a1`. The shared EPUB/member identity and hashes are in each episode’s `source`. The source unit has earlier sealed character witnesses.

**Conditional reading:** The threatened project’s later explicit revelation claim changes the verbal justification for coercive continuation. Schugel shares immediate bodily exposure, so he is not simply risking others from safety; the claimed guarantee remains a claim. Tanya attempts professional refusal and covert self-protection, yet has no demonstrated free exit. Safety non-response is directly experienced; deliberate disabling is her inference. Joint-prayer proposals do not establish voluntary belief or consent.

- **Schugel → Tanya — `YS-CMR5-REL-V01-FAITH-TEST-A`.** `DIRECT_INTERACTION`. New proclaimed revelation supplies confidence, demands cooperation and coerces continuation.
  - Private access: Unavailable in this directed record. Actor-access category: `NO_DIRECT_ACTOR_PRIVATE_ACCESS_IN_THIS_DIRECTED_RECORD`.
  - Behavior/public speech: Stands beside the tester in the dangerous area while remote staff retreat; smiles reassuringly and gestures expansively. Admits shared risk, invokes command after a professional objection, identifies himself as newly devout and proposes joint prayer.
  - Communicative objective: Complete the threatened project through asserted faith-backed cooperation. This remains bounded scene interpretation. Withheld content: No direct interior verifies exactly why he believes the claimed revelation.
  - Written register: 私 / 君 / 少尉 / たまえ; new 天啓 / 信徒 vocabulary is chronology-specific.
  - External reading/consequence: Tanya experiences the reassurance as threatening and suspects safety overrides. Testing continues under a stated order; the later outcome is outside this bounded window.
  - Target agency: Tanya tries professional objection, covert safety activation and continued questioning.
  - Information/misperception: His claimed guarantee is a claim; Tanya's inference that he disabled safeguards is not independently shown here. Inference ceiling: Shared bodily exposure counters a pure other-people's-risk caricature; no objective miracle proof or medically certified insanity.

- **Tanya → Schugel — `YS-CMR5-REL-V01-FAITH-TEST-B`.** `DIRECT_INTERACTION`. Ritual courtesy and a professional boundary conceal intense fear, hostility and attempted self-protection.
  - Private access: Direct delight at expected cancellation, horror at the last risky test, prior-life management analogy and safety-failure inference. Actor-access category: `EXPLICIT_BOUNDED_ACTOR_ACCESS`.
  - Behavior/public speech: Objects, restrains candid insults, slowly feeds power and attempts safety activation without publicly announcing the action. Politely asks cancellation, distinguishes soldier from scientist and questions his claimed new faith.
  - Communicative objective: Avoid the test or minimize lethal risk without inflaming the project authority. This remains bounded scene interpretation. Withheld content: Her wish he would stop endangering her and her covert safety effort.
  - Written register: ドクトル / 正直に申しまして / であります / 貴方; surface courtesy mediates much harsher private appraisal.
  - External reading/consequence: Schugel converts her professional identity into a command-obedience argument. A real refusal option is not shown; failed safety activation leaves a technical dilemma.
  - Target agency: Schugel affirms his own presence and persists rather than merely misunderstanding an unclear request.
  - Information/misperception: Safety non-response is directly experienced; the responsible engineer's deliberate disabling remains her inference. Inference ceiling: No voluntary prayer agreement, transparent certainty about device tampering, or conclusion about all later dealings.

### V06-PARTY-CHIEF

**Phase:** V06 Federation Party conference about suppressed intelligence and resistance. **Roles:** Loria — Internal-affairs senior/Party official; Josef (role context) — Party Secretary-General identified by unique role context, not named in this window.

**Authority condition:** Loria has coercive power over some colleagues, but immediately straightens for the sole superior addressed as Secretary-General. **Audience/setting:** Party conference with other officials; question/response should not be reassigned from unnamed participants. **Focalization:** Loria interior; chief's direct speech is role-identified rather than personal-name explicit.

**Source unit:** `YS-CMR0-V06-019-00059` through `YS-CMR0-V06-019-00109`; 51 normalized blocks. `OEBPS/Text/part0017.xhtml`, spine 19. Window SHA256 `52dc192cce33ec49b387bdaf87e5d894561266c444e86775e1021149330bf8be`. The shared EPUB/member identity and hashes are in each episode’s `source`. The source unit has earlier sealed character witnesses.

**Conditional reading:** Political power over colleagues reverses into immediate deference before the uniquely role-identified Secretary-General. Loria suppresses mockery and a fuller critique of unwelcome-news filtering while offering national-affect analysis. The chief redirects coercive showmanship toward causal questions but has no private cognition available. Josef’s identity is high role context without a personal-name token; unnamed Party-member turns remain unassigned.

- **Loria → Josef (role context) — `YS-CMR5-REL-V06-PARTY-CHIEF-A`.** `DIRECT_INTERACTION_ROLE_IDENTIFIED_NOT_NAMED`. Immediate deference masks contempt and supplies a politically qualified explanation.
  - Private access: Direct enjoyment of coercing other officials, withheld ridicule, recognition of bad-news suppression and analysis of nationalist affect. Actor-access category: `EXPLICIT_BOUNDED_ACTOR_ACCESS`.
  - Behavior/public speech: Instantly straightens, suppresses a rueful smile and raises a hand before speaking. Confirms the chief's information question and explains the emotional national cause rather than merely Party loyalty.
  - Communicative objective: Give a useful explanation while preserving standing before the one superior who can command him. This remains bounded scene interpretation. Withheld content: Mockery of colleagues and the full critique of suppressed unwelcome reports.
  - Written register: 同志書記長 / 仰る通り / よろしいでしょうか; deferential teaching contrasts with suave threat to other officials.
  - External reading/consequence: The chief interrupts his threat-play and asks why nominal concessions fail. The senior's inquiry constrains the meeting; institutional truthfulness remains politically costly.
  - Target agency: The Secretary-General independently redirects from punitive showmanship to an information problem.
  - Information/misperception: Questions at p105 belong only to an unnamed Party member; they must not be made Josef's line. Inference ceiling: Exact personal identity is high-confidence role context, not an explicit name; no neutral proof that every reported concession or result is true.

- **Josef (role context) → Loria — `YS-CMR5-REL-V06-PARTY-CHIEF-B`.** `DIRECT_INTERACTION_ROLE_IDENTIFIED_NOT_NAMED`. A supreme Party interlocutor stops threatened field assignment and asks for a causal account.
  - Private access: Unavailable in this directed record. Actor-access category: `NO_DIRECT_ACTOR_PRIVATE_ACCESS_IN_THIS_DIRECTED_RECORD`.
  - Behavior/public speech: Interrupts the exchange and receives immediate posture change/deference. Questions disrupted information, known hostility and why concessions fail to secure loyalty.
  - Communicative objective: Clarify the cause of unexpectedly strong rejection and intelligence failure. This remains bounded scene interpretation. Withheld content: Independent private motive and broader emotional life are unavailable.
  - Written register: 同志ロリヤ / 我々 / たまえ; only explicitly role-supported utterances, no textbook-satire fingerprint imported.
  - External reading/consequence: Loria recognizes only one person requires this immediate response and privately critiques the chief's bad-news aversion. Loria's threatened dispatch of another official is interrupted; no reform policy is demonstrated.
  - Target agency: Loria answers with analysis while withholding ridicule and a fuller indictment.
  - Information/misperception: Reasonable-sounding questions do not certify neutrality, ignorance, or the truth of the chief's concession premise. Inference ceiling: Recognition/role-context evidence cannot turn this into a full personally named Josef voice or private-life model.

### V03-COUNCIL

**Phase:** V03 Free Republic provisional defence council. **Roles:** de Lugo — Major General before escape; defence/army undersecretary with emergency command; unnamed colonial council — Older/senior colonial generals, not individually identified.

**Authority condition:** Legal office command conflicts with age, seniority and colonial resentment; group is not one named person. **Audience/setting:** Noisy council, mutual blame, paperwork and tea. **Focalization:** de Lugo interior; council voices/group resistance are not individually attributable.

**Source unit:** `YS-CMR0-V03-033-00163` through `YS-CMR0-V03-033-00181`; 19 normalized blocks. `text/part0031.html`, spine 33. Window SHA256 `b0038cb3f41831aaadfb1cf82a0ba80e3f9b56b2e88af4aa641f664195abfbbb`. The shared EPUB/member identity and hashes are in each episode’s `source`. The source unit has earlier sealed character witnesses.

**Conditional reading:** Legal office command does not ensure practical obedience from older, resentful colonial generals. de Lugo’s private fatigue and strategic timing become patient procedural questions. The target is a typed unnamed group; no individual reverse actor is fabricated. Tea and paperwork are state context, not preferred leisure, and actual compliance is not certified.

- **de Lugo → unnamed colonial council — `YS-CMR5-REL-V03-COUNCIL-A`.** `DIRECT_INTERACTION_WITH_TYPED_GROUP`. Patient procedural assertion tries to make a dysfunctional coalition act.
  - Private access: Direct fatigue, contempt for report-writing/blame culture, strategic patience and sober recognition of paper-only authority. Actor-access category: `EXPLICIT_BOUNDED_ACTOR_ACCESS`.
  - Behavior/public speech: Drinks the tea, reinspects papers and begins speaking despite the noise. Calls for deliberation on retaking the objective and asks force-assembly status.
  - Communicative objective: Find the usable moment and turn blame into military action. This remains bounded scene interpretation. Withheld content: His frustration and tactical timing judgment.
  - Written register: 審議しよう / 状況は; procedural command does not certify personal popularity.
  - External reading/consequence: A council officer acts as though he has not heard; narrator emphasizes senior colleagues' resistance. Emergency office gives legal command, but actual compliance is not established.
  - Target agency: Council resistance prevents a fiction of automatic obedience; no fabricated named reverse edge.
  - Information/misperception: His explanation of others' resentment is an appraisal/general narration, not each unnamed officer's verified interior. Inference ceiling: Group-target professional episode only; tea in a tiring meeting is not a favorite drink or full domestic personality.

### V14-COMBINED-RELIEF

**Phase:** V14 eastern HQ rescue as relief components converge. **Roles:** Ahrens — Armoured Captain; Tospan — Infantry Lieutenant/advance component; Meybert — Artillery Captain/relief commander.

**Authority condition:** Known combined-arms colleagues retain differentiated branch roles; emergency need shapes overt warmth. **Audience/setting:** Battlefield convergence, shouted welcome and immediate tactical coordination. **Focalization:** Ahrens joy and bounded assessment are narrated; Tospan/Meybert primarily direct speech/action.

**Source unit:** `YS-CMR0-V14-019-00178` through `YS-CMR0-V14-019-00208`; 31 normalized blocks. `item/xhtml/p-010.xhtml`, spine 19. Window SHA256 `35c082cd9035bd0e1fa1dad8cbb7872f17a0447f027719cfcbc370844fbb3262`. The shared EPUB/member identity and hashes are in each episode’s `source`. The source unit has earlier sealed character witnesses.

**Conditional reading:** Four directions share an emergency combined-arms convergence. Ahrens’s joy, embrace wish and kiss remark promptly yield to branch-specific work; Tospan’s courteous surprise does not certify a matching sentiment. Ahrens probes actual reserve capacity; Meybert gives grim limits rather than fabricated reassurance. No actual kiss, romantic identity, broad friendship voice or readiness promotion follows. AHRENS resolves to the existing ELMAR_AHRENS candidate identity; its separate focused re-audit remains outside this sealed package.

- **Ahrens → Tospan — `YS-CMR5-REL-V14-COMBINED-RELIEF-A`.** `DIRECT_INTERACTION`. Relief-driven joy immediately turns into competent familiar combined-arms work.
  - Private access: Direct joy at known friendly infantry and desire to embrace, alongside practical situation recognition. Actor-access category: `EXPLICIT_BOUNDED_ACTOR_ACCESS`.
  - Behavior/public speech: Waves his cap, cheers, laughs, taps Tospan's shoulder and coordinates armour with infantry. Exclaims about a possible kiss, gives a concrete tactical report and calls for their usual shared task.
  - Communicative objective: Welcome essential comrades and rapidly integrate complementary combat functions. This remains bounded scene interpretation. Withheld content: Full personal affection outside this emergency is unavailable.
  - Written register: 中尉 / 仕事だ / いつものように; exuberant greeting shifts promptly to work.
  - External reading/consequence: Tospan is surprised to find him there and accepts the coordination. Infantry/armour establish a working local defence before artillery arrives.
  - Target agency: Tospan arrives under Tanya's rescue order and independently performs the infantry role.
  - Information/misperception: The kiss remark and narrated embrace wish are not an actual kiss or romantic identity evidence. Inference ceiling: Ahrens remains a focused-audit candidate here; this relational evidence alone is not a sealed full character readiness result.

- **Tospan → Ahrens — `YS-CMR5-REL-V14-COMBINED-RELIEF-B`.** `DIRECT_INTERACTION`. Surprise at a known counterpart becomes prompt professional integration.
  - Private access: Unavailable in this directed record. Actor-access category: `NO_DIRECT_ACTOR_PRIVATE_ACCESS_IN_THIS_DIRECTED_RECORD`.
  - Behavior/public speech: Arrives with infantry, shares information and performs covering/antitank cooperation. Asks why Captain Ahrens is present.
  - Communicative objective: Establish the counterpart's presence and cooperate in the assigned rescue. This remains bounded scene interpretation. Withheld content: No independent private Tospan reflection is supplied.
  - Written register: アーレンス大尉殿 / なぜ; one short courteous question, not a robust off-duty voice sample.
  - External reading/consequence: Ahrens welcomes the infantry enthusiastically and recognizes complementary work. The combined assault gains a workable breakthrough; complete battle outcome is beyond this window.
  - Target agency: Ahrens gives the situation rather than merely demanding rank submission.
  - Information/misperception: Brief surprise and coordinated action do not reveal a broad private friendship register. Inference ceiling: Do not attribute Ahrens's kiss/embrace wish to Tospan or infer a symmetric personal sentiment.

- **Ahrens → Meybert — `YS-CMR5-REL-V14-COMBINED-RELIEF-C`.** `DIRECT_INTERACTION`. Practical reinforcement demand tests a colleague's grim capacity report.
  - Private access: Narrated desire for further reinforcement; no complete strategic doctrine. Actor-access category: `EXPLICIT_BOUNDED_ACTOR_ACCESS`.
  - Behavior/public speech: Coordinates the converged arms and turns to the arriving artillery counterpart. Asks the relief situation, extraction feasibility and whereabouts of strategic reserve.
  - Communicative objective: Identify what assistance can genuinely be brought to the fight. This remains bounded scene interpretation. Withheld content: Independent broad private assessment beyond urgent need is unavailable.
  - Written register: メーベルト大尉殿 / 状況は / どこに; specific operational questions.
  - External reading/consequence: Meybert confirms the feared shortage rather than offering reassurance. Paper reserves cannot supply real immediate reinforcement.
  - Target agency: Meybert supplies limits and remains a cooperating professional rather than an obstructive rank target.
  - Information/misperception: His reserve expectation is corrected by an informed scarcity report. Inference ceiling: No proof of omniscient reserve knowledge or an all-context optimistic persona.

- **Meybert → Ahrens — `YS-CMR5-REL-V14-COMBINED-RELIEF-D`.** `DIRECT_INTERACTION`. Uncomfortable realism supplies a peer with the actual limit on reserves.
  - Private access: Unavailable in this directed record. Actor-access category: `NO_DIRECT_ACTOR_PRIVATE_ACCESS_IN_THIS_DIRECTED_RECORD`.
  - Behavior/public speech: Arrives with hauled guns, joins the combined-arms posture and confirms the shortage. States the lack of nearby friendly troops and that strategic reserves exist on paper.
  - Communicative objective: Give a usable capacity account without inventing aid. This remains bounded scene interpretation. Withheld content: No direct private monologue behind the brief reply.
  - Written register: だ / のだ / 紙の上だ; clipped peer report differs from panic in the earlier superior radio call.
  - External reading/consequence: Ahrens keeps probing because reinforcements are urgently needed. Relief remains constrained by genuinely limited available personnel.
  - Target agency: Ahrens's questions expose the discrepancy; both still act within available means.
  - Information/misperception: Paper allocation and delivered force must stay separate. Inference ceiling: No inherited Ahrens joy, timeless stammer or guaranteed future rescue.

## Episode schema

Each UTF-8/LF/NFC JSONL line is one `youjo-senki/directed-relationship-episode/v1` record. The file has 77 episode lines and no extra manifest row. All 31 original top-level fields are mapped; eight added publication/provenance fields make 39. No analytical field is removed. Null means unavailable/not recorded at the stated channel; it is not a zero score. The exact row meanings are:

| Fields | Meaning and mapping |
|---|---|
| `relationship_episode_id`, `actor_id`, `target_id`, `direction` | Literal stable ID and original directed identity tokens. No renumbering or reverse inference. |
| `direction_kind`, `dependence_group` | Literal interaction/appraisal/testimony/group type and shared source dependence. |
| `source` | `route_kind=CMR0_PARAGRAPH`; exact source Drive ID, safe EPUB filename, source SHA256, volume, OPF path, member path, member SHA256, integer spine/paragraph, locator ID and text SHA256. Original raw Japanese chapter label is omitted. |
| `supporting_source_blocks` | Every original locator ID/text SHA256 and integer paragraph in original order; `source_ref=source` resolves the same record’s exact EPUB/volume/OPF/member context. No support is an independently counted scene. |
| `volume`, `spine_index` | Original top-level volume/spine; required to agree with primary source and read window. |
| `actual_read_window` | Exact start/end locator, block count and joined-text SHA256, plus literal source-review access flags. Hash is SHA256 of LF-joined normalized paragraph text with no final LF. It identifies a complete inherited source read, not a fresh port read. |
| `scene_chronology`, `roles_at_this_episode`, `power_and_role_condition`, `audience_and_setting`, `scene_focalization` | Literal era, current office/rank, authority/refusal constraints, audience/state and segmented focalization. They condition the finding. |
| `prior_sealed_cmr5_witness_ids`, `new_relationship_fit_window`, `reserve_overlap_blocks` | Exact earlier witness dependencies, novelty flag relative to the earlier 95 package, and source reviewer’s zero reserved-block overlap. |
| `directed_orientation_observed` | The source-supported paraphrased stance of this actor toward this target in this state. |
| `five_channels` | Separate `private_cognition`, `observable_behavior`, `public_speech`, `external_interpretation`, `institutional_consequence`. A public claim/observer interpretation is not an actor’s verified private belief. |
| `speaker_and_focalizer_certainty` | Literal inherited combined qualifier; separate fields below retain the actual attribution/mind-access distinction. No inferred numeric or HIGH model confidence. |
| `speaker_attribution` | Literal actor identity, certainty, channel, attribution basis and whether personal name was explicit. Primary anchor may itself be narration/action. |
| `focalizer_attribution` | Literal scene focalizer IDs, certainty, transition scope, actor private-access category and the prohibitions on target mind borrowing and unattributed witness interpretation. |
| `speech_generation_chain` | Seven preserved keys implement the six-step appraisal→objective→withholding→role constraint→register→surface process; `objective_status` qualifies interpretation. `private_appraisal_available`, `communicative_objective`, `withheld_private_content`, `relationship_and_role_constraint`, `register_selection` and `surface_wording_policy` retain all substantive findings. |
| `information_and_misperception_condition`, `target_agency_or_reciprocal_evidence`, `inference_ceiling` | Knowledge gaps, actual target response/agency and counterlimits. The target-response field is local evidence, not permission to fill missing reverse coverage. |
| `review_status`, `not_a_model`, `qa_status` | Literal SOURCE_RELATIONSHIP_PREPARATION_ONLY, true and pending construction/QA status. |
| `schema`, `status`, `record_kind`, `source_use` | Added format/provisional/source-analysis type; character models and ensemble QA remain pending. |
| `review_basis`, `provenance_ref` | Added inherited-adjudication/full-analytical-read/hash-validation scope and link to this schema. |
| `resolved_actor_id`, `resolved_target_id` | Added same-person identity route; only AHRENS→ELMAR_AHRENS differs from original tokens. This is not a global alias or readiness edit. |

## Exact-source reopening and preservation

Find the episode ID, read its `source` and supporting tuples, and retrieve the EPUB identified by the source Drive ID and SHA256. Select the exact OPF spine/member, then the normalized paragraph ordinal/locator; confirm text SHA256 against the frozen CMR0 extraction. Use the inclusive `actual_read_window` for speaker/focalizer transitions and state. A short lexical control never replaces reopening its context.

The frozen source locator is Drive ID `140ow12czVj4J8Q_JR44MSWI98LUxj3uk`, SHA256 `c84fa4c8e0251730887b51913a8f32ea68c39be68ff4adae8d995d49292f5cfe`, 63,812 paragraph records. The task deterministically rebuilt byte-identical locator bytes from the exact original extraction script and independently verified local EPUBs; this is not a claim that the 52.9 MB locator was downloaded from Drive. The source member index is Drive ID `1GlDNvT5spgIQk5VaUU5S2Qsk5dF174hR`, SHA256 `e05b9fe26ec35e4590b9e148005b49f7ed142ec2f6ca2868e99561981372e220`, 608 members. Raw Japanese source text, anchors and bulk source-derived exports remain Drive-primary.

### Sealed analytical inputs and controls

| Input role | Exact original bytes | SHA256 |
|---|---:|---|
| 77-episode sealed source adjudication | 516115 | `3454424d9c10dcd1b2d67963d8011a4e33efa26550ea2d8574a5447cd86b12db` |
| Complete relationship source review | 35079 | `54b2ae7bc32287ff54aaaf554a6081f50b9cbb6d61316069536efac832040e09` |
| Relationship source package seal | 1934 | `8e1a8183719317a83716c9d2fdec0dabdadf0f515ca972a5caa60421ef7fc254` |
| Source package validation | 938 | `03c061afb3aed5160426e93283b948e23c9989aef7b8ae000b537714a2159e2a` |
| 32-window source manifest | 39835 | `78b4bb590f1b512b5572f3e5b736a80c850ce7c61224b9315de0d6a977509d31` |
| 42-cell core coverage ledger | 17296 | `04d186aa4c1f7cf1705c187d2c68f146b54ab19f68a1d412c0b653464e34d9f8` |
| Preseal attribution/identity correction receipt | 1793 | `229316f4b56912e2dc99b4fe74fb934a4026f7670dcc196f6e2090824e8ca448` |
| Construction QA reserve metadata only | 2855 | `428fc476ff7a275162740a6f6f970e886a7aa7706c595bbac3614c968db96953` |
| Construction QA exclusion coordinates only | 1385 | `fc4c90cd970065ac5a025bd9996dcf0c29be31f17ad4c480006289c1c77dc3d0` |

The original 95-character source diagnostics remain SHA256 `4a8c958318269d016c811b6267725d9bb2114b67f09be7bf9a5d17b0c79e8122`; the original 22 readiness rows remain SHA256 `e3c5634277a857b789a556953ab226237415d892559f10d8299b8679b3be2799`. This relationship addendum does not change them. **87 blocks outside the earlier 95-read union** is a relative novelty measure only; those blocks may already occur in Tanya’s 814 admitted diagnostics or mature V2 familiarity.

The source package’s preseal receipt records separate speaker/focalizer fields and normalization of expanded Loria/de Lugo identity labels to `LORIA` and `DE_LUGO` before the source seal. Stable record IDs and interpretations were unchanged. This port starts from the final sealed bytes; it does not recreate a preseal version or claim that unavailable earlier bytes were inspected.

### Controlled publication transformations

All English analytical findings, five channels, objectives, access/certainty, chronology, limits and target-agency values are retained verbatim. Exact source string coordinates become integers; the OPF and member SHA are enriched from the frozen member index. Raw chapter labels are omitted. A private receipt retains every original/destination mapping and byte hash.

Only three written-register strings change punctuation: `YS-CMR5-REL-V06-MUD-A` separates a polite qualifier and inability-to-agree form; `YS-CMR5-REL-V14-CENSURE-A` separates apology and acknowledgement; `YS-CMR5-REL-V14-ADOPTION-C` separates the order predicate and silence imperative. All lexical forms and the supported refusal/gratitude/authority functions remain. No source paragraphs, Japanese dialogue passages, source anchors, invented canonical lines or adaptation speech are included. Other short written lexemes, pronouns, address forms, suffixes and qualified predicates remain bounded analytical controls tied to their exact scene.

Machine validation checks all 77 primary routes and 1,141 supporting edges, all 32 joined window hashes and 2,043 distinct block hashes, exact original field mappings/IDs, core counts/dependencies, identity route, every reserved range, unchanged 95/22 inputs, UTF-8/LF/NFC, no Drive URLs/private paths, and the 1 MiB per-file limit. Source-ready relationship analysis is pending verified main integration of this port; character reconstruction and independent ensemble QA remain separate required work.
