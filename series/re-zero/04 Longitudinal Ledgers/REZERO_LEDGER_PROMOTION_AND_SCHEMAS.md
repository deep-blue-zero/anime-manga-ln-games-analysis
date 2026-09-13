---
series: RE_ZERO
artifact_type: ledger_architecture
scope: LONGITUDINAL_LEDGER_PROMOTION_AND_SCHEMA_CONTRACT
generation: V0.3
status: canonical
release_state: mutable_active
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
---

# Re:Zero — longitudinal ledger promotion and schemas

## Responsibility

This document defines **when** Re:Zero receives longitudinal ledgers and what responsibilities those ledgers may own. It is not itself a data ledger.

No recurring ledger was promoted at bootstrap. Frozen volume readings were the initial source of analytical state.

## Current promoted state

At the project-initiation architecture-repair boundary after the V02 freeze, the recurring responsibilities below crossed the promotion threshold. Their canonical current home is now:

`REZERO_MASTER_LONGITUDINAL_LEDGER.md`

The master ledger was backfilled from the frozen V01/V02 canonical readings and advanced prospectively through V03. It did not exist prospectively for the first two readings, and no frozen reading was changed. It owns claim revision, route/event-state, knowledge, relationship, character-state/stress, institution/power, mechanics/world-model, diagnostic ordinary-life, Japanese terminology/register, prospective-question, and promotion-readiness state.

The following candidate sections now define responsibilities that may later split out of the master ledger when independent retrieval/revision burden warrants specialization. They are not unpromoted gaps and do not authorize parallel competing homes.

### Registered exact candidate homes

These paths are reservations, not instantiated artifacts:

| Responsibility | Exact candidate filename | V03 disposition |
|---|---|---|
| event-state / route | `REZERO_EVENT_STATE_AND_ROUTE_LEDGER.md` | `RETAIN IN MASTER` |
| knowledge / information asymmetry | `REZERO_KNOWLEDGE_AND_INFORMATION_ASYMMETRY_LEDGER.md` | `RETAIN IN MASTER` |
| relationship continuity | `REZERO_RELATIONSHIP_CONTINUITY_LEDGER.md` | `RETAIN IN MASTER` |
| mechanics / metaphysics | `REZERO_MECHANICS_METAPHYSICS_AND_WORLD_MODEL_LEDGER.md` | `RETAIN IN MASTER` |
| institution / faction / power | `REZERO_INSTITUTIONS_FACTIONS_AND_POWER_LEDGER.md` | `DEFER WITH TRIGGER` |
| ordinary life / preferences | `REZERO_ORDINARY_LIFE_AND_PREFERENCES_LEDGER.md` | `DEFER WITH TRIGGER` |
| Japanese voice / register / terminology | `REZERO_JAPANESE_VOICE_REGISTER_AND_TERMINOLOGY_LEDGER.md` | `DEFER WITH TRIGGER` |
| character reconstruction readiness | `REZERO_CHARACTER_RECONSTRUCTION_READINESS_LEDGER.md` | `RETAIN IN MASTER` |

If promoted, every filename above lives in `series/re-zero/04 Longitudinal Ledgers/`. The synthesis architecture and master ledger record the V03 review rationale and exact later triggers.

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

Reserved home: `REZERO_EVENT_STATE_AND_ROUTE_LEDGER.md`.

Potential fields:

- source volume/item and analytical horizon;
- local event-state ID;
- focalizer;
- triggering conditions;
- major observed events;
- outcome;
- current-state durability;
- active-world status;
- retained experience/knowledge;
- reader-only information;
- revision and carry-forward implications;
- linked claims;
- relationship implications.

Purpose: prevent failed, superseded, active, and alternate-route events from collapsing into one chronology.

Promote only when interacting loops or routes require an independently maintained chronology, branch map, or carry-forward matrix; a count of event-states alone is insufficient.

### Knowledge and information-asymmetry ledger

Reserved home: `REZERO_KNOWLEDGE_AND_INFORMATION_ASYMMETRY_LEDGER.md`.

Potential fields:

- proposition/secret;
- holder;
- source of knowledge;
- confidence;
- event-state and route;
- false or competing belief;
- material nonholder;
- disclosure event;
- suppression or constraint;
- decision and relationship consequences;
- revision history.

Purpose: reconstruct decisions against actual information rather than reader omniscience.

Promote only when recurring proposition-holder-nonholder networks, mistaken beliefs, and disclosure revisions can no longer be retrieved safely from the compact master table.

### Relationship-state ledger

Reserved home: `REZERO_RELATIONSHIP_CONTINUITY_LEDGER.md`.

Potential fields:

- dyad/network;
- active event-state and route;
- Subaru's retained relationship history where relevant;
- counterpart's retained relationship history;
- mutually enacted history;
- reader-only discarded-state evidence;
- trust;
- disclosure;
- dependency;
- affection/duty/fear/rivalry;
- power asymmetry;
- consent and obligation;
- address/register evidence;
- rupture/repair;
- non-mutual continuity;
- state-specific divergence;
- next uncertainty.

Purpose: preserve asymmetric continuity and recipient-conditioned behavior.

Promote only when multiple dyads or a network require independently maintained remembered histories, rupture/repair chains, disclosure transitions, or cross-dyad comparison.

### Character-state and stress continuity ledger

This responsibility remains embedded in the master character/readiness tables and, after promotion, in protocol-governed character monographs. It has no separately reserved file at V03. If later evidence shows a distinct cross-character stress-state retrieval burden, an architecture review must first define its non-duplicative scope.

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

