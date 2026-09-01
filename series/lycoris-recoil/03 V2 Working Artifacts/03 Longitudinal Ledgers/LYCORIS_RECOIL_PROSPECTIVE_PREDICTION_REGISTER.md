---
series: LYCORIS_RECOIL
artifact_type: ledger
scope: V2 prospective predictions, checkpoint freezes, and later adjudication
generation: V2
status: canonical
source_boundary: TV E01-E13 + Short 01; CP4_POST_E13 adjudicated through Short 01; SHORT01_OUTBOUND_FREEZE frozen before Short 02
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
mutable: true
current_checkpoint: SHORT01_OUTBOUND_FREEZE
---

# Lycoris Recoil Prospective Prediction Register

## 1. Responsibility

This register preserves what V2 predicted **before** later source evidence was opened.

Its purpose is to test whether the developing models generate behavior rather than merely redescribe scenes after the fact.

Prediction results are analytical validation evidence, not source facts about the characters.

---

# 2. CP0 — clean start

```yaml
checkpoint_id: CP0_PRE_E01
frozen: true
allowed_evidence: source_identity_and_bundle_metadata_only
v2_narrative_evidence: none
v1_claims_admissible_for_prediction: false
supplementary_sources_admissible: false
behavioral_predictions: none_by_design
reason: preserve_a_clean_pre_e01_baseline
```

E01 therefore begins without V2 behavioral predictions.

This is intentional: importing V1 expectations into CP0 would defeat the prospective restart.

---

# 3. Prediction schema

| Field | Meaning |
|---|---|
| Prediction ID | e.g. `PRED-CP1-CHI-001` |
| Checkpoint | Frozen model boundary |
| Allowed evidence | Exact prior source horizon |
| Target source/state | Later episode/short/supplementary premise |
| Character/relationship | Target |
| Condition/premise | What situation is being tested |
| Predicted action class | Likely behavior |
| Predicted affect direction | Where state should move |
| Predicted register | Speech/performance expectation |
| Predicted moral/relational choice | Where relevant |
| Confidence | HIGH/MODERATE/LOW |
| Reconstruction class | R1/R2/R3/R4 |
| Adjudication | Later result |
| Explanation | Why prediction succeeded/failed |

---

# 4. Adjudication vocabulary

Use:

- `SUPPORTED`
- `PARTIALLY_SUPPORTED`
- `NOT_TESTED`
- `DISCONFIRMED`
- `DEVELOPMENTAL_INVALIDATION`
- `NEW_MODIFIER_REQUIRED`

`DEVELOPMENTAL_INVALIDATION` means the prediction used a model of an earlier state but the later character had genuinely changed.

`NEW_MODIFIER_REQUIRED` means the base policy may survive but an unmodeled condition materially changed the response.

---

# 5. Recommended checkpoint structure

## `CP1_POST_E03`

Use E01-E03 only to predict selected E04-E06 behavior classes.

## `CP2_POST_E06`

Use E01-E06 only to predict selected E07-E10 behavior classes.

## `CP3_POST_E10`

Use E01-E10 only to predict selected E11-E13 behavior classes.

## `CP4_POST_E13`

Use TV E01-E13 only to predict selected mundane/relational behavior in Shorts 01-06.

## `CP5_ANIME_NATIVE_FINAL`

After all six shorts and baseline freeze, use A1-only reconstruction for selected supplementary-source premise predictions where feasible.

These checkpoints are recommended anchors. Episode-level outgoing predictions may also be recorded between them.

---

# 6. Prediction register

## CP0 adjudication

`CP0_PRE_E01` contained no predictions by design. E01 therefore has `NO_ADJUDICATION_APPLICABLE`.

## E01 outbound freeze

```yaml
freeze_id: E01_OUTBOUND_FREEZE
frozen: true
allowed_evidence: E01_only
created_before: E02
supplementary_sources_admissible: false
full_checkpoint: false
next_major_checkpoint: CP1_POST_E03
```

| Prediction ID | Freeze | Target condition/domain | Prediction | Confidence | Reconstruction class | Result |
|---|---|---|---|---|---|---|
| `PRED-E01-001` | E01_OUTBOUND | Takina / work and status | Takina will continue prioritizing opportunities that could improve DA evaluation or enable return, even when LycoReco local-help logic initially feels secondary | HIGH | R2 | `NOT_TESTED` |
| `PRED-E01-002` | E01_OUTBOUND | Chisato → Takina goals | Chisato will continue supporting Takina's stated return goal rather than demand that Takina reject DA or imitate Chisato | MODERATE-HIGH | R2 | `NOT_TESTED` |
| `PRED-E01-003` | E01_OUTBOUND | Chisato/Takina operations | conflict will recur around third-party risk, lethal force, and whether personal competence justifies imposed danger | HIGH | R2 | `SUPPORTED` |
| `PRED-E01-004` | E01_OUTBOUND | Takina development | operational rationalism and formal/compressed social style will persist even if social responsiveness expands; growth should not be simple personality replacement | MODERATE | R3 | `SUPPORTED` |
| `PRED-E01-005` | E01_OUTBOUND | Chisato social behavior | rapid informalization and teasing will recur as primary low-stakes social tactics; explicit rejection/severe vulnerability remain unmodeled modifiers | MODERATE-HIGH | R2 | `SUPPORTED` |
| `PRED-E01-006` | E01_OUTBOUND | Chisato violence ethics | life-preservation rule will continue to include enemies unless later evidence qualifies it | HIGH | R2 | `SUPPORTED` |
| `PRED-E01-007` | E01_OUTBOUND | LycoReco information ecology | person-centered local work will again reveal information/opportunities DA overlooks because DA filters by larger security relevance | MODERATE | R3 | `SUPPORTED` |
| `PRED-E01-008` | E01_OUTBOUND | Fuki/Takina | their conflict will continue to involve command authority, Takina's self-authorized judgment, and teammate safety rather than mere personality dislike | MODERATE | R3 | `NOT_TESTED` |
| `PRED-E01-009` | E01_OUTBOUND | Takina humor | further dry/semantic reciprocal teasing will appear once sufficient shared frame exists, before any wholesale loss of baseline formality | LOW-MODERATE | R3 | `SUPPORTED` |
| `PRED-E01-010` | E01_OUTBOUND | Chisato ↔ DA | ethical divergence from DA will continue to coexist with selective cooperation rather than simple institutional rejection | MODERATE-HIGH | R2 | `PARTIALLY_SUPPORTED` |

## E01 outbound adjudication at E02 closeout

| Prediction | E02 adjudication | Explanation |
|---|---|---|
| `PRED-E01-001` | `NOT_TESTED` | DA-return/status priority is not materially revisited. |
| `PRED-E01-002` | `NOT_TESTED` | Chisato does not materially discuss Takina's DA-return goal. |
| `PRED-E01-003` | `SUPPORTED` | serious conflict recurs around lethal authorization, enemy life, mission risk, and team coordination. |
| `PRED-E01-004` | `SUPPORTED` | Takina remains route/mission/rationality oriented while accepting food/play; FLAC shows state-dependent activation without personality replacement. |
| `PRED-E01-005` | `SUPPORTED` | Chisato repeats direct playful invitation and rapid incorporation with Takina and Kurumi. |
| `PRED-E01-006` | `SUPPORTED` | Chisato again preserves/treats enemy life and explicitly says the attackers were only enemies `this time`. |
| `PRED-E01-007` | `SUPPORTED` | the E01 Saori photograph corrects DA's false transaction timeline by three hours. |
| `PRED-E01-008` | `NOT_TESTED` | Fuki/Takina conflict is absent. |
| `PRED-E01-009` | `SUPPORTED` | `映画の見過ぎですね` and related corrections recur within safe shared frames before any wholesale loss of baseline formality. |
| `PRED-E01-010` | `PARTIALLY_SUPPORTED` | ethical divergence from DA-style licensed killing becomes explicit and LycoReco information feeds the DA ecosystem, but direct Chisato↔DA cooperation is not central. |

## E02 outbound freeze

```yaml
freeze_id: E02_OUTBOUND_FREEZE
frozen: true
allowed_evidence: E01-E02_only
created_before: E03
supplementary_sources_admissible: false
full_checkpoint: false
next_major_checkpoint: CP1_POST_E03
```

| Prediction ID | Freeze | Target condition/domain | Prediction | Confidence | Reconstruction class | Result |
|---|---|---|---|---|---|---|
| `PRED-E02-001` | E02_OUTBOUND | Takina / DA status | If DA return or institutional evaluation becomes actionable, Takina will continue to treat it as important rather than behaving as though E02 ordinary-life participation has already replaced that goal. | HIGH | R2 | `SUPPORTED` |
| `PRED-E02-002` | E02_OUTBOUND | Chisato → Takina ordinary life | Chisato will continue using concrete play, food, or shared activity rather than abstract persuasion to draw Takina into ordinary-life participation, often initiating past Takina's first reserve while still leaving room for actual acceptance/refusal. | MODERATE-HIGH | R2 | `NEW_MODIFIER_REQUIRED` |
| `PRED-E02-003` | E02_OUTBOUND | Takina social development | Takina will be able to accept low-stakes social participation without abandoning concise operational/corrective speech; development should remain additive rather than Chisato-like personality replacement. | HIGH | R2 | `SUPPORTED` |
| `PRED-E02-004` | E02_OUTBOUND | Chisato/Takina ethical conflict | A further disagreement over Chisato's life-preservation policy will not automatically rupture cooperation; Takina is likely to argue mission/team consequences directly while continuing to function as partner. | MODERATE-HIGH | R2 | `NOT_TESTED` |
| `PRED-E02-005` | E02_OUTBOUND | Takina failure/accountability | Under a perceived mission failure for which she feels responsible, Takina will tend toward rapid self-accounting/apology rather than blame displacement; Chisato will tend to reduce personal blame where she sees the failure as not Takina's fault. | MODERATE | R3 | `SUPPORTED` |
| `PRED-E02-006` | E02_OUTBOUND | Takina performed state | Urgent protection/threat will produce substantially greater Layer-B acoustic activation in Takina than routine planning/formal speech while her language remains comparatively compressed. | MODERATE | R3 | `NOT_TESTED` |
| `PRED-E02-007` | E02_OUTBOUND | Chisato competence calibration | When Takina is better suited to a concrete task, Chisato will be willing to delegate rather than defend status as the more famous/skilled Lycoris. | LOW-MODERATE | R3 | `NOT_TESTED` |
| `PRED-E02-008` | E02_OUTBOUND | Kurumi / café | Chisato will treat Kurumi's continued presence as ordinary social participation as well as operational utility, while the depth of Kurumi's own belonging remains open. | MODERATE | R3 | `SUPPORTED` |
| `PRED-E02-009` | E02_OUTBOUND | Takina humor | Takina's dry/corrective humor will recur in safe shared frames without requiring Chisato-like flamboyance or wholesale register loss. | LOW-MODERATE | R3 | `PARTIALLY_SUPPORTED` |


## E02 outbound adjudication at E03 closeout

| Prediction | E03 adjudication | Explanation |
|---|---|---|
| `PRED-E02-001` | `SUPPORTED` | DA access immediately reactivates Takina's return pursuit; she conditions leisure on return, seeks Kusunoki, and formally argues for reinstatement. |
| `PRED-E02-002` | `NEW_MODIFIER_REQUIRED` | Concrete activity remains Chisato's ordinary tactic, but severe identity/belonging distress produces explicit verbal affirmation and agency-restoring value articulation in addition to activity invitation. |
| `PRED-E02-003` | `SUPPORTED` | Takina voluntarily joins the cafe gathering without losing concise/formal/corrective speech or DA orientation. |
| `PRED-E02-004` | `NOT_TESTED` | E03 does not center a new Chisato/Takina dispute over life-preservation policy. |
| `PRED-E02-005` | `SUPPORTED` | Takina says `全部 自分のせい`; Chisato reduces over-blame by separating Takina's autonomous rescue motive from institutional sanction. |
| `PRED-E02-006` | `NOT_TESTED` | Mock battle shows very high Layer-B activation, but the frozen condition was urgent protection/threat, not controlled training. |
| `PRED-E02-007` | `NOT_TESTED` | No clean Chisato-to-Takina task delegation occurs in E03. |
| `PRED-E02-008` | `SUPPORTED` | Kurumi functions as both information capability and ordinary board-game/cafe participant. |
| `PRED-E02-009` | `PARTIALLY_SUPPORTED` | Concise corrective/social language persists (`非常識な人ですよ 千束は`), but Layer-C humor quality remains unverified. |

