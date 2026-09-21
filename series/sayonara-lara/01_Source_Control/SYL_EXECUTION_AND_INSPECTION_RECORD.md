---
title: "Sayonara Lara: Execution and Inspection Record"
artifact_id: SYL_EXECUTION_AND_INSPECTION_RECORD
artifact_type: execution_inspection_record
series: Sayonara Lara
generation: V1_JP_AUDITED
version: "1.8"
status: canonical
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
do_not_use_as_literary_evidence: true
created: "2026-09-20"
source_boundary: "Capability and channel coverage for E01-E12 analysis"
---

# Execution and inspection record

## Bootstrap execution profile

```yaml
execution_profile:
  product_surface: Codex desktop
  tool_runtime_location: owner-controlled local Windows runtime
  observation_date: "2026-09-20"
  source_transport: VERIFIED_LOCAL_EVIDENCE_PLANE
  filesystem_read: VERIFIED
  filesystem_write: VERIFIED
  image_inspection: VERIFIED
  audio_decode_and_metadata: VERIFIED
  audio_content_inspection: UNAVAILABLE
  continuous_av_inspection: UNAVAILABLE
  git_write: VERIFIED_LOCAL
  inspection_method: "Complete text reads; original-resolution still-image inspection; ffprobe 8.1.1 metadata/decode-route probe; no native auditory or continuous-video claim"
  probe_receipts:
    - "E01 contact_sheet_001 inspected at original detail"
    - "E01 FLAC probed as 44.1 kHz stereo, 1439.985488 s"
    - "Authority scope SHA-256 and protected activation tag verified"
```

`UNAVAILABLE` means this runtime has no verified route that passes local audio samples or continuous video into the analytical model. It does not mean the source lacks audio. No transcript, waveform, or metadata output will be mislabeled as hearing.

## Coverage matrix

| Episode | Japanese text | English aid | Static visual | Audio transport/decode | Auditory interpretation | Continuous AV | Narrative transaction |
|---|---|---|---|---|---|---|---|
| E01 | COMPLETE: all 323 aligned cues read | COMPLETE AS SECONDARY AID | COMPLETE_FOR_DECLARED_SCOPE: all 43 sheets plus targeted original frames | VERIFIED AVAILABLE | UNAVAILABLE | UNAVAILABLE IN SUPPLIED INPUT | CLOSED: text/static scope |
| E02 | COMPLETE: all 327 aligned cues read | COMPLETE AS SECONDARY AID | COMPLETE_FOR_DECLARED_SCOPE: all 42 sheets plus targeted original frames | VERIFIED AVAILABLE | UNAVAILABLE | UNAVAILABLE IN SUPPLIED INPUT | CLOSED: text/static scope |
| E03 | COMPLETE: all 399 aligned cues read | COMPLETE AS SECONDARY AID | COMPLETE_FOR_DECLARED_SCOPE: all 44 sheets plus targeted original frames | VERIFIED AVAILABLE | UNAVAILABLE | UNAVAILABLE IN SUPPLIED INPUT | CLOSED: text/static scope |
| E04 | COMPLETE: all 416 aligned cues read | COMPLETE AS SECONDARY AID | COMPLETE_FOR_DECLARED_SCOPE: all 36 sheets plus targeted original frames | VERIFIED AVAILABLE | UNAVAILABLE | UNAVAILABLE IN SUPPLIED INPUT | CLOSED: text/static scope + checkpoint |
| E05 | COMPLETE: all 338 aligned cues read | COMPLETE AS SECONDARY AID | COMPLETE_FOR_DECLARED_SCOPE: all 41 sheets plus targeted original frames | VERIFIED AVAILABLE | UNAVAILABLE | UNAVAILABLE IN SUPPLIED INPUT | CLOSED: text/static scope |
| E06 | COMPLETE: all 279 aligned cues read | COMPLETE AS SECONDARY AID | COMPLETE_FOR_DECLARED_SCOPE: all 39 sheets plus targeted original frames | VERIFIED AVAILABLE | UNAVAILABLE | UNAVAILABLE IN SUPPLIED INPUT | CLOSED: text/static scope |
| E07 | COMPLETE: all 323 aligned cues read | COMPLETE AS SECONDARY AID | COMPLETE_FOR_DECLARED_SCOPE: all 39 sheets plus targeted original frames | VERIFIED AVAILABLE | UNAVAILABLE | UNAVAILABLE IN SUPPLIED INPUT | CLOSED: text/static scope |
| E08 | COMPLETE: all 336 aligned cues read | COMPLETE AS SECONDARY AID | COMPLETE_FOR_DECLARED_SCOPE: all 39 sheets plus targeted original frames | VERIFIED AVAILABLE | UNAVAILABLE | UNAVAILABLE IN SUPPLIED INPUT | CLOSED: text/static scope + checkpoint |
| E09-E12 | AVAILABLE / NOT YET INSPECTED | AVAILABLE / SECONDARY | AVAILABLE / NOT YET INSPECTED | VERIFIED AVAILABLE | UNAVAILABLE | UNAVAILABLE IN SUPPLIED INPUT | NOT STARTED |

