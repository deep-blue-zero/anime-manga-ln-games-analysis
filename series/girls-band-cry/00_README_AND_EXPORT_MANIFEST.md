---
series: GBC
artifact_type: corpus_map
scope: E01-E13
generation: V1
status: historical_legacy
source_boundary: "Manga and anime discussions - Girls Band Cry Analysis - Full Transcript(2).md"
supersedes: null
superseded_by: null
do_not_use_as_current_authority: true
---

# Girls Band Cry — V1 Episode Deep-Reading Archive

## Purpose

This archive preserves the original episode-by-episode analytical responses from the V1 *Girls Band Cry* conversation as **verbatim transcript extracts** rather than reconstructed summaries.

The source export is:

`Manga and anime discussions - Girls Band Cry Analysis - Full Transcript(2).md`

The episode files preserve the original assistant response text exactly. Added YAML front matter and archival section labels sit outside that verbatim text so the files remain machine-routable without silently rewriting the historical analysis.

## Authority state

All files remain `historical_legacy` and `do_not_use_as_current_authority: true`.

They are provenance and V2 revision targets, not current V2 authority.

## Episode 13 gap

The export contains the user's request for the final Episode 13 deep dive at Turn 43, but **no corresponding assistant deep-dive turn is present**. The export header also reports `bottom_reached: false`.

Accordingly, `GBC_E13_DEEP_READING.md` no longer reconstructs a missing main response from the later synthesis. Instead it records the gap explicitly and preserves the later **Assistant Turn 48 ED/epilogue analysis verbatim**.

This is intentionally different from the prior reconstructed E13 file.

## Supplemental episode material

Where the V1 conversation contained later episode-specific analytical follow-ups, they are appended verbatim to the relevant episode file under archival source labels. These include:

- E01 — requested performance clips and Momoka/Nina 「空の箱」 comparison;
- E08 — requested confrontation clips, 「空の箱」 confession-scene refinement, and yuri/fansub interpretation;
- E11 — full performance clip refinement plus later Tomo-family/visual-sequence analysis;
- E13 — ED/epilogue analysis only, because the original main deep dive is absent from this export.

## Manifest

| Episode | Verbatim source turns | Approx. extracted words | File | Status |
|---:|---|---:|---|---|
| 01 | Turn 8 + Turn 12 | 5,996 | `GBC_E01_DEEP_READING.md` | Verbatim transcript extraction |
| 02 | Turn 14 | 6,155 | `GBC_E02_DEEP_READING.md` | Verbatim transcript extraction |
| 03 | Turn 16 | 7,295 | `GBC_E03_DEEP_READING.md` | Verbatim transcript extraction |
| 04 | Turn 18 | 7,171 | `GBC_E04_DEEP_READING.md` | Verbatim transcript extraction |
| 05 | Turn 20 | 8,994 | `GBC_E05_DEEP_READING.md` | Verbatim transcript extraction |
| 06 | Turn 22 | 8,019 | `GBC_E06_DEEP_READING.md` | Verbatim transcript extraction |
| 07 | Turn 24 | 9,888 | `GBC_E07_DEEP_READING.md` | Verbatim transcript extraction |
| 08 | Turn 26 + Turn 28, Turn 30, Turn 32 | 13,194 | `GBC_E08_DEEP_READING.md` | Verbatim transcript extraction |
| 09 | Turn 34 | 7,975 | `GBC_E09_DEEP_READING.md` | Verbatim transcript extraction |
| 10 | Turn 36 | 8,945 | `GBC_E10_DEEP_READING.md` | Verbatim transcript extraction |
| 11 | Turn 38 + Turn 40, Turn 56, Turn 58, Turn 60 | 12,787 | `GBC_E11_DEEP_READING.md` | Verbatim transcript extraction |
| 12 | Turn 42 | 8,275 | `GBC_E12_DEEP_READING.md` | Verbatim transcript extraction |
| 13 | Turn 48 (supplement only) | 3,954 | `GBC_E13_DEEP_READING.md` | Original main deep-dive absent from this export; Turn 48 ED/epilogue preserved verbatim |

## Recommended V2 use

Treat the V1 files as hypotheses to audit, not conclusions to inherit automatically.

Major claims should transition through:

**PRESERVE / STRENGTHEN / REVISE / DOWNGRADE / REJECT / OPEN**

Preferred future route:

**V2 synthesis → V2 specialist artifact → V2 episode reading → timestamped Japanese subtitle / frame / audio / clip evidence → primary source bundle**

## Provenance caution

The transcript export itself carries two validation cautions:

- `first_message_confirmed: false`
- `bottom_reached: false`

E01-E12 assistant deep-dive turns are present in full in the supplied export and are preserved here verbatim. No claim is made that material missing from the export never existed in the original conversation.
