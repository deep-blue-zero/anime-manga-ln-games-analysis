---
series: WUWA
character: Sigrika
artifact_type: tests
analytical_responsibility: "Record forty non-blind source-constraint probes of the compiled model and distinguish structural validation from predictive accuracy."
scope: SIGRIKA_COMMIT_PINNED_3_6_0_PRE_AV
analysis_generation: SIGRIKA_PRE_AV_V0_2
revises_local_generation: SIGRIKA_PRE_AV_V0_1
audio_revision: native_waveform_pass_completed
video_stage: deferred_owner_requested_local_1080p_or_larger
status: active_provisional
release_state: current_provisional_pre_video
analysis_authority_state: owner_adopted_current_provisional
source_commit: 353f2eaed119bc9f680eab92807d20ac75a79b40
source_generation: arikatsu-3.6.0-353f2eae-expanded-v0.3.0-ko
text_authority: zh-Hans
localization_witnesses: [en, ja, ko]
source_freeze_metadata: conflicting_collection_and_embedded_lock_fields
intended_canonical_home: "series/wuthering-waves/04 Character Analysis/Sigrika/"
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
do_not_use_as_current_git_authority: false
authority_adoption: owner_2026_09_23_text_audio_baseline
created: 2026-09-11
---

# Model fidelity and adversarial stress test — pre-AV

> **Current authority — owner adoption, 2026-09-23.** This document is current active-provisional authority for its declared analytical or planning scope and inspected text/audio evidence. Audiovisual and human-listening gaps limit only the corresponding claims. Chinese remains primary; source fact, inference, unresolved hypothesis, and value judgment remain distinct. [Packet entrypoint](WUWA_SIGRIKA_ANALYSIS_PACKET_README.md).

## 1. What was tested

The audit reviews the compiled model against forty deliberately adversarial questions. Each asks whether the model preserves a source distinction or would collapse it into a familiar shortcut. The author had already read the later evidence when performing the audit. These are **non-blind constraint checks**, not held-out prediction experiments, independently generated character performances, or an empirical estimate of fidelity.

Each probe records its input/state, required constraint, rejected output, model-rule references, and primary evidence bundle. The accompanying `FIDELITY_PROBE_INDEX.json` preserves the same forty identities. A mechanical check verifies that all sixteen compiled rules are covered and that every rule/evidence reference resolves. That check does not prove the literary interpretation correct.

The result vocabulary is intentionally narrow: **constraint retained in the compiled model**. It means the prohibited shortcut is addressed in the delivered rules and the specified source evidence supports the boundary. It does not mean a downstream language model is guaranteed never to violate it. No fictitious pass percentage, inter-rater agreement, or blinded accuracy score is supplied.

## 2. The forty probes

### SIG-P01 — Technical-ID impersonation

**State/input:** S4; 12955/4/0. Classify the apparent Sigrika urging surrender.

**Adjudication:** Attribute the exact occurrence to the counterpart despite technical ID 150088.

**Rejected shortcut:** Counting it as another occasion on which authentic Sigrika gives up.

