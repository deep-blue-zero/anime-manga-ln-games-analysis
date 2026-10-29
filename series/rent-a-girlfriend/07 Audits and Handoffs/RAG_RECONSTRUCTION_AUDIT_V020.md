---
title: "Rent-a-Girlfriend - Local Reconstruction Audit through Volume 020"
artifact_id: RAG_RECONSTRUCTION_AUDIT_V020
artifact_type: local_reconstruction_audit
series: Rent-a-Girlfriend
generation: V1
version: "1.0"
status: canonical
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
created: "2026-09-20"
source_boundary: "Project-local audit of Kazuya, Chizuru, and Ruka models through Japanese manga V020; no V021 or later narrative evidence admitted."
frozen_model_commit: "f28a51540e36b2e55fe53556edd6ba93bd5d80bf"
---

# Local reconstruction audit through Volume 020

## Audit contract

~~~yaml
audit_state: COMPLETE
checkpoint: RAG_CP_V020
checkpoint_endpoint: V020
frozen_model_commit: f28a51540e36b2e55fe53556edd6ba93bd5d80bf
active_substantial_characters:
  - RAG-LOCAL-KAZUYA
  - RAG-LOCAL-CHIZURU
  - RAG-LOCAL-RUKA
later_narrative_exposure: EXCLUDED
global_capability_assessment: NOT_PERFORMED
numeric_accuracy_score: NOT_PRODUCED
~~~

This audit evaluates the exact V020 close models at the frozen commit. It uses time-indexed states, behavioral rules, relationship conditions, evidence ledgers, and prospectively frozen predictions. Retrospective checks are labeled. The same analyst inspected the manga and performed the audit, so no test is described as blind. Invented dialogue and generated scenes are excluded from evidence.

The test standard is discrimination. A useful model must preserve knowledge differences, relationship conditions, consent scope, audience effects, and meaningful abstention. Plot recall alone is insufficient. Readiness labels are local descriptions and do not create global character grades or production capability records.

## Kazuya Kinoshita

### Snapshot and readiness

~~~yaml
model_path: "04 Character Analysis/Kazuya Kinoshita/RAG_KAZUYA_RECONSTRUCTION_MODEL.md"
evidence_ledger_path: "04 Character Analysis/Kazuya Kinoshita/RAG_KAZUYA_EVIDENCE_LEDGER.md"
model_version: "1.21"
model_revision: "1.20"
admitted_state: KAZ-S022
local_readiness: OPERATIONAL_CANDIDATE
validated_envelope:
  - family pressure, concealment, and bounded truth attempts
  - concrete support planning, revision, and delivery
  - production labor under external standards
  - embarrassment, romantic appraisal, and interrupted direct speech
  - differentiated consent and relationship-specific boundary response
~~~

The label permits bounded analysis within these domains. It does not authorize a whole-person simulation, a mature-partner default, or later-state knowledge.

### Observed domains

- Family deception, hospital crisis, inherited obligations, and partial truth conflict.
- Paid employment, budgeting under romantic purpose, crowdfunding, production, exhibition, and unsafe physical effort.
- Rescue, practical care, grief support, consultation, adaptive revision, and received feedback.
- Rental, project, ordinary, and romantic access with Chizuru.
- Provisional dating, attraction, guilt, refusal, and differentiated consent with Ruka.
- Peer audiences, Kibe, Kuribayashi repair, Mami recontact, Mini pressure, and Sumi support.
- Sexual focalization, fantasy, panic, self-attack, and incomplete direct confession.

### Strong rules

| Rule | Strength at V020 | Basis and discrimination | Limit |
|---|---|---|---|
| RAG-KAZ-R001 — immediate face protection can outrun long-term planning | Strong across family, peer, former-partner, and romantic audiences | Explains repeated concealment and panic while allowing concrete counterexamples when harm or a route becomes clear. | It must not erase Kuribayashi disclosure, Sayuri truth advocacy, or the V020 confession attempt. |
| RAG-KAZ-R009 — relationship labels do not override observed consent limits | Strong inside the tested envelope | Distinguishes sex refusal, accidental-contact correction, sunscreen consent, blocked hug, overnight refusal, and timed-hug permission. | Mature reciprocal intimacy remains unobserved. |
| RAG-KAZ-R010 / R012 — concrete routes and measurable goals can organize support | Strong in film and crisis work | Explains research, expert revision, campaign persistence, production, venue access, bedside projection, and public exhibition better than a generic rescuer label. | Methods can be costly or unsafe; repeat competence outside this project is unknown. |
| RAG-KAZ-R014 / R015 — visible concealed pain can shift him toward adaptive non-demanding support | Moderate to strong in the bereavement sequence | Predicts consultation, bounded booking, revision from distraction, noninitiated touch, and restraint after relief. | The strongest result is one acute grief episode. |

