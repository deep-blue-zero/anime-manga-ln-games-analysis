---
title: "Rent-a-Girlfriend - Local Reconstruction Audit through Volume 010"
artifact_id: RAG_RECONSTRUCTION_AUDIT_V010
artifact_type: local_reconstruction_audit
series: Rent-a-Girlfriend
generation: V1
version: "1.0"
status: canonical
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
created: "2026-09-19"
source_boundary: "Project-local audit of Kazuya, Chizuru, and Ruka models through Japanese manga V010; no V011 or later narrative evidence admitted."
frozen_model_commit: "18fe1738f18a66a91e6a3a340f845f3d7c3d4efe"
---

# Local reconstruction audit through Volume 010

## Audit contract

~~~yaml
audit_state: COMPLETE
checkpoint: RAG_CP_V010
checkpoint_endpoint: V010
frozen_model_commit: 18fe1738f18a66a91e6a3a340f845f3d7c3d4efe
active_substantial_characters:
  - RAG-LOCAL-KAZUYA
  - RAG-LOCAL-CHIZURU
  - RAG-LOCAL-RUKA
later_narrative_exposure: EXCLUDED
global_capability_assessment: NOT_PERFORMED
numeric_accuracy_score: NOT_PRODUCED
~~~

This audit evaluates the exact V010 models at the frozen input commit. It uses their time-indexed states, behavioral rules, relationship conditions, evidence ledgers, and the block's prospectively frozen predictions. Retrospective checks are labeled as such. The same analyst inspected the source and performed this audit, so no check is described as blind. Generated scenes and invented dialogue are not used as evidence.

The audit tests rule discrimination rather than mere plot recall. A useful rule must distinguish plausible alternatives, preserve what each person knows, and specify where it should abstain. Results use `SUPPORTED_IN_THIS_TEST`, `PARTLY_SUPPORTED`, `CONTRADICTED`, `NO_DIAGNOSTIC_OPPORTUNITY`, and `UNRESOLVED`.

## Kazuya Kinoshita

### Snapshot and readiness

~~~yaml
model_path: "04 Character Analysis/Kazuya Kinoshita/RAG_KAZUYA_RECONSTRUCTION_MODEL.md"
evidence_ledger_path: "04 Character Analysis/Kazuya Kinoshita/RAG_KAZUYA_EVIDENCE_LEDGER.md"
model_version: "1.10"
model_revision: "1.9"
admitted_state: KAZ-S012
local_readiness: OPERATIONAL_CANDIDATE
validated_envelope:
  - sudden family or peer scrutiny
  - Chizuru-related vocational support
  - accidental or pressured intimacy with an observable consent boundary
  - bounded repair after concrete harm
  - Ruka status overstatement under direct correction
~~~

This label is local and conditional. It means rule-based scenario work is supportable inside the named envelope, while ordinary routine, calm long-range planning, mature partnership, and generalized honesty remain insufficiently modeled.

### Observed domains

- Breakup response, loneliness, sexual fantasy, embarrassment, family expectations, and peer pressure.
- Rental booking, money use, paid employment, gift planning, and practical support.
- Emergency rescue, privacy protection, reckless self-cost, apology, and friendship repair.
- Chizuru's acting goal, casting loss, family purpose, work pride, and new stage opportunity.
- Ruka's provisional status, attraction, sexual refusal, unilateral kisses, false public claim, and continuing nonreciprocity.
- Sumi practice-client adaptation and purpose-specific consultation.
- Partial disclosure, direct correction, audience-specific concealment, and digital access.

### Strong rules

| Rule | Strength at V010 | Basis and successful discrimination | Limit |
|---|---|---|---|
| RAG-KAZ-R001 — immediate face protection can outrun long-term planning | Strong across repeated audience tests | Predicts sudden false stabilization, concealment, reckless drinking, and V010 family avoidance better than a uniformly honest or purely passive model. | Does not imply that he never tells the truth; Kuribayashi repair and Mami correction are counterexamples. |
| RAG-KAZ-R002 — romantic attention receives alternating inflation and displacement | Strong in romantic appraisal contexts | Explains idealization, discounting of care, paid dream-date intensity, and repeated reliance on service framing. | Ordinary low-stakes self-appraisal remains sparse. |
| RAG-KAZ-R007 — personalized reciprocity can mobilize practical effort | Moderate to strong in gift and vocation contexts | Christmas gift leads to work and reciprocal booking; acting fatigue leads to a bounded gift; stage news produces direct promised support. | The newest stage promise has no durability test yet. |
| RAG-KAZ-R009 — relationship labels do not override observed consent limits | Strong inside the tested intimacy envelope | Kazuya refuses Ruka's sexual pressure, asks Chizuru to move after accidental closeness, accepts the Ferris-wheel correction, and recoils from Ruka's party kiss. | Mature reciprocal intimacy has not been observed. |