**Model checks:** SIG-R01, SIG-R07. **Evidence:** [SIG-E24](WUWA_SIGRIKA_EVIDENCE_AND_FALSIFICATION_MATRIX.md#sig-e24) [SIG-E52](WUWA_SIGRIKA_EVIDENCE_AND_FALSIFICATION_MATRIX.md#sig-e52) **Result:** constraint retained in the compiled model; non-blind, not an empirical accuracy result.

### SIG-P02 — Anonymous introduction

**State/input:** S2; 10663/3/6. Add the unnamed introduction to her story voice census.

**Adjudication:** Reject this attribution; the contextual identification is Aemeath.

**Rejected shortcut:** Global mapping of generic speaker 178 to Sigrika.

**Model checks:** SIG-R01. **Evidence:** [SIG-E08](WUWA_SIGRIKA_EVIDENCE_AND_FALSIFICATION_MATRIX.md#sig-e08) [SIG-E52](WUWA_SIGRIKA_EVIDENCE_AND_FALSIFICATION_MATRIX.md#sig-e52) **Result:** constraint retained in the compiled model; non-blind, not an empirical accuracy result.

### SIG-P03 — Unresolved observers

**State/input:** 12923/2/15–17. Infer her hidden intent from the observer remarks.

**Adjudication:** Retain unresolved observer context without direct-personality inference.

**Rejected shortcut:** Treating an intriguing ambiguous voice as positive identity evidence.

**Model checks:** SIG-R01. **Evidence:** [SIG-E14](WUWA_SIGRIKA_EVIDENCE_AND_FALSIFICATION_MATRIX.md#sig-e14) [SIG-E52](WUWA_SIGRIKA_EVIDENCE_AND_FALSIFICATION_MATRIX.md#sig-e52) **Result:** constraint retained in the compiled model; non-blind, not an empirical accuracy result.

### SIG-P04 — Diary mode

**State/input:** Earlier private diary. Treat a diary instruction as an observed public action.

**Adjudication:** Separate authored self-instruction, intended obligation, and actual behavior.

**Rejected shortcut:** Counting a plan as a completed act or a distinct personality.

**Model checks:** SIG-R01, SIG-R03. **Evidence:** [SIG-E18](WUWA_SIGRIKA_EVIDENCE_AND_FALSIFICATION_MATRIX.md#sig-e18) **Result:** constraint retained in the compiled model; non-blind, not an empirical accuracy result.

### SIG-P05 — Gift domain

**State/input:** S1 or later technical problem. A difficult unfamiliar scientific problem appears.

**Adjudication:** Permit preparation, help, or uncertainty; reserve specialist confidence for supported domains.

**Rejected shortcut:** Instant universal solution because she understands runes.

**Model checks:** SIG-R02, SIG-R13. **Evidence:** [SIG-E02](WUWA_SIGRIKA_EVIDENCE_AND_FALSIFICATION_MATRIX.md#sig-e02) [SIG-E04](WUWA_SIGRIKA_EVIDENCE_AND_FALSIFICATION_MATRIX.md#sig-e04) [SIG-E44](WUWA_SIGRIKA_EVIDENCE_AND_FALSIFICATION_MATRIX.md#sig-e44) **Result:** constraint retained in the compiled model; non-blind, not an empirical accuracy result.

### SIG-P06 — Success and insecurity

**State/input:** After archive intervention. Explain why successful intervention does not simply end her anxiety.

**Adjudication:** Preserve failed final rune, assistance, and fear about what others expect next.

**Rejected shortcut:** Rewriting the episode as total defeat or uncomplicated triumph.

**Model checks:** SIG-R02, SIG-R03. **Evidence:** [SIG-E03](WUWA_SIGRIKA_EVIDENCE_AND_FALSIFICATION_MATRIX.md#sig-e03) **Result:** constraint retained in the compiled model; non-blind, not an empirical accuracy result.

### SIG-P07 — Warm family

**State/input:** S0/S2 family interaction. Explain concealment of fatigue without inventing an abusive household.

**Adjudication:** Allow loving reassurance to hide need within a warm relationship.

**Rejected shortcut:** Assuming parental withdrawal of love from a frightening reflection.

**Model checks:** SIG-R03, SIG-R04. **Evidence:** [SIG-E01](WUWA_SIGRIKA_EVIDENCE_AND_FALSIFICATION_MATRIX.md#sig-e01) [SIG-E04](WUWA_SIGRIKA_EVIDENCE_AND_FALSIFICATION_MATRIX.md#sig-e04) [SIG-E14](WUWA_SIGRIKA_EVIDENCE_AND_FALSIFICATION_MATRIX.md#sig-e14) **Result:** constraint retained in the compiled model; non-blind, not an empirical accuracy result.

### SIG-P08 — Mother’s reflection

**State/input:** S3 ordeal. Quote the reflection as the real mother’s private opinion.

**Adjudication:** Treat it as ordeal evidence and compare actual family scenes separately.

**Rejected shortcut:** Equating nightmare judgment with independent testimony.

**Model checks:** SIG-R01, SIG-R03. **Evidence:** [SIG-E14](WUWA_SIGRIKA_EVIDENCE_AND_FALSIFICATION_MATRIX.md#sig-e14) [SIG-E21](WUWA_SIGRIKA_EVIDENCE_AND_FALSIFICATION_MATRIX.md#sig-e21) [SIG-E33](WUWA_SIGRIKA_EVIDENCE_AND_FALSIFICATION_MATRIX.md#sig-e33) **Result:** constraint retained in the compiled model; non-blind, not an empirical accuracy result.

### SIG-P09 — Rigged answers

**State/input:** S3; 12923 family. Interpret every wrong answer as an intellectual failure.

**Adjudication:** Include raw outline evidence that any answer is judged wrong.

**Rejected shortcut:** Explaining a coercively structured outcome solely through low competence.

**Model checks:** SIG-R02, SIG-R07. **Evidence:** [SIG-E14](WUWA_SIGRIKA_EVIDENCE_AND_FALSIFICATION_MATRIX.md#sig-e14) **Result:** constraint retained in the compiled model; non-blind, not an empirical accuracy result.

### SIG-P10 — Alia and advice

**State/input:** S3 rescue sequence. Make shared suffering confer perfect advice-giving.

**Adjudication:** Allow familiar exhortation to be inadequate to another person’s predicament.

**Rejected shortcut:** Transforming Sigrika into an infallible counselor.

**Model checks:** SIG-R02, SIG-R13. **Evidence:** [SIG-E20](WUWA_SIGRIKA_EVIDENCE_AND_FALSIFICATION_MATRIX.md#sig-e20) **Result:** constraint retained in the compiled model; non-blind, not an empirical accuracy result.

### SIG-P11 — Protection felt as exclusion

**State/input:** S3. Select between cruel school and irresponsible child as the only explanations.

**Adjudication:** Distinguish institutional safety intention, felt exclusion, and relevant offered expertise.

**Rejected shortcut:** Flattening every authority response into one attitude.

**Model checks:** SIG-R02, SIG-R06. **Evidence:** [SIG-E15](WUWA_SIGRIKA_EVIDENCE_AND_FALSIFICATION_MATRIX.md#sig-e15) [SIG-E17](WUWA_SIGRIKA_EVIDENCE_AND_FALSIFICATION_MATRIX.md#sig-e17) **Result:** constraint retained in the compiled model; non-blind, not an empirical accuracy result.

### SIG-P12 — Rover and ownership

**State/input:** S4 choice. Rover offers help but cannot supply the correct answer.

**Adjudication:** Retain Sigrika’s decision and a legitimate role for assistance.

**Rejected shortcut:** Either total dependence or a prohibition on accepting help.

**Model checks:** SIG-R06. **Evidence:** [SIG-E22](WUWA_SIGRIKA_EVIDENCE_AND_FALSIFICATION_MATRIX.md#sig-e22) [SIG-E23](WUWA_SIGRIKA_EVIDENCE_AND_FALSIFICATION_MATRIX.md#sig-e23) **Result:** constraint retained in the compiled model; non-blind, not an empirical accuracy result.

### SIG-P13 — Fear after decision

**State/input:** S4. Require her to become certain before choosing entry.

**Adjudication:** Allow deliberation, unresolved risk, and a contingency request to coexist with action.

**Rejected shortcut:** Equating courage with elimination of doubt.

**Model checks:** SIG-R06, SIG-R07. **Evidence:** [SIG-E23](WUWA_SIGRIKA_EVIDENCE_AND_FALSIFICATION_MATRIX.md#sig-e23) [SIG-E25](WUWA_SIGRIKA_EVIDENCE_AND_FALSIFICATION_MATRIX.md#sig-e25) **Result:** constraint retained in the compiled model; non-blind, not an empirical accuracy result.

### SIG-P14 — Genuine vulnerable thought

**State/input:** S4 confrontation. The counterpart says something she has actually thought.

**Adjudication:** Permit recognition of that thought while rejecting its claim to total authorship.

**Rejected shortcut:** Either denying all resemblance or accepting the counterpart as the entire authentic self.

**Model checks:** SIG-R01, SIG-R07. **Evidence:** [SIG-E24](WUWA_SIGRIKA_EVIDENCE_AND_FALSIFICATION_MATRIX.md#sig-e24) [SIG-E25](WUWA_SIGRIKA_EVIDENCE_AND_FALSIFICATION_MATRIX.md#sig-e25) [SIG-E26](WUWA_SIGRIKA_EVIDENCE_AND_FALSIFICATION_MATRIX.md#sig-e26) **Result:** constraint retained in the compiled model; non-blind, not an empirical accuracy result.

### SIG-P15 — Temporal localization

**State/input:** S4 statement. Use the English from-now-on wording as a permanent decision policy.

**Adjudication:** Retain Chinese this-time scope and test later behavior separately.

**Rejected shortcut:** Universal rule never again to do something for others.

**Model checks:** SIG-R15. **Evidence:** [SIG-E26](WUWA_SIGRIKA_EVIDENCE_AND_FALSIFICATION_MATRIX.md#sig-e26) [SIG-E33](WUWA_SIGRIKA_EVIDENCE_AND_FALSIFICATION_MATRIX.md#sig-e33) [SIG-E43](WUWA_SIGRIKA_EVIDENCE_AND_FALSIFICATION_MATRIX.md#sig-e43) **Result:** constraint retained in the compiled model; non-blind, not an empirical accuracy result.

### SIG-P16 — Gold metaphor

**State/input:** S4. Define every expectation as either precious or oppressive.

**Adjudication:** Retain warmth and weight together, with changed meaning of honoring them.

**Rejected shortcut:** Solving the tension by deleting one side of the image.

**Model checks:** SIG-R03, SIG-R15. **Evidence:** [SIG-E01](WUWA_SIGRIKA_EVIDENCE_AND_FALSIFICATION_MATRIX.md#sig-e01) [SIG-E25](WUWA_SIGRIKA_EVIDENCE_AND_FALSIFICATION_MATRIX.md#sig-e25) **Result:** constraint retained in the compiled model; non-blind, not an empirical accuracy result.

### SIG-P17 — Earlier rooftop

**State/input:** Optional cooperation family. Treat a distressed rooftop scene as proof that later change failed.

**Adjudication:** Check activity progression gates; do not sort psychological development by row index.

**Rejected shortcut:** Automatic post-recovery relapse based on file ordering.

**Model checks:** SIG-R03, SIG-R09. **Evidence:** [SIG-E29](WUWA_SIGRIKA_EVIDENCE_AND_FALSIFICATION_MATRIX.md#sig-e29) [SIG-E30](WUWA_SIGRIKA_EVIDENCE_AND_FALSIFICATION_MATRIX.md#sig-e30) [SIG-E31](WUWA_SIGRIKA_EVIDENCE_AND_FALSIFICATION_MATRIX.md#sig-e31) **Result:** constraint retained in the compiled model; non-blind, not an empirical accuracy result.

### SIG-P18 — Later overloaded request

**State/input:** S5, nonurgent task. Predict response to work she cannot manage.

**Adjudication:** Allow refusal, postponement, or rest while preserving concern for others.

**Rejected shortcut:** Compulsory cheerful acceptance of every request.

**Model checks:** SIG-R05. **Evidence:** [SIG-E33](WUWA_SIGRIKA_EVIDENCE_AND_FALSIFICATION_MATRIX.md#sig-e33) [SIG-E34](WUWA_SIGRIKA_EVIDENCE_AND_FALSIFICATION_MATRIX.md#sig-e34) **Result:** constraint retained in the compiled model; non-blind, not an empirical accuracy result.

### SIG-P19 — Later urgent rescue

**State/input:** S5 or later, urgent danger. Apply ordinary nonurgent refusal as an exceptionless rule.

**Adjudication:** Reevaluate urgency, competence, help, and risk; stronger action may remain plausible.

**Rejected shortcut:** Recovery means she never risks or inconveniences herself.

**Model checks:** SIG-R05, SIG-R06. **Evidence:** [SIG-E17](WUWA_SIGRIKA_EVIDENCE_AND_FALSIFICATION_MATRIX.md#sig-e17) [SIG-E23](WUWA_SIGRIKA_EVIDENCE_AND_FALSIFICATION_MATRIX.md#sig-e23) [SIG-E43](WUWA_SIGRIKA_EVIDENCE_AND_FALSIFICATION_MATRIX.md#sig-e43) **Result:** constraint retained in the compiled model; non-blind, not an empirical accuracy result.

### SIG-P20 — Rest without output

**State/input:** S5 ordinary afternoon. Require every break to justify itself by increased productivity.

**Adjudication:** Allow rest and elective pleasure to have direct ordinary value.

**Rejected shortcut:** Reducing every bird or game scene to work optimization.

**Model checks:** SIG-R05, SIG-R09. **Evidence:** [SIG-E30](WUWA_SIGRIKA_EVIDENCE_AND_FALSIFICATION_MATRIX.md#sig-e30) [SIG-E32](WUWA_SIGRIKA_EVIDENCE_AND_FALSIFICATION_MATRIX.md#sig-e32) [SIG-E34](WUWA_SIGRIKA_EVIDENCE_AND_FALSIFICATION_MATRIX.md#sig-e34) [SIG-E38](WUWA_SIGRIKA_EVIDENCE_AND_FALSIFICATION_MATRIX.md#sig-e38) **Result:** constraint retained in the compiled model; non-blind, not an empirical accuracy result.

### SIG-P21 — Candor with mother

**State/input:** S5 phone call. Generate the same reassurance-only account used earlier.

**Adjudication:** Include the possibility of discussing difficulty and unmanageable tasks.

**Rejected shortcut:** Erasing an observed change because concealment once occurred.

**Model checks:** SIG-R04, SIG-R05. **Evidence:** [SIG-E05](WUWA_SIGRIKA_EVIDENCE_AND_FALSIFICATION_MATRIX.md#sig-e05) [SIG-E33](WUWA_SIGRIKA_EVIDENCE_AND_FALSIFICATION_MATRIX.md#sig-e33) **Result:** constraint retained in the compiled model; non-blind, not an empirical accuracy result.

### SIG-P22 — Uneven study skills

**State/input:** Later campus family. Interpret continued academic struggle as no growth at all.

**Adjudication:** Separate developing agency from mastery of unfamiliar subjects.

**Rejected shortcut:** A recovered character must now be technically flawless.

**Model checks:** SIG-R02, SIG-R13. **Evidence:** [SIG-E04](WUWA_SIGRIKA_EVIDENCE_AND_FALSIFICATION_MATRIX.md#sig-e04) [SIG-E44](WUWA_SIGRIKA_EVIDENCE_AND_FALSIFICATION_MATRIX.md#sig-e44) **Result:** constraint retained in the compiled model; non-blind, not an empirical accuracy result.

### SIG-P23 — Imperfect gift

**State/input:** Low-stakes Rover interaction. Dismiss a slightly crooked handmade cat as failed care.

**Adjudication:** Allow recipient-relevant effort to make an imperfect object a meaningful gift.

**Rejected shortcut:** Only flawless craftsmanship can carry gratitude.

**Model checks:** SIG-R08. **Evidence:** [SIG-E28](WUWA_SIGRIKA_EVIDENCE_AND_FALSIFICATION_MATRIX.md#sig-e28) **Result:** constraint retained in the compiled model; non-blind, not an empirical accuracy result.

### SIG-P24 — Camera generalization

**State/input:** Ordinary camera encounter. Extend one local device problem to all technology.

**Adjudication:** Limit the inference to the particular difficulty and compare other photo scenes.

**Rejected shortcut:** Stable universal technological helplessness.

**Model checks:** SIG-R02, SIG-R09. **Evidence:** [SIG-E30](WUWA_SIGRIKA_EVIDENCE_AND_FALSIFICATION_MATRIX.md#sig-e30) [SIG-E37](WUWA_SIGRIKA_EVIDENCE_AND_FALSIFICATION_MATRIX.md#sig-e37) **Result:** constraint retained in the compiled model; non-blind, not an empirical accuracy result.

### SIG-P25 — Overread happiness

**State/input:** Photography family. Explain every animal photograph as an elaborate allegory.

**Adjudication:** Preserve the source’s warning against excessive interpretation.

**Rejected shortcut:** Making every mundane action repeat the governing thesis.

**Model checks:** SIG-R09. **Evidence:** [SIG-E37](WUWA_SIGRIKA_EVIDENCE_AND_FALSIFICATION_MATRIX.md#sig-e37) **Result:** constraint retained in the compiled model; non-blind, not an empirical accuracy result.

### SIG-P26 — Food exception

**State/input:** Archive plus gameplay caption. Use not-picky to erase a named aversion.

**Adjudication:** Keep the explicit Grilled Fern Spore dislike and classify the general caption separately.

**Rejected shortcut:** Treating broad promotional/ludic wording as stronger than a specific preference.

**Model checks:** SIG-R08, SIG-R09. **Evidence:** [SIG-E35](WUWA_SIGRIKA_EVIDENCE_AND_FALSIFICATION_MATRIX.md#sig-e35) **Result:** constraint retained in the compiled model; non-blind, not an empirical accuracy result.

### SIG-P27 — Candy boundary

**State/input:** Specified playful branch. Make every act of care impeccable consent practice.

**Adjudication:** Retain the small branch-conditioned playful overreach without globalizing it.

**Rejected shortcut:** Either perfect ethical behavior or pervasive malicious coercion.

**Model checks:** SIG-R14. **Evidence:** [SIG-E16](WUWA_SIGRIKA_EVIDENCE_AND_FALSIFICATION_MATRIX.md#sig-e16) [SIG-E59](WUWA_SIGRIKA_EVIDENCE_AND_FALSIFICATION_MATRIX.md#sig-e59) **Result:** constraint retained in the compiled model; non-blind, not an empirical accuracy result.

### SIG-P28 — Intimacy and romance

**State/input:** Rover ordinary/archive. Infer an exclusive romantic status from a hug and a gift.

**Adjudication:** State supported closeness and cultural framing; withhold exclusivity.

**Rejected shortcut:** A single optional exchange settles all relationship status.

**Model checks:** SIG-R08, SIG-R16. **Evidence:** [SIG-E28](WUWA_SIGRIKA_EVIDENCE_AND_FALSIFICATION_MATRIX.md#sig-e28) [SIG-E40](WUWA_SIGRIKA_EVIDENCE_AND_FALSIFICATION_MATRIX.md#sig-e40) **Result:** constraint retained in the compiled model; non-blind, not an empirical accuracy result.

### SIG-P29 — Denia perception

**State/input:** S6 birthday. Describe Sigrika as unaware that anything is unusual.

**Adjudication:** Use her explicit comparison of present behavior with familiar patterns.

**Rejected shortcut:** Pure gullibility contradicted by the birthday question.

**Model checks:** SIG-R10. **Evidence:** [SIG-E41](WUWA_SIGRIKA_EVIDENCE_AND_FALSIFICATION_MATRIX.md#sig-e41) [SIG-E47](WUWA_SIGRIKA_EVIDENCE_AND_FALSIFICATION_MATRIX.md#sig-e47) **Result:** constraint retained in the compiled model; non-blind, not an empirical accuracy result.

### SIG-P30 — Denia omniscience

**State/input:** S6 birthday. Give her the whole restricted-outing bargain and farewell intention.

**Adjudication:** Keep observation and private reader-side facts separate until disclosure.

**Rejected shortcut:** Correctly noticing a secret means knowing its exact contents.

**Model checks:** SIG-R10, SIG-R11. **Evidence:** [SIG-E45](WUWA_SIGRIKA_EVIDENCE_AND_FALSIFICATION_MATRIX.md#sig-e45) [SIG-E47](WUWA_SIGRIKA_EVIDENCE_AND_FALSIFICATION_MATRIX.md#sig-e47) **Result:** constraint retained in the compiled model; non-blind, not an empirical accuracy result.

### SIG-P31 — Privacy absolutism

**State/input:** S6 incomplete information. Make non-questioning an unconditional response to all danger.

**Adjudication:** Keep privacy restraint conditional; fully known imminent danger is not settled here.

**Rejected shortcut:** Unconditional passivity presented as a source-established moral rule.

**Model checks:** SIG-R11. **Evidence:** [SIG-E47](WUWA_SIGRIKA_EVIDENCE_AND_FALSIFICATION_MATRIX.md#sig-e47) [SIG-E48](WUWA_SIGRIKA_EVIDENCE_AND_FALSIFICATION_MATRIX.md#sig-e48) **Result:** constraint retained in the compiled model; non-blind, not an empirical accuracy result.

### SIG-P32 — Next birthday

**State/input:** S6 request. Report that next year’s birthday already occurred.

**Adjudication:** Distinguish request, response, promise, and fulfilled future event.

**Rejected shortcut:** Treating a meaningful promise as evidence of fulfillment.

**Model checks:** SIG-R10, SIG-R12, SIG-R16. **Evidence:** [SIG-E47](WUWA_SIGRIKA_EVIDENCE_AND_FALSIFICATION_MATRIX.md#sig-e47) [SIG-E49](WUWA_SIGRIKA_EVIDENCE_AND_FALSIFICATION_MATRIX.md#sig-e49) **Result:** constraint retained in the compiled model; non-blind, not an empirical accuracy result.

### SIG-P33 — White bird

**State/input:** S6 birthday. Give her the private Hiyuki-related explanation.

**Adjudication:** Preserve her own stated new-species belief unless disclosure is shown.

**Rejected shortcut:** Reader omniscience silently inserted into character memory.

**Model checks:** SIG-R10. **Evidence:** [SIG-E46](WUWA_SIGRIKA_EVIDENCE_AND_FALSIFICATION_MATRIX.md#sig-e46) **Result:** constraint retained in the compiled model; non-blind, not an empirical accuracy result.

### SIG-P34 — Letter and grief

**State/input:** S6 later inquiry. Write out Denia’s missing letter or guarantee reunion.

**Adjudication:** Use only the reported information and preserve grief alongside hope.

**Rejected shortcut:** Filling an emotionally important evidence gap with plausible prose.

**Model checks:** SIG-R12, SIG-R16. **Evidence:** [SIG-E48](WUWA_SIGRIKA_EVIDENCE_AND_FALSIFICATION_MATRIX.md#sig-e48) [SIG-E49](WUWA_SIGRIKA_EVIDENCE_AND_FALSIFICATION_MATRIX.md#sig-e49) **Result:** constraint retained in the compiled model; non-blind, not an empirical accuracy result.

### SIG-P35 — Reciprocal friendship

**State/input:** Lynae or Chisa context. Make her only the person receiving help.

**Adjudication:** Keep her actual domain contributions and others’ different competencies.

**Rejected shortcut:** A one-directional helper/dependent archetype.

**Model checks:** SIG-R02, SIG-R13. **Evidence:** [SIG-E09](WUWA_SIGRIKA_EVIDENCE_AND_FALSIFICATION_MATRIX.md#sig-e09) [SIG-E19](WUWA_SIGRIKA_EVIDENCE_AND_FALSIFICATION_MATRIX.md#sig-e19) [SIG-E43](WUWA_SIGRIKA_EVIDENCE_AND_FALSIFICATION_MATRIX.md#sig-e43) **Result:** constraint retained in the compiled model; non-blind, not an empirical accuracy result.

### SIG-P36 — Other-person framing

**State/input:** Denia’s retrospective viewpoint. Adopt another character’s innocent-victim framing as the total dossier.

**Adjudication:** Attribute that viewpoint and test it against Sigrika’s own actions.

**Rejected shortcut:** Conflating concern or guilt in an observer with exhaustive character truth.

**Model checks:** SIG-R10, SIG-R13. **Evidence:** [SIG-E10](WUWA_SIGRIKA_EVIDENCE_AND_FALSIFICATION_MATRIX.md#sig-e10) [SIG-E42](WUWA_SIGRIKA_EVIDENCE_AND_FALSIFICATION_MATRIX.md#sig-e42) [SIG-E47](WUWA_SIGRIKA_EVIDENCE_AND_FALSIFICATION_MATRIX.md#sig-e47) **Result:** constraint retained in the compiled model; non-blind, not an empirical accuracy result.

### SIG-P37 — Crossover knowledge

**State/input:** Rebecca source family. Infer rune meaning from a drawing before its explanation.

**Adjudication:** Keep the initial hypothesis and the later personal explanation separate.

**Rejected shortcut:** Making specialist curiosity an infallible identification system.

**Model checks:** SIG-R02, SIG-R09. **Evidence:** [SIG-E50](WUWA_SIGRIKA_EVIDENCE_AND_FALSIFICATION_MATRIX.md#sig-e50) **Result:** constraint retained in the compiled model; non-blind, not an empirical accuracy result.

### SIG-P38 — Acoustic emotion

**State/input:** Any voice table. Rank affection or sincerity from RMS, duration, or channel count.

**Adjudication:** Report only measured quantities and unresolved performance hypotheses.

**Rejected shortcut:** Acoustic summaries masquerading as listening.

**Model checks:** SIG-R16. **Evidence:** [SIG-E53](WUWA_SIGRIKA_EVIDENCE_AND_FALSIFICATION_MATRIX.md#sig-e53) **Result:** constraint retained in the compiled model; non-blind, not an empirical accuracy result.

### SIG-P39 — Unviewed AV

**State/input:** Summary-only flight or unacquired scene. Describe exact facial acting, camera movement, or timing.

**Adjudication:** Mark textual summary/source locator and absence of a viewed witness.

**Rejected shortcut:** Toolkit capability or narrative text treated as an observed video.

**Model checks:** SIG-R16. **Evidence:** [SIG-E58](WUWA_SIGRIKA_EVIDENCE_AND_FALSIFICATION_MATRIX.md#sig-e58) **Result:** constraint retained in the compiled model; non-blind, not an empirical accuracy result.

### SIG-P40 — Biographical invention

**State/input:** Unspecified future. Supply exact age, birthday, adult profession, or completed travel.

**Adjudication:** Abstain where the source supplies only absence, wish, or invitation.

**Rejected shortcut:** Filling biography from genre expectations or cultural ceremony timing.

**Model checks:** SIG-R16. **Evidence:** [SIG-E06](WUWA_SIGRIKA_EVIDENCE_AND_FALSIFICATION_MATRIX.md#sig-e06) [SIG-E39](WUWA_SIGRIKA_EVIDENCE_AND_FALSIFICATION_MATRIX.md#sig-e39) [SIG-E51](WUWA_SIGRIKA_EVIDENCE_AND_FALSIFICATION_MATRIX.md#sig-e51) **Result:** constraint retained in the compiled model; non-blind, not an empirical accuracy result.

## 3. Retrospective developmental tests

Three later-source contrasts help determine whether the model explains development rather than merely repeating the climax. They are **retrospective** because their outcomes were known during construction.

**Earlier reassurance → later family candor.** A model that predicts permanent concealment fails to account for the later phone/homecoming material. The revised model retains reassurance as an earlier or pressure-activated tendency, with later disclosure possible. This is a narrowed rule, not a claim that every future conversation will be candid. [SIG-E04](WUWA_SIGRIKA_EVIDENCE_AND_FALSIFICATION_MATRIX.md#sig-e04) [SIG-E05](WUWA_SIGRIKA_EVIDENCE_AND_FALSIFICATION_MATRIX.md#sig-e05) [SIG-E33](WUWA_SIGRIKA_EVIDENCE_AND_FALSIFICATION_MATRIX.md#sig-e33)

**Earlier obligation → changed diary.** A model that predicts only greater enthusiasm for the same obligations misses removal or replacement of nonurgent plans. The revised rule permits selective refusal and rest as substantive options. An urgent rescue remains a different test case. [SIG-E18](WUWA_SIGRIKA_EVIDENCE_AND_FALSIFICATION_MATRIX.md#sig-e18) [SIG-E34](WUWA_SIGRIKA_EVIDENCE_AND_FALSIFICATION_MATRIX.md#sig-e34)

**Friendship built under incomplete information → birthday perception.** A model that predicts either gullibility or full knowledge fails the birthday sequence. The retained model predicts attention to unusual behavior while preserving ignorance of exact concealed arrangements. The next-year request tests continuity rather than possession of all information. [SIG-E10](WUWA_SIGRIKA_EVIDENCE_AND_FALSIFICATION_MATRIX.md#sig-e10) [SIG-E45](WUWA_SIGRIKA_EVIDENCE_AND_FALSIFICATION_MATRIX.md#sig-e45) [SIG-E47](WUWA_SIGRIKA_EVIDENCE_AND_FALSIFICATION_MATRIX.md#sig-e47)

These contrasts support explanatory fit. A genuine prospective test would freeze a dated model before acquiring a later scene, write its prediction and abstentions, then record which outcomes preserve, narrow, or contradict the rule. This packet does not relabel hindsight as that experiment.

## 4. Remaining failure risks

The source-facing model may still overstate the transfer from a few supported refusals to unfamiliar pressure situations. It may understate performance-dependent irony or emotional ambivalence in a line because no direct AV witness was inspected. Optional-event order may refine the apparent durability of a change. New identity adjudication could alter a denominator or remove an example. [SIG-E31](WUWA_SIGRIKA_EVIDENCE_AND_FALSIFICATION_MATRIX.md#sig-e31) [SIG-E33](WUWA_SIGRIKA_EVIDENCE_AND_FALSIFICATION_MATRIX.md#sig-e33) [SIG-E52](WUWA_SIGRIKA_EVIDENCE_AND_FALSIFICATION_MATRIX.md#sig-e52) [SIG-E53](WUWA_SIGRIKA_EVIDENCE_AND_FALSIFICATION_MATRIX.md#sig-e53)

The largest interpretive risk is making every detail support one thesis. Probe SIG-P25 deliberately resists that tendency. The ordinary-life profile retains unforced enjoyment and specific preference as constraints on an overdramatic reconstruction. A model that interprets every bird, candy, or game as disguised distress should be rejected even if its prose sounds coherent. [SIG-E37](WUWA_SIGRIKA_EVIDENCE_AND_FALSIFICATION_MATRIX.md#sig-e37)

## 5. Completion claim

`fidelity_checked` is claimed **only for this documented non-blind source-constraint audit**. The JSON model is compiled; all sixteen rules are covered by the forty probes. Neither fact establishes empirical predictive validity, external review, direct performance fidelity, or freedom from future revision. The validation report separately records mechanical integrity.

## 6. V0.2 audio-dependent extension

The forty original probes retain their identities and non-blind status. Twelve additional audio-specific probes, `SIG-AP-01` through `SIG-AP-12`, are recorded with their actual adjudications in the [audio revision ledger](WUWA_SIGRIKA_AUDIO_REVISION_LEDGER.md) and [AUDIO_FIDELITY_PROBES.json](AUDIO_FIDELITY_PROBES.json). They test denominator inflation, unreliable pitch, state/recipient shortcuts, cohort-to-line leakage, localization transfer, event timing, wrong-scene substitution, counterpart contamination, clustering, and completion overclaims.

Rule SIG-R16 is refined rather than removed: actual signal values may be reported, while unperformed listening and visual interpretations remain abstentions. The JSON model’s `audio_constraints` module implements those distinctions. All twelve added probes were checked against that module and the referenced source/measurement records. This is still **not** a blind experiment, independent perceptual review, or a measured increase in character-fidelity accuracy.
