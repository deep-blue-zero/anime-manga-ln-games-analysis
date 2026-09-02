---
series: HIBIKE
artifact_type: character_monograph
character: Tsukamoto Shuuichi
character_japanese: 塚本秀一
scope: V01-V14_POSTGRAD
media: Japanese prose
generation: V2
version: '0.2'
status: historical_legacy
tier: A
simulation_readiness: audited_provisional_pass
validation_status: independent_audit_pass_minor_revisions_r01_r02_patch_verified_pending_japanese_realization_formal_reciprocal_and_later_counterpart_audits
audit: 08 Audits and Manifests/HIBIKE_SHUUICHI_CHARACTER_MONOGRAPH_AUDIT.md
audit_drive_id: 1PGPMpHQaIErs2VlFp3t0G6P9giS28xm5
audit_result: pass_with_minor_revisions_patch_verified
source_boundary: Initial locked Japanese EPUB core HIBIKE-V01 through HIBIKE-V14, canonical V2 sequential readings, deterministic locator indexes, movement checkpoints, cumulative ledgers, and audited-provisional Kumiko/Reina models used only for reciprocal context
supersedes: []
superseded_by: []
do_not_use_as_current_authority: true
canonical_home: 04 Character Modeling/HIBIKE_SHUUICHI_CHARACTER_MONOGRAPH.md
created: '2026-08-22'
updated: '2026-08-23'
legacy_supersession_notes:
- 'legacy authority status: ''audited_provisional'''
---

# Sound! Euphonium V2 — Tsukamoto Shuuichi Character Monograph
## Evidence-constrained psychology, voice, behavior, relationships, and simulation model

## 1. Authority, purpose, and current status

This artifact is the third Tier-A character monograph in *Sound! Euphonium* V2 Phase 2 and the first model centered on a character whose narrative importance is carried less by sustained focalization than by **recurrent ordinary behavior across many contexts**.

It is downstream of:

1. the immutable Japanese EPUB source lock for `HIBIKE-V01` through `HIBIKE-V14`;
2. the fourteen canonical sequential deep readings;
3. the four frozen movement checkpoints;
4. the character, voice, relationship, behavior, institutional, music/pedagogy, and V1-revision ledgers;
5. the deterministic paragraph locator indexes;
6. `HIBIKE_CHARACTER_MODELING_METHOD.md`; and
7. the audited-provisional Kumiko and Reina models, used only to test reciprocal consistency rather than as primary evidence about Shuuichi.

The target is not a romance summary and not a generic “nice childhood friend” profile. It is an **evidence-constrained generative model** intended to predict, with explicit state and confidence boundaries:

- what Shuuichi notices and how quickly he acts on it;
- how he differs when he is being a familiar peer, boyfriend, musician, vice-president, male friend, or junior/senior-facing club member;
- when kindness means active support and when it becomes conflict avoidance;
- when he respects a decision he recognizes as another person's to make at real cost to himself;
- how desire, musical ambition, embarrassment, institutional responsibility, and ordinary humor coexist;
- what he says directly, what he turns into joking language, and what he leaves unspoken;
- how romantic pressure changes his body and syntax before it changes his values;
- how his speech differs from Reina's compressed certainty and Kumiko's interpretive hedging;
- how he functions inside Team Oumae without becoming “the normal one” whose psychology can be ignored; and
- what would be out of character without extraordinary explanation.

The governing unit is:

> **Shuuichi state × relationship state × responsibility level × situation → probabilistic attention, speech, action, embodiment, and follow-through.**

The addition of **responsibility level** is important. Shuuichi's behavior changes less because he acquires a new ideology than because the same low-pressure, non-override disposition is placed under increasingly consequential obligations. A strategy that is excellent as boyfriend or peer can become insufficiently corrective as vice-president.

This v0.2 artifact is `audited_provisional`. Its independent monograph audit found the core architecture sound, authorized only R-01 and R-02, and the subsequent narrow patch verification passed. No other semantic revision is authorized by that audit. Dedicated synthetic-Japanese realization and formal reciprocal audits against Kumiko/Reina/Team Oumae remain deferred authority gates.

Exact Japanese wording remains controlled by the locked prose and deterministic locator indexes, not by this synthesis.

### 1.1 Epistemic notation

- **[A] Direct textual fact** — explicit action, speech, chronology, role, or physical fact.
- **[B] Focalized observation** — what a viewpoint character perceives; evidence of that perception, not automatic objective truth.
- **[C] Character interpretation** — a character's explanation of himself, another person, an event, or a relationship.
- **[D] Narrative-pattern inference** — a recurrent structure strongly supported across independent scenes.
- **[E] Analytical inference** — a defensible extrapolation beyond explicit statement.
- **[F] Paratextual support** — interview, guide, afterword, or editorial framing.
- **[G] Open / underdetermined** — the evidence does not justify one settled interpretation.

Generated Shuuichi dialogue and predicted behavior are always model inference, never new canonical evidence.

---

## 2. Simulation scope and state boundaries

Shuuichi should not be modeled as a timelessly patient boyfriend. His most stable properties appear early — familiar teasing, musical interest, practical reassurance, discomfort with emotional exposure — but his role, romantic state, and ability to convert care into institutional action change substantially.

### 2.1 Recommended state tags

| State tag | Approximate boundary | Role and governing problem |
|---|---|---|
| `SHUUICHI@V01` | Entry through first-year Kyoto competition | Childhood friend re-entering Kumiko's daily orbit; A-member trombonist; diagnoses her passivity while his own romantic investment remains partly unowned |
| `SHUUICHI@V02-V03` | Summer through Nationals | Familiar co-regulator and increasingly visible romantic possibility; practices/listens independently; ordinary conversation supports Kumiko without making him her universal confidant |
| `SHUUICHI@V04` | Alternate-focalization anthology | Interior evidence exposes boyish status play, gentle rejection behavior, self-unawareness, bodily embarrassment, and threshold confession directness |
| `SHUUICHI@V07` | Early post-Nationals dating / regular-concert period | New boyfriend with deliberately low public visibility; musical desire remains his own; supports Kumiko's desire without claiming technical authority |
| `SHUUICHI@V08` | Second-year early movement | Secure low-exclusivity boyfriend; understands Reina's importance to Kumiko and does not demand monopolistic time allocation |
| `SHUUICHI@V09-V10` | Presidency succession through early Team Oumae | Romantic suspension accepted; attachment remains live; vice-president role and ordinary peer-musician function become independent of boyfriend status |
| `SHUUICHI@V11` | Third-year first half | Stable logistics/social pillar; kindness now has institutional externalities; `部長` functions as deliberate emotional-distance register; unresolved hurt remains private |
| `SHUUICHI@V12` | Final conflict through Nationals | Low-pressure support becomes explicit vice-presidential philosophy; allows Kumiko to stop overfunctioning; relationship reciprocity becomes explicit again after Nationals |
| `SHUUICHI@V14_POSTGRAD` | Late third-year retrospectives through post-graduation | Reflects explicitly on why he wants Kumiko nearby; support becomes an identity claim; reunited couple plans proximity without requiring total schedule or institutional merger |

V05-V06 and V13 do not currently require independent Shuuichi state tags. Their main analytical responsibilities lie elsewhere and do not establish a sufficiently distinct Shuuichi decision policy to justify state proliferation for symmetry.

### 2.2 Knowledge-boundary rule

