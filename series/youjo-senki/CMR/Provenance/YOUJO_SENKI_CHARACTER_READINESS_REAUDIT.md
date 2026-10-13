---
series: YOUJO_SENKI
artifact_id: YOUJO_SENKI_CHARACTER_READINESS_REAUDIT
artifact_type: source_preparation_readiness_reaudit
scope: "Japanese LN V01-V14; frozen initial20, two supplementary reviewed subjects, seven open focused audits and one withdrawn tentative name"
generation: V2_CMR
version: "1.0"
status: active_provisional
canonical_home: "series/youjo-senki/CMR/Provenance/YOUJO_SENKI_CHARACTER_READINESS_REAUDIT.md"
snapshot_date: 2026-10-12
promotion_status: PROPOSED_PENDING_VERIFIED_MAIN_INTEGRATION
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
---

# Source-facing character readiness re-audit

This controlled analytical port preserves **95 source-preparation diagnostics**, **21 actual-read non-Tanya readiness assessments**, and **one Tanya owner pointer**. The reviewed subjects comprise the 19 non-Tanya members of the frozen initial20 and two supplementary subjects. A separate work register retains seven current `NOT_YET_AUDITED` candidates and the history of one withdrawn tentative name. These are source/readiness results; they do not establish completed character models or predictive QA.

The [ensemble diagnostics](../Diagnostics/ENSEMBLE_CHARACTER_DIAGNOSTICS.jsonl) retain all supported English findings, conditions, separate five channels, literal speaker/focalizer certainty, written-register analysis, confidence, counterevidence and inference ceilings. The [machine readiness ledger](YOUJO_SENKI_CHARACTER_READINESS_REAUDIT.jsonl) contains 31 typed records: one port manifest, 21 actual-read assessments, one Tanya owner pointer, seven open candidate audits and one withdrawn-name record. Filter by `record_kind` before counting assessments. All 95 diagnostics remain separately identifiable, including Mary’s excluded afterword and Josef’s mediated recognition context.

The complete substantive analytical fields of the sealed95 diagnostics and22 readiness records, the full source-readiness review, and correction/seal/validation/gap material were read for this port. The source reviewer read checksum-validated contiguous Japanese CMR0 windows, while the root independently verified original EPUB bytes and deterministic extraction. `source_container_reopened_here=false` remains literal for that reviewer. The port does not claim a second independent Japanese semantic or primary-container reopen.

The source package logs **61 distinct windows / 3,309 distinct normalized Japanese blocks** in its fit and mode-control scope. Several diagnostics share scenes and several windows overlap, so neither 95 nor 61 is an independent behavioral-scene count. A primary anchor can be another actor’s wording or documentary context; its extraction mode is not actor attribution. The source-integrity seal verifies coordinates and hashes, while semantic attribution remains grounded in the documented source reading. No numerical personality probabilities or predictive scores are added.

## Governing baseline and gates

The [initial CMR1 readiness baseline](YOUJO_SENKI_CMR1_READINESS_BASELINE.md) remains a complete `historical_legacy` snapshot with its veto as current authority. All 20 original classifications and original metrics remain preserved. This re-audit supplies a separate current provisional analytical layer under the [CMR method](../Methods/YOUJO_SENKI_CHARACTER_MODELING_REFERENCE_METHOD.md); it does not rewrite the frozen alias map, retrieval counts or original audit bytes. Effective promotion awaits verified main integration.

Only one initial-roster class changes: **Meybert → narrow provisional `DOMAIN_BOUNDED`**, supported by actual field/garrison cognition and differentiated upward, downward and known-colleague speech. **Tospan and Josef remain `RECOGNITION_PROFILE`. Visha remains `DOMAIN_BOUNDED`** despite independent early friendship and ordinary material. Lergen retains `FULL_SPECTRUM` with specific domestic/private limits; the label does not authorize unsourced life completion. Gassman is newly audited as narrow `DOMAIN_BOUNDED` and Erya as limited `RECOGNITION_PROFILE`.

All non-Tanya model emission remains gated on the root’s first Tanya model and independent QA. This port records the source-preparation gate; it does not certify it has passed. Tanya’s source inventory is separately closed at 814 ordinary textual diagnostics plus a separately typed image-paratext witness, navigable through the [Tanya diagnostic index](../Diagnostics/YOUJO_SENKI_TANYA_DIAGNOSTIC_NAVIGATION.md). Her exact readiness/model/QA decision remains root-owned; the inherited null reaudited-class pointer is preserved rather than replaced with an inferred verdict. This package cannot alone establish completion of all20 current readiness decisions.

The source reviewer separately sealed seven construction-held-out QA units. Their outcomes are excluded from these95 fit diagnostics and readiness decisions. This port has not consumed their private outcomes or supplied predictions/scores. Construction separation, wider-arc familiarity and shared-cache access do not establish a fully blinded test. Source-only directed-relationship work outside this sealed95 package is a separate artifact and is not silently imported here.

## Readiness results

The current non-Tanya assessments comprise one retained `FULL_SPECTRUM`, 17 `DOMAIN_BOUNDED` and three `RECOGNITION_PROFILE` ceilings. These are qualified readiness labels; each entry’s supported domains, remaining gaps, source access and model gate remain binding.

