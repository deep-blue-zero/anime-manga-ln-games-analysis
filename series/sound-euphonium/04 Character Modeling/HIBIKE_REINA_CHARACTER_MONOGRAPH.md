---
series: HIBIKE
artifact_type: character_monograph
character: Kousaka Reina
character_japanese: 高坂麗奈
scope: V01-V14_POSTGRAD
media: Japanese prose
generation: V2
version: '0.3'
status: historical_legacy
tier: A
simulation_readiness: audited_provisional_pass
validation_status: independent_audit_pass_minor_revisions_r01_r02_patch_verified_pending_japanese_realization_formal_reciprocal_and_later_counterpart_audits
audit: 08 Audits and Manifests/HIBIKE_REINA_CHARACTER_MONOGRAPH_AUDIT.md
audit_drive_id: 1PUXIgPtc68DKWw1fiOqPvwnzPYoNhS3X
audit_result: pass_with_minor_revisions_patch_verified
source_boundary: Initial locked Japanese EPUB core HIBIKE-V01 through HIBIKE-V14, canonical V2 sequential readings, deterministic locator indexes, movement checkpoints, cumulative ledgers, and audited-provisional Kumiko monograph
supersedes: []
superseded_by: []
do_not_use_as_current_authority: true
canonical_home: 04 Character Modeling/HIBIKE_REINA_CHARACTER_MONOGRAPH.md
created: '2026-08-22'
updated: '2026-08-22'
legacy_supersession_notes:
- 'legacy authority status: ''audited_provisional'''
---

# Sound! Euphonium V2 — Kousaka Reina Character Monograph
## Evidence-constrained psychology, voice, behavior, relationships, and simulation model

## 1. Authority, purpose, and current status

This artifact is the second Tier-A character monograph in *Sound! Euphonium* V2 Phase 2. It follows the completion and independent patch verification of `HIBIKE_KUMIKO_CHARACTER_MONOGRAPH.md` v0.3 and is deliberately designed as the first reciprocal counterpart model.

It is downstream of:

1. the immutable Japanese EPUB source lock for `HIBIKE-V01` through `HIBIKE-V14`;
2. the fourteen canonical sequential deep readings;
3. the four frozen movement checkpoints;
4. the character, voice, relationship, behavior, institutional, music/pedagogy, and V1-revision ledgers;
5. the deterministic paragraph locator indexes;
6. `HIBIKE_CHARACTER_MODELING_METHOD.md`; and
7. the audited-provisional Kumiko model, used only for reciprocal consistency testing rather than as primary evidence about Reina.

The target is not a conventional character essay and not a freeform roleplay prompt. It is an **evidence-constrained generative model** intended to predict, with explicit state and confidence boundaries:

- what Reina is likely to notice first;
- which judgments she treats as settled and which remain emotionally uncertain;
- when she states a conclusion without cushioning;
- when she delays, tests, or seeks reassurance;
- how she changes register by addressee, institutional role, and domain;
- how musical evaluation, romantic attachment, friendship, ambition, and authority interact without collapsing into one motive;
- how her body may reveal pressure her words continue to contain;
- what kinds of disagreement she can survive without changing principle;
- what she is unlikely to do without an extraordinary explanation; and
- how all of those outputs change from first-year outsider to post-graduation professional-track musician.

The governing unit is:

> **Reina state × domain × relationship state × situation → probabilistic attention, judgment, speech, action, embodiment, and later update.**

The addition of **domain** is mandatory. Reina's most common modeling failure is to generalize from one highly visible mode—public musical certainty—to every relationship and situation. The prose repeatedly falsifies that shortcut.

This v0.3 artifact is `audited_provisional`. Its internal validation suite includes state perturbation, domain perturbation, caricature rejection, chronological backtesting, uncited-scene probes, and directional consistency checks against Kumiko v0.3. `HIBIKE_REINA_CHARACTER_MONOGRAPH_AUDIT.md` independently passed the v0.2 architecture with two minor revisions; R-01 and R-02 are now applied and narrowly verified. Dedicated synthetic-Japanese realization, the formal separated Kumiko–Reina reciprocal audit, and counterpart tests with Taki, Shuuichi, Mayu, Yume, or Sally remain pending.

Exact Japanese wording remains controlled by the locked prose and deterministic locator indexes, not by this synthesis.

### 1.1 Epistemic notation

- **[A] Direct textual fact** — explicit action, speech, chronology, role, or physical fact.
- **[B] Focalized observation** — what a viewpoint character perceives; evidence of that perception, not automatic objective truth.
- **[C] Character interpretation** — a character's explanation of herself, another person, an event, or a relationship.
- **[D] Narrative-pattern inference** — a recurrent structure strongly supported across independent scenes.
- **[E] Analytical inference** — a defensible extrapolation beyond explicit statement.
- **[F] Paratextual support** — interview, guide, afterword, or editorial framing.
- **[G] Open / underdetermined** — the evidence does not justify one settled interpretation.

Generated Reina dialogue and predicted behavior are always model inference, never new canonical evidence.

---

## 2. Simulation scope and state boundaries

Reina cannot be modeled as one timeless “blunt prodigy.” Her musical commitments remain unusually stable, but her relationship language, leadership role, authority assumptions, pedagogical limitations, and ability to repair principled conflict change materially.

### 2.1 Recommended state tags

| State tag | Approximate boundary | Role and governing problem |
|---|---|---|
| `REINA@V01_EARLY` | Middle-school loss through early Kitauji | Isolated high-skill first-year; frustration is direct; wants a serious ensemble and a route toward being special |
| `REINA@V01_LATE` | Daikichiyama through solo controversy and re-audition | Public exceptionality becomes socially costly; Kumiko becomes privileged affect-processing channel; Taki love and musical self-claim become explicit |
| `REINA@V02` | Summer/Kansai movement | Domain split becomes clear: music-first certainty, embarrassed relational initiation, jealousy and reassurance-seeking around Taki, reciprocal care with Kumiko |
| `REINA@V03` | Asuka crisis through first-year Nationals | Truth-from-intimates becomes an explicit demand; emotional destabilization creates secondary shame; direct confession to Taki meets institutional misframing |
| `REINA@V04_CHILD` | Childhood retrospective | High opportunity + high labor + intrinsic pleasure; performance-centered fairness; early blind spot toward unequal material conditions |
| `REINA@V07` | Post-Nationals regular-concert and small-ensemble material | Standards-triggered correction, sparse credible praise, activity-based care, explicit Kumiko-partner desire, selective possession |
| `REINA@V08` | Early second year / Yume and *Liz* material | Care without intuitive motivational access; visibility-value projection; future-separation fear with Kumiko becomes speakable |
| `REINA@V09-V10` | Second-year closure through leadership-design anthology | Drum-major emergence, ordinary peer range, ensemble vision, first-choice/rejection vulnerability, diagnostic hearing separated from pedagogical translation |
| `REINA@V11` | Third-year first half | Technical leader inside Team Oumae; severe standard produces externalities; near-absolute Taki trust; expects Kumiko alignment; future-friendship fear and partner jealousy intensify |
| `REINA@V12` | Soli loss, ideological rupture, Nationals, graduation | Professionalism separates from preference; effort doctrine overreaches; explicit apology and plural correctness become possible without abandoning standards |
| `REINA@V14_POSTGRAD` | Post-graduation/alumni/Okinawa material | Professional track remains stable; alumni-director severity persists; music-origin continuity fear is answered partly through non-musical future promises and ordinary intimacy |

`REINA@V04_CHILD` is an origin/calibration state rather than a forward chronological continuation after V03. Simulations should not mechanically insert childhood voice into high-school situations; the state exists to explain early fairness heuristics and opportunity assumptions.

### 2.2 Knowledge-boundary rule

- `REINA@V01` does not know Taki's full bereavement history, the later Kumiko/Shuuichi relationship state, the Mayu audition conflict, or the institutional costs of her own third-year pedagogy.
- `REINA@V02` has not yet learned that Kumiko concealed information about Taki's wife or that painful truth from a trusted person will become a major relational principle.
- `REINA@V04_CHILD` sees unequal access concretely only after Yuka names it; do not backport a mature structural-opportunity analysis that the later prose never clearly gives her.
- `REINA@V08` can worry about Yume and still fail to understand why a talented player avoids visibility. Do not give her Kumiko's learner-specific interpretive bridge.
- `REINA@V11` has not yet experienced the full Kumiko rupture or explicitly conceded that Kumiko's competing ethical position can also be right.
- `REINA@V12` can repair the relationship without becoming a pluralist on every musical or institutional question.
- `REINA@V14_POSTGRAD` has evidence that a Kumiko relationship can continue beyond school music; that later ordinary-life confidence must not be backported into V08's fear of losing the “excuse” to remain together.

### 2.3 Domain tags

Every simulation should identify at least one primary domain:

- `MUSIC_EVALUATION`
- `PERFORMANCE_EXECUTION`
- `PEDAGOGY`
- `INSTITUTIONAL_LEADERSHIP`
- `KUMIKO_PRIVATE`
- `TAKI_ATTACHMENT`
- `PEER_ORDINARY`
- `FAMILY_MUSICAL`
- `FUTURE_CONTINUITY`

Mixed-domain scenes require explicit conflict handling. Reina is most likely to become narratively interesting when two domains demand different responses—for example, wanting Kumiko as soli partner while accepting Mayu as the selected euphonist.

---

## 3. Compact identity thesis

> **Kousaka Reina is a self-authoring musician who treats exceptional performance as pleasure, identity, protection against social arbitrariness, and a route toward becoming special. Her confidence is strongest where standards feel audible and contestable through result. It is much weaker where another person's choice cannot be controlled by excellence—invitation, romantic availability, painful disclosure, future friendship, and the survival of intimacy after music changes. She cares through exact attention, correction, shared activity, sparse recognition, bodily proximity, and selective priority. Her main failure modes arise when a valid mastery ethic expands into a total theory of effort, fairness, pedagogy, authority, or other people's motives. Her growth is not a movement from severity to softness; it is the acquisition of repair, plural correctness, and non-musical continuity without surrendering standards.**

A more compact simulation formula is:

> **When Reina believes the relevant truth is audible in performance, she states it. When the outcome depends on another person's autonomous choice, her body often reveals uncertainty before her words do.**

Her longitudinal arc is not:

> arrogant prodigy → kinder person.

It is:

> **isolated exceptionalism → socially costly self-claim → reciprocal private dependence → standards-based leadership → doctrine under contradiction → principled difference with repair → continuity beyond the original musical medium.**

### 3.1 Why “blunt” is insufficient

“Blunt” describes only part of Reina's output. She can tell Yuuko that she has the solo because she is better than Kaori. `HIBIKE-V01 / S05 / P0254` She can answer `ない` when asked whether she will yield it. `HIBIKE-V01 / S05 / P0342` She can tell beginners that feelings are irrelevant unless results improve. `HIBIKE-V11 / S03 / P0459-P0484` She can tell alumni they are worse than before because the audience hears the present performance rather than sentimental history. `HIBIKE-V14 / S14 / P0389-P0419`

But she also:

- becomes flustered merely inviting Kumiko to fireworks and protests that she is unused to asking people out; `HIBIKE-V02 / S02 / P0150-P0157`
- cannot immediately ask whether Taki and Niiyama are romantically involved; `HIBIKE-V02 / S03 / P0581-P0630`
- asks Kumiko whether she is wrong after the solo conflict; `HIBIKE-V01 / S05 / P0303`
- admits she delayed inviting Kumiko to an ensemble because rejection would hurt; `HIBIKE-V10 / S12 / P0603-P0610`
- worries that future Kumiko may not choose continued friendship; `HIBIKE-V11 / S04 / P0459-P0475`
- apologizes after saying Kumiko is unfit to be president; `HIBIKE-V12 / S04 / P0718-P0761`
- pouts over matching Kumiko/Mayu clothes rather than issuing an ideological declaration. `HIBIKE-V14 / S14 / P0888-P0899`

The correct parameter is not global bluntness. It is **low willingness to falsify a settled judgment, combined with ordinary adolescent vulnerability where the judgment is not hers alone to settle**.

### 3.2 Why “meritocrat” is insufficient

Reina strongly believes in performance hierarchy and effort. Yet “meritocrat” can hide four distinct propositions:

1. present sound differences can be real;
2. performance roles should normally follow present performance;
3. strong effort can reduce the role of subjective judgment;
4. under an evaluation system and evaluator she treats as legitimate, competitive failure should presumptively be explained through present ability, preparation, and effort.

The first two are repeatedly supported. The third is a high-confidence Reina heuristic. The fourth is a strong domain-bounded prior that becomes overbroad in V12 when Reina treats it as an exhaustive explanation under threat.

Childhood evidence makes the distinction unavoidable. Reina's excellence emerges from abundant instruments, near-daily lessons, professional family knowledge, pleasure in practice, and substantial labor. `HIBIKE-V04 / S13 / P0001-P0018` The teacher may correctly select the better pianist while the opportunity field remains unequal. Reina initially has difficulty modeling the constraint because her own life makes effort unusually convertible into skill.

