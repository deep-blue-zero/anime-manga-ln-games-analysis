---
title: "IDOLY PRIDE V2 Source Snapshot History"
project: "IDOLY PRIDE"
document_id: "IDOLY_PRIDE_V2_SOURCE_SNAPSHOT_HISTORY"
version: "1.0"
status: "rolling-live-corpus-registry"
created: "2026-08-13"
updated: "2026-08-13"
framework_version: "2.1"
---

# IDOLY PRIDE V2 SOURCE SNAPSHOT HISTORY

## Purpose

This registry tracks source snapshots for a continuing live-service work.

It distinguishes source arrival from analytical release. A new source snapshot does not automatically create a new frozen analytical release.

## Snapshot registry

### IP-V2-SNAPSHOT-2026-08-13-A

Status: `BASELINE / SOURCE-LOCKED`

Game source frontier:

- latest incremental `idoly-corpus` refresh: `2026-08-13T20:13:01+00:00`;
- `idoly-ingest` generated: `2026-08-13T20:24:41+00:00`;
- source story folders: 3,879;
- ingest bundles: 665;
- analysis-bundle validation: PASS.

Anime frontier:

- TV Episodes 01-12 complete;
- exact supplied analysis ZIPs hashed on 2026-08-13;
- total screenshots: 9,052;
- total contact sheets: 458;
- subtitle timing audit: PASS.

4koma frontier:

- source manifest dated 2026-08-09;
- 151 official images represented.

Known gaps:

- 45 telephone references without upstream audio;
- 32 unavailable processed asset references;
- small Episode 1 subtitle-snapshot provenance mismatch;
- minor archive-size differences in several anime ZIPs relative to the older extraction manifest.

Analytical release association:

- none yet; this is the initial working V2 baseline.

Next source snapshot rule:

When a later `idoly-corpus` refresh or newly supplied audiovisual source extends this baseline, assign a new identifier such as:

`IP-V2-SNAPSHOT-YYYY-MM-DD-B`

Then create a delta entry recording added, modified, removed/replaced, and newly available assets and route them by semantic impact.
