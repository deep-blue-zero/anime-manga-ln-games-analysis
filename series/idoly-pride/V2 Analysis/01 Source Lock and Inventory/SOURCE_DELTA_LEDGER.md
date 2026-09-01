---
series: IDOLY_PRIDE
artifact_type: source_delta_ledger
artifact_role: LEDGER
scope: LIVE_CORPUS_SOURCE_DELTAS
generation: V2
version: "1.0"
status: canonical
phase: "2"
baseline_snapshot_id: IP-V2-SNAPSHOT-2026-08-13-A
current_admitted_snapshot_id: IP-V2-SNAPSHOT-2026-08-13-A
source_boundary: "Initialized at P2-0 against the frozen Phase-1 source snapshot. No later source snapshot is admitted at creation."
supersedes: null
superseded_by: null
do_not_use_as_current_authority: false
integrity_status: INITIALIZED_NO_POST_BASELINE_DELTA
created: "2026-08-16"
updated: "2026-08-16"
next_delta_id: IP-DELTA-YYYYMMDD-001
---

# IDOLY PRIDE V2 — SOURCE DELTA LEDGER

## 0. Current state

Baseline and current admitted snapshot:

> **`IP-V2-SNAPSHOT-2026-08-13-A`**

Initialization result:

> **NO LATER SOURCE SNAPSHOT ADMITTED**

This rolling ledger records future changes between audited extraction snapshots. It is not a list of every source already present in the frozen Phase-1 corpus.

---

## 1. Delta schema

```yaml
delta_id:
source_id:
previous_snapshot:
current_snapshot:
change_type:  # added | modified | removed | replaced | asset-added | upstream-correction
characters:
units:
relationships:
initial_priority:
impact_class:  # CLASS-1 ADDITIVE-TEXTURE | CLASS-2 SIGNIFICANT-DEVELOPMENT | CLASS-3 ARCHITECTURAL
affected_claims:
affected_documents:
requires_reanalysis:
status:
notes:
```

Impact is determined by what the source changes, not whether it is a main story, event, card, message, telephone, 4koma, or formal asset.

---

## 2. Current delta entries

```yaml
delta_entries: []
```

There is no unadmitted post-IP-V2-SNAPSHOT-2026-08-13-A source material in the analytical authority chain at P2-0 initialization.

---

## 3. Change-type rules

- `added` — genuinely new source/story/content entity.
- `modified` — same source identity, changed source contents.
- `removed` — source disappears without a designated replacement.
- `replaced` — source is superseded by a provider-designated successor/version.
- `asset-added` — previously absent formal/audio/visual asset becomes available.
- `upstream-correction` — extraction/provider metadata or text is corrected without being new narrative content.

Do not treat a reupload, Drive copy, connector retry, filename-only change, or analytical reclassification as a source delta.

---

## 4. Impact routing

### CLASS-1 ADDITIVE-TEXTURE

Default route: relevant ledger(s). Polished synthesis changes only if accumulation becomes meaningful.

### CLASS-2 SIGNIFICANT-DEVELOPMENT

Route: affected character/relationship/unit/theme ledgers + `PENDING_REANALYSIS_QUEUE.md` for downstream specialist synthesis re-audit.

### CLASS-3 ARCHITECTURAL

Route: broad claim audit, affected specialist artifacts, governing architecture if necessary, and continuous full-series synthesis when that phase exists.

A small message may be Class 2/3 if it resolves or overturns a major ambiguity.

---

## 5. Snapshot admission gate

A future source snapshot may not become current merely because its files appear in Drive.

Before admission:

1. compare against the last audited manifest;
2. write delta entries;
3. classify impact;
4. route affected entities/claims;
5. identify any pending Class-2/3 work;
6. update `SOURCE_SNAPSHOT_HISTORY.md`;
7. only then update the current-state map and affected `validated_through` frontiers.

Frozen Phase-1 artifacts remain valid for the snapshot they claim even after later snapshots exist.