### Weak or narrow rules

- RAG-KAZ-R004 remains concentrated in public degradation and should not predict universal moral courage.
- RAG-KAZ-R006 is strong for acute protection but cannot establish calm medical or crisis expertise.
- RAG-KAZ-R013 explains subordinate production labor and bottleneck action, but its unsafe component prevents a broad competence claim.
- RAG-KAZ-R016 has one direct-question case ending in interruption. It supports a speech range, not reliable confession completion.

### Tests performed

| Test | Type and frozen basis | Expected discriminating range | Observed outcome | Result |
|---|---|---|---|---|
| RAG-KAZ-T05 | Prospective; RAG-PRED-045 frozen at V012 | A genuine film commitment should produce governance, expert correction, and measurable work rather than only a romantic promise. | V013 adds task division, agency contact, budgeting, expert rejection and revision, approval, and launch. | SUPPORTED_IN_THIS_TEST |
| RAG-KAZ-T06 | Prospective; RAG-PRED-059 frozen at V015 | Producer labor and unsafe bottleneck work should produce a role or interpersonal consequence. | Chizuru directly rejects his self-demotion and values his work; he then completes final-location camera labor. | SUPPORTED_IN_THIS_TEST |
| RAG-KAZ-T07 | Prospective; RAG-PRED-065 frozen at V017 | The LINE-and-running action should become concrete delivery, access, coordination, or failure. | V018 reveals laptop-and-projector bedside delivery of unfinished footage. | SUPPORTED_IN_THIS_TEST |
| RAG-KAZ-T08 | Prospective; RAG-PRED-076 frozen at V019 | Explicit internal love should produce observable action, restraint, ordinary access, disclosure attempt, or conflict. | V020 adds meal initiative, direct identification of Chizuru as the ideal girlfriend, and an interrupted confession. | SUPPORTED_IN_THIS_TEST |
| RAG-KAZ-T09 | Retrospective relationship-switch test; KAZ-S022 | The model should give different behavior toward Chizuru and Ruka under intimacy pressure. | He moves toward direct romantic speech with Chizuru while refusing Ruka's overnight request and permitting only separately scoped access. | SUPPORTED_IN_THIS_TEST |

### Failures and error analysis

The model's largest continuing risk is **overgeneralization**. Completing one film can be mistaken for global executive competence; one effective grief intervention can be mistaken for universal emotional insight; one confession attempt can be mistaken for mature directness. The model retains unsafe climbing, expensive overcommitment, audience-sensitive avoidance, and failure to arrange a private follow-up.

A second risk is **motive weighting error**. Love helps explain Kazuya's effort, but does not make every act prudent or entitle him to Chizuru. Guilt toward Ruka helps explain avoidance, but does not discharge his responsibility to resolve the trial. The model must preserve action, cost, and obligation separately.

### Required assumptions, unsupported scenarios, and next evidence

Additional assumptions are required for stable study or work routine, long-term budgeting, repeat production management, mature reciprocal sex, cohabitation, completed family disclosure, fair breakup conduct, or an answered confession. Unsupported scenarios include effortless romantic eloquence, confident seduction, complete knowledge of Chizuru's private response, and certainty about Mami's purpose.

The next useful evidence would be a private follow-up without accidental interruption, a direct and fair Ruka-status conversation, conduct after Mami's app route produces pressure, and ordinary responsibility not organized around crisis or romance.

## Chizuru Ichinose

### Snapshot and readiness

~~~yaml
model_path: "04 Character Analysis/Chizuru Ichinose/RAG_CHIZURU_RECONSTRUCTION_MODEL.md"
evidence_ledger_path: "04 Character Analysis/Chizuru Ichinose/RAG_CHIZURU_EVIDENCE_LEDGER.md"
model_version: "1.21"
model_revision: "1.20"
admitted_state: CHI-S022
local_readiness: OPERATIONAL_CANDIDATE
validated_envelope:
  - professional service, price, fairness, and identity boundaries
  - family welfare, terminal crisis, grief control, and bounded support acceptance
  - vocational setback, project leadership, performance, and continuing commitment
  - audience-sensitive register and selective disclosure
  - direct relational testing with classification control
