---
series: TOMOZAKI
artifact_type: current_state_and_corpus_map
scope: GIT_NATIVE_ANALYTICAL_ROOT
source_boundary: "Audited Japanese light-novel EPUB corpus: numbered main Volumes 01-11 plus side-story Volumes 06.5 and 08.5; source audit dated 2026-08-29"
source_audit_date: 2026-08-29
generation: V2.1_ARCHITECTURE_REMEDIATION
status: canonical
release_state: mutable_active
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
project_initialization:
  historical_gate_status: VIOLATED_ARCHITECTURE_MISSING_BEFORE_V01
  remediation_status: ACTIVE
  architecture_lifecycle: EVOLVING
  governing_method: "00 Frameworks and Methods/TOMOZAKI_ANALYTICAL_METHOD.md"
  synthesis_architecture: "00 Frameworks and Methods/TOMOZAKI_SYNTHESIS_ARCHITECTURE.md"
  method_status: canonical
  architecture_status: canonical_evolving
  source_reconnaissance_complete: true
  required_day_one_infrastructure_initialized: false
  historical_day_one_infrastructure: []
  current_longitudinal_infrastructure:
    - "03 Longitudinal Ledgers/TOMOZAKI_EFFORT_COMPETITION_AND_GOAL_OWNERSHIP_LEDGER.md"
    - "03 Longitudinal Ledgers/TOMOZAKI_CHARACTER_STATE_LEDGER.md"
    - "03 Longitudinal Ledgers/TOMOZAKI_RELATIONSHIP_STATE_LEDGER.md"
    - "03 Longitudinal Ledgers/TOMOZAKI_CLAIM_REVISION_AND_EVIDENCE_INDEX.md"
    - "03 Longitudinal Ledgers/TOMOZAKI_SOCIAL_ATMOSPHERE_AND_GROUP_SYSTEMS_LEDGER.md"
  sequential_analysis_lock: CLOSED_AT_CURRENT_V11_BOUNDARY
  longitudinal_reconciliation_gate: OPEN_BACKFILL_IN_PROGRESS
  specialist_synthesis_gate: CLOSED
  full_series_synthesis_gate: CLOSED
---

# Bottom-Tier Character Tomozaki — current state and corpus map

## 1. Responsibility

This is the **canonical current entrypoint** for the Tomozaki analytical root. It answers four questions:

1. What source/evidence boundary is currently available and authoritative?
2. What analytical work has actually been completed?
3. Where does each analytical responsibility live?
4. What is the next governed analytical operation?

This file is a router and state record. It is not itself a substitute for deep readings, ledgers, monographs, or synthesis.

## 2. Repository and evidence authority

Analytical root: `series/tomozaki/`  
Primary medium: Japanese light novel  
Repository authority: Git for owner-reviewed analytical artifacts under the active repository authority epoch  
Primary/evidence plane: governed Google Drive evidence root  
Series evidence folder ID: `1YldXgz3sglS1CLD_CvUieUM_GOr-VElg` (`Tomozaki`)

The Japanese EPUBs remain outside Git. Git stores analytical interpretation, routing, source-lock metadata, and future derived analytical artifacts.

## 3. Current source boundary

Source lock: [`01 Source Lock and Inventory/TOMOZAKI_SOURCE_LOCK_AND_INVENTORY.md`](01%20Source%20Lock%20and%20Inventory/TOMOZAKI_SOURCE_LOCK_AND_INVENTORY.md)

Current audited inventory, dated 2026-08-29:

- main numbered light novels V01-V11, with no gaps;
- side-story volumes V06.5 and V08.5;
- V07 represented by the acquired Special Edition witness;
- 13 EPUB objects total;
- 13/13 ZIP CRC checks passed;
- 13/13 EPUB container checks passed;
- 11 packaging-conformant under the audit;
- V04 and V11 carry non-blocking `mimetype`-ordering warnings;
- no exact duplicate groups.

This source inventory is **verified**. It does not establish availability or authority for V12+, adaptations, translations, retailer bonuses outside the audited EPUBs, interviews, or reception material.

## 4. Current analytical state

**Volumes 01 through 11 have been read, analyzed, and prospectively frozen. Volumes 06.5 and 08.5 have been read and closed under story-local supplemental routing. V11 is the current numbered-volume boundary. Sequential-source completion is valid; synthesis completion is not. Architecture remediation and cumulative backfill are active.**

Current completed responsibilities:

- analytical methodology: established;
- source inventory and source lock: established;
- V01 sequential deep reading: completed and frozen;
- V02 sequential deep reading: completed and frozen;
- V03 sequential deep reading: completed and frozen;
- V04 sequential deep reading: completed and frozen;
- V05 sequential deep reading: completed and frozen;
- V06 sequential deep reading: completed and frozen;
- V06.5 supplemental reading: placement recorded before prose, completed, and closed;
- V07 sequential deep reading: Special Edition structure segregated, narrative and image layer read, analyzed, and frozen;
- V08 sequential deep reading: package and image layer audited, narrative read in order, all carried claims and questions adjudicated, and post-state frozen;
- V08.5 supplemental reading: metadata/contents placement staged before prose, all stories and images read, mixed chronology adjudicated, alternate/adapted material segregated, and supplemental state closed;
- V09 sequential deep reading: pre-prose freeze staged, package and images audited, narrative read in order, all numbered and supplemental claims adjudicated, and post-state frozen;
- V10 sequential deep reading: pre-prose freeze staged, package and images audited, narrative read in order, all carried claims and questions adjudicated, Nagisa causal limits preserved, and post-state frozen;
- V11 sequential deep reading: pre-prose freeze staged before source access, package and all image layers audited, narrative read in order, all thirty-six carried claims and twelve controlling questions adjudicated, and forty current-boundary claims frozen;
- effort/competition/goal-ownership ledger: canonical and current through V11 for effort regimes, goal origin, stopping conditions, comparative self-worth, capacity governance, viable routes, disclosure authority, and the distinction between retrospective meaning and antecedent control;
- canonical synthesis architecture: established in remediation, lifecycle `EVOLVING`;
- architecture/role-gap audit: current for downstream readiness;
- character-state, relationship-state, claim/revision/evidence, and social-atmosphere/group-systems ledgers: first cumulative remediation backfill authored through V11 and file-locally validated.

Current open responsibilities:

- reconcile the authored cumulative layers against one another and complete the Japanese voice/register layer plus twelve targeted L2/L3 locator queues;
- deepen Tomozaki, Hinami, Kikuchi, and Mimimi to mature literary-monograph responsibility;
- deepen or reclassify the Tama, Mizusawa, and Yuzu candidates according to evidence sufficiency;
- create the mandatory relationship and thematic specialists;
- perform cross-specialist and locator convergence;
- revise the existing full-series synthesis candidate last and then conduct a new release audit.

The seven existing character files and the existing full-series synthesis are preserved as `active_provisional` pre-remediation candidates. They are useful hypothesis and retrieval aids, but their former filenames or claims of completeness do not open the architecture-defined synthesis gate.

V01 was read from audited witness `Bottom-Tier Character Tomozaki - Volume 01.epub`, Drive file ID `1B7r3rf0bIZ1gnFg88NTeDa5K6C4LVlF0`, SHA-256 `49d1577da47a22e0838b8430a52bfe24639effcfb519786149cba7ed1d0bc0c4`.

V02 was read from audited witness `Bottom-Tier Character Tomozaki - Volume 02.epub`, Drive file ID `1kCgzfriuHOjBmDOqsgR0MpLEz3aTqI25`, SHA-256 `9eac14b30b4192e41c901e8194e7ab99e306ef8b6226cf8fa18ee71b75a57c5c`.

V03 was read from audited witness `Bottom-Tier Character Tomozaki - Volume 03.epub`, Drive file ID `1-jH7p1p6e_VntksYmTbWsmLR_PXHOYJz`, SHA-256 `5672493f7007900154601a990bd205c7b24f1d502305dee14d21d4313f2f517d`.

V04 was read from audited witness `Bottom-Tier Character Tomozaki - Volume 04.epub`, Drive file ID `11uMXDm8P_rogddhc2zbFPUCIIzAV96yM`, SHA-256 `7c6425a95c81aa9c917d1437ec1c40ea00011f8e846815f896f4d00303b03c11`. The locked witness retains its non-blocking warning that `mimetype` is stored but is not the first ZIP entry.

V05 was read from audited witness `Bottom-Tier Character Tomozaki - Volume 05.epub`, Drive file ID `1-jxcBWOue222BQgLe_YtCx2b-yxTwgey`, SHA-256 `f43355c286c8b33db529febb6389cb08fa9ef5a65a7e13e3c2a8490214965e89`. The witness is packaging-conformant. Its appended `ふたりのヒミツ` is identified by the afterword as a prior-volume store-purchase bonus and is kept separate from post-V05 progression claims.

V06 was read from audited witness `Bottom-Tier Character Tomozaki - Volume 06.epub`, Drive file ID `1qLaYW6sAB53rRmy9e9JiY5kqYjLVyoea`, SHA-256 `b61815bb4077ce8cd2ae81413580fe3918638814fad55a2593d0327fbd002c43`. The witness is packaging-conformant.

V06.5 was read from audited witness `Bottom-Tier Character Tomozaki - Volume 06.5.epub`, Drive file ID `1OsdRIVq-OlNt5H_IbuWQ520ukjA5ztMs`, SHA-256 `8a5a1eedf1d0ae51d3c0f8a797ee33079139b1a5b0dbbf29a9e4593998fe77dd`. Its package placement was recorded after V06 closed and before any story prose was opened. The witness is packaging-conformant.

V07 was read from audited witness `Bottom-Tier Character Tomozaki - Volume 07 - Special Edition.epub`, Drive file ID `1VEZAtMl5OCikfdXuNFwktUgJAWTelL_-`, SHA-256 `055892e6b5378e0f1df7682a4e53a56ae4c6b67105fcefa771a51da1c899f205`. The witness is packaging-conformant. Its 50-page `FLY mini ART WORKS` block was structurally and visually inspected before narrative reading and remains segregated as edition-specific visual paratext rather than chronology-bearing story evidence.

V08 was read from audited witness `Bottom-Tier Character Tomozaki - Volume 08.epub`, Drive file ID `13BKJFLC8KlyTSTkYqnv7a7O4h0TMGmJi`, SHA-256 `05c238aeb33ed48ffe47ed1c9ba339c6d0e0e2a7b0dd32f78b166f46460de49e`. The witness is packaging-conformant. Its nine image-only front-matter pages and ten inserted main-novel illustrations were inspected; twelve trailing promotional pages remain excluded from narrative evidence.