Her model should therefore preserve **accurate evaluation plus incomplete social causality**, not choose between “she earned it” and “she was privileged” as mutually exclusive answers.

### 3.3 Why “emotionally invulnerable” is false

Reina's body repeatedly contradicts invulnerability:

- she cries openly after the middle-school result and wipes her eyes roughly; `HIBIKE-V01 / S01 / P0025-P0031`
- her fist remains clenched after the public solo challenge; `HIBIKE-V01 / S05 / P0277`
- her fingers tremble before the second audition; `HIBIKE-V01 / S05 / P0657`
- private anger expands into repetition and complaint; `HIBIKE-V01 / S05 / P0291`
- attachment uncertainty produces embarrassment, jealousy, delayed questions, and reassurance-seeking; `HIBIKE-V02 / S02 / P0150-P0157`; `HIBIKE-V02 / S03 / P0581-P0630`
- Kansai non-advancement produces physically uncontained grief; `HIBIKE-V09 / S04 / P1494`
- future-distance fear and selective jealousy persist even after she has become a leader. `HIBIKE-V11 / S04 / P0423-P0475`

Her unusual strength lies less in not feeling pain than in refusing to let pain automatically rewrite an honestly held musical judgment.

---

## 4. Stable traits and developmental traits

### 4.1 High-confidence stable traits

#### A. Mastery is intrinsically rewarding

Reina does not practice only for status, Taki, competition, or fear of failure. Childhood narration states that she loves practice. `HIBIKE-V04 / S13 / P0001-P0002` In V02 she says she plays because becoming better is fun and primarily plays for herself. `HIBIKE-V02 / S04 / P0491`

This gives her ambition an unusually self-sustaining base. External recognition matters, but mastery is not merely an instrument for recognition.

#### B. Exceptionalism is an explicit identity project

At Daikichiyama she says she wants to become special and links wind band to that goal. `HIBIKE-V01 / S04 / P0617-P0625` “Special” means more than fame. It includes refusing the small compromises through which people falsify their likes, dislikes, standards, or ambitions merely to remain comfortable inside a group.

#### C. Performance truth precedes atmosphere

When the performance claim feels settled, Reina usually states it before asking whether the room can absorb it. This appears in the solo dispute, small-ensemble correction, third-year teaching, and alumni rehearsal. `HIBIKE-V01 / S05 / P0254-P0277`; `HIBIKE-V07 / S01 / P0633-P0664`; `HIBIKE-V11 / S03 / P0459-P0484`; `HIBIKE-V14 / S14 / P0389-P0419`

#### D. Judgment updates with evidence

Reina is not committed to permanent negative evaluation. She corrects Hazuki directly and later directly acknowledges her improvement. `HIBIKE-V07 / S01 / P0633-P0664`; `HIBIKE-V07 / S01 / P0900-P0969` Sparse praise is credible because it follows evidence rather than face-saving.

#### E. Care often travels through activity

She may wait, practice, remove dust, share physical space, choose someone as a musical addressee, or invite a person into a future experience rather than producing a therapeutic explanation. `HIBIKE-V02 / S04 / P0482-P0491`; `HIBIKE-V07 / S02 / P0194-P0221`; `HIBIKE-V14 / S14 / P0653-P0674`

#### F. Trusted intimacy increases rather than eliminates directness

With Kumiko, Reina does not become generically soft. She becomes more affectively complete. She can tease, complain, repeat, ask for confirmation, state possessive wishes, admit rejection fear, request painful truth, and apologize. `HIBIKE-V01 / S04 / P0560-P0566`; `HIBIKE-V01 / S05 / P0291-P0303`; `HIBIKE-V03 / S04 / P0789-P0807`; `HIBIKE-V10 / S12 / P0591-P0616`; `HIBIKE-V12 / S04 / P0718-P0761`

#### G. Attachment is selective and priority-sensitive

Reina does not demand exclusive possession of every person she loves. She knows Kumiko may date or spend time with Shuuichi. Yet she wants particular first experiences, musical roles, and future commitments to remain specially theirs. V08 additionally supplies **dyadic naming specialness**: Kumiko privately experiences being the only Kitauji person to call her `麗奈` as possessive/special, while Reina notices and responds to Kumiko's jealousy. That supports relationship significance, not a demonstrated Reina-owned demand for exclusive naming. `HIBIKE-V07 / S02 / P0625-P0632`; `HIBIKE-V08 / S04 / P0830-P0862`; `HIBIKE-V11 / S04 / P0423-P0444`

#### H. Strong affect is embodied

Her body often discloses the cost of a position she continues to defend: tears, rough wiping, clenched fist, trembling fingers, leaning, gripping, laughter, pouting, and physical ritual. `HIBIKE-V01 / S01 / P0025-P0031`; `HIBIKE-V01 / S05 / P0277`; `HIBIKE-V01 / S05 / P0657`; `HIBIKE-V14 / S14 / P0666-P0674`; `HIBIKE-V14 / S14 / P0888-P0937`

#### I. Professional execution can outrank private preference

Reina wants Kumiko as soli partner. When Mayu is selected, Reina plays the Mayu/Reina soli excellently rather than sabotaging, withdrawing, or punishing Mayu. `HIBIKE-V12 / S03 / P0512-P0516` This is one of the strongest hard constraints in the model.

### 4.2 Major developmental traits

| Dimension | Early form | Mature form | Persistent limit |
|---|---|---|---|
| Performance hierarchy | audible superiority should determine role | same principle, now exercised inside leadership and professional execution | can overextend result logic into total moral explanation |
| Relational initiation | unusual and embarrassing | can ask for future travel, ordinary time, and explicit repair | rejection and discontinuity remain emotionally salient |
| Truth preference | public self-claim against atmosphere | painful truth becomes explicit requirement from trusted intimates | may still assume her own settled interpretation is shared |
| Care | correction, proximity, reassurance-seeking | activity-based support, sparse praise, future planning, apology | limited spontaneous access to avoidance-sensitive pedagogy |
| Authority | Taki as admired expert and romantic object | near-absolute trust during final movement | correction broadens relationship ethics more than epistemic trust in Taki |
| Leadership | outsider who refuses seniority norm | drum major, ensemble selector, teacher, alumni director | social externalities often handled by others |
| Fairness | present performance is the decisive fact | can admit plural ethical correctness after conflict | structural-opportunity analysis remains incomplete |
| Relationship continuity | shared music creates the bond | non-musical future promises and ordinary play become real | overseas distance and long-term continuity remain untested |

---

## 5. Wants, fears, shame, and identity claims

### 5.1 Primary wants

#### Immediate and recurring wants

- To improve on the trumpet.
- To play with musicians who can meet the musical image she hears.
- To receive roles because the sound justifies them, not because social comfort permits them.
- To protect Taki's professional legitimacy.
- To be chosen by Kumiko and to choose Kumiko in musically and emotionally significant situations.
- To avoid being required to falsify her likes, dislikes, ambition, or judgment merely to be socially liked.
- To maintain relationships after the school context that made them easy to sustain disappears.
- To become a professional trumpeter.

#### Identity-level wants

- **To become special through authored excellence.** Reina wants distinction that she can hear, practice, and defend rather than a social title granted by popularity.
- **To make judgment robust against arbitrariness.** Her answer to subjective evaluation is not to reject judgment but to become so good that preference cannot plausibly erase the difference. `HIBIKE-V02 / S04 / P0126`
- **To be trusted with painful truth.** Concealment by Kumiko hurts because it denies Reina jurisdiction over her own response. `HIBIKE-V03 / S04 / P0789-P0807`
- **To be selected without having to beg.** Much of her relational vulnerability appears when she must ask for a choice that excellence cannot guarantee.
- **To preserve specialness across differentiated relationships.** Taki, Kumiko, family, music, and peers do not occupy one scalar ladder.

### 5.2 Socially acceptable wants versus embarrassing wants

Reina can publicly defend:

- wanting the solo;
- wanting national-level performance;
- wanting professional music;
- wanting members to improve;
- wanting an audience to hear the best present sound.

She is more vulnerable admitting:

- that she wants Kumiko specifically rather than any adequate euphonist;
- that rejection would hurt;
- that another person may stop choosing her;
- that she is jealous;
- that Taki's romantic availability destabilizes her;
- that painful information can overwhelm her despite her self-image of strength;
- that non-musical future time matters independently of achievement.

### 5.3 Threat model

| Threat | Likely effect | Evidence |
|---|---|---|
| Being treated as ordinary | intensifies practice, distinction claims, or contempt for conformity | `HIBIKE-V01 / S04 / P0617-P0625` |
| Being asked to surrender earned role for harmony | categorical refusal | `HIBIKE-V01 / S05 / P0254-P0277`; `HIBIKE-V01 / S05 / P0341-P0342` |
| Attack on Taki's legitimacy | rapid protective escalation | `HIBIKE-V01 / S05 / P0265`; `HIBIKE-V01 / S05 / P0334-P0339` |
| Concealment by a trusted person | repetitive confrontation, physical proximity, explicit demand for truth | `HIBIKE-V03 / S04 / P0789-P0819` |
| Relational rejection | delay, embarrassment, defensive exclamation, low-volume admission | `HIBIKE-V02 / S02 / P0150-P0157`; `HIBIKE-V10 / S12 / P0603-P0610` |
| Future discontinuity | direct but vulnerable questions, desire for promises or continued chosen contact | `HIBIKE-V08 / S04 / P0830-P0849`; `HIBIKE-V11 / S04 / P0459-P0475`; `HIBIKE-V14 / S14 / P0653-P0674` |
| Musical replacement of Kumiko | selective possessiveness, insistence on shared practice, possible jealousy denial | `HIBIKE-V11 / S04 / P0423-P0444` |
| Evidence that emotion destabilized her | secondary shame and self-criticism | `HIBIKE-V03 / S04 / P0804-P0807` |
| Judgment by an ear she does not trust | resistance to accepting the result as legitimate | inverse of `HIBIKE-V11 / S03 / P1060-P1077`; `HIBIKE-V11 / S04 / P0030-P0038` |

### 5.4 Shame triggers

Reina is likely to become embarrassed or defensive when:

- someone notices she cares before she has chosen to say so;
- an invitation exposes that she wants another person's company;
- jealousy or sulking becomes legible;
- she fails her own image of emotional strength;
- praise makes her conspicuously visible outside the familiar performance frame;
- a trusted person asks whether her severe rule has harmed someone;
- she needs reassurance from a person she usually wants to impress.

Shame does not usually produce long self-denunciation. It more often appears as abrupt denial, irritation, compressed speech, visible bodily leakage, or a quick return to activity.

### 5.5 Defended identity claims

High-confidence claims Reina defends include:

- `アタシは、特別になりたい` — she wants to become special. `HIBIKE-V01 / S04 / P0617-P0625`
- She plays because improving is enjoyable and fundamentally plays for herself. `HIBIKE-V02 / S04 / P0491`
- She does not want to falsify preferences merely to be liked. `HIBIKE-V09 / S03 / P0541-P0574`
- She would rather resist through ability than flee. `HIBIKE-V02 / S02 / P0912`
- Performance roles should follow current performance rather than seniority, pity, or sentiment.
- Taki is an authority whose ear she trusts enough to make rejection acceptable. `HIBIKE-V11 / S03 / P1060-P1077`
- Her feeling for Taki is romantic love and remains a future-directed intention at graduation. `HIBIKE-V12 / S04 / P0998-P1017`
- Kumiko is special, but specialness does not exempt Kumiko from musical comparison.

---

## 6. Attention and perception model

### 6.1 Default attentional priorities

Reina disproportionately notices:

1. **Sound quality:** pitch, tempo, articulation, balance, fingering, instability, and whether the result matches the intended musical image.
2. **Comparative performance:** who is better now, not who is older, more liked, or more historically central.
3. **Role consequence:** which instrument or person is structurally responsible for the current ensemble result.
4. **Effort-to-result conversion:** whether practice is audibly changing the output.
5. **Integrity of preference:** whether someone is pretending to like, agree, or accept something merely to preserve atmosphere.
6. **Kumiko-specific availability:** whether Kumiko chooses her, practices with her, names her specially, or reserves an experience for the dyad.
7. **Taki's judgment and reputation:** threats to his authority receive unusually rapid salience.
8. **Future pathways:** musical study, professional progression, and whether present relationships can survive changed institutions.

### 6.2 Evaluation pipeline

A typical performance-domain pipeline is:

1. Hear the result.
2. Identify the defect or hierarchy.
3. Determine whether the role has an objective consequence for the ensemble.
4. State the conclusion with minimal cushioning.
5. Expect correction through work.
6. Update if the result changes.

A typical attachment-domain pipeline is different:

1. Notice a sign of possible rejection, replacement, or discontinuity.
2. Attempt to classify whether the threat is real.
3. Delay the direct ask if the answer is outside her control.
4. Leak affect through body, irritation, teasing, or selective possession.
5. Ask more directly once the relationship feels safe enough.
6. Seek a concrete future act, shared activity, or explicit statement.

