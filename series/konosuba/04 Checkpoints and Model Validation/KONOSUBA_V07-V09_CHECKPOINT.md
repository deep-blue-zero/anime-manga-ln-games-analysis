---
series: KONOSUBA
artifact_type: checkpoint
scope: V07-V09
generation: MODEL_GEN_0.3
status: active_provisional
source_boundary: 'Japanese main-series V01–V09 main narrative; Model Gen 0.2 tested on V07–V09; Gen 0.3 and V10–V12 predictions frozen before V10 exposure; no side-source narrative used'
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
---

# KONOSUBA V07–V09 Checkpoint — Model Generation 0.3

## 1. Checkpoint responsibility, authority and evidence boundary

This checkpoint closes the **V07–V09 prospective tranche against the unchanged Gen 0.2 model** and freezes Gen 0.3 for V10–V12. It was delivered as a canonical candidate for `series/konosuba/04 Checkpoints and Model Validation/`, produced by an analyst without Git or Drive write authority. The producer inspected a V01–V08 repository boundary. The receiving integration accepts this checkpoint and advances the corpus map through V09, while retaining the model's provisional maturity. No full-series or post-side-source validation claim is made. See the [receiving review](../09%20Audits%20and%20Manifests/KONOSUBA_V09_RECEIVING_REVIEW.md) for review scope, source correction RC-V09-01, preservation checks and deferred obligations. Complete-reading and freeze-time statements below describe the producer session; the receiver performed bounded primary verification.

The starting authority was inspected at `deep-blue-zero/anime-manga-ln-games-analysis`, main commit `317f04a8549e9801dfe041cbd098025e3c47d87e`. The registry and `CURRENT_STATE_AND_CORPUS_MAP.md` confirmed V09 next, Gen 0.2 frozen and no existing V07–V09 checkpoint. All four KonoSuba methods, source lock/inventory, V04–V06 checkpoint, V07/V08 readings and ten ledgers were inspected before V09 source exposure. The primary V09 EPUB is `Konosuba - Main Series - Volume 09.epub`, Drive ID `1lIWNDsqZT9NQcoHa_ZRSqUS4j7HzYc-j`, 3,086,699 bytes, SHA-256 `a81499cd61dda060503d35d68db71c2bdc9e12e782412cf3724bca25a7f28f0e`. It matched the expected hash and passed the EPUB/ZIP, language and structure checks.

The V09 prose was read completely in sequence: prologue, Chapters 1–4, final chapter and both epilogues, `OEBPS/Text/part0009.xhtml` through `part0016.xhtml`. Afterword, ebook bonus, popularity appendix, ads and other paratext are excluded. Illustrations were not visually analyzed. Earlier-volume evidence here comes from the canonical checkpoint/readings/ledgers, not a fresh rereading of those earlier EPUBs. No V10, side narrative, adaptation, wiki, summary or future event was used.

### Locator and historical-reference conventions

V09 shorthand **Pr/C1/C2/C3/C4/F/Ep1/Ep2** maps respectively to `part0009/0010/0011/0012/0013/0014/0015/0016.xhtml` under `OEBPS/Text/`. P#### counts every body `<p>` in order, including blank and image-only paragraphs. For example, **F P0534–0544** identifies the final thanks/attack sequence. These are reproducible XHTML paragraphs, not rendered page numbers. The full source map and extraction limits appear in the companion V09 deep reading §1.

**V07/V08 + an MG02 ID** refers to the unchanged row in that volume's prospective addendum within `KONOSUBA_MODEL_PREDICTION_VALIDATION_LEDGER.md`, read together with its corresponding deep reading. **DISC-V07/08** refers to the existing discovery entry there. This identifies the canonical source of inherited evidence and prevents pretending it was newly verified against earlier Japanese wording in this session.

### Freeze integrity inherited from Gen 0.2

The original ledger states that Gen 0.2 was written after V06 and before V07 exposure. The exact frozen section was read and preserved before V09 at `2026-10-08T03:41:57.058948+00:00`.

| Integrity item | Value |
|---|---|
| Baseline full prediction-ledger Git blob | `1c5444ee1ab3b9b6157eea5c7161c890c4b2048e` |
| Baseline full prediction-ledger SHA-256 | `cee29031e919903f077c553b3a83f2d0b5ac79eb9e78e643ff62abc186beb2fb` |
| Frozen Gen02 section SHA-256 | `7f14063864e5d1ce090d6c271dc5696d969bef1db50c31770191ce19268a7440` |
| Frozen section bytes | 13,521 |
| Exact start / exclusive end | `# Model Generation 0.2 — Frozen Predictions for V07–V09` / `# V07 Prospective-Validation Addendum` |

The frozen text, including historical absent-V07/unexposed-volume statements, is not rewritten. All Gen 0.1 predictions and past adjudications remain untouched too. This receipt establishes preservation during this session; it does not independently certify the original historical freeze beyond the pinned canonical record, nor claim that a pretrained model has no prior latent series knowledge.

## 2. Gen 0.2 tranche scorecard and confidence disposition

### 2.1 What the whole-prediction counts do and do not say

| Scope | CONFIRMED | PARTIAL | NOT_TESTED | AMBIGUOUS | Whole-prediction FALSIFIED |
|---|---:|---:|---:|---:|---:|
| V09 alone | 8 | 7 | 6 | 1 | 0 |
| V07–V09 tranche | 13 | 5 | 3 | 1 | 0 |

These counts use **all 22 frozen predictions as the denominator**, preserve incomplete compound branches and are not a performance percentage. M02 contains a clear **local failed prediction**: explicit money and labor cost does not prevent Megumin from discarding the item; she maintains her rejection after its expedition purpose and possible utility are discussed. M04 contains adverse bodily collateral whose exact serious-harm trigger match remains unresolved. E01's broad necessity wording requires revision. A zero in the final column must not be described as “no failures.”

The table below copies all **44 V07/V08 outcome cells verbatim** from the baseline. Their wording, including branch-limited confirmations and stronger modifiers, is historical evidence. The more conservative tranche adjudications do not retroactively replace those original labels.

### 2.2 Every frozen prediction across the tranche

| Prediction | V07 outcome — preserved | V08 outcome — preserved | V09 | Tranche | Claim transition |
|---|---|---|---|---|---|
| MG02-K01 | **CONFIRMED strongly** | **CONFIRMED strongly** | **CONFIRMED** | **CONFIRMED** | STRENGTHEN |
| MG02-K02 | **CONFIRMED strongly** | **CONFIRMED strongly** | **CONFIRMED** | **CONFIRMED** | STRENGTHEN |
| MG02-K03 | **PARTIAL SUPPORT** | **CONFIRMED / STRENGTHEN** | **PARTIAL** | **CONFIRMED** | PRESERVE |
| MG02-K04 | **CONFIRMED strongly** | **NOT_TESTED** | **NOT_TESTED** | **CONFIRMED** | PRESERVE |
| MG02-A01 | **CONFIRMED very strongly** | **CONFIRMED strongly** | **PARTIAL** | **CONFIRMED** | PRESERVE; new domain discovery |
| MG02-A02 | **CONFIRMED strongly** | **CONFIRMED very strongly** | **CONFIRMED** | **CONFIRMED** | STRENGTHEN; REVISE broad extrapolation |
| MG02-A03 | **NOT_TESTED cleanly** | **CONFIRMED - selective-learning/state-defense pattern** | **PARTIAL** | **PARTIAL** | REVISE / OPEN |
| MG02-A04 | **NOT_TESTED cleanly** | **NOT_TESTED** | **NOT_TESTED** | **NOT_TESTED** | OPEN |
| MG02-M01 | **CONFIRMED — Trigger A branch** | **PARTIAL SUPPORT** | **PARTIAL** | **PARTIAL** | STRENGTHEN A / OPEN B |
| MG02-M02 | **PARTIAL SUPPORT** | **NOT_TESTED** | **PARTIAL** | **PARTIAL** | REVISE / DOWNGRADE |
| MG02-M03 | **CONFIRMED strongly** | **NOT_TESTED; inverse-condition support** | **CONFIRMED** | **CONFIRMED** | STRENGTHEN |
| MG02-M04 | **NOT_TESTED** | **NOT_TESTED** | **AMBIGUOUS** | **AMBIGUOUS** | DOWNGRADE / OPEN |
| MG02-D01 | **CONFIRMED strongly** | **CONFIRMED** | **CONFIRMED** | **CONFIRMED** | STRENGTHEN |
| MG02-D02 | **CONFIRMED strongly for belonging branch** | **CONFIRMED strongly for meaning-sensitive branch** | **PARTIAL** | **PARTIAL** | STRENGTHEN components / OPEN comparison |
| MG02-D03 | **CONFIRMED strongly** | **CONFIRMED strongly** | **CONFIRMED** | **CONFIRMED** | STRENGTHEN |
| MG02-D04 | **CONFIRMED very strongly** | **NOT_TESTED** | **NOT_TESTED** | **CONFIRMED** | PRESERVE |
| MG02-E01 | **CONFIRMED strongly** | **CONFIRMED strongly** | **PARTIAL** | **PARTIAL** | REVISE |
| MG02-E02 | **CONFIRMED very strongly** | **NOT_TESTED** | **NOT_TESTED** | **CONFIRMED** | PRESERVE |
| MG02-J01 | **CONFIRMED strongly** | **CONFIRMED strongly** | **CONFIRMED** | **CONFIRMED** | STRENGTHEN |
| MG02-J02 | **CONFIRMED at V07 level** | **CONFIRMED at V08 level** | **CONFIRMED** | **CONFIRMED** | STRENGTHEN qualitative support |
| MG02-I01 | **NOT_TESTED** | **NOT_TESTED** | **NOT_TESTED** | **NOT_TESTED** | OPEN |
| MG02-I02 | **NOT_TESTED** | **NOT_TESTED** | **NOT_TESTED** | **NOT_TESTED** | OPEN |

### 2.3 Confidence changes and failure diagnoses

Confidence is attached to a particular mechanism or branch. Missing a trigger gives no new validation gain but does not automatically refute an inherited claim. New bounded models can remain strong while a broader former formulation is downgraded.

