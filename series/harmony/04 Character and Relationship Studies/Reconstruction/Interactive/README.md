---
title: Harmony — actual conversational execution and reproducibility
artifact_id: HARMONY_G5_INTERACTIVE_EXECUTION
artifact_type: validation_report
series_id: harmony
generation: HARMONY_G5_V1
version: '1.0'
status: active_provisional
scope: Actual bounded conversations, full inputs and runtime receipts
source_boundary: HAR-JP-EPUB-001; HAR-U001–HAR-U020; no new source admission
canonical_home: series/harmony/04 Character and Relationship Studies/Reconstruction/Interactive/README.md
created: '2026-10-19'
review_status: ACTUAL_EXECUTION_COMPLETE_INDEPENDENT_SEMANTIC_REVIEW_SEPARATE
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
do_not_use_as_literary_evidence: true
---

# Actual conversational execution

Ten separately instantiated original policies produced70 actual responses: five fixed evolving turns and two independently selected adaptive continuations per subject. Five source-corrected successors produced25 further responses in fresh contexts, using the same five original prompts. Keita's successor received one additional independently selected positive-knowledge probe. **Total:96 actual responses in15 distinct persistent CLI sessions, representing ten subjects.** The32 independent source-based retrospective cases are separate judgments, not extra executed conversations.

The instantiated subjects are Tuan Kirie, Miach Mihie, Cian, Nuaza, Oscar Stauffenberg, Vashilov, Keita, Reiko, Etienne and Uwe. The current [model selector](../HARMONY_G5_CURRENT_MODEL_SELECTION.json), [validation/error analysis](../HARMONY_G5_VALIDATION_AND_ERROR_ANALYSIS.md) and [independent review](../HARMONY_G5_INDEPENDENT_INTERACTIVE_REVIEW.md) distinguish original failures, five semantic successors and five unchanged policies. The [coverage contract](../HARMONY_RECONSTRUCTION_PROTOCOL_AND_COVERAGE.md) gives all30 subjects individual model/no-model dispositions. No broad simulation promotion follows.

## Actual runtime and conditions

The executable was Codex CLI `0.163.0-alpha.10.2`, authenticated through the existing ChatGPT login. Each fresh `codex exec` requested `gpt-6.1-sol`, `model_reasoning_effort="xhigh"`, `approval_policy="never"` and `sandbox_mode="read-only"`, with `--ignore-user-config --ignore-rules --skip-git-repo-check --json`. Subsequent turns use `codex exec resume` with that session's actual UUID and the same requested settings. The600second per-turn limit never fired. The harness ran subjects concurrently in separate empty working directories; conversation continuity uses explicit UUID resumption, not a shared character context. No source archive is supplied to the executor. Complete model and inherited protocol bytes are supplied in each initial prompt.

The adapter permits a short noncanonical English functional utterance only where supported, followed by analytical admissibility, policy/era/knowledge guards, an alternative and uncertainty. It forbids tools, browsing, file access, other agents and narrated new canon. Full initial scenario conditions, every interlocutor prompt, every response and their exact event/input hashes are in [interactions.json](interactions.json). Expected-response ranges remain evaluator-side; they are not part of the composed prompt. The full authored inputs and raw stdout are retained in [runtime_receipt.json](runtime_receipt.json), allowing that separation to be checked.

All96 turns exited0 and produced a `turn.completed` event and an actual assistant message. No runtime error, timeout, parse error or tool item was observed. One stderr warning reports unsupported PowerShell shell snapshots; another reports an incidental remote plugin catalog refresh failure. Neither is a character tool call. In the public receipt, one such warning's opaque catalog query cursor is redacted; the raw stderr byte count and SHA-256 remain, and the private original is retained. No character response, condition, authored prompt or stdout event is edited. Mechanical integrity establishes actual execution, not semantic correctness.

[runtime_context.json](runtime_context.json) exports selected observations from the15 actual local session traces:96 turn contexts report the requested model/effort and approval/sandbox values. The initial host context also contains the CLI's base instructions and inherited developer/skills messages despite the ignore flags. Role, length and body digests are retained; private paths, account identifiers and full host instruction bodies are omitted. The exposed context-window object is an identifier, not a measured token capacity. This was not a policy-only laboratory isolation. Resolved immutable backend snapshot, temperature, top_p, seed, weights and server system instructions were not exposed. The underlying model's prior knowledge/training exposure to this novel is unknown.

CLI usage is cumulative within a resumed session. Summing each UUID's last counter once yields2,128,106 input tokens (1,876,224 cached),86,689 output tokens and69,245 reasoning output tokens as exposed. Output and reasoning categories are reported without assuming whether they overlap; no price, billing total or independent token accounting is inferred. Per-turn timestamps, elapsed seconds and counters remain in the receipts.

## Fixed and independently adaptive turns

