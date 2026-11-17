---
title: "Rent-a-Girlfriend - Character Analysis Promotion Audit at V020"
artifact_id: RAG_CHARACTER_ANALYSIS_PROMOTION_AUDIT_V020
artifact_type: character_analysis_promotion_audit
series: Rent-a-Girlfriend
generation: V1
version: "1.0"
status: canonical
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
created: "2026-09-20"
source_boundary: "Japanese manga witnesses RAG-JP-EPUB-V001-V020; promotion decisions use the closed V020 checkpoint and admit no V021 narrative evidence."
---

# Character analysis promotion audit at V020

## Audit identity and freeze

~~~yaml
audit_id: RAG_CHARACTER_ANALYSIS_PROMOTION_AUDIT_V020
audit_kind: POST_CHECKPOINT_CHARACTER_HOME_AND_MODEL_PROMOTION
frozen_series_branch: series/rent-a-girlfriend
basis_commit: 940f1b3050e41ff0fac8a79fcdbb8260b0f0ca06
basis_checkpoint: RAG_CP_V020
basis_reconstruction_audit: RAG_RECONSTRUCTION_AUDIT_V020
admitted_volume_range: V001-V020
latest_admitted_volume: V020
later_narrative_exposure: EXCLUDED
cast_rows_reviewed: 14
prior_character_homes: 3
resulting_character_homes: 12
new_evidence_ledgers: 9
prior_reconstruction_models: 3
resulting_reconstruction_models: 6
new_reconstruction_models: 3
new_monographs: 0
global_registry_write: NOT_PERFORMED
global_capability_assessment: NOT_PERFORMED
numeric_accuracy_score: NOT_PRODUCED
architecture_amendment: NOT_REQUIRED
~~~

This audit repairs the gap between the cumulative cast router and the character-analysis tree after V020. It uses only the already closed V001-V020 readings, current cumulative ledgers, `RAG_CP_V020`, `RAG_RECONSTRUCTION_AUDIT_V020`, and the existing Kazuya, Chizuru, and Ruka character homes. It does not reopen volume transactions, inspect V021, create global character records, or infer new primary observations.

## Decision standard

An evidence ledger is warranted when a person has a recurring, evidence-supported analytical responsibility that can no longer be retrieved responsibly from a short router row. The ledger may remain `UNMODELED`; artifact existence does not imply behavioral generalization.

A reconstruction model is warranted only when the admitted evidence supports materially distinct time-indexed states, a repeated response mechanism across more than one context, explicit relationship and knowledge conditions, counterevidence, and meaningful abstention. A model promoted here begins at `PARTIAL_MODEL`. No new character has enough tested ordinary-life breadth or validation to begin at `OPERATIONAL_CANDIDATE`.

A monograph requires an independent integrated argument, competing interpretations, literary function, and reconciled source routes. This audit creates no monographs. The task is longitudinal evidence ownership and bounded operational modeling, not retrospective character essay production.

## Complete cast-row disposition