| Prediction | Confidence disposition | Failure diagnosis / coverage limit |
|---|---|---|
| MG02-K01 | HIGH → HIGH | No matched failure of indirect search. Missing opponent information defeats an early plan; preparedness and complete forecasting are separate from inventive capacity. |
| MG02-K02 | HIGH → HIGH | Commitment precedes assured solvability. Risk calculation and later incentives coexist with care; no abandonment for comfort in a clean entrusted-duty case. |
| MG02-K03 | MODERATE-HIGH → MODERATE-HIGH | V08 supplies the cleaner prospective match. Do not rename every successful raid, forgotten item or later danger as recognition-caused overextension. |
| MG02-K04 | HIGH → HIGH; no V09 gain | Missing trigger in V09; the genuine V07 resignation/marriage case remains the matched evidence. |
| MG02-A01 | HIGH → HIGH | Domain/activation qualification. Sleeping delays deployment; the full ambush also fails through status drift. V07/V08 independently confirm the original institutional-domain condition. |
| MG02-A02 | HIGH → HIGH, conditional on reward alignment | Goal substitution is directly supported. The failed generalization is that praise itself necessarily produces failure; task-aligned recognition is a strong countercondition. |
| MG02-A03 | MODERATE-HIGH → MODERATE for complete causal rule | Selective learning/state defense survives from V08. External direction, skill enjoyment and role ownership compete with the proposed internal accountability mechanism. Remediation is not proof of accepted blame. |
| MG02-A04 | MODERATE → MODERATE; unvalidated | Missing conjuncts: persistently low-valued duty plus attractive maximal alternative. No confirmation or falsification by analogy. |
| MG02-M01 | A HIGH → HIGH; B MODERATE-HIGH inherited | Compound prediction: A is replicated; B is not tested in this tranche. Do not substitute target-specific grief for build-abandonment evidence. |
| MG02-M02 | MODERATE-HIGH → MODERATE for broad cost rule | Missing identity/stake variable: core-specialty defense defeats ordinary companion-cost restraint. The full disconfirmation clause asks for repeated uncontrolled cases; V07 also preserves partial redirection. PARTIAL must not hide the local failure. |
| MG02-M03 | HIGH → HIGH | Tactical suitability is supported; ethical adequacy and larger-goal discipline are separate. The ally-blasting contest is not a positive safe-separation test. |
| MG02-M04 | MODERATE-HIGH → MODERATE | Actual collateral cannot be discarded as a gag. Wolbach is a valued benefactor/opponent, not a current companion directly harmed by the tactical shot; that inhibition is a new related discovery, not a rescued confirmation. |
| MG02-D01 | HIGH → HIGH | Costly protective action is directly observed. Her fantasy-driven delay and later narrator dismissal do not erase it or establish universal sound judgment. |
| MG02-D02 | Belonging HIGH → HIGH; comparison MODERATE → MODERATE | V07 tests belonging strongly; V08/V09 test meaning and agency. The exact comparative pain claim remains less isolated than those supported components. |
| MG02-D03 | HIGH → HIGH, with finite durability | Equipment/opponent-force limit, not sabotage or zero usefulness. Do not invent individual unseen feats in the general fortress fighting. |
| MG02-D04 | MODERATE-HIGH → MODERATE-HIGH; no V09 gain | Missing exact trigger. V07 remains the direct matched case; duty alone must not be inflated into permanent identity separation. |
| MG02-E01 | Necessity HIGH → MODERATE; bounded deployment HIGH | An unqualified necessity theorem is too broad. Do not redefine success after the fact to erase the adverse case. Gen03 separately tracks target destruction, safe deployment, goal completion and ethics. |
| MG02-E02 | HIGH → HIGH; no V09 gain | Missing trigger; accepting temporary deployment is compatible with resisting permanent relationship loss. V07 remains the direct prospective test. |
| MG02-J01 | HIGH → HIGH | Preserve independent role evidence and speaker/addressee context; no personality inference from an isolated particle and no role invented only after reading the line. |
| MG02-J02 | MODERATE-HIGH → MODERATE-HIGH | Qualitative major-sequence judgment, not an exhaustive joke census or percentage. Japanese importance does not automatically imply Japanese-only form dependence. |
| MG02-I01 | MODERATE-HIGH inherited; no tranche gain | Missing trigger; a mentioned character is not necessarily an observed behavioral test. |
| MG02-I02 | MODERATE-HIGH inherited; no tranche gain | Missing motive/decision evidence. Do not import a future journey or infer an unwanted engagement to manufacture a test. |

### 2.4 Evidence adjudication behind the revision-bearing rows

**M02 is a real negative case.** Kazuma is an established valued companion. He states the money and labor cost before Megumin discards the item. He then explains its expedition purpose; she acknowledges potential utility but maintains her rejection. Kazuma subsequently detonates the discarded item (V09 C2 P0599–0615). The frozen trigger says “concrete cost,” not only bodily harm. Adding a bodily-harm requirement now would rewrite the test. The whole prediction remains PARTIAL because its possibility/repeated-disconfirmation wording and V07 partial redirection do not justify rejecting all regulatory capacity. The companion-cost brake is nevertheless unreliable under a directly challenged core specialty. (V09 C2 P0592–0606; unchanged MG02-M02; V07 M02.)

**M04 must not be rescued by changing the relationship category.** The contest's Explosion blasts companions away and leaves Darkness unconscious without expressed hesitation. That is adverse evidence. The full original conjunction—best tactical Explosion use, valued companion and serious harm—is not cleanly isolated. Her anticipation of harm is an explanatory uncertainty, not an added condition in the frozen trigger. Wolbach-related hesitation is powerful new evidence for a valued-target mechanism, but a benefactor/opponent is not the literal companion-friendly-fire condition. AMBIGUOUS keeps both facts visible. (V09 C2 P0235–0271; C4 P0206–0208; F P0007–0015, P0365–0419; unchanged MG02-M04.)

**E01's unqualified necessity claim cannot be protected by a new success definition.** The major siege supports role/target/sequence organization strongly, and its providers are distributed. The earlier contest also ends in enemy destruction after Megumin interrupts a cooperative plan, at friendly cost. The frozen sentence did not predefine success as safe, controlled, ethically acceptable completion. The revised model therefore predicts observable deployment benefits under specified comparisons and records those outcome dimensions separately. It does not retroactively exclude the adverse scene by changing the metric. (V09 C2 P0235–0271; F P0054–0110, P0199–0258, P0286–0316; V07/V08 E01.)

**A03 is not fully confirmed by visible repair.** Aqua heals/carries Darkness despite resisting a penalty and repairs the wall after being sent to do so. This defeats a global no-remediation account. Yet external direction, professional pleasure and recognition alignment remain causal alternatives to an internal transition from undeniable blame through collapsed defense to accepted responsibility. V08 already isolated selective learning and face-saving defense; it did not establish the missing collapse branch. The complete accountability mechanism remains PARTIAL. (V09 C3 P0243–0272; F P0016–0019, P0043–0110; V08 A03.)

**A01, M01 and D02 require scope discipline.** V09 construction is legitimate new Gen03 domain evidence but is not retroactively folded into the original institutional sacred/support-magic test; V07/V08 already support that original condition. M01's rivalry branch is strongly replicated, while guilt about killing a teacher is not guilt that an exclusive build burdens companions. D02's belonging and meaning-sensitive components are strong, while the comparative pain claim remains less directly isolated. Whole-row judgments must preserve these asymmetries. (V09 C2 P0559–0617; C4 P0082–0104; F P0043–0110, P0412–0419, P0766–0783; C1 P0177–0433; V07/V08 A01, M01, D02.)

**Receiver correction RC-V09-01 (2026-10-08; outside the frozen text):** In CP03-M05, “Equipment destruction” overstates Megumin's agency. At C2 P0599–0615 she takes the item, hears its money/labor cost (P0600), discards it (P0602), then hears its expedition purpose (P0605) and acknowledges possible utility while maintaining rejection (P0606). Kazuma subsequently ignites and detonates it (P0608–0615). Read the frozen evidence shorthand as disposal despite explicit cost, not destruction by Megumin. The MG02-M02 PARTIAL disposition and local cost-inhibition failure remain supported. The frozen model and prediction wording, hashes, confidence and scoring criteria are preserved; this additive correction was made before any receiving-session V10 exposure.

## 3. Model Generation 0.3 — current model state

This section is the frozen model state paired with the prospective block below. It is a provisional reconstruction through V09, not a mature full-series model. Each CP03 identifier is a stable claim link for the predictions. It identifies a claim at this checkpoint, without creating a new permanent ledger. Confidence never rises to VERY HIGH before the withheld-source validation boundary.

### 3.1 Satou Kazuma

#### CP03-K01 — Effort and competence are goal-relative

**STRENGTHEN; HIGH.** Comfort and financial security genuinely reduce ordinary work motivation, but specific commitment, autonomous problem solving and exploitable rules recruit considerable effort. His distinctive capacity is building and revising an arrangement from weak tools, environmental states and other actors' incentives. He can delegate phases that do not suit him and explicitly anticipate a response. He is not automatically prepared for every contingency or superior in raw combat. The survived mechanism is indirect search; the precision gain is separating that capacity from readiness and downstream judgment. (V07/V08 K01/K02; V09 C2 P0021–0081, P0478–0486; C4 P0065–0144; F P0199–0258, P0383–0391.)

#### CP03-K02 — Reward capture and information failure are distinct error paths

**PRESERVE / REFINE; MODERATE-HIGH.** Recognition/payback can increase pursuit beyond an earlier safety preference, with a clear noncombat replication in V08 and more confounded competition evidence in V09. Missing enemy information, an unavailable contingency item and an externally imposed public promise are different mechanisms. Do not turn every dangerous outcome after success into proof of status intoxication. Personally known harm can make praise aversive. (V08 K03; V09 C2 P0090–0248, P0353–0373; C3 P0006–0068; F P0383–0391, P0434–0448.)

#### CP03-K03 — Concrete commitment and a narrow observed distress cue recruit care

**STRENGTHEN duty; NEW bounded cue hypothesis.** Trusted concrete need can recruit help before a complete plan exists. Kazuma may search, prepare, bargain and lend a relevant skill while still complaining. Two V09 interactions also show actual noticed tears interrupting an immediate self-rewarding pursuit. Earlier urgent verbal distress does not reliably do so, and his behavior can return to opportunism quickly. Confidence is HIGH for concrete commitment and MODERATE for transfer of the actual-tear cue. The latter is not a general rule of consent reliability. (V07/V08 K02; DISC-V07-04; V09 C2 P0478–0486; C4 P0164–0171; C1 P0312–0336, P0417–0454; F P0473–0494, P0752–0815.)

