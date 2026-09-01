---
series: GBC
artifact_type: analytical_method
scope: E01-E13
media: TV_anime
language_priority: Japanese
analysis_generation: V2
status: canonical
source_boundary: "Girls Band Cry TV anime Episodes 1-13 and the locked primary audiovisual materials defined by GBC_SOURCE_LOCK.md; V1 material is revision-target provenance only"
supersedes: null
superseded_by: null
do_not_use_as_current_authority: false
created: 2026-08-17
updated: 2026-08-17
---

# Girls Band Cry — V2 Episode Deep-Reading Method

## 1. Objective

This method governs the second-pass sequential analysis of *Girls Band Cry* Episodes 1–13.

Each episode reading must do more than explain plot, themes, and character arcs. It must capture enough linguistic, vocal, embodied, relational, musical, and decision-making evidence that the later character monographs can accurately reconstruct how the major characters think, speak, behave, and interpret the world.

The method therefore combines:

- prospective literary close reading;
- retrospective but explicitly separated recontextualization;
- Japanese-language analysis;
- voice and acting analysis;
- visual-form analysis;
- music/performance analysis;
- material/institutional analysis;
- relationship-state tracking;
- behavioral reconstruction;
- V1 claim adjudication;
- precise source/provenance routing.

---

## 2. Core epistemic rules

### Rule 1 — The episode is first read prospectively

For the main episode analysis, interpret characters with only the information available by that point in the series.

Later revelations may be discussed only in a clearly labeled retrospective section.

Do not allow later knowledge to make earlier uncertainty disappear.

### Rule 2 — Observation is not interpretation

Separate:

- directly observable audiovisual fact;
- translation/linguistic observation;
- strong inference;
- literary interpretation;
- reconstructive prediction;
- open question.

Example:

- **Observation:** Nina switches from polite to plain/rougher speech in a conflict.
- **Interpretation:** the register shift marks loss of social restraint.
- **Reconstruction hypothesis:** perceived invalidation may increase the probability that Nina abandons politeness in future intimate conflict.

These are related but not identical claims.

### Rule 3 — Repetition is stronger than vividness

A memorable breakdown, confession, performance, or fight should not automatically define the character's baseline personality.

Behavioral rules require either recurrence or a strong explanation of why a local extreme is representative.

### Rule 4 — Counterexamples are mandatory

When the episode appears to support a general rule about a character, search the episode and earlier episodes for counterexamples.

A useful model says not only “she does X,” but “she tends to do X under Y conditions, except when Z.”

### Rule 5 — Relationship context is part of personality evidence

Do not treat behavior toward one person as universal.

A character may be blunt with one bandmate, deferential with family, teasing with another, guarded with strangers, and professionally composed with industry personnel.

### Rule 6 — Japanese audio/text outranks translation when characterization depends on wording

English subtitles may be used for navigation, but speech claims should be checked against Japanese wording and audio whenever materially important.

### Rule 7 — The performance track is part of the text

Pitch, pace, breath, laughter, crying, hesitation, vocal tension, overlap, and silence are evidence when interpreting an audiovisual character.

### Rule 8 — CG acting is not merely illustrative

Body language, blocking, gaze, touch, micro-gesture, pacing, and physical timing can carry characterization not stated in dialogue.

### Rule 9 — Music is action

Songs and performances should be analyzed as events in which characters make decisions, reveal values, respond to one another, and transform conflict into form.

### Rule 10 — V1 is a hypothesis bank

Do not use V1 claims to pre-fill V2 conclusions. Each major inherited claim must be re-adjudicated.

---

## 3. Source hierarchy

The exact asset list is governed by `GBC_SOURCE_LOCK.md` once created.

Within an episode, evidence priority is generally:

1. original Japanese episode audio and moving image;
2. Japanese subtitle/dialogue track;
3. frame/contact-sheet/screenshot evidence derived from the episode;
4. official song/lyric material when within source boundary;
5. supplemental official materials explicitly admitted by the source lock;
6. V1 analysis as historical comparison only.