### Weak or narrow rules

- RAG-KAZ-R004 is supported by one concentrated peer-conflict sequence; it should not be generalized to every insult or audience.
- RAG-KAZ-R006 has strong rescue evidence but a narrow acute-danger sample. It cannot predict medical competence or calm crisis leadership.
- RAG-KAZ-R008 explains the Kuribayashi repair well, but the family deception shows that concrete guilt does not reliably generalize into broad disclosure.
- RAG-KAZ-R007 remains weaker for sustained planning than for immediate gifts, spending, or verbal encouragement.

### Tests performed

| Test | Type and frozen basis | Expected discriminating range | Observed outcome | Result |
|---|---|---|---|---|
| RAG-KAZ-T01 | Prospective; RAG-PRED-026 frozen at V007 | Under private or sexual opportunity, bounded support and an observable limit were expected rather than automatic exploitation or complete competence. | V008 shows temporary shelter with a request to move and refusal of Ruka's sexual pressure. | SUPPORTED_IN_THIS_TEST |
| RAG-KAZ-T02 | Prospective; RAG-PRED-031 frozen at V008 | If acting support is practical rather than only idealizing speech, gift choice should respond to Chizuru's work burden. | V009's 2,500-yen pickled-plum gift is chosen for acting fatigue after paid consultation. | SUPPORTED_IN_THIS_TEST |
| RAG-KAZ-T03 | Retrospective relationship-switch check; KAZ-S012 | The model should distinguish enthusiasm for Chizuru's stage success from boundary management with Ruka, rather than emit generic romantic pursuit. | Kazuya promises stage support to Chizuru, accepts her bodily correction, and recoils from Ruka's kiss. | SUPPORTED_IN_THIS_TEST |
| RAG-KAZ-T04 | Negative/adversarial generalization check | Evidence of repair and consent sensitivity should not predict generalized honesty under family pressure. | V010 repeats concealment and depends on Chizuru to absorb Nagomi's demand. | SUPPORTED_IN_THIS_TEST as a model limit |

### Failures and error analysis

No audited Kazuya rule is contradicted by V010. The main risk is **overgeneralization**: isolated mature acts can be turned into a global competence claim. RAG-KAZ-T04 blocks that move. A second risk is **motive weighting error**: his wish to protect Chizuru cannot erase the avoidable care burden created by his overdrinking. The current model preserves both intent and cost.

The model has not received a diagnostic test of calm, multi-step family disclosure. Predicting success or failure there would exceed the tested envelope rather than count as a model result.

### Required assumptions, unsupported scenarios, and next evidence

Additional assumptions are required for long-term employment, budgeting discipline, study habits, stable friendship routine, mature reciprocal sex, cohabitation, or a resolved relationship. Unsupported scenarios include expert crisis management, effortless public confession, confident seduction, and knowledge of Chizuru's private romantic state.

The next useful evidence would show whether he responds to Sayuri's hospitalization with practical care or self-focused panic; whether stage support becomes durable action; whether he directly addresses Ruka's kiss and trial status; and whether bounded honesty can extend to family or Kibe.

## Chizuru Ichinose

### Snapshot and readiness

~~~yaml
model_path: "04 Character Analysis/Chizuru Ichinose/RAG_CHIZURU_RECONSTRUCTION_MODEL.md"
evidence_ledger_path: "04 Character Analysis/Chizuru Ichinose/RAG_CHIZURU_EVIDENCE_LEDGER.md"
model_version: "1.10"
model_revision: "1.9"
admitted_state: CHI-S012
local_readiness: OPERATIONAL_CANDIDATE
validated_envelope:
  - rental-client boundary and performance questions
  - identity exposure across campus, work, and family audiences
  - concrete family need and bounded exceptions
  - vocational disclosure, setback, and renewed effort
  - chosen care followed by interpretive or access limits
