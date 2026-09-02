---
series: 86-Eighty-Six
series_id: '86'
artifact_type: character_modeling_reference_method
scope: V01-V14+ALTER1
generation: V2
version: '1.1'
status: canonical
date: '2026-08-17'
source_boundary: Locked original-Japanese V01-V14; Alter.1 audited supplemental; Alter.2 excluded from mainline characterization
governing_method: 86_FULL_SERIES_ANALYTICAL_METHOD_V2.md
governing_architecture: 86_MULTI_DOCUMENT_SYNTHESIS_ARCHITECTURE_V2.md v2.2
current_entrypoint: 00_README_AND_CORPUS_MAP.md
primary_locator_authority: 86_PHASE5_LOCKED_LOCATOR_INDEX.tsv
source_verification_authority: 86_PHASE8_JAPANESE_SOURCE_VERIFICATION_AUDIT.md
working_source_verification: 86_CHARACTER_MODELING_ATTACHED_SOURCE_VERIFICATION.tsv
release_integrated: '2026-08-20'
release_id: 86-V2-V01-V14-1.0
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
---

# 86-Eighty-Six V2 — Character Modeling Reference Method
## Source-grounded reconstruction of personality, Japanese voice, behavior, relationship-conditioned register, emotional-state variation, and bounded behavioral inference

## 0. Purpose and authority

The existing V2 corpus already explains the major characters of *86* at literary, political, ethical, military, relational, and philosophical levels. The Character Modeling Reference layer has a narrower responsibility:

> **Make a character recoverable as a person without mistaking a reconstruction tool for canon.**

A successful Character Modeling Reference profile should support high-fidelity recognition and comparison of a character across ordinary life, conflict, fear, humor, affection, command, grief, embarrassment, injury, institutional pressure, and relationship-specific contexts. It should make the reader able to identify what is stable, what is situational, what is interlocutor-dependent, what is strongly evidenced, and what remains uncertain.

The layer is therefore designed for questions such as:

- What does this character sound like in Japanese, rather than in normalized English summary?
- Which parts of their register remain stable across emotional states?
- What changes when they speak to a peer, subordinate, commander, family member, intimate partner, stranger, or political authority?
- How do they behave before they have time to formulate an explicit philosophy?
- What kinds of situations reliably make them intervene, withdraw, deflect, argue, obey, command, joke, overfunction, or ask for help?
- What ordinary preferences and habits keep the character from collapsing into a thematic abstraction?
- Which generated lines or behaviors would feel wrong even if they were thematically compatible?
- How far can the corpus support behavioral prediction before prediction becomes invention?

This layer is **derived reference infrastructure**. It does not create independent canonical facts. When a profile conflicts with a narrower source or canonical analytical home, the narrower authority controls.

The governing authority order is:

1. original Japanese primary source;
2. Phase-5 source/locator authority and Phase-8 exact-source verification;
3. canonical V2 deep readings and longitudinal ledgers;
4. canonical specialist Documents 01–14 and source-sensitive Documents 16–17;
5. canonical continuous synthesis, Document 18;
6. Character Modeling Reference profiles, matrix, diagnostic index, and crosswalk;
7. V1 legacy material as discovery aid only;
8. synthetic/generated examples, which are never evidence.

This method inherits the full-series V2 requirement that interpretation remain multi-layered. Character reconstruction must not erase military, political, historical, bodily, institutional, or source-language context merely because the immediate task is personality modeling.

---

# I. What a character model is — and is not

## 1. A character model is a constrained reconstruction surface

A profile is a structured account of the recurring features that make a character recognizably themselves. It should capture enough evidence to support statements such as:

- "This reaction fits the established baseline under this kind of pressure."
- "This line uses a register attested with this interlocutor."
- "This emotional openness is possible, but only in a narrower state than the character's resting voice."
- "The character has shown this behavior more than once, but the evidence is relation-specific rather than global."
- "The corpus does not establish a stable tendency here."

The model is not a deterministic simulator. Characters can surprise one another, contradict themselves, grow, regress, perform roles, misread situations, and behave atypically under extreme conditions. A profile should preserve that possibility rather than eliminating it.

## 2. A character model is not a philosophical abstract

The numbered specialist corpus remains the primary home for themes such as:

- self-authorship;
- pride;
- trauma and recovery;
- memory;
- political legitimacy;
- citizenship;
- military professionalism;
- paternalism;
- artificial-person standing;
- love and dependence;
- home and return.

The profile asks how those issues become **behaviorally and linguistically visible in one person**.

For example, "values autonomy" is insufficient characterization. The profile must show what kinds of control the character rejects, what help they accept, whether they ask directly or indirectly, whether they react differently to institutional authority and family authority, and how the Japanese language of refusal changes by context.

## 3. A character model is not a route to hidden canon

Behavioral inference can estimate what is more or less plausible given existing evidence. It cannot establish events that have not occurred, internal thoughts never supplied, or relationship outcomes outside the source boundary.

A hypothetical response may be useful for QA. It does not become canonical merely because it sounds convincing.

## 4. A character model is not an anime voice-performance model

The current source boundary is the Japanese light novels and audited prose supplements. Anime acting, pitch, tempo, breath, prosody, facial animation, and audiovisual staging may be analyzed in a future adaptation layer, but they must not be silently imported here.

The present "voice" model is a **written-Japanese idiolect and discourse model**: pronouns, address, politeness, syntax, lexical choice, sentence endings, rhetorical habits, role language, speech acts, narration/focalization, and contextual register.

---

# II. Source boundary and working source state

## 1. Mainline and supplemental scope

The active Character Modeling Reference source boundary is:

- original-Japanese Volumes 01–14 as mainline primary evidence;
- Alter.1 in its audited supplemental role;
- Alter.2 excluded from mainline characterization.

Alter.1 may be used actively for ordinary-life evidence because low-pressure scenes, gifts, food, birthdays, photographs, jokes, domestic routines, leisure, and small promises are disproportionately useful for distinguishing personality from crisis behavior. Its supplemental status must remain visible wherever it carries a claim.

Alter.2 may be used only when an explicitly labeled counterfactual/AU comparison is requested. It must not be merged into a mainline character baseline.

## 2. Working copies