This table is updated episode by episode. `COMPLETE_FOR_DECLARED_SCOPE` will always name the inspected channel and boundary. Contact-sheet review is static visual coverage, not continuous-video viewing.

## Stage allocation

- Source inventory, episode readings, ledgers, checkpoints, and Git operations: this local Codex run.
- Performance/music/sound-image claims: deferred unless an authorized auditory reviewer or verified native-audio route supplies interval-linked observations.
- Motion/microperformance/editing-rhythm claims: bounded to sampled endpoints unless a later targeted continuous-video route is supplied.
- Major monographs and specialist synthesis: synthesis-readiness phase after E12; Rowan is an explicit planned character target.

## Run log

| Record | Boundary | Operation | Result | Limitations |
|---|---|---|---|---|
| SYL-X0001 | Bootstrap | Verified package hashes, live governance, authority tuple, branch/root absence, E01-E12 bundle inventory, local tool and Git routes | Foundation accepted; sequential gate opened | No episode narrative admitted; auditory and continuous-video routes unavailable |
| SYL-X0002 | E01 | Read all 323 aligned Japanese cues; inspected all 43 contact sheets and selected original-resolution frames; constructed analyst scene map; synchronized six ledgers and evidence debts | E01 narrative transaction closed for declared text/static scope | No auditory interpretation; no continuous video; mirror truth conditions and catastrophe causality remain provisional |
| SYL-X0003 | E02 | Read all 327 aligned Japanese cues; inspected all 42 contact sheets and selected original-resolution frames; constructed analyst scene map; synchronized six ledgers and debts | E02 narrative transaction closed for declared text/static scope | No auditory interpretation or continuous video; Grace's causality and princess-light mechanism remain assertions/provisional correlations |
| SYL-X0004 | E03 | Read all 399 aligned Japanese cues; inspected all 44 contact sheets and selected original-resolution frames; constructed analyst scene map; synchronized six ledgers and debts | E03 narrative transaction closed for declared text/static scope | No auditory interpretation or continuous video; heart/light event is a strong correlation, not a completed true-love identification |
| SYL-X0005 | E04 + checkpoint | Read all 416 aligned Japanese cues; inspected all 36 contact sheets and selected original-resolution frames; constructed analyst scene map; synchronized six ledgers and debts; completed first contradiction/readiness checkpoint | E04 narrative transaction and G2 checkpoint closed for declared text/static scope | No auditory interpretation or continuous video; friendship is explicit, while romance/true-love classification and Lisa's reliability remain open |
| SYL-X0006 | E05 | Read all 338 aligned Japanese cues; inspected all 41 contact sheets and selected original-resolution frames; constructed analyst scene map; synchronized six ledgers and debts | E05 narrative transaction closed for declared text/static scope | No auditory interpretation or continuous video; exact agency, motion, target, and outcome in the Lisa/Kōta/fish-marked-object sequence remain open |
| SYL-X0007 | E06 | Read all 279 aligned Japanese cues; inspected all 39 contact sheets and selected original-resolution frames; constructed analyst scene map; synchronized six ledgers and debts | E06 narrative transaction closed for declared text/static scope | No auditory interpretation or continuous video; bridge/object causality, mirror-surveillance duration, public-tail trigger, and the blond observer's identity and sightline remain open |
| SYL-X0008 | E07 | Read all 323 aligned Japanese cues; inspected all 39 contact sheets and selected original-resolution frames; constructed analyst scene map; synchronized six ledgers and debts | E07 narrative transaction closed for declared text/static scope | No auditory interpretation or continuous video; heart/reversion causality, blade manifestation/mechanics, E05 object linkage, and true-love test remain open |
| SYL-X0009 | E08 + checkpoint | Read all 336 aligned Japanese cues; inspected all 39 contact sheets and selected original-resolution frames including the trophy/certificate coda; constructed analyst scene map, contradiction/readiness checkpoint, six ledger changes, and debts | E08 narrative transaction and second G2 checkpoint closed for declared text/static scope | No auditory interpretation or continuous video; Lisa/Grace light doctrines conflict, potion horizon and final-bout score remain open |