## `CP1_POST_E03`

```yaml
checkpoint_id: CP1_POST_E03
frozen: true
allowed_evidence: E01-E03_only
created_before: E04
supplementary_sources_admissible: false
full_checkpoint: true
next_major_checkpoint: CP2_POST_E06
```

| Prediction ID | Checkpoint | Target condition/domain | Prediction | Confidence | Reconstruction class | Result |
|---|---|---|---|---|---|---|
| `PRED-CP1-001` | CP1_POST_E03 | Takina / DA status | Takina's DA-return desire will remain live until she herself revises it; growing LycoReco participation will coexist with rather than automatically erase it. | HIGH | R2 | `UNTESTED` |
| `PRED-CP1-002` | CP1_POST_E03 | Chisato → Takina goals | Chisato will continue widening Takina's choices without demanding exclusivity; if Takina still wants DA, Chisato will support the option rather than treat it as betrayal. | HIGH | R2 | `UNTESTED` |
| `PRED-CP1-003` | CP1_POST_E03 | Takina / ordinary life | Takina's ordinary-life development will increasingly include self-chosen preferences/actions rather than only accepting activities initiated by Chisato. | MODERATE-HIGH | R3 | `SUPPORTED` |
| `PRED-CP1-004` | CP1_POST_E03 | Chisato / severe vulnerability | Under severe identity/belonging distress, Chisato will shift from ordinary teasing toward direct person-specific affirmation and explicit agency restoration, then return the final decision to the other person. | MODERATE | R3 | `UNTESTED` |
| `PRED-CP1-005` | CP1_POST_E03 | Takina / tactical risk | Takina may continue imposing bounded tactical risk on highly competent partners when she predicts control, including Chisato; later evidence may require a consent/relationship modifier rather than simple disappearance of the policy. | MODERATE-HIGH | R3 | `UNTESTED` |
| `PRED-CP1-006` | CP1_POST_E03 | Takina / performed state | Takina's controlled baseline voice will persist, but threats to belonging/agency and high-intensity combat will widen Layer-B activation substantially. | MODERATE | R3 | `SUPPORTED` |
| `PRED-CP1-007` | CP1_POST_E03 | Fuki/Takina | Fuki/Takina hostility will continue to contain shared history and some mutual recognition rather than becoming pure interpersonal hatred. | MODERATE | R3 | `UNTESTED` |
| `PRED-CP1-008` | CP1_POST_E03 | Erika/Takina | Erika's explicit defense and guilt/awkwardness will create pressure toward direct repair or concern if a safe opportunity appears. | LOW-MODERATE | R3 | `UNTESTED` |
| `PRED-CP1-009` | CP1_POST_E03 | Kurumi / cafe | Kurumi will function simultaneously as information capability and ordinary cafe participant; utility will not exhaust her role in the group. | MODERATE | R3 | `SUPPORTED` |
| `PRED-CP1-010` | CP1_POST_E03 | Chisato ↔ DA | Chisato's DA relationship will remain selective rather than binary: she will use institutional access/cooperation where useful while directly challenging concealment or coercive claims. | MODERATE-HIGH | R2 | `SUPPORTED` |
| `PRED-CP1-011` | CP1_POST_E03 | Chisato/Fuki | Chisato/Fuki interaction will continue to combine combative banter with familiarity and knowledge that would be unlikely between simple enemies. | LOW-MODERATE | R3 | `SUPPORTED` |
| `PRED-CP1-012` | CP1_POST_E03 | Takina / self-authored preference | When Takina is given low-stakes room to choose, E03 predicts a gradual shift from `what restores institutional usefulness?` toward at least some explicit consideration of `what do I want?`, without immediate wholesale value replacement. | MODERATE | R3 | `SUPPORTED` |

## CP1_POST_E03 adjudication at E04 closeout

The twelve CP1 prediction wordings remain exactly as frozen before E04. E04 may update only adjudication fields.

| Prediction | E04 adjudication | Explanation |
|---|---|---|
| `PRED-CP1-001` | `NOT_TESTED` | Takina's DA-return decision is not directly revisited; continued Lycoris role-identification is not equivalent to a tested return choice. |
| `PRED-CP1-002` | `NOT_TESTED` | No new DA-return decision gives Chisato an opportunity to support or oppose it. |
| `PRED-CP1-003` | `SUPPORTED` | Takina generates self-authored ordinary evidence: explicit karinto preference, sustained personal inquiry, and person-specific positive evaluation. |
| `PRED-CP1-004` | `NOT_TESTED` | No severe identity/belonging collapse comparable to E03 occurs. |
| `PRED-CP1-005` | `NOT_TESTED` | No clean new case of Takina imposing tactical risk on a highly competent partner. |
| `PRED-CP1-006` | `PARTIALLY_SUPPORTED` | Controlled baseline persists while social inquiry/laughter expand, but E04 lacks the frozen threat/belonging condition required to test the second clause cleanly. |
| `PRED-CP1-007` | `NOT_TESTED` | Fuki/Takina shared-history hostility is not directly exercised. |
| `PRED-CP1-008` | `NOT_TESTED` | Erika/Takina repair does not appear. |
| `PRED-CP1-009` | `SUPPORTED` | Kurumi simultaneously performs gun-market information work and ordinary cafe/game/bath participation. |
| `PRED-CP1-010` | `NOT_TESTED` | Chisato's personal role boundary is tested, but direct new Chisato↔DA cooperation/concealment confrontation is not. |
| `PRED-CP1-011` | `SUPPORTED` | Chisato/Fuki competitive banter persists and they mirror the same complaint about the game opponent. |
| `PRED-CP1-012` | `SUPPORTED` | E04 directly moves Takina from missing specification/function toward explicit likes, questions, and person-directed judgments. |

## E04 outbound freeze

```yaml
freeze_id: E04_OUTBOUND_FREEZE
frozen: true
allowed_evidence: E01-E04_only
created_before: E05
supplementary_sources_admissible: false
full_checkpoint: false
next_major_checkpoint: CP2_POST_E06
source_native_predictions_frozen_before_v1_comparison: true
```

| Prediction ID | Freeze | Target condition/domain | Prediction | Confidence | Reconstruction class | Result |
|---|---|---|---|---|---|---|
| `PRED-E04-001` | E04_OUTBOUND | Takina / ordinary choice | In unfamiliar civilian-choice domains, Takina will often search for rules/function first, but concrete exposure will increasingly allow explicit personal preference without wholesale loss of operational style. | HIGH | R2 | `NOT_TESTED` |
| `PRED-E04-002` | E04_OUTBOUND | Takina → Chisato | Takina will increasingly initiate personal questions, evaluations, or playful responses toward Chisato rather than remaining a purely reactive recipient of Chisato's social initiative. | MODERATE-HIGH | R3 | `SUPPORTED` |
| `PRED-E04-003` | E04_OUTBOUND | Chisato / role boundary | Chisato will continue treating Lycoris duty as context-bounded rather than a total identity; capability alone will not make her self-deploy in every public-security event. | MODERATE-HIGH | R3 | `NOT_TESTED` |
| `PRED-E04-004` | E04_OUTBOUND | Chisato / life-time ethic | Chisato's life-preservation choices will continue to protect others' future time while permitting forceful nonlethal punishment; generic pacifism should continue to fail as a model. | HIGH | R2 | `SUPPORTED` |
| `PRED-E04-005` | E04_OUTBOUND | Chisato / ordinary experience | Chisato will continue treating finite ordinary experiences as ends worth bounded cost, not merely recovery between missions. | MODERATE | R3 | `SUPPORTED` |
| `PRED-E04-006` | E04_OUTBOUND | Kurumi / cafe | Kurumi will continue combining information work with ordinary cafe/group participation rather than being reduced to hacker utility. | MODERATE-HIGH | R2 | `SUPPORTED` |
| `PRED-E04-007` | E04_OUTBOUND | Yoshimatsu / Alan | Yoshimatsu will continue treating Chisato's exceptional killing aptitude as a purpose that should be realized, creating pressure against Chisato's self-authored ends. | HIGH | R2 | `SUPPORTED` |
| `PRED-E04-008` | E04_OUTBOUND | Majima / information control | Majima will escalate against the hidden-order system specifically because concealment/framing prevents public recognition of his disruption. | HIGH | R2 | `PARTIALLY_SUPPORTED` |
| `PRED-E04-009` | E04_OUTBOUND | DA / epistemic security | DA will continue suppressing or reframing violent incidents to preserve public normality even when that restricts ordinary police/public access to truth. | HIGH | R2 | `SUPPORTED` |
| `PRED-E04-010` | E04_OUTBOUND | Takina / play bandwidth | Takina's controlled baseline will continue to coexist with high-activation laughter or playful response in safe relational frames; vocal expansion should remain state-conditioned rather than global. | MODERATE | R3 | `NOT_TESTED` |



## E04 outbound adjudication at E05 closeout

The ten `E04_OUTBOUND_FREEZE` prediction wordings remain immutable. E05 appends only the following outcomes:

| Prediction | E05 adjudication | Explanation |
|---|---|---|
| `PRED-E04-001` | `NOT_TESTED` | No clean new unfamiliar civilian-choice domain matching the frozen condition. |
| `PRED-E04-002` | `SUPPORTED` | Takina independently pursues artificial-heart information, returns under the stated privacy condition, and supplies specific post-deception repair. |
| `PRED-E04-003` | `NOT_TESTED` | E05 is an assigned protection job, not an unrelated off-duty emergency. |
| `PRED-E04-004` | `SUPPORTED` | Terminality/revenge pressure and lethal threat do not convert Chisato to execution; she remains forceful and nonlethal. |
| `PRED-E04-005` | `SUPPORTED` | Chisato treats the Tokyo tour/guide experience as a substantive end and is personally disappointed when its interpersonal frame proves staged. |
| `PRED-E04-006` | `SUPPORTED` | Kurumi combines ordinary game participation with central technical/intelligence work. |
| `PRED-E04-007` | `SUPPORTED` | Alan life-gift is explicitly paired with mission language and an Alan-linked staged test pressures Chisato toward killing. |
| `PRED-E04-008` | `PARTIALLY_SUPPORTED` | Majima explicitly kills a Lycoris; the E05 killing scene itself does not restate concealment/public-recognition as motive, so the causal link remains longitudinal from E04. |
| `PRED-E04-009` | `SUPPORTED` | The subway attack remains an accident one month later and police describe repeated ordered conversion of incidents into accidents. |
| `PRED-E04-010` | `NOT_TESTED` | E05 has threat activation and private curiosity, not a clean new safe-frame laughter/play event. |

Result distribution: `SUPPORTED` 6; `PARTIALLY_SUPPORTED` 1; `NOT_TESTED` 3; no disconfirmation.

## CP1_POST_E03 cumulative adjudication through E05

`CP1_POST_E03` remains frozen until the E06 closeout creates `CP2_POST_E06`. E05 changes only one previously partial result: `PRED-CP1-006` becomes `SUPPORTED` because immediate protection threat now produces the predicted sharp Layer-B activation jump in Takina (`E05-AUD-006`) while routine/personal speech remains controlled. `PRED-CP1-003`, `PRED-CP1-009`, `PRED-CP1-011`, and `PRED-CP1-012` remain supported; all other CP1 states remain as previously recorded unless their frozen condition was not tested.

## E05 outbound freeze

```yaml
freeze_id: E05_OUTBOUND_FREEZE
frozen: true
allowed_evidence: E01-E05_only
created_before: E06
supplementary_sources_admissible: false
full_checkpoint: false
next_major_checkpoint: CP2_POST_E06
source_native_predictions_frozen_before_v1_comparison: true
```