CMR-0 verified the chat-local V01–V14 and Alter.1 EPUBs against the Phase-8 identities. All fifteen working files matched the locked SHA-256 values and passed ZIP/CRC integrity checks. `86_CHARACTER_MODELING_ATTACHED_SOURCE_VERIFICATION.tsv` records that working-state verification.

This does not create a new source lock. Phase 5 and Phase 8 remain source authority.

## 3. Primary-source escalation rule

A profile writer should not reread every volume indiscriminately for every claim. Use the mature V2 corpus as a retrieval scaffold:

1. current corpus map and this method;
2. relevant character/relationship/voice ledgers;
3. relevant specialist document;
4. relevant deep reading;
5. diagnostic locator index when available;
6. Phase-5 locked locator when available;
7. exact Japanese source context.

But when the claim concerns exact wording, address, syntax, a one-scene behavior, a disputed interpretation, or a new diagnostic passage not already indexed, return to the Japanese source.

---

# III. Evidence model for character reconstruction

The Character Modeling Reference layer uses two overlapping evidence systems:

1. the full-series V2 evidence classes (`PF`, `NV`, `CS`, `BA`, `LI`, `MI`, `VI`, `PT`, `SI`, `IT`, `AM`, `RR`);
2. a character-modeling functional classification that identifies **what kind of modeling claim** the evidence supports.

The second classification does not replace the first.

## 1. `DIRECT_SOURCE_FACT`

Use when the source directly supplies the relevant information.

Examples include:

- first-person pronoun;
- addressee form;
- explicit preference or fear;
- direct action;
- stated relationship;
- overt refusal;
- explicit self-description;
- observable bodily action narrated without meaningful ambiguity.

A character statement remains `CS`, not automatically `PF`. If a character says "I am not afraid," that is direct evidence that they said it; whether they are in fact unafraid must be tested against narration and behavior.

## 2. `REPEATED_BEHAVIORAL_PATTERN`

Use for a recurring action tendency established across more than one meaningful scene.

Examples:

- regularly answers emotional pressure with practical action;
- habitually uses humor to soften group tension;
- tends to continue functioning while concealing bodily impairment;
- repeatedly challenges unilateral self-sacrifice;
- routinely translates concern into material assistance rather than verbal reassurance.

Recurrence is necessary but not sufficient. The repeated scenes should not all be one prolonged crisis unless the claim is explicitly crisis-specific.

## 3. `RELATIONSHIP_CONDITIONED_PATTERN`

Use when the pattern appears reliably with a specific person or relationship class.

This category is essential because a character's register and behavior may be stable **within a relation** while differing elsewhere.

Examples:

- retains a marked self-reference with everyone but becomes more teasing with household peers;
- uses rank/title publicly and personal name privately;
- permits one person to interrupt behavior they reject from institutional authority;
- becomes unusually direct with someone whose judgment they trust.

Do not generalize a relationship-conditioned pattern into a universal trait without evidence.

## 4. `EMOTIONAL_STATE_DELTA`

Use for a meaningful departure from the resting baseline under a defined state:

- fear;
- anger;
- grief;
- embarrassment;
- exhaustion;
- pain;
- affection;
- command pressure;
- ideological threat;
- acute shame;
- relief.

The analytical unit is **baseline → delta**, not the extreme behavior alone.

## 5. `HIGH_CONFIDENCE_INFERENCE`

Use when no single passage states the conclusion but multiple independent evidence channels converge.

A high-confidence inference should normally have at least two of the following:

- repeated behavior;
- linguistic recurrence;
- narration/focalization;
- relationship evidence;
- consequence across volumes;
- explicit self- or other-character reflection that is itself corroborated.

Mark it as inference even when confidence is high.

## 6. `OPEN_INFERENCE`

Use when the pattern is potentially useful but underdetermined.

Appropriate labels include:

- `OPEN`;
- `LOW_CONFIDENCE`;
- `RELATION_SPECIFIC_ONLY`;
- `SINGLE_SCENE_ONLY`;
- `FINAL_ARC_OPEN`.

A good profile may contain explicit uncertainty. Removing uncertainty for smoothness is a methodological failure.

---

# IV. Claim-strength rubric

Every predictive or summarizing characterization claim should be assessed along six dimensions.

| Dimension | Question |
|---|---|
| **Directness** | Is the claim directly observable/stated, or inferred? |
| **Recurrence** | Does it appear once, repeatedly, or longitudinally? |
| **Context breadth** | Does it survive ordinary, crisis, institutional, and relational changes? |
| **Temporal stability** | Is it stable across volumes, or limited to one developmental phase? |
| **Relation scope** | Is it universal, role-specific, or specific to one interlocutor? |
| **Counterevidence** | Are there meaningful exceptions that narrow the rule? |

Use four confidence bands:

### `HIGH`

Strongly recurring, source-grounded, and robust across relevant contexts, or directly and repeatedly established.

### `MODERATE`

Supported by multiple pieces of evidence but narrower in context, relation, or time.

### `LOW`

Plausible but supported by limited evidence. Useful only if visibly qualified.

### `OPEN`

Insufficient evidence to stabilize a model. Preserve the question rather than filling it.

Do not map these bands to fake numerical probabilities.

---

# V. Stable baseline versus developmental state

L01 records state change rather than static summaries. Character profiles must preserve the same discipline.

## 1. Stable baseline

A stable baseline is a trait or repertoire feature that persists across meaningful changes in plot state.

Examples can include:

- general level of verbal excess;
- characteristic self-reference;
- habitual social energy;
- typical humor mode;
- default formality;
- attentional habits;
- recurrent way of offering care;
- common response to uncertainty.

## 2. Developmental state

A developmental state is true at a particular boundary but may later change.

Profiles should distinguish:

- early-series baseline;
- middle-series expansion or correction;
- V14-boundary state.

The later state does not erase the earlier one. If a character learns to ask for help, the profile should not rewrite earlier scenes as though help-seeking was always available.

## 3. Stable form with expanded semantic capacity

A character may develop without changing their fundamental linguistic style. This is especially important for Shin and Frederica.