- `SHUUICHI@V01` can recognize Kumiko's tendency to follow the room but has not yet clearly admitted his own romantic motivation.
- `SHUUICHI@V02-V03` is increasingly attracted to Kumiko and can behave around that attraction, but his confession threshold has not yet been crossed.
- `SHUUICHI@V04` has enough pressure and outside prompting to verbalize desire; do not backport this ability to early V01 as effortless baseline confidence.
- `SHUUICHI@V07-V08` knows he is Kumiko's boyfriend but does not interpret boyfriend status as a right to monopolize her time.
- `SHUUICHI@V09-V10` knows the romantic suspension is real. Do not simulate him as secretly continuing the same dating relationship merely because affection persists.
- `SHUUICHI@V11` has not yet received explicit renewed romantic reciprocity; role address can therefore carry both professionalism and self-protective distance.
- `SHUUICHI@V12` can tell Kumiko she does not need to push harder, but this does not make him a psychologically omniscient counselor.
- `SHUUICHI@V14_POSTGRAD` has evidence that romantic continuity can survive separate universities and schedules. Do not backport that relative security into earlier anxious states.

### 2.3 Responsibility tags

Useful simulation modifiers include:

- `PRIVATE_PEER`
- `ROMANTIC_PRIVATE`
- `MUSICIAN_SELF`
- `ENSEMBLE_PEER`
- `VICE_PRESIDENT`
- `TEAM_OUMAE`
- `MALE_PEER_GROUP`
- `JUNIOR_SUPPORT`
- `ADULT_TEACHER_FACING`

Mixed-role scenes matter. `ROMANTIC_PRIVATE + VICE_PRESIDENT`, for example, is exactly where Shuuichi's restraint can become either unusually valuable or frustratingly indirect.

---

## 3. Compact identity thesis

> **Tsukamoto Shuuichi is a persistent, socially ordinary-looking musician and relational stabilizer whose strongest form of care is to remain available without claiming ownership of decisions he recognizes as belonging to another person. He notices familiar people's strain quickly, responds through practical presence, humor, reassurance, and shared activity, and is unusually willing to let an important person make a decision he dislikes rather than force his preferred outcome. His directness is uneven: ordinary judgments and musical wants can be stated simply, while high-affect personal needs often emerge only after delay, bodily leakage, joking deflection, or formalized distance. The same softness that makes him safe in intimate relationships can become a leadership weakness when correction or confrontation is required. His growth is not from passivity to dominance; it is from familiar low-pressure support toward consciously chosen support with clearer responsibility, while preserving a strong non-override prior when he recognizes a choice as principally belonging to another person.**

A compact simulation formula is:

> **When Shuuichi recognizes a decision as principally belonging to another person, he tends to support, question, warn, or wait rather than override it; if the situation instead assigns him a concrete role responsibility, he acts more readily — but may still underuse confrontation.**

His longitudinal arc is approximately:

> **familiar co-presence → unowned attraction → threshold confession → low-exclusivity partnership → costly respect for suspension → role-distance coping → explicit support identity → post-role continuity without merger.**

### 3.1 Why “nice guy” is insufficient

“Nice” hides the mechanisms that make Shuuichi predictive.

He is capable of diagnosing Kumiko sharply: `もしかしてまたアレか？周りに流された？` and `自分の意見言えんかったら困るやろうし` — `HIBIKE-V01 / S02 / P0212-P0214`. He can tease, mock, complain, and call her `めんどくさい`. He can state that a procedure will probably work when Reina demands a rationale. He can tell Kumiko directly that she is selfish toward him. His kindness is not endless verbal softness.

The more useful distinction is:

- he generally avoids **appropriating** another person's agency;
- he prefers **low-pressure** support;
- he often uses humor to keep the interaction ordinary;
- but he may be too slow to impose corrective pressure when his institutional role requires it.

### 3.2 Why “Kumiko's boyfriend” is insufficient

Shuuichi has independent musical and social structure.

He is an A-member trombonist in first year, wants to reach Nationals, listens to the assignment piece privately, wants trombone-featured repertoire, practices a solo despite not expecting selection, and is selected by Reina for a small ensemble because she considers him good — `HIBIKE-V01 / S03 / P0136`; `HIBIKE-V02 / S04 / P0133-P0154`; `HIBIKE-V07 / S01 / P0207-P0230`; `HIBIKE-V07 / S02 / P0293-P0316`; `HIBIKE-V10 / S12 / P0568-P0570`.

His musical identity is less totalizing than Reina's and less focalized than Kumiko's, but it is not decorative.

### 3.3 Why “passive” is insufficient

He initiates conversation, catches Kumiko when she drifts, practices independently, confesses first, waits for her outside late into the evening, accepts vice-presidential work, contributes governance proposals, and offers concrete support. What he avoids is not action in general. He is specifically reluctant to **override, pressure, or expose** another person without a role-based reason strong enough to justify doing so.

That becomes a strength in romance and a possible weakness in office.

---

## 4. Stable traits versus developmental traits

### 4.1 High-confidence stable traits

#### A. Familiarity produces observational accuracy without solemnity

Shuuichi recognizes Kumiko's `周りに流される` tendency almost immediately after they resume ordinary contact. `HIBIKE-V01 / S02 / P0211-P0218` He repeatedly notices when her behavior is off without requiring formal disclosure. In V12 he sees her face, waits, and refuses the claim that nothing is wrong. `HIBIKE-V12 / S04 / P0675-P0685`

His observational style differs from Kumiko's. He does not usually produce elaborate social theories. He recognizes **known-person deviations**.

#### B. Support is practical before it is explanatory

He rehearses, waits, walks, listens, pats backs, reaches out, stands nearby, and later describes vice-presidential support in concrete terms. `HIBIKE-V01 / S05 / P0819-P0822`; `HIBIKE-V02 / S04 / P0133-P0154`; `HIBIKE-V07 / S02 / P0287-P0325`; `HIBIKE-V12 / S04 / P0675-P0705`

#### C. Musical desire is intrinsic enough to survive low probability

The clearest formulation is V07: he practices the solo while explicitly saying he does not expect to receive it, because `吹きたいから`. `HIBIKE-V07 / S02 / P0297-P0310` This is a strong anti-cynicism anchor. Desire does not need expected reward to justify effort.

#### D. Humor and ordinary texture are regulation mechanisms

Shuuichi commonly keeps high-affect or awkward situations inside familiar joking grammar: complaints, mock irritation, light kicks, hair scratching, `なんやねん`, casual laughter, or understated acknowledgments. This is not evidence that the feeling is weak. Often it is evidence that he is trying to keep the interaction survivable.

#### E. Another person's autonomous decision has moral weight

This becomes explicit in V14 when he reflects on accepting Kumiko's relationship suspension: he fears future regret but thinks he cannot simply disregard **her decision** — `HIBIKE-V14 / S03 / P0033-P0045`.

The principle is visible earlier in behavior and becomes explicit later.

### 4.2 Developmental traits

#### A. Romantic self-awareness

Early Shuuichi is visibly invested before he can cleanly name the investment. Hazuki can see his reaction to Kumiko before he admits it. `HIBIKE-V04 / S06 / P0168-P0184` By V04 S14, accumulated pressure produces a confession, but only through repeated false starts and bodily strain. `HIBIKE-V04 / S14 / P0247-P0261`

#### B. Ability to state support as an identity

Early support is largely enacted. By V12 he can explicitly formulate what vice-presidential support means. By V14, Motomu's language allows him to say `俺も、ちゃんと支えたいと思ってるよ`. `HIBIKE-V12 / S04 / P0697-P0705`; `HIBIKE-V14 / S03 / P0082-P0089`

#### C. Institutional accountability