| Prediction ID | Freeze | Target condition/domain | Prediction | Confidence | Reconstruction class | Result |
|---|---|---|---|---|---|---|
| `PRED-E05-001` | E05_OUTBOUND | Chisato / Alan purpose | If Alan-linked pressure again treats saved life or exceptional talent as an obligation to kill, Chisato will resist donor ownership and define legitimate purpose through self-authored helping rather than obedience. | HIGH | R2 | `UNTESTED` |
| `PRED-E05-002` | E05_OUTBOUND | Chisato / terminality and force | Another person's urgency, suffering, or limited remaining time will motivate assistance but will not by itself authorize revenge execution; Chisato will preserve forceful nonlethal options. | HIGH | R2 | `UNTESTED` |
| `PRED-E05-003` | E05_OUTBOUND | Takina -> Chisato personal inquiry | Takina will continue initiating person-specific questions/verification about Chisato; explicit concrete boundaries will constrain *how* she pursues the information more readily than they extinguish the curiosity itself. | MODERATE-HIGH | R2 | `PARTIALLY_SUPPORTED` |
| `PRED-E05-004` | E05_OUTBOUND | Takina / threat performance | Immediate protection threat will again widen Takina's Layer-B activation sharply relative to routine operational/personal speech without producing a globally expansive baseline. | MODERATE-HIGH | R3 | `SUPPORTED` |
| `PRED-E05-005` | E05_OUTBOUND | Takina / epistemic repair | When a larger story or source proves deceptive, Takina may preserve narrower claims/experiences that remain independently supported rather than treating all associated meaning as false. | LOW-MODERATE | R3 | `UNTESTED` |
| `PRED-E05-006` | E05_OUTBOUND | Kurumi / cafe | Kurumi will continue functioning simultaneously as ordinary group participant and high-value technical/intelligence capability. | HIGH | R2 | `SUPPORTED` |
| `PRED-E05-007` | E05_OUTBOUND | Yoshimatsu / coercion method | Yoshimatsu/Alan pressure will continue to use intermediaries, staged conditions, or indirect manipulation when necessary to push Chisato toward the externally assigned killing purpose. | MODERATE-HIGH | R3 | `SUPPORTED` |
| `PRED-E05-008` | E05_OUTBOUND | DA / epistemic security | DA's hidden-order system will continue prioritizing managed public normality over transparent attribution of violent events, with information compartmentalized across ordinary institutions. | HIGH | R2 | `SUPPORTED` |
| `PRED-E05-009` | E05_OUTBOUND | Majima / Lycoris | Majima's escalation will continue to target Lycoris or the hidden-order apparatus rather than ending with a single isolated Lycoris killing. | HIGH | R2 | `SUPPORTED` |
| `PRED-E05-010` | E05_OUTBOUND | Chisato/Takina bodily permission | In low-stakes private contexts, Chisato may permit increasing nonsexual physical proximity from Takina when the interaction respects an explicit boundary rather than treating proximity itself as forbidden. | LOW-MODERATE | R3 | `UNTESTED` |


## E05 outbound adjudication at E06 closeout

The ten `E05_OUTBOUND_FREEZE` wordings remain exactly as frozen before E06. E06 appends only outcome evidence.

| Prediction | E06 adjudication | Explanation |
|---|---|---|
| `PRED-E05-001` | `NOT_TESTED` | Majima invokes the Alan pendant and asks Chisato's mission, but rescue interrupts before Chisato gives the predicted self-authorship response. |
| `PRED-E05-002` | `NOT_TESTED` | No new terminality/last-wish case asks Chisato to authorize revenge execution. |
| `PRED-E05-003` | `PARTIALLY_SUPPORTED` | Takina continues person-specific verification by modeling Chisato's vulnerability and behavior, but E06 provides no new explicit privacy/refusal boundary comparable to E05. |
| `PRED-E05-004` | `SUPPORTED` | Chisato-targeting urgency and high-intensity rescue again produce major Layer-B activation increases over Takina's controlled routine baseline. |
| `PRED-E05-005` | `NOT_TESTED` | Kurumi's reveal supplies adjacent causal-partition evidence, but the frozen condition specifically requires a deceptive story/source with narrower valid claims. |
| `PRED-E05-006` | `SUPPORTED` | Kurumi simultaneously remains ordinary cafe/game participant and central cyber/intelligence capability. |
| `PRED-E05-007` | `SUPPORTED` | Robota explicitly reports a boss-directed additional Chisato objective through Himegama and engineers Majima's interest using Chisato combat footage. |
| `PRED-E05-008` | `SUPPORTED` | DA withholds information as `極秘`, routes intrusion through ordinary policing, uses Lycoris as bait, and suffers a targeting leak from its own compartmentalized surveillance data. |
| `PRED-E05-009` | `SUPPORTED` | Majima explicitly seeks to destroy DA, continues anti-Lycoris operations, and then selects Chisato as a worthy counterweight. |
| `PRED-E05-010` | `NOT_TESTED` | Shared residence expands domestic proximity, but E06 does not present a new conditional bodily-contact boundary test. |

Result distribution: `SUPPORTED` 5; `PARTIALLY_SUPPORTED` 1; `NOT_TESTED` 4; no disconfirmation.

## CP1_POST_E03 final adjudication at E06 closeout

`CP1_POST_E03` is now closed as the E04-E06 major checkpoint. Its wording remains immutable.

| Prediction | Final CP1 result | Final basis through E06 |
|---|---|---|
| `PRED-CP1-001` | `NOT_TESTED` | Takina's current DA-return preference is not directly revisited after E03. |
| `PRED-CP1-002` | `NOT_TESTED` | No new active DA-return choice tests Chisato's response. |
| `PRED-CP1-003` | `SUPPORTED` | E04 gives independent preference/action generation. |
| `PRED-CP1-004` | `NOT_TESTED` | No second severe identity/belonging collapse tests the E03 modifier. |
| `PRED-CP1-005` | `NOT_TESTED` | No clean later case tests competence-based risk imposed on a partner. |
| `PRED-CP1-006` | `SUPPORTED` | E05 and E06 threat/combat states both sharply widen Takina Layer-B activation. |
| `PRED-CP1-007` | `NOT_TESTED` | Fuki/Takina is not materially revisited. |
| `PRED-CP1-008` | `NOT_TESTED` | Erika/Takina direct repair is not materially revisited. |
| `PRED-CP1-009` | `SUPPORTED` | Kurumi repeatedly remains both ordinary member and technical node through E06. |
| `PRED-CP1-010` | `SUPPORTED` | E06 formal information request -> DA secrecy -> Chisato-sanctioned circumvention demonstrates selective rather than binary DA relation. |
| `PRED-CP1-011` | `SUPPORTED` | E04 Chisato/Fuki interaction confirms combative familiarity. |
| `PRED-CP1-012` | `SUPPORTED` | E04 Takina independently generates low-stakes preference/evaluation. |

Final distribution: `SUPPORTED` 6; `NOT_TESTED` 6; no `DISCONFIRMED` or `DEVELOPMENTAL_INVALIDATION` outcome.

## `CP2_POST_E06`

```yaml
checkpoint_id: CP2_POST_E06
frozen: true
allowed_evidence: E01-E06_only
created_before: E07
supplementary_sources_admissible: false
full_checkpoint: true
next_major_checkpoint: CP3_POST_E10
source_native_predictions_frozen_before_v1_comparison: true
```

| Prediction ID | Checkpoint | Target condition/domain | Prediction | Confidence | Reconstruction class | Result |
|---|---|---|---|---|---|---|
| `PRED-CP2-001` | CP2_POST_E06 | Chisato / Alan assigned purpose | If Alan-linked actors again frame Chisato's saved life or talent as an obligation to kill, Chisato will resist ownership of purpose and preserve a self-authored helping/nonlethal interpretation unless a new coercive modifier removes ordinary choice. | HIGH | R2 | `SUPPORTED` |
| `PRED-CP2-002` | CP2_POST_E06 | Chisato / lethal threat | Even under severe personal danger, Chisato will prefer disabling/nonlethal force when she perceives a viable path; later evidence may qualify this under catastrophic third-party tradeoffs. | HIGH | R2 | `PARTIALLY_SUPPORTED` |
| `PRED-CP2-003` | CP2_POST_E06 | Chisato combat mechanics | Degrading Chisato's visual access to preparatory attack cues will materially reduce her evasion advantage compared with visually legible confrontation. | MODERATE-HIGH | R3 | `UNTESTED` |
| `PRED-CP2-004` | CP2_POST_E06 | Takina / partner threat | A credible threat to Chisato will trigger rapid Takina protective mobilization and substantial Layer-B activation while tactical language remains comparatively concise. | HIGH | R2 | `SUPPORTED` |
| `PRED-CP2-005` | CP2_POST_E06 | Takina / responsibility | When adverse outcomes have multiple causal contributors, Takina will preserve responsibility for her own authored choices rather than scapegoat, while still assigning concrete repair duties to materially involved others. | MODERATE-HIGH | R3 | `UNTESTED` |
| `PRED-CP2-006` | CP2_POST_E06 | Takina / system adaptation | If a recurring low-stakes system is structurally disadvantageous and the mechanism becomes legible, Takina will alter procedure/rules rather than merely repeat the losing strategy or abandon the activity. | MODERATE | R3 | `SUPPORTED` |
| `PRED-CP2-007` | CP2_POST_E06 | Chisato-Takina / closeness and autonomy | Greater private/domestic familiarity will not automatically erase Takina's exit/refusal agency; closeness should continue to permit negotiated boundaries and nonexclusive choices. | HIGH | R2 | `SUPPORTED` |
| `PRED-CP2-008` | CP2_POST_E06 | Takina / force discrimination | When rescue allows precision rather than area suppression, Takina may increasingly exploit her accuracy to disable/nonfatally constrain targets instead of treating vital-point lethality as the only competent option. | LOW-MODERATE | R3 | `UNTESTED` |
| `PRED-CP2-009` | CP2_POST_E06 | Kurumi / group role and repair | Kurumi will continue combining ordinary-group participation with technical/intelligence work, and personal causal involvement will increase rather than end her participation in solving the resulting problem. | HIGH | R2 | `SUPPORTED` |
| `PRED-CP2-010` | CP2_POST_E06 | DA / epistemic security | DA secrecy and compartmentalization will continue to create operational blind spots or downstream risks even while providing real protective capacity; LycoReco actors will selectively use and circumvent the institution rather than simply join or reject it. | HIGH | R2 | `SUPPORTED` |
| `PRED-CP2-011` | CP2_POST_E06 | Majima / Chisato and balance | After selecting Chisato as a worthy counterweight, Majima will continue personalized interest in her while preserving the broader DA/hidden-order conflict; his targeting should not collapse into generic indiscriminate violence alone. | HIGH | R2 | `SUPPORTED` |
| `PRED-CP2-012` | CP2_POST_E06 | Yoshimatsu / coercion architecture | Yoshimatsu/Alan-side actors will continue using proxies, staged incentives, information asymmetry, or third parties when direct commands would expose donor-purpose coercion or invite Chisato's refusal. | MODERATE-HIGH | R2 | `SUPPORTED` |

`CP2_POST_E06` is the current frozen prospective boundary. Do not change these prediction wordings after E07 evidence is opened.


## CP2_POST_E06 adjudication through E07

| Prediction | E07 adjudication | Explanation |
|---|---|---|
| `PRED-CP2-001` | `PARTIALLY_SUPPORTED` | Yoshimatsu directly applies Alan `role` pressure and begins linking Chisato's Lycoris identity/talent to that role; Chisato nevertheless preserves her self-authored helping interpretation of `頂いた時間`. The explicit killing mandate is not completed to Chisato in E07, so the frozen full condition is only partially instantiated. |
| `PRED-CP2-002` | `NOT_TESTED` | No new current lethal-threat confrontation cleanly tests Chisato's nonlethal combat choice. |
| `PRED-CP2-003` | `NOT_TESTED` | No new Chisato fight tests degraded visual access. |
| `PRED-CP2-004` | `NOT_TESTED` | No new direct Chisato threat triggers a Takina rescue/mobilization sequence. |
| `PRED-CP2-005` | `NOT_TESTED` | No new adverse multi-contributor outcome cleanly tests Takina's responsibility partition. |
| `PRED-CP2-006` | `NOT_TESTED` | No recurring structurally disadvantageous low-stakes system becomes newly legible in the sense required by the frozen prediction. |
| `PRED-CP2-007` | `SUPPORTED` | After E06 cohabitation, Takina still refuses optional leisure for independent work and explicitly offers to return to DA when café viability is threatened. Closeness has not erased exit/nonexclusive agency. |
| `PRED-CP2-008` | `NOT_TESTED` | No new rescue-fire/precision-disabling choice occurs. |
| `PRED-CP2-009` | `SUPPORTED` | Kurumi remains ordinary café/game participant and central technical operator, including forged credentials and group infiltration after her E06 causal involvement. |
| `PRED-CP2-010` | `SUPPORTED` | DA's strong AI perimeter forces physical intrusion, but Robota manipulates human command/attention with false incidents; the police-station event is covered publicly and LycoReco/Fuki continue selective information exchange. |
| `PRED-CP2-011` | `SUPPORTED` | Majima identifies Chisato as the old-tower opponent, calls their renewed collision fate, asks about her mission, and simultaneously continues the broader DA intrusion/escalation plan. |
| `PRED-CP2-012` | `SUPPORTED` | Yoshimatsu moves coercion through Mika and then directly attempts to recruit Takina as someone who should understand Chisato's proper `居場所`. |