If the audio and subtitle differ materially, record the discrepancy rather than silently choosing one.

---

## 4. Locator standard

Every important claim should be recoverable.

Preferred locator form:

`E## HH:MM:SS-HH:MM:SS`

When helpful, append:

- Japanese line or distinctive phrase;
- frame/contact-sheet identifier;
- clip filename;
- song/performance title;
- source asset name.

Example:

`E08 18:42-19:13 — 「私はあなたの思い出じゃない」 — Nina -> Momoka`

Exact timestamps should be measured from the locked episode source rather than guessed from memory.

---

## 5. Episode analysis workflow

Each episode should be processed in five passes.

### Pass A — Narrative and state-map pass

Establish:

- episode events;
- scene boundaries;
- who knows what;
- relationship states at entry and exit;
- explicit decisions;
- unresolved questions;
- material circumstances;
- performances/rehearsals/songs.

This prevents later thematic analysis from misremembering causal order.

### Pass B — Japanese dialogue and character-voice pass

For all major scenes, inspect:

- wording;
- address terms;
- politeness;
- plain/polite switching;
- dialect;
- sentence endings;
- lexical repetition;
- ellipsis;
- insults;
- teasing;
- apology/thanks;
- hesitation;
- interactional rhythm;
- who interrupts whom;
- what is left unsaid.

Record not only “what the line means” but why this character says it this way to this person at this moment.

### Pass C — Audio, acting, and visual-form pass

Inspect:

- vocal delivery;
- posture;
- gaze;
- hands;
- body orientation;
- physical distance;
- touch;
- pacing/stillness;
- camera position/movement;
- cuts;
- lighting/color;
- spatial motifs;
- use of phones/screens/doors/windows/thresholds;
- transitions into performance abstraction;
- recurring objects;
- visual jokes or exaggeration that reveal ordinary behavior.

### Pass D — Music, institution, and material-world pass

Inspect:

- rehearsal process;
- instrument relationships;
- arrangement decisions;
- lyrics;
- vocal interpretation;
- live-performance interaction;
- venue/industry constraints;
- money;
- school/work;
- housing;
- labels/agencies;
- promotion;
- ticketing;
- travel/equipment/logistics.

### Pass E — Synthesis and adversarial pass

Ask:

- What does the episode actually establish?
- What does it complicate?
- What tempting interpretation does it fail to prove?
- What did V1 get right?
- What did V1 overstate or miss?
- What new character-model rules are supported?
- What counterexamples narrow them?
- What must remain open?

---

## 6. Required structure of every V2 episode deep reading

Each `GBC_E##_DEEP_READING.md` should normally use the following structure.

### 6.1 YAML authority and provenance

Minimum fields:

```yaml
series: GBC
artifact_type: deep_reading
scope: E01
analysis_generation: V2
status: canonical
source_boundary: "Locked Japanese audiovisual Episode 1 source"
supersedes: null
superseded_by: null
do_not_use_as_current_authority: false
```

Add source IDs/checksums when the source-lock workflow supports them.

### 6.2 Episode thesis

One concise statement describing what the episode newly does in the series.

Avoid summarizing the plot.

### 6.3 Prospective episode state

Record:

- what is known at episode start;
- unresolved tensions entering the episode;
- what is not yet knowable;
- character/relationship state before new events.

### 6.4 Scene-by-scene close reading

For each analytically important scene:

- locator;
- local action;
- Japanese language;
- vocal delivery;
- embodied acting;
- visual grammar;
- relationship effect;
- worldview/behavioral evidence;
- literary significance.

Not every scene needs equal length. Ordinary scenes are still important when they reveal baseline personality or speech.

### 6.5 Character reconstruction observations

Create a subsection for each major character present.

For every character, separate:

**Baseline evidence**
- ordinary behavior;
- ordinary speech;
- social habits.

