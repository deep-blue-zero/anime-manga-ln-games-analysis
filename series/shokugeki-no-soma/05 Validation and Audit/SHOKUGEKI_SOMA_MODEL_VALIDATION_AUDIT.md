---
series: SHOKUGEKI
artifact_type: model_validation_audit
scope: SOMA_CHARACTER_MODEL_SAMPLE
generation: V1
status: canonical
source_boundary: Original Japanese manga sampled volumes V01, V03, V08, V13, V19, V25, V30, V36. V01-V25 form the construction set; V30 and V36 are prospective holdouts. This audit evaluates the predictive warrant of SHOKUGEKI_SOMA_FINAL_CHARACTER_MODEL.md and does not convert the project into a full V01-V36 literary reread.
validated_artifact: SHOKUGEKI_SOMA_FINAL_CHARACTER_MODEL.md
construction_snapshot_revision: "0B24avie5yJngZDkzWVc3YjFZWm85bGFVWUZaWGV0Zk4vM2l3PQ"
post_v30_snapshot_revision: "0B24avie5yJngakRWdU5WQi96K3lvU1owbnVMUHFDZklHcDB3PQ"
post_v36_revision: "0B24avie5yJngYWU2cTJRTC82MCszZGFVQjhLV3Z1ZTVjN2owPQ"
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
created: 2026-08-17
---

# SHOKUGEKI_SOMA_MODEL_VALIDATION_AUDIT

## 1. Purpose and audit question

This document is the validation and methodological-audit companion to `SHOKUGEKI_SOMA_FINAL_CHARACTER_MODEL.md`.

The final character model is intentionally generative. It claims that, given enough situational context, the sampled Japanese manga evidence can support predictions about how **Yukihira Soma / 幸平創真** is likely to speak, decide, compete, learn, collaborate, support another person, respond to authority, react to failure, and use cooking as a mode of cognition in situations that never literally occur in the sampled volumes.

That kind of model creates an obvious retrospective risk. Once the ending is known, a sufficiently flexible character essay can make almost any late-series behavior look inevitable. The governing method therefore reserved two volumes from free model construction:

- **V30** as the first longitudinal holdout;
- **V36** as the final endpoint holdout.

The audit question is consequently narrower and more demanding than "does the final model fit the manga?"

> **Did the model, in forms frozen before V30 and before V36, prospectively predict the kinds of speech, behavior, cognition, relationship dynamics, and exception conditions that the held-out volumes actually supplied?**

A second question follows:

> **Where did the holdouts reveal genuine new mechanisms, insufficiently tested conditions, or limits that prevent the final model from claiming more predictive authority than the source design warrants?**

The audit is therefore designed to preserve both successes and failures. A `PARTIAL`, `MISS`, or `UNTESTED` cannot be retroactively converted into a `CONFIRM` merely because the mature model can now explain the scene.

---

# 2. Executive validation result

The project produced twenty broad prospective holdout tests across V30 and V36.

| Holdout | CONFIRM | PARTIAL | MISS | UNTESTED |
|---|---:|---:|---:|---:|
| V30 | 9 | 1 | 0 | 0 |
| V36 | 9 | 0 | 0 | 1 |
| **Total** | **18** | **1** | **0** | **1** |

Nineteen of the twenty broad predictions encountered a source condition that permitted meaningful evaluation. Of those nineteen directly testable predictions:

- eighteen received full `CONFIRM` dispositions;
- one received `PARTIAL`;
- none received `MISS`.

The remaining V36 prediction was `UNTESTED` because the volume did not supply the relevant condition: genuinely interdependent shared-kitchen work with local task hierarchy comparable to V30.

This is strong **within-sample qualitative validation**. It is not a statistical accuracy percentage, and it must not be presented as one. The twenty tests are broad, partly correlated, selected to probe known model dimensions, and scored by the same analytical process that built the model. They are not twenty independent Bernoulli trials, not a random sample of all possible Soma situations, and not an independently blinded benchmark.

The defensible conclusion is:

> **The frozen model generalized unusually well to two strategically chosen late-series volumes, including conditions that were absent or weakly represented in the construction set. No directly tested broad prediction suffered a clear contradiction. The holdouts nevertheless added new mechanisms and left meaningful coverage gaps, so the final model should be treated as strongly validated within its sampled domains rather than exhaustive or infallible.**

---

# 3. Governing protocol and evidentiary authority

The audit is subordinate to the canonical governing documents:

1. `SHOKUGEKI_SOMA_ANALYTICAL_METHOD.md`;
2. `SHOKUGEKI_SOMA_SYNTHESIS_ARCHITECTURE.md`;
3. `SHOKUGEKI_SOURCE_INVENTORY.md`;
4. the sequential publication-boundary readings;
5. the longitudinal ledgers;
6. `SHOKUGEKI_SOMA_FINAL_CHARACTER_MODEL.md` as the mature reconstruction surface.

The analytical method established four controls that matter especially here:

- original Japanese manga as primary evidence;
- conditional hypotheses rather than trait adjectives;
- preservation of counterevidence;
- and late-volume holdouts that cannot silently inform earlier model construction.

The synthesis architecture further requires two auditable snapshots:

- **Snapshot A — after V25:** the construction/model-training boundary before V30;
- **Snapshot B — after V30:** the revised boundary before V36.

Earlier sequential readings are historical publication-boundary artifacts and were not rewritten to make them look more prescient after later volumes became known.

---

# 4. Audit provenance: the freezes are recoverable from Drive revision history

A major strength of this corpus is that the freezes are not merely asserted in retrospective prose. The mutable behavioral ledger retained Google Drive revision history across the project.

## 4.1 Snapshot A — V25 construction freeze

Canonical behavioral ledger:

`SHOKUGEKI_SOMA_BEHAVIORAL_MODEL_LEDGER.md`\
Drive ID: `1SydrqDMZFoXyU0p6QAI_JqLcflAOjSoL`

Most recent V25-scoped revision before V30:

- revision ID: `0B24avie5yJngZDkzWVc3YjFZWm85bGFVWUZaWGV0Zk4vM2l3PQ`
- modified: `2026-08-17T15:58:35.127Z`
- recorded scope: `SOMA_BEHAVIORAL_MODEL_V01_V03_V08_V13_V19_V25_PLUS`
- `last_updated_scope: V25`