E07 incremental CP2 state:

- `SUPPORTED`: 5
- `PARTIALLY_SUPPORTED`: 1
- `NOT_TESTED`: 6
- `DISCONFIRMED`: 0
- `NEW_MODIFIER_REQUIRED`: 0

CP2 remains open through E10.

## E07 outbound freeze

```yaml
freeze_id: E07_OUTBOUND_FREEZE
frozen: true
allowed_evidence: E01-E07_only
created_before: E08
supplementary_sources_admissible: false
full_checkpoint: false
parent_checkpoint: CP2_POST_E06
next_major_checkpoint: CP3_POST_E10
source_native_predictions_frozen_before_v1_comparison: true
```

| Prediction ID | Freeze | Target condition/domain | Prediction | Confidence | Reconstruction class | Result |
|---|---|---|---|---|---|---|
| `PRED-E07-001` | E07_OUTBOUND | Chisato / Yoshimatsu | Because Chisato currently understands Yoshimatsu primarily as the benefactor who gave her time, she will seek/accept continued personal contact or gratitude unless his coercive killing mandate becomes sufficiently explicit to force model revision. | MODERATE-HIGH | R3 | `UNTESTED` |
| `PRED-E07-002` | E07_OUTBOUND | Takina / Yoshimatsu placement claim | If Yoshimatsu's claim that Chisato's `居場所` is elsewhere becomes actionable, Takina will not automatically treat donor/talent teleology as overriding Chisato's present wishes; however, her own institutional-place history may make the claim psychologically salient. | MODERATE | R3 | `UNTESTED` |
| `PRED-E07-003` | E07_OUTBOUND | Chisato / Mika secrecy | After the current promise-context repair, Chisato will preserve ordinary trust with Mika rather than punish him for the past concealment; a new concealment that directly constrains her current agency remains an open modifier. | MODERATE-HIGH | R3 | `UNTESTED` |
| `PRED-E07-004` | E07_OUTBOUND | Mika / Yoshimatsu | Mika will continue resisting Yoshimatsu's instrumentalization of Chisato but will have difficulty directly harming or emotionally severing Yoshimatsu because E07 demonstrates absent lethal resolve despite explicit conflict. | HIGH | R2 | `UNTESTED` |
| `PRED-E07-005` | E07_OUTBOUND | Takina / DA and LycoReco | Takina's growing LycoReco integration will continue to coexist with rather than erase DA-linked options until she herself explicitly revises them; practical duty may still activate institutional-return language. | HIGH | R2 | `UNTESTED` |
| `PRED-E07-006` | E07_OUTBOUND | Chisato–Takina / lethal ethics | The pair's lethal/nonlethal disagreement will remain available under real stakes without automatically rupturing partnership; Takina has not yet adopted Chisato's universal anti-killing rule. | HIGH | R2 | `UNTESTED` |
| `PRED-E07-007` | E07_OUTBOUND | Majima / visibility escalation | Because the police-station assault was again concealed, Majima will escalate toward a more publicly undeniable action while retaining personalized interest in Chisato. | HIGH | R2 | `UNTESTED` |
| `PRED-E07-008` | E07_OUTBOUND | DA / cyber-organizational attack | Robota's new physical foothold plus human-command manipulation will produce a deeper DA information/coordination compromise; technical strength alone will not remove the institutional vulnerability. | HIGH | R2 | `UNTESTED` |
| `PRED-E07-009` | E07_OUTBOUND | Kurumi / counter-technical role | Kurumi will remain the LycoReco group's principal means of diagnosing or countering the evolving DA/Robota information conflict while continuing ordinary group participation. | HIGH | R2 | `UNTESTED` |
| `PRED-E07-010` | E07_OUTBOUND | Chisato / identity after revelation | Chisato will continue ordinary helping/café behavior after learning more about her rescue rather than allowing Alan-origin biography alone to replace her present self-authored vocation. | MODERATE-HIGH | R2 | `UNTESTED` |

`E07_OUTBOUND_FREEZE` is now the current episode-level prospective boundary. `CP2_POST_E06` remains the governing major checkpoint through E10.


## E07 outbound adjudication at E08 closeout

| Prediction | E08 adjudication | Explanation |
|---|---|---|
| `PRED-E07-001` | `PARTIALLY_SUPPORTED` | Chisato continues wanting Yoshimatsu to return, invokes their promise, and defends him against Majima's Alan accusation. Direct new Chisato↔Yoshimatsu contact does not occur. |
| `PRED-E07-002` | `NOT_TESTED` | Yoshimatsu's E07 claim about Chisato's `居場所` is not directly made actionable through Takina in E08. |
| `PRED-E07-003` | `SUPPORTED` | Chisato preserves ordinary trust in Mika after E07 and asks him to confirm her Yoshimatsu interpretation rather than punishing him for past concealment. |
| `PRED-E07-004` | `NOT_TESTED` | E08 escalates Yoshimatsu's coercion and ends with blame directed at Mika, but does not yet show Mika making a new direct harm/severance decision. |
| `PRED-E07-005` | `PARTIALLY_SUPPORTED` | Takina's LycoReco integration becomes materially stronger through stewardship, but E08 does not directly reactivate or revise her DA-return option. |
| `PRED-E07-006` | `SUPPORTED` | Chisato remains nonlethal while Takina mobilizes with her ordinary firearm against Majima; partnership remains intact and no universal anti-killing conversion occurs. |
| `PRED-E07-007` | `NOT_TESTED` | Majima deepens personalized Chisato contact, but E08 does not yet execute a new publicly undeniable visibility attack. |
| `PRED-E07-008` | `NOT_TESTED` | No new deeper Radiata/DA coordination compromise is completed in E08. |
| `PRED-E07-009` | `PARTIALLY_SUPPORTED` | Kurumi remains an ordinary participant and technical/economic collaborator, but the specific DA/Robota counter-conflict is not the focus of E08. |
| `PRED-E07-010` | `SUPPORTED` | Chisato continues café work, teaching, Halloween outreach, helping, and self-authored nonlethal identity after learning more about Alan/Yoshimatsu. |

E07 outbound E08 tranche:

- `SUPPORTED`: 3
- `PARTIALLY_SUPPORTED`: 3
- `NOT_TESTED`: 4
- `DISCONFIRMED`: 0
- `NEW_MODIFIER_REQUIRED`: 0

## CP2_POST_E06 adjudication through E08

| Prediction | E08 update | Current CP2 result |
|---|---|---|
| `PRED-CP2-001` | Yoshimatsu explicitly denies role choice; Majima tells Chisato Alan can support killing; Chisato reasserts `私は やりたいようにやります`; proxy coercion then removes ordinary choice. | `SUPPORTED` |
| `PRED-CP2-002` | Chisato remains nonlethal/non-escalatory in an armed Majima encounter, but no clean active disabling-force choice is required. | `PARTIALLY_SUPPORTED` |
| `PRED-CP2-003` | No new degraded-vision test. | `NOT_TESTED` |
| `PRED-CP2-004` | Takina rapidly mobilizes armed when Chisato is under credible threat and then creates high-activation security rules. | `SUPPORTED` |
| `PRED-CP2-005` | No new multi-contributor adverse outcome cleanly tests responsibility partition. | `NOT_TESTED` |
| `PRED-CP2-006` | Café deficit becomes legible and Takina systematically changes cost, labor, menu, automation, and investment procedure rather than repeating the losing system. | `SUPPORTED` |
| `PRED-CP2-007` | Takina continues independent initiative/boundaries; `同棲` play is bounded rather than treated as obligation. | `SUPPORTED` |
| `PRED-CP2-008` | Takina fires at Majima, but retained evidence does not establish deliberate nonvital discrimination. | `NOT_TESTED` |
| `PRED-CP2-009` | Kurumi remains ordinary café participant plus technical/economic collaborator. | `SUPPORTED` |
| `PRED-CP2-010` | E08 offers little new DA-secrecy evidence; prior support remains controlling. | `SUPPORTED` |
| `PRED-CP2-011` | Majima personally visits Chisato, shares old-tower history/media interests, and preserves the counterweight framing. | `SUPPORTED` |
| `PRED-CP2-012` | Himegama uses trusted medical access and information asymmetry to incapacitate Chisato on Yoshimatsu's side. | `SUPPORTED` |

CP2 cumulative state through E08:

- `SUPPORTED`: 8
- `PARTIALLY_SUPPORTED`: 1
- `NOT_TESTED`: 3
- `DISCONFIRMED`: 0
- `NEW_MODIFIER_REQUIRED`: 0

CP2 remains open through E10.

## E08 outbound freeze

```yaml
freeze_id: E08_OUTBOUND_FREEZE
frozen: true
allowed_evidence: E01-E08_only
created_before: E09
supplementary_sources_admissible: false
full_checkpoint: false
parent_checkpoint: CP2_POST_E06
next_major_checkpoint: CP3_POST_E10
source_native_predictions_frozen_before_v1_comparison: true
```

| Prediction ID | Freeze | Target condition/domain | Prediction | Confidence | Reconstruction class | Result |
|---|---|---|---|---|---|---|
| `PRED-E08-001` | E08_OUTBOUND | Chisato / Alan betrayal evidence | If direct evidence links Yoshimatsu/Alan to coercion against her rather than merely Majima's accusation, Chisato's gratitude narrative will come under acute pressure; she is likely to distinguish the value she gave the rescue from the coercer's claimed purpose rather than simply accept killing destiny. | HIGH | R2 | `UNTESTED` |
| `PRED-E08-002` | E08_OUTBOUND | Takina / Chisato nonresponse | If Chisato violates an expected check-in/medical/safety routine under ambiguous danger, Takina will escalate quickly from contact attempts to physical search/intervention using explicit protocol rather than wait passively. | HIGH | R2 | `UNTESTED` |
| `PRED-E08-003` | E08_OUTBOUND | Takina / LycoReco stewardship | Takina will continue directing operational/administrative competence toward preserving LycoReco or Chisato-valued ordinary life without requiring an immediate verbal declaration that DA no longer matters. | HIGH | R2 | `UNTESTED` |
| `PRED-E08-004` | E08_OUTBOUND | Takina / ordinary-life agency | Takina will continue generating or revising civilian solutions based on self-authored goals and newly learned social criteria rather than functioning only as a recipient of Chisato's invitations. | MODERATE-HIGH | R3 | `UNTESTED` |
| `PRED-E08-005` | E08_OUTBOUND | Chisato–Takina / care grammar | Under nonterminal everyday stress, Takina will tend to express care through concrete rules/maintenance while Chisato will often translate those acts into personal or domestic relational meaning; this difference should remain compatible rather than automatically conflictual. | MODERATE-HIGH | R3 | `UNTESTED` |
| `PRED-E08-006` | E08_OUTBOUND | Chisato / bodily control | Threats that bypass Chisato's perceptual evasion through trusted access, immobilization, or unavoidable bodily intervention will be more effective than visually legible frontal attacks even without greater raw combat capability. | HIGH | R2 | `UNTESTED` |
| `PRED-E08-007` | E08_OUTBOUND | Chisato / Majima moral comparison | Shared interests or anti-determinist language may permit temporary commonality with Majima, but Chisato will continue rejecting moral equivalence so long as Majima's self-authorship authorizes killing. | HIGH | R2 | `UNTESTED` |
| `PRED-E08-008` | E08_OUTBOUND | Mika / Yoshimatsu coercion | Yoshimatsu's escalation against Chisato will increase pressure on Mika's divided loyalties; Mika may preserve protective secrecy or hesitation, but direct harm to Chisato will make continued nonconfrontation progressively harder to sustain. | MODERATE-HIGH | R3 | `UNTESTED` |
| `PRED-E08-009` | E08_OUTBOUND | Yoshimatsu / proxies | Alan-side coercion will continue to use intermediaries, trusted routines, or staged constraints to move Chisato toward the killing role rather than relying on transparent consent. | HIGH | R2 | `UNTESTED` |
| `PRED-E08-010` | E08_OUTBOUND | Chisato–Takina / place and belonging | Takina's practical investment in Chisato's important place will continue to deepen person-specific attachment even if explicit self-labeling of LycoReco as Takina's permanent home remains delayed or conditional. | MODERATE | R3 | `UNTESTED` |