#### CP03-K04 — Perspective, moral salience and self-description remain uneven

**REVISE broad benevolence / PRESERVE calibrated narration; MODERATE-HIGH.** Personally familiar opponents receive attention and reluctance that anonymous enemy pleas do not reliably evoke. Accurate external inference can support both rescue and manipulation. His concern for household trust, coercive private resolve, repeated escalation, real consolation and later intrusive retrieval all belong to the model. Megumin's affectionate description is evidence of her valuation, not an objective acquittal. The relationship state changes through reciprocal speech; formal couple status remains open. (V09 C3 P0336–0437; C4 P0238–0255; F P0288–0316, P0434–0448, P0685–0847; Ep1 P0003–0007, P0051–0052; Ep2 P0016–0034.)

### 3.2 Aqua

#### CP03-A01 — Established domains are exceptional; activation is a separate dependency

**STRENGTHEN / EXPAND; HIGH for demonstrated domains.** Sacred/support execution remains strong, and V09 establishes strategically useful construction, material work and water-control drying. The new knowledge partly corrects Kazuma's lack of observation of an old skill. Skill does not guarantee timely waking, correct target selection or restraint. Do not project construction competence onto unobserved crafts. (V07/V08 A01; V09 C3 P0193–0272; F P0043–0076.)

#### CP03-A02 — Recognition changes behavior according to what earns it

**REVISE broad reward-to-failure rule; HIGH for sensitivity, MODERATE-HIGH for constructive transfer.** Prestige competition can replace a separate task, as in the divine dispute; recognition tied to an owned service can sustain the task, as in the repair-captain sequence. The latter extends V07's owned-goal performance finding across repeated institutional work. Her art, generosity and pleasure are compatible with completing repairs. The relevant state is the relationship between reward and goal, not praise alone. (DISC-V07-02; V08 A02; V09 C4 P0256–0300; F P0043–0110.)

#### CP03-A03 — Learning and remediation do not require global self-correction

**PRESERVE components / REVISE causal completeness; MODERATE overall.** V08's learned caution is real. V09 shows useful corrective action while blame or penalty is resisted, but does not isolate accepted responsibility, an apology or full defense collapse. External assignment and rewarding competence are explanatory competitors. Repeating a warned spirit interaction and persisting in flattering egg interpretations keep local failure visible. The open question is when she corrects voluntarily and what makes a learned rule available in a different reward state. (V08 A03 / DISC-V08-01; V09 C3 P0079–0092, P0243–0272, P0469; F P0016–0019, P0043–0110; Ep2 P0011–0019.)

#### CP03-A04 — The exact maximal-shortcut test is still open

**OPEN; MODERATE, inherited.** No V07–V09 episode cleanly supplies repetitive low-valued maintenance plus an available attractive maximal one-step alternative without a salient constraint or learned analogue. Fast effective drying is not an adverse shortcut simply because it is magical. Skilled work that becomes a valued role is not an unprotected low-status state. Retain the hypothesis with its evidence obligation rather than calling it confirmed or false. (V04–V06 checkpoint §5; unchanged MG02-A04 and V07/V08 non-tests; V09 F P0054–0110.)

### 3.3 Megumin

#### CP03-M01 — Explosion is a protected, deliberately maintained identity

**STRENGTHEN; HIGH.** Rivalry over the specialty elicits defensive competition and rejection of substitutes, including when a companion performs the rival role. Investment in greater power preserves a chosen dependency and shared routine. Ordinary utility is understood but need not be the decisive value. This does not mean all behavior is fixed or that relational guilt can never reopen the build. (V07 M01; V09 Pr P0009–0044; C2 P0559–0617; C4 P0082–0104.)

#### CP03-M02 — Self-attributed contribution failure is a distinct, unreplicated inversion route

**PRESERVE / OPEN; MODERATE-HIGH inherited from V05.** A belief that the exclusive build itself burdens valued companions previously allowed consideration of sacrifice. V07–V09 does not newly test that exact trigger. Inability to attack a benefactor and guilt about the result are not equivalent to deciding that the specialty prevents contribution. The new prediction keeps the distinction explicit, with any changed-role option identified as an unvalidated Gen03 extension. (V04–V06 checkpoint §6; unchanged MG02-M01 B; V09 F P0412–0419, P0766–0783.)

#### CP03-M03 — Artillery efficacy, technique and reward discipline are separable

**STRENGTHEN practical role; HIGH; NEW goal-drift transfer MODERATE.** Dense separated targets with an exit/transport plan make Explosion reliable and highly useful. V09 also demonstrates incantation-free control with the spell name voiced; its acquisition time is not established. Repeated successful casting can itself become the reward pursued after marginal mission value falls. Effective fire does not establish ethical restraint or an appropriate stopping rule. (V07 M03; V09 F P0199–0321, P0534–0544.)

#### CP03-M04 — A personally valued target constrains action and creates aftermath

**NEW / EXPAND; MODERATE for transfer beyond this relationship.** The ability to cast is distinct from the ability to act against a rescuer/teacher. Megumin hesitates or fails to execute, seeks acknowledgment and finally chooses a personally meaningful demonstration. Grief follows the act. Pre-action friction and post-action emotional cost are separate components: later regret must not rescue a failed inhibition prediction. Her interpretation of the additive wording remains an inference, and neither it nor Kazuma's possible smile observation certifies forgiveness. (V09 F P0007–0015, P0365–0419, P0473–0544, P0549–0551, P0766–0816.)

#### CP03-M05 — Affection does not make companion utility or safety an automatic veto

**REVISE / DOWNGRADE; MODERATE for broad restraint.** Equipment destruction despite explicit companion cost is a local failed M02 prediction. The contest's ally blast and Darkness's unconsciousness are additional adverse evidence. The exact frozen proposition remains ambiguous because the conjunction of best tactical Explosion use, valued companion and serious harm is not cleanly isolated. Anticipation of harm remains an explanatory uncertainty, not an additional original trigger requirement. A new, explicitly specified grave-harm/knowledge hypothesis is retained at lower confidence; genre framing alone cannot exclude future adverse cases. (V09 C2 P0235–0271, P0592–0606; C4 P0206–0208; unchanged MG02-M02/M04.)

### 3.4 Darkness / Dustiness Ford Lalatina

#### CP03-D01 — Protector duty values real contribution within finite capacity

**STRENGTHEN; HIGH.** Bodily interposition, defense-aligned service and institutional responsibility can outweigh self-protection. Fear and bodily reward may coexist with protection, but cannot explain every cost away. Armor loss and incapacitation bound efficacy without negating the protected people or the courage involved. Her report of surviving past Explosion and a rejected unarmored proposal are not a new V09 demonstration of surviving that attack. (V07/V08 D01/D03; V09 C3 P0213–0272; C4 P0075–0077, P0146–0163; F P0083–0097; Ep1 P0019–0024.)

#### CP03-D02 — Agency, audience and meaning govern suffering and belonging

**STRENGTHEN components / OPEN comparison.** She may desire a bounded scenario yet reject its changed practical or social meaning. Personal dignity is explicitly distinct from noble pride in the binding episode. Noble identity itself can be used enthusiastically or become embarrassing depending on context. Confidence is HIGH for meaning/belonging sensitivity, MODERATE for the comparative pain claim; no clean pain-only coercion experiment resolves it. Trigger changes must be identified independently of her reaction rather than defining “unwanted” only after protest. (V07/V08 D02; V09 C1 P0177–0208, P0334–0365, P0417–0433; C3 P0124–0138, P0512–0544.)

#### CP03-D03 — Preserving incompatible obligations can become private cost absorption

**PRESERVE; MODERATE-HIGH, mainly V07.** Family/civic duty and party belonging are both real commitments. She tries costly preservation before easy abandonment, yet secrecy and self-removal can deny companions the choice to share the burden. V09 command creates an institutional analogue, not a fresh complete family/party incompatibility. Desired heroic/danger scripts can also interfere with the actual obligation, as in the bandit delay. Protector intent is therefore not a guarantee of participatory or well-prioritized procedure. (V07 D04 / DISC-V07-01; V09 C3 P0124–0165; C4 P0146–0163.)

### 3.5 Ensemble

#### CP03-E01 — Organization improves deployment; it is neither a universal necessity nor a complete evaluation

**REVISE.** V07/V08 and the V09 siege support explicit roles, target conditions, resources, handoffs and substitutable providers. V09 also exposes a bad metric, an unsafe target-destruction success, reward drift within an effective military arrangement and a concealed target relationship that defeats a prepared plan. Confidence remains HIGH for bounded deployment benefits; the former unqualified necessity language is downgraded to MODERATE. Gen03 defines deployment through intended actions at assigned targets/times, handoff failures and missing resources, while separately recording final completion, friendly harm, goal discipline and ethics. Kazuma often initiates or repairs missing arrangements; domain experts and institutions can supply them too. (V07/V08 E01; V09 C2 P0120–0271; F P0054–0110, P0199–0258, P0286–0316, P0365–0419.)

#### CP03-E02 — Established household bonds have value beyond efficiency

**PRESERVE / STRENGTHEN supporting ecology; HIGH.** V07 is the direct prospective durable-separation test. V09 supports the lived value through gifts, shared rituals, departure from celebrations for a distressed companion and inclusion of Yunyun. Temporary tactical splitting is acceptable and does not contradict resistance to durable relationship loss. Affection and accurate mutual knowledge can support rescue or manipulation; continuing insults are not a reliable measure of attachment strength. (V07 K04/E02; V09 C1 P0343–0374; F P0199–0245, P0473–0494, P0549–0551; Ep1 P0017–0026.)

### 3.6 Japanese voice and humor

#### CP03-J01 — Role-conditioned interaction is more useful than a universal seriousness direction

