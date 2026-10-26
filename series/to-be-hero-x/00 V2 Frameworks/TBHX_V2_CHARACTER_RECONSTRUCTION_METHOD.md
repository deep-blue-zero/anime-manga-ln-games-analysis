---
title: "To Be Hero X V2 — Character Reconstruction Method"
series: TBHX
artifact_type: governing_method
artifact_role: project_character_reconstruction_method
generation: V2
version: "1.0"
status: canonical
method_lifecycle: INITIAL
scope: Source-bounded, time-indexed behavioral, decision, speech, relationship and performance modeling of To Be Hero X Season 1 characters for Phase-5 Document 20 and any later subject-specific operational models
adapted_from: governance/analytical-methods/GENERIC_CHARACTER_RECONSTRUCTION_METHOD.md (v1.0, opt-in corpus reference)
governing_method: TBHX_V2_ANALYTICAL_METHOD.md
synthesis_architecture: TBHX_V2_MULTI_DOCUMENT_SYNTHESIS_ARCHITECTURE.md
current_entrypoint: TBHX_CURRENT_STATE_AND_CORPUS_MAP.md
source_boundary: Methodological artifact with no new source findings; applies to the admitted Mandarin-primary Chinese-original audiovisual Season 1, Episodes 1-24, and the project's accepted evidence about it
do_not_use_as_literary_evidence: true
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
created: 2026-10-25
last_updated: 2026-10-25
---

# To Be Hero X V2 — Character Reconstruction Method

## 0. Authority and boundaries

This method governs how the *To Be Hero X* V2 corpus converts mature, source-grounded understanding of its characters into **conditional behavioral and speech models**. It is the governing method for Phase-5 Document 20, `20_CHARACTER_BEHAVIOR_PERSONALITY_SPEECH_AND_SITUATIONAL_MODELING_REFERENCE.md`, and for any subject-specific operational model the project later writes. The synthesis architecture (v1.5, Phase 5 and §10) places it; this document states how the work is done.

It is adapted from the opt-in corpus reference `governance/analytical-methods/GENERIC_CHARACTER_RECONSTRUCTION_METHOD.md`. The generic reference supplies the model structure, the evidence-distance scale and the validation vocabulary. This method adds what the TBHX source demands: offices that outlive their bearers, presentations that are not separate persons, a broadcast order that withholds causes, retrospective disclosure that must not leak backward, a Mandarin-primary voice layer, an audiovisual performance layer whose inspection routes differ in kind, and a world in which public belief is itself causal.

What this method is not:

- **Not canon.** A prediction about what a character would do in an unshown situation is an inference. It never becomes a source fact, a claim key or evidence about the character.
- **Not the literary authority.** The Phase-3 specialists 06–16 explain characters as literary subjects, and the Phase-2 ledgers and claim register carry current claim authority. Models are derived from them and route back to them (§2).
- **Not a capability assessment.** The project describes evidence coverage, maturity, deficits and validation results. It never assigns the reconstruction evaluator's overall A–E tiers, dimension grades or scenario-readiness states, and no TBHX task edits `characters/reconstruction_capabilities.jsonl`, `characters/CHARACTER_RECONSTRUCTION_INDEX.md` or any partition under `characters/registry/`. Those belong to the reconstruction evaluator and the character discovery agent under their maintenance policies.
- **Not role-play.** A model that produces fluent dialogue it cannot trace to source behavior has failed, however convincing it sounds.

The governing principle is:

> **A TBHX character model predicts what a specific person, in a specific state, with a specific knowledge boundary, is likely to notice, value, decide, say and do — conditionally, with named exceptions and named limits — and it can always answer which source behavior supports the prediction and when the source does not decide.**

---

## 1. Purpose: the questions a model must answer

For a bound state of a sufficiently evidenced character, a model estimates:

1. what the character notices first in a situation;
2. how the character interprets it;
3. what the character values, fears and finds humiliating, unjust, admirable or binding;
4. what the character wants;
5. how the character chooses among competing priorities;
6. what the character is likely to say;
7. how that speech is shaped by the relationship and the setting;
8. what the character is likely to do;
9. how the character responds to the consequences;
10. what pushes the character away from ordinary behavior;
11. when the available evidence is too thin to predict usefully.

The last question is not optional. A TBHX model must be able to say: **“Several responses are plausible; the available source does not distinguish them reliably.”** Where the source does rank alternatives, the model may give an ordinal ranking and name the contextual variable most likely to decide among them. It never assigns numeric probabilities.

---

## 2. Position in the corpus: literary authority and derived prediction

