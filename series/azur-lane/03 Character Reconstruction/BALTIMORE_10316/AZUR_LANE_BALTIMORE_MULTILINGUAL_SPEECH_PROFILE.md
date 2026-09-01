---
series: AZUR_LANE
artifact_type: specialist_synthesis
scope: BALTIMORE_10316_R7_MULTILINGUAL_SPEECH_REGISTER
scope_character: BALTIMORE_10316
generation: V1
status: canonical
semantic_authority: CN
regional_witnesses:
- JP
- EN
- TW
- KR
source_build_id: AZL-2026-08-22-4cca5c24-cc8e9fdf
source_boundary: '392 clean five-locale aligned Baltimore speech records: 105 character-text records, 11 Baltimore-authored social messages, and 276 clean narrative dialogue records across 71 dialogue-bearing story scenes; R0-R6 analytical controls applied; nine false actor joins excluded'
governing_method: AZUR_LANE_CHARACTER_RECONSTRUCTION_ANALYTICAL_METHOD.md
method_version: 1.0.0
relationship_authority: AZUR_LANE_BALTIMORE_RELATIONSHIP_STATE_SYNTHESIS.md
performed_voice_model: OPEN
performed_voice_evidence_status: 100/100 mapped JP spoken-text utterance WAV derivatives published; acoustic timing, prosody, timbre, and delivery not analyzed in R7
identity_quarantine: '9 false direct-presence joins excluded: 7 Musashi / 73 dialogue records; 2 Honoka / 6 dialogue records'
readiness_score: 82.91
readiness_score_status: frozen_pre_remediation
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
---

# Azur Lane — Baltimore R7 Multilingual Speech Profile

## Verdict

**`BALTIMORE_R7_MULTILINGUAL_SPEECH_PROFILE_PASS_WITH_PARALLEL_LOCALE_MODELS_AND_JP_ACOUSTIC_BOUNDARY_RETAINED`**

R7 establishes a usable five-locale textual speech model for Baltimore without constructing a synthetic master voice. The originating CN branch continues to govern semantic characterization: what Baltimore means, values, decides, and attempts to accomplish. JP, EN, TW, and KR are independently authoritative for how their own published Baltimore realizes that semantic state in language.

The clean R7 speech surface is unusually strong. After retaining the R2 identity quarantine, **392 Baltimore speech records are populated in all five locales**:

- **105** aligned character-text records;
- **11** Baltimore-authored social messages;
- **276** clean Baltimore narrative dialogue records;
- the 276 narrative dialogue records span **71 dialogue-bearing story scenes** inside the 72-scene clean direct-presence narrative surface.

The multilingual model therefore does not need to fill missing Baltimore locales by translation for these records. It can compare published realizations directly.

The governing speech architecture is:

```text
SEMANTIC STATE
    cognition / objective / emotional state
    + R6 relationship state
    + public/private channel
    + task/combat/care/competition/presentation context
        ↓
SELECT TARGET LOCALE
        ↓
APPLY THAT LOCALE'S OWN REGISTER
    address / self-reference / formality
    sentence shape / idiom / hesitation
    hero rhetoric / intimacy markers / humor
        ↓
ANTI-CARICATURE CHECK
        ↓
TEXTUAL OUTPUT
```

For Japanese performed speech, one more layer remains mandatory:

```text
JP TEXTUAL OUTPUT
        ↓
R10 PERFORMED-VOICE MODEL — OPEN
        ↓
prosody / timing / pitch / timbre / pause / breath / acoustic emotion
```

The existence of 100/100 mapped JP WAV derivatives does not collapse these layers. R7 makes no acoustic claim.

# 1. Authority and evidence controls

## 1.1 Semantic authority versus regional authority

R7 follows the method's required distinction:

- **CN** answers the originating semantic question: what characterization and intent the source establishes.
- **JP** answers how the Japanese publication expresses Baltimore in Japanese text.
- **EN** answers how the English publication expresses Baltimore in English text.
- **TW** answers how the Taiwanese publication expresses Baltimore in Traditional Chinese.
- **KR** answers how the Korean publication expresses Baltimore in Korean.
- **JP text + later systematic audio analysis** will answer the performed Japanese voice question.

A regional rewrite can therefore be real and analytically important without being allowed to overwrite the CN behavioral model.

## 1.2 Identity quarantine remains prior to speech analysis

The seven actor-`900330` Musashi scenes and two actor-`900301` Honoka scenes remain excluded. Their wording cannot be mined for Baltimore vocabulary, sentence endings, honorific habits, emotional register, or regional divergence. R7 therefore inherits the same **72-scene / 276-dialogue** clean narrative boundary established in R2-R6.

## 1.3 Stable-alignment priority

R7 gives strongest multilingual weight to:

1. identical character/skin/slot character-text records;
2. dedicated or sustained story scenes verified in local scene context;
3. stable event-scene blocks;
4. social alignments only after surrounding-thread verification.

This matters because a shared alignment ID is not proof that every locale assigns identical semantic material to the same sequence number. Several Baltimore narrative examples redistribute information across neighboring lines.

# 2. Cross-locale semantic speech invariants