Reserved home: `REZERO_INSTITUTIONS_FACTIONS_AND_POWER_LEDGER.md`.

Potential fields:

- institution/faction;
- stated rules/goals;
- observed behavior;
- leadership/member divergence;
- office/status and legal authority;
- enforcement capacity;
- territorial capacity;
- resources;
- patronage;
- information access;
- reputation;
- coercive leverage;
- alliances and internal conflict;
- unresolved contradictions or legitimacy claims.

Purpose: separate formal doctrine from actual power and heterogeneous actor behavior.

Promote when royal-selection or later institutional evidence requires an independently maintained model of actors, formal rules, actual enforcement, resources, patronage, status, coercion, and internal divergence.

### Mechanics and world-model ledger

Reserved home: `REZERO_MECHANICS_METAPHYSICS_AND_WORLD_MODEL_LEDGER.md`.

Potential fields:

- proposition/mechanism;
- who claims it;
- observed regularity;
- cost;
- exception;
- corroboration;
- reader-only pattern;
- competing theory;
- unresolved causation;
- current confidence;
- revision history.

Purpose: prevent character theory from becoming objective lore by repetition.

Promote only when competing theories, observations, costs, exceptions, corroboration, and revision ancestry become too dense for the master table without flattening epistemic status.

### Ordinary-life and preference ledger

Reserved home: `REZERO_ORDINARY_LIFE_AND_PREFERENCES_LEDGER.md`.

Potential fields:

- character;
- domain;
- domain vocabulary where supported: routine, food, labor, study, play, domesticity, leisure, rest, gifts, comfort, boredom, low-stakes social behavior, practical competence, or preference;
- low-stakes observation;
- source/state;
- recipient/context;
- recurrence;
- analytical implication;
- counterexample.

Purpose: prevent character models from being built only from crisis behavior.

Promote when recurrent low-stakes evidence across enough characters, states, or relationships develops an independent comparative burden that monographs plus the master table cannot represent safely.

### Japanese voice, register, and terminology ledger

Reserved home: `REZERO_JAPANESE_VOICE_REGISTER_AND_TERMINOLOGY_LEDGER.md`.

Potential fields:

- speaker/focalizer;
- exact short Japanese form and source locus;
- form type: self-reference, address, title, honorific, sentence ending, lexical choice, formula, narration, or other;
- event/developmental state;
- recipient and social setting;
- role/status and politeness level;
- pragmatic function;
- contrast or shift;
- translation-sensitive implication;
- recurrence, exception, and confidence.

Purpose: preserve speaker-, recipient-, and state-conditioned language without reducing voice to tics or treating a translation choice as Japanese evidence.

Promote when wording and register observations recur across enough speakers, recipients, states, or witnesses that VNN loci and the master terminology table no longer support reliable comparison.

### Character reconstruction readiness ledger

Reserved home: `REZERO_CHARACTER_RECONSTRUCTION_READINESS_LEDGER.md`.

Potential fields:

- character;
- source horizon and default state;
- supported developmental/event states;
- knowledge, remembered-history, recipient, role, and stress coverage;
- ordinary-life coverage and mundane gaps;
- relationship and matched-recipient coverage;
- Japanese-register coverage;
- competence, care, failure, recovery, counterevidence, and abstention coverage;
- current readiness state;
- missing evidence and downgrade conditions;
- monograph/fidelity-audit dependency and result.

Purpose: make character promotion evidence-based and auditable under `REZERO_CHARACTER_RECONSTRUCTION_PROTOCOL.md`.

Promote only when the number and maturity of candidates create an independent cross-horizon audit-scheduling burden. Do not create it merely because one character becomes ready; a single promotion remains routable from the master ledger and its monograph.

## Adjacent future evidence/index layer

The following are architecture candidates, not longitudinal ledgers, and remain uninstantiated through V03:

- `09 Evidence and Indexes/REZERO_CLAIM_EVIDENCE_INDEX.md` — promote after claim-to-locus routing across many freezes or specialists becomes repeatedly error-prone;
- `09 Evidence and Indexes/REZERO_LOCATOR_INDEX.md` — promote after heterogeneous witness locator conventions make direct navigation unreliable;
- `09 Evidence and Indexes/REZERO_CHARACTER_EVIDENCE_MATRIX.md` — promote when comparing evidence breadth and gaps across many near-mature characters becomes materially useful; the matrix cannot promote readiness by itself;
- `09 Evidence and Indexes/REZERO_WITNESS_DEPENDENCY_INDEX.md` — promote after admitted supplemental items develop a dependency/duplication graph the catalog cannot retrieve safely.

These candidates may normalize retrieval but may not become competing claim ledgers, source locks, or witness-admission authorities.

## Ledger history semantics

A promoted ledger should preserve material revisions. Do not overwrite a prior belief as though it never existed when the change matters to understanding the analysis.

Use append/history fields or explicit revision notes where appropriate. The current-state row may change, but frozen volume evidence and material prior interpretations remain recoverable.

## Canonical-home rule

One recurring responsibility gets one canonical ledger home. Do not create competing `notes`, `tracker`, and `master ledger` files that all claim to own the same state.

While a responsibility remains in `REZERO_MASTER_LONGITUDINAL_LEDGER.md`, that file is its canonical cumulative home. If a dedicated ledger is promoted, migrate the necessary current state and material history, leave a clear routing row in the master, update the synthesis architecture and corpus map, and stop maintaining two full competing versions.