`E08_OUTBOUND_FREEZE` is now the current episode-level prospective boundary. `CP2_POST_E06` remains the governing major checkpoint through E10.



## E08 outbound adjudication at E09 closeout

| Prediction | E09 adjudication | Explanation |
|---|---|---|
| `PRED-E08-001` | `NOT_TESTED` | The audience gains strong evidence of Yoshimatsu/Alan's coercive history, but Chisato herself is not shown receiving direct proof that Yoshimatsu ordered or authorized the heart attack. Her gratitude model therefore has not yet faced the frozen condition. |
| `PRED-E08-002` | `SUPPORTED` | Chisato's unexplained nonresponse to the medical/check-in routine produces immediate Takina physical search and armed intervention at the clinic. |
| `PRED-E08-003` | `PARTIALLY_SUPPORTED` | Takina's person-directed stewardship continues through prognosis-aware field monitoring and her effort to preserve Chisato's life; E09 is less about maintaining LycoReco's administrative ordinary-life system than E08, so the exact frozen domain is only partially instantiated. |
| `PRED-E08-004` | `SUPPORTED` | Takina independently designs a civilian outing around Chisato and impending separation, using her own planning style rather than merely receiving Chisato's invitation. |
| `PRED-E08-005` | `NOT_TESTED` | The frozen condition specified nonterminal everyday stress. E09 care occurs under explicit terminal knowledge, so the behavior is informative but not a clean test of the prediction as written. |
| `PRED-E08-006` | `NOT_TESTED` | E09 confirms the serious consequence of the already-completed E08 trusted-access attack, but it does not introduce a new post-freeze threat of the specified class. |
| `PRED-E08-007` | `NOT_TESTED` | Chisato and Majima do not interact in E09. |
| `PRED-E08-008` | `SUPPORTED` | Direct harm to Chisato produces Mika's guilt, disclosure of the Yoshimatsu history under pressure, and an attempted call/contact with Yoshimatsu; continued nonconfrontation is becoming harder to sustain. |
| `PRED-E08-009` | `NOT_TESTED` | E09 reveals historical proxy recruitment of Mika and present consequences of Himegama's E08 action, but no new post-freeze Alan coercive operation cleanly tests `will continue`. |
| `PRED-E08-010` | `SUPPORTED` | Takina's person-specific attachment deepens through the planned day, prognosis-aware care, and DA return chosen to save Chisato; she still does not explicitly declare LycoReco her permanent home. |

E08 outbound E09 tranche:

- `SUPPORTED`: 4
- `PARTIALLY_SUPPORTED`: 1
- `NOT_TESTED`: 5
- `DISCONFIRMED`: 0
- `NEW_MODIFIER_REQUIRED`: 0

## CP2_POST_E06 adjudication through E09

| Prediction | E09 update | Current CP2 result |
|---|---|---|
| `PRED-CP2-001` | Chisato again preserves her self-authored role against Kusunoki and flashback establishes Alan's intended killing teleology, but present Chisato still lacks direct knowledge tying Yoshimatsu to the current coercive attack. | `SUPPORTED` |
| `PRED-CP2-002` | Chisato is incapacitated during the direct attack and E09 does not provide a new severe-threat combat choice. | `PARTIALLY_SUPPORTED` |
| `PRED-CP2-003` | No new combat test of degraded visual access. | `NOT_TESTED` |
| `PRED-CP2-004` | Chisato's disappearance/credible danger triggers rapid Takina protective mobilization and high Layer-B activation with concise language. | `SUPPORTED` |
| `PRED-CP2-005` | No clean new multi-contributor responsibility dispute for Takina. | `NOT_TESTED` |
| `PRED-CP2-006` | The outing contains plan disruption, but Chisato rather than Takina is the principal agent of procedural reinterpretation; do not overfit. | `SUPPORTED` |
| `PRED-CP2-007` | Takina chooses DA return and physical separation while the relationship remains intact; Chisato explicitly authorizes the move. | `SUPPORTED` |
| `PRED-CP2-008` | Takina fires at Himegama but E09 does not cleanly establish a precision nonvital rescue choice. | `NOT_TESTED` |
| `PRED-CP2-009` | Kurumi shifts from scrubbed digital evidence to human-source investigation and continues working for Chisato's repair. | `SUPPORTED` |
| `PRED-CP2-010` | Chisato rejects DA role ownership but selectively bargains with DA for Takina; Takina then uses DA's operation as a means toward Chisato's survival. | `SUPPORTED` |
| `PRED-CP2-011` | Majima's interest in Chisato leads him to identify and physically approach Yoshimatsu while his larger operational trajectory continues. | `SUPPORTED` |
| `PRED-CP2-012` | E09 flashback supplies historical evidence that Yoshimatsu recruited Mika through a private promise to cultivate Chisato's talent; present Himegama coercion remains part of the same architecture. | `SUPPORTED` |

CP2 cumulative state through E09:

- `SUPPORTED`: 8
- `PARTIALLY_SUPPORTED`: 1
- `NOT_TESTED`: 3
- `DISCONFIRMED`: 0
- `NEW_MODIFIER_REQUIRED`: 0

CP2 remains open through E10.

## E09 outbound freeze

```yaml
freeze_id: E09_OUTBOUND_FREEZE
frozen: true
allowed_evidence: E01-E09_only
created_before: E10
supplementary_sources_admissible: false
full_checkpoint: false
parent_checkpoint: CP2_POST_E06
next_major_checkpoint: CP3_POST_E10
source_native_predictions_frozen_before_v1_comparison: true
```

| Prediction ID | Freeze | Target condition/domain | Prediction | Confidence | Reconstruction class | Result |
|---|---|---|---|---|---|---|
| `PRED-E09-001` | E09_OUTBOUND | Takina / DA return | Once back inside DA, Takina will prioritize leads/actions that improve Chisato's survival chances over the symbolic prestige of reinstatement; institutional access will function primarily as a means unless later evidence restores DA as an end in itself. | HIGH | R2 | `SUPPORTED` |
| `PRED-E09-002` | E09_OUTBOUND | Chisato–Takina / separation | Physical/institutional separation will not by itself rupture the relationship: Chisato will continue treating Takina's DA choice as legitimate, and Takina will retain person-specific concern/action toward Chisato across the separation. | HIGH | R2 | `SUPPORTED` |
| `PRED-E09-003` | E09_OUTBOUND | Chisato / mortality | While physically capable, Chisato will continue spending remaining time on ordinary/helping activity rather than reorganizing her identity around medical withdrawal; severe deterioration remains an open modifier. | HIGH | R2 | `SUPPORTED` |
| `PRED-E09-004` | E09_OUTBOUND | Chisato / Yoshimatsu betrayal | If Chisato receives direct evidence that Yoshimatsu's Alan project caused or endorsed the current coercion, gratitude will come under acute pressure, but she will preserve the self-authored `救世主`/helping meaning as hers rather than accepting the intended killing role. | HIGH | R2 | `SUPPORTED` |
| `PRED-E09-005` | E09_OUTBOUND | Takina / lethal ethics | A direct path to Himegama or another actor responsible for Chisato's heart damage can still activate Takina's willingness to use lethal force; closeness with Chisato has not erased this policy. | MODERATE-HIGH | R2 | `NOT_TESTED` |
| `PRED-E09-006` | E09_OUTBOUND | Takina / performed state | Chisato-threatening emergencies will continue to produce strong Layer-B activation, while deliberate high-stakes rescue decisions may remain acoustically controlled; importance should not be modeled as one-dimensional loudness/pitch expansion. | HIGH | R2 | `SUPPORTED` |
| `PRED-E09-007` | E09_OUTBOUND | Mika / Yoshimatsu | After direct harm to Chisato, Mika will move toward more active confrontation or protective intervention against Yoshimatsu even if attachment/guilt prevents emotionally simple severance. | HIGH | R2 | `PARTIALLY_SUPPORTED` |
| `PRED-E09-008` | E09_OUTBOUND | Kurumi / Alan investigation | Kurumi will continue combining technical investigation with human/contextual inference when Alan's digital traces are scrubbed, especially where that can create a repair path for Chisato. | MODERATE-HIGH | R3 | `SUPPORTED` |
| `PRED-E09-009` | E09_OUTBOUND | Majima / Yoshimatsu | Majima's direct approach to Yoshimatsu will intersect the Alan/Chisato conflict without automatically making Majima an Alan subordinate; any cooperation should remain bounded by Majima's independent balance/anti-DA aims. | MODERATE-HIGH | R3 | `SUPPORTED` |
| `PRED-E09-010` | E09_OUTBOUND | DA / Takina agency | Takina will selectively use DA's information, mobility, or authority for Chisato-related ends and may resist or redirect institutional priorities if they block the perceived rescue path; full open defection is not yet predicted. | MODERATE-HIGH | R3 | `SUPPORTED` |

`E09_OUTBOUND_FREEZE` is now the current episode-level prospective boundary. `CP2_POST_E06` remains the governing major checkpoint through E10.

## E09 outbound adjudication at E10 closeout

| Prediction | E10 adjudication | Explanation |
|---|---|---|
| `PRED-E09-001` | `SUPPORTED` | Takina uses DA interrogation and the Majima operation to pursue Alan/Yoshimatsu for Chisato; she explicitly tells Majima that she is not interested in him as the endpoint. |
| `PRED-E09-002` | `SUPPORTED` | Institutional separation does not rupture the relationship: Chisato preserves Takina's future options and later entrusts Enkuboku to Takina/Fuki, while Takina's DA activity remains Chisato-directed. |
| `PRED-E09-003` | `SUPPORTED` | Chisato remains active while physically capable: she closes LycoReco on her own terms, engages patrons and Mika, and then chooses a new helping/rescue action rather than medical withdrawal. |
| `PRED-E09-004` | `SUPPORTED` | Mika directly reveals Yoshimatsu's bargain to raise Chisato as the strongest killer; Chisato preserves her self-authored savior/helping meaning and gratitude while refusing donor-purpose ownership. |
| `PRED-E09-005` | `NOT_TESTED` | Himegama or another direct actor responsible for the heart damage is not placed in Takina's reach. Her severe coercion of a captured intermediary does not instantiate the frozen condition. |
| `PRED-E09-006` | `SUPPORTED` | `待ちなさい！` produces very high Layer-B activation, while deliberate Yoshimatsu-location questions return toward a controlled pitch center despite equally serious stakes. |
| `PRED-E09-007` | `PARTIALLY_SUPPORTED` | Mika breaks concealment and moves into active protective intervention, but E10 ends before direct confrontation *against* Yoshimatsu; he is presently helping Chisato rescue him. |
| `PRED-E09-008` | `SUPPORTED` | Kurumi's opening research combines technical paper-tracing with contextual inference about undocumented Lycoris and illicit human testing in pursuit of the artificial-heart repair/origin path. |
| `PRED-E09-009` | `SUPPORTED` | Majima directly engages Yoshimatsu, rejects Alan as another hidden-order actor, threatens him, and remains independent rather than becoming an Alan subordinate. |
| `PRED-E09-010` | `SUPPORTED` | Takina selectively uses DA access for Yoshimatsu/Chisato ends and explicitly deprioritizes Majima as the object of her own concern. |

E09 outbound E10 tranche:

- `SUPPORTED`: 8
- `PARTIALLY_SUPPORTED`: 1
- `NOT_TESTED`: 1
- `DISCONFIRMED`: 0
- `NEW_MODIFIER_REQUIRED`: 0

## CP2_POST_E06 final adjudication at E10 closeout

E10 is the terminal source window for `CP2_POST_E06`. No frozen CP2 wording is altered.