| Subject | Frozen baseline → current targeted ceiling | Confidence | Diagnostics / windows | Decision |
|---|---|---|---|---|
| Viktoriya Ivanovna Serebryakov | DOMAIN_BOUNDED → DOMAIN_BOUNDED | HIGH | 11 / 6 | STRENGTHEN |
| Erich von Lergen | FULL_SPECTRUM → FULL_SPECTRUM | MODERATE_HIGH | 9 / 7 | STRENGTHEN |
| Hans von Zettour | DOMAIN_BOUNDED → DOMAIN_BOUNDED | HIGH | 10 / 6 | STRENGTHEN |
| Matheus Johann Weiss | DOMAIN_BOUNDED → DOMAIN_BOUNDED | HIGH | 7 / 6 | STRENGTHEN |
| Grantz | DOMAIN_BOUNDED → DOMAIN_BOUNDED | HIGH | 6 / 5 | STRENGTHEN |
| Uger | DOMAIN_BOUNDED → DOMAIN_BOUNDED | HIGH | 5 / 5 | STRENGTHEN |
| Kurt von Rudersdorf | DOMAIN_BOUNDED → DOMAIN_BOUNDED | HIGH | 4 / 4 | STRENGTHEN |
| Mary Sue | DOMAIN_BOUNDED → DOMAIN_BOUNDED | HIGH | 6 / 6 | STRENGTHEN_WITH_SOURCE_MODE_CORRECTION |
| Drake | DOMAIN_BOUNDED → DOMAIN_BOUNDED | HIGH | 4 / 4 | STRENGTHEN |
| Calandro | DOMAIN_BOUNDED → DOMAIN_BOUNDED | HIGH | 3 / 3 | STRENGTHEN |
| Loria | DOMAIN_BOUNDED → DOMAIN_BOUNDED | HIGH | 2 / 2 | STRENGTHEN |
| Romel | DOMAIN_BOUNDED → DOMAIN_BOUNDED | MODERATE_HIGH | 2 / 2 | RETAIN_WITH_NARROW_SCOPE |
| Conrad | DOMAIN_BOUNDED → DOMAIN_BOUNDED | MODERATE_HIGH | 3 / 2 | STRENGTHEN |
| de Lugo | DOMAIN_BOUNDED → DOMAIN_BOUNDED | MODERATE | 2 / 2 | RETAIN_WITH_NARROW_SCOPE |
| Anson Sioux | DOMAIN_BOUNDED → DOMAIN_BOUNDED | MODERATE | 3 / 3 | STRENGTHEN_WITH_TERMINAL_STATE_BOUNDARY |
| Adelheid von Schugel | DOMAIN_BOUNDED → DOMAIN_BOUNDED | MODERATE | 3 / 3 | STRENGTHEN_WITH_REGISTER_AND_BELIEF_BOUNDARY |
| Meybert | RECOGNITION_PROFILE → DOMAIN_BOUNDED | MODERATE | 5 / 5 | REVISE_CLASS_NARROWLY_SOURCE_GROUNDED |
| Tospan | RECOGNITION_PROFILE → RECOGNITION_PROFILE | MODERATE | 4 / 4 | STRENGTHEN_WITHOUT_PROMOTION |
| Josef | RECOGNITION_PROFILE → RECOGNITION_PROFILE | MODERATE | 2 / 2 | STRENGTHEN_WITH_MODE_CORRECTION |
| Igor Gassman | NOT_YET_AUDITED → DOMAIN_BOUNDED | MODERATE | 3 / 3 | NEW_SOURCE_AUDIT_NARROW_DOMAIN |
| Erya | NOT_YET_AUDITED → RECOGNITION_PROFILE | MODERATE | 1 / 1 | NEW_SOURCE_AUDIT_LIMITED_RECOGNITION |
| Tanya Degurechaff | FULL_SPECTRUM → ROOT-OWNED POINTER | UNSCORED ROOT DECISION | 0 / 0 | OWNED_BY_ROOT_CMR2_SOURCE_CLOSURE |

## Source-mode and attribution controls

Mary’s `YS-CMR5-MARY_SUE-V11-001` at `YS-CMR0-V11-028-00016` is explicitly `EXCLUDED_ADAPTATION_AFTERWORD`, with `usable_for_behavioral_model=false`. Carlo Zen’s author/adaptation commentary and authorial `僕` supply no Mary behavior, direct novel dialogue, voice performance or V11 narrative development. The frozen nine-volume alias-hit metric remains historical retrieval evidence; its interpretation is corrected without altering it.

Josef’s `YS-CMR5-JOSEF-V04-001` is `MEDIATED_RECOGNITION_CONTEXT` from an in-world satirical textbook and retrospective interview. It supports recognition of ideological portrayal, not favorite wine, neutral speech, transparent private motive or a psychiatric diagnosis. The separate V06 official exchange retains speaker certainty `HIGH_ROLE_CONTEXT_NOT_NAMED_IN_LINE` and overall `MODERATE_ATTRIBUTION`. The secretary’s context supplies limited official inquiry while his proper name is absent from those lines.

Lergen’s V11 memoir is retrospective written self-presentation with admitted omissions. It is not contemporaneous conversational voice or a certificate of every earlier defended motive. Mary’s V04 family letter and quiet self-comments remain separate delivery modes; Gassman’s V14 audible self-directed remarks do not become stranger-facing conversation. Early Meybert/Tospan V05 records are other officers’ reports and evaluations, not their live private thought or exact direct speech.

Grantz V02-001 retains null speaker identity for the unattributed final rush line; V02-004 retains null speaker identity and `NO_DIRECT_SPEECH`. Mixed windows retain their segmented focalization. Grantz’s V03 protective-equipment scene ends before de Lugo’s separate headquarters scene; the source correction prevents inheriting de Lugo’s thought. Gassman V06 explicitly states that `貴官`/`かね` are **not verified in that window**. These negative observations must not be mined as attested forms.

Zettour’s V14 adoption changes the order’s subsequent authority; it does not erase the original forgery. Official censure, gratitude, outcome praise and observer patriotism can coexist. Cultural-book wishes, promised employment, preferred leave and procurement promises remain prospective unless their fulfillment is independently observed. These controls apply even when a finding’s overall confidence is high.

## Per-subject supported domains and limits

### Viktoriya Ivanovna Serebryakov

Class retained and strengthened. Six distinct source episodes across V01,V03,V05,V06,V10,V14 show interiority, non-Tanya friendship, ordinary texture and differentiated speech. Early friendship defeats a strictly Tanya-centered evidence account, but does not independently establish broad adult nonmilitary domains. No full-spectrum promotion from isolated ordinary material.