| Artifact | Responsibility | Authority | Canonical home |
|---|---|---|---|
| Phase-3 specialists 06–16 | Characters and relationships as literary subjects: development, ethics, wounds, relations, failure modes | Literary interpretation, subordinate to evidence and claim authority | `03 V2 Specialist Syntheses/01 Characters and Relationships/` |
| Phase-2 ledgers and claim register | Current claim wording, confidence and state | Current claim authority | `02 V2 Longitudinal Ledgers/` |
| Documents 17–19 | Lexical voice; visual form and embodiment; sound and vocal performance | Specialist authority within their stated evidence boundaries | `03 V2 Specialist Syntheses/03 Language Audio and Visual Form/` |
| Reconstruction evidence ledger | Retrieval map of source observations grounding behavior and speech rules (§11) | Evidence routing, not interpretation | §11 |
| Operational model | Time-indexed dispositions, states, rules, speech, relationships, limits and counterexamples (§8) | Derived inference | Document 20; later subject models (§11) |
| Validation records | Prediction freezes, tests, adjudications, fidelity audits (§12) | Test records | §11 |
| Document 20 | Series-wide integration of the operational layer, coverage tiers and retrieval routes (§13) | Derived reference | as Document 20 |

**Direction of correction.** When a model and the literary corpus disagree, the disagreement is resolved in the literary corpus through the claim-revision system, and the model follows. A model never revises a monograph by implication, and a monograph does not certify a model.

**The synthetic-output firewall.** Model predictions, simulated scenes and generated dialogue are never evidence. They may be tested against the source; they may not be cited as source, used to strengthen a claim, or counted as a validation success for themselves.

---

## 3. Subject, office, presentation and attribution

TBHX repeatedly separates four things that ordinary characterization merges. Every model keeps them apart.

| Layer | Question | Examples |
|---|---|---|
| **Subject continuity** | Which person is this? | Lin Ling and Original Nice are distinct subjects; the veteran E-Soul and Yang Cheng are distinct subjects. |
| **Office or role** | Which socially constituted position does the person occupy? | Nice as brand, ranked office and Trust-constituted body; E-Soul as trans-bearer hero identity; X as ranked apex office; the Sacred Maiden role; Lucky Cyan. |
| **Presentation** | How is the person rendered or presented in a scene? | X's civilian presentation (black hair, glasses, suit) and public presentation (white/silver hair); Luo Li's suit and helmet; masks; render-state changes. |
| **Attribution** | What do other characters, publics and institutions believe about the person? | Public belief in Demon King Zero; the sole-credit story around A-Hu; FOMO personas; `怪物` classification of Big Johnny. |

Rules:

- **One office, several subjects.** Lin Ling and Original Nice are not collapsed into one psychological subject because both occupy the public Nice role. E24 foregrounds Lin Ling and a cracked Nice figure separately; personal continuity between that figure and Original Nice remains open, and no model assumes it.
- **One subject, several presentations.** X's civilian and public presentations are modeled as role- and state-conditioned presentations of one bearer. The public office does not exhaust his private personality: ordinary work, friendship, privacy and refusal of overtime are constitutive of the person (Specialist 15, `P2-CR-CH14`, `P2-CR-P16`).
- **Shared problem, distinct subjects.** X and Zero are not interchangeable because both occupy the series' apotheosis problem. Zero is a historical subject known through X's authored history-space testimony and the Commission's public history; X is a present subject with ordinary-life evidence.
- **Address is not identity.** `岩叔` is an address to Yan Mo, not his name; `尚总` addresses Shang De. Use the canonical Mandarin-primary analytical names in `TBHX_NAME_LOCALIZATION_CROSSWALK.md`.
- **Belief about a person is evidence of the believer.** A public, institution or character's account of someone is attribution evidence (`OS`/`RB` in §6), not a disposition of the person described.
- **Non-human and transformed subjects keep subjecthood.** A-Hu's personhood precedes heroization and human-legible speech; Big Johnny's danger does not make `怪物` an adequate total ontology. A model may record limited speech evidence without treating the subject as less of a person.

---

## 4. Time-indexed states

### 4.1 State notation

Every model binds one state, written `Subject@State`. Because TBHX narrates out of chronological order, a state carries two coordinates:

```yaml
state: <Subject>@<diegetic state label>
diegetic_anchor: <the diegetic boundary, e.g. "before first manifestation", "after leaving the orphanage">
first_shown: <broadcast episode where the state first appears>
disclosed_through: <latest broadcast episode whose disclosures the model uses about this state>
```

Examples of the form (not completed models): `Yang-Cheng@pre-awakening` (diegetic anchor: before the E05 first manifestation; first shown E05); `Original-Nice@pre-E01-collapse` (first shown across E01 and E21–E23; disclosed through E23); `Qing@post-escape-busker` (first shown E09); `X@civilian-E24-eve` (first shown E24).

A late state may use earlier evidence as history, labeled as such. An earlier state may never be explained by later knowledge that the character did not have (§5).