**Stress-state evidence**
- triggers;
- escalation;
- shutdown/withdrawal;
- recovery.

**Relationship-conditioned evidence**
- how behavior changes by interlocutor.

**Worldview evidence**
- explicit principles;
- implicit values;
- contradictions.

**Voice evidence**
- Japanese wording/register;
- audio performance;
- recurring expressions.

**Embodied evidence**
- mannerisms;
- gaze/touch/posture/movement.

**Negative evidence**
- expected behavior that does not occur;
- moments where a proposed rule fails.

### 6.6 Behavioral Reconstruction Delta

This subsection is mandatory.

It translates observations into provisional model updates.

Recommended table:

| Character | Candidate rule | Trigger/context | Evidence | Counterexample / limit | Confidence | Delta |
|---|---|---|---|---|---|---|
| Nina | ... | ... | ... | ... | medium | NEW |

Allowed delta labels:

- `NEW`
- `STRENGTHEN`
- `NARROW`
- `REVISE`
- `REJECT`
- `NO_CHANGE`

A candidate rule should not be stabilized from a single vivid event without qualification.

### 6.7 Speech and voice delta

For each major character, record changes or confirmations in:

- pronouns;
- address;
- honorifics;
- register;
- dialect;
- syntax;
- characteristic lexical items;
- sentence endings;
- silence/ellipsis;
- vocal pace/tension;
- crying/laughing/shouting;
- partner-specific change.

Do not produce decontextualized “catchphrase lists.”

### 6.8 Relationship delta

Track pairwise changes.

Recommended fields:

- relationship;
- entry state;
- event;
- exit state;
- trust delta;
- disclosure delta;
- power/authority delta;
- conflict/repair pattern;
- speech/register delta;
- physical-affect/touch delta where applicable.

### 6.9 Music/performance analysis

When present:

- song's narrative position;
- lyrical relevance;
- arrangement/instrumental role;
- who leads/follows/responds;
- performance acting;
- audience relation;
- continuity with earlier versions;
- whether music resolves or preserves disagreement.

### 6.10 Visual-form analysis

Identify formal choices that materially shape meaning.

Do not merely list pretty shots.

Ask what the direction makes visible about:

- conflict;
- intimacy;
- isolation;
- hierarchy;
- performance identity;
- memory;
- subjectivity;
- social pressure.

### 6.11 Material and institutional analysis

Record practical conditions that constrain choices.

This is especially important for claims about artistic integrity or autonomy.

### 6.12 Retrospective recontextualization

Only here may later-series knowledge be used freely.

Label whether the later material:

- clarifies;
- complicates;
- reverses;
- leaves unchanged;
- introduces a new ambiguity.

Do not rewrite the prospective section to match the retrospective conclusion.

### 6.13 V1 claim adjudication

For every relevant prior major claim, use:

**PRESERVE · STRENGTHEN · REVISE · DOWNGRADE · REJECT · OPEN**

Include claim IDs once `GBC_V1_BASELINE_AND_REVISION_TARGETS.md` exists.

### 6.14 Open questions

List questions that the episode raises but cannot answer.

These should be revisited at checkpoints.

### 6.15 Cumulative delta

Conclude with what the episode changed in the overall model of:

- Nina;
- Momoka;
- Subaru;
- Tomo;
- Rupa;
- Hina/Diamond Dust as applicable;
- band identity;
- music;
- industry;
- major themes.

---

## 7. Detailed character-reconstruction protocol

### 7.1 Distinguish trait, state, strategy, role, and development

Every observed behavior should be tested against five possibilities:

- **Trait:** relatively stable disposition.
- **State:** temporary emotional condition.
- **Strategy:** behavior chosen to achieve an immediate goal.
- **Role performance:** behavior shaped by social expectation or deliberate presentation.
- **Development:** a changed pattern that becomes more likely over time.

Example: Subaru's polished friendliness may at different moments be trait-level warmth, a learned social skill, deliberate mediation, acting, or genuine disclosure. V2 should not force all of those into one authenticity judgment.