| Prediction | E10 final update | Final CP2 result |
|---|---|---|
| `PRED-CP2-001` | Mika's confession directly gives Chisato the Yoshimatsu killing-purpose bargain; she answers with explicit self-authorship rather than accepting assigned purpose. | `SUPPORTED` |
| `PRED-CP2-002` | E10 provides no new severe-threat Chisato combat choice; the prior partially supported state remains the correct terminal adjudication. | `PARTIALLY_SUPPORTED` |
| `PRED-CP2-003` | No clean E10 combat test degrades Chisato's visual access. | `NOT_TESTED` |
| `PRED-CP2-004` | Takina's Chisato-directed operational focus persists; E10 also preserves the previously validated threat-activation model. | `SUPPORTED` |
| `PRED-CP2-005` | No clean E10 multi-contributor adverse-outcome responsibility dispute instantiates the frozen condition. | `NOT_TESTED` |
| `PRED-CP2-006` | No contradictory low-stakes system evidence appears; the previously supported adaptation policy remains valid. | `SUPPORTED` |
| `PRED-CP2-007` | DA separation and Chisato's group dispersal preserve exit/nonexclusive choice while relationship continuity remains intact. | `SUPPORTED` |
| `PRED-CP2-008` | Takina uses deliberately bounded nonlethal coercion in interrogation, but not the frozen precision-rescue condition; do not convert a near miss into a test. | `NOT_TESTED` |
| `PRED-CP2-009` | Kurumi continues technical/contextual investigation of Chisato's heart history before accepting Chisato's request to move on. | `SUPPORTED` |
| `PRED-CP2-010` | Majima directly weaponizes DA secrecy; Chisato/Takina continue selective use rather than binary institutional acceptance/rejection. | `SUPPORTED` |
| `PRED-CP2-011` | Majima's Chisato/Yoshimatsu interest remains nested inside the broader anti-DA/hidden-order project. | `SUPPORTED` |
| `PRED-CP2-012` | Yoshimatsu admits responsibility for Chisato's divergence and reasserts sacrificial Alan purpose while proxy/staged coercion remains active. | `SUPPORTED` |

Final `CP2_POST_E06` outcome:

- `SUPPORTED`: 8
- `PARTIALLY_SUPPORTED`: 1
- `NOT_TESTED`: 3
- `DISCONFIRMED`: 0
- `NEW_MODIFIER_REQUIRED`: 0

`CP2_POST_E06` is now **CLOSED**. The three `NOT_TESTED` items remain genuine untested conditions rather than inferred successes.

## `CP3_POST_E10` — frozen full checkpoint

```yaml
checkpoint_id: CP3_POST_E10
frozen: true
allowed_evidence: E01-E10_only
created_before: E11
supplementary_sources_admissible: false
full_checkpoint: true
next_major_checkpoint: CP4_POST_E13
source_native_predictions_frozen_before_v1_comparison: true
```

| Prediction ID | Checkpoint | Target condition/domain | Prediction | Confidence | Reconstruction class | Result |
|---|---|---|---|---|---|---|
| `PRED-CP3-001` | CP3_POST_E10 | Chisato / Yoshimatsu hostage | If Yoshimatsu remains under immediate threat, Chisato will resist treating him as expendable because of his coercive intent and will seek a rescue/direct-answer path; preserving his life will not imply accepting his killing-purpose claim. | HIGH | R2 | `UNTESTED` |
| `PRED-CP3-002` | CP3_POST_E10 | Chisato / direct Yoshimatsu confrontation | If Chisato receives a direct answer from Yoshimatsu about his intended purpose, she will preserve the distinction between gratitude for received life and ownership of its meaning; she is unlikely to accept donor intent as binding vocation. | HIGH | R2 | `UNTESTED` |
| `PRED-CP3-003` | CP3_POST_E10 | Mika / Yoshimatsu | Mika will act more directly to protect Chisato within the Yoshimatsu crisis than he did before E09, but attachment/guilt may complicate lethal severance or emotionally simple opposition. | HIGH | R2 | `UNTESTED` |
| `PRED-CP3-004` | CP3_POST_E10 | Takina / DA and Chisato rescue | While DA access remains useful, Takina will continue prioritizing actions that improve Chisato's survival or reach Yoshimatsu over reinstatement prestige; if institutional priorities block that path, she is likely to redirect/resist before simply surrendering the person-specific objective. | HIGH | R2 | `UNTESTED` |
| `PRED-CP3-005` | CP3_POST_E10 | Takina / lethal force | Credible immediate danger to Chisato will continue to permit severe or lethal-force willingness in Takina; closeness has not converted her into Chisato's universal nonlethal doctrine. | MODERATE-HIGH | R2 | `UNTESTED` |
| `PRED-CP3-006` | CP3_POST_E10 | Chisato-Takina / crisis reunion | Institutional or physical separation will not require relational reauthorization before cooperation: under acute crisis, the pair should be able to resume person-specific coordination rapidly while retaining distinct tactical/moral styles. | HIGH | R2 | `UNTESTED` |
| `PRED-CP3-007` | CP3_POST_E10 | Takina / performed state | Chisato-critical emergencies will continue to produce large Layer-B activation spikes, but deliberate tactical/rescue decisions may remain acoustically compressed; semantic importance will not map monotonically to F0 or intensity. | HIGH | R2 | `UNTESTED` |
| `PRED-CP3-008` | CP3_POST_E10 | DA / public exposure | The public-gun/Lycoris-exposure crisis will force a sharper conflict between secrecy preservation and immediate protection; DA information-control rules are likely to constrain or complicate otherwise straightforward protective action. | HIGH | R2 | `UNTESTED` |
| `PRED-CP3-009` | CP3_POST_E10 | Majima / balance and civilian exposure | Majima will preserve independent anti-DA/balance aims rather than become subordinate to Alan; even when his plans intersect Chisato, he is likely to continue treating public exposure and imposed choice as legitimate tools. | HIGH | R2 | `UNTESTED` |
| `PRED-CP3-010` | CP3_POST_E10 | Yoshimatsu / coercion | Yoshimatsu/Alan-side coercion will continue to prefer staged constraints, hostages, proxies, or sacrificial pressure over transparent consent, and Yoshimatsu's own life may remain expendable to the talent-purpose ideal. | HIGH | R2 | `UNTESTED` |
| `PRED-CP3-011` | CP3_POST_E10 | Chisato / mortality and agency | While physically capable, Chisato will continue using finite time for helping, relationship, and self-chosen action rather than reorganizing herself around passive medical withdrawal; severe physiological collapse remains an explicit modifier. | HIGH | R2 | `UNTESTED` |
| `PRED-CP3-012` | CP3_POST_E10 | Chisato / distributed competence | When trusted peers can cover a macro/public-security task, Chisato will be willing to entrust it to them rather than insist on sole-hero status, especially when a person-specific rescue requires her attention. | MODERATE-HIGH | R3 | `UNTESTED` |

`CP3_POST_E10` is frozen before V1 comparison and before E11 evidence. Do not edit these prediction wordings after E11 is opened.

## E11 adjudication of `CP3_POST_E10` — first tranche

Prediction wording remains immutable.

| Prediction | E11 adjudication | Explanation |
|---|---|---|
| `PRED-CP3-001` | `SUPPORTED` | Chisato enters the old tower to save Yoshimatsu and accepts tactical vulnerability rather than treat him as expendable. |
| `PRED-CP3-002` | `NOT_TESTED` | Majima interrupts before Chisato obtains a substantive direct Yoshimatsu answer about intended purpose. |
| `PRED-CP3-003` | `PARTIALLY_SUPPORTED` | Mika accompanies Chisato, questions solo entry, and supports her departure; direct Yoshimatsu-facing protective confrontation remains untested. |
| `PRED-CP3-004` | `SUPPORTED` | Takina accepts permanent loss of DA return because `ここでは千束を救えない`. |
| `PRED-CP3-005` | `SUPPORTED` | Takina enters the Chisato/Majima firefight with severe/live-force willingness intact. |
| `PRED-CP3-006` | `SUPPORTED` | Crisis cooperation resumes immediately on Takina's arrival without relational renegotiation. |
| `PRED-CP3-007` | `SUPPORTED` | Chisato-critical emergency produces large activation while consequential decision lines remain acoustically heterogeneous. |
| `PRED-CP3-008` | `SUPPORTED` | Public Lycoris identification forces firing restriction during active danger, making secrecy an operational constraint. |
| `PRED-CP3-009` | `SUPPORTED` | Majima continues independent anti-DA exposure, anti-Alan action, and imposed-choice tactics. |
| `PRED-CP3-010` | `NOT_TESTED` | Immediate hostage control is Majima's; current Alan-side staged self-sacrifice is not cleanly tested. |
| `PRED-CP3-011` | `SUPPORTED` | Chisato continues active rescue/helping under terminal prognosis and bodily danger. |
| `PRED-CP3-012` | `SUPPORTED` | Chisato continues entrusting macro public defense to peers while taking the Yoshimatsu-specific task. |

E11 CP3 tranche: `9 SUPPORTED / 1 PARTIALLY_SUPPORTED / 2 NOT_TESTED / 0 DISCONFIRMED`. CP3 remains open through E13.

## `E11_OUTBOUND_FREEZE`

```yaml
freeze_id: E11_OUTBOUND_FREEZE
frozen: true
allowed_evidence: E01-E11_only
created_before: E12
supplementary_sources_admissible: false
full_checkpoint: false
governing_major_checkpoint: CP3_POST_E10
source_native_predictions_frozen_before_v1_comparison: true
```

| Prediction ID | Freeze | Target condition/domain | Prediction | Confidence | Reconstruction class | Result |
|---|---|---|---|---|---|---|
| `PRED-E11-001` | E11_OUTBOUND | Chisato / Yoshimatsu purpose | If Yoshimatsu directly presses Chisato to accept killing as the meaning of the life/heart she received, Chisato will refuse the vocation while preserving the distinction between his personhood, her gratitude, and his coercive ideology. | HIGH | R2 | `UNTESTED` |
| `PRED-E11-002` | E11_OUTBOUND | Chisato / sensory disadvantage | If low visibility or physiological impairment continues, Chisato's evasion advantage will degrade materially; she is likely to seek environmental, tactical, or partner compensation rather than become inexplicably invulnerable. | HIGH | R2 | `UNTESTED` |
| `PRED-E11-003` | E11_OUTBOUND | Takina / Chisato crisis | Having accepted loss of DA return, Takina will continue prioritizing immediate Chisato rescue over restoring institutional standing and will not require DA authorization for that objective. | HIGH | R2 | `UNTESTED` |
| `PRED-E11-004` | E11_OUTBOUND | Takina / force | Direct threats to Chisato will continue to permit severe/live-force action from Takina even while Chisato's own nonlethal rule remains distinct. | HIGH | R2 | `UNTESTED` |
| `PRED-E11-005` | E11_OUTBOUND | Chisato-Takina / crisis coordination | The pair will rapidly resume complementary tactical coordination after reunion without treating prior institutional separation as relational rupture; value differences may remain visible inside that cooperation. | HIGH | R2 | `UNTESTED` |
| `PRED-E11-006` | E11_OUTBOUND | Mika / Yoshimatsu | If Chisato cannot safely resolve the Yoshimatsu/Alan crisis herself, Mika will face increased pressure toward direct protective action; attachment and guilt will make any lethal severance emotionally/morally non-simple. | MODERATE-HIGH | R3 | `UNTESTED` |
| `PRED-E11-007` | E11_OUTBOUND | Kurumi/Mizuki / rescue | Kurumi and Mizuki's voluntary return will produce concrete informational/logistical contribution to the heart-rescue problem rather than remaining a sentimental reversal only. | HIGH | R2 | `UNTESTED` |
| `PRED-E11-008` | E11_OUTBOUND | Fuki/Erika/Takina | Fuki and/or Erika will remain capable of practical support for Takina despite her institutional defection; E11's permission/apology makes simple betrayal treatment less likely. | MODERATE | R3 | `UNTESTED` |
| `PRED-E11-009` | E11_OUTBOUND | Majima / ideology | Majima will continue treating anti-coercion/balance as justification for imposed violent methods; Chisato will continue rejecting moral equivalence even where their anti-assigned-purpose language overlaps. | HIGH | R2 | `UNTESTED` |
| `PRED-E11-010` | E11_OUTBOUND | DA / exposure | DA will attempt to contain or reinterpret the public Lycoris exposure, but embodied witnesses and visible violence will make restoration of the pre-exposure epistemic status quo materially harder than an ordinary cover story. | HIGH | R2 | `UNTESTED` |


## E11 outbound adjudication at E12 closeout

Prediction wording remains immutable.