### 4.2 State families the source requires

TBHX characters occupy states such as:

- before an institution assigns a heroic role;
- during an imposed or chosen public identity;
- during a specific crisis;
- after a traumatic event;
- after a meaningful relationship change;
- after learning information previously unavailable to them.

The underlying person continues through all of them. Yang Cheng before awakening and Yang Cheng as E-Soul are one person whose powers, expectations, obligations and knowledge change; the source shows him pursuing the rescue while powerless, so agency precedes amplification and the awakening is not modeled as a change of disposition.

### 4.3 Change classes

Each difference from a prior state carries one or more change classes:

| Class | Meaning | TBHX illustration |
|---|---|---|
| `DISPOSITION` | A durable change in temperament or values | Lin's later self-naming is a genuine development, not retrojected into E01 |
| `KNOWLEDGE` | New information changes appraisal | Qīng after the cabin recorder (E10); X's revised account of his own beginning (E24) |
| `RELATIONSHIP` | A relation is formed, broken or redefined | X/A-Hu adversarial trust at E24 |
| `CONTEXT` | Situation, institution or public field changes | Trust hardening Ghostblade's silence into a public and relational constraint |
| `ROLE` | Office or presentation changes | Lin's E01 role adoption as Nice; Qīng's movement from Sacred Maiden to Lucky Cyan |
| `RESOURCE` | Capacity, power or material means change | Yang's first manifestation; A-Hu's post-awakening outward speech |
| `REVEALED_NOT_NEW` | The story discloses late something already operative | Original Nice's genuine admiration for Smile, disclosed in E21 about a pre-E01 state; Ghostblade's silence predating herohood |
| `UNRESOLVED` | The source does not decide | Continuity between Original Nice and the E24 cracked Nice figure |

**Development versus disclosure.** Before tagging a change, ask: was the trait operative before the episode that reveals it? Does any earlier scene show it working? Does the character's own later account claim it was always there, and is that account independently supported? A trait disclosed late but already operative is `REVEALED_NOT_NEW` and must not be modeled as growth; a trait first enacted late is development and must not be pushed backward into earlier states.

---

## 5. Knowledge and epistemic state

A character's behavior depends on what that character knows at that state. Each model records a **knowledge-state table**: what the character knows, believes falsely, suspects, or does not know, at the bound state, with the evidence for each entry.

Keep these partitions separate:

| Partition | Question |
|---|---|
| Character knowledge | What does this person know at this state? |
| Other characters' knowledge | What do particular others know, and do they share it? |
| Public knowledge | What has been narrated publicly, and to which public? |
| Institutional knowledge | What does the Commission, an office, a platform or a laboratory hold? |
| Broadcast-boundary audience knowledge | What could a viewer know at that episode? |
| Mature-corpus knowledge | What the full-season analysis now knows |

Rules:

- **No backward leakage.** E24 knowledge may not appear in a simulation of a character as they existed at E09. Whatever E24 later discloses about the nighttime coin donor of E09, for example, Qīng at E09 acts without that knowledge, and the prospective uncertainty of the frozen E09 reading remains its own historical fact.
- **Public is not private.** The public Demon King Zero account is not what X knows; the sole-credit story is not what A-Hu knows.
- **Retrospective explanation is not conscious reason.** A motive the corpus reconstructs later does not become the earlier character's conscious reason for acting unless the source shows the character holding it.
- **Account for concealment, misleading public narratives, incomplete witness information, mistaken identity, role assignments, selective disclosure and retrospective revelation.** Typical TBHX hazards include Nuonuo's belief that her father had died (false, but her experienced absence is real), Xiao Qiang's suspicion of Vortex while the broadcast audience already knows who killed A-Sheng, X's coworkers not knowing who sits beside them, and A-Hu knowing X's civilian identity while withholding it from disclosure even as he proposes preventive assassination.
- **Shared history is not personal knowledge.** X's history-space shares an account with A-Hu at E24; before that, A-Hu does not hold it, and after it A-Hu holds X's authored account, not an independently verified archive.

Broadcast order and diegetic chronology remain distinct throughout. A model may be built for an early diegetic state that the source only shows late; its knowledge boundary is the diegetic one.

---

## 6. Evidence

### 6.1 Four kinds of evidence

| Kind | What it is | TBHX classes | Generic classes |
|---|---|---|---|
| Source dialogue and observable action | What the character says and does on screen | `F-DLG`, `F-VIS`, `F-MOTION`, `F-AUD` | `DS`, `DB`, `PF` |
| Self-report, claimed intention, narrated perspective | The character's own account, voice-over or narration | `F-DLG` recorded as self-report | `NI` (viewpoint-bound) |
| Others' descriptions and institutional classification | What other characters, publics and institutions say about the character | `F-DLG`, `F-INST` recorded as attribution | `RB`, `OS` |
| Analyst inference about unobserved inner states | Best explanation of several observations | `INF`, `INT` | `INF` |