~~~

The model supports bounded action ranges, not hidden-thought reconstruction. Romantic self-classification, sustained private friendship, close-friend speech, and long-term acting outcome remain outside the validated envelope.

### Observed domains

- Rental-girlfriend work, dissatisfied-client correction, price and fairness regulation, referral, and explicit work pride.
- Campus identity, rental alias, family performance, former-partner confrontation, and audience-sensitive improvisation.
- Rescue, illness, apartment and bathroom care, medicine, batting, hospital visits, and direct crisis messaging.
- Acting training, performance, casting loss, script work, family-linked purpose, and a new stage opportunity.
- Personalized gift exchange, received support, selective disclosure, and role-based rebounding.
- Physical boundaries in accidental, staged, and family-pressure contexts.

### Strong rules

| Rule | Strength at V010 | Basis and successful discrimination | Limit |
|---|---|---|---|
| RAG-CHI-R001 — entitlement or identity risk prompts direct private correction | Strong | Repeats from early client correction through campus limits, unsolicited LINE objection, and the Ferris-wheel accident. | She can temporarily conceal or defer correction when audience risk is higher. |
| RAG-CHI-R002 — concrete family welfare can justify a bounded exception | Strong in family-linked contexts | Explains hospital performance, hot-spring continuation, batting/hospital access, the unbooked birthday visit, and crisis contact. | The exception does not reveal one private motive or grant standing access. |
| RAG-CHI-R003 — audience determines register without defining authenticity | Strong | Distinguishes rental warmth, campus cover, family improvisation, Mami containment, and direct boundary speech. | Register alone cannot identify sincerity or romance. |
| RAG-CHI-R007 — vocational and personal exchanges remain explicitly classified | Strong | Acting purpose, paid support, gift acceptance, rental-work pride, and stage disclosure coexist with continued role language. | Classification does not prove emotional absence. |
| RAG-CHI-R009 — vocational defeat can coexist with renewed work and selective personal access | Moderate to strong | Casting loss is followed by script work, continued bookings, another stage opportunity, chosen family attendance, and crisis communication. | Career outcome and durability remain incomplete. |

### Weak or narrow rules

- RAG-CHI-R005 is based on a small number of public-defense episodes and should not predict universal intervention against unfairness.
- RAG-CHI-R006 covers rescue, shared-space, and exposure tests but should not be turned into a universal intimacy script.
- RAG-CHI-R008 is well supported for the Sumi referral and Kuribayashi coordination but has a narrow professional-collaboration sample.
- Any rule assigning romance as the cause of unpaid care remains unsupported; multiple motives fit the conduct.

### Tests performed

| Test | Type and frozen basis | Expected discriminating range | Observed outcome | Result |
|---|---|---|---|---|
| RAG-CHI-T01 | Prospective; RAG-PRED-023 frozen at V006 | Acting consequences should reorganize rental availability or support rather than remain decorative biography. | V007 casting loss postpones retirement and produces renewed script work and Kazuya's paid support. | SUPPORTED_IN_THIS_TEST |
| RAG-CHI-T02 | Prospective; RAG-PRED-035 frozen at V009 | Direct LINE or prior unpaid care should produce a bounded non-booking access consequence. | V010 adds chosen family attendance and a direct hospital message. | SUPPORTED_IN_THIS_TEST |
| RAG-CHI-T03 | Retrospective professional/intimacy check; CHI-S012 | A skilled provider should lead the requested scenario while retaining observable physical and identity limits. | Chizuru directs lovers-mode poses, protects her identity, and immediately corrects accidental breast contact. | SUPPORTED_IN_THIS_TEST |
| RAG-CHI-T04 | Negative/adversarial access check | Unpaid care and technical contact should not be treated as general permission. | She objects to the unsolicited add in V009, then chooses the same route for a specific V010 crisis. | SUPPORTED_IN_THIS_TEST |

### Failures and error analysis

RAG-PRED-015 expected practical acting consequences in V005 and was disconfirmed at that horizon. The recoverable category is **timing and overgeneralization**, not abandonment of the acting model: the evidence then did not justify immediate consequence, while later volumes supplied casting, support, and stage effects. The failed test remains failed.

