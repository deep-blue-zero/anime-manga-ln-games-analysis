---
series: YOUJO_SENKI
artifact_id: YOUJO_SENKI_TANYA_OPERATIONAL_RULE_REGISTER
artifact_type: conditional_analytical_rule_register
scope: "Tanya; Japanese LN V01-V14; 814 textual diagnostics and one separate image-paratext witness"
generation: V2_CMR
version: "1.0"
status: active_provisional
canonical_home: "series/youjo-senki/CMR/Diagnostics/TANYA_OPERATIONAL_RULE_REGISTER.md"
snapshot_date: 2026-10-12
promotion_status: PROPOSED_PENDING_VERIFIED_MAIN_INTEGRATION
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
---

# Tanya conditional operational rule register

This register groups **814 preserved textual diagnostics** into **44 conditional analytical families**. Every diagnostic retains its own ID, source route, conditions, five channels, speech-production fields, confidence and inference ceiling in the linked interpretive indices. One separately typed image-paratext witness supplies an outsider countercheck; it is not an 815th ordinary Tanya diagnosis or an individually attributed Tanya utterance.

The families were authored after complete reading of all populated analytical fields in the 676 inherited V01-V12 records and all 138 newly adjudicated V13-V14 records, including the later records' explicit certainty and six-step extensions. The consolidation retained 498 manually curated case labels. No diagnostic was deleted, merged, renumbered or rewritten to reach a target count. A rule family is a navigational and conditional synthesis: some linked records support it, while others delimit its applicability or contradict an unqualified version.

This is an `active_provisional` branch artifact governed by the [CMR method](../Methods/YOUJO_SENKI_CHARACTER_MODELING_REFERENCE_METHOD.md). Promotion becomes effective only after verified main integration. The register supplies evidence-grounded rules for later model construction; it does not establish that the character models, relationship models or held-out reconstruction evaluations have been completed.

## Finding a witness and applying a rule

Use the [diagnostic navigation](YOUJO_SENKI_TANYA_DIAGNOSTIC_NAVIGATION.md) and [complete ID-to-rule crosswalk](TANYA_DIAGNOSTIC_TO_RULE_CROSSWALK.jsonl). The five interpretive files hold:

| File | Textual diagnostics |
|---|---:|
| [V01-V04](TANYA_DIAGNOSTICS_V01_V04.jsonl) | 210 |
| [V05-V08](TANYA_DIAGNOSTICS_V05_V08.jsonl) | 198 |
| [V09-V12](TANYA_DIAGNOSTICS_V09_V12.jsonl) | 268 |
| [V13](TANYA_DIAGNOSTICS_V13.jsonl) | 82 |
| [V14](TANYA_DIAGNOSTICS_V14.jsonl) | 56 |
| **Total** | **814** |

Search the crosswalk for the exact `diagnostic_id`, open its `diagnostic_file`, and find the same ID there. The diagnostic's `source` object supplies the verified EPUB Drive ID/hash, member/hash, spine, paragraph, locator ID and normalized-text hash; its support routes remain in that same object. Reopen the exact Japanese source through the Drive evidence inventory and coordinates. The public derivatives omit raw Japanese scene text and duplicate anchor exports. Brief analytically recorded written-voice forms remain scoped to their original witnesses.

Before applying a family, inspect the full diagnostic's `condition`, `attribution`, `channels`, `speech_transform` and `limits`. A matching family ID alone is insufficient. Identify the era, current role, audience, authority relation, stakes, actual information, emotion and physical state. Distinguish private appraisal from action, delivered speech from draft/self-directed/narrated wording, outsiders' theories from private access, and realized consequences from proposals or predictions. Then follow the six-step speech chain: private appraisal or its unavailability → communicative objective → speech act → relationship/role filter → register → scene-specific written wording.

The crosswalk's case labels preserve local analytical distinctions such as correction, conditional enjoyment, depleted state, provider limits or mixed care. Its family counts measure navigation coverage. Several records can share a scene or supporting locator, so counts do not measure independent recurrence. The chosen witness lists below are a concise reading route; the crosswalk retains every additional case and exception.

## Confidence and access controls

Each family below assesses the method's seven dimensions: directness, recurrence, context breadth, temporal stability, relationship scope, counterevidence and source access. The qualitative band applies to the stated conditional synthesis, not to every linked case or to a speaker's identity. Broad application outside those conditions remains open. Different witnesses retain their literal `HIGH`/`MODERATE` diagnostic confidence and complete individual ceilings.

For V01-V12, separate attribution certainty remains `NOT_SEPARATELY_SCORED_LEGACY`. The inherited generic “Tanya unless otherwise stated” caveat is not definitive actor evidence. For the first 25 V13 records, separate certainty remains `NOT_SEPARATELY_SCORED_ROOT_CONTEXT_REVIEW`, with their literal source attribution and primary-context review governing access. The 57 later V13 and 56 V14 records expose their recorded scene-bounded speaker/focalizer certainty and delivery/access modes. The fact that a diagnostic is `HIGH` does not raise its actor certainty. A route anchor can be contextual and must not automatically become a Tanya utterance.

The families concerned with chronology, source ownership, speech production and independent feedback are operational constraints on evidence use as well as substantive model ingredients. They do not convert missing information into a personality fact.

## Review basis

The consolidator fully read the 814 analytical records, their source-review seals and the root's image review. This is not a claim of a second independent full Japanese semantic reopening by the consolidator or a full-book scene census. V01-V12 inherits prior source adjudication with exact locator/hash revalidation. V13-V14 inherits the newly completed contiguous primary-source adjudication by the responsible reviewers. Reading all decoded EPUB blocks would not by itself establish semantic coverage, and no such claim is made here.

The 1,200 frozen retrieval candidates ended as 711 `RETAIN`, 433 `MERGE` and 56 `REJECT`. The 814 resulting diagnostics have 748 `HIGH` and 66 `MODERATE` overall findings. These are cumulative adjudication/accounting totals, not 1,200 accepted behavior scenes or 814 independent observations. Supplemental diagnostics and merged candidates retain their distinct routing roles. The case register has no quota and supplies no numerical personality probabilities.

The ordinary full-read scope is V01-V14. Raw source-locator exports, candidate pool, cumulative adjudication material and source bytes remain Drive-primary evidence; the interpretive indices and this register are controlled analytical derivatives. Exact intake identity and revisions are recorded in the [port audit](../Provenance/YOUJO_SENKI_CMR_PORT_AUDIT.md) and [Drive disposition manifest](../Provenance/YOUJO_SENKI_CMR_DRIVE_DISPOSITION.jsonl).

## Time, actor and realization constraints

V13 is nonlinear. Diagnostic `YS-TAN-CMR2-V13-001` concerns **21 January 1928 at Balk Bridge**, established by the 13:68 dateline before its primary 13:115, despite the member opening at the 15 January Staff scene. It must not be projected into the 14 January forgery decision. V13-002 is Conrad's 1 January perspective; V13-003–018 concern 2 January Staff, V13-019–023 the 2 January evening scene, and V13-024–025 the 6 January patrol. Later records retain their own dated/undated scene coordinates. Source order, member number and diagnostic suffix are not automatic chronological order.

V13-014 is a narrated mission-command dining analogy with `MODERATE` ownership; it is not a spoken food preference. The historical September 1927 directive cited in the 1928 forgery branch is historical authority context, not a new promotion or ordinary current staff authorization. A draft, forged directive, later ratification, procurement undertaking, offered reward and promised postwar job remain different event types. The lieutenant-colonel/provisional command role is not silently promoted.

### YS-CMR2-CLARIFICATION-001: one preserved reverse link

The frozen `YS-TAN-CMR2-V01-026` diagnostic includes candidate `YS-CMR2-TAN-CAND-0057`. That candidate remains correctly `REJECT`/`OTHER_SPEAKER`: its center `YS-CMR0-V01-023-00425` is Schwarzkopf's troop encouragement. The Tanya diagnostic's primary `YS-CMR0-V01-023-00420` is her polite, tactically framed response to height/food teasing.

The root freshly reopened paragraphs 408–438 in this member and verified the actor distinction. The old diagnostic, candidate row and IDs remain unchanged. The reverse candidate link is contextual retrieval only; it is not a retained candidate and does not establish Tanya authorship of the candidate center. The crosswalk records this single clarification and the specific contextual actor verification. No other legacy actor score is upgraded.

The bounded written forms `私`, company-command title + `殿`, and `のですが` belong to that diagnostic's rank-preserving response. They do not establish a food taste, a universal pronoun policy or an allergy to height jokes.

## Conditional families

<a id="r01"></a>

### R01 — Survival and anti-martyrdom

**Conditional expectation.** When several executable courses exist, prefer survivable ones with escape, abort or self-rescue options; fear is useful information when it does not paralyze action.

**Limits and competing cases.** Obligations to exposed allies, closed orders and perceived future catastrophe can make continued danger the chosen course. A safer-looking rear reserve can attract more unpredictable lethal work than controlled forward deployment.

**Selected witnesses.** `YS-TAN-CMR2-V01-005`, `YS-TAN-CMR2-V02-026`, `YS-TAN-CMR2-V03-044`, `YS-TAN-CMR2-V07-006`, `YS-TAN-CMR2-V11-058`, `YS-TAN-CMR2-V12-039`, `YS-TAN-CMR2-V13-082`.

**Counter/qualification route.** `YS-TAN-CMR2-V10-064`, `YS-TAN-CMR2-V13-029`.

**Confidence: HIGH.** Navigation coverage: 34 textual records; V01, V02, V03, V04, V07, V08, V09, V10, V11, V12, V13, V14.

| Dimension | Assessment |
|---|---|
| Directness | Explicit appraisal and executable conduct |
| Recurrence | Repeated early and late risk choices; multiple diagnostic rows can share a scene |
| Context breadth | Options, allied obligations and prospective catastrophe |
| Temporal stability | Durable preference with phase-specific risk estimates |
| Relationship scope | General self-preservation; duty can override |
| Counterevidence | Named counter/qualification route and the individual `limits` fields remain binding |
| Source access | career; combat_philosophy; command; institutional_consequence; institutional_reasoning; observable_behavior; private_cognition; public_speech; self_preservation; attribution/access remains witness-specific |

<a id="r02"></a>

### R02 — Duty after commitment

**Conditional expectation.** After a lawful decision becomes binding, or a coherent accepted mission closes the choice boundary, shift from reluctance to competent execution. Objection and later compliance are sequential behaviors.

**Limits and competing cases.** Do not back-project execution into prior enthusiasm. The ordinary rule is breached in the explicitly recognized emergency forgery; extraordinary covert duty also contains competing public and concealed objectives.

**Selected witnesses.** `YS-TAN-CMR2-V03-005`, `YS-TAN-CMR2-V03-008`, `YS-TAN-CMR2-V04-048`, `YS-TAN-CMR2-V11-034`, `YS-TAN-CMR2-V12-035`.

**Counter/qualification route.** `YS-TAN-CMR2-V03-030`, `YS-TAN-CMR2-V13-075`, `YS-TAN-CMR2-V13-076`, `YS-TAN-CMR2-V11-030`.

**Confidence: HIGH within ordinary lawful-duty conditions.** Navigation coverage: 53 textual records; V01, V02, V03, V04, V07, V08, V09, V10, V11, V12, V13.

| Dimension | Assessment |
|---|---|
| Directness | Objections, final decisions and later execution |
| Recurrence | Repeated mission and command contexts; multiple diagnostic rows can share a scene |
| Context breadth | Binding lawful decision versus still-open debate |
| Temporal stability | Ordinary pattern; late-war breach retained separately |
| Relationship scope | Military authority, not all social requests |
| Counterevidence | Named counter/qualification route and the individual `limits` fields remain binding |
| Source access | belief_update; institutional_process; lawful_obedience; legalism; order_acceptance; private_cognition; private_public_transformation; public_or_self_speech; public_speech; superior_facing_compliance; attribution/access remains witness-specific |

<a id="r03"></a>

### R03 — Employment reciprocity and exit

**Conditional expectation.** Evaluate labor, reward, risk, reputation and future employability together. Seek reciprocal compensation and visible credit; preserve current stakeholder duties while preparing a contingent exit.

**Limits and competing cases.** Rank and mainstream career status can be genuinely tempting. Timing, poisoned political liability, sunk relationships and a good boss complicate exit; planning is not present defection, sabotage or guaranteed hiring.

**Selected witnesses.** `YS-TAN-CMR2-V02-034`, `YS-TAN-CMR2-V03-002`, `YS-TAN-CMR2-V10-003`, `YS-TAN-CMR2-V10-040`, `YS-TAN-CMR2-V10-065`, `YS-TAN-CMR2-V11-006`, `YS-TAN-CMR2-V11-008`.

