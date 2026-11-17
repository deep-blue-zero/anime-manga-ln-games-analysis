---
title: "KSOA-CB1 pre-registered comparison and adjudication protocol"
series: "Kamakura Police Station: The Case Files of Asumi Ogasawara / 鎌倉署・小笠原亜澄の事件簿"
series_id: kamakura-sho
artifact_id: KSOA_CB1_COMPARISON_PROTOCOL
artifact_type: comparison_protocol
generation: KSOA-CB1-COMPARISON
version: "1.0"
created: "2026-11-15"
status: canonical
scope: "Pre-registered criteria, units, twelve dimensions, record fields, dispositions, adjudication rule and integration principle for comparing KSOA-G1 with KSOA-CB1. Registered 2026-11-14, before unblinding."
source_boundary: "Seven Japanese publisher EPUB witnesses KSOA-JP-V01-W01 to KSOA-JP-V07-W01 (all narrative sections); GPT corpus KSOA-G1 at 7d8ece76cbefeea3eb1d7cd02d4ca99e41966d4a; KSOA-CB1 blind package frozen 2026-11-15T10:52:54Z, manifest SHA-256 35f7a16eddf07a6dffb0750e1146c34874d227a486886db36ca7bf9248113040."
canonical_home: series/kamakura-sho/audits/KSOA_CB1_COMPARISON/COMPARISON_PROTOCOL.md
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
do_not_use_as_literary_evidence: true
compared_generations: [KSOA-G1, KSOA-CB1]
gpt_basis_commit: 7d8ece76cbefeea3eb1d7cd02d4ca99e41966d4a
cb1_blind_package_manifest_sha256: 35f7a16eddf07a6dffb0750e1146c34874d227a486886db36ca7bf9248113040
source_record: "comparison/COMPARISON_PROTOCOL.md in the KSOA-CB1 comparison workspace (outside Git)"
source_record_sha256: 978e97f27ed0c49bb6d724c0dfc6080a75a553617814e761998210e566f8364a
source_record_bytes: 5268
source_record_body_sha256: 218267de6eb77d4fb9b9a23712e6370a9afcb09f7c1fc2bc023dc35e35849496
copy_transformations: []
path_rewrites: []
integration_date: "2026-11-15"
integrated_by: INT-6
source_record_front_matter: |
  title: "KSOA-CB1 pre-registered comparison and adjudication protocol"
  generation: KSOA-CB1
  artifact_type: comparison_protocol
  status: draft_noncurrent
  do_not_use_as_current_authority: true
  registered: "2026-11-14, before any comparison and before the custodian opened either corpus's analytical bodies"
---

# Pre-registered comparison protocol

This protocol fixes the comparison criteria before unblinding, as the synthesis architecture and the reasoning policy (Section 17) recommend: hold criteria constant and compare against the primary source.

## 1. Unblinding preconditions

1. All seven KSOA-CB1 volume readings, the longitudinal synthesis, the monographs, the claim and uncertainty inventory and the readiness analysis are written.
2. `BLIND_PACKAGE_MANIFEST.sha256` covers every blind file and is recorded in `CUSTODIAN_RECORD.md` with a UTC timestamp. The Phase 2 freeze record is then written.
3. Only after step 2 does any agent open the GPT corpus. Blind files are never edited after the freeze. Corrections to the Claude baseline appear only in the discrepancy register and adjudication report.

## 2. Comparison basis

- GPT corpus: `series/kamakura-sho/` at a pinned `origin/main` commit recorded at unblinding, plus the pinned head of any open Kamakura PR whose content changes readings (for example PR #587's opening synopses), recorded separately.
- Read completely, not by search excerpt: the seven `readings/KSOA_Vnn_DEEP_READING.md`; the case, disclosure, character and claim ledgers; the Asumi and Motoya monographs; the partnership study; the mystery, policing and integrated syntheses; the source-completion, convergence, role-gap, V04-reconciliation, readiness, checkpoint-locator and producer-review audits.

## 3. Units of comparison

For each volume: the case solution and mechanics; the suspect and alternative sets; the clue-detectability judgments; the chronology; disclosure order; focalization claims; setting and institutional claims; and the character facts and generalizations for every named character with substantive evidence. Series-level: the thesis set, the motif inventory, the stability and change claims, and the monograph portraits. Readiness: stable dispositions, speech registers, counterexamples, limits.

## 4. Dimensions (scored qualitatively, with concrete examples)

Source coverage · narrative reconstruction · mystery reasoning · psychological interpretation · ordinary-life detail · relationship modeling · Japanese-language analysis · longitudinal synthesis · thematic interpretation · operational reconstruction · evidence traceability · retrieval completeness. Report literary completeness, interpretive sophistication, source accuracy, character-reconstruction coverage and retrieval convenience separately. Issue no overall winner.

## 5. Discrepancy record fields

`ID` (KCMP-NNN) · volume and source locator · subject (character, scene, case or theme) · GPT claim or omission with exact artifact path and anchor · CB1 claim or omission with exact file and ID · primary Japanese evidence (short, verified quotation and locator) · difference type (fact / evidence coverage / inference / interpretation / source boundary / presentation; multiple allowed) · counterevidence and alternatives · disposition · proposed correction and canonical destination.

Dispositions: `AGREE`, `GPT_OMISSION`, `CLAUDE_OMISSION`, `GPT_COMPRESSION`, `CLAUDE_COMPRESSION`, `GPT_ERROR`, `CLAUDE_ERROR`, `BOTH_INCOMPLETE`, `INTERPRETIVE_DISAGREEMENT`, `UNRESOLVED`, `ARCHITECTURAL_DIFFERENCE_ONLY`. A record may carry more than one diagnostic dimension.

An omission claim (`GPT_OMISSION` / `CLAUDE_OMISSION`) requires a search of the **entire** other corpus: for GPT, the readings, all ledgers, studies and audits; for CB1, the readings, section notes, character evidence, exit states, synthesis and monographs. Absence from one document is not an omission.

## 6. Adjudication rule

The Japanese EPUB witness decides questions of what the novels depict. For each consequential discrepancy: retrieve the passage and its context; verify speaker, focalizer, chronology and disclosure boundary; separate what the text establishes from what an analyst infers; state the strongest competing explanation; reconcile or correct; record residual uncertainty; and trace dependent claims. Majority, confidence, length or elegance never decides. Agreement between the two analyses is checked directly against the source wherever a claim is consequential.

## 7. Sampling for agreement checks

Every material disagreement is adjudicated. For agreements, check a stratified sample against the source: at least one case-solution claim, one clue-detectability claim, one register claim and one ordinary-life claim per volume, plus every load-bearing claim in the two lead monographs.

## 8. Integration principle

Preserve source-supported findings from both analyses. Correct demonstrated errors in either through the authorized route (claim revision, erratum or superseding non-sequential artifact). Never edit frozen readings or freezes. Maintain one canonical current portrait per character and boundary. The CB1 baseline stays an identifiable, noncurrent, independently authored analysis with limited authority.
