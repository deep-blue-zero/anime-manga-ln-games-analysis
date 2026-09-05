---
series: ASCENDANCE_OF_A_BOOKWORM
artifact_type: master_longitudinal_ledger
scope: PRE_SPLIT_CROSS_VOLUME_STATE
generation: V0.4
status: canonical
release_state: mutable_active
source_boundary: "Japanese-language light-novel corpus through V02; V01-V02 frozen from Ascendance of a Bookworm - Volumes 01-02.epub"
committed_high_water_mark: V02
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
---

# Ascendance of a Bookworm — master longitudinal ledger

This file is the canonical **pre-split cumulative state** for the Japanese-primary numbered-volume analysis. It begins before V01 so that the first source-unit transaction has a durable place to propagate evidence instead of allowing important cross-volume observations to remain scattered in standalone deep readings.

It is deliberately one ledger rather than a collection of empty specialist ledgers. A responsibility is split into its own file only after recurring evidence creates independent retrieval or revision pressure.

## Current state

```yaml
longitudinal_state:
  architecture_lifecycle: INITIAL
  committed_high_water_mark: V02
  numbered_volumes_completed:
    - V01
    - V02
  source_derived_claims_present: true
  dedicated_ledgers_split_from_master: []
  next_source_unit: V03
  next_source_unit_authorization: separate
  next_part_boundary_review: V03
```

V01 and V02 are frozen. The entries below preserve the cumulative state promoted from `../02 Sequential Readings/BOOKWORM_V01_DEEP_READING.md` and `../02 Sequential Readings/BOOKWORM_V02_DEEP_READING.md`; they do not import V03 or later knowledge.

## Update contract

After each numbered volume, add only observations that deserve cumulative retrieval beyond the local deep reading. Every durable entry should preserve enough metadata to recover:

- source unit and Japanese part identity;
- focalizer or asserting source position when material;
- evidence class (`DIRECT`, `CORROBORATED INFERENCE`, `INTERPRETIVE HYPOTHESIS`, or `OPEN / UNRESOLVED`);
- current formulation;
- prior formulation when revised;
- revision state (`PRESERVE`, `STRENGTHEN`, `REVISE`, `DOWNGRADE`, `REJECT`, or `OPEN`) where applicable;
- evidence locator or route back to the deep reading/source;
- counterevidence or rival reading when material;
- temporal, identity, institutional, or information state needed to prevent hindsight collapse.

Do not duplicate scene summaries merely because they exist. Promote an observation when it changes or constrains a longitudinal model.

## 1. Character identity, state, and practical agency

**Responsibility:** preserve changes in self-concept, names/titles/roles, developmental state, bodily constraint, competence, resources, institutional position, and the actual options available to a character.

| Source boundary | Subject | State / transition | Evidence class | Current interpretation | Constraint / counterevidence | Evidence route |
|---|---|---|---|---|---|---|
| V01 / `第一部「兵士の娘」I` | Urano / Myne | Urano awakens in Myne's body with prior-life self-continuity and access to Myne's memories; felt ownership of some local emotions initially remains alien | DIRECT + OPEN | Urano's first-person identity continuity is clear; replacement/merger/original-Myne ontology is unresolved | Myne's memories and inherited affect complicate a simple replacement model; Myne's heat hypothesis is not independent confirmation | V01 §§4, 19 C08 |
| V01 | Myne | Investment in continued life shifts from weak/conditional toward created meaning and reciprocal obligation | CORROBORATED INFERENCE | Books remain the dominant stable desire, but a completed written story and later obligation to Lutz give Myne reasons to resist disappearance | Book access still organizes most long-range goals | V01 §§4-5, 8.4, 19 C02 |
| V01 | Myne | Physical capacity improves through repeated gate walks and activity | DIRECT | Part of Myne's weakness is trainable/deconditioning-sensitive rather than a single static illness state | She remains far below ordinary child labor capacity and still has recurrent fever episodes | V01 §6.2-6.3 |
| V01 | Myne | Abnormal internal heat becomes phenomenologically distinct from ordinary weakness/fever | DIRECT + CORROBORATED INFERENCE | Heat responds to despair/anger and concentrated resistance; external eye/pressure effects make a distinct phenomenon likely | Exact mechanism and diagnosis are unconfirmed | V01 §6.4, C05 |
| V01 | Myne | Cognitive/administrative/commercial value becomes legible outside the household | CORROBORATED INFERENCE | Her self-assessment overweights inability to perform physical labor; Otto and Benno identify scarce nonphysical competence | Physical limitations impose genuine costs and dependence | V01 §§9, 15, C03 |
| V02 / `第一部「兵士の娘」II` | Urano / Myne | Identity discontinuity becomes explicit to Lutz; current Myne discloses the prior-life identity and is deliberately accepted by him | DIRECT + OPEN | Social recognition of current Myne is now much clearer than metaphysical continuity; simple instantaneous replacement is weakened but not excluded | Lutz's choice is relational, not metaphysical proof; Effa's earlier fever-dream evidence complicates the transition model | V02 §§4.3, 4.6, 5 |
| V02 | Myne | Investment in continued life becomes explicitly positive | DIRECT + CORROBORATED INFERENCE | Myne now says she does not want to die and values paper progress, family, usefulness, relationships, and enjoyment of current life | She can still conceptualize surrender to the heat; physical crisis can overwhelm agency | V02 §6, C02 |
| V02 | Myne | `身食い` crisis accelerates beyond ordinary fatigue-related fever | DIRECT + CORROBORATED INFERENCE | Myne can distinguish the moving heat from ordinary fever; triggers become easier and suppression more costly; final collapse overwhelms control | Complete mechanism and V02 emergency-treatment outcome remain OPEN | V02 §12 |

