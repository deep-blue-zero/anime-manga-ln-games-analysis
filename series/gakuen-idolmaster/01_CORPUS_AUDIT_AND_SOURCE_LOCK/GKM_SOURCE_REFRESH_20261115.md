---
title: "Gakuen Idolmaster V2 — Transcript refresh, 2026-11-15"
project: "Gakuen Idolmaster / 学園アイドルマスター"
document_type: "versioned source lock and corpus comparison"
version: "1.0"
phase: "0 - Corpus Audit and Source Lock"
source_lock: "GAKUMAS V2 Source Lock 1.1 baseline and Source Lock 1.2"
status: "canonical Source Lock 1.2 declaration and comparison"
---

# Transcript refresh — 2026-11-15

## Source identities

[Source Lock 1.1](GKM_SOURCE_REFRESH_20261112.md) pins revision 86. Revision 88 is its direct child in `DreamGallery/Campus-adv-txts`. Each expanded archive accounts for the entire `Resource/` tree of its pin. The local predecessor folder suffix records when the copy was set aside. The generated timestamp comes from the provenance file inside that archive.

| Source state | Local snapshot name | Commit | Upstream revision | Archive generated in UTC |
| --- | --- | --- | ---: | --- |
| Source Lock 1.1 | `gakuen-idolmaster-transcripts-archive.pre-update-20261115` | `82412aa5029abd363e68aec145e36525cf9b6b06` | 86 | 2026-11-12T04:44:04Z |
| Source Lock 1.2 | `gakuen-idolmaster-transcripts-archive` | `f8ff5ef7b243f2f7e3b2723def31072874539ca9` | 88 | 2026-11-15T17:13:55Z |

| SHA-256 control | Revision 86 | Revision 88 |
| --- | --- | --- |
| `00_context/manifest.csv` | `273e4b4ecf9f913774574b0d22e9d2be49a1007457560d3b110183bccc6e2f22` | `10ad24271fbf7d322284a8364af09ba3551635ea4e793f2046dbdb491ce2c423` |
| `00_context/manifest.json` | `3c8d654b11560132bb759f6d2f31f98741d01c05f55df1eb5f8607e2c1371130` | `d6d922a20cd599555d7ea687d092b92f248502ea4c8b8299f24438375a5c147e` |
| `00_context/category_counts.json` | `45e38f4400dfeede79a2174eae91ee53ba82cb6f60459e3a7feb754809189459` | `6b6ccc4a0d229f09c2ec3a72c2c230d643a343a31845ef056575197f089df6d2` |
| A1 raw inventory | `4a6ef6aae83039adf6cea80567c972bdc3a1301a5f9d5198dfa23b9700331158` | `3f04f275a8d18ae1d2741bcf4e0b63a1666a905a921d117779a55a7fb477a599` |
| A2 exact-byte inventory | `f9823e1af252fc96daccca85ddc601772236c42a10b32b8ee6222720e660bf3a` | `c6ee96ed4f8da720dedbf4ba35f2a17e73b3d2a03228a952d2b565344fbb5d4b` |

The [source delta](GKM_SOURCE_DELTA_20261115.tsv) records all 103 additions once. Its SHA-256 is `ab4d444bceee7aa6e1246face80aab6c83cbd2a653576c9326afae6d21d132b2`. All 3,949 previous original names retain their archive paths, categories, raw SHA-256 and Git blob IDs. Existing A2 paths and exact bytes also match. There are zero removals, byte revisions, path moves or category changes. The upstream diff also changes the repository revision marker.

## Source families

| Category | Revision 86 objects / A2 messages | Revision 88 objects / A2 messages | Added objects / messages | Source family in the addition |
| --- | ---: | ---: | ---: | --- |
| Idol communications | 366 / 15,455 | 369 / 15,574 | 3 / 119 | Kanae rank 3, episode 000, parts 01–03 |
| Support cards | 540 / 10,618 | 547 / 10,757 | 7 / 139 | `1-0013` (2 / 40), `2-0084` (2 / 40), `3-0115` (3 / 59) |
| Dear Idol | 510 / 34,473 | 520 / 35,288 | 10 / 815 | `adv_dear_hkne_001.txt` through `adv_dear_hkne_010.txt` |
| Live | 106 / 194 | 114 / 209 | 8 / 15 | Kanae live 001, four opening and four closing variants |
| Produce events | 1,107 / 13,825 | 1,140 / 14,555 | 33 / 730 | P1 Kanae activity 001–020 (22 files / 497 messages, 017 and 018 each split), school 001–011 (11 / 233) |
| Growth | 39 / 150 | 42 / 162 | 3 / 12 | `adv_pgrowth_001_hkne_01.txt` through `_03.txt` |
| Produce step | 217 / 0 | 224 / 0 | 7 / 0 | Six common step/phase files and one Kanae rest file under the common prefix |
| Produce main story | 622 / 11,772 | 653 / 12,444 | 31 / 672 | Kanae P1 openings (7 / 41), after-step 1–2 (6 / 148), mid/final audition before and after (12 / 298), endings (6 / 185) |
| Startup | 33 / 219 | 34 / 225 | 1 / 6 | `adv_startup_2026_user-bd-01_hkne-01.txt` |
| **Full archive** | **3,949 / 100,847** | **4,052 / 103,355** | **103 / 2,508** | |