These are different routes, not one. A self-report is evidence of what the character says about themself. Another character's report of a motive is evidence of that belief. A rule that rests only on attribution or inference says so.

### 6.2 Text layer versus performance layer

- **The Mandarin text layer establishes wording.** Displayed hardsubs in the native WEB frames are the lexical witness of record; reconstructed OCR is navigation; Japanese and English tracks are secondary witnesses and never Mandarin register authority. Quotations used to ground voice rules meet analytical method §5.4 (quote-grade rule).
- **Text does not establish performance.** A subtitle cannot establish pitch, vocal tension, breath, pause duration, laughter quality or a specific emotional delivery. Spoken `ta` does not mark gender; a written `他/她/它` distinction is textual evidence only (analytical method §5.2).
- **A model may hold a good discourse-voice profile without an acoustic profile.** Document 17 supplies discourse voice. An acoustic profile requires Document 19 evidence from an actual audition route.

### 6.3 Inspection lanes

Performance claims follow `governance/source-policies/MANGA_ANIME_MEDIUM_AND_INSPECTION_LANE_ROUTING_POLICY.md` (Sections 2–4) and the architecture's evidence states (§10.4).

| Model content | Admissible route |
|---|---|
| Wording, register, address, self-reference | Displayed Mandarin text; Document 17 |
| Static posture, costume, expression, proximity endpoints | Native frames; Document 18 |
| Gesture trajectory, timing, blocking, microperformance over time | Accepted continuous-motion evidence; Document 18 |
| Vocal delivery, prosody, breath, laughter quality, silence as design | Original-speed audition by a verified listening route; Document 19 |
| Speaker attribution not textually marked | Text-layer or contextual corroboration; never voice-actor recognition or camera focus alone |
| Emotion, intention, motive | Inference or interpretation only; perceiving delivery is not perceiving an inner state |

External handoff observations are `PRODUCER_REPORTED` until accepted; a model may cite them only as reported, non-load-bearing evidence.

### 6.4 Narrative frames

Record the frame of every observation:

| Frame | Use in a model |
|---|---|
| Diegetic present | Ordinary admission |
| Flashback or memory | Admit for the remembered state; note whose memory frames it |
| X's history-space | Authored testimony; admissible for what X presents, not as a neutral archive |
| In-world broadcast, ranking card, news or platform content | Attribution evidence about public narrative, not character fact |
| Montage | Admit individual shots only as far as they show behavior; adjacency is not causation |
| Credits coda, opening and ending sequences, previews | Excluded from behavioral evidence unless separately classified as diegetic |

### 6.5 Evidence-ledger row

Each observation that grounds a rule records: an evidence ID; `Subject@State`; locator in the WEB source-absolute clock with cue or frame reference (analytical method §4); situation type (ordinary or crisis; private or public); interlocutor or audience; narrative frame; evidence kind and class; inspection lane; evidence state (§10.4 of the architecture); quotation status; and the claim keys and specialist sections it supports. The ledger is a retrieval map into readings and audits, not a copy of them.

### 6.6 Negative evidence requires opportunity

Absence of a behavior counts only where the situation gave the character a real opportunity to show it. Otherwise it is a gap. Keep **evidence-backed limitations** (the source affirmatively shows the character does not, cannot or would not) separate from **evidence gaps** (the source never tests it).

---

## 7. Ordinary life versus crisis

TBHX is crowded with identity crises, institutional coercion, competition, violence, grief and survival. A model built only from those scenes predicts every situation as a crisis. Each rule therefore carries a situation-class tag drawn from the architecture's Document 20 list: ordinary domestic or social interaction; professional or public performance; competition; embarrassment; anger; grief; fear; moral disagreement; acute danger; caregiving; intimacy; institutional pressure; recovery after crisis.

Wherever the source shows ordinary life, sample it deliberately: conversation, meals, friendship, work, everyday annoyance, humor, casual self-presentation, quiet caregiving, private hobbies and life outside heroic performance. X's office work, friendships, home life and refusal of overtime are part of his characterization, not comic relief, and his model must draw on them.

Starting points already established in the corpus, each to be routed through the evidence ledger before use:

- **X:** office work, home life, the private friendship with Smile, the bar conversation with A-Hu, `绝不加班` and `准点下班`;
- **Qīng:** play and music with Luo, the safe-failure experiment and its laughter, street performance as livelihood;
- **Yang Cheng:** everyday contact with Xia Qing, including the milk-tea-shop history;
- **Lin Ling and Xiao Yueqing:** domestic and relational scenes inside and around imposed content work;
- **Luo Li and Nuonuo:** friendship through shared technical work;
- **Little Johnny, Big Johnny and A-Sheng:** household life and chosen kinship;
- **A-Hu and Xinya:** neighborhood life and children's praise;
- **Queen:** private recovery and the later support circle;
- **Smile:** pedagogy, public warmth and family provenance.