A later state must not overwrite an earlier one merely because the mature series provides a more convenient final label.

## 2. Relationships and recipient-conditioned behavior

**Responsibility:** preserve dependence, reciprocity, trust, disclosure, secrecy, affection, obligation, contract, service, mentorship, patronage, rivalry, coercion, conflict/repair, and behavior that changes with the recipient.

| Source boundary | Parties / network | Relationship state | Power / information asymmetry | Change | Evidence class | Evidence route |
|---|---|---|---|---|---|---|
| V01 | Myne ↔ Effa/Gunther/Tuuli | Dependence remains high, but Urano's initially alien family ties begin becoming chosen/reciprocal attachments | Family knows Myne as a sick child; Myne holds inaccessible prior-life knowledge and does not fully share project categories | Care shifts from one-way survival support toward contribution through food, hygiene, gifts, stories, and knowledge | CORROBORATED INFERENCE | V01 §§4.3, 7 |
| V01 | Myne ↔ Tuuli | Caregiver/competence-benchmark relationship becomes more reciprocal | Tuuli retains superior local embodied competence; Myne has imported craft/hygiene/cooking knowledge | Inherited jealousy is increasingly displaced by admiration, gratitude, and efforts to benefit Tuuli | CORROBORATED INFERENCE | V01 §7.4 |
| V01 | Myne ↔ Lutz | Ad hoc exchange develops into a credible complementary partnership substrate | Lutz has strength/local execution; Myne has concepts, literacy, calculation, introductions; both have private goals | Food/help exchange expands into pacing/care, career support, paper-production commitment, and survival-significant obligation | CORROBORATED INFERENCE | V01 §8, C04 |
| V01 | Myne ↔ Otto | Literacy mentorship becomes reciprocal labor relationship and institutional bridge | Otto knows local administration/trade; Myne supplies unusually valuable calculation/document labor | Otto trains and employs Myne while steering her toward work compatible with her body | DIRECT + CORROBORATED INFERENCE | V01 §9.1-9.2 |
| V01 | Myne ↔ Benno | Conditional commercial gatekeeper relationship begins | Benno privately knows his own monopolistic/protective commercial intent and possible `身食い` explanation; Myne does not | Paper prototype becomes a test for access/employment; Benno identifies Myne as potentially valuable product/intellectual capital | DIRECT as viewpoint + CORROBORATED INFERENCE | V01 §9.3-9.4 |
| V02 | Myne ↔ Lutz | Complementary production partnership becomes identity-bearing and survival-relevant | Lutz now knows Urano's disclosed identity; Myne knows Lutz has consciously accepted the current person; family lacks this disclosure | Lutz confronts the discontinuity, accepts current Myne, continues physical/career partnership, and becomes active in emergency survival efforts | DIRECT + CORROBORATED INFERENCE | V02 §§5, 14 |
| V02 | Myne ↔ Benno | Gatekeeper relationship expands into investor/mentor/protector/extractor role | Benno possesses market, contract, guild, and `身食い` knowledge that the children lack; he also wants Myne's product knowledge | He finances tools, binds terms, controls disclosure, teaches pricing, and negotiates emergency magical access | DIRECT + CORROBORATED INFERENCE | V02 §§7, 9-12, 15 |
| V02 | Myne ↔ Frieda / Guild Master | Shared-condition comparison and commercial capture relationship begins | Frieda/Guild Master know `身食い`, magic-tool access, and elite commercial networks; Myne has valuable product knowledge and little institutional leverage | Frieda recognizes the condition; the Guild Master seeks commercial advantage while also becoming the emergency route to a magic tool | DIRECT + CORROBORATED INFERENCE | V02 §§10, 12 |
| V02 | Lutz ↔ family | Occupational disagreement becomes explicit | Parents possess household authority and craft-route expectations; Lutz possesses a strong merchant aspiration but lacks formal merchant upbringing | Father favors craft; mother fears merchant uncertainty/education gap; Myne refuses to decide Lutz's vocation for him | DIRECT | V02 §16 |

Do not infer one timeless relationship from later closeness, hostility, status, or knowledge.