That revision explicitly contains the frozen V30 tests. It is therefore possible to reconstruct the prediction state without relying on the post-V30 ledger.

Parallel voice and relationship ledgers also preserve V25-era revisions at approximately the same synchronization point, providing corroborating evidence that the project state was advanced as a coordinated corpus rather than one document being edited retrospectively in isolation.

## 4.2 Snapshot B — post-V30 freeze

Behavioral-ledger revision after V30 scoring and model revision, but before V36:

- revision ID: `0B24avie5yJngakRWdU5WQi96K3lvU1owbnVMUHFDZklHcDB3PQ`
- modified: `2026-08-17T16:30:53.140Z`
- recorded scope: `SOMA_BEHAVIORAL_MODEL_V01_V03_V08_V13_V19_V25_V30_PLUS`
- `last_updated_scope: V30`

This revision explicitly states that the V30-revised model is frozen before the final holdout and contains the V36 behavioral tests.

Again, the voice and relationship ledgers possess synchronized V30-era revisions at approximately `16:30-16:31Z`, supporting the same corpus-state boundary.

## 4.3 Post-V36 revision

The substantive V36 update appears in the behavioral ledger as:

- revision ID: `0B24avie5yJngYWU2cTJRTC82MCszZGFVQjhLV3Z1ZTVjN2owPQ`
- modified: `2026-08-17T17:21:33.606Z`
- scope through V36.

A later synchronization-only revision at `17:51:07.077Z` corrected a stale prose coverage line that still listed V01-V25 despite correct V36 YAML metadata. That cleanup did not change the holdout scorecard or the substantive model.

## 4.4 What revision history proves—and what it does not

The revision chain materially reduces one form of hindsight bias: the broad predictions demonstrably existed in stored corpus state before the corresponding holdout revisions were incorporated into the cumulative ledger.

It does **not** prove perfect experimental blinding. The same language model/analytical process performed the project, and a general-purpose model may possess latent prior knowledge of a well-known manga. The artifact freeze therefore establishes procedural prospectiveness inside the corpus; it cannot establish the stronger claim that the analyst had no latent familiarity with later series events.

That limitation is addressed explicitly in Section 15 rather than hidden.

---

# 5. Source-boundary controls

## 5.1 Construction set

The free construction set was:

- V01;
- V03;
- V08;
- V13;
- V19;
- V25.

These volumes were allowed to create, revise, strengthen, downgrade, or leave open model claims.

## 5.2 First holdout

V30 was not allowed to revise the model until its frozen predictions had been scored.

Its canonical boundary is Japanese manga Chapters 254-262, ending at CBZ image `30-186`. The two-page Senzaemon interlude at `30-187` to `30-188` is supplementary and supplies no diagnostic direct Soma evidence; later-volume state was excluded.

## 5.3 Final holdout

V36 was likewise scored before revision.

Its evidence is tiered:

- **Tier A:** serialized Chapters 309-315, ending at `36-145`;
- **Tier B:** official final-volume `Le dessert` 1-3 material, used as canonical post-finale evidence but not projected backward to overwrite the serialized local state.

This matters because `Le dessert` includes retrospective and future information. The audit permits it to establish endpoint state or clarify provenance, but not to rewrite what an earlier volume could have supported at its publication boundary.

## 5.4 Unsampled volumes

Volumes outside the eight-volume sample do not repair gaps in this audit. Their possible existence is a limitation, not an invitation to silently fill missing conditions with remembered series knowledge.

---

# 6. Scoring rubric

The four score labels are qualitative dispositions, not numerical grades.

## CONFIRM

Use when the held-out source supplies a diagnostic condition and Soma's behavior matches the **mechanism or functional direction** predicted before the source was incorporated.

A mere lack of contradiction is normally insufficient for a positive behavioral prediction. The principal exception is a prediction explicitly formulated as a **negative constraint**, where the relevant audit question is whether a predicted surprising behavior actually appears under a context in which it could plausibly have appeared.

## PARTIAL

Use when:

- the source condition overlaps but does not cleanly instantiate the frozen condition;
- only part of a compound prediction is tested;
- the broad direction survives but the source requires a substantial mechanism refinement;
- or the scene is compatible with the prediction without warranting a full test.

`PARTIAL` must not later be promoted simply because the revised model explains the scene well.

## MISS

Use when a relevant held-out scene materially contradicts the frozen rule under conditions where its exception clauses do not save it.

A `MISS` is not "the source contains an unexpected detail." Holdouts are expected to add details. A miss means the model predicted the wrong behavioral direction or excluded something the source clearly does.

## UNTESTED

Use when the holdout simply does not supply the condition necessary to evaluate the prediction.

Absence is not confirmation.

This category is methodologically important because the project deliberately preserves open teamwork questions in V25 and later refuses to pretend that V36 retests them when it does not.

---

# 7. Snapshot A: what the model actually claimed after V25

The V25 freeze was not a vague assertion that "Soma is competitive and creative." By that point the model already made several fairly restrictive distinctions.

The strongest construction-state formulation was approximately:

> **Soma is a low-ceremony, customer-trained experimentalist whose confidence comes from repeated contact with solvable problems rather than a need to believe himself superior. He approaches credible deficiency, admits missing knowledge cheaply, learns across prestige boundaries, treats contextual constraints as part of cooking, respects demonstrated competence and functional responsibility without converting them automatically into social submission, and preserves authorship by transforming rather than avoiding influence. Competition remains porous to admiration and exchange.**

V25 also left explicit gaps. Most importantly, its first bout was a team contest only at the scoreboard level; the cooks produced parallel individual dishes. The model therefore did **not** claim direct evidence that Soma could work inside genuinely interdependent shared-dish production, accept peer correction in real time, or shift dynamically between task leadership and subordinate execution.

That gap is what made V30 a meaningful holdout rather than a late repetition of already observed behavior.

## 7.1 Frozen V30 tests

The stored pre-V30 model specified:

1. **Voice stability:** low-ceremony morphology and shallow `～っす` accommodation should persist.
2. **Deficiency approach:** credible gaps should attract observation, tasting, questioning, or testing rather than sustained denial.
3. **Opponent permeability:** hostile/rival excellence should remain epistemically usable.
4. **Authority decomposition:** rank should affect expectations but not automatically settle factual comparison or create deep social deference.
5. **Authorship:** external influence should be incorporated without eliminating `俺の料理`.
6. **Context:** recipient/service/environmental constraints should remain operative when present.
7. **Care:** visible vulnerability should more likely produce a concrete next move than prolonged abstract consolation.
8. **Competition does not totalize relationships:** win/loss should not automatically rewrite social register into superior/subordinate.
9. **Low-prestige filtering:** useful mechanisms may come from low-status as well as elite sources.
10. **Negative constraints:** bluffing knowledge, prestige-only ingredient preference, opponent-skill denial, and title-only ceremonial submission should be surprising absent intervening development.

---

# 8. V30 holdout audit

## V30-01 — Voice stability

**Frozen prediction:** low-ceremony morphology and shallow `～っす` accommodation should persist.

**Score:** **CONFIRM**

V30 raises the stakes without linguistically replacing Soma. He continues to address Tsukasa with `司先輩` while using the same shallow casual-politeness architecture observed much earlier. He does not become ceremonially formal because the contest is institutionally decisive. His cook-performance register remains available through `おあがりよ`, and direct challenge language remains ordinary with Erina.

The source therefore tests more than simple catchphrase recurrence. It confirms that **pressure changes urgency and compression more than it changes Soma's baseline social architecture**.

**Audit caution:** V30 contains a narrow range of formal-adult contexts. The score validates high-stakes peer/senior competition, not every possible professional ceremony.

## V30-02 — Deficiency approach

**Frozen prediction:** credible gaps should attract observation/tasting/questioning/testing rather than denial.

**Score:** **CONFIRM**

Soma tastes Tsukasa's current course, recognizes that it exceeds the level he previously encountered, and does not protect the older comparison by claiming Tsukasa must simply have held back. He accepts that his own current strongest dishes are insufficient for the required main-course problem and moves into testing and correction.

This is especially diagnostic because the championship context gives him strong ego incentives to minimize the opponent's improvement. Instead, he updates the problem.

**Model effect after scoring:** strengthened the claim that confidence is compatible with empirical uncertainty, but did not create that claim retroactively; the mechanism was already present in the freeze.

## V30-03 — Opponent permeability

**Frozen prediction:** hostile or rival excellence should remain epistemically usable.

**Score:** **CONFIRM**

Tsukasa and Rindo are the final opposing pair and are tied to the Central conflict, yet their cooking remains material to taste and analyze. Soma does not invoke ideological opposition as a reason to discount technical evidence.

This reproduces a construction-set pattern under maximal institutional opposition: hostility does not authorize epistemic dishonesty.

**Audit strength:** high. The scene supplies both meaningful opposition and demonstrably superior current cooking.

## V30-04 — Authority decomposition

**Frozen prediction:** rank may affect expectations but should not automatically settle factual comparison or create deep social deference.

**Score:** **CONFIRM**

V30 supplies the strongest direct validation of this distinction.

Soma contests Erina's attempt to settle the course-role dispute through status. He treats her palate as evidence and her title as non-dispositive. Yet when the task later changes and Erina owns the urgent final-dish problem, he can execute her instructions at high speed without humiliation.

The holdout therefore confirms that the construction model's "irreverence" decomposition was directionally correct. Soma is not anti-hierarchy in a simple sense. He distinguishes:

- prestige;
- competence;
- task ownership;
- and global interpersonal rank.

**Novel mechanism added after scoring:** dynamic task hierarchy. The source demonstrates role switching more clearly than the construction set did.

## V30-05 — Authorship under influence

**Frozen prediction:** external influence should be incorporated without eliminating `俺の料理`.

**Score:** **CONFIRM**

Soma explicitly recruits Erina's God Tongue for repeated calibration. He accepts corrections immediately, modifies components, and still preserves a final arrangement that is not reducible to Erina's exact instructions. The appetizer also recombines prior `ゆきひら改` resources with new inputs.

This is a high-value test because it exposes Soma to strong external intelligence in real time rather than merely showing him remember a teacher's technique later.

The result supports the mature distinction:

> **correction can penetrate the work deeply without capturing authorship.**

## V30-06 — Context remains first-class

**Frozen prediction:** recipient, service, or environmental constraints should remain operative when present.

**Score:** **CONFIRM**

V30 expands contextual design from the single dish to the course sequence. Soma's appetizer is not evaluated only as an isolated plate; its temporal flavor path and what it does to Erina's subsequent main become part of the final culinary object.

This is a genuine extrapolation from earlier bento, service-workflow, and ingredient-context reasoning. The exact multi-course mechanism was new, but the underlying rule—**what the eater actually experiences depends on context beyond plated composition**—survived.

## V30-07 — Care / agency restoration

**Frozen prediction:** visible vulnerability should more likely produce a concrete next move than prolonged abstract consolation.

**Score:** **PARTIAL**

This score is deliberately preserved.

V30 does not present a clean analogue to Megumi's execution anxiety, the child's fear of ridicule, or Hisako's shame. Erina is a highly competent peer whose problem is not simple visible vulnerability. Soma responds by attacking the adequacy of her current cooking, framing their cooperation as `俺とお前の食戟`, demanding a real decisive dish, and then serving as her assistant once she commits.

The scene is strongly compatible with the deeper idea of **agency restoration**, but the frozen condition was underspecified for a high-competence peer. Awarding full `CONFIRM` would overstate how directly V30 tested the prediction as written.

**Post-score revision:** the mature model becomes competence-sensitive: some people need safer failure; some need meaningful work; a highly capable peer may need a challenge that forces full authorship.

This is the most important preserved non-confirmation in the entire project.

## V30-08 — Competition does not totalize relationships

**Frozen prediction:** win/loss should not automatically rewrite social register into superior/subordinate.

**Score:** **CONFIRM**

V30 goes beyond simple compatibility. Soma turns cooperation itself into `俺とお前の食戟`. Rivalry is not merely tolerated beside teamwork; it becomes a mechanism that pressures the shared output upward.

After victory, the relationship does not settle into fixed leader/follower status. Teasing and challenge survive.

**Novel mechanism added after scoring:** **agonistic synchronization**—with a sufficiently capable and trusted peer, competitive pressure can organize cooperation rather than undermine it.

The mechanism is new; the directional prediction is confirmed.

## V30-09 — Low-prestige filtering

**Frozen prediction:** useful mechanisms may come from low-status as well as elite sources.

**Score:** **CONFIRM**