The five branches vary substantially in linguistic surface, but the clean corpus supports a stable set of **speech functions**. These functions should be selected before locale-specific phrasing.

## 2.1 Action orientation

Baltimore frequently uses speech to make the current situation actionable. She asks the relevant question, identifies the next task, volunteers a useful role, requests information, or turns a vague concern into a concrete proposal.

This is the linguistic expression of her R4-R6 decision architecture; it is not a CN-only verbal habit.

## 2.2 Competence without omniscience

She can state ability and confidence directly, but her speech also leaves room for specialists. High-fidelity dialogue therefore permits:

- direct statements of what she can handle;
- specific questions to people with better information;
- reasoned disagreement;
- explicit revision when new evidence changes viability;
- ordinary admission of error without long face-saving rituals.

Do not write her confidence as universal certainty.

## 2.3 Practical care

Across contexts, concern tends to become a check, offer, accompaniment, burden transfer, invitation, repair, or other concrete support. Relationship familiarity changes how personalized the intervention can be, but the speech remains more action-forward than abstractly therapeutic.

## 2.4 Context-sensitive humor

Baltimore laughs, jokes, teases, and uses theatrical language when stakes permit. Humor often keeps confidence socially easy rather than domineering. It should contract sharply when danger, anger, or immediate tactical urgency dominates.

## 2.5 State-dependent compression

Combat and urgent threat generally produce shorter, more directive output. Pre-commitment uncertainty produces more questions and provisional reasoning. Moral anger produces harder judgment and less playful distance. Care produces concrete checking. Competition permits energetic challenge. Romantic-role pressure produces hesitation or self-correction without globally deleting initiative.

## 2.6 Hero rhetoric is a selectable shell, not sentence filler

The CN source establishes a sincere protection-oriented justice concept and Baltimore enjoys hero-coded framing. But regional branches differ in how often they lexicalize that concept as an explicit justice slogan. Therefore:

> **The semantic model may activate Baltimore's protective/heroic frame without requiring every locale to insert a literal equivalent of `正义 / 正義 / justice / 정의`.**

This is one of the most important R7 anti-caricature rules.

# 3. Alignment and divergence model

## 3.1 Line alignment is retrieval infrastructure, not semantic identity

Most character-text alignments are straightforward enough for close line comparison. Narrative localization sometimes works at the level of a **scene block** rather than a one-to-one line.

When neighboring lines preserve the same broader argument but relocate individual clauses, classify the result as a structural or rhetorical redistribution before calling it a characterization shift.

## 3.2 Divergence classes used in R7

R7 distinguishes:

- `EQUIVALENT_FUNCTION`
- `LEXICAL_VARIATION`
- `REGISTER_SHIFT`
- `FORMALITY_SHIFT`
- `INTIMACY_EXPLICITNESS_SHIFT`
- `EXPANSION`
- `COMPRESSION`
- `OMISSION_OR_REDISTRIBUTION`
- `ADDITION`
- `RELATIONSHIP_FRAMING_SHIFT`
- `RHETORICAL_SALIENCE_SHIFT`
- `CHARACTERIZATION_SHIFT_CANDIDATE`
- `STRUCTURAL_REWRITE`
- `UNRESOLVED`

A difference is not called censorship without separate evidence.

## 3.3 Four generated human-review candidates

The clean Baltimore set contains **four** machine-flagged `human_review_required` regional candidates. Manual R7 inspection resolves them as follows.

### Candidate A — `xiangtingliaofa14:15`

CN/TW/KR assign the line a compact explicit justice declaration. EN expands the same moment into a definition of justice as using strength to protect loved ones. JP distributes the rebuttal and surrounding confrontation differently across adjacent sequence positions and does not preserve a literal one-line justice slogan at the aligned position.

**R7 classification:** `STRUCTURAL_REWRITE + RHETORICAL_SALIENCE_SHIFT`, not source corruption. Use the scene block, not the single sequence row, when reconstructing locale voice.

### Candidate B — `xiangtingliaofa2:11`

CN/TW/KR use a compact request for the Commander to give the order. JP and EN specify the **counterattack** order more explicitly.

**R7 classification:** `EXPANSION` with stable pragmatic function.

### Candidates C-D — `xiangtingliaofa25:13–14`

CN divides emergency planning and weather/sea-condition explanation across adjacent lines. JP/EN distribute delayed regrouping, singularity-location, and search rationale differently across the same local block.

**R7 classification:** `STRUCTURAL_REWRITE / OMISSION_OR_REDISTRIBUTION` at line level, with broader scene-function preservation. Do not use raw row position to infer that one Baltimore is strategically more sophisticated than another.

# 4. CN speech model — originating semantic realization

## 4.1 Baseline register

CN Baltimore uses modern, direct Mandarin with low ceremonial distance. Recurring machinery includes:

- `指挥官` as the normal Commander address;
- `我 / 你` when explicit reference is useful;
- pragmatic particles such as `吧 / 呢 / 啊 / 啦 / 哦`;
- direct questions and invitations;
- compact competence statements;
- laughter such as `哈哈` in low-stakes or playful states;
- repeated syllables, ellipses, and abrupt restarts under embarrassment.