## 3. Institutions, status, law/custom, and coercive structure

**Responsibility:** distinguish stated rules from custom, enforcement, patronage, exceptions, material resources, class barriers, information access, coercive leverage, nominal permission, and practical freedom.

| Source boundary | Institution / rule | Stated rule or doctrine | Observed practice | Enforcement / exception | Agency consequence | Evidence route |
|---|---|---|---|---|---|---|
| V01 | `洗礼式` / age-seven transition | Baptism registers a child as a city person and is tied to beginning formal apprenticeship | Seasonal public procession/temple ceremony for commoners; nobles reportedly receive clergy privately | Class-differentiated ritual practice reported; temple interior perspective unread | Age seven is a social/legal-work threshold rather than the beginning of all responsibility | V01 §12.1 |
| V01 | Apprenticeship / `見習い` | Children normally enter work through family/kin occupational introductions | Tuuli's sewing route follows Effa's network; Lutz lacks support for his desired route | Family opposition and lack of sponsor materially constrain occupational choice | Social connections are productive capital | V01 §12.2 |
| V01 | `市民権` | Otto links city membership to baptismal registration, residence, work, marriage, and housing | Otto spent accumulated capital to obtain city status and remain with Corinna | Outsider acquisition is costly; exact legal code unread | Status can redirect livelihood even when skill and money exist | V01 §12.3 |
| V01 | Travel commerce / `旅商人` | Otto reports mobile trade knowledge/routes are normally transmitted within traveling families | No ordinary city-child apprenticeship path is described | City settlement/citizenship is itself a common aspiration in Otto's account | Lutz's imagined career requires redefinition rather than simple apprenticeship | V01 §9.3, §17 |
| V01 | Noble-linked magic access | Benno reports magical tools are expensive and access may require noble contract/patronage | No tool is directly observed in use in V01 | Benno's account is informed testimony, not demonstrated law/mechanism | If his `身食い` model is correct, survival could create severe dependence/coercive leverage | V01 §6.4, §16.4 |
| V02 | `契約魔術` | Magical bilateral contract is strongly binding and breach can threaten life | Restricted magical paper/ink, signatures, blood, activation, disappearance of contract paper | Strong enforcement does not preserve a readable ordinary copy of terms | Contract literacy, memory, and bargaining remain essential even under magical enforcement | V02 §9 |
| V02 | Commercial Guild | Trade requires registration/authorization; pre-baptism temporary registration is normally tied to merchant families | Blood-linked guild cards, access control, deposit/transfer functions, and discretionary admission are observed | Myne/Lutz are an unusual non-kin exception won through negotiation/leverage | Technical/product capability cannot become legal commerce without institutional permission | V02 §10 |
| V02 | Noble-linked magic access | `身食い` survival can require scarce magic tools obtained through noble connections | Frieda is alive because Guild Master wealth/connections acquired tools; Benno negotiates emergency access for Myne | Access is temporary, costly, and scarce rather than universal | Survival probability is class- and patronage-sensitive | V02 §12 |
| V02 | Occupational/marriage network | Work, inheritance, citizenship, marriage, and guild power are tightly coupled | Gilberta female-line inheritance, Corinna heirship, Otto citizenship purchase, craftmaster/customer requirements | Guild Master market power can affect marriage options and business risk | Formal and informal status shape intimate and occupational choices together | V02 §19 |

Political or ethical judgment should follow reconstruction of the actual choice set rather than substitute for it.

## 4. Knowledge transfer, literacy, production, education, labor, and commerce

**Responsibility:** preserve the chain from remembered/claimed knowledge through local translation, demonstrated result, collaborators/prerequisites, and systemic consequence.

