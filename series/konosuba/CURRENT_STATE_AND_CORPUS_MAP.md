---
series: KONOSUBA
artifact_type: corpus_map
scope: FULL_MAIN_SERIES
generation: V1
status: canonical
source_boundary: Japanese light novel main series V01-V17 source-complete; V07 acquired/audited 2026-08-27; canonical sequential reading complete through V08
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
---

# KONOSUBA - Current State and Corpus Map

## 1. Purpose

This is the canonical first-read document for the KONOSUBA analytical project. It identifies the current source boundary, governing methods, project phase, authority rules, intended analytical architecture, and the retrieval path an analyst should follow before reading or modeling the series.

The project is designed around one primary objective:

> Build evidence-grounded, prospectively tested models of KONOSUBA's major characters that can reproduce plausible behavior, decision-making, interpersonal dynamics, ordinary-life preferences, comic failure modes, seriousness overrides, and Japanese-language voice across both canonical-comic and transferred cross-context situations.

The project is not primarily a plot-summary project and is not satisfied by trait lists, catchphrase imitation, or fandom shorthand such as "Aqua is stupid" or "Megumin likes Explosion." It seeks the generative mechanisms underneath those surface descriptions.

## 2. Current authority state

**Project state:** ACTIVE / PROVISIONAL - Phase 3 V07-V09 prospective validation; V01-V08 complete, Model Generation 0.2 remains frozen, V07-V08 outcome evidence entered, V09 next.

**Canonical entrypoint:** this file.

**Governing framework documents:**

1. `00 Frameworks and Methods/KONOSUBA_SYNTHESIS_ARCHITECTURE_AND_ROADMAP.md`
2. `00 Frameworks and Methods/KONOSUBA_VOLUME_DEEP_READING_METHOD.md`
3. `00 Frameworks and Methods/KONOSUBA_CHARACTER_RECONSTRUCTION_AND_VALIDATION_PROTOCOL.md`
4. `00 Frameworks and Methods/KONOSUBA_JAPANESE_HUMOR_AND_VOICE_PROTOCOL.md`
5. `01 Source Lock and Inventory/KONOSUBA_SOURCE_LOCK.md`
6. `01 Source Lock and Inventory/KONOSUBA_SOURCE_INVENTORY.md`

These documents are canonical methodology until explicitly superseded. Sequential readings and later syntheses must conform to them unless a documented methodological revision is made.

## 3. Canonical source route

**Primary-source root:** `Konosuba`

Google Drive folder:
`../../provenance/drive-artifacts/DRIVE_ARTIFACT_REFERENCE_INDEX.md#drive-ref-0f70fc4c9766e347`

Subdirectories:

- `Main Series` - Japanese EPUBs V01-V17, source-complete.
- `Short Stories` - `Yorimichi`.
- `Spin-offs` - `Consulting the Masked Devil`.
- `Extra - Dust` - Dust V06-V07.
- `Source Audit and Manifests` - ingestion manifest and Japanese-language audit.

The updated source manifest records 21 retained primary books from 28 input EPUBs (27 valid; one zero-byte corrupt), with main-series V01-V17 all present. The original 20-book batch remains covered by `KONOSUBA_SOURCE_LANGUAGE_AUDIT.md`; V07 was separately verified against manifest SHA-256 `38c1fa428ba096cdc4c8b7a5df393dd5763b438e780ef2cef138860c608143c5` and passed the dedicated `KONOSUBA_V07_SOURCE_LANGUAGE_AND_INTEGRITY_AUDIT.md` before the continuity gate was removed.

## 4. Main-series source boundary

### Present

`V01 V02 V03 V04 V05 V06 V07 V08 V09 V10 V11 V12 V13 V14 V15 V16 V17`

### Missing

`none`

The former V07 continuity gate was resolved on 2026-08-27. V07 is present in the canonical Main Series folder, matches the updated manifest SHA-256, and passed a dedicated Japanese-language/integrity audit. Canonical analysis may now proceed in sequence through V08-V17 subject to the established tranche checkpoints and frozen-prediction rules.