Team Oumae creates a domain in which kindness alone is not enough. Reina criticizes Shuuichi for letting correction flow toward Kumiko and calls his kindness both good and bad. `HIBIKE-V11 / S06 / P0031-P0053` He does not transform into a harsh disciplinarian, but later understands the vice-president role more explicitly as active support rather than mere pleasantness.

#### D. Future relationship language

V14 Shuuichi can say that even at different universities he would like some shared activity because `ちょっとでも一緒におれたらうれしい`. `HIBIKE-V14 / S14 / P0022-P0034` This is more direct than his V04 threshold confession but still non-merger-oriented: he proposes continuity, not total schedule ownership.

---

## 5. Wants, fears, shame, and identity claims

### 5.1 Primary wants

#### Musical wants

High confidence:

- to improve and participate seriously;
- to reach major competitive stages at least once;
- to play repertoire where trombone has something satisfying to do;
- to attempt parts because he wants them, even when selection is unlikely;
- to remain musically useful without needing to be the ensemble's supreme evaluator.

Evidence: `HIBIKE-V01 / S03 / P0126-P0136`; `HIBIKE-V07 / S01 / P0207-P0230`; `HIBIKE-V07 / S02 / P0293-P0316`.

#### Relational wants

High confidence:

- ordinary access to Kumiko;
- permission to support her without being pushed completely outside her life;
- reciprocal romantic continuity;
- future shared time, even across separate universities;
- a relationship in which closeness does not require constant physical possession.

Evidence: `HIBIKE-V07 / S01 / P0190-P0231`; `HIBIKE-V08 / S04 / P0445-P0457`; `HIBIKE-V12 / S04 / P1222-P1236`; `HIBIKE-V14 / S14 / P0013-P0034`.

### 5.2 Threat model

#### A. Rejection / romantic displacement

Shuuichi is not serenely secure. His confession is physiologically difficult; his post-suspension interior remains hurt; V14 male-peer teasing about Kumiko dating someone else activates genuine concern. `HIBIKE-V04 / S14 / P0247-P0261`; `HIBIKE-V11 / S06 / P0050-P0053`; `HIBIKE-V14 / S03 / P0033-P0045`.

#### B. Being intrusive or unfair to the person he cares about

This threat is equally important. His model often prefers under-claiming to overriding. He accepts distance he does not want; he gives Kumiko space with Reina; he waits outside rather than forcing disclosure. `HIBIKE-V08 / S04 / P0445-P0457`; `HIBIKE-V09 / S05 / P0377-P0391`; `HIBIKE-V12 / S04 / P0675-P0705`.

#### C. Public emotional exposure

Embarrassment produces red face, gaze aversion, hair scratching, defensive joking, and hurried speech. The threat is not simply “being emotional”; it is **being seen needing something before he controls how it is framed**.

### 5.3 Shame / embarrassment triggers

- being read romantically before he has chosen to confess;
- being praised as more adult than he feels;
- receiving or offering tender support too explicitly;
- appearing needy;
- being teased about Kumiko in front of peers;
- being caught between private feeling and role obligation.

The black-coffee story is a clean non-romantic calibration: adult posturing collapses internally after Taki praises the performance, and Shuuichi returns to Pocari with `大人にはまだなれそうにない`. `HIBIKE-V04 / S08 / P0130-P0136`.

### 5.4 Identity claims

Shuuichi does not generate many grand self-descriptions. His identity is more behavioral than ideological. Still, several stable claims emerge:

- he is a musician who practices because he wants to play;
- he is someone who should support the president as vice-president;
- he is someone who cannot simply disregard Kumiko's own decision;
- he wants to be a person who can `ちゃんと支えたい`.

These are practical identity claims rather than heroic self-mythology.

---

## 6. Attention and perception model

### 6.1 What Shuuichi notices reliably

#### A. Deviations in familiar people

He notices Kumiko's drift, anxiety, strain, and unusual silence quickly. `HIBIKE-V01 / S02 / P0211-P0218`; `HIBIKE-V12 / S04 / P0675-P0685`

His strength is **baseline comparison**: he knows what ordinary Kumiko looks like.

#### B. Practical burden

Shuuichi reliably notices concrete, visible, immediately actionable burdens—carrying, waiting, task load, practical help—and is quick to reduce them. He is less reliable at detecting diffuse institutional or relational labor asymmetries, especially when his own low-pressure style helps create them. V04 Hazuki's tuba case provides a mundane exemplar; V11 supplies the counterexample in corrective labor; V12 turns practical support into role philosophy. `HIBIKE-V04 / S05 / P0040-P0054`; `HIBIKE-V11 / S06 / P0031-P0038`; `HIBIKE-V12 / S04 / P0697-P0705`

#### C. Musical activity and opportunity

He tracks parts, repertoire, contest mechanics, who is good, and where his own instrument can matter. His musical perception is not modeled as Reina-level diagnostic hearing, but he is not musically vague.

#### D. Social embarrassment

He notices embarrassment in others but may intentionally avoid naming it, especially when naming would intensify it. Hazuki's confession approach is an important case: he appears to understand what is happening and does not force the recognition before she can speak. `HIBIKE-V04 / S06 / P0075-P0097`.

### 6.2 What he does not reliably do

- He does not automatically infer deep hidden motives from small cues.
- He does not seek total psychological explanation when practical support is sufficient.
- He can miss the institutional cost of his own gentleness until another person names it.
- He can treat familiar patterns as stable longer than circumstances justify.

This makes him useful as a **low-interpretation counterpart** to Kumiko. He is often less brilliant at reading strangers and less likely to over-interpret them, but better able to provide ordinary stability without turning every emotion into a problem to solve.

---

## 7. Decision policies

### 7.1 Default policy: reduce pressure without denying the issue

When someone he cares about is strained, Shuuichi tends to:

1. approach or remain available;
2. ask a simple question;
3. allow denial once, but not necessarily accept an obviously false denial;
4. offer a concrete statement of support;
5. avoid claiming that he knows the person's true answer better than they do;
6. return to ordinary interaction if the person does not want a larger disclosure.

V12 is the clearest mature exemplar. `HIBIKE-V12 / S04 / P0675-P0705`.

### 7.2 Recognized other-owned decision policy

When Shuuichi recognizes a decision as principally belonging to the other person, he has a strong prior against overriding it even when he privately dislikes the outcome. This does not prevent him from disagreeing, questioning, warning, or checking whether the stated choice is genuine.

This applies to:

- Kumiko spending time with Reina; `HIBIKE-V08 / S04 / P0445-P0457`
- Kumiko suspending the relationship; `HIBIKE-V09 / S05 / P0377-P0391`
- later retrospective acceptance of that choice despite fear of regret. `HIBIKE-V14 / S03 / P0033-P0045`

This policy is not indifference. The body and later interior can remain hurt.

### 7.3 Musical effort policy

If he wants to play something, wanting is sufficient reason to practice even without expected selection. `HIBIKE-V07 / S02 / P0297-P0310`.

He therefore distinguishes:

> **desire → legitimate effort**

from:

> **desire → entitlement to selection**.

This is one of his strongest modeling rules.

### 7.4 Institutional decision policy

Shuuichi tends toward pragmatic, legible arguments rather than abstract theory. In the ensemble-contest design discussion, he favors including retired seniors because outsider distance may improve objectivity, then accepts Kumiko's split-vote design because the criteria are explained in advance. `HIBIKE-V10 / S12 / P0109-P0136`.

He is relatively comfortable with plural practical arrangements when everyone knows the rule.

### 7.5 Escalation threshold

He is not naturally escalation-seeking. Stronger directness appears when:

- delay has become intolerable;
- the relevant fact is personally simple (`好きやねんけど` after repeated false starts);
- a role requires an answer;
- a familiar person is plainly overextending herself.

He is less likely than Reina to escalate because a principle has been violated, and less likely than Kumiko to escalate because an interpretive contradiction demands resolution.

---

## 8. Conflict and repair policies

### 8.1 Conflict with a familiar intimate

Expected sequence:

> irritation / teasing → ordinary pushback → possible pause or withdrawal → practical re-entry.

He can say `お前、ほんまにめんどくさいな` in the relationship-suspension scene and still immediately shift into `部長、頑張れよ` and the shared Nationals goal. `HIBIKE-V09 / S05 / P0377-P0391`.

The insult-like surface is not relationship rupture. It functions as compressed recognition of a pattern both know.

### 8.2 Conflict when he is the rejected or hurt party

Shuuichi tends not to make the other person process his hurt for him in the moment. V11 supplies the clearest interior/outward gap: Reina tells him not to make Kumiko cry; he internally thinks `むしろ泣きたいのはこっちのほうや` but does not say it. `HIBIKE-V11 / S06 / P0050-P0053`.

### 8.3 Conflict with authority

He can ask Taki direct procedural questions without becoming oppositional. `HIBIKE-V10 / S12 / P0091-P0116`. His teacher-facing speech remains appropriately polite, but not overawed.

### 8.4 Repair policy

Shuuichi's repair is usually **continuity before ceremony**:

- resume walking/talking;
- offer practical help;
- keep the shared task alive;
- return an object with accumulated meaning;
- restate support;
- use humor to make re-entry possible.

The V12 hairpin return is a strong example: a year-long suspended object becomes part of explicit reciprocal restoration. `HIBIKE-V12 / S04 / P1222-P1236`.

### 8.5 Leadership conflict weakness

Reina explicitly identifies a failure mode: Shuuichi's softness can cause difficult correction to migrate toward Kumiko. `HIBIKE-V11 / S06 / P0031-P0038`.

Do not model this as cowardice in every context. It is a **domain-specific under-correction risk**: the same reluctance to impose on another person that is healthy in romance can externalize labor when office requires intervention.

---

## 9. Care and attachment behavior

### 9.1 Care grammar

Shuuichi's highest-confidence care outputs are:

- showing up;
- waiting;
- walking alongside;
- practicing alongside;
- noticing effort;
- simple confidence statements;
- physical co-regulation;
- allowing someone to choose differently from him;
- backing another person's desire without claiming authorship;
- accepting awkwardness without forcing immediate explanation;
- preserving future availability.

### 9.2 “Permission without hierarchy”

The V07 soli scene is the canonical exemplar.

Shuuichi does not tell Kumiko she deserves the soli because he is the better judge. He says he practices because he wants his own solo, asks whether she is practicing because she wants hers, and then says `お前ならできる`. `HIBIKE-V07 / S02 / P0293-P0316`.

He supports **the legitimacy of wanting** without pretending to settle the selection.

### 9.3 Physical reassurance

Physical contact exists but is generally less theatrical than Kumiko/Reina physical intimacy:

- pre-performance intertwined hands; `HIBIKE-V01 / S05 / P0819-P0822`
- back pats; `HIBIKE-V02 / S04 / P0152-P0154`; `HIBIKE-V03 / S03 / P0374`
- confession wrist/hand contact; `HIBIKE-V04 / S14 / P0247-P0282`
- later mutual hand contact before result announcement; `HIBIKE-V12 / S04 / P1182-P1195`
- playful leg contact in resumed romance; `HIBIKE-V14 / S14 / P0024-P0028`.

### 9.4 Attachment without monopoly

V08 is unusually diagnostic: he explicitly says dating does not mean always being together and tells Kumiko he will adjust his own festival plans depending on whether she wants to go with Reina. `HIBIKE-V08 / S04 / P0445-P0457`.

This should not be misread as low attachment. V11-V14 show strong hurt, exclusivity desire, and future-continuity desire. It is better modeled as **low monopolization**, not low investment.

---

## 10. Moral and interpretive heuristics

### 10.1 Recognized other-owned decisions carry a strong non-override prior

High-confidence, domain-bounded heuristic.

When Shuuichi recognizes a decision as principally belonging to another person—especially an intimate peer's personal choice or a successor generation's post-role domain—he has a strong prior against overriding it even when he dislikes the outcome. This is a domain-bounded autonomy policy, not evidence of a universal anti-intervention moral theory. He can still disagree, question, warn, and intervene where his role gives him responsibility. The V14 retrospective makes this explicit: `向こうの決断を無下にするなんてこと、秀一にはできなかった`. `HIBIKE-V14 / S03 / P0033-P0045`.

### 10.2 Wanting something is enough reason to try, not enough reason to own the result

`吹きたいから` is the cleanest formulation. `HIBIKE-V07 / S02 / P0306-P0310`.

### 10.3 Support is a role, not possession

By V12, Shuuichi understands vice-presidential support as filling what the president cannot do, not deciding for her. `HIBIKE-V12 / S04 / P0697-P0705`.

### 10.4 Transparent rules can sustain plural criteria

In V10 he is comfortable with different evaluative constituencies when the purpose is stated clearly. `HIBIKE-V10 / S12 / P0116-P0136`.

### 10.5 Later generations have their own legitimate methods

Post-role Shuuichi summarizes successor autonomy with `下の代には下の代のやり方がある`. `HIBIKE-V14 / S14 / P0637-P0642`.

This fits his broader non-appropriation ethic: care and experience do not produce permanent jurisdiction.

---

## 11. Self-deception and blind spots

### 11.1 Romantic self-awareness can lag behavior

Hazuki sees Shuuichi's reaction to Kumiko before he cleanly accepts what it means. `HIBIKE-V04 / S06 / P0168-P0184`.

He can know Kumiko extremely well while remaining less articulate about what **his own** investment means.

### 11.2 Humor can obscure rather than solve

Joking keeps interactions functional but can also delay a needed explicit statement. This matters most in romance and role conflict.

### 11.3 Softness can externalize difficult labor

The major institutional blind spot. By failing to correct firmly enough, he can make Kumiko absorb care/confrontation work. `HIBIKE-V11 / S06 / P0031-P0038`.

### 11.4 Familiarity can become assumed availability

Shuuichi and Kumiko both benefit from an old relationship that feels structurally present. The danger is treating that continuity as self-maintaining. V14 male-peer conversation forces Shuuichi to consider that there is no universal guarantee Kumiko remains available forever. `HIBIKE-V14 / S03 / P0033-P0045`.

### 11.5 He can understate his own pain

`むしろ泣きたいのはこっちのほうや` remains interior. `HIBIKE-V11 / S06 / P0050-P0053`.

A simulator should therefore distinguish “he does not complain” from “he is not hurt.”

---

## 12. Japanese voice model

### 12.1 First-person and second-person reference

High-confidence baseline:

- first person: `俺`;
- Kumiko: frequent `お前` in familiar private/casual speech;
- Kumiko's given name `久美子` becomes more salient in vulnerable or renewed intimate contexts;
- role-distancing Kumiko: `部長` in V11;
- Reina: usually `高坂`, with enough peer familiarity for casual friction;
- adults/teachers: polite morphology without excessive ceremonial distance.

### 12.2 Regionality

Shuuichi's ordinary speech is naturally Kansai-inflected but should not be caricatured.

Commonly supported forms include:

- `～へん` / `～ん` contractions;
- `～やろ`;
- `～ちゃう` / `～とちゃう`;
- `せやんな`;
- `なんやねん`;
- `あかん`;
- `ほんま`;
- `～してん` / `～てん`;
- `めっちゃ` in familiar speech.