| Source boundary | Knowledge / process | Claimed knowledge | Local translation / collaborators | Result | Systemic consequence | Evidence route |
|---|---|---|---|---|---|---|
| V01 | General innovation model | Urano remembers many modern/historical concepts | Success depends on local materials, embodied craft, labor, tools, risk knowledge, institutions, and collaborators | Mixed: several low-dependency transfers work; paper/clay/ink attempts repeatedly fail | Establishes the cumulative rule that information alone is not practical agency | V01 §10, C01 |
| V01 | Hair-cleaning mixture / decorative craft / basketry | Myne possesses remembered formulas or actual prior craft experience | Household ingredients, Effa/Tuuli materials and labor, locally improvised tools | Demonstrably successful and socially visible | Novel personal-care/aesthetic products attract adoption/commercial interest | V01 §10.1 |
| V01 | Cooking / parue utilization | Myne imports techniques rather than exact ingredient identities | Local food knowledge, family labor, Lutz household scarcity | Multiple accepted dishes; parue residue materially increases usable food | Knowledge can create household value when adapted rather than replicated literally | V01 §§10.1, 13 |
| V01 | Papyrus/clay/wood/bamboo/ink writing media | Myne knows that historical writing media existed but often lacks reliable process knowledge | Lutz supplies physical/local help; household scarcity and category conventions constrain experiments | Papyrus poor; clay inscription works but firing fails; wood/bamboo socially misclassified as fuel; soot/clay pencil works as substitute | Failure modes demonstrate procedural, storage, communication, and resource bottlenecks | V01 §10.2 |
| V01 | Literacy and gate administration | Urano knows how to read/write conceptually; local script/vocabulary must be learned | Otto teaches with slate and job-specific documents | Rapid task-specific literacy, arithmetic, correspondence handling | Literacy provides rare nonphysical employability and social access | V01 §9.1, §11 |
| V01 | Plant-fiber paper proposition | Myne knows non-animal writing material should be possible | Lutz commits to physical production; Benno supplies a market gate | No prototype yet; conditional deadline established | Private book-making desire becomes a potentially disruptive commercial project | V01 §9.3, P01-P03 |
| V02 | Plant-fiber paper | Myne remembers the functional concept but not a locally turnkey process | Lutz, Marc, Benno, artisans, tools, wood species, binder, steaming, beating, sheet formation, measurement, water, and season | Functional paper completed; Trombe performs especially well but is hazardous/scarce; ordinary wood remains viable with tuning | Paper becomes a real commodity and future production system, not merely a private experiment | V02 §7 |
| V02 | Hair-cleaning mixture replication | Household process already works | Professional refinement filters out small plant solids and initially worsens function | Failure reveals unrecognized abrasive/scrubbing contribution | Demonstrates tacit/hidden process variables and risk of optimizing the wrong feature | V02 §8 |
| V02 | Hair ornaments | Myne supplies design/technique and product concept | Frieda commission, Benno pricing, Effa/Tuuli production skill, Lutz-family paid labor, household coordination | Luxury commission succeeds; wider demand and rush orders emerge | Household craft becomes networked micro-enterprise and exposes imitation/control pressure | V02 §17 |
| V02 | Merchant education | Myne/Lutz possess uneven partial skills | Benno/Marc/Otto plus deliberate winter study supply etiquette, local numeracy tools, money, product knowledge, literacy, and memory discipline | Both expand practical merchant competence | Human capital becomes an explicit prerequisite for occupational mobility | V02 §§16, 18 |

Credit causal contribution rather than protagonist-centered narrative salience.

## 5. World-model evidence: religion, magic/system mechanics, history, politics, economics

**Responsibility:** keep character belief, institutional doctrine, observed regularity, demonstrated exception, independent corroboration, and unresolved contradiction distinct.

| Source boundary | Domain | Proposition | Source position | Evidence class | Corroboration / exception | Current world-model state | Evidence route |
|---|---|---|---|---|---|---|---|
| V01 | Reincarnation/identity | Urano awakens as Myne with local memories | Urano/Myne first person | DIRECT for experience; OPEN for ontology | Shuu independently anchors Urano's prior-life traits; no independent metaphysical explanation | Event/continuity experienced; mechanism unresolved | V01 §§3.4, 4, C08 |
| V01 | Parue | Winter `パルゥ` trees/fruit follow unusual locally known conditions and noon change | Myne + Tuuli/local practice | DIRECT/observed + local testimony | No mechanism supplied | Treat as stable local phenomenon; Earth botanical analogy insufficient | V01 §16.1 |
| V01 | Magical creatures / `魔石` | Small `シュミル` are `魔獣`; mishandled disassembly can dissolve body around a recoverable/sellable stone | Lutz/local children | DIRECT as viewpoint/practice | Stone has ordinary commercial destination | Magic-related categories have commoner economic consequences | V01 §16.3 |
| V01 | `魔力` / `身食い` | Benno says some commoners possess magic and excess magic may consume a person without discharge | Benno private testimony | DIRECT as testimony; diagnosis OPEN | Myne's abnormal heat + peer-observed eye/pressure effects are compatible but not diagnostic | Magic-linked explanation is leading reader-side hypothesis, not confirmed fact | V01 §§6.4, 16.4, C05 |
| V01 | Religion/civic registration | Temple baptism is tied to city recognition and work transition | Otto/local public practice | CORROBORATED INFERENCE for institutional role | No temple-insider viewpoint yet | Religion and civic status are institutionally entangled at V01 boundary | V01 §12.1 |
| V02 | Reincarnation/identity | Current Myne discloses Urano identity; Lutz accepts current person; earlier Myne had fever dreams suggestive of another experiential world | Myne, Lutz, Effa | DIRECT for reports/choices; OPEN for ontology | Behavioral discontinuity is independently recognized; dream evidence complicates simple replacement | Social continuity strengthened; metaphysical mechanism remains unresolved | V02 §5 |
| V02 | `身食い` | Frieda/Guild Master identify a recognized condition involving internally accumulating `魔力` and temporary discharge through magic tools | Frieda/Guild Master/Benno + Myne/Lutz observation | CORROBORATED INFERENCE approaching strong diagnosis; mechanism partly OPEN | Independent analogous symptoms plus final external heat/vapor crisis; V02 treatment outcome unread | `身食い` is the strongly supported local diagnosis; exact system model remains incomplete | V02 §12 |
| V02 | `魔力` social doctrine | Marc presents magic as a noble power, while informed actors describe commoner `身食い` as excess magic | Marc versus Benno/Frieda/Guild Master | OPEN / UNRESOLVED | Evidence is internally tensioned rather than one-sided | Noble-only doctrine cannot yet be treated as objective universal fact | V02 §13 |
| V02 | Contract/authorization magic | Magic is used in contracts and blood-linked guild registration/finance | Benno + directly observed institutional practice | DIRECT + CORROBORATED INFERENCE | Multiple independent commercial uses | Magic is embedded in ordinary institutional power, not only creatures/illness | V02 §§9-10 |
| V02 | Weekly social time | Seven named days structure routine and `土の日` is observed as rest day | Local practice / Myne learning | DIRECT as observed convention | Myne learns terminology relatively late | Calendar knowledge is role-distributed and socially operational | V02 §20 |