### 7.2 Model triggers, not only traits

Prefer:

> Under perceived invalidation by someone whose recognition matters to her, Nina tends to escalate...

rather than:

> Nina is confrontational.

Trigger-conditioned formulations are much more useful for later reconstruction.

### 7.3 Model goals and feared outcomes

For important actions ask:

- What does the character want to happen?
- What outcome is she trying to prevent?
- What identity does she protect?
- What would count as humiliation, abandonment, betrayal, defeat, or loss of self?

### 7.4 Model recovery and repair

Characters are not defined only by escalation.

Track:

- whether they apologize;
- whether they apologize directly or indirectly;
- whether they use gifts, music, food, practical help, joking, touch, or silence as repair;
- whether they need the other person to move first;
- whether they reinterpret the conflict later.

### 7.5 Track decision thresholds

When possible, identify what changes a character from:

- hesitation -> action;
- endurance -> refusal;
- politeness -> bluntness;
- avoidance -> disclosure;
- independence -> asking for help;
- argument -> violence/physical action;
- private feeling -> public performance.

### 7.6 Track social asymmetry

Record behavior toward:

- peers;
- elders;
- family;
- authority figures;
- fans/audience;
- strangers;
- industry professionals;
- admired people;
- disliked people;
- people the character feels responsible for.

### 7.7 Track ordinary-life behavior

High-drama scenes overrepresent crisis behavior.

Deliberately capture:

- eating;
- shopping;
- commuting;
- texting;
- waiting;
- joking;
- rehearsal downtime;
- chores;
- drinking;
- studying;
- casual conversation;
- small annoyances;
- how the character occupies shared space.

These scenes are often the best evidence for simulation-like reconstruction.

---

## 8. Japanese speech-analysis protocol

### 8.1 Pronoun and reference tracking

Record first-person and second-person strategies.

Do not assume Japanese speakers use explicit pronouns at English frequency.

Track name use, kinship terms, role terms, omitted subjects, and shifts in explicitness.

### 8.2 Address and honorifics

Track:

- surname/given-name use;
- `-san`, `-chan`, `-senpai`, or absence of honorific;
- nicknames;
- changes in address after relational shifts.

### 8.3 Politeness and plain speech

Track not merely whether speech is polite, but what causes switching.

Possible functions include:

- social distance;
- upbringing;
- anger containment;
- deference;
- sarcasm;
- professional role;
- embarrassment;
- intimacy.

### 8.4 Regional language

Where Nina's Kumamoto/Kyushu features appear, record:

- exact form;
- context;
- whether it appears under emotional pressure or in relaxed speech;
- whether the feature marks home identity, loss of control, familiarity, or simply natural speech.

Do not exoticize dialect or infer emotion solely from its presence.

### 8.5 Syntax and sentence endings

Track recurring patterns rather than isolated endings.

Ask:

- Does the character finish assertions strongly or trail off?
- Does she hedge?
- Does she challenge through questions?
- Does she issue imperatives?
- Does she use nominal fragments?
- Does she repeat another person's words before responding?

### 8.6 Lexical fields

Track repeated vocabulary around:

- right/wrong;
- winning/losing;
- regret;
- responsibility;
- liking/disliking;
- belief;
- music;
- professionalism;
- family;
- money;
- apology;
- self-description.

These may reveal stable conceptual categories in the character's worldview.

### 8.7 Interactional rhythm

Record:

- interruptions;
- overlap;
- silence;
- rapid reply;
- delayed reply;
- refusal to answer;
- topic change;
- echo/repetition;
- escalation through tempo.

### 8.8 Translation-sensitive claims

When a subtitle choice materially alters interpretation, record:

- Japanese line;
- literal semantic range;
- pragmatic force;
- subtitle rendering;
- what is lost/gained;
- whether multiple translations are defensible.