Shin's growth often occurs because new content becomes speakable inside a still restrained register. Frederica's archaizing idiolect remains stable while the content carried by that idiolect ranges from comedy to fear, grief, family attachment, ethical accusation, and political self-assertion.

A profile must therefore ask separately:

- Did the **form** change?
- Did the **semantic content** change?
- Did the **interlocutor** change what became sayable?
- Did the emotional state temporarily compress or expand the form?

---

# VI. Behavioral grammar

Behavioral grammar is the set of recurring action tendencies through which a character becomes predictable enough to recognize while remaining non-deterministic.

Every profile should address the following where evidence permits.

## 1. Attention

What does the character tend to notice first?

Possible domains:

- threat;
- emotional asymmetry;
- competence;
- institutional inconsistency;
- bodily condition;
- social embarrassment;
- material needs;
- rank or role;
- another person's silence;
- tactical terrain;
- signs of abandonment;
- violations of dignity.

Do not infer an attentional priority from one scene.

## 2. First response under uncertainty

Does the character tend to:

- ask;
- observe;
- joke;
- attack;
- delay;
- obey;
- challenge;
- take over;
- withdraw;
- intellectualize;
- seek another person's judgment;
- convert uncertainty into practical work?

This should be state- and relation-qualified.

## 3. Intervention threshold

What reliably moves the character from observation to action?

Distinguish:

- danger to self;
- danger to another;
- violation of procedure;
- perceived betrayal;
- ideological line-crossing;
- humiliation;
- a loved person's self-disposal;
- threat to group continuity;
- threat to autonomy.

## 4. Failure response

Track whether the character typically:

- self-blames;
- externalizes;
- retries immediately;
- withdraws;
- asks for feedback;
- compensates through overwork;
- apologizes;
- hides consequences;
- converts failure into a narrower practical problem;
- revises the goal.

## 5. Repair after harm

If the character hurts someone, how do they respond?

Possible forms include:

- explicit apology;
- behavioral correction without verbal apology;
- gift/practical action;
- avoidance;
- rationalization;
- renewed argument;
- acceptance of the other's anger;
- need for a third party to mediate.

## 6. Decision style

Profiles should distinguish:

- rapid versus deliberative;
- principle-first versus consequence-first;
- individual versus consultative;
- role-based versus personal;
- practical versus symbolic;
- private decision versus public explanation.

No one axis should be treated as the character's entire psychology.

---

# VII. Japanese voice fingerprint

The Japanese voice fingerprint is a mandatory profile section where the corpus provides enough dialogue.

## 1. Required linguistic fields

Record, where supported:

- first-person pronoun or self-reference;
- second-person forms;
- names, ranks, titles, kinship terms, callsigns, and honorifics used for important interlocutors;
- politeness baseline;
- formal/casual alternation;
- roughness or softness;
- sentence length and fragmentation;
- contraction;
- ellipsis;
- command/request forms;
- hedging and modal language;
- characteristic sentence endings;
- literary, archaizing, military, aristocratic, technical, or institutional vocabulary;
- repeated lexical choices with characterological value;
- characteristic rhetorical patterns such as self-correction, repetition, blunt negation, understatement, or theatrical exaggeration.

## 2. No dictionary personality mapping

A form such as `俺`, `あたし`, `わらわ`, `それがし`, or `です/ます` is evidence about register and self-presentation. It is not by itself proof of masculinity, childishness, arrogance, intimacy, submission, intelligence, or emotional distance.

Interpret forms in context and longitudinally.

## 3. No context-free "true voice"

Prefer the model:

> **one person with a repertoire of context-sensitive registers**

rather than:

> public fake voice versus private true voice.

Use the latter only when the source explicitly constructs such a distinction.

## 4. Semantic admission versus stylistic transformation

A character's growth may be expressed by new content entering an old style. The profile should track what the character becomes able to say **without assuming that emotional growth must sound more verbose, modern, or conventionally therapeutic**.

## 5. Translation-sensitive control

When English analytical vocabulary would merge distinct Japanese systems, preserve the Japanese distinctions established by T12, Document 12, and Document 16.

Particular caution applies to:

- `帰る / 戻る / 還る / 帰還 / 生還`;
- `故郷 / 祖国`;
- `一緒に / 共に`;
- `誇り / 誇りしか`;
- `従う / 支える / 信じる / 頼る`;
- `人格 / 疑似人格 / 自我 / 自己同一性 / 意志 / 意思`;
- `赦す / 許す`;
- role/title systems such as `女王`, rank, callsign, personal name, and kinship address.

Do not write as if an English synthesis term were a repeated Japanese source word.

## 6. Focalization control

The novels use narration, close focalization, free-indirect coloring, technical explanation, character statements, political rhetoric, and other evidence states. A sentence near a character is not automatically that character's voice.

Before using a passage as a voice exemplar, classify whether it is:

- direct dialogue;
- quoted inner speech;
- close-third focalized narration;
- narratorial statement;
- in-world document;
- technical explanation;
- retrospective memoir or report;
- paratext.

---

# VIII. Relationship-conditioned register

L02 establishes that relationships are changing systems rather than static labels. The Character Modeling Reference layer extends this into a directed linguistic/behavioral matrix.

## 1. Directionality is mandatory

`A → B` and `B → A` are separate evidence objects.

For each directed relation, record where supported:

- speaker self-reference;
- target address;
- rank/title/name/callsign/kinship use;
- honorific pattern;
- politeness;
- command/request style;
- teasing/insult style;
- emotional disclosure level;
- public/private difference;
- household/battlefield/institutional difference;
- conflict/crisis difference;
- meaningful one-time register shifts;
- source routes;
- confidence and temporal boundary.

## 2. Intimacy must not be inferred from one marker

Honorific omission, first-name use, roughness, or directness can be relationally meaningful, but none proves intimacy by itself.

Require contextual support from:

- narration;
- repeated interaction;
- relationship state;
- scene function;
- longitudinal change.

## 3. Relation change does not require register replacement

A relation may deepen while the same core speech form remains. The diagnostic question is often **what the form is now carrying**, not whether it has disappeared.

## 4. Public and private roles may coexist

Lena can remain a competent officer in intimate scenes. Frederica can remain archaizing while frightened. Raiden can remain rough while caring. Lerche's retainer register can be both institutional role-language and individualized voice.

