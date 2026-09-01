---
series: HIBIKE
artifact_type: revision_method
scope: V1_TO_V2
media: Japanese light novels
generation: V2
status: active_provisional
source_boundary: "V1 analytical corpus compared against V2 locked Japanese primary text"
supersedes: null
superseded_by: null
do_not_use_as_current_authority: false
---

# Sound! Euphonium — V1 → V2 Revision Method

## 1. Purpose

V1 is substantial enough that V2 should not merely overwrite it.

This method preserves V1 as intellectual provenance while creating a deterministic route from old claims to current authority.

The governing revision vocabulary is:

- `PRESERVE`
- `STRENGTHEN`
- `REVISE`
- `DOWNGRADE`
- `REJECT`
- `OPEN`

V2 earns authority claim by claim through Japanese-primary rereading, not by virtue of being newer.

---

## 2. Status of V1

The V1 corpus remains under:

`90 Legacy and Superseded/V1 Analysis/`

It should be treated as **historical_legacy** once V2 becomes active.

V1 continues to matter for:

- provenance;
- recovering prior reasoning;
- identifying scenes and hypotheses;
- comparing interpretive change;
- demonstrating which V2 conclusions are genuinely new.

V1 must not be silently edited to match V2.

---

## 3. Why revision is necessary

The need for V2 is not primarily that V1's macro reading is obviously wrong.

The V1 documents themselves repeatedly warn that their OCR-derived text is reading-grade rather than definitive quotation-grade. That creates uneven risk.

### High revision-risk claims

Claims dependent on:

- exact particles;
- sentence endings;
- dialect forms;
- honorifics;
- pronouns;
- punctuation;
- quotation boundaries;
- small kana;
- ruby/orthographic distinction;
- exact names/kanji;
- subtle grammatical scope;
- line-level lexical repetition.

These require fresh verification from locked Japanese EPUB text.

### Medium revision-risk claims

Claims dependent on:

- fine scene sequencing;
- who exactly said or inferred something;
- minor character attribution;
- viewpoint transitions;
- local causality;
- precise chronology;
- omitted short passages.

### Lower—but not zero—revision risk

Broad claims based on repeated narrative structure, such as:

- Kumiko's movement toward owned desire;
- Kitauji's changing institutional culture;
- the social limits of meritocracy;
- asymmetry in Mizore/Nozomi;
- Mayu as a challenge to Kumiko's desire-centered model.

These are less likely to disappear because of a particle error, but V2 must still test scope, counterexamples, and wording.

---

## 4. Claim unit

The revision ledger should not operate only at document level.

A claim row should contain, when applicable:

- `claim_id`
- `v1_artifact`
- `v1_section`
- `v1_claim_summary`
- `claim_domain`
- `scope`
- `v1_source_basis`
- `ocr_sensitivity`
- `v2_primary_locators`
- `v2_disposition`
- `v2_current_formulation`
- `reason_for_change`
- `current_authority_artifact`
- `confidence`
- `open_dependencies`

---

## 5. Claim domains

Classify claims into domains so revision can be audited systematically.

Recommended domains:

- `THEME`
- `CHARACTER`
- `RELATIONSHIP`
- `VOICE_LANGUAGE`
- `FOCALIZATION_FORM`
- `MUSIC_PEDAGOGY`
- `INSTITUTION_LEADERSHIP`
- `MERIT_JUDGMENT`
- `FAMILY_ADULTHOOD`
- `MATERIAL_OPPORTUNITY`
- `REGIONALITY`
- `MOTIF_SYMBOL`
- `CHRONOLOGY_FACT`
- `PARATEXT`

A claim may have more than one domain but should have one primary routing home.

---

## 6. Disposition definitions

### PRESERVE

The V1 formulation remains materially correct at the same level of confidence.

Use when V2 confirms rather than merely fails to contradict it.

### STRENGTHEN

V1 was correct and V2 provides stronger, broader, cleaner, or more directly grounded support.

Typical reasons:

- clean Japanese wording clarifies a pattern;
- later/local evidence was underused;
- multiple perspectives converge;
- a recurring linguistic pattern can now be demonstrated rather than asserted.

### REVISE

The core insight survives but the formulation, scope, mechanism, or emphasis changes materially.

Examples of revision types:

- too universal → conditional;
- moral explanation → social/behavioral mechanism;
- one-sided relationship reading → asymmetric dyadic model;
- symbolic reading → symbolic plus technical/material account.

### DOWNGRADE

The claim remains plausible but V1 expressed more confidence or breadth than the evidence supports.

### REJECT

V2 primary evidence contradicts the claim or shows that it depended on a factual/OCR error.

Do not use `REJECT` merely because a different interpretation is more interesting.

### OPEN

Evidence remains materially underdetermined or a needed source is absent.

An `OPEN` claim is not a failure. It is an explicit protection against false closure.

---

## 7. Audit workflow per volume

After the independent V2 volume reading is drafted:

### Step 1 — extract V1 claims

Read the corresponding V1 deep reading and identify:

- executive thesis;
- major character claims;
- major relationship claims;
- language/voice claims;
- formal claims;
- thematic claims;
- source-sensitive quotations;
- unresolved predictions.

### Step 2 — map to V2 evidence

Attach clean primary locators.

### Step 3 — adversarial test

For each major claim ask:

- What evidence would make this false?
- Did V1 ignore a contrary scene?
- Is the claim actually Kumiko's interpretation?
- Does another viewpoint complicate it?
- Does clean Japanese weaken a linguistic reading?
- Is the claim specific to this volume or only visible with hindsight?

