---
series: RE_ZERO
artifact_type: source_lock
scope: SOURCE_ADMISSION_CONTRACT_AND_CURRENT_INVENTORY_STATE
generation: V0.1
status: canonical
release_state: mutable_active
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
---

# Re:Zero — source lock and inventory

## Current lock state

**UNLOCKED.** This bootstrap does not claim possession, completeness, edition identity, publication order, or integrity for any Re:Zero primary-source object.

No source-facing analytical artifact should describe itself as a complete or source-locked Re:Zero reading until this document is updated from verified evidence.

## Authority responsibility

This file owns the Git-side record of **which source witnesses have been admitted for analysis and what each witness is allowed to support**.

Primary-source binaries and extraction products remain outside this analytical Git root. This file may record governed references, identifiers, hashes, filenames, edition metadata, and audit results when they are actually verified.

## Required admission record

For each admitted source item, record at least:

| Field | Requirement |
|---|---|
| `source_id` | stable local analytical identifier |
| `witness_class` | one of the classes defined by `REZERO_ROUTE_AND_WITNESS_PROTOCOL.md` |
| `language` | source language |
| `edition/publisher` | edition identity when available |
| `title` | source title as printed/encoded |
| `main_volume` | global numbered volume when applicable |
| `arc` | source-verified arc identity when applicable |
| `publication_date` | verified or explicitly unknown |
| `provenance_anchor` | governed Drive/reference locator when allowed |
| `integrity` | hash/audit status when available |
| `analytical_horizon` | earliest point at which prospective analysis may open it |
| `notes` | ambiguity, duplicate, variant, or routing concerns |

## Source families to inventory separately

Do not assume all of these are present. Inventory only what is actually acquired.

- Japanese numbered main light novels;
- Japanese mainline supplemental/EX/short-story material;
- Japanese IF or other alternate-route material;
- web-novel material if intentionally admitted;
- official translations if intentionally admitted as convenience/comparison witnesses;
- anime video/audio/subtitle witnesses if adaptation analysis is planned;
- official reference books, interviews, game/event scripts, or other sources only when a defined analytical responsibility exists.

## Main-light-novel lock requirements

Before `REZERO_LN_V01_DEEP_READING.md` begins:

1. verify the exact Volume 01 object and edition;
2. verify language and readable text integrity;
3. establish a stable source identifier and provenance anchor;
4. record its hash or equivalent audit evidence if available;
5. confirm that no later-volume text is bundled into the analytical input;
6. record any translation witness separately rather than merging text streams.

Before claiming a continuous `V01-VNN` corpus, verify every numbered item and gap explicitly.

## Supplemental placement control

Acquisition does not authorize reading.

For each supplemental witness, record:

- witness class;
- publication relationship to the main spine;
- diegetic/route relationship if source-grounded;
- spoiler/information risks;
- earliest safe insertion horizon;
- whether the placement is `VERIFIED`, `PROVISIONAL`, or `OPEN`.

If the appropriate horizon is unknown, leave the material unopened for prospective analysis.

## Version and duplication control

If multiple files appear to represent the same work:

- compare edition metadata;
- compare hashes where available;
- distinguish true duplicates from revised editions, bonus-text variants, or extraction differences;
- do not silently deduplicate semantically distinct witnesses.

Normalized English filenames are locators only. They do not replace Japanese titles or establish canonical terminology.

## Current inventory table

No items admitted yet.

| source_id | witness_class | language | identity | integrity | horizon | status |
|---|---|---|---|---|---|---|
| — | — | — | — | — | — | `UNLOCKED` |

## First source-audit deliverable

The next revision of this file should replace the empty inventory with verified source rows and state whether the main Japanese light-novel spine is sufficiently locked to begin Volume 01.

Do not convert general knowledge about how many Re:Zero volumes, side stories, or adaptations exist into inventory facts. Inventory is an evidence record, not a bibliography assembled from memory.