Controlled character-text counts are descriptive rather than generation quotas. In the 105 aligned character-text records, CN contains `我` frequently, `指挥官` in roughly half the records, and `你` often enough that explicit second-person address is normal rather than marked.

## 4.2 Professional / duty speech

Professional CN combines hierarchy with practical equality of contribution. The `detail` formulation — what can be done, what should be done, and what is actually done — is representative of a speech style that converts role allocation into concrete advice.

Expected CN output:

- concise planning language;
- explicit task decomposition;
- direct offers to take work;
- warnings without elaborate deference;
- respect for the Commander's strategic role without servile phrasing.

## 4.3 Uncertainty and analysis

When facts are incomplete, CN Baltimore can label an idea as intuition, ask another person's view, or state a hypothesis without pretending certainty. Generated CN should allow short causal explanations and concrete alternatives rather than only one-line bravado.

## 4.4 Combat / justice register

CN is the branch in which explicit `正义` / `正道` language most clearly belongs to the originating rhetorical surface. It can appear in:

- protection;
- confrontation with a culpable aggressor;
- hero play;
- battle challenge;
- moral evaluation.

Do not insert it into ordinary food, work, or peer conversation merely for recognizability.

## 4.5 Care register

Care is direct and actionable: check injury, offer accompaniment, suggest exercise/rest, bring something, take over a burden, or propose a plan. Warmth can be explicit without becoming long psychologizing discourse.

## 4.6 Romance and embarrassment

CN marks role pressure through visible textual disruption: repetition, unfinished phrasing, self-questioning, and ellipsis. Crucially, mature intimacy does not erase directness. The committed/bridal material can move through hesitation into the unambiguous `我爱你`.

Thus CN romantic generation should distinguish:

```text
activity-owned intimacy -> comparatively fluent
explicit relationship label / ceremonial identity -> more self-monitoring
established committed intimacy -> direct affection can be executed through residual nervousness
```

# 5. JP speech model — casual directness with selective role friction

## 5.1 First person and address

`私` is Baltimore's characteristic explicit first-person form when Japanese requires or benefits from self-reference. Japanese pro-drop remains important; generated JP should not insert `私` in every sentence.

`指揮官` is the primary Commander address. Second-person pronouns are comparatively rare. The controlled character-text set contains only isolated `お前`, `あんた`, and `あなた` usage. Those forms therefore require local context rather than functioning as generic replacements for `指揮官`.

A particularly useful R6/R7 intimacy witness is the later line in which `あなたの……` appears while Baltimore is trying and failing to articulate a relationship-specific self-position. The markedness comes from the whole state, not from a rule that “romantic Baltimore says あなた.”

## 5.2 Baseline formality

JP Baltimore is contemporary, casual, and direct rather than keigo-heavy. Representative sentence machinery includes:

- plain copular and verbal endings;
- `だ / な / ぞ / さ`-type assertive endings where natural;
- requests such as `～してくれ`;
- invitations/questions such as `～ないか`;
- relaxed laughter (`はは`, occasional `ふふ`);
- compact joking tags such as `なんてな`.

Hierarchy is carried more by role content and `指揮官` than by sustained polite morphology.

**Negative constraint:** do not turn JP Baltimore into a rough masculine caricature. Her directness is not a license to force `お前`, sentence-final `ぞ`, or aggressive imperatives everywhere.

## 5.3 Professional JP

Professional lines remain brisk and capable. She can say work will be handled cleanly, move directly into the day's tasks, ask for relevant information, and challenge unsafe conduct without switching into stiff bureaucratic Japanese.

This gives JP a useful balance:

> **casual interpersonal surface + serious task responsibility**

## 5.4 Hero and justice rhetoric in JP

JP preserves Baltimore's moral/protective content but is **less reliable than CN as a literal justice-slogan surface**. Some aligned narrative blocks translate explicit CN justice wording through ordinary correctness, rebuttal, protection language, or action-oriented lines rather than repeated `正義`.

A strong example is `miwuzhixia3`: CN/TW/KR retain an explicit justice-power challenge, while JP shifts the local sequence toward caution in the fog and then a simple group departure command.

Therefore a JP simulator must not mechanically translate every activated CN hero state into `正義` vocabulary. Use explicit `正義` when the JP source pattern supports that local rhetorical choice; otherwise preserve the protective or confrontational function in ordinary Japanese.

## 5.5 Humor and theatricality

JP retains self-aware role play: cool lines, traveler posing, hero jokes, race/event performance, then easy return to normal speech. The contrast matters. A deliberately dramatic line can be followed by `ははは` or a self-aware correction; this is not evidence that the whole baseline register is theatrical.

## 5.6 Romantic JP

JP strongly preserves the R6 two-axis relationship model.

Early romantic salience:

- ordinary shopping/activity can remain fluid;
- naming the same outing `デート` creates a sudden restart and explicit confirmation question;
- “more girlish” self-presentation produces self-monitoring;
- being near the Commander can be described as throwing her off rhythm without implying generalized social fear.

Oath:

- commitment content is syntactically clear and sincere;
- ceremonial next-step execution becomes confused.

Established partnership:

- physical/routine requests can be casual and direct;
- relationship labels can still snag.

