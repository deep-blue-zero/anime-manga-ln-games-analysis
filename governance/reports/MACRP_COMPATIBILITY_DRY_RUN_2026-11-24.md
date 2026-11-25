# MACRP compatibility dry run — 2026-11-24

This is a configuration and compatibility record for the [MACRP protocol](../source-policies/MANGA_ANIME_MULTI_AGENT_CHARACTER_RECONSTRUCTION_PASS_PROTOCOL.md) v1.0. It is not a run record, an owner authorization, a baseline freeze, an analytical finding or a capability assessment.

Its project facts come from repository files at `main` commit `bf571a7d5d47cf845f6ead633eb41b568b6e9659`. The one exception is the open-PR state noted in Section 4, which came from the repository's open pull-request list on the same day. It inspected no primary source and changed no project. Paths are given as text, relative to each project's root, and may have moved since. Section numbers in parentheses are the protocol's. A real run repeats every step against its own live baseline.

Each case asks whether the protocol can identify the source boundary, the existing artifact homes, the agent configuration, the execution requirements and the expected deliverables, and what it would stop on.

## 1. Monogatari: prospective MACRP-F

**Invocation tested:** configure MACRP-F through the admitted V30 boundary and its authorized supplements, with the existing V2 analysis as the frozen comparison baseline.

| Protocol step | Result |
|---|---|
| Eligibility (2.2) | Registry route `series/monogatari-series`, entrypoint `V2 Analysis/CURRENT_STATE_AND_CORPUS_MAP.md`, `PRESENT_VERIFIED`. A completed V2 generation exists as a baseline. Outcome: `ELIGIBLE_WITH_LIMITS`, pending the gate items below |
| Source boundary (2.3, 6.1) | Japanese numbered volumes V01-V30 (a supplied-corpus boundary; no V31 source is present or authorized). The Hyakumonogatari and Mijikanamonogatari supplements are claim-admitted under evidence ceilings, and the guidebook is a controlled dual witness. Anime and English are excluded. The F boundary cannot exceed this without a separate admission decision |
| Baseline artifacts (2.1, 2.3) | Deep readings in `V2 Analysis/02 Volume Deep Readings/`: V09 onward typed `deep_reading`, V01-V08 untyped and classified by the directory fallback. Also four immutable season checkpoints; ledgers in `V2 Analysis/03 Longitudinal Ledgers/`; monographs D04-D11 and relationship, voice and specialist syntheses D12-D20 in `V2 Analysis/04 Specialist Synthesis/`; and the claim-revision ledger. The entrypoint names D22 as the next artifact. D23-D25, the reconstruction infrastructure, do not exist, and the planned D25 profiles are declared derived use, a materialized view below the monographs |
| Current-state consistency (2.3) | The V2 method's front matter still reads "Proposed governing method", and the entrypoint still says Documents 03-20 have not begun. Both are integration findings, recorded at the frozen baseline and resolved within the run's scope |
| Diagnosis (2.4) | Missing operational artifacts (no D24 or D25, no probes) suggest MACRP-R first. F is justified only if the owner judges that V2's capture omitted reconstruction evidence pervasively. That is the owner's call at configuration time, and the protocol forces it to be recorded |
| Gate route (4.3) | The entrypoint has no `sequential_analysis_lock` field. A reconstruction-oriented generation is a material restart and must opt in. Before the first new reading it needs `project_initiation_gate: REQUIRED` in the root's routing descriptor, a current-eligible method and architecture for the new generation (including its rule on retrospective material in unit readings), initialized infrastructure, an OPEN lock, and a continuation-policy run declaration with the generation's own high-water mark. New readings, typed `deep_reading`, go to new paths in the same root, and V2 readings and checkpoints stay frozen. The registered entrypoint sits inside `V2 Analysis/`, so the generation gets its own entrypoint, the routing descriptor reroutes the registration to it, and the V2 map becomes the V2 generation's historical surface. The root has no run-stop or terminal-closure record to update |
| Configuration (5.3) | Topology Section 4.1 per unit. The Dense shape distributes workstreams across the specialists who serve the units in turn; a Japanese voice and wordplay specialist (6-7) and a chronology and knowledge-state specialist (11) carry the hardest responsibilities. Each unit reconciles against its V2 reading. Rotating narrators make the focalizer field and workstream 3 load-bearing. Rereading agents know the series, so unit work is retrospective unless uncontaminated agents freeze separate prospective accounts |
| Deliverables (9, 16) | Per-unit readings and transaction records with receipts; the new generation's ledgers; successor monographs where general revision is warranted; D24 and D25, or their architecture successors, as derived-use models; sealed probes; a baseline comparison against V2 |
| Stops | No owner authorization of the restart or run; V2 baseline not settled while D22 is in progress; no current-eligible method for the new generation |