## 5. Derivation corpus versus validation corpus

### Core derivation corpus

The Japanese main-series novels V01-V17 are the corpus from which the principal character models will be derived.

### Withheld validation corpus

The following material is intentionally withheld from core model construction until the main-series models have been frozen:

- `Konosuba - Short Stories - Yorimichi.epub`
- `Konosuba - Spin-off - Consulting the Masked Devil.epub`
- `Konosuba Extra - Dust - Volume 06.epub`
- `Konosuba Extra - Dust - Volume 07.epub`

After chronology, canonicity, narrator/viewpoint, and character-coverage checks, suitable portions of these sources may be used as out-of-sample validation. This separation is deliberate: a model that predicts behavior in material it was not built from is stronger than one that merely explains the entire corpus retrospectively.

## 6. Mandatory reconstruction subjects

The initial mandatory full-model subjects are:

- Satou Kazuma
- Aqua
- Megumin
- Darkness

Secondary characters are promoted to full reconstruction subjects only when the corpus provides enough varied evidence across speech, action, relationships, ordinary life, conflict, and changing stakes. Narrative importance alone is not sufficient.

A secondary character may first receive a limited profile, relationship role, or voice note without being promoted to a full reconstruction model.

## 7. Core analytical commitments

The project treats comedy as evidence, but as evidence whose literalness must be adjudicated.

The analyst must distinguish:

- stable disposition from one-off gag;
- trait from temporary state;
- ignorance from bad reasoning;
- ability from judgment;
- judgment from self-regulation;
- deliberate impracticality from inability;
- comic amplification from realistic baseline behavior;
- Kazuma's narration from independently observable character evidence;
- literal semantic meaning from pragmatic Japanese-language effect;
- affection from politeness or idealization;
- ritualized conflict from genuinely relationship-threatening conflict;
- canonical farce from behavior expected to transfer into a more realistic crossover context.

The project aims to explain **why a character selects an apparently foolish action**, not merely to label the action foolish.

## 8. Prospective model-validation rule

Character-model development is intentionally prospective.

At each checkpoint, the project must freeze the current model and record falsifiable behavioral predictions **before** reading the next tranche. Later evidence then receives one of the established revision states:

- PRESERVE
- STRENGTHEN
- REVISE
- DOWNGRADE
- REJECT
- OPEN

Prediction failures are analytical evidence. They must not be erased by silently rewriting the earlier model after the fact.

## 9. Planned analytical phases

### Phase 0 - Framework, source lock, and baseline infrastructure

**COMPLETE.** Governing methods, source lock, source inventory, and current-state map are established.

### Phase 1 - V01-V03

**COMPLETE.** V01-V03 deep readings are complete. `KONOSUBA_V01-V03_CHECKPOINT.md` freezes Model Generation 0.1, and `KONOSUBA_MODEL_PREDICTION_VALIDATION_LEDGER.md` preserves the V04-V06 predictions written before V04 exposure.

### Phase 2 - V04-V06

**COMPLETE.** V04-V06 prospectively tested frozen Model Generation 0.1. `KONOSUBA_V04-V06_CHECKPOINT.md` closes the tranche, adjudicates the 20 Gen 0.1 predictions, and freezes Model Generation 0.2. The frozen Gen 0.1 prediction text remains provenance and was not rewritten after exposure.

The tranche result is 16 CONFIRMED, 2 PARTIAL/revision-bearing, 2 NOT_TESTED, and 0 complete falsifications. The count is not treated as a standalone score; the partial and untested cases remain open evidence obligations.

### Phase 2.5 - V07 continuity gate

**COMPLETE.** V07 was acquired, manifest-reconciled, Japanese-language/integrity audited, registered in the source inventory/lock, and only then opened for canonical analysis. The old 20-book source audit remains preserved as historical provenance; a dedicated V07 audit records the gate closure.

### Phase 3 - V07-V09