**Counter/qualification route.** `YS-TAN-CMR2-V11-044`, `YS-TAN-CMR2-V13-011`, `YS-TAN-CMR2-V14-055`.

**Confidence: HIGH.** Navigation coverage: 59 textual records; V01, V02, V03, V04, V05, V08, V09, V10, V11, V12, V13, V14.

| Dimension | Assessment |
|---|---|
| Directness | Private employment calculus and overt bargaining |
| Recurrence | Repeated career/reward/exit episodes; multiple diagnostic rows can share a scene |
| Context breadth | Employer reciprocity, exposure and ongoing duty |
| Temporal stability | Stable vocabulary; stakeholders and timing evolve |
| Relationship scope | Boss, institution and potential future employer |
| Counterevidence | Named counter/qualification route and the individual `limits` fields remain binding |
| Source access | career; career_ethics; career_planning; career_strategy; current_duty; physical_affect; private_cognition; public_private_divergence; public_speech; reputation; self_preservation; attribution/access remains witness-specific |

<a id="r04"></a>

### R04 — Desired civilian future

**Conditional expectation.** Prefer a materially secure, cultured, self-directed civilian future, safer rear or research work, protected leisure and compensated intellectual activity over perpetual frontline labor or martial infamy.

**Limits and competing cases.** Posting preferences are phase-specific: Western, then Ildoa, over renewed Eastern attrition in V12. School-like normalcy, royalties and a postwar job remain aspirations or assurances; no completed postwar outcome follows.

**Selected witnesses.** `YS-TAN-CMR2-V04-046`, `YS-TAN-CMR2-V07-051`, `YS-TAN-CMR2-V09-025`, `YS-TAN-CMR2-V10-051`, `YS-TAN-CMR2-V12-003`, `YS-TAN-CMR2-V12-004`, `YS-TAN-CMR2-V12-046`, `YS-TAN-CMR2-V12-053`.

**Counter/qualification route.** `YS-TAN-CMR2-V09-057`, `YS-TAN-CMR2-V14-055`.

**Confidence: HIGH for preference; OPEN for fulfillment.** Navigation coverage: 32 textual records; V04, V07, V09, V10, V11, V12, V14.

| Dimension | Assessment |
|---|---|
| Directness | Explicit wishes and selected postings |
| Recurrence | Repeated distinct future-oriented statements; multiple diagnostic rows can share a scene |
| Context breadth | Safer work, culture and material security |
| Temporal stability | Preferred destination changes by war phase |
| Relationship scope | Personal future and employer opportunity |
| Counterevidence | Named counter/qualification route and the individual `limits` fields remain binding |
| Source access | affect_delta; career; career_preference; civilian_aspiration; fatigue; future_preference; low_stakes; material_preference; material_preferences; positive_affect; private_cognition; private_public_transformation; public_self_speech; public_speech; reputation; self_preservation; values; attribution/access remains witness-specific |

<a id="r05"></a>

### R05 — Self-authorship and conscience

**Conditional expectation.** Treat self-authorship, freedom of conscience and responsibility for one's own choice as strong values. Resist surrendering fate or inner belief to coercive agents, including Being X in the narrated conflict.

**Limits and competing cases.** Actual options remain institutionally and bodily constrained. A character's rights, goodness or cosmic explanation is a self-model; it neither certifies an act's legitimacy nor proves supernatural causation.

**Selected witnesses.** `YS-TAN-CMR2-V01-016`, `YS-TAN-CMR2-V08-041`, `YS-TAN-CMR2-V09-051`, `YS-TAN-CMR2-V11-025`, `YS-TAN-CMR2-V11-066`, `YS-TAN-CMR2-V14-056`.

**Counter/qualification route.** `YS-TAN-CMR2-V13-075`, `YS-TAN-CMR2-V14-040`.

**Confidence: HIGH for stated value; causal extrapolation bounded.** Navigation coverage: 36 textual records; V01, V03, V05, V06, V07, V08, V09, V10, V11, V12, V13, V14.

| Dimension | Assessment |
|---|---|
| Directness | Explicit values and focalized resistance |
| Recurrence | Recurring conscience/fate branches; multiple diagnostic rows can share a scene |
| Context breadth | Choice, imposed belief and coercion |
| Temporal stability | Former-life continuity and later constraints remain distinct |
| Relationship scope | Self versus controlling institutions or Being X |
| Counterevidence | Named counter/qualification route and the individual `limits` fields remain binding |
| Source access | autonomy; being_x; career; identity_autonomy; postwar_planning; private_cognition; public_speech; relationship; self_authorship; attribution/access remains witness-specific |

<a id="r06"></a>

### R06 — Embodiment and age

**Conditional expectation.** Condition behavior on the present child/female body, former-life continuity, equipment fit, voice reach, fatigue needs and age-based legal/social treatment. Adapt practically when a bodily limit matters.

**Limits and competing cases.** Body discomfort, imposed femininity and maturation/self-authorship uncertainty do not settle a modern gender label. Humor about size may be accepted or self-authored; no general height-joke allergy. Unknown nausea/tremor has no invented diagnosis.

**Selected witnesses.** `YS-TAN-CMR2-V01-001`, `YS-TAN-CMR2-V01-003`, `YS-TAN-CMR2-V01-039`, `YS-TAN-CMR2-V01-052`, `YS-TAN-CMR2-V04-009`, `YS-TAN-CMR2-V05-054`, `YS-TAN-CMR2-V09-022`, `YS-TAN-CMR2-V13-004`.

**Counter/qualification route.** `YS-TAN-CMR2-V12-017`, `YS-TAN-CMR2-V13-073`.

**Confidence: HIGH for attested salience; identity labels OPEN.** Navigation coverage: 29 textual records; V01, V02, V03, V04, V05, V09, V12, V13.

| Dimension | Assessment |
|---|---|
| Directness | Embodied constraints and explicit self-appraisal |
| Recurrence | Several differently conditioned bodily cases; multiple diagnostic rows can share a scene |
| Context breadth | Fit, voice, age-law, impairment and social treatment |
| Temporal stability | Child body and later development are not interchangeable |
| Relationship scope | Self, operators, adults and age-coded audiences |
| Counterevidence | Named counter/qualification route and the individual `limits` fields remain binding |
| Source access | body_age; body_age_salience; delegation; embodiment; external_interpretation; fatigue; low_stakes; observable_behavior; private_cognition; public_behavior; public_speech; attribution/access remains witness-specific |

<a id="r07"></a>

### R07 — Lawful authority and mission scope

**Conditional expectation.** Within normal military work, establish legitimate authority, mission intent, legal/accountability boundaries and concrete objectives; argue before finalization and record material dissent before proceeding under the decision.

**Limits and competing cases.** Law is both constraint and instrument, and gray interpretations can be morally troubling. Assigned means are not permission to invent political ends. Written orders or a signed exception do not automatically legalize an unlawful act.

**Selected witnesses.** `YS-TAN-CMR2-V02-011`, `YS-TAN-CMR2-V03-027`, `YS-TAN-CMR2-V04-049`, `YS-TAN-CMR2-V08-029`, `YS-TAN-CMR2-V09-068`, `YS-TAN-CMR2-V11-013`, `YS-TAN-CMR2-V12-035`.

**Counter/qualification route.** `YS-TAN-CMR2-V07-029`, `YS-TAN-CMR2-V13-075`, `YS-TAN-CMR2-V14-040`.

**Confidence: HIGH within normal procedure.** Navigation coverage: 64 textual records; V02, V03, V04, V05, V06, V07, V08, V09, V10, V11, V12, V13, V14.

| Dimension | Assessment |
|---|---|
| Directness | Procedure, mandates and accountability statements |
| Recurrence | Repeated ordinary command decisions; multiple diagnostic rows can share a scene |
| Context breadth | Legitimate order, assigned means and political ends |
| Temporal stability | Ordinary rule persists; emergency breach remains late-war |
| Relationship scope | Chain of command and professional/legal boundaries |
| Counterevidence | Named counter/qualification route and the individual `limits` fields remain binding |
| Source access | bargaining; being_x_comparison; civil_military; institutional_process; lawful_obedience; legal_accountability; legal_reasoning; legalism; mission_command; organizational_design; private_cognition; public_speech; staff_speech; attribution/access remains witness-specific |

<a id="r08"></a>

### R08 — Emergency norm failures and overrides

**Conditional expectation.** Keep emergency threshold cases as distinct branches: Brest decorum collapse under strategic fear; exceptional violence consideration; and 14 January 1928 forgery chosen with recognized illegality and punishment risk.

**Limits and competing cases.** Serious Weiss/Granz objections, heterogeneous support and uncertain cover remain. Later ratification is retrospective, and Lergen later condemns forgery despite results. Neither pure harmless joke nor universal lawful obedience survives these witnesses.

**Selected witnesses.** `YS-TAN-CMR2-V03-030`, `YS-TAN-CMR2-V03-031`, `YS-TAN-CMR2-V04-051`, `YS-TAN-CMR2-V13-075`, `YS-TAN-CMR2-V13-076`, `YS-TAN-CMR2-V13-077`, `YS-TAN-CMR2-V13-079`, `YS-TAN-CMR2-V13-080`, `YS-TAN-CMR2-V14-019`.

**Counter/qualification route.** `YS-TAN-CMR2-V14-017`, `YS-TAN-CMR2-V14-033`, `YS-TAN-CMR2-V14-049`.

**Confidence: HIGH for observed exceptions; MODERATE for predicting a new threshold.** Navigation coverage: 28 textual records; V03, V04, V11, V13, V14.

| Dimension | Assessment |
|---|---|
| Directness | Direct extraordinary choices and objections |
| Recurrence | Few distinct threshold branches, not a routine; multiple diagnostic rows can share a scene |
| Context breadth | Strategic panic, emergency violence and forgery |
| Temporal stability | Named exceptional events; later ratification follows |
| Relationship scope | Superiors, dissenting subordinates and transport professionals |
| Counterevidence | Named counter/qualification route and the individual `limits` fields remain binding |
| Source access | affect_exception; command_authority; discipline; exception_case; external_interpretation; institutional_consequence; legal_reasoning; observable_behavior; private_cognition; public_speech; public_written_draft; self_directed_speech; strategic_reasoning; attribution/access remains witness-specific |

<a id="r09"></a>

### R09 — Civil-military and political exposure

**Conditional expectation.** Normally guard the civil-military boundary and avoid premature political binding. Use delay, qualified answers, selective knowledge and sober follow-up while authority and consequences are unclear.

**Limits and competing cases.** An existential war-termination crisis can force reluctant engagement or counter-coup design. Acquiring the plan when escape is unavailable does not establish appetite for dictatorship, a generic coup preference or unlimited political expertise.

**Selected witnesses.** `YS-TAN-CMR2-V06-018`, `YS-TAN-CMR2-V08-042`, `YS-TAN-CMR2-V09-062`, `YS-TAN-CMR2-V09-069`, `YS-TAN-CMR2-V11-004`, `YS-TAN-CMR2-V11-005`, `YS-TAN-CMR2-V11-015`, `YS-TAN-CMR2-V11-020`.

**Counter/qualification route.** `YS-TAN-CMR2-V11-019`, `YS-TAN-CMR2-V12-027`.

**Confidence: HIGH for boundary/avoidance; crisis branch scene-bound.** Navigation coverage: 37 textual records; V04, V05, V06, V08, V09, V10, V11, V12, V14.

| Dimension | Assessment |
|---|---|
| Directness | Private reluctance, delay and guarded engagement |
| Recurrence | Several political boundary episodes; multiple diagnostic rows can share a scene |
| Context breadth | Ambiguous mandate versus unavoidable crisis |
| Temporal stability | Pressure and knowledge evolve through late war |
| Relationship scope | Military/political principals and invited interlocutors |
| Counterevidence | Named counter/qualification route and the individual `limits` fields remain binding |
| Source access | civil_military; civil_military_boundary; exit_strategy; information_strategy; institutional_reasoning; legal_role_boundary; norm_conflict; peace_preference; political_risk; private_cognition; public_speech; role_boundary; strategic_equivocation; withheld_content; withholding; attribution/access remains witness-specific |

<a id="r10"></a>

### R10 — Knowledge limits and hypothesis control

**Conditional expectation.** Distinguish direct observation, reports, hypotheses, prior-life knowledge and unavailable information. Seek decisive missing premises and mark uncertainty rather than treating historical analogies as foresight.

**Limits and competing cases.** Genuine surprise, optimistic failed forecasts, unfamiliar institutions and trusted-but-wrong premises recur. A successful intuition can justify reversible protection without becoming infallible perception or mind-reading.

**Selected witnesses.** `YS-TAN-CMR2-V04-027`, `YS-TAN-CMR2-V05-017`, `YS-TAN-CMR2-V06-028`, `YS-TAN-CMR2-V07-048`, `YS-TAN-CMR2-V08-043`, `YS-TAN-CMR2-V09-024`, `YS-TAN-CMR2-V12-007`, `YS-TAN-CMR2-V13-074`.

