---
series: KONOSUBA
artifact_type: corpus_map
scope: FULL_MAIN_SERIES
generation: V1
status: canonical
source_boundary: Japanese main-series V01-V17 source-complete with accepted sequential analysis through V12; 41-object expanded-source snapshot reconciled 2026-10-16 and separately gated from main derivation
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
project_initialization:
  status: canonical
  architecture_lifecycle: EVOLVING
  governing_method: 00 Frameworks and Methods/KONOSUBA_VOLUME_DEEP_READING_METHOD.md
  synthesis_architecture: 00 Frameworks and Methods/KONOSUBA_SYNTHESIS_ARCHITECTURE_AND_ROADMAP.md
  method_status: canonical
  source_reconnaissance_complete: true
  required_ledgers_initialized: true
  sequential_analysis_lock: open
  next_permitted_operation: CHECKPOINT_V10_V12
sequential_execution:
  mode: continuous_sequential
  unit_type: volume
  authorized_start: V11
  terminal_boundary: V17
  committed_high_water_mark: V12
  next_candidate_operation: CHECKPOINT_V10_V12
  confirmation_between_units: false
  run_state: active
---

# KONOSUBA - Current State and Corpus Map

## 1. Purpose

This is the canonical first-read document for the KONOSUBA analytical project. It identifies the current source boundary, governing methods, project phase, authority rules, intended analytical architecture, and the retrieval path an analyst should follow before reading or modeling the series.

The project is designed around one primary objective:

> Build evidence-grounded, prospectively tested models of KONOSUBA's major characters that can reproduce plausible behavior, decision-making, interpersonal dynamics, ordinary-life preferences, comic failure modes, seriousness overrides, and Japanese-language voice across both canonical-comic and transferred cross-context situations.

The project is not primarily a plot-summary project and is not satisfied by trait lists, catchphrase imitation, or fandom shorthand such as "Aqua is stupid" or "Megumin likes Explosion." It seeks the generative mechanisms underneath those surface descriptions.

## 2. Current authority state

**Project state:** ACTIVE / PROVISIONAL — V01–V12 sequential analysis accepted. Gen03 remains the canonical frozen prospective model derived from V01–V09. V10, V11 and V12 local outcomes are preserved separately; the V10–V12 tranche remains OPEN until its formal checkpoint, complete J02 pool and Gen04 freeze are accepted. V11 K04 remains FALSIFIED; V12 adds partly matched adverse evidence without erasing that failure. Original model/prediction wording and blank fields are unchanged. The owner’s 2026-10-16 instruction authorizes continuous execution through V17 and the bounded synthesis, validation and expanded-corpus program. The next operation is the V10–V12 checkpoint; V13 remains unopened.

**SEQUENTIAL_ANALYSIS_LOCK = OPEN.** This is continuation of the mature imported project, with its four current methods, existing ten ledgers and source boundary verified. The structured run declarations recover the current owner-authorized bounds; they do not create new source authority. The [run and reconciliation audit](09%20Audits%20and%20Manifests/KONOSUBA_CONTINUOUS_COMPLETION_RUN_AUDIT.md) records accepted, working and published state separately.

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
Canonical Drive source-folder ID: `1cCqwK0Bvd9OjcnN8jdsixAQrVOmlFfuw`.

Subdirectories:

- `Main Series` - Japanese EPUBs V01-V17, source-complete.
- `Short Stories` - four Yorimichi collections.
- `Spin-offs` - seven novels: Explosions V01–V03, Continued Explosions V01–V02, Masked Devil and Fantastic Days.
- `Extra - Dust` - V01–V07 and the separately titled, unnumbered continuation.
- `Artbooks` - Cheers and Blessing.
- `Fanbooks` - Official Memorial Fanbook.
- `TRPG` - core and advanced rulebooks.
- `Source Audit and Manifests` - six audit/import/propagation files; no EPUB.

The [source inventory](01%20Source%20Lock%20and%20Inventory/KONOSUBA_SOURCE_INVENTORY.md) and [41-object coverage/admission matrix](01%20Source%20Lock%20and%20Inventory/KONOSUBA_SOURCE_COVERAGE_AND_ADMISSION_MATRIX.md) reconcile all eight live folders: 17 main novels, 19 supplemental prose volumes and five mixed/reference books. The current audit manifest covers 36 objects; five later Calibre imports complete the 41. Newly retrieved bytes match all recorded hashes. The older 20-book language audit, V07 audit and 21-book Git inventory retain their historical scopes and are not present-corpus completeness certificates. The former migrated `drive-ref` fragments are unresolved in the current reference index; verified source-plane IDs in the inventory/matrix supply recovery without changing frozen migration records.

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