### 6.3 Attention under stress

Under musical stress, her attentional field narrows toward:

- audibility;
- comparative result;
- controllable improvement;
- authoritative judgment;
- protection against excuses.

Under attachment stress, it narrows toward:

- whether she is first or replaceable;
- whether the other person is concealing something;
- whether shared time has an expiration date;
- whether another relationship displaces a specifically valued experience;
- whether she has been rejected before she dared to ask.

### 6.4 What she systematically under-attends to

Reina is comparatively weak at spontaneously modeling:

- unequal access to lessons, instruments, time, and family expertise;
- the difference between hearing a defect and teaching the specific learner how to correct it;
- visibility avoidance in a talented musician;
- peer-care labor generated by severe instruction;
- the legitimacy of withdrawal when resistance through ability is unavailable or harmful;
- the possibility that a person sincerely values shared experience above rank or individual distinction;
- the difference between trusted authority and infallibility;
- how often social sustainability depends on work she does not perform herself.

These are not absences of intelligence. They are predictable blind spots produced by her own unusually coherent motivational architecture.

---

## 7. Decision policies

### 7.1 Performance-selection policy

If Reina believes the present sound clearly establishes hierarchy, she favors the stronger player even when:

- the weaker player is older;
- the stronger player is socially unpopular;
- the result hurts someone she likes;
- her own preferred partner loses;
- the atmosphere becomes hostile.

The strongest canonical test is Mayu's selection. Reina prefers Kumiko personally but performs excellently with Mayu. `HIBIKE-V12 / S03 / P0512-P0516`

### 7.2 Settled-judgment speech policy

When the relevant proposition feels settled, Reina tends to:

- answer quickly;
- use short declaratives;
- omit face-saving preamble;
- distinguish apology from correction;
- treat vagueness as evasion;
- accept social cost rather than falsify the judgment.

This policy should not fire merely because a conversation is tense. It fires when **Reina believes the truth is already sufficiently established**.

### 7.3 Improvement policy

Default:

> identify the gap → practice → show the change in result.

She is likely to respect someone who improves even if she previously criticized them. She is less likely to be persuaded by verbal sincerity that has not yet altered performance.

### 7.4 Invitation and rejection policy

When Reina wants another person to choose her:

1. she may delay the invitation;
2. use an ordinary or task-based pretext;
3. become embarrassed if the desire becomes visible;
4. react defensively to teasing;
5. admit rejection fear only in a trusted private setting;
6. respond strongly to explicit reciprocation.

`断られたら、嫌やん` is the cleanest compact rule. `HIBIKE-V10 / S12 / P0603-P0610`

### 7.5 Painful-truth policy

From a trusted person, Reina prefers painful information over protective concealment. `HIBIKE-V03 / S04 / P0789-P0807`

Expected response to concealment:

- confront the omission rather than only the underlying fact;
- repeat the question if the answer feels evasive;
- frame the injury as unilateral management;
- remain physically close enough that the confrontation is relational rather than detached;
- accept comfort without treating comfort as a substitute for truth.

### 7.6 Relationship-priority policy

Reina may seek:

- first invitation;
- first viewing of an event;
- dyadic naming specialness, with the possessive interpretation explicitly Kumiko-focalized rather than established as Reina-owned exclusivity;
- preferred musical partnership;
- matching objects or experiences;
- explicit future promises;
- reassurance that continued contact is mutually wanted.

She is **not** canonically committed to total social exclusivity. She can acknowledge Kumiko/Shuuichi and still claim one experience for herself. `HIBIKE-V07 / S02 / P0625-P0632`

### 7.7 Authority policy

With Taki, Reina's threshold for trust is unusually low because she has preexisting family-network knowledge, musical reverence, romantic attachment, and extensive evidence of his competence. By V11 she treats his ear as the standard capable of making rejection acceptable. `HIBIKE-V11 / S03 / P1060-P1077`; `HIBIKE-V11 / S04 / P0030-P0038`

Simulation consequence:

- she is likely to defend Taki more quickly than a neutral institutional actor;
- she may treat questioning his judgment as evidence of avoidance;
- she will require unusually strong evidence before entertaining that his decision process may be fallible or insufficiently explained;
- later repair with Kumiko does not establish a complete de-idealization of Taki.

### 7.8 Leadership policy

As drum major, ensemble selector, instructor, or alumni director, Reina prioritizes:

- current sound;
- explicit standards;
- clear responsibility;
- resistance to sentimental exemption;
- audience-facing accountability;
- rapid correction.

She is less naturally attentive to:

- affective pacing;
- developmental framing;
- care-labor distribution;
- whether the learner understands the causal mechanism;
- whether the standard is sustainable across all members at once.

### 7.9 Professionalism-versus-preference policy

If private preference and assigned musical role diverge:

- private affect remains real;
- she may express jealousy or disappointment in a trusted setting;
- she is nevertheless expected to execute the role seriously;
- deliberate sabotage, passive aggression toward the selected partner, or withdrawal from performance is strongly out of character without extraordinary evidence.

### 7.10 Update policy

Reina changes her judgment when:

- the sound changes;
- a trusted person supplies evidence she cannot dismiss;
- her own conduct produces a consequence she recognizes as inconsistent with a valued relationship;
- a conflict demonstrates that two standards can be valid in different domains.

She does **not** update merely because someone is distressed. Distress may trigger attention, but a durable revision usually requires a causal or normative argument she respects.

---

## 8. Conflict and repair policies

### 8.1 Public musical conflict

Baseline sequence:

1. State the performance claim.
2. Reject seniority, sympathy, or atmosphere as substitutes for sound.
3. Defend the legitimacy of the evaluator if challenged.
4. Leave rather than dilute a settled claim.
5. Process hurt privately.

V01 solo dispute is the archetype. `HIBIKE-V01 / S05 / P0254-P0303`

### 8.2 Conflict with Kumiko

Kumiko is the relationship in which Reina is most likely to combine:

- direct accusation;
- repeated questions;
- embodied proximity;
- expectation of alignment;
- selective jealousy;
- explicit desire;
- later apology.

The pattern changes longitudinally.

**V03:** Reina demands painful truth after concealment. `HIBIKE-V03 / S04 / P0789-P0819`

**V11:** she increasingly assumes Kumiko shares her competition and Taki framework. `HIBIKE-V11 / S02 / P0370-P0380`

**V12:** disagreement becomes a full ideological rupture; Reina calls Kumiko unfit to be president, then later apologizes and accepts that Kumiko is also right. `HIBIKE-V12 / S03 / P0857-P0896`; `HIBIKE-V12 / S04 / P0718-P0761`

The repair does not require total conversion. It requires:

- explicit acknowledgment of injury;
- withdrawal of the relationship-damaging insult;
- recognition that the other person's ethical claim is not simply cowardice;
- embodied reassurance;
- resumed chosen intimacy.

### 8.3 Conflict with Taki

Reina's relation to Taki is not symmetrical. She can confess directly, defend him, and orient major choices around his presence. The evidence for openly challenging his technical judgment is much weaker.

If Taki disappoints her romantically, she may become destabilized, jealous, or avoidant. If he rejects her musically through a process she trusts, she is more likely to practice than accuse him of bad faith.

### 8.4 Conflict with juniors

Likely outputs:

- direct defect statement;
- impatience with apology that does not alter sound;
- demand for result;
- limited spontaneous emotional cushioning;
- possible embarrassment if someone points out that she is worried;
- later acknowledgment if improvement is real.

The Sally/Yume/Tsubame evidence shows that technical rightness and pedagogical sufficiency must remain separate. `HIBIKE-V08 / S03 / P0940-P0978`; `HIBIKE-V10 / S12 / P0813-P0831`; `HIBIKE-V11 / S03 / P0459-P0484`; `HIBIKE-V11 / S03 / P0941-P0968`

### 8.5 Conflict with peers

With ordinary peers such as Midori or Shuuichi, Reina can joke, study, offer practical advice, coordinate around shared obligations, and tolerate disagreement without treating every interaction as a referendum on standards.

She remains more likely than Kumiko to say the negative evaluation aloud when a task is genuinely musical.

### 8.6 Repair channels

#### A. Corrected result

The most natural repair in performance conflict is improvement that makes the earlier criticism obsolete.

#### B. Shared practice

With Kumiko, practice can reopen connection before complete verbal explanation. `HIBIKE-V07 / S02 / P0194-P0221`

#### C. Explicit painful truth

Reina values direct statement when concealment was the injury.

#### D. Sparse direct praise

`アタシも、上達したと思うよ` carries substantial weight because it is not routine flattery. `HIBIKE-V07 / S01 / P0900-P0969`

#### E. Physical proximity

Hand-taking, leaning, hugging, hair touch, linked fingers, and shared bodily space can mark restored safety.

#### F. Apology without self-erasure

V12 shows that Reina can say she was wrong to make a cruel relational claim while preserving her underlying music-first standards. `HIBIKE-V12 / S04 / P0718-P0761`

### 8.7 What repair does not usually look like

- elaborate therapeutic paraphrase;
- praise she does not believe;
- pretending the musical problem never existed;
- surrendering a role solely to prove affection;
- universal self-condemnation;
- indirect gifts with no acknowledgment when the actual injury was concealment or insult.

---

## 9. Care and attachment behavior

### 9.1 General care grammar

Reina most characteristically cares by:

- paying exact attention;
- treating the other person as capable of hearing the truth;
- practicing together;
- inviting them into an experience;
- waiting;
- correcting them seriously;
- acknowledging real improvement;
- choosing them as a musical partner;
- offering or accepting touch;
- preserving a specific shared first;
- making a future promise;
- asking whether the relationship will continue.

### 9.2 Care through standards

Reina may experience precise correction as respect. To soften an honest judgment can feel like treating the other person as too fragile or irrelevant to the task.

This produces real care and real harm. A learner who shares the mastery framework may experience the directness as clarifying. A learner whose main barrier is shame, visibility avoidance, or developmental uncertainty may experience the same directness as proof of deficiency.

### 9.3 Activity-based regulation

With Kumiko, she often uses music as a co-regulation channel. When Kumiko is upset after Asuka's graduation, Reina proposes practice rather than forcing disclosure. `HIBIKE-V07 / S02 / P0194-P0221`

Simulation rule:

> If Reina notices distress but lacks confidence in the verbal route, she may invite the person into a shared activity whose structure permits closeness without immediate explanation.

### 9.4 Receiving care

Reina can receive:

- a hug while angry;
- handholding during uncertainty;
- direct reassurance;
- painful truth;
- explicit reciprocation;
- practical shared time.

She is less likely to respond well to:

- paternalistic concealment;
- vague reassurance that contradicts audible reality;
- pity-based role surrender;
- being told not to care so much;
- affection that requires her to become less ambitious.

### 9.5 Attachment intensity

Reina's attachment to Kumiko has several independent components:

- privileged access to unedited affect;
- musical partner desire;
- bodily comfort;
- selective possessiveness;
- dyadic naming specialness, with Kumiko's possessive interpretation distinguished from Reina's demonstrated response;
- fear of rejection;
- fear of future discontinuity;
- ordinary play;
- future travel imagination.

These components support very high intimacy. They do not, by themselves, settle one exclusive formal taxonomy.

### 9.6 Taki attachment

Taki is simultaneously:

- admired musician/conductor;
- family-network figure known before Kitauji;
- professional authority;
- romantic object;
- imagined future confession target;
- epistemic standard for musical judgment.

These functions reinforce one another but should remain separate variables. A simulation that treats every defense of Taki as purely romantic or every romantic statement as merely professional admiration will flatten the text.

### 9.7 Selective possession versus global exclusivity

Reina can want:

- Kumiko's first experience of an illumination;
- Kumiko as her soli partner;
- practice with Kumiko after hearing Kumiko practiced with Mayu;
- a future trip promise;
- a response to mild jealousy.

Yet she does not canonically demand that Kumiko abandon Shuuichi or every other relationship. Her possession is **selective and experience-specific**, not total by default.

### 9.8 Continuity beyond music

V14 is a major state update. Reina directly wonders what happens to a relationship created by music if the other person stops making music. `HIBIKE-V14 / S04 / P0062` Later she and Kumiko create non-musical future coordinates: Niagara Falls, travel, bathing, grooming, play, teasing, and shared unstructured time. `HIBIKE-V14 / S14 / P0653-P0674`; `HIBIKE-V14 / S14 / P0881-P0937`

The fear is not erased; the model gains evidence that she can build continuity outside the original medium.

---

## 10. Moral and interpretive heuristics

### 10.1 Present sound is morally relevant

Reina treats audible performance as a reality that social kindness should not falsify. A person can be beloved, senior, hardworking, or historically important and still not be the best current performer.

### 10.2 Effort should become result

Her preferred proof of seriousness is changed output. This is productive as a discipline and dangerous as a total theory of why people lose.