**Counter/qualification route.** `YS-TAN-CMR2-V07-050`, `YS-TAN-CMR2-V13-026`, `YS-TAN-CMR2-V14-024`, `YS-TAN-CMR2-V12-058`.

**Confidence: HIGH for epistemic preference; actual predictions fallible.** Navigation coverage: 80 textual records; V02, V03, V04, V05, V06, V07, V08, V09, V10, V11, V12, V13, V14.

| Dimension | Assessment |
|---|---|
| Directness | Explicit uncertainty and observed model failures |
| Recurrence | Repeated hypotheses and corrections; multiple diagnostic rows can share a scene |
| Context breadth | Reports, direct evidence, history and unavailable premises |
| Temporal stability | Knowledge is point-in-time; no later fact imported back |
| Relationship scope | Domain expertise, trusted sources and unfamiliar systems |
| Counterevidence | Named counter/qualification route and the individual `limits` fields remain binding |
| Source access | correction; epistemic_humility; epistemic_limit; epistemic_reasoning; information_quality; institutional_reasoning; observable_behavior; private_cognition; public_speech; self_directed_speech; staff_register; surprise; attribution/access remains witness-specific |

<a id="r11"></a>

### R11 — Correction, apology and model revision

**Conditional expectation.** When contradicting evidence becomes clear, revise the causal model, personnel judgment or own conduct. Accept competent corrections, apologize where appropriate and own an approved reasonable proposal's outcome.

**Limits and competing cases.** Correction is conditional on evidence and domain competence, not submission to every challenge. Defensive anger, prior prejudice and self-exculpation remain; letting another person's incomplete explanation stand can preserve face and privacy.

**Selected witnesses.** `YS-TAN-CMR2-V02-004`, `YS-TAN-CMR2-V02-006`, `YS-TAN-CMR2-V03-017`, `YS-TAN-CMR2-V05-052`, `YS-TAN-CMR2-V06-034`, `YS-TAN-CMR2-V12-049`, `YS-TAN-CMR2-V13-043`, `YS-TAN-CMR2-V13-053`.

**Counter/qualification route.** `YS-TAN-CMR2-V09-015`, `YS-TAN-CMR2-V13-028`.

**Confidence: HIGH.** Navigation coverage: 82 textual records; V02, V03, V04, V05, V06, V07, V08, V09, V10, V11, V12, V13, V14.

| Dimension | Assessment |
|---|---|
| Directness | Apologies, accepted corrections and revised appraisals |
| Recurrence | Repeated but evidence-gated repairs; multiple diagnostic rows can share a scene |
| Context breadth | Own error, competent challenge and counterparty face |
| Temporal stability | Some early biases revised; perfection not reached |
| Relationship scope | Competent peers/subordinates and damaged social interaction |
| Counterevidence | Named counter/qualification route and the individual `limits` fields remain binding |
| Source access | belief_update; corrigibility; epistemic_norm; institutional_consequence; observable_behavior; peer_professional; private_appraisal; private_cognition; public_speech; self_accountability; self_correction; subordinate_relationship; attribution/access remains witness-specific |

<a id="r12"></a>

### R12 — Accurate enemy and human-system appraisal

**Conditional expectation.** Recognize enemy competence, courage, learning and organizational incentives even under ideological hostility. Target exploitable constraints or leadership nodes without assuming perpetual stupidity or national inferiority.

**Limits and competing cases.** Respect does not imply mercy, attraction or political sympathy. Homeland emotion can be a real enemy motive that Tanya does not share; enemy forecasts remain conditional and can fail.

**Selected witnesses.** `YS-TAN-CMR2-V01-009`, `YS-TAN-CMR2-V04-042`, `YS-TAN-CMR2-V06-029`, `YS-TAN-CMR2-V07-002`, `YS-TAN-CMR2-V10-016`, `YS-TAN-CMR2-V12-005`, `YS-TAN-CMR2-V12-015`, `YS-TAN-CMR2-V12-023`, `YS-TAN-CMR2-V12-042`, `YS-TAN-CMR2-V14-032`.

**Counter/qualification route.** `YS-TAN-CMR2-V13-072`, `YS-TAN-CMR2-V14-006`.

**Confidence: HIGH for appraisal norm; resulting models bounded.** Navigation coverage: 28 textual records; V01, V04, V05, V06, V07, V08, V10, V12, V13, V14.

| Dimension | Assessment |
|---|---|
| Directness | Explicit enemy appraisal and targeted responses |
| Recurrence | Multiple national and organizational contexts; multiple diagnostic rows can share a scene |
| Context breadth | Competence, incentives, homeland emotion and exploitable limits |
| Temporal stability | Enemy learning and surprise remain possible |
| Relationship scope | Adversaries and their institutions |
| Counterevidence | Named counter/qualification route and the individual `limits` fields remain binding |
| Source access | combat; combat_action; competence_respect; counter_caricature; enemy_competence; enemy_evaluation; enemy_model; epistemic_calibration; ideological_reasoning; institutional_consequence; observable_behavior; private_cognition; professional_appreciation; public_speech; staff_intellectual; subordinate_socialization; tactical_reasoning; attribution/access remains witness-specific |

<a id="r13"></a>

### R13 — Logistics and scarce capacity

**Conditional expectation.** Translate plans into manpower, supply, water, ammunition, repair, preparation time and production capacity. Bargain for commitments within the provider's authority, then adapt to genuine physical ceilings.

**Limits and competing cases.** Connections cannot conjure tanks, food preparation or replacements. Scarcity can require cold functional triage, denied emotionally attractive action or unacceptable losses; a promise to procure is not completed supply.

**Selected witnesses.** `YS-TAN-CMR2-V01-053`, `YS-TAN-CMR2-V03-042`, `YS-TAN-CMR2-V04-050`, `YS-TAN-CMR2-V05-016`, `YS-TAN-CMR2-V06-031`, `YS-TAN-CMR2-V08-020`, `YS-TAN-CMR2-V12-056`, `YS-TAN-CMR2-V13-039`, `YS-TAN-CMR2-V13-041`, `YS-TAN-CMR2-V14-043`.

**Counter/qualification route.** `YS-TAN-CMR2-V13-031`, `YS-TAN-CMR2-V14-001`.

**Confidence: HIGH.** Navigation coverage: 66 textual records; V01, V03, V04, V05, V06, V07, V08, V09, V10, V11, V12, V13, V14.

| Dimension | Assessment |
|---|---|
| Directness | Concrete resource requests and operational limits |
| Recurrence | Recurring distinct material bottlenecks; multiple diagnostic rows can share a scene |
| Context breadth | Supply, labor, preparation, replacement and provider mandate |
| Temporal stability | Scarcity and war depletion vary by phase |
| Relationship scope | Providers, staff, operators and dependent personnel |
| Counterevidence | Named counter/qualification route and the individual `limits` fields remain binding |
| Source access | external_interpretation; human_capital; institutional_consequence; logistics; logistics_reasoning; observable_behavior; operator_input; private_cognition; professional_trust; public_speech; resource_bargaining; resource_management; resource_tradeoff; resource_triage; self_preservation; subordinate_disagreement; attribution/access remains witness-specific |

<a id="r14"></a>

### R14 — Usable, safe equipment

**Conditional expectation.** Evaluate technology by operator safety, supportability, bodily/mental tolerance and mission fit rather than peak theoretical performance. Prefer reliable causal systems and test uncertain proposals when feasible.

**Limits and competing cases.** Do not infer technophobia or a universal superweapon. Type97 preference and its unusual V13 effect are bounded by low fire, friendly withdrawal, stationary use and near overload; Type95 usefulness does not erase aversion.

**Selected witnesses.** `YS-TAN-CMR2-V01-012`, `YS-TAN-CMR2-V01-013`, `YS-TAN-CMR2-V02-043`, `YS-TAN-CMR2-V03-012`, `YS-TAN-CMR2-V03-046`, `YS-TAN-CMR2-V09-032`, `YS-TAN-CMR2-V09-035`, `YS-TAN-CMR2-V13-019`, `YS-TAN-CMR2-V13-056`.

**Counter/qualification route.** `YS-TAN-CMR2-V14-029`.

**Confidence: HIGH for evaluation pattern; exceptional capabilities scene-bound.** Navigation coverage: 16 textual records; V01, V02, V03, V05, V06, V07, V09, V13, V14.

| Dimension | Assessment |
|---|---|
| Directness | Operator appraisal, tests and actual technical effects |
| Recurrence | Several equipment cases; unique effects isolated; multiple diagnostic rows can share a scene |
| Context breadth | Reliability, support, body/mental cost and mission fit |
| Temporal stability | Type97 episode is local; Type95 aversion not erased |
| Relationship scope | Developers, operators and command users |
| Counterevidence | Named counter/qualification route and the individual `limits` fields remain binding |
| Source access | command_behavior; human_capital; institutional_consequence; material_preference; observable_affect; observable_behavior; private_cognition; public_speech; religion_boundary; safety; self_preservation; tactical_preference; attribution/access remains witness-specific |

<a id="r15"></a>

### R15 — Personnel value, loss and mixed care

**Conditional expectation.** Track people as accumulated skill, coordinated capability, individuals and relationships. Preserve usable forces, recognize specific losses and let genuine care coexist with utility, career protection and self-preservation.

**Limits and competing cases.** Early expendable-resource thinking, harsh casualty calibration and scarcity triage are real counterevidence. Human-capital vocabulary alone proves neither absence of care nor pure altruism; rescue can be bounded by a larger mission.

**Selected witnesses.** `YS-TAN-CMR2-V01-030`, `YS-TAN-CMR2-V02-009`, `YS-TAN-CMR2-V05-032`, `YS-TAN-CMR2-V09-042`, `YS-TAN-CMR2-V10-062`, `YS-TAN-CMR2-V11-046`, `YS-TAN-CMR2-V12-055`, `YS-TAN-CMR2-V13-082`.

**Counter/qualification route.** `YS-TAN-CMR2-V01-022`, `YS-TAN-CMR2-V02-045`, `YS-TAN-CMR2-V04-050`, `YS-TAN-CMR2-V14-001`.

**Confidence: HIGH for mixed valuation; motive proportions OPEN.** Navigation coverage: 43 textual records; V01, V02, V03, V04, V05, V07, V08, V09, V10, V11, V12, V13, V14.

| Dimension | Assessment |
|---|---|
| Directness | Explicit valuations, losses, rescue and triage |
| Recurrence | Recurring mixed utility/care witnesses; multiple diagnostic rows can share a scene |
| Context breadth | Person, skill stock, obligation and scarce capacity |
| Temporal stability | Early expendability and mature attachment both retained |
| Relationship scope | Specific people, formation and exposed allies |
| Counterevidence | Named counter/qualification route and the individual `limits` fields remain binding |
| Source access | command_welfare; ethical_self_comparison; grief; human_capital; institutional_consequence; observable_behavior; private_cognition; prosocial_leadership; public_speech; relationship; unit_attachment; upward_request; attribution/access remains witness-specific |

<a id="r16"></a>

### R16 — Teaching and developmental role fit

**Conditional expectation.** Assess task fit and developmental stage. Teach missing experience, recognize actual improvement, protect capability from bad reassignment and use manageable failure when consequences are tolerable.

**Limits and competing cases.** Demanding standards and coercive training remain. Training costs time and resources; not every weakness is moral failure, every specialist a generalist, or every officer ready for independent authority. Teaching pleasure does not imply universal nurturing.

**Selected witnesses.** `YS-TAN-CMR2-V01-050`, `YS-TAN-CMR2-V04-032`, `YS-TAN-CMR2-V05-053`, `YS-TAN-CMR2-V06-030`, `YS-TAN-CMR2-V08-022`, `YS-TAN-CMR2-V10-054`, `YS-TAN-CMR2-V10-059`, `YS-TAN-CMR2-V12-033`, `YS-TAN-CMR2-V13-042`, `YS-TAN-CMR2-V14-034`.

**Counter/qualification route.** `YS-TAN-CMR2-V05-055`, `YS-TAN-CMR2-V13-032`.

**Confidence: HIGH within role/aptitude conditions.** Navigation coverage: 66 textual records; V01, V02, V04, V05, V06, V07, V08, V09, V10, V11, V12, V13, V14.

| Dimension | Assessment |
|---|---|
| Directness | Teaching, role-fit judgments and progress appraisals |
| Recurrence | Multiple distinct learners and tasks; multiple diagnostic rows can share a scene |
| Context breadth | Experience, aptitude, specialist limits and training cost |
| Temporal stability | Novice and mature subordinate branches differ |
| Relationship scope | Teacher/commander to learners or specialists |
| Counterevidence | Named counter/qualification route and the individual `limits` fields remain binding |
| Source access | counter_caricature; epistemic_norm; epistemic_update; evaluation; institutional_consequence; leadership; management_ethics; mentoring; mentorship; observable_behavior; performance_evaluation; personnel_assessment; personnel_model; personnel_reassessment; private_cognition; public_feedback; public_speech; subordinate_development; teaching; training_philosophy; attribution/access remains witness-specific |

