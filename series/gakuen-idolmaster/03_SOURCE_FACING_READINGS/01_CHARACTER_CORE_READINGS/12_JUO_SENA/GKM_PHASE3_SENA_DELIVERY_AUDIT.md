---
series: GKM
artifact_type: audit
scope: CHARACTER_JUO_SENA_PHASE3_DELIVERY
character: "Juo Sena / 十王星南"
generation: V2
status: canonical
source_boundary: "Phase-3 textual character-core delivery audit; AV request is separate active-provisional infrastructure"
supersedes: null
superseded_by: null
do_not_use_as_current_authority: false
last_updated: "2026-08-16"
---

# GKM PHASE 3 — SENA DELIVERY AUDIT

## Result

**PASS.** The Sena Phase-3 textual core reconciles to **184 unique source objects / 4,515 dialogue messages** under GAKUMAS V2 Source Lock 1.0.

## Delivered canonical core artifacts

| artifact | bytes | whitespace words |
|---|---:|---:|
| `GKM_CORE_12_JUO_SENA.md` | 59,127 | 8,800 |
| `GKM_CORE_12_JUO_SENA_EVIDENCE_MATRIX.md` | 16,604 | 2,495 |
| `GKM_PHASE3_SENA_CORE_PASS_REPORT.md` | 8,260 | 1,140 |
| `GKM_PHASE3_SENA_SOURCE_METRICS.json` | 4,748 | 417 |

The separate `GKM_SENA_AUDIOVISUAL_BASELINE_AND_REQUESTS.md` is **active_provisional** and intentionally excluded from the immutable textual-core ZIP because audiovisual acquisition and inspection remain open.

## Source reconciliation

| family | objects | messages |
|---|---:|---:|
| Produce Story | 42 | 719 |
| Produce Events | 81 | 1,000 |
| Idol Communications | 21 | 876 |
| Dear Idol | 27 | 1,880 |
| Live | 8 | 16 |
| Growth | 3 | 12 |
| Startup/seasonal | 2 | 12 |
| **TOTAL** | **184** | **4,515** |

Produce Story control: **31 Series-1 / 11 Series-2 objects**. No Series-3 Produce Story source is present, and none has been invented.

## A1 verification

Eight high-load Dear scenes were checked against their raw ADV scripts:

- Dear 001 — retirement / `凡人` / first-person dream;
- Dear 005 — perfect image / avoidance of stronger idols;
- Dear 009 — exhibition / top-idol declaration / fanhood;
- Dear 016 — successor-to-rival revision;
- Dear 018 — Kotone's fan history / reciprocal star;
- Dear 020 — parameters as only a fraction of idol power;
- Dear 025 — Saki as other self / H.I.F. reform problem;
- Dear 027 — summer Prima Stella / institutional restructuring / world-scale reopening.

The dialogue-only bundle remains the reading layer; raw ADV governs exact text and staging disputes.

## Evidence-boundary checks

- Legacy full-chat analysis is used only for `PRESERVE / STRENGTHEN / REVISE / DOWNGRADE / REJECT / OPEN` claim routing.
- P1 and P2 result branches remain separate; the true-labeled P1 possession/history endpoint is not universalized.
- Dear 001–027 is labeled `D-SENA`, not silently merged with hypothetical Series-3 material.
- CIDOL scripts are treated as textual performance-intention evidence, not proof of timbre, choreography, animation, camera or MV execution.
- Official music metadata is used only to normalize title/performer/release identity and acquisition status.
- Current/future release dates are explicitly versioned as of 2026-08-16.
- Recipient-side ethical judgments about Kotone, Ume, China, Misuzu, Tsubame and Shion remain open to later source correction.

## Structural validation

- UTF-8 decoding: **5/5 current delivery/support artifacts passed**.
- YAML front matter: **4/4 Markdown artifacts passed**.
- Source metrics JSON: **valid**.
- Required main-document sections: **all present**.
- Evidence/falsification claims: **56**.
- Exact normalized cross-document prose paragraphs >=600 characters duplicated across substantive artifacts: **0**.

## Authority check

- `GKM_CORE_12_JUO_SENA.md` — **canonical Phase-3 source-facing core**.
- `GKM_CORE_12_JUO_SENA_EVIDENCE_MATRIX.md` — **canonical subordinate evidence/falsification matrix**.
- `GKM_PHASE3_SENA_CORE_PASS_REPORT.md` — **canonical completion checkpoint**.
- `GKM_PHASE3_SENA_SOURCE_METRICS.json` — machine-readable source accounting.
- `GKM_SENA_AUDIOVISUAL_BASELINE_AND_REQUESTS.md` — **active_provisional**, pending AV evidence.

## Packaging policy

The ZIP contains analytical artifacts only. It does **not** redistribute the Source Lock transcript bundle, raw game scripts, legacy transcript, audio, video, images or other primary-source payloads.