V08.5 was read from audited witness `Bottom-Tier Character Tomozaki - Volume 08.5.epub`, Drive file ID `1Xqu390B_qO1-Vb6aRiA1Dj8ZWWla7EhJ`, SHA-256 `59862bdcd7f0b885277dd3b6002116fa5b263dfb510089ecbc47fa697628a5dc`. Its package placement was recorded after V08 closed and before any story prose was opened. The witness is packaging-conformant. All 38 image assets were inspected; fourteen trailing promotional pages are excluded from narrative evidence.

V09 was read from audited witness `Bottom-Tier Character Tomozaki - Volume 09.epub`, Drive file ID `16LTaamXaorLJSXLyz_-TyFanr0KDOfIM`, SHA-256 `5740b7a68999f70daee42fd9235d88d68d9911a73dc7c02e59658de49bcf334d`. The witness is packaging-conformant. All 30 JPEG assets were inspected; six front-matter images, ten narrative illustrations, one gaiji image, and twelve trailing promotional images were segregated by function.

V10 was read from audited witness `Bottom-Tier Character Tomozaki - Volume 10.epub`, Drive file ID `13mY73cl9ICy-vPyrOUs5ADEHlxz8Zxw8`, SHA-256 `316d510c2062119a1d3b77e3bb1cb6746340479db07c16579504bd1d5060b2d7`. The witness is packaging-conformant. All 26 JPEG assets were inspected; seven cover/front-matter images, eight narrative illustrations, one gaiji image, and ten trailing promotional images were segregated by function.

V11 was read from audited witness `Bottom-Tier Character Tomozaki - Volume 11.epub`, Drive file ID `15oMprkgH7ZNAeipMu6Ahkcsa7wwCjjFa`, SHA-256 `c8f3fa288d426c0f2c2e2816366df4d636492ff4ec5bcb71d2a7b79bdba12141`. All archive CRC checks passed. The locked witness retains its non-blocking warning that `mimetype` is stored but is not the first ZIP entry. All 28 JPEG assets were inspected and separated into eight cover/front-matter images, ten narrative illustrations, and ten trailing promotional images.

The bounded V03 state establishes that Tomozaki's learned forms have become transferable competence while making **goal ownership**, rather than method naturalness, the central distinction in his conflict with Hinami. He can complete Hinami's assigned fireworks confession but chooses not to because he does not yet own the relationship end. His first correction overshoots into abandoning useful appearance and communication practices; Kikuchi's recipient-specific account then helps him distinguish memorized content that transmits little lived image from practiced form that can accurately carry sincere content. Tomozaki returns with a hybrid model: owned or answerable ends may be pursued through deliberate skill. He uses Hinami's result logic and their Atafami asymmetry to negotiate continuation of coaching under this revised rule.

V03 also adds Mizusawa's effortless-success regime: high social competence and advantageous outcomes can remain experientially external when he does not identify with the goal. His rejected confession to Hinami is painful and clarifying because it is owned. Hinami's result-based confidence, disbelief in stable true desire, and ability to contain direct disclosure pressure become source-grounded, while the origin and final motive of her perfectionism remain open. Tomozaki's bounded-agency development is revised rather than simply strengthened: the Nakamura/Yuzu camp plan reserves final action for Nakamura but relies on deception and control-heavy means. The exact V03 evidence and historical V04 freeze remain in `02 Sequential Readings/TOMOZAKI_V03_DEEP_READING.md`.

V04 confirms that the learned-skill/owned-end hybrid survives ordinary use. Tomozaki can now approve and constrain proposed targets, but Hinami still originates the curriculum, so the coaching relationship is negotiated without becoming equal co-authorship. Yuzu demonstrates that accepting the same burden can be either submission or agency depending on who owns the reason. Tomozaki's first attempt to prove desire's independent value fails because he defends it as a faster route and thereby remains inside Hinami's efficiency criterion.

The volume also exposes the ethical and systemic limits of local optimization. Tomozaki successfully mobilizes Konno's group through inferred care, status insecurity, and romantic interest; the class enjoys a double victory, but later hostility is displaced onto Hirabayashi and then Tama. `空気` is therefore modeled as path-dependent, accumulative, feedback-sensitive, and capable of target substitution. Hinami can calculate emotion, yet her attachment to Tama creates an explicit exception to her ordinary adaptation doctrine. Tama's closing request establishes that chosen self-modification can preserve authenticity when the actor owns the reason. The exact evidence, counterreadings, claim adjudications, abstentions, and V05 freeze are in `02 Sequential Readings/TOMOZAKI_V04_DEEP_READING.md`.

V05 rejects a universal-deficit reading of Tama. Her expressive fundamentals already exceed Tomozaki's; the copied drills fail until the training is rebuilt around her actual strengths, limited curiosity about classmates, recipient fit, settled public character, and the exceptional cost of failure under harassment. The resulting curriculum is genuinely distributed across Tama, Tomozaki, Mizusawa, Takei, Mimimi, and Kikuchi. Tama changes delivery, relational orientation, and public legibility while retaining the governing reason and evaluative core of her action.