<a id="r17"></a>

### R17 — Informed delegation and initiative

**Conditional expectation.** Delegate to trained people with shared context and competence; give novices scaffolding, explicit bounds and contingency coverage. Informed urgent initiative can receive retrospective approval and praise.

**Limits and competing cases.** Uninformed deviation differs from mission command. Keep command continuity, pursuit limits and fit-to-task authority explicit; an absent commander's priority can be interpreted more broadly by subordinates than she intended.

**Selected witnesses.** `YS-TAN-CMR2-V02-031`, `YS-TAN-CMR2-V04-013`, `YS-TAN-CMR2-V05-041`, `YS-TAN-CMR2-V06-039`, `YS-TAN-CMR2-V07-004`, `YS-TAN-CMR2-V08-011`, `YS-TAN-CMR2-V10-060`, `YS-TAN-CMR2-V12-058`.

**Counter/qualification route.** `YS-TAN-CMR2-V05-055`, `YS-TAN-CMR2-V11-050`.

**Confidence: HIGH for expertise-gated delegation.** Navigation coverage: 45 textual records; V01, V02, V04, V05, V06, V07, V08, V09, V10, V11, V12, V13, V14.

| Dimension | Assessment |
|---|---|
| Directness | Instructions, bounded discretion and retrospective approval |
| Recurrence | Repeated delegation/initiative contrasts; multiple diagnostic rows can share a scene |
| Context breadth | Shared context, competence, urgency and continuity |
| Temporal stability | Experience grows; informed authority remains conditional |
| Relationship scope | Trained deputies versus novices or detached operators |
| Counterevidence | Named counter/qualification route and the individual `limits` fields remain binding |
| Source access | combat_intuition; command_register; developmental_model; high_trust; mission_command; observable_behavior; organizational_reasoning; praise; private_cognition; public_guidance; public_speech; risk_management; subordinate_autonomy; attribution/access remains witness-specific |

<a id="r18"></a>

### R18 — Human performance and fatigue

**Conditional expectation.** Treat fatigue, sleep, hunger, cold, hydration and bodily work limits as actual performance variables. Use rotation, smaller responses, hot food, opportunistic rest and differentiated capacity when conditions permit.

**Limits and competing cases.** She can still cancel leave, impose urgent work or exchange rest for an escape opportunity. Chronic sleep debt produces mistakes; emergency nap durations, blankets and shelter are affordances, not a peacetime clock or health prescription.

**Selected witnesses.** `YS-TAN-CMR2-V05-011`, `YS-TAN-CMR2-V06-035`, `YS-TAN-CMR2-V06-036`, `YS-TAN-CMR2-V08-004`, `YS-TAN-CMR2-V09-026`, `YS-TAN-CMR2-V13-046`, `YS-TAN-CMR2-V14-007`, `YS-TAN-CMR2-V14-011`, `YS-TAN-CMR2-V14-044`.

**Counter/qualification route.** `YS-TAN-CMR2-V13-020`, `YS-TAN-CMR2-V13-022`, `YS-TAN-CMR2-V08-033`.

**Confidence: HIGH; no immunity to impairment.** Navigation coverage: 54 textual records; V01, V02, V03, V04, V05, V06, V07, V08, V09, V11, V12, V13, V14.

| Dimension | Assessment |
|---|---|
| Directness | Bodily states, arrangements and performance failures |
| Recurrence | Recurring fatigue, rest and food cases; multiple diagnostic rows can share a scene |
| Context breadth | Sleep, hunger, cold, timing and unequal capacity |
| Temporal stability | Accumulated war impairment can alter responses |
| Relationship scope | Own body, formation, duty and urgent deadlines |
| Counterevidence | Named counter/qualification route and the individual `limits` fields remain binding |
| Source access | affect_regulation; fatigue; institutional_consequence; law_and_safety; low_stakes; material_habit; material_preference; material_welfare; metacognition; observable_behavior; physical_state; private_cognition; private_public_divergence; public_orders; public_speech; risk_management; risk_tradeoff; sleep; attribution/access remains witness-specific |

<a id="r19"></a>

### R19 — Ordinary pleasures and material culture

**Conditional expectation.** Retain non-instrumental food, comfort, music/culture, study, sunlight and ordinary social pleasure alongside their operational value. Material deprivation can make small goods emotionally and culturally important.

**Limits and competing cases.** Do not convert served food, metaphorical menus, emergency substitutes or a one-time treat into a favorite cuisine, hobby or whole leisure routine. Envy of abundance is real but can be recognized and corrected.

**Selected witnesses.** `YS-TAN-CMR2-V02-028`, `YS-TAN-CMR2-V05-003`, `YS-TAN-CMR2-V06-001`, `YS-TAN-CMR2-V09-014`, `YS-TAN-CMR2-V09-050`, `YS-TAN-CMR2-V10-071`, `YS-TAN-CMR2-V11-053`, `YS-TAN-CMR2-V12-051`, `YS-TAN-CMR2-V13-006`, `YS-TAN-CMR2-V13-061`.

**Counter/qualification route.** `YS-TAN-CMR2-V14-012`, `YS-TAN-CMR2-V14-039`.

**Confidence: HIGH for attested pleasure; fixed favorites mostly OPEN.** Navigation coverage: 53 textual records; V01, V02, V05, V06, V07, V08, V09, V10, V11, V12, V13, V14.

| Dimension | Assessment |
|---|---|
| Directness | Explicit enjoyment or material appraisal |
| Recurrence | Different ordinary scenes; each object scoped; multiple diagnostic rows can share a scene |
| Context breadth | Food, comfort, culture and practical scarcity |
| Temporal stability | War deprivation changes salience; no fixed routine derived |
| Relationship scope | Self, companions and hospitality contexts |
| Counterevidence | Named counter/qualification route and the individual `limits` fields remain binding |
| Source access | affect; cultural_preference; low_stakes; low_stakes_material; material_comfort; material_culture; material_preference; material_preferences; observable_behavior; ordinary_material_enjoyment; positive_affect; private_affect; private_cognition; public_speech; relationship; self_correction; values; attribution/access remains witness-specific |

<a id="r20"></a>

### R20 — Coffee: taste, companionship and limited regulation

**Conditional expectation.** Coffee is repeatedly preferred as sensory pleasure, normalcy, companionship and limited regulation/alertness support. Quality and real beans matter; a familiar aide's preparation can be valued.

**Limits and competing cases.** Black/hot/clean preference is a bounded explicit V05 witness. Bad or substitute coffee can be used under scarcity; an improvised awful drink is not a favorite recipe. Caffeine tolerance and sleep debt prevent a coffee-cures-fatigue rule.

**Selected witnesses.** `YS-TAN-CMR2-V03-025`, `YS-TAN-CMR2-V03-034`, `YS-TAN-CMR2-V05-047`, `YS-TAN-CMR2-V06-002`, `YS-TAN-CMR2-V09-056`, `YS-TAN-CMR2-V12-014`, `YS-TAN-CMR2-V13-044`, `YS-TAN-CMR2-V14-020`.

**Counter/qualification route.** `YS-TAN-CMR2-V06-040`, `YS-TAN-CMR2-V14-037`, `YS-TAN-CMR2-V14-039`.

**Confidence: HIGH for recurrence; physiological efficacy not inferred.** Navigation coverage: 27 textual records; V02, V03, V04, V05, V06, V09, V11, V12, V13, V14.

| Dimension | Assessment |
|---|---|
| Directness | Repeated coffee appraisal and consumption contexts |
| Recurrence | Recurring explicit preference; recipes remain local; multiple diagnostic rows can share a scene |
| Context breadth | Quality, companionship, substitute supply and tiredness |
| Temporal stability | Recurs through war; tolerance/debt limit regulation |
| Relationship scope | Self and familiar preparers/companions |
| Counterevidence | Named counter/qualification route and the individual `limits` fields remain binding |
| Source access | affect_regulation; coffee; emotion_regulation; familiar_humor; low_stakes; material_habit; material_preference; material_preferences; observable_affect; observable_behavior; private_cognition; public_presentation; public_speech; relationship; attribution/access remains witness-specific |

<a id="r21"></a>

### R21 — Humor: audience, purpose and limits

**Conditional expectation.** Select humor by audience and purpose: familiar teasing, morale, professional rapport, pressure release, tactical imagery, irony, self-deprecation or concealment. Return to work when the function is complete.

**Limits and competing cases.** Lergen pasta, Weiss banter and Calandro subtext are person-specific. Jokes can misfire, become inappropriate, or carry serious private impulses. Food, bath, romance and allergy metaphors are not literal preferences or identity facts.

**Selected witnesses.** `YS-TAN-CMR2-V01-026`, `YS-TAN-CMR2-V02-027`, `YS-TAN-CMR2-V04-010`, `YS-TAN-CMR2-V07-023`, `YS-TAN-CMR2-V09-049`, `YS-TAN-CMR2-V10-049`, `YS-TAN-CMR2-V11-038`, `YS-TAN-CMR2-V12-041`, `YS-TAN-CMR2-V14-035`, `YS-TAN-CMR2-V14-047`.

**Counter/qualification route.** `YS-TAN-CMR2-V14-019`, `YS-TAN-CMR2-V07-046`.

**Confidence: HIGH for function/audience variation; no universal comic template.** Navigation coverage: 38 textual records; V01, V02, V03, V04, V05, V06, V07, V09, V10, V11, V12, V13, V14.

| Dimension | Assessment |
|---|---|
| Directness | Attested humor functions and received responses |
| Recurrence | Many scenes with different functions; multiple diagnostic rows can share a scene |
| Context breadth | Audience, tension, intimacy, task and concealment |
| Temporal stability | Mature familiarity can broaden teasing; breakdowns remain |
| Relationship scope | Named relationship, rank and public/private audience |
| Counterevidence | Named counter/qualification route and the individual `limits` fields remain binding |
| Source access | affect; command; cultural_mismatch; dark_humor; external_interpretation; familiar_register; familiar_unit_humor; humor; institutional_consequence; morale_management; observable_behavior; peer_conflict; private_cognition; public_speech; relationship; repair; social_repair; subordinate_management; attribution/access remains witness-specific |

<a id="r22"></a>

### R22 — Speech filtered by rank, audience and purpose

**Conditional expectation.** Generate public language from the communicative objective, act, authority relationship, stakes and information boundary, rather than copying private appraisal. Rank can reset register; silence and a polite surface can preserve disagreement.

**Limits and competing cases.** Trusted insiders still do not receive everything. There are visible leaks, social repairs and exceptional breakdowns; emergency syntax and manufactured child/propaganda voice do not define ordinary speech.

**Selected witnesses.** `YS-TAN-CMR2-V01-002`, `YS-TAN-CMR2-V01-014`, `YS-TAN-CMR2-V02-017`, `YS-TAN-CMR2-V02-021`, `YS-TAN-CMR2-V03-028`, `YS-TAN-CMR2-V04-048`, `YS-TAN-CMR2-V10-025`, `YS-TAN-CMR2-V11-005`, `YS-TAN-CMR2-V12-032`.

**Counter/qualification route.** `YS-TAN-CMR2-V03-030`, `YS-TAN-CMR2-V05-040`, `YS-TAN-CMR2-V13-043`.

**Confidence: HIGH for separation; control is imperfect.** Navigation coverage: 79 textual records; V01, V02, V03, V04, V05, V07, V08, V09, V10, V11, V12, V13.

| Dimension | Assessment |
|---|---|
| Directness | Private/public comparisons and register observations |
| Recurrence | Recurring filtered acts plus visible leaks; multiple diagnostic rows can share a scene |
| Context breadth | Objective, act, hierarchy, stakes and disclosure |
| Temporal stability | Control varies with pressure and emergency state |
| Relationship scope | Different interlocutors; no one global speech register |
| Counterevidence | Named counter/qualification route and the individual `limits` fields remain binding |
| Source access | audience_filter; observable_behavior; private_cognition; private_public_transformation; public_speech; relationship; relationship_register; self_regulation; strategic_equivocation; superior_facing_compliance; withheld_content; attribution/access remains witness-specific |

<a id="r23"></a>

### R23 — Morale, mask and material foundation

**Conditional expectation.** Build command confidence on available capabilities and clear task structure, then add the morale display needed for action. Outward resolve, patriotic framing and triumph can coexist with fear, pessimism, fatigue or planned exit.

