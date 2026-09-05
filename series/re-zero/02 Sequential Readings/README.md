---
series: RE_ZERO
artifact_type: sequential_reading_contract
scope: MAIN_LIGHT_NOVEL_VOLUME_FREEZES
generation: V0.1
status: canonical
release_state: mutable_active
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
---

# Re:Zero — sequential readings

This directory is the canonical home for **prospective main-light-novel deep readings**.

No deep reading is present at bootstrap.

## Filename contract

Use global numbered identities:

- `REZERO_LN_V01_DEEP_READING.md`
- `REZERO_LN_V02_DEEP_READING.md`
- ...

Do not restart filenames at arc boundaries. Record a source-verified arc identity in front matter and the volume body.

Optional arc checkpoints may use a stable form such as `REZERO_ARC_<ID>_CHECKPOINT.md`, but only after the boundary is source-verified and the contributing main volumes are frozen.

## Freeze contract

Before opening `VNN`, the reader must have a frozen state for `VNN-1` and a recorded next-volume horizon. For `V01`, the bootstrap abstentions serve as the empty prior state.

Each volume file should contain:

1. exact source witness and integrity/provenance reference;
2. prior frozen state and pre-reading expectations;
3. volume/arc identity;
4. event/scene structure selected for analytical significance;
5. focalization and information-state changes;
6. route/event-state distinctions where relevant;
7. character-state and relationship changes;
8. institutions/factions/status and practical agency;
9. mechanics/world-model claims separated from character theory;
10. ordinary-life evidence where model-relevant;
11. Japanese wording/register notes where interpretation depends on them;
12. claim revision table using `PRESERVE / STRENGTHEN / REVISE / DOWNGRADE / REJECT / OPEN`;
13. counterevidence and rival readings;
14. bounded next-volume questions and expectations;
15. freeze declaration.

## What a deep reading is not

A volume deep reading is not a chapter-by-chapter transcript, plot recap, or wiki replacement. Select scenes because they change an analytical model, expose uncertainty, provide counterevidence, or establish a retrieval point that later work will need.

## Spoiler discipline

Do not consult later main volumes, later-positioned supplements, alternate routes, web-novel text, adaptation episodes, fandom chronologies, or retrospective summaries to make an earlier deep reading look more accurate.

If accidental contamination occurs, identify it explicitly and quarantine the affected claim rather than laundering hindsight into the freeze.

## Supplemental separation

Non-spine material belongs under `03 Supplemental and Alternate Witnesses` until its role is established. Even a mainline supplement should not be embedded inside a numbered volume file unless the source-routing decision intentionally admits it as part of that reading's evidence boundary.