Do not model intimacy as stripping away all role-coded language unless the source does so.

---

# IX. Emotional-state delta protocol

Every major profile must distinguish resting baseline from altered states.

## 1. Minimum state inventory

Consider, where evidence exists:

- ordinary/resting;
- amused;
- teasing;
- affectionate;
- embarrassed;
- irritated;
- angry;
- frightened;
- grieving;
- exhausted;
- physically injured;
- commanding;
- ideologically threatened;
- vulnerable/self-disclosing.

Do not create empty categories for symmetry.

## 2. Delta dimensions

For each state, ask what changes in:

- sentence length;
- politeness;
- lexical abstraction;
- repetition;
- hesitation;
- command force;
- self-reference;
- target address;
- physical behavior;
- proximity/touch;
- ability to ask for help;
- humor;
- decision speed;
- concern for audience/image.

Also record what **does not change**. Persistence can be more character-defining than alteration.

## 3. Crisis-state quarantine

One extreme scene cannot redefine the baseline.

Examples of prohibited moves:

- treating Shin's crisis language as his everyday conversational style;
- treating Lena's battlefield command register as her only voice;
- treating Frederica's political accusation as constant grandiosity;
- treating Theo's harshest accusation as proof that cruelty is his normal relation to everyone;
- treating Ernst's breakdown as his complete paternal baseline.

## 4. Exception handling

A genuine exception should be preserved, not normalized away. A line may matter precisely because the character almost never speaks that way.

Profiles should mark such evidence as:

- `RARE_BREAK`;
- `ONE_TIME_RELATIONAL_SHIFT`;
- `CRISIS_ONLY`;
- `DEVELOPMENTAL_FIRST`;
- `UNREPEATED_AT_BOUNDARY`.

---

# X. Ordinary-life control sample

Ordinary scenes are mandatory characterization controls when the corpus supplies them.

## 1. Why ordinary evidence matters

Crisis-only modeling systematically exaggerates:

- ideology;
- trauma;
- heroism;
- command;
- tragedy;
- competence;
- self-sacrifice.

The resulting profile may be thematically accurate and personally false.

## 2. Ordinary-life dimensions

Mine evidence for:

- food and appetite;
- shopping;
- clothing/fashion;
- hobbies;
- art;
- reading;
- school;
- chores;
- cooking;
- rest and sleep;
- gifts;
- birthdays;
- photographs;
- leisure;
- jokes;
- small irritations;
- comfort behaviors;
- domestic routines;
- celebrations;
- low-stakes disagreement;
- how the character behaves when no crisis requires them to symbolize anything.

## 3. Sampling rule

For major characters, a canonical profile should normally include diagnostic evidence from at least:

- one low-pressure scene;
- one interpersonal conflict or disagreement;
- one vulnerable/crisis state;
- one role/competence scene;
- one relationship-specific scene with a major interlocutor.

This is a minimum diversity rule, not a quota. Evidence-rich characters should use a broader spread.

## 4. Alter.1 rule

Alter.1 is especially useful for ordinary controls, but mainline scenes should anchor the stable model wherever possible. If a trait appears only in Alter.1, label it supplemental and do not automatically generalize it across mainline contexts.

---

# XI. Humor and comic rhythm

Humor is canonical characterization, not disposable tonal filler.

Profiles should identify, where applicable:

- deadpan;
- sarcasm;
- teasing;
- reaction humor;
- literalism;
- embarrassment comedy;
- theatrical self-importance;
- role incongruity;
- mock formality;
- verbal escalation;
- understated punchline;
- physical/comic timing described in prose.

A serious thematic role frequently produces flattening pressure. Frederica, Raiden, Theo, Ernst, Vika, Lerche, Annette, and Fido are particularly vulnerable to losing comic texture if profiles are written only from specialist theses.

The profile should ask:

> What kind of joke would this character make, tolerate, fail to understand, or become the target of?

The answer must remain source-grounded rather than generated from archetype.

---

# XII. Conflict, disagreement, and moral interruption

A useful character model needs to know **how the person disagrees**, not merely what they believe.

Track:

- escalation versus de-escalation;
- directness;
- sarcasm;
- motive attack versus behavior critique;
- logical argument versus relational appeal;
- willingness to shout, threaten, command, plead, or withdraw;
- whether disagreement is experienced as abandonment;
- tolerance for being contradicted;
- whether apology follows;
- whether resentment persists;
- whether the character acts before agreement is reached.

### Moral interruption

Several *86* relationships contain a recurring pattern in which one character interrupts another person's self-disposal, overreach, or coercive action. The profile must distinguish:

- emergency interruption;
- command authority;
- paternalism;
- peer objection;
- permanent guardianship.

The same outward action can have different ethical and relational meanings depending on standing, urgency, scope, and whether judgment is returned afterward.

---

# XIII. Care model

Separate at least five dimensions of care.

## 1. Giving care

How does the character normally help?

- practical work;
- food;
- bodily protection;
- listening;
- instruction;
- command;
- humor;
- presence;
- direct reassurance;
- future planning.

## 2. Asking for care

Is the request direct, indirect, delayed, disguised as logistics, or almost absent?

## 3. Accepting care

Does the character accept immediately, resist, negotiate conditions, joke, become embarrassed, reinterpret the act as duty, or permit help only after functional collapse?

## 4. Rejecting care

Why?

Possible reasons include:

- autonomy;
- shame;
- role responsibility;
- distrust;
- fear of burden;
- fear of loss;
- rejection of pity;
- disagreement about what recovery should mean.

## 5. Overcare and control

Profiles should identify when the character's care becomes behaviorally controlling without turning every strong intervention into paternalism.

---

# XIV. Body, gesture, and embodied characterization

The light novels contain prose and illustrations capable of supporting embodied characterization. Use only what the current source boundary actually supplies.

Track recurring evidence such as:

- posture;
- gaze avoidance;
- stillness;
- physical distance;
- touch;
- reflexive movement;
- injury concealment;
- fatigue response;
- bodily confidence;
- clothing behavior;
- spatial habits;
- willingness to be touched or physically assisted.

Do not infer anime-only gesture, seiyuu performance, timing, or staging.