The climax tests that distinction. Hinami precisely engineers Konno's overreach and public collapse by using grievance, directional ambiguity, class resentment, and Konno's romantic wound. The class converts justified grievance into licensed retaliation and makes Konno the substitute target. Tama uses her newly trained interface to transmit the same principle she held before training: collective attack remains wrong even when its target has done wrong. The immediate harassment stops and Yuzu helps Konno re-enter ordinary peer life, but no apology, restitution, institutional response, or durable systemic safeguard is shown. V05 therefore establishes cessation and partial repair rather than completed justice.

V05 also retests Mizusawa's owned desire after rejection: he acts, accepts risk, discloses his continuing feeling, and refuses to extract privileged information about Hinami from Tomozaki. Kikuchi's forward movement becomes broader social participation and independent interpretive contribution. Tomozaki functions as a team-supported teacher and leader, wants to know Hinami more deeply, and has not yet demonstrated whether understanding her will include confronting her method. The exact evidence, supplemental routing, claim adjudications, abstentions, and V06 freeze are in `02 Sequential Readings/TOMOZAKI_V05_DEEP_READING.md`.

V06 opens by making calculability a chosen risk policy rather than a competence limit: Hinami has improved enough to take an Atafami game from Tomozaki, but he wins the set by entering states she cannot model and she prefers certain local loss to an uncontrolled gamble. Tomozaki then confronts her V05 method. Hinami agrees that the final blow was unnecessary for cessation and owns it as revenge motivated by love of Tama's unchanged correctness. The admission makes the Tama exception explicit without explaining its origin, reconciling it with doctrine, or supplying apology.

The volume's ordinary state is managed coexistence rather than completed justice. Konno and Akiyama maintain a cold peace through private criticism, while Yuzu absorbs maintenance work and also authors a new public role as festival committee chair. Tomozaki's festival leadership transfers Hinami-taught strategic form into an end he owns: he centers Kikuchi's play, gives her a real opt-out, and translates rather than replaces her authorship. Tama's public character remains usable, variable, and refusible. Tomozaki's growing workload, socially functional self-erasure, and uneven consent in Instagram practice remain live limits.

V06 also separates the romance vectors. Mizusawa continues an owned pursuit of Hinami but does not become the project's ethical authority. Mimimi directly names romantic love for Tomozaki; Tomozaki accepts that the feeling is real but has not answered or selected a direction. Kikuchi advances into public authorship, while Tomozaki's relation to her remains analytically distinct from his curiosity toward Hinami and response obligation toward Mimimi. The exact evidence, all V05 claim adjudications, and the untouched thirteen-question V07 freeze are in `02 Sequential Readings/TOMOZAKI_V06_DEEP_READING.md`.

V06.5 is a mixed-chronology anthology. Retrospective evidence grounds Hinami's middle-school result/self-proof loop without revealing its initiating cause; Kikuchi's image-only May-June diary pages date the growth of shared-literature friendship and authorship; interstitial stories show learned form becoming intuition, Mimimi rediscovering process-valued running, and Mizusawa moving historically from owned waiting to owned pursuit. A V06-concurrent Yuzu story shows real Konno support without apology or restitution. Only the final Mimimi viewpoint directly follows V06: she internally accepts the declaration as love, fears rejection and relationship loss, and still has no chosen action policy or Tomozaki answer. Full story-local routing and epistemic limits are in `02 Sequential Readings/TOMOZAKI_V06_5_SUPPLEMENTAL_READING.md`.

V07 converts the romance curriculum from externally scaffolded exploration into Tomozaki's owned terminal choice. He names Mimimi and Kikuchi as real interests, removes confession from task compliance, and ultimately asks Kikuchi to date him. He does not exploit Mimimi's declaration as validation or select her from gratitude after apparent rejection. Mimimi instead bears a conspicuous cost: she rescues their public comedy performance and later sends Tomozaki back to seek a direct answer from Kikuchi despite knowing that success will close her own route. Her love remains at the volume boundary, and the future friendship cost is unresolved.

Kikuchi retains authorship as the play becomes collective. Her attempted universal sociability reveals that voluntary effort can still be governed by a world-level ideal that excludes the actor. The `炎人` counterexample and her move toward affinity, craft, and `作家志望` establish selected habitat as an alternative to compulsory assimilation. Her public play marries Libra and Alcia; her private novel gives Chris and Libra the intimate ending she wants. Those artifacts expose a continuing public/private split rather than one deterministic fictional prophecy. Tomozaki and Kikuchi's real relationship begins through direct clarification, request, and accepted consent.

The Hinami inquiry adds attributed evidence of deliberate persona construction and a centerless public explanation, but it does not solve her effort origin. A discrepancy between elementary- and middle-school memories of her sisters is left private and unresolved. Alcia is a strong authored model, not direct Hinami autobiography. Tomozaki's festival performance further shows that competence means preparation, delegation, relational support, and recovery: he freezes on stage, accepts Mimimi's rescue, and continues. The exact evidence, all V06 claim adjudications, the Special Edition routing, thirty frozen V07 claims, and fifteen V08 tests are in `02 Sequential Readings/TOMOZAKI_V07_DEEP_READING.md`.

