---
series: RE_ZERO
artifact_type: ledger_architecture
scope: LONGITUDINAL_LEDGER_PROMOTION_AND_SCHEMA_CONTRACT
generation: V0.1
status: canonical
release_state: mutable_active
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
---

# Re:Zero — longitudinal ledger promotion and schemas

## Responsibility

This document defines **when** Re:Zero receives longitudinal ledgers and what responsibilities those ledgers may own. It is not itself a data ledger.

No recurring ledger is promoted at bootstrap. Frozen volume readings remain the initial source of analytical state.

## Promotion threshold

Create a ledger only when at least one of these becomes true:

- the same question recurs across enough volume freezes that reliable retrieval is costly;
- state comparisons require a table or maintained chronology that prose files cannot safely reproduce;
- later revisions need a canonical current-state surface while frozen historical readings remain immutable;
- a character, relationship, institution, or mechanic accumulates enough evidence that ad hoc summaries risk contradiction.

Do not create empty ledgers in advance.

## Candidate ledger responsibilities

These are candidates, not mandatory files.

### Route and event-state ledger

Potential fields:

- source volume/item;
- local event-state ID;
- focalizer;
- triggering conditions;
- major observed events;
- outcome;
- current-state durability;
- retained experience/knowledge;
- reader-only information;
- revision implications.

Purpose: prevent failed, superseded, active, and alternate-route events from collapsing into one chronology.

### Knowledge and information-asymmetry ledger

Potential fields:

- proposition/secret;
- holder;
- source of knowledge;
- confidence;
- event-state;
- who incorrectly believes the opposite;
- disclosure changes;
- decision/relationship consequences.

Purpose: reconstruct decisions against actual information rather than reader omniscience.

### Relationship-state ledger

Potential fields:

- dyad/network;
- each party's remembered history;
- trust;
- disclosure;
- dependency;
- affection/duty/fear/rivalry;
- power asymmetry;
- address/register evidence;
- rupture/repair;
- state-specific divergence.

Purpose: preserve asymmetric continuity and recipient-conditioned behavior.

### Character-state and stress continuity ledger

Potential fields:

- character;
- source horizon;
- goals;
- self-model;
- observed stressors;
- behavioral changes;
- coping/recovery evidence;
- retained experience;
- ordinary-life baseline;
- candidate stable tendencies;
- contradictions/counterevidence.

Purpose: distinguish durable development from local crisis effects without diagnosing from vibes.

### Institution, faction, and power ledger

Potential fields:

- institution/faction;
- stated rules/goals;
- observed behavior;
- leadership/member divergence;
- enforcement capacity;
- resources;
- patronage;
- information access;
- coercive leverage;
- unresolved contradictions.

Purpose: separate formal doctrine from actual power and heterogeneous actor behavior.

### Mechanics and world-model ledger

Potential fields:

- proposition/mechanism;
- who claims it;
- observed regularity;
- cost;
- exception;
- corroboration;
- reader-only pattern;
- current confidence;
- revision history.

Purpose: prevent character theory from becoming objective lore by repetition.

### Ordinary-life and preference ledger

Potential fields:

- character;
- domain;
- low-stakes observation;
- source/state;
- recipient/context;
- recurrence;
- analytical implication;
- counterexample.

Purpose: prevent character models from being built only from crisis behavior.

## Ledger history semantics

A promoted ledger should preserve material revisions. Do not overwrite a prior belief as though it never existed when the change matters to understanding the analysis.

Use append/history fields or explicit revision notes where appropriate. The current-state row may change, but frozen volume evidence and material prior interpretations remain recoverable.

## Canonical-home rule

One recurring responsibility gets one canonical ledger home. Do not create competing `notes`, `tracker`, and `master ledger` files that all claim to own the same state.