Where the source offers no ordinary-life sample — Zero, for example, is known only through history and testimony — record the gap. Never invent a baseline.

---

## 8. Model layers

### 8.1 Header

```yaml
subject: <canonical V2 analytical name>
discovery_subject_id: <analysis_subject_id if one exists, else null>
state: <Subject>@<state label>
diegetic_anchor: <boundary>
first_shown: <E##>
disclosed_through: <E##>
source_boundary: <admitted units and accepted evidence used>
basis_commit: <full commit at which the evidence was read>
model_version: <version>
coverage_tier: <FULL_PROFILE | BOUNDED_PROFILE | UNDERDETERMINED>   # §13; not a capability grade
inspection_lanes: [<lanes whose evidence the model uses>]
evidence_states_admitted: [<e.g. INDEPENDENTLY_VERIFIED, ACCEPTED_CLAIM; REPORTED only as unweighted>]
knowledge_state_table: <anchor>
excluded_evidence: <what was left out and why>
```

### 8.2 Stable dispositions

Recurring temperament, default social behavior, ordinary affect, initiative, inhibition, values and response tendencies, each with its recurrence evidence across states and situation classes.

### 8.3 Developmental state

Knowledge, relationships, obligations, available resources, wounds, role, status and changing expectations at the bound state, each with `valid_from` and `valid_until` and its change classes (§4.3).

### 8.4 Situational delta

Temporary emotional, physiological or contextual conditions — exhaustion, grief, acute fear, public humiliation, violent threat, professional pressure, Fear contamination — that alter behavior without changing state or disposition. A delta is never promoted into a trait.

### 8.5 Appraisal and salience

What the character interprets as important, threatening, desirable, humiliating, unjust, admirable or personally binding, and what overrides each appraisal. TBHX makes salience unusually diagnostic: what a character notices first about another person — a rank, a face, a voice, a record, a debt — often predicts the rest of the encounter.

### 8.6 Decision rules

The preferred form:

> **trigger + perceived stakes + current state → likely response family**, with inhibitors, overrides, observed exceptions, confidence and counterevidence.

Each rule records:

- its supporting evidence and situation classes;
- its counterevidence and an alternative explanation;
- the observation that would falsify it;
- its status: `OBSERVED` (one case or one context), `CANDIDATE_POLICY` (recurrent or explicitly established, untested on held-out material), or `PROMOTED_POLICY` (recurrent and survived validation under §12);
- the knowledge state and situational delta it presupposes.

A useful rule excludes something. A rule compatible with every behavior predicts nothing. Rules state the response family (protective interposition, withdrawal, refusal, negotiation, disclosure, concealment, escalation, exit), not a scripted action.

### 8.7 Speech-generation model

Speech follows decision:

`appraisal → communicative objective → speech act → relationship filter → register → wording`.

Record:

- a register matrix by interlocutor and mode, as attested (casual, workplace, public, family, conflict, embarrassment, support, monologue);
- Mandarin features from the source: identity grammar (`是 / 就是 / 不是 / 谁`), self-reference, address terms and relational morphology (`姐`, `叔`, `总`, `前辈`, diminutive `小`, familiar `阿`, kinship terms), modality, negation scope, sentence-final particles, evasions and directness, from Document 17 and the Chinese-language ledger;
- what is directly attested, separately from what would merely sound plausible;
- **“would sound wrong if”** traps: wordings, registers or social moves the character would not use, with evidence.

Evaluate speech on two separate axes: **decision fidelity** (the character would say this) and **surface fidelity** (the character would say it this way). Speech is generated from the character's interpretation, priorities and intent, never from catchphrases. `准点下班` belongs to a role-boundary decision, not to every X utterance; `我要成为` marks future-directed becoming, not a slogan any hero may repeat; a smile-related line is not Smile's voice.

### 8.8 Directed relationship conditioning

Behavior of A toward B is not B toward A, and a behavior observed with one interlocutor is not globalized. For each significant other, record trust, deference, rivalry, care, shame, resentment, familiarity, protectiveness, authority, what each knows about the other, and how speech changes. TBHX examples of asymmetry the models must preserve: X toward A-Hu versus A-Hu toward X (adversarial trust from both sides, with different knowledge and risk); Wang Yi's protection of Nuonuo versus Nuonuo's experience of absence and surveillance; Queen recognizing Qīng's singing versus Qīng's lingering self-measurement through luck.

### 8.9 Embodied and vocal performance