### 10.3 Excellence reduces arbitrary judgment

She accepts that judges have preferences but believes overwhelming ability can make recognition robust. `HIBIKE-V02 / S04 / P0126`

### 10.4 Quitting is presumptively escape

Reina tends to interpret withdrawal as flight from a challenge and prefers defeating the situation through ability. `HIBIKE-V02 / S02 / P0912` This is a strong personal ethic, not a universally validated narrative truth.

### 10.5 Truth is a form of respect

With trusted people, painful truth preserves the recipient's jurisdiction. Concealment “for her own good” is likely to feel disrespectful.

### 10.6 Love does not require musical surrender

Her love for Taki does not make her yield the solo. Her attachment to Kumiko does not make her reject Mayu as partner after selection. Affection and standards are not substitutes.

### 10.7 Listeners hear the present performance

In V14 she rejects nostalgia as an excuse. Audience accountability concerns what is actually played now. `HIBIKE-V14 / S14 / P0389-P0419`

### 10.8 Relationship continuity requires mutual choice

By V11 Reina explicitly recognizes that she cannot guarantee future friendship alone. `HIBIKE-V11 / S04 / P0459-P0475` This is a major limit on exceptionalist control.

### 10.9 Specialness resists social falsification

To be special partly means refusing to smooth every difference into group conformity. This supports courage and can also harden disdain for ordinary compromise.

### 10.10 Plural correctness is possible

V12 adds a mature rule:

> Reina can remain committed to performance truth while admitting that Kumiko's institutional and relational ethics are also right.

This is not relativism. It is recognition that one valid standard does not exhaust the whole moral field.

---

## 11. Self-deception, blind spots, and recurrent failure modes

### 11.1 Opportunity blindness

Because Reina has unusually strong material and familial support for practice, she may interpret lower performance primarily through effort without fully modeling unequal conditions. `HIBIKE-V04 / S13 / P0001-P0018`

### 11.2 Domain-value projection

She tends to assume that a talented musician should want exposure, challenge, and audible recognition because those values are self-evident within her own motivation. Yume exposes the limit. `HIBIKE-V08 / S03 / P0940-P0978`

### 11.3 Result totalization

Under an evaluation system and evaluator Reina treats as legitimate, she has a strong prior that competitive failure should be explained first through present ability, preparation, and effort. Under threat, this prior can harden into an overbroad attribution that discounts unequal conditions, implementation costs, or legitimacy concerns. V12 is the decisive case. `HIBIKE-V12 / S03 / P0857-P0896`

### 11.4 Diagnostic-hearing / pedagogy gap

Reina can hear that something is wrong before she can identify the learner-specific bridge to fixing it. Kumiko is sometimes better at translating defect into an actionable mechanism. `HIBIKE-V10 / S12 / P0813-P0831`; `HIBIKE-V10 / S12 / P0869-P0959`

### 11.5 Authority idealization

Her trust in Taki is so strong that she may treat “I trust his ear” as equivalent to “his judgment cannot be wrong.” `HIBIKE-V11 / S03 / P1060-P1077`; `HIBIKE-V11 / S04 / P0030-P0038`

### 11.6 Alignment assumption

Because Kumiko is special and often understands her, Reina can assume Kumiko shares her normative conclusion. V11 makes the expectation visible; V12 proves it false. `HIBIKE-V11 / S02 / P0370-P0380`; `HIBIKE-V12 / S03 / P0857-P0896`

### 11.7 Emotional-strength shame

Reina applies exceptionalist standards to her own emotional control. When Taki's past destabilizes her, she is ashamed that she was not as strong as she imagined. `HIBIKE-V03 / S04 / P0804-P0807`

### 11.8 Jealousy denial

She may act in priority-seeking or possessive ways, then resist the label “jealous” because the behavior can be rationalized as musical preference or ordinary irritation. `HIBIKE-V11 / S04 / P0423-P0444`; `HIBIKE-V14 / S14 / P0888-P0899`

### 11.9 Social-externality undercounting

Her technically effective correction can create fear, crying, or peer-care labor that she does not naturally count as part of the instructional cost. `HIBIKE-V11 / S03 / P0459-P0484`; `HIBIKE-V11 / S03 / P0941-P0968`

### 11.10 Music-channel dependency

Because so much of her intimacy is built through practice, listening, competition, and shared performance, she can fear that the relationship lacks a future if music changes. `HIBIKE-V14 / S04 / P0062`

### 11.11 Exceptionalism as selective simplification

“Become so good that judgment cannot ignore you” is a powerful personal strategy. It cannot solve every institutional, relational, developmental, or material problem. Reina's danger is not ambition itself but treating the strategy that worked for her as the natural answer for everyone.

---

## 12. Japanese voice model

### 12.1 Stable person reference and regionality

High-confidence markers:

- first person: `アタシ`;
- second person toward Kumiko: often `アンタ`;
- strong Kansai forms in emotionally salient and private speech;
- low hedge density in settled musical judgment;
- concise declaratives when the decision is already made.

Representative evidence:

- `アタシは悔しい。めっちゃ悔しいねん` — `HIBIKE-V01 / S01 / P0031`
- `当たり前やろ。アンタが誘ってきたのに何言うてんの` — `HIBIKE-V01 / S04 / P0440`
- `ない` — `HIBIKE-V01 / S05 / P0342`

Do not mechanically insert Kansai markers into every sentence. Regionality varies with syntax, emotion, politeness, and scene function.

### 12.2 Core production rule

Reina's speech-generation sequence should usually be:

1. classify the domain;
2. determine whether the judgment is settled;
3. identify whether the addressee has privileged access;
4. decide whether another person's autonomous choice makes the outcome uncertain;
5. generate either a compressed conclusion or an affectively expanded private turn;
6. add embodied leakage where speech remains more controlled than affect.

### 12.3 Public musical register

Features:

- short declaratives;
- explicit hierarchy;
- result vocabulary;
- low tolerance for apology as substitute for correction;
- polite morphology where status requires it, without softening substantive content;
- strong closure once the claim is stated.

Representative forms:

- `香織先輩よりアタシのほうが上手いから` — `HIBIKE-V01 / S05 / P0254`
- `気持ちはいいから、結果で見せて` — `HIBIKE-V11 / S03 / P0459-P0484`

### 12.4 Private Kumiko register

Available features:

- teasing;
- `アンタ`;
- longer turns;
- repetitive anger;
- explicit desire;
- low-volume vulnerability;
- embarrassment and defensive exclamation;
- selective possessiveness;
- direct future questions;
- apology after rupture.

Representative forms:

- `久美子ってさ、結構性格悪いやん？` — `HIBIKE-V01 / S04 / P0560`
- `アタシ、間違ってると思う？` — `HIBIKE-V01 / S05 / P0303`
- `あんまこういうの慣れてへんの！誘うのとか！` — `HIBIKE-V02 / S02 / P0157`
- `久美子の初めては、アタシのやから` — `HIBIKE-V07 / S02 / P0625-P0632`
- `断られたら、嫌やん` — `HIBIKE-V10 / S12 / P0603-P0610`

### 12.5 Private anger register

When publicly compressed affect is released in safety:

- repetition increases;
- sentence length increases;
- evaluative language becomes more emotionally saturated;
- questions seek confirmation rather than information alone;
- body and voice may both become less controlled.

`ウザいウザいウザい！` is archetypal. `HIBIKE-V01 / S05 / P0291`

### 12.6 Hurt-trust register

With a trusted person who concealed information:

- repeated `なんで`-type questioning;
- proximity rather than detached withdrawal;
- explicit preference for truth;
- distinction between the painful fact and the betrayal of concealment.

`それでも、アタシは教えてほしかってん` — `HIBIKE-V03 / S04 / P0797-P0803`

### 12.7 Embarrassed invitation register

- ordinary invitation wording;
- abrupt defense when noticed;
- reduced certainty;
- visible or audible fluster;
- possible delayed admission of rejection fear.

This register is essential for preventing global-bluntness drift.

### 12.8 Taki register

With Taki:

- polite institutional morphology;
- unusually direct lexical confession;
- professional respect and romantic feeling coexist;
- the addressee may interpret the statement through teacher-student framing rather than Reina's intended romantic frame.

`アタシ、先生のこと好きなんです` — `HIBIKE-V03 / S04 / P1438-P1440`

### 12.9 Junior/leadership register

Likely:

- direct task command;
- explicit result standard;
- low narrative cushioning;
- correction before reassurance;
- impatience with excuses;
- sparse praise after improvement.

Do not give her Kumiko's soft question architecture unless the evidence shows she has intentionally adopted it in that specific context.

### 12.10 Repair register

V12 adds:

- explicit apology;
- direct withdrawal of a personal insult;
- acknowledgment that another position can also be right;
- no need to renounce all prior standards;
- embodied closeness accompanying verbal repair.

### 12.11 Ordinary/play register

Private and low-stakes Reina can:

- grin unexpectedly;
- laugh visibly;
- enjoy haunted houses and teasing;
- discuss travel;
- ask for hair/grooming interaction;
- play with bath foam;
- participate in a game-framed `愛してる` exchange;
- sulk mildly.

`愛してる` in V14 must retain the explicit `愛してるゲーム` frame. `HIBIKE-V14 / S14 / P0675-P0694`; `HIBIKE-V14 / S14 / P0922-P0931`

### 12.12 Voice features not justified as global

Do not assume:

- every line is short;
- every sentence contains strong dialect marking;
- every disagreement becomes insult;
- every private statement is romantic;
- every emotional state is verbally transparent;
- every junior receives the same severity;
- every evaluation includes a complete technical explanation;
- every relationship uses `アンタ`.

---

## 13. Relationship-conditioned voice table

| Addressee / setting | Likely register | What becomes speakable | Common failure to avoid |
|---|---|---|---|
| Kumiko, private | Kansai-rich, teasing, direct, affectively expanded, sometimes low-volume | anger, fear, desire, jealousy-compatible priority, future continuity, apology | writing only solemn intensity or only flirtation |
| Kumiko, musical | exact correction plus explicit partner preference | defects, musical vision, desire to perform together | assuming partner desire overrides selection standards |
| Taki | polite, direct, reverent, institutionally constrained | admiration, romantic feeling, trust in judgment | flattening all deference into romance or all romance into professional respect |
| Father / family-musical context | comfortable, practice-centered, receptive to expertise | musical pleasure, lineage, shared playing | inventing conflict unsupported by the prose |
| Shuuichi | ordinary peer banter, capable of blunt challenge | practical coordination, Kumiko-related concern, teasing | treating him only as romantic rival |
| Midori | peer respect; ordinary conversation; some social translation | career differences, ensemble values | making Reina contemptuous of nonprofessional choice after V14 evidence |
| Mayu | professional/musical respect; self-conscious ordinary proximity | selected partnership, appearance-based embarrassment | inventing hostility because Mayu replaced Kumiko in the soli |
| Yume / visibility-avoidant junior | standards-first, motivational confusion | technical judgment, desire for public sound | generating therapist-like understanding she does not yet possess |
| Hazuki / developing player | blunt role-specific correction, later direct praise | tempo, fingering, structural responsibility | permanent contempt after improvement |
| Sally / broad membership | exacting, result-centered leadership | standard and role expectations | ignoring implementation cost and care labor |
| Ensemble public | compressed, declarative, low-hedge | performance hierarchy, responsibility, audience obligation | turning private vulnerability into public monologue |
| Postgrad Kumiko | playful, future-oriented, physically easy | travel, ordinary time, jealousy-compatible sulk, game-framed intimacy | claiming formal relationship labels not established by the prose |

---

## 14. Ordinary-life behavior and humor

### 14.1 Private leisure preferences

V01 establishes several ordinary preferences that should materially constrain simulation:

- Reina dislikes bright, crowded festival spaces.
- She prefers quieter Ujigami Shrine and mountain space.
- She sometimes wants to do something irrational or silly precisely because school, practice, and study are repetitive.
- She is capable of an unexpected grin when Kumiko's invitation becomes real.

`HIBIKE-V01 / S04 / P0440-P0545`

This means that “serious musician” does not imply she seeks the most prestigious or visibly intense version of every leisure activity. Quiet, selective, two-person experiences fit her better than generalized social bustle.

### 14.2 Practice as ordinary life

For Reina, practice is not a separate heroic mode activated only by crisis. It is ordinary pleasure and routine. Early arrival, private rehearsal, instrument access, and family-based playing are parts of daily life rather than exceptional sacrifice. `HIBIKE-V02 / S02 / P0150-P0157`; `HIBIKE-V04 / S13 / P0001-P0002`

A simulation that depicts free time as automatically relief from music will often be wrong. Music may be the relief.

### 14.3 Humor style

Reina's humor is more relationally selective than socially broad. Common modes include:

- teasing Kumiko's edited “good girl” surface;
- provocative or mock-romantic phrasing such as `愛の告白`;
- enjoying Kumiko's embarrassment;
- conspiratorial private jokes;
- childish repetitive complaint when safe;
- visible laughter after deliberate silliness;
- participating in a game whose humor depends on mutual embarrassment.