### Expanded-corpus and post-validation stages

The other 15 supplemental prose books, individual main-EPUB bonuses, and eligible fiction within the five mixed/reference books belong to a separate post-validation stage. Their presence does not expand main-series derivation. The [source-lock amendment](01%20Source%20Lock%20and%20Inventory/KONOSUBA_SOURCE_LOCK.md) and [architecture §9](00%20Frameworks%20and%20Methods/KONOSUBA_SYNTHESIS_ARCHITECTURE_AND_ROADMAP.md#9-expanded-corpus-responsibility-amendment--2026-10-16) define the four-stage dependency and evidence-proportional outputs. Additional sources are supplementary-only in this run rather than selectively recruited tests. Image-only artbooks, fanbook and TRPG books require direct page/component inspection. Expanded synthesis remains incomplete until the full admitted narrative scope and required outputs have validated dispositions; the original four validation books are insufficient by themselves.

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

**COMPLETE.** V07-V09 prospectively tested the immutable Model Generation 0.2 predictions. `KONOSUBA_V07-V09_CHECKPOINT.md` closes the 22-prediction tranche: 13 CONFIRMED, 5 PARTIAL, 3 NOT_TESTED and 1 AMBIGUOUS. The partial cases include a locally failed cost-inhibition prediction (`MG02-M02`); `MG02-M04` remains AMBIGUOUS. Model Generation 0.3 and its 25 V10-V12 predictions are frozen after V09 and before V10 exposure. The original Gen 0.1/0.2 wording and historical outcomes remain preserved.

### Phase 4 - V10-V12

**ACTIVE / CHECKPOINT DUE.** V10–V12 principal narratives and local prospective tests of unchanged Gen03 are complete. Their separate outcomes and V11’s K04 falsification remain preserved. The formal tranche is OPEN: accept `KONOSUBA_V10-V12_CHECKPOINT.md`, independently verify the complete J02 pool, and freeze Gen04 with V13–V15 predictions before V13 exposure. V13 remains unopened; no Gen04 is declared by the V12 transaction.

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
- `09 Audits and Manifests`

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
- `02 Sequential Readings/KONOSUBA_V09_DEEP_READING.md` — active provisional V09 authority; tranche-closing prospective validation volume against Model Generation 0.2.
- `02 Sequential Readings/KONOSUBA_V10_DEEP_READING.md` — active provisional V10 authority; first prospective validation volume against frozen Model Generation 0.3, with the V10-V12 tranche still open.

- [KONOSUBA_V11_DEEP_READING.md](02%20Sequential%20Readings/KONOSUBA_V11_DEEP_READING.md) — active provisional V11 authority; second local prospective test of Gen03, complete main narrative and synchronized ledgers.

- [KONOSUBA_V12_DEEP_READING.md](02%20Sequential%20Readings/KONOSUBA_V12_DEEP_READING.md) — active provisional V12 authority; third local prospective test of Gen03, complete principal narrative and synchronized ledgers.

### Active cumulative ledgers through V12

- `KONOSUBA_CHARACTER_STATE_LEDGER.md`
- `KONOSUBA_RELATIONSHIP_STATE_LEDGER.md`
- `KONOSUBA_DECISION_ERROR_LEDGER.md`
- `KONOSUBA_COMPETENCE_CONTEXT_LEDGER.md`
- `KONOSUBA_HUMOR_MECHANICS_LEDGER.md`
- `KONOSUBA_JAPANESE_VOICE_HUMOR_LEDGER.md`
- `KONOSUBA_SERIOUSNESS_OVERRIDE_LEDGER.md`
- `KONOSUBA_KAZUMA_NARRATOR_LEDGER.md`
- `KONOSUBA_ORDINARY_LIFE_PREFERENCES_LEDGER.md`
- `KONOSUBA_MODEL_PREDICTION_VALIDATION_LEDGER.md` — preserves immutable Gen 0.1/0.2 text and historical outcomes, the completed V07-V09 Gen 0.2 adjudication, and all 25 Gen 0.3 V10-V12 predictions frozen before V10 exposure with their original blank outcome/adjudication fields; a separate V10 local addendum records 6 CONFIRMED, 6 PARTIAL and 13 NOT_TESTED. The V10-V12 tranche remains open. A separate V11 addendum records 8 CONFIRMED / 4 PARTIAL / 12 NOT_TESTED / 1 FALSIFIED; the original fields remain blank. A separate V12 addendum records all25 local dispositions; the complete formal tranche remains open pending its checkpoint.

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

### V09 prospective-validation and Model Generation 0.3 state

The [V09 receiving review](09%20Audits%20and%20Manifests/KONOSUBA_V09_RECEIVING_REVIEW.md) records acceptance, bounded source verification and correction RC-V09-01. Read its equipment-disposal correction alongside frozen CP03-M05; the original model and prediction bytes remain preserved.

V09 is complete as the third and tranche-closing prospective test of Model Generation 0.2. `02 Sequential Readings/KONOSUBA_V09_DEEP_READING.md` is the active provisional V09 reading authority. The prologue, main chapters and both narrative epilogues are included; afterword, ebook bonus, poll and other non-main-narrative material do not contribute to the canonical model.

`04 Checkpoints and Model Validation/KONOSUBA_V07-V09_CHECKPOINT.md` is the completed tranche checkpoint and canonical Model Generation 0.3 freeze. Its 22-row Gen 0.2 closeout is **13 CONFIRMED, 5 PARTIAL, 3 NOT_TESTED and 1 AMBIGUOUS**. The checkpoint preserves the exact frozen predictions and the original V07/V08 outcome wording alongside V09 evidence, confidence transitions and failure diagnostics.

The count must be read with its boundaries: `MG02-M02` is PARTIAL with a locally failed ordinary-companion-cost inhibition prediction; `MG02-M04` is AMBIGUOUS because adverse collateral is visible but the full serious-harm/tactical-choice trigger is unresolved. `MG02-E01` is PARTIAL and requires revision of the broad routing-necessity claim. These results are not erased by narrower Gen 0.3 hypotheses. Untested inherited branches remain untested rather than gaining confirmation from analogous scenes.

Model Generation 0.3 is derived from Japanese V01-V09 main-narrative evidence and its **25 V10-V12 predictions are already frozen before any V10 narrative exposure in this analytical session**. The exact block and freeze receipt are identified by the checkpoint and prediction ledger; outcome/adjudication fields remain blank. V10 is next, as the first prospective test of this frozen generation. Retrieve and preserve that block before opening V10.

The earlier V01-V08 subsections, including the V06-era Gen 0.2 freeze-state prose, remain historical records of their original analytical states. Their future-facing statements are not rewritten; this V09 subsection and the live status/next-action fields provide the current continuation state.

### V10 local prospective-validation state

The [V10 receiving review](09%20Audits%20and%20Manifests/KONOSUBA_V10_RECEIVING_REVIEW.md) records acceptance and source-timing correction RC-V10-01. The correction preserves all frozen predictions and V10 outcome labels.

V10 is complete as the first prospective test of frozen Model Generation 0.3. `02 Sequential Readings/KONOSUBA_V10_DEEP_READING.md` is the active provisional V10 reading authority. The prologue, Chapters 1–5 and narrative epilogue (`text/part0009.html`–`text/part0015.html`) were read completely in sequence: 3,026 all-body paragraphs. Afterword, ebook bonus, other paratext and uninspected illustrations do not contribute narrative evidence; V11+, withheld side narrative and external series knowledge were not used.

The V10 local addendum in `03 Longitudinal Ledgers/KONOSUBA_MODEL_PREDICTION_VALIDATION_LEDGER.md` adjudicates all 25 Gen03 predictions: **6 CONFIRMED, 6 PARTIAL and 13 NOT_TESTED**, with no whole-row AMBIGUOUS or FALSIFIED outcome. This is a local coverage record, not a closed-tranche score. PARTIAL rows retain tested versus untested branches and contrary evidence; NOT_TESTED does not count as confirmation or failure.

Key boundaries include: `MG03-K01` supports indirect search and delegation without fully replicating the exact new-capability revision branch; `MG03-M01` supports specialist identity activation without isolating companion-utility priority; `MG03-D02` supports audience sensitivity while retaining enjoyment of actual coercive control as contrary agency-component evidence; `MG03-E01` supports deployment repair without completing the alternative-provider/comparative branches. `MG03-J01` remains mapping-specific, and `MG03-J02` remains open for the complete V10–V12 pooled census. The single admired meal, farm casts/return hunt and Iris's duty-linked self-restriction do not silently fill the stricter repeated-service, planned-exit, weakening-operation or original-wish/duty triggers.

The funding decision's chronology is material: Levi agrees to continued defense and additional offensive support before Ragcraft's identity is exposed. Later exposure strengthens gratitude and the alliance; it does not cause the earlier support reversal. Specialist success also retains its actual contributions and limits: Aqua's engaged support competence does not erase the fugu readiness failure; Darkness initiates protective actions and the gag-release escape idea; Iris supplies the dragon's terminal attack and independently defeats the impersonator as Kazuma and Darkness try to open her door, before they can intervene.

Model Generation 0.3 remains the current frozen prospective model, derived from V01–V09. Its exact 25-prediction V10–V12 block remains **45,675 bytes**, SHA-256 `ebe83ef5dc87fc2e85f8f711e2ba373239d4eea4fd14f466537dbd3625d76150`, with original Outcome/Adjudication fields blank. The model block remains **17,746 bytes**, SHA-256 `dfd92578ddef97eeaf942a6a5d713f37a84678abc9433bce05d36d2ec659d85a`. V10 evidence is additive; frozen wording, confidences and disconfirmation conditions are unchanged. The V09 receiving correction RC-V09-01 continues to govern the earlier equipment-disposal shorthand without rewriting frozen bytes.

Phase 4 V10–V12 is **ACTIVE**, with V10 complete and the tranche **OPEN**. V11 is next, **UNOPENED and awaiting new authorization**. No V10–V12 checkpoint or Model Generation 0.4 freeze has been completed, and no V13–V15 prediction set is created at this stage. The completed V07–V09 checkpoint remains the current model-freeze authority.

Source-policy metadata remains a separate responsibility. The source-lock reading-state lag and the previously user-reported expanded side-corpus inventory lag remain deferred as recorded in the V09 receiving review; the expanded inventory was not re-audited by this V10 analysis. No source lock, inventory, source-route listing or withholding rule is updated by this state change. Side narratives remain withheld under the governing source policy.

All earlier V01–V09 subsections, including their original future-facing freeze/next-volume statements and the V09 receiving-review route, remain historical records. This V10 subsection and the live current-state/next-action fields supply the current continuation state without rewriting those records.

### V11 local prospective-validation state

The [V11 reading](02%20Sequential%20Readings/KONOSUBA_V11_DEEP_READING.md) and [receiving review](09%20Audits%20and%20Manifests/KONOSUBA_V11_RECEIVING_REVIEW.md) close the main source through epilogue P0143: seven members, 2,865 all-body paragraphs, 108,101 base characters. All ten ledgers carry additive V11 records. The 25 local outcomes are **8 CONFIRMED / 4 PARTIAL / 12 NOT_TESTED / 1 FALSIFIED**.

`MG03-K04` fails locally: Kazuma notices Aqua’s actual tears and continues the selected teasing/humiliation before later relief. Legitimate property recovery and eventual mercy remain coexisting evidence. `MG03-I02` now has a clean expressed-wish/understood-duty/narrowed-request match. `MG03-E02` remains untested because the required efficiency-promising reorganization is not established, despite actual lasting retirement and strong household resistance. Missing safety/logistics, harm-knowledge and membership-change conjuncts remain visible in M03/M05/D02.

The complete V11 humor census contains 112 fixed episodes: 108 clear L0–L2, 2 L3 and 2 unresolved; original fine-code disagreement and partial coding blindness remain disclosed. Eleven role/window comparisons retain adverse and insufficient cases. J02 is still PARTIAL/TRANCHE_OPEN until the complete V10–V12 pooled scope is scored. No new model generation is introduced.

Kazuma’s actual castle departure, coerced return, delayed confession and reciprocal care do not collapse into a unitary loyalty claim. Aqua’s accurate appraisal/effective power coexist with prestige-goal failure. Megumin’s dignity inhibition differs from build-burden guilt; the intermediate relationship request is not a completed exclusive couple. Darkness’s protective initiative coexists with manipulation and usefulness insecurity. The final child’s identity and parentage remain unknown at this boundary. Komekko’s diary is a report, not proof she witnessed every event it names.

V11’s separately identified bonus **そのスキル、危険につき** remains unread and reserved for the expanded stage. Source metadata reconciliation covers all 41 objects; this source-unit acceptance advances only MAIN-11’s principal main narrative. Earlier map subsections retain their historical future-facing wording. Current authority and next-operation declarations govern continuation to V12 after exact publication checks close.

### V12 local prospective-validation state

The [V12 reading](02%20Sequential%20Readings/KONOSUBA_V12_DEEP_READING.md) and [receiving review](09%20Audits%20and%20Manifests/KONOSUBA_V12_RECEIVING_REVIEW.md) accept the eight principal-main members `text/part0009.html`–`part0016.html`: 2,841 all-body paragraphs, 2,624 nonempty and 101,448 base characters. The producer, independent humor reader and receiving integrator each read that complete main narrative; their overlapping coverage is not added. Independent semantic review is separately bounded. All ten ledgers receive additive V12 records.

K04 retains a strong adverse actual-visible-tears candidate with explicit cue/motive matching limits; its local ambiguity does not rescue V11's clean failure. Aqua's owned sustained healing is observed, but recognition-conditioned continuation remains untested because reward onset is unshown. Actual tactical contribution, injury and finite endurance coexist with pleasure; eventual Eris rescue remains distinct from Kazuma's useful prepared water. The mutual intermediate relationship advances beyond V11 without becoming an exclusive settled couple. Initial unwanted contact and later directed participation remain separate. Civic education predates Kazuma's discovery; principal pension/treatment tax and temporary orphanage bridging remain distinct.

The complete source-first humor census has130 fixed units:127 clear L0–L2 and three unresolved mixed cases, giving local bounds127–130/130. All119 original lineages and22 pre-coding operations survive. Both L files sealed before code/aggregate exchange; disclosed within-volume boundary preview means discovery was not fully blind. Fourteen fixed voice comparisons retain weak, adverse and sparse windows. A factual role gloss is corrected by an explicit erratum outside the immutable window registry. J02 remains PARTIAL/TRANCHE_OPEN until the complete V10–V12 pool is independently verified at checkpoint.

The separately identified V12 bonus **伝説の魔女**, afterword and other edition components remain unread and assigned to later component review. Only MAIN-12's principal narrative advances to READ_COMPLETE/ANALYZED; the fixed41-object identity seal and all other narrative dispositions are preserved. A metadata-only field rename clarifies membership in the five-record incremental Calibre manifest without asserting that the other36 never underwent Calibre processing. No future main or side narrative enters these prospective states. Earlier map subsections preserve historical future-facing wording; the current declarations and this update govern continuation.

## 13. Current next actions

1. Preserve `KONOSUBA_V07-V09_CHECKPOINT.md`, the exact frozen Gen03 V10-V12 prediction block, RC-V09-01 and the new V10 local validation record. The 25 predictions remain frozen with their original blank outcome/adjudication fields; do not regenerate or rewrite them.
2. Close the accepted V12 transaction’s exact source audit, housekeeping and final audit. Then complete the separately reviewable V10–V12 checkpoint and Gen04 V13–V15 forecast freeze. The accepted principal-main high-water mark is V12; V13 remains unopened. Continue without routine confirmation through V17 while preserving every source and forecast gate.
3. At each unit boundary, refresh live map/governance and relevant ledgers, retrieve the existing frozen checkpoint/predictions and earlier outcomes, verify preserved bytes, and complete the source-identity/capability gate before narrative exposure. Append evidence without erasing adverse cases or untested branches.
4. Adjudicate every Gen03 forecast across V10–V12, retaining disconfirmations, partial causal coverage and untested branches. Verify the complete J02 pool before formal closure. Accept and commit the checkpoint/Gen04 forecast freeze before V13 exposure; the V12 transaction itself creates neither a new generation nor a completed tranche.
5. Keep all side narrative and edition bonuses outside prospective derivation. Freeze the main-only reconstruction suite before the four designated holdouts, preserve the validation results, then perform the full expanded-prose/component program and attributable post-validation reconstruction. Source metadata is now reconciled separately in the 41-object matrix; no metadata or download state counts as completed literary analysis.

## 14. Governing principle

The project succeeds only if the final models can explain not merely that the characters are funny, but **what repeatedly makes each specific character become funny in a specific way, what suppresses that behavior, and how the same underlying person should behave when the genre register changes**.