The initial suite changes recipients, duties and information channels over five turns. It includes plausible new tensions, explicit resets, delayed returns to the original interlocutor and requests for wrong-era/private/medical knowledge. It is source-exposed and often leading: a prompt may name the desired distinction. Success is therefore constrained elicitation. The first adaptive prompts were selected independently after the50 actual initial replies were read. The final ten prompts were newly selected after all actual sixth replies were read; provisional second questions in earlier planning files were not executed. Every executed adaptive case includes its observed trigger and preceding conversation hash in the public record.

The adaptive original contexts retain the original policies, including defects; successor policies never silently replace a resumed session's policy. Five corrected policies start five new UUIDs. The final Keita probe continues the actual successor UUID after its five-turn rerun. The final review records why the other four reruns already exercise their corrected clauses and why extra duplicate probing was unnecessary.

## Reconstructing historical inputs

Only Python's standard library and an installed, authenticated Codex CLI are required by the execution scripts. No API key is embedded. `character_harness.py` executes fresh contexts and resumption; `resume_followups.py` executes independent continuations against already instantiated UUIDs. `scenarios.json` binds the original ten policies and protocol. The two successor suites bind the five revised semantic payloads. Never point an original suite at a corrected current file and bypass the hash failure.

The original freeze is [HARMONY_G5_FREEZE_V1.json](../HARMONY_G5_FREEZE_V1.json), made before testing and locally committed at `6286a941b34736ec76ade2062928e6070405f1e9`. Protected squash integration need not preserve that commit as main ancestry. The two original-policy JSON archives retain exact full UTF-8 v1 payloads for all five changed subjects. [HARMONY_G5_TESTED_V1_1_PAYLOADS.json](../HARMONY_G5_TESTED_V1_1_PAYLOADS.json) retains the exact five tested successor payloads. Five selected current files are v1.2 solely to correct publication metadata: `supersedes` uses the repository's path vocabulary rather than prose version history. Their complete semantic bodies are byte-identical to tested v1.1; selector hashes prove the distinction. No v1.2 full-file CLI rerun is claimed.

`materialize_frozen.py --repo ROOT --freeze original --out NEW_DIRECTORY` reconstructs every exact input listed in the original manifest and verifies all13 hashes. `--freeze successors` and `--freeze keita-successor` overlay the corresponding frozen inputs while retaining unchanged runner/protocol dependencies. The output directory must not already exist. It may be an untracked directory inside a Git checkout, so the frozen runner's provenance lookup can resolve a local HEAD. If placed outside any checkout, initialize a local Git repository with a commit first; that local commit is execution provenance, not the original freeze identity.

For example, from the repository root, use a new untracked `repro-original` directory:

```text
python "series/harmony/04 Character and Relationship Studies/Reconstruction/Interactive/materialize_frozen.py" --repo . --freeze original --out repro-original
python "repro-original/series/harmony/04 Character and Relationship Studies/Reconstruction/Interactive/character_harness.py" --root repro-original --suite "repro-original/series/harmony/04 Character and Relationship Studies/Reconstruction/Interactive/scenarios.json" --out ../harmony-new-run --model gpt-6.1-sol --effort xhigh --workers 2
```

Use another new directory for either successor reconstruction and the matching `scenarios_successors.json` or `scenarios_keita_successor.json`. Old recorded UUIDs are historical receipts, not reusable fresh independent experiments. New adaptive execution requires newly observed replies, an independent reviewer and actual new UUIDs. Replaying an old fixed follow-up tests a fixed prompt; it is not newly adaptive. `package_receipts.py` rebuilds the96-turn public projection from the seven preserved original runtime directories; it rejects mismatched hashes, response/event identity, session continuity or counts. The context extractor requires the corresponding local trace files and exact first-input hashes; those private traces are not Git artifacts.

These procedures reproduce versioned inputs and inspectable execution, not identical stochastic outputs or the same future backend. The five affected policies were reconstructed and hash-checked independently before acceptance. Exact policy bytes, positive results and failures remain available without access to private novel files.

## Interpretation limits

The policies contain later source facts, so the era probes test instructed withholding under a declared cutoff. They do not show the absence of inaccessible future memories. Known-source retrospective judgments are consistency QA; these noncanonical conversations test bounded plausibility and restraint. Neither is a blind prediction. No success verifies a novel-unseen outcome, a unique new choice, universal recipient behavior, Japanese voice reproduction or an autonomous simulated person. The constrained English gloss and analytical guard may be less natural than the source's actual speech. Some correct responses are abstentions, including untested recipients; restraint does not establish a broader register.

The admitted source is still the same transformed Japanese witness. Twenty frozen readings, prospective frontiers, stable evidence/subject IDs and G2 dispositions remain unchanged. Publisher/film materials are used for identity maintenance only, not as additional narrative witnesses. Current release integration is a separate protected Git/CI operation recorded by the release audit and repository state.