| Character | Prior router state | V020 row audit | Artifact action | Resulting readiness | Decision |
|---|---|---|---|---|---|
| Kazuya Kinoshita | OPERATIONAL_CANDIDATE | Existing ledger/model and V020 reconstruction audit remain current. | Preserve both files byte-for-byte; no monograph. | OPERATIONAL_CANDIDATE | Existing model already owns the evidence and retains its V020-tested envelope. |
| Chizuru Ichinose | OPERATIONAL_CANDIDATE | Existing ledger/model and V020 reconstruction audit remain current. | Preserve both files byte-for-byte; no monograph. | OPERATIONAL_CANDIDATE | Existing model already owns the evidence and retains its V020-tested envelope. |
| Mami Nanami | EVIDENCE_LEDGER_ELIGIBLE | Repeated contradiction testing, research, audience-sensitive presentation, and access-building recur from V001 through V020. | Create evidence ledger and bounded model; no monograph. | PARTIAL_MODEL | Method generalizes better than motive; endpoint and ordinary life remain unknown. |
| Nagomi Kinoshita | EVIDENCE_LEDGER_ELIGIBLE | Family expectation, chosen-kin inclusion, heirloom support, funeral routing, and the V020 proposal require a dedicated trace. | Create evidence ledger; withhold model and monograph. | UNMODELED | Nearly all decisions remain conditioned by one uncorrected couple premise; response under truth is absent. |
| Sayuri Ichinose | EVIDENCE_LEDGER_ELIGIBLE | Family interpretation, screen history, film consent, terminal truth conflict, and posthumous influence require a dedicated historical trace. | Create evidence ledger; withhold model and monograph. | UNMODELED | Evidence is rich but terminal, family-concentrated, partly retrospective, and unable to support prospective validation. |
| Mini Yaemori | EVIDENCE_LEDGER_ELIGIBLE | Campaign coordination and relationship intervention recur across project, logistics, and confidant contexts. | Create evidence ledger and bounded model; no monograph. | PARTIAL_MODEL | Coordination and intervention form repeat; calibration, privacy, and independent goals remain sparse. |
| Katsuhito Ichinose | EVIDENCE_LEDGER_ELIGIBLE | Flashback support, taxi work, terminal reassurance, and continued family influence warrant historical ownership. | Create evidence ledger; withhold model and monograph. | UNMODELED | The sample is retrospective, narrow, terminal, and dominated by survivor memory. |
| Kazuo Kinoshita | UNMODELED | Re-audited through V020; only limited family and misread-money confrontation evidence is available. | No separate home; no model or monograph. | UNMODELED | Evidence density and domain breadth remain below the character-home threshold. |
| Harumi Kinoshita | UNMODELED | Re-audited through V020; evidence remains limited to family/hospital context. | No separate home; no model or monograph. | UNMODELED | Evidence density remains below the character-home threshold. |
| Kibe | EVIDENCE_LEDGER_ELIGIBLE | Childhood testimony, forceful intervention, selective secrecy, and the V020 intermediary route require a dedicated trace. | Create evidence ledger; withhold model and monograph. | UNMODELED | Conduct is intermittent, high-stakes, and repeatedly conditioned by incomplete relationship information. |
| Kuribayashi | EVIDENCE_LEDGER_ELIGIBLE | Rental-client injury and vulnerable friendship repair require a dedicated trace, with V020 peer contact as a later boundary. | Create evidence ledger; withhold model and monograph. | UNMODELED | The sample is concentrated in one V003-V005 disclosure/repair cluster and lacks longitudinal breadth. |
| Ruka Sarashina | PARTIAL_MODEL | Existing ledger/model and V020 reconstruction audit remain current. | Preserve both files byte-for-byte; no monograph. | PARTIAL_MODEL | One improved request-and-permission case does not erase earlier boundary failures or fill ordinary-life gaps. |
| Umi | EVIDENCE_LEDGER_ELIGIBLE | Acting-colleague access, promotion, breakup disclosure, invitation, and Kazuya question require a bounded trace. | Create evidence ledger; withhold model and monograph. | UNMODELED | One professional/romantic-probe route is insufficient; surname, independent routine, and response remain unknown. |
| Sumi Sakurasawa | EVIDENCE_LEDGER_ELIGIBLE | Adaptive communication, training persistence, planned care, grief listening, hospital support, and friend-framed teaching recur across distinct contexts. | Create evidence ledger and bounded model; no monograph. | PARTIAL_MODEL | Support methods repeat, but independent goals, broad spontaneous competence, conflict, and later conduct remain sparse. |

The resulting readiness distribution is two `OPERATIONAL_CANDIDATE`, four `PARTIAL_MODEL`, and eight `UNMODELED` rows. `UNMODELED` now has two distinct retrieval situations: six characters have dedicated evidence ledgers but no model, while Kazuo and Harumi remain router-only because the evidence does not yet justify an independent home.

