---
series: ASCENDANCE_OF_A_BOOKWORM
artifact_type: master_longitudinal_ledger
scope: PRE_SPLIT_CROSS_VOLUME_STATE
generation: V0.5
status: canonical
release_state: mutable_active
source_boundary: "Japanese-language light-novel corpus through V03; V01-V03 frozen from Ascendance of a Bookworm - Volumes 01-03.epub"
committed_high_water_mark: V03
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
  committed_high_water_mark: V03
  numbered_volumes_completed:
    - V01
    - V02
    - V03
  source_derived_claims_present: true
  dedicated_ledgers_split_from_master: []
  part_1_boundary_review: COMPLETE
  part_1_boundary_synthesis: ../05 Specialist Synthesis/BOOKWORM_PART1_BOUNDARY_SYNTHESIS.md
  next_source_unit: V04
  next_source_unit_authorization: separate
  next_part_boundary_review: V07
```

V01-V03 are frozen. The entries below preserve cumulative state promoted from the three numbered deep readings through `../02 Sequential Readings/BOOKWORM_V03_DEEP_READING.md`; they do not import V04 or later knowledge.

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
| V03 / `第一部「兵士の娘」III` | Myne | Survival preference becomes explicitly bounded by family belonging and self-authored life | DIRECT + CORROBORATED INFERENCE | Myne wants to live, but refuses the ordinary noble-contract route when survival would require surrendering family and practical autonomy; she seeks alternatives rather than choosing death as an end | Prior death reduces fear; exact future option set remains open | V03 §§6-7, 27 |
| V03 | Myne | Family becomes capable of constraining the book drive in direct conflict | DIRECT | Myne recognizes the current family as as important as books after confronting the temple-library choice | The book drive remains extremely strong and suppressing it destabilizes mana | V03 §7 |
| V03 | Myne | `身食い` becomes materially explained as uncontrolled mana; `威圧` demonstrates unusually strong/increasing mana | DIRECT + CORROBORATED INFERENCE | Mana amount and emotional control are independent practical risks; magic tools buy time by absorbing mana | Myne's general frailty is not fully explained by `身食い`; long-run management remains open | V03 §§5, 22-25 |
| V03 | Myne | Enters negotiated blue-robed temple service while retaining home residence and workshop ties | DIRECT | Institutional position is an exception won through mana scarcity, commercial resources, family resistance, and negotiation rather than ordinary class equality | Temple hierarchy and Temple Head hostility remain active constraints | V03 §§24-27 |
| V03 | Lutz | Merchant aspiration becomes demonstrably self-authored and proceeds into formal apprenticeship | DIRECT + CORROBORATED INFERENCE | Lutz would pursue the route even without Myne; savings, training, maternal support, and explicit acculturation expand his practical options | Father remains resistant; inherited merchant cultural capital is still missing | V03 §§8-9 |

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
| V03 | Myne ↔ Lutz | Dyad becomes independently retrieval-worthy across identity, care, creation, rights, and future separation | Lutz retains privileged Urano knowledge; both now know the other has deliberately chosen continued joint creation | Magical sales rights and explicit mutual commitments preserve linkage even as temple service may separate daily work | DIRECT + CORROBORATED INFERENCE | V03 §§8-10 |
| V03 | Lutz ↔ family | Conflict shifts from undifferentiated opposition toward partial family alliance | Parents still hold household authority; Lutz now articulates independent motive and material plan | Carla becomes explicit ally and begins protecting his household interests; father opposition remains | DIRECT | V03 §8 |
| V03 | Myne ↔ family | Family becomes an explicit life-defining commitment and active protection network | Family lacks Urano disclosure but knows `身食い`/mana danger; parents possess little formal power against temple nobles | Parents risk severe punishment rather than surrender Myne; negotiated temple terms preserve co-residence | DIRECT + CORROBORATED INFERENCE | V03 §§6-7, 24-27 |
| V03 | Myne ↔ Frieda | Friendship/competition becomes a parallel survival comparison | Frieda has direct experience of noble-contract survival and greater wealth; Myne has different values and refuses equivalent dependency | Frieda spends scarce tool capacity on Myne while also pursuing debt/commercial leverage | DIRECT + CORROBORATED INFERENCE | V03 §§4-6, 12 |
| V03 | Myne ↔ Benno | Protection/extraction/education role becomes infrastructural | Benno controls local commercial procedure and sees risks Myne misses; Myne supplies knowledge and growth potential | Benno funds contracts, hides identities, builds workshop routes, protects against Guild Master capture, and retains commercial interest | DIRECT + CORROBORATED INFERENCE | V03 §§11, 14-18, 31 |
| V03 | Myne ↔ temple officials | New dependent/negotiated institutional relationship begins | Temple possesses legal/status power and mana infrastructure; Myne possesses scarce mana, money, family solidarity, and dangerous uncontrolled pressure | Temple Head attempts coercive seizure; Priest Chief brokers a leverage-based exception | DIRECT + CORROBORATED INFERENCE | V03 §§20-27 |

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
| V03 | Contract-magic jurisdiction | Magical rights can affect nonsigners within a bounded jurisdiction | City wall functions as magic boundary; some contracts affecting outsiders require lord reporting; ordinary duplicate records are retained | Uninformed third parties may still be punished; access to contract tools is merchant-restricted | Enforcement can exceed consent/knowledge; procedural and documentary safeguards become critical | V03 §18 |
| V03 | Guild/association registration | New trade structures require institutional registration and negotiated incumbent scope | Plant Paper Association delayed by Guild Master discretion; parchment conflict mediated through product segmentation | Administrative timing can be used as leverage without changing formal rule text | Innovation requires governance strategy as well as production competence | V03 §§17-18 |
| V03 | Merchant apprenticeship | Merchant cultural capital is normally transmitted through family and firm networks | Lutz must explicitly learn presentation, schedule, etiquette, documents, customer behavior, and tools | Earnings/sponsorship can partly substitute for inherited capital | Cross-class occupational mobility is possible but costly and acculturative | V03 §§8-9, 19 |
| V03 | Temple status hierarchy | Blue clergy are noble-linked; gray clergy/orphanage workers occupy subordinate positions | Wealthy-appearing Myne receives deference; poor parents trigger abrupt class contempt and attempted seizure | Mana shortage lets family negotiate an exceptional blue-robed commuting arrangement | Nominal status is leverage-sensitive and does not imply generalized equality | V03 §§20-27 |
| V03 | Temple mana infrastructure | Blue clergy supply mana to sacred tools used in public/religious functions including spring agriculture-linked ritual | Political purge/recalled noble children reduce blue clergy and available mana | Scarcity increases value of Myne's mana and willingness to grant exceptions | Bodily mana becomes public/institutional resource and bargaining asset | V03 §§22-27 |
| V03 | Noble/commoner `身食い` access | Commoner mana is biologically possible, but safe management is noble-controlled | Frieda survives through purchased/noble-linked tools; Myne gains temple alternative because institution needs mana | Wealth improves contract terms; institutional scarcity opens exceptional route | Survival and practical freedom depend on access to tools, patronage, and leverage | V03 §§5-6, 22-27 |

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
| V03 | Pound cake / ratio abstraction | Myne remembers a recipe family based on equal-weight proportions | Ratio avoids incompatible unit translation; Ilse supplies professional mixing, oven, heat, and testing expertise | Successful product and later recipe-right sale | Abstract relations can improve knowledge portability, but expert local execution remains necessary | V03 §§13, 30 |
| V03 | Plant-paper scaling | Children possess a working prototype process | Adult bodies, larger/redesigned tools, river/water, storage, drying, Mark/artisans, Lutz as process carrier, Benno as capital/market coordinator | Adult workshop successfully produces plant paper | Prototype becomes organization capable of reproducing output without Myne's direct labor | V03 §§15-16 |
| V03 | Product diffusion policy | Myne wants useful knowledge/products to spread | Rights, exclusivity periods, collaborator profit, poor-user price effects, secrecy, and self-protection shape release decisions | Mixed policy rather than indiscriminate diffusion | Innovation governance includes distributional and security consequences | V03 §§12, 14 |
| V03 | Hair ornaments | Winter demand becomes organized production | Multiple households produce for pay; rights can be sold/licensed | 186 winter units and formal rights transaction | Household craft has become repeatable distributed enterprise | V03 §§14, 29 |
| V03 | Culinary/marketing capability | Myne introduces recipes and tasting concepts | Ilse reconstructs professionally; Benno/Mark identify missing chef/supply/marketing capacity | New products and controlled tasting event succeed | Imported ideas induce adjacent organizational capability-building | V03 §§30-31 |

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
| V03 | `身食い` / mana | Internal `身食い` heat is mana running wild; magical tools absorb/transfer it temporarily | Frieda, Priest Chief, direct observed tool/`威圧` behavior | CORROBORATED INFERENCE / operationally strong | Multiple informed sources and observed effects align | Mechanism substantially clarified; full biology and long-run prognosis remain open | V03 §§5, 22-25 |
| V03 | Noble/commoner mana | Commoners can possess mana; nobles monopolize ordinary safe management through tools/training/status | Frieda/temple explanations + Myne case | CORROBORATED INFERENCE | Resolves V02 testimony tension without requiring biological exclusivity | Noble-only magic is best modeled as social/institutional monopoly, not universal biological fact | V03 §§5, 22-23 |
| V03 | Temple mana economy | Blue clergy fill magical sacred tools; mana shortage follows political noble depletion/reassignment; spring ritual is tied to agriculture | Priest Chief/temple practice | DIRECT as explanation/practice; metaphysical crop mechanism not fully independently measured | Institutional behavior and resource scarcity corroborate practical importance | Mana is public/religious infrastructure as well as bodily capacity | V03 §22 |
| V03 | Religious doctrine | Darkness/Light deities and seasonal divine family structure baptism and public prayer | Temple ritual/doctrine | DIRECT for doctrine/practice | No independent metaphysical adjudication | Treat as socially/institutionally real doctrine, not proven cosmological history | V03 §21 |
| V03 | `威圧` | Emotionally overflowing mana can be directed as incapacitating pressure; strength tracks mana quantity | Priest Chief + observed confrontation | DIRECT + CORROBORATED INFERENCE | Myne nearly incapacitates/kills Temple Head; control stops through consequence reframing | Dangerous operational mana effect established | V03 §25 |
| V03 | Elite magical communication | White magic bird carries urgent noble correspondence | Gustav viewpoint | DIRECT as observed practice | Fits wider institutional use of magic | Magic supports elite administrative communication | V03 §33 |

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
| V03 | Lutz | Retains privileged Urano identity knowledge while family receives only `身食い`/mana explanation | Strong relational knowledge; no metaphysical proof | No equivalent family identity disclosure occurs | Myne/Lutz remains epistemically unique | V03 §§6, 8-10 |
| V03 | Tuuli | Sees merchant-facing Myne's bargaining competence for the first time | Sister/household baseline is strong but commercial exposure limited | Household model expands without Urano disclosure | Confirms recipient/context gap between home and merchant behavior | V03 §29 |
| V03 | Myne | Gains deeper mana, temple, contract-jurisdiction, and class information while still missing many local risk assumptions | Rapid learner; prior-world analogies remain incomplete | Knowledge shifts from private concepts toward institutional procedure | Better reasoning increases leverage but does not remove child/status vulnerability | V03 §§18, 20-27 |
| V03 | Priest Chief | Understands temple mana scarcity, hierarchy, and `威圧`; initially misreads commoner parental attachment | Institutionally positioned but shaped by temple experience | Updates after family resistance and mana crisis | Becomes adaptive negotiator rather than omniscient authority | V03 §§22, 25-27 |
| V03 | Gustav | Frames guild intervention as system maintenance and receives temple investigation request | Powerful commercial official with self-interested civic model | Reader gains rationale unavailable to Benno | Rival governance models become legible without resolving normative dispute | V03 §32 |
| V03 | Ilse | Recognizes Myne's knowledge anomaly from a professional domain | Skilled culinary focalizer but lacks prior-life information | Myne uses “dream” as protective explanation | Strategic disclosure must not be mistaken for metaphysical evidence | V03 §30 |

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
| V03 | Myne/Frieda | Frieda is physically robust when mana is controlled, while Myne remains chronically frail | Prevents reducing Myne's entire bodily condition to `身食い` | Important differential through V03 | V03 §§5, 34 |
| V03 | Lutz | Lockable storage, food competition, clothing, hygiene, and merchant tools are material to occupational independence | Household/resource details explain why paid work and merchant entry matter personally | Developmental state as he enters apprenticeship | V03 §§8-9, 34 |
| V03 | Myne household | Baptism clothing is made through collaborative reuse and craft rather than wealth | Appearance changes institutional class inference despite low household resources | Scene-specific but analytically important | V03 §§20, 34 |
| V03 | Paper workshop | Water, drying, storage, weather, adult body size, and equipment scale govern production viability | Material conditions determine whether prototype can become organization | Structural production condition | V03 §§15-16, 34 |
| V03 | Tuuli | Hygiene/presentation improves customer-facing opportunity and she begins deliberate visual/trend observation | Ordinary grooming and observation become craft/occupational capital | Emerging apprentice-development state | V03 §29 |

Possible evidence includes food, clothing, comfort, hobbies, work rhythm, study, gifts, shopping, etiquette, humor, rest, annoyance, avoidance, sensory preference, domestic routine, and treatment of low-status or low-stakes interactions.

This section is not a trivia inventory.

## 8. Major claims, counterevidence, and revision state

**Responsibility:** preserve only claims important enough that later evidence could materially strengthen, revise, downgrade, reject, or leave open.

| Claim ID | First source boundary | Earlier formulation | Revision state | Current formulation | Supporting evidence | Counterevidence / rival reading | Current authority |
|---|---|---|---|---|---|---|---|
| V01-C01 | V01 | Imported information enters as a hypothesis whose practical value depends on local translation; tacit/hidden variables can defeat superficially improved replication | STRENGTHEN | Imported knowledge remains conditional agency; portable abstraction can reduce one translation problem, but tacit expertise, bodily execution, local tools, organization, and institutions remain decisive through scale-up | Ratio-based cake + Ilse; adult paper workshop redesign; association conflict; capability-building | Some low-dependency techniques still transfer rapidly | V03 current state; earlier formulations preserved in V01/V02 freezes |
| V01-C02 | V01 | Books remain central, while relationships, usefulness, work, family belonging, and enjoyment provide explicit positive reasons to live | REVISE / STRENGTHEN | Myne positively wants to live, but survival is bounded by family belonging and self-authorship; family has become co-central enough to constrain the book drive in direct conflict | Noble-contract refusal; family disclosure; library conflict; negotiated temple entry | Book desire remains extremely powerful; prior death reduces fear | V03 current state |
| V01-C03 | V01 | Commercial and institutional actors increasingly price Myne's literacy, planning, product knowledge, and negotiation as scarce capital | STRENGTHEN / REFINE | Myne's cognitive/commercial competence creates real leverage, while local institutional risk blindness and bodily limits remain material | Workshop, contracts, product rights, temple negotiation, Benno corrections | She repeatedly misses class signals, contract consequences, and noble/temple danger | V03 current state |
| V01-C04 | V01 | Partnership spans production, education, identity recognition, privileged disclosure, care, and survival motivation | STRENGTHEN | Myne/Lutz is an independently retrieval-worthy chosen dyad spanning identity, care, creation, career, magical sales rights, and mutual future commitments | V03 self-authored career + contract + creation promise | Romance remains unproven; daily institutional paths begin diverging | V03 current state |
| V01-C05 | V01 | `身食い` is the strongly corroborated local diagnosis matching Myne's moving heat and accelerating crisis; exact mechanism remains incomplete | REVISE / STRENGTHEN | `身食い` is uncontrolled mana; magical tools temporarily absorb it; Myne has unusually strong/increasing mana and can manifest `威圧`; chronic frailty remains partly separate | Frieda tool use/comparison; Priest Chief explanation; confrontation | Long-run prognosis/management and full bodily etiology remain OPEN | V03 current state |
| V01-C06 | V01 | Literacy, contract comprehension, record reconstruction, and institutional procedure remain power even when magic enforces agreements | STRENGTHEN | Literacy, human-readable records, jurisdiction knowledge, and procedure are protective infrastructure because magical enforcement can exceed signer knowledge and has bounded reach | Nonsigner contract risk; city boundary; ordinary duplicate parchment; guild reporting | Exact full legal code remains unread | V03 current state |
| V01-C07 | V01 | Anomalous knowledge/products create increasing scrutiny, capture attempts, and strategic concealment | STRENGTHEN | Myne is now actively concealed, investigated, bargained over, and institutionally targeted because of both knowledge and mana | Benno secrecy; Guild Master/Othmar; temple financial investigation; attempted seizure | Family still lacks the full prior-life model | V03 current state |
| V01-C08 | V01 | Ontology remains unresolved; simple instantaneous replacement is weakened by family memory and Lutz's recognition | PRESERVE / OPEN | Urano/Myne metaphysical mechanism remains unresolved; Part 1 strengthens social continuity without independent metaphysical adjudication | Lutz acceptance; family attachment; continued Myne memory access | No source mechanism resolving replacement/merger/continuity | V03 current state |
| V02-C09 | V02 | Magic is embedded in contracts, guild identity/authorization/finance, and survival infrastructure | STRENGTHEN | Magic also supports temple/civic tools, agriculture-linked ritual, elite communication, and class administration | Sacred tools, `威圧`, white magic bird, temple mana economy | Exact system mechanics remain partial | V03 current state |
| V02-C10 | V02 | `身食い` survival is class-mediated by money and noble-linked access to scarce magical tools | STRENGTHEN | Wealth can improve dependent-contract terms but does not erase noble infrastructure monopoly; temple mana scarcity creates an exceptional alternative route for Myne | Frieda arrangement; temple negotiation | Generalizability beyond observed cases remains limited | V03 current state |
| V02-C11 | V02 | Product diffusion creates exposure, bargaining, imitation, and institutional-control pressure | STRENGTHEN | Innovation now triggers association/incumbent conflict, market segmentation, rights sales, controlled marketing, capture attempts, and adjacent capability-building | Plant Paper Association; parchment settlement; tasting event; Benno expansion | Long-run welfare/distribution effects remain OPEN | V03 current state |
| V02-C12 | V02 | Scalable production increasingly depends on household/craft networks rather than Myne's personal labor | STRENGTHEN | Sustainable production now spans households, professional artisans, adult workshop labor, process carriers, merchant capital, and institutional permission | 186 ornaments; adult paper workshop; Mark/artisans; Ilse | Scale beyond city remains prospective | V03 current state |
| V02-C13 | V02 | Lutz's occupational agency is constrained by kin expectations and educational capital while paid coordination/training expand options | STRENGTHEN | Lutz's merchant path is demonstrably self-authored; maternal alliance, savings, sponsorship, and explicit cross-class acculturation provide runway | Family resolution; formal apprenticeship; first-day viewpoint | Father opposition and cultural-capital deficits remain | V03 current state |
| V02-C14 | V02 | Ordinary noble-only `魔力` doctrine conflicts with commoner `身食い`; precise model required | REVISE / RESOLVE | Commoners can possess mana; nobles monopolize most ordinary tools, training, and institutional pathways that make mana survivable and useful | Frieda + Priest Chief + Myne mana evidence | Later sources may refine biological/institutional distribution | V03 current state |
| V03-C15 | V03 | — | OPEN | Practical autonomy is leverage- and jurisdiction-sensitive: nominal status or permission alone does not establish freedom | Temple negotiation; contract jurisdiction; Guild Master discretion | Future institutional contexts may vary | V03 current state |
| V03-C16 | V03 | — | OPEN | Myne has undergone genuine value development: family belonging is no longer instrumental to book-seeking and can constrain it in direct conflict | Library decision; noble-contract refusal; family negotiation | Books remain co-central rather than displaced | V03 current state |
| V03-C17 | V03 | — | OPEN | Privacy, concealment, readable records, contract design, and jurisdiction knowledge now function as deliberate protective infrastructure around valuable people and knowledge | Benno concealment; ordinary contract copy; magic sales-right contract; temple investigation | Protection remains incomplete against higher-status actors | V03 current state |
| V03-C18 | V03 | — | OPEN | Households, guilds, associations, lordly authority, firms, and temple structures form layered institutions whose conflicts often emerge through incentives and discretion rather than simple rule violation | Parchment conflict; Gustav/Benno models; temple hierarchy | Full territorial legal architecture remains incomplete | V03 current state |
| V03-C19 | V03 | — | OPEN | Mana is simultaneously embodied risk and scarce public/institutional resource, tying Myne's health to temple and agriculture-linked infrastructure | `身食い`, sacred tools, mana shortage, negotiated service | Exact agricultural mechanism remains doctrine/practice rather than fully measured causal proof | V03 current state |
| V03-C20 | V03 | — | OPEN | Lutz's cross-class development requires active acculturation and material runway; “following Myne” is no longer an adequate occupational explanation | Self-authorship, savings, maternal support, apprenticeship viewpoint | Myne relationship remains a major enabling factor | V03 current state |

A claim's historical formulation remains discoverable even after the current model changes.

## 9. Prospective prediction and open-question register

### V01 → V02 adjudication

The V01 predictions were frozen before V02 and remain preserved in `BOOKWORM_V01_DEEP_READING.md` and the V02 ledger generation. V02 confirmed or strengthened most of that model; no historical wording is rewritten here.

### V02 → V03 adjudication

| Entering boundary | Question / prediction | Confidence | Basis at entering boundary | Tested by | Outcome | Historical note |
|---|---|---:|---|---|---|---|
| V02 | V02-P01 — Guild Master/Frieda household will attempt to use remaining magical-tool capacity on Myne's present crisis | high | Benno emergency plan and prior negotiation | V03 | CONFIRMED / STRENGTHENED | Frieda spends her own dwindling reserve use |
| V02 | V02-P02 — Available intervention will be temporary rather than a definitive cure | high | Frieda history; depleted tool; reported limited extension | V03 | CONFIRMED / STRENGTHENED | Tool absorbs mana and buys time; no cure |
| V02 | V02-P03 — Earnings/product knowledge will increasingly function as survival capital, not only book-production capital | high | Benno survival-capital framing | V03 | CONFIRMED / STRENGTHENED | Money, rights, products, workshop income and contracts shape options |
| V02 | V02-P04 — Frieda will become a significant `身食い`/wealth/noble-access comparison and information node | medium-high | shared condition and Guild Master resources | V03 | CONFIRMED / STRENGTHENED | Frieda's own negotiated noble future supplies comparison |
| V02 | V02-P05 — Lutz's merchant route will require concrete family resolution before ordinary apprenticeship/baptism progression | high | unresolved parental opposition | V03 | CONFIRMED / STRENGTHENED | Carla recognizes self-authored goal and becomes ally; apprenticeship begins |
| V02 | V02-P06 — Lutz will retain privileged knowledge of Urano identity; equivalent immediate family disclosure is not expected | medium-high | V02 confrontation and family normalization | V03 | CONFIRMED / PRESERVE | Family learns `身食い`, not Urano |
| V02 | V02-P07 — Spring paper scaling will require more formal labor/tooling/market organization and strategic disclosure control | high | winter limits, financing, guild rivalry | V03 | CONFIRMED / STRENGTHENED | Adult workshop, redesigned tools, association negotiation, concealment |
| V02 | V02-P08 — Hair ornaments will move toward a broader market with imitation/competition pressure | high | pre-launch demand and rush production | V03 | CONFIRMED / STRENGTHENED | 186 winter pieces; rights/diffusion formalized |
| V02 | V02-P09 — Noble-only magic doctrine versus commoner `身食い` will require a more precise model | medium | V02 contradictory testimony | V03 | REVISE / RESOLVE | Mana possession not noble-exclusive; management infrastructure is noble-dominated |
| V02 | V02-P10 — Merchant survival will depend increasingly on contract, etiquette, legal, and institutional literacy rather than invention alone | high | contract magic and guild registration | V03 | CONFIRMED / STRENGTHENED | Jurisdiction, associations, records, etiquette, apprenticeship culture |
| V02 | V02-P11 — Stronger desire to live will reduce voluntary surrender risk, but worsening symptoms can still overwhelm agency | medium-high | explicit attachment plus final collapse | V03 | CONFIRMED / REVISED | Myne seeks life but under autonomy/family constraints; emotional conflict itself destabilizes mana |
| V02 | V02-P12 — V03 closes Part 1 and requires the first mandatory architecture/promotion review after its freeze | certain process state | governing architecture | V03 | CONFIRMED | Review completed; Part 1 synthesis instantiated |

### V03 → V04 frozen prospective state

These entries are frozen **before V04 is opened**.

| Entering boundary | Question / prediction | Confidence | Basis at entering boundary | Tested by | Outcome | Historical note |
|---|---|---:|---|---|---|---|
| V03 | V03-P01 — Myne will begin temple service under negotiated blue-robed/commuting conditions, but actual treatment will not equal ordinary noble equality | high | leverage-based exception and class hostility | V04 or later | OPEN | Frozen at V03 |
| V03 | V03-P02 — Priest Chief will become a major regulator/teacher/gatekeeper | high | operational authority, mana knowledge, successful restraint/negotiation | V04 or later | OPEN | Frozen at V03 |
| V03 | V03-P03 — Temple Head hostility will remain a concrete danger despite settlement | high | attempted seizure and near-lethal confrontation | V04 or later | OPEN | Frozen at V03 |
| V03 | V03-P04 — Attendants/gray clergy/orphanage structures will force Myne to confront temple hierarchy and labor relations | high | blue-robed attendant expectation + gray/orphan structure | V04 or later | OPEN | Frozen at V03 |
| V03 | V03-P05 — Myne's mana contribution will link survival access to temple/public agricultural obligations | high | mana shortage, sacred tools, spring ritual | V04 or later | OPEN | Frozen at V03 |
| V03 | V03-P06 — Workshop/business continuity will require active coordination around temple schedules and institutional boundaries | high | negotiated workshop exception + new role | V04 or later | OPEN | Frozen at V03 |
| V03 | V03-P07 — Myne/Lutz continuity will persist through workshop/contract linkage even if ordinary daily work diverges | medium-high | magical sales-right contract + mutual creation commitment | V04 or later | OPEN | Frozen at V03 |
| V03 | V03-P08 — Temple literacy/library access will expose new doctrine/institutional knowledge requiring continued belief-vs-world separation | high | library motive + baptism/temple doctrine | V04 or later | OPEN | Frozen at V03 |
| V03 | V03-P09 — Strong/increasing mana and imperfect emotional control will remain a risk while ordinary frailty remains analytically separate | high | Frieda comparison + `威圧` | V04 or later | OPEN | Frozen at V03 |
| V03 | V03-P10 — Temple/noble investigation of Myne's origin, wealth, products, and network will increase | high | Gustav receives temple financial/workshop inquiry | V04 or later | OPEN | Frozen at V03 |
| V03 | V03-P11 — Paper/ornament/food innovations will continue diffusing through institutions without requiring Myne's direct manual production | medium-high | adult workshop, rights sales, professional reconstruction | V04 or later | OPEN | Frozen at V03 |
| V03 | V03-P12 — Lutz merchant acculturation will continue independently, with etiquette/document/customer gaps narrowing through practice | high | first apprentice day and explicit training structure | V04 or later | OPEN | Frozen at V03 |

## 10. Dedicated-ledger split rule

Split a responsibility out of this file when at least one of the following becomes true:

- entries are numerous enough that independent retrieval is materially faster or safer;
- the dimension has its own revision cadence or evidence schema;
- several character/specialist artifacts depend on it directly;
- maintaining it inside the master file causes duplicated reconstruction work;
- the dimension needs an independent audit, locator index, or high-water mark.

Likely—but not guaranteed—future splits include character/state, relationships, institutions/agency, knowledge-production/economy, world-model/religion-magic, information state, ordinary life/body, and claim revision.

Do not split for cosmetic symmetry or because another series uses that ledger.

At the V03 Part 1 boundary, **no master-ledger split is yet required**. The checkpoint instead records evidence-earned future responsibilities for Myne, Lutz, Myne/Lutz, mana/`身食い`/class access, and knowledge/production/commerce. Reassess ledger density at V07 or earlier if Part 2 creates independent revision cadence or material retrieval loss.

## 11. Part-boundary reconciliation

At V03, V07, V12, V21, and V33:

1. reconcile all entries through the just-frozen part boundary;
2. adjudicate material predictions and claims;
3. identify unresolved contradictions;
4. check whether a responsibility should split or merge;
5. identify character/relationship promotion candidates without enrolling them automatically;
6. identify specialist responsibilities that have become warranted;
7. record any required architecture amendment in `../CURRENT_STATE_AND_CORPUS_MAP.md`.

### V03 / Part 1 review — COMPLETE

Results:

- `../05 Specialist Synthesis/BOOKWORM_PART1_BOUNDARY_SYNTHESIS.md` instantiated as the integrated V01-V03 checkpoint;
- Myne character monograph — **WARRANTED_NOT_INSTANTIATED**;
- Lutz character monograph — **WARRANTED_NOT_INSTANTIATED**;
- Myne/Lutz relationship synthesis — **WARRANTED_NOT_INSTANTIATED**;
- mana / `身食い` / class access / temple-noble infrastructure specialist — **WARRANTED_NOT_INSTANTIATED**;
- knowledge transfer / production / commerce / institutional diffusion specialist — **WARRANTED_NOT_INSTANTIATED**;
- Benno and Frieda character monographs — **MONITOR**;
- master-ledger split — **DEFER**;
- evidence/index promotion — **DEFER**;
- next mandatory review — **V07 after Part 2**.

No global character registry enrollment is performed by this analytical authoring session.

## 12. Freeze and mutability behavior

This ledger is mutable current state. Frozen deep readings preserve their historical source boundaries. Updating this ledger may revise the **current** interpretation but must not rewrite the earlier deep-reading record or pretend later knowledge was available prospectively.

If a responsibility later splits into a dedicated canonical ledger, this file should retain a compact routing note and cease duplicating that responsibility's detailed current state.