**Supported domains.** Early pre-Tanya first-person identity/family belonging; Independent Erya peer conversation, sleep and deployed-food baseline; Adjutant intelligence/translation initiative; Formal respectful but firm superior-facing disagreement; Visha to Weiss irritation and deliberate factual withholding; Leave, social hospitality and demonstrated coffee preparation; Late chosen commitment, humor and shared command-group trust.

**Remaining gaps.** Independent adult civilian/stranger interactions; Intimate/dating/domestic baseline; Permanent peacetime tastes/leisure; Range of actual prisoner-facing Japanese speech; Combat-specific utterance diversity.

**Countercontrols.** Do not generalize affectionate casual Erya speech to officers or strangers. Do not turn competence at coffee/translation into enjoyment in every context. Private irritation can coexist with polite factual speech. Late volunteering must not erase semi-compulsory initial mage recruitment.

**Diagnostic route.** `YS-CMR5-VISHA-V01-001`, `YS-CMR5-VISHA-V01-002`, `YS-CMR5-VISHA-V01-003`, `YS-CMR5-VISHA-V05-001`, `YS-CMR5-VISHA-V05-002`, `YS-CMR5-VISHA-V06-001`, `YS-CMR5-VISHA-V14-001`, `YS-CMR5-VISHA-V14-002`, `YS-CMR5-VISHA-V03-001`, `YS-CMR5-VISHA-V10-001`, `YS-CMR5-VISHA-V10-002`.

### Erich von Lergen

Class retained with explicit domain limits. Broad professional-social/interior coverage is directly strengthened across V01,V06,V10,V11,V14, including early/late development, foreign peers and civilian counterparts. Full-spectrum class does not permit unsourced private family life; source access and predictive fidelity vary by subdomain.

**Supported domains.** Early direct personnel-officer anxiety and merit/duty conflict; Observed work/smoking and constrained public presentation; Foreign-peer hospitality, surprise and recovery; Civilian counterpart disagreement, explanation repair and political self-doubt; Retrospective memoir self-presentation with admitted silence; Late censure, gratitude, respect and institutional contradiction.

**Remaining gaps.** Domestic/intimate household behavior; Leisure preferences beyond work-related tobacco/hospitality; Exact full range of combat-command speech; Contemporaneous thought cannot be substituted by memoir; Expanded Calandro relation through invasion/warning needs separate case.

**Countercontrols.** Do not project public composure into absence of anxiety. Do not treat observer interpretation of Tanya as her motive. Memoir is written retrospective, not live spoken voice or transparent historical truth. Outcome praise and sincere gratitude coexist with explicit condemnation of forgery.

**Diagnostic route.** `YS-CMR5-LERGEN-V01-001`, `YS-CMR5-LERGEN-V01-002`, `YS-CMR5-LERGEN-V11-001`, `YS-CMR5-LERGEN-V10-001`, `YS-CMR5-LERGEN-V10-002`, `YS-CMR5-LERGEN-V14-001`, `YS-CMR5-LERGEN-V14-002`, `YS-CMR5-LERGEN-V06-001`, `YS-CMR5-LERGEN-V10-003`.

### Hans von Zettour

Class retained and strengthened. Direct source cases across V01,V08,V11,V14 include strategic surprise, personal collateral, friend rupture, authority performance, gratitude and cultural aspiration. These support a differentiated professional/institutional/reciprocal model while domestic and neutral civilian life remain unestablished.

**Supported domains.** Early restrained staff objection contrasted with Rudersdorf; Philosophy-reading practice, strategic surprise and shame; Field rescue with personal collateral and institutional manipulation; Direct private Rudersdorf rupture, tremor and must-versus-can conflict; Official adoption/performed authority, Uger relation; Grantz information gathering and shift from indirection to blunt command; Late fatigue, direct gratitude, cultural aspiration and future-work promise.

**Remaining gaps.** Domestic/intimate ordinary life; Stable civilian social baseline; Favorite authors/books/tobacco or peacetime habits; Intermediate mentoring states not reopened as a complete trajectory.

**Countercontrols.** No timeless omniscient chessmaster: early surprise and late rear-area information limits are explicit. Friendly form can coexist with coercive closure. Personal care and strategic leverage coexist in rescue. Future work assurance is a promise, not observed postwar fulfillment.

**Diagnostic route.** `YS-CMR5-ZETTOUR-V01-001`, `YS-CMR5-ZETTOUR-V01-002`, `YS-CMR5-ZETTOUR-V01-003`, `YS-CMR5-ZETTOUR-V08-001`, `YS-CMR5-ZETTOUR-V14-001`, `YS-CMR5-ZETTOUR-V14-002`, `YS-CMR5-ZETTOUR-V14-003`, `YS-CMR5-ZETTOUR-V14-004`, `YS-CMR5-ZETTOUR-V14-005`, `YS-CMR5-ZETTOUR-V11-001`.

### Matheus Johann Weiss

Retained high DOMAIN_BOUNDED. Independent source episodes span V02,V03,V04,V06,V14 and show thought, judgment, permitted disagreement, ordinary service and state-specific humor. Source supports a military-relational model, not an unconstrained private self.

**Supported domains.** Practical deputy care and observed nonsmoking; Independent rescue feasibility and concern for Grantz; Formal legal reservations and task clarification; Peace logic versus emotional loss; Intoxicated holiday humor versus sober baseline; Late chosen duty, withheld joke and familiar command-group laughter.

**Remaining gaps.** Civilian/intimate domestic baseline; Favorite food/drink/leisure; Generic humorous register outside known relationships.

**Diagnostic route.** `YS-CMR5-WEISS-V14-001`, `YS-CMR5-WEISS-V14-002`, `YS-CMR5-WEISS-V03-001`, `YS-CMR5-WEISS-V02-001`, `YS-CMR5-WEISS-V04-001`, `YS-CMR5-WEISS-V06-001`, `YS-CMR5-WEISS-V06-002`.

### Grantz