**ACTIVE.** V07-V08 are complete as the first two prospective tests of frozen Model Generation 0.2. V07-V08 outcome evidence has been appended without rewriting the frozen V07-V09 prediction text. V09 is next and will close the tranche and produce Model Generation 0.3.

### Phase 4 - V10-V12

Model Generation 0.4.

### Phase 5 - V13-V15

Model Generation 0.5.

### Phase 6 - V16-V17

Final sequential checkpoint and freeze of the main-series evidence base.

### Phase 7 - Specialist synthesis

Character monographs, party ensemble synthesis, humor-system synthesis, and Japanese-language comedy synthesis.

### Phase 8 - Reconstruction suite

Formal generative character models, party interaction model, cross-context transfer model, simulation tests, and consistency audit.

### Phase 9 - Full-series synthesis and archival closure

Full-series synthesis, evidence indexes, claim revision ledger, final source/authority audit, and corpus-map conversion to stable release form if the project is frozen.

## 10. Folder materialization policy

Do not create empty folders merely because the target architecture contains them. Create each layer when it has a distinct active responsibility.

Current materialized layers:

- `00 Frameworks and Methods`
- `01 Source Lock and Inventory`
- `02 Sequential Readings`
- `03 Longitudinal Ledgers`
- `04 Checkpoints and Model Validation`

Later folders should be materialized only when the first artifact of that role is generated.

## 11. Retrieval precedence

For later work, retrieve in this order:

1. this `CURRENT_STATE_AND_CORPUS_MAP.md`;
2. governing framework/method document for the task;
3. latest checkpoint and prospective prediction state;
4. relevant longitudinal ledger;
5. relevant volume deep reading;
6. specialist synthesis or reconstruction model once those exist;
7. Japanese primary source for final verification.

A later synthesis never licenses invented evidence. Exact wording, linguistic claims, and scene-level assertions should escalate to the Japanese source.

## 12. Current sequential state

### Completed

- `02 Sequential Readings/KONOSUBA_V01_DEEP_READING.md` — active provisional V01 authority.
- `02 Sequential Readings/KONOSUBA_V02_DEEP_READING.md` — active provisional V02 authority.
- `02 Sequential Readings/KONOSUBA_V03_DEEP_READING.md` — active provisional V03 authority.
- `02 Sequential Readings/KONOSUBA_V04_DEEP_READING.md` — active provisional V04 authority; first prospective validation volume against Model Generation 0.1.
- `02 Sequential Readings/KONOSUBA_V05_DEEP_READING.md` — active provisional V05 authority; second prospective validation volume against Model Generation 0.1.
- `02 Sequential Readings/KONOSUBA_V06_DEEP_READING.md` — active provisional V06 authority; tranche-closing prospective validation volume against Model Generation 0.1.
- `02 Sequential Readings/KONOSUBA_V07_DEEP_READING.md` — active provisional V07 authority; first prospective validation volume against Model Generation 0.2.
- `02 Sequential Readings/KONOSUBA_V08_DEEP_READING.md` — active provisional V08 authority; second prospective validation volume against Model Generation 0.2.

### Active cumulative ledgers through V08

- `KONOSUBA_CHARACTER_STATE_LEDGER.md`
- `KONOSUBA_RELATIONSHIP_STATE_LEDGER.md`
- `KONOSUBA_DECISION_ERROR_LEDGER.md`
- `KONOSUBA_COMPETENCE_CONTEXT_LEDGER.md`
- `KONOSUBA_HUMOR_MECHANICS_LEDGER.md`
- `KONOSUBA_JAPANESE_VOICE_HUMOR_LEDGER.md`
- `KONOSUBA_SERIOUSNESS_OVERRIDE_LEDGER.md`
- `KONOSUBA_KAZUMA_NARRATOR_LEDGER.md`
- `KONOSUBA_ORDINARY_LIFE_PREFERENCES_LEDGER.md`
- `KONOSUBA_MODEL_PREDICTION_VALIDATION_LEDGER.md` — preserves immutable Gen 0.1 predictions/outcomes and frozen Gen 0.2 V07-V09 predictions written before V07 exposure.