The persistent audit risk is **genuine underdetermination**. Professional skill, fairness, family concern, gratitude, and personal attachment can explain overlapping portions of Chizuru's conduct. Selecting romance or emotional absence as the master cause would be a motive-weighting error. The model's abstention is substantive because it still predicts register, boundaries, and bounded exceptions.

### Required assumptions, unsupported scenarios, and next evidence

Additional assumptions are required for explicit romantic confession, reciprocal partnership, sexual intimacy, close-friend banter, domestic routine, long-term acting success, or a settled choice between acting and rental work. Unsupported scenarios include unlimited availability after a crisis message, hostility toward all clients, effortless vulnerability, and access to Kazuya's entire Ruka history.

The next useful evidence would show Sayuri's condition and Chizuru's care decisions; the practical effect of the new stage role; whether LINE remains crisis-specific; how she responds when family and rental truths collide; and any direct self-report that discriminates professional, ethical, familial, and romantic motives.

## Ruka Sarashina

### Snapshot and readiness

~~~yaml
model_path: "04 Character Analysis/Ruka Sarashina/RAG_RUKA_RECONSTRUCTION_MODEL.md"
evidence_ledger_path: "04 Character Analysis/Ruka Sarashina/RAG_RUKA_EVIDENCE_LEDGER.md"
model_version: "1.10"
model_revision: "1.9"
admitted_state: RUK-S009
local_readiness: PARTIAL_MODEL
strongest_domain: "rivalry and access pressure inside the nonreciprocal provisional relationship"
conditionally_operational_domains:
  - status challenge by Chizuru or Mami
  - direct access seeking through campus, work, domestic, or family routes
  - short-term tactical redirection after refusal, apology, or visible family cost
~~~

Ruka does not reach an overall `OPERATIONAL_CANDIDATE` label because nearly all substantial evidence is organized around one relationship goal. School routine, her own family, friendships, non-romantic work conduct, and durable response to rejection remain too sparse. The named rivalry domain can still support cautious rule-based work.

### Observed domains

- Rental-provider recognition, client history, secrecy bargaining, and performance expertise.
- Low-pulse history, medication, self-monitoring, robot metaphor, and subjective love criterion.
- Direct pursuit, messaging, dates, workplace and campus access, cooking, storm lodging, and birthday contact.
- Chizuru and Mami rivalry, family-recognition strategy, fabricated evidence, public overstatement, and local apology.
- Sexual pressure, Kazuya's refusal, and two unilateral kisses.

### Strong and weak rules

| Rule | Strength at V010 | Basis and successful discrimination | Limit |
|---|---|---|---|
| RAG-RUK-R001 — bodily excitement prompts rapid access seeking | Strong within the romance domain | Predicts direct testing, trial bargaining, messaging, campus entry, domestic staging, and family pursuit. | Pulse is her represented criterion, not medical or relational truth. |
| RAG-RUK-R002 — asymmetric information becomes negotiated pressure | Strong within rivalry contexts | Rental knowledge, Chizuru recognition, Mami discovery, false claims, and family labeling become tactical resources. | She sometimes protects the secret and can use a lower public label temporarily. |
| RAG-RUK-R004 — physiological difference organizes self-worth and certainty | Strong as represented self-model | Childhood report, monitoring, and categorical love language recur. | It has no authority as diagnosis or proof of healthy reciprocity. |
| RAG-RUK-R005 — concrete relational cost redirects tactics without dissolving the goal | Moderate to strong | She stops after immediate retreat, abandons disclosure before Nagomi, apologizes after Mami, and then pursues status by another route. | Durable definitive rejection has not been tested. |
| RAG-RUK-R003 — professional experience sharpens performance recognition | Narrow | She identifies Chizuru's provider behavior and rental system accurately. | Few professional settings and no sustained competence sample. |

### Tests performed