A doctrine can be socially real while its metaphysical proposition remains unproven.

## 6. Focalization, information asymmetry, and epistemic state

**Responsibility:** preserve who knows what, who believes what, what the reader knows, what is concealed or misunderstood, and how information changes available action.

| Source boundary | Knower / focalizer | Information state | Reliability / limitation | Disclosure or concealment change | Consequence | Evidence route |
|---|---|---|---|---|---|---|
| V01 | Myne | Interprets setting through Japanese/Earth analogies | Analogies are cognitively useful but repeatedly incomplete; observation must be separated from inference | No omniscient correction is available for many domains | Corpus must keep observation, analogy, and local testimony distinct | V01 §3.1 |
| V01 | Otto / Benno | Independently observe Myne's literacy, calculation, composure, and negotiation as age/class anomalies | Both have relevant adult work experience but commercial interests | Private epilogue gives reader information Myne lacks | Reader knows Myne is more conspicuously anomalous than she realizes | V01 §§3.2, 15 |
| V01 | Benno | Suspects `身食い`; knows possible noble/magic-tool implications | Explicit uncertainty; not diagnostic confirmation | Hypothesis is private and unavailable to Myne | Reader-side model advances beyond protagonist knowledge | V01 §§3.2, 6.4 |
| V01 | Lutz / Fey | Observe Myne's recipient-specific behavior, unusual mind, and anger-linked eye/pressure effect | Child viewpoints; Fey's fear affects description | Corroborates that anomaly is not purely first-person fever phenomenology | Social visibility/risk increases | V01 §§3.3, 15.4 |
| V01 | Shuu | Supplies prior-life baseline for Urano's book fixation/tunnel attention | Retrospective friend viewpoint | Establishes pre-reincarnation continuity unavailable to local cast | Prevents attributing all obsessive behavior to Myne's new circumstances | V01 §3.4 |
| V02 | Lutz | Recognizes knowledge/behavior discontinuity and receives Urano identity disclosure | Strong direct familiarity with current Myne; still lacks metaphysical access | Becomes uniquely informed local peer | Identity secrecy is no longer universal; relationship acquires privileged epistemic status | V02 §§4.3, 14 |
| V02 | Effa | Remembers prior Myne's fever-dream reports and interprets current drive through family resemblance | Retrospective maternal viewpoint; ordinary explanatory frame | Supplies reader evidence not available to Lutz/Myne in their confrontation | Weakens overly clean replacement narratives while showing family normalization | V02 §§4.6, 5 |
| V02 | Benno / Guild Master / Frieda | Possess much more `身食い`, guild, pricing, and noble-access knowledge than Myne | Commercial interests and family interests shape presentation | Myne gains partial diagnosis/access knowledge; emergency planning still contains private negotiations | Survival and market agency depend on navigating asymmetric expert information | V02 §§10-12 |
| V02 | Myne | Possesses broad conceptual knowledge but repeatedly lacks local tacit variables and institutional assumptions | Strong experiment design; incomplete local process/mechanism knowledge | Paper and shampoo failures expose hidden variables | Epistemic humility/iteration becomes more important than raw recall | V02 §§7-8 |

Do not flatten multiple viewpoints into an omniscient composite narrator.

## 7. Ordinary life, bodily limits, risk, competence, and low-stakes behavior

**Responsibility:** retain mundane evidence only when it materially improves reconstruction of values, attachment, competence, self-presentation, recipient effects, state transitions, or practical agency.

