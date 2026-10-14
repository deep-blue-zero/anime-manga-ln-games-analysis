---
title: "Silent Witch — SW Master Longitudinal Ledger"
artifact_id: SW_MASTER_LONGITUDINAL_LEDGER
artifact_type: master_longitudinal_ledger
series: "Silent Witch: Secrets of the Silent Witch"
series_id: silent-witch
generation: V1
version: "1.2"
last_updated: "2026-10-14"
status: canonical
scope: "Exclusive pre-split cumulative state; Japanese LN V01 and V02 closed and reconciled into every typed section"
source_boundary: "Japanese LN V01 and V02, witnesses SW-LNJP-V01 and SW-LNJP-V02, closed; no other source unit in any lane analyzed."
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
  state: V02_CLOSED
  committed_high_water_mark: V02
  analyzed_units: [SW-LNJP-V01, SW-LNJP-V02]
  frozen_units: [SW-LNJP-V01, SW-LNJP-V02]
  literary_observations: 252  # V01 reading 001..132; V02 reading SW-E-LNJP-V02-001..120
  local_character_identities: 31
  character_models: 0
  readiness_assessments: 12  # evidence reviews SW-RD-0001..0012; no tier awarded
  claim_records: 26
  revision_records: 18  # SW-CR-0001..0018, all at V02 closure
  prediction_records: 20  # prospective questions SW-P-0001..0020; zero predictions registered
  split_ledger_paths: []
  sequential_analysis_lock: OPEN
  sequential_analysis_lock_scope: CONTINUOUS_RUN_AUTHORIZED_2026-10-14
