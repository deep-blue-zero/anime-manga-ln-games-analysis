---
series: IMOSAE
artifact_type: source_and_coordinate_audit
scope: V01-V14_release_source_integrity_and_route_resolution
generation: V1
status: canonical
source_boundary: Locked Japanese RAW/NORM/visual/gaiji releases; no new source payload or supplemental admission
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
version: '1.0'
date: '2026-10-13'
---

# Main-series source and coordinate audit

**Result: PASS for the checks explicitly listed below.** The [machine receipt](IMOSAE_MAIN_SERIES_SOURCE_AND_COORDINATE_AUDIT.json) records per-volume byte identities and totals. Speaker, narrative level and interpretation are separate semantic review responsibilities; cryptographic integrity alone does not establish them.

| Check actually executed | Result / denominator |
|---|---|
| Locked original Japanese EPUB byte size and SHA-256 | PASS, 14/14; 222,679,906 total bytes |
| ZIP member CRC/integrity | PASS, 14/14 archives |
| Frozen normalized paragraph-sidecar size/SHA-256 | PASS, 14/14 sidecars against immutable release manifest |
| Unique locators, paragraph hashes/fingerprints and annotation bounds | PASS, 34,766 normalized paragraphs |
| Original EPUB source-block XPath resolution | PASS, 34,766/34,766 blocks, using each sidecar member/XPath |
| Ruby/gaiji/format/visual-anchor inventory | 29,083 ruby annotations; 651 gaiji occurrences; 15,175 format annotations; 552 visual anchors |
| Frozen indexed original raster asset SHA-256 | PASS, 666/666 asset members: 104 inline-gaiji members (65 distinct content hashes) and 562 other visual assets |
| Unified prospective E identifiers | PASS, 3,666 unique units; 3,579 prior plus 87 V14 |
| Primary coordinate references | PASS, 3,729 references to exact normalized blocks or frozen visual assets, including legacy role suffixes |
| G005 all-volume occurrence and original glyph/ruby | PASS, exactly two occurrences, V01/V14; matching source image SHA and しか ruby, with explicit analytical override |

The private execution used the locked original EPUBs provided in the authorized source workspace and the canonical sidecar/manifest identities already obtained through Drive intake. Original source domain remains Drive; Git holds analysis, metadata and routing. The new evidence index contains no surface paragraphs, copied volumes or source media. Original and normalized releases remain immutable.

The normalized payload boundary is precise: all fourteen paragraph sidecars were freshly hash-checked here; V14's normalized Markdown identity and full prospective reading were checked in Phase A. Earlier intake refreshed fifteen of thirty-two normalized-release payloads. This report does **not** claim all thirty-two were freshly downloaded or each prior normalized Markdown file independently re-fetched. That is a limitation on the executed check, not a missing original Japanese volume.

Every original block route was computationally resolved. That is not a claim of fresh semantic reading of all thirteen earlier novels or all 562 non-gaiji visuals during Phase F. Prior whole prospective readings/checkpoints remain source-bounded historical authority. Mature specialist/model work reopened diagnostic primary contexts; the release semantic audit states its actual coverage. V14 was read in full publication order with its visual/afterword package before retrospective work began.

The G005 exception demonstrates why the distinction matters. A frozen high-confidence substitute can be semantically wrong while hashes and coordinates remain valid. Both original assets/ruby supply scolding; ordinary Unicode 吐 remains unaffected. The current errata and exact exception metadata expose this without changing RAW/NORM/GAIJI-MAP bytes.

The nineteen protected historical analysis files—thirteen V01–V13 readings, four prior checkpoints and two V01–V06 monographs—are verified separately against the captured baseline in the release integrity review. The new fifth checkpoint, V14 reading, reconciled ledgers and mature products are additional or explicitly logged maintained changes. Full Git preflight, housekeeping and exact-head integration audit remain distinct from this source PASS.