A body-state change can alter behavior without redefining personality. Theo's disability, Shin's sensory loss, and other bodily changes should be modeled as interaction between stable disposition, changed capability, social response, and newly available choices.

---

# XV. Values in behavioral form

Profiles may summarize established values only by translating them into recurrent conduct.

Examples of the required transformation:

- **"values autonomy"** → which decisions does the character insist on owning, and when do they accept constraint?
- **"values professionalism"** → what actions do they treat as competent or irresponsible?
- **"values loyalty"** → does loyalty mean obedience, presence, challenge, remembrance, or shared risk?
- **"values dignity"** → what kinds of pity, euphemism, command, or bodily treatment trigger refusal?
- **"values family"** → who receives family language, what obligations follow, and what control is rejected?

The full normative argument remains in the specialist corpus.

---

# XVI. Diagnostic locator index method

`86_CHARACTER_DIALOGUE_AND_BEHAVIOR_LOCATOR_INDEX.tsv` is a semantic retrieval aid. It does not compete with Phase-5 locator authority.

## 1. Required fields

The index should use:

`entry_id`\
`character`\
`target_or_relation`\
`state_tag`\
`diagnostic_dimension`\
`volume_or_source`\
`canonical_locator_id`\
`source_route`\
`scene_context`\
`evidence_layer`\
`voice_features`\
`behavior_features`\
`why_diagnostic`\
`confidence`\
`notes`

## 2. What belongs in the index

Prefer passages that do real diagnostic work:

- reveal baseline voice;
- expose a state change;
- distinguish two relationships;
- show ordinary behavior;
- show conflict/care style;
- establish a marked address form;
- contain a rare but consequential break;
- show a value becoming behavior;
- expose a mischaracterization trap.

Do not use the index as an exhaustive quotation warehouse.

## 3. Locator authority

If a useful passage already has a Phase-5 locked locator, reuse it exactly.

If it does not:

- do not fabricate a canonical `VXX-L###` ID;
- record the exact volume/source, EPUB spine route or chapter/section, short Japanese anchor, and scene context available from the primary source;
- set `canonical_locator_id` to blank or controlled `LOCATOR_GAP`;
- explain the gap in `notes`.

A locator gap is not a source gap. It means the passage is newly diagnostic for CMR but was not part of the frozen Phase-5 canonical locator set.

## 4. Evidence-layer field

Recommended values:

- `DIALOGUE_EXACT`;
- `INNER_SPEECH_EXACT`;
- `NARRATION_BEHAVIOR`;
- `FOCALIZED_NARRATION`;
- `ILLUSTRATION_PARATEXT`;
- `ALTER1_SUPPLEMENTAL`;
- `PARAPHRASE_ROUTE`.

---

# XVII. V1 legacy discovery rule

V1 may identify scene-level characterization that V2's thematic synthesis underweighted. It is useful for rediscovering:

- jokes;
- habits;
- ordinary interactions;
- voice observations;
- memorable small scenes;
- craft notes.

But V1 is never the final basis of a CMR claim.

For every V1-derived candidate:

1. identify the underlying source scene;
2. retrieve it in the Japanese primary source or canonical V2 deep reading;
3. check L01/L02/L09 and relevant specialist home;
4. check the V1→V2 revision infrastructure if the claim is interpretively material;
5. retain only the re-grounded current formulation.

Mark unverified legacy discoveries `V1_DISCOVERY_PENDING_REGROUNDING` and exclude them from canonical profile prose until resolved.

---

# XVIII. Synthetic/generated-content firewall

This layer will eventually be used for hypothetical dialogue and behavioral reconstruction. That use creates a serious contamination risk.

The firewall is absolute.

## 1. Synthetic output is never evidence

Generated dialogue, crossover scenes, imagined reactions, counterfactuals, and model-created Japanese cannot be cited as proof of characterization.

## 2. Synthetic output never enters the diagnostic locator index

Only source-derived material belongs in `86_CHARACTER_DIALOGUE_AND_BEHAVIOR_LOCATOR_INDEX.tsv`.

## 3. Synthetic Japanese must never fill a lexical gap

If the corpus does not show how a character would phrase something, the correct result is uncertainty, not model-authored Japanese presented as characteristic.

## 4. Reconstruction tests are temporary QA

A model may privately or temporarily generate test outputs to see whether the profile distinguishes states or relationships. Those outputs test the **usefulness of the profile**, not the truth of the generated scene.

If preserved at all outside scratch space, every synthetic example must carry both labels:

`SYNTHETIC_NON_EVIDENCE`\
`RECONSTRUCTION_TEST_ONLY`

Canonical profiles should normally omit synthetic dialogue entirely.

## 5. Failed reconstruction returns to evidence

If a test reveals ambiguity, reopen the source evidence. Do not solve an evidence problem by generating additional examples.

---

# XIX. Mischaracterization-trap protocol

Every profile must include a mandatory section identifying the most likely ways a later model will flatten the character.

A useful trap is specific and falsifiable.

Weak:

> Do not misunderstand the character.

Strong:

> Do not make every Shin line emotionally explicit merely because the scene is intimate; his development often consists of new admissions inside still-low-excess syntax.

Potential trap classes include:

- trauma reduction;
- theme reduction;
- protagonist-orbit reduction;
- competence = adulthood;
- reserve = lack of care;
- roughness = stupidity;
- politeness = submission;
- archaic speech = constant grandiosity;
- comic scene = noncanonical filler;
- one crisis state = stable baseline;
- romantic attachment = sole motive;
- institutional title = essential identity;
- accurate insight = omniscience;
- support = obedience;
- rejection of pity = rejection of all care;
- artificial origin = generic robotic personality.

Each trap should route to at least one positive counterexample in the diagnostic scene bank or locator index.

---

# XX. "Would sound wrong if..." constraints

Negative constraints are required because a model can produce a thematically plausible character who nevertheless sounds wrong.

These constraints should identify violations such as:

- register too modern or too archaic for the established idiolect;
- emotional verbosity inconsistent with baseline;
- therapeutic vocabulary unsupported by the source;
- unexplained abandonment of habitual self-reference;
- incorrect title/name/honorific for the interlocutor;
- uniform politeness across relations where the source shows variation;
- philosophical eloquence replacing practical speech;
- inability to joke when the source clearly establishes comic range;
- generic sarcasm assigned to a character whose humor works differently;
- extreme-state behavior treated as ordinary;
- total certainty where the character normally hedges;
- immediate apology where the established repair style is behavioral or delayed.

These are constraints, not immutable laws. If the source contains a meaningful exception, note it.

---

# XXI. Required profile architecture

Every character profile should preserve the following semantic responsibilities, while allowing proportional length.

1. **Authority and scope**
2. **Reconstruction thesis**
3. **Stable personality baseline**
4. **Behavioral grammar**
5. **Japanese voice fingerprint**
6. **Relationship-conditioned registers**
7. **Emotional-state deltas**
8. **Ordinary-life texture**
9. **Humor and comic rhythm**
10. **Conflict and disagreement style**
11. **Care style**
12. **Body, gesture, and embodied characterization**
13. **Values in behavioral form**
14. **Mischaracterization traps**
15. **Would-sound-wrong constraints**
16. **Diagnostic scene bank**
17. **Reconstruction confidence and open uncertainties**
18. **Authority routing / crosswalk summary**

Profiles may add character-specific sections when needed, but should not delete these responsibilities merely because a theme is already covered elsewhere.

---

# XXII. Diagnostic scene bank protocol

A profile's scene bank should be small enough to retrieve and diverse enough to prevent flattening.

## 1. Selection principle

Choose scenes for **diagnostic contrast**, not fame.

A scene qualifies when it reveals one or more of:

- resting baseline;
- ordinary humor;
- relationship-specific register;
- emotional-state delta;
- care style;
- conflict style;
- role competence;
- self-disclosure;
- unusual break from baseline;
- bodily-state effect;
- future-oriented desire.

## 2. Scene-bank metadata

Each entry should provide:

- compact scene label;
- source volume/supplement;
- canonical locator ID or `LOCATOR_GAP`;
- target/interlocutor;
- state tag;
- why the scene is diagnostic;
- relevant CMR index entry ID once CMR-3 exists.

## 3. No quotation dumping

The scene bank routes to evidence. It should not reproduce long source passages.

---

# XXIII. Reconstruction confidence and behavioral prediction

Profiles may support bounded prediction using language such as:

- "typically";
- "often";
- "with this interlocutor";
- "under this kind of pressure";
- "the corpus strongly supports";
- "the evidence suggests";
- "no stable pattern is established."

Avoid `always`, `never`, `definitely`, or universal rules unless the source genuinely supports them.

Before predicting behavior, identify:

1. current developmental boundary;
2. relationship context;
3. emotional/physical state;
4. public/private or institutional setting;
5. whether the situation resembles any attested diagnostic scene;
6. counterevidence;
7. confidence band.

Prediction is strongest when multiple attested conditions overlap. It weakens rapidly when the scenario requires values, institutions, technologies, cultural assumptions, or relationship states absent from the corpus.

---

# XXIV. Directed relationship/register matrix method

`86_CHARACTER_RELATIONSHIP_REGISTER_MATRIX.md` becomes the cross-character comparison surface.

Each row should minimally include:

| Speaker | Target | Time/scope | Context | Self-reference | Target address | Politeness/register | Command/request style | Relational behavior | Significant shift | Locator route | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|

A relationship should receive more than one row when its register materially changes across:

- early/mid/late development;
- public/private setting;
- battlefield/household setting;
- ordinary/crisis state.

Do not create rows simply for symmetry when the source offers no meaningful evidence.

---

# XXV. Crosswalk method

`86_CHARACTER_MODELING_CROSSWALK.md` prevents the CMR layer from becoming a parallel canon.

For every profile section, route to the narrowest existing authority:

- Documents 02–12 where relevant;
- L01 character state;
- L02 relationship state;
- L09 voice/address;
- other longitudinal ledgers where needed;
- V01–V14 deep readings;
- Alter.1 when used;
- diagnostic locator index;
- Phase-5 locator ID where available;
- Document 16 for high-value Japanese passage control.

The crosswalk answers:

> **Where did this profile conclusion come from, and where should a later model go if it needs more precision than the profile provides?**

---

# XXVI. Profile lifecycle and authority states

## 1. Draft

New profiles begin:

`status: active_provisional`

They remain provisional through initial drafting and diagnostic evidence collection.

## 2. Pilot/QA state

A profile may be structurally complete while still awaiting reconstruction or retrieval QA. Do not promote early for convenience.

## 3. Canonical promotion

Promotion to `canonical` requires passing all applicable CMR-9 gates:

- source grounding;
- state-versus-trait;
- relationship specificity;
- V1 contamination;
- synthetic contamination;
- thematic flattening;
- reconstruction test;
- retrieval test.

CMR-2 Frederica remains a pilot until the method itself survives the stress test. If the pilot exposes a methodological gap, revise this method before scaling.

---

# XXVII. QA gates

## Gate A — Source grounding

PASS requires:

- no unsupported Japanese quotation;
- no invented address forms;
- no invented relationship changes;
- every load-bearing voice claim has a source route;
- every diagnostic scene routes to source evidence;
- quotation state is clear.

## Gate B — State versus trait

PASS requires that the profile distinguish:

- anger from baseline;
- grief from baseline;
- battlefield from ordinary behavior;
- injury state from personality;
- development from timeless essence;
- comic behavior from noncanonical filler.

## Gate C — Relationship specificity

PASS requires:

- no assumption of one universal register;
- major relation-specific differences recorded where supported;
- `A → B` and `B → A` kept distinct;
- isolated address forms not overinterpreted.

## Gate D — V1 contamination

PASS requires every retained V1 discovery to be re-grounded in current source/V2 evidence.

## Gate E — Synthetic contamination

PASS requires:

- no generated quotation treated as source;
- no synthetic Japanese in evidence sections;
- no generated material in the locator index;
- any temporary reconstruction output clearly quarantined outside evidence.

## Gate F — Thematic flattening

Remove the character's name and ask whether the profile would still unmistakably describe that person.

If the result could describe several characters merely by swapping theme words, FAIL.

## Gate G — Reconstruction test

For every substantial profile, temporarily test at least three states:

- ordinary;
- conflict/pressure;
- vulnerability.

For major characters, also test at least one relationship-conditioned contrast.

The test asks whether outputs are distinguishable **because of source-grounded constraints**, not because the model improvises archetype flavor.

Synthetic test outputs are discarded or quarantined.

## Gate H — Retrieval test

A later reader/model must be able to move:

profile → relationship/register matrix → diagnostic locator index → canonical analytical home/ledger → locked or transparent primary-source route.

If answering a basic voice-state question requires rediscovering the full corpus from scratch, FAIL.

## Gate I — Contradiction audit

For every `HIGH` stable trait, search for the strongest meaningful counterexample.

Outcomes:

- `SURVIVES` — counterexample is state/relationship-specific and does not overturn baseline;
- `NARROW` — trait needs context restriction;
- `DOWNGRADE` — confidence should be reduced;
- `OPEN` — model should not stabilize the trait.

This additional gate prevents the layer from converting recurrence into deterministic personality law.

---

# XXVIII. Frederica pilot acceptance test

Frederica is the first profile because she stresses nearly every dimension simultaneously.

The pilot must preserve all of these at once:

- former imperial status;
- adopted-family position;
- genuine childhood;
- unusual political/historical intelligence;
- comic range;
- fear and grief;
- archaizing identity-bearing diction;
- self-rule;
- relationship-specific affection;
- inherited political symbolism;
- resistance to adults treating competence as adulthood.

## 1. Non-negotiable idiolect control

Her `わらわ / そなた` system and related archaizing register must remain visible across serious and comic contexts where the source does so.

The profile must not "modernize" her for emotional accessibility.

## 2. Non-grandiosity control

Archaic diction does not mean every line is ceremonial, philosophical, or regal. The pilot must recover ordinary irritation, teasing, fear, embarrassment, practical complaint, and childlike need inside the same broad idiolect.

## 3. State differentiation test

The profile must support source-traceable distinctions among at least:

- ordinary/household Frederica;
- joking/teasing Frederica;
- frightened Frederica;
- grieving Frederica;
- politically assertive Frederica;
- Frederica speaking as family;
- Frederica confronting inherited sovereignty.

If these states collapse into one "wise child-empress" voice, the method fails.

## 4. Relationship differentiation test

At minimum, examine directed registers involving:

- Frederica → Shin;
- Shin → Frederica;
- Frederica → Ernst;
- Ernst → Frederica;
- Frederica → Kiriya where source boundary permits;
- Frederica → the surviving Spearhead peers;
- Frederica → Vika where relevant.

## 5. Authority-bounded insight

Frederica's perceptiveness is evidence of perceptiveness, not omniscience. Her diagnoses of Shin, Annette, Ernst, or political actors must be separated into:

- what she directly knows;
- what she infers;
- where later evidence corroborates her;
- where her projection or own wound may color the reading.

## 6. Pilot verdict

CMR-2 ends with one of:

- `METHOD_PASS`;
- `METHOD_PASS_WITH_NARROW_AMENDMENT`;
- `METHOD_REVISION_REQUIRED`.

Do not begin full CMR-4 scaling until the pilot receives the first or second verdict and any amendment is applied.

---

# XXIX. Initial roster retrieval emphases

These emphases guide evidence mining; they are not conclusions to impose.

## Shin

Prioritize low-excess syntax, deadpan/ordinary speech, command, help-seeking, semantic admission, Fido/peer/Frederica/Lena differences, bodily concealment, and the difference between self-expendability and a simple death wish.

## Lena

Prioritize officer/public/private registers, cultivated politeness, command, moral certainty and self-correction, Shin intimacy, Shiden-specific address, and how emotion enters without erasing professional competence.

## Raiden

Prioritize rough colloquial speech, practical correction, mundane caretaking, humor, peer authority, anger, and independent future content beyond his stabilizer function.

## Theo

Prioritize sarcasm, art, critical perception, the difference between cruelty and insight, humor, bodily change, accommodation, and boundary-sensitive care.

## Kurena

Prioritize emotional transparency, `あたし`, jealousy without jealousy-reduction, professional marksmanship, embarrassment, fear of uselessness, and belonging after romantic nonselection.

## Anju

Prioritize restraint, social composure, buried anger, domestic competence, Daiya/Dustin continuity, grief without permanent memorialization, and under-verbalized affection.

## Shiden

Prioritize abrasive register, Lena-specific relational language, independent command competence, protective interruption, and identity outside original Spearhead.

## Ernst

Prioritize public-office versus household register, theatricality, idealism, paternal affection, benevolence becoming control, rage/breakdown, and Frederica's capacity to challenge him.

## Grethe

Prioritize adult military professionalism, engineering/technical discourse, sarcasm/humor where attested, command, and care for exceptional soldiers without reducing them to assets.

## Annette

Prioritize technical/scientific speech, bluntness, guilt, friendship with Lena, childhood history with Shin, and behavior when another person's bodily risk activates responsibility or fear.

## Vika

Prioritize aristocratic/intellectual register, technical abstraction, moral distance and specific attachments, Sirin-related language, eccentric humor, and the limits of brilliance as moral authority.

## Lerche

Prioritize `それがし`, retainer grammar, `死神殿`, service vocabulary, role-coded formality, humor, individuality within artificial continuity, and Vika-specific relation.

## Rito

Prioritize younger-soldier relation to the core group, ordinary speech, nonrevenge versus forgiveness, moral action, public memory, and how his perspective differs from Shin's.

## Marcel

Prioritize hostility, guilt, Eugene, later responsibility, accusation/remorse register, and change that does not erase earlier wrongdoing.

## Fido

Prioritize formal artificial voice, observer/witness function, loyalty, memory, ordinary companionship, humor, and evidence for relational particularity without assuming one simple ontology of machine personhood.

---

# XXX. Update protocol when the source boundary expands

When V15+ is added, do not silently rewrite canonical profiles.

Use the series source-lock/update process first. Then classify each profile-level change using the project's revision vocabulary:

- `PRESERVE`;
- `STRENGTHEN`;
- `REVISE`;
- `DOWNGRADE`;
- `REJECT`;
- `OPEN`.

For each changed profile, record:

- prior formulation;
- new evidence;
- disposition;
- new source boundary;
- whether a voice baseline, relationship register, or state model changes;
- whether old diagnostic scenes remain representative.

A later volume may reveal that an apparent stable trait was developmental, or that a rare exception was the first sign of a new repertoire. Preserve the earlier state rather than pretending the new evidence was always available.

---

# XXXI. Canonical profile front-matter template

Before QA promotion:

```yaml
series: "86-Eighty-Six"
series_id: "86"
artifact_type: "character_reference_profile"
character: "<source-attested display name>"
scope: "V01-V14+ALTER1"
generation: "V2"
status: "active_provisional"
source_boundary: "Locked original-Japanese V01-V14; Alter.1 audited supplemental"
governing_method: "86_CHARACTER_MODELING_REFERENCE_METHOD.md"
primary_locator_authority: "86_PHASE5_LOCKED_LOCATOR_INDEX.tsv"
supersedes: null
superseded_by: null
do_not_use_as_current_authority: false
```

After all QA gates pass, `status` may become `canonical` without changing the semantic responsibility of the artifact.

---

# XXXII. Controlled state and evidence tags

The following vocabulary should be preferred for interoperability across profiles, the locator index, and register matrix.

## State tags

- `ORDINARY`
- `HOUSEHOLD`
- `COMIC`
- `TEASING`
- `AFFECTION`
- `EMBARRASSMENT`
- `IRRITATION`
- `ANGER`
- `FEAR`
- `GRIEF`
- `EXHAUSTION`
- `INJURY`
- `COMMAND`
- `COMBAT_STRESS`
- `IDEOLOGICAL_CONFLICT`
- `SELF_DISCLOSURE`
- `CARE_GIVING`
- `CARE_RECEIVING`
- `FAILURE`
- `GUILT`
- `UNCERTAINTY`
- `FUTURE_DESIRE`
- `REFUSAL`
- `MORAL_INTERRUPTION`

Use combinations when necessary rather than forcing one dominant tag.

## Modeling evidence tags

- `DIRECT_SOURCE_FACT`
- `REPEATED_BEHAVIORAL_PATTERN`
- `RELATIONSHIP_CONDITIONED_PATTERN`
- `EMOTIONAL_STATE_DELTA`
- `HIGH_CONFIDENCE_INFERENCE`
- `OPEN_INFERENCE`
- `LOCATOR_GAP`
- `ALTER1_SUPPLEMENTAL`
- `RARE_BREAK`
- `DEVELOPMENTAL_FIRST`
- `CRISIS_ONLY`

---

# XXXIII. Retrieval routes

## Character reconstruction

`CURRENT_STATE_AND_CORPUS_MAP.md`\
→ `86_<CHARACTER>_CHARACTER_REFERENCE_PROFILE.md`\
→ `86_CHARACTER_RELATIONSHIP_REGISTER_MATRIX.md`\
→ `86_CHARACTER_DIALOGUE_AND_BEHAVIOR_LOCATOR_INDEX.tsv`\
→ relevant L01/L02/L09 and specialist document\
→ Phase-5 locator or transparent `LOCATOR_GAP` source route\
→ original Japanese source

## Exact Japanese wording

Document 12\
→ Document 16\
→ Phase-5/Phase-8 route\
→ original Japanese source

## Character development

Profile\
→ L01 / relevant specialist character or ensemble document\
→ sequential deep reading\
→ source

## Relationship/register question

Profile\
→ directed register matrix\
→ L02 + L09\
→ diagnostic index\
→ source

## Hypothetical behavior

Profile constraints\
→ relationship matrix\
→ diagnostic scenes\
→ identify confidence and unmatched scenario features\
→ generate only as `SYNTHETIC_NON_EVIDENCE`

---

# XXXIV. Completion standard for the Character Modeling Reference layer

The layer is complete only when:

- this method is canonical;
- all sixteen initial profiles exist and have passed QA;
- the directed relationship/register matrix covers the major relations actually evidenced by the roster;
- the diagnostic dialogue/behavior index is populated with retrievable source routes;
- the crosswalk routes profile sections back into the established V2 authority system;
- no synthetic output has contaminated evidence;
- V1-derived discoveries have current grounding;
- the corpus map and architecture reflect completion;
- the final README contains the reconstruction retrieval route;
- release manifests and checksums include the new layer.

The standard is not equal document size. It is **traceable reconstructability proportional to evidence density**.

---

# XXXV. Final governing principles

1. **Source before flavor.** A distinctive line unsupported by the text is worse than a restrained uncertainty.
2. **Flavor before abstraction.** A profile that merely repeats thematic theses has failed even if every thesis is correct.
3. **State is not trait.** Fear, grief, battle, injury, and embarrassment can reveal a person without defining their entire baseline.
4. **Relation is directional.** The way A speaks to B is not the way B speaks to A, and neither necessarily generalizes elsewhere.
5. **Voice is contextual.** Written Japanese idiolect is a repertoire, not a single frozen register.
6. **Ordinary life is evidence.** Low-pressure scenes control against crisis-only caricature.
7. **Inference stays labeled.** Plausibility does not become fact through confident prose.
8. **Negative constraints matter.** Knowing what would sound wrong is part of high-fidelity reconstruction.
9. **Synthetic work is quarantined.** A convincing reconstruction validates the model's usefulness, never its own canonicity.
10. **The profile is a router.** It should make the Japanese source easier to recover, not easier to forget.

The practical success criterion is simple:

> **A future model should be able to reconstruct the character's recognizable voice, ordinary personality, emotional variation, relationship-conditioned behavior, and uncertainty boundaries while remaining traceable to the canonical Japanese evidence.**

# XXVII. CMR-10 release integration

CMR-10 integrated this method into frozen release `86-V2-V01-V14-1.0` on 2026-08-20. This administrative transition changes the canonical entrypoint from the active-work `CURRENT_STATE_AND_CORPUS_MAP.md` to `00_README_AND_CORPUS_MAP.md` and records the completed architecture version. It does not broaden the V01–V14 + Alter.1 source boundary, alter the evidence model, authorize generated dialogue as evidence, or elevate CMR above narrower Japanese-primary and V2 authorities.
