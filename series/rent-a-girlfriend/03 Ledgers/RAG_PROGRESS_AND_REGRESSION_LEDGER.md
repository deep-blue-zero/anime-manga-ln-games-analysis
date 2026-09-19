---
title: "Rent-a-Girlfriend - Progress and regression ledger"
artifact_id: RAG_PROGRESS_AND_REGRESSION_LEDGER
artifact_type: progress_regression_ledger
series: Rent-a-Girlfriend
generation: V1
version: "1.7"
status: canonical
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
created: "2026-09-19"
source_boundary: "Japanese manga witnesses RAG-JP-EPUB-V001-V007; inspected and closed through V007."
---

# Progress and regression ledger

## Responsibility

Preserve domain-specific changes against named baselines without collapsing them into one romance score.

## Record schema

`change_id | domain | prior_state | classification | observed_delta | agents_who_know | consequence | durability_boundary | reversal_or_reconfiguration | evidence_refs`

Markdown tables and bounded prose may implement this semantic schema. Unknown values remain unknown; rows cite canonical volume evidence IDs rather than duplicating primary observations.

## Update and routing rule

Update after each eligible volume only when inspected evidence materially affects this responsibility. Preserve stable IDs and historical states. A reviewed domain may record no material change without manufacturing a row. Consequential claims route back to the owning volume reading and forward to the project artifacts named by the series architecture.

## Current coverage

