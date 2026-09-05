---
series: PJSK
artifact_type: source_lock
scope: ANALYTICAL_LAYER
generation: V1
status: canonical
source_boundary: "Sibling Project SEKAI Japanese corpus pipeline"
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
---


# Project SEKAI Analytical Source Lock


## Authority


The analytical layer does not maintain an independent transcript corpus. Source identity, repository pins, canonical stories, chronology metadata, generated projections, and provenance are governed by the sibling pjsk-corpus-pipeline and its CURRENT_STATE_AND_CORPUS_MAP.md plus manifests.


Before a new analytical campaign, read the source current-state map and record the source/pipeline generation used by the resulting artifact in its source boundary or analysis cutoff.


## Rules


- Canonical story records outrank retrieval projections for textual interpretation.
- Character, relationship, unit, and LLM bundles are retrieval aids with stable locators, not separate narrative authorities.
- Do not silently merge secondary transcript wording into the preferred Japanese source.
- Preserve chronology uncertainty, conditioned ordering, special contexts, and My SEKAI separation where the source corpus does.
- Important verbatim claims should remain traceable to canonical source locators.
- If the source corpus advances while an analysis is underway, the analytical artifact retains the source boundary it actually used; newer source material enters later through the live-service integration method.


## Current lock state


Architecture initialized. The current source lock is dynamic by reference to the canonical sibling source current-state map until the first bounded analytical reading is created. Each later reading must declare its actual source boundary rather than relying on file modification time.