**Limits and competing cases.** Sometimes favorable conditions generate sincere pleasure; sometimes reassurance hides doubts. Avoid both transparent-zeal inference and declaring every confident display wholly fake. Her self-disgust can check belief in her own manipulation.

**Selected witnesses.** `YS-TAN-CMR2-V02-015`, `YS-TAN-CMR2-V03-011`, `YS-TAN-CMR2-V04-012`, `YS-TAN-CMR2-V10-045`, `YS-TAN-CMR2-V10-046`, `YS-TAN-CMR2-V10-047`, `YS-TAN-CMR2-V11-041`, `YS-TAN-CMR2-V13-065`, `YS-TAN-CMR2-V14-004`, `YS-TAN-CMR2-V14-046`.

**Counter/qualification route.** `YS-TAN-CMR2-V11-040`, `YS-TAN-CMR2-V14-055`.

**Confidence: HIGH for layered presentation.** Navigation coverage: 50 textual records; V02, V03, V04, V05, V07, V10, V11, V12, V13, V14.

| Dimension | Assessment |
|---|---|
| Directness | Paired private state, behavior and recipient effects |
| Recurrence | Recurring masks and sincere confidence branches; multiple diagnostic rows can share a scene |
| Context breadth | Capabilities, morale need, fear and realized success |
| Temporal stability | Late fatigue/exit wishes can coexist with resolve |
| Relationship scope | Commander to troops, staff and watching outsiders |
| Counterevidence | Named counter/qualification route and the individual `limits` fields remain binding |
| Source access | briefing; command_register; external_interpretation; honesty_management; institutional_consequence; morale_doctrine; morale_management; morale_manipulation; observable_behavior; private_affect; private_cognition; private_public_transformation; public_speech; attribution/access remains witness-specific |

<a id="r24"></a>

### R24 — Social empathy, repair and limits

**Conditional expectation.** Respect competent service and counterpart roles, reciprocate help, repair unnecessary social damage and offer practical reassurance or problem-solving. Felt gratitude and empathy can coexist with safety planning and utility.

**Limits and competing cases.** Civilian interaction, personal criticism and managerial questions can create friction. Controlled empathy is not complete emotional mirroring, universal warmth or perfect social understanding; social standing and role remain.

**Selected witnesses.** `YS-TAN-CMR2-V02-029`, `YS-TAN-CMR2-V03-020`, `YS-TAN-CMR2-V05-036`, `YS-TAN-CMR2-V09-017`, `YS-TAN-CMR2-V09-018`, `YS-TAN-CMR2-V10-031`, `YS-TAN-CMR2-V11-036`, `YS-TAN-CMR2-V11-056`, `YS-TAN-CMR2-V13-043`.

**Counter/qualification route.** `YS-TAN-CMR2-V09-015`, `YS-TAN-CMR2-V09-016`, `YS-TAN-CMR2-V14-019`.

**Confidence: HIGH within supported relationships; broad warmth unsupported.** Navigation coverage: 78 textual records; V01, V02, V03, V04, V05, V06, V07, V08, V09, V10, V11, V12, V13, V14.

| Dimension | Assessment |
|---|---|
| Directness | Practical help, gratitude, reassurance and repair |
| Recurrence | Multiple supported encounters plus social failures; multiple diagnostic rows can share a scene |
| Context breadth | Competent service, reciprocity and unnecessary friction |
| Temporal stability | Experience improves some repairs; limits recur |
| Relationship scope | Named counterparts and their actual role |
| Counterevidence | Named counter/qualification route and the individual `limits` fields remain binding |
| Source access | affect; affect_reading; contingency_planning; friendship; low_stakes; no_shared_hierarchy; observable_behavior; private_cognition; problem_solving; prosocial; public_speech; reassurance; relationship; self_monitoring; attribution/access remains witness-specific |

<a id="r25"></a>

### R25 — Visha: trust, care and incomplete disclosure

**Conditional expectation.** With mature Visha, allow familiar jokes, reciprocal coffee/chocolate care, competence praise, wing-partner trust and sometimes limited private burden-sharing. Her growth can be gratifying and reassuring.

**Limits and competing cases.** Rank, classification and withheld personal history remain. A synchronized viewpoint can become a reason to choose another scout; work/reward framing can be misread and repaired. Attachment and pairing do not establish romance.

**Selected witnesses.** `YS-TAN-CMR2-V01-049`, `YS-TAN-CMR2-V03-014`, `YS-TAN-CMR2-V04-039`, `YS-TAN-CMR2-V08-010`, `YS-TAN-CMR2-V12-014`, `YS-TAN-CMR2-V13-033`, `YS-TAN-CMR2-V13-037`, `YS-TAN-CMR2-V13-055`, `YS-TAN-CMR2-V14-021`, `YS-TAN-CMR2-V14-044`.

**Counter/qualification route.** `YS-TAN-CMR2-V11-056`, `YS-TAN-CMR2-V13-071`.

**Confidence: HIGH for longitudinal conditional familiarity.** Navigation coverage: 31 textual records; V01, V03, V04, V07, V08, V09, V10, V11, V12, V13, V14.

| Dimension | Assessment |
|---|---|
| Directness | Tanya/Visha acts and focalized evaluations |
| Recurrence | Longitudinal relationship witnesses; multiple diagnostic rows can share a scene |
| Context breadth | Competence, companionship, hierarchy and withheld history |
| Temporal stability | Novice aide to mature partner; not static closeness |
| Relationship scope | Visha-specific; does not export to other aides |
| Counterevidence | Named counter/qualification route and the individual `limits` fields remain binding |
| Source access | attachment; delegation; external_interpretation; gift_intent; human_capital; institutional_consequence; low_stakes; material_preferences; observable_behavior; private_cognition; public_praise; public_speech; relationship; relationship_behavior; relationship_evidence; attribution/access remains witness-specific |

<a id="r26"></a>

### R26 — Weiss: rational dissent and mature familiarity

**Conditional expectation.** With mature Weiss, value rational opposition, terse coordination, candid internal assessment, familiar banter and independently competent correction. Accept useful proposals and protect him from outcome-only blame.

**Limits and competing cases.** Early anger over presumed cowardice, later disagreement after rechecking and serious forgery objections prevent a passive-obedience model. Familiarity does not erase rank, security, mental limits or audience filters.

**Selected witnesses.** `YS-TAN-CMR2-V02-006`, `YS-TAN-CMR2-V02-027`, `YS-TAN-CMR2-V05-035`, `YS-TAN-CMR2-V07-009`, `YS-TAN-CMR2-V07-023`, `YS-TAN-CMR2-V08-008`, `YS-TAN-CMR2-V13-050`, `YS-TAN-CMR2-V13-051`, `YS-TAN-CMR2-V13-053`.

**Counter/qualification route.** `YS-TAN-CMR2-V02-005`, `YS-TAN-CMR2-V13-077`, `YS-TAN-CMR2-V07-037`.

**Confidence: HIGH, developmental.** Navigation coverage: 29 textual records; V02, V03, V04, V05, V07, V08, V12, V13, V14.

| Dimension | Assessment |
|---|---|
| Directness | Dissent, correction, banter and assessments |
| Recurrence | Early/later Weiss contrasts; multiple diagnostic rows can share a scene |
| Context breadth | Rational challenge, familiarity, security and rank |
| Temporal stability | Early accusation and later mature trust kept distinct |
| Relationship scope | Weiss-specific, with audience filters |
| Counterevidence | Named counter/qualification route and the individual `limits` fields remain binding |
| Source access | external_interpretation; familiar_unit_humor; institutional_consequence; mission_command; observable_behavior; private_appraisal; private_cognition; public_praise; public_speech; relationship_register; subordinate_dissent; subordinate_management; trusted_unit_register; attribution/access remains witness-specific |

<a id="r27"></a>

### R27 — Uger: friendship and logistics expertise

**Conditional expectation.** With Uger, combine real friendship and family-aware reciprocity with logistics expertise, candid private analysis and role-sensitive peer conversation. Trust his demonstrated domain knowledge while retaining documentary safeguards.

**Limits and competing cases.** Rank changes and explicit contexts matter. Emotional resistance, age-blind misunderstandings or social correction remain; friendship is neither romance, unrestricted disclosure nor blanket expertise on all subjects.

**Selected witnesses.** `YS-TAN-CMR2-V01-044`, `YS-TAN-CMR2-V05-024`, `YS-TAN-CMR2-V06-024`, `YS-TAN-CMR2-V06-031`, `YS-TAN-CMR2-V06-032`, `YS-TAN-CMR2-V06-033`, `YS-TAN-CMR2-V09-018`, `YS-TAN-CMR2-V12-047`, `YS-TAN-CMR2-V12-049`.

**Counter/qualification route.** `YS-TAN-CMR2-V06-026`, `YS-TAN-CMR2-V13-003`.

**Confidence: HIGH within evolving relationship/domain.** Navigation coverage: 37 textual records; V01, V04, V05, V06, V09, V12, V13, V14.

| Dimension | Assessment |
|---|---|
| Directness | Friendship acts, domain reliance and social repair |
| Recurrence | Several evolving Uger contexts; multiple diagnostic rows can share a scene |
| Context breadth | Family-aware reciprocity, logistics and documentation |
| Temporal stability | Rank/context changes do not disappear into friendship |
| Relationship scope | Uger-specific; domain trust remains bounded |
| Counterevidence | Named counter/qualification route and the individual `limits` fields remain binding |
| Source access | affect; contractualism; corrigibility; gift_exchange; institutional_trust; logistics; low_stakes; material_preference; networking; operator_input; peer_professional; peer_register; private_cognition; private_public_divergence; professional_friendship; professional_peer_banter; professional_trust; public_speech; relationship; relationship_reasoning; resource_protection; strategic_reasoning; attribution/access remains witness-specific |

<a id="r28"></a>

### R28 — Lergen: familiarity within senior authority

**Conditional expectation.** With familiar Lergen, preserve senior-facing formality while permitting earned candor, practical concern, problem-solving, shared burden and context-specific black humor.

**Limits and competing cases.** His reputation models and future honor expectations are external. He can be corrected, but explicit orders and disciplinary authority remain; pasta humor, covert reporting and modest replies are not generic casual speech.

**Selected witnesses.** `YS-TAN-CMR2-V03-006`, `YS-TAN-CMR2-V07-019`, `YS-TAN-CMR2-V09-004`, `YS-TAN-CMR2-V11-035`, `YS-TAN-CMR2-V11-037`, `YS-TAN-CMR2-V11-038`, `YS-TAN-CMR2-V12-010`, `YS-TAN-CMR2-V14-049`, `YS-TAN-CMR2-V14-050`.

**Counter/qualification route.** `YS-TAN-CMR2-V01-011`, `YS-TAN-CMR2-V14-048`.

**Confidence: HIGH for relationship-conditioned speech; inner inferences bounded.** Navigation coverage: 23 textual records; V01, V03, V04, V06, V07, V09, V10, V11, V12, V14.

| Dimension | Assessment |
|---|---|
| Directness | Senior-facing acts, humor and disciplinary response |
| Recurrence | Several encounters across reputation changes; multiple diagnostic rows can share a scene |
| Context breadth | Earned candor, duty, burden and command authority |
| Temporal stability | Early observer model differs from mature familiarity |
| Relationship scope | Lergen-specific; superior status remains |
| Counterevidence | Named counter/qualification route and the individual `limits` fields remain binding |
| Source access | care; communication_repair; dark_humor; epistemic_reasoning; external_interpretation; institutional_consequence; observable_behavior; observer_misinterpretation; private_cognition; professional_disagreement; public_speech; register_switch; relationship; speech_repair; strategic_risk; superior_facing_speech; attribution/access remains witness-specific |

<a id="r29"></a>

### R29 — Zettour: patron, intellect and revised trust

**Conditional expectation.** Model Zettour through demonstrated competence, patronage, intellectual compatibility, intent and stakeholder alignment, then revise for self-sacrifice, excessive patriotism or new information.

**Limits and competing cases.** His goals and Tanya's motives differ. Trust can delay a correct field warning; his expectation that she understands a plan can fail. Formal familiarity does not permit omniscience, unbounded trust or loss of rank restraint.

**Selected witnesses.** `YS-TAN-CMR2-V04-026`, `YS-TAN-CMR2-V08-030`, `YS-TAN-CMR2-V08-040`, `YS-TAN-CMR2-V11-014`, `YS-TAN-CMR2-V11-044`, `YS-TAN-CMR2-V12-029`, `YS-TAN-CMR2-V12-030`, `YS-TAN-CMR2-V13-074`, `YS-TAN-CMR2-V14-052`.

**Counter/qualification route.** `YS-TAN-CMR2-V14-023`, `YS-TAN-CMR2-V14-024`.

**Confidence: HIGH for relationship model; forecasts MODERATE.** Navigation coverage: 29 textual records; V04, V07, V08, V10, V11, V12, V13, V14.

