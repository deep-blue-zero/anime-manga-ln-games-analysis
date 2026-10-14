---
title: "Silent Witch — SW Master Longitudinal Ledger"
artifact_id: SW_MASTER_LONGITUDINAL_LEDGER
artifact_type: master_longitudinal_ledger
series: "Silent Witch: Secrets of the Silent Witch"
series_id: silent-witch
generation: V1
version: "1.1"
last_updated: "2026-10-14"
status: canonical
scope: "Exclusive pre-split cumulative state; Japanese LN V01 closed and reconciled into every typed section"
source_boundary: "Japanese LN V01, witness SW-LNJP-V01, closed; no other source unit in any lane analyzed."
created: "2026-10-12"
canonical_home: "series/silent-witch/03 Longitudinal Ledgers/SW_MASTER_LONGITUDINAL_LEDGER.md"
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
do_not_use_as_literary_evidence: true
---

# Master longitudinal ledger

This is the single pre-split cumulative analytical home specified by [the architecture](../00%20Frameworks%20and%20Methods/SW_SYNTHESIS_ARCHITECTURE.md). The current entrypoint is [the corpus map](../CURRENT_STATE_AND_CORPUS_MAP.md). This file preserves cumulative meaning and revision history; volume readings own underlying diagnostic observations, and Drive owns raw source/locator derivatives.

## Actual initialization state

```yaml
longitudinal_state:
  state: V01_CLOSED
  committed_high_water_mark: V01
  analyzed_units: [SW-LNJP-V01]
  frozen_units: [SW-LNJP-V01]
  literary_observations: 132  # owned by the V01 reading: SW-E-LNJP-V01-001..132
  local_character_identities: 16
  character_models: 0
  readiness_assessments: 8  # evidence reviews SW-RD-0001..0008; no tier awarded
  claim_records: 18
  revision_records: 0
  prediction_records: 12  # open prospective questions SW-P-0001..0012; zero predictions registered
  split_ledger_paths: []
  sequential_analysis_lock: OPEN
  sequential_analysis_lock_scope: JAPANESE_LN_V01_ONLY
```

The initialization state, preserved here as history, was NO_SOURCE_UNIT_ANALYZED at PRE_V01 with every count at zero. Those zero records were truthful absence of analysis, not findings about the novel. The records below were appended at V01 closure on 2026-10-14 from the [V01 deep reading](../02%20Sequential%20Readings/SW_V01_DEEP_READING.md). They contain no simulated dialogue and no material from any later unit.

## Common record contract

Every source-bearing record carries: stable typed ID; continuity/witness/source unit; applicable diegetic interval and disclosure boundary; evidence class; canonical observation reference; exact evidence route; formulation; support; material counterevidence/rival explanation; uncertainty; created/updated boundary; and supersession/revision references where relevant.

Stable IDs are never renumbered. Source observation grammar is `SW-E-LNJP-V<NN>-<sequence>` for numbered LN units; the volume reading owns those IDs. Supplement/web IDs are separate. Local entity keys resolve only inspected identity evidence and are not global character enrollments.

The common fields apply to all sections. The following field lists define each section's additional exclusive responsibility; they are schemas, not populated rows.

