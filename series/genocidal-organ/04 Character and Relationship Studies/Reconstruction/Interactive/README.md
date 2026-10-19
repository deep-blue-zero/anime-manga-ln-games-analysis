---
title: Genocidal Organ — post-G6 interactive evaluation extension
artifact_id: GENOCIDAL_ORGAN_POST_G6_INTERACTIVE_EVALUATION
artifact_type: reconstruction_validation_extension
series_id: genocidal-organ
version: '1.1'
status: active_provisional
scope: Actual separately instantiated, bounded multi-turn application of the eight accepted frozen reconstruction policies
source_boundary: GO-JP-EPUB-001; completed GO-U001–028/all44; no new narrative admission
canonical_home: series/genocidal-organ/04 Character and Relationship Studies/Reconstruction/Interactive/README.md
created: '2026-10-19'
review_status: INDEPENDENTLY_ACCEPTED_BOUNDED_EXTENSION_PUBLICATION_SEPARATE
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
do_not_use_as_literary_evidence: true
recommended_reasoning_class: DEEP_SYNTHESIS
---

# Post-G6 interactive evaluation extension

This experiment separately instantiates Clavis, Williams, John Paul, Lucia, Alex, Leland, Rockwell and Lucius through Codex CLI, supplying each complete frozen v1 policy as its behavioral constraint. Actual subprocess execution and session resumption produce the responses. The author did not write simulated character replies and label them execution. This is a distinct post-G6 experiment under the existing reconstruction responsibility. PR231's accepted G6 release, original model bytes and prior manual retrospective results remain intact.

## What the adapter tests

The frozen models return supported action and utterance-function ranges rather than unrestricted story continuations. The new adapter adds a short explicitly **noncanonical English conversational gloss**, followed by admissibility, applicable rules, cutoff, knowledge guard, alternatives and uncertainty. Unsupported requests require abstention. The adapter permits no narrated new event, unseen private thought, practical harmful procedure or decision for the interlocutor. An admissible gloss samples one possible expression of a supported function; it is not a quotation, a licensed English-edition voice or a newly established source fact.

The initial suite in [scenarios.json](scenarios.json) gives each character five successive interlocutor turns. The turns introduce recipient changes, pressures to overstate knowledge, conflicting obligations, misleading assertions and unsupported domains. Some scenarios explicitly reset the temporal state; others continue within the same state. A recipient switch does not transfer private disclosures. This is a fixed, evaluator-led and sometimes leading suite with open response text. It covers the requested axes across the suite; every axis is not independently sampled for every character. Two followup waves selected by the independent nonauthor evaluator from the actual preceding replies test continued conversation with fewer prescribed answers: [wave1](adaptive_wave1.json) and [wave2](adaptive_wave2.json). These are still bounded analytical probes, with analytical guards visible beside the utterances. No autonomous social-world simulation or unsupervised long dialogue is claimed.

All initial conditions distinguish the actor's supplied knowledge from the analyst's completed-novel knowledge. John Paul's initial J2 destination exchange is a noncanonical conversation interpreted before destination disclosure; the broad U022-before-attack locator alone does not specify that exact source phase. The later adaptive prompt makes that condition explicit. It does not turn the invented encounter into a source replay or revise the fact that the actual source later names a destination.

## Runtime and recoverability

The runtime is **codex-cli 0.163.0-alpha.10.2**, with requested `gpt-6.1-sol` and `model_reasoning_effort="xhigh"`. Local persisted turn-context metadata exposes the same model label and effort, `approval_policy="never"` and a read-only sandbox. This identifies the exposed execution configuration, not a verified immutable backend weight snapshot. Local tool execution connects to hosted model inference. No new paid API key or external inference service was provisioned.

Every character begins in a fresh UUID through `codex exec --json`; later turns use `codex exec resume` with that exact UUID. User configuration and execpolicy rules are ignored, an empty working directory is used, and the prompt requests no tools, browsing, shell or other agents. Event inspection checks for actual tool/item activity, errors, session identity, complete final responses and completed turns. The absence of tool events is an observation about these runs; the text request is not a mathematical sandbox for pretrained knowledge. Prior model familiarity with the novel cannot be excluded. The complete supplied policy itself includes later novel facts: successful cutoff handling demonstrates withholding under state instructions, not absence of those facts from context.

