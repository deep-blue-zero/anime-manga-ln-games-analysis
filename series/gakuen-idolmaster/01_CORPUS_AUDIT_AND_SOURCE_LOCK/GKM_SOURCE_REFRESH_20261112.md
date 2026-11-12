---
title: "Gakuen Idolmaster V2 — Transcript Refresh and Source Delta, 2026-11-12"
project: "Gakuen Idolmaster / 学園アイドルマスター"
document_type: "versioned source lock and corpus comparison"
version: "1.0"
phase: "0 - Corpus Audit and Source Lock"
source_lock: "GAKUMAS V2 Source Lock 1.0 baseline and Source Lock 1.1"
status: "canonical Source Lock 1.1 declaration and comparison"
---

# Transcript refresh and source delta — 2026-11-12

## Compared source states

[GKM Source Lock](GKM_SOURCE_LOCK.md) defines the frozen 1.0 corpus. The revision 32 local copy matches the canonical manifest and category-count checksums. The two local snapshots each enumerate the complete `Resource/` tree at the stated commit in the DreamGallery/Campus-adv-txts clone. Revision 32 is an ancestor of revision 86. The generated timestamps identify extraction snapshots.

| State | Local archive directory | Upstream commit | Revision | Archive generated UTC | Raw objects | Extracted messages |
| --- | --- | --- | --- | --- | ---: | ---: |
| Source Lock 1.0 | `gakuen-idolmaster-transcripts-archive.pre-update-20260921` | `00d150a069a3ffa723a1ff264752ba242024caad` | 32 | 2026-08-02 22:21:04 | 3,777 | 93,924 |
| Source Lock 1.1 | `gakuen-idolmaster-transcripts-archive` | `82412aa5029abd363e68aec145e36525cf9b6b06` | 86 | 2026-11-12 04:44:04 | 3,949 | 100,847 |

The other local snapshots capture revisions 454 (June 21 archive), 28 (July 27), 62 (September 21), 67 (October 5) and 69 (October 14). Their suffixes identify when they were set aside. The provenance file inside each snapshot identifies when it was generated. The two compared snapshots are locally available under the Gakuen Idolmaster extraction workspace. Source Lock 1.0 retains its registered Drive archive identity and its original scope.

| SHA-256 control | Source Lock 1.0 | Revision 86 |
| --- | --- | --- |
| `00_context/manifest.csv` | `82ed6510a74bfa278591ddcaefa35f771423228eb62c5e03d820d4f4362196b1` | `273e4b4ecf9f913774574b0d22e9d2be49a1007457560d3b110183bccc6e2f22` |
| `00_context/category_counts.json` | `41838e3b05d3fc348735d073a132e3e77a8b7c5c02f21cd33955cf382040d878` | `45e38f4400dfeede79a2174eae91ee53ba82cb6f60459e3a7feb754809189459` |
| Raw identity/hash inventory | `dd96b8349e2e2b0ab5f9935bd81efaba11bcfa024074e67edb1caf6deffe02e1` | `4a6ef6aae83039adf6cea80567c972bdc3a1301a5f9d5198dfa23b9700331158` |

## Identity and coverage reconciliation

[Per-object source delta](GKM_SOURCE_DELTA_20261112.tsv) records all 195 changed identities, with archive-relative A1 paths, both snapshot hashes where applicable, message and line counts, change flags and preliminary analytical routing. The delta TSV SHA-256 is 8690ddc13509049806cd774766b71ab59dbf4eeb92cb0602ce792d04be3cbe41. Filename and A1 actor-code hints assist assignment. Source participants, story states and claim dispositions are established in the corresponding readings.

| Identity disposition | Count |
| --- | ---: |
| Same original identity, archive path, category and raw SHA-256 | 3,754 |
| New upstream filename | 172 |
| Same original identity and path, new raw bytes | 13 |
| Same upstream filename, category and raw bytes, changed archive path | 10 |
| Removed or missing upstream/archive objects | 0 |
| Content-modified and moved | 0 |
| Byte delta limited to line-ending normalization | 0 |

The 10 moves are pre-existing Dear Idol episode `010-01` scripts. The sorter moved them from the generic Dear directory to the respective character directories. Their old locators remain valid for the 1.0 snapshot. The new locators refer to the same A1 material.