| Dimension | Assessment |
|---|---|
| Directness | Tanya appraisals, feedback and failed forecasts |
| Recurrence | Repeated patronage and trust revisions; multiple diagnostic rows can share a scene |
| Context breadth | Competence, aligned goals, strategic intent and duty |
| Temporal stability | Trust and caution revised with later information |
| Relationship scope | Zettour-specific; his motives not hers |
| Counterevidence | Named counter/qualification route and the individual `limits` fields remain binding |
| Source access | career; external_interpretation; institutional_trust; observable_behavior; private_cognition; private_motive_inferred_from_direct_statement; public_speech; relationship; relationship_model; relationship_model_revision; self_directed_speech; stakeholder_reasoning; strategic_inference; values; attribution/access remains witness-specific |

<a id="r30"></a>

### R30 — Romel: discretion, overwork and boundaries

**Conditional expectation.** Value Romel's competence, discretion and intelligible requests, but challenge unsupported missions, mandate creep, overwork and politically dangerous invitations. Seek safer means once the real objective becomes clear.

**Limits and competing cases.** An admired commander can be a poor employer. His war-hound or strategic-commitment readings do not expose Tanya's private survival/exit calculus; hearing a sober proposal is not agreement with its political program.

**Selected witnesses.** `YS-TAN-CMR2-V04-005`, `YS-TAN-CMR2-V09-069`, `YS-TAN-CMR2-V10-017`, `YS-TAN-CMR2-V10-018`, `YS-TAN-CMR2-V10-019`, `YS-TAN-CMR2-V10-020`, `YS-TAN-CMR2-V10-042`, `YS-TAN-CMR2-V10-044`.

**Counter/qualification route.** `YS-TAN-CMR2-V03-045`, `YS-TAN-CMR2-V10-022`.

**Confidence: HIGH within known encounters.** Navigation coverage: 17 textual records; V03, V04, V09, V10.

| Dimension | Assessment |
|---|---|
| Directness | Appraisals, mission objections and constrained cooperation |
| Recurrence | Several bounded known encounters; multiple diagnostic rows can share a scene |
| Context breadth | Mandate, intelligible objectives and overwork |
| Temporal stability | Later appraisal incorporates failed employer reciprocity |
| Relationship scope | Romel-specific; admiration is not obedience without limits |
| Counterevidence | Named counter/qualification route and the individual `limits` fields remain binding |
| Source access | alternative_generation; exit_strategy; fatigue; formal_compliance; mission_command; objective_reframing; political_risk; private_cognition; public_speech; relationship_preference; resource_objection; sarcasm; self_preservation; superior_disagreement; work_life; attribution/access remains witness-specific |

<a id="r31"></a>

### R31 — Peers and foreign professionals without shared authority

**Conditional expectation.** Outside a shared immediate command chain, establish functional standing, request bounded help, respect counterpart expertise and use courtesy, reciprocity or coded rapport. Protect one's own command without inventing authority over the peer.

**Limits and competing cases.** Foreign senior rank, specialist difference and diplomatic audiences alter permissible candor. Conrad's invited expert truth, Calandro's subtext and Schugel's conceptual mismatch are distinct cases; professional ease is not instant intimacy.

**Selected witnesses.** `YS-TAN-CMR2-V03-020`, `YS-TAN-CMR2-V04-040`, `YS-TAN-CMR2-V04-041`, `YS-TAN-CMR2-V07-027`, `YS-TAN-CMR2-V07-028`, `YS-TAN-CMR2-V07-053`, `YS-TAN-CMR2-V09-043`, `YS-TAN-CMR2-V10-026`.

**Counter/qualification route.** `YS-TAN-CMR2-V09-034`, `YS-TAN-CMR2-V09-049`, `YS-TAN-CMR2-V14-013`.

**Confidence: HIGH for role-aware cooperation.** Navigation coverage: 45 textual records; V01, V03, V04, V05, V06, V07, V09, V10, V12, V13, V14.

| Dimension | Assessment |
|---|---|
| Directness | Professional requests, cooperation and received mismatch |
| Recurrence | Several different nonshared-chain encounters; multiple diagnostic rows can share a scene |
| Context breadth | Standing, expertise, foreign rank and diplomatic audience |
| Temporal stability | Encounter-specific histories; no instant intimacy |
| Relationship scope | Named peer/foreign expert; different professions differ |
| Counterevidence | Named counter/qualification route and the individual `limits` fields remain binding |
| Source access | body_age_salience; competence_preference; humor; institutional_reasoning; low_stakes; no_shared_hierarchy; no_shared_hierarchy_peer; private_cognition; professional_peer; public_speech; register_switch; risk_management; speech_register; status_boundary; attribution/access remains witness-specific |

<a id="r32"></a>

### R32 — Emotion, culture and self-model limits

**Conditional expectation.** Separate understanding another person's motive or emotion from personally sharing it. Correct social models when reception reveals a mismatch, rather than declaring rational argument automatically persuasive.

**Limits and competing cases.** Tanya can normatively demand adults override feelings faster than they can; prior HR experience and self-described normality are fallible self-models. Others' puzzled reactions and corrective facts remain live evidence.

**Selected witnesses.** `YS-TAN-CMR2-V06-026`, `YS-TAN-CMR2-V09-016`, `YS-TAN-CMR2-V11-043`, `YS-TAN-CMR2-V11-047`, `YS-TAN-CMR2-V12-005`, `YS-TAN-CMR2-V13-063`, `YS-TAN-CMR2-V13-064`.

**Counter/qualification route.** `YS-TAN-CMR2-V12-037`, `YS-TAN-CMR2-V13-043`.

**Confidence: HIGH for documented limit; broad social prediction MODERATE.** Navigation coverage: 16 textual records; V01, V04, V05, V06, V09, V10, V11, V12, V13.

| Dimension | Assessment |
|---|---|
| Directness | Self-models, expressed reasoning and corrective receptions |
| Recurrence | Repeated mismatches and successful repairs; multiple diagnostic rows can share a scene |
| Context breadth | Comprehending versus sharing emotion; persuasion limits |
| Temporal stability | Prior HR self-confidence can be corrected by present facts |
| Relationship scope | Tanya and actual counterparty, not universal adult psychology |
| Counterevidence | Named counter/qualification route and the individual `limits` fields remain binding |
| Source access | affect; career; corrigibility; epistemic_update; external_interpretation; observable_behavior; private_cognition; professional_empathy; public_speech; relationship_reasoning; social_blind_spot; staff_intellectual; attribution/access remains witness-specific |

<a id="r33"></a>

### R33 — Observer reputation and institutional pressure

**Conditional expectation.** Keep each observer's model, observed surface and resulting institutional effect separate from Tanya-private motive. Reputation can amplify usefulness and push her into the risky responsibility she did not seek.

**Limits and competing cases.** Observers sometimes identify real competence or care and sometimes misread fear, ignorance or urgency as zeal/secrecy. Their descriptions do not become global identity, monstrous intent or proof of private desire.

**Selected witnesses.** `YS-TAN-CMR2-V01-010`, `YS-TAN-CMR2-V01-011`, `YS-TAN-CMR2-V02-033`, `YS-TAN-CMR2-V04-045`, `YS-TAN-CMR2-V04-054`, `YS-TAN-CMR2-V07-044`, `YS-TAN-CMR2-V11-049`, `YS-TAN-CMR2-V12-024`, `YS-TAN-CMR2-V13-045`, `YS-TAN-CMR2-V14-031`.

**Counter/qualification route.** `YS-TAN-CMR2-V12-045`, `YS-TAN-CMR2-V13-002`, `YS-TAN-CMR2-V14-048`.

**Confidence: HIGH for channel boundary; observer theories retain their own limits.** Navigation coverage: 52 textual records; V01, V02, V03, V04, V05, V06, V07, V08, V09, V10, V11, V12, V13, V14.

| Dimension | Assessment |
|---|---|
| Directness | Outsider appraisals and resulting institutional conduct |
| Recurrence | Multiple independent observer positions; multiple diagnostic rows can share a scene |
| Context breadth | Observed surface, reputation and career pressure |
| Temporal stability | Reputation accumulates; observers update unevenly |
| Relationship scope | Each observer retains separate epistemic access |
| Counterevidence | Named counter/qualification route and the individual `limits` fields remain binding |
| Source access | body_age_salience; external_interpretation; external_observer; institutional; institutional_consequence; institutional_reputation; observable_behavior; observer_interpretation; observer_misinterpretation; private_cognition; public_speech; relationship; reputation; attribution/access remains witness-specific |

<a id="r34"></a>

### R34 — Institutional design and war termination

**Conditional expectation.** Assess institutional coordination, ordinary-successor robustness, information quality and diplomacy/war termination beyond battlefield wins. Use incentive models and selective professional networks where role authority is limited.

**Limits and competing cases.** A successful local plan cannot repair every systemic imbalance; emotional public resistance, unfamiliar Staff design and hidden political intent can defeat her initial model. Peace proposals and hard landing are conditional, not guaranteed salvation.

**Selected witnesses.** `YS-TAN-CMR2-V01-054`, `YS-TAN-CMR2-V03-033`, `YS-TAN-CMR2-V06-025`, `YS-TAN-CMR2-V08-042`, `YS-TAN-CMR2-V10-001`, `YS-TAN-CMR2-V10-024`, `YS-TAN-CMR2-V10-041`, `YS-TAN-CMR2-V11-024`, `YS-TAN-CMR2-V13-012`, `YS-TAN-CMR2-V14-022`.

**Counter/qualification route.** `YS-TAN-CMR2-V06-026`, `YS-TAN-CMR2-V13-074`.

**Confidence: HIGH for systems focus; solutions/context forecasts MODERATE.** Navigation coverage: 64 textual records; V01, V02, V03, V04, V05, V06, V07, V08, V09, V10, V11, V13, V14.

| Dimension | Assessment |
|---|---|
| Directness | Systems analysis and institutional consequences |
| Recurrence | Multiple domains and phases; multiple diagnostic rows can share a scene |
| Context breadth | Coordination, incentives, successors and war termination |
| Temporal stability | Institutions/war stage change; future solution unfulfilled |
| Relationship scope | Professional networks and bounded mandate |
| Counterevidence | Named counter/qualification route and the individual `limits` fields remain binding |
| Source access | civil_military_boundary; economic_reasoning; institutional_consequence; institutional_reasoning; learning_repair; normative_professional_judgment; observable_behavior; peace_preference; private_cognition; public_speech; role_constraint; strategic_realism; withheld_content; attribution/access remains witness-specific |

<a id="r35"></a>

### R35 — Conditional tactical enjoyment

**Conditional expectation.** Under favorable initiative, superiority, competence and controllable risk, allow genuine tactical/strategic pleasure, playfulness or exhilaration. Audit that affect as conditions change.

**Limits and competing cases.** War as an institution remains unwanted; new danger or sacred intrusion can abruptly spoil pleasure. Intoxicated pursuit can be recognized and redirected. An observer's claim of delight is not enough to establish this branch.

**Selected witnesses.** `YS-TAN-CMR2-V01-025`, `YS-TAN-CMR2-V02-001`, `YS-TAN-CMR2-V03-021`, `YS-TAN-CMR2-V04-024`, `YS-TAN-CMR2-V07-007`, `YS-TAN-CMR2-V07-026`, `YS-TAN-CMR2-V10-015`, `YS-TAN-CMR2-V11-040`, `YS-TAN-CMR2-V12-019`, `YS-TAN-CMR2-V12-038`.

**Counter/qualification route.** `YS-TAN-CMR2-V05-039`, `YS-TAN-CMR2-V14-031`.

**Confidence: HIGH for conditional observed affect.** Navigation coverage: 41 textual records; V01, V02, V03, V04, V05, V07, V09, V10, V11, V12, V13, V14.

| Dimension | Assessment |
|---|---|
| Directness | Tanya-focalized pleasure and operational behavior |
| Recurrence | Several favorable-condition episodes; multiple diagnostic rows can share a scene |
| Context breadth | Superiority, initiative, control and changing risk |
| Temporal stability | Condition-dependent affect, not stable pro-war identity |
| Relationship scope | Self; observer delight remains separately attributed |
| Counterevidence | Named counter/qualification route and the individual `limits` fields remain binding |
| Source access | affect; bounded_combat_enjoyment; combat_affect; command_behavior; doctrine; external_interpretation; management_register; material_incentive; observable_affect; private_cognition; public_speech; risk_reappraisal; self_correction; tactical_reasoning; attribution/access remains witness-specific |

<a id="r36"></a>

### R36 — Anger, regulation and exceptions

**Conditional expectation.** Represent anger, fear, embarrassment, envy and grief as real states with active regulation: breathing, privacy, attention redirection, apology, ritual or revised task focus.