This is particularly important for intimacy, confession, insult, obligation, and moral evaluation.

---

## 9. Voice-performance protocol

For important dialogue, describe delivery qualitatively.

Useful categories:

- pitch: low / modal / raised / unstable;
- loudness: quiet / normal / projected / shouted;
- pace: slowed / measured / rapid / rushed;
- articulation: clear / clipped / slurred / swallowed;
- breath: steady / breathy / broken / gasping;
- tension: relaxed / compressed / strained;
- affect: flat / dry / amused / brittle / angry / pleading / embarrassed / grieving;
- turn-taking: patient / interruptive / overlapping / delayed;
- non-lexical vocalization: sigh, laugh, sob, scoff, groan, hum.

Do not invent numerical acoustic values unless they are actually measured.

---

## 10. Embodied-acting protocol

For each important scene ask:

- Where is the character looking?
- Is the body oriented toward or away from the interlocutor?
- Who closes distance?
- Who retreats?
- Who initiates touch?
- Does the character freeze, pace, fidget, slump, brace, or flinch?
- What do the hands do?
- How does instrument handling change under emotion?
- Does the character perform confidence physically while the voice contradicts it?
- Does the CG animation permit micro-acting that the dialogue does not state?

Physical action that contradicts speech is especially valuable evidence.

---

## 11. Music and performance protocol

### 11.1 Song function

Classify whether the song is functioning as:

- self-expression;
- communication to another person;
- group negotiation;
- professional product;
- memory;
- defiance;
- mourning;
- self-reconstruction;
- competitive statement;
- unresolved contradiction.

A song may have multiple functions.

### 11.2 Performance interaction

Track:

- eye contact;
- cues;
- instrumental handoff;
- who stabilizes tempo;
- who drives intensity;
- how the vocalist phrases against the band;
- moments of synchronization;
- visible misalignment;
- reaction after performance.

### 11.3 Reused songs

When a song returns, compare:

- performer;
- arrangement;
- vocal interpretation;
- narrative context;
- who is listening;
- what the song now means.

`空の箱` is a major V2 test case because its meaning changes depending on who performs it and when it returns.

### 11.4 Collective authorship

For later Togenashi Togeari material, track whether each member's distinct contribution is visible/audible.

The V1 phrase “conflict becomes composition” should be considered proven only if V2 can demonstrate the mechanism formally and musically, not merely thematically.

---

## 12. Relationship-analysis protocol

For each major relationship, track five dimensions:

1. **Recognition** — what does each person understand or misunderstand about the other?
2. **Dependence** — what does each need from the other?
3. **Power** — who decides, teaches, pays, organizes, protects, or withholds?
4. **Intimacy** — disclosure, physical closeness, emotional exclusivity, romantic coding.
5. **Repair** — how conflict is survived.

For Nina/Momoka, also track projection explicitly:

- Nina using Momoka as proof that refusal is meaningful;
- Momoka using Nina as contact with a lost version of herself;
- moments where either recognizes the other as an autonomous person rather than a symbolic role.

For Nina/Hina, distinguish:

- Nina's account of Hina;
- Hina's observable behavior;
- institutional context;
- what remains inaccessible because the series follows Nina more closely.

---

## 13. Character-specific V2 watchlists

These are questions to test, not conclusions to inherit.

### 13.1 Iseri Nina

Track:

- polite upbringing vs emotional register leakage;
- Kumamoto/Kyushu features;
- right/wrong vocabulary;
- defeat/non-regret distinction;
- tendency to universalize interpersonal injury;
- sensitivity to being disbelieved;
- desire for recognition;
- idealization and de-idealization;
- possession/jealousy/intimacy where supported;
- strategic compromise learned over time;
- ability to admit limitation without treating it as moral defeat;
- ordinary humor, embarrassment, pettiness, warmth, and competence;
- how speech changes with Momoka, Subaru, Tomo, Rupa, Hina, family, strangers, and professionals.

### 13.2 Kawaragi Momoka