| Source boundary | Subject | Ordinary-life observation | Analytical significance | Stability / state dependence | Evidence route |
|---|---|---|---|---|---|
| V01 | Myne | Strong prior-life hygiene, food, bathing, tooth, and cleanliness expectations produce both innovation and disgust | Imported values are behaviorally productive but not uniformly prosocial; willingness to help is recipient/cost dependent | Acculturation begins but prior standards persist | V01 §14.1 |
| V01 | Myne | Initially recoils from slaughter, entrails, unfamiliar ingredients, fire/tool work; can later remain present and participate more | Demonstrates genuine local acculturation and competence change | Some limits improve with exposure; strength remains limiting | V01 §14.2, §6.3 |
| V01 | Household | Ash, fats, cloth, fuel, gathered food, game, and winter processing all have multiple competing uses | Material scarcity explains many rational constraints on experimentation | Structural household condition at V01 boundary | V01 §13 |
| V01 | Lutz household | Food competition makes higher-yield parue recipes materially valuable | Grounds Lutz's reciprocity and shows innovation value is need-relative | Household-specific evidence; do not universalize exact scarcity level | V01 §§8.1, 13 |
| V01 | Myne | Self-worth tracks comparison with Tuuli's physical labor while outsiders value cognitive work | Ordinary work mismatch is a primary source of distorted self-assessment | Likely state-dependent as occupational options expand; later evidence needed | V01 §§6.3, 14.3, C03 |
| V02 | Myne/Lutz households | Paid winter work changes willingness to supply labor and turns kin craft into accounted production | Cash and explicit accounting alter household incentives and reveal hidden economic contribution | Emerging enterprise state, not yet mature firm structure | V02 §§16-17 |
| V02 | Myne | Everyday enjoyment, usefulness, study, production, and family contribution become explicit reasons to remain alive | Ordinary life is now evidence of identity investment rather than mere background | Stronger than V01 but remains vulnerable to physical crisis | V02 §6 |
| V02 | Myne/Lutz | Different memory strategies reflect information abundance versus scarcity | Myne expects future lookup; Lutz must retain scarce instruction | Environmental information access shapes cognitive strategy and merchant competence | V02 §18 |

Possible evidence includes food, clothing, comfort, hobbies, work rhythm, study, gifts, shopping, etiquette, humor, rest, annoyance, avoidance, sensory preference, domestic routine, and treatment of low-status or low-stakes interactions.

This section is not a trivia inventory.

## 8. Major claims, counterevidence, and revision state

**Responsibility:** preserve only claims important enough that later evidence could materially strengthen, revise, downgrade, reject, or leave open.

| Claim ID | First source boundary | Earlier formulation | Revision state | Current formulation | Supporting evidence | Counterevidence / rival reading | Current authority |
|---|---|---|---|---|---|---|---|
| V01-C01 | V01 | Modern knowledge is conditional agency: value depends on local translation through material, embodied, labor, institutional, and relational prerequisites | STRENGTHEN | Imported information enters as a hypothesis whose practical value depends on local translation; tacit/hidden variables can defeat superficially improved replication | Completed paper only through distributed production system; shampoo filtering failure; localization of sheet size | Some low-dependency techniques still transfer rapidly | V02 current state; V01 historical formulation preserved |
| V01-C02 | V01 | Books remain Myne's stable core desire, but relational obligation has begun to supply an independent reason to preserve life | REVISE / STRENGTHEN | Books remain central, while relationships, usefulness, work, family belonging, and enjoyment now provide explicit positive reasons to live | Myne states she does not want to die and likes current life; identity/Lutz/family developments | Heat crisis can still overwhelm agency; disappearance remains conceptually available in identity confrontation | V02 current state |
| V01-C03 | V01 | Myne's self-assessment systematically undervalues nonphysical competence | STRENGTHEN | Commercial and institutional actors increasingly price Myne's literacy, planning, product knowledge, and negotiation as scarce capital | Benno/Guild Master/Frieda interest; contracts; commissions; paper | Physical dependence remains real and economically consequential | V02 current state |
| V01-C04 | V01 | Myne/Lutz reciprocity has become a durable complementary partnership substrate | STRENGTHEN | Partnership now spans production, education, identity recognition, privileged disclosure, care, and survival motivation | Paper production; identity confrontation; final crisis; winter education | No independent relationship synthesis yet; family conflict remains unresolved | V02 current state |
| V01-C05 | V01 | Myne's abnormal heat is distinct from ordinary deconditioning/illness; `身食い` is plausible but unconfirmed | STRENGTHEN | `身食い` is now the strongly corroborated local diagnosis matching Myne's moving heat and accelerating crisis; exact mechanism and V02 intervention outcome remain OPEN | Frieda/Guild Master independent recognition; external heat/vapor; Benno emergency plan | No on-page V02 treatment outcome; magic system incomplete | V02 current state |
| V01-C06 | V01 | Literacy and writing materials function as stratified institutional/class resources | STRENGTHEN | Literacy, contract comprehension, record reconstruction, and institutional procedure remain power even when magic itself enforces agreements and registration | Contract-magic memory test; guild procedures; merchant education | No systematic citywide literacy rate | V02 current state |
| V01-C07 | V01 | Myne is increasingly socially legible as anomalous outside her family | STRENGTHEN | Anomalous knowledge/products create increasing scrutiny, capture attempts, and strategic concealment by competing commercial actors | Lutz confrontation; Guild Master/Frieda; Benno controls disclosure; product novelty | Family continues to normalize behavior through recovery/kin resemblance | V02 current state |
| V01-C08 | V01 | Original-Myne/Urano ontology is unresolved | REVISE / OPEN | Ontology remains unresolved; simple instantaneous replacement is weakened by family memory of prior fever dreams and by the relationally explicit transition recognized by Lutz | Urano continuity, Myne memories, Lutz confrontation, Effa fever-dream report | No independent metaphysical mechanism; social acceptance is not proof | V02 current state |
| V02-C09 | V02 | — | OPEN | Magic is demonstrably embedded in contracts, guild identity/authorization/finance, and survival infrastructure | Contract magic, blood-linked guild cards, magic tools | Exact institutional ownership and mechanics remain partial | V02 current state |
| V02-C10 | V02 | — | OPEN | `身食い` survival is class-mediated by money and noble-linked access to scarce magical tools | Frieda/Guild Master history; Benno survival-capital framing | V02 does not show Myne's intervention outcome or universal rule | V02 current state |
| V02-C11 | V02 | — | OPEN | Product diffusion creates exposure, bargaining, imitation, and institutional-control pressure alongside opportunity | Hair-ornament demand; Guild Master capture attempt; Benno secrecy | Full competitive market not yet observed | V02 current state |
| V02-C12 | V02 | — | OPEN | Scalable production increasingly depends on household/craft networks rather than Myne's personal labor | Effa/Tuuli/Lutz-family production; Marc/artisans; tool financing | Scale remains limited and seasonal | V02 current state |
| V02-C13 | V02 | — | OPEN | Lutz's occupational agency is constrained by kin expectations and educational capital while paid coordination/training expand his option set | Family dispute; winter education; wage-accounted work | No family resolution yet | V02 current state |
| V02-C14 | V02 | — | OPEN | Ordinary noble-only `魔力` doctrine conflicts with evidence of commoner `身食い`; a more precise model is required | Marc versus Benno/Frieda/Guild Master | Terminology/social-doctrine explanation not yet available | V02 current state |