Gesture, posture, gaze, proximity, timing, silence and vocal modulation enter only through the routes in §6.3 and only from accepted evidence. Each performance constraint names its lane and evidence state. Where Document 19 has not auditioned a channel, the model records the gap and makes no acoustic claim.

### 8.10 Negative constraints

What behavior, dialogue or social move is comparatively unlikely, typed as evidence-backed limitation or evidence gap (§6.6), with the evidence explaining why.

### 8.11 Counter-structure, known limits and abstention

Counterexamples, rival readings, and the contexts the source has not tested sufficiently. Name the situations in which the model should decline to predict.

### 8.12 Presentation- and role-conditioned policies

Where a character occupies a public role or presentation, model it as a condition on policies, not as a second personality. X in public presentation and X in civilian presentation share dispositions and differ in obligations, availability and what others expect; Queen's public rule-authority and private recovery belong to one person. A presentation change is recorded with its change class.

---

## 9. Confidence, distance and abstention

Confidence uses the project's scale — High, Medium-High, Medium, Low, Open — as defined in Part I §4 of `CLAIM_REVISION_AND_CONFIDENCE_LEDGER.md`. It attaches to the exact rule wording.

Extrapolation distance:

| Distance | Situation |
|---|---|
| `D0` | Attested: the source shows this situation |
| `D1` | Close variation: same situation type, one changed detail |
| `D2` | Novel situation within the work's world and the bound state |
| `D3` | Crossover, counterfactual or substantially different setting |

Confidence falls with distance unless a promoted rule specifically covers the case. A `D3` prediction states a scenario contract: assumed chronology, interlocutor relationship and setting, and which TBHX mechanics (Trust/Fear, office, publicity) are assumed to hold.

The architecture's four evidence grades map onto this method as follows: *recurrent source behavior* = `D0`/`D1` from a `CANDIDATE_POLICY` or `PROMOTED_POLICY`; *strong extrapolation* = `D1`/`D2` from a promoted rule; *plausible but underdetermined inference* = an `OBSERVED` rule or a `D2`/`D3` case without a covering rule; *unsupported invention* = not admitted.

---

## 10. Ethical and psychological boundaries

A model never reduces a character to a moral score, a hero/villain designation, a personality stereotype or a presumed diagnosis. The corpus has already rejected clinical labels the source does not supply — no clinical PTSD or single-cause account of Original Nice's suicide, no clinical depression or alcohol dependence for Queen after X — and models keep those rejections.

Keep distinct:

- values from conduct;
- intention from result;
- role from disposition;
- public identity from personhood;
- coercion from voluntary cooperation, including resource-dependent consent;
- manipulation from ordinary persuasion, and coercive environmental design from transparent design that widens another person's options (Yan Mo's choice architecture versus Luo's safe-failure experiment);
- emotional vulnerability from permanent incapacity;
- trauma-informed interpretation from unsupported clinical diagnosis.

A morally objectionable character may remain internally coherent and situationally complex. A morally sympathetic character may act inconsistently, selfishly or harmfully without the model ceasing to recognize their established personality.

---

## 11. Artifact responsibilities and canonical homes

| Artifact | Responsibility | Home | When it is created |
|---|---|---|---|
| Phase-3 monograph | Literary interpretation of the character | existing specialist | already canonical; not regenerated |
| Reconstruction evidence ledger | Evidence rows (§6.5) grounding rules, sectioned by subject and state with stable heading anchors | `04 V2 Evidence and Revision/TBHX_V2_CHARACTER_RECONSTRUCTION_EVIDENCE_LEDGER.md` | with Document 20 drafting |
| Operational model | Layers of §8 for one subject and state | inside Document 20; split into a subject file only under the condition below | with Document 20 |
| Validation records | Prediction registers, adjudications, adversarial tests, fidelity audits (§12) | `04 V2 Evidence and Revision/Character Reconstruction Validation/` | with the first validation run |
| Document 20 | Series-wide integration, coverage tiers, retrieval routes (§13) | per the architecture | Phase 5 |

**Dedicated directory decision.** No reconstruction directory is created now. A subject's operational model moves out of Document 20 into its own file only when it needs an identity independent of Document 20: separate versioning, an attached validation record, or a stable evidence target for later external assessment. The proposed home is then `03 V2 Specialist Syntheses/04 Character Reconstruction Models/`, created with its first accepted model, one stable file per subject and state, named `TBHX_V2_<SUBJECT>_<STATE>_RECONSTRUCTION_MODEL.md`. Such a file carries the recognized front-matter quartet with reciprocal supersession links, is revised by a superseding version rather than by rewriting an assessed version, and is never promoted by editing its front matter. Document 20 then keeps a summary and a route to it. Do not create empty directories, duplicate monographs or placeholder models.