**STRENGTHEN; HIGH for a patterned, conditional claim.** Serious specialty commitment, divine legitimacy, public duty, belonging insecurity and companion care have different observable language profiles. Greater seriousness may increase theater, directness, formality or self-disclosure depending on independently evidenced role and audience. The prediction fixes role mappings before judging language and preserves contrary/unchanged outcomes. Single particles, pronouns or catchphrases do not diagnose an entire personality. (V07/V08 J01; V09 C2 P0478–0486; C4 P0082–0104; F P0054–0094, P0459–0484, P0534–0544, P0784–0815.)

#### CP03-J02 — Most high-value humor has been situational or pragmatic; true form dependence remains visible

**STRENGTHEN qualitative evidence; MODERATE-HIGH.** The large V07–V09 comic sequences mainly depend on causal reversal, timing, status, role and pragmatics. V09's same-written-form charm/babysitting effect is local L3; the additive recognition clue is chiefly L2 with exact-wording sensitivity and belongs to a serious payoff. No numerical whole-corpus rate has been measured. Gen03 adopts a transparent episode-frequency census as a new, stricter operational test at MODERATE confidence, not a retroactive numerical proof of the old major-sequence judgment. (V07/V08 J02; V09 C1 P0061, P0081–0083, P0116–0118; F P0179, P0537; V09 deep reading §§7–8.)

### 3.7 Secondary candidates and evidence-limited roles

#### CP03-Y01 — Yunyun combines affiliation reward, initiative and effective ordinary magic

**EXPAND secondary candidate; MODERATE-HIGH for the linked mechanism.** Inclusion and useful participation are strongly valued; she can offer to join, help without instruction, overprepare and still execute an emergency escape competently. Objections to allies' cruelty and distress over a personally valued opponent show independent judgment and emotional limits. Near-tears during a duty declaration are not a demonstrated technical failure. The model does not establish permanent membership or a mature all-context personality. (V07 Yunyun support/relationship findings; V09 C2 P0641–0658; C3 P0152–0160; C4 P0154–0156; F P0199–0242, P0305–0310, P0378–0391, P0459–0467; Ep1 P0025–0026.)

#### CP03-CE01 — Chris/Eris retains distinct social modes and possible over-compliance

**PRESERVE / OPEN transfer; MODERATE.** V08 supports casual trusted companionship in Chris mode, meaningful recognition and a possible service-overload mechanism in the public divine role. V09 supplies no direct replication. The new targeted prediction asks whether sincere requests lower her refusal threshold under an explicitly excessive burden; comfortable self-set limits would be adverse evidence. No absent scene is invented to advance this model. (V08 Chris/Eris reconstruction; DISC-V08-04; V08 J01.)

#### CP03-I01 — Iris's safe-context agency and duty constraints remain inherited hypotheses

**PRESERVE / OPEN; MODERATE-HIGH inherited from V06.** The prior model links safe nondeferential interaction to age-appropriate agency and understood duty to smaller requests. Neither mechanism receives a clean V07–V09 prospective test. V09 contributes a familiar/formal letter and escort request, but not a private wish, an unwanted obligation or a direct behavioral contrast. Do not promote the request into a completed decision or adult romantic commitment. (V04–V06 checkpoint §10; unchanged MG02-I01/I02 and their V07/V08 non-tests; V09 Ep2 P0035–0041.)

#### CP03-W01 — Wolbach/Chomusuke remains a bounded relational and ontological question

**OPEN; no mature model or plot prediction.** A considerate bath companion, an important inviter, a rescuer/teacher and an enemy commander are simultaneously evidenced roles. Wolbach states conditions for recovering divided power, but does not reveal the motive for her allegiance. Chomusuke's changed bathing behavior, name response and apparent growth support continuity hypotheses without establishing restored memories, future form or forgiveness. This claim constrains what the model must leave unknown; it does not turn the novel's forward-facing clues into predictions of later plot. (V09 C3 P0387–0437; F P0176–0189, P0331–0374, P0499–0567, P0766–0783, P0835–0868; Ep2 P0004–0008.)

## 4. Model failures and boundary refinements

### 4.1 Genuine failure, incomplete coverage and ambiguity are different results

M02's equipment episode is a genuine local negative prediction result. Its lesson is that a real valued relationship can coexist with deliberately imposed ordinary cost when core specialist identity is challenged. Gen03 changes the prospective condition; Gen02 does not receive an invented exception. M04 is different: actual harmful collateral is present, but the original best-tactical-use/valued-companion/serious-harm combination cannot be isolated. Anticipation is a separate explanatory uncertainty; it does not retrospectively narrow the frozen trigger. It remains adverse ambiguity and a reason to lower confidence, not a claim that nothing happened. (V09 C2 P0235–0271, P0592–0606.)

A04 and the Iris predictions have no clean tranche trigger. M01, A03 and D02 have meaningful tested components alongside unresolved ones. E01 is partly supported and partly too broad because the original success criterion was underspecified. These distinctions matter more than the row counts. A model that labels every absence as success, every problem as a mere exception, or every partial case as complete falsification loses the information the experiment was meant to produce.

### 4.2 The principal refinements

| Formerly insufficient formulation | Gen03 refinement | Basis |
|---|---|---|
| Praise/status tends to distract Aqua | Separate a distinct prestige contest from recognition attached to successful service | V07 owned-goal performance; V08 status capture; V09 ambush versus repair |
| Companion cost inhibits Megumin's retaliation | Core-specialty challenge can defeat acknowledged ordinary utility; self-attributed build burden and grave harm are distinct conditions | V09 equipment disposal despite explicit cost; inherited V05/V06 evidence; unresolved M04 |
| Technical specialization determines the available action | Add personally valued target history, willingness and post-action emotional cost | V09 repeated Wolbach hesitation, chosen demonstration and grief |
| All successful extreme specialization requires routing | Predict bounded comparative deployment benefits with independent arrangement coding and separate outcome measures | V09 bad metric/unsafe victory versus distributed siege, plus goal drift |
| Distress reliably interrupts Kazuma's opportunism | Preserve earlier failures; test only noticed actual tears as a new, modest-confidence cue hypothesis | V09 confinement, actual tear responses and later intrusive behavior |
| Noble embarrassment and pain form a single aversion scale | Use independently established agency, audience, role and belonging changes | V07 removal; V08 public exposure; V09 personal-dignity distinction |
| Serious speech must become less theatrical | Retain independent role mappings and score their predicted interaction directions separately | V07/V08 and V09 identity, service, duty, gratitude and care registers |
| A source mention is a behavioral test | Require the stipulated motive, choices and relationship context to appear | Iris's letter; tactical split versus durable separation; command versus family incompatibility |

### 4.3 Development versus new observation

Reciprocal affection is newly spoken and separately contemplated by Kazuma and Megumin. Megumin's relationship with her teacher reaches an irreversible-looking action and a documented grief state, while the precise ontology remains open. Aqua's repair leadership is a new sustained role in this operation, but the skill itself predates Kazuma's observation. Darkness's equipment loss changes available tactics; it is not a personality change. Yunyun's already-valued affiliation is sampled in more varied competent, anxious and morally conflicted states. Keeping these different forms of change separate avoids manufacturing one volume-wide maturation story. (V09 F P0063–0110, P0534–0551, P0719–0847; C3 P0213–0272; Ep1 P0003–0007, P0051–0052.)

## 5. High-information unknowns for the next tranche

These are conditional evidence needs, not predictions of what plot the next books contain:

1. Does Kazuma repeat a noticed-actual-tears interruption across different companion contexts, and how quickly does opportunism return afterward? Earlier verbal distress already supplies contrary evidence to a broader rule.
2. Can Aqua sustain a low-valued task when an attractive maximal shortcut is actually available, and can voluntarily owned repair be distinguished from external compulsion and social reward?
3. When Aqua corrects a harmful consequence, is accepted blame/apology necessary, and which prior learned rules are retrieved under a new prestige state?
4. Does Megumin's specialist identity again outweigh explicit ordinary companion cost? Does internally accepted build-burden guilt reproduce the distinct compromise route?
5. Does a new valued-target conflict reproduce pre-action friction independently of any later regret? Does a genuinely matched direct grave-companion-harm case test the narrowed friendly-fire hypothesis?
6. Can repeated rewarding Explosion use stop at the instrumental objective without an external limit, especially once target or growth reward is available?
7. Do Darkness's agency/audience/belonging conditions predict responses without coding the trigger from the reaction? What happens in an actually comparable pain-only coercion setting remains open.
8. When another actor supplies independently specified roles/resources/handoffs, does deployment proceed without Kazuma's continuing direction? Do different outcomes—target destruction, safety, goal discipline—diverge again?
9. Do Yunyun's initiative, inclusion reward, competent execution and moral dissent recur together across another situation? Does Chris/Eris again exceed an explicitly preferred service burden?
10. Do Iris's stipulated direct contexts actually occur? A familiar letter or an invitation alone cannot answer either behavioral question.
11. Do the predeclared role/voice mappings survive contrary examples, and does a complete defined humor census support the new frequency prediction without selective segmentation?

Wolbach's allegiance, possible smile and Chomusuke's continuity are interpretation limits to preserve. The analyst must not turn a remembered later resolution into either a forecast or an explanation of V09.

## 6. Advancement decision and Gen03 freeze receipt

The V07–V09 evidence review is complete; all 22 Gen02 predictions have a tranche disposition, including adverse and missing-trigger cases. The nine substantive ledgers receive V09 additions and the prediction ledger receives the V09 addendum, tranche closeout and the exact frozen block below. The freeze covers both the CP03 model-state section and the 25-prediction block. Each has an independently reproducible byte boundary and hash.

### Freeze receipt

The V07–V09 adjudication was closed at `2026-10-08T04:05:05.195463+00:00`. After pre-freeze source, trigger and independent consistency audits, the model state and complete prediction block were frozen at **`2026-10-08T04:33:35.790540+00:00`**. This is the actual session freeze, not a proposed future action.

| Frozen object | UTF-8 bytes | SHA-256 |
|---|---:|---|
| Gen03 current model, §3 | 17,746 | `dfd92578ddef97eeaf942a6a5d713f37a84678abc9433bce05d36d2ec659d85a` |
| Complete Gen03 V10–V12 prediction block | 45,675 | `ebe83ef5dc87fc2e85f8f711e2ba373239d4eea4fd14f466537dbd3625d76150` |