A claim's historical formulation remains discoverable even after the current model changes.

## 9. Prospective prediction and open-question register

### V01 → V02 adjudication

The following predictions were frozen before V02 was opened. Their historical wording is preserved; outcomes are now recorded from V02.

| Entering boundary | Question / prediction | Confidence | Basis at entering boundary | Tested by | Outcome | Historical note |
|---|---|---:|---|---|---|---|
| V01 | V01-P01 — Myne and Lutz will make a serious paper prototype attempt because both employment opportunity and Myne's book goal now depend on it | high | Benno's explicit conditional gate; Lutz's commitment | V02 | CONFIRMED / STRENGTHENED | Functional paper completed and accepted |
| V01 | V01-P02 — Practical process/material translation will be a larger paper bottleneck than merely remembering that plant-fiber paper exists | high | V01 production-failure pattern; bodily limits | V02 | CONFIRMED / STRENGTHENED | Multiple material/process variables and collaborators determine outcome |
| V01 | V01-P03 — Benno will become more involved if the prototype is viable, with commercially protective/controlling interests rather than pure charity | high | Private epilogue intent | V02 | CONFIRMED / STRENGTHENED | Financing, contracts, secrecy, instruction, emergency planning |
| V01 | V01-P04 — Lutz's family opposition or occupational expectations will materially affect his merchant route | medium-high | Kin-sponsored apprenticeship structure; Lutz secrecy | V02 | CONFIRMED / STRENGTHENED | Father favors craft; mother fears merchant uncertainty/education gap |
| V01 | V01-P05 — Myne's abnormal heat will recur and require a better explanation; `身食い` remains the leading reader-side hypothesis | high recurrence; medium diagnosis | First-person episodes + Benno hypothesis | V02 | STRONGLY CONFIRMED; mechanism partly OPEN | Frieda/Guild Master independently recognize condition; crisis accelerates |
| V01 | V01-P06 — Myne's unusual literacy/products/behavior will attract increasing scrutiny outside the family | medium-high | Otto, Benno, Fey, neighborhood product interest | V02 | CONFIRMED / STRENGTHENED | Lutz identity confrontation and commercial capture pressure |
| V01 | V01-P07 — Gate clerical work will remain a credible fallback or competing labor path | medium | Otto's training and valuation | V02 | PRESERVE / DOWNWEIGHT | Otto still requests calculation help; merchant/paper route dominates |
| V01 | V01-P08 — Family attachment will deepen while book/resource/risk conflicts continue | medium | clay-story acceptance, survival obligation, repeated household friction | V02 | CONFIRMED / STRENGTHENED | Myne explicitly values current life and household contribution |
| V01 | V01-P09 — Temple/noble/magic institutions will become more relevant if the heat problem is real, but exact timing/access remains unknown | medium | Benno testimony + baptism/citizenship link | V02 | CONFIRMED / STRENGTHENED | Contract magic, guild magic, noble-linked survival tools |
| V01 | V01-P10 — Myne/Lutz division of labor will become more explicit, with concepts/planning paired to Lutz's physical/local execution | high | merchant-meeting commitment | V02 | CONFIRMED / EXPANDED | Production, education, identity, care, emergency action |