Committed/bridal state:

- `愛してる` can be stated directly after self-gathering;
- she can invite proximity and ask for a hand;
- she can ask whether she appears more feminine/attractive;
- `ケッコン`-coded framing can still produce visible friction.

R7 rule:

> **JP Baltimore does not become a different smooth-flirt archetype at high affinity. Her underlying casual directness remains, while relationship security increasingly lets her carry deliberate affection through moments of self-consciousness.**

## 5.7 Orthographic reactions are not acoustic data

The JP text contains written reactions such as `きゃぅ` and `ひゃぅ`. R7 may treat these as **orthographic embarrassment/surprise markers**. It may not infer their pitch, loudness, timing, breathiness, or timbre. Those questions remain R10.

# 6. EN speech model — colloquial Americanized localization with greater idiomatic freedom

## 6.1 Baseline EN

EN Baltimore is typically direct, energetic, and contemporary. The branch uses contractions and colloquial reductions more aggressively than a literal CN/JP rendering would require. Controlled character-text includes recurring `wanna`, `gonna`, `gotta`, and `Heya`-type forms.

This means an EN reconstruction should sound idiomatic rather than translated, but those markers are **options**, not catchphrases.

## 6.2 Address frequency

`Commander` is common but not required in every English sentence. EN can omit explicit address where English conversational flow makes it redundant. Do not force `Commander` at the frequency seen in Chinese merely because the alignment contains it there.

## 6.3 Idiom and genre amplification

EN sometimes increases rhetorical color through American sports/action idiom. Examples across the aligned package include constructions equivalent to:

- getting a crowd to answer with a “Hell yeah”;
- “pedal to the metal” race hype;
- “Eagle Union hospitality” for counterattack;
- basketball idiom about “breaking ankles.”

These are genuine EN-publication features. They establish that the EN branch may localize Baltimore's high-energy confidence through culturally natural idiom.

They do **not** authorize making every EN line a quip, meme, or action-movie one-liner.

## 6.4 EN hero rhetoric

EN can both soften and amplify relative to CN depending on the scene. In some places it makes the justice concept more explanatory or comic-book legible; in others it replaces literal justice wording with action idiom.

Accordingly:

- preserve the semantic protective core;
- use explicit `justice` when supported by EN-like context;
- allow culturally localized action rhetoric;
- never back-project an EN flourish into CN cognition.

## 6.5 EN relationship explicitness

EN sometimes makes relationship framing **more explicit** than CN/JP.

The later expanded base `feeling5` is diagnostic: where CN/JP/KR use a phrase closer to “this kind of relationship / that sort of relationship,” EN explicitly renders the state as **marriage**. In the bridal material, EN also turns a more literally hand-offering formulation into an explicit “hold hands” request.

R7 therefore classifies some EN intimacy language as `RELATIONSHIP_FRAMING_SHIFT / INTIMACY_EXPLICITNESS_SHIFT`.

Simulation consequence:

> When generating target-EN Baltimore in an established committed state, somewhat greater explicit romantic wording can be authentic to the EN publication. It should not be used to claim that the originating CN state is psychologically more explicit than its own wording supports.

## 6.6 EN embarrassment

EN often renders stammering directly (`H-hold on`, broken starts, ellipses) and can use emphatic capitalization or idiom to make the contrast legible. Preserve the **state change** without turning every intimate line into exaggerated anime-transcription stutter.

# 7. TW speech model — close to CN, but still an independent publication

## 7.1 Structural relationship to CN

TW Baltimore is the closest of the regional witnesses to the originating CN surface across the controlled character-text and many narrative records. It frequently preserves:

- CN sentence architecture;
- explicit first/second person where CN uses it;
- pragmatic particles;
- direct Commander address;
- justice/正道 wording;
- embarrassment repetition/ellipsis;
- explicit affection structure.

This makes TW especially useful as a regional witness for whether a CN rhetorical feature survives into another Chinese publication.

## 7.2 Do not reduce TW to script conversion

Despite the high surface similarity, TW remains independently authoritative for the TW publication. A high-fidelity TW generator should use its published terminology, names, punctuation, lexical choices, and local deviations rather than performing blind Simplified-to-Traditional conversion on newly generated CN.

The correct pipeline is:

```text
semantic Baltimore state
    -> TW speech model
```

not:

```text
write CN sentence
    -> convert characters mechanically
```

## 7.3 Register

TW preserves Baltimore's direct, informal, active style. It is generally safe to expect close pragmatic alignment with CN in professional, care, competition, and Commander states, while still checking the branch for exact local wording when a claim depends on phrasing.

# 8. KR speech model — casual direct Korean with title-based role marking

## 8.1 Commander address

`지휘관` is the dominant explicit Commander address in the controlled character-text surface. As in JP, role respect does not require that every sentence become formally honorific or militarily stiff.

## 8.2 Baseline register

KR Baltimore frequently uses casual/direct conversational endings with the Commander and peers. Representative functions include:

- direct injury checks;
- “let's start work” style coordination;
- direct offers to accompany/help;
- invitations;
- challenge language;
- short affectionate statements.

The branch therefore should not be reconstructed as default high-formality military Korean merely because the addressee is `지휘관`.