Commercial yakiniku sauce is treated as engineered culinary information rather than disqualified by prestige. Soma identifies the useful pre-balanced function and modifies it for the dish.

This is a particularly clean holdout because the surrounding contest is maximally elite. The source had every opportunity to shift Soma toward prestige-filtered reasoning and instead preserves the construction-set permeability.

## V30-10 — Negative constraints

**Frozen prediction:** knowledge bluffing, prestige-only ingredient preference, opponent-skill denial, and title-only ceremonial submission should remain surprising.

**Score:** **CONFIRM**

No diagnostic violation appears despite multiple opportunities:

- Soma admits incomplete memory of `パテ・ド・カンパーニュ` rather than bluffing;
- he uses commercial sauce without status anxiety;
- he recognizes Tsukasa's improved skill;
- and neither Tsukasa's nor Erina's status becomes self-justifying truth.

**Audit caution:** this is a compound negative constraint, not four independent successful predictions. It counts as one broad test.

## 8.11 V30 verdict

V30 returns:

**9 CONFIRM / 1 PARTIAL / 0 MISS / 0 UNTESTED.**

More importantly, it validates the model on a condition the construction set had intentionally left weak: true interdependent work.

The holdout does not merely repeat V25. It demonstrates that Soma can:

- solicit peer correction;
- preserve authored responsibility;
- contest task ownership;
- provoke a strong partner toward a better solution;
- and then become that partner's rapid subordinate when the task changes.

That new mechanism is incorporated only **after** the frozen scorecard.

---

# 9. Snapshot B: what V30 was allowed to change before V36

The post-V30 revision legitimately expands the model in areas the construction set could not directly establish.

The major additions are:

1. **Peer correction at high bandwidth can coexist with authorship.**
2. **Task hierarchy is reversible and local.** Soma can oppose a person's global authority claim, accept their correction on a component, lead his own authored contribution, and then execute under that same person's direction when they own the urgent problem.
3. **Agonistic synchronization:** competition among highly capable trusted peers can be a mode of cooperation.
4. **Context can be sequential and relational across multiple dishes.**
5. **Care through agency restoration is competence-sensitive**, although V30's care result remains `PARTIAL` because the frozen condition was not cleanly instantiated.

The audit must resist two hindsight errors here.

First, these V30 mechanisms cannot be cited as if V25 had already predicted their exact form. V25 predicted directions—authorship persistence, non-totalizing competition, competence-respecting hierarchy—but left genuine interdependence open.

Second, V30's strong performance cannot be used to loosen the V36 test. The revised model must be frozen again before the endpoint.

## 9.1 Frozen V36 tests

The stored V30-scoped behavioral ledger states:

1. **Increased institutional status should not produce prestige-capture or title-dependent self-worth.**
2. **Credible gaps should still attract inquiry/testing rather than denial.**
3. **Opponent/rival excellence should remain usable information.**
4. **Authorship should remain robust but influence-permeable.**
5. **Relationship outcomes should not automatically totalize into dominance hierarchy.**
6. **If Erina appears diagnostically, rivalry/teasing should remain compatible with trust and culinary exchange.**
7. **If shared work occurs, Soma should accept local task authority when competence/ownership is clear.**
8. **Recipient/context should remain a first-class design variable when the source supplies one.**
9. **Low-status ingredients/mechanisms should remain usable when functionally appropriate.**
10. **Deep title-only deference, knowledge bluffing, opponent-skill denial, or prestige-only ingredient reasoning would be meaningful model failures absent explicit intervening development.**

The V36 sequential reading later groups these under corresponding endpoint labels such as voice continuity, rank/status non-capture, deficiency openness, influence-permeable authorship, relationship non-totalization, Erina rivalry/trust, local functional hierarchy, recipient/context, low-prestige permeability, and negative constraints.

---

# 10. V36 final-holdout audit

## V36-01 — Voice continuity despite increased status

**Frozen expectation:** increased status should not produce prestige capture; the voice model should remain recognizable rather than becoming ceremonially elite.

**Score:** **CONFIRM**

V36 provides a stronger temporal test than V30. The serialized BLUE material already preserves Soma's direct, low-ceremony style under world-class evaluation. `Le dessert 3 Futur` then moves him to age 25, after First Seat history and international professional success.

The expected status-driven linguistic transformation does not occur. He returns to Yukihira, speaks to Erina in a familiar register, frames improvement through more cooking and challenge, and retains the experimental social world visible near the beginning of the series.

This supports a strong reconstruction constraint:

> **Maturation should be modeled primarily through expanded competence, contextual reasoning, and relational understanding—not by replacing Soma's speech with a prestigious adult-chef persona.**

The holdout does not prove that he never uses formal Japanese in any unsampled professional situation. It does confirm continuity in high-status endpoint contexts that could easily have motivated such a rewrite.

## V36-02 — Rank/status non-capture

**Frozen prediction:** institutional status should not become title-dependent self-worth or a reason to stop self-testing.

**Score:** **CONFIRM**

BLUE achievement, later First Seat history, and international demand do not close Soma's developmental loop. He continues to evaluate himself through what he can actually make and through the responses of credible cooks/eaters rather than through possession of the title itself.

This is especially visible after the canonical BLUE final result: Erina defeats him, and the result becomes a reason to broaden himself further rather than a contradiction that must be denied because his status has risen.

The endpoint therefore confirms that prestige can accrue around Soma without becoming the principal internal authority by which he understands his cooking.

## V36-03 — Deficiency openness

**Frozen prediction:** credible gaps should continue to attract inquiry, testing, and retraining rather than denial.

**Score:** **CONFIRM VERY STRONGLY**

V36 supplies both retrospective and endpoint support.

Hayama's testimony describes Soma's repeated willingness to challenge cooks stronger than himself. The Tamako/failure material explains why failed food can remain cognitively usable. After Erina's BLUE victory, Soma's response is renewed training and expanded exposure.

The volume therefore reinforces the mechanism already inferred across the construction set:

> **Soma's resilience is not a belief that he cannot lose; it is low defensiveness toward actionable evidence of insufficiency.**

This is one of the most strongly validated claims in the final model because both holdouts attack it under escalating stakes without producing a miss.

## V36-04 — Influence-permeable authorship

**Frozen prediction:** authorship should remain robust while absorbing external influence.

**Score:** **CONFIRM VERY STRONGLY**

