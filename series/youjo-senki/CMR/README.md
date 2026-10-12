---
series: YOUJO_SENKI
artifact_type: reconstruction_corpus_index
scope: Japanese LN V01-V14 CMR continuation; V01-V12 diagnostic port checkpoint
status: active_provisional
canonical_home: Git
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
updated: '2026-10-11'
---

# Youjo Senki character modeling and reconstruction

This is the operational character-reconstruction layer beneath the [current series entrypoint](../CURRENT_STATE_AND_CORPUS_MAP.md). It constrains decisions and written Japanese dialogue in source-bounded hypothetical situations. The mature [V2 literary corpus](../V2%20Analysis/00_README_AND_CORPUS_MAP.md) remains the specialist home for literary, political, military, ethical, and thematic interpretation through Japanese LN V14. CMR neither replaces that corpus nor extends the source horizon beyond V14.

## Current verified checkpoint

| Responsibility | Verified state | Readable route |
|---|---|---|
| Original CMR Drive inventory | All five folders and 20 current files classified; retained revisions recorded, current core bytes verified | [Port audit](Provenance/YOUJO_SENKI_CMR_PORT_AUDIT.md), [machine-readable disposition](Provenance/YOUJO_SENKI_CMR_DRIVE_DISPOSITION.jsonl) |
| Governing CMR method | Complete v1.1 substantive body preserved; active provisional Git candidate, promotion/pointer update pending main integration | [Method](Methods/YOUJO_SENKI_CHARACTER_MODELING_REFERENCE_METHOD.md) |
| CMR-1 initial roster | Preserved historical 20-character source-contextual audit; source re-audit in progress | [Readiness baseline](Provenance/YOUJO_SENKI_CMR1_READINESS_BASELINE.md) |
| Japanese source lock | All fourteen local EPUB hashes, sizes, archive CRC checks and OPF routes match the locked sources; live Drive IDs/names/sizes verified | [Integrity and reproducibility audit](Provenance/YOUJO_SENKI_CMR_INTEGRITY_REPRODUCTION_AUDIT.md) |
| CMR-0 / CMR-2A | Exact 63,812-locator, 608-member and 1,200-candidate outputs reproduced | [Integrity audit](Provenance/YOUJO_SENKI_CMR_INTEGRITY_REPRODUCTION_AUDIT.md#exact-reproduced-objects) |
| Tanya CMR-2B V01-V12 | Exact frozen 1,045-candidate ledger and 676-diagnostic index reproduced; all 676 analytical records now inspectable in Git | [Diagnostic navigation](Diagnostics/YOUJO_SENKI_TANYA_DIAGNOSTIC_NAVIGATION.md) |
| Tanya V13-V14 closure | 155 candidate centers remain outside the frozen V12 authority; source-contextual append work is in progress | Closure audit will be linked after its complete validation |
| Tanya model and independent QA | Pending source closure and all-volume rule consolidation | No emitted model is claimed |
| Other eligible models, directional relationships, ensemble QA | Pending Tanya pilot and source-readiness re-audit | No completed package is claimed |
| Publication and authority promotion | Candidate checkpoint; branch publication and integration are separately audited | [Port audit](Provenance/YOUJO_SENKI_CMR_PORT_AUDIT.md) |

The inherited source adjudication and its processing-integrity revalidation are different claims. The diagnostic port preserves the original English interpretation and explicit limits, without claiming that every V01-V12 scene has been newly reread. In particular, inherited `HIGH` diagnostic confidence does not become `HIGH` certainty about who spoke or focalized a passage. Generic original attribution caveats remain visible.

## Retrieval for an analyst or simulator

1. Resolve literary responsibility and admitted source horizon at the [series entrypoint](../CURRENT_STATE_AND_CORPUS_MAP.md).
2. Read the [CMR method](Methods/YOUJO_SENKI_CHARACTER_MODELING_REFERENCE_METHOD.md), including the five distinct evidence channels and the six-step speech-production chain.
3. Use the [diagnostic navigation](Diagnostics/YOUJO_SENKI_TANYA_DIAGNOSTIC_NAVIGATION.md) to find stable diagnostic IDs by volume, setting, relationship, ordinary-life domain, and linguistic hazard. Each JSONL record supplies its source tuple and the original candidate IDs.
4. Open the original EPUB through its verified Drive file ID; resolve the OPF member, spine position and normalized paragraph ordinal using the Drive-primary CMR-0 locator/member layer. Printed-book pages and screen pagination are not interchangeable with that ordinal.
5. Apply a completed source-bounded model and directed relationship register only when their routes and QA are actually present. Distinguish supported prediction, contextual inference, and an unsupported domain requiring abstention. Generated wording never becomes a source witness.

## Evidence and authority boundaries

The [disposition manifest](Provenance/YOUJO_SENKI_CMR_DRIVE_DISPOSITION.jsonl) is the maintained project-local Drive artifact reference and crosswalk for this continuation. It records current originals, retained revision visibility, exact hashes when accessible, analytical transformations, and evidence exclusions. It extends the series evidence routing without rewriting the repository's frozen historical migration crosswalk.

Source EPUBs, raw Japanese paragraph text, the approximately 52.9 MB locator TSV, full candidate pool, raw diagnostic TSV, adjudication history and extraction work remain Drive-primary evidence or private working material. The Git JSONL slices preserve analytical findings, conditional states, channels, uncertainty, and typed source routes. They omit novel passage anchors; compact written-voice lexemes, where present, are bounded linguistic facts rather than copied scene dialogue. Byte size alone is not the eligibility argument.

The method's Git wrapper keeps its substantive predecessor body intact and labels the old Drive folder map as provenance. Canonical method promotion remains pending a verified main result and explicit predecessor-pointer update. This branch checkpoint may be read as provisional analytical work, but it is not evidence that integration has occurred.

## Coverage controls carried forward

The historical CMR-1 classes remain starting hypotheses rather than a license to populate unsupported interiority. Tanya and Lergen were full-spectrum candidates; other subjects require professional or recognition limits. The current source re-audit distinguishes direct speech/interiority, action, observer reference, retrospective reference, and adaptation/afterword material. Alias-hit counts alone never establish a character's developmental coverage.

Mary needs developmental segmentation. Josef's mediated satirical presentation cannot supply ordinary private cognition. Visha's non-Tanya low-stakes evidence is being deliberately checked. Tanya's attraction/orientation and several ordinary-life preferences remain underdetermined; neither embodied continuity nor isolated necessity supports an imposed categorical identity or a universal habit.

No global character capability system, owner-controlled character registry, global generated catalog, source media, or unrelated series artifact is authored by this checkpoint. New evidence-backed character discoveries will be handed off through a project-local record when the models are complete.