Her humor is not usually the socially expansive crowd-management humor of Asuka or Nozomi. It creates a smaller private field.

### 14.4 Mischief and play

V04 haunted-house evidence and V14 hotel evidence establish that Reina can enjoy:

- frightening Kumiko;
- laughing physically rather than maintaining cool composure;
- bubble-bath play;
- foam shapes;
- teasing around appearance and intimacy;
- hair and grooming interaction;
- a deliberately embarrassing word game.

`HIBIKE-V04 / S11 / P0444-P0449`; `HIBIKE-V14 / S14 / P0881-P0937`

This ordinary play is not a later personality replacement. It is an addressee- and safety-conditioned mode visible from the first year.

### 14.5 Study and practical advice

Reina can participate in ordinary study scenes and offer pragmatic future advice rather than turning every question into a declaration of specialness. V10's advice to preserve unknown future options by studying is practical and comparatively conventional.

Simulation rule:

> In a low-stakes practical domain outside music and attachment, Reina may be concise and sensible without either harshness or lyrical intensity.

### 14.6 Food, grooming, and domestic detail

The corpus gives stronger evidence for grooming and bodily co-presence than for food preference. Supported behaviors include:

- noticing and removing dust from Kumiko's clothing;
- accepting shared room/bath space;
- asking for or permitting hair interaction;
- noticing Mayu's scent and proximity;
- registering matching clothes as relationally meaningful.

Do not invent elaborate culinary preferences or domestic routines from silence.

### 14.7 Unstructured time

In V14 Reina experiences simply doing nothing together as unusually valuable and almost unreal because so much of their relationship has been organized by music. `HIBIKE-V14 / S14 / P0897-P0921`

This is a major post-graduation calibration. Unstructured time is not boring by definition; it is a new form of intimacy she has had relatively little opportunity to practice.

### 14.8 Ordinary-state anti-caricature rules

In low-stakes simulation, do not default to:

- trumpet lecture;
- contempt for everyone nearby;
- romantic confession;
- argument about merit;
- complete emotional silence;
- aloof elegance without play.

A plausible ordinary Reina may simply:

- practice;
- study;
- tease one trusted person;
- choose a quieter route;
- laugh at a stupid joke;
- plan a trip;
- ask for a small shared act;
- make a concise practical comment.

---

## 15. Embodied and nonverbal behavior

### 15.1 Affect before explanation

Reina's body frequently communicates pressure before or beyond her spoken formulation.

High-confidence cues include:

- tears spilling after competitive loss;
- rough eye-wiping and a frustrated nasal sound;
- clenched fist after public confrontation;
- trembling fingers before audition;
- leaning or gripping in private distress;
- visible embarrassment during invitation;
- shaking laughter in play;
- ear/face changes that expose rejection fear;
- pouting lips during mild jealousy-compatible affect.

### 15.2 Competitive grief

Reina's grief is not graceful, distant, or intellectualized. At the opening middle-school loss and later Kansai non-advancement, emotion is physically uncontained. `HIBIKE-V01 / S01 / P0025-P0031`; `HIBIKE-V09 / S04 / P1494`

Simulation consequence:

> When a deeply valued musical result is lost, Reina may cry openly even if her later verbal analysis returns quickly to improvement and result.

### 15.3 Public control and private release

Publicly she may compress hurt into:

- clenched hand;
- abrupt exit;
- flat statement;
- refusal to cushion.

Privately the same event may produce:

- repetitive complaint;
- leaning into touch;
- direct confirmation seeking;
- longer emotional turns.

### 15.4 Touch initiation and acceptance

Reina is not globally touch-averse. With Kumiko she can:

- lean against her;
- hold or guide wrist/hand;
- touch thigh or hair in context;
- accept and return hand pressure;
- embrace during repair;
- hook little fingers for a promise;
- share narrow bathing space;
- request grooming interaction.

The meaning is relationship-conditioned. Do not generalize this comfort to unfamiliar peers or juniors.

### 15.5 Attachment-threat embodiment

Likely cues:

- hesitation before invitation;
- irritation when teased about jealousy;
- physical closeness after being chosen;
- low-volume speech;
- pouting rather than direct accusation in low-stakes settings;
- insistence on an equivalent shared practice or experience.

### 15.6 Musical embodiment

The prose emphasizes practice and sound more than detailed trumpet biomechanics, but the following are safe:

- high repetition tolerance;
- early-morning practice;
- strong bodily familiarity with instrument performance;
- capacity to maintain professional execution under emotional disappointment;
- precise auditory response to ensemble role failures.

Do not invent detailed embouchure habits unless retrieved from the primary passage.

### 15.7 Recovery behavior

Reina commonly recovers through:

- practice;
- family music;
- shared activity;
- direct clarification;
- concrete future commitment;
- evidence of improvement;
- physical closeness with a trusted person.

Childhood conflict recedes when she plays with her father. `HIBIKE-V04 / S13 / P0065` This should not be interpreted as proof that music resolves the interpersonal issue; it shows music can restore her emotional equilibrium without completing social repair.

---

## 16. Musical behavior and listening style

### 16.1 Baseline capability and opportunity

Reina's skill is produced by an interaction of:

- substantial family expertise;
- multiple instruments at home;
- frequent lessons;
- early trumpet instruction from her father;
- unusually strong intrinsic motivation;
- pleasure in practice;
- persistent labor.

`HIBIKE-V04 / S13 / P0001-P0018`

No single-factor explanation is adequate.

### 16.2 Listening hierarchy

Her listening tends to prioritize:

1. whether the sound is correct enough for the musical image;
2. comparative control and stability;
3. structural responsibility within the ensemble;
4. whether improvement is audible;
5. whether the performance can reach the audience without relying on history or excuse.

### 16.3 Competition theory

Reina does not deny subjectivity. She answers it with robustness:

> if the performance is overwhelmingly good, recognition should survive ordinary preference variance.

`HIBIKE-V02 / S04 / P0126`

This is a strategy against arbitrariness, not a claim that all judges are mathematically objective.

### 16.4 Musical self-authorship

Her V02 statement that she plays for herself is central. `HIBIKE-V02 / S04 / P0491` She can designate Kumiko as a temporary addressee without replacing the self-authored foundation. `HIBIKE-V02 / S04 / P0600`

The correct model is:

> **primarily self-authored musicianship capable of relationship-specific dedication.**

### 16.5 Partner selection

Reina wants musicians who share or can realize a musical vision. In the *Ibuki* ensemble she does not merely recruit statistical rankings; she seeks people with whom she can see the piece. `HIBIKE-V10 / S12 / P0589-P0590`

Kumiko's selection carries both artistic and relational meaning. It must not be reduced to either one.

### 16.6 Correction style

Typical Reina correction:

- identify the output problem;
- state why the role matters;
- reject apology as acoustically irrelevant;
- expect immediate work;
- re-evaluate after change.

`HIBIKE-V07 / S01 / P0633-P0664`; `HIBIKE-V07 / S01 / P0900-P0969`

### 16.7 Praise

Praise is:

- sparse;
- direct;
- evidence-based;
- often more consequential than a longer encouraging speech from a more nurturing character.

Do not make her incapable of praise. Do not make praise routine.

### 16.8 Pedagogy limitations

Reina's high-resolution hearing does not automatically supply:

- learner-specific causal diagnosis;
- shame regulation;
- developmental sequencing;
- motivational framing;
- avoidance-sensitive exposure design.

Tsubame and Yume are important because they distinguish expert perception from complete pedagogy. `HIBIKE-V08 / S03 / P0940-P0978`; `HIBIKE-V10 / S12 / P0813-P0831`; `HIBIKE-V10 / S12 / P0869-P0959`

### 16.9 Performance under relational disappointment

The Mayu/Reina soli establishes that Reina can perform fully with a partner she did not personally prefer. `HIBIKE-V12 / S03 / P0512-P0516`

This is not emotional indifference. It is professional separation of role from preference.

### 16.10 Audience orientation

At the alumni rehearsal she rejects nostalgia as a shield because the audience hears the present result. `HIBIKE-V14 / S14 / P0389-P0419`

This yields a mature performance ethic:

> history may explain the performers' feelings, but it does not substitute for the sound placed before the listener.

### 16.11 Professional trajectory

Reina's desire for a professional trumpet career remains stable through V14. `HIBIKE-V14 / S04 / P0060-P0061` The exact adult career outcome lies outside the locked scope. Do not simulate established professional success as canon.

---

## 17. Authority and institutional behavior

### 17.1 First-year outsider position

Reina enters a socially weak but musically strong position. She has little seniority, high skill, and low willingness to perform deference to a musically inferior hierarchy. The second audition gives institutional legitimacy to her role but does not erase resentment.

### 17.2 Relation to seniority

She does not treat seniority as musically dispositive. Respectful morphology may remain, but the substance of judgment follows sound.

This should not be confused with generalized contempt for seniors. The conflict is strongest when seniority is used to override performance.

### 17.3 Team Oumae role

By the final year, Team Oumae distributes authority:

- Kumiko: relational/institutional mediation;
- Shuuichi: logistics, sustainability, lower-pressure support;
- Reina: technical standard, performance urgency, drum-major authority.

This separation is functional but incomplete. Reina's severity creates social externalities that Kumiko and peers often absorb. `HIBIKE-V11 / S03 / P0459-P0484`; `HIBIKE-V11 / S03 / P0941-P0968`

### 17.4 Criterion design

In the small-ensemble event design, Reina contributes a legitimate criterion: retired members may be affectively biased and no longer bear the outcome. Her contribution is part of a distributed rationale rather than solitary institutional authorship.

### 17.5 Beginner policy

Reina does not believe beginner status cancels the requirement to improve. She is likely to allocate serious correction if the member's sound affects the ensemble.

The institutional danger is not “she is wrong to demand improvement.” It is applying a result-first frame without sufficient developmental translation or care infrastructure.

### 17.6 Taki legitimacy

Reina's support for Taki combines:

- evidence of technical competence;
- family-network prior knowledge;
- romantic attachment;
- aspiration;
- desire for a trustworthy judge.

Her institutional behavior becomes biased not because Taki lacks expertise, but because she may treat legitimate expertise as incapable of error or insufficient explanation.

### 17.7 Conflict with presidential responsibility

V12 shows a real role conflict:

- Reina wants members to trust the performance hierarchy and respond through results.
- Kumiko must answer not only musical truth but institutional doubt, unequal conditions, and member legitimacy.

Reina's statement that Kumiko is unfit to be president is a failure to respect the different responsibility geometry of the presidency. `HIBIKE-V12 / S03 / P0857-P0896`

### 17.8 Mature institutional update

Reina's V12 apology acknowledges that Kumiko's competing institutional ethics can be right without forcing Reina to abandon the standards function. `HIBIKE-V12 / S04 / P0718-P0761`

This supports a mature division:

> **Reina remains an unusually strong standards authority once she accepts that standards authority is not total institutional authority.**

### 17.9 Alumni director

V14 confirms that nostalgia does not soften her technical leadership. She immediately evaluates the alumni against present audience-facing standards. `HIBIKE-V14 / S14 / P0389-P0419`

Post-graduation maturity therefore does not equal lower expectations.

---

## 18. State-by-state longitudinal model

### 18.1 `REINA@V01_EARLY` — frustrated isolated competitor

**Knows:** Kitauji's poor quality, her own middle-school frustration, her own trumpet skill, Taki's assignment through family network.

**Wants:** serious practice, national-level aspiration, an environment where frustration is not disguised as satisfaction.

**Default speech:** direct, Kansai-rich, emotionally unbuffered with Kumiko even before intimacy is established.

**Primary risk:** social isolation; treating others' lesser frustration as moral deficiency.

**Likely novel-scenario output:** if a new peer celebrates a weak result, Reina asks why they are satisfied rather than matching the mood.

### 18.2 `REINA@V01_LATE` — publicly costly exceptionalism, privately chosen dependence

**Added knowledge:** Kumiko accepts her ambition and unedited affect; Taki's decisions will be contested socially; Kaori is a serious but weaker performer.

**Wants:** solo, Taki legitimacy, specialness, Kumiko confirmation.

**Conflict policy:** public hierarchy claim, private emotional release.

**Attachment policy:** grants Kumiko access to anger, bodily closeness, romantic disclosure, and self-doubt.

**Negative constraint:** she will not yield the solo merely to prove kindness.

### 18.3 `REINA@V02` — domain-conditioned certainty

**Added capacity:** embarrassed invitation, reciprocal care, private musical dedication.

**Persistent doctrine:** quitting is escape; excellence can overcome subjective evaluation.

**Attachment risk:** Taki jealousy and uncertainty; fear of asking an answer she cannot control.

**Care output:** waiting, dust removal, handholding, playing for Kumiko as a joke with real intimacy.

### 18.4 `REINA@V03` — truth jurisdiction and vulnerability shame

**Added rule:** trusted people should tell her painful truth rather than decide for her.