The additional files contribute 16,066 raw lines and 2,508 raw `[message …]` commands. They use existing archive categories and command types. The additions include 177 `branch`, 66 `branchgroup` and 64 `choicegroup` commands, and 1,781 `voice` commands. The seven message-free Produce-step scripts each carry a voice command along with staging instructions. Review these objects in A1. Base continuity dispositions on the commands and readings for each state, including scripts whose filenames say `normal`, `failure` or `true`.

## Derivative and deduplication controls

- **A1.** All 3,948 and 4,051 UTF-8 objects respectively match their pinned Git blob after CRLF-to-LF normalization. The opaque `musics.txt` matches its Git blob byte for byte in both snapshots. Archive SHA-256 always uses exact local bytes. Each of the 103 new objects has a Git blob ID distinct from every other revision 88 object.
- **A2.** Exact extractor reconstruction matched all 3,575 and 3,671 dialogue derivatives. The 96 new A2 payloads have distinct SHA-256 even after the source-file headers are excluded. Seven new message-free steps account for the increase from 374 to 381 objects without A2. The raw message totals are 100,866 and 103,374. The same 19 extractor omissions occur in four inherited files: `adv_dear_hrnm_012.txt`, `adv_dear_hume_009.txt`, `adv_dear_shro_035.txt` (16), and `adv_live_kcna_001_start-01-01.txt`.
- **A3.** The manifests record 3,818 → 3,832 memberships and 3,785 → 3,799 distinct A1 identities. In each snapshot 25 A1 identities occur across bundle families and eight additional memberships repeat within the shared family. The seven support additions and seven common steps account for the increase. The bundle builder still lacks `hkne` in its character map. It retains 13 character bundles and 2,725 character-assigned objects, while the unassigned inventory grows from 164 to 253. The 89 newly unassigned Kanae objects contain 2,369 extracted messages. Use the A1 locator in the delta TSV for all 89 objects. The earlier five horizontal scripts keep their Source Lock 1.1 locators.

## Scope and source admission