### V01-V03 Model Generation 0.1 state

`04 Checkpoints and Model Validation/KONOSUBA_V01-V03_CHECKPOINT.md` is the canonical first model freeze. Model Generation 0.1 was derived only from V01-V03 main narrative and was frozen before V04 exposure.

`03 Longitudinal Ledgers/KONOSUBA_MODEL_PREDICTION_VALIDATION_LEDGER.md` preserves the immutable prospective V04-V06 predictions and their completed V04-V06 adjudications. It now also contains Model Generation 0.2 predictions for V07-V09 frozen before any V07 exposure. Earlier prediction text may not be rewritten.

Checkpoint-level conclusions include: Kazuma's systems/exploit competence is strong but not identical to globally high judgment; Aqua's global “uselessness” and globally weak-updater models are rejected in favor of extreme competence plus state-specific deployment/externality errors; Megumin's Explosion commitment is a knowingly protected identity rather than low intelligence; Darkness wants specific danger/powerlessness conditions while also strongly valuing contribution, protector duty, and belonging; party attachment is better inferred from costly action than reduced verbal aggression.

The V01 EPUB ebook bonus `アクア先生`, V02 ebook purchase bonus, and V03 ebook bonus `眠れる森のクルセイダー` are treated as non-sequential supplementary material pending chronology adjudication. They do not update the canonical longitudinal model at this stage.

### V04 prospective-validation state

V04 produced strong support for Model Generation 0.1 without a clear falsification, but the project does not convert this into an early Model Generation 0.2. Key V04 interim outcomes include:

- `MG01-K01` CONFIRMED with unusually strong replication of both exploit preference and the predicted embodied second-order blind spot;
- `MG01-E01` CONFIRMED by two independent specialist-routing resolutions (Running Hawk-Kites and Hans);
- Kazuma concrete loyalty, grievance retaliation, and mixed-motive predictions confirmed at V04 level;
- Aqua sacred/domain diagnosis, loyalty-by-action, and high-output externality mechanisms strongly supported;
- Megumin social-framing and group-support predictions confirmed, while direct friendly-fire inhibition remains untested in V04;
- Darkness protector/contribution/belonging predictions confirmed, while pain-based coercion receives only partial/supportive evidence;
- Japanese seriousness/register-shift and non-L3-dominant humor predictions confirmed at V04 level.

The V04 ebook bonus `町内会の不死の王` remains supplementary paratext pending chronology adjudication and does not update the sequential model.

### V05 prospective-validation state

V05 provides a second prospective test and, unlike V04, introduces a genuine model-boundary revision alongside broad confirmation. Key V05 outcomes include:

- `MG01-K01` strongly CONFIRMED again: Japanese interface/facility exploitation succeeds locally but produces the Magic Killer second-order disaster, independently replicating Kazuma's post-transition consequence blind spot;
- Kazuma concrete loyalty, grievance retaliation, and mixed-motive predictions remain CONFIRMED; V05 newly shows that identity recognition can override his own optimization preference when he preserves Megumin's Explosion build;
- Aqua sacred/domain action and loyalty-by-action remain CONFIRMED, while `MG01-A03` tedious-duty shortcut remains NOT_TESTED;
- `MG01-M01`, `M02`, and `M03` are strongly CONFIRMED; V05 also reveals that Megumin can voluntarily abandon Explosion identity under sufficiently strong relational guilt/contribution pressure; `M04` friendly-fire inhibition remains NOT_TESTED;
- Darkness protector and meaningful-contribution predictions remain CONFIRMED; pain-only coercion still lacks a clean matched test; noble/belonging anxiety remains active and the royal invitation makes V06 a high-value direct test;
- `MG01-E01` and `E02` are strongly CONFIRMED by the Sylvia/Magic Killer routing and reciprocal cleanup/identity-preservation behaviors;
- `MG01-J02` remains CONFIRMED; `MG01-J01` is now PARTIAL and requires REVISE because Yunyun becomes *more* theatrically Crimson-Demon-like under serious duty, showing that seriousness realigns register around active role rather than universally reducing theatricality.