**V01 record defaults.** Unless a row says otherwise, every V01 record has: continuity Japanese LN main track; witness and source unit `SW-LNJP-V01`; diegetic interval from three months after the Worgan dragon to one week after Thornley’s arrest; disclosure boundary V01; created and last updated at V01 closure, 2026-10-14; no supersession. The canonical observation reference is the `obs.` number in the [V01 reading](../02%20Sequential%20Readings/SW_V01_DEEP_READING.md#614-observation-register), meaning `SW-E-LNJP-V01-<nnn>`. The evidence route is that observation, then its locator, then the locally retained sealed locator package. Evidence classes use the method’s grammar abbreviated as OTE, CRB, NP, SI, WH, SP, NE, CON and UQ. Romanized names are analyst conveniences.

**Local identities at V01.** These keys resolve inspected identity only and are not global enrollments.

| Local key | Japanese name and aliases in V01 | Identity notes |
|---|---|---|
| sw.monica | モニカ・エヴァレット; 〈沈黙の魔女〉; cover name モニカ・ノートン; 同期殿, 子リス, ノートン会計 | One person under two names; the cover is known to her confidants only. |
| sw.felix | フェリクス・アーク・リディル; 第二王子; 生徒会長; マスター to his spirit | Prologue watcher identification is inference only, SW-C-0006. |
| sw.louis | ルイス・ミラー; 〈結界の魔術師〉 | — |
| sw.cyril | シリル・アシュリー; 生徒会副会長; adopted son of the ハイオーン marquisate | — |
| sw.nero | ネロ; human-form alias バーソロミュー・アレクサンダー | Nature undisclosed. |
| sw.lynn | リィンズベルフィード; リン | Wind upper spirit. |
| sw.wildianu | ウィルディアヌ; ウィル | Water upper spirit contracted to Felix. |
| sw.isabelle | イザベル・ノートン; ケルベック伯爵令嬢 | — |
| sw.lana | ラナ・コレット | — |
| sw.elliott | エリオット・ハワード | — |
| sw.bridget | ブリジット・グレイアム | — |
| sw.neil | ニール・クレイ・メイウッド | — |
| sw.thornley | ヴィクター・ソーンリー | Removed from the school at V01. |
| sw.selma | セルマ・カーシュ | Removed at V01. |
| sw.aaron | アーロン・オブライエン | Removed at V01. |
| sw.rosalie | ロザリー・ミラー | — |

## 1. Character state and speech — SW-S

Owns source-bearing character changes, role constraints, ordinary behavior, self-conception and written-speech conditioning.

Fields: local key; name/title/address alias and scope; state before; represented perception/appraisal/affect; options; action/speech; consequence; state after; change kind; persistent feature; persona/private distinction; audience/recipient; register/address/silence feature; diagnostic ordinary-life basis.

Change kinds: DISPOSITION_CHANGE, KNOWLEDGE_CHANGE, ROLE_CONTEXT_CHANGE, RELATIONSHIP_CHANGE, REVEALED_NOT_NEW, UNRESOLVED. A knowledge-change summary links to SW-K for proposition ownership. A relational effect links to SW-R.

Records at V01:

| ID | Key | State before → after | Kind | Process: perception → appraisal/affect → options → act/speech → consequence | Persona/private; recipient; register | Obs. | Class | Rival; uncertainty |
|---|---|---|---|---|---|---|---|---|
| SW-S-0001 | sw.monica | Baseline at entry: recluse by preference; underfed; numbers as work and comfort; believes herself a makeweight Sage. | REVEALED_NOT_NEW | Legend heard → stomach pain, sweat → hide → stammered evasions → secret kept by others’ assumptions. | Public legend vs private recluse; polite stammer to humans, plain to Nero. | 004, 005, 006, 013, 016 | NP, CRB | R: preference for solitude rather than fear. U: none material. |
| SW-S-0002 | sw.monica | Chantless casting understood as avoidance turned mastery; can only cast silently, so any magic exposes her. | REVEALED_NOT_NEW | Exam fear → cannot chant → remove the chant → mastery → title. | Constraint operates at school in every scene. | 007, 008, 033 | NP | R: talent independent of cause. U: deeper origin, see SW-S-0004. |
| SW-S-0003 | sw.monica | Pain, fear or exposure produce absorption in numbers. | REVEALED_NOT_NEW | Threat or pain → fear → numerical refuge → reduced awareness → comic or productive outcome. | Song series, lashes, ledgers; narrated in hiragana once. | 014, 037, 071, 072, 085 | NP | R: habit of mind only. U: none; narrator states it. Links SW-C-0002. |
| SW-S-0004 | sw.monica | Associative evidence of past harm: dream of a drinking man, a bottle and a silence rule; head-covering flinch; fear of an adult male form; rank makes truth; refusal to let others be falsely accused. | REVEALED_NOT_NEW; UNRESOLVED | Raised hand → expects a blow → covers head; injustice to another → forces speech. | Not narrated as memory, only as dream and reflex. | 037, 040, 057, 058, 059 | SI, UQ | R: dream distortion and startle. U: who, when, how often. Links SW-C-0003. |
| SW-S-0005 | sw.monica | From reflexive nod and failed greeting to thanks, requests, chosen tasks, a completed false-name introduction, an accusation, plain speech to a friend. | DISPOSITION_CHANGE, provisional | Repeated: fear → recalled duty or care → speech act forced out → recognized or rebuffed. | Fluent with non-humans, in proof, in anger at formulas, in writing; breaks on self-reference. | 041, 045, 053, 059, 087, 104, 112, 114, 115 | OTE | R: role pressure, not disposition. U: generalization to strangers untested; SW-P-0012. |
| SW-S-0006 | sw.monica | Hermit Sage → student Monica Norton under Kerbeck cover → council treasurer with public badge. | ROLE_CONTEXT_CHANGE | Coerced acceptance → cover lived → competence displayed → appointment she cannot refuse. | Cover known to confidants; badge as public marking. | 011, 012, 074, 075, 084, 114 | OTE | R: none. U: none. |
| SW-S-0007 | sw.monica | Learns that an authority can investigate instead of deferring to rank. | KNOWLEDGE_CHANGE | Expected rank to decide → Cyril’s inquiry → surprise. | — | 058, 091 | OTE, NP | R: Cyril is an exception. U: whether expectation generalizes. Links SW-K-0014. |
| SW-S-0008 | sw.monica | Self-worth unchanged: cannot be proud; talent is a curse that took father and friend; claims no attachment to people while acting on attachments. | UNRESOLVED | Praise or challenge → refusal of pride; others’ need → anonymous care. | Report reduces achievements to “various things happened”. | 026, 066, 089, 090, 093, 101, 115 | CRB, NP | R: accurate self-report about romance only. U: father’s case. Links SW-C-0014. |
| SW-S-0009 | sw.felix | Public persona of perfect courtesy and command; private 僕, game vocabulary, life as remainder; wish withheld. | REVEALED_NOT_NEW | — | 私 public, 僕 private; さて as dominance. | 020, 023, 062, 078 | OTE, NP | R: affectation. U: reason for the remainder. |
| SW-S-0010 | sw.felix | Strategic actor: year-long trap for Aaron; key test; lies to council and to Elliott; destroyed Louis’s brooch; hides magic literacy and spirit. | REVEALED_NOT_NEW | Threat or puzzle → test or trap → concealment. | Kindness and calculation coincide in act. | 069, 074, 077, 079, 121 | OTE | R: prudent ruler-in-training. U: aims. |
| SW-S-0011 | sw.felix | Model of Monica: not a civilian; purpose unknown; too incompetent to be the king’s; amusing because indifferent to him. | KNOWLEDGE_CHANGE | Observes oddities → tests → appoints to keep near. | Pet lexicon toward her. | 063, 069, 078 | OTE | R: interest beyond the game. U: open. Links SW-K-0004. |
| SW-S-0012 | sw.felix | Rapt devotion to the Silent Witch in the abstract. | REVEALED_NOT_NEW | — | Warms and flushes describing her. | 003, 024, 122 | OTE, SI | R: idealization only. U: watcher identity, SW-C-0006. |
| SW-S-0013 | sw.cyril | Loyal to Felix to the point of violence; scrupulous procedure; needs recognition; adopted, with an unsaid sentence to his mother. | REVEALED_NOT_NEW | Disrespect to Felix → rage; injury → care first; incident → inquiry. | 私; stiff archaic register; hyperbolic oaths. | 057, 080, 091, 095, 096 | NP, OTE | R: none. U: object of elided wish. |
| SW-S-0014 | sw.cyril | Memory altered after noticing the slant; constitution crisis from brooch malfunction; treated without knowing it; remembers a monster. | KNOWLEDGE_CHANGE (unaware) | Notices evidence → erased → crisis → exhausted by an unknown mage. | — | 081, 098, 099, 103 | OTE, NP | R: none. U: whether memory returns. |
| SW-S-0015 | sw.cyril | Toward Monica: hostility for disrespect → professional recognition; private unverified suspicion from her hand. | RELATIONSHIP_CHANGE | Work observed → judgment revised → introduces her by office. | Office title ノートン会計. | 080, 111, 114 | OTE, SI | R: curiosity only about the hand. U: what he concludes. Links SW-R-0011. |
| SW-S-0016 | sw.louis | Coercive politeness; mock-scriptural motto; ear-pinching; doting husband. | REVEALED_NOT_NEW | Need → coerce with charm and threat. | 私; 同期殿; imperatives under pressure. | 009, 010, 011, 094 | OTE | R: none. U: none. |
| SW-S-0017 | sw.louis | Beaten by Monica at selection; regards her as a monster in power; wants her confident; reads the order as surveillance; planted a disciple. | REVEALED_NOT_NEW | — | Private candour with Lynn. | 116, 117, 118, 119 | CRB | R: self-serving memory. U: examiners’ view. Links SW-C-0017. |
| SW-S-0018 | sw.nero | Talking familiar; reads novels; senses magic; shapeshifts; strong; dislikes cold; knows her fear responses; hides the kiss from her; vows to protect her. | REVEALED_NOT_NEW | — | オレ様; garbles human names. | 041, 072, 076, 102 | OTE, CRB | R: none. U: nature, SW-C-0013. |
| SW-S-0019 | sw.isabelle | Brave heir in the prologue; theatrical villainess; devoted collaborator; effective tactician. | REVEALED_NOT_NEW | — | わたくし; お姉様; persona switching. | 018, 019, 025, 128 | OTE | R: none. U: none. |
| SW-S-0020 | sw.lana | Brusque new-money baron’s daughter, herself mocked; becomes Monica’s first friend. | RELATIONSHIP_CHANGE | Scorn → grooming → shared wound → apology → pride. | わたし; 貴女 → モニカ. | 031, 046, 047, 083, 112 | OTE | R: uses Monica as audience. U: low. |
| SW-S-0021 | sw.thornley | Contemptuous elite teacher; wounded by Monica’s published work; organized embezzlement; used restricted magic; removed. | ROLE_CONTEXT_CHANGE | Exposure threat → erase witnesses → confronted → sealed in dream. | たまえ/かね register. | 029, 051, 104, 105, 107, 108, 109 | OTE, CRB | R: none. U: none material. |
| SW-S-0022 | sw.elliott | Vigilant guard of Felix; trap-setter; contempt for presumptuous commoners; unaccepting of Monica. | REVEALED_NOT_NEW | — | 俺; flippant over contempt. | 036, 061 | OTE | R: none. U: none. |
| SW-S-0023 | sw.bridget | Cold, exacting, strikes Monica with a fan; unaccepting. | REVEALED_NOT_NEW | — | あたくし; お前. | 070 | OTE | R: none. U: thin. |
| SW-S-0024 | sw.selma | Devotion without return; over-confession; manipulated on Monica’s inference; removed. | ROLE_CONTEXT_CHANGE | — | 私. | 064, 065 | OTE, CRB | R: own initiative. U: instigator identity rests on inference. |

## 2. Directional relationships and obligations — SW-R

Owns A-to-B relationship change; B-to-A is separate even within a shared episode.

Fields: actor; recipient; relation/role; actor's aim; trust/disclosure state before/after; obligation origin/terms; initiative/refusal; dependency/resources/power; concealment or disclosure act; conflict/repair; independent goals; reciprocity assessment; linked knowledge/state IDs.

Attraction, affection, loyalty, duty, dependence and understanding are separate variables. No romance score or assumed mutuality is stored.

Records at V01:

| ID | Actor → recipient | Relation and actor’s aim | Trust and disclosure, before → after | Obligation, power, initiative | Concealment, conflict, repair | Reciprocity; independent goals | Obs. |
|---|---|---|---|---|---|---|---|
| SW-R-0001 | Monica → Louis | Junior Sage; avoid his anger; complete the task. | Fear with trust in his competence → unchanged; goodwill to his family. | Obeys under coercion; reports in writing. | She privately reads his motives correctly. | Asymmetric; her goal is to survive the year. | 009, 011, 094 |
| SW-R-0002 | Louis → Monica | Uses her as an incongruous instrument; wants her confident. | Respect hidden behind insult. | Holds the king’s mandate and the power of choice; feeds her sweets. | Conceals his disciple and his reading of the order. | Asymmetric; his goals include his own pride and the king’s business. | 010, 011, 116, 117, 118, 119 |
| SW-R-0003 | Monica → Nero | Comfort; candour. | Full trust → unchanged. | Dependent for comfort and errands. | Unaware he withholds the kiss. | Mutual in care. | 039, 041 |
| SW-R-0004 | Nero → Monica | Teasing protector; calls her his favourite. | — | Volunteers; vows violence against anyone who breaks her. | Withholds the kiss; hides his own nature from others. | Possessive; own goals undisclosed. | 072, 076, 102 |
| SW-R-0005 | Monica → Isabelle | Grateful, bewildered; defers though older. | Low → grateful acceptance. | Receives protection by staged cruelty. | Worries for Isabelle’s reputation. | Unequal in enthusiasm. | 018, 025, 082 |
| SW-R-0006 | Isabelle → Monica | Adoration; collaborator in the cover. | Knows identity from the start. | Initiates every intervention. | Performs cruelty as care. | Her own enjoyment of the role. | 019, 025, 128 |
| SW-R-0007 | Monica → Lana | First friendship; wants to be liked; plain speech by exit. | Fear → trust; fears losing her over the post. | Initiates a request to be taught. | Does not disclose identity. | Becoming mutual. | 045, 046, 082, 083, 112 |
| SW-R-0008 | Lana → Monica | Brusque care; pride in her braiding. | Scorn → friendship. | Teaches, routes her round crowds, apologizes. | — | Lana has her own outsider wound. | 031, 047, 055, 083 |
| SW-R-0009 | Monica → Felix | Ward to be guarded; fear of proximity and rank. | Thanks him, avoids him. | Cannot refuse his assignments. | Unaware of his tests, kiss and devotion to her other self. | No romantic interest shown. | 048, 075, 085, 113 |
| SW-R-0010 | Felix → Monica | Suspect, pet, game; useful accountant. | Suspicion without fear → keeps her close. | Rank and charm; stakes his office on her. | Tests her; conceals much; kisses her cheek. | Asymmetric; his aims withheld. | 036, 063, 069, 073, 075, 078, 088 |
| SW-R-0011 | Monica → Cyril | Fear of his temper; admiration of his striving. | Fear → admiration. | Accepts his training. | Anonymous treatment and brooch repair. | One-sided care; he does not know. | 089, 101, 114 |
| SW-R-0012 | Cyril → Monica | Hostility for disrespect to Felix → professional recognition. | Distrust → qualified respect; private suspicion. | Supervises, investigates on her behalf. | Nearly checks her hand; interrupted. | Developing; his goal is Felix’s and his family’s approval. | 057, 080, 091, 111, 114 |
| SW-R-0013 | Felix → Cyril | Trusts his fairness; protects him. | — | Assigns him to Monica deliberately. | Hides his spirit from him. | Partial disclosure only. | 103, 120 |
| SW-R-0014 | Cyril → Felix | Devoted loyalty; seeks recognition. | Total trust. | Defends him with force. | Unaware of Felix’s secrets. | Asymmetric knowledge. | 023, 096 |
| SW-R-0015 | Felix → Elliott | Uses his vigilance. | — | Lies to him about the night. | — | Partial disclosure. | 079 |
| SW-R-0016 | Elliott → Felix | Watchful friend; resents solo risks. | — | Sets traps on his behalf. | — | — | 036, 061 |
| SW-R-0017 | Felix → Duke Clockford | Grandson and dependant. | — | States he cannot defy the duke. | Removes the duke’s placements. | Conflict concealed. | 062, 120 |
| SW-R-0018 | Louis → Felix | Watcher; finds him uncanny. | Distrust. | King’s mandate. | Surveillance brooch disguised as a father’s gift. | Opponents. | 009, 119 |
| SW-R-0019 | Felix → Louis | Believes Louis watches him; resents theft of his prey. | Distrust. | Destroyed the brooch. | Hides his literacy. | Opponents; misattributes the arrest. | 120, 121 |
| SW-R-0020 | Thornley → Monica | Contempt → terror and recognition. | — | Attempted erasure and destruction of her mind. | — | Ended by arrest. | 104, 107 |
| SW-R-0021 | Selma → Aaron | Devotion without return. | — | Committed crimes for him. | — | Not reciprocated. | 064, 065 |
| SW-R-0022 | Lynn → Louis | Service without reverence. | — | Courier and transport. | — | — | 094, 117 |

## 3. Chronology and epistemic state — SW-K

Owns proposition-specific participant/reader knowledge and event/revelation order.

Fields: proposition ID/formulation; event and disclosure anchors; order/date certainty; knower/attributing observer; knowledge/belief/suspicion/ignorance status; evidence available to that knower; truth assessment separately; prior/current state; source of change; withheld/false information; continuity conflict.

One character's known proposition cannot be inherited by all participants. Uncertain dates remain uncertain. Event order may be partial; no invented complete calendar is required.

Records at V01:

| ID | Proposition | Anchors | Knower: status | Truth assessment | Change source; withheld information | Obs. |
|---|---|---|---|---|---|---|
| SW-K-0001 | Relative chronology: Worgan dragon in late summer; three months later Louis’s visit; arrival day with Aaron’s trial and the signboard; school day 1 flowerpot and night sighting; day 2 proof, staircase, Selma, appointment, Cyril’s erasure that evening; day 3 badge, Cyril’s crisis, Thornley’s arrest; one week later epilogue and secret episode. Mission term about one year. | S15:E000033; S15:E000169; S15:E000661; S25:E000173 | Reader | Partial order; no calendar dates. | — | 001, 022, 081, 115 |
| SW-K-0002 | Monica Norton is the Silent Witch. | S15:E000351 | Monica, Nero, Louis, Lynn, Isabelle and household: know. Thornley: guessed, in custody. Cyril: suspects. Felix, council, Lana, school: do not know. | True. | Rosalie was not told at her examination. | 107, 111, 122 |
| SW-K-0003 | Monica’s mission is to guard the second prince. | S15:E000578 | Monica, Louis, Lynn, Isabelle, Nero: know. Felix: purpose unknown to him. | True as stated order. | — | 069 |
| SW-K-0004 | Monica is an agent of the king. | S21:E000347 | Felix: considered and rejected as she is too incompetent. | True in substance. | Felix’s model, SW-S-0011. | 069 |
| SW-K-0005 | The order’s real intent is surveillance. | S27:E000253 | Louis: believes. Monica: suspects a hidden purpose. | Unverified; king not shown. | — | 034, 119 |
| SW-K-0006 | Louis has planted a disciple in the academy. | S27:E000069 | Louis, reader: know. Monica: does not. | True per Louis. | Identity withheld. | 116 |
| SW-K-0007 | Felix holds an upper-spirit contract and knows magic. | S21:E000321; S27:E000367 | Felix, Wildianu, Nero, reader: know. Cyril, council, Monica: do not. Louis: senses something. | True. | Concealed even from Cyril. | 069, 102, 121 |
| SW-K-0008 | Felix’s night outing was a decoy operation. | S19:E000526; S21:E001056 | Elliott, Monica: believe. Felix: knows it false. | False. | Purpose withheld. | 079 |
| SW-K-0009 | Felix knew of Aaron’s fraud for a year. | S21:E000994 | Felix, Wildianu, reader. Council: told otherwise. | True. | — | 074, 077 |
| SW-K-0010 | Felix kissed Monica’s cheek. | S21:E000687 | Felix, officers present, Nero, reader: know. Monica: does not. | True. | Nero withholds it. | 073, 076 |
| SW-K-0011 | Thornley organized the embezzlement and erased Aaron’s and Cyril’s memories. | S24:E000556; S24:E000573 | Monica, Louis, Lynn, council, public via press: know of the crimes. Cyril: unaware of his own erasure. | True per culprit’s own dream. | — | 108 |
| SW-K-0012 | Thornley manipulated Selma. | S24:E000282; S27:E000030 | Monica: infers and reports. | Inference; culprit’s account silent. | Instigator of Selma’s phrase unnamed in her section. | 064, 108 |
| SW-K-0013 | Monica arrested Thornley. | S24:E000641; S27:E000340 | Monica, Lynn, Louis: know. Felix, public: credit Louis. | True. | Misattribution arranged by Louis’s leak. | 120 |
| SW-K-0014 | Authorities may investigate rather than defer to rank. | S22:E000902 | Monica: learns from Cyril. | True for Cyril. | — | 091 |
| SW-K-0015 | Monica treated Cyril in the forest. | S23:E000676 | Monica, Nero, Lynn: know. Cyril: remembers a monster. Felix: told it was a tall man. | True. | — | 098, 103 |
| SW-K-0016 | Louis was beaten by Monica in the selection duel. | S27:E000225 | Louis: remembers. Monica: participant who interprets her selection as pity. | True per Louis. | Examiners’ view unstated. | 013, 117 |
| SW-K-0017 | Felix destroyed Louis’s brooch himself. | S27:E000363 | Felix, Wildianu, reader. Louis: does not know the cause. | True. | — | 121 |
| SW-K-0018 | Monica’s father is dead; she was adopted by his pupil. | S18:E000278 | Monica, reader. | True. | Names, cause and the pupil’s identity withheld. | 032, 090 |
| SW-K-0019 | Thornley’s pride was wrecked by Monica’s published formula. | S24:E000518 | Thornley. Monica: unaware. | True per Thornley. | — | 107 |
| SW-K-0020 | Nero is non-human and probably not a spirit. | S24:E000195 | Felix: intuits. Monica: knows Nero’s abilities. | Undetermined. | Nature withheld. | 102 |

## 4. Institutions, world and magic — SW-W

Owns cumulative operational world/institution claims and their exceptions.

Fields: domain; stated rule/doctrine; asserting source position; demonstrated operation; conditions/costs/resources; exception/failure; enforcement versus nominal rule; role/political/material constraint; mathematical or magical reasoning basis; current formulation; competing causal model; linked chronology/claim IDs.

Character explanation, institutional belief, observed mechanism and universal law remain distinguishable. A single successful demonstration does not prove an unlimited rule.

Records at V01:

| ID | Domain | Current formulation | Asserting source | Demonstration; conditions and costs | Exceptions; open points | Locators |
|---|---|---|---|---|---|---|
| SW-W-0001 | Chanting | Humans must chant to shape magical power; formulas are woven by chant. | Narrator rule | Every human caster except Monica chants. | — | S15:E000357–E000358 |
| SW-W-0002 | Shortened chant | Shortened chanting halves the time but still takes seconds. | Narrator | Cyril, S17:E000447–E000448. | — | S15:E000362; S15:E000370 |
| SW-W-0003 | Chantless casting | Monica alone in the world; about eight in ten formulas; one reason she was chosen. | Narrator | Repeated throughout. | Which formulas resist is unstated. | S15:E000363–E000371 |
| SW-W-0004 | Spirits | Spirits need neither chant nor formula; have far more power; upper spirits contracted by about ten mages nationally. | Narrator | Lynn’s barrier and flight; Felix’s lizard. | — | S15:E000358; S15:E000432; S16:E000043 |
| SW-W-0005 | Spirit kinds | Lynn is wind and excels at flight; Wildianu is water and excels at illusion, weak at sensing. | Narrator | Transport; failed spying on Nero. | — | S23:E000197; S24:E000231 |
| SW-W-0006 | Spirit-king summoning | Few in the kingdom can summon a spirit king; Sheffield is the wind spirit king. | Narrator in Isabelle’s view | Prologue wyverns. | — | S12:E000008–E000009 |
| SW-W-0007 | Elements | People have an innate favoured element; many mages use only that one. | Nero’s judgment | Cyril ice-only per Nero; Monica multi-element. | Nero’s claim, not narrator law. | S24:E000027–E000028 |
| SW-W-0008 | Flight | Requires fine control and physical ability; upper-mage level; drains in about half an hour. | Narrator; Nero | Monica cannot fly. | — | S16:E000041; S23:E000194–E000195; S24:E000023–E000025 |
| SW-W-0009 | Mana in the body | Limited capacity; magic-made water carries power; excess causes poisoning; Sages tolerate more; casting consumes energy and mages favour sweets. | Narrator | Monica drinks a little magic water; flags after heavy casting. | — | S19:E000053–E000058; S25:E000049 |
| SW-W-0010 | Over-absorption | Absorption continues past capacity; must vent; five severity grades; early poisoning brings elation, later hallucination; treat by exhausting power; can be cultivated for faster recovery. | Narrator and Monica | Cyril’s crisis and treatment. | — | S23:E000262–E000269; S23:E000395; S23:E000677–E000678; S23:E000745–E000749 |
| SW-W-0011 | Magic tools | Treated gems carry formulas; usable by non-mages; very expensive; a protective formula normally guards the working formula; without it strong attack can cause misfire. | Narrator and Monica | Louis’s brooch; Cyril’s brooch reversed. | — | S15:E000501–E000506; S23:E000696–E000699 |
| SW-W-0012 | Enchantment | Imbuing objects is enchantment; Monica can rewrite a simple tool though not trained in it. | Narrator | Brooch repair. | — | S23:E000724–E000732 |
| SW-W-0013 | Spell interference | Interfering with another’s formula requires far superior skill and is wildly improper. | Narrator | Monica unpicks and reweaves Thornley’s spell. | — | S24:E000460–E000467 |
| SW-W-0014 | Mind interference | Restricted art; permitted for interrogating grave criminals or national emergency with authorization of the mages’ guild or the Seven Sages; side effects memory loss, derangement, unconsciousness; misuse costs the licence; completed form is butterfly-shaped. | Monica; narrator; old grimoires reported | Aaron, Selma, Cyril; Monica’s butterflies. | Whether a Sage may self-authorize is unresolved. | S17:E000562–E000571; S24:E000267–E000268; S24:E000495; S24:E000610 |
| SW-W-0015 | Sight magic | Far-sight and night-sight are not see-through and need line of sight. | Narrator | Night sighting from the attic. | — | S18:E000731 |
| SW-W-0016 | Seven Sages | Apex mages; staff as tall as the bearer; count-equivalent magic-count title; royal advisers; socially prominent. | Narrator; characters | — | — | S12:E000041–E000042; S16:E000221; S25:E000216 |
| SW-W-0017 | Sage selection | Two years ago one vacancy became two through a further illness; interview and attack-only duel; examiners named no ranking. | Monica; Louis | — | Examiners’ view unstated. | S15:E000835; S27:E000204–E000212 |
| SW-W-0018 | Named Sages | Barrier, Silent, Star-reading, Thorn, Cannon, Jewel; the Jewel Mage is a second-prince partisan whom Louis despises. | Characters | — | Seventh unnamed. | S25:E000218; S23:E000713–E000716 |
| SW-W-0019 | Mage institutions | Minerva trains mages; a mages’ guild licenses and disciplines; the magic corps employs upper mages; magic was once a noble monopoly. | Narrator | Thornley handed to the guild. | — | S15:E000159–E000164; S17:E000030–E000032; S27:E000053 |
| SW-W-0020 | Peerage | Duke, marquis, count, viscount, baron; lesser gentry below; dukes are royal kin; titles above count used as styles. | Louis | — | — | S16:E000177; S16:E000206 |
| SW-W-0021 | Succession | Three princes by different mothers; no heir named; second prince’s faction strongest with the duke’s backing. | Monica’s hearsay; Caroline’s belief | — | Character beliefs only. | S15:E000447–E000458; S21:E000403–E000412 |
| SW-W-0022 | Serendia Academy | Royal elite school under the duke; three great schools; donations buy privileges; council appointed by its president and bought through the duke; ledgers mismanaged for decades; dining tasted for poison. | Narrator; characters | Attic, appointments, ledgers. | — | S17:E000017–E000046; S17:E000110; S18:E000246; S24:E000328 |
| SW-W-0023 | Rank as truth | In the school’s practice a higher-ranked accuser decides truth; Cyril’s inquiry is a counterexample. | Monica’s knowledge; Cyril’s act | Staircase case. | Scope of the counterexample. | S20:E000423; S22:E000902 |
| SW-W-0024 | Dragons | Calamities; colour-named kinds superior and black worst; weak points between the eyes and in the eyes; wyverns flock around a greater dragon; Kerbeck guards the east. | Isabelle’s knowledge; Annie; narrator | Prologue. | — | S10:E000015–E000037; S10:E000097–E000156; S15:E000193–E000196 |

## 5. Load-bearing claims and revision history — SW-C / SW-CR

SW-C owns the current bounded formulation and its retrieval route. Fields: claim ID; question/domain; formulation; source/knowledge range; class; support; counterevidence; alternatives; confidence and reason; current transition/state; discriminating observation; dependent artifacts/IDs; revision references.

SW-CR owns append-only change events. Fields: revision ID; claim ID; earlier formulation and boundary; transition; new formulation and boundary; new support/counterevidence; reason; affected homes; correction versus later reinterpretation; date/reviewer. Allowed transitions:

| Transition | Meaning |
|---|---|
| PRESERVE | Material formulation retained after review. |
| STRENGTHEN | Same formulation receives stronger independent support. |
| REVISE | Wording, scope or mechanism materially changes. |
| DOWNGRADE | Confidence or warranted scope decreases. |
| REJECT | Claim is contradicted sufficiently to cease being accepted. |
| OPEN | Discriminating evidence remains insufficient or conflicting. |

An initial claim has no invented predecessor. It may begin OPEN or another justified initial assessment; a revision event requires an actual previous formulation. Preserve rejected claims for provenance rather than deleting their IDs. Normative criteria are explicit and separate from evidence confidence.

Claim records at V01:

| ID | Question | Formulation | Range; class | Support | Counterevidence; alternatives | State; confidence | Discriminating observation | Dependents |
|---|---|---|---|---|---|---|---|---|
| SW-C-0001 | Origin of the silence | Chantless casting began as avoidance of speech; silence and mastery are one mechanism. | V01; NP, SI | obs. 007, 033 | Talent may exceed the cause; deeper origins, SW-C-0003. | Initial assessment: supported, with a second V01 observation; high. | Disclosure of earlier training history. | SW-S-0002 |
| SW-C-0002 | Fear response | Pain, fear or exposure drive Monica into numerical absorption. | V01; NP | obs. 014, 037, 071, 072, 085 | Habit rather than defence. | Established; high. | Scenes where fear does not produce it. | SW-S-0003; SW-F-0006 |
| SW-C-0003 | Past harm | V01 supplies associative evidence of past harm by a drinking adult man she called おじさん, linked to a learned rule of silence. | V01; SI for existence, UQ for identity | obs. 037, 040, 057, 058, 059 | Dream distortion; startle reflex. | OPEN for identity; moderate for existence. | Backstory disclosure naming the man. | SW-S-0004; SW-P-0005 |
| SW-C-0004 | Selection | The makeweight self-assessment is contradicted by Louis’s memory of the duel; the examiners’ ranking is unstated. | V01; CRB | obs. 013, 117 | Louis’s memory may be self-serving. | OPEN on examiners; high that her belief lacks support. | Any examiner’s statement. | SW-S-0008; SW-K-0016 |
| SW-C-0005 | Mission purpose | Stated protection; Monica doubts it; Louis reads surveillance; king unshown. | V01; CRB | obs. 034, 119 | Protection and surveillance may coexist. | OPEN. | King or royal agent on stage. | SW-K-0005; SW-P-0007 |
| SW-C-0006 | The watcher | The prologue’s unnamed watcher is Felix. | V01; SI | obs. 003, 024, 122 | Another blue-eyed noble. | Strong inference, unstated. | Explicit narration or Felix’s recollection. | SW-S-0012 |
| SW-C-0007 | Felix’s divergence | Public and private selves diverge; he removes the duke’s placements while professing he cannot defy him. | V01; OTE, SI | obs. 020, 062, 077, 078, 120 | Prudence rather than resistance. | Observation established; motive OPEN. | Felix’s wish disclosed. | SW-S-0009; SW-S-0010 |
| SW-C-0008 | Recognition by Felix | Felix has not identified Monica as the Silent Witch. | V01 exit; OTE | obs. 069, 122 | — | Established at V01. | Felix witnessing her magic. | SW-P-0003 |
| SW-C-0009 | Recognition by Cyril | Cyril holds an unverified suspicion from her hand and remark. | V01 exit; SI | obs. 111 | Idle curiosity. | Strong inference. | Cyril acting on it. | SW-P-0004 |
| SW-C-0010 | Form of power | Monica’s power is narrated through external focalizers; her own viewpoint narrates fear, comedy and small uses. | V01; SI | obs. 002, 056, 098, 106, 117 | The staircase is narrated in her view with the narrator’s praise. | Established for V01. | A later scene of awe in her own viewpoint. | SW-F-0001 |
| SW-C-0011 | Rank and truth | The school treats rank as epistemic authority; Cyril’s inquiry is the first counterexample and revises her expectation. | V01; OTE, NP | obs. 058, 091 | Cyril’s fairness may be exceptional. | Established. | Further authorities’ conduct. | SW-W-0023; SW-S-0007 |
| SW-C-0012 | Thornley’s crimes | Organized embezzlement; erased Aaron’s and Cyril’s memories; Selma’s manipulation inferred. | V01; CRB, OTE | obs. 022, 081, 108 | Selma acted alone. | Aaron and Cyril established; Selma inferred. | Thornley’s interrogation results. | SW-K-0011; SW-K-0012 |
| SW-C-0013 | Nero’s nature | Neither an ordinary cat nor, in Felix’s judgment, a spirit. | V01; CRB | obs. 072, 102 | Unusual familiar spirit. | OPEN. | Disclosure of origin. | SW-P-0008 |
| SW-C-0014 | Talent as curse | Monica regards her talent as a curse that took her father and friend; her care for Cyril projects this. | V01; CRB, NP | obs. 090, 101 | — | Established as belief; father’s case OPEN. | Account of the father’s death. | SW-S-0008 |
| SW-C-0015 | Friendship | The bond with Lana rests on a shared experience of being called boring. | V01; OTE | obs. 031, 046, 083, 112 | Convenience on Lana’s side. | Established. | Disclosure strain. | SW-R-0007; SW-R-0008 |
| SW-C-0016 | Comedy and harm | The comedy of coercion registers harm in most cases; the non-consensual kiss is unevaluated and unknown to its recipient. | V01; NE | obs. 010, 073, 076, 092 | The narration treats it as harmless play. Criterion: whether effect on the affected person is registered independent of tone. | Recorded. | Any later revisiting. | SW-F-0008 |
| SW-C-0017 | Louis’s stance | Coercion combined with investment in her self-respect and his own pride. | V01; CRB, SI | obs. 011, 117, 118 | Pure self-interest. | Established by the secret episode. | Louis acting against her interests. | SW-S-0017 |
| SW-C-0018 | Source of perception | Monica’s numerical perception and comfort derive from her father’s teaching. | V01; NP | obs. 026, 043, 044 | Innate disposition. | Established. | — | SW-S-0001 |

Revision records: none. Every V01 claim is an initial formulation with no predecessor.

## 6. Prospective questions and predictions — SW-P

Owns genuine prospective tests and open questions across source-unit boundaries.

Fields: ID; frozen wording; preparation boundary/reference; basis observations/claims; target opportunity; expected outcome if any; falsifying/weakening outcome; confidence basis; test status; eligible adjudicating observations; result/revision route.

Statuses: OPEN, TESTED_SUPPORTED, TESTED_COMPLICATED, TESTED_DISCONFIRMED, UNTESTED, or RETIRED_WITH_REASON. An open question needs no predicted answer. An absent opportunity is UNTESTED; a remembered later event is never a newly frozen prediction.

Records at V01. All were frozen at V01 closure on 2026-10-14 in the reading’s section 9.2. None carries a predicted answer: the entry freeze registered no predictions because of disclosed prior franchise exposure, and the same reason applies at exit.

| ID | Frozen wording | Basis | Target opportunity | Expected outcome | Weakening outcome | Status |
|---|---|---|---|---|---|---|
| SW-P-0001 | Who is the disciple Louis planted in the academy, and does Monica learn of it? | obs. 116 | A Louis-connected student or disclosure. | None. | — | OPEN |
| SW-P-0002 | What is Felix’s wish, why is his life a remainder, and where does he go at night? | obs. 078, 079 | Felix viewpoint scenes. | None. | — | OPEN |
| SW-P-0003 | Will Felix connect Monica with the Silent Witch, and what would force it? | obs. 069, 122 | Felix witnessing or hearing of her magic. | None registered; see the bounded expectation in the reading’s section 10, which is not a prediction. | — | OPEN |
| SW-P-0004 | Will Cyril verify his suspicion about her hand? | obs. 111 | Repeat of the glove scene; confrontation. | None. | — | OPEN |
| SW-P-0005 | Who was the man in the dream; what happened to her father; how did talent take him? | obs. 037, 090 | Backstory disclosure. | None. | — | OPEN |
| SW-P-0006 | Who is the Minerva friend; does he return? | obs. 090 | A Minerva acquaintance appears. | None. | — | OPEN |
| SW-P-0007 | What does the king intend, and what grounds the duke’s hold on Felix? | obs. 062, 119 | King or duke on stage. | None. | — | OPEN |
| SW-P-0008 | What is Nero? | obs. 102 | Disclosure of origin or powers. | None. | — | OPEN |
| SW-P-0009 | Does Monica’s use of mind interference have consequences? | obs. 110 | Guild or Sage reaction. | None. | — | OPEN |
| SW-P-0010 | What role does the Jewel Mage play? | obs. 100 | Further appearance. | None. | — | OPEN |
| SW-P-0011 | Do Elliott and Bridget accept Monica; how does Elliott’s contempt meet her concealed rank? | obs. 061, 070 | Council scenes. | None. | — | OPEN |
| SW-P-0012 | Do Monica’s speech gains persist and generalize to strangers? | obs. 112, 114 | Ordinary scenes with strangers. | None. | — | OPEN |

## 7. Literary form, motifs and evaluation — SW-F

Owns recurring prose/form and ethical-framing patterns that warrant cumulative retrieval.

Fields: feature/domain; textual/formal mechanism; focalization/withholding/reader alignment; Japanese wording/register evidence; recurrence and changed function; affected-person access; evaluative criterion; consequences/tone; strongest rival interpretation; one-off versus promoted reason; linked claims/observations.

A scene's comic tone is distinct from its represented act and normative assessment. Avoid compulsory ethical scoring of every passage. Isolated details without cumulative significance remain in their volume reading.

Records at V01:

| ID | Feature | Mechanism | Focalization and withholding | Wording evidence | Function and recurrence | Rival reading | Promotion reason | Obs. |
|---|---|---|---|---|---|---|---|---|
| SW-F-0001 | External focalization of power | Monica’s full power is shown through Isabelle, Cyril, Thornley and Louis; her own view narrates fear and small uses. | Reader sees awe others feel and fear she feels. | Repeated “monster” in four viewpoints. | Prologue, chapters 9 and 10, secret episode. | The staircase gives narrator praise in her view, but for a pratfall. | Governs how later power scenes should be read. | 002, 098, 106, 117 |
| SW-F-0002 | Typographic silence | Withheld words printed as dots or dashes. | Erasure shown as erasure. | Cyril’s blanked destination; elided object of his wish; elided dream content. | Chapters 8, 9, 10. | Ordinary ellipsis. | Recurs; links to the title’s silence. | 081, 096, 107 |
| SW-F-0003 | Narrator’s deadpan correction | One-line paragraphs that correct a character’s inference or name an abuse. | Keeps reader outside every character. | “The impressive one was Isabelle”; “abuse”; “human rights”. | Throughout. | Pure joke delivery. | Main evaluative voice of the series so far. | 010, 025, 092 |
| SW-F-0004 | Romance-novel intertext | Characters borrow plots, roles and nicknames from a popular novelist. | Genre self-awareness inside the story. | Cover story; villainess; “ice prince”; alias. | Chapters 1, 3, 8, 10. | Decoration. | Shapes the cover and its irony. | 012, 019, 102 |
| SW-F-0005 | Pet lexicon | Powerful people speak to Monica as an animal to be tamed, fed and disciplined. | Comic surface over asymmetry. | 子リス; taming; owner; reward. | Chapters 4–8, epilogue. | Affectionate teasing. | Central to the Felix relation. | 036, 075, 078, 092 |
| SW-F-0006 | The riddle-song’s series | The same number series serves escape, memory, explanation and punishment. | Ties comic and dark registers. | Pig counts following the sum of the two before. | Chapters 2, 4, 5, 10. | Running gag. | Four functions in one volume. | 014, 037, 049, 109 |
| SW-F-0007 | Three-layer discrepancy | Legend, observers’ misreadings, interior shown side by side. | Reader alone holds all three. | Isabelle’s praise and the narrator’s causes. | Throughout. | — | The volume’s structural engine. | 018, 131 |
| SW-F-0008 | Comedy and harm | Comic register applied to coercion, a blow and a non-consensual kiss. | Harm sometimes registered, the kiss not. | Narrator’s abuse line; paw-pad joke. | Chapters 1, 7, 8. | All harmless play. Criterion: effect on the affected person registered independently of tone. | Normative baseline for later volumes. | 010, 070, 073, 076 |
| SW-F-0009 | Edition-level disclosure order | Frontispieces and character card disclose name, scenes and lines before the text. | Packaging pre-empts prose withholding. | Character card; night-fight caption. | Front matter. | Standard LN packaging. | Disclosure order differs from narrative order. | 124, 130 |

## 8. Reconstruction readiness — SW-RD

Owns local, domain-specific readiness decisions, not operational model rules or global grades.

Fields: local identity; continuity/state/source boundary; requested output tier/domain; readiness state; evidence variety/ordinary/recipient coverage; affirmative limitations; missing evidence; held-out/prospective test route; actual results; restrictions/abstentions; reviewer/date; existing model/evidence path only when created; prior decision/revision route.

Readiness vocabulary and tier criteria come from [the character method](../00%20Frameworks%20and%20Methods/SW_CHARACTER_RECONSTRUCTION_METHOD.md). Absence of evidence and affirmative negative evidence are separately recorded. No character is assessed in this bootstrap.

Records at V01. These are evidence reviews made under the character method after V01 closure, not models. No recognition profile, domain model, fuller reconstruction or synthetic dialogue exists; no rule IDs exist; no test has been run; no tier is awarded. Global capability assessment remains with the designated curation process and is not touched. Reviewer: the V01 sequential integrator, 2026-10-14.

| ID | Identity; state boundary | Tier considered | Readiness state | Evidence variety | Affirmative limitations | Missing evidence | Test route | Restrictions |
|---|---|---|---|---|---|---|---|---|
| SW-RD-0001 | sw.monica; V01 exit | Recognition profile | UNASSESSED. Evidence inventory appears adequate for a future assessment. | Ordinary life, crisis, study, work; at least eight recipients with contrasting speech; consistent fluency conditions; self-report against conduct; counterevidence recorded. | Key past withheld; much of her interior comic in register. | Speech with strangers beyond the school’s first week; reaction to disclosure. | Freeze anchors before V02; check against V02 ordinary scenes. | No profile may be drafted without separate authorization. |
| SW-RD-0002 | sw.monica; V01 exit | Domain-bounded model | INSUFFICIENT_EVIDENCE | As above. | Single volume; romance, politics, family and formal Sage duty barely sampled. | Longitudinal transitions; domains above. | Later volumes. | — |
| SW-RD-0003 | sw.felix; V01 exit | Any tier | INSUFFICIENT_EVIDENCE | Public scenes, three private scenes, two outside judgments. | Affirmative limitation: his motives are deliberately withheld and his public statements are shown to be unreliable. | His wish; the duke’s hold; his nights. | Later disclosure. | Public behaviour must not be taken as interior evidence. |
| SW-RD-0004 | sw.cyril; V01 exit | Any tier | INSUFFICIENT_EVIDENCE | Rich interior in two scenes; consistent public conduct; recipient contrast between Felix and Monica. | Few ordinary scenes. | Ordinary life; family scenes. | Later volumes. | — |
| SW-RD-0005 | sw.louis; V01 exit | Any tier | INSUFFICIENT_EVIDENCE | Coercive public scenes; candid private scene; domestic glimpse. | Only one private scene. | Professional and family conduct. | Later volumes. | — |
| SW-RD-0006 | sw.nero; V01 exit | Any tier | INSUFFICIENT_EVIDENCE | Frequent dialogue with Monica; one scene with Felix. | Nature undisclosed. | Origin and limits. | Later disclosure. | — |
| SW-RD-0007 | sw.isabelle, sw.lana; V01 exit | Any tier | INSUFFICIENT_EVIDENCE | Several scenes each. | Thin interiors. | Viewpoint scenes. | Later volumes. | Keep explicitly thin. |
| SW-RD-0008 | All other V01 identities | Any tier | INSUFFICIENT_EVIDENCE | One to three scenes each. | Thin. | — | — | Keep explicitly thin. |

## 9. Unit closure and acceptance — SW-U

Owns cumulative transaction bookkeeping separately from claims.

Fields: witness/unit; source lock and locator fidelity state; admitted prose/image/paratext coverage independently; inspection completed; semantic review/acceptance state; each typed responsibility's update IDs or no-material-update rationale; exit freeze; durable/committed closure reference; remaining mandatory/optional evidence; publication/audit routes.

At initialization no numbered volume, supplement, or web unit was closed. Repository-wide publication facts belong to the entrypoint/actual Git workflow; this ledger links their receipts without guessing.

Records at V01:

| Field | SW-U-V01 |
|---|---|
| Witness and unit | `SW-LNJP-V01`, Japanese LN Volume 01. |
| Source lock and locator fidelity | Byte-locked; original local locator package recovered and its six inner seals verified 2026-10-14; every quoted fragment and cited locator in the reading verified against the sealed block map. |
| Prose coverage | Complete: prologue, ten chapters, epilogue, in-volume secret episode. |
| Image coverage | Complete: all 24 image resources viewed, including frontispieces, story illustrations and the four character-reference pages. |
| Paratext coverage | Complete: contents, credits, afterword, colophon, notices, jacket. |
| Inspection | Completed 2026-10-14. |
| Semantic review | Author self-review including later-knowledge leakage check; owner semantic acceptance not claimed. |
| SW-S | SW-S-0001 to SW-S-0024. |
| SW-R | SW-R-0001 to SW-R-0022. |
| SW-K | SW-K-0001 to SW-K-0020. |
| SW-W | SW-W-0001 to SW-W-0024. |
| SW-C / SW-CR | SW-C-0001 to SW-C-0018; no revision events because no predecessors existed. |
| SW-P | SW-P-0001 to SW-P-0012, all OPEN; no predictions. |
| SW-F | SW-F-0001 to SW-F-0009. |
| SW-RD | SW-RD-0001 to SW-RD-0008, evidence reviews only. |
| Exit freeze | `SW-FR-V01-EXIT` in the reading’s section 10. |
| Durable closure | The commit that adds the V01 reading and this record; its identity and CI receipts are in Git history, not here. |
| Remaining mandatory evidence | None. |
| Remaining optional evidence | Publisher-original EPUB comparison; printed pagination; web and companion comparisons, each requiring authorization. |
| Architecture review | First closed-volume review recorded in the synthesis architecture; one master ledger remains adequate; no split. |

## Write, amend, and split rules

The authorized sequential integrator appends source-bearing state and revision events after full unit inspection. Patch current claim/readiness views only with preserved prior events. Record every affected responsibility's material delta or explained no-update in the unit closeout. Coverage completion never mechanically promotes an inference or readiness level.

Correct an objective error through an explicit correction event retaining old/new evidence routes and affected homes. Later reinterpretation is a source-bounded revision, not a rewrite of the historical freeze. If a record cannot be supported, defer or mark uncertainty rather than padding a table.

Split a typed responsibility only after recurring evidence establishes independent retrieval/revision pressure or a separate specialist dependency. Record exact transferred IDs, ownership, new path and necessary bounded backfill in architecture/entrypoint. Preserve historical routes and prohibit duplicate live datasets. Architecture-defined split decisions, not arbitrary row counts, govern this transition.
