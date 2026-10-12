---
series: YOUJO_SENKI
artifact_type: character_modeling_reference_method
scope: V01-V14
source_media: Japanese light novels
source_boundary: "Original Japanese Youjo Senki light novels Volumes 01-14 in Drive source folder 1s8Ido1uUbAyR-lXstTyOVfoeHaUDop-g"
generation: V2_CMR
version: "1.1"
status: active_provisional
canonical_home: "series/youjo-senki/CMR/Methods/YOUJO_SENKI_CHARACTER_MODELING_REFERENCE_METHOD.md"
primary_source_root: "1s8Ido1uUbAyR-lXstTyOVfoeHaUDop-g"
primary_source_audit_manifest: "1JXarPgypYVSdzAexUyyOa4qH8mxlyHcx"
translation_audit_ledger: "1mQno_ayho-R3jacL374LrNamAe_Sbkf0"
parent_analysis_status: "Mature V2 interpretation remains Git-primary at series/youjo-senki/V2 Analysis; CMR is subordinate reconstruction infrastructure."
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
artifact_id: YOUJO_SENKI_CHARACTER_MODELING_REFERENCE_METHOD
port_revision: "1"
port_date: 2026-10-11
source_drive_id: "16tMcTb0rZZ7U3gjidf6bzJ-TravNQcCh"
source_drive_revision: "0B24avie5yJngSElKajFBL2hDaFE4Qm9vazUweGdMcldtT3BzPQ"
source_sha256: "405d89789d730ec3ccdff1de020d318dc39c9910b36577d2b3e1f63a52737361"
historical_drive_home: "Youjo Senki/06 Character Modeling and Reconstruction/00 Frameworks and Methods"
promotion_status: PROPOSED_PENDING_VERIFIED_MAIN_INTEGRATION
former_drive_pointer_update_status: NOT_PERFORMED
---

> **Git port proposal.** The complete v1.1 method body is preserved below. This branch artifact remains `active_provisional`; promotion of this analytical home awaits verified main integration. The original Drive method is the retained, revision-bound source for the port. Its planned pointer/supersession metadata update has not been performed.

The series first-read route remains [CURRENT_STATE_AND_CORPUS_MAP.md](../../CURRENT_STATE_AND_CORPUS_MAP.md). Mature literary interpretation remains in `series/youjo-senki/V2 Analysis/`, including the Japanese/English warning layer in Document 12. The original Japanese V01–V14 EPUBs and source-derived bulk evidence remain in Drive. This working Git method adds no source range, adaptation material, private-life facts, or completed model by its existence.

The original Drive hierarchy named in Section XV and the body is retained as the **historical v1.1 architecture**. Its intended Git allocation is:

| Original Drive responsibility | Intended current allocation |
|---|---|
| `00 Frameworks and Methods` | `CMR/Methods/` for eligible methodological authority |
| `01 Evidence and Locators` | Drive for EPUBs, deterministic extracted text, raw locator/member/alias/metrics/candidate/diagnostic ledgers and audited source scripts; `CMR/Diagnostics/` for authored interpretive findings and compact navigation |
| `02 Character Models` | `CMR/Models/` for source-limited operational models |
| `03 Relationship Registers` | `CMR/Relationships/` for directional analytical registers |
| `04 QA and Simulation` | `CMR/QA/` for analytical validation and uncertainty records |
| Port, preservation, and authority reconciliation | `CMR/Provenance/` |

These are responsibility allocations. Directories are populated only when real artifacts exist. Until the project CMR index is created, use the existing series entrypoint; no planned model or QA file is represented as already complete. The [port audit](../Provenance/YOUJO_SENKI_CMR_PORT_AUDIT.md) and [historical CMR1 baseline](../Provenance/YOUJO_SENKI_CMR1_READINESS_BASELINE.md) record the controlled transformations and intake evidence limits.

<!-- Preserved v1.1 substantive method body begins below. -->


# YOUJO SENKI CHARACTER MODELING REFERENCE METHOD
## Source-grounded reconstruction of voice, preferences, behavior, speech, relationships, and scenario-conditioned action

## 0. Purpose

This document governs the *Youjo Senki* Character Modeling and Reconstruction (CMR) layer.

The purpose of CMR is narrower than literary synthesis and more demanding than a conventional character profile. The existing analytical corpus already explains the series at the level of Tanya Degurechaff's psychology, military professionalism, political economy, institutional logic, war, doctrine, translation, ethics, and strategic structure. CMR exists to answer a different class of question:

> **Given a particular character, developmental point, relationship, situation, stake level, and information state, what patterns of attention, appraisal, behavior, speech, and register are strongly supported by the primary source, and how far can those patterns be extrapolated before the result becomes invention?**

A successful model should support high-fidelity recognition and bounded simulation across both high-stakes and low-stakes contexts. It should be useful for questions such as:

- What would Tanya notice first in this situation?
- What would she privately think, and what would she actually say aloud?
- How would her wording change with Zettour, Visha, Weiss, Lergen, a civilian, an enemy officer, or Being X?
- How does she behave when she is frightened, angry, exhausted, professionally irritated, relieved, materially comfortable, or off duty?
- Which ordinary preferences and habits are actually evidenced rather than inferred from thematic characterization?
- Which behaviors remain stable across career stages, and which belong to a particular rank, command role, or war phase?
- Which characters besides Tanya have enough source coverage to support full-spectrum reconstruction, and which only support domain-bounded models?
- When is a generated line recognizably character-consistent, and when is it merely thematically plausible fan fiction?