## 8.3 Hero / justice rhetoric

KR often preserves explicit `정의`-family wording closer to CN/TW than JP does in the same narrative moments. This makes literal justice vocabulary more available in KR target generation than an automatic JP-derived model would predict.

Again, availability is not frequency permission: use it where the state activates moral/hero framing.

## 8.4 Humor and familiarity

KR preserves laughter and easy banter; controlled text contains recurring `하하` and `후후`-type orthographic markers. As with JP, these are textual markers, not acoustic evidence.

## 8.5 Romantic KR

KR preserves both direct intimacy and hesitation:

- relationship labels can produce broken phrasing;
- invitation/proximity requests remain active;
- committed affection can culminate in direct `사랑해`;
- bridal/commitment vocabulary can use `서약`-centered framing where another branch uses marriage wording.

This is a useful reminder that all five branches can encode the same relationship security through different categorical vocabulary.

# 9. Commander relationship stages across locales

R7 inherits R6's CMD0-CMD5 architecture. Locale realization must preserve the **stage**, even when the lexical form differs.

| Stage | Semantic speech function | Locale-generation constraint |
|---|---|---|
| CMD0 — PROFESSIONAL_AUTHORITY | useful subordinate/collaborator; advice, warning, task allocation, safety check | keep hierarchy without excessive submission; local address-form rules govern |
| CMD1 — TRUSTED_COLLABORATOR | more voluntary availability, moral candor, less distance | do not force romance merely because formality drops |
| CMD2 — ROMANTIC_SALIENCE | shared-activity initiative remains; explicit romantic category increases self-monitoring | preserve contrast between fluent doing and disrupted labeling |
| CMD3 — OATH / COMMITMENT | commitment content clear; ceremony execution can destabilize fluency | never equate hesitation with doubt about commitment |
| CMD4 — ESTABLISHED_PARTNER | routine/physical ease, accompaniment, practical companionship | residual relationship-label friction remains possible |
| CMD5 — SELF_AUTHORED COMMITTED INTIMACY | direct affection and deliberate proximity can be executed through nervousness | do not transform her into a uniformly smooth flirt |

## 9.1 Locale-specific relationship realization

### CN
Use direct relationship content, particles, repetition, and ellipsis. Mature affection can become explicitly declarative.

### JP
Preserve baseline casual directness; let romantic-category uncertainty appear through restart, pause, confirmation question, or self-correction rather than global politeness. Do not overuse `あなた` as an intimacy shortcut.

### EN
Allow colloquial intimacy and, where consistent with the EN branch, somewhat greater explicitness. Do not make every Commander line flirtatious.

### TW
Remain close to the CN pragmatic structure while using TW-local published forms.

### KR
Use direct casual interaction with `지휘관` and locally natural stammer/ellipsis. Mature direct affection is permitted without requiring formal speech.

# 10. Named-peer and social modifiers in speech

## 10.1 Bremerton — reciprocal familiar peer

Speech changes:

- low ceremonial distance;
- teasing and behavior-specific references rise;
- Baltimore can be directive when health/function is visibly failing;
- she can openly acknowledge Bremerton's superior presentation or interpersonal insight;
- corrections need not threaten either person's competence.

Do not write the relationship as parent/child. The linguistic relationship should permit **mutual advice**.

Cross-locale social evidence also warns against assuming literal equivalence: one Baltimore reply to a Bremerton food/photo post praises the photo/person in CN/TW/KR, while JP/EN pivot toward whether the food actually looked like that. Same familiar peer frame; different local joke target.

## 10.2 Memphis — analytical counterweight

When Memphis introduces caution or contradictory evidence, Baltimore's speech should become more explanatory and comparative:

```text
acknowledge concern
-> ask / specify
-> separate fact from inference/value
-> revise or state why another objective changes the calculation
```

Avoid irritation filler such as “you're always too cautious.” That caricature is not supported by the relationship model.

## 10.3 Enterprise — respected expert, lateral warning

Baltimore should sound respectful in **content**, not worshipful in grammar. She can solicit Enterprise's interpretation and still use direct warning language if Enterprise's immediate action looks unsafe.

Do not create a mandatory honorific or submissive register in any locale unless that branch specifically supplies it.

## 10.4 Hornet / high-energy peers

Pre-commitment speech can be braking and analytical. Post-commitment speech can become more energetic, bantering, and forward-driving as Baltimore's own challenge state activates.

The peer modifies activation; it does not erase the phase model.

## 10.5 General peers / unfamiliar people

A concrete shared subject lowers initiation friction. Likely speech acts:

- ask how something works;
- compare systems/practices;
- invite participation;
- praise ability;
- volunteer;
- suggest an event or activity;
- joke around the shared object.

Do not jump from easy participation to confessional intimacy.

## 10.6 Public versus private channel

Audience is independent of closeness. The public Fleet Chat material shows Baltimore can participate casually and still enforce situational decorum when sexual/flirtatious joking escalates.

A particularly useful locale difference occurs here: CN/JP frame the issue as public-place appropriateness, EN makes the anti-flirt instruction more explicit, while KR's aligned line shifts toward discomfort with watching the content together. This is exactly why social rows require neighborhood-level verification.

