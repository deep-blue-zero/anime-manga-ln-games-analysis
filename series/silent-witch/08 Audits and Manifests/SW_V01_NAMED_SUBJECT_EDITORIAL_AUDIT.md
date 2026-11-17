---
title: "Silent Witch — V01 Named-Subject Editorial Audit"
artifact_id: SW_V01_NAMED_SUBJECT_EDITORIAL_AUDIT
artifact_type: editorial_audit
series: "Silent Witch: Secrets of the Silent Witch"
series_id: silent-witch
generation: V1
version: "1.0"
status: canonical
scope: "Bounded named-subject and referential-clarity repair of the frozen V01 reading, with one erratum; no literary reading, source change or boundary advance"
source_boundary: "Japanese LN V01 reading as published; no source text reread for this audit beyond the locators already cited"
created: "2026-10-14"
canonical_home: "series/silent-witch/08 Audits and Manifests/SW_V01_NAMED_SUBJECT_EDITORIAL_AUDIT.md"
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
do_not_use_as_literary_evidence: true
---

# V01 named-subject editorial audit

## Assignment and boundary

The owner instructed a correction of a recurring weakness in analytical prose: generic roles standing in for characters whose identities are already established. For Silent Witch the instruction covered a bounded repair of the frozen [V01 reading](../02%20Sequential%20Readings/SW_V01_DEEP_READING.md), project-local method and template integration, and this receipt. It did not authorize a new literary reading, a rewrite of the analysis, a change to claims or freezes, a source-admission change, or any advance past V01. None occurred.

The corpus-wide rule was proposed separately, on the cross-cutting branch `codex/named-subject-default`, as section 15 of the analytical handoff and integration contract, with pointers in `AGENTS.md`, the ChatGPT routing subsection and the stage handoff template. That governance change follows its own integration path and is not part of this series branch. The Silent Witch method now states the rule locally and defers to the contract wherever the contract states it.

| Field | Value |
|---|---|
| Reading before | Version 1.0, SHA-256 `43c351c48ca5ce873f1b4f14cf3783933d44160f22f675fa3ea16e18c697bb91`, as published at series-branch commit `bbe6413cc74918c6ef7c6cf4b5d109da0ffe4618`. |
| Reading after | Version 1.1; its containing commit and hash are recorded by Git. |
| Classification vocabulary | `JUSTIFIED_ROLE_REFERENCE`, `SOURCE_REQUIRED_ANONYMITY`, `KNOWLEDGE_BOUNDARY_REQUIRED`, `UNNECESSARY_GENERICIZATION`, `AMBIGUOUS_REFERENT`, `INCORRECT_IDENTITY_OR_ATTRIBUTION`. |

## Method

1. A disposable scanner listed every non-table occurrence of 36 candidate role and epithet patterns in the reading: 176 candidates. The scanner judged nothing and substituted nothing.
2. Each candidate was read in its paragraph and classified by hand. Tables were reviewed separately.
3. Each supported defect was repaired as an exact replacement whose old text had to match exactly once; any other count would have stopped the patch. One hundred replacements were applied this way.
4. A sampled semantic check then read the synopsis, the chapter-7 close reading, the chapter-10 opening and the exit freeze in full. It found three pronoun problems introduced by the repairs themselves, which were fixed by hand: a broken clause in the kiss paragraph, a “his” that could mean Felix or Wildianu, and a “his favourite … he will eat him” whose referents could be swapped.
5. Mechanical preservation checks compared the reading before and after.

## Findings

| Class | Repaired | Typical pattern |
|---|---:|---|
| `UNNECESSARY_GENERICIZATION` | 73 | Felix as “the prince” where only his personal choices mattered; Nero as “the cat”; Thornley as “the teacher”; Cyril as “the vice-president”; Monica as “the heroine” or “a girl”. |
| `AMBIGUOUS_REFERENT` | 16, plus 3 pronoun repairs | “A count’s daughter”, which fits both Caroline and Isabelle; “his spirit”, which fits both Lynn and Wildianu; a rationale with no stated holder. |
| `KNOWLEDGE_BOUNDARY_REQUIRED` | 10 | Retrospective naming that needed the earlier participant’s knowledge stated alongside it. |
| `INCORRECT_IDENTITY_OR_ATTRIBUTION` | 0 | No passage named the wrong person. |
| Erratum: knowledge state | 1 | See below. |

No defect involved a misattributed speaker, thinker or recipient.

### Representative changes