```

The initialization state, preserved here as history, was NO_SOURCE_UNIT_ANALYZED at PRE_V01 with every count at zero. Those zero records were truthful absence of analysis, not findings about the novel. The records below were appended at V01 closure on 2026-10-14 from the [V01 deep reading](../02%20Sequential%20Readings/SW_V01_DEEP_READING.md). They contain no simulated dialogue and no material from any later unit. Records marked as V02 records were appended at V02 closure on 2026-10-14 from the [V02 deep reading](../02%20Sequential%20Readings/SW_V02_DEEP_READING.md) under the same rule.

## Common record contract

Every source-bearing record carries: stable typed ID; continuity/witness/source unit; applicable diegetic interval and disclosure boundary; evidence class; canonical observation reference; exact evidence route; formulation; support; material counterevidence/rival explanation; uncertainty; created/updated boundary; and supersession/revision references where relevant.

Stable IDs are never renumbered. Source observation grammar is `SW-E-LNJP-V<NN>-<sequence>` for numbered LN units; the volume reading owns those IDs. Supplement/web IDs are separate. Local entity keys resolve only inspected identity evidence and are not global character enrollments.

The common fields apply to all sections. The following field lists define each section's additional exclusive responsibility; they are schemas, not populated rows.

**V01 record defaults.** Unless a row says otherwise, every V01 record has: continuity Japanese LN main track; witness and source unit `SW-LNJP-V01`; diegetic interval from three months after the Worgan dragon to one week after Thornley’s arrest; disclosure boundary V01; created and last updated at V01 closure, 2026-10-14; no supersession. The canonical observation reference is the `obs.` number in the [V01 reading](../02%20Sequential%20Readings/SW_V01_DEEP_READING.md#614-observation-register), meaning `SW-E-LNJP-V01-<nnn>`. The evidence route is that observation, then its locator, then the locally retained sealed locator package. Evidence classes use the method’s grammar abbreviated as OTE, CRB, NP, SI, WH, SP, NE, CON and UQ. Romanized names are analyst conveniences.

**V02 record defaults.** Every V02 record has: continuity Japanese LN main track; witness and source unit `SW-LNJP-V02`; diegetic interval from about two weeks after Monica’s enrolment to about six weeks after it, the evening of the delivery day; disclosure boundary V02; created and last updated at V02 closure, 2026-10-14; no supersession unless stated. Its `obs.` numbers refer to the [V02 reading](../02%20Sequential%20Readings/SW_V02_DEEP_READING.md#618-observation-register), meaning `SW-E-LNJP-V02-<nnn>`, and its bare locators to `SW-LNJP-V02`. A V01 observation cited in a V02 record is written `V01 obs. nnn`.

**Local identities at V01.** These keys resolve inspected identity only and are not global enrollments.

| Local key | Japanese name and aliases in V01 | Identity notes |
|---|---|---|
| sw.monica | モニカ・エヴァレット; 〈沈黙の魔女〉; cover name モニカ・ノートン; 同期殿, 子リス, ノートン会計 | One person under two names; the cover is known to her confidants only. |
| sw.felix | フェリクス・アーク・リディル; 第二王子; 生徒会長; マスター to Wildianu | Prologue watcher identification was inference only at V01; established from his own viewpoint at V02, SW-C-0006. |
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

**Local identities added at V02.**

| Local key | Japanese name and aliases in V02 | Identity notes |
|---|---|---|
| sw.glen | グレン・ダドリー; 肉屋の倅 | Transfer student; apprentice mage. Identification as Louis’s disciple is inference only, SW-P-0001. |
| sw.casey | ケイシー・グローヴ; ブライト伯爵令嬢 | Also the prologue’s unnamed conspirator, identified by object, SW-C-0019. Removed from the school. |
| sw.claudia | クローディア・アシュリー; 〈歩く図書館〉 | Cyril’s adoptive sister; Neil’s fiancée. |
| sw.caroline | カロライン・シモンズ; ノルン伯爵令嬢 | The V01 staircase girl, first named in V02. To be expelled. |
| sw.maclaggan | ウィリアム・マクレガン; 〈水咬の魔術師〉 | Monica’s and Louis’s former Minerva teacher. |
| sw.lindsay | リンジー・ペイル | Dance teacher; Monica’s homeroom teacher after Thornley. |
| sw.boyd | カール・ボイド | Chess teacher. |
| sw.mary | メアリー・ハーヴェイ; 〈星詠みの魔女〉 | A Sage. |
| sw.mabel | メイベル・ヘインズ | Stage-effects lead. |
| sw.agatha | アガサ | Isabelle’s maid; also present in V01’s prologue. |
| sw.eliane | エリアーヌ; エリアーヌ・ハイアット | Felix’s second cousin; house given variously, V02 reading section 8.8. Not on stage. |
| sw.lionel | ライオネル | First prince. Not on stage. |
| sw.count-bright | ブライト伯爵 | Casey’s father. Not on stage except in memory. |
| sw.monica-father | モニカの父 | Unnamed. Known from memory and delirium. |
| sw.monica-uncle | 叔父 | Unnamed; the man in the V01 dream, SW-C-0003. |

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

Records at V02:

| ID | Key | State before → after | Kind | Process: perception → appraisal/affect → options → act/speech → consequence | Persona/private; recipient; register | Obs. | Class | Rival; uncertainty |
|---|---|---|---|---|---|---|---|---|
| SW-S-0025 | sw.monica | Father’s fate unknown → learned researcher of the body as number, reviled, stoned and burned as a heretic with his papers. | REVEALED_NOT_NEW | Felix’s demand for expectations → old wound → memory; poisoning → delirium of the execution. | Private memory; never spoken to anyone. | 034, 044 | CRB | R: drugged distortion; V02 section 8.1. U: research, place, date. |
| SW-S-0026 | sw.monica | Man in the V01 dream unidentified → her paternal uncle, who beat her for reciting numbers and forbade speaking of her father in public. | REVEALED_NOT_NEW | Numbers recited → bottle, poker threat → apology and promise of silence. | Child’s plea; promise to say nothing before people. | 045 | CRB | R: as above. U: duration; how it ended. |
| SW-S-0027 | sw.monica | Duties of imposed roles never considered → accepts duties as treasurer, then as Sage. | DISPOSITION_CHANGE | Elliott’s noblesse oblige → shame at avoiding duty → practice; at the climax, acts alone as the Silent Witch. | Private resolve, then public act before Casey. | 024, 033, 083 | CRB, SI | R: compliance with Felix’s pressure. U: persistence. |
| SW-S-0028 | sw.monica | Speech gains among trusted people → refusals and assertions to superiors and opponents. | DISPOSITION_CHANGE | Fact or another’s interest at stake → fear overridden → full sentences. | To Elliott, Caroline, Casey, Louis; still fails at a simple request in class. | 023, 043, 072, 095 | OTE | R: situational, not general. U: strangers. |
| SW-S-0029 | sw.monica | Terror of Nero’s human form → at ease with it. | DISPOSITION_CHANGE | Repeated contact → noticed only when Nero points it out. | Large strange men still frighten her. | 006 | CRB | R: specific to Nero. U: generalization. |
| SW-S-0030 | sw.monica | Self-exclusion as out of place → offers herself as the most out of place, as a gift. | DISPOSITION_CHANGE | Refuses Lana from imagined shame; later serves coffee from her father’s pot to friends. | Self-description in public. | 003, 031, 058 | OTE | R: none. U: none. |
| SW-S-0031 | sw.monica | Unable to say she expects nothing → says it: cannot expect anything of anyone; only numbers are safe. | REVEALED_NOT_NEW | Romance novel → incomprehension → resolution in numbers. | Private, to Nero. | 057 | CRB | R: contradicted by conduct. U: none. |
| SW-S-0032 | sw.monica | Political indifference → uses factional logic to save Casey. | ROLE_CONTEXT_CHANGE | Execution threatened → looks straight at Louis → bargains on his faction’s interest. | First negotiation she wins. | 095 | OTE | R: Louis chose to concede. U: none. |
| SW-S-0033 | sw.monica | Hides power from everyone at school → reveals herself to Casey by act and by name. | KNOWLEDGE_CHANGE | Lives at stake → ritual chant naming herself. | Before an enemy who is also a friend. | 084, 085 | OTE | R: none. U: consequences, SW-P-0019. |
| SW-S-0034 | sw.felix | Watcher inferred → watcher established; secret student of magic and fan of the Silent Witch; searching for her. | REVEALED_NOT_NEW | Isabelle’s account → memory; Louis overheard → joy and search. | Private 僕; public 私 and denial of magic. | 014, 064, 065, 087, 088 | CRB, OTE | R: none. U: none. |
| SW-S-0035 | sw.felix | Motive withheld → states he must become king without wanting anything prepared for his name; holds the role while he bears the name. | UNRESOLVED | Eliane mentioned → indifference → resolve. | Private thought; said aloud only to Elliott. | 062, 077 | CRB | R: rhetoric. U: meaning, SW-C-0022. |
| SW-S-0036 | sw.louis | Coercer with private respect → also a gift-giver, a user of an unknowing decoy, and a negotiator who spares Casey to keep Monica’s cooperation. | REVEALED_NOT_NEW | Mission interest → calculation → concession. | Courteous surface, violent reputation, private candour. | 009, 010, 096, 099 | CRB | R: pure self-interest. U: none. |
| SW-S-0037 | sw.cyril | Fair but hostile superior → concealed protector who asks to be called Cyril. | RELATIONSHIP_CHANGE | Her endangerment and illness → care disguised as duty. | Shouting register persists; gentle in dance and sickroom. | 037, 046, 059, 069, 098 | OTE | R: duty to the prince. U: none. |
| SW-S-0038 | sw.cyril | Suspicion of Monica’s hand → also links the forest mage to the Silent Witch. | KNOWLEDGE_CHANGE | Isabelle’s account of the wyverns → memory of the silent monster. | Private. | 054 | CRB | R: none. U: link to Monica. |
| SW-S-0039 | sw.elliott | Contempt → shame, a noble’s protective duty, and grudging respect for her eye. | DISPOSITION_CHANGE | Castling → self-loathing; carriage → trusts her; still calls her presumptuous. | Flippant surface over a strict code. | 020, 021, 023, 024, 063 | OTE, CRB | R: self-interest. U: future acceptance. |
| SW-S-0040 | sw.casey | — → a friend who was an assassin under orders, grieving her brothers and her land. | REVEALED_NOT_NEW | Father’s order → infiltration → staged accident → device → surrender. | Cheerful persona; resigned truth. | 027, 079, 080, 082, 097 | OTE, CRB | R: friendship partly real. U: V02 section 8.3. |
| SW-S-0041 | sw.lana | Brusque helper → public friend; her pride and loneliness as a parvenu’s daughter disclosed. | REVEALED_NOT_NEW | Out of place everywhere → wants to give the best → hurt → accepts Monica’s coffee. | Haughty manner over care. | 029, 032 | CRB | R: none. U: none. |
| SW-S-0042 | sw.claudia | — → learned, gloomy, sharp, devoted to Neil; saved Monica; refuses thanks. | REVEALED_NOT_NEW | Jealousy → surveillance; poisoning → competent first aid. | Deliberate unapproachability; changes air with Neil. | 047, 048, 050, 068 | OTE | R: none. U: SW-P-0020. |
| SW-S-0043 | sw.isabelle | Theatrical admirer → also a deliberate policy-maker for Monica’s protection. | REVEALED_NOT_NEW | Debt to the Silent Witch → villainess performance as deterrence → mirrored revenge. | Stage villainess in public, devotee in private. | 052, 055 | CRB | R: enjoyment of the role. U: none. |
| SW-S-0044 | sw.glen, sw.maclaggan, sw.bridget, sw.neil | Thin entries: Glen, generous, loud, powerful and imprecise, rule-bending; MacLaggan, fond teacher with poor eyesight and unstated knowledge; Bridget, clever and cold, unconvinced; Neil, kind, competent, sensitive about height and his engagement. | REVEALED_NOT_NEW | — | — | 015, 016, 018, 039, 041, 089 | OTE, CRB | Keep explicitly thin. |

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
| SW-R-0013 | Felix → Cyril | Trusts his fairness; protects him. | — | Assigns him to Monica deliberately. | Hides Wildianu from him. | Partial disclosure only. | 103, 120 |
| SW-R-0014 | Cyril → Felix | Devoted loyalty; seeks recognition. | Total trust. | Defends him with force. | Unaware of Felix’s secrets. | Asymmetric knowledge. | 023, 096 |
| SW-R-0015 | Felix → Elliott | Uses his vigilance. | — | Lies to him about the night. | — | Partial disclosure. | 079 |
| SW-R-0016 | Elliott → Felix | Watchful friend; resents solo risks. | — | Sets traps on his behalf. | — | — | 036, 061 |
| SW-R-0017 | Felix → Duke Clockford | Grandson and dependant. | — | States he cannot defy the duke. | Removes the duke’s placements. | Conflict concealed. | 062, 120 |
| SW-R-0018 | Louis → Felix | Watcher; finds him uncanny. | Distrust. | King’s mandate. | Surveillance brooch disguised as a father’s gift. | Opponents. | 009, 119 |
| SW-R-0019 | Felix → Louis | Believes Louis watches him; resents theft of his prey. | Distrust. | Destroyed the brooch. | Hides his literacy. | Opponents; misattributes the arrest. | 120, 121 |
| SW-R-0020 | Thornley → Monica | Contempt → terror and recognition. | — | Attempted erasure and destruction of her mind. | — | Ended by arrest. | 104, 107 |
| SW-R-0021 | Selma → Aaron | Devotion without return. | — | Committed crimes for him. | — | Not reciprocated. | 064, 065 |
| SW-R-0022 | Lynn → Louis | Service without reverence. | — | Courier and transport. | — | — | 094, 117 |

Records at V02:

| ID | Actor → recipient | Relation and actor’s aim | Trust and disclosure, before → after | Obligation, power, initiative | Concealment, conflict, repair | Reciprocity; independent goals | Obs. |
|---|---|---|---|---|---|---|---|
| SW-R-0023 | Monica → Lana | Friend; wants to be with her. | Fear of shaming her → asks to go with her; treasures her notes. | Monica initiates a request for the first time. | Refusal repaired by Lana’s return. | Mutual; Lana has merchant ambitions. | 003, 008, 058 |
| SW-R-0024 | Lana → Monica | Friend and protector. | Pride-driven help → public claim of friendship. | Daily notes in convalescence. | Hurt at the tea, healed by the coffee. | Mutual. | 029, 031, 032 |
| SW-R-0025 | Monica → Casey | Friend, then rescuer. | Trust → knows of the discarded tea, chooses not to look → accuses → refuses to forget her. | Saves her from execution by bargaining. | Exposure; grief. | Asymmetric. | 027, 073, 090, 095 |
| SW-R-0026 | Casey → Monica | Instrument of access; ambivalent affection. | Cultivated trust → confession → farewell by name. | Uses Monica’s schedule access. | Throws away her tea to rescue her; final apology for promises. | Casey’s aim: kill or win Felix. | 082, 097 |
| SW-R-0027 | Monica → Cyril | Subordinate; growing trust; guilt. | Fear → trust; calls him Cyril. | Refuses to recant for his sake. | Lets him bear blame for the rope. | Asymmetric. | 043, 069, 098 |
| SW-R-0028 | Cyril → Monica | Concealed protector. | Fair judgment → active care disguised as duty. | Does her work; carries her; chocolate. | Apologizes for a fault not his. | Seeks the prince’s approval in parallel. | 026, 046, 059, 098 |
| SW-R-0029 | Elliott → Monica | Contempt cracked by shame and respect. | Distrust → trusts her eye; protects her as a noble. | Orders her to safety. | Cannot apologize for castling. | His code of roles. | 020, 021, 024 |
| SW-R-0030 | Monica → Elliott | Fear; unspoken debt for the idea of duty. | Unchanged outwardly. | — | Fears his anger over chess. | — | 033 |
| SW-R-0031 | Felix → Monica | Taming game, anger at harm, identification with his former self. | Suspicion → guardian presence at her bedside. | Demands she meet expectations. | Exploits her slip; joins the barbecue. | Seeks the Silent Witch, not Monica. | 036, 038, 049, 061 |
| SW-R-0032 | Monica → Felix | Wary duty. | Unchanged; registers his charm as pressure. | Must meet royal expectation. | Hides the attempt on his life. | — | 036, 038 |
| SW-R-0033 | Felix → the Silent Witch | Adoration and search. | From afar → resolved to find her. | — | Keeps her papers locked away. | Personal absorption. | 065, 087, 088 |
| SW-R-0034 | Louis → Monica | Instrumental care; values her cooperation. | Reward and warning. | Concedes on Casey for her sake. | Warns against attachment. | His faction and mission. | 009, 096, 099 |
| SW-R-0035 | Monica → Louis | Fear and trust; bargaining partner. | Trusts his word at once. | Wins a concession. | Asks his faction directly. | — | 095 |
| SW-R-0036 | Isabelle → Monica | Devotion as policy. | Unchanged; private debt explained. | Revenge on Caroline; convalescence room. | Public cruelty as cover. | Repays Kerbeck’s debt. | 052, 055 |
| SW-R-0037 | Claudia → Monica | Coerced friendship; lifesaver refusing thanks. | Jealous watching → claimed friendship. | Saves her life. | Baits her with the Silent Witch. | Devotion to Neil. | 047, 048, 050, 068 |
| SW-R-0038 | Claudia → Neil; Neil → Claudia | Devoted fiancée; dutiful, self-doubting fiancé. | — | Parents’ arrangement. | Height and rank disparity. | — | 048 |
| SW-R-0039 | Monica → Glen; Glen → Monica | Kinship in concealment; cheerful partnership. | Secret kept on both sides. | Dance partners. | Each unknowingly shields the other. | Glen’s master unnamed. | 015, 018 |
| SW-R-0040 | Felix → Glen | Suspicion because of his master. | Watchful. | Uses the dance to observe. | No link found. | — | 040 |
| SW-R-0041 | Bridget → Felix | Probing, unseduced; childhood acquaintance. | Tests his memory. | — | Underwater exchange at tea. | Her own judgment of Monica. | 039 |
| SW-R-0042 | Casey → Felix | Would-be assassin of the duke’s candidate. | — | Father’s order. | Thwarted. | Bright and Randall. | 080, 081 |

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

Records at V02:

| ID | Proposition | Anchors | Knower: status | Truth assessment | Change source; withheld information | Obs. |
|---|---|---|---|---|---|---|
| SW-K-0021 | Interval of V02. | From about two weeks after enrolment to about six weeks; festival next month. | Reader. | Stated. | S11:E000718; S21:E000232; S22:E000137. | 120 |
| SW-K-0022 | Monica Norton is the Silent Witch. | V02 exit. | Known: Monica, Nero, Louis, Lynn, Isabelle and her maid, Casey (removed). Not known: Felix, Cyril, the school. | True. | Casey learned by act and chant. | 084, 085 |
| SW-K-0023 | An assassination attempt with a 螺炎 failed. | Delivery day. | Known: Monica, Casey, Louis, Lynn, Nero, Felix by overhearing. Not known: Cyril, Elliott, the school. | True. | Concealed by Monica and Louis. | 076, 086, 087 |
| SW-K-0024 | The Silent Witch stopped it. | Same. | Known: as above, including Felix. | True. | Louis overheard. | 087 |
| SW-K-0025 | Casey was the culprit. | Same. | Known: Monica, Louis, Lynn, Nero. Not known: Felix, council, friends. | True. | Withheld from the council. | 080, 095 |
| SW-K-0026 | The timber fell by Cyril’s oversight. | Same. | Believed: Cyril, council. | False. | Monica knows the rope was cut. | 098 |
| SW-K-0027 | Glen is Louis’s disciple. | V02. | Louis; Felix knows Glen’s master’s identity. Not known: Monica, Glen as to decoy role. | Strong inference only. | Name withheld. | 010, 015, 040 |
| SW-K-0028 | Felix was the watcher at Kerbeck. | Three months before V01. | Felix, Wildianu, reader. Not known: Monica. | True. | Felix’s viewpoint. | 064 |
| SW-K-0029 | Felix studies magic and has a spirit. | V01–V02. | Felix, Wildianu, reader; Nero suspects. Not known: Monica, council. | True. | Public denial. | 014, 065, 075 |
| SW-K-0030 | Monica’s father was burned as a heretic; her uncle abused her. | Childhood, before Minerva. | Monica, reader. | Strong inference; memory and delirium. | No date or place. | 034, 044, 045 |
| SW-K-0031 | Caroline poisoned Monica. | Third week of V02 events, approx. | Felix, Cyril, Claudia, Isabelle, teachers; rumour. | True. | Caroline to be expelled. | 044, 052 |
| SW-K-0032 | The duke plans war on Randall as a step to the Empire. | — | Believed by Casey and Count Bright via Randall nobles. | Unverified report. | No scene with the duke. | 081 |
| SW-K-0033 | Claudia was following Monica over Neil. | Week before the poisoning. | Claudia, Monica, reader. | Stated by Claudia. | Whether she also suspects more, unknown. | 048, 050 |
| SW-K-0034 | MacLaggan does or does not recognize Monica. | V02. | Unknown. | Unresolved. | His remark in the secret episode. | 016, 089 |

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

Records at V02:

| ID | Domain | Current formulation | Asserting source | Demonstration; conditions and costs | Exceptions; open points | Locators |
|---|---|---|---|---|---|---|
| SW-W-0025 | Measuring power | Crystal scale to 250; bands 1–49, 50–99, 100–129, 130+; 200+ rare; Sages 150+ measured yearly; peaks late teens; colour shows element. | Narrator, MacLaggan | Glen breaks it past 250; Monica last 202. | Fewer than a handful exceed 250; two Sages. | S14:E000235; S14:E000271–E000282; S14:E000331–E000333 |
| SW-W-0026 | Three talents | Quantity of power, understanding of formulas, control of power. | MacLaggan | Glen: control without precision. | — | S14:E000233–E000265 |
| SW-W-0027 | Chantless casting, public account | Instant derivation of the optimal formula. | Plate, MacLaggan, Felix | — | Narrative cause differs, SW-C-0001. | S12:E000004; S14:E000240; S20:E000621–E000626 |
| SW-W-0028 | Ritual chant | Summoning a higher being needs a chant of respect that cannot be omitted. | Narrator | Monica speaks it. | — | S23:E000538–E000545 |
| SW-W-0029 | Remote casting; two spells | Remote origin at a cost in precision; holding two spells is very hard. | Narrator, Monica | Monica does both. | — | S11:E000403; S11:E000503–E000505 |
| SW-W-0030 | Body magic | All magic on human bodies forbidden in Ridill, including healing; stricter than mind interference. | Monica, narrator | — | The Empire allows limited medical magic. | S16:E000324–E000347 |
| SW-W-0031 | The Empire | Largest continental state, east; young emperor; reforms; mages emigrating; merchants waiting. | Narrator, Lana, Neil | — | — | S16:E000339–E000347; S17:E000508–E000512 |
| SW-W-0032 | Randall | Small kingdom between Ridill and the Empire; first prince’s mother’s home; chocolate technology; secret aid to Bright. | Felix, Casey | — | Cross-border aid violates interstate rules. | S21:E000440–E000446; S23:E000170–E000171 |
| SW-W-0033 | Succession and factions | Three princes, three mothers; Lionel said indifferent; Felix’s mother the late second queen; duke wants Eliane for Felix; central versus regional nobles. | Felix, Louis, Elliott, Mary, Monica | — | All reports; king and duke off stage. | S17:E000516; S21:E000443; S23:E000073; S26:E000235; S28:E000232 |
| SW-W-0034 | The east and dragons | Front line; private armies; central fear of revolt; dragon knights slow to poor counties; Kerbeck strongest, neutral. | Cyril, Isabelle, Casey | Kreme earth dragon; Bright’s losses. | — | S20:E000242–E000300; S23:E000156–E000175 |
| SW-W-0035 | Seven Sages | Jade Room for king and Sages; issued robes; Thorn Witch male, of the oldest house, plant enchantment; Star-reading Witch Mary Harvey; Cannon Mage named. | Narrator, Monica, Felix | Rose trap. | — | S18:E000085; S23:E000480–E000487; S28:E000117; S28:E000214–E000224 |
| SW-W-0036 | Academy barrier and security | Louis’s dormant barrier with detection; node in the old-garden fountain; Thorn Witch’s rewrite trap; crest and permit checks; blades banned. | Monica, Lynn, Elliott | Monica rewrites it. | Inside threats not covered. | S17:E000735–E000751; S22:E000284; S23:E000431–E000486 |
| SW-W-0037 | 螺炎 | Fixed brooch-sized assassination device; absorbs ambient power; screw-shaped fire piercing most barriers; short range; stoppable only by its user. | Monica | Smothered without oxygen. | — | S23:E000190–E000211; S25:E000086–E000099 |
| SW-W-0038 | Mind interference in interrogation | Permitted for grave criminals; may leave subjects permanently unconscious. | Louis, narrator | Withdrawn for Casey. | — | S26:E000167–E000171 |
| SW-W-0039 | Academy life | Electives two of twenty-plus; dance and tea classes; cafeteria service billed to fees; fire needs application; festival play of the founding king and seven spirit kings. | Narrator, characters | — | — | S13:E000107; S16:E000056; S17:E000595–E000602; S22:E000029–E000031; S22:E000193–E000202 |
| SW-W-0040 | Reference paratext kept apart | Card statements absent from the narrative. | Character cards | — | Not narrative evidence. | S30:E000004–S33:E000004 |

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

Claim records. Rows SW-C-0001 to SW-C-0018 were registered at V01 and now show the current formulation after V02 review; their V01 wording is preserved in the revision records below. Rows SW-C-0019 onward were registered at V02.

| ID | Question | Formulation | Range; class | Support | Counterevidence; alternatives | State; confidence | Discriminating observation | Dependents |
|---|---|---|---|---|---|---|---|---|
| SW-C-0001 | Origin of the silence | Chantless casting began as avoidance of speech, and silence and mastery are one mechanism; the avoidance has an earlier root in childhood punishment for speaking, while the public account explains the capacity as instant computation. | V01–V02; NP, SI | V01 obs. 007, 033; V02 obs. 011, 016, 045 | Capacity may exceed any cause; the public account is not false. | REVISE at V02 (SW-CR-0001); high. | Monica’s own account of how she learned it. | SW-S-0002; SW-S-0026 |
| SW-C-0002 | Fear response | Pain, fear or exposure drive Monica into numerical absorption; the habit began as a vow to keep her father’s numbers. | V01–V02; NP | V01 obs. 014, 037, 071, 072, 085; V02 obs. 004, 038, 044 | Habit rather than defence. | STRENGTHEN at V02 (SW-CR-0002); high. | Fear without absorption. | SW-S-0003; SW-F-0006 |
| SW-C-0003 | Past harm | The man in the V01 dream is Monica’s paternal uncle, who after her father’s execution beat her for reciting numbers and defending him and imposed silence about him in public. | V01–V02; CRB under drug, SI | V01 obs. 037, 040, 057–059; V02 obs. 045 | Drug distortion; V02 reading section 8.1. | REVISE at V02 (SW-CR-0003): identity resolved; duration and end OPEN. | Sober account or third-party report. | SW-S-0004; SW-S-0026; SW-P-0005 |
| SW-C-0004 | Selection | The makeweight self-assessment is contradicted by Louis’s memory of the duel; the examiners’ ranking is unstated. | V01; CRB | obs. 013, 117 | Louis’s memory may be self-serving. | OPEN on examiners; high that her belief lacks support. Reviewed at V02: PRESERVE (SW-CR-0004). | Any examiner’s statement. | SW-S-0008; SW-K-0016 |
| SW-C-0005 | Mission purpose | Stated protection; Monica doubts it; Louis reads surveillance, uses a decoy, chose Monica partly for her distrust of people, and calls himself first-prince because he dislikes the duke and Felix; the king is unshown. | V01–V02; CRB | V01 obs. 034, 119; V02 obs. 010, 096 | Protection and surveillance may coexist. | STRENGTHEN and partly REVISE at V02 (SW-CR-0005); king’s intent OPEN. | King or royal agent on stage. | SW-K-0005; SW-P-0007 |
| SW-C-0006 | The watcher | The prologue’s watcher is Felix. | V01–V02; OTE | V01 obs. 003, 024, 122; V02 obs. 064, 088 | — | STRENGTHEN to OTE at V02 (SW-CR-0006). | — | SW-S-0012; SW-S-0034 |
| SW-C-0007 | Felix’s divergence | Public and private selves diverge: he denies a talent for magic while studying it and hiding a spirit; he removes the duke’s placements while professing he cannot defy him; he must become king without wanting what is prepared for his name, holding the role while he bears it. | V01–V02; OTE, SI | V01 obs. 020, 062, 077, 078, 120; V02 obs. 014, 062, 065, 077 | Prudence rather than resistance. | STRENGTHEN at V02 (SW-CR-0007); motive OPEN. | Felix’s wish disclosed. | SW-S-0009; SW-S-0010; SW-S-0035; SW-C-0022 |
| SW-C-0008 | Recognition by Felix | Felix has not identified Monica as the Silent Witch; at V02 exit he is searching the school for her and his search excludes Monica. | V01–V02 exit; OTE | V01 obs. 069, 122; V02 obs. 087 | — | STRENGTHEN at V02 (SW-CR-0008). | Felix witnessing her magic. | SW-P-0003; SW-P-0014 |
| SW-C-0009 | Recognition by Cyril | Cyril holds an unverified suspicion from her hand and remark (V01), and at V02 links the forest mage with the Silent Witch; V02 shows no renewed link to Monica. | V01–V02 exit; SI, CRB | V01 obs. 111; V02 obs. 054 | Idle curiosity. | REVISE at V02 (SW-CR-0009). | Cyril acting on either link. | SW-P-0004; SW-S-0038 |
| SW-C-0010 | Form of power | Awe at Monica’s power is narrated through external focalizers; from V02 her own viewpoint also narrates her power, as calculation under constraint. | V01–V02; SI | V01 obs. 002, 056, 098, 106, 117; V02 obs. 004, 025, 083, 086 | The V01 staircase anticipated this. | REVISE at V02 (SW-CR-0010). | — | SW-F-0001; SW-F-0010 |
| SW-C-0011 | Rank and truth | The school treats rank as epistemic authority; Cyril’s inquiry is the first counterexample; at V02 rank is also used as a weapon of justice (Felix, Isabelle) and Elliott’s code ties rank to duty. | V01–V02; OTE, NP | V01 obs. 058, 091; V02 obs. 021, 024, 052, 053 | Cyril’s fairness may be exceptional. | STRENGTHEN at V02 (SW-CR-0011). | Further authorities’ conduct. | SW-W-0023; SW-S-0007 |
| SW-C-0012 | Thornley’s crimes | Organized embezzlement; erased Aaron’s and Cyril’s memories; Selma’s manipulation inferred. | V01; CRB, OTE | obs. 022, 081, 108 | Selma acted alone. | Aaron and Cyril established; Selma inferred. Reviewed at V02: PRESERVE (SW-CR-0012). | Thornley’s interrogation results. | SW-K-0011; SW-K-0012 |
| SW-C-0013 | Nero’s nature | Neither an ordinary cat nor, in Felix’s judgment, a spirit. | V01; CRB | obs. 072, 102 | Unusual familiar spirit. | OPEN. Reviewed at V02: PRESERVE (SW-CR-0013). | Disclosure of origin. | SW-P-0008 |
| SW-C-0014 | Talent as curse | Monica regards her talent as a curse that took her father and friend; her father was executed as a heretic for forbidden research into the body as number, and the friend turned away when she mastered chantless magic. | V01–V02; CRB, NP | V01 obs. 090, 101; V02 obs. 034, 044 | Delirium distortion. | REVISE at V02 (SW-CR-0014); research OPEN. | Account of the research. | SW-S-0008; SW-S-0025; SW-P-0017 |
| SW-C-0015 | Friendship | The bond with Lana rests on shared experience of being called boring and being out of place, and on mutual gestures of giving; Lana began from pride and stays from affection. | V01–V02; OTE, CRB | V01 obs. 031, 046, 083, 112; V02 obs. 008, 029, 031, 032 | Convenience on Lana’s side. | STRENGTHEN and REVISE at V02 (SW-CR-0015). | Disclosure strain. | SW-R-0007; SW-R-0008; SW-R-0023; SW-R-0024 |
| SW-C-0016 | Comedy and harm | The comedy of coercion registers harm in most cases; the non-consensual kiss is unevaluated and unknown to its recipient. | V01; NE | obs. 010, 073, 076, 092 | The narration treats it as harmless play. Criterion: whether effect on the affected person is registered independent of tone. | Recorded. Reviewed at V02: PRESERVE; UNTESTED (SW-CR-0016). | Any later revisiting. | SW-F-0008 |
| SW-C-0017 | Louis’s stance | Louis combines coercion with investment in her self-respect and his own pride; at V02 also gifts, an unknowing decoy, and a concession calculated to keep her cooperation. | V01–V02; CRB, SI | V01 obs. 011, 117, 118; V02 obs. 009, 010, 096, 099 | Pure self-interest. | STRENGTHEN at V02 (SW-CR-0017). | Louis acting against her interests. | SW-S-0017; SW-S-0036 |
| SW-C-0018 | Source of perception | Monica’s numerical perception and comfort derive from her father’s teaching; she memorized his burning numbers as proof he lived and keeps his coffee pot. | V01–V02; NP, CRB | V01 obs. 026, 043, 044; V02 obs. 034, 044, 058 | Innate disposition. | STRENGTHEN at V02 (SW-CR-0018). | — | SW-S-0001; SW-S-0025 |
| SW-C-0019 | Casey and the prologue | Casey Grove is the prologue’s unnamed conspirator, acting on Count Bright’s order with a 螺炎, from grievance at central neglect and gratitude to Randall; her friendship was begun instrumentally and its later reality is left ambivalent. | V02; OTE for identity, UQ for feeling | V02 obs. 027, 070, 079–082, 097, 111 | Partly genuine friendship. | Identity established; feeling OPEN. | Casey’s later testimony. | SW-S-0040; SW-P-0019 |
| SW-C-0020 | Duty | Monica derives a concept of duty from Elliott’s noblesse oblige and transposes it to her roles as treasurer and Sage; the climax is narrated as acceptance of the title as responsibility. | V02; SI | V02 obs. 024, 033, 083, 084 | Compliance under pressure. | Strong inference. | Her conduct when duty and fear conflict again. | SW-S-0027 |
| SW-C-0021 | Concealment of the attempt | Monica’s concealment is a political bargain using Louis’s factional logic, at a cost to Cyril and her conscience; the volume presents it sympathetically and leaves its justice unjudged. | V02; NE | V02 obs. 095, 096, 098 | Mercy as plain virtue. Criterion: costs to others registered. | Recorded. | Later consequences. | SW-F-0015 |
| SW-C-0022 | Felix’s discontinuities | A cluster of unexplained details surrounds Felix’s identity and history: Bridget’s childhood test, his memory of a boy apologizing as a royal, the role held while he bears the name, the seer’s blindness to his star. No hypothesis is registered. | V02; UQ | V02 obs. 039, 049, 062, 093 | Ordinary nostalgia and rhetoric. | OPEN. | Any disclosure about his childhood. | SW-P-0016 |
| SW-C-0023 | Affiliation | Monica says she cannot expect anything of anyone or be absorbed in anyone, while her conduct shows growing attachment; no romantic interest on her side is shown; Felix’s first-love-like absorption is directed at the Silent Witch as an idea. | V02; CRB, SI | V02 obs. 038, 057, 071, 088 | Her statement is accurate for romance. | Recorded. | Her own account of attachment. | SW-S-0031 |
| SW-C-0024 | Mission and belonging | Louis chose Monica partly for her distrust of people and reads her attachment as a risk; Monica shares the warning that Monica Norton is temporary. | V02; CRB | V02 obs. 096; S18:E000792–E000798 | — | Recorded. | A conflict between friendship and mission. | SW-R-0034 |
| SW-C-0025 | Isabelle’s method | Isabelle’s cover-bullying is a deliberate deterrence policy and her revenge mirrors the crime; the volume treats humiliation as justice. | V02; CRB, NE | V02 obs. 052–055 | Pure enjoyment of the role. | Recorded. | — | SW-F-0016 |
| SW-C-0026 | Out of place | 場違い organizes the social plot through three outsiders by class or region, Monica, Lana and Casey, reversing from exclusion to self-gift. | V02; SI (form) | V02 obs. 003, 029, 031 | Common word. | Recorded. | Recurrence. | SW-F-0012 |

Revision records at V01: none. Every V01 claim was an initial formulation with no predecessor.

Revision records at V02, 2026-10-14, reviewer the V02 sequential integrator:

| Revision | Claim | Earlier formulation and boundary | Transition | New formulation and boundary | Reason | Affected homes | Kind |
|---|---|---|---|---|---|---|---|
| SW-CR-0001 | SW-C-0001 | Chantless casting began as avoidance of speech; silence and mastery are one mechanism. (V01) | REVISE | Chantless casting began as avoidance of speech, and silence and mastery are one mechanism; the avoidance has an earlier root in childhood punishment for speaking, while the public account explains the capacity as instant computation. (V02) | See V02 reading section 9.1. | V02 evidence | Later reinterpretation, not correction. |
| SW-CR-0002 | SW-C-0002 | Pain, fear or exposure drive Monica into numerical absorption. (V01) | STRENGTHEN | Pain, fear or exposure drive Monica into numerical absorption; the habit began as a vow to keep her father’s numbers. (V02) | See V02 reading section 9.1. | V02 evidence | Later reinterpretation, not correction. |
| SW-CR-0003 | SW-C-0003 | V01 supplies associative evidence of past harm by a drinking adult man she called おじさん, linked to a learned rule of silence. (V01) | REVISE | The man in the V01 dream is Monica’s paternal uncle, who after her father’s execution beat her for reciting numbers and defending him and imposed silence about him in public. (V02) | See V02 reading section 9.1. | V02 evidence | Later reinterpretation, not correction. |
| SW-CR-0004 | SW-C-0004 | The makeweight self-assessment is contradicted by Louis’s memory of the duel; the examiners’ ranking is unstated. (V01) | PRESERVE | Unchanged (V02). | No new evidence on the selection. | — | Review, not change. |
| SW-CR-0005 | SW-C-0005 | Stated protection; Monica doubts it; Louis reads surveillance; king unshown. (V01) | STRENGTHEN | Stated protection; Monica doubts it; Louis reads surveillance, uses a decoy, chose Monica partly for her distrust of people, and calls himself first-prince because he dislikes the duke and Felix; the king is unshown. (V02) | See V02 reading section 9.1. | V02 evidence | Later reinterpretation, not correction. |
| SW-CR-0006 | SW-C-0006 | The prologue’s unnamed watcher is Felix. (V01) | STRENGTHEN | The prologue’s watcher is Felix. (V02) | See V02 reading section 9.1. | V02 evidence | Later reinterpretation, not correction. |
| SW-CR-0007 | SW-C-0007 | Public and private selves diverge; he removes the duke’s placements while professing he cannot defy him. (V01) | STRENGTHEN | Public and private selves diverge: he denies a talent for magic while studying it and hiding a spirit; he removes the duke’s placements while professing he cannot defy him; he must become king without wanting what is prepared for his name, holding the role while he bears it. (V02) | See V02 reading section 9.1. | V02 evidence | Later reinterpretation, not correction. |
| SW-CR-0008 | SW-C-0008 | Felix has not identified Monica as the Silent Witch. (V01) | STRENGTHEN | Felix has not identified Monica as the Silent Witch; at V02 exit he is searching the school for her and his search excludes Monica. (V02) | See V02 reading section 9.1. | V02 evidence | Later reinterpretation, not correction. |
| SW-CR-0009 | SW-C-0009 | Cyril holds an unverified suspicion from her hand and remark. (V01) | REVISE | Cyril holds an unverified suspicion from her hand and remark (V01), and at V02 links the forest mage with the Silent Witch; V02 shows no renewed link to Monica. (V02) | See V02 reading section 9.1. | V02 evidence | Later reinterpretation, not correction. |
| SW-CR-0010 | SW-C-0010 | Monica’s power is narrated through external focalizers; her own viewpoint narrates fear, comedy and small uses. (V01) | REVISE | Awe at Monica’s power is narrated through external focalizers; from V02 her own viewpoint also narrates her power, as calculation under constraint. (V02) | See V02 reading section 9.1. | V02 evidence | Later reinterpretation, not correction. |
| SW-CR-0011 | SW-C-0011 | The school treats rank as epistemic authority; Cyril’s inquiry is the first counterexample and revises her expectation. (V01) | STRENGTHEN | The school treats rank as epistemic authority; Cyril’s inquiry is the first counterexample; at V02 rank is also used as a weapon of justice (Felix, Isabelle) and Elliott’s code ties rank to duty. (V02) | See V02 reading section 9.1. | V02 evidence | Later reinterpretation, not correction. |
| SW-CR-0012 | SW-C-0012 | Organized embezzlement; erased Aaron’s and Cyril’s memories; Selma’s manipulation inferred. (V01) | PRESERVE | Unchanged (V02). | Only the investigators’ visits are shown. | — | Review, not change. |
| SW-CR-0013 | SW-C-0013 | Neither an ordinary cat nor, in Felix’s judgment, a spirit. (V01) | PRESERVE | Unchanged (V02). | No disclosure. | — | Review, not change. |
| SW-CR-0014 | SW-C-0014 | Monica regards her talent as a curse that took her father and friend; her care for Cyril projects this. (V01) | REVISE | Monica regards her talent as a curse that took her father and friend; her father was executed as a heretic for forbidden research into the body as number, and the friend turned away when she mastered chantless magic. (V02) | See V02 reading section 9.1. | V02 evidence | Later reinterpretation, not correction. |
| SW-CR-0015 | SW-C-0015 | The bond with Lana rests on a shared experience of being called boring. (V01) | STRENGTHEN | The bond with Lana rests on shared experience of being called boring and being out of place, and on mutual gestures of giving; Lana began from pride and stays from affection. (V02) | See V02 reading section 9.1. | V02 evidence | Later reinterpretation, not correction. |
| SW-CR-0016 | SW-C-0016 | The comedy of coercion registers harm in most cases; the non-consensual kiss is unevaluated and unknown to its recipient. (V01) | PRESERVE; UNTESTED | Unchanged (V02). | No recurrence of the kiss. | — | Review, not change. |
| SW-CR-0017 | SW-C-0017 | Coercion combined with investment in her self-respect and his own pride. (V01) | STRENGTHEN | Louis combines coercion with investment in her self-respect and his own pride; at V02 also gifts, an unknowing decoy, and a concession calculated to keep her cooperation. (V02) | See V02 reading section 9.1. | V02 evidence | Later reinterpretation, not correction. |
| SW-CR-0018 | SW-C-0018 | Monica’s numerical perception and comfort derive from her father’s teaching. (V01) | STRENGTHEN | Monica’s numerical perception and comfort derive from her father’s teaching; she memorized his burning numbers as proof he lived and keeps his coffee pot. (V02) | See V02 reading section 9.1. | V02 evidence | Later reinterpretation, not correction. |

## 6. Prospective questions and predictions — SW-P

Owns genuine prospective tests and open questions across source-unit boundaries.

Fields: ID; frozen wording; preparation boundary/reference; basis observations/claims; target opportunity; expected outcome if any; falsifying/weakening outcome; confidence basis; test status; eligible adjudicating observations; result/revision route.

Statuses: OPEN, TESTED_SUPPORTED, TESTED_COMPLICATED, TESTED_DISCONFIRMED, UNTESTED, or RETIRED_WITH_REASON. An open question needs no predicted answer. An absent opportunity is UNTESTED; a remembered later event is never a newly frozen prediction.

Records at V01. All were frozen at V01 closure on 2026-10-14 in the reading’s section 9.2. None carries a predicted answer: the entry freeze registered no predictions because of disclosed prior franchise exposure, and the same reason applies at exit.

| ID | Frozen wording | Basis | Target opportunity | Expected outcome | Weakening outcome | Status |
|---|---|---|---|---|---|---|
| SW-P-0001 | Who is the disciple Louis planted in the academy, and does Monica learn of it? | obs. 116 | A Louis-connected student or disclosure. | None. | — | OPEN; narrowed at V02 |
| SW-P-0002 | What is Felix’s wish, why is his life a remainder, and where does he go at night? | obs. 078, 079 | Felix viewpoint scenes. | None. | — | OPEN; partly addressed at V02 |
| SW-P-0003 | Will Felix connect Monica with the Silent Witch, and what would force it? | obs. 069, 122 | Felix witnessing or hearing of her magic. | None registered; see the bounded expectation in the reading’s section 10, which is not a prediction. | — | OPEN; pressure increased at V02 |
| SW-P-0004 | Will Cyril verify his suspicion about her hand? | obs. 111 | Repeat of the glove scene; confrontation. | None. | — | OPEN |
| SW-P-0005 | Who was the man in the dream; what happened to her father; how did talent take him? | obs. 037, 090 | Backstory disclosure. | None. | — | OPEN; largely answered at V02 |
| SW-P-0006 | Who is the Minerva friend; does he return? | obs. 090 | A Minerva acquaintance appears. | None. | — | OPEN |
| SW-P-0007 | What does the king intend, and what grounds the duke’s hold on Felix? | obs. 062, 119 | King or duke on stage. | None. | — | OPEN |
| SW-P-0008 | What is Nero? | obs. 102 | Disclosure of origin or powers. | None. | — | OPEN; UNTESTED at V02 |
| SW-P-0009 | Does Monica’s use of mind interference have consequences? | obs. 110 | Guild or Sage reaction. | None. | — | OPEN; UNTESTED at V02 |
| SW-P-0010 | What role does the Jewel Mage play? | obs. 100 | Further appearance. | None. | — | OPEN; UNTESTED at V02 |
| SW-P-0011 | Do Elliott and Bridget accept Monica; how does Elliott’s contempt meet her concealed rank? | obs. 061, 070 | Council scenes. | None. | — | OPEN; Elliott partly at V02 |
| SW-P-0012 | Do Monica’s speech gains persist and generalize to strangers? | obs. 112, 114 | Ordinary scenes with strangers. | None. | — | OPEN; partly at V02 |

Status notes and records at V02. None carries a predicted answer, for the same exposure reason. V01’s bounded expectation is discussed in the V02 reading’s section 9.3 and not scored.

| ID | Frozen wording or V02 note | Basis | Target opportunity | Expected outcome | Weakening outcome | Status |
|---|---|---|---|---|---|---|
| SW-P-0001 | V02: decoy role and traits disclosed; Glen fits; unnamed; Monica unaware. | V02 obs. 010, 015, 040, 041 | Naming or Monica learning. | None. | — | OPEN |
| SW-P-0002 | V02: must become king without desire; nights not mentioned. | V02 obs. 077 | — | None. | — | OPEN |
| SW-P-0003 | V02: Felix searches for the Witch on campus. | V02 obs. 087 | — | None. | — | OPEN |
| SW-P-0005 | V02: uncle and father’s execution disclosed; research, place, date and passage to the guardian remain. | V02 obs. 034, 044, 045 | — | None. | — | OPEN |
| SW-P-0011 | V02: Elliott shamed and protective but still calls her presumptuous; Bridget unconvinced. | V02 obs. 021, 024, 039, 063 | — | None. | — | OPEN |
| SW-P-0012 | V02: refusals, accusation and bargaining; still fails at a simple request. | V02 obs. 023, 043, 072, 095 | — | None. | — | OPEN |
| SW-P-0013 | What does MacLaggan know about Monica and Glen? | V02 obs. 016, 089 | His conduct toward either. | None. | — | OPEN |
| SW-P-0014 | What will Felix’s search for the Silent Witch lead him to do? | V02 obs. 087 | Felix scenes. | None. | — | OPEN |
| SW-P-0015 | What is the tournament Boyd intends for Monica? | V02 obs. 089 | Chess scenes. | None. | — | OPEN |
| SW-P-0016 | What explains the cluster around Felix in SW-C-0022? | V02 obs. 039, 049, 062, 093 | Any disclosure about his childhood. | None. | — | OPEN |
| SW-P-0017 | What was her father’s forbidden research, and does it relate to the Empire’s legalization of body magic? | V02 obs. 034, 035, 044 | Backstory. | None. | — | OPEN |
| SW-P-0018 | What event does Mary Harvey foresee? | V02 obs. 093 | — | None. | — | OPEN |
| SW-P-0019 | Do Casey’s confession, Count Bright and the Randall connection have consequences? | V02 obs. 080, 081, 096 | Political scenes. | None. | — | OPEN |
| SW-P-0020 | What does Claudia know or suspect beyond her jealousy? | V02 obs. 050, 118 | Claudia scenes. | None. | — | OPEN |

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

Records at V02:

| ID | Feature | Mechanism | Focalization and withholding | Wording evidence | Function and recurrence | Rival reading | Promotion reason | Obs. |
|---|---|---|---|---|---|---|---|---|
| SW-F-0010 | Power in Monica’s own viewpoint | Her magic narrated as calculation under constraint; awe kept in others. | Revises SW-F-0001; withholding moves from power to past. | Clock tower; horses; rope; barrier rewrite. | Prologue, chapters 3, 10, 11. | Exceptional scenes. | Changes how power scenes work from V02. | 004, 025, 086 |
| SW-F-0011 | Mirrored scenes | Paired scenes that invert or answer each other. | Reader alone sees both halves. | Dosed tea twice; hidden rescue and spoken name; hard and soft walls. | Chapters 7–8, prologue and 11, 11 and epilogue. | Coincidence. | Structural habit. | 005, 052, 084, 098 |
| SW-F-0012 | 場違い | One word tracks three outsiders and reverses meaning. | Social plot. | Refusal, charge, self-gift. | Prologue, chapter 6. | Common word. | Organizes class theme. | 003, 029, 031 |
| SW-F-0013 | Anonymity resolved by object | An unnamed agent identified by an object, not a name. | Fair-play withholding. | Red jewel, three rivets. | Prologue and chapter 11. | — | Technique for later mysteries. | 080, 111 |
| SW-F-0014 | Disclosure of the past in altered states | Backstory given in memory under stress and in delirium. | Reliability question. | Fire, bottle, poker. | Chapters 4 and 7. | Hallucination. | Governs evidential weight of backstory. | 034, 044, 045 |
| SW-F-0015 | Comedy and harm, V02 | Mercy and revenge played warmly; costs registered in the prose. | Harm to Cyril registered; revenge enjoyed. | Guilt tears; high laugh. | Chapter 8, epilogue. | All harmless. Criterion as SW-F-0008. | Normative continuity. | 052, 098 |
| SW-F-0016 | Performance and roles | Characters act parts: villainess, prince, friend, decoy, transfer student. | Masks within masks. | Isabelle’s lessons; Elliott on actors; Felix’s name. | Throughout. | Genre convention. | Links cover, Felix and Casey. | 055, 062, 116, 119 |

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

Records at V02, reviewer the V02 sequential integrator, 2026-10-14. Evidence reviews only; no model, profile, dialogue or tier.

| ID | Identity; state boundary | Tier considered | Readiness state | Evidence variety | Affirmative limitations | Missing evidence | Test route | Restrictions |
|---|---|---|---|---|---|---|---|---|
| SW-RD-0009 | sw.monica; V02 exit | Recognition profile | UNASSESSED. Evidence now spans two volumes, many recipients, ordinary life, crisis, negotiation and disclosed history. | Adequate for a future assessment. | Key history from delirium; romance absent. | Formal Sage duties among peers; family. | Hold-out scenes from a later volume. | No profile without separate authorization. |
| SW-RD-0010 | sw.monica; V02 exit | Domain-bounded model | INSUFFICIENT_EVIDENCE | As above. | Two volumes; politics and romance thin. | Longitudinal transitions. | Later volumes. | — |
| SW-RD-0011 | sw.felix; V02 exit | Any tier | INSUFFICIENT_EVIDENCE | Rich private scenes added. | Affirmative limitation: identity cluster unexplained; public statements unreliable. | Disclosure of SW-C-0022 matters. | Later disclosure. | Public behaviour is not interior evidence. |
| SW-RD-0012 | sw.cyril, sw.louis, sw.elliott, sw.casey, sw.lana, sw.claudia, sw.isabelle and all other identities; V02 exit | Any tier | INSUFFICIENT_EVIDENCE | Cyril, Louis, Elliott and Lana gained viewpoint scenes. | Casey removed from the school. | More ordinary scenes. | Later volumes. | Keep thin entries thin. |

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
| Editorial revision | 2026-10-14: reading version 1.1 named-subject and referential-clarity repair, with one recorded erratum aligning the synopsis to SW-C-0009; no claim, observation, locator, quotation or freeze changed; two ledger cells in SW-S identities and SW-R-0013 clarified from “his spirit” to Wildianu. See the V01 named-subject editorial audit. |

Records at V02:

| Field | SW-U-V02 |
|---|---|
| Witness and unit | `SW-LNJP-V02`, Japanese LN Volume 02. |
| Source lock and locator fidelity | Byte-locked 2026-10-14 in the source lock register; package built with the generalized driver; every quoted fragment and cited locator in the reading verified against the sealed block map. |
| Prose coverage | Complete: prologue, eleven chapters with continuation, epilogue, secret episode. |
| Image coverage | Complete: all 29 image resources accounted for; every admitted image viewed; preview images excluded. |
| Paratext coverage | Complete: contents, credits, afterword, colophon, notices, jacket; publisher preview excluded. |
| Inspection | Completed 2026-10-14. |
| Semantic review | Author self-review with leakage check and name-and-reference check; owner acceptance not claimed. |
| SW-S | SW-S-0025 to SW-S-0044. |
| SW-R | SW-R-0023 to SW-R-0042. |
| SW-K | SW-K-0021 to SW-K-0034. |
| SW-W | SW-W-0025 to SW-W-0040. |
| SW-C / SW-CR | SW-C-0019 to SW-C-0026; SW-CR-0001 to SW-CR-0018 on all V01 claims. |
| SW-P | SW-P-0013 to SW-P-0020 added; twelve statuses noted; no predictions. |
| SW-F | SW-F-0010 to SW-F-0016. |
| SW-RD | SW-RD-0009 to SW-RD-0012, evidence reviews only. |
| Exit freeze | `SW-FR-V02-EXIT` in the reading’s section 10. |
| Durable closure | The commit that adds the V02 reading and these records; receipts in Git history. |
| Remaining mandatory evidence | None. |
| Remaining optional evidence | Publisher-original comparison; printed pagination; web comparison. |
| Architecture review | Not due: no supplemental admission, no ledger pressure; recorded as reviewed in the architecture at V02. |

## Write, amend, and split rules

The authorized sequential integrator appends source-bearing state and revision events after full unit inspection. Patch current claim/readiness views only with preserved prior events. Record every affected responsibility's material delta or explained no-update in the unit closeout. Coverage completion never mechanically promotes an inference or readiness level.

Correct an objective error through an explicit correction event retaining old/new evidence routes and affected homes. Later reinterpretation is a source-bounded revision, not a rewrite of the historical freeze. If a record cannot be supported, defer or mark uncertainty rather than padding a table.

Split a typed responsibility only after recurring evidence establishes independent retrieval/revision pressure or a separate specialist dependency. Record exact transferred IDs, ownership, new path and necessary bounded backfill in architecture/entrypoint. Preserve historical routes and prohibit duplicate live datasets. Architecture-defined split decisions, not arbitrary row counts, govern this transition.