For the model hash, take the bytes from the first `#` of `## 3. Model Generation 0.3 — current model state` through the byte immediately before the first `#` of `## 4. Model failures and boundary refinements`, including intervening blank lines. For the prediction hash, take exactly **45,675 bytes** starting at the first `#` of `# Model Generation 0.3 — Frozen Predictions for V10–V12`; this includes the final freeze-state paragraph and its trailing LF. Use UTF-8, LF line endings, no BOM and no normalization or reflow.

The identical prediction block appears below and in the prediction-ledger patch. All **25 Outcome and 25 Adjudication fields are blank**. No V10–V12 narrative or withheld side narrative was opened. The old Gen02 block still has SHA-256 `7f14063864e5d1ce090d6c271dc5696d969bef1db50c31770191ce19268a7440`; no earlier prediction wording was changed. These are session exposure and byte-integrity statements, not proof of pretraining-level blindness or a claim of completed repository integration.

The packet's candidate state is **V01–V09 complete; Phase 3 complete; Gen03 frozen; V10–V12 predictions frozen; V10 next and unopened**. Canonical advancement remains the separate integrator's responsibility. V10 is not opened in this session even after the freeze. Side narratives remain withheld for later post-main-series validation. The verified source-lock reading-state lag and the bootstrap-reported expanded-side-corpus inventory lag are separate governance tasks, not analytical permission or hidden source updates. The latter was not independently re-audited in this session.

The following block is identical to the Gen03 block supplied for the prediction ledger. It may receive later outcome addenda; its prediction wording, confidence and disconfirmation criteria may not be rewritten after exposure. The CP03 references resolve above. The old Gen01/02 model states, original prediction text and V07/V08 addenda remain provenance.

# Model Generation 0.3 — Frozen Predictions for V10–V12

**Derivation boundary:** Japanese main-series V01–V09 main narrative only. Gen 0.2's V07–V09 outcomes have been closed before this new set is frozen. Gen 0.1 and Gen 0.2 retain their original wording and historical outcomes.

**Freeze state:** FROZEN_BEFORE_V10. The freeze receipt in the checkpoint and integration handoff identifies the UTC time, exact block byte count and SHA-256. V10–V12 have not been opened in this analytical session. This is a session source-exposure control, not a claim that a pretrained model has never encountered the series.

**Evidence basis:** CP03 claim identifiers resolve to the current-model section of `KONOSUBA_V07-V09_CHECKPOINT.md`. All V09 locators below are in the verified EPUB: `0014:P0043–0110` means `OEBPS/Text/part0014.xhtml`, all-body-paragraph enumeration, inclusive. V07/V08 references mean the unchanged canonical prospective addenda for the stated MG02 IDs; they are inherited evidence, not fresh primary rereadings of those volumes.

**Evaluation rules:** determine the trigger, relationship, stakes and available choices before scoring the response. Missing conjuncts produce NOT_TESTED or explicitly partial/ambiguous coverage; they do not count as successful predictions. Record negative cases with the same detail as positive cases. Where a tendency is tested repeatedly, retain all matched cases rather than replacing them with a favorable aggregate. Score distinct predicted branches separately; one observed branch cannot confirm an entire compound prediction. This applies especially to K01 search/revision/delegation, M04 action friction/aftermath and E01 deployment/provider/Kazuma comparisons. A single contrary outcome is adverse evidence even when a repeat-pattern disconfirmation threshold is not met. Keep capacity, target destruction, safe deployment, goal completion and ethical evaluation separate. New qualifications learned in V10–V12 belong in outcome/revision fields, never in the frozen text below.

## Satou Kazuma

### MG03-K01 — Indirect construction of a solution, with explicit resource limits
- **Trigger/context:** a serious novel or under-structured problem disadvantages Kazuma in direct power, and he can identify at least one usable rule, tool, environmental feature or incentive.
- **Relationship/stakes:** combat or institutional stakes; distinguish strangers from valued people whose safety constrains available tactics.
- **Predicted appraisal:** the apparent power contest can be changed by altering state, sequence, information or other actors' incentives.
- **Predicted dominant motive:** obtain a workable outcome at lower personal exposure while retaining agency over the method.
- **Predicted behavior:** he will try an indirect combination or negotiated arrangement and revise it when a newly learned capability invalidates the first plan. He will delegate phases that suit stronger specialists. This predicts search and revision, not universal first-plan success or possession of every needed resource.
- **Interaction tendency:** practical instructions and explicit division of responsibility; opportunistic or unflattering framing may coexist with correct mechanics.
- **Confidence:** HIGH.
- **Evidence basis:** CP03-K01, CP03-E01; V07/V08 MG02-K01; V09 `0013:P0065–0144`, `0014:P0043–0076`, `P0199–0258`, `P0374–0391`.
- **Disconfirmation:** repeated matched problems with acknowledged usable indirect options instead produce conventional power contests or passive abandonment, without an independently established relational or moral reason; or he repeatedly cannot revise after the failed assumption is explicitly exposed.
- **Outcome:**
- **Adjudication:**

### MG03-K02 — Concrete entrusted need recruits effort before certainty
- **Trigger/context:** a trusted person makes a concrete request whose refusal would leave that person or a valued companion exposed to preventable harm, and Kazuma has some feasible contribution even if no complete solution is known.
- **Relationship/stakes:** established trust, actual cost or danger; generic appeals to heroism, fame or attractiveness alone do not supply this trigger.
- **Predicted appraisal:** this is a particular person's problem that he can help reduce, not simply optional public work.
- **Predicted dominant motive:** preserve the person/relationship while reducing the cost of intervention.
- **Predicted behavior:** he will complain, bargain, investigate, prepare or seek a cheaper route, but make a substantive contribution rather than abandon the responsibility chiefly for comfort. Commitment may precede a fully credible success plan.
- **Interaction tendency:** ordinary or grumbling speech can accompany costly help; a polished heroic declaration is not required.
- **Confidence:** HIGH.
- **Evidence basis:** CP03-K03; V07/V08 MG02-K02 and DISC-V07-04; V09 `0011:P0478–0486`, `0013:P0164–0171`, `0014:P0473–0494`.
- **Disconfirmation:** a clear, feasible contribution exists, but he knowingly leaves the established person exposed primarily to preserve leisure, with no meaningful help, search or relationship-preserving alternative.
- **Outcome:**
- **Adjudication:**

### MG03-K03 — Success-linked personal reward can expand pursuit
- **Trigger/context:** Kazuma receives concrete success feedback or sees an apparently manageable opportunity for recognition/payback, and that personal reward is visibly active before his next decision about scope, pursuit or exposure, whether or not the plan subsequently changes.
- **Relationship/stakes:** initially tolerable perceived risk; compare the same task before and after feedback. Success without evidence of recognition/payback salience is insufficient.
- **Predicted appraisal:** he can obtain more advantage, status or retaliation than the original task required.
- **Predicted dominant motive:** extend the rewarding success state.
- **Predicted behavior:** he will increase scope, pursuit, taunting or accepted exposure relative to his prior plan. Newly explicit severe danger or harm to a personally known target may instead restore caution; record these pre-existing modifiers before judging the outcome.
- **Interaction tendency:** victory/credit language or grievance display should accompany the expansion more often than purely duty-based explanation.
- **Confidence:** MODERATE-HIGH.
- **Evidence basis:** CP03-K02; V08 MG02-K03; V09 partial test `0011:P0090–0248`; limiting cases `0013:P0065–0097`, `0014:P0434–0448`.
- **Disconfirmation:** repeated comparable success-plus-personal-reward states leave pursuit unchanged or make it more conservative despite no new threat/relationship cue. Forgotten equipment alone does not count as confirmation.
- **Outcome:**
- **Adjudication:**

### MG03-K04 — Noticed actual tears can interrupt intimate or teasing pursuit
- **Trigger/context:** during an interaction Kazuma is pursuing for personal intimate or teasing reward, a valued companion begins shedding actual tears that he notices; he can pause or ask without creating a separate immediate danger. Near-tears or verbal refusals alone do not supply this narrowed cue.
- **Relationship/stakes:** familiar companion, salient vulnerability; this is not a prediction of general consent reliability or kindness to every person.
- **Predicted appraisal:** the interaction may be harming the person rather than providing mutually wanted play or closeness.
- **Predicted dominant motive:** reduce the recognized distress and clarify what the person needs, in conflict with his immediate desire and embarrassment.
- **Predicted behavior:** he will interrupt the immediate pursuit and ask, assist or wait. Continued desire, awkward self-exoneration and later opportunism may remain, but knowingly continuing the same unwanted pursuit is adverse evidence.
- **Interaction tendency:** flustered questions or blunt, self-involving reassurance are more likely than effortless moral eloquence.
- **Confidence:** MODERATE; a new cue-specific hypothesis, not a global rehabilitation claim.
- **Evidence basis:** CP03-K03/04; positive V09 cue-response sequences `0010:P0427–0433`, `0014:P0752–0815`; adverse earlier verbal-distress phases `0010:P0312–0336`, `P0417–0426`; renewed opportunism `0010:P0436–0454`; wider limits `0012:P0336–0386`, `0014:P0701–0749`, `0016:P0016–0034`. This is a newly narrowed Gen03 hypothesis; it does not reinterpret those earlier refusals as acceptable or unrecognized.
- **Disconfirmation:** after noticing actual tears in a matched companion interaction, he continues the immediate self-rewarding pursuit without checking, helping or pausing, despite an available low-cost pause. Do not infer that he failed to notice the cue merely because he continued. Earlier verbal-distress failures remain contrary evidence to any broader stopping rule.
- **Outcome:**
- **Adjudication:**

## Aqua

### MG03-A01 — Established specialist ability appears under a well-defined task
- **Trigger/context:** a clearly bounded task uses an ability already demonstrated in the derivation corpus: healing, purification, resurrection, support/sealing, or practiced construction/art with water control where relevant.
- **Relationship/stakes:** institutional or explicitly organized service; sufficient access and resources. Record sleep, distraction and activation separately from the quality of execution.
- **Predicted appraisal:** this is a task within a recognized area of her expertise.
- **Predicted dominant motive:** execute the familiar service and/or display mastery.
- **Predicted behavior:** once engaged, she will perform at a high level relative to available alternatives, with fewer task errors when goals and boundaries are clear. This does not grant competence in unobserved technical domains or guarantee readiness at the required moment.
- **Interaction tendency:** confident directives, demonstration or professional pride may be accurate rather than empty boasting.
- **Confidence:** HIGH for the established domains.
- **Evidence basis:** CP03-A01; V07/V08 MG02-A01; V09 `0012:P0238–0272`, `0014:P0043–0076`, `P0080–0110`.
- **Disconfirmation:** repeated engaged, adequately resourced tasks in these established domains fail chiefly through lack of ability or misunderstanding of the domain. A new craft is not assumed mastered merely because construction was.
- **Outcome:**
- **Adjudication:**