V08 opens a self-authored long-term direction while refusing to confuse desire with feasibility. Offline Atafami shows Tomozaki a community and professional ecosystem; Ashigaru's tournament-format test distinguishes aggregate technical superiority from action under one consequential opportunity. Tomozaki owns the aim of professional play, but income, university, parental support, tournament record, and an exit rule remain unsettled. His `self-search alliance` is likewise owned in purpose even though it incidentally satisfies Hinami's assigned group task. Hinami's own contrast sharpens: Atafami elicits direct enjoyment and frustration, while her prestigious education-and-career route remains detailed but desire-poor.

The new relationship fails its first maintenance test through accumulation rather than lack of affection. Kikuchi repeatedly asks for time, information, and touch; Tomozaki repeatedly fits her around gaming, work, and group obligations. He refuses Rena's sexual proposition but leaves the adult player's sexualized access unbounded and gives Kikuchi a materially incomplete account. V08 ends when Kikuchi sees a notification referring to the concealed sexual call. This proves a disclosure failure, not an affair, and the source stops before explanation or repair. The exact evidence, all V07 claim adjudications, thirty-two frozen V08 claims, and the V08.5 placement burden are in `02 Sequential Readings/TOMOZAKI_V08_DEEP_READING.md`.

V08.5 does not cross that endpoint. Three numbered stories occupy the V07-V08 winter interlude: they establish early reciprocal scheduling in Tomozaki and Kikuchi's relationship, Kikuchi's knowledge of Mimimi's confession, and the guarded sister inquiry before the V08 first date. Hinami's pre-series retrospective directly establishes two younger sisters, Nagisa and Haruka; Nagisa is absent by middle school, but her fate and the causal mechanism remain unstated. The same story links Hinami's national-second-place basketball defeat, unequal team-goal ownership, Haruka-mediated Atafami enjoyment, individually measurable proof, first defeat by nanashi, and adoption of `NO NAME`. Rena's retrospective grounds her attention/status regime without excusing its ethics. The afterword identifies the karaoke story as parallel and the VR bonus as a drama-CD rewrite, so both remain outside main-continuity progression. Full routing, claims, and abstentions are in `02 Sequential Readings/TOMOZAKI_V08_5_SUPPLEMENTAL_READING.md`.

V09 resolves the notification as a multi-part disclosure, priority, and boundary conflict rather than an affair. Tomozaki and Kikuchi move from local apology through painful disclosure to mutual selection, treating specialness as a history they must build rather than a compatibility fact proved before dating. Mimimi makes her no-wrongdoing limit concrete by ending their habitual walk, then prevents Tomozaki from solving the conflict through wholesale social self-amputation. Rena escalates after a narrow message boundary; Tomozaki refuses the immediate proposition and touch, but no durable contact policy is established.

The volume also reclassifies Tomozaki's self-concept and Hinami's coaching. Ashigaru identifies reason-independent change-readiness as Tomozaki's strong-character capacity, while Hinami directly treats reasonless action as nearly unintelligible. Tomozaki abandons the assigned group-center goal, sets professional-game milestones, begins a Found-to-Jack experiment, and owns `knowing Hinami` as a life goal. With Kikuchi's inquiry, he identifies the coaching project as a reproducibility test of Hinami's life method; Hinami tacitly confirms the central insight. That does not prove a single motive, romance, consent to rescue, or any missing-sister cause. Full evidence, all prior adjudications, thirty-six frozen claims, and the V10 burden are in `02 Sequential Readings/TOMOZAKI_V09_DEEP_READING.md`.

V10 tests whether care can reach Hinami without converting her into an object of cure. Her friends use ordinary birthday forms, remembered food, play, and distributed testimony to produce reactions she cannot wholly precompute. Tomozaki and Kikuchi integrate their relationship into that peer and game-professional world, name jealousy directly, and collaborate despite visible cost. Tomozaki also tells Mizusawa Hinami's private coaching history without permission, explicitly recognizing the act as a rights violation; later voluntary disclosure by Hinami remains analytically distinct.

Hinami directly states that middle sister Nagisa opposed bullying in sixth grade, entered an unmarked road, was struck, and died. She cannot know whether the entry was accidental or intentional, so the event gives her a certain result without a usable cause, regret, or counterfactual lesson. This sharpens the proof/reason structure without authorizing a suicide finding or a single-cause account of Hinami. The Endo barter gives Tomozaki a six-month promotional obligation and three-month follower target, creating the first sponsor-like professional experiment. V10 ends when a family birthday video begins, before the message or aftermath. Full evidence, adjudications, thirty-six frozen claims, and the V11 burden are in `02 Sequential Readings/TOMOZAKI_V10_DEEP_READING.md`.

V11 shows that Hinami's family did not simply neglect meaning. Her mother Yoko filled the household with affirmation and retrospectively organized events as meaningful; the birthday video praises Aoi by turning a childhood marathon and later national running result into a destiny-like continuity. Nagisa's death makes that inherited account intolerable: Yoko again says the world chose the result and that it has meaning, while Aoi experiences the framework as false. Hinami's later demand for controllable antecedent cause, measurable proof, and victory is therefore a strong formation response without becoming a sufficient explanation of every trait. Nagisa's intent remains unresolved, and neither the private practice nor the family's language licenses a religious or cult identification.