The governing principle is:

> **Make the character recoverable as a person without mistaking a reconstruction tool for canon.**

Generated simulations are never primary evidence, never self-training data, and never allowed to create new canonical facts.

---

# I. Authority and source hierarchy

## 1. Primary-source authority

The original Japanese light novels are the evidentiary authority for CMR.

Current source boundary:

- Volumes 01-14;
- Japanese-language EPUBs supplied by the user;
- source folder Drive ID `1s8Ido1uUbAyR-lXstTyOVfoeHaUDop-g`;
- source audit manifest Drive ID `1JXarPgypYVSdzAexUyyOa4qH8mxlyHcx`.

The audit manifest records fourteen ebooks spanning Volumes 01-14. Thirteen are structurally conformant EPUB containers. Volume 02 has a container-level mimetype-order/compression irregularity but passes ZIP integrity and otherwise remains readable. This is an ingestion issue, not a literary-evidence demotion.

## 2. Analytical authority

The existing V2 multi-document *Youjo Senki* synthesis remains the current analytical authority for mature series-level claims. CMR does not replace, renumber, or silently revise that corpus.

CMR is a derived reference layer. Its job is to transform already-understood characterization into source-verifiable behavioral and linguistic constraints, and to recover low-level evidence that broad synthesis naturally compresses.

Authority order for reconstruction work:

1. original Japanese primary source;
2. source-audit and exact locator infrastructure produced by CMR;
3. existing canonical V2 analytical documents, including the Japanese/English translation audit where relevant;
4. CMR diagnostic index, ordinary-life ledger, relationship-register matrix, and character models;
5. generated examples and held-out simulations.

If a CMR profile conflicts with the Japanese source, the source controls.

If a CMR profile conflicts with a narrower canonical analytical claim whose source basis is stronger, the narrower authority controls until the discrepancy is re-audited.

## 3. Adaptation boundary

This method models the **written-Japanese light-novel characters**.

Anime acting, voice-actor prosody, pitch, timing, facial animation, shot staging, anime-original dialogue, and adaptation-specific behavior must not be silently merged into this layer. They may later form a separately labeled audiovisual adaptation model.

"Voice" in this method means written Japanese idiolect and discourse behavior unless explicitly labeled otherwise.

---

# II. The central Youjo Senki reconstruction problem

## 1. Do not collapse cognition, behavior, speech, and reputation

For Tanya in particular, characterization frequently exists in the gap between what she privately wants and what other people think she wants.

Every diagnostic scene should therefore distinguish five channels where evidence exists:

1. **Private cognition** - what the character actually thinks, fears, wants, calculates, remembers, or infers.
2. **Observable behavior** - what the character physically or institutionally does.
3. **Public speech / presentation** - what the character says given role, rank, audience, doctrine, and professional constraints.
4. **External interpretation** - what other characters believe the behavior or speech means.
5. **Institutional consequence** - what the organization, chain of command, propaganda system, enemy, or social environment does with that interpretation.

This separation is mandatory for Tanya and strongly recommended for every character whose role performance diverges from private motive.

A common Tanya sequence is:

> private fear or self-preservation -> professionally rational action -> outward appearance of courage/zeal -> superior misinterpretation -> greater responsibility/exposure

A model that collapses the sequence into "Tanya is fearless and aggressive" has failed even if the final action is superficially correct.

## 2. Private narration is not spoken dialogue

Tanya's internal language can be substantially more:

- sardonic;
- economically reductive;
- frightened;
- hostile;
- irreverent;
- bureaucratically cynical;
- openly contemptuous of Being X;
- or dismissive of romanticized military ideals

than her outward professional speech.

The simulator must never use internal monologue as a generic speech corpus.

A line can be psychologically Tanya-like and still be dialogue Tanya would not say aloud to that interlocutor.

## 3. Speech reconstruction is a transformation pipeline

Speech reconstruction is not a synonym for imitating vocabulary. For characters with sufficient evidence, the model must reconstruct the causal transformation from private state into an utterance appropriate to the immediate social situation.

Required speech-generation chain:

> `private appraisal -> communicative objective -> speech act -> relationship/role constraint -> register -> surface wording`

This chain is especially important for Tanya because psychologically characteristic thoughts are often precisely the thoughts she does **not** say aloud. A generated line is not high-fidelity merely because its content resembles her internal narration.

For each speech-bearing diagnostic scene, distinguish where evidence permits:

- what the character privately appraises;
- what the character wants the interlocutor to understand, do, believe, or refrain from doing;
- what private content is withheld or reformulated;
- which speech act is selected;
- what rank, relationship, setting, and face-management constraints apply;
- which register is selected;
- and what surface wording results.

Speech must therefore be evaluated at two levels:

1. **decision fidelity** - whether the character chose the appropriate communicative act;
2. **surface fidelity** - whether the wording, politeness, syntax, address, and rhythm fit the Japanese source profile.

A model may be psychologically correct and linguistically wrong, or linguistically recognizable and psychologically wrong. Both failure modes must remain visible.

## 4. Military role is part of personality expression

Rank, assignment, chain of command, staff/field role, unit responsibility, and legal authority are not background metadata. They constrain behavior and language.

The model must know whether Tanya is:

- a cadet;
- junior officer;
- staff-college student;
- battalion commander;
- combined-arms commander;
- subordinate addressing General Staff authority;
- superior issuing orders;
- officer speaking to civilians;
- officer speaking outside formal duty;
- or human confronting Being X outside ordinary institutional legitimacy.

A scenario without role state is underspecified.

---

# III. Reconstruction-readiness audit

Before creating a full character model, conduct a coverage audit. Plot importance alone does not justify simulation.

## 1. Required evidence dimensions

For each candidate character, assess:

### A. Direct dialogue density
Enough speech must exist to distinguish stable register from topic-specific phrasing.

### B. Observable action density
The corpus must contain decisions and actions, not merely descriptions or other characters' opinions.

### C. Internal access
Record whether the novels provide direct thought, focalization, retrospective reflection, or only external observation.

Lack of internal POV does not disqualify a character, but it lowers the ceiling on claims about private motive.

### D. Temporal spread
Evidence should span enough of the character's arc to distinguish stable traits from one crisis.

### E. Context diversity
Relevant contexts include, where available:

- routine work;
- staff/planning work;
- command;
- combat;
- training;
- disagreement;
- recovery;
- travel;
- meals/socializing;
- boredom;
- private conversation;
- ideological or existential crisis.

### F. Relationship diversity
A full-spectrum model should ideally show the character with more than one relational class:

- superior;
- subordinate;
- peer;
- familiar/intimate associate;
- stranger/civilian;
- enemy or political counterpart.

### G. Stake diversity
High-stakes evidence alone is insufficient for a full-spectrum person model. Low-stakes evidence alone is insufficient for crisis reconstruction.

### H. Linguistic distinctiveness
There must be enough Japanese-language material to identify pronouns, address behavior, politeness, syntax, speech acts, and contextual register.

### I. Counterevidence
A good model needs enough material to identify exceptions and failed generalizations.

## 2. Coverage classes

### `FULL_SPECTRUM`
Supports broad reconstruction across multiple relationships, stakes, developmental states, and situation classes.

### `DOMAIN_BOUNDED`
Supports high-confidence reconstruction inside one or more well-attested domains, but should not invent private or ordinary-life behavior outside them.

### `RECOGNITION_PROFILE`
Supports judging whether a proposed line or action is compatible with the character, but not free generation across novel situations.

### `INSUFFICIENT`
Evidence is too thin or too one-dimensional for a stable model.

## 3. Provisional pilot roster

These are hypotheses to audit, not preauthorized conclusions:

- **Tanya Degurechaff** - expected `FULL_SPECTRUM`; first pilot.
- **Viktoriya Ivanovna Serebryakov** - expected high `DOMAIN_BOUNDED`, possibly `FULL_SPECTRUM` after audit.
- **Erich von Lergen** - expected `FULL_SPECTRUM` or high `DOMAIN_BOUNDED`, with unusually valuable Tanya-observer evidence.
- **Hans von Zettour** - expected high `DOMAIN_BOUNDED`; strong strategic/institutional model, likely lower ordinary-private ceiling.
- **Kurt von Rudersdorf** - expected `DOMAIN_BOUNDED`, strong operations/command coverage.
- **Matheus Johann Weiss** - expected `DOMAIN_BOUNDED`, strong subordinate/unit/command evidence.
- **Mary Sue** - expected developmental `DOMAIN_BOUNDED`; strong state dependence must be preserved.
- **Romel, Schugel, Drake, Uger, and others** - audit before promotion.

Do not promote a character merely because they are memorable, ideologically interesting, or narratively important.

---

# IV. Primary-source extraction and locator model

## 1. Stable locator principle

EPUB "page numbers" are not assumed to be stable across readers.

Preferred locator format:

`VNN / EPUB member / paragraph ordinal / short Japanese anchor`

Example abstract form:

`V04 / OEBPS/Text/chapter03.xhtml / p0142 / <short anchor>`

The locator must survive extraction reruns and support reopening the exact source context.

## 2. Preserve source distinctions

Extraction should preserve where possible:

- chapter/section structure;
- paragraph boundaries;
- dialogue versus narration;
- Japanese punctuation;
- ruby/furigana relations;
- emphasis;
- ranks, titles, callsigns, and names;
- scene breaks;
- source file identity and checksum.

Do not normalize all character names into one form inside the evidence text. Use an alias map separately.

## 3. Character alias authority

Create a controlled alias table covering:

- full name;
- surname;
- given name;
- military rank/title;
- callsign;
- nickname;
- Japanese orthographic variants where relevant.

The alias table exists for retrieval. It must not rewrite evidence into a uniform voice.

---

# V. Diagnostic dialogue-and-behavior index

The core CMR evidence artifact is a source-verified diagnostic index. It should not contain every sentence a character speaks. It should contain scenes that establish reusable behavioral or linguistic constraints.

## 1. Required diagnostic row fields

Each row should record, where applicable:

- `diagnostic_id`
- `character`
- `volume`
- `source_locator`
- `developmental_state`
- `rank_role`
- `pov_source`
- `evidence_mode`
- `interlocutor`
- `relationship_class`
- `power_relation`
- `setting`
- `stakes`
- `immediate_objective`
- `emotional_state`
- `physical_state`
- `information_state`
- `attention_target`
- `private_appraisal`
- `observable_behavior`
- `speech_act`
- `communicative_objective`
- `withheld_private_content`
- `speech_act_subtype`
- `directness_level`
- `politeness_register`
- `address_form`
- `disagreement_strategy`
- `disclosure_level`
- `humor_sarcasm_mode`
- `utterance_length_class`
- `short_japanese_anchor`
- `register_observations`
- `surface_voice_notes`
- `external_interpretation`
- `institutional_consequence`
- `evidence_class`
- `confidence`
- `counterevidence_or_exception`
- `inference_ceiling`

Not every field will be populated in every scene. Unknown must remain unknown rather than being reconstructed after the fact.

## 2. Diagnostic selection rules

Prefer passages that reveal one or more of the following:

- a recurring decision process;
- a clear register shift;
- divergence between thought and speech;
- response under a new stake level;
- response to a particular interlocutor;
- ordinary voluntary choice;
- reaction to praise, criticism, error, inconvenience, or uncertainty;
- failure and repair;
- an exception to an otherwise strong rule;
- developmental change.

Do not inflate the index with near-duplicate battlefield commands unless they add a new diagnostic dimension.

For speech reconstruction, diagnostic diversity should be preferred over raw dialogue volume. Deliberately seek examples of:

- reporting;
- requesting;
- ordering;
- refusing;
- warning;
- probing for information;
- bargaining;
- praising competence;
- correcting error;
- reprimanding;
- reassuring;
- motivating;
- politely disagreeing;
- concealing disagreement;
- signaling solidarity;
- joking or using sarcasm;
- receiving praise or hospitality;
- small talk and other low-stakes social speech.

The goal is to recover how the character performs different communicative functions, not merely what topics they discuss.

## 3. Tanya pilot scale

For Tanya, a target of roughly **250-350 genuinely diagnostic states** is reasonable because she has unusually dense internal access and wide context coverage.

This is not a quota. Diversity and source usefulness matter more than count.

Other characters may be adequately modeled with substantially fewer scenes if their behavioral space is narrower and well sampled.

---

# VI. Evidence classes and inference control

## `DIRECT_SOURCE_FACT`
Directly observed action, explicit preference, explicit statement, attested pronoun/address form, narrated physical behavior, or other source-level fact.

## `CHARACTER_STATEMENT`
What the character explicitly says about self, others, or the world. This is direct evidence of the statement, not automatic proof that the statement is true.

## `REPEATED_BEHAVIORAL_PATTERN`
A recurring tendency supported across more than one meaningful scene.

## `RELATIONSHIP_CONDITIONED_PATTERN`
A behavior or register stable with a particular person or relationship class but not established globally.

## `EMOTIONAL_STATE_DELTA`
A meaningful baseline change under fear, anger, exhaustion, pain, embarrassment, relief, affection, ideological threat, or another defined state.

## `ROLE_CONDITIONED_PATTERN`
A behavior or register tied to military rank, staff/field role, command responsibility, civilian context, or another institutional role.

## `OBSERVER_INTERPRETATION`
Another character's interpretation. Especially important for Tanya; never silently merge with Tanya's actual motive.

## `INSTITUTIONAL_EFFECT`
Observable consequence created by organization, chain of command, propaganda system, enemy, or social institution.

## `HIGH_CONFIDENCE_INFERENCE`
Multiple independent evidence channels converge but the conclusion is not directly stated.

## `OPEN_INFERENCE`
Potentially useful but underdetermined. Preserve uncertainty visibly.

---

# VII. Confidence rubric

Every predictive or summarizing claim should be assessed across:

1. **Directness** - observed versus inferred.
2. **Recurrence** - single scene versus repeated pattern.
3. **Context breadth** - survives across different situations or not.
4. **Temporal stability** - stable across developmental stages or phase-bound.
5. **Relationship scope** - general, role-specific, or person-specific.
6. **Counterevidence** - exceptions that narrow the rule.
7. **Source access** - internal POV, external observation, or unreliable report.

Use qualitative confidence bands:

- `HIGH`
- `MODERATE`
- `LOW`
- `OPEN`

Do not invent false numerical probabilities as evidence quality.

Scenario simulation may separately use qualitative likelihood labels such as `LIKELY`, `PLAUSIBLE`, `UNLIKELY`, and `OUT_OF_CHARACTER`, but these remain model judgments, not empirical percentages.

---

# VIII. Developmental-state model

A character model must preserve time.

## 1. Required state variables

At minimum, simulation packets should track where relevant:

- volume/era;
- rank;
- command role;
- unit/institution;
- current relationships;
- current knowledge;
- major prior experiences already occurred;
- physical condition;
- immediate threat level;
- public versus private setting.

## 2. Avoid retroactive competence

Later Tanya cannot be projected backward onto early Tanya.

Do not grant characters:

- future operational experience;
- later relationship familiarity;
- future information;
- later ideological conclusions;
- later command habits

before the relevant source boundary.

## 3. Avoid relationship leakage

A relationship has its own developmental state. The model should not use late-series familiarity when simulating an early encounter.

---

# IX. Behavioral grammar

A reconstruction model should encode **conditional tendencies**, not slogans.

Every full or domain-bounded profile should address the following where supported.

## 1. Attention

What does the character notice first?

Potential Youjo Senki domains include:

- threat;
- competence;
- rank/authority;
- objective ambiguity;
- logistical constraint;
- waste;
- morale;
- political consequence;
- doctrinal inconsistency;
- personal danger;
- subordinate condition;
- ideological enthusiasm;
- opportunity for institutional maneuver.

## 2. Appraisal under uncertainty

Does the character tend to:

- gather more information;
- reduce the issue to formal constraints;
- calculate risk;
- ask a superior;
- delegate;
- attack early;
- delay;
- seek legal/procedural cover;
- frame the problem in economic terms;
- invoke doctrine;
- rely on intuition or experience?

## 3. Intervention threshold

What moves the character from observation to action?

Distinguish danger to self, danger to subordinates, mission failure, incompetence, waste, illegal or illegitimate order, ideological threat, reputational danger, and institutional breakdown.

## 4. Decision style

Track:

- rapid versus deliberative;
- rule-constrained versus improvisational;
- principle-first versus consequence-first;
- consultative versus unilateral;
- private motive versus public justification;
- reversible versus commitment-heavy action.

## 5. Failure response

Does the character:

- self-blame;
- externalize;
- revise doctrine;
- gather evidence;
- overwork;
- punish;
- retrain;
- seek reassignment;
- document responsibility;
- conceal vulnerability;
- ask for help?

## 6. Repair after harm

Track whether repair occurs through:

- explicit apology;
- changed orders;
- material assistance;
- retraining;
- institutional correction;
- private reassurance;
- acceptance of criticism;
- avoidance;
- rationalization.

## 7. Tanya-specific provisional process model

The following is a hypothesis to be tested against the diagnostic index, not a final algorithm:

> perceive situation -> identify threats and formal constraints -> determine governing authority/duty -> estimate survival/resource/reputation costs -> identify legally and doctrinally available actions -> choose a viable course -> formulate professionally acceptable outward presentation -> act -> update based on others' interpretation and institutional consequence

Important constraint: self-preservation is central but not sufficient to predict Tanya. Mission duty, legitimate authority, subordinate responsibility, career incentives, law, doctrine, reputation, and available alternatives constrain what "self-preservation" means in practice.

---

# X. Japanese voice fingerprint

Every character with sufficient speech receives a written-Japanese voice model.

## 1. Required linguistic fields

Record where supported:

- first-person pronoun/self-reference;
- second-person forms;
- names, surnames, ranks, titles, callsigns, honorifics;
- baseline politeness;
- formal/casual alternation;
- military report language;
- command forms;
- request forms;
- refusal forms;
- modality and hedging;
- sentence length;
- fragmentation;
- ellipsis;
- rhetorical questions;
- characteristic sentence endings;
- technical, economic, bureaucratic, doctrinal, ideological, colloquial, or religious vocabulary;
- metaphor/analogy habits;
- humor and sarcasm;
- narration-versus-dialogue differences;
- emotional-state deltas;
- interlocutor-specific deltas.

## 2. Tanya must be modeled as multiple registers

At minimum distinguish:

### `INTERNAL_TANYA`
Adult-salaryman-derived cognition, private strategic/economic/legal framing, private fear and resentment, Being-X hostility.

### `SUPERIOR_FACING_TANYA`
Correct, professional, careful, useful, doctrinally literate, generally constrained by legitimate hierarchy.

### `COMMAND_TANYA`
Directive, economical, objective-focused, with tolerance for subordinate initiative conditioned by competence and mission.

### `STAFF_INTELLECTUAL_TANYA`
Abstract, analytic, doctrinal, economic, organizational, operational/strategic.

### `COMBAT_TANYA`
Compressed, immediate, action-oriented; internal emotion may intensify while external wording becomes more functional.

### `PRIVATE_OFF_DUTY_TANYA`
Lower-formality material to be source-audited rather than presumed; likely the main area where the current synthesis has compressed evidence.

### `BEING_X_TANYA`
Ordinary professional containment may fail because Tanya treats Being X as coercive and illegitimate rather than a valid institutional superior.

Do not create a generic "Tanya voice" by averaging these registers.

## 3. Speech-act and interaction reconstruction

For each modeled character with sufficient dialogue, maintain a speech-act layer that answers **how the character accomplishes communicative work** rather than merely cataloguing favored words.

At minimum, where evidence exists, recover how the character:

- reports information;
- requests action;
- gives orders;
- refuses or resists;
- disagrees;
- praises competence;
- criticizes failure;
- reassures;
- teaches or explains;
- probes for information;
- bargains;
- jokes;
- performs small talk;
- handles praise, gifts, hospitality, or unexpected kindness.

For each function, preserve relationship and state dependence. "How Tanya disagrees" is not one global template: disagreement with Zettour, Weiss, Visha, a civilian, or a stranger of equal apparent competence may use different levels of directness, disclosure, and institutional framing.

## 4. Translation-sensitive lexical warning layer

`V2 Analysis/12_JAPANESE_ENGLISH_TRANSLATION_AUDIT_LEDGER.md` (Drive `1mQno_ayho-R3jacL374LrNamAe_Sbkf0`) is the canonical warning layer for places where official English may obscure recurring Japanese conceptual or grammatical structure.

Speech reconstruction should consult it whenever source examples involve translation-sensitive networks such as:

- `僕 / 私`;
- `思想の自由`;
- `規律`;
- `理屈`;
- `人的資源 / 人的資本 / 人材 / 人財`;
- `勝ち癖`;
- `社会契約`;
- Reich / Heimat distinctions;
- title/allusion language that feeds a character's conceptual vocabulary.