V05 also supports mutual Kazuma/Megumin romantic interest as an active relationship variable, but not formal couple status.

The V05 ebook bonus, if present in the collected EPUB, remains supplementary paratext pending chronology adjudication and does not update the sequential model.

### V06 prospective-validation and Model Generation 0.2 state

V06 closes the first prospective-validation tranche. `04 Checkpoints and Model Validation/KONOSUBA_V04-V06_CHECKPOINT.md` is the canonical Generation 0.2 freeze. Final Gen 0.1 adjudication across V04-V06: **16 CONFIRMED, 2 PARTIAL/revision-bearing, 2 NOT_TESTED, 0 complete falsifications**.

Key tranche-closing revisions and discoveries include:

- Kazuma's indirect exploit competence remains strongly supported, but V06 isolates a distinct failure mode: status/recognition success can induce overextension even without an exploit-transition error;
- Kazuma is not indispensable to high-stakes victory when an institution supplies role structure. His comparative advantage is strongest in novel, under-structured, rule-heavy, cross-domain problems;
- Kazuma's recurring fantasy of replacing his dysfunctional party is downgraded as a stable preference: actual separation/reclassification produces attachment and exclusion anxiety;
- Aqua remains an elite sacred/support specialist whose judgment quality depends heavily on context, salience, and incentives; `MG01-A03` remains untested rather than being confirmed by analogy;
- Megumin's Explosion commitment is relationally permeable rather than absolute, while direct serious valued-companion friendly-fire inhibition (`MG01-M04`) remains untested under a clean matched trigger;
- Darkness's protector ethic now clearly includes social fairness/dignity protection and can override royal hierarchy; peer-belonging sensitivity remains a stronger psychological vulnerability than generic pain, while pain-only coercion (`MG01-D02`) remains only partially tested;
- the ensemble routing theorem is revised from “Kazuma routes the specialists” to **“successful extreme specialization requires routing, but the routing source is substitutable”**;
- the Japanese seriousness rule is revised from universal de-theatricalization to **register alignment with the role/identity that becomes authoritative under serious stakes**;
- Iris is promoted to a secondary reconstruction candidate based on V06 evidence about constrained agency, nondeferential safety, learning, royal duty, and older-brother attachment. She is twelve in this source state; present behavior must not be back-projected into adult romantic commitment.

Model Generation 0.2 was frozen before V07 exposure. `KONOSUBA_MODEL_PREDICTION_VALIDATION_LEDGER.md` contains the immutable 22 V07-V09 predictions plus V07 and V08 prospective-validation addenda. V09 remains required before Model Generation 0.3.

The V06 author afterword is excluded from character-model derivation. Narrative interlude and epilogues are included because they resolve causal and relationship state within the volume.

### V07 prospective-validation state

V07 is the first prospective test of Model Generation 0.2 and strongly validates several mechanism-level predictions without creating an early new model generation.

Key V07 outcomes include:

- `MG02-K01` and `K02` CONFIRMED strongly: Kazuma solves the Hydra and Dustiness/wedding problems through state changes, weak-tool/incentive exploits and then sacrifices his IP/wealth route for a concrete companion loss;
- `MG02-K04` CONFIRMED strongly: Darkness's credible departure/marriage produces loneliness, failed replacement, investigation and rescue;
- `MG02-K03` receives PARTIAL support from post-Sylvia status inflation but no clean V07 dangerous overextension;
- `MG02-A01` CONFIRMED very strongly through Hydra domain reasoning and instant removal of Dustiness father's hidden demonic curse; `A02` is strongly confirmed by the false dragon-egg prestige/caretaking capture; `A03/A04` remain cleanly untested;
- `MG02-M01` Trigger A and `M03` are strongly confirmed; `M02` receives partial support and `M04` remains untested;
- `MG02-D01`, `D03`, and especially `D04` receive strong confirmation. V07 adds a new Darkness failure path: protector paternalism/self-erasure through concealed burden absorption;
- `MG02-D02` is strongly confirmed for belonging sensitivity through resignation and re-entry anxiety, while pain-only coercion remains incompletely tested;
- `MG02-E01/E02` are strongly confirmed. Community/social capital is now an explicit routing/resource layer;
- `MG02-J01/J02` are confirmed at V07 level; Megumin's serious `bad wizard` rescue is a direct example of seriousness increasing theatricality around the authoritative role;
- Iris `I01/I02` are not tested because Iris is not directly present in qualifying V07 scenes.