```yaml
initialized: true
inspected_through_volume: V007
row_count: 42
state: CURRENT_THROUGH_V007
```
```

## Records

| Change ID | Domain / prior state | Classification and observed delta | Knowledge / consequence | Durability boundary and reconfiguration | Evidence refs |
|---|---|---|---|---|---|
| RAG-PRG-001 | Information: strangers after first rental | GAIN — Kazuya and Chizuru learn each other's university identity, family linkage, hospital context, and neighboring residence. | Both know; creates practical access and risk. | Durable through V001; no knowledge erasure. | RAG-E-V001-005, RAG-E-V001-006, RAG-E-V001-007 |
| RAG-PRG-002 | Public status: no shared social identity | RECONFIGURATION — a private service becomes a girlfriend claim believed by family and peers. | Several audiences know a false version; correction cost rises. | Durable through V001; new audiences accumulate. | RAG-E-V001-003, RAG-E-V001-006, RAG-E-V001-011 |
| RAG-PRG-003 | Access: one-off bookings | GAIN — one paid Wednesday hour becomes recurring until both grandmothers leave hospital. | Jointly acknowledged by Kazuya and Chizuru. | Active at V001 boundary; conditional and untested for long durability. | RAG-E-V001-009 |
| RAG-PRG-004 | Honesty: Kazuya intends to end the lie | LOSS — he repeatedly defers or interrupts disclosure under immediate social pressure. | He recognizes the lie and its cost; family and peers remain uninformed. | Pattern persists through V001; attempted confession is counterevidence to total unwillingness. | RAG-E-V001-004, RAG-E-V001-006, RAG-E-V001-008, RAG-E-V001-011 |
| RAG-PRG-005 | Boundary understanding: Kazuya initially treats performance as personal fraud | GAIN — he admits fault and learns explicit rules around campus, residence, time, payment, and routing. | Knowledge changes; compliance remains inconsistent. | Durable knowledge through V001, with repeated behavioral pressure. | RAG-E-V001-002, RAG-E-V001-005, RAG-E-V001-007, RAG-E-V001-008, RAG-E-V001-009 |
| RAG-PRG-006 | Romance: no mutually acknowledged attraction | NO_DEMONSTRATED_CHANGE — Kazuya's attraction is explicit, while Chizuru's romantic state and any joint status remain unestablished. | Kazuya alternates idealization and discounting; Chizuru maintains limits. | No private romantic transition through V001 despite material/social closeness. | RAG-E-V001-009, RAG-E-V001-010, RAG-E-V001-013, RAG-E-V001-014 |
| RAG-PRG-007 | Transactional accountability: the V001 drinking extension is unsettled | GAIN — Chizuru invoices and receives recognition of a 17,000-yen extension charge while denying special treatment. | Both central characters know; prevents exceptional access from becoming an unpriced precedent. | Durable accounting fact through V002; emotional meaning remains open. | RAG-E-V002-002 |
| RAG-PRG-008 | Identity separation: campus and rental audiences were spatially separate | LOSS — the Izu trip brings both presentations and both friend groups into one location, and Mami weaponizes the rental name. | Kazuya, Chizuru, and Mami know parts of the collision; male friends retain the cover. | Exposure risk persists at V002 boundary. | RAG-E-V002-004, RAG-E-V002-005, RAG-E-V002-007 |
| RAG-PRG-009 | Honesty: repeated intention without public correction | MIXED_GAIN — Kazuya publicly announces a breakup and later plans full disclosure to Kibe, but still withholds the rental truth. | Friends update the future label while preserving a false past and false moral premise. | Partial correction is durable; complete disclosure remains pending. | RAG-E-V002-008, RAG-E-V002-012, RAG-E-V002-015 |
| RAG-PRG-010 | Former-partner boundary: Mami has renewed ambiguous proximity | LOSS — her explicit separation goal, identity intervention, deliberate kiss, and private meeting increase influence over Kazuya. | Kazuya reads possible reunion; Chizuru observes the kiss; Mami controls her stated goal. | Active at V002 boundary, interrupted by emergency. | RAG-E-V002-003, RAG-E-V002-007, RAG-E-V002-009, RAG-E-V002-016 |
| RAG-PRG-011 | Peer audience: friends passively believe the couple claim | RECONFIGURATION — Kibe acts on that belief through a fight, moral appeal, and ferry tickets. | False information now produces material opportunities and costs. | Durable consequence even if later corrected. | RAG-E-V002-012, RAG-E-V002-014, RAG-E-V002-015 |
| RAG-PRG-012 | Scheduled access: weekly arrangement active until both grandmothers leave hospital | CONTRACTION — Nagomi's expected discharge defines a final booking and Kazuya says he will stop renting Chizuru. | Both central characters acknowledge an intended endpoint. | Termination not yet verified; emergency may reconfigure it. | RAG-E-V002-011, RAG-E-V002-013, RAG-E-V002-016 |
| RAG-PRG-013 | Personal action: Chizuru's positive significance is often discounted as paid or impossible | GAIN_IN_ACTION — Kazuya accepts immediate physical risk in an unpriced rescue attempt. | Only Kazuya and reader have the action at the boundary; Chizuru is unconscious. | Strong behavioral delta, but outcome and stable self-understanding unobserved. | RAG-E-V002-017 |
| RAG-PRG-014 | Rescue information: Chizuru is unconscious and unaware of Kazuya's dive | GAIN — she wakes, saves him through CPR, and both survive to receive medical care. | Both central characters know the reciprocal care; friends know a public version. | Durable event knowledge; motive remains disputed or unspoken. | RAG-E-V003-001, RAG-E-V003-003 |
| RAG-PRG-015 | Mami trajectory: private meeting and Kazuya confession planned | INTERRUPTION — the emergency cancels the meeting and no confession occurs. | Mami, Kazuya, and reader know the missed plan from different positions. | Later resumption is possible, but the V002 sequence is not completed. | RAG-E-V003-002 |
| RAG-PRG-016 | Self-knowledge: Kazuya acts for Chizuru without settled interpretation | GAIN — he privately recognizes serious feeling and asks to continue the relationship in rental form. | Kazuya and reader know; Chizuru receives the request without the interior confession. | Durable recognition through V003; behavioral maturity remains untested. | RAG-E-V003-005, RAG-E-V003-009 |
| RAG-PRG-017 | Access: final discharge-week booking and announced end | RECONFIGURATION — Chizuru permits “a little longer” and defines a real-girlfriend exit condition. | Both central characters know the new rule. | Continued access remains paid, temporary, and nonexclusive. | RAG-E-V003-009, RAG-E-V003-010 |
| RAG-PRG-018 | Honesty: weekend breakup disclosure is jointly planned | LOSS — the family trip and room arrangement displace disclosure despite Sayuri's hypothetical acceptance of lies. | The central pair retain truth; grandmothers retain the false couple belief. | No correction through V003. | RAG-E-V003-006, RAG-E-V003-007 |
| RAG-PRG-019 | Privacy: the rental secret is contained among Kazuya, Chizuru, and company context | LOSS — Ruka independently recognizes Chizuru and gains leverage over the false couple. | Ruka, Kazuya, and Chizuru know of the breach; Kuribayashi is not shown knowing. | Exposure remains unresolved at the cliffhanger. | RAG-E-V003-013, RAG-E-V003-014 |
| RAG-PRG-020 | Romance: Kazuya is attracted but no private state is acknowledged | ASYMMETRIC_GAIN — Kazuya recognizes serious feeling; Chizuru does not reciprocally acknowledge romance and preserves rental boundaries. | Kazuya and reader know his state; joint status remains unchanged. | Do not collapse one-sided recognition into couple progress. | RAG-E-V003-005, RAG-E-V003-008, RAG-E-V003-009, RAG-E-V003-010 |
| RAG-PRG-021 | Ruka relation: informed challenger with no agreed romantic status | RECONFIGURATION — secrecy leverage and sincere feeling produce a provisional girlfriend arrangement. | Kazuya, Ruka, and Chizuru know its purpose and asymmetry. | The status persists through V004 but lacks reciprocal love and began under disclosure pressure. | RAG-E-V004-003, RAG-E-V004-004, RAG-E-V004-005 |
| RAG-PRG-022 | Privacy: Ruka can expose the secret at will | LIMITED_GAIN — Ruka later says she never intended disclosure and understands the trial form. | Kazuya receives reassurance; Chizuru observes some of the campus encounter. | Her continuing access demands and the origin bargain prevent treating risk as eliminated. | RAG-E-V004-009 |
| RAG-PRG-023 | Chizuru model: job and private goal underexplained | GAIN — acting school, actress ambition, tuition need, and performance practice become explicit. | Kazuya and reader gain vocational context. | Goal is durable knowledge; future success and full family awareness remain unknown. | RAG-E-V004-012 |
| RAG-PRG-024 | Kazuya appraisal: acknowledged attachment without tested rival uncertainty | LOSS_THEN_PARTIAL_REPAIR — he surveils Chizuru under a false boyfriend theory, then accepts correction and apologizes. | Chizuru learns of the following; Kazuya revises his own belief. | Apology does not undo the boundary violation or prove future restraint. | RAG-E-V004-011, RAG-E-V004-013 |
| RAG-PRG-025 | Reciprocity: central exchange remains primarily paid or emergency-based | GAIN — Chizuru gives a personalized off-contract gift and Kazuya begins work and returns an unpriced object. | Both know the exchange; Kazuya attaches strong personal meaning. | His delivery occurs during paid access, and no mutual romantic acknowledgment follows. | RAG-E-V004-014, RAG-E-V004-015, RAG-E-V004-016 |
| RAG-PRG-026 | Ordinary life: Kazuya has no paid employment in observed material | GAIN — financial pressure and reciprocal obligation lead him to a karaoke job. | Kazuya and reader know; the workplace also becomes the final setting. | Initial employment is established, while sustained competence and durability remain untested. | RAG-E-V004-010, RAG-E-V004-015, RAG-E-V004-019 |
| RAG-PRG-027 | Consent clarity: V004 ends before the private-room act | GAIN — Kazuya retreats from Ruka's sexual and relational pressure, and she stops rather than completing the anticipated act. | Both know the refusal; Ruka later frames sequence and patience as necessary. | One respected refusal does not neutralize the trial's coercive origin or future pressure. | RAG-E-V005-001, RAG-E-V005-002 |
| RAG-PRG-028 | Family exposure: Ruka prepares to reveal the rental truth | INTERRUPTION_AND_RECONFIGURATION — Nagomi's daughter-like attachment to Chizuru causes Ruka to preserve the secret and seek recognition instead. | Ruka gains new family-affect information; Nagomi remains uninformed. | Disclosure risk falls immediately but becomes a long contest rather than disappearing. | RAG-E-V005-006, RAG-E-V005-007 |
| RAG-PRG-029 | Employment: Kazuya has only begun work | GAIN — the job becomes routine, supplies first wages, exposes Kuribayashi's hurt, and funds a repair booking. | Work now has financial, relational, and logistical consequence. | Long-term competence remains underobserved, while Ruka's entry adds secrecy pressure. | RAG-E-V005-007, RAG-E-V005-008, RAG-E-V005-009 |
| RAG-PRG-030 | Honesty: Kazuya repeatedly plans but fails to disclose | BOUNDED_GAIN — he completes a direct confession to Kuribayashi about the rental-girlfriend deception. | Kuribayashi updates and accepts the apology; other audiences retain false beliefs. | The gain is durable for one friendship and cannot be generalized to family or Kibe. | RAG-E-V005-011 |
| RAG-PRG-031 | Chizuru collaboration: provider, neighbor, and deception partner | GAIN — she knowingly supports the Kuribayashi repair and privately recruits Kazuya for Sumi's practice date. | Both gain an off-platform coordination channel tied to paid work. | No mutual romance is acknowledged, and acting ambition receives no V005 consequence. | RAG-E-V005-012, RAG-E-V005-014 |
| RAG-PRG-032 | Mami trajectory: dormant after the missed meeting | REACTIVATION_SIGNAL — Mami sees Kazuya with Sumi and reacts in surprise. | Only observation is established at the boundary. | Her inference and action remain deferred to V006. | RAG-E-V005-017 |
| RAG-PRG-033 | Sumi practice: date begins under near-total communication failure | GAIN — supported activity, protection, role performance, a smile, and a spoken name create a small successful training arc. | Sumi, Kazuya, and reader observe the change; Chizuru later receives a favorable account. | One encounter does not establish stable communication or independent provider competence. | RAG-E-V006-001 through RAG-E-V006-004 |
| RAG-PRG-034 | Chizuru career: acting goal has not altered practical conditions | DELAYED_GAIN — a new opportunity leads her to consider retiring from rental work. | Kazuya learns that the relationship's commercial access route may end. | Opportunity and proposed exit are not completed outcomes. | RAG-E-V006-006, RAG-E-V006-007 |
| RAG-PRG-035 | Ruka relation: provisional and emotionally mismatched | FALSE_START — Kazuya begins an official-status proposal from duty and anticipated loss, then the workplace collision interrupts it. | Ruka receives evidence of possible conversion but no completed agreement. | Underlying nonreciprocity persists and must be revisited. | RAG-E-V006-009, RAG-E-V006-010 |
| RAG-PRG-036 | Mami trajectory: observation without known action | ESCALATION — research, paid access, and direct accusation turn observation into strategic intervention. | Mami and Chizuru exchange privileged relationship information; Kazuya overhears. | Mami's desired final state and response to Chizuru's challenge remain unknown. | RAG-E-V006-005, RAG-E-V006-008, RAG-E-V006-011, RAG-E-V006-013, RAG-E-V006-014 |
| RAG-PRG-037 | Kazuya attachment: conscious but private and appearance-heavy | GAIN_WITH_OPEN_RECEPTION — he distinguishes admiration of Chizuru's conduct from physical attraction and directly names her as his preference. | Kazuya and reader receive the full synthesis; Chizuru receives the final statement. | Her interpretation, reciprocation, and any relationship change remain unobserved. | RAG-E-V006-015, RAG-E-V006-016, RAG-E-V006-017 |
| RAG-PRG-038 | Kazuya communication | MIXED — he retreats under Chizuru's direct question, then later speaks plainly to Sayuri. | Audience and risk still govern communicative competence. | Chizuru still lacks his explicit love declaration. | RAG-E-V007-001, RAG-E-V007-015 |
| RAG-PRG-039 | Chizuru career | REGRESSION_THEN_RECOVERY — she loses a role and questions her talent, then resumes script work and rental income. | Persistence follows observable defeat. | Long-term career success remains unknown. | RAG-E-V007-003 through RAG-E-V007-006 |
| RAG-PRG-040 | Kazuya-Chizuru access | MATERIAL_GAIN_WITHOUT_STATUS — repeated paid bookings expand to an unbooked outing and family visit. | Chizuru initiates both forms of private access. | Mutual romantic status remains unacknowledged. | RAG-E-V007-011 through RAG-E-V007-013 |
| RAG-PRG-041 | Kazuya support | GAIN — work, bookings, privacy protection, and status-independent commitment make support more concrete. | Conduct now carries financial, bodily, and relational cost. | Paid access and continuing deception remain limits. | RAG-E-V007-005, RAG-E-V007-009, RAG-E-V007-016 |
| RAG-PRG-042 | Sumi communication and work | LIMITED_GAIN — she continues preparation and client work despite severe difficulty. | Supplemental evidence shows persistence and reflective concern. | Stable independent competence is not established. | RAG-E-V007-007 |