Retained high DOMAIN_BOUNDED with explicit developmental states. V02 ordinary/trauma, V03 desert adaptation and V14 politically strained competent reporting differ meaningfully. Protective equipment judgment and late skill must not erase moral protest or prove complete healing.

**Supported domains.** New-officer ambition and travel fear; Meal/rest adaptation and calm night-watch attention; Arene sensory moral injury and interrupted protest; V03 protective-equipment adaptation, subordinate discipline and self-recognized limit; Coerced obedience distinct from agreement; Late competent reporting under political-authority fear.

**Remaining gaps.** Civilian/intimate adulthood; Permanent psychiatric conclusions or recovery endpoint; Favorite coffee/food; Broad polished conversational repertoire.

**Diagnostic route.** `YS-CMR5-GRANTZ-V14-001`, `YS-CMR5-GRANTZ-V02-001`, `YS-CMR5-GRANTZ-V02-002`, `YS-CMR5-GRANTZ-V02-003`, `YS-CMR5-GRANTZ-V02-004`, `YS-CMR5-GRANTZ-V03-001`.

### Uger

Retained high DOMAIN_BOUNDED. V01,V06,V09,V10,V14 directly support family-aware professional judgment, logistics duty and interpersonal candor. Fatherhood is real evidence but does not license invented home scenes. Humane concern does not mean effortless assent to every peace proposal.

**Supported domains.** Direct family affection and early peer framing; Emotional sacrifice/settlement objection; Human limits, gratitude and frank criticism; Family-cost resentment alongside logistics solidarity; Formal senior-staff compliance under strain.

**Remaining gaps.** Detailed actual household routines; Generic therapist-like speech; Broad leisure/private preferences; Independent assessment of self-described poor combat-command fitness.

**Diagnostic route.** `YS-CMR5-UGER-V14-001`, `YS-CMR5-UGER-V01-001`, `YS-CMR5-UGER-V06-001`, `YS-CMR5-UGER-V09-001`, `YS-CMR5-UGER-V10-001`.

### Kurt von Rudersdorf

Retained high DOMAIN_BOUNDED. V01,V02,V09,V11 establish operational reasoning, peer register, ordinary institutional friction and developmental political danger. Book promise is actual V09 prospective speech, not fulfilled civilian conduct. Late private motive is partly Zettour focalization and must remain so.

**Supported domains.** Early opposition to excessive mobilization; Trusted Zettour peer planning and risk appetite; Disliked staff food under secure-work constraint; Tanya-specific teasing and conditional book promise; Late sacrifice/obligation defense and must-versus-can conflict.

**Remaining gaps.** Unrestricted domestic/intimate behavior; Actual postwar authorship; Favorite meals/tobacco; All private motive behind late backup-plan position.

**Diagnostic route.** `YS-CMR5-RUDERSDORF-V01-001`, `YS-CMR5-RUDERSDORF-V02-001`, `YS-CMR5-RUDERSDORF-V09-001`, `YS-CMR5-RUDERSDORF-V11-001`.

### Mary Sue

Class retained with temporal segmentation. Direct V03,V04,V06,V12 episodes establish agency, care, ordinary family attachment, changing speech and later grievance. V11's only frozen メアリー hit is Carlo Zen's animated-film afterword and is excluded from LN behavior/voice; the frozen nine-volume metric is a retrieval result, not nine verified narrative volumes. Rank-form supplemental retrieval found real later scenes without altering the frozen alias map.

**Supported domains.** Deliberated exile enlistment, regret and paternal memory; Early family letter, grandmother food, desired tea/cookies and training satisfaction; Novice threat learning; Prisoner-protection argument and political misreading; Late personalized moral certainty, fatigue and accusation toward Drake.

**Remaining gaps.** A continuous V03-to-V12 trajectory between sampled states; Independent adult civilian/intimate baseline; Broad later noncombat conversational range; Later launch-exchange continuation not fitted here.

**Countercontrols.** Do not back-project late rigid certainty onto the deliberating novice. Food in a private letter is not proof of every lifelong preference. Drake's interior explanation is not Mary's thought. Author/adaptation words and actor performances supply no Mary voice evidence.

**Diagnostic route.** `YS-CMR5-MARY_SUE-V03-001`, `YS-CMR5-MARY_SUE-V04-001`, `YS-CMR5-MARY_SUE-V04-002`, `YS-CMR5-MARY_SUE-V06-001`, `YS-CMR5-MARY_SUE-V12-001`, `YS-CMR5-MARY_SUE-V11-001`.

### Drake

Retained high domain-bound source support across V04,V05,V06. Multiple interlocutors, crisis modes and grief expose a person beyond strategic cynicism. Command outside his own unit cites actual delegated authority; formal rank alone is insufficient. Source enables professional-protective, coalition and morally constrained interaction, not invented domestic life.

**Supported domains.** Direct tactical warning to Mary and novice-survival guidance; Actual delegated command and rearguard protection; Casualty grief, obstruction anger and medical gratitude; Alcohol in grief-linked peer contact; Political-risk-aware public protection and private prisoner concern.

**Remaining gaps.** Neutral civilian domestic life; Stable leisure/drink preferences; Complete reciprocal Mikel/Liliya relationships; A wider calm register independent of military role.

**Countercontrols.** Alcohol in grief does not prove habitual enjoyment, favorite drink or diagnosis. Concern for prisoners does not remove political calculation or the danger of overheard speech. Calling for a novice to fall is a friendly-territory survival tactic, not a generic retreat rule.

**Diagnostic route.** `YS-CMR5-DRAKE-V04-001`, `YS-CMR5-DRAKE-V04-002`, `YS-CMR5-DRAKE-V05-001`, `YS-CMR5-DRAKE-V06-001`.

### Calandro

Retained high domain-bound class. V06 peer/staff exchanges and V11 invasion supply different authority structures, direct private recognition and voice changes. Explicitly missing the decapitation threat before repair defeats an omniscient-spymaster reading. Gaps in ordinary civilian life remain material.

