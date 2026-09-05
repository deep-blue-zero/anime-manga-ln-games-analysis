---
series: ASCENDANCE_OF_A_BOOKWORM
artifact_type: master_longitudinal_ledger
scope: PRE_SPLIT_CROSS_VOLUME_STATE
generation: V0.3
status: canonical
release_state: mutable_active
source_boundary: "Japanese-language light-novel corpus through V01; V01 frozen from Ascendance of a Bookworm - Volume 01.epub"
committed_high_water_mark: V01
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
  committed_high_water_mark: V01
  numbered_volumes_completed:
    - V01
  source_derived_claims_present: true
  dedicated_ledgers_split_from_master: []
  next_source_unit: V02
  next_source_unit_authorization: separate
```

V01 is frozen. The entries below are cumulative state promoted from `../02 Sequential Readings/BOOKWORM_V01_DEEP_READING.md`; they do not import V02 or later knowledge.

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

Possible evidence includes food, clothing, comfort, hobbies, work rhythm, study, gifts, shopping, etiquette, humor, rest, annoyance, avoidance, sensory preference, domestic routine, and treatment of low-status or low-stakes interactions.

This section is not a trivia inventory.

## 8. Major claims, counterevidence, and revision state

**Responsibility:** preserve only claims important enough that later evidence could materially strengthen, revise, downgrade, reject, or leave open.

| Claim ID | First source boundary | Earlier formulation | Revision state | Current formulation | Supporting evidence | Counterevidence / rival reading | Current authority |
|---|---|---|---|---|---|---|---|
| V01-C01 | V01 | — | STRENGTHEN | Modern knowledge is conditional agency: value depends on local translation through material, embodied, labor, institutional, and relational prerequisites | Contrasting successful craft/cooking transfers with failed writing-media attempts; dependence on collaborators | Some low-dependency techniques transfer very rapidly | V01 freeze |
| V01-C02 | V01 | — | PRESERVE | Books remain Myne's stable core desire, but relational obligation has begun to supply an independent reason to preserve life | Prologue/Shuu continuity; clay-story hope; Lutz obligation during heat episode | Long-range goals remain overwhelmingly book-centered | V01 freeze |
| V01-C03 | V01 | — | PRESERVE | Myne's self-assessment systematically undervalues nonphysical competence | “Useless” self-judgment versus Otto/Benno valuation | Physical inability genuinely burdens household and limits options | V01 freeze |
| V01-C04 | V01 | — | PRESERVE | Myne/Lutz reciprocity has become a durable complementary partnership substrate | Food/help exchange, pacing, career support, paper commitment, Lutz POV | No formal partnership; motivations remain mixed | V01 freeze |
| V01-C05 | V01 | — | OPEN | Myne's abnormal heat is distinct from ordinary deconditioning/illness; `身食い` is plausible but unconfirmed | Affect/will-linked phenomenology, peer-observed anomaly, Benno testimony | No diagnostic confirmation or direct magical measurement | V01 freeze |
| V01-C06 | V01 | — | PRESERVE | Literacy and writing materials function as stratified institutional/class resources in the observed city domains | Household absence, pictorial signs, slate learning, expensive parchment/ink, gate paperwork | No systematic citywide literacy rate | V01 freeze |
| V01-C07 | V01 | — | PRESERVE | Myne is increasingly socially legible as anomalous outside her family | Otto/Benno, Lutz/Fey, product novelty | Family normalizes her; no formal authority response yet | V01 freeze |
| V01-C08 | V01 | — | OPEN | Original-Myne/Urano ontology is unresolved | Urano first-person continuity + Myne memory/affect access + Myne's own heat speculation | V01 contains no independent metaphysical adjudication | V01 freeze |

A claim's historical formulation remains discoverable even after the current model changes.

## 9. Prospective prediction and open-question register

The following V02-facing state is frozen **before V02 is opened**. These predictions are not evidence about V02 and must be adjudicated only after a separately authorized V02 read.

| Entering boundary | Question / prediction | Confidence | Basis at entering boundary | Tested by | Outcome | Historical note |
|---|---|---:|---|---|---|---|
| V01 | V01-P01 — Myne and Lutz will make a serious paper prototype attempt because both employment opportunity and Myne's book goal now depend on it | high | Benno's explicit conditional gate; Lutz's commitment | V02 or later | OPEN | Frozen at V01 |
| V01 | V01-P02 — Practical process/material translation will be a larger paper bottleneck than merely remembering that plant-fiber paper exists | high | V01 production-failure pattern; bodily limits | V02 or later | OPEN | Frozen at V01 |
| V01 | V01-P03 — Benno will become more involved if the prototype is viable, with commercially protective/controlling interests rather than pure charity | high | Private epilogue intent | V02 or later | OPEN | Frozen at V01 |
| V01 | V01-P04 — Lutz's family opposition or occupational expectations will materially affect his merchant route | medium-high | Kin-sponsored apprenticeship structure; Lutz secrecy | V02 or later | OPEN | Frozen at V01 |
| V01 | V01-P05 — Myne's abnormal heat will recur and require a better explanation; `身食い` remains the leading reader-side hypothesis | high recurrence; medium diagnosis | First-person episodes + Benno hypothesis | V02 or later | OPEN | Frozen at V01 |
| V01 | V01-P06 — Myne's unusual literacy/products/behavior will attract increasing scrutiny outside the family | medium-high | Otto, Benno, Fey, neighborhood product interest | V02 or later | OPEN | Frozen at V01 |
| V01 | V01-P07 — Gate clerical work will remain a credible fallback or competing labor path | medium | Otto's training and valuation | V02 or later | OPEN | Frozen at V01 |
| V01 | V01-P08 — Family attachment will deepen while book/resource/risk conflicts continue | medium | clay-story acceptance, survival obligation, repeated household friction | V02 or later | OPEN | Frozen at V01 |
| V01 | V01-P09 — Temple/noble/magic institutions will become more relevant if the heat problem is real, but exact timing/access remains unknown | medium | Benno testimony + baptism/citizenship link | V02 or later | OPEN | Frozen at V01 |
| V01 | V01-P10 — Myne/Lutz division of labor will become more explicit, with concepts/planning paired to Lutz's physical/local execution | high | merchant-meeting commitment | V02 or later | OPEN | Frozen at V01 |

## 10. Dedicated-ledger split rule

Split a responsibility out of this file when at least one of the following becomes true:

- entries are numerous enough that independent retrieval is materially faster or safer;
- the dimension has its own revision cadence or evidence schema;
- several character/specialist artifacts depend on it directly;
- maintaining it inside the master file causes duplicated reconstruction work;
- the dimension needs an independent audit, locator index, or high-water mark.

Likely—but not guaranteed—future splits include character/state, relationships, institutions/agency, knowledge-production/economy, world-model/religion-magic, information state, ordinary life/body, and claim revision.

Do not split for cosmetic symmetry or because another series uses that ledger.

At the V01 boundary, **no split is warranted**. The master ledger remains sufficient to represent the cumulative state without material retrieval loss.

## 11. Part-boundary reconciliation

At V03, V07, V12, V21, and V33:

1. reconcile all entries through the just-frozen part boundary;
2. adjudicate material predictions and claims;
3. identify unresolved contradictions;
4. check whether a responsibility should split or merge;
5. identify character/relationship promotion candidates without enrolling them automatically;
6. identify specialist responsibilities that have become warranted;
7. record any required architecture amendment in `../CURRENT_STATE_AND_CORPUS_MAP.md`.

The first mandatory review occurs after V03 unless an earlier volume exposes a material architecture gap.

## 12. Freeze and mutability behavior

This ledger is mutable current state. Frozen deep readings preserve their historical source boundaries. Updating this ledger may revise the **current** interpretation but must not rewrite the earlier deep-reading record or pretend later knowledge was available prospectively.

If a responsibility later splits into a dedicated canonical ledger, this file should retain a compact routing note and cease duplicating that responsibility's detailed current state.
