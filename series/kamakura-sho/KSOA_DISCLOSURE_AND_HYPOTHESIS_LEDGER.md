---
title: "Kamakura Police Station — disclosure and hypothesis ledger"
series: "Kamakura Police Station: The Case Files of Asumi Ogasawara / 鎌倉署・小笠原亜澄の事件簿"
series_id: kamakura-sho
artifact_id: KSOA_DISCLOSURE_AND_HYPOTHESIS_LEDGER
artifact_type: disclosure_and_hypothesis_ledger
generation: KSOA-G1
version: "1.0"
created: "2026-11-12"
status: canonical
scope: "Time-bounded narration and character knowledge, prospective hypotheses and later adjudication."
source_boundary: "Japanese publisher EPUBs V01–V07. Bibliography, bytes and package structure reconciled. Narrative admission and inspection are pending."
canonical_home: series/kamakura-sho/KSOA_DISCLOSURE_AND_HYPOTHESIS_LEDGER.md
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
do_not_use_as_literary_evidence: true
---

# Disclosure and hypothesis ledger

**Analytical rows at initialization: 0.** This ledger records what the reader, each investigator and relevant other characters could know at a specified point. A proposition may be true in story chronology, available to one character, and undisclosed to the reader. Record these differences explicitly.

| Record and key | Required fields |
|---|---|
| Horizon `H` | Generation and stable ID, volume and section, witness, exact inclusive end anchor and preceding exclusive endpoint, previous horizon, assigned evidence scope, exposure/debt, capture time and digest, and path/anchor of the committed prospective snapshot |
| Disclosure `D` | First reader-access horizon and exact evidence, proposition presented, focalizer/speaker, channel, explicitness and emphasis, known story-time position and possible prior clues |
| Knowledge `K` | Proposition/evidence ID, actor or reader ID, story time of acquisition or warranted range, horizon where that acquisition is established to the reader, transmission or inference route, basis and mode (access, belief, suspicion, confirmed, error or unknown) |
| Hypothesis `HYP` | Case and proposer IDs, origin horizon, exact frozen formulation, leading alternatives, supporting and weakening evidence, limits, confidence and predicted discriminator or falsifier |
| Adjudication `ADJ` | Original hypothesis/version, test and adjudication horizon, new evidence, effect on alternatives, outcome, revised confidence and residual ambiguity |

Use stable `KSOA-Vnn-{kind}-NNNN` IDs for all rows, with `H` ordered by actual volume/section/anchor and the predecessor chain. Identity and time of knowledge are distinct fields. A team's access requires a source-supported route to the relevant members. A reader may directly observe a scene that an investigator first encounters through testimony. Unestablished access is unknown. A later revelation about what someone already knew creates a row with both its earlier event time and its later evidence horizon.

At every prologue, chapter and epilogue close, and before material in-section revelations, freeze the prospective records before opening the next span and retain their contents in the owning volume reading. Keep the entering and exiting snapshots attributable and recoverable. Give each freeze a spoiler-neutral anchor and include a self-contained record of what is available through its exact cutoff, with links to the versions it uses. Include unresolved hypotheses, conflicts and exposure limits. Keep later adjudications out of the freeze's text and link labels. If the account is reconstructed after exposure, label it retrospective, with the actual exposure and scope.

To answer “what could be inferred by this boundary?”, open the selected frozen snapshot from the relevant reading, follow predecessor and evidence references through its cutoff, and retrieve only visible versions, using that bound for names, captions and links as well as body text. A later-state table or raw current ledger can expose future rows. An operator constructing a prospective input view renders just the frozen snapshot and bounded earlier records. A fragment link identifies a section inside a full reading, so confirm the view excludes later sections before sharing it with a prospective analyst. A case-close review can read subsequent adjudications in a retrospective view. Record whether each decisive clue was available, salient or obscured, how well it discriminated at the time, and which material facts first appeared later. An unused alternative stays recoverable with its original rationale.

New evidence adds a disclosure or adjudication at the new horizon. Hypothesis revisions reference the predecessor, including when the same conjecture is reopened. Record outcomes such as supported, partly supported, contradicted, no diagnostic opportunity or unresolved, with the actual reasoning. Cross-link the [case evidence ledger](KSOA_CASE_EVIDENCE_LEDGER.md) for the source record and the [claim revision ledger](KSOA_CLAIM_REVISION_LEDGER.md) if a literary conclusion changes.