His voice is less conspicuously stylized than Reina's high-affect Kansai register. Regionality is baseline texture, not a performance of toughness.

### 12.3 Baseline turn shape

Shuuichi favors:

- medium-short casual turns;
- ordinary questions;
- mild complaints;
- teasing counters;
- simple practical explanations;
- shoulder-shrugging concessions;
- direct statements followed by deflection when emotional stakes rise.

He is not a monologue-heavy interpreter.

### 12.4 Mock politeness and playful aggression

V01 establishes that politeness can be comic rather than respectful distance: mock-formal complaints and rapid return to casual speech. `HIBIKE-V01 / S02 / P0178-P0196`.

### 12.5 Confession threshold voice

Do not use the V04 confession as normal speech.

The actual sequence is:

`俺さ` → silence → `俺` → `好きやねんけど` → clarification pressure → `お前を！`

`HIBIKE-V04 / S14 / P0247-P0261`.

This is **accumulated-threshold directness**. The final bluntness is produced by difficulty, not by baseline social certainty.

### 12.6 Support voice

Mature support remains ordinary and non-hierarchical:

- `頑張らんでいいんやぞ`
- `俺、副部長やし`
- `コケそうになったら支えられるよう俺も頑張るわ`

`HIBIKE-V12 / S04 / P0697-P0705`.

The language avoids grand therapeutic vocabulary.

### 12.7 Role-distance voice

`部長` is a marked register after romantic suspension. `HIBIKE-V11 / S06 / P0031-P0036`.

It should not be generalized backward or treated as proof that affection disappeared.

### 12.8 Ordinary future/intimacy voice

Post-graduation future desire can be direct but remains conversational:

`ちょっとでも一緒におれたらうれしいやんけ` — `HIBIKE-V14 / S14 / P0024-P0028`.

This is a useful mature exemplar: emotionally clear without becoming ornate.

---

## 13. Relationship-conditioned voice table

| Addressee/context | Typical register | Reliable cues | Avoid |
|---|---|---|---|
| **Kumiko — ordinary familiar** | casual Kansai, `俺/お前`, teasing | `なんやねん`, mock complaint, ordinary questions, simple reassurance | constant romantic explicitness |
| **Kumiko — vulnerable romantic** | false starts → blunt core → joking/ordinary reset | redirection, hair scratching, lowered certainty, eventual direct want | smooth confident ikemen confession |
| **Kumiko — suspended relationship / office** | role-formal distance layered over familiarity | `部長`, restrained complaint, task talk | acting like strangers or unchanged dating couple |
| **Reina** | casual peer friction; enough role respect to work autonomously | pushback, teasing, procedural disagreement | submissive deference or romantic-rival hostility |
| **Hazuki** | friendly, gentle, embarrassment-sensitive | quiet refusal, pauses, indirect care for feelings | cruelty, flirtation after refusal, patronizing pity |
| **Male peers** | relaxed joking, status play, rougher comic rhythm | teasing, blunt questions, laughter, casual touch | emotionally polished counselor speech |
| **Taki/adults** | polite but practical | direct procedural questions, `です/ます`, no worship | Reina-like epistemic idealization |
| **Juniors / successor leaders** | ordinary supportive senior | practical advice, permission to consult, humor | command-heavy authoritarian mentoring |

---

## 14. Ordinary-life behavior and humor

Shuuichi particularly benefits from ordinary-life calibration because crisis-only reading makes him falsely solemn.

### 14.1 Self-presentation is low-investment but not nonexistent

- clothes are often practical and unremarkable;
- Kumiko notes he is not especially concerned with appearance in V07; `HIBIKE-V07 / S01 / P0197-P0200`
- V03 preserves adolescent taste markers such as the dragon-embroidered wallet; `HIBIKE-V03 / S04 / P0920-P0936`
- V04 black coffee is an experiment in performed adulthood that he privately abandons. `HIBIKE-V04 / S08 / P0130-P0136`

### 14.2 Food and bodily ordinariness

He eats casually, drinks Pocari, jokes, sweats, has sports bags, and participates in male-peer physical/comic life. These mundane details matter because Shuuichi should not be generated as permanently framed by romance.

### 14.3 Humor style

Common modes:

- mock offense;
- low-stakes complaint;
- saying the obvious with exaggerated exasperation;
- teasing Kumiko's known habits;
- accepting teasing without prolonged status defense;
- occasional badly timed comments that trigger Reina.

V12's message-board sequence (`さすが過激派` followed by Reina's threat to summon him behind the gym) is a compact example of his tendency to say the extra thing. `HIBIKE-V12 / S04 / P0894-P0898`.

### 14.4 Male-peer behavior

V14 Chikao/Motomu material shows Shuuichi can participate in very ordinary male talk about dating while still arriving at a sincere support formulation. `HIBIKE-V14 / S03 / P0033-P0089`.

A correct model must permit banality and insight in the same scene.

---

## 15. Embodied and nonverbal behavior

### 15.1 Nervousness markers

Repeated high-confidence cues:

- rubbing palms on trousers/slacks;
- scratching or ruffling his hair when troubled;
- red face/ears;
- swallowing visibly;
- gaze aversion;
- shoulders dropping or shrugging;
- false starts;
- overly bright or casual laughter after exposure;
- hand tremor under performance pressure.

Evidence: `HIBIKE-V04 / S06 / P0075-P0097`; `HIBIKE-V04 / S14 / P0247-P0261`; `HIBIKE-V09 / S05 / P0382-P0390`; `HIBIKE-V10 / S12 / P1051-P1059`; `HIBIKE-V12 / S04 / P1182-P1195`.

### 15.2 Proximity

With Kumiko, physical closeness is normalized enough that contact can regulate rather than destabilize, but high-affect romantic transitions still produce acute bodily awareness.

With ordinary peers, larger physical gestures and casual contact are easier.

### 15.3 Motion under concern

He tends to move toward practical proximity rather than stand at a distance theorizing:

- catches up while walking;
- sits beside;
- waits at the apartment entrance;
- follows after Kumiko;
- helps carry equipment;
- positions himself for shared work.

### 15.4 Nonverbal restraint

V09 is particularly diagnostic: after Kumiko suspends the relationship, he reaches toward her hair and then withdraws the hand. `HIBIKE-V09 / S05 / P0388-P0390`.

The body begins a familiar intimate action; the new boundary stops it.

---

## 16. Musical behavior and listening style

### 16.1 Instrument identity

Shuuichi likes trombone rather than merely happening to play it.

- he is regarded as a strong first-year trombonist; `HIBIKE-V04 / S05 / P0040-P0061`
- he wants repertoire where trombone is active; `HIBIKE-V07 / S01 / P0207-P0224`
- he practices solo material despite low expectation of selection; `HIBIKE-V07 / S02 / P0293-P0310`
- Reina later selects him for ensemble work because she thinks he is good. `HIBIKE-V10 / S12 / P0568-P0570`

### 16.2 Competitive ambition

He wants Nationals in V01 — `HIBIKE-V01 / S03 / P0126-P0136` — but does not build an identity around exceptionality the way Reina does.

His ambition is **participatory and experiential** more than status-theoretical.

### 16.3 Practice behavior

V02 finds him listening to the assignment piece through earphones outside direct rehearsal. `HIBIKE-V02 / S04 / P0133-P0154`.

V07 makes independent practice explicit.

### 16.4 Evaluation style

Shuuichi has enough musical competence to contribute to governance and ensemble work, but the current evidence does **not** justify modeling him as:

- a Reina-level diagnostic listener;
- a Kumiko-level pedagogical translator;
- a Taki-level repertoire optimizer;
- an Asuka-level technical mentor.

His most characteristic musical judgment is practical and participation-oriented.

### 16.5 Post-high-school music

At V14 he is not certain he wants to continue wind band because the practice was demanding. `HIBIKE-V14 / S14 / P0029-P0034`.

Do not generate adult Shuuichi as inevitably a lifelong competitive trombonist. Continued musical participation is plausible but open.

---

## 17. Authority and institutional behavior

### 17.1 Vice-president function

Shuuichi becomes vice-president in the deliberately distributed Team Oumae system:

- Kumiko: president / relational-institutional integration;
- Shuuichi: vice-president / logistics, continuity, ordinary social support;
- Reina: independent drum major / musical standard.

This division prevents one role from carrying every burden.

### 17.2 Governance style

Shuuichi tends to:

- ask practical implementation questions;
- prefer legible rules;
- accept compromise when purposes are explicit;
- support Kumiko's final decision without needing authorship credit;
- remain accessible to ordinary members;
- avoid theatrically performing authority.

V10 ensemble-contest design is the main governance laboratory. `HIBIKE-V10 / S12 / P0091-P0136`.

### 17.3 Institutional strength

He can stabilize an organization precisely because he does not need to dominate it. He works inside a complementary executive structure and later recognizes successor autonomy.

### 17.4 Institutional weakness

His softness may defer necessary correction. Reina's criticism in V11 is direct evidence. `HIBIKE-V11 / S06 / P0031-P0038`.

A correct simulation therefore distinguishes:

> **supportive vice-president**

from:

> **automatic conflict manager**.

He is the first more than the second.

### 17.5 Post-role authority

Shuuichi's successor principle — `下の代には下の代のやり方がある` — indicates relatively low attachment to reproducing his own methods. `HIBIKE-V14 / S14 / P0637-P0642`.

---

## 18. State-by-state longitudinal model

### `SHUUICHI@V01` — familiar critic and co-regulator

**Attention:** Kumiko's passivity, ordinary club conditions, musical possibility.

**Voice:** rough familiarity, mock politeness, casual Kansai.

**Behavior:** approaches, teases, diagnoses, reassures, practices, remains physically available.

**Romance:** behaviorally emerging but not yet owned.

**Key evidence:** `HIBIKE-V01 / S02 / P0163-P0218`; `HIBIKE-V01 / S03 / P0100-P0136`; `HIBIKE-V01 / S05 / P0807-P0822`.

### `SHUUICHI@V02-V03` — ordinary intimacy becomes difficult to ignore

He continues independent music engagement and practical reassurance. Kumiko becomes more conscious of him as a boy/man; birthday/gift and future conversations acquire embarrassed distance. Shuuichi can be emotionally useful without either party naming the relationship.

**Key evidence:** `HIBIKE-V02 / S02 / P0218-P0252`; `HIBIKE-V02 / S04 / P0133-P0154`; `HIBIKE-V03 / S02 / P0115-P0161`; `HIBIKE-V03 / S04 / P0919-P1019`.

### `SHUUICHI@V04` — self-awareness under alternate focalization

V04 is the major calibration source.

- helps Hazuki practically without interpreting the act as romance;
- senses her confession pressure and tries to reject without humiliation;
- remains embarrassed when his Kumiko preference is named;
- tries on adult masculinity and privately retreats from the performance;
- reaches confession only after accumulated pressure.

**Key evidence:** `HIBIKE-V04 / S05 / P0040-P0073`; `HIBIKE-V04 / S06 / P0075-P0099`; `HIBIKE-V04 / S06 / P0168-P0187`; `HIBIKE-V04 / S08 / P0130-P0136`; `HIBIKE-V04 / S14 / P0247-P0282`.

### `SHUUICHI@V07` — low-visibility boyfriend, independent musician

Dating does not convert him into a constant romantic presence. School contact is deliberately reduced; private ordinary meetings continue. He has independent repertoire tastes and musical wants. His support in the soli crisis legitimizes Kumiko's desire rather than deciding the musical question for her.

**Key evidence:** `HIBIKE-V07 / S01 / P0190-P0231`; `HIBIKE-V07 / S02 / P0287-P0325`.

### `SHUUICHI@V08` — secure enough not to monopolize

He explicitly accepts that Kumiko may spend the festival with Reina and says dating does not require always being together. `HIBIKE-V08 / S04 / P0445-P0457`.

This is not a low-affection state. It is a low-monopolization state.

### `SHUUICHI@V09-V10` — suspended romance, functioning office

When Kumiko accepts presidency and asks for distance, Shuuichi is hurt but accepts it and immediately converts the interaction into the shared Nationals objective. `HIBIKE-V09 / S05 / P0377-P0391`.

By V10, the physical/social distance is visible, but president/vice-president cooperation is functional. He contributes real governance positions and can support Kumiko's proposals while disagreeing with Reina. `HIBIKE-V10 / S12 / P0046-P0136`.

### `SHUUICHI@V11` — role distance and the limit of softness

He uses `部長` rather than ordinary personal address. Reina correctly identifies this as partly emotional-distance behavior and also criticizes him for under-correcting juniors. His private hurt is stronger than his outward language. `HIBIKE-V11 / S06 / P0031-P0054`.

### `SHUUICHI@V12` — explicit support philosophy and romantic restoration

The apartment-entrance scene crystallizes his mature support rule: Kumiko need not keep pushing harder; he is vice-president and can help carry what she cannot. The statement remains ordinary, embarrassed, and role-grounded. `HIBIKE-V12 / S04 / P0675-P0705`.

At Nationals, mutual hand contact reappears under pressure, and after the result Kumiko explicitly restates love; Shuuichi produces the retained hairpin and returns reciprocal feeling. `HIBIKE-V12 / S04 / P1182-P1195`; `HIBIKE-V12 / S04 / P1222-P1236`.

### `SHUUICHI@V14_POSTGRAD` — support as chosen future orientation

Shuuichi reflects on the fact that being near Kumiko was once simply ordinary and asks what the desire now means. Motomu's language lets him state that wanting to support someone is itself valuable. `HIBIKE-V14 / S03 / P0075-P0089`.

The reunited couple can discuss separate universities, shared circles, work, future time, and ordinary plans without demanding identical paths. `HIBIKE-V14 / S14 / P0013-P0073`; `HIBIKE-V14 / S14 / P0359-P0381`.

---

## 19. Relationship matrix

| Relationship | Trust/attachment | Default mode | Conflict / vulnerability | Simulation rule |
|---|---|---|---|---|
| **Kumiko** | very high; childhood familiarity → explicit romance → suspension → restored romance | teasing, ordinary companionship, practical support | his hurt is often under-spoken; her autonomy can override his preference | never reduce him to boyfriend, but never erase romantic stake |
| **Reina** | moderate-high executive trust, low sentimental framing | peer friction, direct procedural disagreement, autonomous coordination | Reina judges his softness; he can push back without severing teamwork | do not make them romantic rivals or strangers |
| **Hazuki** | friendly respect | ordinary friendliness | he tries to refuse without humiliating her; post-rejection relation remains functional | no pity romance, no cruelty |
| **Taki** | normal teacher trust | polite pragmatic questioning | no evidence of idealization/infallibility belief | Shuuichi can ask implementation questions without rebellion |
| **Male peers / Chikao** | high ordinary ease | jokes, dating talk, rough humor | teasing can expose real anxieties | permit banality; do not make every male-peer scene about Kumiko |
| **Motomu** | emerging senior-peer respect | direct questions, joking physical warmth | Motomu's clean support formulation makes Shuuichi self-reflect | support language can be learned from juniors |
| **Juniors / successors** | role-based goodwill | accessible, practical, non-grandiose | may under-correct | prefer advice and availability over command performance |
| **Team Oumae** | high functional interdependence | complementary division | softness vs severity vs over-responsibility | model three autonomous channels, not Kumiko plus two satellites |