**Fit:** the protocol routes F through the initiation gate instead of around it. It also surfaced that the cheaper route, MACRP-R building D24 and D25 from V2, should be weighed first. The generation's directory layout stays an architecture decision.

## 2. Rent-a-Girlfriend: prospective MACRP-T

**Invocation tested:** execute MACRP-T for Kazuya Kinoshita, concentrating on mundane behavior, written voice, humor and independent practical competence.

| Protocol step | Result |
|---|---|
| Eligibility (2.2) | Route `series/rent-a-girlfriend`, entrypoint `CURRENT_STATE_AND_CORPUS_MAP.md`, `PRESENT_VERIFIED`. Kazuya has an evidence ledger and a model in `04 Character Analysis/Kazuya Kinoshita/`. Outcome: `ELIGIBLE` |
| Authorization (3.1) | The instruction names deficiencies but no units, so the boundary defaults to the admitted boundary and the principal records a selection rule that passes the reread test |
| Source boundary | Japanese manga V001-V040 admitted. V041-V047 are inventory only and outside every MACRP mode; Reviewer A's boundary check (10.1) catches any record that strays there. Anime and translations are excluded |
| Baseline artifacts | `04 Character Analysis/Kazuya Kinoshita/RAG_KAZUYA_EVIDENCE_LEDGER.md` and `RAG_KAZUYA_RECONSTRUCTION_MODEL.md`; `03 Ledgers/RAG_CAST_AND_RECONSTRUCTION_READINESS.md`; `03 Ledgers/RAG_CLAIMS_PREDICTIONS_AND_REVISIONS_LEDGER.md`; the project reconstruction spec; reconstruction audits V010-V040 in `07 Audits and Handoffs/`. No monograph exists; the architecture plans `RAG_KAZUYA_CHARACTER_MONOGRAPH.md` |
| Current-state consistency | The model header records `local_readiness: PARTIAL_MODEL`, a V010 basis checkpoint and a V028 use endpoint, while the router and the V040 audit say otherwise; the claims ledger's coverage block stops at V033. These are integration findings the run fixes or bounds |
| Diagnosis | The project records sparse ordinary repertoire, underobserved competence outside relationship crisis, written speech only partly modeled and no humor analysis. The sources were read but these dimensions were not captured: "evidence present but not extracted", which calls for MACRP-T |
| Diagnostic selection (6.2) | Units with low-stakes routine, work and study, friendship outside crisis, comic scenes and dense dialogue, stratified across V001-V040. Adverse units where competence or humor would be expected and is absent. An uncited-source sample owned by Reviewer B. The reread test (4.2) keeps the selection well short of most of the forty volumes |
| Gate route | None needed. Records are typed `macrp_targeted_evidence_record` (or a project retrospective type), sit outside `01 Sequential Readings/`, and stay `draft_noncurrent` until acceptance. The run's state lives under `macrp_run`; the entrypoint's `sequential_execution` block (lock OPEN, V040 terminal, awaiting separate V041 authorization) is untouched. With an OPEN lock, writing the run into that block would look like an admission authorization, which Section 12.2 forbids |
| Configuration | Standard. Principal; specialist B (ordinary life and microbehavior, 4-5); specialist C (Japanese written voice and humor, 6-7); specialist E (ethics and conflict, competence and agency, 9-10); Reviewers A and B; probe designer, respondents and judges. The page-reading medium supports written register and drawn behavior, never performed voice |
| Deliverables | New ledger rows with canonical `occurrence_id`s and preference categories. Persona matters here: statements made on a rental date are not sincere preferences by default. A successor Kazuya model, or a revision under the project's convention, with new mechanisms, priority arbitration, a voice matrix and a humor section. Claim revisions. Sealed tests E, G and B, plus C against Chizuru where they share scenes, with a generic-sketch control. A baseline comparison. Leads for discovery and the evaluator that name the changed workstreams and the recorded limits for Japanese voice and humor, with no grade |
| Out of scope | Writing Kazuya's monograph, unless the instruction adds it. The run records the qualification state and leaves any production obligation visible |