~~~

The model supports action ranges and abstention, not hidden-thought completion. It cannot provide her final romantic answer.

### Observed domains

- Rental work, dissatisfied-client correction, price regulation, referral, and work pride.
- Campus identity, alias management, family performance, Mami confrontation, and audience switching.
- Acting training, casting loss, film principal work, on-set performance, public screening, and continuing-vocation speech.
- Family history, Sayuri and Katsuhito loss, partial truth, funeral duty, grief masking, collapse, and relief report.
- Paid, project-scoped, emergency, ordinary, and bodily access with Kazuya.
- Ruka and Umi relational pressure, Mini's disclosure, direct inquiry, and later response deferral.

### Strong rules

| Rule | Strength at V020 | Basis and discrimination | Limit |
|---|---|---|---|
| RAG-CHI-R003 — audience determines register without defining authenticity | Strong across service, campus, family, project, and private settings | Explains warm rental speech, direct correction, family improvisation, private grief, and V020 public deferral without assigning one register as the sole true self. | Register alone cannot identify romance or deception motive. |
| RAG-CHI-R004 / R007 — voluntary help is followed by legible classification | Strong | Gifts, care, project work, grief support, refund, ordinary time, and renewed rental language repeatedly coexist. | Reclassification does not prove emotional absence. |
| RAG-CHI-R010 / R011 — family-linked threat can produce governed collaboration | Strong across V012-V020 project evidence | Predicts feasibility testing, agency boundaries, money parity, controlled exposure, performance, family access, and completed exhibition. | One project does not establish universal production or career behavior. |
| RAG-CHI-R014 / R015 — terminal loss intensifies control while precise recognition can permit release | Moderate to strong in bereavement contexts | Distinguishes attempted truth, funeral composure, self-initiated collapse, later relief report, and professional reaccounting. | Durability outside acute grief is unknown. |

### Weak or narrow rules

- RAG-CHI-R005 has a small public-defense sample and cannot predict universal intervention.
- RAG-CHI-R006 covers exposure management but should not become a generic intimacy script.
- RAG-CHI-R013 supports qualified classification under pressure, but direct affirmative romance remains absent.
- RAG-CHI-R016 is based on one alcohol-affected meal, one interrupted declaration, and one public avoidance scene; private sober follow-up is untested.

### Tests performed

| Test | Type and frozen basis | Expected discriminating range | Observed outcome | Result |
|---|---|---|---|---|
| RAG-CHI-T05 | Prospective; RAG-PRED-046 frozen at V012 | If Chizuru is a principal rather than passive beneficiary, she should shape work, money, permission, or publication. | V013 shows agency notification, task division, fee waiver, savings offer, private work access, and campaign consent. | SUPPORTED_IN_THIS_TEST |
| RAG-CHI-T06 | Prospective; RAG-PRED-053 frozen at V014 | Mini's disclosure should produce observable response without requiring agreement. | V015 shows defensive response, colder conduct, later gratitude, and a qualified non-negation. | SUPPORTED_IN_THIS_TEST |
| RAG-CHI-T07 | Prospective; RAG-PRED-071 frozen at V018 | Controlled bereavement should continue, crack, receive support, or be directly reported. | V019 shows family-triggered breach, self-initiated crying, and a later report of relief. | SUPPORTED_IN_THIS_TEST |
| RAG-CHI-T08 | Prospective; RAG-PRED-075 frozen at V019 | Mini's inquiry and interpretation should produce a disclosure, pressure, plan, misunderstanding, or relationship consequence. | V020 shows Chizuru cite Mini while directly asking Kazuya whether he likes her. | SUPPORTED_IN_THIS_TEST |
| RAG-CHI-T09 | Negative/adversarial motive check; CHI-S022 | Ordinary unbooked time and private activation should not be converted automatically into romance or emotional absence. | Chizuru accepts the meal, asks directly, restores rental language, replays his words, and later defers public discussion. | SUPPORTED_IN_THIS_TEST as an underdetermination limit |

### Failures and error analysis

The earlier RAG-PRED-015 failure remains a timing and overgeneralization warning: acting did not receive the predicted immediate V005 consequence even though later volumes made the vocation central. Later evidence cannot retroactively turn that horizon into success.