| Category | 1.0 objects / messages | Revision 86 objects / messages | Added | Modified | Moved | Net messages |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Idol communications | 321 / 13,616 | 366 / 15,455 | 45 | 2 | 0 | +1,839 |
| Support cards | 498 / 9,777 | 540 / 10,618 | 42 | 1 | 0 | +841 |
| Dear Idol | 462 / 31,438 | 510 / 34,473 | 48 | 3 | 10 | +3,035 |
| Numbered events | 136 / 8,507 | 151 / 9,456 | 15 | 1 | 0 | +949 |
| Produce events | 1,101 / 13,716 | 1,107 / 13,825 | 6 | 2 | 0 | +109 |
| Produce main story | 608 / 11,626 | 622 / 11,772 | 14 | 1 | 0 | +146 |
| Startup and seasonal | 31 / 215 | 33 / 219 | 2 | 0 | 0 | +4 |
| Produce step | 217 / 0 | 217 / 0 | 0 | 1 | 0 | 0 |
| Unit | 66 / 4,525 | 66 / 4,525 | 0 | 1 | 0 | 0 |
| Music index | 1 / 0 | 1 / 0 | 0 | 1 | 0 | 0 |
| Other unchanged categories | 336 / 504 | 336 / 504 | 0 | 0 | 0 | 0 |
| Total | 3,777 / 93,924 | 3,949 / 100,847 | 172 | 13 | 10 | +6,923 |

The raw scan found 93,943 and 100,866 `[message …]` commands respectively. In each snapshot, 19 fall outside the archive extractor's `text=… name=` pattern. There are 3,403 and 3,575 dialogue derivatives respectively, with exact manifest coverage. Both archives have 374 objects with no derivative. Use A1 for the 19 omitted raw commands, inner speech and choice context, and for all script-visible timing, non-message commands and voice, music and motion references. A3 assignment and overlap stay outside the A1 count. The bundle validator reports 2,615 → 2,725 character-assigned files, 402 shared files in both archives, and 159 → 164 ambiguous or unassigned files. The increase of five warrants separate routing even though the A1 inventory reconciles.

## Modified-object findings

Thirteen existing upstream objects change bytes, all with the same extracted message count. Three change ordered Japanese message text. Recognized speaker sequences are stable across the modified scripts. The common P3 Produce event is the only modified script with a different sequence of inline ruby readings.

- `adv_cidol-hrnm-3-018_03.txt` changes the Producer's description of Rinami's work from `パーソナリティ` to `ゲスト出演`. A motion clip also changes. References to the assignment should use the correct version.
- `adv_csprt-3-0063_03.txt` changes China's `おススメ` to `おすすめ` in her report that she watched Lilja's anime recommendation. This is an orthographic correction.
- `adv_pevent_003_cmmn_school_1-006-02.txt` changes three ruby readings of `一番星` from `プリマステラ` to `トップアイドル` and changes the third choice from `測れない` to `計れない`. The displayed option order and concepts are stable. Treat choice text and target mapping as A1 evidence. Its sibling `-03.txt` changes staging/voice metadata and retains the ordered message text.
- `adv_cidol-hski-3-015_03.txt` restages a Saki/Temari/Kotone scene, with actor, facial, camera, voice, SE, BGM and message-timing changes. The ordered message text is unchanged. Match script revision before using the scene for AV comparison.
- Tsubame Dear 020 and 022 and Sena Dear 025 change fade, camera, actor and/or light-related commands. Event 001 part 03, one common Produce step, Temari's P1 normal after-step and U1 Episode 04 part 07 likewise change non-message commands. Their wording is unchanged. Scene- or performance-level claims may still depend on the changed metadata.
- `transcripts_raw/98_miscellaneous/musics.txt` is the sole object in each snapshot that fails strict UTF-8 decoding. It is present in the manifest and matches its pinned Git blob byte for byte. Its changed payload requires separate format verification before its content can inform the musical identity ledger.

## Admission and scope