The present crisis separates capacity from reason. Hinami withdraws from spring break, school, and the student council without handoff, yet retains elite Atafami competence. Tomozaki understands much of the formation history but converts that understanding into a unilateral credential claim: she should trust him because she cannot beat `nanashi`. Hinami studies his secondary character, reverses an 0-2 set, defeats him 3-2, and calls life a bad game. The victory invalidates his proposed authority; it does not establish that her crisis judgment is the series' final ontology. Tomozaki then loses his own reason to play and withdraws, exposing a parallel between method and motive.

Kikuchi's fiction reaches Tomozaki where direct speech fails. A conditional publication opportunity for `純混血とアイスクリーム` forces her to ask why she writes and whether insight grants permission to use another person's pain. Tomozaki and Kikuchi reselect the relationship, and the peer group proposes a collective narrative project for Hinami. At the boundary the project has not been executed, Hinami has not consented to it, Mizusawa has not confessed, and no cure or return is shown. Jack's fourth-place offline tournament finish is real route evidence without closing Tomozaki's professional feasibility question. Full evidence, all thirty-six V10 claim adjudications, all twelve V11 question adjudications, forty frozen V11 claims, and the current abstentions are in `02 Sequential Readings/TOMOZAKI_V11_DEEP_READING.md`.

No Tomozaki character is currently enrolled in the canonical character registry. Character discovery is maintained independently by the designated curation agent through `characters/registry.jsonl` and generated `CHARACTER_ANALYSIS_INDEX.md`. This analytical branch does not create character upsert inputs or independently edit either character output. Eligible distributed character analysis through V11 may be discovered after merge by the curation agent, provided no existing character reference is invalidated.

## 5. Architecture

### `00 Frameworks and Methods/`
Canonical paired foundation: source-facing analytical method plus corpus/synthesis architecture.

Current artifact:

- `TOMOZAKI_ANALYTICAL_METHOD.md`
- `TOMOZAKI_SYNTHESIS_ARCHITECTURE.md` — canonical `EVOLVING` architecture; records the historical gate violation, cumulative responsibilities, evidence routing, dependencies, and completion gates

### `01 Source Lock and Inventory/`
Exact primary-source boundary, audited witness identity, source integrity, exclusions, and future source-lock revision rules.

Current artifact:

- `TOMOZAKI_SOURCE_LOCK_AND_INVENTORY.md`

### `02 Sequential Readings/`
Canonical home for volume-by-volume source-facing deep readings and bounded prospective freezes.

Current artifacts:

- `README.md`
- `TOMOZAKI_V01_DEEP_READING.md` — V01 closed/frozen
- `TOMOZAKI_V02_DEEP_READING.md` — V02 closed/frozen
- `TOMOZAKI_V03_DEEP_READING.md` — V03 closed/frozen
- `TOMOZAKI_V04_DEEP_READING.md` — V04 closed/frozen
- `TOMOZAKI_V05_DEEP_READING.md` — V05 closed/frozen
- `TOMOZAKI_V06_DEEP_READING.md` — V06 closed/frozen
- `TOMOZAKI_V06_5_SUPPLEMENTAL_READING.md` — V06.5 routed and closed
- `TOMOZAKI_V07_DEEP_READING.md` — V07 closed/frozen; Special Edition paratext segregated
- `TOMOZAKI_V08_DEEP_READING.md` — V08 closed/frozen; image and trailing promotional layers segregated
- `TOMOZAKI_V08_5_SUPPLEMENTAL_READING.md` — V08.5 routed and closed; parallel and adapted bonus layers segregated
- `TOMOZAKI_V09_DEEP_READING.md` — V09 closed/frozen; image, gaiji, and trailing promotional layers segregated
- `TOMOZAKI_V10_DEEP_READING.md` — V10 closed/frozen; Nagisa disclosure and family-video endpoint causally bounded
- `TOMOZAKI_V11_DEEP_READING.md` — V11 closed/frozen; family formation evidence, crisis, game result, and proposed intervention bounded

### `03 Longitudinal Ledgers/`
Canonical home for recurring cross-volume questions once repetition creates a real retrieval/revision need.

Current artifacts:

- `README.md`
- `TOMOZAKI_EFFORT_COMPETITION_AND_GOAL_OWNERSHIP_LEDGER.md` — current through V11
- `TOMOZAKI_CHARACTER_STATE_LEDGER.md` — canonical remediation backfill; time-indexed character state through V11
- `TOMOZAKI_RELATIONSHIP_STATE_LEDGER.md` — canonical remediation backfill; directional relationship/network state through V11
- `TOMOZAKI_CLAIM_REVISION_AND_EVIDENCE_INDEX.md` — canonical L1 crosswalk of the 319-claim/140-question universe, with promoted/local coverage accounting and twelve targeted L2/L3 escalation queues
- `TOMOZAKI_SOCIAL_ATMOSPHERE_AND_GROUP_SYSTEMS_LEDGER.md` — canonical remediation backfill for `空気`, status, reputation, punishment, facilitation, repair, and distributed intervention through V11

Mandatory next cumulative artifact:

- `TOMOZAKI_JAPANESE_VOICE_REGISTER_AND_KEY_TERMS_LEDGER.md`

The effort ledger remains deliberately narrow and canonical. The new ledgers complement it; they do not regenerate or summarize it away. The voice/register layer will require targeted Japanese-source escalation where the readings do not retain sufficient local speech evidence.

### `04 Character Analysis/`
Canonical home for source-grounded character modeling after sufficient longitudinal evidence accumulates.