The endpoint makes the old `俺自身の味` problem explicit. Soma's BLUE cooking visibly contains accumulated contact with other cuisines, rivals, teachers, ordinary mechanisms, prior Yukihira work, and even family failure. The narrative nevertheless frames the result as `自分自身の味`.

This is almost an ideal holdout for the construction-set hypothesis because the endpoint could have resolved individuality through purity, hidden innate genius, or a single secret family essence. Instead it resolves individuality through **metabolized influence**.

The audit therefore grants high predictive warrant to the final model's distinction:

> **Influence is compatible with authorship; authorship-erasing role capture is the thing Soma resists.**

## V36-05 — Relationship non-totalization

**Frozen prediction:** major relationship outcomes should not automatically become permanent dominance hierarchy.

**Score:** **CONFIRM**

Erina defeats Soma in the BLUE final. That is precisely the kind of result that could have stabilized their relation into winner/loser hierarchy.

It does not.

The later relationship remains an unfinished developmental loop organized around renewed cooking, evaluation, teasing, and the desire to make Erina acknowledge his food. Erina's victory matters, but it does not totalize the relationship.

This strongly confirms a broader model rule visible with Hayama, Nene, Alice, and other rivals: **competitive results answer a comparison without exhausting the social or epistemic value of the other person.**

## V36-06 — Erina-specific rivalry and trust

**Frozen prediction:** if Erina appears diagnostically, rivalry/teasing should remain compatible with trust and culinary exchange.

**Score:** **CONFIRM VERY STRONGLY**

V36 does not resolve Erina's importance by replacing rivalry with generalized softness.

Soma criticizes her compromised cooking, invokes the arrogant/high-level rival identity he recognizes, cooks specifically for her, continues to seek the `美味い` she has withheld, and remains challenge-oriented in the future material.

At the same time, the relationship is more important than before. Erina is a privileged evaluator, recipient, developmental counterpart, and—by endpoint implication—romantically significant person.

The holdout therefore validates a subtle prediction:

> **greater trust and attachment need not produce a fundamentally gentler surface register in Soma.**

This is important for future synthetic dialogue. A generic romance template that makes mature Soma suddenly ceremonious or emotionally florid would be poorly grounded.

## V36-07 — Local functional hierarchy in shared work

**Frozen prediction:** if shared work occurs, Soma should accept local task authority when competence/ownership is clear.

**Score:** **UNTESTED**

V36 does not provide a new genuinely interdependent shared-production scene comparable to the V30 final course.

This is not a `CONFIRM by continuity`. The condition is absent.

The audit therefore preserves V30 as the strongest authority for reversible task hierarchy and refuses to multiply evidence where none exists.

This `UNTESTED` is methodologically healthy: it demonstrates that the audit does not require every holdout prediction to receive a positive score.

## V36-08 — Recipient/context remains first-class

**Frozen prediction:** recipient and context should remain causal design variables when the source supplies them.

**Score:** **CONFIRM VERY STRONGLY**

V36 supplies perhaps the strongest recipient test in the sample.

Soma explicitly makes a dish for Erina, prepares for Mana as a relevant eater, and identifies the person Erina actually wants to feed. The old unresolved Erina evaluation also functions as a long-horizon development constraint on Soma's dish.

This goes beyond generic sentiment. The source connects **who the food is for** to what culinary problem is being solved and to what counts as a meaningful breakthrough.

The endpoint therefore confirms the longitudinal expansion:

`ingredient/process context -> service context -> eating-sequence context -> specific recipient/relationship context`

without requiring the final model to claim that every dish is emotionally personalized.

## V36-09 — Low-prestige mechanism permeability

**Frozen prediction:** low-status ingredients and mechanisms should remain usable when functionally appropriate.

**Score:** **CONFIRM**

The endpoint preserves ordinary and low-status sources inside elite cooking. Carbonated water, diner practice, donburi architecture, family cooking, and failed food remain part of the same usable search space as international technique.

Again, this does not mean Soma prefers humble ingredients on ideological grounds. The validated rule is weaker and more precise:

> **social prestige is not a reliable filter for whether a mechanism contains useful culinary information.**

## V36-10 — Negative constraints

**Frozen prediction:** title-only deference, knowledge bluffing, opponent-skill denial, or prestige-only ingredient reasoning would constitute meaningful failures absent intervening development.

**Score:** **CONFIRM**

The endpoint supplies no such diagnostic reversal. Soma's increased status does not produce title capture; external techniques remain usable; rival strength remains acknowledgeable; and ordinary mechanisms remain legitimate.

As with the V30 negative-constraint item, these are not counted as four statistically independent successes. They form one compound falsification surface.

## 10.11 V36 verdict

V36 returns:

**9 CONFIRM / 0 PARTIAL / 0 MISS / 1 UNTESTED.**

The untested item is a source limitation, not a near-confirmation.

The endpoint's most important new information is **explanatory and relational rather than corrective**:

- Tamako gives causal provenance to the failure model;
- `自分自身の味` gives explicit endpoint language to influence-permeable authorship;
- Erina becomes a uniquely privileged recipient and developmental counterpart;
- the epilogue gives strong romantic implication;
- and mature status gives a long-range voice-continuity test.

These additions make the mature model richer. They should not be counted as extra holdout "hits" when they were not separately predicted.

---

# 11. Combined validation matrix