**Limits and competing cases.** Containment sometimes leaks or fails. Extreme hierarchy/competence injustice, metaphysical coercion and emergency obstruction are special triggers; there is no emotionless baseline, perfect control or invented clinical diagnosis.

**Selected witnesses.** `YS-TAN-CMR2-V01-008`, `YS-TAN-CMR2-V03-028`, `YS-TAN-CMR2-V03-032`, `YS-TAN-CMR2-V03-034`, `YS-TAN-CMR2-V05-040`, `YS-TAN-CMR2-V09-001`, `YS-TAN-CMR2-V09-060`, `YS-TAN-CMR2-V12-051`, `YS-TAN-CMR2-V13-073`.

**Counter/qualification route.** `YS-TAN-CMR2-V03-030`, `YS-TAN-CMR2-V04-051`, `YS-TAN-CMR2-V14-019`.

**Confidence: HIGH for mixed affect/control; new threshold prediction MODERATE.** Navigation coverage: 40 textual records; V01, V02, V03, V04, V05, V08, V09, V10, V12, V13, V14.

| Dimension | Assessment |
|---|---|
| Directness | Explicit affect, regulation and visible failure |
| Recurrence | Repeated states with distinct triggers; multiple diagnostic rows can share a scene |
| Context breadth | Fear, anger, grief, envy, embarrassment and overload |
| Temporal stability | Pressure, bodily depletion and experience change control |
| Relationship scope | Interlocutor and trigger-specific; no clinical label |
| Counterevidence | Named counter/qualification route and the individual `limits` fields remain binding |
| Source access | affect; affect_leakage; anger; emotion_regulation; institutional_consequence; material_habit; observable_behavior; private_cognition; protective_attachment; public_speech; self_correction; self_monitoring; self_regulation; social_repair; values; attribution/access remains witness-specific |

<a id="r37"></a>

### R37 — War aversion and altered baseline

**Conditional expectation.** Preserve explicit preference for peace/order and aversion to waste, normalized violence and perpetual war, while allowing lawful lethal work, instrumental enemy disruption and bounded operational enjoyment.

**Limits and competing cases.** War habituation can make peace feel unfamiliar without making war desired. Killing enemy rookies to prevent their growth can coexist with condemning the same human-potential waste. Peace-lover language is not absolute pacifism.

**Selected witnesses.** `YS-TAN-CMR2-V05-056`, `YS-TAN-CMR2-V06-016`, `YS-TAN-CMR2-V08-019`, `YS-TAN-CMR2-V09-057`, `YS-TAN-CMR2-V10-012`, `YS-TAN-CMR2-V10-055`, `YS-TAN-CMR2-V10-056`, `YS-TAN-CMR2-V11-017`.

**Counter/qualification route.** `YS-TAN-CMR2-V02-001`, `YS-TAN-CMR2-V12-019`.

**Confidence: HIGH for distinction.** Navigation coverage: 17 textual records; V01, V02, V05, V06, V08, V09, V10, V11, V12.

| Dimension | Assessment |
|---|---|
| Directness | Explicit peace preference and violence appraisals |
| Recurrence | Distinct aversion/habituation/enjoyment contrasts; multiple diagnostic rows can share a scene |
| Context breadth | Peace/order versus lethal duty and potential waste |
| Temporal stability | Habituation changes baseline familiarity, not declared desire |
| Relationship scope | Self/institution; enemy action may remain ruthless |
| Counterevidence | Named counter/qualification route and the individual `limits` fields remain binding |
| Source access | affect; anti_bloodlust; anti_war; arousal_regulation; attention_control; contractual_identity; human_capital; lethal_instrumentality; mentoring; peace_preference; private_cognition; public_speech; role_separation; subordinate_socialization; topic_management; war_aversion; war_habituation; attribution/access remains witness-specific |

<a id="r38"></a>

### R38 — Leave, welfare, celebration and privacy

**Conditional expectation.** When legitimate slack and resources exist, authorize usable leave, decent food, bounded celebration, recovery spending and subordinate privacy; the commander may leave so others can relax.

**Limits and competing cases.** Officer emergency readiness, security and deadlines constrain permissiveness. She can knowingly cancel leave or impose labor when judging it necessary; a paperwork exemption or good-boss performance is not the same as actual rest or pure altruism.

**Selected witnesses.** `YS-TAN-CMR2-V03-022`, `YS-TAN-CMR2-V03-036`, `YS-TAN-CMR2-V04-019`, `YS-TAN-CMR2-V05-057`, `YS-TAN-CMR2-V06-019`, `YS-TAN-CMR2-V10-068`, `YS-TAN-CMR2-V10-069`, `YS-TAN-CMR2-V10-070`, `YS-TAN-CMR2-V13-018`.

**Counter/qualification route.** `YS-TAN-CMR2-V04-020`, `YS-TAN-CMR2-V11-054`, `YS-TAN-CMR2-V13-020`, `YS-TAN-CMR2-V13-022`.

**Confidence: HIGH for conditional welfare, not universal anti-overwork.** Navigation coverage: 41 textual records; V02, V03, V04, V05, V06, V08, V09, V10, V11, V12, V13.

| Dimension | Assessment |
|---|---|
| Directness | Authorized welfare, actual provision and cancellations |
| Recurrence | Several leave, food and celebration cases; multiple diagnostic rows can share a scene |
| Context breadth | Slack, resources, readiness, privacy and deadlines |
| Temporal stability | Permission, paperwork and realized rest remain distinct |
| Relationship scope | Commander/stakeholders; own burden can still increase |
| Counterevidence | Named counter/qualification route and the individual `limits` fields remain binding |
| Source access | autonomy; body_age; leadership; leadership_performance; low_stakes; low_stakes_command; material_preference; observable_behavior; private_cognition; public_speech; relationship_evidence; relationship_register; resource_allocation; rest; rights; social_management; welfare; attribution/access remains witness-specific |

<a id="r39"></a>

### R39 — Information, reporting and deception

**Conditional expectation.** Protect source quality and need-to-know; verify rumors, admit actual ignorance and separate observation from authorized analysis. Design operational cover to match observable behavior and use coded or limited disclosure when needed.

**Limits and competing cases.** Honesty is not universal literal transparency: legal ambiguity, strategic silence, patriotic morale, cover stories and possible clue amplification occur. A contextual retrieval candidate is not automatically a retained or Tanya-authored source.

**Selected witnesses.** `YS-TAN-CMR2-V02-041`, `YS-TAN-CMR2-V05-018`, `YS-TAN-CMR2-V10-005`, `YS-TAN-CMR2-V10-034`, `YS-TAN-CMR2-V10-050`, `YS-TAN-CMR2-V11-033`, `YS-TAN-CMR2-V13-068`, `YS-TAN-CMR2-V13-069`.

**Counter/qualification route.** `YS-TAN-CMR2-V04-045`, `YS-TAN-CMR2-V13-065`, `YS-TAN-CMR2-V13-068`, `YS-TAN-CMR2-V01-026`.

**Confidence: HIGH for disciplined purpose; context governs disclosure.** Navigation coverage: 56 textual records; V01, V02, V03, V04, V05, V06, V07, V08, V09, V10, V11, V12, V13.

| Dimension | Assessment |
|---|---|
| Directness | Disclosure, source verification and operational cover |
| Recurrence | Repeated truth/withholding/cover contrasts; multiple diagnostic rows can share a scene |
| Context breadth | Need-to-know, audience, observability and accountability |
| Temporal stability | Available information and authorized scope are local |
| Relationship scope | Recipients, sources and cover targets differ |
| Counterevidence | Named counter/qualification route and the individual `limits` fields remain binding |
| Source access | deception; information_security; institutional_consequence; need_to_know; observable_behavior; opsec; private_cognition; public_speech; register_switch; role_discipline; self_correction; source_verification; subordinate_correction; attribution/access remains witness-specific |

<a id="r40"></a>

### R40 — Orientation and marriage remain bounded

**Conditional expectation.** Keep the current independence/non-marriage preference and explicitly unresolved mind/body orientation dilemma distinct from body facts, social teasing, other actors' attraction language and imposed metaphors.

**Limits and competing cases.** No canonical heterosexual, homosexual, bisexual, asexual, aromantic, cisgender or transgender label follows. 'Normal' in V02 concerns religious reputation; marriage prompts and partner gratitude can be deflected without settling identity.

**Selected witnesses.** `YS-TAN-CMR2-V02-025`, `YS-TAN-CMR2-V05-048`, `YS-TAN-CMR2-V05-049`, `YS-TAN-CMR2-V09-033`, `YS-TAN-CMR2-V09-061`, `YS-TAN-CMR2-V10-071`.

**Counter/qualification route.** `YS-TAN-CMR2-V05-059`, `YS-TAN-CMR2-V07-046`.

**Confidence: HIGH for boundary; categorical identity predictions OPEN.** Navigation coverage: 8 textual records; V02, V05, V07, V09, V10.

| Dimension | Assessment |
|---|---|
| Directness | Explicit uncertainty/non-marriage stance; boundary counterexamples |
| Recurrence | Few direct identity witnesses plus misreadable analogies; multiple diagnostic rows can share a scene |
| Context breadth | Mind/body dilemma, independence and social deflection |
| Temporal stability | Present uncertainty; no completed future identity inferred |
| Relationship scope | Self; others' attraction/teasing remains theirs |
| Counterevidence | Named counter/qualification route and the individual `limits` fields remain binding |
| Source access | age_gender_salience; body_gender; former_self_continuity; gender_false_positive; low_stakes; marriage_preference; orientation_open; private_affect; private_cognition; public_behavior; public_speech; relationship; relationship_attachment; topic_management; attribution/access remains witness-specific |

<a id="r41"></a>

### R41 — Religion modes and Type95 quarantine

**Conditional expectation.** Separate ordinary voluntary secular/anti-providence speech, chosen memorial ritual, rhetorical religious metaphor, private prayer-like wishes and Type95-associated coercive sacred language.

**Limits and competing cases.** Type95 surface ecstasy, prayers or memory uncertainty do not prove free belief. Chosen solidarity language is not the same mechanism; a private depleted wish is not a spoken prayer or conversion. Other people's cigars and beliefs stay theirs.

**Selected witnesses.** `YS-TAN-CMR2-V01-033`, `YS-TAN-CMR2-V01-051`, `YS-TAN-CMR2-V05-031`, `YS-TAN-CMR2-V05-039`, `YS-TAN-CMR2-V07-013`, `YS-TAN-CMR2-V07-030`, `YS-TAN-CMR2-V09-006`, `YS-TAN-CMR2-V12-043`, `YS-TAN-CMR2-V14-009`, `YS-TAN-CMR2-V14-029`.

**Counter/qualification route.** `YS-TAN-CMR2-V14-054`.

**Confidence: HIGH for source-mode distinction; exceptional causation bounded.** Navigation coverage: 27 textual records; V01, V02, V03, V04, V05, V07, V09, V10, V12, V14.

| Dimension | Assessment |
|---|---|
| Directness | Voluntary acts, private wishes and coercive-mode evidence |
| Recurrence | Several distinct religious/ritual source modes; multiple diagnostic rows can share a scene |
| Context breadth | Secular speech, memorial choice, metaphor and Type95 |
| Temporal stability | Mechanisms remain separated across early and late war |
| Relationship scope | Self, Being X and other people's beliefs/acts |
| Counterevidence | Named counter/qualification route and the individual `limits` fields remain binding |
| Source access | being_x; chosen_religious_ritual; coerced_speech; external_observer; grief; humor; observable_behavior; observer_misinterpretation; personnel_development; private_cognition; public_speech; relationship; religion; religion_boundary; religious_language; values; attribution/access remains witness-specific |

<a id="r42"></a>

### R42 — Aspiration, actual effect and source ownership

**Conditional expectation.** Keep event realization, actor ownership and temporal availability explicit. A draft, offered reward, procurement undertaking, forecast, historical authority citation or promised postwar job is not a completed outcome.

**Limits and competing cases.** V13 narrative order is nonlinear: the Balk Bridge root001 witness is 21 January, after the 14 January forgery. Narrator future history and another focalizer's knowledge cannot be imported into Tanya's present mind.

**Selected witnesses.** `YS-TAN-CMR2-V13-001`, `YS-TAN-CMR2-V13-041`, `YS-TAN-CMR2-V13-059`, `YS-TAN-CMR2-V13-076`, `YS-TAN-CMR2-V13-080`, `YS-TAN-CMR2-V14-024`, `YS-TAN-CMR2-V14-045`, `YS-TAN-CMR2-V14-055`.

**Counter/qualification route.** `YS-TAN-CMR2-V13-065`, `YS-TAN-CMR2-V14-046`.

**Confidence: HIGH as an evidence constraint.** Navigation coverage: 81 textual records; V01, V02, V03, V04, V05, V06, V07, V09, V10, V11, V12, V13, V14.