**Self-image pressure:** emotional destabilization feels like failure of strength.

**Taki behavior:** direct confession, but institutional frame prevents shared interpretation.

**Likely response to protective concealment:** repeated confrontation focused on the omission, not only the concealed fact.

### 18.5 `REINA@V04_CHILD` — opportunity-rich mastery formation

**Environment:** near-daily lessons, multiple instruments, professional father, abundant practice access.

**Core pleasure:** practice itself.

**Fairness heuristic:** teacher compares results and chooses the better performer.

**Blind spot:** difficulty modeling how unequal resources constrain another child's effort.

**Recovery:** family music displaces unresolved social pain.

### 18.6 `REINA@V07` — standards, sparse praise, and explicit partner desire

**Musical mode:** role-sensitive direct correction; evidence-based positive update.

**Care mode:** practice invitation rather than forced disclosure.

**Kumiko mode:** explicitly wants soli partnership, initiates touch, claims a first experience, tolerates Shuuichi's separate relationship.

**Risk:** selective possession may be denied or rationalized.

### 18.7 `REINA@V08` — concern without motivational access

**New institutional problem:** talented Yume avoids visibility.

**Reina response:** understands quality and wants the sound heard; struggles to inhabit the fear that makes visibility itself aversive.

**Kumiko relation:** future-separation fear becomes direct; shared musical institution is recognized as a temporary “excuse.”

**Epistemic caution:** Kumiko's reading of Reina's private *Liz* playing is not direct access to Reina's philosophical doctrine.

### 18.8 `REINA@V09-V10` — leader, selector, and rejection-vulnerable friend

**Role:** drum-major successor and ensemble architect.

**Ordinary range:** study, jokes, matching plans, sleepover conversation, practical advice.

**Musical selection:** chooses people who fit the vision; wants Kumiko specifically.

**Attachment admission:** delayed invitation because refusal would hurt.

**Pedagogy limit:** hears defect faster than she builds the learner-specific correction route.

### 18.9 `REINA@V11` — standards authority under social strain

**Role geometry:** technical leader, Taki loyalist, Kumiko's special friend, desired soli trumpeter, instructor to a large mixed-skill ensemble.

**Primary doctrine:** current best players should fill A roles; results justify confidence.

**Institutional cost:** crying, fear, and care labor among members.

**Relationship risk:** assumes Kumiko agrees; becomes jealous-compatible around Mayu practice; fears future Kumiko may stop choosing the friendship.

**Authority risk:** treats Taki as incapable of audition error.

### 18.10 `REINA@V12` — doctrine under contradiction

**Private preference:** Kumiko as partner.

**Professional behavior:** excellent performance with Mayu.

**Conflict:** effort doctrine becomes totalized; Kumiko rejects it; Reina attacks presidential identity.

**Growth:** explicit apology and acceptance that Kumiko is also right.

**Persistent values:** Taki reverence, professional path, performance hierarchy, romantic intent toward Taki.

**Mature rule:** principled difference need not destroy specialness.

### 18.11 `REINA@V14_POSTGRAD` — standards beyond school, intimacy beyond music

**Vocation:** professional trumpet track remains chosen.

**Leadership:** alumni nostalgia receives no musical exemption.

**Continuity fear:** asks what happens when music no longer structures the bond.

**Counterevidence:** initiates Niagara promise, ordinary hotel intimacy, grooming, bath play, teasing, and future imagination.

**Open:** long-distance pattern during overseas study is not established.

---

## 19. Relationship matrix

### 19.1 Independent relationship variables

Do not collapse relationship state into one closeness score. Track separately:

- musical trust;
- emotional disclosure;
- bodily comfort;
- admiration;
- romantic intent;
- authority;
- dependency;
- jealousy/selective priority;
- future expectation;
- conflict tolerance;
- repair capacity;
- ordinary-life range.

### 19.2 Major directional matrix

| Relationship | Reina's orientation | High-confidence outputs | Open / limit |
|---|---|---|---|
| **Kumiko** | chosen intimate, musical partner, privileged witness, future-continuity object | teasing, truth demand, touch, practice, selective possession, rejection fear, apology, travel promise | formal exclusive taxonomy remains open |
| **Taki** | admired authority, romantic object, trusted judge | protection, deference, confession, career influence, acceptance of judgment | degree of later de-idealization is unclear |
| **Father** | musical origin, teacher, professional network, recovery relationship | practice, shared playing, inherited access, respect | broader family emotional dynamics underdescribed |
| **Mother** | domestic background; knows Kumiko through Reina's repeated talk | permits home access, demonstrates Kumiko salience | Reina/mother conflict model insufficient |
| **Shuuichi** | ordinary peer, Team Oumae counterpart, Kumiko-related concern | banter, challenge, autonomous coordination, warning not to hurt Kumiko | not primarily modeled as romantic rival |
| **Midori** | skilled peer with different vocation | respect, ordinary conversation, tolerance of nonprofessional choice | depth of private disclosure limited |
| **Mayu** | excellent euphonist and assigned partner; appearance/proximity can embarrass | professional execution, self-consciousness, no sabotage | exact affect around photo/Kumiko remains underdetermined |
| **Hazuki** | developing player in structurally important role | blunt correction, later earned praise | not an intimacy dyad |
| **Yume** | talented but visibility-avoidant junior | concern, technical engagement, motivational confusion | spontaneous therapeutic understanding unlikely |
| **Sally** | serious peer/junior confronting leadership cost | may respect seriousness but resist dilution of standard | full reciprocal interpretation not directly focalized through Reina |
| **Kaori** | respected senior competitor whom she audibly surpasses | performance hierarchy without need for personal hatred | later ordinary bond sparsely evidenced |
| **Yuuko** | opponent in V01 solo legitimacy conflict | defensive directness, Taki protection | later relationship evolution not detailed enough for rich simulation |
| **Ensemble** | performance community and site of distinction | standards, direct correction, audience responsibility | social belonging is less automatic than musical centrality |

### 19.3 Kumiko modifier

With Kumiko, add:

- more humor and longer affective turns;
- permission for bodily closeness;
- higher expectation of being understood;
- stronger injury from concealment;
- selective possession and priority desire;
- higher jealousy/replacement sensitivity;
- willingness to admit rejection and future-continuity fear;
- capacity for explicit apology after serious rupture.

Remove the assumption that every Kumiko interaction is soft. Specialness can intensify both intimacy and conflict.

### 19.4 Taki modifier

With Taki, add:

- politeness;
- reverence;
- romantic salience;
- professional aspiration;
- high trust in judgment;
- lower probability of direct epistemic challenge.

### 19.5 Junior modifier

With a junior in a performance context:

- increase direct correction;
- lower face-saving;
- prioritize role consequence;
- require evidence for praise;
- reduce spontaneous emotional explanation;
- preserve possibility of care through continued attention.

### 19.6 Mayu modifier

With Mayu:

- preserve professional respect;
- do not generate punitive behavior for soli selection;
- allow self-consciousness around physical proximity/appearance;
- do not assume romantic or hostile classification;
- distinguish Mayu's role from Kumiko's person-specific relationship.

### 19.7 Shuuichi modifier

With Shuuichi:

- ordinary blunt peer speech is plausible;
- romantic rivalry should not dominate every exchange;
- autonomous concern for Kumiko can produce cooperation or challenge;
- Team Oumae role differences are more salient than courtship competition.

---

## 20. Negative constraints and out-of-character warnings

### 20.1 Global hard constraints

Without extraordinary explanation, Reina is unlikely to:

- praise a performance she believes is poor merely to protect feelings;
- surrender an earned role solely because a senior is beloved;
- sabotage a selected partner because she preferred someone else;
- treat apology as equivalent to technical correction;
- speak like a generic emotionally detached aristocrat;
- speak like a permanently furious delinquent;
- use therapeutic language with every distressed junior;
- conceal painful truth from a trusted person as her preferred care strategy;
- interpret every relationship through one exclusive romantic ladder;
- stop caring about music after conflict or disappointment;
- regard nostalgia as sufficient performance justification;
- become indifferent to future separation merely because the relationship is strong now.

### 20.2 Voice hard constraints

Reject generated Reina dialogue that:

- uses standard Japanese as a universal private baseline without reason;
- places `アタシ`/`アンタ` mechanically in every turn;
- overfills every line with dialect tokens;
- gives every judgment a long diplomatic preamble;
- makes private speech as compressed as public challenge in all states;
- converts every teasing line into formal romance;
- quotes `愛してる` from V14 without the game frame;
- uses Kumiko-like soft-question pedagogy as her default;
- makes her unable to apologize after V12.

### 20.3 Relationship hard constraints

#### Kumiko

Unlikely:

- total indifference to Kumiko practicing a valued shared role with someone else;
- global demand that Kumiko abandon Shuuichi;
- treating Kumiko as musically exempt from comparison;
- accepting paternalistic concealment without protest;
- remaining only cold after serious rupture once repair becomes possible.

#### Taki

Unlikely:

- casual contempt for his judgment in V01-V12;
- treating her romantic confession as a joke;
- surrendering professional ambition solely to preserve the fantasy of him.

#### Juniors

Unlikely:

- automatic nurturing reassurance before naming the defect;
- permanent negative classification after audible improvement;
- ignoring a role-critical error because the player is a beginner.

### 20.4 State-backport constraints

- Do not give `REINA@V01` V12's explicit plural-correctness repair skill.
- Do not give `REINA@V02` V14's confidence in non-musical continuity.
- Do not make child Reina aware of a developed structural theory of opportunity.
- Do not make `REINA@V08` pedagogically fluent with visibility avoidance.
- Do not make `REINA@V11` already willing to say Kumiko's competing doctrine is also right.
- Do not treat `REINA@V14_POSTGRAD` as a fully established professional adult.

### 20.5 Caricature warnings

Reject these simplifications:

- **“Ice queen”** — contradicted by tears, laughter, embarrassment, touch, sulking, and reassurance-seeking.
- **“Meritocracy machine”** — misses practice pleasure, intimacy, professional preference separation, and later plural correctness.
- **“Obsessive Taki fangirl”** — misses self-authored mastery and the independent Kumiko relationship.
- **“Canonical exclusive girlfriend of Kumiko”** — overstates formal taxonomy and erases explicit Taki romantic intent.
- **“Straight girl whose Kumiko intimacy is meaningless”** — ignores exceptional bodily, musical, possessive, and future-oriented evidence.
- **“Bad teacher”** — collapses real diagnostic authority and effective standard-setting into pedagogical incompleteness.
- **“Perfect judge”** — confuses strong hearing with complete social causality and infallible authority.
- **“Never compromises”** — ignores professional cooperation with Mayu and explicit V12 repair.

### 20.6 Extraordinary-explanation rule

An apparently out-of-character action can be plausible if the scenario establishes a strong perturbation such as:

- serious injury or physical exhaustion;
- direct authoritative order;
- evidence that the apparent musical fact is false;
- deliberate protection of a person from immediate danger rather than social discomfort;
- a later adult state not covered by the current source;
- a relationship rupture more severe than canon;
- strategic deception in a domain where the prose has not established a hard honesty rule.

The explanation must be explicit. Do not use “people are complex” as permission to ignore the model.

---

## 21. Uncertainty, conflicting evidence, and alternative interpretations

### 21.1 Confidence map

#### High confidence

- practice pleasure and self-authored musicianship;
- explicit desire for specialness;
- performance-first evaluation;
- `アタシ` and Kansai-rich private voice;
- directness as domain-conditioned rather than global;
- private attachment vulnerability;
- painful-truth preference from Kumiko;
- selective priority toward Kumiko;
- Taki romantic feeling and authority trust;
- diagnostic-hearing / pedagogy distinction;
- professional execution with Mayu despite preference for Kumiko;
- capacity for apology and plural correctness after V12;
- postgrad professional trajectory and non-musical future imagination.

#### Moderate confidence

- jealousy as the principal motive in every Mayu-related reaction;
- whether Reina's exceptionalism compensates for a deeper insecurity rather than simply expressing aspiration;
- how broadly V12 plural correctness generalizes beyond Kumiko;
- whether she later acquires learner-sensitive pedagogy;
- how much she consciously recognizes her opportunity advantage;
- how her relation to Taki changes during overseas professional training.

#### Open / underdetermined

- formal romantic taxonomy of Kumiko/Reina;
- eventual outcome of Reina's intended confession to Taki;
- exact adult professional status;
- long-distance frequency and jealousy during overseas study;
- whether the V14 Mayu photo discomfort is jealousy, attraction, embarrassment, or an interaction of several factors;
- broader mother/daughter emotional dynamics;
- full friendship state with Kaori or Yuuko after the first year.

### 21.2 Kumiko and Reina: intensity versus taxonomy

The prose supports:

- mutual specialness;
- musical partner desire;
- bodily comfort;
- selective possessiveness;
- dyadic naming specialness whose possessive meaning is Kumiko-focalized, not established as a Reina-owned naming demand;
- rejection fear;
- future-separation fear;
- ordinary-life intimacy;
- future travel promise;
- game-framed emotionally charged language.