**Supported domains.** Foreign-peer agenda control and polished hospitality; Own-staff evidence reporting and politically selective silence; Direct operational error recognition; Commander protection and responsibility-based rearguard offer.

**Remaining gaps.** Household, dating or civilian leisure; Detailed intervening professional development; Independent treaty-success truth beyond his report; Unspoken political position behind strategic silence.

**Countercontrols.** Polite silence does not establish assent. Friendly appearance does not establish transparent sincerity or a universal mask. A foreign peer colonel is not automatically subject to Imperial hierarchy.

**Diagnostic route.** `YS-CMR5-CALANDRO-V06-001`, `YS-CMR5-CALANDRO-V06-002`, `YS-CMR5-CALANDRO-V11-001`.

### Loria

Retained bounded high confidence in the explicitly observed security-state, fixation and political-analysis domains. V04 direct private predation and V06 competent policy explanation must coexist; one neither explains away nor redeems the other. No reciprocal attraction, romance or graphic generative scene is licensed.

**Supported domains.** Direct predatory fixation and state-specific attention change; Security-state fear in observers; Direct political/information-system analysis; Respectful secretary-facing mobilization explanation and withheld contempt.

**Remaining gaps.** Neutral private social behavior; Domestic/intimate reciprocity; Generic safe everyday conversational repertoire; Verified motive for every later policy decision.

**Countercontrols.** Non-graphic analysis only: predation is not softened into affection. Competence does not imply moral reform. Ideological universal claims about emotions are his framing, not established psychology. Textbook/WTN material is separate from live behavior.

**Diagnostic route.** `YS-CMR5-LORIA-V04-001`, `YS-CMR5-LORIA-V06-001`.

### Romel

Retained specialist domain class at the frozen confidence, with this targeted re-audit supporting only the shown V04 field contingency and V10 political/relief reasoning. Neither a coffee act nor a bitter hoped-for holiday licenses taste, leisure or fulfilled retirement. A later independent command episode should precede ambitious transfer claims.

**Supported domains.** Field contingency planning, feint skepticism and acceptance of safe exit; Quiet work-linked coffee moment; Late reinforcement/political frustration; Concern that field subordinates have rest.

**Remaining gaps.** Civilian/private baseline and stable tastes; Wider dialogue repertoire and independent peer intimacy; Additional independent field-command test case; Actual peaceful leave/retirement.

**Countercontrols.** Reinforcement checks are metaphorical promises, not literal personal finance. Coffee in one office moment is not a favorite. Hope for rest is not an observed civilian life.

**Diagnostic route.** `YS-CMR5-ROMEL-V04-001`, `YS-CMR5-ROMEL-V10-001`.

### Conrad

Retained specialist diplomatic/professional class. V10 and V12 direct dialogue is dense, causally situated and relationally distinct from staff command. Social hospitality is real but work-linked; a cigar joke's ambiguous motive is not neutral proof of theft or a stable personal preference.

**Supported domains.** Civilian explanation/translation of military consequences; Direct challenge to Lergen and repair of communication; Professional cigar hospitality, joke and cooperation; Punctual high-level meeting and Rudersdorf-linked nostalgia.

**Remaining gaps.** Domestic/intimate life; Neutral hobbies or favorite tobacco; Detailed motivation behind every joke; Broad emotional-state stress range.

**Countercontrols.** Explanation corrects a failure without guaranteeing political outcomes. Civilian authority and military command structures differ. Lergen's uncertainty about the joke is not Conrad's disclosed intention.

**Diagnostic route.** `YS-CMR5-CONRAD-V10-001`, `YS-CMR5-CONRAD-V10-002`, `YS-CMR5-CONRAD-V12-001`.

### de Lugo

Retained moderate specialist readiness. Two V03 episodes offer substantial direct interiority and concrete institutional choice: withdrawal under defeat and command at a divided council. Office fatigue and tea add texture but do not create a general peacetime self. Prior multi-volume retrieval remains a route, not automatically verified development.

**Supported domains.** Direct defeat shame and evacuation triage; Self-control under demands to preserve resistance; Weary tea/paperwork office texture; Patience and strategic timing amid factional seniority.

**Remaining gaps.** Civilian/private life; Wide temporal development beyond V03 direct sample; Favorite tea or tastes; Neutral conversational baseline outside official crisis.

**Countercontrols.** Paper authority is constrained by older factional officers. A direct tea act is not a favorite. Ten-hour deadline is episode-specific triage, not a universal formula.

**Diagnostic route.** `YS-CMR5-DE_LUGO-V03-001`, `YS-CMR5-DE_LUGO-V03-002`.

### Anson Sioux

Retained moderate source-bounded readiness across V01,V02. Battlefield cognition, retreat and actual family contact produce different voices and priorities. Narrative outcome limits prevent treating later references or Mary's remembered father as new contemporaneous Anson behavior.

**Supported domains.** Direct battlefield anguish, faith and error recognition; Practical retreat after political misjudgment; Family regret, unequal evacuation connections and tenderness; Homeland preservation and future-seed duty.

**Remaining gaps.** Long adult peacetime speech repertoire; Detailed household routines and tastes; Post-death motives; Unobserved private marriage chronology.

**Countercontrols.** Patriotic duty and regret over lost family time coexist. Recognizing strategic error does not prove total political clarity. Family tenderness must not become invented domestic scenes.

**Diagnostic route.** `YS-CMR5-ANSON_SIOUX-V01-001`, `YS-CMR5-ANSON_SIOUX-V02-001`, `YS-CMR5-ANSON_SIOUX-V02-002`.

### Adelheid von Schugel

Retained moderate technical/religious specialist class. Two V01 experiment stages and later V09 presentation distinguish pre/post-claim behavior, actual participation in risk and repeated formal engineering voice. Tanya's disabled-safety inference and Schugel's claims of shared faith remain attributed rather than asserted as transparent truth.

**Supported domains.** Technical defense and experiment-user risk calibration; Newly devotional self-description and commanded tests; Own bodily exposure as scientific-sacrifice defense; Later friendly/forceful technical-religious fellowship.