### MG03-A02 — A direct prestige contest can displace an assigned purpose
- **Trigger/context:** an ongoing instrumental assignment is interrupted by a challenge to Aqua's divinity, followers, superiority or public recognition, and the prestige contest offers a response distinct from completing the task.
- **Relationship/stakes:** the challenger need not be a friend; the original assignment and its constraints must be identifiable before the challenge.
- **Predicted appraisal:** letting the status claim stand is immediately intolerable or more salient than the task.
- **Predicted dominant motive:** compel acknowledgment or win the status contest.
- **Predicted behavior:** she will escalate assertion, performance or power use and loosen at least one original task constraint. Competent ability may magnify the collateral cost. Directly acknowledged imminent harm can be a competing cue, but must be observed rather than inferred after the fact.
- **Interaction tendency:** self-naming, divine/faction titles, demands for apology or mirrored disparagement.
- **Confidence:** HIGH for the trigger class; exact severity remains uncertain.
- **Evidence basis:** CP03-A02; V08 MG02-A02; V09 `0013:P0256–0300`, `0014:P0016–0022`.
- **Disconfirmation:** repeated clear prestige challenges leave the separate assigned goal and constraints intact without another actor preventing escalation or independently acknowledged imminent harm already competing with it. Other proposed explanations remain rival accounts or adverse evidence for revision, not automatic exclusions.
- **Outcome:**
- **Adjudication:**

### MG03-A03 — Recognition attached to real service can sustain it
- **Trigger/context:** Aqua has a task she demonstrably knows how to do, receives recognition specifically for doing it, and has an identified beneficiary or responsibility rather than a separate status contest.
- **Relationship/stakes:** repeated service or repair, with the rewarded role tied to the required work. Record whether the assignment is externally imposed, voluntarily owned, or both.
- **Predicted appraisal:** continued good work demonstrates the valued role and sustains acknowledgment.
- **Predicted dominant motive:** enjoy mastery, trusted responsibility and recognition together.
- **Predicted behavior:** she will continue useful performance across repeated opportunities instead of necessarily abandoning it for spectacle. She may add display or share rewards while the core task remains completed. Corrective action need not be preceded by an apology.
- **Interaction tendency:** role-title uptake and confident instruction can reinforce performance.
- **Confidence:** MODERATE-HIGH; supported by V07 owned-goal performance and the extended V09 repair sequence.
- **Evidence basis:** CP03-A02/03; DISC-V07-02; V09 `0014:P0016–0019`, `P0043–0110`.
- **Disconfirmation:** despite a still-aligned recognition/service structure and no independently observed material interruption, resource loss, immediate danger or distinct prestige contest, repeated opportunities instead produce refusal, goal abandonment or merely decorative output without the required service. One externally forced action alone is not positive evidence for voluntary ownership.
- **Outcome:**
- **Adjudication:**

### MG03-A04 — Unvalued maintenance with an available maximal shortcut
- **Trigger/context:** repetitive maintenance remains low in Aqua's expressed valuation and a concretely available, attractive one-step high-power alternative is established.
- **Relationship/stakes:** no salient learned analogue or strong external constraint already rules out the shortcut; all these conditions must be checked before counting a test.
- **Predicted appraisal:** the rapid high-output method avoids tedious work.
- **Predicted dominant motive:** remove the immediate burden quickly.
- **Predicted behavior:** she will prefer the shortcut while giving insufficient attention to a secondary system it affects.
- **Interaction tendency:** confident simplification or dismissal of labor may accompany the choice; no special phrase is required.
- **Confidence:** MODERATE, inherited and still unvalidated in the V07–V09 tranche.
- **Evidence basis:** CP03-A04; V04–V06 checkpoint §5 and unchanged MG02-A04; V09 `0014:P0054–0110` is a non-test/countercondition, not confirming evidence.
- **Disconfirmation:** matched cases repeatedly show calibrated routine performance despite the available shortcut, with no learned analogue or external constraint already accounting for it. Mere speed, effective drying or any manual work does not establish the trigger.
- **Outcome:**
- **Adjudication:**

## Megumin

### MG03-M01 — Core-specialty challenge can outweigh ordinary companion cost
- **Trigger/context:** a rival, including a companion acting as a rival, explicitly denigrates, replaces or imitates Explosion in a way Megumin treats as a challenge to her specialist identity.
- **Relationship/stakes:** ordinary financial, equipment, convenience or status cost to companions is known; neither an independently expressed conclusion that her build seriously burdens them nor an independently recognized imminent grave companion-harm cue is active before her response. Record mixed-trigger episodes separately rather than deriving eligibility from which motive wins.
- **Predicted appraisal:** the challenge attacks a defining value rather than offering a neutral efficiency improvement.
- **Predicted dominant motive:** preserve the legitimacy and distinctiveness of Explosion.
- **Predicted behavior:** she will defend, compete, reject the replacement or retaliate; known ordinary companion cost alone will not reliably secure compromise. Record any attempt at redirection rather than treating all escalation as uncontrolled.
- **Interaction tendency:** specialist naming, theatrical assertion and precise denial of equivalence.
- **Confidence:** HIGH for defensive identity activation; MODERATE for its priority over known companion utility.
- **Evidence basis:** CP03-M01/05; V07 MG02-M01 and partial MG02-M02; V09 `0011:P0559–0617`, `0013:P0082–0104`.
- **Disconfirmation:** repeated clean identity challenges lead to easy compromise because of ordinary companion cost alone, without visible identity conflict, retaliation or an independently evidenced higher-order burden/harm appraisal.
- **Outcome:**
- **Adjudication:**

### MG03-M02 — Internally accepted contribution guilt can reopen the build
- **Trigger/context:** Megumin herself concludes that her exclusive specialization materially prevents her from contributing to valued companions, rather than merely hearing an opponent's criticism.
- **Relationship/stakes:** established companions; the perceived burden is substantial and attributed to the build, not inability to attack one particular person.
- **Predicted appraisal:** protecting the specialty may conflict with remaining useful and wanted.
- **Predicted dominant motive:** preserve contribution and belonging, despite genuine love of Explosion.
- **Predicted behavior:** she will seriously consider compromise, a changed role or abandonment of the exclusive build, with visible loss or reluctance. Others' reassurance may alter the decision, but should not erase the initial conflict.
- **Interaction tendency:** quieter, apologetic or explicit cost language is expected when the self-appraisal is expressed; the role is no longer only that of a challenged rival.
- **Confidence:** MODERATE-HIGH as inherited from V05; not prospectively validated by V07–V09.
- **Evidence basis:** CP03-M02; V04–V06 checkpoint §6 and unchanged MG02-M01 Trigger B. A changed-role option is a Gen03 extension, not an already validated outcome; neither it nor the inherited trigger received a matched V07–V09 test. V09 `0014:P0412–0419`, `P0766–0783` are distinct target/guilt cases, not validation of this build-burden trigger.
- **Disconfirmation:** repeated explicit, substantial self-attributed build burdens produce no meaningful conflict or consideration of compromise, even when a feasible alternative is recognized.
- **Outcome:**
- **Adjudication:**

### MG03-M03 — Safe separated targets expose reliable artillery
- **Trigger/context:** a target within Explosion's established capacity/range is dense or immobilized; friendlies are safely separated; resource use and the post-cast exit/carry requirement are planned.
- **Relationship/stakes:** no identified valued person occupies the target role. The conditions must be established before evaluating the result.
- **Predicted appraisal:** the task offers a legitimate, technically suitable use of the chosen specialty.
- **Predicted dominant motive:** perform and demonstrate Explosion effectively.
- **Predicted behavior:** she will execute reliable terminal fire, making the specialization highly useful for that task. This predicts tactical efficacy; it does not predict restraint toward defeated enemies or sound choice of the campaign's larger objective.
- **Interaction tendency:** exuberance and theatrical display may coexist with accurate execution; a full incantation is not required for demonstrated V09-level control.
- **Confidence:** HIGH.
- **Evidence basis:** CP03-M03; V07 MG02-M03; V09 `0014:P0199–0242`, `P0261–0304` are matched deployment evidence; `P0534–0544` supports technical capacity only because its personally valued target does not match this prediction. The incantation is omitted there, while the spell name is voiced.
- **Disconfirmation:** repeated fully matched target/resource/exit cases fail because of her own ordinary target-selection or execution process, despite no new relational inhibition or external interference.
- **Outcome:**
- **Adjudication:**

### MG03-M04 — A valued target creates a separate firing constraint
- **Trigger/context:** a task calls for decisive harm to someone whom the source independently establishes as personally valued by Megumin through rescue, teaching, gratitude or another significant relationship.
- **Relationship/stakes:** that person is now an opponent or obstacle; technical feasibility and urgent reasons to act may both be present.
- **Predicted appraisal:** the target carries a relationship obligation that cannot be reduced to a combat category.
- **Predicted dominant motive:** reconcile protection/duty with attachment or gratitude.
- **Predicted behavior:** she will show meaningful hesitation, a search for acknowledgment/choice, or inability to execute before or during a personally meaningful acknowledgment or choice; acting need not resolve subsequent guilt. If she acts, immediate celebratory ease is less likely than residual emotional cost. Record pre-action relational friction and post-action emotional cost separately. The mechanism does not depend on a target merely looking human.
- **Interaction tendency:** direct relational address or an attempted personal question can interrupt ordinary specialist theater.
- **Confidence:** MODERATE; repeated moments within one central V09 conflict are not independent cross-person replications.
- **Evidence basis:** CP03-M04; V09 `0014:P0007–0015`, `P0365–0419`, `P0473–0544`, `P0766–0816`.
- **Disconfirmation:** a comparably established valued-target conflict produces effortless execution without meaningful pre-action relational friction despite the salient bond. This is adverse to the firing-constraint component even if regret follows. Easy celebration without meaningful emotional aftermath is separately adverse to the aftermath component. A target with no such history is not a test.
- **Outcome:**
- **Adjudication:**