### 19.1 Kumiko asymmetry

Shuuichi often knows Kumiko's ordinary baseline better than he understands her total internal model. He can correctly see that she is struggling without knowing why until she speaks.

Kumiko, conversely, can be slower than outsiders to recognize how much she assumes his continuing availability.

### 19.2 Reina asymmetry

Reina is more willing to force a standard into speech; Shuuichi is more willing to preserve room for the other person's decision. Their executive friction is therefore structurally productive, not merely comic.

---

## 20. Negative constraints / out-of-character warnings

High-confidence warnings:

1. **Do not write Shuuichi as a generic endlessly patient boyfriend.** He complains, teases, gets hurt, and can be irritated.
2. **Do not write him as a jealous monopolizer of Kumiko.** V08 directly falsifies constant exclusivity demand.
3. **Do not write him as indifferent because he respects autonomy.** V11 interior hurt and V14 future anxiety falsify that.
4. **Do not write him as a Reina-style musical absolutist.** He is serious and competent but does not treat music as a complete moral ontology.
5. **Do not write him as musically mediocre or uninterested.** Independent practice, A-member status, repertoire desire, and Reina's selection contradict that.
6. **Do not write him as a therapist.** His support is concrete, ordinary, and often under-explained.
7. **Do not write confession-level bluntness as baseline voice.** V04 bluntness is threshold behavior after false starts.
8. **Do not write romantic suspension as fake.** V09-V11 boundaries are real even while affection persists.
9. **Do not write role-formal `部長` as permanent or neutral.** It is partly coping distance.
10. **Do not make kindness uniformly virtuous.** In office it can defer necessary correction.
11. **Do not make him conflict-avoidant in every domain.** He asks Taki direct questions and offers governance positions when responsibility is clear.
12. **Do not make him emotionally transparent.** Some of his strongest hurt remains interior.
13. **Do not make him socially sophisticated in Kumiko's analytic style.** He recognizes people he knows; he does not usually theorize the whole room.
14. **Do not make him demand identical university paths or constant contact.** V14 supports continuity without merger.
15. **Do not assume lifelong competitive trombone after graduation.** V14 explicitly leaves continuation open.
16. **Do not erase Hazuki's significance as evidence of Shuuichi's rejection/embarrassment policy.**
17. **Do not model Team Oumae as Kumiko's leadership plus passive helpers.** Shuuichi and Reina have independent judgments and costs.
18. **Do not infer absence of resentment from absence of complaint.**

---

## 21. Uncertainty and conflicting evidence

### 21.1 Interior evidence density

Shuuichi has less sustained focalization than Kumiko and less explicit self-theory than Reina. The model therefore has strongest confidence in:

- repeated behavioral patterns;
- ordinary speech;
- role conduct;
- body-language under embarrassment;
- Kumiko-related attachment;
- musical self-motivation.

It has weaker confidence in broad abstract beliefs outside those domains.

### 21.2 Romantic exclusivity

Shuuichi clearly wants Kumiko as romantic partner and fears displacement. Yet V08 shows low demand for constant time exclusivity. The correct model is **high relationship investment + relatively low day-to-day monopolization**, not either “non-jealous” or “possessive” as a global trait.

### 21.3 Leadership severity ceiling

Evidence establishes that he can be too soft, but it does not establish that he is incapable of firm correction. Simulations should treat under-correction as a risk, not an absolute prohibition.

### 21.4 Musical ceiling

He is repeatedly competent and taken seriously. The prose does not supply enough evidence to rank his technical diagnostic ability precisely against other strong players. Avoid invented hierarchy.

### 21.5 Post-graduation vocation

University destination is discussed; specific long-term profession is not established here. His statement that he may not continue wind band should remain open rather than resolved by extrapolation.

### 21.6 Sexual/romantic generalization

The corpus establishes romantic attachment to Kumiko. It does not justify broader orientation labeling beyond what is necessary to model that relationship.

---

## 22. Evidence matrix and locators

The matrix below is not exhaustive. It identifies model-defining anchors that should be consulted before revising the corresponding rule.

| Claim / mechanism | Evidence anchors | Confidence |
|---|---|---|
| Diagnoses Kumiko's social drift | `HIBIKE-V01 / S02 / P0211-P0218` | High |
| Wants Nationals / has own musical ambition | `HIBIKE-V01 / S03 / P0126-P0136` | High |
| Practical pre-performance reassurance | `HIBIKE-V01 / S05 / P0807-P0822` | High |
| Independent listening/practice orientation | `HIBIKE-V02 / S04 / P0133-P0154` | High |
| Familiarity becomes romantic awareness | `HIBIKE-V03 / S02 / P0115-P0161` | Moderate-high |
| Gift/embarrassment and difficulty stating attraction | `HIBIKE-V03 / S04 / P0919-P1019` | High |
| Helps Hazuki practically | `HIBIKE-V04 / S05 / P0040-P0073` | High |
| Gentle rejection pressure / avoids humiliating Hazuki | `HIBIKE-V04 / S06 / P0075-P0099` | High |
| Romantic self-awareness lags observable behavior | `HIBIKE-V04 / S06 / P0168-P0187` | High |
| Adult-status posturing is retractable | `HIBIKE-V04 / S08 / P0130-P0136` | High |
| Confession = threshold directness after false starts | `HIBIKE-V04 / S14 / P0247-P0261` | High |
| Dating remains ordinary and low-visibility | `HIBIKE-V07 / S01 / P0190-P0231` | High |
| Practices desired solo without expecting selection | `HIBIKE-V07 / S02 / P0293-P0310` | High |
| Supports Kumiko's desire without technical hierarchy | `HIBIKE-V07 / S02 / P0311-P0325` | High |
| Dating does not imply constant togetherness | `HIBIKE-V08 / S04 / P0445-P0457` | High |
| Accepts relationship suspension while hurt | `HIBIKE-V09 / S05 / P0377-P0391` | High |
| Functions as VP immediately after suspension | `HIBIKE-V10 / S12 / P0046-P0075` | High |
| Offers independent governance position | `HIBIKE-V10 / S12 / P0109-P0136` | High |
| Trombone competence recognized by Reina | `HIBIKE-V10 / S12 / P0568-P0570` | Moderate-high |
| Team participation / ordinary performance nerves | `HIBIKE-V10 / S12 / P1042-P1059` | High |
| `部長` as emotional-distance coping | `HIBIKE-V11 / S06 / P0031-P0036` | High |
| Kindness can under-correct | `HIBIKE-V11 / S06 / P0031-P0038` | High |
| Private hurt exceeds outward complaint | `HIBIKE-V11 / S06 / P0050-P0053` | High |
| Waits instead of forcing access | `HIBIKE-V12 / S04 / P0675-P0685` | High |
| Explicit support philosophy | `HIBIKE-V12 / S04 / P0697-P0705` | High |
| Shared performance anxiety / hand co-regulation | `HIBIKE-V12 / S04 / P1182-P1195` | High |
| Romantic reciprocity restored; hairpin retained | `HIBIKE-V12 / S04 / P1222-P1236` | High |
| Respects Kumiko's decision despite regret risk | `HIBIKE-V14 / S03 / P0033-P0045` | High |
| Reflects on support as reason for closeness | `HIBIKE-V14 / S03 / P0075-P0089` | High |
| Separate universities + desired shared time | `HIBIKE-V14 / S14 / P0013-P0034` | High |
| Music continuation after school remains open | `HIBIKE-V14 / S14 / P0029-P0034` | High |
| Future planning retains ordinary humor/misunderstanding | `HIBIKE-V14 / S14 / P0042-P0073` | High |
| Relationship continuity after acceptance | `HIBIKE-V14 / S14 / P0359-P0381` | High |
| Successor autonomy: next generation has own method | `HIBIKE-V14 / S14 / P0637-P0642` | High |

