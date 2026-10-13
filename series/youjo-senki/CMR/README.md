---
series: YOUJO_SENKI
artifact_type: reconstruction_corpus_index
scope: Japanese LN V01-V14 source closure and bounded operational reconstruction
status: active_provisional
canonical_home: Git
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
updated: '2026-10-13'
---

# Youjo Senki character modeling and reconstruction

This is the operational character-reconstruction layer beneath the [current series entrypoint](../CURRENT_STATE_AND_CORPUS_MAP.md). It constrains decisions and written Japanese dialogue in source-bounded hypothetical situations. The mature [V2 literary corpus](../V2%20Analysis/00_README_AND_CORPUS_MAP.md) remains the specialist home for literary, political, military, ethical, and thematic interpretation through Japanese LN V14. CMR neither replaces that corpus nor extends the source horizon beyond V14.

## Current verified corpus

| Responsibility | Verified state | Readable route |
|---|---|---|
| Original Drive inventory | Five folders, twenty original files and retained revisions classified; twelve source append/preservation records added | [Port audit](Provenance/YOUJO_SENKI_CMR_PORT_AUDIT.md), [original disposition](Provenance/YOUJO_SENKI_CMR_DRIVE_DISPOSITION.jsonl), [source append disposition](Provenance/YOUJO_SENKI_CMR_SOURCE_APPEND_DISPOSITION.jsonl) |
| Method | Complete v1.1 body preserved with explicit Git routing; promotion and predecessor pointers await verified main integration | [Method](Methods/YOUJO_SENKI_CHARACTER_MODELING_REFERENCE_METHOD.md) |
| Source integrity / reproducibility | Fourteen locked original EPUBs; exact 63,812 locators, 608 members and 1,200 candidate centers reproduced | [Integrity audit](Provenance/YOUJO_SENKI_CMR_INTEGRITY_REPRODUCTION_AUDIT.md) |
| Tanya V01-V14 adjudication | All 1,200 candidates closed: 711 RETAIN, 433 MERGE, 56 REJECT; 814 textual diagnostic states; V12 prefixes preserved | [Closure audit](Provenance/YOUJO_SENKI_TANYA_CMR2_V14_CLOSURE_AUDIT.md), [diagnostic navigation](Diagnostics/YOUJO_SENKI_TANYA_DIAGNOSTIC_NAVIGATION.md) |
| All-volume consolidation / written voice | 44 conditional rule families, 815 typed crosswalk rows including separate image control, 40 own-voice source controls | [Rule register](Diagnostics/TANYA_OPERATIONAL_RULE_REGISTER.md), [crosswalk](Diagnostics/TANYA_DIAGNOSTIC_TO_RULE_CROSSWALK.jsonl), [voice controls](Diagnostics/TANYA_WRITTEN_VOICE_SOURCE_CONTROLS.jsonl) |
| Readiness / completed roster | 29 authored packages: 2 FULL_SPECTRUM with limits, 23 DOMAIN_BOUNDED, 4 RECOGNITION_PROFILE; 418 anchored claims | [Model and source navigation](YOUJO_SENKI_MODEL_AND_SOURCE_NAVIGATION.md), [re-audit](Provenance/YOUJO_SENKI_CHARACTER_READINESS_REAUDIT.md), [supplement](Provenance/YOUJO_SENKI_SUPPLEMENTARY_CHARACTER_READINESS.md) |
| Directional relationships | 77 episodes; seven-person 42-cell core: 24 direct, 3 partial, 15 not yet audited in this packet | [Register](Relations/YOUJO_SENKI_DIRECTED_RELATIONSHIP_REGISTER.md), [episodes](Relations/YOUJO_SENKI_DIRECTED_RELATIONSHIP_EPISODES.jsonl) |
| Independent QA | All 29 original assessments and current successor/ensemble reviews complete with limits; seven actual source continuations remain partial; original Tanya and ensemble failures remain versioned | [Versioned model QA routes](YOUJO_SENKI_MODEL_AND_SOURCE_NAVIGATION.md#current-qa-qualifications), [current ensemble release](QA/YOUJO_SENKI_ENSEMBLE_CONSISTENCY_QA.md) |
| Open questions / curation | Twenty-three source ceilings retained; project-local discoveries prepared for the sole routine character curator | [Open questions](Provenance/YOUJO_SENKI_OPEN_QUESTIONS_AND_COUNTEREVIDENCE.md), [curator handoff](Provenance/YOUJO_SENKI_CHARACTER_CURATION_HANDOFF.md) |
| Publication / promotion | Branch proposal; exact-head publication and owner-governed integration remain separately certified | [Port audit](Provenance/YOUJO_SENKI_CMR_PORT_AUDIT.md) |

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

The method's Git wrapper keeps its substantive predecessor body intact and labels the old Drive folder map as provenance. Canonical method promotion remains pending a verified main result and explicit predecessor-pointer update. This branch checkpoint may be read as provisional analytical work, but it is not evidence that integration has occurred. Frozen model/original-QA promotion fields are historical construction/evaluation snapshots; separately verified release/promotion receipts control actual Git/main publication and native-Drive authority cutover.

## Coverage controls carried forward

The historical CMR-1 classes remain starting hypotheses rather than a license to populate unsupported interiority. Tanya and Lergen were full-spectrum candidates; other subjects require professional or recognition limits. The current source re-audit distinguishes direct speech/interiority, action, observer reference, retrospective reference, and adaptation/afterword material. Alias-hit counts alone never establish a character's developmental coverage.

Mary needs developmental segmentation. Josef's mediated satirical presentation cannot supply ordinary private cognition. Visha's positive non-Tanya and low-stakes evidence is admitted with developmental and later observer limits. Tanya's attraction/orientation and several ordinary-life preferences remain underdetermined; neither embodied continuity nor isolated necessity supports an imposed categorical identity or a universal habit.

No global character capability system, owner-controlled character registry, global generated catalog, source media, or unrelated series artifact is authored by this checkpoint. Evidence-backed character discoveries use the project-local curation handoff; global registry enrollment remains the character curator's responsibility.