---

## 12. Validation

### 12.1 Season-1 tests are retrospective

Every analyst who has worked on this corpus has read all twenty-four episodes. Any test against Season-1 material is therefore **retrospective**: label it so, record what the analyst had been exposed to, and weight it below a prospective test. A retrospective fit is never presented as a prediction.

### 12.2 Prospective freezes

A prospective test requires material the analyst has not seen:

- **Future admitted source.** If the owner later admits new source material through the continuation policy, predictions for it are frozen in a committed prediction register before exposure, then adjudicated in a separate record without editing the frozen register.
- **Blind within-season benchmark.** A fresh analyst receives only this method, the generic reference and a bounded evidence package (for example, E01–E12 evidence for a subject), with monographs and later units withheld; predictions are frozen before release of held-out units; leakage — recognizing the work or recalling later events — is recorded.

Outcomes: `SUPPORTED | PARTLY_SUPPORTED | CONTRADICTED | NO_DIAGNOSTIC_OPPORTUNITY | CONFOUNDED | UNRESOLVED`. `NO_DIAGNOSTIC_OPPORTUNITY` is not failure.

### 12.3 Adversarial tests

As the model's use requires:

- **perturbation:** change one condition of an attested situation (interlocutor, knowledge state, publicity, presentation) and check that the prediction changes only where a rule says it should;
- **decoys:** present plausible but out-of-character responses that violate a named rule or trap, and check that the model rejects them;
- **negative controls:** situations where the model should abstain;
- **voice falsification:** score decision fidelity and surface fidelity separately; fluent wording the character would not choose fails;
- **source-grounded counterexamples:** test each rule against the strongest source scene that cuts against it;
- **named falsification conditions:** each rule states what would falsify it (§8.6);
- **baseline comparison:** the model must do better than a generic personality sketch of the same character.

### 12.4 Fidelity audit and records

Before a model is offered as mature, audit it rule by rule: `PASS | PASS_WITH_BOUND | NEEDS_TARGETED_SOURCE_REVIEW | INSUFFICIENT_EVIDENCE`. Score qualitatively, with denominators and exclusions stated; do not report accuracy percentages. When more than one model or provider has built a model of the same character, compare rules and predictions, not prose. A model never uses its own simulated outputs as evidence (§2).

---

## 13. Document 20: conditions and coverage tiers

Document 20 integrates the operational layer for the series. It does not duplicate the Phase-3 monographs; it cites them and the evidence ledger.

**Coverage tiers** describe the project's evidence coverage. They are not the evaluator's grades.

| Tier | Condition | Model scope |
|---|---|---|
| `FULL_PROFILE` | Recurrent evidence across more than one state or arc; directed relationships with several significant others; Mandarin voice evidence from Document 17; an ordinary-life sample, or a recorded gap with crisis-only rules marked as such | All layers of §8, with abstentions |
| `BOUNDED_PROFILE` | Substantial evidence in one arc, role or relationship | Layers restricted to attested domains and states |
| `UNDERDETERMINED` | Limited or only mediated evidence | Attested behaviors, attribution evidence and explicit abstentions only |

Document 20 assigns tiers from evidence. It should begin its review with the subjects of the dedicated Phase-3 specialists and then their principal relations; it should keep historical or testimony-mediated subjects such as Zero at the tier their evidence supports, never filling them from archetype.

Document 20 is complete when:

1. every included subject has a declared coverage tier, a header (§8.1) and a knowledge-state table;
2. every rule carries evidence routes to the evidence ledger, a state binding, its situation classes, status, distance, confidence, counterevidence and falsification condition;
3. speech rules separate decision fidelity from surface fidelity and rest on Document 17's lexical evidence;
4. embodied and acoustic constraints rest only on Document 18/19 accepted evidence and inherit their `OPEN` states;
5. every subject's ordinary-life sample or gap is recorded;
6. directed relationship tables are present for each `FULL_PROFILE` subject;
7. negative constraints are typed and abstention conditions are named;
8. no capability grade, tier or readiness state of the global evaluator appears;
9. predictions are labeled as inference, never as canon.

---

## 14. Readiness review and the evaluator boundary

### 14.1 When TBHX models are ready for review

A subject's TBHX reconstruction artifacts are ready for an owner or evaluator review — which this project never performs on itself — when:

1. Document 20 is canonical and integrated on `main`;
2. the subject's section satisfies §13, with its evidence-ledger rows at WEB-clock locators and claim keys;
3. at least one labeled retrospective validation pass has run, including decoys, negative controls and voice falsification, followed by a fidelity audit;
4. any model offered for independent assessment has a stable path and the recognized front-matter quartet (§11);
5. the current map records the subject's coverage, deficits and validation results.