**Remaining gaps.** Civilian/private sociality; Full miracle continuation not reopened in this package; Objective truth of revelation beyond scene-specific evidence; Stable safety calibration in unobserved devices.

**Countercontrols.** His exposure means he does not merely endanger others from complete safety. Tanya's supposed fellowship is not her actual belief. The existence of an exit apparatus does not establish harmlessness or consent.

**Diagnostic route.** `YS-CMR5-SCHUGEL-V01-001`, `YS-CMR5-SCHUGEL-V01-002`, `YS-CMR5-SCHUGEL-V09-001`.

### Meybert

Revised to narrow, provisional DOMAIN_BOUNDED for artillery/combined-arms duty, garrison adjustment and known-colleague interaction. Actual V09 focal cognition and multiple upward/downward/familiar speech transformations, plus independent V14 shock reporting and V05 observer counterhistory, overcome the frozen audit's lack of speaker-attributed breadth in this limited domain. No full-spectrum, unrestricted voice or broad civilian promotion; predictive fidelity still requires independent QA.

**Supported domains.** Ordinary garrison discomfort, self-correction and colleague humor; Direct role distribution, property tradeoff and accountability; Upward impossibility report and conditional responsibility pressure; Subordinate close-defense orders; Later shock-induced stammering and explicit uncertainty.

**Remaining gaps.** Civilian/private baseline; Intimate and stranger conversation; Long casual dialogue beyond known colleague; Full successful rescue outcome after V14 dispatch.

**Countercontrols.** Conditional shelling offer is communicative pressure, not observed indiscriminate fire. Property damage is justified inside an urgent episode, not a generic lawless disposition. Do not turn early observer criticism into timeless incompetence. Late stammering is a state change, not stable incapacity.

**Diagnostic route.** `YS-CMR5-MEYBERT-V09-001`, `YS-CMR5-MEYBERT-V09-002`, `YS-CMR5-MEYBERT-V09-003`, `YS-CMR5-MEYBERT-V14-001`, `YS-CMR5-MEYBERT-V05-001`.

### Tospan

Retained recognition at moderate confidence. V09 supplies direct self-qualified colleague speech and V14 clear cooperative action, but several nearby decisions and most rescue banter belong to Meybert/Ahrens. Independent interiority and diversified role-conditioned speech remain too thin for a reliable generative domain model. Recognition is strengthened; absence of promotion is not a claim of source insufficiency.

**Supported domains.** Ordinary uniform discomfort; Respectful factual correction of Meybert; Hesitation about the outsider metaphor; Formal/familiar support request; Direct late infantry/tank cooperation.

**Remaining gaps.** Independent complex private decision cases; Wide speaker-attributed command/register repertoire; Adult civilian/private baseline; Reliable spontaneous long dialogue.

**Countercontrols.** Do not inherit Meybert's stronger outsider formulation, private thought or sharp register. V09 deployment is Meybert's expectation, not a directly shown action there. Ahrens's kissing joke is not Tospan's romantic intention or an actual kiss.

**Diagnostic route.** `YS-CMR5-TOSPAN-V09-001`, `YS-CMR5-TOSPAN-V09-002`, `YS-CMR5-TOSPAN-V14-001`, `YS-CMR5-TOSPAN-V05-001`.

### Josef

Retained recognition. V04 textbook/WTN presentation cannot establish favorite wine, neutral voice or psychiatric diagnosis. V06 secretary questions add tightly contextual official speech despite absent proper-name label in those lines; they do not establish a neutral private self. Frozen alias retrieval missed this rank-only exchange and remains unchanged.

**Supported domains.** Satirical ideological presentation recognized as mediated; Contextually attributed secretary inquiry about information and mobilization; Loria's rank-sensitive reaction.

**Remaining gaps.** Explicit named attribution in the supplemental secretary exchange; Independent neutral interiority; Ordinary neutral conversation, tastes and hobbies; Broad action/relation repertoire.

**Countercontrols.** Textbook benevolence is propaganda diction, not transparent private motive. Contextual speaker identification must retain its qualification. Rational official questions coexist with terror-filtered information.

**Diagnostic route.** `YS-CMR5-JOSEF-V04-001`, `YS-CMR5-JOSEF-V06-001`.

### Igor Gassman

Newly audited supplementary subject. V06,V07,V14 actual Japanese episodes support bounded negotiation/staff/cultural-work behavior with different relationships and public/self-directed registers. Direct private calculation and limits justify a compact professional domain model after the global gate; not a full life. This is source-based discovery, not automatic promotion from V2 importance or name counts.

**Supported domains.** Interested peace mediation and restraint on further gain; Foreign-peer bargaining with diplomatic directness; Staff evidence tests and interpretation of political silence; Direct late cultural regret and self-recognition; Work-linked cigar reflection and admitted operational limits.

**Remaining gaps.** Household, intimate and neutral civilian baseline; Full chronological role transitions; Independently adjudicated administrative superiority; Generic unbounded comic-diplomat speech.

**Countercontrols.** Peace and profit coexist; neither pure altruism nor unbounded profiteering. Claimed objectivity and claimed administrative skill are character positions. Foreign rank does not imply shared command authority. Cigar reflection is narrated; favorite brand is unknown.

**Diagnostic route.** `YS-CMR5-GASSMAN-V06-001`, `YS-CMR5-GASSMAN-V07-001`, `YS-CMR5-GASSMAN-V14-001`.

### Erya

New limited recognition subject based on a single contiguous V01 early peer episode. The relationship is materially useful for Visha's pre-Tanya personhood; Erya's own voice is distinguishable but independent causal coverage is sparse. One source episode does not justify a broader generative subject or an insufficient-source verdict on unread material.

**Supported domains.** Visha friendship, wake-up and food teasing; Rumor-bearing playful peer speech; Assignment difference and farewell-day context.

**Remaining gaps.** Independent interiority; Later trajectory; Family/full-name details; Adult command or civilian behavior; Reliable spontaneous broad dialogue.