| ID | Frozen domain | Holdout | Score | What the holdout actually established |
|---|---|---|---|---|
| V30-01 | voice stability | V30 | **CONFIRM** | championship stakes preserve low-ceremony baseline and shallow accommodation |
| V30-02 | deficiency approach | V30 | **CONFIRM** | improved Tsukasa becomes a problem to update against, not deny |
| V30-03 | opponent permeability | V30 | **CONFIRM** | ideological opponents remain culinary evidence |
| V30-04 | authority decomposition | V30 | **CONFIRM** | rank is not proof; local task authority can still be obeyed |
| V30-05 | authorship | V30 | **CONFIRM** | God Tongue correction enters the dish without erasing Soma's authorship |
| V30-06 | context | V30 | **CONFIRM** | course order and temporal eating path become first-class variables |
| V30-07 | care | V30 | **PARTIAL** | agency-restoration direction survives, but high-competence peer condition requires revision |
| V30-08 | non-totalizing competition | V30 | **CONFIRM** | internal rivalry becomes a collaboration mechanism |
| V30-09 | low-prestige permeability | V30 | **CONFIRM** | commercial sauce remains usable engineered knowledge |
| V30-10 | negative constraints | V30 | **CONFIRM** | no bluffing, title-only submission, skill denial, or prestige-only ingredient logic |
| V36-01 | status/voice continuity | V36 | **CONFIRM** | adulthood and elite status do not replace Soma's basic register |
| V36-02 | rank/status non-capture | V36 | **CONFIRM** | status does not terminate self-testing or make title the measure of self-worth |
| V36-03 | deficiency openness | V36 | **CONFIRM** | failure and defeat remain actionable information at endpoint |
| V36-04 | influence-permeable authorship | V36 | **CONFIRM** | `自分自身の味` is built from metabolized external influence |
| V36-05 | relationship non-totalization | V36 | **CONFIRM** | Erina's BLUE victory does not stabilize a global dominance hierarchy |
| V36-06 | Erina rivalry + trust | V36 | **CONFIRM** | attachment deepens without erasing challenge/teasing/evaluation |
| V36-07 | local task hierarchy | V36 | **UNTESTED** | no new shared-production scenario; preserve V30 authority |
| V36-08 | recipient/context | V36 | **CONFIRM** | specific recipient becomes causally relevant to culinary design and breakthrough |
| V36-09 | low-prestige permeability | V36 | **CONFIRM** | ordinary mechanisms remain usable alongside elite technique |
| V36-10 | negative constraints | V36 | **CONFIRM** | no endpoint reversal into prestige capture, bluffing, or skill denial |

---

# 12. What the holdouts validate strongly

## 12.1 Japanese voice architecture — HIGH within sampled contexts

The holdouts strongly support continuity of:

- colloquial masculine baseline;
- shallow `～っす` accommodation;
- concrete phrasing for serious content;
- challenge/teasing persistence in close rivalry;
- and contextual cook-performance markers.

V36's age-25 material is particularly valuable because it prevents the model from assuming that adolescent casualness must disappear with professional maturation.

**Limit:** the sample is not a frequency corpus of every professional register and does not test every possible formal ceremony, customer demographic, or adult institution.

## 12.2 Deficiency, failure, and learning — HIGH

This is probably the best-validated behavioral domain.

Both holdouts support:

- approach toward credible gaps;
- low bluffing pressure;
- willingness to use stronger cooks as information;
- and continuation after defeat without requiring the loss to become emotionally trivial.

V36 additionally provides retrospective causal support through Tamako, but the predictive success does not depend on knowing that backstory in advance.

## 12.3 Authority decomposition — HIGH

The combined sample supports a stable distinction among:

- title/prestige;
- demonstrated competence;
- procedural legitimacy;
- local task ownership;
- and total social hierarchy.

V30 is the strongest validation because Soma can contest Erina's title claim and later obey her task instructions without contradiction.

## 12.4 Influence-permeable authorship — HIGH

V30 validates real-time correction without authorship collapse. V36 validates endpoint selfhood built from accumulated external influence.

The model can therefore predict with high confidence that Soma will not ordinarily experience learning another person's useful method as a threat to being himself.

## 12.5 Contextual cooking — HIGH

The holdouts extend rather than reverse the construction trajectory.

Context now has validated examples at several scales:

- ingredient/environment;
- service and workflow;
- transport/storage;
- eating sequence;
- dish-to-dish interaction;
- specific recipient and relationship.

This warrants strong confidence in predicting that Soma asks what the food must **do in this actual situation**, not merely what ingredient or technique has the highest abstract prestige.

## 12.6 Competition without social totalization — HIGH

The holdouts support competition as compatible with:

- admiration;
- information exchange;
- alliance;
- trust;
- interdependence;
- and strong attachment.

Results matter, but they do not automatically define the entire relationship.

---

# 13. What the holdouts validate only conditionally

## 13.1 Care and support — MEDIUM-HIGH, explicitly competence-sensitive

The broad agency-restoration model survives, but V30's `PARTIAL` prevents overstatement.

The sampled support patterns differ materially by condition:

- Megumi: consequential role and concrete credit;
- frightened child: reduce the cost of failure after provocation misfires;
- Hisako: shared-failure normalization, role reframing, concrete route forward;
- Erina: hard challenge that reactivates authorship in a highly competent peer.

The mature model is useful, but it should not predict one universal "Soma comfort style." The correct first question is what kind of blockage the person has and how much competence/trust the relationship supports.

## 13.2 Social perception — MEDIUM

The sample rejects "generally oblivious" and supports perception of posturing, confidence shifts, awkwardness, and some motivational mismatch.

It also preserves a weakness: concealed shame or fear can initially escape his calibration. V08 directly shows a provocative approach misfire before he adjusts.

Therefore do not model Soma as psychologically omniscient.

## 13.3 Dynamic collaboration hierarchy — MEDIUM-HIGH but scenario-concentrated

V30 is extremely strong direct evidence. V36 does not retest it.

The final model can predict reversible task hierarchy confidently in a similar high-competence culinary collaboration, but the corpus does not establish Soma as an across-domain organizational leader, manager, or commander.

---

# 14. Important endpoint additions that are not holdout "wins"

A validation audit must separate **new explanatory knowledge** from **predicted behavior**.

## 14.1 Tamako and the formative history of failure

V36's Tamako material strongly explains why the construction model found failure cognitively recoverable. But the audit must not count that backstory as another independent confirmation. The pre-V36 model did not specifically predict Tamako's role.

The legitimate claim is:

> the source later provides causal provenance that is unusually congruent with a previously inferred behavioral rule.

## 14.2 Erina's endpoint romantic implication

The post-finale material supports strong romantic implication and privileged-recipient status. The frozen V36 test predicted rivalry/trust compatibility if Erina appeared; it did **not** preregister a romantic outcome.

Therefore romance is an endpoint relationship finding, not part of the headline validation score.

## 14.3 Agonistic synchronization

V25 predicted that competition need not destroy alliance and that authorship should survive cooperation. It did not specifically predict that Soma would deliberately turn collaboration into `俺とお前の食戟` and use internal rivalry as the engine of the joint course.

V30 therefore represents:

- confirmation of the frozen directional claims;
- plus discovery of a more specific mechanism.

That distinction is important. A successful holdout can still teach the model something new.

---

# 15. Threats to validity and reasons not to overstate the result