Track:

- rough/clipped everyday register;
- older-sister behavior;
- artistic confidence vs life uncertainty;
- guilt toward Diamond Dust;
- financial realism;
- generosity;
- unilateral protection;
- nostalgia;
- avoidance;
- self-erasure;
- alcohol effects;
- apology and vulnerability;
- differences between musician/professional register and intimate register;
- how Nina uniquely destabilizes her.

### 13.3 Awa Subaru

Track:

- social code-switching;
- acting as deception vs acting as intelligence;
- mediation;
- humor;
- teasing;
- conflict avoidance vs intervention;
- family-role pressure;
- ability to manipulate a scene for a constructive purpose;
- sincere disclosure;
- drumming as affirmative identity rather than rebellion only;
- how her voice differs when performing politeness, acting, joking, or speaking candidly.

### 13.4 Ebizuka Tomo

Track:

- clipped critical register;
- standards and competence judgments;
- hostility vs defensiveness;
- impatience;
- need for recognition;
- response to incompetence;
- response to affection;
- relationship with Rupa;
- family/achievement evidence;
- meaning of competitive awards and their destruction;
- whether criticism functions as control, fear, care, craft discipline, or combinations of these;
- moments of softness and how they differ linguistically from ordinary speech.

### 13.5 Rupa

Track with unusually strict anti-overreach discipline:

- sparse speech;
- calm delivery;
- humor;
- timing;
- practical competence;
- alcohol-related material;
- grief;
- racism and normalization of mistreatment;
- protectiveness;
- relationship with Tomo;
- moments where composure breaks or where others infer too much from composure;
- what the series simply does not show about her private interiority.

### 13.6 Hina

Track independently from Nina:

- baseline register;
- controlled vs emotionally activated speech;
- practical philosophy;
- relationship to compromise;
- interpretation of the school conflict;
- relationship to Diamond Dust;
- professional performance;
- Nina-specific shifts;
- evidence for regret, resentment, concern, rivalry, or unresolved attachment;
- what the work leaves intentionally ambiguous.

---

## 14. Special V2 analytical tests

### 14.1 Correctness / non-regret test

Every major occurrence of concepts such as:

- 正しい / 間違っている;
- 勝つ / 負ける;
- 後悔;
- responsibility/blame;
- liking oneself;
- being believed/understood

should be indexed when materially relevant.

Ask whether the series equates moral correctness with a life worth affirming. V1 argued that it does not; V2 must verify this longitudinally.

### 14.2 Authenticity test

Avoid treating authenticity as a simple binary.

For each major conflict ask:

- authentic to what?
- honest to whom?
- is social performance automatically false?
- can a strategic compromise preserve a deeper value?
- can uncompromising behavior become coercive?

### 14.3 Protection / control test

Track when care is delivered through unilateral decisions.

Ask whether the protected person experiences the action as care, control, abandonment, or some mixture.

### 14.4 Romance/yuri-coding test

For Nina/Momoka, classify evidence rather than forcing a binary verdict.

Possible evidence classes:

- conventional romantic language;
- confession-like framing;
- visual romantic coding;
- jealousy/possessiveness;
- emotional exclusivity;
- physical intimacy;
- reciprocal verbal declaration;
- relational behavior compatible with but not exclusive to romance;
- deliberate ambiguity.

The final synthesis should describe the strength and type of coding precisely.

### 14.5 Industry complexity test

For every professional constraint ask:

- who bears the risk?
- what is gained by compromise?
- what is lost?
- what forms of autonomy become possible only through institutions?
- what forms of autonomy institutions restrict?

### 14.6 Ensemble-causality test

Ask what would fail if Subaru, Tomo, or Rupa were removed from a scene or decision.

This prevents Nina/Momoka centrality from making the other members analytically decorative.

### 14.7 Ending/epilogue status test

For the ED and post-E13 material, classify each claim as:

- literal;
- strongly implied;
- symbolic;
- mixed literal/symbolic;
- open.