### Step 4 — disposition

Assign one revision state.

### Step 5 — route current formulation

Record which V2 artifact now carries the authoritative version.

---

## 8. Full-series V1 theses requiring explicit audit

The final V1 synthesis contains several high-value theses that should each receive dedicated ledger entries rather than being implicitly inherited.

Examples include:

### Desire

V1: the series concerns how private desire becomes audible inside collective life.

V2 audit questions:

- Does this adequately include characters whose relation to music is not strongly ambition-centered?
- Does the formulation overprivilege Kumiko's development?
- How do Mayu, Hazuki, Aoi, and non-A performers constrain it?

### Kumiko's developmental sequence

V1: `perception → judgment → speech → intervention → leadership → transmission`.

Audit:

- Is this chronology too clean?
- Where does she regress or act strategically before being fully self-aware?
- Which capacities preexist but are socially inhibited rather than undeveloped?

### Meritocracy

V1: meritocratic selection is necessary, incomplete, and socially dangerous.

Audit:

- What exactly counts as merit in Taki's practice?
- How contextual is selection by repertoire and ensemble balance?
- Which legitimacy problems are procedural versus relational?

### Specialness

V1 distinguishes hierarchical, functional, projected, and relational specialness.

Audit:

- Is this taxonomy textually robust or a useful analyst abstraction?
- Which characters actually articulate each version?
- Does relational irreplaceability risk underplaying functional replacement anxiety?

### Empathy as power

V1 argues that Kumiko's perception gives her capacity to influence and manage others.

Audit:

- When does she actually act strategically?
- When is V1 reading ordinary attentiveness as manipulation?
- How do other characters perceive her interventions?

### Institutional maturation

V1 reads Kitauji as moving from concentrated charismatic dependence toward distributed institutional memory.

Audit:

- What practices are actually transmitted?
- Which depend on Taki?
- Which fail to reproduce?
- What changes in the second and third generations?

### Teaching as mature euphonium function

V1 interprets adult Kumiko's teaching as an extension of relational listening.

Audit:

- What evidence directly links her educational choice to these skills?
- What is symbolic interpretation versus explicit motivation?

---

## 9. Character revision policy

V1 character summaries often compress development into a mature arc. V2 should retain two layers:

### Historical state truth

What the character is like at a specific point.

### Full-arc synthesis

What later evidence reveals about stable and changing patterns.

When these conflict, do not rewrite the earlier artifact to sound like the later person.

This is especially important for simulation-grade character models.

---

## 10. Relationship revision policy

Do not revise a relationship claim by searching only for stronger intimacy evidence.

Audit all of:

- mutuality;
- asymmetry;
- exclusivity;
- practical dependence;
- conflict;
- jealousy;
- ordinary companionship;
- address language;
- third-party perception;
- unresolved ambiguity.

For romantic/yuri-coded material, distinguish:

1. explicit textual status;
2. strong romantic/yuri coding;
3. intimate but not determinately romantic evidence;
4. analyst inference.

---

## 11. Language-claim revision policy

Because V2's clean-text advantage is greatest here, all major V1 voice claims must be re-evidenced rather than simply marked `PRESERVE` from memory.

For each major character:

- collect multiple exact examples;
- compare addressees;
- compare emotional states;
- compare public/private settings;
- compare internal narration and speech where available;
- check whether a claimed dialect feature is recurrent or exceptional.

A single vivid line is insufficient to define a complete voice.

---

## 12. Anthology and focalization revision policy

The V1 analysis correctly recognized that alternate focalizers change the evidentiary field.

V2 should use the anthology material to audit claims made from Kumiko-centered volumes.

Where another viewpoint reveals Kumiko, Reina, Asuka, Mizore, Nozomi, Shuuichi, or another major character from outside, record whether it:

- confirms self-presentation;
- exposes a blind spot;
- changes perceived social influence;
- reveals behavior absent from Kumiko's knowledge;
- or leaves the earlier interpretation intact.

---

## 13. No novelty bias

A V2 project can fail by assuming every old conclusion needs correction.

The correct question is not:

> What can V2 say that V1 did not?

It is:

> What formulation best survives the cleaner and more systematic evidence?

A large number of `PRESERVE` or `STRENGTHEN` dispositions is acceptable if earned.

---

## 14. Supersession rules

### During active reread

- V2 volume-local findings are `active_provisional`.
- V1 remains the historical record.
- the current corpus map should route questions to V2 where a V2 artifact exists, but warn when full-series synthesis is not yet complete.

### After a movement checkpoint

The checkpoint becomes preferred authority for that completed boundary unless superseded by later full-series work.

### After V2 final freeze

V2 full-series/specialist/character artifacts become canonical current authority.

V1 remains preserved under `90 Legacy and Superseded` with `do_not_use_as_current_authority: true` in any newly generated legacy metadata/indexing surface.

Do not delete V1.

---

## 15. Minimum revision-ledger deliverables

Before V2 can be frozen:

- every V1 volume executive thesis has a disposition;
- every major V1 full-series thesis has a disposition;
- every V1 voice/register claim used in V2 character models has been clean-text verified;
- factual corrections are separately indexed;
- rejected/downgraded claims route to explicit reasons;
- preserved claims route to current evidence;
- unresolved claims remain `OPEN` rather than disappearing.

---

## 16. Immediate implementation

Create `HIBIKE_V1_CLAIM_REVISION_LEDGER.md` as soon as V2 Volume 1 begins.

The ledger should grow prospectively. Do not defer all revision work until after Volume 10, because that would recreate the same compression problem V2 is designed to solve.