## 15.1 Latent-knowledge / analyst-contamination risk

This is the largest conceptual limitation.

The project used a general-purpose language model to analyze a published manga. Even when later volumes are not opened during construction, the model may possess latent training-data familiarity, remembered summaries, or broad cultural knowledge of the series.

The Drive revision freezes demonstrate that the **artifact state** was prospectively recorded. They cannot prove that the analyst's underlying model weights were ignorant of later events.

This means the project is stronger than an ordinary retrospective essay but weaker than a preregistered experiment run by an analyst with demonstrably zero prior knowledge.

Mitigation used here:

- original Japanese source treated as governing evidence;
- explicit freeze documents;
- no unsampled volume allowed to establish claims;
- scorecard written before cumulative revision;
- publication-boundary discipline;
- preserved `PARTIAL` and `UNTESTED` dispositions.

Residual risk remains.

## 15.2 Strategic rather than random holdout selection

V30 and V36 were chosen because they were analytically valuable:

- V30 tests collaboration/interdependence and late institutional stakes;
- V36 tests endpoint stability, adulthood, final rivalry, failure, and authorship.

This is good **stress-test design** but not representative sampling. The holdouts intentionally concentrate important model dimensions.

Consequently, the audit supports generalization across these stressed domains better than it supports claims about the base rate of every kind of Soma behavior.

## 15.3 Broad prediction granularity

Several tests are broad families rather than exact next-line predictions.

For example, "deficiency attracts inquiry rather than denial" allows multiple behaviors—tasting, questioning, testing, retraining. This is appropriate for a generative personality model, but broader predictions are easier to satisfy than highly specific scene forecasts.

The audit compensates by requiring mechanism-level alignment and by refusing to count novel details as extra successes. Still, headline counts should not be confused with a narrow benchmark such as exact dialogue prediction.

## 15.4 Correlated predictions

The twenty tests are not independent.

Examples:

- deficiency openness and opponent permeability overlap;
- rank non-capture and negative title-deference constraints overlap;
- authorship and collaboration hierarchy interact;
- recipient/context and support behavior can overlap in Erina scenes.

Therefore no binomial significance calculation or statistical confidence interval is appropriate.

## 15.5 Same-process scoring

The same analytical system that built the model also scored the holdouts. There is no independent human rater or second model adjudicating borderline cases.

This especially matters for the V30 care `PARTIAL`, where judgment is interpretive. The conservative score helps, but does not replace independent reliability testing.

## 15.6 Eight-volume sample

The project samples eight of thirty-six tankobon volumes. It is longitudinal and strategically diverse, but not exhaustive.

Unsampled volumes may contain:

- low-frequency speech forms;
- unusual relationships;
- exceptions under conditions absent from the sample;
- or scenes that would narrow a HIGH claim to a more conditional formulation.

The final model is therefore **mature within sample**, not equivalent to a line-complete full-series corpus model.

## 15.7 Manga-only acoustic limitation

The model reconstructs written Japanese voice and manga textual/visual prosody. It does not directly model:

- pitch;
- speaking rate;
- acoustic emphasis;
- breath/laughter quality;
- seiyuu performance habits;
- or anime-specific dialogue adaptations.

A later audio pass could add these without superseding the manga voice model.

---

# 16. Coverage gaps: conditions the sample does not warrant simulating with high confidence

The final character model should remain explicitly cautious in the following areas.

## 16.1 Prolonged grief or bereavement in present-time action — OPEN

The sample contains family history and emotional meaning but not a strong extended present-time grief episode for Soma. Do not assume his ordinary actionability rule fully predicts sustained bereavement.

## 16.2 Severe non-culinary physical danger — OPEN

The corpus is dominated by culinary, institutional, social, and competitive problems. It does not robustly establish how Soma behaves in life-threatening violence, disaster response, or military-style danger.

## 16.3 Long-term romantic relationship behavior — OPEN / endpoint-limited

Erina has strong romantic implication at the endpoint, but the source does not provide a developed mutual dating/marriage register. Synthetic scenes involving established domestic romance should therefore be labeled extrapolative.

## 16.4 Formal personnel leadership at scale — OPEN

Soma can coordinate tasks and accept/reverse local hierarchy. The sample does not establish him as a manager of a large permanent staff, institutional administrator, or strategic organizational leader.

## 16.5 Deep apology and guilt after serious interpersonal harm — UNDERDETERMINED

The sampled volumes do not provide enough high-stakes cases where Soma recognizes that he personally caused major emotional harm and must repair the relationship over time.

## 16.6 Deception for social or strategic purposes — UNDERDETERMINED

The model supports directness and low bluffing around knowledge, but it does not prove that Soma is categorically incapable of tactical deception in every domain.

## 16.7 Non-food ideological disputes without an actionable cooking analogue — MEDIUM/OPEN

V19 tests ideology through culinary institutions. The model should be more cautious when a hypothetical moral or political dispute cannot be translated into craft, evidence, procedural legitimacy, or concrete consequences.

## 16.8 Broad everyday intimacy outside the culinary/social ecosystem — MEDIUM/OPEN

Food is Soma's dominant social interface in the sample. Quiet domestic conversation with no cooking, competition, or problem-solving anchor is less strongly constrained.

---

# 17. Final confidence calibration by model domain

| Domain | Final audit confidence | Reason |
|---|---|---|
| colloquial Japanese baseline and shallow politeness | **HIGH** | longitudinal construction + both holdouts + adult endpoint |
| serious-content diction remains concrete | **HIGH** | repeated across identity, ideology, failure, family, Erina |
| admission of ignorance / low bluffing pressure | **HIGH** | repeated and survives V30 negative-constraint test |
| fair-loss resilience / deficiency approach | **HIGH** | V08, V13, V30, V36 provide escalating tests |
| opponent competence remains epistemically usable | **HIGH** | Hayama, Alice, Tsukasa, Nene, endpoint rivals |
| prestige-permeable learning | **HIGH** | elite and low-status mechanisms both recur through holdouts |
| influence-permeable authorship | **HIGH** | V13-V25 construction, direct V30 and V36 confirmation |
| authority decomposition | **HIGH** | seniors, Central, WGO, Erina, V30 dynamic hierarchy |
| contextual cooking | **HIGH** | ingredient, logistics, workflow, sequence, recipient layers |
| competition does not totalize relationships | **HIGH** | repeated victories/defeats + both holdouts |
| care as agency restoration | **MEDIUM-HIGH** | strong multi-case evidence, but V30 remains PARTIAL and condition-sensitive |
| shame/vulnerability detection | **MEDIUM** | known V08 calibration miss plus later improvement |
| social perception of posturing/awkwardness | **MEDIUM-HIGH** | repeated, but not universal psychological insight |
| interdependent task hierarchy | **MEDIUM-HIGH** | V30 is strong; V36 UNTESTED; scenario concentration remains |
| large-team/organizational leadership | **OPEN** | not directly tested |
| explicit adult romance register | **OPEN / relationship-specific** | endpoint implication without developed couple dialogue |
| grief/bereavement behavior | **OPEN** | insufficient present-time evidence |
| non-culinary crisis behavior | **OPEN** | source-domain gap |