## New artifact manifest

| Character | Evidence ledger | Reconstruction model |
|---|---|---|
| Mami Nanami | `04 Character Analysis/Mami Nanami/RAG_MAMI_EVIDENCE_LEDGER.md` | `04 Character Analysis/Mami Nanami/RAG_MAMI_RECONSTRUCTION_MODEL.md` |
| Nagomi Kinoshita | `04 Character Analysis/Nagomi Kinoshita/RAG_NAGOMI_EVIDENCE_LEDGER.md` | Withheld |
| Sayuri Ichinose | `04 Character Analysis/Sayuri Ichinose/RAG_SAYURI_EVIDENCE_LEDGER.md` | Withheld |
| Mini Yaemori | `04 Character Analysis/Mini Yaemori/RAG_MINI_EVIDENCE_LEDGER.md` | `04 Character Analysis/Mini Yaemori/RAG_MINI_RECONSTRUCTION_MODEL.md` |
| Katsuhito Ichinose | `04 Character Analysis/Katsuhito Ichinose/RAG_KATSUHITO_EVIDENCE_LEDGER.md` | Withheld |
| Kibe | `04 Character Analysis/Kibe/RAG_KIBE_EVIDENCE_LEDGER.md` | Withheld |
| Kuribayashi | `04 Character Analysis/Kuribayashi/RAG_KURIBAYASHI_EVIDENCE_LEDGER.md` | Withheld |
| Umi | `04 Character Analysis/Umi/RAG_UMI_EVIDENCE_LEDGER.md` | Withheld |
| Sumi Sakurasawa | `04 Character Analysis/Sumi Sakurasawa/RAG_SUMI_EVIDENCE_LEDGER.md` | `04 Character Analysis/Sumi Sakurasawa/RAG_SUMI_RECONSTRUCTION_MODEL.md` |

## New evidence-ledger promotions

### Mami Nanami

The new ledger separates five states: former-partner re-entry, active relationship disruption, platform investigation, contradiction integration with a dormant family route, and V020 family access under a professional account. Its central limitation is motive. Research, questioning, selective presentation, and access-building are observable; reunion, punishment, protection, business interest, and control remain unresolved alternatives.

### Nagomi Kinoshita

The new ledger makes the false couple premise explicit in every family judgment it conditions. It preserves daughter-like inclusion, the engagement-ring transfer and pawn authorization, funeral support routing, and the V020 Mami meeting without converting care into calibrated knowledge. A model is withheld until Nagomi is tested under corrected facts and outside the couple-centered family role.

### Sayuri Ichinose

The new ledger distinguishes general acceptance of human lying from knowledge of the specific rental deception. It routes screen history, family interpretation, campaign-story consent, terminal film reception, partial correction, final love, and posthumous influence. Later memories are labeled as survivor evidence rather than new Sayuri conduct.

### Mini Yaemori

The new ledger distinguishes measurable project competence from weaker romantic authorization. Campaign analytics, team coordination, unauthorized disclosure, deceptive trip engineering, admission under questioning, confidant access, and the continuing causal effect of her disclosure all remain visible together.

### Katsuhito Ichinose

The new ledger provides a historical home for encouragement, taxi work, collision, terminal reassurance, Sayuri-directed support, and later family memory. Direct flashback conduct and posthumous influence remain separate.

### Kibe

The new ledger preserves both the care and the error in Kibe's interventions. Childhood knowledge and practical support coexist with violence and relationship judgments made under false information. The V020 Mami–Nagomi introduction is recorded as an intermediary action without assigning him Mami's motive or the interrupted confession's missing content.

### Kuribayashi

The new ledger owns the concentrated rental-client injury and repair sequence. It records that Kazuya's costly self-disclosure, rather than a simple correction, makes local repair possible. The long evidence gap prevents a durable forgiveness or friendship rule.

### Umi