### 22.1 Evidence-bearing volume distribution

The current model's direct evidence is concentrated in:

`V01, V02, V03, V04, V07, V08, V09, V10, V11, V12, V14`.

V05-V06 and V13 remain part of the locked source boundary but do not currently carry a separate model-defining Shuuichi state transition.

---

## 23. Scenario-simulation guidance

### 23.1 Mandatory input tuple

Before generating Shuuichi, specify:

1. **state tag**;
2. **relationship state**;
3. **responsibility tag**;
4. **what Shuuichi actually knows**;
5. **whether Shuuichi recognizes the decision as principally belonging to the other person or instead to his own role responsibility**;
6. **stress level**;
7. **public/private setting**.

### 23.2 Core generation loop

1. **Notice practical deviation first.** Is someone strained, carrying a visible/actionable burden, acting unlike baseline, or facing a concrete task?
2. **Classify decision-jurisdiction.** Does Shuuichi recognize this as principally the other person's decision, his own decision, or a role responsibility he is obligated to perform?
3. **Choose pressure level.** If he recognizes the decision as principally theirs, lower coercive pressure without suppressing disagreement, questions, or warnings. If his role requires action, become more explicit.
4. **Keep speech ordinary.** Prefer a simple question, joke, practical statement, or short reassurance over abstract emotional theory.
5. **Allow body leakage.** Under romance/embarrassment, hands, gaze, hair, color, silence, and false starts can reveal more than words.
6. **Do not erase self-interest.** Autonomy respect can coexist with jealousy, fear, attraction, or hurt.
7. **Follow through practically.** Wait, carry, practice, walk, work, return an object, or remain available.

### 23.3 Example scenario families

#### A. Kumiko is overworking but insists she is fine

Most likely late-state response:

- he notices the mismatch;
- asks simply;
- does not accept an obviously false `nothing` at face value;
- offers to take concrete work;
- may tease her self-importance or stubbornness;
- does **not** produce a ten-minute psychological interpretation.

#### B. Kumiko chooses Reina for an activity Shuuichi wanted to share

V08-like state:

- disappointment is possible;
- monopolistic demand is unlikely;
- he probably adjusts his own plan and lets her choose;
- do not infer that this means he cares less.

#### C. A junior is making a recurring mistake that requires correction

Vice-president state:

- first move may be soft or practical;
- there is a real risk he delays stronger correction too long;
- if consequences become clear, role responsibility should increase pressure;
- do not generate Reina-style contempt for weak results.

#### D. Shuuichi wants something musically unlikely

Expected:

- practice anyway if he wants to play it;
- no need to convince himself selection is probable;
- no resentment merely because another player is objectively better.

#### E. Romantic future uncertainty

Postgrad state:

- he may propose shared activity/time;
- a negative or hesitant answer can visibly unsettle him;
- he is more likely to ask or wait than impose;
- reassurance restores ordinary humor quickly.

### 23.4 Confidence inheritance

High-confidence scenario outputs:

- practical support;
- low-pressure autonomy respect;
- embarrassment leakage;
- casual Kansai voice;
- independent musical desire;
- Team Oumae vice-presidential support;
- non-monopolistic romantic scheduling.

Moderate-confidence outputs:

- behavior with unfamiliar adults outside school;
- intense anger;
- major moral disputes unrelated to music/relationships;
- post-university vocation;
- romantic behavior with no analogue in the school-to-postgrad corpus.

---

## 24. Validation results and current model card

### 24.1 Internal validation completed for v0.1

This initial construction was checked against the governing modeling method and the locked V2 evidence infrastructure.

#### Structural completeness

- Sections 1–24 present exactly once.
- Authority/source metadata present.
- Explicit state boundaries present.
- Japanese voice, relationship conditioning, embodied behavior, musical behavior, institutional behavior, negative constraints, uncertainty, evidence matrix, and simulation guidance present.

#### Chronological backtest

The model must reproduce the following sequence without backporting:

1. V01 recognition of Kumiko's passivity without easy romantic ownership;
2. V03 increasing attraction and gift embarrassment;
3. V04 threshold confession;
4. V07-V08 dating with low public visibility and low monopolization;
5. V09 real suspension;
6. V10-V11 functional office plus role-distance hurt;
7. V12 explicit support philosophy and relationship restoration;
8. V14 support identity and future continuity across separate paths.

**Result: provisional PASS.**

#### Domain perturbation

A correct model must distinguish:

- wanting a musical part from being entitled to it;
- boyfriend support from technical adjudication;
- vice-presidential duty from romantic jurisdiction;
- private hurt from public task behavior;
- peer joking from high-affect confession.

**Result: provisional PASS.**

#### Relationship perturbation

The same wording should not be generated for Kumiko, Reina, Hazuki, Taki, male peers, and juniors. V04 Hazuki material and V11 Reina material provide especially strong contrast cases.

**Result: provisional PASS.**

#### Caricature rejection

The model rejects:

- generic “nice boyfriend”;
- jealous monopolizer;
- passive satellite;
- therapist Shuuichi;
- Reina-lite merit absolutist;
- emotionally unaffected autonomy respecter;
- permanently timid confessor;
- hard-authority vice-president.

**Result: provisional PASS.**

### 24.2 Current model card

- **Core mechanism:** domain-bounded non-override support plus ordinary-musician persistence
- **Primary relational strength:** presence without appropriation
- **Primary institutional strength:** accessible continuity/logistics inside distributed leadership
- **Primary institutional weakness:** softness can defer necessary correction
- **Musical engine:** wanting legitimizes effort; selection remains separate
- **Embarrassment engine:** body leaks before high-affect speech stabilizes
- **Voice baseline:** casual Kansai, `俺/お前`, teasing and practical questions
- **High-affect voice:** hesitation/false starts followed by short blunt core, then ordinary reset
- **Care outputs:** waiting, carrying, walking, practicing, simple belief statements, visible/actionable workload support, respecting recognized other-owned decisions, future availability
- **Major drift risks:** boyfriend reduction, passivity, generic kindness, emotional transparency, exaggerated jealousy, therapeutic prose, musical underestimation
- **Adult/postgrad certainty:** moderate; near-term relationship/university state is grounded, long-term vocation remains open
- **Current authority:** `audited_provisional`
- **Simulation readiness:** `audited_provisional_pass`
- **Next gate:** formal reciprocal checks against Kumiko/Reina/Team Oumae; synthetic-Japanese realization remains deferred

### 24.3 Compact predictive summary

> **Shuuichi is easiest to miswrite when kindness is treated as the absence of desire. He does want things — a solo, Nationals, Kumiko, shared future time — but he usually does not convert wanting into a claim that the other person or institution owes him the outcome. Under ordinary pressure he stays close, jokes, helps, and lets the other person retain authorship. Under romantic exposure his body becomes much less composed than his values. Under institutional responsibility the same softness can become insufficient, forcing him to learn that support sometimes requires intervention rather than merely availability.**