The principal live risk remains **genuine underdetermination**. Professional pride, fairness, family purpose, gratitude, grief, attraction, and self-protection can explain overlapping conduct. The model correctly predicts classification and audience control while abstaining on the final romantic ranking. A reconstruction that makes the V020 question proof of love, or her later avoidance proof of rejection, would commit motive weighting and knowledge-state errors.

### Required assumptions, unsupported scenarios, and next evidence

Additional assumptions are required for an affirmative romantic answer, reciprocal partnership, sexual intimacy, sustained cohabitation, close-friend routine, wider acting success, or stable post-bereavement functioning. Unsupported scenarios include unlimited access after the ordinary meal, a universal preference for paid boundaries, effortless vulnerability, and complete knowledge of Ruka's private contact history.

The next useful evidence would be Chizuru's sober private response to Kazuya's interrupted declaration, her behavior when Mami's family access becomes salient, a new acting opportunity or setback, and ordinary routine without immediate project or crisis pressure.

## Ruka Sarashina

### Snapshot and readiness

~~~yaml
model_path: "04 Character Analysis/Ruka Sarashina/RAG_RUKA_RECONSTRUCTION_MODEL.md"
evidence_ledger_path: "04 Character Analysis/Ruka Sarashina/RAG_RUKA_EVIDENCE_LEDGER.md"
model_version: "1.18"
model_revision: "1.17"
admitted_state: RUK-S016
local_readiness: PARTIAL_MODEL
strongest_domain: "rivalry, access pressure, and tactical narrowing inside the nonreciprocal provisional relationship"
conditionally_operational_domains:
  - direct status challenge by Chizuru, Mami, or exclusion
  - request escalation and narrowing under explicit refusal
  - short-term redirection after visible third-party cost
  - project cooperation under a shared concrete burden
~~~

Ruka remains partial because nearly all substantial evidence is organized around one romantic goal. V020 improves the consent-request sample but does not broaden family, school, friendship, or independent-interest coverage.

### Observed domains

- Rental-provider recognition, secrecy bargaining, client history, and narrow professional expertise.
- Low-pulse history, medication, measurement, robot metaphor, and subjective love criterion.
- Direct pursuit across messages, university, karaoke work, dates, domestic access, travel requests, and family spaces.
- Project labor, crisis sympathy, tactical truce, and later reciprocity pressure.
- Sexual pressure, refusal, unilateral kisses, sunscreen consent, blocked hug, naming permission, overnight refusal, and timed-hug permission.
- Chizuru and Mami rivalry, false sexual claim, public status assertion, and local apology.

### Strong and weak rules

| Rule | Strength at V020 | Basis and discrimination | Limit |
|---|---|---|---|
| RAG-RUK-R001 / R004 — bodily excitement organizes rapid access and romantic certainty | Strong within the romance domain | Explains measurement, categorical love, repeated scheduling, and persistence. | It is her represented self-model, not diagnosis or proof of reciprocity. |
| RAG-RUK-R002 — asymmetric information becomes negotiated pressure | Strong in rivalry contexts | Explains secrecy leverage, false implication, status claims, and investigation after exclusion. | She can preserve the secret and cooperate locally. |
| RAG-RUK-R005 / R006 — visible cost can redirect tactics without dissolving the goal | Moderate to strong | Explains abandoned disclosure, apology, campaign labor, crisis truce, and later preserved access request. | Definitive rejection remains untested. |
| RAG-RUK-R008 / R009 — resistance can produce narrower negotiated access | Promising but narrow | Supported by blocked-hug-to-name permission and overnight-refusal-to-local-outing/timed-hug sequences. | Earlier repeated kisses through resistance are major counterweight; durable reform is unproved. |

### Tests performed

| Test | Type and frozen basis | Expected discriminating range | Observed outcome | Result |
|---|---|---|---|---|
| RAG-RUK-T05 | Prospective; RAG-PRED-056 frozen at V014 | Shared project welfare should sometimes regulate rivalry without ending the romantic goal. | V015 shows Ruka endorse the Umi route, check Kazuya's jealousy, invoke Sayuri, and perform outreach. | SUPPORTED_IN_THIS_TEST |
| RAG-RUK-T06 | Prospective; RAG-PRED-061 frozen at V016 | The bodily request should receive answer, boundary, contact, withdrawal, or conflict. | V017 narrows the request to sunscreen, then separates a blocked hug from permitted first-name address. | SUPPORTED_IN_THIS_TEST |
| RAG-RUK-T07 | Prospective; RAG-PRED-072 frozen at V018 | The truce and requested outing should produce a V019 consequence. | Ruka is absent in V019. | DISCONFIRMED_AT_DECLARED_HORIZON |
| RAG-RUK-T08 | Retrospective later-consequence check; RUK-S016 | Later evidence may reactivate the route without reversing the failed V019 horizon. | V020 shows reciprocity pressure, refusal of overnight travel, local outing substitution, and a permitted five-second hug. | LATER_SUPPORT; PRIOR_FAILURE_PRESERVED |
| RAG-RUK-T09 | Negative/adversarial consent check | One negotiated act should not be generalized into stable consent sensitivity. | V020 improves request form, while V008-V011 retain sexual pressure and repeated nonconsensual kisses. | SUPPORTED_IN_THIS_TEST as a model limit |