| Test | Type and frozen basis | Expected discriminating range | Observed outcome | Result |
|---|---|---|---|---|
| RAG-RUK-T01 | Prospective; RAG-PRED-013 frozen at V004 | Private access should produce direct relational or sexual pressure, with immediate refusal capable of changing the tactic. | V005 private-room escalation stops when Kazuya retreats; no sexual act occurs. | SUPPORTED_IN_THIS_TEST |
| RAG-RUK-T02 | Prospective; RAG-PRED-024 frozen at V006 | The interrupted status proposal could alter later conduct if Ruka appeared. | Ruka does not appear in V007. | NO_DIAGNOSTIC_OPPORTUNITY |
| RAG-RUK-T03 | Prospective; RAG-PRED-034 frozen at V009 | Mami's challenge should create correction, rivalry, or status pressure rather than disappear. | Ruka apologizes locally, then pursues family recognition and initiates another kiss. | SUPPORTED_IN_THIS_TEST |
| RAG-RUK-T04 | Negative/adversarial consent check | Provisional status and sincere love should not be allowed to predict mutual consent. | Kazuya refuses sex in V008 and recoils from the V010 kiss; Ruka's claimed status does not change those facts. | SUPPORTED_IN_THIS_TEST as a model limit |

### Failures and error analysis

The V007 test produced no evidence and is preserved as `NO_DIAGNOSTIC_OPPORTUNITY`; treating absence as calm acceptance would be an evidence error. V010 also exposes an **omitted inhibition risk** in any overbroad directness rule: Ruka accepts the public label “friend” temporarily when it grants entry to the family event. The model must therefore predict categorical claims under challenge as a likely tactic, not as every utterance in every audience.

Her false sex claim is an **evidence-backed limitation**, not a reason to discard her sincere self-report of love. Conversely, sincerity cannot sanitize factual overstatement, pressure, or unilateral contact. A model that chooses only manipulation or only innocence commits motive-weighting error.

### Required assumptions, unsupported scenarios, and next evidence

Additional assumptions are required for a precise medical diagnosis, her own family's conduct, ordinary school friendships, interests outside romance, mature partnership, calm acceptance of lasting rejection, or informed response to all of Kazuya's support language toward Chizuru. Unsupported scenarios include treating pulse as objective love proof, assuming consent from the trial label, professional expertise outside the shown rental-recognition context, and broad cruelty or broad selflessness.

The next useful evidence would show her response to Kazuya's recoil, Sayuri's hospitalization, explicit information about Chizuru's new stage work, a definitive status conversation, and ordinary conduct not organized around Kazuya.

## Cross-model findings

The three models pass the most important knowledge-separation check. Kazuya knows his preference and the full extent of his refusals; Chizuru does not know every private Ruka event; Ruka does not know Kazuya's full support language or Chizuru's private interpretation; the family knows neither rental truth nor trial status. None of the current rules requires giving both sides the same information.

Relationship-switch behavior is also distinct. Kazuya responds to Chizuru through admiration, purchased access, vocational support, and concealment; to Ruka through guilt, attraction, factual correction, refusal, and avoidance. Chizuru shifts among warm provider performance, direct boundary speech, family improvisation, and crisis coordination. Ruka alternates direct claims, tactical lower labels, domestic effort, apology, and renewed pressure. These differences are more useful than generic adjective profiles.

The weakest shared domain is ordinary life. The corpus strongly samples crisis, rivalry, family performance, and identity risk. It weakly samples study, stable friendships, hobbies, quiet work, and low-stakes conversation. All three models must abstain more often there.

## Audit disposition

| Character | Local readiness | Accepted use | Withheld use |
|---|---|---|---|
| Kazuya | OPERATIONAL_CANDIDATE | V010-bounded family-pressure, support, embarrassment, repair, and consent-limit scenarios with named relationship conditions. | Mature partnership, broad ordinary routine, calm long-term planning, or later development. |
| Chizuru | OPERATIONAL_CANDIDATE | V010-bounded professional, family-welfare, identity, vocational, and chosen-care scenarios with motive uncertainty preserved. | Romantic interior certainty, broad private routine, completed career transition, or later development. |
| Ruka | PARTIAL_MODEL | Cautious rivalry, access-pressure, and tactical-redirection scenarios inside the provisional relationship. | Whole-person simulation, diagnosis, family/school routine, durable rejection, or later development. |

No `BOUNDED_VALIDATED` label is assigned. The tests are analyst-selected, source-overlapping, and limited to ten volumes. Kazuya and Chizuru are ready for bounded monograph drafting against RAG_CP_V010; Ruka requires more independent-domain evidence or a deliberately narrow dossier. No global registry grade or production capability record is created.