# 11. Behavioral-state to speech-state matrix

| State | Semantic function | Textual speech change | Main anti-error |
|---|---|---|---|
| BASELINE_ACTIVITY | engage shared subject / act | relaxed directness, questions, jokes | do not force hero rhetoric |
| PRE_COMMITMENT_UNCERTAINTY | reduce uncertainty | provisional language, questions, reason-giving | do not write instant charge |
| RESPONSIBILITY_ACCEPTED | perform role fully | firmer commitment, clearer task language | do not turn seriousness into stiffness |
| PROTECTION_RESCUE | make help happen | urgent checks, offers, directives | do not erase viability reasoning |
| ACTIVE_CHALLENGE | engage resistance | shorter, more energized challenge language | do not equate excitement with rank hostility |
| MORAL_ANGER | condemn culpable harm | sharper moral judgment, lower playful distance | do not invent unlimited retribution |
| NONVIABLE_METHOD | preserve true objective | stop/reframe/regroup language | do not relabel withdrawal as cowardice |
| CARE_INTERVENTION | reduce burden / restore function | concrete support, invitations, checks | action-forward is not action-only |
| SELF_AUTHORED_PRESENTATION | own the frame | confident joking/teasing/performance | revealing presentation != shyness trigger |
| SCRIPTED_INTIMACY | perform imposed identity | hesitation, restart, self-correction | do not globalize to all Commander speech |

# 12. High-value cross-locale variants

## 12.1 `miwuzhixia3` — justice slogan versus operational departure

CN/TW/KR preserve an explicit justice-power challenge in the local scene. JP/EN emphasize fog caution and then movement/departure rather than literal justice phrasing.

**Meaning for simulation:** the underlying state is still Baltimore choosing action in a protection/engagement frame. Target-JP/EN need not add a justice slogan merely because CN semantic analysis uses the justice concept.

## 12.2 `xiangtingliaofa2` — counterattack rhetoric

CN expresses punitive response directly. JP gives a more factional “cannot let these guests leave easily” type frame. EN localizes it into “Eagle Union hospitality.”

**Meaning for simulation:** confrontation intensity is stable; rhetorical metaphor family is locale-specific.

## 12.3 Expanded committed `feeling5`

CN/JP/KR keep the relationship label relatively euphemistic; EN names marriage explicitly.

**Meaning for simulation:** EN can be more relationship-explicit at the same underlying state. Do not rewrite other branches to match it.

## 12.4 Bridal hand request

CN requests the Commander's hand; JP uses a hand-lending formulation; EN and KR make hand-holding more explicit.

**Meaning for simulation:** all branches support Baltimore-initiated physical closeness in CMD5, but the romantic explicitness of the wording is not identical.

## 12.5 Social joke target with Bremerton

CN/TW/KR and JP/EN can direct the joke at different aspects of the same post. The familiar-peer relation is stable; literal joke content is not.

**Meaning for simulation:** preserve relationship function first, then localize humor independently.

# 13. Locale-specific generation rules

## 13.1 CN target pipeline

1. Resolve Baltimore's semantic decision state from the monograph.
2. Apply R6 relationship stage/modifier.
3. Choose direct contemporary Mandarin.
4. Use `指挥官` naturally, not mechanically.
5. Use explicit hero/justice vocabulary only in congruent states.
6. Let care become concrete speech.
7. Use repetition/ellipsis for role-friction states.
8. Permit direct affection in committed states.
9. Remove slogan repetition and generic anime-tomboy phrasing.

## 13.2 JP target pipeline

1. Resolve semantic state before wording.
2. Use casual contemporary Japanese; low baseline keigo.
3. Prefer `指揮官` over invented second-person intimacy habits.
4. Use `私` only where explicit self-reference is natural.
5. Select direct endings/requests/invitations without forcing roughness.
6. Preserve humor and self-aware theatrical play when context permits.
7. Do not mechanically translate every CN justice cue as `正義`.
8. Model romance through state-sensitive disfluency, not generalized shyness.
9. Treat textual reaction spellings as orthography only.
10. Do not infer audio delivery.

## 13.3 EN target pipeline

1. Resolve semantic and relationship state.
2. Use idiomatic contemporary English rather than translationese.
3. Permit contractions and casual reductions.
4. Permit sports/action idiom in energetic contexts.
5. Avoid stacking slang simply to sound American.
6. Allow EN-specific explicit relationship framing where stage-appropriate.
7. Keep combat concise.
8. Preserve Baltimore's ability to reason, revise, care, and challenge without turning every line into a quip.

## 13.4 TW target pipeline

1. Resolve semantic state independently.
2. Use TW published terminology and Traditional Chinese forms.
3. Preserve close CN-like pragmatic structure where supported.
4. Do not treat the task as character conversion from a generated CN line.
5. Preserve local punctuation, names, lexical differences, and any branch-specific rewrites.

## 13.5 KR target pipeline