**Source Lock 1.1 admits the revision 86 ADV snapshot**, under [GKM Source Lock §6](GKM_SOURCE_LOCK.md#6-live-service-update-policy). The delta extends the existing Produce, Dear, communication, event and support families and preserves the A1 acquisition and derivative model. The 172 additions account for 4.6% of the baseline object count. Full source-first reading of the new arcs and scrutiny of the 13 revised objects are required. The evidence favors targeted continuation within the existing architecture. The five new `adv_dear_hkne_000-0*-horizontal.txt` objects require an explicit route and character-status disposition. The A1 reading identifies Hiwatari Kanae and Kuramoto China in a five-part horizontal arc, with internal C1 ordering and a D-CHINA-compatible winning state. The scripts do not establish a playable-character promotion or universal placement in Produce.

This declaration fixes the revision 86 textual boundary. Scope each new analytical result to the applicable revision. Source Lock 1.0 findings remain tied to their original bytes and evidence boundary. The version decision leaves the Rinha audiovisual gate and Phase 7 authority with their governing documents. The current corpus map records the admission state separately from analytical coverage.

## Reading coverage and assignment

- Read the winter Tsubame, Kotone and Sena Dear episodes 028–037 and the new character-specific P3 selection/final variants, activity scenes and Sena explanation scenes with branch and route boundaries preserved. Determine the status of the thirteen `037-01` items and the five Kanae horizontal arc parts from the raw scripts.
- Read new communication episodes as episode families with ordered parts. Follow material cross-track evidence into the affected subjects' character homes, especially where the encounter adds evidence beyond the filename subject. Recheck the Saki and Rinami communication revisions separately.
- Read Events 027, 028 and 030 in episode order. Event 029 has four unchanged scripts in both snapshots and remains in the baseline tranche. Read the changed Event 001 staging against its old version.
- Read the sixteen new support-card story families and the changed `3-0063` part 03. Update participant and source-location records. Treat story order as internal and preserve uncertainty about alignment to individual Produce or Dear routes.
- Read both Saki startup clips as seasonal frames. Reconcile the school-event choice edit, non-verbal Produce/Unit changes and song-index uncertainty with their ledger or AV owners.
- Track every material object through an actual reading or a justified technical disposition before declaring revision 86 analytical coverage. Corpus comparison establishes inventory coverage only.

## Reproduction

1. Read each snapshot's `00_context/manifest.csv` using its column headers. Verify unique original names and sorted raw paths, equality of listed and actual A1 paths, and equality of listed and actual derivative paths. Use `git ls-tree -r -z <commit> -- Resource` in the upstream clone for each expected filename and Git blob ID.
2. Compute SHA-256 on exact archive bytes and check `size_bytes`. Confirm the Git blob ID by SHA-1 of `blob <length>\0` followed by file bytes. In both local snapshots all Japanese ADV matches the pinned Git blobs after CRLF-to-LF normalization (3,776 and 3,948 objects respectively). `musics.txt` already matches without normalization. Use the exact archive bytes for the archive SHA-256 in the delta.
3. Hash the full archive inventory as UTF-8 with LF terminators. Sort by `original_name` and emit one line per object, with the original name, archive-relative sorted path and lowercase raw SHA-256 separated by tabs. Verify the inventory fingerprints above.
4. Outer-join manifests on original name for comparison and record both exact source identities. Use raw SHA-256 to distinguish changed content from sorter moves. Compare against `git diff --name-status --find-renames <old> <new> -- Resource` to cross-check upstream changes. No upstream renames or removals appear in this range.
5. Count raw commands with prefix `[message `, then count messages captured by the builder's `\btext=(.*?)\s+name=` pattern and reconcile category totals. A2 counts describe extracted message commands, including hidden and inner messages. Classify edits by ordered message text and speaker fields, choice/branch commands and non-message staging. The flags are screening metadata. For meaningful changes, the affected reading resolves wording and branch effects against A1.


## Source Lock 1.1 — transcript refresh, 2026-11-12

The [reading partition](../04_CUMULATIVE_LEDGERS_AND_INDICES/GKM_PRIMARY_SOURCE_LOCATOR_LEDGER.md#source-lock-11--transcript-refresh-2026-11-12) accounts for all 172 additions and 6,923 extracted message commands once. The thirteen existing byte revisions are resolved as seven common or technical comparisons, two communication revisions, one support orthography change, two Tsubame staging revisions and one Sena staging revision. The ten path moves have exact before/after locators. Source and semantic verification independently reproduced the per-object hashes and sampled high-impact readings across the change families.

The 19 raw messages omitted from A2 occur in four unchanged objects: `adv_dear_hrnm_012.txt`, `adv_dear_hume_009.txt`, `adv_dear_shro_035.txt` (16), and `adv_live_kcna_001_start-01-01.txt`. These controls identify a baseline extractor limitation. Use A1 for them. All five new A3-unassigned entries are the Kanae horizontal parts, covered by the dedicated reading. The non-UTF-8 music resource remains inventoried as opaque. The new textual scope does not establish an AV match or close any perceptual dependency.