Current artifacts:

- `README.md`
- `Tomozaki Fumiya/TOMOZAKI_FUMIYA_CHARACTER_MONOGRAPH.md`
- `Hinami Aoi/HINAMI_AOI_CHARACTER_MONOGRAPH.md`
- `Kikuchi Fuka/KIKUCHI_FUKA_CHARACTER_MONOGRAPH.md`
- `Nanami Minami/NANAMI_MINAMI_CHARACTER_MONOGRAPH.md`
- `Natsubayashi Hanabi/NATSUBAYASHI_HANABI_CHARACTER_MONOGRAPH.md`
- `Mizusawa Takahiro/MIZUSAWA_TAKAHIRO_CHARACTER_MONOGRAPH.md`
- `Izumi Yuzu/IZUMI_YUZU_CHARACTER_MONOGRAPH.md`

These seven artifacts are pre-remediation candidates, all currently `active_provisional`. Tomozaki and Hinami are first-priority deep monographs; Kikuchi and Mimimi follow. Tama, Mizusawa, and Yuzu require either substantial deepening or explicit bounded-dossier scope. Relationship and whole-corpus responsibilities cannot be delegated to these individual files.

### `05 Full-Series Synthesis/`
Canonical home for whole-corpus integration only after the longitudinal, character, relationship, specialist, and convergence gates pass.

Current artifact:

- `TOMOZAKI_FULL_SERIES_SYNTHESIS.md` — preserved `active_provisional` pre-remediation synthesis candidate; not mature final authority and not to be rewritten until specialist convergence

### `06 Specialist Synthesis/`
Architecture-defined future home for relationship and thematic literary synthesis. The directory remains uninstantiated until the first specialist is drafted. Mandatory responsibilities are enumerated in `TOMOZAKI_SYNTHESIS_ARCHITECTURE.md`.

### `07 Character Reconstruction Models/`
Deferred future home for simulation-oriented derived-use models. No model is authorized until literary authority converges; future models must declare that they are not primary literary authority.

### `08 Audits and Manifests/`
Canonical home for title-local audit and manifest artifacts whose responsibility is provenance, path/state closure, or validation rather than interpretation.

Current artifact:

- `TOMOZAKI_BOOTSTRAP_PATH_MANIFEST.json`
- `TOMOZAKI_ARCHITECTURE_AND_SYNTHESIS_ROLE_GAP_AUDIT.md` — current architecture and downstream-readiness authority
- `TOMOZAKI_FULL_SERIES_SYNTHESIS_VALIDATION_AUDIT.md` — immutable pre-remediation checkpoint; source-coverage findings remain useful, but its architecture-closure conclusion is superseded by the role-gap audit

### `.repository/`
Declarative routing inputs consumed by the bounded global-index housekeeping workflow.

Current artifact:

- `series-registry.json`

Directory `90` remains intentionally absent. Directories `06` and `07` now have architecture-defined future responsibilities but remain uninstantiated until their dependency gates open.

## 6. Current-boundary analytical questions after V11

V11 closes the present source boundary while deliberately leaving several active questions:

- Will the proposed collective narrative project be executed, and can it obtain Hinami's consent without turning understanding into authority over her?
- Can Hinami distinguish rejecting her inherited retrospective-meaning system from having no affirmative reason of her own?
- Can Tomozaki recover an owned reason to play after losing the `nanashi` credential on which he based his rescue claim?
- Does Hinami return to school, the student council, friendship, or coaching, and under what terms?
- Can Haruka's admiration become self-authored rather than dependent on Aoi as a perfect example?
- How will Kikuchi govern motive, consent, fictionalization, and possible publication when her writing uses another person's pain?
- Can Tomozaki and Kikuchi sustain their renewed relationship through allocation, privacy, third-party access, and unequal intervention costs?
- Does Mizusawa confess, what response does he receive, and what stopping condition follows?
- Do Tomozaki's Endo promotion and Jack experiment produce durable professional evidence beyond one fourth-place tournament finish?
- Do Mimimi's romantic stopping rule, Yuzu's absorber limit, Rena's durable boundary compliance, or Konno/Akiyama accountability move?
- Will the series preserve the distinction between explanatory formation and exhaustive causal reduction?
- Does a later volume revise the competing claims that life is a learnable game and that life is a bad game, or keep both as bounded character theories?

Sections 8-10 of the V11 deep reading contain the controlling numbered claim state, questions, and abstentions for any later source expansion. Both side-story volumes remain separately routed historical evidence layers and must not be converted into actor knowledge.

## 7. Main reading order and side-story control

The default prospective main chain is:

`V01 → V02 → V03 → V04 → V05 → V06 → V07 → V08 → V09 → V10 → V11`

Current position: **V01-V11 complete; V06.5 and V08.5 routed and closed; the post-V11 numbered freeze is the active current boundary.** Preserve every earlier numbered freeze and both story-local supplemental layers if a later numbered volume is admitted.

Volumes V06.5 and V08.5 are inside the source lock but outside that simple integer-numbered chain. V06.5 is integrated as a publication-order supplement after V06 with story-local diegetic placement; only its tenth unit directly advances the post-V06 state. V08.5 is integrated after V08 as a mixed-chronology supplement; none of its units advances beyond the V08 endpoint, and its parallel/adapted units remain segregated.

