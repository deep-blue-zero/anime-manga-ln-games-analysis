---
title: "Wandering Witch — Source and Edition Register"
artifact_id: WW_SOURCE_REGISTER
artifact_type: source_edition_register
version: "1.0"
status: canonical
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
authority_generation: WW-INITIAL
authority_scope: "INITIAL bootstrap rules and attributed source metadata only; no literary findings"
source_boundary: "Metadata reconnaissance: Japanese main volumes 01–25 plus separate 2014 Upper and Lower editions; no narrative admitted"
created: 2026-11-07
last_updated: 2026-11-07
---

# Source and edition register

## What is known, and from which layer

The 2026-11-07 campaign metadata reconciliation reports twenty-seven current primary EPUB witnesses: main Japanese V01–25 and separate 2014 original Upper/Lower editions. The governed *Elaina / Wandering Witch* evidence collection and its historical manifest dated **2026-08-31** supply the administrative basis. Private source resolution belongs to the governed evidence/campaign receipt; public local keys below do not expose remote identifiers.

The manifest summary reports 27 primary and 32 audited files, 25 main volumes, two original parts, five archived alternatives, 27 passing ZIP CRC/container checks and 32 packaging-conformant files. It reports Japanese metadata for all primary witnesses and no currently grouped exact/content-equivalent primary duplicates. Those are attributed historical checks, not independently repeated checks of present remote bytes.

Five archived alternatives concern main V03, V04, V08, V16 and V17. The historical comparisons report matching publication-content entries except package metadata and cover images, with higher-resolution-cover versions selected as primary. This project has not independently revalidated that equivalence. They are provenance copies, not extra volumes; an image difference remains relevant to visual claims even if prose equivalence is later proven.

## Unresolved audit-history contradiction

The same manifest retains `audit_notes` describing only nineteen audited EPUBs, missing main V01/V12/V13/V14 within range 1–17, and a missing original Upper. Other notes say no main gaps in the observed numeric range and describe a quick Japanese-language scan. Current listing and summary fields support the twenty-seven-witness inventory, but do not establish when or how the contradictory notes became stale.

Do not present the metadata as a single clean completed audit. Retain both claims with their scope: current reported presence is supported; historical narrative consistency is unresolved. Resolving this requires an authoritative corrected audit history or a new bounded verification, not deleting the inconvenient notes.

The original Upper/Lower metadata belongs to 2014 separate editions. Original Lower is explicitly **not** main GA Novel V01. No passage equivalence, publication-to-story chronology, authorial revision intent or shared continuity has been established by this bootstrap.

## Current reported witness inventory

Presence for every row is `METADATA_REPORTED_PRESENT`. “NOT_INSPECTED” means no analytical primary inspection in this project; it does not negate the historical auditor's reported actions.

| Public local key | Source unit | Language basis | Lane | Current immutable bytes | Project admission / inspection |
|---|---|---|---|---|---|
| WW-MAIN-V01 | Main V01 | ja, reported | Main candidate | NOT_VERIFIED | NOT_ADMITTED / NOT_INSPECTED |
| WW-MAIN-V02 | Main V02 | ja, reported | Main candidate | NOT_VERIFIED | NOT_ADMITTED / NOT_INSPECTED |
| WW-MAIN-V03 | Main V03 | ja, reported | Main candidate | NOT_VERIFIED | NOT_ADMITTED / NOT_INSPECTED |
| WW-MAIN-V04 | Main V04 | ja, reported | Main candidate | NOT_VERIFIED | NOT_ADMITTED / NOT_INSPECTED |
| WW-MAIN-V05 | Main V05 | ja, reported | Main candidate | NOT_VERIFIED | NOT_ADMITTED / NOT_INSPECTED |
| WW-MAIN-V06 | Main V06 | ja, reported | Main candidate | NOT_VERIFIED | NOT_ADMITTED / NOT_INSPECTED |
| WW-MAIN-V07 | Main V07 | ja, reported | Main candidate | NOT_VERIFIED | NOT_ADMITTED / NOT_INSPECTED |
| WW-MAIN-V08 | Main V08 | ja, reported | Main candidate | NOT_VERIFIED | NOT_ADMITTED / NOT_INSPECTED |
| WW-MAIN-V09 | Main V09 | ja, reported | Main candidate | NOT_VERIFIED | NOT_ADMITTED / NOT_INSPECTED |
| WW-MAIN-V10 | Main V10 | ja, reported | Main candidate | NOT_VERIFIED | NOT_ADMITTED / NOT_INSPECTED |
| WW-MAIN-V11 | Main V11 | ja, reported | Main candidate | NOT_VERIFIED | NOT_ADMITTED / NOT_INSPECTED |
| WW-MAIN-V12 | Main V12 | ja, reported | Main candidate | NOT_VERIFIED | NOT_ADMITTED / NOT_INSPECTED |
| WW-MAIN-V13 | Main V13 | ja, reported | Main candidate | NOT_VERIFIED | NOT_ADMITTED / NOT_INSPECTED |
| WW-MAIN-V14 | Main V14 | ja, reported | Main candidate | NOT_VERIFIED | NOT_ADMITTED / NOT_INSPECTED |
| WW-MAIN-V15 | Main V15 | ja, reported | Main candidate | NOT_VERIFIED | NOT_ADMITTED / NOT_INSPECTED |
| WW-MAIN-V16 | Main V16 | ja, reported | Main candidate | NOT_VERIFIED | NOT_ADMITTED / NOT_INSPECTED |
| WW-MAIN-V17 | Main V17 | ja, reported | Main candidate | NOT_VERIFIED | NOT_ADMITTED / NOT_INSPECTED |
| WW-MAIN-V18 | Main V18 | ja, reported | Main candidate | NOT_VERIFIED | NOT_ADMITTED / NOT_INSPECTED |
| WW-MAIN-V19 | Main V19 | ja, reported | Main candidate | NOT_VERIFIED | NOT_ADMITTED / NOT_INSPECTED |
| WW-MAIN-V20 | Main V20 | ja, reported | Main candidate | NOT_VERIFIED | NOT_ADMITTED / NOT_INSPECTED |
| WW-MAIN-V21 | Main V21 | ja, reported | Main candidate | NOT_VERIFIED | NOT_ADMITTED / NOT_INSPECTED |
| WW-MAIN-V22 | Main V22 | ja, reported | Main candidate | NOT_VERIFIED | NOT_ADMITTED / NOT_INSPECTED |
| WW-MAIN-V23 | Main V23 | ja, reported | Main candidate | NOT_VERIFIED | NOT_ADMITTED / NOT_INSPECTED |
| WW-MAIN-V24 | Main V24 | ja, reported | Main candidate | NOT_VERIFIED | NOT_ADMITTED / NOT_INSPECTED |
| WW-MAIN-V25 | Main V25 | ja, reported | Main candidate | NOT_VERIFIED | NOT_ADMITTED / NOT_INSPECTED |
| WW-ORIG2014-UPPER | Original 2014 Upper | ja, reported | Separate earlier edition | NOT_VERIFIED | NOT_ADMITTED / NOT_INSPECTED |
| WW-ORIG2014-LOWER | Original 2014 Lower | ja, reported | Separate earlier edition, not main V01 | NOT_VERIFIED | NOT_ADMITTED / NOT_INSPECTED |