| Before | After | Class |
|---|---|---|
| The volume opens away from its heroine. | The volume opens with Isabelle Norton, not with Monica Everett. | `KNOWLEDGE_BOUNDARY_REQUIRED` |
| …a black cat at its feet: the Silent Witch. Isabelle watches, enraptured. | …the Silent Witch. Isabelle knows her rescuer only by that title; chapter 1 identifies the Witch as Monica Everett. Isabelle watches, enraptured. | `KNOWLEDGE_BOUNDARY_REQUIRED` |
| …guarding a blond student sitting as bait. The blond student releases her… | …guarding a blond student sitting as bait; Monica does not yet know that he is Felix. He releases her… | `KNOWLEDGE_BOUNDARY_REQUIRED` |
| …a quarrel between Lana and a count’s daughter. … When the count’s daughter blames Lana… | …a quarrel between Lana and Caroline, a count’s daughter. … When Caroline blames Lana… | `AMBIGUOUS_REFERENT` |
| …tells his spirit that if a Sage must watch him he would rather it were the one he adores: the Silent Witch. | …tells Wildianu that … the one he adores: the Silent Witch. He does not know that she is Monica. | `AMBIGUOUS_REFERENT`; `KNOWLEDGE_BOUNDARY_REQUIRED` |
| The cat, in human form, delivers the unconscious vice-president to the prince… | Nero, in human form, delivers the unconscious Cyril to Felix… | `UNNECESSARY_GENERICIZATION` |
| The prince has slipped his spirit into the cat’s robe to spy… | Felix has slipped Wildianu into Nero’s robe to spy… | `AMBIGUOUS_REFERENT` |
| In delirium he begs the brooch back from the cat… | …from Nero, whom he sees only as a cat… | `KNOWLEDGE_BOUNDARY_REQUIRED` |
| Nobody would take so plain and so obviously amateur a girl for a Sage… | Louis argues that nobody would take… | `AMBIGUOUS_REFERENT` |

### Erratum

The synopsis said Cyril, having studied Monica’s hand, “is almost sure where he has seen it.” That attributes more knowledge than the reading’s own evidence supports: claim SW-C-0009 and observation SW-E-LNJP-V01-111 record an unverified suspicion inferred from his actions. Because the change alters a stated knowledge state, it is classed as a substantive correction rather than a stylistic one, and it is recorded visibly in the reading’s editorial revision record. The new wording says he appears to connect the hand with the one that reached for him in the forest and says nothing. The claim, its class and its state are unchanged.

## Role references deliberately retained

Twenty-two occurrences of “the prince” remain, with every other retained label, because the role does analytical work:

- **`JUSTIFIED_ROLE_REFERENCE` — royal status is the point:** the brooch watching “the prince” rather than protecting him; Aaron’s insult that the prince is royal in name only; Monica as “the prince’s guard”; the death sentence for an attempt on royalty; Monica speaking to the prince without lifting her eyes; Cyril’s rage at slights to the prince; the plan to brainwash the prince; attempts on the prince’s life; the mission statement in the knowledge table.
- **`JUSTIFIED_ROLE_REFERENCE` — titles and framings:** the chapter titled for the prince’s secret; Monica’s own belief that “the prince” has paw pads, her phrase for 殿下; jacket copy; the cover image’s cat, described as drawn.
- **`SOURCE_REQUIRED_ANONYMITY`:** the prologue’s unnamed blue-eyed watcher, whose identification remains inference under SW-C-0006; the hooded figure, the Witch and the small caster in the prologue as Isabelle perceives them; Monica unnamed in the prologue.
- **`KNOWLEDGE_BOUNDARY_REQUIRED`, retained as focalized perception:** the monster Cyril believes he saw; the shabby girl and the girl of fifteen in Thornley’s viewpoint before he realizes who she is; the Silent Witch as the reputation Annie, Isabelle and Felix know.

## Semantic-preservation checks

| Check | Result |
|---|---|
| Japanese quotations | 64 before and after, identical text and order; each still verified verbatim against the sealed block map at its cited locator. |
| Locators | 521 occurrences before and after, identical sequence; all present in the element map. |
| Observation citations | 116 `obs.` citations identical; the register’s 132 rows unchanged. |
| Claims and questions | SW-C and SW-P identifiers unchanged in sequence; the only additions are SW-C-0009 and SW-E-LNJP-V01-111 cited in the new revision record. |
| Structure | All headings unchanged except the added editorial revision record; 314 table rows before and after. |
| Freezes | Entry and exit freezes keep their content and knowledge statements; the exit freeze’s list of relationships now names Felix where it had “a prince”. |
| Event order and arguments | Unchanged; replacements are confined to the reference expressions and the clauses that state knowledge boundaries. |

The master ledger received two clarifications of “his spirit” to Wildianu and a note in SW-U-V01. No ledger claim, record count or state changed.

## Remaining questions

- The corpus-wide standard is on `codex/named-subject-default` pending owner review and integration. Until it reaches main, the Silent Witch method’s local statement is the operative rule for this project.
- Earlier Claude-authored readings in other projects may contain the same pattern. The instruction did not authorize repairing them; each would need its own bounded audit under its project’s frozen-artifact rules.