**Countercontrols.** Keep Erya's 私/君/だよ speech distinct from Visha's 貴女/わ/かしら. The tea-behind-lines joke is not a favorite drink. Visha's affectionate perspective is not Erya's interiority.

**Diagnostic route.** `YS-CMR5-ERYA-V01-001`.

### Tanya Degurechaff

Tanya is deliberately not duplicated in YS-CMR5. Parent separately owns CMR2 source work, model and QA, including V13/V14 candidate closure. This pointer marks ownership, not source completion or an inferred class decision.

**Remaining gaps.** Root owns Tanya source closure and independent QA; this entry must be replaced or linked to the exact root decision before the full initial20 audit is claimed complete..

**Root-owned current inventory.** 814 ordinary textual diagnostics plus one separate image witness. Source closure is not a model/QA pass; use the existing Tanya navigation and the root-owned decision.


## Open focused audits and withdrawn-name history

The seven current candidates below remain `NOT_YET_AUDITED_FOCUSED_CHARACTER_PACKAGE`, with no readiness confidence assigned. Incidental appearances in another subject’s fit context do not complete an independent character audit. Absence from the present targeted sample does not establish insufficient available source. Build independent speaker/focalizer-attributed windows across relevant states before a readiness decision; fit-excluded QA outcomes are not new fit witnesses.

| Candidate | Current focused-audit status | Recorded encounter routes |
|---|---|---|
| Elmar Ahrens | NOT_YET_AUDITED | `YS-CMR0-V05-029-00294`, `YS-CMR0-V05-029-00296`, `YS-CMR0-V09-031-00218`, `YS-CMR0-V14-019-00179`, `YS-CMR0-V14-019-00181` |
| Mikel | NOT_YET_AUDITED | `YS-CMR0-V06-019-00272`, `YS-CMR0-V06-019-00273`, `YS-CMR0-V06-019-00321` |
| Liliya | NOT_YET_AUDITED | `YS-CMR0-V05-029-00049`, `YS-CMR0-V06-019-00306` |
| Johnson | NOT_YET_AUDITED | `YS-CMR0-V04-023-00381` |
| Thon | NOT_YET_AUDITED | `YS-CMR0-V05-029-00315`, `YS-CMR0-V05-029-00318` |
| Wustemann | NOT_YET_AUDITED | `YS-CMR0-V05-029-00323`, `YS-CMR0-V06-013-00485`, `YS-CMR0-V06-013-00490`, `YS-CMR0-V06-013-00494` |
| Klam | NOT_YET_AUDITED | `YS-CMR0-V08-025-00531`, `YS-CMR0-V08-025-00532`, `YS-CMR0-V08-025-00533`, `YS-CMR0-V08-025-00538`, `YS-CMR0-V08-025-00542` |

The sealed historical gap file contained an eighth tentative label, `RUDER`/“Ruder.” The subsequent source notice `YS-CMR5-GAP-NAME-CORRECTION-001` withdraws it as working-note shorthand for **Rudersdorf**, rather than an established separate person. The reviewer’s full exact-CMR0 and mature-V2 separate-name searches found no corresponding independent route; the actual `YS-CMR0-V10-016-00054` counterpart is Rudersdorf. This is a name-establishment correction, not an insufficient-source classification.

The machine ledger retains the old row under `WITHDRAWN_TENTATIVE_NAME` with its complete historical values and the notice; it is excluded from the current seven-candidate list. The original eight-row gap bytes/hash and original review bytes/hash remain unchanged. A future independent discovery of a different person would require its own source establishment rather than reuse of this withdrawn label.

## Ensemble schema and exact source reopening

<a id="ensemble-schema"></a>

Each `youjo-senki/ensemble-character-diagnostic/v1` record uses `active_provisional` analytical status, its original stable diagnostic/character IDs, and a provenance reference to this document. The original analytical schema is deliberately preserved so no English finding is replaced by a generic roster capsule.

| Field | Meaning and preservation rule |
|---|---|
| `record_kind`, `source_use` | Ordinary source diagnostic, separately mediated recognition control, or excluded author/adaptation mode-control. The kind does not itself grant a generative model. |
| `diagnostic_id`, `character_id`, `review_status` | Exact stable input identities and literal source-review status. |
| `source` | Original safe source file/Drive ID, container hash, volume, member, spine, paragraph, locator ID and normalized-text hash; verified OPF/member hash added. Numeric coordinates are typed as integers. |
| `read_window` | Original actually read first/end IDs, count, joined-text hash, access split and false container-reopen flag. “Actual read” describes the sealed source reviewer, not a second Japanese read by the porter. |
| `bounded_finding` | Complete supported English analytical finding. |
| `five_channels` | Separate private cognition, conduct, delivered/documentary/self speech, external interpretation and institutional consequence; null remains unavailable. |
| `speaker_attribution`, `focalizer_attribution` | Literal identity, certainty and segmented-access statements; overall confidence does not upgrade them. |
| `written_japanese_register` | Preserved written-language analysis and small forms; eight connected examples were separated into the same attested forms with English explanation. Negative/private/narrative forms retain their original restriction. No audio accent, pitch or timing is supplied. |
| `developmental_state`, optional `rank_role`/`interlocutor` | Original provided conditions. Other scene/stakes/state qualifications remain in the finding/channels/ceiling; missing structured conditions are not invented. |
| `inference_ceiling`, `counterevidence_or_exception` | Complete preserved scope, uncertainty and countercase. |
| `evidence_class`, `confidence` | Literal source finding class/band, including statement-, presentation-, report- and attribution-bounded confidence. |
| Optional `narrative_mode`, `usable_for_behavioral_model` | Original explicit mode/exclusion controls; Mary’s exclusion remains false. |
| `review_basis`, `provenance_ref` | Inherited contiguous-source adjudication and complete analytical port read, with no duplicate primary reopen claim. |