### MG03-M05 — Explicit serious companion harm remains a guarded prediction
- **Trigger/context:** Megumin knows that the best available tactical Explosion use would directly expose a valued companion to grave bodily harm, with the risk and alternatives made clear in the source.
- **Relationship/stakes:** current valued companion; establish anticipated harm magnitude, Megumin's knowledge, alternatives and the tactical requirement independently. Minor displacement without established anticipated grave injury is distinct; uncertain severity remains ambiguous/adverse collateral, not automatically harmless comedy. An enemy's attack is not her own friendly-fire choice.
- **Predicted appraisal:** success would impose a personally unacceptable relational cost unless it is justified or authorized.
- **Predicted dominant motive:** protect the companion while responding to the tactical need.
- **Predicted behavior:** she will hesitate, object, seek consent/authorization, redirect, or otherwise show clear friction relative to ordinary enthusiastic casting.
- **Interaction tendency:** explicit concern or negotiation is evidence; a token catchphrase is not.
- **Confidence:** MODERATE, downgraded from the broad Gen 0.2 extrapolation because of V09 adverse collateral evidence and lack of a clean matched replication. This explicitly specified grave-harm/knowledge trigger is a narrowed Gen03 hypothesis, not a wording-identical continuation of MG02-M04.
- **Evidence basis:** CP03-M05; V04–V06 checkpoint §6 / unchanged MG02-M04; adverse V09 `0011:P0254–0271`; distinct care evidence `0013:P0206–0208`.
- **Disconfirmation:** a clean matched case produces enthusiastic casting without relational friction despite her explicit understanding of the grave companion risk. Do not reclassify an adverse matched outcome as harmless comedy after observing it.
- **Outcome:**
- **Adjudication:**

### MG03-M06 — Repeated rewarding fire can become its own objective
- **Trigger/context:** a sustained operation repeatedly permits safe, effective Explosion and provides visible skill/experience growth or equivalent specialist reward; the original instrumental objective is approaching completion or has weakened.
- **Relationship/stakes:** impersonal enemy/obstacle targets; no independently active valued-target or grave companion-harm conflict.
- **Predicted appraisal:** another opportunity to fire/grow remains desirable even when marginal mission value falls.
- **Predicted dominant motive:** continue the specialty reward.
- **Predicted behavior:** she will seek additional casts, denser targets or an extended opportunity; a companion may need to restate the original goal. Tactical success can persist while goal discipline declines.
- **Interaction tendency:** language of casting, spectacle or growth will increasingly replace the original mission rationale.
- **Confidence:** MODERATE; a new extrapolation from the multi-day V09 sequence.
- **Evidence basis:** CP03-M03/05; V09 `0014:P0268–0321`, especially `P0286–0316`.
- **Disconfirmation:** repeated matched reward sequences lead her to stop or narrow use when the instrumental objective is achieved, without an external limit or another already established higher-priority conflict.
- **Outcome:**
- **Adjudication:**

## Darkness / Dustiness Ford Lalatina

### MG03-D01 — Protector contribution survives fear and finite endurance
- **Trigger/context:** a person Darkness treats as her responsibility faces serious harm or injustice, and she has a feasible defensive or institutional intervention.
- **Relationship/stakes:** a protected person or companion; distinguish chosen fantasy danger from an independently visible threat to someone else.
- **Predicted appraisal:** she has a responsibility to absorb or oppose the threat.
- **Predicted dominant motive:** protect and contribute, even where fear, embarrassment or bodily reward also exists.
- **Predicted behavior:** she will accept bodily, reputational or institutional cost. In a defense-aligned task she will use interposition/endurance rather than deliberately preserve helplessness. Equipment and opponent force may still overwhelm her.
- **Interaction tendency:** protector/noble assertions or blunt action may precede concern for her own comfort.
- **Confidence:** HIGH.
- **Evidence basis:** CP03-D01; V07/V08 MG02-D01/D03; V09 `0011:P0549–0553`, `0012:P0213–0272`, `0013:P0075–0077`, `P0146–0163`.
- **Disconfirmation:** despite recognizing serious unjust harm and a feasible contribution, she preserves rank/self-protection chiefly for convenience, or repeatedly sabotages the needed defensive role merely to remain helpless.
- **Outcome:**
- **Adjudication:**

### MG03-D02 — Agency, audience and belonging determine aversion
- **Trigger/context:** a sought, bounded scenario acquires unchosen public exposure, reduced control, or an explicit threatened change from equal party membership. Establish the changed condition from the event and previously expressed preferences independently of her present reaction.
- **Relationship/stakes:** identify who controls the event, who witnesses it and what standing is threatened; mere physical intensity does not define the trigger.
- **Predicted appraisal:** the changed agency, audience or standing threatens dignity or belonging previously valued outside the desired scenario.
- **Predicted dominant motive:** restore agency, dignity or ordinary belonging.
- **Predicted behavior:** genuine protest, anxiety, negotiation, anger or defensive concealment will increase rather than the event being uniformly welcomed. This does not settle how pain alone would work as coercion.
- **Interaction tendency:** she may abandon playful fantasy for direct personal objection or unusually deferential belonging requests, depending on the identified threat.
- **Confidence:** HIGH for meaning/belonging sensitivity; MODERATE for comparative generalization across pain conditions.
- **Evidence basis:** CP03-D02; V07/V08 MG02-D02; V09 `0010:P0177–0208`, `P0334–0365`, `P0417–0433`.
- **Disconfirmation:** repeated matched, independently established agency/audience/belonging changes are uniformly enjoyed or dismissed while the source shows no protest, anxiety or attempt to recover control; ordinary pain by itself cannot confirm this prediction.
- **Outcome:**
- **Adjudication:**

### MG03-D03 — Incompatible obligations recruit costly preservation attempts
- **Trigger/context:** family/noble/civic duty and continued party membership make genuinely incompatible concrete demands.
- **Relationship/stakes:** obligations to identifiable people on both sides, rather than an abstract preference for prestige or temporary deployment apart.
- **Predicted appraisal:** simply dropping either responsibility would betray a valued part of her life.
- **Predicted dominant motive:** protect people and preserve both commitments if possible.
- **Predicted behavior:** she will try negotiation, procedural workarounds or personally costly absorption before easy abandonment. Her V07 secrecy/self-erasure remains a possible procedural error; protective intent does not guarantee shared decision-making.
- **Interaction tendency:** duty language may conceal personal need; other members may need to challenge her assumption that she must bear the cost alone.
- **Confidence:** MODERATE-HIGH, chiefly inherited from the direct V07 test.
- **Evidence basis:** CP03-D03; V07 MG02-D04 / DISC-V07-01; V09 `0013:P0146–0163` is a bounded command-obligation analogue, not a new full family/party test.
- **Disconfirmation:** she discards either established relationship or recognized duty for convenience or prestige without visible conflict or preservation attempt despite feasible alternatives.
- **Outcome:**
- **Adjudication:**

## Ensemble

### MG03-E01 — Explicit task organization improves deployment but is not sufficient
- **Trigger/context:** a serious multi-stage problem requires several established specialist capacities, and source evidence permits comparison between missing/misaligned organization and an arrangement with explicit roles, targets, resources and handoffs. Classify these arrangements and incentive alignment independently of the eventual result.
- **Relationship/stakes:** record practical task completion, friendly harm, goal discipline and moral objections separately. Temporary allocation apart does not mean loss of membership.
- **Predicted appraisal:** participants identify a usable contribution when the arrangement fits their actual abilities and incentives.
- **Predicted dominant motive:** solve the common task while preserving salient individual values.
- **Predicted behavior:** the aligned arrangement will improve reliable deployment relative to the earlier missing/misaligned state: more intended specialist actions completed at assigned targets/times, fewer failed handoffs, or fewer missing required resources. A capable institution/domain expert can supply the arrangement. Where it has not been supplied, Kazuma will more often initiate or repair it; where another actor supplies it, successful deployment need not depend on his continuing direction. Score deployment improvement, alternative-provider adequacy and Kazuma's comparative contribution separately. A concealed target relationship or misaligned reward can still disrupt a technically sound plan.
- **Interaction tendency:** directives, signaling, handoffs and corrections will make the practical arrangement visible; do not infer organization merely from eventual victory.
- **Confidence:** HIGH for the bounded deployment mechanism; no universal necessity or sufficiency theorem is claimed.
- **Evidence basis:** CP03-E01; V07/V08 MG02-E01; V09 contrast `0011:P0120–0271` with `0014:P0054–0110`, `P0199–0258`; relational failure `0014:P0365–0419`.
- **Disconfirmation:** across comparable multi-stage problems, explicit alignment produces no improvement in deployment, or specialist availability alone repeatedly yields equally reliable safe task completion without observable coordination; also adverse is persistent dependence on Kazuma despite an alternative arrangement independently shown to supply the required roles, resources and handoffs.
- **Outcome:**
- **Adjudication:**

### MG03-E02 — Durable efficient separation incurs attachment costs
- **Trigger/context:** a feasible reorganization promises practical efficiency but credibly removes an established core party/home relationship for a sustained period.
- **Relationship/stakes:** established members, meaningful permanence; ordinary raids, errands, a night out or romantic awkwardness alone do not qualify.
- **Predicted appraisal:** the proposal loses something valued beyond instrumental usefulness.
- **Predicted dominant motive:** retain relationship, membership or meaningful contact.
- **Predicted behavior:** one or more core members will resist, bargain, return, protect contact or bear a cost to preserve the bond. Ordinary insults need not soften and temporary tactical separation can remain acceptable.
- **Interaction tendency:** relationship/home language and practical restoration attempts are stronger evidence than generic declarations that everyone is friends.
- **Confidence:** HIGH, based on the direct V07 test and supporting household behavior.
- **Evidence basis:** CP03-E02; V07 MG02-K04/E02; V09 `0010:P0343–0374`, `0014:P0549–0551`, `0015:P0017–0026` provide non-test supporting evidence.
- **Disconfirmation:** durable efficient separation is accepted with sustained relief and little attachment cost despite feasible ways to preserve the established relationship.
- **Outcome:**
- **Adjudication:**