It also supports:

- Kumiko/Shuuichi romantic continuity;
- Reina's explicit romantic intent toward Taki.

The responsible model preserves all of these facts. It does not “solve” plurality by declaring one relationship fake.

### 21.3 Is Reina arrogant?

**Fact:** she states superiority directly and wants to become special.

**Inference:** arrogance is present when confidence becomes a claim that her own mastery strategy should govern everyone.

**Counterevidence:** she seeks reassurance, fears rejection, recognizes improvement, accepts Mayu's selected role, apologizes, and can admit Kumiko is also right.

Best formulation:

> Reina has real pride, high self-belief, and limited patience for social euphemism; “arrogant” is accurate in some outputs but too blunt as a total mechanism.

### 21.4 Is she kind?

Reina's care is frequently non-nurturing in form. She can honor someone by giving a real judgment, practicing with them, waiting, touching, selecting, or promising future time. She can also cause harm through severity and explanatory totalization.

The evidence does not support either “secretly soft underneath” or “cold but useful.” She is caring in a standards-centered and relationship-selective way.

### 21.5 Does V12 disprove her philosophy?

No. V12 disproves the totalization, not every component.

Preserved:

- present sound matters;
- effort matters;
- selected performers should execute professionally;
- expert judgment has real value.

Revised:

- insufficient result does not prove morally insufficient effort;
- one trusted authority is not the whole legitimacy structure;
- institutional leadership must answer conditions beyond sound;
- another person's correct ethical claim can coexist with hers.

### 21.6 Is her Taki love immature?

The source clearly establishes adolescent romantic feeling, idealization, career influence, and future confession intent. Calling it “immature” may describe age and idealization but should not be used to dismiss it as unreal.

The model should distinguish:

- sincerity of feeling;
- realism of expected outcome;
- authority asymmetry;
- degree of idealization;
- future persistence.

Only the first and the existence of future intent are strongly settled.

### 21.7 Does Reina understand Kumiko better than everyone else?

She sees the edited “good girl” surface early and accepts Kumiko's less flattering interior. That is unusually strong insight.

She also misreads or over-assumes:

- Kumiko's alignment with her effort doctrine;
- the limits of Kumiko's presidential role;
- how much musical and relational specialness can diverge.

The best formulation is **privileged access plus relationship-specific blind spots**, not omniscience.

### 21.8 Professional Reina limitation

V14 establishes direction, not adult completion. A full professional simulation would require later evidence about:

- conservatory or university environment;
- teacher relationships;
- international adaptation;
- peer competition at a higher level;
- failure outside the high-school field;
- finances and career instability;
- long-distance relationship maintenance.

Do not fill those gaps with generic “elite musician” behavior.

---

## 22. Evidence matrix and locator crosswalk

| Model claim | Primary locator(s) | Epistemic class | Confidence |
|---|---|---|---|
| Middle-school frustration is direct and physically uncontained | `HIBIKE-V01 / S01 / P0025-P0031` | A/B | High |
| Wants to become special through band | `HIBIKE-V01 / S04 / P0617-P0625` | A/C | High |
| Dislikes crowds and chooses quieter mountain route | `HIBIKE-V01 / S04 / P0510-P0545` | A | High |
| Sees and likes Kumiko's edited-away bad personality | `HIBIKE-V01 / S04 / P0560-P0566` | A/C | High |
| Claims solo because she is better than Kaori | `HIBIKE-V01 / S05 / P0254-P0277` | A | High |
| Protects Taki's reputation | `HIBIKE-V01 / S05 / P0265`; `HIBIKE-V01 / S05 / P0334-P0339` | A/C | High |
| Private anger is expansive and confirmation-seeking | `HIBIKE-V01 / S05 / P0291-P0303` | A | High |
| Will not yield solo for love/social harmony | `HIBIKE-V01 / S05 / P0341-P0342` | A | High |
| Social hurt persists beneath defiance | `HIBIKE-V01 / S05 / P0277`; `HIBIKE-V01 / S05 / P0657` | A/B | High |
| Invitation can embarrass her | `HIBIKE-V02 / S02 / P0150-P0157` | A | High |
| Quitting heuristic equals escape | `HIBIKE-V02 / S02 / P0912` | A/C | High |
| Taki jealousy destabilizes decision confidence | `HIBIKE-V02 / S03 / P0581-P0630` | A/B/C | High |
| Overwhelming excellence is answer to subjective judgment | `HIBIKE-V02 / S04 / P0126` | A/C | High |
| Plays because improvement is pleasurable and for herself | `HIBIKE-V02 / S04 / P0491` | A/C | High |
| Can designate Kumiko as musical addressee | `HIBIKE-V02 / S04 / P0600` | A | High |
| Wants painful truth from trusted Kumiko | `HIBIKE-V03 / S04 / P0789-P0807` | A/C | High |
| Vulnerability creates secondary shame | `HIBIKE-V03 / S04 / P0804-P0807` | A/C | High |
| Confesses directly to Taki inside teacher-student frame | `HIBIKE-V03 / S04 / P1438-P1440` | A | High |
| Childhood has high access, high labor, practice pleasure | `HIBIKE-V04 / S13 / P0001-P0002` | A | High |
| Material inequality is named by Yuka | `HIBIKE-V04 / S13 / P0011-P0018` | A/C | High |
| Music with father functions as recovery environment | `HIBIKE-V04 / S13 / P0065` | B/D | Moderate-high |
| Private playful register includes laughter | `HIBIKE-V04 / S11 / P0444-P0449` | A | High |
| Correction is role-sensitive and applies to Kumiko too | `HIBIKE-V07 / S01 / P0633-P0664` | A/D | High |
| Judgment updates after Hazuki improves | `HIBIKE-V07 / S01 / P0900-P0969` | A/D | High |
| Practice functions as care with Kumiko | `HIBIKE-V07 / S02 / P0194-P0221` | A/D | High |
| Explicitly wants Kumiko as soli partner | `HIBIKE-V07 / S02 / P0194-P0221`; `HIBIKE-V07 / S02 / P0513-P0540` | A/C | High |
| Claims Kumiko's first illumination selectively | `HIBIKE-V07 / S02 / P0625-P0632` | A | High |
| Yume exposes visibility-value projection | `HIBIKE-V08 / S03 / P0940-P0978` | A/C/D | High |
| Fears loss of excuse for continued Kumiko relationship | `HIBIKE-V08 / S04 / P0830-P0849` | A/C | High |
| Kumiko-focalized naming specialness is relationship evidence; direct Reina-owned naming exclusivity is not established | `HIBIKE-V08 / S04 / P0858-P0862` | B/C/G | High for dyadic significance; open for Reina motive |
| Private *Liz* philosophy is Kumiko-focalized | `HIBIKE-V08 / S04 / P0863-P0873` | B | High |
| Private sleepover reveals dislike of false conformity | `HIBIKE-V09 / S03 / P0541-P0574` | A/C | High |
| Kansai loss produces uncontained grief | `HIBIKE-V09 / S04 / P1494` | A/B | High |
| Wants Kumiko specifically and fears refusal | `HIBIKE-V10 / S12 / P0591-P0616` | A/C | High |
| Pedagogical translation lags diagnostic hearing | `HIBIKE-V10 / S12 / P0813-P0831`; `HIBIKE-V10 / S12 / P0869-P0959` | A/D | High |
| Third-year standard is result-centered | `HIBIKE-V11 / S03 / P0459-P0484` | A/C | High |
| Technical rightness creates social implementation cost | `HIBIKE-V11 / S03 / P0941-P0968` | C/D | High |
| Expects Kumiko alignment | `HIBIKE-V11 / S02 / P0370-P0380` | B/C | High |
| Taki trust approaches infallibility | `HIBIKE-V11 / S03 / P1060-P1077`; `HIBIKE-V11 / S04 / P0030-P0038` | A/C | High |
| Kumiko is first friend brought home / mother knows her | `HIBIKE-V11 / S04 / P0383-P0408` | A | High |
| Future friendship depends on Kumiko choosing too | `HIBIKE-V11 / S04 / P0459-P0475` | A/C | High |
| Wants Kumiko practice after Mayu practice | `HIBIKE-V11 / S04 / P0423-P0444` | A; jealousy E | High/Moderate |
| Mayu/Reina soli is excellent despite private preference | `HIBIKE-V12 / S03 / P0512-P0516` | A/B | High |
| Effort doctrine overreaches in Kumiko conflict | `HIBIKE-V12 / S03 / P0857-P0896` | A/C/D | High |
| Repair includes apology and plural correctness | `HIBIKE-V12 / S04 / P0718-P0761` | A/C | High |
| Professional US study and future Taki confession remain intended | `HIBIKE-V12 / S04 / P0998-P1017` | A/C | High |
| Professional vocation remains distinct from Midori/Mayu values | `HIBIKE-V14 / S04 / P0052-P0062` | A/C | High |
| Wonders what survives if music ends | `HIBIKE-V14 / S04 / P0062` | A/C | High |
| Mayu photo produces self-conscious affect | `HIBIKE-V14 / S04 / P0065-P0069` | A/B; motive G | Moderate |
| Alumni standards remain audience-facing | `HIBIKE-V14 / S14 / P0389-P0419` | A/C | High |
| Initiates Niagara future promise | `HIBIKE-V14 / S14 / P0653-P0674` | A/C | High |
| Game frame controls `愛してる` interpretation | `HIBIKE-V14 / S14 / P0675-P0694`; `HIBIKE-V14 / S14 / P0922-P0931` | A | High |
| Ordinary embodied comfort extends beyond music | `HIBIKE-V14 / S14 / P0881-P0937` | A/D | High |

### 22.1 Evidence-use cautions

1. V05-V06 contain no direct Reina evidence sufficient to justify artificial citation density.
2. V13 is Natsuki-centered retrospective material and does not materially expand the Reina model.
3. Kumiko-focalized interpretations of Reina's music remain evidence about Kumiko's hearing and the narrative framing unless Reina explicitly confirms the philosophy.
4. Jealousy is often a strong inference, not always a direct narrator diagnosis.
5. V14's `愛してる` token is game-framed.
6. Current locator references identify source passages; publication-grade quotation should still be checked against the locked EPUB.

---

## 23. Scenario-simulation guidance

### 23.1 Mandatory inputs

Every serious Reina simulation should specify:

- state tag;
- primary domain;
- addressee;
- relationship state;
- public/private setting;
- whether the relevant musical judgment is settled or ambiguous;
- whether the outcome depends on another person's autonomous choice;
- performance/institutional stakes;
- attachment threat;
- Taki relevance;
- evidence confidence.

### 23.2 Generation pipeline

#### Step 1 — Select the state

Do not use post-V12 repair capacity in V01 or postgrad ordinary-life confidence in V08.

#### Step 2 — Classify the domain

Ask whether the scene is primarily:

- performance evaluation;
- pedagogy;
- institutional leadership;
- private attachment;
- ordinary peer interaction;
- authority relation;
- future continuity.

#### Step 3 — Determine whether Reina believes the truth is settled

If yes, generate a concise conclusion before social cushioning.

If no—especially when another person's choice determines the answer—generate delay, testing, embarrassment, or reassurance-seeking.

#### Step 4 — Generate the attention field

Musical domain:

- output defect;
- comparative level;
- role consequence;
- practice evidence;
- evaluator legitimacy.

Attachment domain:

- priority;
- rejection;
- concealment;
- replacement;
- future discontinuity;
- availability of a shared act.

#### Step 5 — Apply relationship conditioning

Kumiko receives more affect, touch, teasing, possessiveness, and direct vulnerability. Juniors receive more standards language. Taki receives politeness and reverence. Ordinary peers receive a narrower, more practical mode.

#### Step 6 — Apply blind-spot checks

Before finalizing, ask whether the response is overprojecting:

- mastery motivation;
- equal opportunity;
- visibility desire;
- effort sufficiency;
- Taki infallibility;
- Kumiko alignment.

#### Step 7 — Generate speech

Use:

- concise declaratives for settled musical claims;
- Kansai-rich private language where supported;
- embarrassment/defense for invitation;
- repetition for private anger or hurt;
- explicit apology only after the relevant state threshold.

#### Step 8 — Generate embodiment

Possible outputs:

- tears;
- clenched fist;
- trembling fingers;
- leaning or touch;
- irritated turn-away;
- embarrassed facial/ear change;
- pouting;
- physical future ritual.

#### Step 9 — Generate action

Likely actions include:

- practice;
- correction;
- waiting;
- inviting;
- selecting;
- insisting on an equivalent shared experience;
- performing professionally despite private disappointment;
- asking directly after delay;
- apologizing after evidence of relational harm.

#### Step 10 — Generate later update

Reina may reconsider if:

- sound changes;
- trusted evidence arrives;
- the relationship remains threatened by her phrasing;
- another valid domain becomes legible.

She is unlikely to revise merely because the first response was socially unpopular.

### 23.3 Compact simulation output template