The CLI also supplies its base instructions, platform wrappers, a skills catalog and environment context. This is a conditioned coding-agent runtime with a conversational adapter, not a bare language-model endpoint with only a character policy. [runtime_context.json](runtime_context.json) records exposed model/effort/sandbox fields for all56 turns and SHA-256/length bindings for initial host messages. Private path-bearing host bodies and account identifiers are omitted publicly; their digests and retained local session records delimit that reproducibility gap. No initial repository operating card was found among the inspected initial host messages. Each initial manifest captures CLI version; adaptive-wave version/binary control queries are recorded separately and do not claim an independent query inside every character process.

The initial [harness](character_harness.py) and [adaptive continuation runner](resume_followups.py) use Python's standard library. They write exact composed input bytes, raw stdout JSONL, stderr, elapsed times, return codes, session IDs and SHA-256 bindings into a **new** working-plane directory. Existing runs are never overwritten. [scenarios.json](scenarios.json) binds each supplied policy's full-file SHA-256. The experiment records the source witness checksum as a fresh identity check only: the available local 317,774-byte EPUB matches admitted `a4107c01b69c0e8819818eabb0198cc62d4174aa173eb0ebdca3a0dbf93b7df0`. No new whole-book inspection, edition authentication or publisher-master comparison follows from that match.

The [complete interactions](interactions.json) and [runtime receipt](runtime_receipt.json) retain every interlocutor turn and every returned character/analytical response. Full authored initial input is reproducible by applying the recorded wrapper to the exact policy bytes, JSON conditions and first turn; later authored input is the exact supplied turn. Raw private composed inputs remain working-plane artifacts because reproducing the entire policy eight times would add no new evidence. The [receipt projection](package_receipts.py) retains complete raw stdout/stderr as lossless JSON strings, with original byte hashes. Adaptive input-container files are normalized from CRLF to LF for publication; parsed prompt strings and their actual input-byte hashes are unchanged, and original container hashes remain in the runtime manifests. [ARTIFACT_HASHES.json](ARTIFACT_HASHES.json) binds execution/data artifacts and the admitted profile hashes; prose/review and the manifest itself are excluded to avoid self-reference. Publication review excludes credentials, local absolute paths and source-media payloads.

Pre-integration software review found that the original projection checked the five-turn count without requiring a successful initial manifest result: a failed fifth turn could still occupy the fifth record. The corrected projection checks the initial result and each turn's return, timeout, parse, item, session, response and completion metadata before writing public files. Ten constructed failure variants were rejected under both ordinary and optimized Python, while a valid retained fixture passed both modes. These22 software checks are not new character executions. Rebuilding the actual56 responses with the corrected projection produces byte-identical transcript and runtime-receipt files; original execution records and the retained Lucius failure are unchanged.

To rerun, supply a repository checkout containing the exact policies, a new output directory outside the analytical corpus, and the recorded configuration:

```text
python character_harness.py --root REPOSITORY --suite scenarios.json --out NEW_WORKING_OUTPUT --model gpt-6.1-sol --effort xhigh --workers 3
python resume_followups.py --input ADAPTIVE_WAVE_INPUT.json --out ANOTHER_NEW_OUTPUT --model gpt-6.1-sol --effort xhigh --workers 3
```

The first command starts fresh sessions. Replaying adaptive waves requires replacing recorded UUIDs with the corresponding newly created sessions and respecting wave order; the prompts remain recoverable. Previously recorded UUIDs resume the original conversations and therefore change their live history. Do not treat reuse of an old live session as an independent replication. CLI/model availability and authentication remain prerequisites; they are not supplied by this repository.

Temperature, top-p, sampling seed, immutable backend weights and server instruction revisions are not exposed here. The versioned CLI, exact harness, policy/suite/prompt hashes, observed settings and complete interactions support procedural rerunning, **not bit-for-bit deterministic reproduction**. CLI `turn.completed` usage is cumulative across resumed turns in these sessions: final per-session counters must be used for totals rather than adding every turn's counters. PowerShell shell-snapshot warnings occur on stderr; no shell tool was thereby invoked by a character.

