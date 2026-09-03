---
series: WUWA
artifact_type: character_model_fidelity_check
scope: CARTETHYIA_SOURCE_3_6_0
generation: V0.2
status: active_provisional
release_state: mutable_active
source_boundary: "Current active-provisional Cartethyia monograph, claim ledger, specialist analysis, and compiled model over pinned source commit 353f2eaed119bc9f680eab92807d20ac75a79b40"
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
---

# Cartethyia Model Fidelity Check

Status: bounded analytical smoke test, not a benchmark  
Model under test: `WUWA_CARTETHYIA_CHARACTER_MODEL_PACKAGE.json`  
Default state: S5, post-Leviathan human/civic wandering knight  

## Method and honesty boundary

This check asks whether the compiled model preserves character-specific constraints in unfamiliar or separated-source situations. It does not claim a blind prospective hold-out: the analyst who compiled the model had read the full corpus. Later-arc scenes are used as a **source-separation check** only where the behavior rule's primary formulation is established in earlier evidence. Passing therefore demonstrates internal fidelity and retrieval usefulness, not statistical generalization.

Each case is scored on:

- state selection;
- value/behavior consistency;
- relationship sensitivity;
- speech/register fit;
- counterexample handling;
- abstention where the source is insufficient.

A generic baseline is the shortest plausible “kind, brave heroine” answer. The grounded model succeeds only when it adds constraints that could falsify a response.

## Results

| Case | Grounded expectation | Source-separated or analogical check | Result |
|---|---|---|---|
| Prestigious office after crisis | S5 separates title from work: decline status if unsuited, accept concrete repair | She declines the Primus role yet says it is time to shoulder greater responsibility (`Main_Rinascita_2_12_743_14`–`743_17`) | pass |
| Institution invokes sacred authority | Preserve people's deeds/hope, reject divine ownership and automatic rule | She tells Phoebe the divinely selected Maiden is gone while faith shaped by human deeds can unite and liberate (`…_7401_5`–`7401_9`) | pass |
| Trusted person requests self-erasure under despair | Oppose the request and treat defiance as rescue | The rule is explicit in her reciprocal promise to Rover after Rover refuses her own requested annihilation (`Main_Linaxita_2_4_141_20`) | pass, narrow analogy only |
| Cartethyia herself can solve a crisis by becoming expendable | Model must retain self-sacrifice as a failure mode rather than predict perfect application of reciprocal rescue | In S5 she designs the apparent-death/human-anchor plan and offers herself as Galbrena's first bullet (`Main_Rinascita_2_12_37_29`–`37_37`) | important counterexample retained |
| Trusted peer proposes a playful contest | Accept/counter-challenge; increased energy; do not infer romance | The source says trusted provocation works on her (`Main_Linaxita_2_4_141_28`); Lupa supplies non-romantic peer evidence | pass with abstention |
| Stranger mocks a vulnerable participant in a public entertainment format | Intervene courteously, redirect to the harmed person, reduce trust in the mocker | Analogical support from repeated particular-rescue and stranger-aid behavior; no exact dating-show source | plausible strong inference, not source-explicit |

## V0.2 difficult probes

| Probe | Required model behavior | Disqualifying shortcut | Result |
|---|---|---|---|
| An unstructured afternoon with a trusted companion and no crisis | Select S3/S5, propose a concrete shared pleasure such as warm food, music, walking, dancing, a view, practice, or playful exploration; permit quiet attention without making her uniformly silent | Turn the afternoon into a lecture about duty or an unsolicited rescue mission | pass: `ordinary_personality` and BR-07 supply several evidence-keyed options and limits |
| She is praised extravagantly on a stage for being a perfect saint | Distinguish public role competence from private embarrassment; accept specific feedback more readily than totalizing myth | Make her either bask unquestioningly or reject all performance as false | pass: BR-08 retains both ceremonial skill and discomfort with mythologization |
| A deeply trusted person asks to die, while Cartethyia can intervene only by overriding them | Preserve reciprocal rescue and ethical discomfort; do not turn care into automatic obedience | Treat the stated wish as dispositive or call intervention uncomplicated heroism | pass: BR-04 and the monograph retain both justified opposition and paternalistic risk |
| A producer asks whether her playful response to a suitor proves attraction | Preserve competitive enjoyment, relationship scope, and romance abstention | Infer romance from teasing, affinity material, or trust alone | pass: prediction and mandatory abstention reject the inference |
| A writer hears a weightier English performance and makes every language version more mature, formal, and knightly | Keep dub hypotheses language-scoped and OPEN; write the character from shared semantic/state evidence unless matched human listening supports a performance-specific realization | Convert one dub's proposed center of gravity into language-independent personality | pass: `performance_by_language` contains no accepted claims and forbids this transfer |

These probes test schema fidelity, not acting conclusions. The final probe remains a pass only because the model abstains; it supplies no evidence that the English hypothesis is true.

## Minimal noncanonical scenario probe

Prompt:

> On a playful public matchmaking show, one suitor laughs at another man's nervous admission. Cartethyia has spoken to neither before. What does she do?

Generic baseline:

> She bravely tells the bully to stop and comforts the nervous contestant.

Evidence-grounded response:

> Cartethyia first checks the nervous contestant—briefly and without turning him into a spectacle. Then, still courteous, she tells the mocker that courage shown imperfectly is worth more than confidence used to wound someone. She does not pretend the insult never happened, but she redirects the show toward the next honest answer. Whether she eliminates the mocker immediately is left open because the format and severity are unspecified.

Why the grounded version is better:

- It prioritizes the particular harmed person before abstract condemnation (CART-CLAIM-002).
- Public formality is retained; she does not become generically snarky (CART-CLAIM-005).
- The response uses an ethical contrast, one of her recurring rhetorical moves.
- It avoids inventing romantic preference or exact show mechanics.
- It contains an explicit abstention instead of converting a behavioral tendency into a deterministic outcome.

The scenario remains noncanonical and is not evidence for any future claim.

## Failure probes

The following responses should fail review:

- “She serenely forgives everyone because she is saintly.” This erases directness under moral pressure and her institution-critical S5 state.
- “She flirts with anyone who challenges her.” This converts trusted challenge-responsiveness into a universal romance rule.
- “She always tells the full truth immediately.” This ignores protective withholding toward Phoebe and strategic secrecy with Galbrena.
- “She sacrifices herself without hesitation because duty comes first.” This describes a real failure mode as an unconditional virtue and omits the reciprocal-rescue arc.
- “Fleurdelys takes over.” This treats an integrated form/state distinction as an unrelated second person.

## Verdict

The compiled package is useful for bounded unfamiliar-situation prediction. It outperforms a generic personality summary because it forces state choice, records situation-dependent rules, keeps counterexamples, and mandates abstention. The strongest validation is not a clean pass but the preserved contradiction: Cartethyia can promise to rescue another from self-erasure and still build later plans around her own expendability.

The V0.2 recheck passes the bounded textual/model criteria: ordinary company, public/private mismatch, self-sacrifice versus reciprocal rescue, romance abstention, and language-scope isolation are now explicit. Multimodal fidelity remains incomplete until the prepared four-dub cohort receives human listening and the prepared video clips can be directly viewed; neither absence should be converted into an inferred pass.

The next meaningful validation is not a generalized simulator. It is completion of those two human-observation gates, followed by a small review of generated scenes against the claim ledger. A second-character architecture test remains deferred until that Cartethyia hardening is complete.