Readiness for review is not readiness for any scenario. Whether a subject is enrolled in the character discovery registry is the discovery agent's decision; a subject without a discovery row cannot be assessed, and the project may note such absences only as leads.

### 14.2 Evaluator-facing crosswalk

The project shows where each evaluator dimension is addressed; it never grades them.

| Evaluator dimension | Where a TBHX model addresses it |
|---|---|
| `PSYCHOLOGICAL_MODEL` | Appraisal and salience (§8.5); decision rules (§8.6) |
| `LONGITUDINAL_STATE` | State binding (§4); developmental state (§8.3) |
| `VOICE_REGISTER` | Speech-generation model (§8.7), from Document 17 |
| `MUNDANE_BEHAVIOR` | Ordinary-life sample (§7) |
| `RELATIONSHIP_CONDITIONING` | Directed relationship conditioning (§8.8) |
| `INTERIORITY` | Evidence kinds and frames (§§6.1, 6.4) |
| `CONFLICT_BEHAVIOR` | Crisis-tagged rules (§§7, 8.6) |
| `ETHICAL_DELIBERATION` | Ethical boundaries (§10); moral-disagreement rules |
| `HUMOR_PLAY` | Ordinary-life and humor-tagged rules (§7) |
| `SOURCE_COMPLETENESS` | Header source boundary and excluded evidence (§8.1) |
| `NEGATIVE_EVIDENCE` | Evidence-backed limitations (§§6.6, 8.10) |
| `TEMPORAL_SPECIFICITY` | `Subject@State`, validity intervals and knowledge tables (§§4–5) |

For scenario uses (dialogue, cross-scenario, mundane social, ethical deliberation, romance or relationship, professional context), a model states what evidence exists and its limits; for cross-scenario use it writes the `D3` scenario contract (§9).

---

## 15. TBHX failure modes

Treat each as a prohibition.

1. **Office–bearer collapse:** modeling Nice, E-Soul or X as one person because one office persists.
2. **Presentation split:** modeling X's civilian and public presentations as two personalities.
3. **Apotheosis conflation:** modeling X as Zero, or Zero as X, because both occupy the godhood problem.
4. **Attribution as disposition:** treating a public story, ranking, persona or institutional classification as the character's trait.
5. **Testimony as archive:** treating X's history-space as a neutral record rather than authored testimony.
6. **Retrospective leakage:** giving an earlier state knowledge or motives the source discloses later.
7. **Mechanics as personality:** treating a Trust/Fear effect — Ghostblade's hardened silence, Smile's smile as power condition — as the whole disposition.
8. **Catchphrase overfitting:** reproducing signature lines without their pragmatic fit.
9. **Crisis-only sampling:** no ordinary-life control sample.
10. **Translation as voice authority:** building Mandarin voice from Japanese or English tracks.
11. **Script as performance:** inferring delivery from subtitles, or acoustic profiles from unauditioned audio.
12. **Producer report as audition:** treating an external continuous-AV observation as verified without acceptance.
13. **Invented interiority or diagnosis:** giving the model thoughts or clinical labels the source never grants.
14. **Globalized relationship behavior:** applying behavior seen with one interlocutor to all.
15. **Absence read as limitation** without an opportunity.
16. **Synthetic output treated as evidence.**

---

## 16. Governing rules

1. A model is derived from the literary corpus and routes back to it.
2. Synthetic output is never evidence, and predictions are never canon.
3. Subject, office, presentation and attribution are separate.
4. Every model binds one time-indexed state with a recorded knowledge boundary.
5. Later disclosure is not earlier knowledge, and revealed-not-new is not development.
6. Disposition, state and situation are separate layers.
7. A rule excludes something and carries its exceptions and falsifier.
8. Speech follows decision; voice comes from the Mandarin source; performance comes only from inspection routes that can perceive it.
9. Relationship conditioning is directional.
10. Absence is evidence only where opportunity existed.
11. Confidence falls with distance; the model may abstain.
12. Season-1 tests are retrospective unless a blind or prospective design makes them otherwise.
13. The project describes coverage; the evaluator grades capability.

---

## Changelog

### v1.0 — 2026-10-25 — Initial adoption

Adapts the corpus reference method for To Be Hero X: subject/office/presentation/attribution separation; dual-coordinate `Subject@State` binding with change classes; knowledge-state tables against retrospective leakage; Mandarin-primary text and lane-bounded performance evidence; ordinary-life control sampling; operational model layers; confidence and distance; ethical boundaries; artifact homes and the deferred subject-model directory; retrospective, blind and prospective validation; Document 20 coverage tiers and completion conditions; readiness review and the evaluator boundary. Lifecycle `INITIAL`: the method has not yet governed a completed Document 20 and will be reviewed at Document 20's start and at Phase-5 closure.