### V02 → V03 frozen prospective state

These entries are frozen **before V03 is opened**.

| Entering boundary | Question / prediction | Confidence | Basis at entering boundary | Tested by | Outcome | Historical note |
|---|---|---:|---|---|---|---|
| V02 | V02-P01 — Guild Master/Frieda household will attempt to use remaining magical-tool capacity on Myne's present crisis | high | Benno emergency plan and prior negotiation | V03 or later | OPEN | Frozen at V02 |
| V02 | V02-P02 — Available intervention will be temporary rather than a definitive cure | high | Frieda history; depleted tool; reported limited extension | V03 or later | OPEN | Frozen at V02 |
| V02 | V02-P03 — Earnings/product knowledge will increasingly function as survival capital, not only book-production capital | high | Benno survival-capital framing | V03 or later | OPEN | Frozen at V02 |
| V02 | V02-P04 — Frieda will become a significant `身食い`/wealth/noble-access comparison and information node | medium-high | shared condition and Guild Master resources | V03 or later | OPEN | Frozen at V02 |
| V02 | V02-P05 — Lutz's merchant route will require concrete family resolution before ordinary apprenticeship/baptism progression | high | unresolved parental opposition | V03 or later | OPEN | Frozen at V02 |
| V02 | V02-P06 — Lutz will retain privileged knowledge of Urano identity; equivalent immediate family disclosure is not expected | medium-high | V02 confrontation and family normalization | V03 or later | OPEN | Frozen at V02 |
| V02 | V02-P07 — Spring paper scaling will require more formal labor/tooling/market organization and strategic disclosure control | high | winter limits, financing, guild rivalry | V03 or later | OPEN | Frozen at V02 |
| V02 | V02-P08 — Hair ornaments will move toward a broader market with imitation/competition pressure | high | pre-launch demand and rush production | V03 or later | OPEN | Frozen at V02 |
| V02 | V02-P09 — Noble-only magic doctrine versus commoner `身食い` will require a more precise model | medium | V02 contradictory testimony | V03 or later | OPEN | Frozen at V02 |
| V02 | V02-P10 — Merchant survival will depend increasingly on contract, etiquette, legal, and institutional literacy rather than invention alone | high | contract magic and guild registration | V03 or later | OPEN | Frozen at V02 |
| V02 | V02-P11 — Stronger desire to live will reduce voluntary surrender risk, but worsening symptoms can still overwhelm agency | medium-high | explicit attachment plus final collapse | V03 or later | OPEN | Frozen at V02 |
| V02 | V02-P12 — V03 closes Part 1 and requires the first mandatory architecture/promotion review after its freeze | certain process state | governing architecture | V03 | OPEN | Process obligation frozen at V02 |

## 10. Dedicated-ledger split rule

Split a responsibility out of this file when at least one of the following becomes true:

- entries are numerous enough that independent retrieval is materially faster or safer;
- the dimension has its own revision cadence or evidence schema;
- several character/specialist artifacts depend on it directly;
- maintaining it inside the master file causes duplicated reconstruction work;
- the dimension needs an independent audit, locator index, or high-water mark.

Likely—but not guaranteed—future splits include character/state, relationships, institutions/agency, knowledge-production/economy, world-model/religion-magic, information state, ordinary life/body, and claim revision.

Do not split for cosmetic symmetry or because another series uses that ledger.

At the V02 boundary, **no split is yet warranted**. Candidate promotions—Myne, Lutz, Myne/Lutz, `身食い`/magic-class access, and knowledge/production—must be reconsidered at the mandatory V03 Part 1 boundary review.

## 11. Part-boundary reconciliation

At V03, V07, V12, V21, and V33:

1. reconcile all entries through the just-frozen part boundary;
2. adjudicate material predictions and claims;
3. identify unresolved contradictions;
4. check whether a responsibility should split or merge;
5. identify character/relationship promotion candidates without enrolling them automatically;
6. identify specialist responsibilities that have become warranted;
7. record any required architecture amendment in `../CURRENT_STATE_AND_CORPUS_MAP.md`.

The first mandatory review occurs **after V03**. V02 has not exposed a material representation gap requiring an early split.

## 12. Freeze and mutability behavior

This ledger is mutable current state. Frozen deep readings preserve their historical source boundaries. Updating this ledger may revise the **current** interpretation but must not rewrite the earlier deep-reading record or pretend later knowledge was available prospectively.

If a responsibility later splits into a dedicated canonical ledger, this file should retain a compact routing note and cease duplicating that responsibility's detailed current state.