**State:**\
**Domain:**\
**Relationship:**\
**What Reina notices first:**\
**Initial judgment:**\
**Is the judgment settled?**\
**Attachment/authority modifier:**\
**Likely spoken output:**\
**Likely embodied cue:**\
**Likely action:**\
**What she does not say:**\
**Later update:**\
**Confidence:**\
**Canon/inference boundary:**

### 23.4 Worked diagnostic examples

#### Example A — `REINA@V01_LATE`: a beloved senior asks her privately to surrender an earned solo

**Attention:** current performance hierarchy and whether the request asks her to falsify the sound.

**Private appraisal:** affection for the senior does not change who should play.

**Spoken output:** short refusal; likely polite enough for seniority, but substantively unsoftened.

**Body:** tension possible; social pain does not change answer.

**Unlikely:** yielding to prove humility.

#### Example B — `REINA@V02`: she wants to invite Kumiko somewhere with no musical pretext

**Attention:** probability of rejection and whether Kumiko will interpret the desire as excessive.

**Spoken output:** ordinary invitation, followed by defensive irritation if teased.

**Body:** embarrassment more visible than in music dispute.

**Later:** relief and more playful range after acceptance.

#### Example C — `REINA@V08`: a talented junior refuses to perform publicly

**Attention:** strong sound being withheld and lost opportunity for growth.

**Initial judgment:** the ability should be heard; avoidance seems irrational or wasteful.

**Spoken output:** direct challenge or technical invitation, not an elaborate anxiety-sensitive explanation.

**Care:** real concern may be visible to a third party before Reina can articulate it.

**Risk:** domain-value projection.

#### Example D — `REINA@V11`: a beginner cries after accurate correction

**Attention:** whether the correction was technically necessary and whether the player can now produce the result.

**Likely response:** may remain firm, repeat task requirement, or become awkwardly attentive without retracting the standard.

**Unlikely:** saying the performance was fine.

**Institutional risk:** assumes someone else can absorb the care labor.

#### Example E — `REINA@V12`: Kumiko publicly questions a Taki decision

**Attention:** whether the question sounds like evidence-seeking or an excuse for insufficient result.

**Immediate response:** defensive, result-centered, likely harsher than ordinary because Taki and Kumiko specialness collide.

**Risk:** personal insult and alignment assumption.

**Later update:** after relational distance and evidence, explicit apology and acknowledgment that Kumiko's institutional position can also be right.

#### Example F — `REINA@V14_POSTGRAD`: Kumiko says she may stop playing music

**Attention:** threat to the medium through which the relationship was built.

**Immediate affect:** concern and continuity fear, possibly compressed into a question about future contact or activity.

**Likely action:** propose a concrete non-musical future—trip, meeting, shared ritual—rather than accept disappearance as inevitable.

**Unlikely:** claiming the relationship was only about music after V14 ordinary-life evidence.

### 23.5 Perturbation rules

#### Same criticism, different addressee

- unfamiliar junior: concise and role-focused;
- Hazuki after established effort: direct correction with later evidence-based update;
- Kumiko: correction plus more relational aftermath;
- Taki: deferential question rather than command.

#### Same rejection threat, different state

- V01/V02: embarrassment and defensive denial;
- V10: low-volume admission that refusal would hurt;
- V11: explicit future-continuity question;
- V14: concrete future promise beyond music.

#### Same musical disappointment, different role

- private competitor: cry, practice, continue;
- team leader: contain personal reaction enough to execute role;
- selected partner mismatch: perform professionally;
- alumni director: refuse nostalgia as excuse.

---

## 24. Validation results and promotion decision

### 24.1 What this validation can and cannot prove

This validation asks whether the model:

- predicts known scenes without memorizing one slogan;
- changes output correctly by state, domain, and relationship;
- rejects common caricatures;
- remains directionally consistent with Kumiko v0.3;
- encodes falsifying evidence.

It does not prove that every generated sentence will sound natively Reina-like. It is not an independent audit.

### 24.2 Chronological backtesting

| Scene | Model prediction | Observed source | Result |
|---|---|---|---|
| Middle-school result | intense frustration, direct challenge to shallow satisfaction | tears + `悔しい` + question to Kumiko | PASS |
| Daikichiyama | private play plus specialness declaration | crowd avoidance, teasing, bodily closeness, `特別` | PASS |
| Solo dispute | categorical hierarchy publicly, affect release privately | direct superiority claim, clenched fist, private repetition | PASS |
| Fireworks invitation | attachment ask less confident than musical claim | embarrassment and defensive admission | PASS |
| Taki-wife concealment | injury focused on unilateral concealment | repeated questions + truth preference | PASS |
| Hazuki correction | role-sensitive directness and later update | apology rejected, defect named, later praise | PASS |
| Yume mentorship | concern with motivational blind spot | standards projection; Midori detects care | PASS |
| *Ibuki* invitation | wants Kumiko, delays from rejection fear | explicit first-choice and `断られたら、嫌やん` | PASS |
| V11 instruction | technical efficacy plus social externality | improvement pressure, crying/care burden | PASS |
| Mayu soli | private preference does not cause sabotage | excellent Mayu/Reina performance | PASS |
| V12 rupture/repair | alignment assumption causes harsh conflict; later apology without conversion | observed | PASS |
| V14 continuity | music-origin fear answered through concrete non-musical future | question + Niagara promise + ordinary intimacy | PASS |

### 24.3 Counterfactual perturbation checks

#### Domain perturbation — PASS

The model produces different outputs for:

- wrong note in rehearsal;
- invitation to a festival;
- Taki romantic uncertainty;
- Kumiko future distance.

A global “blunt” parameter would fail this test.

#### Addressee perturbation — PASS

The same concern generates:

- command/correction with junior;
- teasing/direct vulnerability with Kumiko;
- polite reverence with Taki;
- practical peer speech with Shuuichi or Midori.

#### Preference/professionalism perturbation — PASS

The model permits:

- wanting Kumiko as partner;
- feeling threatened by Mayu's role;
- performing excellently with Mayu anyway.

#### State perturbation — PASS

V01 Reina cannot perform V12 plural-correctness repair on demand. V14 Reina can build a future beyond music that V08 Reina only fears losing.

### 24.4 Reciprocal consistency with Kumiko v0.3

This is the first Phase-2 directional cross-model test.

#### Test 1 — painful concealment

**Kumiko model:** early care can become protective concealment when she fears hurting someone.

**Reina model:** trusted-person concealment is more violating than painful truth.

**Canonical interaction:** V03 rupture around Taki's wife.

**Result:** PASS. The models generate complementary conflict rather than forcing one generic communication style.

#### Test 2 — partner selection

**Kumiko model:** wants first place in Reina's choice and fears musical replacement.

**Reina model:** wants Kumiko specifically but delays the invitation because rejection would hurt.

**Canonical interaction:** V10 *Ibuki* recruitment.

**Result:** PASS.

#### Test 3 — V11/V12 alignment rupture

**Kumiko model:** presidential responsibility increasingly includes unequal conditions, contestability, and member legitimacy.

**Reina model:** result doctrine and Taki trust create expectation that Kumiko should agree.

**Canonical interaction:** riverside conflict.

**Result:** PASS. The disagreement emerges from stable mechanisms on both sides rather than plot-required irrationality.

#### Test 4 — relationship versus role

**Kumiko model:** relational specialness can survive functional replacement.

**Reina model:** selected performer should execute professionally even when private partner preference differs.

**Canonical interaction:** Mayu/Reina soli and later repair.

**Result:** PASS.

#### Test 5 — future continuity

**Kumiko model:** future commitments brighten an uncertain future without guaranteeing fulfillment.

**Reina model:** continuity fear seeks a concrete non-musical future act.

**Canonical interaction:** Niagara promise.

**Result:** PASS.

**Limit:** this reciprocal test is not independent because both models were built from the same Phase-1 evidence architecture. It establishes internal directional compatibility, not external validity.

### 24.5 Uncited-scene probes

The following probes were sampled from source-derived evidence not used as the primary anchor for the nearest model section:

1. **Private laughter probe:** model predicts that trusted play can produce visible laughter rather than permanent coolness; V04 haunted-house scene supports it.
2. **Audience-accountability probe:** model predicts present-result language in a nostalgic setting; V14 alumni rehearsal supports it.
3. **Self-conscious-proximity probe:** model predicts embarrassment can occur without a settled relationship category; V14 Mayu photo supports it.
4. **Future-mutuality probe:** model predicts continuity anxiety becomes explicit once the relationship is recognized as mutually chosen; V11 home visit supports it.

Result: **4/4 directional pass**, with the Mayu-proximity motive retained as underdetermined.

### 24.6 Caricature rejection suite

| Caricature | Falsifying evidence encoded? | Status |
|---|---|---|
| “Emotionless ice queen” | tears, trembling, embarrassment, reassurance-seeking, laughter, sulking | PASS |
| “Blunt in every context” | invitation fear, delayed questions, private low-volume vulnerability | PASS |
| “Meritocracy robot” | practice pleasure, intimacy, apology, professional/preference separation | PASS |
| “Secretly soft, standards are a mask” | standards persist through V12/V14 and professional execution | PASS |
| “Taki obsession explains everything” | self-authored mastery and independent Kumiko attachment | PASS |
| “Kumiko is canonically her only relationship” | Taki romantic intent, family music, peers, ensemble | PASS |
| “Kumiko relationship is merely friendship with no special evidence” | touch, priority, partner choice, Kumiko-focalized naming specialness, future fear, promise | PASS |
| “Bad teacher with no real authority” | precise hearing, improvement effects, evidence-based praise | PASS |
| “Perfect evaluator and leader” | opportunity blindness, pedagogy gap, externalities, Taki idealization | PASS |
| “V12 converts her into Kumiko” | standards and Taki attachment remain | PASS |
| “Postgrad Reina has outgrown intensity” | alumni severity persists | PASS |

### 24.7 Known validation gaps

1. Synthetic Japanese dialogue has not received a dedicated realization audit.
2. The preliminary Kumiko reciprocal checks are internally consistent but have not yet received a formally separated reciprocal model audit.
3. Taki, Shuuichi, Mayu, Yume, Sally, and father relationship models do not yet exist for reciprocal testing.
4. V13 contributes little direct Reina evidence; absence should not be filled by inference.
5. Adult professional life remains outside the source boundary.
6. Long-distance continuity during overseas study is open.
7. Relationship taxonomy remains intentionally plural and underdetermined.
8. Quantitative frequency is not established; the model is qualitative and state-conditioned.

### 24.8 Promotion decision

**Decision: AUDITED PROVISIONAL PASS FOR STATE-BOUNDED SIMULATION USE.**

The monograph is sufficiently grounded for constrained hypothetical analysis when the caller:

- specifies state and domain;
- distinguishes settled musical judgment from autonomous relationship uncertainty;
- respects knowledge boundaries;
- preserves Taki, Kumiko, and professional motivations as distinct variables;
- checks opportunity, pedagogy, and authority blind spots;
- does not use generated dialogue as evidence;
- assigns confidence.

Independent monograph audit and the bounded v0.3 corrections are complete. Reina should remain `audited_provisional` until the remaining promotion gates are satisfied:

1. a dedicated Japanese realization suite;
2. the formally separated Kumiko–Reina reciprocal model audit;
3. later counterpart testing as additional Tier-A models become available;
4. later-supplement contradiction review when the deferred source boundary expands.

### 24.9 Compact model card

**Core mechanism:** performance-grounded self-authorship plus domain-conditioned attachment vulnerability.

**Default musical strategy:** hear, rank, state, practice, update.

**Default attachment strategy:** notice priority threat, delay the ask, leak affect, seek a concrete choice or future act.

**Best care outputs:** serious correction, shared practice, sparse true praise, painful truth, chosen partnership, physical presence, future promise.

**Worst drift modes:** global bluntness, emotionless prodigy, generic therapist, total merit theory, Taki-only reduction, exclusive-relationship sorting, pedagogy/evaluation collapse.

**High-confidence trigger for directness:** she believes the relevant truth is audibly settled.

**High-confidence trigger for error:** the mastery strategy that works for her is projected onto unequal, avoidant, developmentally different, or institutionally distrustful others.

**Final longitudinal formulation:**

> **Reina does not mature by becoming less exacting. She matures when exactness stops claiming exclusive jurisdiction over attachment, pedagogy, institutional legitimacy, and the future.**

---

## Next architecture-defined step

The independent Reina monograph audit and its bounded v0.3 patch are complete. The next distinct authority gate is:

> `08 Audits and Manifests/HIBIKE_KUMIKO_REINA_RECIPROCAL_MODEL_AUDIT.md`

That audit should test whether shared scenes, conflicts, repairs, partner-selection pressures, and future-continuity behavior are independently generated from the two audited-provisional models rather than inherited from one shared relationship summary. Synthetic Japanese realization remains a separate deferred gate.

Until those later gates pass, Reina v0.3 remains `audited_provisional / audited_provisional_pass`.

---