The audit is not a replacement for reopening the Japanese source. Its purpose is to prevent English convenience wording from being mistaken for the character's stable Japanese lexical architecture.

## 5. Character-specific speech problem statement

Every promoted character model should identify its principal speech-reconstruction hazard. The shared schema is standardized; the main distortion risk is character-specific.

Initial hypotheses to test:

| Character | Primary speech-reconstruction hazard |
|---|---|
| Tanya Degurechaff | Private cognition being mistakenly verbalized; internal sarcasm/economic framing over-exported into public dialogue |
| Hans von Zettour | Stated conclusions being confused with what he wants others to infer; strategic indirection flattened into exposition |
| Erich von Lergen | Formal decorum flattening private alarm, moral judgment, and observer anxiety |
| Matheus Johann Weiss | Loyal disagreement flattened into either passive obedience or generic insubordination |
| Viktoriya Serebryakov | Familiarity with Tanya and comparatively ordinary social warmth being generalized to unrelated interlocutors |
| Mary Sue | Distinct developmental/ideological states collapsed into one permanently intensified voice |

These are hypotheses, not canonical findings. The diagnostic corpus may revise them.

---

# XI. Everyday-life, preferences, and material-habits ledger

Broad literary synthesis overweights crisis because crisis is narratively important. Simulation requires ordinary texture too.

Create a dedicated low-stakes evidence ledger for:

- food;
- drink;
- alcohol;
- sleep;
- fatigue;
- lodging;
- comfort;
- climate;
- clothing;
- money/pay;
- equipment preferences;
- reading/study;
- work routine;
- paperwork;
- leave;
- socializing;
- shopping;
- travel;
- boredom;
- preferred working environment;
- attitudes toward luxury;
- gifts;
- praise;
- hospitality;
- favors;
- small irritations;
- humor;
- leisure.

Recommended evidence classes:

- `EXPLICIT_PREFERENCE`
- `EXPLICIT_AVERSION`
- `VOLUNTARY_SELECTION`
- `REPEATED_SELECTION`
- `HABITUAL_PRACTICE`
- `OBSERVED_ENJOYMENT`
- `COMPETENCE`
- `SOCIAL_ACCOMMODATION`
- `CONSTRAINT_DRIVEN`
- `STATE_DEPENDENT`
- `OTHER_REPORT`
- `ANALYTICAL_INFERENCE`

Every row must contain an **inference ceiling**.

## Mandatory low-stakes speech oversampling

Because the novels and mature synthesis naturally overrepresent war, command, crisis, and institutional reasoning, the CMR evidence pass must deliberately oversample rare low-stakes conversational material when it exists. Priority contexts include:

- meals and mess-hall conversation;
- coffee and other voluntary drink choices;
- hospitality;
- waiting and transit;
- leave and rest;
- mild inconvenience;
- praise and compliments;
- joking and teasing;
- casual disagreement;
- social drinking where attested;
- physical comfort or discomfort;
- conversations in which no mission outcome must be solved.

The purpose is not to manufacture a domestic personality from thin evidence. It is to recover the speech baseline that crisis-heavy literary synthesis tends to compress.

Examples of forbidden inference jumps:

- one meal != favorite food;
- competence != enjoyment;
- military necessity != preference;
- accepting hospitality != habitual taste;
- participation != voluntary enthusiasm;
- crisis behavior != ordinary routine;
- officer role != private personality;
- repeated wartime habit != proven peacetime permanence.

---

# XII. Relationship-conditioned modeling

Relationships are directional state transformations, not unordered tags.

Model separately:

- Tanya -> Visha
- Visha -> Tanya
- Tanya -> Weiss
- Weiss -> Tanya
- Tanya -> Zettour
- Zettour -> Tanya
- Lergen -> Tanya
- Tanya -> Lergen

and so forth where evidence justifies it.

In addition to canonical person-to-person relationships, maintain a relationship-class model for situations where no shared institutional hierarchy exists. This is required for bounded crossover simulation and useful for ordinary encounters with foreign officers or political actors.

Minimum relationship classes should include where evidenced:

- legitimate superior;
- subordinate;
- institutional peer;
- familiar associate;
- civilian/service professional;
- stranger of ambiguous status;
- adversary;
- **no-shared-hierarchy professional peer** - a competent military or political actor whose authority is real in another system but not formally binding on the character.

The last class must not silently import one universe's chain of command into another. Status may still affect caution, deference, diplomatic politeness, or information control without creating formal obedience.

For each direction, record changes in:

- address;
- politeness;
- initiative;
- directness;
- disclosure;
- humor/teasing;
- willingness to interrupt;
- willingness to disagree;
- command behavior;
- trust;
- competence assumptions;
- tolerance of error;
- expected obligations;
- emotional openness;
- exceptional behaviors not generalized elsewhere.

A convincing multi-character simulation requires relationship-specific retrieval. Independently generating two generic character voices is insufficient.

---

# XIII. Scenario packet and simulation protocol

## 1. Minimum scenario packet

Before generating behavior or dialogue, resolve as much of the following as possible:

- date/volume era;
- character developmental state;
- rank and role;
- location;
- present interlocutors;
- relationship state;
- public/private setting;
- relevant known information;
- immediate objective;
- stake level;
- physical state;
- emotional state;
- institutional constraints;
- what the character is *not* allowed to know.