The new ledger distinguishes Kazuya's jealous observation from Umi's direct conduct. It records acting-colleague access, audience reach, recent breakup, dinner invitation, relationship question, campaign promotion, and Chizuru's later recall without inferring a stable motive.

### Sumi Sakurasawa

The new ledger treats alternate-channel communication as agency and preserves the role of preparation and the other person's accommodation. It tracks practice, gift guidance, itinerary design, bounded inquiry, shared grief, hospital visiting, and the explicit paid-to-friend transition in V018. The unheard confession remains outside Kazuya's knowledge.

## New bounded model promotions

### Mami Nanami — `PARTIAL_MODEL`

Accepted envelope:

- specific contradictions in a relationship account can prompt targeted questioning;
- public data or service routes can become institution-mediated access;
- presentation changes with audience while sincerity and motive remain unresolved;
- former-partner access can be pursued without a stated final relational claim;
- dormant information may be reactivated through a lower-friction intermediary route.

Withheld envelope: final motive, family history, sustained business competence, response to full truth, response to firm exclusion, and any assumption that the V020 service is either purely genuine or purely instrumental. The V011-V019 absence remains a model gap rather than inferred planning time.

### Mini Yaemori — `PARTIAL_MODEL`

Accepted envelope:

- measurable shared problems can activate volunteered expertise and coordination;
- perceived mutual interest plus inertia can prompt direct intervention;
- separate access to both principals can produce mediation filtered through Mini's own theory;
- self-privacy can be defended while other people's access boundaries are treated as negotiable;
- the chosen supporter relation can become visible in peer settings.

Withheld envelope: privileged knowledge of the romance, broad creator success, confidentiality under a firm stop request, independent life goals, and post-V020 relationship results. Helpful campaign work does not authorize her disclosures or Ruka-directed deception.

### Sumi Sakurasawa — `PARTIAL_MODEL`

Accepted envelope:

- high speech load can prompt writing, gesture, phone, objects, activity, or bounded touch rather than simple withdrawal;
- known needs and preparation time can produce a concrete care itinerary;
- partial distress disclosure can receive co-presence before solution;
- a structured role can support limited protective performance;
- difficult performance can lead to practice and preparation;
- an explicit frame change can preserve support while limiting transactional ambiguity.

Withheld envelope: diagnosis, broad spontaneous provider competence, independent work management, family life, direct romantic rejection, conflict outside support settings, and post-V018 behavior. Most strong cases involve Kazuya, so relationship breadth remains a central limitation.

## Deliberate model nonpromotions

| Character | Strongest modeled-looking material | Why it remains evidence only | Evidence that would change the decision |
|---|---|---|---|
| Nagomi | Repeated family inclusion and material care | One false couple premise governs nearly every high-value choice; independent routine and truth-conditioned response are absent. | Conduct after full correction, plus repeated decisions in family/business contexts not organized by the apparent couple. |
| Sayuri | Repeated family interpretation, artistic support, and terminal agency | The sample is terminal and retrospectively selected; her exact knowledge remains incomplete and prospective checks are impossible. | Substantial canonical flashback coverage across ordinary, professional, and conflicting relationships. |
| Katsuhito | Consistent dream support and final reassurance | Very small retrospective sample, one family relation, and no prospective validation path. | Broad contemporaneous flashbacks showing ordinary work, disagreement, and relationships outside Chizuru. |
| Kibe | Direct moral intervention and practical opportunity creation | Intermittent high-stakes acts rely on false or partial information; ordinary independent conduct is sparse. | Repeated choices after receiving the full relationship history and evidence from another relationship domain. |
| Kuribayashi | Anger followed by repair after reciprocal vulnerability | One concentrated injury/repair cluster with a long later gap cannot support a general rule. | Later conduct testing trust, conflict, and friendship durability in ordinary settings. |
| Umi | Professional help combined with personal questioning | One acting-colleague and romantic-probe route; motive, surname, routine, and response are missing. | Repeated independent work and relationship decisions, including his response to Chizuru's qualified answer. |