---

# 18. How the final character model should be used after this audit

`SHOKUGEKI_SOMA_FINAL_CHARACTER_MODEL.md` is validated as the preferred **mature reconstruction surface** for the sampled project.

Use it with three levels of discipline.

## 18.1 High-confidence reconstruction

It is appropriate to make fairly strong predictions when a novel scenario resembles validated domains such as:

- cooking under uncertainty;
- encountering a superior technique;
- losing or winning a fair contest;
- interacting with a prestigious expert;
- learning from a rival;
- working with a capable peer;
- using low-status or elite mechanisms pragmatically;
- deciding how to design food for a real recipient or service context;
- or speaking to established sampled relationship classes.

## 18.2 Conditional reconstruction

Use explicit qualifiers when simulating:

- emotional support;
- shame/fear responses;
- close relationship conflict;
- task leadership;
- or unfamiliar institutional settings.

First identify which sampled condition is actually analogous.

## 18.3 Open-domain reconstruction

For grief, established romance, non-culinary physical crisis, or large-scale management, the correct output is not false confidence. The model may offer a **reasoned extrapolation**, but it should be labeled as such and should not be presented as if directly demonstrated in the eight-volume corpus.

## 18.4 Synthetic Japanese dialogue rule

Future generated Soma dialogue should be labeled synthetic unless it is a short verified primary-source quotation with a locator.

The model is strongest at reproducing:

- pragmatic function;
- register choice;
- degree of ceremony;
- challenge/correction structure;
- and relationship-specific social stance.

It is not licensed to invent lines and then cite them as canon.

---

# 19. Reproducibility and retrieval route

For future audit or challenge, retrieve evidence in this order:

1. `SHOKUGEKI_SOMA_MODEL_VALIDATION_AUDIT.md` — scoring logic, snapshots, limitations;
2. `SHOKUGEKI_SOMA_FINAL_CHARACTER_MODEL.md` — mature predictive formulation;
3. `SHOKUGEKI_SOMA_BEHAVIORAL_MODEL_LEDGER.md` — current claims and revision history;
4. `SHOKUGEKI_SOMA_JAPANESE_VOICE_LEDGER.md` — linguistic claim history;
5. `SHOKUGEKI_SOMA_RELATIONSHIP_REGISTER_MATRIX.md` — interlocutor-specific model;
6. `SHOKUGEKI_V30_SOMA_CHARACTER_READING.md` and `SHOKUGEKI_V36_SOMA_CHARACTER_READING.md` — holdout scorecards and local evidence;
7. earlier sequential readings — construction history without later rewriting;
8. locked original Japanese CBZs — exact primary-source verification.

### Key behavioral-ledger revision checkpoints

| Project state | Revision ID | Scope |
|---|---|---|
| V25 construction freeze | `0B24avie5yJngZDkzWVc3YjFZWm85bGFVWUZaWGV0Zk4vM2l3PQ` | through V25 |
| post-V30 revised freeze | `0B24avie5yJngakRWdU5WQi96K3lvU1owbnVMUHFDZklHcDB3PQ` | through V30 |
| post-V36 substantive state | `0B24avie5yJngYWU2cTJRTC82MCszZGFVQjhLV3Z1ZTVjN2owPQ` | through V36 |

These revisions are part of the project's provenance and should be preserved as evidence that the two holdout scorecards were not created only after the final endpoint model stabilized.

---

# 20. Final methodological verdict

The eight-volume Soma modeling pass succeeds at its stated goal more strongly than a purely retrospective character essay would justify.

The reason is not simply that the final model can explain V30 and V36. A flexible model written after V36 could always do that. The stronger evidence is that:

- a V01-V25 construction state was frozen;
- V30 was read as a prospective holdout and returned **9 CONFIRM / 1 PARTIAL / 0 MISS / 0 UNTESTED**;
- the model was revised only after that scorecard;
- the V30 state was frozen again;
- V36 returned **9 CONFIRM / 0 PARTIAL / 0 MISS / 1 UNTESTED**;
- the `PARTIAL` and `UNTESTED` were preserved rather than normalized into success;
- and Drive revision history retains recoverable pre-holdout snapshots.

The model's strongest predictive warrant now concerns:

- low-ceremony Japanese voice;
- low defensiveness toward actionable deficiency;
- prestige-permeable learning;
- influence-permeable authorship;
- contextual cooking cognition;
- decomposition of prestige, competence, and task authority;
- competition that does not totalize relationships;
- and agency-oriented support with competence-sensitive variation.

The principal reasons for restraint are equally clear:

- only eight of thirty-six volumes were sampled;
- holdouts were strategic rather than random;
- predictions are broad and correlated;
- the same analytical process built and scored the model;
- latent prior series knowledge cannot be ruled out;
- and several human conditions important to a truly general personality simulation remain weakly sampled or absent.

The appropriate final authority statement is therefore:

> **`SHOKUGEKI_SOMA_FINAL_CHARACTER_MODEL.md` is a strongly validated, source-grounded generative model of Yukihira Soma within the represented culinary, competitive, institutional, collaborative, and relationship conditions. It has demonstrated longitudinal predictive stability against two prospectively frozen late-series holdouts. It should be used as current canonical authority for reconstruction and comparative analysis, while OPEN domains and unsampled-volume limitations remain explicit rather than being filled by confidence.**

With this audit complete, the focused eight-volume Yukihira Soma character-modeling pass has satisfied the Phase 6 exit condition defined by `SHOKUGEKI_SOMA_SYNTHESIS_ARCHITECTURE.md`.