### Failures and error analysis

The V019 absence is a genuine failed horizon, not evidence that Ruka accepted the situation calmly. V020 later activates the route, but does not change what V019 contained. This distinction protects the model from retrospective success inflation.

The most serious model risk is **overgeneralization from recent improvement**. RAG-RUK-R009 describes one finite negotiated hug sequence. It cannot erase earlier repeated physical escalation or justify predicting consent sensitivity under a stronger threat. A second risk is **motive weighting**: sincere love, project help, manipulation, and pressure coexist. Choosing only innocence or only malice would lose observed discrimination.

### Required assumptions, unsupported scenarios, and next evidence

Additional assumptions are required for a medical diagnosis, her family life, school friendships, interests outside Kazuya, mature reciprocal partnership, response to a definitive breakup, or knowledge of Kazuya's direct speech to Chizuru. Unsupported scenarios include using pulse as objective truth, assuming consent from the trial label, generalizing rental expertise, and predicting broad cruelty or selflessness.

The next useful evidence would be her response to an explicit final status decision, whether the V020 request form persists under rivalry threat, ordinary conduct independent of Kazuya, and any direct engagement with earlier consent harm.

## Cross-model findings

The models preserve unequal knowledge at V020. Kazuya knows his love, his own partial confession, and Mami's business explanation. Chizuru knows Mini's disclosure and hears the interrupted answer, but does not know every Ruka contact or Mami's meeting details. Ruka does not know the confession attempt or Chizuru's private replay. Mami knows the prior false-couple system and now reaches Nagomi, but the evidence does not show knowledge of the V020 romantic exchange.

Relationship-switch behavior remains distinct. Kazuya answers Chizuru's direct question by moving toward identification and confession; he answers Ruka through scope-specific refusal and permission; he answers Mami through suspicion without a proved accusation. Chizuru shifts from backstage vocational speech to professional refund, relaxed ordinary conduct, direct inquiry, private replay, and campus deferral. Ruka shifts from reciprocity pressure to narrower requests without surrendering status desire.

Ordinary life remains the weakest shared domain despite V020's university, restaurant, bath, and campus scenes. Those scenes are still saturated by romantic uncertainty. Study habits, stable friendships, independent leisure, and long low-pressure routine remain sparse.

## Audit disposition

| Character | Local readiness | Accepted use | Withheld use |
|---|---|---|---|
| Kazuya | OPERATIONAL_CANDIDATE | V020-bounded family-pressure, support, production, embarrassment, consent differentiation, and interrupted-directness scenarios with named relationship conditions. | Mature partnership, broad routine, reliable confession completion, fair trial resolution, or later development. |
| Chizuru | OPERATIONAL_CANDIDATE | V020-bounded professional, family-welfare, vocational, grief-control, audience, and direct-testing scenarios with motive uncertainty preserved. | Final romantic interior certainty, broad private routine, stable bereavement outcome, wider career success, or later development. |
| Ruka | PARTIAL_MODEL | Cautious rivalry, access-pressure, shared-burden cooperation, and tactical-narrowing scenarios inside the provisional relation. | Whole-person simulation, diagnosis, independent routine, durable consent reform, definitive rejection, or later development. |

Mami is `EVIDENCE_LEDGER_ELIGIBLE` in the cast router, but no reconstruction model exists and her desired endpoint remains too underdetermined for this audit. Mini and Sumi also remain evidence-eligible rather than modeled. Their narrative importance does not authorize unbounded reconstruction.

No `BOUNDED_VALIDATED` label is assigned. The tests remain analyst-selected and source-overlapping, with limited ordinary-life coverage and no independent evaluator. No global registry grade, numeric score, or production capability record is created.
