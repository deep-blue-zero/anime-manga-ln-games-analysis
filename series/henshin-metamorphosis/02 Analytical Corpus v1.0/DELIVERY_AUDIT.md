---
title: "変身 / Henshin — Definitive Second-Pass Synthesis v1.0 Delivery Audit"
artifact_type: "delivery_audit"
version: "1.0"
release_status: "immutable archival release"
release_date: "2026-08-12"
---

# HENSHIN Definitive Second-Pass Synthesis v1.0 — Delivery Audit

## Release validation summary

| Audit | Result |
|---|---:|
| Canonical substantive analytical artifacts | **26** |
| Substantive analytical word count | **171,063** |
| Specialist Documents 01–08 | **8/8 present** |
| Continuous synthesis | **present — 26,029 words** |
| Prospective chapter/finale/checkpoint artifacts | **9** |
| Final longitudinal ledgers | **7** |
| Japanese source SHA-256 | **MATCH** |
| Japanese source CBZ/ZIP integrity | **PASS — 251/251 image entries** |
| Japanese source redistributed in release | **NO** |
| Markdown UTF-8 readability | **35/35 PASS** |
| Markdown YAML/front matter | **35/35 PASS** |
| JSON parse validation | **2/2 PASS** |
| Exact duplicate prose paragraphs >=600 chars across 26 substantive artifacts | **0** |
| Source/binary payloads accidentally packaged | **0** |
| Superseded phase manifests/audits packaged | **0** |
| Temporary midpoint working ledger packaged | **NO** |
| Final packaged release files | **39** |
| `ARTIFACT_CHECKSUMS.sha256` entries | **38/38 expected** |
| ZIP archive CRC integrity | **PASS** |

## Source lock

The governing Japanese source remains:

```text
Henshin -emergence-.cbz
SHA-256: a1107584fbd3f0fab93b485299af82ed9e1f53a10cb49ffeac55813714e3416e
```

The source archive was re-hashed during Phase 9 and tested as a ZIP/CBZ archive. All 251 WEBP members passed archive integrity testing.

The source CBZ is not contained in the analytical release directory or ZIP.

## Prospective-state preservation

The release preserves all seven canonical sequential readings:

- Chapters 1–6;
- Finale.

It also retains the two frozen interpretive checkpoints:

- midpoint after Chapter 3;
- pre-finale after Chapter 6.

The historical `HENSHIN_MIDPOINT_AUDIT_WORKING_LEDGER.md` is intentionally excluded because it was a mutable production artifact superseded by the frozen midpoint audit and final cross-chapter ledgers.

## Epistemic safeguards verified

- Chapter-local truth remains distinct from retrospective full-work truth.
- Early openness is not rewritten as evidence that later exploitation was inevitable.
- Choice, preference, consent, material capacity, and decision-environment authorship remain distinct analytical variables.
- Chapter 6's recovery branch remains genuinely open at the prospective boundary.
- The Finale may close that branch but does not retroactively falsify Saki's Chapter 6 intention.
- Exact drug identity remains unresolved.
- No unsupported clinical diagnosis is assigned.
- Narrative death remains a high-confidence inference until the separately identified p.243 afterword establishes authorial intended death retrospectively.
- Institutional absence remains distinct from institutional impossibility.
- Structural reader implication remains distinct from deliberate authorial reader indictment.
- Saki's visual transformation is not treated as a moral-purity meter.
- Bodily response is never treated as consent.

## Final interpretive state verified

The v1.0 release preserves the mature classification:

> **『変身』 is an ethically compromised cumulative pornographic tragedy.**

The release also preserves the final visibility model:

> **invisibility → desired visibility → portable visibility → hyper-visibility without causal control → visibility without obligation.**

And the title-level transformation chain:

> `変わりたい`  
> → change for Hayato  
> → `この子のために…変わってみせる`  
> → `生まれ変われた`.

## First-pass revision audit

The definitive claim-revision ledger records:

- **122 strengthened**;
- **16 newly visible in Japanese**;
- **12 complicated**;
- **9 still underdetermined**;
- **0 load-bearing first-pass theses fully overturned**.

The absence of full overturns is not treated as evidence that the first pass was already textually precise. The Japanese pass materially strengthened the evidence resolution around refusal, option contraction, kinship language, obedience, ownership, value, belonging, disposal, future language, and self-blame.

## Cleanup audit

The v1.0 delivery tree excludes superseded production history while leaving the historical mutable workspace untouched.

Excluded from final delivery:

- phase-specific corpus manifests from Phases 2–8;
- phase-specific delivery audits from Phases 2–8;
- temporary midpoint working ledger;
- prior tranche ZIP archives and checksum sidecars;
- extracted source pages/contact sheets;
- source CBZ.

No canonical chapter deep reading, frozen checkpoint, final ledger, specialist document, evidence index, or governing reference was removed.

## Immutability policy

After final checksum generation, all files in the v1.0 release directory are set read-only and directories are set non-writable. The release ZIP is likewise treated as immutable.

Any correction, locator backfill, interpretive revision, or new comparative work that requires changing a v1.0 file should be delivered as a new version such as **v1.1** rather than silently replacing v1.0.

## Checksum policy

`ARTIFACT_CHECKSUMS.sha256` covers every file inside the final release directory except the checksum inventory itself.

The final ZIP receives a separate external `.sha256` sidecar.