Find an exact diagnostic ID in [the ensemble JSONL](../Diagnostics/ENSEMBLE_CHARACTER_DIAGNOSTICS.jsonl), then resolve its `source_drive_id` through the [Drive disposition inventory](YOUJO_SENKI_CMR_DRIVE_DISPOSITION.jsonl). Open the hash-matching EPUB, navigate to the exact member/spine/paragraph, and use `locator_id`/`text_sha256` to confirm normalized text. The diagnostic and source window must both be consulted for speaker/focalizer and narrative context. A string tagged “dialogue” by extraction can still be thought, writing, another actor’s line or paratext.

`source.locator` preview strings and duplicate Japanese `source.section_label` strings were omitted. Exact ID/member/paragraph/hash routes remain complete. The original raw source and normalized locator corpus remain evidence inputs; no raw Japanese scene paragraphs or source-text dump is placed in these three Git artifacts.

## Machine readiness ledger and controlled transformation manifest

The ledger’s `PORT_MANIFEST` record describes all input SHA-256 values, source scope/counts, the complete safe field map, source-mode exclusions, the four pre-seal draft corrections, eight lexical transformations, the withdrawn-name notice and port validation scope. `READINESS_ASSESSMENT` rows preserve the source decision/class/confidence, complete supported/gap domains, countercontrols, diagnostic usage lists and window coordinates. Source assessment status is separated from the derivative’s provisional authority status.

The `TANYA_OWNER_POINTER` preserves its original null class/QA decision and adds only the known root-owned 814-diagnostic inventory snapshot and existing navigation route. `NOT_YET_AUDITED_CANDIDATE` records preserve all seven current gap records and enrich their encountered routes with verified source/member metadata. `WITHDRAWN_TENTATIVE_NAME` preserves the eighth old row as history with its corrective notice.

Four draft corrections occurred **before the canonical95 seal**: Grantz V03 scene/attribution, Erya V01 anchor/voice, Drake V04 notice-prefix wording and Gassman V06 removal of forms imported from another window. Their before/after record hashes and corrected fields remain in the manifest. Historical tranche scripts are not current serialized inputs. The analytical port does not modify the sealed95 source records.

The eight written-register transformations separate connected line examples for Visha V06, Weiss V14, Lergen V10/V14, Zettour V14, Grantz V14, Uger V10 and Mary V04. They preserve the same attested small forms and behavioral/pragmatic interpretation; every English substantive finding/channel/attribution/limit remains unchanged. The machine manifest records IDs, fields, before/after value hashes and transformation policy; the private review receipt retains the exact before/after strings.

## Input integrity and validation

| Sealed source input | Bytes | SHA-256 |
|---|---:|---|
| `character_source_diagnostics.jsonl` | 245460 | `4a8c958318269d016c811b6267725d9bb2114b67f09be7bf9a5d17b0c79e8122` |
| `character_readiness_reaudit.jsonl` | 96462 | `e3c5634277a857b789a556953ab226237415d892559f10d8299b8679b3be2799` |
| `source_readiness_review.md` | 44666 | `5682b0ff05116f33653f723277692c6a7655bde9cad2befc46cadaf1b32c668b` |
| `character_source_package_seal.json` | 3403 | `cdf35c5d16a1c28f040df797061f07473361b0d166256a2c40fcc72b8a58ab67` |
| `character_source_package_validation.json` | 816 | `f14a7775a79bafbfb582c9c4b8ac596e6e011ef16056269cb7b7d41c762fe5a2` |
| `character_source_diagnostic_corrections.jsonl` | 2181 | `f62727d94611f3e498ef6fd2493233dd8dd2480d67b08191ffcb07316e1e4234` |
| `character_candidate_gap_register.jsonl` | 10794 | `61143085057108a22b8edbef776452d942013b8b9a18b233ce40996d69fcbf5e` |
| `character_source_windows_manifest.json` | 44939 | `a29bec3b3b8e4e95ddb1797f9a474046e76baf886020008f7ae6faa029139528` |
| `candidate_gap_name_correction_notice.json` | 1540 | `3446a4490e091d70ac0a5bc2a3fe16bfe9793caf616683bbd490a9b90c735d28` |

The frozen original first-readiness audit is 26,319 bytes, Drive ID `1LYRzJS4AL6jHAmIAjkaOC-HIWQQdBp51`, SHA-256 `30ace4c0f4a0b03aa003aea8e7377cb1595450bed326451908a59bf13c5c3417`. The unchanged44-row alias map is Drive ID `1C95SxSuba7Fr9diTMyc1N8q58TbzxsLs`, SHA-256 `567426240c2072a21e6abea40775fd2428a6aec433f85417da2c8de08a8161a9`.

The CMR0 locator corpus is Drive ID `140ow12czVj4J8Q_JR44MSWI98LUxj3uk`, 63,812 rows / 52,894,654 bytes, SHA-256 `c84fa4c8e0251730887b51913a8f32ea68c39be68ff4adae8d995d49292f5cfe`. It was reproduced identically from matching EPUBs; the giant current Drive body was not downloaded for this port. The member index is Drive ID `1GlDNvT5spgIQk5VaUU5S2Qsk5dF174hR`, 608 rows / 203,927 bytes, SHA-256 `e05b9fe26ec35e4590b9e148005b49f7ed142ec2f6ca2868e99561981372e220`.

Validation requires the exact sealed input hashes; all95 original stable IDs and substantive field mappings; 22 original assessment records; 61 window membership/joined-text hashes and 3,309 normalized-block hashes; primary source/member/OPF tuples; literal source certainty/five channels/limits; disjoint diagnostic usage roles; unchanged frozen initial20 classifications; Meybert’s sole initial class revision; two supplementary decisions; seven unaudited records plus one withdrawn label; and resolved source/correction references. Structural checks do not independently re-score semantics or predictive fidelity. The transformation receipt records the complete analytical reads and exact controlled substitutions. Each output is UTF-8 without BOM, LF and under1MiB; no private absolute path, raw scene-text export or live Drive URL is introduced.