V07 also confirms Chris/Eris identity within the canonical sequence through Kazuma's behavioral/address-pattern deduction.

The V07 ebook bonus `たまにはお礼を言いたくて` remains supplementary paratext pending chronology adjudication and does not update the sequential model.


### V08 prospective-validation state

V08 is the second prospective test of Model Generation 0.2. It adds several strong confirmations plus useful non-tests without creating an early model generation.

Key V08 outcomes include:

- `MG02-K01` and `K02` CONFIRMED strongly through joint-festival incentive architecture, Aigis preference modeling, entrusted Chris/Eris artifact duty and Kazuma's crowd-cover action;
- `MG02-K03` receives a cleaner noncombat confirmation: advisor praise/sales success increases scope, status reward and reputational/social risk;
- `MG02-A01` is strongly confirmed in the guild insect-support role; `A02` is very strongly confirmed by worship/status goal substitution;
- `MG02-A03` is now strongly supported as **selective real learning plus state-dependent defense**: Aqua prospectively applies a learned overconfidence rule, yet later defends the pyramid scheme while status/legal face-saving remains available;
- `MG02-A04` remains untested;
- Megumin `M01` receives partial support, while `M02`, `M03` and `M04` do not receive clean trigger matches. The forest Explosion provides strong inverse-condition evidence for why safe target separation matters;
- `MG02-D01`, `D02` and `D03` are strongly supported; V08's ant versus public-stage contrast materially strengthens the semantic/agency-sensitive Darkness model. `D04` is not newly tested;
- `MG02-E01` is strongly confirmed by guild versus Kazuma routing substitution, while `E02` is not newly tested;
- `MG02-J01/J02` are confirmed at V08 level;
- Iris `I01/I02` remain untested because Iris is absent.

V08 also adds two major relationship developments: direct Megumin romantic interest with interrupted Kazuma reciprocity, and a serious Kazuma/Darkness intimacy branch constrained by Darkness's fairness toward Megumin. Neither establishes formal couple status.

Chris/Eris is expanded as a secondary reconstruction candidate: V08 explicitly distinguishes divine and Chris social modes while preserving identity continuity, and identifies conscientious over-compliance as a new possible failure mechanism.

The V08 ebook bonus `漢のロマンを叶えるために` remains supplementary paratext pending chronology adjudication and does not update the sequential model.

## 13. Current next actions

1. Before V09, reread `KONOSUBA_V04-V06_CHECKPOINT.md`, the frozen Model Generation 0.2 prediction section, and the V07-V08 outcome addenda.
2. Begin canonical V09 deep reading as the **tranche-closing** prospective test of Model Generation 0.2.
3. Preserve all pre-V07 prediction wording; V09 may add only outcome/adjudication evidence and longitudinal updates until the tranche checkpoint is complete.
4. After V09, produce `KONOSUBA_V07-V09_CHECKPOINT.md`, adjudicate the full Gen 0.2 tranche, freeze Model Generation 0.3, and write V10-V12 predictions before opening V10.
5. Keep Yorimichi, Consulting the Masked Devil, and Dust V06-V07 withheld from core model derivation until the main-series reconstruction suite reaches its frozen validation boundary.

## 14. Governing principle

The project succeeds only if the final models can explain not merely that the characters are funny, but **what repeatedly makes each specific character become funny in a specific way, what suppresses that behavior, and how the same underlying person should behave when the genre register changes**.
