---
project: DJFW
artifact_type: project_architecture
scope: ongoing_comparative_corpus
generation: V1
status: active_provisional
analysis_root_id: 1j-SJWChEvVtkU9bRqszoocYzXVZxPkjB
source_root_id: 1sr196MHP1yqxMOHQoLZSjnLmAnGc46DL
control_sheet_id: 1fDfRSY9oHovjAcO-YPItDfZlirPjlc3yL8IZQZMRRXg
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
---

# DJFW_PROJECT_ARCHITECTURE.md

## Governing design

DJFW is organized as a comparative research corpus rather than a series corpus. Its architectural unit is the **case**, not an episode, volume, or chapter.

A case may be an individual doujinshi, a fanbook, an all-ages fanwork, a single anthology contribution, a commercial hentai manga volume, a prior-chat metadata-only record, or another derivative fanwork object approved for this comparative project.

## Two-root model

The project uses paired roots:

- Analytical root: methods, case readings, ledgers, baseline briefs, synthesis, audits, and releases.
- Source root: raw fanwork packages, extracted reading copies, page sheets, OCR/translation notes, source metadata, baseline source pointers, and extraction logs.

The analytical root owns interpretation. The source root owns source availability and extraction state.

## Canonical analytical tree

- `DJFW_CURRENT_STATE_AND_CORPUS_MAP.md`
- `DJFW_PROJECT_ARCHITECTURE.md`
- `00 Frameworks and Methods/`
- `01 Project Registry and Source Lock/`
- `02 Case Readings/`
- `03 Character Baselines and Readiness/`
- `04 Comparative Ledgers/`
- `05 Category and Subculture Notes/`
- `06 Synthesis/`
- `07 Evidence and Indexes/`
- `08 Audits and Manifests/`
- `09 Current Release/`
- `90 Legacy and Superseded/`

## Canonical source tree

- `DJFW_SOURCE_ROOT_README.md`
- `00 Source Handling and Policy/`
- `01 Raw Fanwork Uploads/`
- `02 Extracted Reading Copies/`
- `03 Contact Sheets and Page Sheets/`
- `04 OCR Translation and Text Notes/`
- `05 Source Metadata and Bibliography/`
- `06 Baseline Source Pointers/`
- `07 Unavailable or Metadata-Only Cases/`
- `08 Extraction Tools and Logs/`
- `90 Deprecated Source Packages/`

## Sheets versus Markdown

Google Sheets are the operational control plane. They track rows, statuses, IDs, crosswalks, ledgers, vocabulary, and gaps.

Markdown-style documents are the interpretive authority. They explain method, evidence, reasoning, case readings, synthesis, and current state.

## Case ID rule

Every work receives a stable ID before source filing:

`DJFW_CASE_0001`, `DJFW_CASE_0002`, etc.

The ID remains stable even if title, romanization, classification, confidence, or taxonomy placement changes.

## Baseline rule

DJFW should not create duplicate series-level canon corpora. It points to the established series root and creates only lightweight baseline briefs where needed for fanwork comparison.

## Closeout rule

A case is not closed until the case reading, baseline state, source state, control-sheet rows, relevant ledgers, and update manifest agree.
