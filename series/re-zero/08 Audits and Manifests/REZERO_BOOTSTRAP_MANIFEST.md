---
series: RE_ZERO
artifact_type: bootstrap_manifest
scope: GIT_NATIVE_ANALYTICAL_ROOT_BOOTSTRAP
generation: V0.1
status: canonical
release_state: frozen_record
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
---

# Re:Zero — bootstrap manifest V0.1

## Purpose

This manifest records the initial Git-native analytical architecture created for the stable `series/re-zero` branch. It records architecture and governance state, not source findings.

## Base state

- repository: `deep-blue-zero/anime-manga-ln-games-analysis`
- base branch: `main`
- base commit: `f62edb60799f50a255fe2d08a888fdd0bd99dc0d`
- analytical branch: `series/re-zero`
- bootstrap generation: `V0.1`
- source lock at bootstrap: `UNLOCKED`
- substantive Re:Zero findings at bootstrap: none

## Authored paths

- `series/re-zero/.repository/series-registry.json`
- `series/re-zero/CURRENT_STATE_AND_CORPUS_MAP.md`
- `series/re-zero/00 Frameworks and Methods/REZERO_ANALYTICAL_METHOD.md`
- `series/re-zero/00 Frameworks and Methods/REZERO_ROUTE_AND_WITNESS_PROTOCOL.md`
- `series/re-zero/01 Source Lock and Inventory/REZERO_SOURCE_LOCK_AND_INVENTORY.md`
- `series/re-zero/02 Sequential Readings/README.md`
- `series/re-zero/03 Supplemental and Alternate Witnesses/README.md`
- `series/re-zero/04 Longitudinal Ledgers/REZERO_LEDGER_PROMOTION_AND_SCHEMAS.md`
- `series/re-zero/05 Character Analysis/README.md`
- `series/re-zero/06 Adaptation Analysis/README.md`
- `series/re-zero/08 Audits and Manifests/REZERO_BOOTSTRAP_MANIFEST.md`

## Architectural decisions

1. The Japanese published light novel is the intended main semantic anchor once exact witnesses are source-locked.
2. The numbered main light novel receives a prospective volume-by-volume freeze.
3. Repeated/branching event-states are tracked separately from active-world state and from reader-only knowledge.
4. Mainline supplements require verified placement and a safe analytical insertion horizon.
5. IF/alternate routes remain counterfactual witnesses rather than silent main-route additions.
6. Web-novel material remains a developmental/version witness unless future governance deliberately changes its role.
7. Anime is a separate audiovisual witness and receives independent adaptation analysis.
8. Longitudinal ledgers and character monographs are promoted only when evidence creates a real retrieval/revision responsibility.
9. Comparative ethical work, including PACTRIH, remains downstream of source-grounded reconstruction.
10. Character registry maintenance remains outside the series branch's ordinary authoring authority.

## Routing behavior

The branch supplies `series/re-zero/.repository/series-registry.json` as the declarative desired registry row. Repository housekeeping owns synchronization of the global series registry, series README, studies routing surfaces, and corpus index according to the global-index automation policy.

This manifest does not manually claim or rewrite those generated outputs.

## Next analytical gate

The bootstrap is ready for source intake only after repository audit/housekeeping accepts the branch structure.

The next substantive task is to verify and lock the available Japanese Re:Zero source witnesses. Only after Volume 01 is admitted should `REZERO_LN_V01_DEEP_READING.md` be created.