If a field is genuinely unspecified, preserve that ambiguity rather than silently choosing the most convenient state.

## 2. Retrieval before generation

Retrieve the closest canonical diagnostic scenes using weighted similarity.

Priority should generally be:

1. same relationship/interlocutor;
2. same role/power relation;
3. same stakes;
4. same situation class;
5. same emotional state;
6. same developmental era;
7. lexical/topic similarity.

Do not let superficial word overlap outrank a much closer behavioral analogue.

## 3. Generate in causal order

Correct order:

`scenario -> attention -> private appraisal -> communicative objective -> constraints -> likely decision/action -> speech act -> relationship/role filter -> register -> surface dialogue`

Incorrect order:

`scenario -> invent a character-sounding quip -> justify it afterward`

Speech is downstream of state and decision.

## 4. Output modes

### `STRICT_RECONSTRUCTION`
Stay inside strongly evidenced behavioral space. Explicitly surface uncertainty.

### `PLAUSIBLE_EXTRAPOLATION`
Permit a broader hypothesis while labeling where evidence weakens.

### `CREATIVE_CROSSOVER`
May prioritize narrative entertainment, but should still expose which parts are source-grounded and which are speculative when analytical fidelity matters.

Generated output never returns to the evidence corpus as a diagnostic scene.

---

# XIV. Validation and falsification

A reconstruction model must be tested against withheld canon.

## 1. Held-out continuation tests

Select canonical scenes not used in profile construction.

Provide the model with context up to the decision point, withholding what the character actually does next.

Ask it to predict:

- attention target;
- likely appraisal;
- likely action;
- likely speech act;
- likely register;
- confidence;
- rejected alternatives.

Then reveal and compare the canonical continuation.

## 2. Context-bucket validation

Tanya should be tested separately on:

- mundane/low-stakes scenes;
- superior-facing staff interaction;
- subordinate management;
- peer/professional interaction;
- disagreement within legitimate hierarchy;
- combat/tactical emergency;
- exhaustion/injury;
- praise/reward;
- material comfort/leave where available;
- Being-X encounters.

## 3. Perturbation tests

Keep the problem constant while changing one variable:

- Visha vs Weiss vs Zettour;
- private conversation vs staff meeting;
- low stakes vs lethal stakes;
- early-career vs later-career Tanya.

A good model should change appropriately.

## 4. Adversarial caricature tests

The Tanya model should resist prompts that try to convert her into:

- a bloodthirsty war lover;
- an emotionless optimizing robot;
- a reckless action hero;
- an openly insubordinate maverick;
- a patriotic zealot;
- a generic atheist ranter;
- a walking economics textbook who speaks private narration aloud;
- a sadistic commander whose personnel discipline lacks instrumental purpose.

Equivalent anti-caricature tests should be written for each promoted character.

## 5. Promotion gate

A profile may move from `active_provisional` to `canonical` only after:

- source locators validate;
- diagnostic diversity is adequate;
- relationship leakage is checked;
- low-stakes and high-stakes evidence are clearly separated;
- held-out tests are reviewed;
- adversarial caricature tests pass at an acceptable qualitative level;
- major contradictions/open areas are documented.

---

# XV. Artifact architecture

CMR is housed under:

`Youjo Senki/06 Character Modeling and Reconstruction/`

Subdirectories:

## `00 Frameworks and Methods`
Governing methodology and any later method revisions.

Canonical method filename:

`YOUJO_SENKI_CHARACTER_MODELING_REFERENCE_METHOD.md`

## `01 Evidence and Locators`
Primary-source-derived infrastructure:

- source extraction manifest;
- alias map;
- coverage/readiness audit;
- dialogue-and-behavior locator index;
- everyday-life/preferences/material-habits ledger;
- optional source-sensitive crosswalks.

Expected filenames include:

- `YOUJO_SENKI_CMR_SOURCE_EXTRACTION_MANIFEST.md`
- `YOUJO_SENKI_CHARACTER_RECONSTRUCTION_READINESS_AUDIT.md`
- `YOUJO_SENKI_CHARACTER_DIALOGUE_AND_BEHAVIOR_LOCATOR_INDEX.tsv`
- `YOUJO_SENKI_EVERYDAY_LIFE_PREFERENCES_AND_MATERIAL_HABITS_LEDGER.md`

## `02 Character Models`
One current model per character semantic responsibility.

Preferred naming:

- `YOUJO_SENKI_TANYA_DEGURECHAFF_CHARACTER_RECONSTRUCTION_MODEL.md`
- `YOUJO_SENKI_VIKTORIYA_SEREBRYAKOV_CHARACTER_RECONSTRUCTION_MODEL.md`
- `YOUJO_SENKI_ERICH_VON_LERGEN_CHARACTER_RECONSTRUCTION_MODEL.md`

Do not create profiles for failed-readiness characters merely to complete a roster.

## `03 Relationship Registers`
Directional relationship and register infrastructure.

Expected mature artifacts:

- `YOUJO_SENKI_CHARACTER_RELATIONSHIP_REGISTER_MATRIX.md`
- `YOUJO_SENKI_CHARACTER_SPEECH_ACT_AND_INTERACTION_MATRIX.md`

Character models with sufficient dialogue may also maintain a compact character-specific speech artifact when this improves retrieval without duplicating the integrated model. Preferred form:

- `YOUJO_SENKI_<CHARACTER>_SPEECH_REGISTER_AND_INTERACTION_MODEL.md`

Such an artifact is subordinate to the integrated character model and diagnostic source index. It exists to make high-frequency conversational reconstruction cheaper and more precise, not to create a parallel characterization authority.

## `04 QA and Simulation`
Held-out test packs, adversarial validation, contradiction audits, promotion decisions, and simulation protocol snapshots.

Expected mature artifacts:

- `YOUJO_SENKI_CMR_HELD_OUT_VALIDATION_LEDGER.md`
- `YOUJO_SENKI_CMR_QA_AND_PROMOTION_AUDIT.md`

No generated scene becomes evidence.

---

# XVI. Recommended implementation sequence

## CMR-0 - Source verification and extraction

- verify Volumes 01-14 identities against the supplied audit manifest;
- extract text-bearing EPUB members;
- generate deterministic paragraph locators;
- build alias table;
- record extraction irregularities without normalizing source content away.

## CMR-1 - Reconstruction-readiness audit

- measure dialogue/action/internal-access/context spread for candidate characters;
- assign `FULL_SPECTRUM`, `DOMAIN_BOUNDED`, `RECOGNITION_PROFILE`, or `INSUFFICIENT`;
- freeze the first modeling roster only after evidence review.

## CMR-2 - Tanya pilot evidence pack

Build Tanya's diagnostic index slice first, deliberately sampling:

- internal cognition;
- superior-facing speech;
- subordinate command;
- staff/intellectual work;
- combat;
- private/off-duty scenes;
- material preferences;
- fear/anger/exhaustion;
- Being-X encounters;
- observer misinterpretation;
- communicative-objective and withheld-content pairs;
- multiple speech acts including report, request, order, refusal, disagreement, praise, correction, reassurance, probing, bargaining, humor, and small talk;
- low-stakes meals, coffee/hospitality, waiting, travel, leave, and casual professional-social interaction where source evidence exists;
- no-shared-hierarchy professional-peer analogues where canonical foreign/peer interactions permit them.

## CMR-3 - Tanya reconstruction model

Integrate:

- stable baseline;
- developmental states;
- behavioral grammar;
- Japanese voice fingerprint;
- ordinary-life profile;
- relationship deltas;
- negative constraints;
- confidence ceilings;
- speech transformation rules from private appraisal to public utterance;
- speech-act exemplars and relationship-conditioned directness/disclosure;
- explicit character-specific speech hazard statement.

## CMR-4 - Tanya QA

Run held-out continuation, perturbation, and caricature tests before treating Tanya as a mature simulation surface.

## CMR-5 - Method transfer pilots

Recommended next characters:

1. Visha - tests strong dialogue/action with less internal access.
2. Lergen - tests internal judgment and observer interpretation.
3. Zettour - tests a high-quality domain-bounded model where ordinary private life may remain open.

If these succeed, extend to Weiss, Rudersdorf, Mary Sue, and any others that pass readiness audit.

## CMR-6 - Relationship matrix and cross-model QA

Once multiple profiles exist:

- build directional relationship states;
- run cross-character consistency tests;
- verify that profiles do not assign contradictory assumptions to the same canonical scene;
- document underdetermined relationships explicitly.

---

# XVII. Hard constraints

1. **Primary source beats profile.**
2. **Generated output never becomes evidence.**
3. **Internal narration is not generic dialogue.**
4. **Speech is downstream of communicative objective and relationship constraint.** A psychologically plausible thought must not be emitted verbatim unless the source supports that level of disclosure.
5. **No-shared-hierarchy encounters do not create fictional command authority.** Crossover or foreign-professional status may change caution and politeness, not formal obedience.
6. **Observer interpretation is not private motive.**
7. **Role performance is not automatically personality.**
8. **One scene does not establish a stable preference.**
9. **Competence does not prove enjoyment.**
10. **High-stakes behavior does not define low-stakes personality.**
11. **Low-stakes behavior does not automatically predict battlefield action.**
12. **Relationship-specific behavior does not globalize without evidence.**
13. **Later development does not retroactively overwrite earlier state.**
14. **Domain-bounded characters must remain domain-bounded.**
15. **No false precision.** Confidence labels are qualitative unless a later empirical validation design justifies a quantitative metric.
16. **No silent canon completion.** If the source does not tell us what a character privately enjoys, believes, or would do, preserve the gap.
17. **Do not flatten contradiction.** A model that cannot represent a character acting against a strong baseline under specific pressure is too rigid.

---

# XVIII. Success criterion

The project succeeds when a model can do more than produce recognizable catchphrases.

A high-quality CMR should be able to explain:

- why a character noticed one feature of a situation before another;
- why they chose a particular action despite competing values;
- why they said less, more, or something different than they privately thought;
- why their register changed with one interlocutor but not another;
- why a behavior is normal in one developmental state and wrong in another;
- why a tempting generated line is out of character even though its ideology sounds correct;
- and exactly which Japanese source scenes justify the reconstruction.

For Tanya, the most important fidelity test is preserving all three of these at once:

> **the frightened, self-preserving and institutionally calculating adult consciousness in her head; the extraordinarily competent officer visible in her actions; and the heroic, fanatical, monstrous, or providential figure other people construct from those actions.**

A simulator that preserves only one of those Tanyas is not yet Tanya.
