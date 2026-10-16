---
title: "Peach Girl — Character Development and Readiness"
artifact_id: PEACH_GIRL_CHARACTER_DEVELOPMENT_AND_READINESS_LEDGER
artifact_type: character_development_readiness_ledger
series: "Peach Girl / ピーチガール"
series_id: peach-girl
generation: PEACH_GIRL_BOOTSTRAP_V1
version: "0.2"
status: active_provisional
scope: "Character Development and Readiness; source-derived records through the committed high-water mark named in the entrypoint"
source_boundary: "Original Japanese 新装版 mainline; admitted volumes through the entrypoint's committed high-water mark; prospective rows carry their own frontier"
canonical_home: series/peach-girl/03 Longitudinal Ledgers/PEACH_GIRL_CHARACTER_DEVELOPMENT_AND_READINESS_LEDGER.md
created: "2026-10-16"
review_status: OWNER_EXECUTION_AUTHORIZED_LOCAL_RESULT_UNREVIEWED
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
do_not_use_as_literary_evidence: true
---

# Character Development and Readiness

This instrument owns verified local subject identity, character-level developmental/decision state and readiness derived from that evidence. The [architecture](../00%20Frameworks%20and%20Methods/PEACH_GIRL_SYNTHESIS_ARCHITECTURE.md#character-reconstruction-contract) owns the reconstruction contract. Pair feelings/commitments belong in the relationship ledger; proposition knowledge and public reputation belong in the information ledger; arguments and revisions belong in the claims ledger.

Development and readiness share a home because promotion depends on this same subject's state coverage and gaps. They are distinct record types. No character name, trait, psychological conclusion or readiness assessment is prepopulated.

## Records and allocation

| Type / stable identifier | Required fields |
| --- | --- |
| Subject `PG-CHAR-####` | Source-spelled name or bounded unnamed identity; alias/language/basis if inspected; continuity; first observation; identity uncertainty; any actually curated global IDs, otherwise null |
| Development event `PG-CS-####` | Subject; represented time/range and certainty; learned-after source frontier; previous state; event kind; observed action; attributed intention/self-report; options and constraints; recipient/response/consequence where relevant; observation refs; claim/version; interpretation and alternative; support strength/basis; correction link |
| Current subject view | Subject + temporal/disclosure boundary; active event IDs/versions; scoped formulation; unresolved contradictions and unobserved contexts |
| Readiness decision `PG-RD-####` | Subject + target artifact/domain; source and Git evidence cutoff; context diversity; supporting/counterevidence; written-language/form coverage; missing domains; validation status; assessment/reviewer/date; prior decision; governing claim versions |

Event kinds: `DISPOSITION_CHANGE / KNOWLEDGE_CHANGE / RELATIONSHIP_CHANGE / CONTEXT_CHANGE / REVEALED_NOT_NEW / UNRESOLVED`. Link the authoritative knowledge or relationship row; do not restate its entire proposition. Actor-level agency records actual choice processes; the relationship ledger owns their pair-state consequences. A new disclosure of an old habit does not establish newly developed behavior.

Readiness states: `UNASSESSED / INSUFFICIENT_EVIDENCE / BOUNDED_PROVISIONAL / DOMAIN_READY`. These are local scoped assessments, not artifact authority or global capability grades. No row is needed merely to assign every mentioned subject UNASSESSED.

## Evidence, update and history

Allocate an ID only on actual admitted evidence, monotonically within its prefix; never recycle it. Distinguish identity uncertainty, source legibility, timing and interpretation uncertainty. Every state event requires a reading's `PG-EV-VNN-####` with exact locator and disclosure frontier. A self-report can be recorded without being endorsed as a stable trait. A consequential interpretation also points to a `PG-CL-####@version`, supporting evidence, strongest available counterevidence and plausible alternative.

A future VNN transaction appends events for material goal/choice/development changes, newly disclosed state or a consequential contradiction. Ordinary momentary mood stays local unless it changes the model. Update readiness only when an actual proposal is assessed or evidence materially changes an existing assessment. Independent contexts and failures matter; repeated shots of one encounter are not independent tests.

Preserve original names/identity allocation, event formulations, source frontiers and assessment history. Amend the current view through targeted edits with an appended event/revision; retain old versions. Later retrospective explanation has its actual learned-after frontier. A frozen `PG-FR-VNN` cites the versions then active and contains enough state to recover them after this ledger advances. Errata append a reason and replacement link.

The sequential closeout certifies this instrument updated or records no material change without a dummy row. Bootstrap source-derived subject, event, current-state and readiness rows: **0**.

## Subject register

| Subject | Source identity / aliases and basis | Continuity / first observation | Identity uncertainty / global IDs |
| --- | --- | --- | --- |
| PG-CHAR-0001 | 安達もも (Adachi Momo). Surname from classmates at i0007; given name written もも at i0031; called ももちゃん / もも; first-person narrator | Original mainline; PG-EV-V01-0001 (i0007) | None; global ID null |
| PG-CHAR-0002 | 東寺ヶ森 (Tōjigamori), called とーじ by Momo; given name カズヤ called at i0065 (kanji 一矢 shown as a label at i0016, MODERATE) | Original mainline; PG-EV-V01-0004 (i0013) | Kanji of given name MODERATE; global ID null |
| PG-CHAR-0003 | 柏木沙絵 (Kashiwagi Sae), called さえ / さえちゃん; full name at i0015 | Original mainline; PG-EV-V01-0002 (i0009) | None; global ID null |
| PG-CHAR-0004 | 岡安浬 (Okayasu Kairi), furigana カイリ, i0024; called カイリ, 岡安; Momo calls him バカ安 | Original mainline; PG-EV-V01-0007 (i0022) | None; global ID null |
| PG-CHAR-0005 | School nurse, called 操ちゃん by Kairi (i0098); surname not given | Original mainline; i0097 | Given name only; global ID null |
| PG-CHAR-0006 | Leader of Kairi's female fan bloc (wavy hair), unnamed | Original mainline; PG-EV-V01-0014 (i0036–i0041) | Unnamed; may be one of the hallway girls elsewhere; not merged |
| PG-CHAR-0007 | Unnamed middle-school friend who reported Tōji's alleged dislike of dark skin | Reported in flashback, PG-EV-V01-0027 (i0077) | Unnamed; identity unknown |

## Developmental events

| Event / version | Subject / prior | Story time / learned after | Kind / action / intention / options / consequences | Evidence / claim version | Uncertainty / counterreading / correction |
| --- | --- | --- | --- | --- | --- |
| PG-CS-0001@1 | PG-CHAR-0001 / — | Before series start (middle school → high-school entry) / V01 | REVEALED_NOT_NEW: chose her high school because Tōji applied there; long concealed love; two-year sun-avoidance regimen as a precondition for confessing | PG-EV-V01-0006, -0021, -0027; PG-CL-0008@1 | Self-report via narration; durations are her own |
| PG-CS-0002@1 | PG-CHAR-0001 / CS-0001 | Opening day / V01 | DISPOSITION_CHANGE (local): under threat of exposure she tells a deliberate decoy lie to Sae (Kairi). Options: deny, deflect, tell the truth. Chose deception. Consequence: premise for the graffiti accusation; later used against her | PG-EV-V01-0007, -0011, -0040 | Panic response; one instance |
| PG-CS-0003@1 | PG-CHAR-0004 / — | Two years before story (both in 2nd year of middle school) / V01 i0048 | REVEALED_NOT_NEW: was rescued from drowning by Momo; believes she gave him mouth-to-mouth; afraid of water since | PG-EV-V01-0017, -0022; PG-CL-0007@1 | Who gave CPR is disputed |
| PG-CS-0004@1 | PG-CHAR-0004 / CS-0003 | ~1 week after opening day / V01 | DISPOSITION_CHANGE: from flirtatious stranger to active pursuer of Momo (public kiss claim, kiss, repeated advances, proposal i0168) | PG-EV-V01-0013, -0018, -0019, -0029, -0050; PG-CL-0006@1 | Sincerity vs game unresolved |
| PG-CS-0005@1 | PG-CHAR-0002 / — | DayA+1 (D-4) / V01 | KNOWLEDGE_CHANGE: learns by overhearing that Momo has loved him since middle school, and of the tan report → link PG-KN-0004 | PG-EV-V01-0026, -0028 | Acquired without Momo's consent |
| PG-CS-0006@1 | PG-CHAR-0002 / CS-0005 | D-3 / V01 | RELATIONSHIP_CHANGE: confesses (「オレも安達のことが好きだ」); see PG-CM-0001 | PG-EV-V01-0032, -0033 | — |
| PG-CS-0007@1 | PG-CHAR-0003 / — | D-4 to D0 / V01 | DISPOSITION_CHANGE (revealed through action): moves from imitation and competitive flirting to engineered misinformation aimed at the Momo–Tōji relationship (TX-0006…0011) | PG-EV-V01-0034, -0038, -0040, -0042, -0043, -0049, -0052; PG-CL-0002@1, PG-CL-0003@1 | Motive mix unresolved |
| PG-CS-0008@1 | PG-CHAR-0001 / CS-0001 | D-2 / V01 | CONTEXT_CHANGE: asks Tōji to keep their relationship secret, especially from Sae; option to tell Sae refused | PG-EV-V01-0037; PG-CM-0002 | Rationale given: rumor; underlying distrust of Sae |
| PG-CS-0009@1 | PG-CHAR-0001 / CS-0008 | D-1 to D0 / V01 | KNOWLEDGE_CHANGE: receives Sae's claim and finds the packet; doubts Tōji; avoids him without asking; at D0 refuses his kiss | PG-EV-V01-0040, -0041, -0053 | Her inference is reasonable from her information; the information was false or engineered |
| PG-CS-0010@1 | PG-CHAR-0002 / CS-0006 | D0 / V01 | KNOWLEDGE_CHANGE + action: believes Sae's fabricated report that Momo prefers Kairi; forcibly takes Momo to the pergola and attempts a kiss | PG-EV-V01-0051, -0052, -0053; PG-CL-0005@1 | Interior withheld at i0175–i0178 |

## Current subject state

| Subject / boundary | Active event versions | Scoped state | Unresolved evidence / contexts |
| --- | --- | --- | --- |
| PG-CHAR-0001 @ PG-FR-V01 | CS-0001, -0002, -0008, -0009 | Combative in public, anxious and planful in romance; relies on second-hand reports about Tōji; in crisis after refusing his kiss | No family, home or non-romantic daily-life context yet |
| PG-CHAR-0002 @ PG-FR-V01 | CS-0005, -0006, -0010 | Protective, private, inexperienced; trusts Sae; misinformed about Momo | Interior largely withheld |
| PG-CHAR-0003 @ PG-FR-V01 | CS-0007 | Imitative and status-seeking; deliberately deceives both Momo and Tōji | Motive weighting; authorship of graffiti, notes, packet |
| PG-CHAR-0004 @ PG-FR-V01 | CS-0003, -0004 | Provocative, intrusive, attentive; protective in danger; pursuing Momo with stated seriousness | Sincerity; family background (claimed sister unverified) |

## Readiness assessments

| Assessment / prior | Subject / target / domain / cutoff | Evidence diversity / counterevidence | Gaps / validation | Assessment / reviewer / date / claim versions |
| --- | --- | --- | --- | --- |

Revision history: 0.1 — bootstrap schema, zero rows, 2026-10-16 UTC. 0.2 — V01 transaction rows appended (frontier PG-FR-V01), 2026-10-16 UTC.
