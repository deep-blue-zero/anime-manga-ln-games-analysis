---
title: "Rent-a-Girlfriend - Cast and reconstruction readiness"
artifact_id: RAG_CAST_AND_RECONSTRUCTION_READINESS
artifact_type: cast_reconstruction_readiness
series: Rent-a-Girlfriend
generation: V1
version: "1.21"
status: canonical
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
created: "2026-09-19"
source_boundary: "Japanese manga witnesses RAG-JP-EPUB-V001-V020; inspected and closed through V020; checkpointed and locally audited through V010 pending the V020 checkpoint transaction."
---

# Cast and reconstruction readiness

## Responsibility

Route verified character identities, aliases, evidence/model homes, observed domains, gaps, and project-local readiness without creating global registry records.

## Record schema

`local_character_key | preferred_name | verified_aliases | first_evidence | evidence_ledger | model | monograph | observed_domains | missing_domains | local_readiness | last_review`

Markdown tables and bounded prose may implement this semantic schema. Unknown values remain unknown; rows cite canonical volume evidence IDs rather than duplicating primary observations.

## Update and routing rule

Update after each eligible volume only when inspected evidence materially affects this responsibility. Preserve stable IDs and historical states. A reviewed domain may record no material change without manufacturing a row. Consequential claims route back to the owning volume reading and forward to the project artifacts named by the series architecture.

## Current coverage

```yaml
initialized: true
inspected_through_volume: V020
row_count: 14
state: CURRENT_THROUGH_V020__CHECKPOINT_PENDING
```

## Project-local cast router

No listed person has been enrolled or graded in the global character registry by this project.