Do not convert symbolic montage into literal chronology without support.

---

## 15. V1 revision procedure

Before each episode analysis, identify the V1 claims relevant to that episode.

After the V2 reading, assign:

- **PRESERVE** — V1 remains substantially correct.
- **STRENGTHEN** — V1 was correct and V2 adds stronger/more specific evidence.
- **REVISE** — the core insight survives but formulation changes materially.
- **DOWNGRADE** — plausible but less certain/less general than V1 claimed.
- **REJECT** — primary source does not sustain it.
- **OPEN** — evidence remains genuinely unresolved.

Revision status should follow evidence, not a desire for V2 novelty.

---

## 16. Evidence confidence language

Use calibrated phrases:

### High confidence

- “The episode directly establishes...”
- “Across multiple scenes...”
- “The recurring pattern is...”

### Medium confidence

- “The episode strongly suggests...”
- “A plausible relational reading is...”
- “This is consistent with...”

### Low confidence / open

- “This may indicate...”
- “The text permits, but does not require...”
- “There is insufficient evidence to determine...”

Avoid laundering an inference into fact by repetition.

---

## 17. Anti-overfitting safeguards for character modeling

Before adding a behavioral rule to a monograph, test:

1. Is it based on more than one scene?
2. Are the scenes in different emotional states?
3. Does the behavior recur with different interlocutors?
4. If not, is it explicitly relationship-specific?
5. Is there a counterexample?
6. Can the rule be narrowed to explain both evidence and exception?
7. Could the behavior instead be a temporary state, role performance, or plot-specific strategy?
8. Does Japanese wording support the proposed psychological distinction?
9. Does vocal/physical acting agree with the verbal reading?
10. Are we importing an anime archetype that the text itself does not establish?

Only after this should the rule move from provisional to stabilized.

---

## 18. Monograph feed-forward block

At the end of every episode file, include a compact block designed for later monograph ingestion.

Recommended structure:

```markdown
## Monograph feed-forward

### Nina
- Stable observations:
- New candidate rules:
- Counterexamples:
- Speech/register additions:
- Relationship-specific changes:
- Worldview evidence:
- Open uncertainties:

### Momoka
...
```

This prevents the final monograph from depending on memory of thirteen long prose readings.

---

## 19. What an episode reading must not do

Do not:

- write a plot recap with thematic commentary appended;
- infer stable personality from a single crisis scene without qualification;
- treat English subtitle wording as Japanese linguistic evidence;
- reduce Subaru's acting to “fake”; 
- reduce Momoka to a pure authenticity martyr;
- reduce Nina to either moral truth-teller or irrational brat;
- reduce Tomo to tsundere-like bluntness without examining standards, fear, family, and relationship context;
- reduce Rupa to serene caretaker wisdom because she speaks less;
- reduce Hina to antagonist/foil because the story focalizes Nina;
- assume every close Nina/Momoka interaction proves conventional romance;
- assume lack of explicit romance erases romantic coding;
- treat Diamond Dust as sellouts by definition;
- treat independence as costless;
- claim a visual or musical effect without examining the actual source;
- make reconstructive predictions sound like canon facts.

---

## 20. Definition of success

A successful V2 episode corpus should permit a later analyst to answer, with evidence:

- What changed in this episode?
- What was only knowable at the time?
- What does later material change?
- How did each character speak to each important person?
- What did emotion do to her register and voice?
- What behavior repeated?
- What behavior was exceptional?
- What does she appear to believe?
- Where does her behavior contradict that belief?
- How does she repair conflict?
- What does she do in ordinary downtime?
- What does her body communicate that her words do not?
- What does music let her express?
- What practical constraints shape her choices?
- Which V1 claims survive?
- What would a cautious model predict she might do in a new analogous situation?
- How confident should that prediction be?

If the corpus can answer those questions, the later monographs can become genuine character-reconstruction references rather than thematic biographies.
