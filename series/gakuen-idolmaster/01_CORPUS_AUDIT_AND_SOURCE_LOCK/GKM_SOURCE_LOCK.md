---
title: "Gakuen Idolmaster V2 Source Lock"
project: "Gakuen Idolmaster / 学園アイドルマスター"
document_type: "source lock and change-control specification"
version: "2.0"
phase: "0 - Corpus Audit and Source Lock"
source_lock: "GAKUMAS V2 Source Lock 1.0"
created: "2026-08-13"
status: "canonical Phase 0 artifact"
---

# GKM SOURCE LOCK

## 0. Formal declaration

The project hereby designates the Google Drive corpus rooted at:

`../../../provenance/drive-artifacts/DRIVE_ARTIFACT_REFERENCE_INDEX.md#drive-ref-fdad681a6d81f903`

as:

> **GAKUMAS V2 SOURCE LOCK 1.0**

for the initial V2 deep-reading and synthesis cycle.

## 1. Locked upstream state

- Repository: `DreamGallery/Campus-adv-txts`
- Commit: `00d150a069a3ffa723a1ff264752ba242024caad`
- Revision file value: `32`
- Archive generated: `2026-08-02T22:21:04Z`
- Raw scripts: **3,777**
- Extracted message lines: **93,924**

These numbers and identifiers define the textual source state. Later Drive upload timestamps do not change the upstream source date.

## 2. What is locked

Source Lock 1.0 includes the contents represented by:

- `00_context/`
- `transcripts_raw/`
- `transcripts_dialogue_only/`
- `analysis_bundles/`

The lock freezes **source identity and provenance**, not interpretation. Analytical documents and ledgers are expected to change as evidence is read.

## 3. Governing authority order

1. **A1 raw Japanese ADV** governs exact wording, ruby, staging metadata, voice/BGM IDs, branch labels, and script commands.
2. **A2 dialogue-only** is a convenience derivative for reading/search.
3. **A3 analysis bundles** are the preferred ingestion layer but can overlap and are never evidence identities by themselves.
4. External official metadata may identify songs/releases/videos but does not override A1 textual evidence.
5. Reliable indexes such as Project-imas are discovery/crosswalk aids.
6. Legacy V1 analysis is interpretation only and sits outside Source Lock 1.0.

## 4. Canonical evidence identity

Default key:

`original_name + sorted_relative_path`

Where collision or ambiguity is found, extend the key using category and/or file checksum. A bundle filename must never be used as the only evidence identifier.

## 5. Immutability policy

During the Source Lock 1.0 analysis cycle:

- do not rename or reorganize locked primary-source files in a way that destroys their manifest provenance;
- do not silently replace raw scripts with revised upstream versions;
- do not change a claim's source locator to a newer file without recording the source-lock delta;
- derived analytical indexes may add aliases, human-readable names, continuity classes, and AV crosswalks without altering the original identity.

## 6. Live-service update policy

Later material is incorporated only by explicit versioning.

Recommended scheme:

- `1.0` - current frozen 2026-08-02 textual corpus;
- `1.1`, `1.2`, ... - bounded additions/corrections that do not require a structural reread;
- `2.0` - substantial new story era, major source rebuild, or changed extraction model.

Every update must record:

- upstream commit/revision/date if available;
- added/removed/changed source identities;
- line/count deltas;
- affected characters, story states, relationships, institutions, and themes;
- which analytical artifacts require revision;
- whether earlier claims remain valid under the old lock.

No document may simply call itself "current" without naming the source lock it analyzes.

## 7. Audiovisual evidence policy

Actual songs, MVs, dialogue videos, and supplied audio/video are governed by a **separate AV evidence registry**:

- `GKM_AUDIOVISUAL_SOURCE_CROSSWALK`
- `GKM_AUDIOVISUAL_VERIFICATION_QUEUE`
- `GKM_SONG_AND_MUSICAL_IDENTITY_LEDGER`
- `GKM_VOICE_PERFORMANCE_STATE_LEDGER`

Script-visible BGM/voice IDs are inside Source Lock 1.0. The rendered sound/video itself is not, unless later explicitly incorporated into a multimedia source-lock revision.

## 8. Branch and continuity lock rules

A locked source being authentic does not make every source mutually sequential.

The project therefore locks the following rule:

> **Source authenticity and continuity compatibility are separate questions.**

Failure/normal/true-labeled/choice-dependent/result variants remain valid sources but must receive continuity classification. `true` in a filename is described as a **true-labeled branch/state** unless stronger evidence establishes unique canonical status.

## 9. Control-file checksums

The following SHA-256 values were calculated from locally materialized Phase 0 audit/control copies on 2026-08-13. They fingerprint the audit inputs used to produce this Phase 0 package; they are **not** a checksum manifest of all 3,777 raw scripts.

| audit/control file | SHA-256 |
| --- | --- |
| manifest.csv | 82ed6510a74bfa278591ddcaefa35f771423228eb62c5e03d820d4f4362196b1 |
| category_counts.json | 41838e3b05d3fc348735d073a132e3e77a8b7c5c02f21cd33955cf382040d878 |
| bundle_coverage_by_character.tsv | 42feead6676aee0a822f5799ea73a1419f5206b5b9f48c80cf2bb762416b7bc9 |
| bundle_coverage_by_category.tsv | e895148a8846050355b8deee55ddf4da8977227b64e8d5cd43ed4aeff381bd06 |
| ambiguous_or_unassigned_files.tsv | 009f36d1071bdd60db77032d01b2def8013f6cbc2e0f2430c814877a7bad39b8 |
| missing_dialogue_files.tsv | 129117858f6449cc54dcf63ada26750032e460cc47f3cc38494ed4124ebb1490 |
| 00_shared_manifest.json | 8df0ddcb18436c1dd93c9476114c8fc1905cb5559e86f0f3b4e784d8838becb1 |
| 00_story_event_manifest.json | 450dda7ce5917f77a6f75e9a3bd34a022ab3bf0a24d6c33f19dac981c610fc93 |

## 10. Source Lock 1.0 acceptance conditions

Source Lock 1.0 is accepted for Phase 1 because:

- category totals reconcile to 3,777 / 93,924;
- bundle coverage reports reconcile by category;
- 13 complete character bundles are present;
- shared, unit, event, and support layers are separately represented;
- all no-dialogue-extract report rows are zero-message files;
- every dialogue-bearing unassigned file has been enumerated and adjudicated;
- a canonical deduplication rule is defined;
- known bundle-view overlap has been tested directly against bundle manifests;
- V1 analysis has been segregated from primary evidence.

## 11. Lock status

**Status: ACCEPTED - GAKUMAS V2 SOURCE LOCK 1.0**

Phase 1 may rely on this lock without re-litigating basic corpus identity. If a later source contradiction appears, it should be logged as a source-lock issue, not silently repaired.