Kazuo and Harumi are deliberate **home nonpromotions** as well as model nonpromotions. Their router rows remain necessary for identity retrieval, but separate files would only restate sparse family observations.

## Existing central-home preservation

The Kazuya, Chizuru, and Ruka artifacts were structural examples and current analytical authorities, not rewrite targets. Their pre-change SHA-256 identities are the preservation requirements for this change:

| Path | Required SHA-256 |
|---|---|
| `04 Character Analysis/Kazuya Kinoshita/RAG_KAZUYA_EVIDENCE_LEDGER.md` | `7092b00721063112cd60bd12cade961294793ed9ad6e695c1909d0c5de640929` |
| `04 Character Analysis/Kazuya Kinoshita/RAG_KAZUYA_RECONSTRUCTION_MODEL.md` | `97a4497720403cb3209425da313c8b70b3a7af8bcfdc32c97f578fa2a5730ee3` |
| `04 Character Analysis/Chizuru Ichinose/RAG_CHIZURU_EVIDENCE_LEDGER.md` | `1fe767fcd1da4cddec0a23d473896e16bdfcfd3890085f8e231800558216646d` |
| `04 Character Analysis/Chizuru Ichinose/RAG_CHIZURU_RECONSTRUCTION_MODEL.md` | `8d23a31b9d5ea28967340aaeb14395709ef509d05eae402d050f304a0790cf7f` |
| `04 Character Analysis/Ruka Sarashina/RAG_RUKA_EVIDENCE_LEDGER.md` | `8e63d5d0bb738a1fb775bbaf9d3bd9819367c3ea3a05544e3f3ba6127fa890c4` |
| `04 Character Analysis/Ruka Sarashina/RAG_RUKA_RECONSTRUCTION_MODEL.md` | `d2ffcbae9f28ae8eb72e8713dedad268eb06255fb267364f210fb3d035c98830` |

Their readiness remains Kazuya `OPERATIONAL_CANDIDATE`, Chizuru `OPERATIONAL_CANDIDATE`, and Ruka `PARTIAL_MODEL` under `RAG_RECONSTRUCTION_AUDIT_V020`.

## Architecture, registry, and routing disposition

No architecture amendment is required. `RAG_SERIES_ARCHITECTURE.md` already assigns independent homes to recurring characters with evidence-supported responsibilities, allows models before monographs, and withholds artifacts when a separate responsibility is not yet real. This change instantiates that existing design.

The project-local cast router is the only character registry changed. No global `characters/` registry, capability file, global index, or housekeeping-owned derived route is edited. The series registry descriptor is repaired only at its local `catalog_note` so it truthfully records V001-V020 as closed, checkpointed, and audited and identifies V021 as the next candidate requiring new authorization.

The current-state map gains routes to this audit and to the expanded character-analysis inventory. The sequential state remains complete through V020, `sequential_analysis_lock` remains `OPEN` as required for this cumulative branch, and V021 remains narratively inadmissible.

## Validation and release acceptance

Acceptance requires all of the following:

- all fourteen cast rows reviewed and reconciled with actual artifact availability;
- nine new evidence ledgers and exactly three new models present at the declared paths;
- no monograph, global registry, global capability, or later-volume narrative artifact created;
- all evidence references resolve within V001-V020;
- the six preserved Kazuya/Chizuru/Ruka files retain the SHA-256 identities above;
- repository current/index/commit validation and stable-series routing preflight succeed;
- publication uses explicit path staging on `series/rent-a-girlfriend`;
- the final remote head receives the exact-head successful `Repository integration audit`, including any housekeeping child commit permitted by repository policy.

## Next permitted operation

After publication and exact-head integration success, await explicit authorization for V021 or a later bounded volume block. This promotion audit does not authorize inspection of V021 narrative evidence.