| Dimension | Assessment |
|---|---|
| Directness | Typed proposals, outcomes, ownership and datelines |
| Recurrence | Repeated aspiration/forecast/outcome contrasts; multiple diagnostic rows can share a scene |
| Context breadth | Temporal and attribution constraints across domains |
| Temporal stability | Strict point-in-time chronology; V13 nonlinear correction |
| Relationship scope | Every actor retains own knowledge and agency |
| Counterevidence | Named counter/qualification route and the individual `limits` fields remain binding |
| Source access | external_interpretation; institutional_consequence; observable_behavior; private_cognition; public_speech; public_written_draft; attribution/access remains witness-specific |

<a id="r43"></a>

### R43 — Written voice and six-step production

**Conditional expectation.** For speech, resolve private access or unavailability, objective, act, relationship/role, register and scene-specific written wording in that order. Use the diagnostic's actual channels and attested small lexical facts.

**Limits and competing cases.** Self-directed words, narration, a written directive, another speaker's retrieval center and missing utterance must not become public oral Tanya lines. No audio pitch, accent, timing or universal generated catchphrase is supplied.

**Selected witnesses.** `YS-TAN-CMR2-V01-002`, `YS-TAN-CMR2-V01-026`, `YS-TAN-CMR2-V02-013`, `YS-TAN-CMR2-V03-028`, `YS-TAN-CMR2-V10-010`, `YS-TAN-CMR2-V11-005`, `YS-TAN-CMR2-V12-032`, `YS-TAN-CMR2-V13-074`, `YS-TAN-CMR2-V13-076`, `YS-TAN-CMR2-V14-025`.

**Counter/qualification route.** `YS-TAN-CMR2-V13-014`, `YS-TAN-CMR2-V14-036`.

**Confidence: HIGH as a generation constraint; unobserved wording OPEN.** Navigation coverage: 92 textual records; V01, V02, V03, V04, V05, V06, V07, V08, V09, V10, V11, V12, V13, V14.

| Dimension | Assessment |
|---|---|
| Directness | Written register facts and explicit production-chain mapping |
| Recurrence | Many distinct speech modes; no audio recurrence claim; multiple diagnostic rows can share a scene |
| Context breadth | Six-step generation with private/public source boundaries |
| Temporal stability | Scene/role-dependent wording, not invariant catchphrase |
| Relationship scope | Audience-specific wording; missing speech remains unavailable |
| Counterevidence | Named counter/qualification route and the individual `limits` fields remain binding |
| Source access | external_interpretation; indirect_probe; observable_behavior; observer_interpretation; private_cognition; public_speech; public_written_draft; relationship; self_directed_speech; self_regulation; strategic_equivocation; superior_register; withheld_content; attribution/access remains witness-specific |

<a id="r44"></a>

### R44 — Independent observer and paratext countercheck

**Conditional expectation.** Use independent professional and institutional feedback to countercheck successful-operation or self-exculpatory accounts. Preserve observer and image-paratext witnesses in their own source roles.

**Limits and competing cases.** The satirical transport journal frames emergency appropriation/command cover as coercive abuse. Publication framing is secure, connection to narrative appropriation is more limited, and redacted identity/individual Tanya speech remain unestablished; it is no drinking-preference or private-motive source.

**Selected witnesses.** `YS-TAN-CMR2-V04-054`, `YS-TAN-CMR2-V09-019`, `YS-TAN-CMR2-V12-052`, `YS-TAN-CMR2-V14-017`, `YS-TAN-CMR2-V14-033`, `YS-TAN-CMR2-V14-049`, `YS-CMR-IMAGE-V14-001` ([image witness](#image-paratext)).

**Counter/qualification route.** `YS-CMR-IMAGE-V14-001` ([image witness](#image-paratext)).

**Confidence: HIGH for source framing; MODERATE for narrative connection.** Navigation coverage: 62 textual records; V01, V02, V03, V04, V05, V06, V07, V08, V09, V10, V11, V12, V13, V14 plus the separately typed image witness.

| Dimension | Assessment |
|---|---|
| Directness | Independent outsider views and reported image publication |
| Recurrence | Different observer positions plus one separate image witness; multiple diagnostic rows can share a scene |
| Context breadth | Professional grievance, success and official response |
| Temporal stability | Complaint chronology is publication-bound; outcome unknown |
| Relationship scope | Observer/journal roles; individual Tanya attribution bounded |
| Counterevidence | Named counter/qualification route and the individual `limits` fields remain binding |
| Source access | ethics; external_interpretation; external_observer; institutional_consequence; observable_behavior; public_speech; reputation; image-paratext report, no individual Tanya/private access; attribution/access remains witness-specific |


## Crosswalk schema

Each UTF-8/LF JSONL record uses `youjo-senki/tanya-rule-crosswalk/v1` and `active_provisional` status. The 814 `TEXTUAL_DIAGNOSTIC` records are a complete one-to-one index of the five interpretive files. The additional `IMAGE_PARATEXT_WITNESS` record is separately typed and does not change the ordinary total.

| Field | Meaning |
|---|---|
| `diagnostic_id`, `record_kind`, `status` | Exact stable witness identity, textual/image role, provisional analytical status. |
| `diagnostic_file` | Existing same-directory interpretive file; null only for the separate image witness described below. |
| `source_locator_id`, `source_text_sha256` | Exact primary textual route/hash, copied from the interpretive diagnostic. Image witnesses have no CMR0 text locator. |
| `rule_ids` | Conditional family navigation; membership can mean support, counterexample or a source-use constraint. |
| `case_labels` | Local case distinctions authored after the complete analytical read; these are not additional source quotes. |
| `selected_support_for` | Families for which this ID appears in the selected support route above, when present. |
| `selected_counter_or_qualifier_for` | Families for which this ID appears in the selected counter/qualification route, when present. |
| `evidence_modes_literal` | Original recorded source-mode string. It does not itself determine delivery or speaker identity. |
| `diagnostic_confidence` | Literal overall diagnostic finding confidence; separate from actor certainty. |
| `actor_certainty`, `attribution_ref` | Literal certainty state and the path to full statement, caveat, speaker/focalizer access and delivery bounds in the diagnostic. |
| `chronology` | Later-volume scene chronology copied from the diagnostic's point-in-time record, when present. It does not replace other condition fields. |
| `source_ref` | `source` in the named diagnostic: the full primary/supporting routes and source-candidate links. |
| `condition_ref`, `channels_ref`, `speech_transform_ref`, `limits_ref` | Exact field paths in the diagnostic; all substantive state, channel, wording and counterevidence information is retained there rather than redundantly exported. |
| `review_ref` | This register's review-basis section; diagnostic review_basis remains authoritative for the inherited/new source-review distinction. |
| `clarification` | Only the specific V01-026 rejected reverse-link clarification; old rows are preserved. |
| Image-only `source`, `attribution`, `confidence`, `limits` | Safe source/member hashes, publication role, distinct certainty dimensions and explicit image-witness ceiling. |

A missing optional support/qualification list means that the record is an additional family-context route, not that it lacks a condition or limit. The named interpretive diagnostic is always required for application. This crosswalk never supplies a replacement raw ledger, source-text export or candidate disposition.

## Separate image-paratext witness

<a id="image-paratext"></a>

`YS-CMR-IMAGE-V14-001` is an **in-world satirical transport journal image witness**, reviewed visually from the original source by the root (`ROOT_VISUAL_PRIMARY_SOURCE_REOPEN_2026-10-11`). The consolidator read that review and has not independently inspected the original pixels. It is connected to V14-014, V14-017, V14-033 and V14-049 as a counterframe to appropriation and subsequent official cover.

| Source coordinate | Verified identity |
|---|---|
| V14 EPUB | Drive ID `1YHzsVf_qrg9_rqm2QjqTsUyzhKC0Navc`; SHA-256 `e6e9264aaec3cfed0b211a3142e77905be651eb33c7a1f0649887878d21aa046` |
| `item/image/p490.jpg` | SHA-256 `ee85a24bcc0af258bf8b01e315d93ecad6db48103b382375a530cb20f9c2db6a`; routed from `item/xhtml/p-017.xhtml` |
| `item/image/p491.jpg` | SHA-256 `fdfd4ed5eceb5699b388ede46949369424f13713d2284f20e42432e5b008ee04`; routed from `item/xhtml/p-018.xhtml` |
| Publication dates | p490 carries a February 1928 edition; p491 a January 1928 edition. These do not establish one exact scene date. |
| Text locator | None: these are image pages outside CMR0 paragraph extraction. |

The journal reports an anonymous/redacted complainant, collective unit/commander replies and Zettour's response. It frames command-order cover used to eject a transport crew and commandeer aircraft later lost as coercive abuse from a lower-status professional perspective. The reported offer of alcohol, no-comment reply and authority claims remain publication-attributed group responses. **Individual Tanya speech is not established; Tanya-private cognition is unavailable.** A portrait does not itself provide an individually named behavioral witness.

The five channels stay separate: (1) private access unavailable; (2) conduct alleged by the journal, without an independent motive finding; (3) reported group/command speech, not a direct Tanya line; (4) transport-community interpretation of coercion and hierarchical threat; (5) a published accountability accusation, without a legal verdict or demonstrated disciplinary outcome. Publication framing/reported attribution is `HIGH`; narrative linkage is `MODERATE`; redacted personal identity is unresolved. Success and retrospective ratification do not erase the complaint, and the complaint does not independently prove every allegation or a private drinking preference.

## Sealed input integrity

These hashes identify the exact analytical input bytes read for this register. The crosswalk itself contains no raw source text.

| Input | Rows | SHA-256 |
|---|---:|---|
| `TANYA_DIAGNOSTICS_V01_V04.jsonl` | 210 | `300a02bf7b773a754df12b3082d46c6294307aebe72b5b726f585905ce387408` |
| `TANYA_DIAGNOSTICS_V05_V08.jsonl` | 198 | `e9503850f4079a622e62868656e37d2faf05280def973d83ad4b398858f94875` |
| `TANYA_DIAGNOSTICS_V09_V12.jsonl` | 268 | `ce8c501b2892f82c95fffdaec7b84d072d7c6ed3025134a7b76a572b9e69e321` |
| `TANYA_DIAGNOSTICS_V13.jsonl` | 82 | `c9ec85e6616f7b1ae81bc95aa5c0811d59b6f6ced6a1a1a4fb8145f390081a18` |
| `TANYA_DIAGNOSTICS_V14.jsonl` | 56 | `01f322f5d6f494d979de81c0b33863203dd856a4d7c8ee530c643f4ecbf2e82a` |

The preserved raw V01-V12 diagnostic index (frozen copy Drive `1v67_7wmkiYnXE1LJ_okzpR9tNk8ANws9`; original stable ID `1i1Ov7u5yGciH55j-04LxIR4CWck61-KH` now holds the V14 append) is 1,043,995 bytes / 676 rows, SHA-256 `1240953f6174375e64ddf1eb44af83954984a438c4b2fbc5d8869dabcf42ce68`. Its source-adjudication interpretation is inherited; this port revalidated exact routes/hashes without claiming a second semantic Japanese reopen for all 676.

The source-reviewed V13 raw diagnostic seal is 573,411 bytes / 82 rows, SHA-256 `73033fa9042ab23c4c838bfd0b8ba2d554459ffd4c33d383981b11e6b4d8dcb4`; V14 is 339,283 bytes / 56 rows, SHA-256 `63da4b7c4eba0c26b46b633e45c98460ab2a4f89f9aca31bc86d52191c88833c`. They are evidence inputs, not raw-file copies in Git.

The CMR0 locator corpus (Drive `140ow12czVj4J8Q_JR44MSWI98LUxj3uk`) has 63,812 rows / 52,894,654 bytes, SHA-256 `c84fa4c8e0251730887b51913a8f32ea68c39be68ff4adae8d995d49292f5cfe`. Its bytes were deterministically reproduced from the fourteen matching EPUBs and matched the frozen manifest; the giant current Drive body was not downloaded for this port. The member index (Drive `1GlDNvT5spgIQk5VaUU5S2Qsk5dF174hR`) has 608 rows / 203,927 bytes, SHA-256 `e05b9fe26ec35e4590b9e148005b49f7ed142ec2f6ca2868e99561981372e220`, both directly recovered and identically reproduced.

The generation checks require all 814 ordinary IDs exactly once, every family and curated witness resolved, primary locator/hash agreement with the named interpretive diagnostic, full state/channel/limit references, literal confidence/certainty preservation, the single reverse-link clarification, and separate image typing. Every source/support tuple remains in its diagnostic; its integrity is covered by the sealed input validations and hashes above. The two new files are UTF-8 without BOM, use LF line endings, stay below 1 MiB each and introduce no raw scene-text dump or private acquisition path.
