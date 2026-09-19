---
title: "Rent-a-Girlfriend - Directed relationship state ledger"
artifact_id: RAG_RELATIONSHIP_STATE_LEDGER
artifact_type: relationship_state_ledger
series: Rent-a-Girlfriend
generation: V1
version: "1.2"
status: canonical
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
created: "2026-09-19"
source_boundary: "Japanese manga witnesses RAG-JP-EPUB-V001-V002; inspected and closed through V002."
---

# Directed relationship state ledger

## Responsibility

Preserve asymmetric relationship knowledge, labels, acknowledgments, boundaries, actions, and consequences.

## Record schema

`relationship_id | pair | direction | entering_state | event | public_label | private_acknowledgment | beliefs | boundary_change | consequence | exiting_state | evidence_refs`

Markdown tables and bounded prose may implement this semantic schema. Unknown values remain unknown; rows cite canonical volume evidence IDs rather than duplicating primary observations.

## Update and routing rule

Update after each eligible volume only when inspected evidence materially affects this responsibility. Preserve stable IDs and historical states. A reviewed domain may record no material change without manufacturing a row. Consequential claims route back to the owning volume reading and forward to the project artifacts named by the series architecture.

## Current coverage

```yaml
initialized: true
inspected_through_volume: V002
row_count: 12
state: CURRENT_THROUGH_V002
```

## Records

| Relationship ID | Pair and direction | Entering state | Event / public label / private acknowledgment | Boundary change and consequence | Exiting state | Evidence refs |
|---|---|---|---|---|---|---|
| RAG-REL-001 | Kazuya → Chizuru | First-time client idealizing a purchased date | He challenges the performance, apologizes, then repeatedly labels her his girlfriend to family and friends while privately knowing the label is false. | Gains university, family, and residential access; repeatedly presses beyond proposed endings; accepts a Wednesday-only company-routed rule. | Client and deception partner; emotionally impressed and sexually attracted; no mutual romance acknowledged. | RAG-E-V001-002, RAG-E-V001-003, RAG-E-V001-005, RAG-E-V001-006, RAG-E-V001-007, RAG-E-V001-008, RAG-E-V001-009, RAG-E-V001-011, RAG-E-V001-014 |
| RAG-REL-002 | Chizuru → Kazuya | Service provider facing a dissatisfied client | She corrects his harassment, performs for family, protects her campus identity, helps after hearing Nagomi, and defends him at the drinking gathering. | Converts exceptions into explicit limits: no campus contact, no unapproved home access, one paid Wednesday hour, company routing. | Provider and bounded collaborator with shared family stakes; motive mixture unresolved. | RAG-E-V001-002, RAG-E-V001-003, RAG-E-V001-005, RAG-E-V001-006, RAG-E-V001-007, RAG-E-V001-008, RAG-E-V001-009, RAG-E-V001-013 |
| RAG-REL-003 | Kazuya → Mami | Recently rejected former boyfriend | He remains sexually and emotionally preoccupied, reads her renewed familiarity hopefully, and offers physical support after the gathering. | Her re-entry competes with his public girlfriend account and destabilizes his attempted move forward. | Active attachment to former girlfriend; no renewed relationship acknowledged. | RAG-E-V001-001, RAG-E-V001-012, RAG-E-V001-015 |
| RAG-REL-004 | Mami → Kazuya | Initiator of breakup | She resumes familiar address, publicly narrates his dependency, then follows and leans on him. | Reopens proximity after seeing him with Chizuru; intention is withheld. | Former girlfriend taking renewed initiative; motive unresolved. | RAG-E-V001-012, RAG-E-V001-015 |
| RAG-REL-005 | Nagomi → Kazuya and Chizuru | Grandmother worried Kazuya may never form a relationship | Treats Chizuru as a dream fulfilled, presses marriage/sexual continuity, and schedules visits. | Her happiness creates a strong disclosure cost and recurring access condition. | Believes the pair are a serious couple; unaware of payment. | RAG-E-V001-003, RAG-E-V001-008, RAG-E-V001-009 |
| RAG-REL-006 | Sayuri → Chizuru and Kazuya | Chizuru's grandmother; no prior relationship with Kazuya shown | Accepts the couple claim after the hospital coincidence and joins Nagomi's celebration. | Her involvement joins both family networks to the same false proposition. | Believes Kazuya is Chizuru's boyfriend; unaware of the service relation. | RAG-E-V001-006 |
| RAG-REL-007 | Kazuya → Chizuru | Recurring client, neighbor, and deception partner | Thanks her for consolation, preserves the Izu cover, announces a future breakup, apologizes, says he will stop renting her, then dives after her. | Moves toward formal termination while performing an unpriced high-cost rescue attempt. | Paid relationship announced for closure; personal significance evident in action; no mutual romance or rescue outcome established. | RAG-E-V002-001, RAG-E-V002-005, RAG-E-V002-008, RAG-E-V002-012, RAG-E-V002-016, RAG-E-V002-017 |
| RAG-REL-008 | Chizuru → Kazuya | Bounded recurring provider and public girlfriend performer | Enforces the extension charge, attributes consolation to work, reacts ambiguously to the Mami question, accepts a final ferry ride, and reiterates the job frame. | Context collision increases exposure; planned access contracts toward a final booking and announced end. | Provider/collaborator under identity collision; affective evidence expands but romantic acknowledgment remains absent. | RAG-E-V002-002, RAG-E-V002-006, RAG-E-V002-013, RAG-E-V002-014, RAG-E-V002-015, RAG-E-V002-016 |
| RAG-REL-009 | Kazuya → Mami | Former boyfriend hopeful about renewed proximity | Searches for reunion advice, responds to the kiss and origin memory, refuses the Pocky kiss, and plans a later confession. | Attachment remains active but does not produce uniform compliance. | Plans a private confession after disembarkation; no restored relationship. | RAG-E-V002-005, RAG-E-V002-009, RAG-E-V002-010, RAG-E-V002-012, RAG-E-V002-015 |
| RAG-REL-010 | Mami → Kazuya | Former girlfriend taking renewed initiative | States a goal to split the public couple, probes him, kisses him, says she lost control, and schedules a private meeting. | Converts ambiguity into repeated strategic and physical intervention. | Actively destabilizing former partner; desired final relationship remains unknown. | RAG-E-V002-003, RAG-E-V002-005, RAG-E-V002-009, RAG-E-V002-016 |
| RAG-REL-011 | Kibe → Kazuya | Childhood friend who believes Kazuya has a real girlfriend | Punches and argues with him after the breakup announcement, then defends his persistent side to Chizuru. | Friendship loyalty becomes moral pressure because disclosure is incomplete. | Caring but misinformed friend; fuller truth is planned, not delivered. | RAG-E-V002-012, RAG-E-V002-014, RAG-E-V002-015 |
| RAG-REL-012 | Kibe → Chizuru | Friend of her supposed boyfriend | Supplies a childhood account, gives her ferry tickets, and asks her to give Kazuya another chance. | His belief creates a new obligation that she accepts with an explicit endpoint. | Treats her as Kazuya's real partner; unaware of the service relation. | RAG-E-V002-014, RAG-E-V002-015 |