| Prediction | E12 adjudication | Explanation |
|---|---|---|
| `PRED-E11-001` | `SUPPORTED` | Yoshimatsu directly defines killing/world contribution as Chisato's happiness and purpose; Chisato refuses while later preserving gratitude and his life. |
| `PRED-E11-002` | `NOT_TESTED` | E12 does not make renewed low-visibility or comparable sensory-degradation mechanics a diagnostic condition. |
| `PRED-E11-003` | `SUPPORTED` | Takina states she left DA and continues the heart-rescue objective without seeking renewed authorization or status. |
| `PRED-E11-004` | `SUPPORTED` | Takina threatens Yoshimatsu, tries to kill/extract the heart, and remains severe/live-force capable under Chisato-critical stakes. |
| `PRED-E11-005` | `SUPPORTED` | The pair coordinate immediately after reunion and continue functioning after their maximum-stakes disagreement over killing Yoshimatsu. |
| `PRED-E11-006` | `PARTIALLY_SUPPORTED` | Mika helps route Kusunoki's covert rescue and is absent on a separate task, but E12 proper still withholds the decisive direct Yoshimatsu-facing protective act; ending-credit imagery is not used to import E13 outcome. |
| `PRED-E11-007` | `SUPPORTED` | Kurumi/Mizuki supply heart intelligence, helicopter/logistics, control-room route, Robota attribution, police tip, Radiata takeover, and media-cover capability. |
| `PRED-E11-008` | `SUPPORTED` | Fuki/Erika preserve practical continuity with Takina; Erika explicitly fills her role and Fuki's earlier permission remains operative. |
| `PRED-E11-009` | `NOT_TESTED` | Majima reappears in the cliffhanger but supplies no new E12 ideological justification sufficient to test the anti-coercion/balance proposition. |
| `PRED-E11-010` | `SUPPORTED` | Public exposure is reabsorbed only through large-scale technical/media narrative reclassification after Radiata restoration; ordinary simple cover is insufficient. |

E11→E12 outcome: `7 SUPPORTED / 1 PARTIALLY_SUPPORTED / 2 NOT_TESTED / 0 DISCONFIRMED`.

## E12 adjudication of `CP3_POST_E10` — second tranche

The twelve CP3 prediction wordings remain immutable.

| Prediction | E12 adjudication | Explanation |
|---|---|---|
| `PRED-CP3-001` | `SUPPORTED` | Chisato preserves wounded Yoshimatsu despite direct coercion and rejects his purpose claim. |
| `PRED-CP3-002` | `SUPPORTED` | Direct Yoshimatsu answer arrives; Chisato cleanly separates gratitude from binding vocation. |
| `PRED-CP3-003` | `PARTIALLY_SUPPORTED` | Mika participates in covert rescue routing with Kusunoki, but direct Yoshimatsu-facing severance remains outside the E12 narrative boundary. |
| `PRED-CP3-004` | `SUPPORTED` | Takina's DA exit is explicit and Chisato rescue remains primary. |
| `PRED-CP3-005` | `SUPPORTED` | Takina remains willing to use severe/lethal force for Chisato's survival. |
| `PRED-CP3-006` | `SUPPORTED` | Reunion produces immediate coordination; even severe value conflict does not require relational reauthorization. |
| `PRED-CP3-007` | `SUPPORTED` | E12 supplies extreme threat spikes plus quiet high-importance attachment/decision lines. |
| `PRED-CP3-008` | `SUPPORTED` | Exposure forces LilyBell liquidation, firing/command changes, Radiata restoration, and multi-layer cover. |
| `PRED-CP3-009` | `NOT_TESTED` | Majima returns only at the cliffhanger; no new ideological statement is admitted. |
| `PRED-CP3-010` | `SUPPORTED` | Yoshimatsu literally makes his own implanted heart/life the staged constraint intended to force Chisato into killing. |
| `PRED-CP3-011` | `SUPPORTED` | Chisato remains active in rescue, coalition coordination, and institutional intervention under terminal prognosis. |
| `PRED-CP3-012` | `SUPPORTED` | Chisato relies on Takina, Fuki, Kurumi, Mika, Mizuki, and others rather than assuming sole-hero responsibility. |

Cumulative `CP3_POST_E10` status through E12: `11 SUPPORTED / 1 PARTIALLY_SUPPORTED / 0 cumulatively NOT_TESTED / 0 DISCONFIRMED`. `PRED-CP3-009` remains cumulatively supported from E11 despite not being newly tested in E12. CP3 remains open through E13.

## `E12_OUTBOUND_FREEZE`

```yaml
freeze_id: E12_OUTBOUND_FREEZE
frozen: true
allowed_evidence: E01-E12_only
created_before: E13
supplementary_sources_admissible: false
full_checkpoint: false
governing_major_checkpoint: CP3_POST_E10
source_native_predictions_frozen_before_v1_comparison: true
```

| Prediction ID | Freeze | Target condition/domain | Prediction | Confidence | Reconstruction class | Result |
|---|---|---|---|---|---|---|
| `PRED-E12-001` | E12_OUTBOUND | Chisato / Majima endgame | If the renewed direct Majima confrontation continues, Chisato will reject his coercive/balance logic and is likely to preserve her life-preserving/nonlethal boundary rather than convert terminal anger into revenge killing; severe physiological collapse remains a modifier. | HIGH | R2 | `UNTESTED` |
| `PRED-E12-002` | E12_OUTBOUND | Takina / Chisato threat | If Takina perceives Chisato in acute Majima-related danger, she will rapidly prioritize re-entry/rescue without waiting for DA authorization; Layer-B activation is likely to widen sharply under immediate threat. | HIGH | R2 | `UNTESTED` |
| `PRED-E12-003` | E12_OUTBOUND | Chisato-Takina / post-Yoshimatsu conflict | The maximum-stakes disagreement over killing Yoshimatsu will not produce relational rupture; the pair should remain capable of cooperation and person-specific care while retaining distinct lethal ethics. | HIGH | R2 | `UNTESTED` |
| `PRED-E12-004` | E12_OUTBOUND | Mika / Yoshimatsu | If the unresolved Yoshimatsu crisis requires direct intervention, Mika will move toward protective action for Chisato, but his shared history, guilt, and attachment will make lethal severance or its aftermath morally/emotionally non-simple. | MODERATE-HIGH | R3 | `UNTESTED` |
| `PRED-E12-005` | E12_OUTBOUND | Chisato / survival and identity | Chisato will resist any survival route that requires treating Yoshimatsu as expendable or accepting the assigned killing vocation; she can accept rescue/medical help when it does not require that constitutive self-betrayal. | HIGH | R2 | `UNTESTED` |
| `PRED-E12-006` | E12_OUTBOUND | Kurumi / crisis integration | Kurumi's dual technical/social role will continue to produce concrete post-crisis or survival-related coordination rather than reverting to utility-only participation. | MODERATE-HIGH | R3 | `UNTESTED` |
| `PRED-E12-007` | E12_OUTBOUND | Kusunoki/DA/LycoReco | Kusunoki and LycoReco will remain capable of selective cooperation after the exposure crisis and Takina's defection; institutional secrecy concerns will persist, but simple binary expulsion/enmity is unlikely. | MODERATE-HIGH | R3 | `UNTESTED` |
| `PRED-E12-008` | E12_OUTBOUND | ordinary life / post-crisis orientation | If the immediate lethal crisis resolves sufficiently, ordinary/shared activity will reappear as a substantive end rather than mere reward decoration; Chisato's finite-time ethic predicts renewed investment in lived experience. | MODERATE-HIGH | R3 | `UNTESTED` |
| `PRED-E12-009` | E12_OUTBOUND | Fuki-Erika-Takina | DA peer relationships will survive Takina's institutional exit in modified form; practical support, repair, or familiar conflict is more likely than simple social severance. | MODERATE | R3 | `UNTESTED` |
| `PRED-E12-010` | E12_OUTBOUND | Takina / performed attachment | Takina's person-specific attachment will continue to span both extreme threat activation and comparatively controlled explicit care/decision speech; semantic importance will not map monotonically to acoustic intensity. | HIGH | R2 | `UNTESTED` |

`E12_OUTBOUND_FREEZE` is frozen from E01-E12 evidence only and before any V1 comparison or E13 evidence. Do not edit its prediction wording after E13 is opened.



## E12 outbound adjudication at E13 closeout

Prediction wording remains immutable.

| Prediction | E13 adjudication | Explanation |
|---|---|---|
| `PRED-E12-001` | `SUPPORTED` | Chisato continues the Majima endgame without revenge killing, rejects his balance logic, and preserves aim discrimination even with lethal-capable ammunition imposed on her; Majima survives. |
| `PRED-E12-002` | `SUPPORTED` | Takina rapidly re-enters when Chisato is in acute Majima danger, with very high Layer-B activation on `千束～！` and the rescue sequence. |
| `PRED-E12-003` | `SUPPORTED` | The Yoshimatsu killing dispute does not rupture the pair; E13 shows immediate rescue, later search/reunion, play, explicit partnership, and future planning. |
| `PRED-E12-004` | `SUPPORTED` | Mika directly confronts Yoshimatsu for Chisato and crosses the protective-severance threshold; exact lethal mechanism is withheld, and the aftermath remains entangled with love, guilt, concealment, and co-parent history. |
| `PRED-E12-005` | `SUPPORTED` | Chisato accepts the replacement-heart rescue once it no longer requires her to kill Yoshimatsu or adopt his vocation; survival is accepted without constitutive self-betrayal. |
| `PRED-E12-006` | `SUPPORTED` | Kurumi remains both technical rescuer and ordinary ensemble member: she coordinates surgery/heart information, shares Mika's secret, and continues into the mobile LycoReco future. |
| `PRED-E12-007` | `SUPPORTED` | Kusunoki resumes selective operational contact with the mobile LycoReco ensemble after the exposure crisis; secrecy/friction persist, but binary institutional enmity does not emerge. |
| `PRED-E12-008` | `SUPPORTED` | Ordinary/shared life returns as a substantive end: beach recovery, renewed joking/play, future planning, and the Hawaii food-truck LycoReco all foreground lived experience rather than mere victory reward. |
| `PRED-E12-009` | `PARTIALLY_SUPPORTED` | Fuki's tie to Takina clearly survives institutional exit (`たきなは？` and familiar post-crisis continuity), but E13 supplies no equally direct new Erika/Takina post-exit interaction beyond the repair already established in E11-E12. |
| `PRED-E12-010` | `SUPPORTED` | Takina spans extreme crisis activation, controlled explicit care (`元気そうで何よりです`, `あなたは死にません`), high-energy safe banter, and restrained future advice; semantic importance remains non-monotonic with acoustic intensity. |

E12→E13 outcome: `9 SUPPORTED / 1 PARTIALLY_SUPPORTED / 0 NOT_TESTED / 0 DISCONFIRMED`.

## E13 adjudication and closure of `CP3_POST_E10`

The twelve CP3 prediction wordings remain immutable. E13 is the final TV test tranche.

| Prediction | E13 adjudication | Explanation |
|---|---|---|
| `PRED-CP3-001` | `SUPPORTED` | The Yoshimatsu crisis resolves without Chisato treating him as expendable or accepting his killing-purpose claim. |
| `PRED-CP3-002` | `SUPPORTED` | Chisato's final treatment of the Alan gift preserves gratitude while refusing donor ownership; she later discards the recovered Alan token without rejecting the life or relationships enabled by the gift. |
| `PRED-CP3-003` | `SUPPORTED` | Mika directly crosses the Yoshimatsu-facing protective threshold for Chisato; exact lethal mechanics remain off-screen, and the aftermath is morally/emotionally non-simple. |
| `PRED-CP3-004` | `SUPPORTED` | Takina remains outside DA and organizes action around Chisato rather than reinstatement prestige. |
| `PRED-CP3-005` | `SUPPORTED` | Takina's severe-force willingness remains available in Chisato-critical crisis; E13 does not convert her into Chisato's universal nonlethal doctrine. |
| `PRED-CP3-006` | `SUPPORTED` | The pair resume and sustain cooperation without relational reauthorization, including crisis rescue and post-crisis reunion. |
| `PRED-CP3-007` | `SUPPORTED` | E13 again shows enormous Chisato-threat activation alongside much quieter care/future statements and high-energy safe play. |
| `PRED-CP3-008` | `SUPPORTED` | DA's post-exposure order is managed through large-scale reality reclassification and institutional coordination rather than restoration of literal pre-exposure ignorance. |
| `PRED-CP3-009` | `SUPPORTED` | Majima explicitly restates his independent balance ideology, claims conditional allegiance to the weaker side, survives, and remains outside Alan subordination. |
| `PRED-CP3-010` | `SUPPORTED` | Yoshimatsu's own life remains expendable to the talent-purpose ideal through the heart coercion already established, and he dies without retracting the teleology. |
| `PRED-CP3-011` | `SUPPORTED` | Chisato continues choosing action, relationships, ordinary experience, and future possibility rather than passive medical withdrawal. |
| `PRED-CP3-012` | `SUPPORTED` | Distributed competence is explicit in Takina/Fuki task division and the broader ensemble rescue/aftermath structure. |