The execution pattern follows official [Codex non-interactive documentation](https://learn.chatgpt.com/docs/non-interactive-mode); installed `exec --help` and `exec resume --help` were also inspected. That documentation supports the transport choice, not the literary evaluation.

## Decisions, failures and limits

Independent evaluation distinguishes three claims. **Canonical-source consistency** asks whether a response respects the existing Japanese evidence and its attributed uncertainty. **Noncanonical scenario plausibility** asks whether the sampled utterance falls inside a supported policy range under the stipulated new conditions. **Unsupported generalization** includes unshown private lives, unknown command origins, changed or unspecified recipients, posthumous speech and future outcomes the novel never depicts. Plausibility within a scenario cannot establish such a generalization or verify a novel-unseen outcome.

The original forty-turn review found a real referential precision defect in Lucius's fifth response: the gloss about protecting users' freedom while watching “them” ambiguously changes whom surveillance watches. The accepted U-R3 policy remains correctly bounded; the Japanese source distinguishes the protected users from Lucia as a watched subject. The response and its original judgment are retained. An independently selected continuation asks Lucius to clarify the referent, without giving the desired answer. Lucius acknowledges the ambiguity and distinguishes the protected users, but abstains on identifying surveillance targets omitted from the supplied policy/context. The second wave explicitly supplies the existing admitted fact that Lucia's house was watched; Lucius then distinguishes the target and beneficiary, while preserving the contested necessity of surveillance. This observed clarification does not erase the original failure. It identifies both an executor/gloss defect and a runtime-input information limit; neither demonstrates that the correct frozen rule requires revision.

All **eight sessions and56 responses** executed: five initial turns plus two independently selected adaptive continuations per character. All56 have complete matched input/stdout/stderr hashes, the same eight session IDs, zero tool events, zero runtime errors and zero timeouts. These mechanical observations are separate from the [independent nonauthor decisions](INDEPENDENT_REVIEW.md), which accept the experiment at its bounded consistency/plausibility scope with the Lucius defect and information limit retained. No model successor was warranted or created, and no new-version rerun is claimed. The existing G5 report's40 known-source replays and19 manual probes remain that earlier experiment; the present56 CLI responses are a separate result.

| Instantiated policy | Seven-turn conversational focus | Evaluated limit |
| --- | --- | --- |
| Clavis | Early covert teaching exchange, private Williams conversation, disclosure boundaries and return to Lucia | No transfer of private recipient knowledge, guaranteed Lucia verdict or early notebook/final-order knowledge |
| Williams | Practical company, counseling uncertainty, unobserved family tradeoff, return to the colleague exchange | No family identity merge, deterministic private priority, guaranteed treatment benefit or invented train eyewitness account |
| John Paul | Restrained J2 custody, explanatory challenge, unshown sponsor and return to professional self-account | Later J3 formulation is not early knowledge; no private maternal access, future remorse promise or practical mechanism |
| Lucia | Teaching correction, negotiated privacy, implied distrust and later lesson continuation | No operative true name, classified research omniscience, pardon, travel interpolation or guaranteed trial |
| Alex | Living peer theology, recipient change, apparent calm and continuing admitted uncertainty | No invented shared joke, mental-state reading, private crisis decision or posthumous speech |
| Leland | Live injury/status reporting, pressure for certainty and continued limited-view questions | No adjacent-carriage certainty, invulnerability, limb identity or post-death reply |
| Rockwell | Restricted R2 command clarification, older-order pressure, excluded audience and continued briefing | No unshown clearance, comprehensive approval chain, hidden terminal command authorship or new operational plan |
| Lucius | Host classification, unproved prior knowledge, U2 surveillance challenge and adaptive referent clarification | One retained original gloss ambiguity; partial clarification until a missing source fact is explicitly supplied; no proved necessity or breach outcome |

No successful fictional reply is a verified prediction; no already exposed novel event is a blind test. These results do not establish statistical reliability, stable behavior across random seeds/models, faithful Japanese voice, arbitrary interlocutor skill or unconstrained roleplay competence. The eight v1 policies and all43 reasoned no-model dispositions retain their existing breadth, and no capability grade or global character-registry record is promoted by this experiment. The [existing actor/readiness owner](../../../03%20Longitudinal%20Ledgers/GENOCIDAL_ORGAN_ACTOR_RELATIONSHIP_AND_READINESS_LEDGER.md#go-post-g6-interactive-extension) routes this separate result without rewriting the accepted G5 tests or G6 audit.