## Operational schemas

| Record | Required fields |
|---|---|
| Witness version `WW-WV-nnnn` | Local key/version; bibliographic title/creator/publisher/edition as established or UNKNOWN; language metadata and inspected-language status; immutable digest/byte count; governed receipt reference; container/spine/extraction version; primary/archived/derivative relation; verifier/date; identity/equivalence status and evidence |
| Component coverage `WW-COV-nnnn` | Witness version; verified spine/member/heading; narrative/illustration/front matter/afterword/bonus/preview/unresolved type; intended order; exact authorized/inspected extent; TEXT or STILL_IMAGE lane; exclusion/debt; reading route; retrieval result; acceptance boundary |
| Edition/variant relation `WW-ER-nnnn` | Two exact witnesses; proposed relation; alignment operation and scope; mapped and unmatched components; identity/wording/image differences; confidence; independent verification; interpretation limits; separate admission state |
| Source discrepancy `WW-SD-nnnn` | Conflicting metadata statements and dates/scopes; evidence supporting each; provisional operational decision; unknown cause; correction receipt; affected witness/coverage/claim routes; append-only resolution |

Witness identity, source admission, inspection and analytical closure are separate states. Use `NOT_VERIFIED / VERIFIED / CHANGED_UNRESOLVED`; `NOT_ADMITTED / AUTHORIZED_NOT_ADMITTED / ADMITTED`; `NOT_INSPECTED / PARTIAL / COMPLETE_FOR_DECLARED_COMPONENTS`; `NOT_STARTED / IN_PROGRESS / ACCEPTED_AT_BOUNDARY` respectively. A historical integrity check cannot advance any other state automatically.

No chapter IDs, narrative locators or edition alignments are invented now. The actual source mapping will use the verified spine plus bounded inspection. Changed bytes create a new version and trigger locator/dependency review rather than overwriting a witness.

## Initialized gaps and discrepancy

| ID | Evidence-limited fact | State and effect | Closure evidence |
|---|---|---|---|
| WW-SG-001 | No current immutable receipt, exact spine/chapter mapping or project inspection | OPEN; all twenty-seven unadmitted | Bind exact bytes, language, container and source units through actual permitted verification |
| WW-SG-002 / WW-SD-001 | Current 27-primary/25-main/2-original summary conflicts with stale 19-file/missing-items audit notes | OPEN; presence can be recorded, clean audit cannot | Corrected authoritative history or a new verification retaining the prior contradictory statements |
| WW-SG-003 | Earlier originals have no verified passage/continuity relationship to main editions | OPEN; comparison lane remains separate | Separately authorized, exact aligned and unmatched passage audit; Lower never substitutes main V01 |
| WW-SG-004 | Five archived cover alternatives have historical equivalence claims only | OPEN; no independent equivalence/image certification | Recheck exact variants if needed for a claim; retain distinct visual identity and provenance |
| WW-SG-005 | Supplied numeric range and Japanese metadata/quick scan do not certify official completeness or all-content/visual quality | OPEN; no full-work/source-complete claim | Verify selected scope and required components; separately establish any publication extension |

## Update and history

The source custodian proposes identity/coverage evidence; the designated series integrator owns the current register. Append witness versions, relations and discrepancy resolutions. Preserve the exact earlier claim and its boundary when correcting metadata. Never remove originals or archived copies based only on naming similarity.

An admitted reading updates component coverage only after actual inspection, with image and paratext debts visible. A change in source bytes or alignment reopens affected evidence routes and notifies the dependency register. Private receipts stay outside public Git; short public-safe references and verified digests may be used when eligible.

| History ID | Date | Operation | Result |
|---|---|---|---|
| WW-SH-001 | 2026-11-07 | Initialized from current campaign metadata and attributed historical manifest | 27 reported current witnesses; stale audit contradiction and five gaps retained; no narrative admission |