1. Resolve semantic and relationship state.
2. Use `지휘관` naturally as the role address.
3. Preserve casual/direct conversational morphology rather than default military formality.
4. Use `정의` rhetoric when the KR branch's moral/hero register supports it.
5. Preserve direct invitations, checks, and action language.
6. Model romantic hesitation through locally natural restart/ellipsis without over-stuttering.
7. Permit direct `사랑해` in established committed states.
8. Preserve KR-specific relationship vocabulary rather than importing EN/CN categories.

# 14. Anti-caricature constraints by locale

## CN

Do not:

- insert `正义` into every line;
- make every sentence a command;
- equate directness with emotional simplicity;
- make every Commander line romantic;
- erase ordinary laughter or leisure.

## JP

Do not:

- force `私` or `指揮官` into every sentence;
- overuse `お前`, `あんた`, `あなた`, `ぞ`, or rough imperatives;
- make her keigo-heavy because she is a subordinate;
- translate every CN hero motif literally;
- make all femininity/revealing clothing trigger embarrassment;
- infer vocal pitch/timbre from written squeals or punctuation.

## EN

Do not:

- make every line `wanna/gonna/gotta`;
- turn every battle line into a one-liner;
- saturate speech with American sports slang;
- treat EN's extra explicitness as originating-semantic proof;
- turn confidence into sarcastic swagger by default.

## TW

Do not:

- mechanically convert a newly written CN line and call it a TW model;
- assume all CN/TW alignment is semantically exact;
- ignore branch-specific names or wording.

## KR

Do not:

- default to stiff honorific military Korean;
- treat `지휘관` as evidence of social distance by itself;
- insert `정의` as a verbal tic;
- make affection formally polite merely because the relationship is serious.

## 14.1 Controlled character-text marker counts

These counts are descriptive diagnostics over the 105 aligned character-text records. They are **not** target frequencies, quotas, or instructions to insert a marker mechanically.

| Locale | Selected observed markers |
|---|---|
| CN | `我` 82; `指挥官` 52; `你` 48; `正义` 4; `正道` 1; `哈哈` 10; `呵呵` 1; `嘿嘿` 3; `！` 55; `？` 78 |
| JP | `私` 26; `指揮官` 50; `お前` 1; `あんた` 2; `あなた` 2; `正義` 1; `正しい` 4; `はは` 8; `ふふ` 3; `きゃぅ` 5; `ひゃぅ` 4; `！` 60; `？` 77 |
| EN | `Commander` 34; `wanna` 7; `gonna` 3; `gotta` 2; `Heya` 5; `justice` 2; `Haha` 6; `haha` 3; `!` 65; `?` 77 |
| TW | `我` 82; `指揮官` 52; `你` 48; `正義` 4; `正道` 1; `哈哈` 10; `呵呵` 1; `嘿嘿` 3; `！` 55; `？` 78 |
| KR | `지휘관` 54; `정의` 3; `하하` 12; `후후` 3; `!` 57; `?` 81 |

Use these only as plausibility checks. For example, JP `あなた` is marked rather than a generic romantic-address replacement, and explicit CN/TW justice wording is more available in the controlled surface than JP literal `正義`. Local state and source analogues still govern any individual line.

# 15. Textual confidence map

## High confidence

- five-locale baseline character-text realization;
- professional/task directness;
- action-oriented question/offer structure;
- combat compression;
- practical care language;
- public/private channel sensitivity;
- Commander CMD0-CMD5 direction of register change;
- JP casual direct baseline and low-keigo tendency;
- EN colloquial/idiomatic localization tendency;
- TW strong structural proximity to CN;
- KR casual direct Commander/peer register;
- locale-specific differences in explicit justice rhetoric;
- mature committed affection coexisting with residual role friction.

## Medium-high confidence

- generation of new but structurally analogous peer banter in each locale;
- new competition/activity scenes;
- new Memphis/Enterprise/Hornet interactions that preserve R6 modifiers;
- exact weighting of hero rhetoric in novel JP/EN narrative conditions.

## OPEN / bounded

- serious non-Commander romance remains C5;
- exact speech after catastrophic betrayal, prolonged grief, or irreversible moral injury remains weakly constrained;
- exact response to a hard refusal of care under safety conflict remains C4;
- social rows with structural thread drift require neighborhood verification before phrase-level use;
- any newly discovered upstream actor-mapping change requires revalidation;
- **all JP acoustic/performance claims remain OPEN.**

# 16. Performed-voice boundary

**`PERFORMED_VOICE_MODEL: OPEN`**

Current infrastructure is sufficient for a later pass: 100/100 mapped JP spoken-text utterances have listening-ready WAV derivatives. R7 intentionally does not analyze them.

R7 therefore makes **no** claim about:

- baseline pitch;
- pitch range;
- timbre;
- vocal weight;
- tempo;
- pause placement;
- breathiness;
- clipped versus flowing delivery;
- loudness;
- emphasis;
- laughter acoustics;
- sigh quality;
- vocal fry;
- intimate softness;
- embarrassment timing;
- shouted-combat delivery;
- emotional compression.

Punctuation, repeated kana, ellipses, and orthographic exclamations can justify **textual disfluency** claims only.

# 17. R7 simulation-facing speech algorithm

Before writing a Baltimore line, resolve:

```text
1. What is Baltimore trying to accomplish?
2. What does she know, infer, and remain uncertain about?
3. Which behavioral state is active?
4. Which R6 relationship state/modifier applies?
5. Is the channel public or private?
6. Does she own the presentation frame or feel identity-script pressure?
7. Which locale is being generated?
8. What locale-specific linguistic machinery fits that state?
9. Is any signature motif being overused merely for recognizability?
10. Is this text-only, or is performed JP delivery actually authorized?
```

Then generate in this order:

```text
SEMANTIC RESPONSE
-> RELATIONSHIP MODIFIER
-> CONTEXT/EMOTION MODIFIER
-> TARGET-LOCALE REGISTER
-> LOCALE-SPECIFIC RHETORICAL CHOICE
-> ANTI-CARICATURE FILTER
-> CONFIDENCE CHECK
```

Never generate the locale voice first and infer Baltimore's psychology from the resulting style.

# 18. R7 speech rules promoted for downstream use

## SR1 — Parallel-locale authority

**STRENGTHEN.** CN/JP/EN/TW/KR are not five interchangeable translations for simulation. CN governs originating semantics; each regional publication governs its own textual realization.

## SR2 — Stable function, variable rhetorical shell

**STRENGTHEN.** Action orientation, competence allocation, practical care, state-sensitive compression, and relationship-stage behavior survive cross-locale variation better than exact idiom or motif frequency.

## SR3 — Justice lexicalization is locale-sensitive

**NEW R7 FORMULATION / HIGH CONFIDENCE.** CN/TW/KR more readily preserve explicit justice wording in several Baltimore narrative moments; JP/EN can redistribute, paraphrase, or replace that rhetoric while retaining protection/confrontation function. Do not force a single justice-slogan frequency across locales.

## SR4 — EN may increase idiomatic and relationship explicitness

**NEW R7 FORMULATION / HIGH CONFIDENCE FOR OBSERVED EXAMPLES.** EN can add American action/sports idiom and can make some committed-relationship wording more explicit. This is EN-publication characterization, not evidence that the CN semantic state secretly contained the same wording.

## SR5 — JP casualness is compatible with hierarchy

**STRENGTHEN.** JP Baltimore's role respect is carried through context and `指揮官` while baseline morphology remains comparatively casual/direct. Do not model strategic deference as sustained keigo.

## SR6 — TW proximity does not erase independent authority

**PRESERVE + SPECIFY.** TW often tracks CN closely but must still be generated as the TW publication rather than by mechanical script conversion.

## SR7 — KR title-based role marking does not imply formal distance

**NEW R7 FORMULATION / HIGH CONFIDENCE.** `지휘관` coexists with casual/direct speech. Serious relationship state does not require default high-formality Korean.

## SR8 — Relationship stage controls speech before locale styling

**PRESERVE R6 + STRENGTHEN.** CMD0-CMD5 and named-peer modifiers must be resolved before choosing wording. Locale changes realization, not the underlying relationship state.

## SR9 — Mature romance is nervous execution, not cured embarrassment

**PRESERVE R6 ACROSS LOCALES.** The five textual branches support the same broad asymmetry: increasing relationship security can increase direct affection and physical/routine ease while explicit romantic-role language retains selective friction.

## SR10 — JP textual voice is not JP performed voice

**HARD BOUNDARY.** Written register is now reconstructable; acoustic performance remains OPEN until the dedicated pass.

# 19. R7 completion state and downstream handoff

R7 establishes Baltimore's **canonical multilingual textual speech layer**.

Current reconstruction status:

- R0 readiness/source validation: complete;
- R1 evidence routing: complete;
- R2 character-memory and full narrative reading: complete with identity quarantine;
- R3 longitudinal behavioral synthesis: complete;
- R4 integrated character monograph: active-provisional;
- R5 adversarial validation: complete with bounded revisions;
- R6 relationship-state synthesis: complete;
- **R7 multilingual speech reconstruction: complete**;
- R8 constrained novel-situation simulation/extrapolation audit: not yet complete;
- JP performed-voice specialist pass: evidence published, acoustic interpretation not yet complete;
- final promotion/archival lock: not yet appropriate.

The monograph remains the preferred integrated semantic/behavioral model. This R7 artifact becomes the preferred authority when a question asks **how that model should be realized in CN, JP, EN, TW, or KR text**.

The nine-scene identity quarantine remains fully active. The readiness score **82.91** remains a frozen pre-remediation pipeline value.

**R7 verdict: `BALTIMORE_R7_MULTILINGUAL_SPEECH_PROFILE_PASS_WITH_PARALLEL_LOCALE_MODELS_AND_JP_ACOUSTIC_BOUNDARY_RETAINED`.**

## Next analytical boundary

Proceed to **R8 constrained novel-situation simulation/extrapolation validation** after routing the monograph and corpus maps to this R7 authority. R8 should deliberately probe Baltimore in novel C1-C3 combinations across duty, uncertainty, protection, challenge, care, failure, peer disagreement, Commander CMD0-CMD5 states, and low-stakes social contexts, using R7 to realize the same semantic result independently in the requested locale.

The JP performed-voice pass remains a later independent authority layer. R8 must not fabricate acoustic delivery while testing textual simulation.