| Local character key | Preferred name / verified aliases | First evidence | Evidence ledger / model / monograph | Observed and missing domains | Local readiness | Last review |
|---|---|---|---|---|---|---|
| RAG-LOCAL-KAZUYA | Kazuya Kinoshita; 木ノ下和也 | RAG-E-V001-001 | `04 Character Analysis/Kazuya Kinoshita/RAG_KAZUYA_EVIDENCE_LEDGER.md`; `RAG_KAZUYA_RECONSTRUCTION_MODEL.md`; no monograph | Observed through V020: public completion of his producer route, differentiated refusal and permission with Ruka, ordinary meal initiative, direct identification of Chizuru as his ideal girlfriend, and an interrupted confession attempt, in addition to prior support and relational evidence. Missing: broad ordinary routine, durable honesty across audiences, fair resolution of the Ruka trial, a completed answer from Chizuru, and acknowledged reciprocal partnership. | OPERATIONAL_CANDIDATE | V020 volume update |
| RAG-LOCAL-CHIZURU | Chizuru Ichinose; rental alias Chizuru Mizuhara / 水原千鶴; campus surname Ichinose / 一ノ瀬 | RAG-E-V001-002 | `04 Character Analysis/Chizuru Ichinose/RAG_CHIZURU_EVIDENCE_LEDGER.md`; `RAG_CHIZURU_RECONSTRUCTION_MODEL.md`; no monograph | Observed through V020: public film reception, self-endorsed vocational continuity, unbooked direct invitation, refund and weakness accounting, relaxed ordinary meal conduct, direct inquiry into Kazuya's feeling, affected hearing of his partial declaration, and later public avoidance. Missing: sustained bereavement course, completed reciprocal romantic discussion, and final shared relationship classification. | OPERATIONAL_CANDIDATE | V020 volume update |
| RAG-LOCAL-MAMI | Mami Nanami; 七海麻美 | RAG-E-V001-001 | none | Observed through V020: breakup and prior investigation routes now culminate in Twitter contact with Kibe, a senior-smartphone app proposal to Nagomi, a request that her past with Kazuya remain private, and promised follow-up. Missing: private motive, ordinary routine, desired endpoint, and whether the business route is genuine, instrumental, or both. | EVIDENCE_LEDGER_ELIGIBLE | V020 volume update |
| RAG-LOCAL-NAGOMI | Nagomi Kinoshita; 和 | RAG-E-V001-003 | none | Observed through V020: family expectations, strong investment in Chizuru, inherited-object transfer, emergency-support reasoning, and receptive evaluation of Mami's senior-smartphone app proposal. Missing: broader history, conduct under corrected relationship information, and knowledge of Mami's past with Kazuya. | EVIDENCE_LEDGER_ELIGIBLE | V020 volume update |
| RAG-LOCAL-SAYURI | Sayuri Ichinose; former screen name Sayuri Otori / 鳳小百合; 一ノ瀬小百合 | RAG-E-V001-006 | none | Observed through V018 as the film's intended recipient who receives projected unfinished footage, regains limited responsiveness, hears Chizuru's non-dating correction, entrusts the answer to her, praises the film, asks that Kazuya be thanked, exchanges final love, and dies before the funeral. Missing: complete factual belief about the couple, exact diagnosis and death mechanism, and broader career history. | EVIDENCE_LEDGER_ELIGIBLE | V018 volume update |
| RAG-LOCAL-MINI | Mini Yaemori; 八重森みに | RAG-E-V013-012 | none | Observed through V020 as a university junior, creator, campaign analyst, forceful romantic intermediary, architect of a two-person trip through false absence information, and the source Chizuru explicitly cites when asking Kazuya whether he likes her. Missing: broader history, long-term reliability, limits on pressure and manipulation, and independent goals beyond creator work and support for Kazuya. | EVIDENCE_LEDGER_ELIGIBLE | V020 volume update |
| RAG-LOCAL-KATSUHITO | Katsuhito Ichinose; 一ノ瀬勝人 | RAG-E-V012-011 | none | Observed: Chizuru's grandfather and supporter, dream-focused encouragement, taxi work, traffic collision, brief return to consciousness, final reassurance, and death. Missing: broader history, ordinary routine, relationships outside the household, and any direct present-day evidence. | EVIDENCE_LEDGER_ELIGIBLE | V012 |
| RAG-LOCAL-KAZUO | Kazuo Kinoshita; 和男 | RAG-E-V001-003 | none | Observed in family/hospital context and in a financially framed confrontation based on a misread money exchange. Missing: broader routine and calibrated conduct under full information. | UNMODELED | V007 |
| RAG-LOCAL-HARUMI | Harumi Kinoshita; 晴美 | RAG-E-V001-003 | none | Observed only in family/hospital context. | UNMODELED | V001 |
| RAG-LOCAL-KIBE | Kibe; 木部; given name not established through V020 | RAG-E-V001-011 | none | Observed through V020 as Kazuya's childhood friend in peer conflict, moral intervention, childhood report, ferry-ticket initiative, rescue interpretation, Twitter contact with Mami, participation in her Nagomi meeting, and accidental interruption of Kazuya's confession. Missing: ordinary independent conduct and calibration under the full relationship history. | EVIDENCE_LEDGER_ELIGIBLE | V020 volume update |
| RAG-LOCAL-KURIBAYASHI | Kuribayashi; 栗林; given name not established through V005 | RAG-E-V001-011 | none | Observed as a university friend and former Ruka client; V005 shows distress, Chizuru's funded date, discovery of the shared rental context, anger, and acceptance of Kazuya's apology. Missing: broader conduct, independent routine, and durable response. | EVIDENCE_LEDGER_ELIGIBLE | V005 |
| RAG-LOCAL-RUKA | Ruka Sarashina; 更科るか | RAG-E-V003-012 | `04 Character Analysis/Ruka Sarashina/RAG_RUKA_EVIDENCE_LEDGER.md`; `RAG_RUKA_RECONSTRUCTION_MODEL.md`; no monograph | Observed through V020: crisis accommodation later becomes a request for attention; Kazuya refuses an overnight trip, accepts a local bath outing, and explicitly permits her requested five-second hug before practical post-bath care. Missing: sustained ordinary routine, exact medical diagnosis, broader relationships, response to a definitive end of the trial, and durable conduct after negotiated limits. | PARTIAL_MODEL | V020 volume update |
| RAG-LOCAL-UMI | Umi; 海くん; surname not established through V015 | RAG-E-V004-011 | none | Observed through V015 as Chizuru's acting colleague with roughly 230,000 followers; he supplies a play invitation and campaign promotion, reveals a recent breakup, invites dinner, and repeatedly asks about Kazuya. Missing: surname, broader history, independent routine, long-term motive, and response after Chizuru's qualified answer. | EVIDENCE_LEDGER_ELIGIBLE | V015 |
| RAG-LOCAL-SUMI | Sumi Sakurasawa; 桜沢墨 | RAG-E-V005-014 | none | Observed through V018 as a first-year university student and rental girlfriend referred by Chizuru for practice; severe communication difficulty coexists with adaptive learning, protective performance, gift guidance, grief sharing, an unheard confession, and now explicit rejection of solitary-strength reasoning plus a self-funded friend excursion that teaches Kazuya play and direct encouragement as support. Missing: fuller history, stable independent provider competence, broad spontaneous speech, and Kazuya's reception of her romantic feeling. | EVIDENCE_LEDGER_ELIGIBLE | V018 volume update |

The cast router records identity and artifact availability only. Character-state history for Kazuya, Chizuru, and Ruka remains in their evidence ledgers; operational rules remain in their models.