**Fit:** good. The diagnosis maps directly to T, the record typing keeps targeted work out of the sequential gate, and the reread test stops any widening toward all forty volumes.

## 3. Oregairu: prospective MACRP-R

**Invocation tested:** execute MACRP-R for Hachiman and Yukino, integrating and independently reviewing their existing reconstruction models before deciding whether further source inspection is warranted.

| Protocol step | Result |
|---|---|
| Eligibility | Route `series/oregairu`, entrypoint `V2 Analysis/07 Archive and Manifests/OREGAIRU_V2_DRIVE_CORPUS_MAP.md`, `PRESENT_VERIFIED`. Outcome: `ELIGIBLE` |
| Source boundary | Japanese mainline V01-V14 plus canonical .5 material through V14.5 |
| Baseline artifacts | Monographs `V2 Analysis/05 Specialist Synthesis/02_HIKIGAYA_HACHIMAN_...md` and `03_YUKINOSHITA_YUKINO_...md`; derived-use models `V2 Analysis/06 Continuous Synthesis/Character Reconstruction Models/OREGAIRU_V2_CHAR_HACHIMAN_RECONSTRUCTION_MODEL.md` and `..._YUKINO_...`; the character-state, relationship-state, Japanese-voice, epistemic-narratorial, everyday-life and request-intervention-ethics ledgers in `V2 Analysis/04 Checkpoints and Longitudinal Ledgers/`; the Phase 6 adversarial audit and the Phase 8.5 suite audit |
| Freeze state (2.2, 9.5) | The project records a v1.0 release route and "fifty frozen analytical artifacts and the eight audit-bound model hashes"; the suite audit and the corpus manifest record the model hashes. The corpus map does not declare the model files byte-immutable. As a frozen release, the models are analytically immutable. The run issues successors, which stay `draft_noncurrent` until acceptance. The predecessors' administrative supersession metadata lands only through the reviewed governance change routing Section 8.2 requires, never from `series/oregairu`, so promotion waits on that change. The suite audit remains the record of the bytes it examined, and the manifest is refreshed by the project's release process. If the owner reads the release as byte-locked, promotion of the successors waits on an owner-chosen route |
| Diagnosis | The project records no external, blind or held-out measurement and an open deployed-generator calibration. The models are mature, so the work is integration and independent review: MACRP-R. Escalation to T only if Reviewer A finds decisive passages that the existing locators do not support |
| Configuration | Standard. Principal; specialist 1 (workstreams 1-3 and 11, with Hachiman's narration); specialist 2 (4-5, drawing on the everyday-life ledger, and 6-8, voice and the Hachiman-Yukino relationship); specialist 3 (9-10, drawing on the request-intervention-ethics ledger); Reviewers A and B; probe designer, respondents and judges. A first-person narrator makes the `focalizer` field and the `SOURCE_ATTRIBUTED` status central |
| Deliverables | A reconciliation register against both models and monographs; successor models; sealed tests E (a self-description taken as a full account of motive), C (Hachiman against Yukino in identical settings), B, G, and F for any revised monograph. A designer who does not revise the models seals them, and latent knowledge is recorded as `CANNOT_BE_EXCLUDED` for so widely known a work. A baseline comparison on those probes. Hachiman's narrated motives are `SOURCE_ATTRIBUTED`, never direct observation (7.2) |
| Leads | No Oregairu discovery partition exists. A discovery lead naming the monographs and models is in scope (Section 14) and creates no registry entry |

**Fit:** good, conditional on the release-lock reading and on a separate reviewed governance change for the predecessors' metadata. The case prompted the protocol's three-way distinction between a frozen release, a declared byte lock and a merely recorded hash (Sections 1.3, 2.2, 9.1 and 9.5), and the owner stop for the byte-locked case.

## 4. Lycoris Recoil (audiovisual) and Project SEKAI (live-service game): medium independence

**Lycoris Recoil, prospective MACRP-T for Chisato.**

- **Route and boundary.** `series/lycoris-recoil`, entrypoint `CURRENT_STATE_AND_CORPUS_MAP.md`, `PRESENT_VERIFIED`, lock OPEN. Admitted: TV E01-E13 and Friends Shorts 01-06, frozen at the anime-native final checkpoint. The novels, *Recollect* and the anthologies are separate source classes.
- **Homes.** Frozen behavioral and current operational reconstructions in `03 V2 Working Artifacts/04 Character Reconstruction/`. Character syntheses and the voice-performance synthesis in `03 V2 Working Artifacts/05 Specialist Synthesis/`. The microbehavior ledger in `03 V2 Working Artifacts/03 Longitudinal Ledgers/`. The withheld reconstruction evaluation and the completion register in `03 V2 Working Artifacts/08 Audits and Manifests/`.
- **Recorded deficiencies.** The current models were revised after their withheld scoring and have not been evaluated since. Two speaker attributions await a synchronized listener. Perceptual audio is `UNVERIFIED`.
- **Configuration.** Standard: principal; specialist C (voice, 6-7) working in a `CONTINUOUS_AV` context verified under topology Section 5 for the attribution and delivery items; specialist B (microbehavior, 4); Reviewers A and B; probe designer, respondents and judges. The three voice layers stay separate, and listening is accounted for by boundary. Without the AV lane, those items stop and the text and bundle items proceed.
- **Deliverables.** Targeted AV evidence records, a successor operational model, and a fresh post-revision evaluation with newly sealed probes rather than reuse of the earlier scores (Sections 10.4 and 11).
- **Open evaluator work.** The repository's open pull-request list shows an evaluator PR proposing a Chisato candidate. It becomes stale when the cited evidence changes, and that never blocks the run.

**Project SEKAI, prospective MACRP-R for four unit members.**

- **Route and boundary.** `series/project-sekai`, entrypoint `README.md`, `PRESENT_VERIFIED`. The boundary is a locked live-service inventory through event 0222 plus enumerated supplements, so the run binds that exact inventory, never all current events.
- **Homes.** A three-file package per character in `05_CHARACTER_RECONSTRUCTION/<NAME>/` (monograph, model, evidence index), and the readiness matrix and WxS audits in `09_EVIDENCE_AUDITS_AND_MANIFESTS/`.
- **Capability.** The work so far is recorded as local-only, with no independent-agent review, and as Japanese text only. The protocol therefore requires a capability check for genuinely independent contexts.
- **Configuration.** Standard: principal; specialists split by subject pair across workstreams 1-8; Reviewers A and B; probe contexts. Voice is bounded to written register, and Virtual Singer observations are scoped by manifestation.
- **Deliverables.** Reconciliation registers, successor models, and Test C as the central test because the four characters share scenes. The project's R0-R5 readiness labels stay local descriptions, never capability grades.

**Fit:** the lane, manifestation and locked-inventory rules carried over without medium-specific additions. One clarification was added as a result: live-service boundaries are exact locked inventories (Section 6.1).

## 5. Conclusions

- **Coverage.** For the three main cases, the protocol identified the boundary, the homes, a configuration, the gate route and the deliverables from existing project records, without new infrastructure. The two medium cases were configured more briefly, enough to test lanes, inventories and capability checks.
- **Changes prompted.** The protocol gained the three-way freeze distinction and the owner stop for byte-locked targets, and the rule that a live-service boundary is an exact locked inventory.
- **Integration findings.** Stale headers, variant state fields and stale catalog notes recurred, which confirms that every run needs a baseline consistency check.
- **Owner decisions surfaced, not made:**
  - Monogatari: whether to do R before F.
  - Rent-a-Girlfriend: whether to add the monograph to the T scope.
  - Oregairu: whether the v1.0 release locks the model files' bytes.
  - Lycoris Recoil: whether a continuous-AV context is available.