This transaction designates revision 88 as **GAKUMAS V2 Source Lock 1.2** under the [live-service update policy](GKM_SOURCE_LOCK.md#6-live-service-update-policy). The delta adds Kanae's first playable Produce material evidenced in the archive and the Dear chain through 010, within existing story families, extraction rules and evidence classes. It establishes a bounded character reading under the current V2 architecture. Source Locks 1.0 and 1.1 identify the older analytical and archive boundaries. Earlier findings retain the force of their original evidence, with the formerly open transfer proposal resolved in the new chain.

Read the [Kanae revision 88 analysis](../03_SOURCE_FACING_READINGS/01_CHARACTER_CORE_READINGS/14_HIWATARI_KANAE/GKM_HIWATARI_KANAE_SOURCE_LOCK_12_READING.md) for the character, care partnership, institutional admission, rival aspiration and state-specific Produce claims. The [source locator](../04_CUMULATIVE_LEDGERS_AND_INDICES/GKM_PRIMARY_SOURCE_LOCATOR_LEDGER.md#source-lock-12--transcript-refresh-2026-11-15) exposes the six coverage groups and their ledger routes. The continuing [historical-audit dispositions](GKM_HISTORICAL_AUDIT_DISPOSITIONS_20261112.md) refer to Source Lock 1.0. The [Carbon supplement](../05_AUDIOVISUAL_ANALYSIS/GKM_CARBON_AV_OBSERVATION_PACKET.md#source-lock-12--kanae-candidates) records acquisition targets for the new transcript evidence.

## Source-reading and integration receipt

The owner requested one bounded release-delta operation after refreshing the local archive and directed application of the source-reading protocol from [PR #599](https://github.com/deep-blue-zero/anime-manga-ln-games-analysis/pull/599) section 4.1 at `85fc1fd7975c3c9b9592e52e3740f3b4bb8c4362`. The standing configuration is in the [current entrypoint](../CURRENT_STATE_AND_CORPUS_MAP.md#standing-execution-configuration-for-transcript-refreshes). The proposal was open at adoption. The transaction used the live publication policy from `main`. Windows local tool runtime served the Japanese A1 textual lane and command inspection. Model identifiers and reasoning efforts were unobserved.

The entering evidence was Source Lock 1.1, with Kanae's horizontal proposal unresolved there. This is retrospective comparison of the complete bounded update with that accepted state. There was no prospective question freeze or prediction credit. The narrative reading stopped at the revision 88 objects and admitted comparison witnesses.

| Responsibility | Inspection actually completed | Governance and disposition |
| --- | --- | --- |
| Principal reader and integrator | All 103 new A1 objects. All added Japanese messages, local choice and condition alternatives, and staging and voice commands relevant to the new claims. Rechecked H02–H05 physical lines for the winter recap, speech, running echoes, H.I.F. and missed-live promise. | Integrated the canonically routed analysis, sourcing, prior claim revisions and 1.2 ledger rows. Personally checked the primary text and evidence limits behind all accepted claims. |
| Provenance specialist | Both complete manifests, upstream tree identities, exact archive SHA-256, raw command counts, derivative bytes and A3 inventories. | Accepted the 103-row delta and hash controls. All 3,949 predecessor objects remain verifiable through their original locators. |
| Character and register specialist | All ten Dear, three communication, and seven support additions (20 / 1,073), with five previously admitted horizontal files as entering context (326 messages). | Adopted the explicit two-part continuation and wording echoes, distinct preference contexts, and scoped jealousy, reciprocity and honorific claims. |
| Route and state specialist | All 31 Produce main, eight live, and three growth additions (42 / 699), 10 diagnostic event scripts (191 messages), and five already admitted comparison objects at targeted depth. | Verified transfer after China's title, multiple grade-dependent responses, current dual production, nested conditions and two failed normal endings. Left exact route eligibility, result dispatch and calendar matching open. |
| Independent critical reviewer | Fresh A1 sampling before the integrated draft across the entering chapters, Dear, P1, school/activity, commu, support, and command-only scripts. Independently checked the hashes of all 103 additions and four inherited witnesses. Rechecked the repaired reading. | Accepted the draft after narrowing a normal-ending debrief to overall results, distinguishing placeholder voice slots, scoping past clothing selection and the early run, citing the Han Xin branch, and preserving unknown condition dispatch. Added the school-entry wording and smaller phrasing corrections. No material dispute at closeout. |
| Audiovisual candidate specialist | Script identities and local metadata catalogs for Dear 004–005 and 008–010, the rank-3 solo communication, and Produce wrappers and steps. Checked the inherited Carbon register for the horizontal prologue. | The local scan found no matching recording. The specialist proposed P0 for Dear 008–009. Final priority is P1 because the declared ambition and advancement result are explicit in A1 and playback could substantially refine their staging. Five new rows are designated P1, P2, or deferred acquisition. The horizontal prologue keeps its separate target. AV-C only. |

The principal checked named subjects and referents in the entry, D001 household and Producer exchange, D005–010, Produce outcome sections, communication/support sections and claim dispositions. The unnamed player character is identifiable as Producer, the claimed raw player-name token is preserved, and the headmaster and Kuramoto grandfather act in distinct capacities. Role titles remain where service practice or authority matters. The current reading separates present speech, quoted memory, reported judgments, inner speech and alternate options.

The result freezes Kanae's textual boundary through Dear 010 and Produce 001, with the rank-3 episode 000 as a separate source family. Plot facts still open include the exact previous China Produce path, gameplay dispatch and scheduling across modular stories. Native audiovisual recordings and calibrated offsets are separate evidence obligations. Direct listening and continuous-motion review totaled zero seconds.

## Reproduction

1. Compare the declared source pins and their `revision` files with the two local provenance records. Use `git ls-tree -r -z <pin> -- Resource` for each pin. Run `git diff --name-status --no-renames <revision-86-pin> <revision-88-pin>` to reconcile the change set.
2. Reconcile the CSV and JSON manifests row for row, including nullable A2 paths and integer counts. Check unique source names and A1/A2 paths, exact sets of archive files, manifest sizes, and category totals. Compute each raw SHA-256 from bytes. Compute Git blob IDs as SHA-1 of `blob <length>\0` followed by bytes. Compare exact bytes first, then apply CRLF-to-LF normalization to text files that require it.
3. For each inventory fingerprint, sort objects by original name. Join `original_name`, the archive-relative path for that layer and the exact byte SHA-256 with tabs. Encode as UTF-8 with LF after every row, then hash the result. For A2, use only objects with a derivative.
4. Count raw `[message ` commands. Reconstruct A2 with the extraction patterns `\btext=(.*?)\s+name=` and `\bname=(.*?)\s+(?:se=|hide=|clip=)` plus the builder’s header, embedded-line-break conversion and paragraph separators. Compare every derived file byte for byte. Count A3 memberships from the bundle manifests, validate source locators against the corresponding A1 manifest, and reconcile the union plus the unassigned report to the complete A1 inventory.
5. Outer-join on original name and compare archive-relative paths and exact hashes. Group the 103 new objects by manifest category and filename family. Count command tokens at the beginning of A1 script lines and compare their vocabulary against the predecessor. Compare each new Git blob ID and headerless A2 payload SHA-256 against all revision 88 IDs and payloads.