Do not use side-story evidence retroactively to rewrite earlier predictions.

## 8. Work order

Current remediation order:

1. reconcile the four authored remediation ledgers with the pre-existing effort ledger and current map;
2. perform selective Japanese-source escalation, discharge the twelve indexed L2/L3 queues in proportion to risk, and build the voice/register/key-terms ledger;
3. deepen Tomozaki and Hinami, then Kikuchi and Mimimi; deepen or reclassify Tama, Mizusawa, and Yuzu;
4. build Tomozaki/Hinami, Tomozaki/Kikuchi, and Tomozaki/Mimimi relationship syntheses plus the mandatory thematic specialists;
5. perform adversarial claim/locator and cross-specialist convergence audits;
6. substantially revise the full-series synthesis last;
7. run the literary validation/release audit;
8. consider derived reconstruction models only after the literary corpus passes.

If a later numbered volume is admitted before remediation finishes, revise the source lock, preserve all existing freezes, stage the next pre-prose freeze from V11 before source access, and then update every affected cumulative layer. New source work does not erase the remediation dependency chain.


## 9. Current abstentions

At the current V11 boundary this project deliberately does **not** claim:

- a definitive ending or post-V11 state for Tomozaki, Hinami, Mimimi, Tama, Kikuchi, or any other character;
- that the birthday trip saves, cures, diagnoses, permanently changes, or obtains full access to Hinami;
- that Hinami accepted Tomozaki's help, resumed coaching, forgave unauthorized disclosure, or authorized anyone else to know her history;
- that `NO NAME` is Hinami's complete true self or that spontaneous affect is necessarily more authentic than controlled affect;
- that Nagisa intentionally died, died only by accident, experienced a named medical event, left a note, or disclosed intent;
- a precise date, location, bullying sequence, legally responsible actor, or complete family response to Nagisa's death;
- that bullying or any named person singularly caused the collision;
- that Nagisa's death singularly caused Hinami's proof system, masks, effort, coaching, Atafami attachment, isolation, or every later decision;
- that Hinami's permanent uncertainty can be resolved by analyst inference;
- that the three Found mugs are definitively for all three sisters or establish a memorial ritual;
- that the family video, Yoko's language, or Nagisa's death supplies a single sufficient cause of Hinami's present personality;
- that Yoko's private practice, vocabulary, or affirmational household establishes a religion, cult, diagnosis, or abusive intent;
- that Hinami's withdrawal is permanent, that Tomozaki's intervention cures her, or that the proposed collective narrative project has been executed or consented to;
- that Tomozaki's disclosure to Mizusawa was authorized, harmless, necessary, vindicated by outcomes, or ethically complete;
- that specialness, love, trust, or willingness to bear responsibility transfers ownership of another person's secret;
- that Tomozaki is romantically in love with Hinami, permanently non-romantic toward her, jealous of Mizusawa, or destined to pair with either girl;
- that Tomozaki and Kikuchi are permanently stable, conflict-free, or governed by exhaustive privacy, allocation, disclosure, sexual, or third-party rules;
- that Kikuchi's cooperation erases jealousy, waives future interests, or obligates continued permission;
- that Mimimi has stopped loving Tomozaki, resumed private routine, will wait indefinitely, intends interference, or has a complete stopping rule;
- that Rena has durably reformed or respects consent, relationship, age, message, or contact boundaries because Tomozaki removes her touch and Kikuchi objects;
- that Mizusawa's delayed opportunity is withdrawal, surrender, or a terminal pursuit rule;
- that Yuzu's facilitation is costless or establishes her absorber limit;
- that Konno or Akiyama acknowledged harm, offered restitution, or adopted durable accountability;
- that the commissioned game is commercially licensed or distributable beyond the described private use;
- that the promotional barter proves professional status, sponsorship income, sustainable economics, advertising compliance, or a viable career;
- that the three-month follower promise succeeds or the agreement has adequate written and termination protections;
- that Tomozaki completed equipment acquisition, tournament transfer, family negotiation, university comparison, or a professional exit condition;
- that Jack's fourth-place offline finish establishes professional viability, completes the Found-to-Jack experiment, or durably changes Tomozaki's main-character decision;
- that Mizusawa selected a permanent career or can monetize negotiation skill sustainably;
- that Tama will inherit the family shop or that one cake settles vocational ownership;
- that form is always sincere, always manipulative, or sufficient regardless of motive and consequence;
- that beneficial outcomes excuse instrumental, coercive, or concealed methods;
- that relationship-as-coauthored-practice, care-as-disruption, or form-as-medium is universally correct;
- that V08.5 reader knowledge is automatically available to numbered-volume actors;
- a PACTRIH score, comparative-ethics placement, or adaptation comparison;
- a complete series source boundary beyond V11;
- that the seven provisional character-study candidates exhaust every meaningful character, already satisfy mature-monograph responsibility, require monographs for supporting figures, or make a global character-enrollment decision; or
- any V12+, adaptation, translation, reception, or external-authority conclusion.

Those claims require later source-grounded work.

## 10. Current next action

**Reconcile the completed first-wave ledgers, then perform the targeted Japanese-source pass needed for the voice/register/key-terms ledger and the twelve L2/L3 locator queues. Do not revise the final synthesis yet. No broad primary-source reread is authorized.**