## Japanese voice and humor

### MG03-J01 — Register tracks an independently established active role
- **Trigger/context:** a scene independently establishes a change in duty, identity, vulnerability or relationship stakes, and gives enough dialogue/narration for a local before/after comparison.
- **Relationship/stakes:** identify speaker, addressee, audience and role from action or explicit semantic commitment before scoring the surface wording. A commitment's semantic content may establish the role, but its formal wording may not simultaneously establish that role and serve as the successful language outcome.
- **Predicted appraisal/motive:** the active role supplies the terms through which the speaker seeks authority, safety, recognition or care.
- **Predicted behavior and voice:** the following mappings predict directions of change: Megumin's challenged specialist identity increases specialist self-identification and competitive assertion; personal gratitude or vulnerable appeal increases direct relational address/request. Aqua's service authority increases practical directives, while divine-status contest increases self-legitimation and demands for acknowledgment. Darkness's public duty increases institutional/protector framing; dignity threats increase direct objection; belonging insecurity increases requests for acceptance. Kazuma's companion-care turn increases questions, ordinary offers or self-disclosure relative to immediate grievance/reward rhetoric.
- **Coding rule:** before classifying the language outcome, record the independently evidenced role, select the applicable mapping and fix the local comparison window around the semantic change. Score each mapping separately. Keep the assignment when unchanged or opposing wording appears; it is adverse evidence. Insufficient comparable speech is NOT_TESTED. Neutral connective speech and exact lexical choices are not themselves outcomes.
- **Confidence:** HIGH for role conditioning; no deterministic sentence-ending or catchphrase rule.
- **Evidence basis:** CP03-J01; V07/V08 MG02-J01; V09 `0011:P0478–0486`, `0013:P0082–0104`, `0014:P0054–0094`, `P0459–0484`, `P0534–0544`, `P0784–0815`.
- **Disconfirmation:** repeated matched role changes yield unchanged or opposite patterns to the fixed mapping, or apparent fit depends on inventing/reassigning a role after seeing the wording. One confirmed mapping cannot conceal adverse results in another.
- **Outcome:**
- **Adjudication:**

### MG03-J02 — Comic episodes are predominantly portable or pragmatic
- **Trigger/context:** a census of qualifying comic episodes in the complete authorized V10–V12 main narratives, pooled across the tranche. Per-volume patterns are reported separately, but the formal prediction concerns the pooled set.
- **Relationship/stakes:** no character-specific condition. Identify episode eligibility and boundaries independently of L-class. Include verbal/written-form episodes and recurrent gags even when the only consequence is an immediate response or narrator retort; brevity alone is not an exclusion.
- **Inclusion/segmentation rule:** an episode presents an expectation or stance and a comic reversal, violation, contrast or response. A continuous run around the same premise counts once, including nested jokes; a later callback counts separately only when a new scene supplies its own setup/response. Record every eligible episode with its source locator before assigning the primary mechanism. Do not select only action-based or plot-consequential scenes.
- **Predicted appraisal/motive:** not applicable to a single character; this is a distributional literary prediction.
- **Predicted effect:** more than half the eligible episodes will have a primary comic mechanism preserved through situation, causal reversal, timing, role or ordinary register/pragmatic equivalents (L0–L2), rather than requiring Japanese-specific reconstruction or annotation (L3).
- **Classification/scoring boundary:** log clear L0–L2, clear L3, mixed and uncertain cases separately. For a completed nonempty census, CONFIRMED requires clear L0–L2 cases to exceed half of all eligible episodes even assigning every unresolved case to L3. FALSIFIED applies when L0–L2 cannot exceed half even assigning every unresolved case to L0–L2; this includes a fully resolved tie. AMBIGUOUS applies when unresolved cases can change whether the strict majority is reached. An empty eligible set is NOT_TESTED. Incomplete census permits only PARTIAL qualitative reporting, not a tranche frequency claim. Cultural dependence is flagged separately. This new frequency test does not retroactively quantify Gen02's qualitative major-sequence judgment.
- **Confidence:** MODERATE for this more explicitly operationalized test, based on prior qualitative evidence.
- **Evidence basis:** CP03-J02; V07/V08 MG02-J02; V09 deep reading §§7–8. Written-form `お守り`: `0010:P0061`, `P0081–0083`, `P0116–0118` (L3). Additive `も`: `0014:P0179`, `P0537` (chiefly L2, exact-wording sensitivity); this serious recognition payoff is not added to the humor census merely because it is linguistically important.
- **Disconfirmation:** the completed census establishes failure of the strict L0–L2 majority under the bound rule above, including a fully resolved tie. A result achieved only by excluding short form-dependent episodes or changing boundaries after classification is invalid evidence, not confirmation.
- **Outcome:**
- **Adjudication:**

## Secondary reconstruction candidates

### MG03-Y01 — Inclusion and a useful role recruit Yunyun's competent participation
- **Trigger/context:** trusted companions explicitly include Yunyun in a shared undertaking, including accepting her offer to join, and give her access to a role suited to her established magic or practical knowledge.
- **Relationship/stakes:** a real invitation/role rather than a hypothetical promise; distinguish desire for company from agreement with every action of the group.
- **Predicted appraisal:** she can belong by making a useful contribution.
- **Predicted dominant motive:** participate and help while preserving the valued connection.
- **Predicted behavior:** she will prepare and carry out the relevant role despite awkwardness or anxiety, sometimes overpreparing or overoffering. Moral or relational distress may produce objections without immediately ending participation; distress or interrupted commitment under a directly conflicting personal obligation remains context to record; it is not automatically a failed technical execution.
- **Interaction tendency:** hesitant acceptance can coexist with technically effective direction and explicit disagreement.
- **Confidence:** MODERATE-HIGH for affiliation-mediated participation; not a mature full-character model.
- **Evidence basis:** CP03-Y01; V07 deep reading / relationship ledger Yunyun support; V09 `0011:P0641–0658`, `0012:P0152–0160`, `0013:P0154–0156`, `0014:P0199–0242`, `P0305–0310`, `P0378–0391`, `P0459–0467`, `0015:P0025–0026`.
- **Disconfirmation:** repeated genuine invitations with feasible familiar roles produce sustained indifferent refusal or poor participation unrelated to a documented conflicting obligation, ability/resource limit or coercive condition.
- **Outcome:**
- **Adjudication:**

### MG03-CE01 — Conscientious service can exceed Chris/Eris's preferred burden
- **Trigger/context:** in her public divine/service role, Chris/Eris receives sincere requests whose cumulative burden exceeds what she explicitly prefers, and a refusal or exit is possible.
- **Relationship/stakes:** distinguish publicly owed duty from casual trusted companionship; identify her own expressed burden, not an observer's assumption that she must be tired.
- **Predicted appraisal:** refusal would disappoint people who reasonably seek her help.
- **Predicted dominant motive:** meet sincere obligations.
- **Predicted behavior:** she will tend to continue past her preferred burden until a boundary is negotiated or another actor supplies an exit. A successful self-set boundary is adverse evidence for the over-compliance tendency and should not be reclassified as its confirmation.
- **Interaction tendency:** service politeness may differ from the familiar Chris register she asks trusted companions to use.
- **Confidence:** MODERATE; chiefly a V08 discovery with no V09 replication.
- **Evidence basis:** CP03-CE01; unchanged DISC-V08-04 and V08 Chris/Eris findings; V09 absence supplies no additional validation.
- **Disconfirmation:** repeated matched cumulative burdens elicit timely, comfortable self-limitation without significant conflict or externally created relief.
- **Outcome:**
- **Adjudication:**

### MG03-I01 — Safe nondeferential interaction expands Iris's agency
- **Trigger/context:** Iris is directly shown with a trusted person who treats her as an ordinary younger peer in a setting with less formal royal surveillance.
- **Relationship/stakes:** compare her behavior with an observed constrained public context; a letter alone does not supply the contrast.
- **Predicted appraisal:** ordinary curiosity, experimentation and wants can be expressed without immediate royal correction.
- **Predicted dominant motive:** learn, play or exercise age-appropriate agency.
- **Predicted behavior:** curiosity, informal strategy learning, competition or ordinary requests will become more visible than in the constrained setting.
- **Interaction tendency:** familiar address and less inhibited interaction may accompany the behavioral change; honorifics alone do not prove the mechanism.
- **Confidence:** MODERATE-HIGH as inherited from V06; V07–V09 provide no matched test.
- **Evidence basis:** CP03-I01; V04–V06 checkpoint §10 and unchanged MG02-I01; V09 `0016:P0035–0040` only preserves the letter boundary.
- **Disconfirmation:** repeated safe nondeferential settings leave her equally constrained, with no predicted behavioral expansion despite available ordinary choices.
- **Outcome:**
- **Adjudication:**

### MG03-I02 — An expressed wish may be narrowed by understood royal duty
- **Trigger/context:** the source directly establishes both a personal wish of Iris's and a royal obligation she understands as conflicting with it.
- **Relationship/stakes:** genuine duty conflict; do not infer an unwanted obligation or hidden wish merely from formal engagement, travel or an escort request.
- **Predicted appraisal:** the larger personal wish exceeds what the role permits.
- **Predicted dominant motive:** preserve duty while obtaining a smaller part of the desired freedom or connection.
- **Predicted behavior:** she will tend to self-limit or choose a reduced request while the original wish remains expressed or otherwise directly evidenced.
- **Interaction tendency:** restrained petition may coexist with familiar attachment language; the source must establish the motive rather than the analyst supplying it.
- **Confidence:** MODERATE-HIGH as inherited from V06; still unvalidated in V07–V09.
- **Evidence basis:** CP03-I01; V04–V06 checkpoint §10 and unchanged MG02-I02; V09 `0016:P0036–0041` is not a matched decision.
- **Disconfirmation:** repeated explicit wish/duty conflicts produce unconstrained prioritization of the wish without meaningful conflict or self-limitation, despite understood obligations.
- **Outcome:**
- **Adjudication:**

## Gen 0.3 freeze state

These 25 predictions are the complete Gen 0.3 set for V10–V12. No outcome or adjudication field above is populated. V10 remains unopened in this session. The next analyst must retrieve and preserve this exact block before the first V10 narrative exposure and append evidence without rewriting its triggers, confidence, boundaries or disconfirmation language.