Final `CP3_POST_E10` outcome:

- `SUPPORTED`: 12
- `PARTIALLY_SUPPORTED`: 0
- `NOT_TESTED`: 0
- `DISCONFIRMED`: 0
- `NEW_MODIFIER_REQUIRED`: 0

`CP3_POST_E10` is now **CLOSED** at the TV E13 boundary.

## `CP4_POST_E13` — frozen TV-only checkpoint for Shorts 01-06

```yaml
checkpoint_id: CP4_POST_E13
frozen: true
allowed_evidence: TV_E01-E13_only
created_before: SHORT01
supplementary_sources_admissible: false
full_checkpoint: true
next_major_checkpoint: CP5_ANIME_NATIVE_FINAL
source_native_predictions_frozen_before_v1_comparison: true
```

| Prediction ID | Checkpoint | Target condition/domain | Prediction | Confidence | Reconstruction class | Result |
|---|---|---|---|---|---|---|
| `PRED-CP4-001` | CP4_POST_E13 | Chisato / ordinary-life invitation | In low-stakes ordinary contexts, Chisato will continue creating participation through concrete play, food, errands, or shared activity more often than abstract instruction; severe vulnerability remains a modifier that can shift her toward direct affirmation. | HIGH | R2 | `NOT_TESTED` |
| `PRED-CP4-002` | CP4_POST_E13 | Takina / ordinary-life register | Takina's concise/corrective baseline will persist while she voluntarily joins or initiates ordinary activity; development should remain additive rather than Chisato-like personality replacement. | HIGH | R2 | `SUPPORTED` |
| `PRED-CP4-003` | CP4_POST_E13 | Chisato-Takina / low-stakes reciprocity | Teasing, corrections, and physical/playful interaction will remain reciprocal, and either partner will retain the ability to refuse, reshape, or exit an activity without relational rupture or captivity. | HIGH | R2 | `SUPPORTED` |
| `PRED-CP4-004` | CP4_POST_E13 | Takina / care channel | Takina will continue expressing strong person-specific care through practical/procedural forms such as monitoring, scheduling, maintenance, problem-solving, or direct intervention, without requiring explicit affective labeling. | MODERATE-HIGH | R2 | `NOT_TESTED` |
| `PRED-CP4-005` | CP4_POST_E13 | Takina / civilian initiative | Takina will originate at least some civilian preference, plan, or ordinary action rather than functioning only as a respondent to Chisato's initiatives. | MODERATE-HIGH | R3 | `SUPPORTED` |
| `PRED-CP4-006` | CP4_POST_E13 | Chisato / influence without ownership | Chisato will continue widening other people's options through invitations and encouragement rather than demanding exclusivity; refusal/exit agency should remain available in low-stakes interaction. | HIGH | R2 | `NOT_TESTED` |
| `PRED-CP4-007` | CP4_POST_E13 | Kurumi / ensemble role | Kurumi will continue combining technical/information competence with ordinary, playful, or socially embedded café participation; utility will not exhaust her membership. | MODERATE-HIGH | R2 | `PARTIALLY_SUPPORTED` |
| `PRED-CP4-008` | CP4_POST_E13 | Mika / everyday fatherhood | Mika's everyday father/mentor/café-caregiver role will remain behaviorally active alongside operational seriousness; protective information withholding may recur as a modifier rather than disappear. | MODERATE | R3 | `PARTIALLY_SUPPORTED` |
| `PRED-CP4-009` | CP4_POST_E13 | Mizuki / everyday register | Mizuki's adult-romance/social banter will recur in ordinary ensemble contexts without erasing her operational competence or loyalty. | MODERATE | R3 | `PARTIALLY_SUPPORTED` |
| `PRED-CP4-010` | CP4_POST_E13 | LycoReco / ordinary institution | Mundane food, work, errands, customer help, and shared leisure will continue functioning as substantive relational infrastructure rather than mere downtime between security plots. | HIGH | R2 | `SUPPORTED` |
| `PRED-CP4-011` | CP4_POST_E13 | Takina / performed state | Takina will be capable of comparatively controlled explicit care and high-activation safe play within the same ordinary-life horizon; acoustic intensity will remain non-monotonic with semantic/relational importance. | MODERATE-HIGH | R3 | `SUPPORTED` |
| `PRED-CP4-012` | CP4_POST_E13 | Chisato-Takina / physical permission and autonomy | Broad physical and ordinary-life permissions will continue while distinct styles, boundaries, and autonomous choice remain visible; no exclusive or explicitly romantic status should be inferred unless a short supplies direct warrant. | HIGH | R2 | `SUPPORTED` |

`CP4_POST_E13` is frozen from TV E01-E13 evidence only. No Short 01-06, V1 retrospective synthesis, or supplementary narrative evidence was admitted when these predictions were formulated.


## CP4 adjudication after Short 01

The twelve `CP4_POST_E13` prediction wordings remain immutable. Short 01 is the first of six mundane/relational validation tranches.

| Prediction | Short 01 adjudication | Explanation |
|---|---|---|
| `PRED-CP4-001` | `NOT_TESTED` | Chisato is active in ordinary work, but Short 01 does not cleanly test her drawing another person into a new activity through invitation. |
| `PRED-CP4-002` | `SUPPORTED` | Takina retains concise procedural/corrective speech while proactively managing supplies, articulating profitability, and proposing a civilian expansion. |
| `PRED-CP4-003` | `SUPPORTED` | correction, teasing and physical pursuit remain reciprocal; Takina resists Chisato's disarm attempt without relational rupture. |
| `PRED-CP4-004` | `NOT_TESTED` | procedural stewardship is strong, but the short does not make it sufficiently person-specific to test the predicted care channel cleanly. |
| `PRED-CP4-005` | `SUPPORTED` | Takina independently proposes weekly repetition and yakitori for the next event. |
| `PRED-CP4-006` | `NOT_TESTED` | no clean new Chisato invitation/refusal structure tests influence-without-ownership. |
| `PRED-CP4-007` | `PARTIALLY_SUPPORTED` | Kurumi is plainly socially embedded and playful; her technical role is not tested in this short. |
| `PRED-CP4-008` | `PARTIALLY_SUPPORTED` | Mika's food/cafe-caregiver role is direct; operational seriousness/protective withholding is not tested. |
| `PRED-CP4-009` | `PARTIALLY_SUPPORTED` | Mizuki's adult social/drinking/karaoke register is direct; operational competence is not tested. |
| `PRED-CP4-010` | `SUPPORTED` | seasonal food/drink service, inventory, customer work and group leisure are the entire dramatic substance of the short. |
| `PRED-CP4-011` | `SUPPORTED` | controlled Takina business/preference speech coexists with substantially more activated safe civilian initiative. |
| `PRED-CP4-012` | `SUPPORTED` | broad ordinary/physical permission and reciprocal resistance coexist with distinct styles; no explicit romantic/exclusive status is supplied. |

Short 01 CP4 tranche: `6 SUPPORTED / 3 PARTIALLY_SUPPORTED / 3 NOT_TESTED / 0 DISCONFIRMED`.

`CP4_POST_E13` remains **OPEN** through Short 06.

## `SHORT01_OUTBOUND_FREEZE`

```yaml
freeze_id: SHORT01_OUTBOUND_FREEZE
frozen: true
allowed_evidence: TV_E01-E13_plus_SHORT01_only
created_before: SHORT02
supplementary_sources_admissible: false
full_checkpoint: false
governing_major_checkpoint: CP4_POST_E13
source_native_predictions_frozen_before_v1_comparison: true
```

| Prediction ID | Freeze | Target condition/domain | Prediction | Confidence | Reconstruction class | Result |
|---|---|---|---|---|---|---|
| `PRED-SHORT01-001` | SHORT01_OUTBOUND | Takina / civilian initiative | In another low-stakes ordinary context, Takina will remain capable of proactively optimizing, extending, or proposing civilian activity rather than only complying with plans authored by Chisato or Mika. | HIGH | R2 | `UNTESTED` |
| `PRED-SHORT01-002` | SHORT01_OUTBOUND | Takina / operational habit in mundane context | If an ordinary setting presents a safety, logistics, or control problem, Takina may still default toward competence-based or overprepared operational solutions; civilian integration should modify context and purpose rather than erase that grammar. | MODERATE-HIGH | R3 | `UNTESTED` |
| `PRED-SHORT01-003` | SHORT01_OUTBOUND | Chisato-Takina / low-stakes correction | A mundane disagreement or mismatch will remain compatible with teasing, resistance, correction, or physical reshaping without relational rupture or fused agency. | HIGH | R2 | `UNTESTED` |
| `PRED-SHORT01-004` | SHORT01_OUTBOUND | Chisato / role-context boundary | When Takina foregrounds operational capability in an ordinary context where Chisato sees it as inappropriate or excessive, Chisato is likely to challenge the context/use rather than demand loss of competence itself. | MODERATE | R3 | `UNTESTED` |
| `PRED-SHORT01-005` | SHORT01_OUTBOUND | Takina / performed state | Safe civilian initiative, play, or competitive enthusiasm can produce Layer-B activation materially above Takina's controlled planning/explanatory baseline; high activation will remain non-exclusive to threat. | MODERATE-HIGH | R3 | `UNTESTED` |
| `PRED-SHORT01-006` | SHORT01_OUTBOUND | LycoReco / ordinary institution | Food, service, maintenance, errands, seasonal activity, or customer interaction will continue to carry genuine character/relationship content rather than function as empty intermission. | HIGH | R2 | `UNTESTED` |
| `PRED-SHORT01-007` | SHORT01_OUTBOUND | ensemble / utility versus membership | At least one supporting cafe member will again be allowed a comic, leisure, or caregiving role whose value is not exhausted by security/technical utility. | MODERATE-HIGH | R3 | `UNTESTED` |
| `PRED-SHORT01-008` | SHORT01_OUTBOUND | Takina / preference grammar | Takina's ordinary preferences or proposals may remain practical, causal, competitive, or efficiency-oriented rather than converging on Chisato's pleasure vocabulary; additive development should preserve that distinctness. | MODERATE-HIGH | R3 | `UNTESTED` |

`SHORT01_OUTBOUND_FREEZE` is frozen from TV E01-E13 + Short 01 evidence only. No Short 02-06, V1 retrospective synthesis, or supplementary narrative evidence was admitted when these predictions were formulated.

# 7. What to predict

Prefer behavior classes:

- social initiative;
- action/refusal;
- emotional direction;
- register shift;
- humor/play response;
- conflict/repair;
- moral choice;
- relationship adaptation.

Avoid easy plot guessing.

Bad:

> “Chisato will go to the aquarium.”

Better:

> “If Chisato encounters Takina lacking a civilian preference vocabulary, the current model predicts that she will try to create participation through concrete activity rather than abstract instruction.”

The latter tests a generative policy.

---

# 8. Freeze discipline

Once a prediction checkpoint is frozen:

- do not edit its prediction wording after opening the target source;
- append adjudication separately;
- do not improve a prediction retroactively;
- preserve low-confidence predictions and failures;
- distinguish source surprise from analytical failure.

---

# 9. Supplementary-source prediction protocol

After the anime-native baseline freezes, a supplementary story may be prospectively tested only when its premise can be obtained without revealing the behavioral resolution.

If premise-only separation is impossible, skip the prospective test rather than pretending blindness.

---

# 10. Current authority statement

All earlier freezes remain immutable in prediction wording. `CP2_POST_E06` and `CP3_POST_E10` are closed; CP3 finished the TV run at twelve supported, zero partially supported, zero not tested, and zero disconfirmed. `CP4_POST_E13` remains the governing major checkpoint and is open through Short 06; after Short 01 its cumulative state is six supported, three partially supported, and three not tested. `SHORT01_OUTBOUND_FREEZE` is the current episode-level freeze and was created before Short 02 evidence and before Short 01 V1 retrospective comparison.
