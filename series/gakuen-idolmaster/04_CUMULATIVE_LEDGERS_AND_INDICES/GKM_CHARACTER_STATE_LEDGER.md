---
title: "Gakuen Idolmaster V2 - Character State Ledger"
project: "Gakuen Idolmaster"
document_type: "persistent ledger"
version: "2.17"
source_lock: "GAKUMAS V2 Source Lock 1.0"
initialized: "2026-08-13"
last_updated: "2026-11-25 — Carbon write-through and written Event 024 attribution; written Event 023 revision"
status: "active; cumulative through complete Phase-3 character audiovisual integration (13/13)"
---

# CHARACTER STATE LEDGER

> **REVISE — v2.17, 2026-11-25. Hiro’s written Event 023 outcome.** The earlier entry described Hiro as accurately reading her friends. The event establishes that Hiro brings Temari a clue, supports her choice and reports the outcome to Misuzu. Hiro marks her reading of Misuzu’s intention as conditional. The previous wording is preserved in v2.16.

This is a cumulative V2 project ledger. It is initialized in Phase 0 and must be updated rather than recreated as later phases add evidence.

## Schema

| field | meaning |
| --- | --- |
| character |  |
| story_state |  |
| source_id |  |
| self_concept |  |
| desire |  |
| fear_or_constraint |  |
| behavior_delta |  |
| confidence |  |
| notes |  |

## Seed entries

No substantive entries are asserted at Phase 0. The schema is intentionally initialized before close reading so later evidence can be added without changing data conventions.

## Phase 3 — Hanami Saki / 花海咲季

These entries describe the Saki core corpus. `D-SAKI` and `U1` remain separate personal-history tracks. Produce-result rows are branch-scoped rather than additive.

| character | story_state | source_id | self_concept | desire | fear_or_constraint | behavior_delta | confidence | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Hanami Saki | D-SAKI early selection | `adv_dear_hski_001–003` | fast-learning all-rounder who calls herself a future world-best idol but anticipates plateau | become top idol and remain a person worth choosing | future stagnation; Ume's higher ceiling; loss of identity after being overtaken | accepts a Producer who explicitly selects the feared future rather than only the current ace | high | “false genius” is Saki's self-description, not an adequate external diagnosis |
| Hanami Saki | D-SAKI childhood reconstruction | `adv_dear_hski_008–010` | `無敵のお姉ちゃん` maintained by winning early and changing fields before Ume fully catches her | make Ume's belief in her older sister true | being caught and losing the vertical sister relation | admits `勝ち逃げ`, exposes the avoidance inside former invincibility, and makes “world's best” an explicit promise | high | historical victories remain real; the correction concerns how superiority was preserved; Dear 009 also holds the first direct win over Ume (next row, GKM-SAA-005) |
| Hanami Saki | P1 conditional body-development states | `adv_pstory_001_hski_after-step-1-normal-01..03`; `after-step-2-normal-*` | athlete attempting to convert an optimized sports body into an idol body | preserve competitive force while becoming vocally, visually, and physically stage-suitable | muscle/weight history, throat risk, technical plateau | accepts Producer-guided redesign, recovery, and technical specialization | high within P1 | conditional scene pool; do not concatenate every variant into one run |
| Hanami Saki | P1 result ladder | `adv_pstory_001_hski_after-audition-mid-*`; `after-audition-final-*`; `ending-*` | first place is the only fully satisfying result, but every outcome becomes diagnostic material | win and prove that the selected future can grow | failure, “barely” success, or praise that sounds like completion/ceiling | shock/rage gives way to postmortem, renewed training, and another challenge in most ordinary branches | high, branch-scoped | major later defeat shows this micro-cycle has limits |
| Hanami Saki | D-SAKI first direct Ume contest | `adv_dear_hski_009`; `adv_dear_hski_011–012` | older sister who cannot rely on technical superiority but can still construct victory | defeat stronger Ume without fleeing the field | Ume's raw ceiling and Saki's own protected history | wins narrowly in Dear 009 on idol appeal and visible desperate effort while conceding that Ume surpassed her in singing, dance and almost every measurable dimension; Dear 011–012 set up the N.I.A. and end in a tied ranking contest, and the FINALE is won in Dear 019; rivalry becomes durable rather than avoidable (GKM-SAA-005) | high | victory is not proof that Saki has the better natural ceiling |
| Hanami Saki | P2 / N.I.A. | `adv_pstory_002_hski_*`; `adv_dear_hski_013–020` | public competitor whose force now includes fans and Producer strategy | win the FINALE and expand beyond family-only recognition | fan-vote pressure; external rivals; future Ume contest still unresolved | treats fans as both pressure and `外付けの筋肉`, then begins to encounter fandom as lived participation and obligation | high | fan relation remains both genuine and instrumental |
| Hanami Saki | D-SAKI summer H.I.F. loss | `adv_dear_hski_021–023` | older sister determined to perform dignity even as her defining hierarchy collapses | congratulate Ume, preserve the relation, and demand a rematch | first unambiguous loss to Ume; fear that she failed as an older sister | chooses another run immediately but later admits prolonged crying and identity collapse | high | action recovery precedes affective and identity recovery |
| Hanami Saki | D-SAKI Project Stardust | `adv_dear_hski_024–027` | `もっとも弱い花海咲季` who can no longer depend on the old invincible persona | find a form that can win without denying breakage | grief, shame, technical inferiority, Producer's failed ideal | trains with Sena, Rinha, Tsubame, family resources, Producer, and past selves; wins while still visibly weak | high | relational laboratory; does not prove autonomous recovery |
| Hanami Saki | D-SAKI post-loss reconstruction | `adv_dear_hski_027–035`; `adv_cidol-hski-3-017–018` (`017_01` is set the day after the N.I.A. win, before the summer H.I.F.; `017_02–03` and `018_01` follow the summer H.I.F.; GKM-SAA-168, placement per CORE-Saki §16.7) | `不屈`: a self allowed to fall and break while continuing | make the Producer's overwritten dream answer to the Saki who actually exists | dependence, possessiveness, pressure of being the Producer's singular dream | converts abandoned fields, hobbies, songs, failures, and relationships into a plural competitive repertoire | high | accumulation is liberating but can instrumentalize ordinary life |
| Hanami Saki | D-SAKI winter H.I.F. victory | `adv_dear_hski_036–037` | Prima Stella as public older sister and front-runner rather than completed legend | lead the next race, challenge Ume again, and make the title a beginning | singular hierarchy and responsibility of being the visible front | transforms victory speech into open invitation/challenge: `全員わたしについてきなさい` / `お姉ちゃんが先陣を切るわ` | high within D-SAKI | may be a generous hierarchy, not egalitarian transcendence |
| Hanami Saki | U1 unit formation | `adv_unit_01-01_03`; `01-01_12..14`; `01-02_15`; `01-03_01` | initially imagines a two-person Saki/Producer agency and rejects unit dilution | maximize her own path to the top | Kotone/Temari may redirect resources and challenge her competence | revises judgment after evidence of their strength, recruits Temari as `心強い<r=ライバル>仲間</r>`, accepts variable centers and care roles | high within U1 | U1 is a parallel ensemble track |
| Hanami Saki | U1 old-rules summer H.I.F. | `adv_unit_01-04_04..25` | competitor who can make collective excellence increase individual challenge | win as Re;IRIS and then win the singular Prima Stella contest | Begrazia's technical superiority; conflict between unit victory and individual scarcity | contributes to unit recovery, wins the unit division, then becomes summer Prima Stella; institutional verdict names an idol who cultivates idols | high within U1 | cannot be merged with D-SAKI's Ume-champion summer outcome |
| Hanami Saki | C-SAKI song self-audit | `adv_cidol-hski-3-000`; `008`; `015`; `017–019` | many public Saki forms can coexist rather than replacing one another | expose weakness without surrendering authorship; make inherited/shared songs answer to Saki | fear of being seen as pathetic or derivative | uses songs as controlled disclosure and competitive appropriation | high textually; AV pending | exact chronology among communications remains C2/C4 unless internally linked |
| Hanami Saki | PE-SAKI ordinary work ecology | Saki Produce Event corpus | competent self-manager, researcher, worker, and advice-giver | turn unfamiliar contexts into usable competence | tendency to optimize before listening; friendship vulnerability | repeatedly observes, researches, apologizes, and revises methods when evidence contradicts her | moderate-high, C3 | full event/support passes may supply counterexamples |

## Phase 3 AV addendum — Hanami Saki

| character | story_state | AV/text source | self_concept / performed state | behavior delta | confidence | notes |
| --- | --- | --- | --- | --- | --- | --- |
| Hanami Saki | C-SAKI FMW | `AV-DIA-SAKI-006`; `AV-MUS-SAKI-001` | exposed weakness can be praised and staged without losing command | uses Producer recognition as ignition; public confidence returns with seams visible | high | confirms confidence as production technology |
| Hanami Saki | D-SAKI summer loss | `AV-DIA-SAKI-001` | older-sister truth, raw frustration, and next-action command coexist | behavioral recommitment precedes emotional recovery; then explicit dependence | high | sharpens failure model |
| Hanami Saki | D-SAKI Project Stardust | `AV-DIA-SAKI-002` | weakest Saki can win while lacking confidence | accepts `不屈` as identity only after extended doubt and recognition | high | `無敵` → `不屈` confirmed |
| Hanami Saki | C-SAKI post-loss | `AV-DIA-SAKI-003` | regulated intimate Saki can become another person's witness | invites Producer weakness and returns a usable interpretation | high | revises one-way dependency model |
| Hanami Saki | D-SAKI pre-final | `AV-DIA-SAKI-004`; `AV-MUS-SAKI-005` | accumulated selves and songs form the present performer | actively accepts expectation and gathers prior selves into stage ignition | high | exclusivity remains ethically open |
| Hanami Saki | D-SAKI winter victory | `AV-DIA-SAKI-005` | Prima Stella as public older sister/front-runner | formal gratitude becomes open challenge and summons to follow | high | generative hierarchy, not egalitarian closure |
| Hanami Saki | musical cross-section | `AV-MUS-SAKI-001..011` | personal sonic home plus portable performance procedure | remains legible across common, inherited, theatrical, and unit material | high AV; stems absent | identity is adaptable, not genreless |
## Phase 3 — Tsukimura Temari / 月村手毬

`D-TEMARI` and `U1` remain separate personal-history tracks. Produce result states are conditional rather than additive.

| character | story_state | source_id | self_concept | desire | fear_or_constraint | behavior_delta | confidence | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Tsukimura Temari | D-TEMARI early | `adv_dear_ttmr_001–004` | fallen former center; exceptional singer whose present life/body no longer sustain the image | become a universally recognized top idol | public SyngUp stigma; inferior stamina; dependence on former members | accepts present-tense selection and begins following evidence-based food/body guidance | high | first trust is debt repayment, not emotional surrender |
| Tsukimura Temari | D-TEMARI SyngUp reconstruction | `dear 004`, `007–009` | person whose full output was possible because superior members regulated her | sing at her own pace without being kept small | kindness proves inferiority; safety resembles dependency | reconciles with Misuzu but refuses unit reunion; chooses dangerous Producer partnership | high | need changes form rather than disappearing |
| Tsukimura Temari | D-TEMARI origin | `dear 010` | manufactured idol fleeing a hated lazy/dependent child self | become someone she can love | rest may restore the hated self; artificial wings feel counterfeit | accepts that effortful construction can be more compelling than effortless genius | high | late phases must test self-love outside ascent |
| Tsukimura Temari | P1 branch set | `adv_pstory_001_ttmr_*` | first place and complete performance validate the current construction | sustain song and win | body/stamina, weight/food, praise that sounds imprecise | turns results into direct postmortem and next tasks; accepts rest when performance-rationalized | high branch-scoped | hurt is real; rapid action is not emotional invulnerability |
| Tsukimura Temari | D-TEMARI N.I.A. promotion | `dear 012–014` | mysterious/cool singer whose actual volatility keeps escaping the plan | become publicly legible without surrendering strength | fear, anger, peer-protective impulses, social media exposure | adopts a gap-based public image integrating big mouth, fear, tears, and technical authority | high | authored exposure vs institutional extraction remains open |
| Tsukimura Temari | D-TEMARI Rinha confrontation | `dear 015–017` | student/rival whose song, dance, and cool persona were built through Rinha | defeat Rinha and force the unfinished relationship to continue | retirement/abandonment; shame of imitation; old public scandal | admits inheritance publicly, collapses into need, and clarifies the three incompatible founding promises | high | imitation becomes inheritance rather than fraud |
| Tsukimura Temari | D-TEMARI N.I.A. victory | `dear 018–020` | openly contradictory idol whose tears and audacity are now public power | defeat Misuzu and make her a rival | Misuzu may remain caretaker rather than equal | wins, demands pursuit, accepts Misuzu's refusal to run, and makes Producer success part of her dream | high | rivalry requires separate pace and right to refuse |
| Tsukimura Temari | D-TEMARI summer H.I.F. | `dear 021–023` | fan/rival confronted by Misuzu's scale and Sena's title | prove herself against models she genuinely admires | inferiority resurgence; another person looks like the “real idol” | loses, accepts Producer frustration without false consolation, accepts SyngUp training and agrees with the Producer's veto to defer the dissolution live until after winter H.I.F. (GKM-SAA-121) | high | Sena is summer incumbent in this track |
| Tsukimura Temari | D-TEMARI winter preparation | `dear 024–035`; `cidol 016`, `018` | socially constructed singer whose artificial wings can be expanded | become top idol through accumulated rivals and collaborators | overextension, imitation anxiety, exclusivity, dangerous contracts | uses Rinha/Misuzu/China/Gokugetsu/Saki/Producer as differentiated resources; redefines cool as blue flame | high | collaboration is not loss of authorship |
| Tsukimura Temari | D-TEMARI winter victory | `dear 036–037` | Prima Stella whose title is a platform for further attack | transform title toward world No. 1 and keep growing with Producer | self-love may remain achievement-conditioned | credits supporters, rejects custodial defense, calls the meeting and accepts the Producer's ramen proposal (GKM-SAA-006), affirms today's self and today's Producer | high within track | present-tense self-love is real but not yet stress-tested |
| Tsukimura Temari | C-TEMARI song/persona | `cidol 000`, `001`, `002`, `007`, `009`, `015`, `016`, `018` | multiple selves can be selected, performed, inherited, and revised | make contradiction communicable through song | fear that construction/borrowed style makes her false | admits resemblance to songs, treats persona as best costume, accepts help, defines cool as complete combustion | high textually; AV pending | numeric episode order is not exact global chronology |
| Tsukimura Temari | PE-TEMARI | Produce Event corpus | cool stage specialist who remains socially/occupationally uneven | become competent beyond song without losing directness | fear, food guilt, crafts/school/work weakness, romantic overreading | studies scripts, asks advice, sometimes apologizes/revises; often uses song/honesty to compensate | moderate-high C3 | full event/support passes may revise pattern |
| Tsukimura Temari | U1 Re;IRIS formation | Unit Story 01 | former failed-unit member who distrusts intimate teamwork | work with peers without recreating SyngUp containment | fear of hurting loved friends; exclusive Producer attachment | accepts Saki/Kotone's blunt noncaretaking partnership, rotating centers, Kotone leadership | high within U1 | separate ensemble track |
| Tsukimura Temari | U1 embodied/relational state | Unit Story 01 | technically forceful singer with persistent bodily care needs | contribute without being treated as a machine | cold body, food conflict, old Misuzu habits, Kotone's financial risk | recognizes person-specific care, apologizes, shares responsibility, teaches Ume | high within U1 | demonstrates capacity, not D-TEMARI chronology |

## Phase 3 — Fujita Kotone / 藤田ことね

`P1[KOTONE]`, `P2[KOTONE]`, `D-KOTONE`, `C-KOTONE`, `PE-KOTONE`, and `U1` remain track-scoped rather than automatically additive.

| character | story_state | source_id | self_concept | desire | fear_or_constraint | behavior_delta | confidence | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Fujita Kotone | D-KOTONE early precarity | Dear 001–004 | inferior student and overworked provider with hidden capacity | become rich through idolhood and reduce family burden | tuition, debt, exhaustion, poor visible results | accepts rest and better-paid idol work only after Producer intervention | high | first improvement is removal of constraint |
| Fujita Kotone | P1 branch set | `adv_pstory_001_fktn_*` | idol career feels like a tightrope | continue school/idolhood, earn, prove viability | one failure may feel like career/household collapse | cries, converts distress into next action, still seeks praise | high branch-scoped | result branches are conditional |
| Fujita Kotone | D-KOTONE family/debt revelation | Dear 009–011 | self-appointed family fixer who believes she increased parental burden | reverse household fortunes | guilt, debt, overwork, perceived father abandonment | lets Producer/institution intervene in debt, budget, rest, work | high | concrete social/financial production |
| Fujita Kotone | D-KOTONE Sena/N.I.A. | Dear 012–020 | former fan becoming publicly legible rival | defeat a star she genuinely admires; make everyone enjoy the stage | successor scripting, durable self-doubt, public ranking | rejects successor role; demands reciprocity as rival; broadens audience beyond fan ownership | high | `スター性` names nonquantified social effect |
| Fujita Kotone | P2/N.I.A. branches | `adv_pstory_002_fktn_*` | successful idol who fears reverting to `劣等生` | make transformation durable | failure can reactivate rebirth/abandonment narrative | uses Producer/Sena support, keeps competing | high branch-scoped | no dedicated Kotone Series-3 pstory in Source Lock |
| Fujita Kotone | D-KOTONE H.I.F. | Dear 021–025 | confident/unconfident rival and audience host | justify every ticket and count as Sena's true rival | comparative doubt about Sena and the ideal, comparative inferiority, loss (GKM-SAA-122) | focuses on spectators during live; professionally reframes loss then admits grief | high | career value ≠ emotional recovery; the `超自信` / `超自信がない` formula is the Producer's, endorsed by Kotone (GKM-SAA-122) |
| Fujita Kotone | D-KOTONE debt completion | Dear 026–027 | idol finally able to live ordinary professional risk | ordinary training/auditions/lives, top-idol future, chosen wealth | discomfort with one-way receiving | earns final debt target, celebrates `普通`, accepts top-idol goal as repayment | high | `普通` is class/psychological climax; repayment frame remains ethically open |
| Fujita Kotone | C-KOTONE public self | cidol 000/001/007/013/016/019 | cute, greedy, socially skilled self can be usable art | praise, audience pleasure, income, upward mobility | technical comparison, fear of replacement, negative viewer response | integrates greed/weakness into songs; formalizes fanservice; restores visible enjoyment | high textually; AV pending | performance is selective amplification, not mask reveal |
| Fujita Kotone | PE-KOTONE work ecology | Produce Event corpus | economically literate service professional in training | earn as an idol and make spending less frightening | fatigue, job variability, school/work conflict | rapidly adapts to public-facing tasks, calculates value, studies work grammar | moderate-high C3 | later event/support phases may revise |
| Fujita Kotone | U1 Re;IRIS | Unit Story 01 | practical/social member of a high-conflict trio | collective success without erased individuality | money/material anxiety, stronger-looking specialist peers | contributes leadership/care and distributed-center functioning | high within U1 | comparative evidence only; separate continuity |


## Phase 3 — Arimura Mao / 有村麻央

`D-MAO`, individual Produce tracks, modular communications, and `U1` remain continuity-distinct. Result branches are possibility-space evidence rather than one additive biography.

| character | story_state | source_id | self_concept | desire | fear_or_constraint | behavior_delta | confidence | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Arimura Mao | D-MAO child-actor reconstruction | `adv_dear_amao_003`; `adv_cidol-amao-3-015_01..03` | child actor who genuinely wanted the prince/boy stage position | remain the kind of performer she admired | puberty changes body/casting fit; lack of height closes former category | turns prince-coded appearance into resistance against category loss | very high | desire is authentic even though later fixation becomes defensive |
| Arimura Mao | D-MAO early scouting | `adv_dear_amao_001–004` | dorm-leader “prince” who expects adults to demand a cute rebrand | shine without surrendering the prince | prior adults treated cuteness as replacement; Producer's diagnosis threatens same injury | accepts a Producer who researches her history and proposes integration rather than erasure | very high | Producer still exercises strong interpretive power |
| Arimura Mao | D-MAO early reconstruction | `adv_dear_amao_004–009` | self whose cute and cool aspects can coexist without either being the whole truth | become `可愛いとカッコイイを兼ね備えた、無敵の王子様系アイドル` | embarrassment, old defensive habits, audience-blind role projection | experiments with clothing, hair, food, song interpretation, and audience-directed performance | high | merely “acting cute” is explicitly rejected as same old problem |
| Arimura Mao | C-MAO `Fluorite` | `adv_cidol-amao-3-000_01..03` | transformable self whose identity is relationally produced | keep changing without losing continuity | fear that external influence could again dictate who she is | formulates `ボクらしさ` as emerging between self and others | very high textually | modular chronology; philosophical importance high |
| Arimura Mao | D-MAO Shion conflict | `adv_dear_amao_013–016` | person who can name the old prince fixation as `呪い / 呪縛` without repudiating the dream | reclaim princehood as something voluntarily enacted | accusation that she is a `偽物の王子様`; child-actor comparison | distinguishes harmful binding from `ちゃんと本物` aspiration and chooses to keep performing | very high | decisive anti-“fake prince → true cute girl” evidence |
| Arimura Mao | D-MAO N.I.A./Gekka | `adv_dear_amao_018–020`; P2 | challenger whose self-acceptance does not erase external standards | defeat stronger rivals and make the Little Prince publicly meaningful | huge technical gap; tendency to protect/challenge when strategically unnecessary | accepts crowd response while explicitly acknowledging skill deficit; reauthors `リトルプリンス` | high | public recognition is accepted, not simply obeyed |
| Arimura Mao | D-MAO 100Pro transition | `adv_dear_amao_021–026` | future professional who treats the Producer relation as part of chosen identity | obtain professional resources without surrendering coauthorship | Ryuusei argues student Producer is inadequate; separation threatens shared dream | refuses replacement, chooses “all of it,” and calls that `ボクらしい選択` | very high | autonomy and dependency risk coexist |
| Arimura Mao | D-MAO summer H.I.F. loss | `adv_dear_amao_027` | public challenger able to frame defeat forward while privately devastated | surpass awakened Sena and continue toward winter | severe loss after large investment; senior/prince composure | cries `負けた` unguarded at the result with the Producer, frames the loss composedly afterwards, grieves inwardly about not going pro with the Producer now, and breaks down in front of Rinami after the party; returns to challenge (GKM-SAA-012) | very high | behavioral recommitment ≠ emotional recovery |
| Arimura Mao | D-MAO winter preparation | `adv_dear_amao_028–035` | actor, senior, rival, and heir who can use observation and received care as resources | become the visible challenger who can draw Sena back into relation | protector habits; inherited obligations; still-large summit | trains across cast, repays senior care, accepts fear/awkwardness as princely material | high | “rescue” language may still preserve hierarchy |
| Arimura Mao | D-MAO winter victory | `adv_dear_amao_036–037` | Prima Stella and theatre-center `0番` who remains unfinished | make visibility generative and keep reaching toward the ideal | singular title could harden into endpoint/possession | distributes credit/light, enters 100Pro with Producer, chooses continuing transformation | very high within D-MAO | Mao's title ethic is not a universal Hatsuboshi rule |
| Arimura Mao | C-MAO succession | `adv_cidol-amao-3-007_01..03`; `009`; `013`; `017` | inheritor of school songs, senior care, theatrical craft, and relationships | become a source from which others can inherit and alter aspiration | own desire can hide inside service role | teaches Kotone, imagines future entrants, admits personal desire for memories, uses Rinami relation as performance resource | high | later support/event passes should test breadth |
| Arimura Mao | U1 dorm leadership | selected `adv_unit_01-*` Mao passages | responsible senior who moderates rather than preempts all peer conflict | protect juniors while allowing them to form their own relation | over-responsibility and prince hierarchy | permits Saki/Temari conflict under bounded supervision and supports Kotone before H.I.F. | high within U1 | separate ensemble track; not pasted into D-MAO biography |

## Phase 3 - Katsuragi Lilja

`D-LILJA`, P1/P2, conditional P3 fragments, and modular communications remain continuity-distinct. Dear 036 is a D-LILJA result, not a universal winter-H.I.F. result.

| character | story_state | source_id | self_concept | desire | fear_or_constraint | behavior_delta | confidence | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Katsuragi Lilja | D-LILJA origin | `adv_dear_kllj_001-004` | technically weak beginner who sees desire as presumptuous | become an idol despite lacking visible school-salient strengths | exposure, comparison, migration, low self-confidence | accepts Producer naming `strong will` as a talent and begins structured training | very high | courage is named relationally before it is self-owned |
| Katsuragi Lilja | D-LILJA audience formation | `adv_dear_kllj_003-010` | frightened performer learning that stage work is address | make current self reach Sumika/audience | execution consumes attention; fear of disappointing spectators | shifts from correctness to delivery; first live returns courage to Sumika | very high | Sumika is first specific addressee |
| Katsuragi Lilja | D-LILJA N.I.A. | `adv_dear_kllj_011-020` | growing idol who still treats low talent as premise | validate Producer, fans, and own aspiration | insult, rankings, overwork, bodily expendability | learns fan-number distinction, sustains injury, accepts trust/rest, defeats Shion | very high | effort requires governance |
| Katsuragi Lilja | D-LILJA post-summer-H.I.F. | `adv_dear_kllj_021-026` | hardworking idol whose technical ceiling is newly visible | reach H.I.F. level and identify own weapon | weak basics, narrow performance bandwidth | submits to Shion's logic-first basics; discovers intermittent visual/charismatic world-making | very high | `talentless` must be taxonomically revised |
| Katsuragi Lilja | D-LILJA REVERSI formation | `adv_dear_kllj_027-030` | former follower becoming unit initiator/leader | stand beside Sumika and fulfill promise | fear of dragging Sumika down; low unit visibility | proposes same dream, leads relationally, publicizes shared history | high | intimacy becomes strategy as well as relationship |
| Katsuragi Lilja | D-LILJA teammate-rival | `adv_dear_kllj_031-035` | partner capable of separate desire inside attachment | win as REVERSI and personally become Prima Stella | fear individual wanting could split shared dream | accepts `want what you want`; becomes `teammate and rival` with Sumika | very high | differentiation is maturation |
| Katsuragi Lilja | D-LILJA Prima Stella | `adv_dear_kllj_036-037` | publicly validated courage-transmitter who remains unfinished | keep accumulating beyond fulfilled promise | summit could harden into endpoint; shared dream ends | credits support network, accepts title, then moves toward separate future dreams | very high within D-LILJA | track-scoped result |
| Katsuragi Lilja | C-LILJA visual identity | `adv_cidol-kllj-3-015_01..03`; Dear 024-026 | shy person who can consciously author a fantastical visual field | give courage through a world audiences can enter | self-consciousness and intermittent charisma | appropriates styling, props, fantasy vocabulary, and `Katsuragi barrier` | high textually; AV pending | coauthored, not discovered essence |
| Katsuragi Lilja | C-LILJA cultural/fandom self | cidol 005/012/018; Produce Events | quiet Swedish-Japanese student with intense anime/game/fantasy interior | connect private pleasures, family history, and idol work | family distance, unfamiliar environment, tendency to instrumentalize leisure | lets fandom/culture become pleasure and performance authorship | high | Japanese is proficient; cultural adjustment still real |
| Katsuragi Lilja | P2 result states | `adv_pstory_002_kllj_*` | idol increasingly able to claim outcomes | keep moving after win/loss | success called luck; failure once felt predetermined | starts treating loss as violation of legitimate desire rather than proof of inferiority | high branch-scoped | self-credit remains incomplete |
| Katsuragi Lilja | P3 conditional REVERSI fragments | `adv_pstory_003_kllj_*` | unit member facing singular high-stakes results | fulfill shared promise and continue after failure | unit balance/performance failure | selection/final failures produce grief and recommitment rather than bond dissolution | high branch-scoped | four fragments only, not full P3 route |
| Katsuragi Lilja | ordinary life/work | selected Produce Events | student, cook, fan, worker, friend, daughter as well as idol | build life in Japan and do public-facing work | overwork, school adaptation, family distance | studies, cooks, promotes products, rests imperfectly, cares for Producer | moderate-high C3/C4 | later event/support phases may revise |
## Phase 3 — Kuramoto China / 倉本千奈

`D-CHINA`, P1/P2, conditional P3 fragments, and modular communications remain continuity-distinct. Dear 036 is a D-CHINA result, not a universal winter-H.I.F. result.

| character | story_state | source_id | self_concept | desire | fear_or_constraint | behavior_delta | confidence | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Kuramoto China | P1 true ending | `adv_pstory_001_kcna_ending-true-01` | materially secure girl with few self-authored stakes | find something worth continuing through pain | sheltered noncommitment; little history of serious frustration | discovers jealousy, defeat, gratitude and persistence as personally owned experiences | very high | deepest initial deficit is not material poverty |
| Kuramoto China | D-CHINA early | Dear 002–005 | accurate bottom-rank beginner with little defensive pride | become a real idol without pretending she is skilled | weak stamina/flexibility/fundamentals | accepts humiliating correction and slow remediation | very high | trainability is distinct from talent |
| Kuramoto China | D-CHINA privilege audit | Dear 006–011 | privileged beginner who fears advantage contaminates legitimacy | use what she has without abusing it | family name/money/visibility can command outcomes | formulates `濫用` boundary; rejects commanded affection and accepts legitimate aid | very high | stewardship, not renunciation |
| Kuramoto China | D-CHINA N.I.A. | Dear 012–020 | `世界で一番未熟な一流アイドル` | become first-rate through the full social ecology of idolhood | tendency to under-credit relational power | recognizes fans as constitutive force rather than aggregate metric | very high | institutional `本来の実力` doctrine remains normatively open |
| Kuramoto China | D-CHINA election | Dear 021–027 | possible successor who cannot simply inherit Sena's legitimacy | become student-council president as Kuramoto China | alliance can look like installed succession; personal skill gap | adopts Liu-Bang leadership but insists on solo final comparison with Sena | very high | interdependence contains nondelegable accountability |
| Kuramoto China | D-CHINA H.I.F. setup | Dear 028–033 | leader using `仮面`, allies and inherited resources | win without hiding behind `まぐれ` language | raw ability still below elite peers; fear of overclaiming | improves technically, redistributes resources to Hiro, accepts others' recognition | high | self-credit becomes socially ratified |
| Kuramoto China | D-CHINA integrated persona | Dear 034–035 + direct AV | receptive softness `ふにゃ` and organized authority `きり` inside one stable identity | face Sena as genuine rival | public authority can become exhausting or compulsory poise | motion, timing and register show a permeable owned role rather than false mask | very high / AV verified | performed role is authentic, effortful and revisable |
| Kuramoto China | D-CHINA victory | Dear 036–037 | Prima Stella who can claim a relationally produced win but not yet fully self-name top idol | become summit others can aim at | persistent under-crediting; dependence on Producer/witnesses | says `勝ったのは、わたくしです`; publicly commands aspiration; later admits top-idol self-name still premature | very high within D-CHINA | victory and unfinished self-credit coexist |
| Kuramoto China | C-CHINA family roots | cidol 009 | loved heir aware affection has history and hierarchy | answer care without treating people as invisible infrastructure | household power asymmetry; gratitude can become debt | recognizes Kanae/family history and `愛された責任` | high | later support/event evidence should test repayment compulsion; cidol 009 never names the apprentice, so the Kanae identification rested on inference under Source Lock 1.0 and is explicit in China's own words under Source Lock 1.2 (`adv_dear_hkne_001` L425) (GKM-SAA-212) |
| Kuramoto China | C-CHINA song authorship | cidol 014 + `空と約束` commu/3DMV | performer able to define present intention and audience before mobilizing inherited production resources | make current intention publicly answerable | strong Producer/institution production power | coauthors purpose without pretending solitary creation | very high / AV verified | collaborative authorship is still authorship |
| Kuramoto China | Phase-3 integrated AV | Dear 001–037; six song commus; performances/MVs | **accountable inheritance realized as receptive authority** | receive, register, organize and answer for love, capital, correction, tradition, rivals and trust | responsible privilege does not guarantee distributive fairness; gratitude can become debt | uses permeable `わたくし/ですわ` identity, trained public role, curiosity and reciprocal performance to convert inheritance into governed action | very high within current AV boundary | Phases 4–6 must reopen ordinary-life, support-card and ensemble pressure |
## Phase 3 — Shinosawa Hiro / 篠澤広

`D-HIRO`, P1/P2, conditional P3 fragments, and modular communications remain continuity-distinct. Dear 036 Prima Stella is D-HIRO only.

| character | story_state | source_id | self_concept | desire | fear_or_constraint | behavior_delta | confidence | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Shinosawa Hiro | pre-idol / D-HIRO origin | Dear 001/005 | accelerated genius bored by effortless competence | find an arena that resists her | most ordinary achievement feels predetermined | chooses the job least suited to her and calls the process `趣味` | very high | difficulty is entry mechanism, not final endpoint |
| Shinosawa Hiro | D-HIRO bodily floor | Dear 002/004/006/007; P1 | physically fragile beginner with near-zero conventional idol readiness | make resistance durable enough to continue | stamina, flexibility, weight/health, collapse | accepts unusually low-load conditioning while repeatedly asking for harder tasks | very high | subjective desire for pain does not erase safety constraints |
| Shinosawa Hiro | D-HIRO jealousy hinge | Dear 008-010 | hobbyist discovering attachment | perform because she now loves idolhood and hates being left behind | first meaningful defeat/comparison | names first `悔しい`, realizes `好き……アイドルが`, demands immediate live | very high | first nonoptional value |
| Shinosawa Hiro | P2 | Series 2 result states | idol for whom low ability alone is no longer enough | improve and compete without losing difficulty | success could once threaten boredom | admits `それだけじゃ……だめ`; expected success and praise become more tolerable | high branch-scoped | resistance + achievement coexist |
| Shinosawa Hiro | D-HIRO N.I.A. | Dear 011-020 | odd hobbyist becoming fan-aware rival/friend | repay attention and share a dream | audience obligation, father questions use of talent | accepts fans, China/Ume rivalry, NIA win, `趣味のまま、夢` | very high | hobby remains; dream is additive |
| Shinosawa Hiro | D-HIRO image | Dear 021-027 | technically weak but charismatic idol split between goddess reading and cute desire | make public artifact plural without falsifying herself | beauty/`神格` can overwhelm desired cuteness | learns persona can be coauthored; expands rather than discards working image | very high textually; AV pending | not true-self/fake-mask binary |
| Shinosawa Hiro | D-HIRO crisis strategy | Dear 025-030 | performer whose peak output is triggered by credible risk | reach impossible HIF state | the Producer stakes his producer career and their dream/hobby time; Hiro infers that he would stake even their relationship, and he tacitly accepts (GKM-SAA-017) | accepts pressure as shared hobby while beginning to fear actual loss | very high | ethics remain OPEN |
| Shinosawa Hiro | D-HIRO relational power | Dear 031-035 | self whose strongest idol materials were accumulated from others | carry fans/friends/rivals/past into performance | earlier `素手` purity fantasy | names received power; prior history/classmates become part of `素手` | very high | impossibility now carries an accumulated life |
| Shinosawa Hiro | D-HIRO Prima Stella | Dear 036-037 | `不純なアイドル`; momentary summit rather than stable strongest | turn one miracle into a continuing self-owned dream | `奇跡は続かない`; ordinary skill remains limited | claims `今日、勝ったのはわたし`, accepts title as challenge, finally says `トップアイドルになる` | very high within D-HIRO | `瞬間最大風速`; title does not erase conditional P3 states |

## Phase 3 — Himesaki Rinami / 姫崎莉波

`D-RINAMI`, P1/P2, conditional P3 fragments, and modular communications remain continuity-distinct. Dear 036 Prima Stella is D-RINAMI only.

| character | story_state | source_id | self_concept | desire | fear_or_constraint | behavior_delta | confidence | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Himesaki Rinami | pre-route / Dear 001–003 | Dear 001–003 | third-year late bloomer near retirement after failed Love☆しすたぁず market fit | find a final viable idol form | public failure, low confidence, badly fitted `妹キャラ` | accepts strange childhood-based re-staging of her relational strengths | very high | not a beginner; accumulated fundamentals already exist |
| Himesaki Rinami | D-RINAMI produced naturalness | Dear 003–010 | caregiver identity being made public without wanting to become fake again | become legible as herself while still professionally performable | naturalness paradox; Producer's privileged childhood interpretation | rehearses onee-san behavior until public/ordinary registers begin to connect | very high | older-sister identity is hybrid: disposition + production |
| Himesaki Rinami | D-RINAMI N.I.A. | Dear 011–020 | failed past and caring present can coexist | win without treating rivals/fans as enemies | competition feels morally uncomfortable; old persona can be weaponized | owns failed history, defeats Shion/Gekka, develops explicit summit desire | very high | care and rivalry become additive |
| Himesaki Rinami | D-RINAMI summer crisis | Dear 021–027 | idol whose dream is strongly supported by others but must become hers | return because she herself wants to win and continue | father accident, HIF loss, home withdrawal, doubt about dream ownership | says `優勝したかった`; chooses `トップアイドル`; joins fan happiness to own happiness | very high | self-authorship hinge |
| Himesaki Rinami | D-RINAMI mature craft | Dear 028–033 | veteran whose warmth is carried by accumulated technique | turn whole-body precision into hospitality and love | danger of reducing value to “natural onee-san charm” | names `全身でファンサ` as `愛`; H.O.F. converts audience smiles into self-love | very high | craft does not oppose warmth |
| Himesaki Rinami | D-RINAMI summit | Dear 034–037 | Prima Stella who can own failure history, ambition, care, romance and production | remain with Producer and continue toward top idol | professional/romantic fusion; Producer authority | publicly thanks/loves audience; retrospectively chooses strange production; confesses and requests lifelong production | very high within D-RINAMI | vow is marriage-coded, not literal marriage |
| Himesaki Rinami | C-RINAMI musical authorship | CIDOL 000/007/013/017/018 | performer whose emotional truth can be crafted, inherited and peer-produced | make feelings and care communicable without autobiographical purity | risk of overfitting onee-san label or Producer's image | `clumsy trick`, `Campus mode!!`, `36℃ U･B･U`, `ガラクタロード`, RippleSign broaden authorship | very high textually; AV pending | performance identity must be AV-tested |
| Himesaki Rinami | ordinary life/work | selected Produce Events | caretaker who also likes being cared for and seen | maintain reciprocity outside climaxes | default toward helping/organizing others | accepts study/style help, asks Producer to stay, asks to depend, enjoys fan/public work | high C3/C4 | falsifies pure self-sacrifice model |
| Himesaki Rinami | P3 conditional fragments | `adv_pstory_003_hrnm_*` | result-state idol under later competition | continue after selection/final outcomes | four fragments only | shows branch-scoped reaction to result without supplying complete Series-3 biography | high branch-scoped | do not merge with D-RINAMI Prima Stella |

## Phase 3 — Shiun Sumika / 紫雲清夏

`D-SUMIKA`, P1/P2, conditional P3 fragments, and modular communications remain continuity-distinct. Dear 036 Prima Stella is D-SUMIKA only.

| character | story_state | source_id | self_concept | desire | fear_or_constraint | behavior_delta | confidence | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Shiun Sumika | pre-route / ballet past | Dear 005, 010, 032; CIDOL 010 | former prodigy whose expected future collapsed after injury | recover a life with something worth wanting | pain memory, fear of re-injury, expectation as judgment | enters idolhood partly as escape, later explicitly chooses it | very high | not a hidden beginner |
| Shiun Sumika | P1 avoidance | Series 1 Produce Story | bright/social girl using partial noninvestment as escape hatch | stay near idolhood without being fully judged | full effort would make failure personally diagnostic | trains progressively, accepts frustration, stops fleeing valued things | very high | playfulness itself remains genuine |
| Shiun Sumika | D-SUMIKA chosen mask | Dear 007–010 | weak self acknowledged; strong idol self deliberately performed | make chosen ideal true through practice | fear of being seen as weak; Lilja expectation | chooses `強いあたしの仮面`; asks Producer to coauthor fantasy | very high | performance ≠ falsity |
| Shiun Sumika | N.I.A. public expectation | Dear 011–020 | rising idol whose old prodigy status is socially rediscovered | remain at Hatsuboshi and become idol on chosen terms | envy, rumors, social isolation, Gokugetsu manipulation | accepts reliance, rejects fan instrumentalism, chooses belonging | very high | support begins to become lift rather than threat |
| Shiun Sumika | STEP3 body rebuild | Dear 021–024 | dancer whose identity is again high-stakes | rebuild dance without returning to old compulsory prodigy self | Tsubame loss, right/left imbalance, tedious conditioning | strength work; coaches Lilja; technical capacity rises | very high | bodily afterlife of trauma persists |
| Shiun Sumika | expectation relapse | Dear 024–026 | technically excellent idol overfitting public ideals | become strong without killing own preference | fan expectations reproduce old judgment trap | fails at assigned `わがまま`; identifies fear of disappointment | very high | key self-authorship hinge |
| Shiun Sumika | artistic coauthor | CIDOL 012 / `Love & Joy` | ideal self increasingly authored from inside | transform weakness into strength through owned performance choices | tendency to defer to experts/Producer | authors the choreography and drafts lyrics; the ballet-derived motion is hers, endorsed by the Producer; outfit and ponytail are chosen by the Producer at her request, to his taste; fanservice and staging are his proposal, co-designed (GKM-SAA-131) | very high textually; AV pending | Producer deliberately returns space; her bid for his preference belongs with dependency (GKM-SAA-131) |
| Shiun Sumika | REVERSI / public testimony | Dear 027–035 | relationally supported idol capable of making vulnerability vocational | use dance to give courage; fulfill HIF wish with Lilja | authentic history becomes production capital; fear remains | publicly narrates trauma; becomes companion+rival; asks for/receives courage | very high | disclosure is authored promise, not raw dumping |
| Shiun Sumika | D-SUMIKA Prima Stella | Dear 036–037 | `強くなった` idol whose strength includes fear, dependence, craft and history | push others toward desired selves; continue growing | expectations increase with title; Producer dependency | wins within D-SUMIKA, gives courage publicly, receives proof her live gave Producer courage | very high within D-SUMIKA | summit-as-promise, not permanent cure |

## Phase 3 audiovisual integration — Fujita Kotone / 藤田ことね

| character | story_state | source_id | self_concept | desire | fear_or_constraint | behavior_delta | confidence | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Fujita Kotone | integrated AV baseline | `GKM_KOTONE_COMPLETE_AUDIOVISUAL_BASELINE` | materially precarious worker-idol becoming a self-authoring professional and performer of reciprocal value | make paid idol work materially real while making each spectator feel recognized | scarcity, overwork, delegated confidence, repayment compulsion | converts social reading and register mobility into chosen public craft | very high within Phase-3 AV boundary | stable identity is performed reciprocity, not one fixed cute voice or genre |
| Fujita Kotone | foundational solo identity | `世界一可愛い私`; `Yellow Big Bang！` commus/MVs/3DMVs | weak, self-loving, commercially minded idol who can include contradiction inside persona | receive belief and return it as audience pleasure | pressure to make positivity erase weakness | integrates greed, praise, anxiety, enjoyment and public command | very high | visible enjoyment is part of professional truth |
| Fujita Kotone | scalable recognition | `Campus mode!!`; self-esteem song | intuitive social reader becoming a deliberate fanservice technician | make crowd-scale attention feel individually addressed | replacement anxiety; exclusivity toward Producer; risk of reassurance dependence | turns special attention and manufactured confidence into repeatable performance technology | high | manufactured does not mean false |
| Fujita Kotone | late Dear 025–027 | whole Dear 21–27 packet + exact S1 text | professional capable of analysis and grief; debtor becoming ordinary idol | retain rivalry, career, and attachment without emergency deciding everything | H.I.F. loss; fear of not being a true rival; career-as-payment logic | accepts grief, asks for presence, repays family debt, names `普通` as achieved luxury | very high | ordinary development is economic, bodily, temporal, relational and aesthetic |
| Fujita Kotone | Re;IRIS / U1 | canonical `雨上がりのアイリス` commu + 3DMV | distinct solo identity capable of distributed focality | participate in collective performance without disappearing into stronger specialists | risk of projection that social intelligence automatically equals leadership | remains legible inside shared center/blocking | high within U1 | supports distributed-center capacity, not yet permanent mediator status |

## Phase 3 — Hanami Ume / 花海佑芽

| character | story_state | source_id | self_concept | desire | fear_or_constraint | behavior_delta | confidence | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Hanami Ume | P1[UME] early | Series-1 Produce Story + Dear 001–006 | supplementary-admit former athlete whose idol dream begins as pursuit of Saki | beat Saki in the arena Saki chose | derivative horizon; slow start; habitual losing | chooses explicitly to beat Saki **as an idol** and accepts that the post-victory self must author what comes next | very high | relational origin is not falsehood |
| Hanami Ume | D-UME equal-rival hinge | Dear 007–019 | pursuer approaching equality | become someone Saki must fear losing to | discovers that equal rivalry is frightening precisely because loss now matters | names fear without retreat; finally defeats Saki; asks not to be left behind | very high | `fearless Ume` rejected |
| Hanami Ume | post-Saki win | Dear 019–020 | girl whose founding quest has succeeded | remain an idol for reasons not exhausted by Saki | danger of identity collapse after the chase | says `もう、追いかけない`; names love of idols and desire to become an idol properly | very high | differentiation without severance |
| Hanami Ume | Worst Three / widening world | pevent + Dear + CIDOL | friend/rival among China and Hiro rather than only younger sister | learn other forms of strength, treasure and performance | Saki can otherwise monopolize comparison | treats China/Hiro paths as genuine treasures; learns through observation and embodied reintegration | high | individuation through plural relations |
| Hanami Ume | late D-UME | Dear 027–035 | rival who understands idols as renewable fuel for idols | become strongest while making other people more alive | burnout model inherited from Hanami competition; fear of larger dream | revises `burn to ash` toward rivals adding fuel; chooses her song and reasons through a first preference for 100 Pro, where Saki reports decided entry (HSCA-003) | very high | rivalry becomes generative ethic |
| Hanami Ume | D-UME Prima Stella | Dear 036–037 | self-authored `world's strongest idol` | make fans and rivals smile, burn, move and want more idolhood | summit could harden into domination or closure | refuses false modesty, invites others onward, defines strength through generative social effect | very high within D-UME | summit functions as invitation rather than endpoint |
| Hanami Ume | integrated AV baseline | `GKM_UME_COMPLETE_AUDIOVISUAL_BASELINE` | renewable rival whose direct brightness is produced through pressure absorbed and returned | turn fear, comparison, fans, inherited forms and rivals into motion other people can join | risk of mistaking loudness or continuous acceleration for her whole identity | formalizes **compression → rebound → outward address** across voice, body, camera and repertoire | very high within Phase-3 AV boundary | **renewable rivalry realized as reciprocal propulsion**; strength and cuteness remain integrated |

Canonical integrated authority: `GKM_UME_COMPLETE_AUDIOVISUAL_BASELINE.md` — Drive `1p-MzTVcTZ_Mercqc3WxHqXi1m8UwO7bV`. Voice specialist: Drive `1G6Vy6_TnzBxaYiG37APhyOkxsNMDpvRy`. Music/MV specialist: Drive `1EIS_KFKb9yU2T-G2jl-LVX66l6KXNRoR`.

## Phase 3 — Hataya Misuzu / 秦谷美鈴

| character | story_state | source_id | self_concept | desire | fear_or_constraint | behavior_delta | confidence | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Hataya Misuzu | D-MISUZU opening / post-SyngUp! | Dear 001–005 | genuinely depressed former-unit member choosing a livable pace, not merely an effortless superior | reach the top without making the destination unlivable | loss of SyngUp!, low confidence, aversion to self-punishing effort | accepts Producer's environmental support while preserving `ほどほど` / `マイペース` | very high | early low confidence is real; later sovereignty must not be back-projected |
| Hataya Misuzu | P1 / modular daily state | Produce Story + pevent + growth | exceptionally capable idol who economizes effort and plans leisure | make progress efficiently enough that rest remains possible | visible effort is a poor proxy for investment | works selectively, prepares carefully, improves rapidly when engaged | very high | `lazy genius` is too crude |
| Hataya Misuzu | care / dependence state | Dear + pevent | caretaker who sincerely enjoys making close people comfortable and dependent | be needed, trusted and allowed into others' daily life | care can become enclosure; she is less practiced at receiving care | names the pleasure of cooking, cleaning, waiting, bathing/caretaking and being entrusted | very high | tenderness and possessiveness coexist |
| Hataya Misuzu | Temari reconfiguration | Dear 006–010, 032–037 | childhood quasi-sister/caretaker becoming an equal rival | remain together without forcing sameness or restoration | old habit of containing Temari; jealousy over others who command Temari's gaze | learns anger, conflict and `合わないままで一緒にいる`; accepts Temari's own `マイペース` | very high | difference becomes compatible with attachment |
| Hataya Misuzu | Rinha / N.I.A. | Dear 011–020 | former unit member who can love a friend on a separate road | compete, communicate and become a worthy object of aspiration | guilt over not intervening earlier; temptation to restore old unit form | says `ちゃんと喧嘩をしましょう`; offers `わたしに憧れてもいいよ`; accepts non-restoration | very high | relational continuity without institutional restoration |
| Hataya Misuzu | H.I.F. defeat / wrong-path training | Dear 021–026 | proud elite whose defeat exposes stored anger and promise anxiety | defeat rivals and fulfill Prima Stella promise without losing chosen self | resentment; broken promise to Producer; self-punitive overtraining | preserves resentment as fuel, briefly runs with Temari, then rejects frantic identity distortion | very high | `Misuzu should never run` rejected; compulsion, not exertion, is the problem |
| Hataya Misuzu | mature Producer dyad | Dear 027–035 | self-authoring idol who now wants reciprocal access rather than bounded contract distance | share dream, ambition and future while being uniquely chosen | possessive merger language; producer/student authority asymmetry | asks for Producer's inner life, adopts his dream as shared treasure, tolerates greater mutuality | high | intimacy is real; autonomy pressure remains open |
| Hataya Misuzu | D-MISUZU Prima Stella | Dear 036–037 | `悪くて強い、欲張りな一番星` becoming night-sky sovereign | reign at the top without becoming a generic diligence model; carry title farther | title could freeze personality or turn possession into jurisdiction | wins, cries openly, hands Producer four years of effort, discovers innumerable unseen stars beyond the visible sky | very high within D-MISUZU | summit reopens infinity rather than closing it |
| Hataya Misuzu | musical self-authorship | CIDOL 000/005/010/014/015/016 | gentle surface and enormous appetite deliberately integrated into performance identity | leave claw marks, reawaken dreams, capture attention, keep evolving | ownership rhetoric must coexist with fan choice and plural social worlds | rereads old unit repertoire, adopts night-sky imagery and selects permanently developmental repertoire | very high textually; AV pending | `VEIL` is the clearest permanent-growth formulation |
| Hataya Misuzu | P3-C[MISUZU] | four Series-3 conditional files | result-state Misuzu only | react to local selection/final outcomes | incomplete route evidence | preserve outcome-local reactions without constructing a synthetic Series-3 biography | very high | branch control mandatory |

## Phase 3 Character 12 - Juo Sena / 十王星南

**Continuity boundary:** `P1[SENA]`, `P2[SENA]`, `D-SENA`, `M-SENA`; no Sena Series-3 Produce Story family exists in Source Lock 1.0.

**Current model:** **generative supremacy**.

Sena begins as Hatsuboshi's public crown: technically extraordinary, institutionally authoritative, visibly complete, and privately aware of a plateau. Her planned post-graduation move into production is both a real vocation and an avoidance structure. Producing a successor would allow her to preserve meaning without remaining exposed to the possibility that a peer could surpass her.

Phase-3 development:

1. `P1[SENA]` establishes visible ceiling, perfect-image discipline, fear of stronger external comparison, and the limits of treating current ability as destiny.
2. `D-SENA` makes her Producer apprenticeship concrete. Failed scouting, Kotone's refusal, and the exposure of "human/cute Sena" teach that accurate talent recognition does not grant ownership and that recipient context matters.
3. Whitegrass Gekka and other external elites reopen world-scale rivalry. Sena's enthusiasm as a fan proves that admiration, command, and competitive hunger coexist.
4. Producing Kotone, Ume, China and Misuzu, and being challenged by Saki and the wider golden generation (GKM-SAA-146), teaches that visible parameters are only a fraction of idol power. Support, narrative, audience attachment, differentiated pedagogy, and institutional conditions can change outcomes without making measurement useless.
5. The successor project becomes a rival project. Sena no longer seeks someone who can replace her after retirement; she builds people and systems capable of threatening her while she remains onstage.
6. H.I.F./Prima Stella becomes a constitutional office rather than a private possession: a summit whose authority depends on being challengable.

Stable observations:

- exceptional embodied and analytical competence;
- strong institutional imagination and appetite for authority;
- real fanhood beneath command;
- broad practical competence and elite childhood formation;
- possessive language (`私のモノ`, `私のスター`) that can express affection, recognition, rivalry, and jurisdiction at once;
- refusal to equate humility with virtue;
- desire to make the top meaningful by making it contestable.

Ethical risks carried forward:

- benevolent secrecy and paternalistic intervention;
- treating accurate judgment as a title to direct another person;
- class/family resources that make her developmental projects unusually executable;
- coercive challenge as pedagogy;
- founder-centered institutional design.

**Phase-7 prohibition:** do not reduce Sena to arrogant queen, benevolent mentor, stat-machine, hidden soft girl, or future Producer. The current evidence requires all of those surfaces to remain in tension.

## Phase-3 Tsubame delta — 2026-08-16

### Amaya Tsubame / 雨夜燕 — **heroic rivalry**

- **Early state:** `学園No.2` is both earned status and defensive shelter. She can work brutally hard while preserving Sena as the one allowed exception; Dear 006 later names the hidden structure as looking downward for reassurance while only pretending to pursue the summit without surrender.
- **Disruption:** losing to Misuzu destroys the “only Sena can beat me” exception. Tsubame explicitly redefines her goal as becoming Sena's rival `本当の意味で`.
- **Positive vocation:** the route develops an independent dark-hero/hero ideal — performance should give courage, refuse abandonment, and make victory answerable to the people whose expectations it displaced.
- **Individuation hinge:** Dear 024 states `ヒーローみたいなアイドルになる！ その想いに、貴様の有無は関係ない！` and `私はアイドルで在り続けるぞ！`. She can imagine and accept a world without Sena while remaining an idol.
- **Mature state:** after proving independence, she can choose Sena again. Rivalry becomes renewable future architecture rather than the condition of Tsubame's identity.
- **Late epistemic revision:** Dear 027 recognizes `技術だけがアイドルの魅力ではない`; `スター性` becomes an open developmental dimension rather than permission to discard technique.
- **Primary unresolved risk:** hero/non-abandonment language can become paternalistic if Tsubame treats her insight into another person's desire as jurisdiction.
- **AV boundary at textual-pass freeze:** written register and song intentions were canonical while rendered evidence was pending; performed claims are now governed by the integrated AV section immediately below.

## Phase 3 integrated AV — Amaya Tsubame / 雨夜燕 — 2026-08-18

**Current authority:** `GKM_TSUBAME_COMPLETE_AUDIOVISUAL_BASELINE.md` — Drive `1OubUGaGvDwihXTFYbcft47uYYCc7zH50`. Textual authority remains `GKM_CORE_13_AMAYA_TSUBAME.md`; AV revisions route through `GKM_CORE_13_AMAYA_TSUBAME_AV_REVISION_ADDENDUM.md` — Drive `1l7ZL4yHMjrFuQ0Tl5niIyc-0F0OzixDc`.

**Integrated state:** **heroic rivalry performed through directional heroism**. Tsubame's severe, combat-coded form becomes mature when pressure is given a recoverable direction: expose the blocked future, make a road visible, and leave the addressed person able to answer.

| state | performed evidence | current formulation |
|---|---|---|
| pre-recruitment vice president | Dear 000 | strict public authority and immediate correction coexist with practical care for juniors |
| defensive No.2 | Dear 001–005 | disciplined force remains scene-dominant but is organized around a protected hierarchy |
| hierarchy rupture | Dear 006 | gaze, posture, facial control, and vocal timing destabilize before challenge grammar rebuilds agency |
| authored rival/hero | Dear 009–019 + song commus | rivalry becomes fan-facing vocation; childhood hero desire supplies a positive ideal independent of Sena |
| individuation | Dear 021–024 | vulnerability remains declarative/combat-coded; `貴様がいない世界` is performed as chosen separation rather than emotional detachment |
| healthy loss / open future | Dear 025–027 | tears and anger coexist with delight in Sena's strength; defeat redirects motion rather than collapsing identity |
| public musical identity | three P0 song/performance identities | attack, inherited brightness, and invitation become selectable modes inside one stable persona |

**Voice model:** **armored declarative poise** — Tsubame governs scenes through completed clauses, forceful attacks, disciplined timing, and challenge rhetoric. Vulnerability changes volume, pacing, gaze, and breath before it changes syntax; care often arrives as a demand that another person remain contestable.

## Phase 3 — Hataya Misuzu integrated AV state

| character | authority level | current formulation | evidence state | open risk |
|---|---|---|---|---|
| Hataya Misuzu | textual core + integrated AV baseline | **Night-sky sovereignty through centripetal sovereignty**: softness is the performance mechanism by which care, enclosure, possession, and public charisma become continuous; tempo is self-authored rather than morally fixed | Dear 001–037 complete; five song commus; ten 3DMVs; four authored MVs; four comparison sources | whether the night sky preserves stars as independent subjects; Producer closed-dyad/authority risk |

Key corrections: calm is containment rather than invulnerability; high effort is possible but wrong-path acceleration can destroy identity coherence; tears enlarge rather than cancel public sovereignty; group performance preserves full center status rather than reducing her to caretaker support.

Primary AV authority: `GKM_MISUZU_COMPLETE_AUDIOVISUAL_BASELINE.md`.

## Phase 3 AV addendum — Shinosawa Hiro

| character | story_state | source boundary | current AV state | change | confidence | unresolved |
|---|---|---|---|---|---|---|
| Shinosawa Hiro / 篠澤広 | D-HIRO 001–037 + M-HIRO + rendered performance controls | 33 AV objects; `GKM_HIRO_COMPLETE_AUDIOVISUAL_BASELINE.md` | **resistant form**: bodily insufficiency, low-force voice, experimental repertoire, and relational risk are composed into form rather than erased | textual `chosen impossibility becoming accountable attachment` is PRESERVED/STRENGTHENED; improvement creates expressive surplus rather than normalization | high within current source boundary | sustainable noncrisis access to peak concentration; `みちなるひろがる` commu; later post-dream failure |
| Hiro | early Dear | Dear 001–010 AV | micro-affective deadpan; genuine bodily floor; difficulty pleasure; jealousy and `かわいくなりたかった` puncture purely abstract self-explanation | REVISE “loves failure” toward “loves resistance” | high | later event/support ordinary-life breadth |
| Hiro | middle Dear | Dear 011–027 AV | friends/fans make weakness social; `神格` becomes a reception mode; crisis concentration is observable but ethically unresolved | STRENGTHEN charisma beyond metrics; DOWNGRADE goddess-as-essence | high | whether crisis can be replaced by sustainable practice |
| Hiro | late Dear/H.I.F. | Dear 028–037 AV | fear of losing the shared future makes risk consequential; Prima Stella is bounded `瞬間最大風速`, not permanent floor | REJECT stable-conventional-supremacy reading | high in D-HIRO | cross-route result-state reconciliation |
| Hiro | musical identity | principal, common, seasonal and duet packet | experimentalism is curated across Hiro-specific works; common songs reveal subtler portable resistance | STRENGTHEN user's experimental-music observation; REJECT “every Hiro song is avant-garde” | high within packet | full-franchise comparative musicology |

## Sumika audiovisual integration delta — 2026-08-17

| character | state | current formulation | AV consequence | confidence |
|---|---|---|---|---|
| Shiun Sumika | integrated Phase-3 AV | self-authored expectation realized through **kinetic self-authorship** | brightness remains genuine; strategic unseriousness is the defense; ballet becomes technical inheritance; `Love & Joy` converts owned technique into public address | very high |
| Shiun Sumika | hidden-self performance | `カクシタワタシ` creates protected stillness | rejects “quiet serious Sumika is the only true self”; no authored official MV exists in current packet | very high |
| Shiun Sumika | REVERSI | friendship becomes synchronized differentiation | visual/performance form preserves Sumika and Lilja as two readable centers while enabling touch, mirroring, exchange, and rivalry | high |
| Shiun Sumika | D-SUMIKA late direct AV / Dear 032–034 | **reversible register permeability**: testimony and fear can remain visible before social brightness returns | directly strengthens courage-as-fear-plus-support; brightness shifts from preemptive defense toward post-disclosure repair | very high |
| Shiun Sumika | D-SUMIKA Prima Stella / Dear 036–037 | summit authority remains recognizably colloquial and relational; personal reciprocity requires an explicit temporary suspension of the Producer role | REJECT invulnerable-crown endpoint; STRENGTHEN role-conscious intimacy while preserving dependency/asymmetry OPEN | very high within D-SUMIKA |


## Kuramoto China — Phase-3 integrated AV revision (2026-08-21)

| dimension | post-AV state | authority / qualification |
|---|---|---|
| core model | **PRESERVE + STRENGTHEN:** accountable inheritance / relational legitimacy | `GKM_CHINA_COMPLETE_AUDIOVISUAL_BASELINE.md` |
| weakness and charm | technical weakness is neither concealed nor transformed into pure incompetence; visual/vocal legibility makes incompletion socially shareable | Phase-3 AV corpus |
| register | `わたくし／ですわ` is a durable identity-bearing register, not a brittle mask; panic changes timing, breath, pitch, and bodily control more readily than pronoun/ending choice | voice specialist |
| `ふにゃ／きり` | **REVISE:** not false self versus true self; a reversible rhythm of receiving support, gathering herself, and assuming public responsibility | Dear 028–037 + AV synthesis |
| privilege | cultivated poise and production resources remain real advantages; AV does not moralize them away | textual core + AV corroboration |
| Hiro relation | `みちなるひろがる` strengthens the horizontal-reciprocity claim without erasing asymmetry of resources/history | duet commu + rendered performance + official MV |
| summit authority | public command remains relationally ratified rather than solitary; fragility is retained inside authority | D-CHINA / Dear 036–037 |
| future reopening | events, support cards, and Phase-6 relationships may revise ordinary ecology and pair-specific behavior | OPEN until Phases 4–6 |


<!-- LILJA_AV_R1_UPDATE_2026-08-22 -->
## Katsuragi Lilja — Phase-3 integrated AV state

**Current compact model:** courage made circulatory through **tremulous world-making**.

Stable transition grammar: **tremor → relational anchoring → sustained attention → field formation → returned courage**.

- **PRESERVE/STRENGTHEN:** courage is received relationally and returned through performance.
- **REVISE:** strong will is not uniformly healthy; overtraining can convert determination into body-erasure.
- **REJECT:** maturity means eliminating shyness, fragility, dependence, or technical beginnerhood.
- **REVISE:** `魔性` and `葛城結界` are coauthored attention fields, not solitary mystical essence or isolation.
- **REJECT:** Sumika is merely Lilja's unilateral rescuer; REVERSI resolves as synchronized differentiation.
- **DOWNGRADE:** the Producer is omniscient; `桜フォトグラフ` preserves competence alongside improvisation and fallibility.
- **REJECT:** authentic performance must always function as effort/proof; `ガラクタロード` restores pleasure and play.
- **OPEN:** the exact romance/dependence balance of Dear 037 remains Phase-6/7 work.

Authority: `GKM_LILJA_COMPLETE_AUDIOVISUAL_BASELINE.md` and `GKM_CORE_05_KATSURAGI_LILJA_AV_REVISION_ADDENDUM.md`.

<!-- RINAMI_AV_R2_UPDATE_2026-08-22 -->
## Himesaki Rinami — Phase-3 integrated AV R2 state

| field | current formulation |
| --- | --- |
| governing identity | reciprocal care becoming self-authored desire |
| audiovisual mechanism | **reversible hospitality: receive → hold → offer → be answered → expand** |
| stable capacity | creates a low-friction relational field in which others feel seen, soothed, teased, and invited to answer |
| core wound | self-worth organized around usefulness, role-fit, and the fear that desire imposes burdens on people she loves |
| governing desire | to be an idol, competitor, lover, technical professional, and caring person without requiring one identity to erase the others |
| defensive strategy | care-taking, role performance, gentle deflection, delayed first-person claims, and retreat toward a materially valuable family/home life |
| growth mechanism | receives care without converting it immediately into debt; lets technique support warmth; names personal victory and romantic desire; keeps relation open after disclosure |
| public identity | achieved onee-san hospitality rather than biological destiny or empty marketing shell |
| late-state authority | can explain technique, compete directly, receive fan love, claim Prima Stella, confess, and request continuing professional partnership |
| highest-risk failure | fusion of romance, childhood attachment, self-worth, and producer authority may weaken refusal or make approval into oxygen |
| reconstruction-safe rule | preserve the same warm relational voice while varying monitoring, completion, projection, technical sharpness, embarrassment, and willingness to receive care |

### Principal claim transitions

- **STRENGTHEN:** the onee-san frame is real because practiced and socially answerable, not because effortless.
- **REJECT:** the old little-sister persona was wholly fake.
- **REVISE:** naturalness is produced through craft and fit, not discovered by stripping performance away.
- **STRENGTHEN:** competition can intensify care rather than cancel it.
- **PROMOTE:** `優勝したかった` is the central first-person dream-authorship hinge.
- **STRENGTHEN:** technique becomes love through full-surface address and returned audience response.
- **REJECT:** mature Rinami is permanently maternal, soft, selfless, or conflict-averse.
- **OPEN:** chosen Producer/lover fusion remains ethically governance-sensitive.

R2 high-resolution reinspection of Dear 027, 031, 036, and 037 strengthens the sequence model—contraction, hand-to-chest gathering, tears/blush, direct-gaze recovery, completed address—without producing a different character thesis.

<!-- PHASE4_EVENTS_001_005_2026-08-23 -->
## Phase 4 — Events 001–005 ensemble correction

**Authority:** `GKM_EVENTS_001_005_DEEP_READING.md` — Drive `1jb1bUXahrykBDIrdw3VJGdCHSZEGoIe0`.

| character | Phase-4 transition | event evidence | current formulation |
|---|---|---|---|
| Hanami Saki | **STRENGTHEN / REVISE** | E001, E004, E005 | rivalry functions as epistemology and pedagogy; practical care can respect privacy; stated rationality does not exhaust relational motives |
| Tsukimura Temari | **STRENGTHEN / REVISE** | E001, E004 | professional severity remains real, but social distance can collapse too quickly once she decides relation is useful; responds to Lilja's conviction while taking Sumika's dubbed warning as Lilja's (HSCA-006) |
| Fujita Kotone | **STRENGTHEN** | E001, E003, E004; E005 discussion | precarity is bodily visible; social intelligence regulates peers from inside participation; low school status is not low ceiling |
| Arimura Mao | **STRENGTHEN / REVISE** | E003 | senior/prince care is chosen action, but last-summer pressure can turn concern into overreach; she can self-diagnose and repair without abandoning the role |
| Katsuragi Lilja | **STRENGTHEN** | E001, E004 | fear coexists with explicit competitiveness; Lilja asks for another try, persists after Kotone suggests stopping, and claims her ball-toss win after Saki ends the lesson and competes. [Festival game](../05_AUDIOVISUAL_ANALYSIS/GKM_PHASE7_FOUR_EVENT_PERCEPTUAL_ADJUDICATION_20261125.md#the-coach-becomes-an-opponent); cultural uncertainty is specific rather than generic |
| Kuramoto China | **STRENGTHEN** | E002, E005 | accurate weakness-awareness becomes practice; receptive authority can welcome and still enforce norms; inherited sponsorship precedes later legitimacy work |
| Shinosawa Hiro | **STRENGTHEN / REJECT simplification** | E002 | enjoys resistance but explicitly rejects making friends pay for her weakness; selfish failure-seeking model rejected |
| Himesaki Rinami | **STRENGTHEN** | E003, E005 | reversible hospitality can redirect professional anxiety toward audience pleasure; soft register carries firm institutional judgment |
| Shiun Sumika | **STRENGTHEN / REVISE** | E001, E003, E004 | social intelligence includes intervention, non-intervention and knowing reinforcement of the dubbed-warning misunderstanding (HSCA-006); in the shop she explains the relative’s collapse and her temporary work, recognizes Mao’s concern and apologizes for her sharp response. [Beach-restaurant repair](../05_AUDIOVISUAL_ANALYSIS/GKM_PHASE7_FOUR_EVENT_PERCEPTUAL_ADJUDICATION_20261125.md#repair-at-the-beach-restaurant); jealousy need not become enclosure |
| Hanami Ume | **STRENGTHEN** | E002, E005 | low status becomes propulsion; Sena recognizes Ume’s unusual athletic ability and says she could not assess her idol talent in the Event 005 encounter (main-05 L401–L427, L534–L574) |
| Hataya Misuzu | **STRENGTHEN / OPEN** | E002, E005 | softness contains truancy, jealousy, care, and elite skill; student-council capacity question reveals a motive not completed by this event; the E002 jealousy concerns a friend unnamed there whom cross-event evidence strongly supports as Temari, and the student-council motive stays OPEN with competing readings (GKM-SAA-106) |
| Juo Sena | **STRENGTHEN / PROMOTE / REJECT** | E005 | successor-making and rival-making diverge; Saki is reclassified as rival; Ume falsifies an infallible talent-eye model |
| Amaya Tsubame | **STRENGTHEN** | E005 | strict rule enforcement coexists with confidentiality, skepticism toward concentrated authority, and rival recognition |

<!-- PHASE4_EVENTS_006_012_2026-08-23 -->
## Phase 4 — Events 006–012 ensemble correction

**Authority:** `GKM_EVENTS_006_012_DEEP_READING.md` — Drive `12qIoWXbSo45TffFLiTA1WvKgB9wpRLJo`.

| character | Phase-4 transition | event evidence | current formulation |
|---|---|---|---|
| Hanami Saki | **PROMOTE / STRENGTHEN** | E008, E009, E012 | competition-derived optimization is transferable peer pedagogy; care can enforce rest, distinguish leader/friend responsibility, and adapt method to the person rather than merely demand effort |
| Tsukimura Temari | **PROMOTE / STRENGTHEN** | E007, E008, E011 | high standards become domain-sensitive support: a sincere weaker teammate may be actively carried; blunt public syntax coexists with strong inner enthusiasm, fear, and gratitude |
| Fujita Kotone | **STRENGTHEN / REVISE** | E008, E009 | service-work history is professional idol capital and social brokerage; competence also creates a recurring overfunctioning/exhaustion risk |
| Arimura Mao | **PROMOTE / STRENGTHEN** | E011 | refractive role authorship is enacted inside client work: inherited acting skill, requested femininity/princess work, prince desire, and current idol vocation can coexist through negotiated role multiplication |
| Katsuragi Lilja | **PROMOTE / REVISE** | E009, E012 | social expansion can be scaffolded and then self-authored; raw effort can become an `免罪符` ritual, so courage requires method, rest, feedback, and reciprocal support |
| Kuramoto China | **PROMOTE / STRENGTHEN** | E006, E007, E011 | accountable inheritance becomes concrete hospitality/service infrastructure; social and audience skill is a real professional strength; receptive authority can redesign operations and negotiate for others |
| Shinosawa Hiro | **PROMOTE / STRENGTHEN** | E006, E007, E010 | resistance remains pleasurable but no longer monopolizes value; recipient happiness can outrank solitary difficulty, and relational meaning can survive successful completion |
| Himesaki Rinami | **PROMOTE / STRENGTHEN** | E006, E010 | recipient-centered, consent-sensitive scaffolding is stable across junior advising and ordinary friendship; she constrains excess without replacing another person's authorship |
| Shiun Sumika | **PROMOTE / STRENGTHEN** | E009, E012 | apparent unseriousness can conceal fear while desire persists; recovery requires disclosure without abolishing authored brightness; bilateral support becomes explicit |
| Hanami Ume | **STRENGTHEN / REVISE** | E006, E009, E010 | action-first spontaneity includes divergent creativity and active friendship-seeking; planning/recipient scaffolds improve production without erasing propulsion |
| Hataya Misuzu | **STRENGTHEN** | E007, E010 | ordinary reciprocal care with Temari is established; Hiro explicitly places Misuzu in her close-friend network |
| Juo Sena | **STRENGTHEN / OPEN** | E006, E008 context, E010 | bounded delegation can develop juniors; intense affection can become craft/resource deployment; discretionary office power remains elastic enough to keep under governance review |
| Amaya Tsubame | **NO DIRECT DELTA** | — | no direct speaking role in Events 006–012; preserve the Phase-3 model without inference from absence |

<!-- PHASE4_EVENTS_013_020_2026-08-23 -->
## Phase 4 — Events 013–020 character-state additions

**Authority:** `GKM_EVENTS_013_020_DEEP_READING.md` — Drive `1pyVYENC8kCbXvQtYU60pVdYad8yxCobF`.

The following transitions are tranche-level routing instructions, not replacements for the full character ledgers.

| character | transition | Events 013–020 evidence | current implication |
| --- | --- | --- | --- |
| Hanami Saki | **STRENGTHEN / OPEN** | E016 permits Ume's independent friend world while concealing her own loneliness; E019 builds a functioning unit around Temari/Kotone's differentiated strengths | pedagogy and leadership are increasingly relationally adaptive; older-sister identity still constrains admitted vulnerability |
| Tsukimura Temari | **STRENGTHEN** | E016 transmits Rinha's batting pedagogy and receives Kotone's private respect; E019 asserts capacity to travel without Misuzu while retaining care infrastructure | dependence changes form rather than disappearing; harsh technical language can carry learned care |
| Fujita Kotone | **STRENGTHEN** | E016 sibling reciprocates pride; E019 family accepts work priority and Kotone operates comfortably inside peer unit | provider identity is increasingly reciprocal; family and friendship can authorize idol self-investment |
| Arimura Mao | **STRENGTHEN** | E013 old regret toward Sena; E017 role-integration advice to Sena; E018 adaptive senior leadership and joyful prince acting | princehood is genuine vocation when chosen and audience/recipient-sensitive, not merely a defensive shell |
| Katsuragi Lilja | **STRENGTHEN / REVISE** | E015 independently accepts senior opportunity and adjusts stagecraft for distant spectators; E020 publicly integrates fandom and defends dream+hobby dual commitment | courage is increasingly self-authored and audience-directed; borrowed media language can be an authentic expressive resource |
| Kuramoto China | **STRENGTHEN** | E014 consciously performs morale. In E015 China offers a familiar local cheer and invites the audience to join the trio during a playback failure (`adv_event_015_main-04` L519–638). | receptive authority includes crisis leadership and chosen morale work |
| Shinosawa Hiro | **STRENGTHEN / REJECT** | E014 explicitly dislikes a form of suffering whose cost falls on friends; E018 seeks socially collaborative mismatch and reciprocal disclosure | “loves failure/hardship” is decisively inadequate; resistance-seeking is consequence-sensitive and relationally governable |
| Himesaki Rinami | **STRENGTHEN** | E013 first-year class regulation and Sena's recruitment logic; E015 mentorship reverses; E017 observer becomes observed | reversible hospitality and receptive authority are deeply historical; mature care preserves others' authorship and accepts return support |
| Shiun Sumika | **STRENGTHEN** | E018 names fear of Hiro seeing through avoidance; E020 reclaims Sweden through Lilja and shows hobby/fashion competence as world-opening care | chosen brightness remains genuine while protecting vulnerability; relational safety can reduce the need for concealment |
| Hanami Ume | **STRENGTHEN** | E014 gives Hiro recipient-specific, unsentimental sport advice; E016 independent peer world becomes compatible with sister rivalry | reciprocal propulsion includes truthful shared-loss framing and social individuation |
| Hataya Misuzu | **STRENGTHEN** | E014 extraordinary effort chosen for Hiro without abandoning low-effort self-authorship; E019 permits Temari to travel independently | centripetal care can become less enclosing when the relation survives departure and effort remains self-chosen |
| Juo Sena | **STRENGTHEN / REVISE** | E013 explicitly believes she has reached growth limit and identifies equal rival as possible escape; E017 ordinary/fan self enters idol theory | generative supremacy requires two different futures: successors for institutional continuity and rivals for present personal growth |
| Amaya Tsubame | **STRENGTHEN** | E013 reads Sena's distraction, challenges mentorship displacement, and demands a stronger future Sena | directional heroism applies upward as well as downward: pressure protects the rival's capacity to remain a participant |

---

<!-- PHASE4_EVENTS_021_PLUS_2026-08-23 -->
## Phase 4 — Events 021+ character-state additions and numbered-event closure

**Authority:** `GKM_EVENTS_021_PLUS_DEEP_READING.md` — Drive `1kYHscRZA5RSTT6l5TGyaAUMLmeu9uQ6T`.

| character | transition | Events 021+ evidence | current implication |
| --- | --- | --- | --- |
| Hanami Saki | **STRENGTHEN** | E026 accepts representative pressure, studies predecessor performance, and tells Ume/Kotone uncertainty about one's final path is legitimate | optimization/leadership now includes epistemic humility and lineage-conscious goal setting |
| Tsukimura Temari | **STRENGTHEN** | E023 authors a private song/lullaby gift to repair a missed birthday; E026 converts intense envy into professional support | severe standards coexist with ritual memory, attachment, and respect for another idol's jurisdiction |
| Fujita Kotone | **STRENGTHEN** | E022 sibling-derived care expertise and explicit “older friend” framing for Mao; E026 support labor becomes felt responsibility | worker-idol competence includes care, social translation, and visibility of hidden production labor |
| Arimura Mao | **STRENGTHEN / REVISE** | E022 links continued training to Mao's perceived last chance. She receives care, attends with Kotone and states her intention to face Sena and herself. | refractive role authorship requires capacity to receive care and include vulnerable/private material, not protect a sealed prince role |
| Katsuragi Lilja | **PRESERVE** | no major direct speaking role in the final tranche | retain Phase-3 and earlier Phase-4 formulation |
| Kuramoto China | **PROMOTE / STRENGTHEN** | E025 explicitly names her next student-council president; she accepts accountability, refuses Hiro's help when ownership of repair matters, and organizes a collective answer | accountable inheritance now has a concrete future office: institutional receptive authority |
| Shinosawa Hiro | **STRENGTHEN** | E023 brings Temari a useful clue, supports her choice and reports the outcome to Misuzu; E025 identifies herself as a next-council candidate and respects China's refusal | resistance-seeking coexists with sophisticated relational modeling and boundary-respecting help |
| Himesaki Rinami | **STRENGTHEN** | E021 uses enough authority to prohibit Sena/Tsubame from council work and coordinate a training ban | reversible hospitality can become protective command when role obligation blocks self-care |
| Shiun Sumika | **PRESERVE** | no major direct speaking role in the final tranche | retain Phase-3 and earlier Phase-4 formulation |
| Hanami Ume | **STRENGTHEN** | E024 invites Sena to keep singing ENDLESS DANCE with the juniors; Sena credits Ume with encouraging other participation (E024-04 L340, E024-05 L319–323). E025 proposes workflow tooling; E026 turns predecessor language into direct self-address | reciprocal propulsion includes cultural permission-giving, process design, and increasingly autonomous self-motivation |
| Hataya Misuzu | **STRENGTHEN** | E023 states possessive gift logic; E024 corrects Sena's inheritance model; E025 says supporting a trusted president feels like a hobby | centripetal attachment can generate highly reliable selected labor without becoming universal industriousness |
| Juo Sena | **PROMOTE / REVISE** | E021 private imperfection strengthens Tsubame's fandom; E024 producer year culminates in learning from juniors and abandoning one-way song relinquishment | generative supremacy matures toward circulatory legacy rather than successor replacement or self-erasure |
| Amaya Tsubame | **STRENGTHEN** (origin datum; relabelled from PROMOTE / REVISE, HSCA-108) | E021 documents childhood fandom, post-H.I.F. “Sena is complete” despair, and renewed belief that Sena can be reached | heroic rivalry has a historical collapse state; mature form depends on intimate knowledge and recovered counterfactual imagination; the Tsubame core never claimed an uninterrupted heroic rivalry, so E021 adds an origin datum compatible with the core (§1–§3, §5; `学園No.2《こんなもの》に、価値なんてない`, `adv_event_021_main-04` L181) |

**Phase-4 numbered-event state:** COMPLETE under Source Lock 1.0 — 136 dedicated event scripts / 8,507 messages across the four canonical tranche readings.


<!-- PHASE5_SUPPORT_SERIES_01_2026-08-23 -->
## Phase 5 — Support Series 1 character-state additions

**Authority:** `GKM_SUPPORT_SERIES_01_DEEP_READING.md` — Drive `1bIaJl--tZuINAqz_mhNfufWMLjnEibwz`; 26 scripts / 470 messages.

| character | transition | Support Series 1 evidence | current implication |
| --- | --- | --- | --- |
| Hanami Saki | **STRENGTHEN / REVISE** | S0000 converts China's fatigue into immediate optimization and initially cites Ume as the baseline; separately turns Hiro's academic first place into a rematch goal | care defaults to diagnose→prescribe→act, but individualization is not automatic; Ume's exceptional body can distort Saki's first calibration |
| Tsukimura Temari | **STRENGTHEN** | S0001 shows late-middle-school Temari volunteering for every vocal opportunity and privately judging unused opportunity; high-school Saki is interesting because she competes for the floor | professional severity and initiative norm predate Class 1-1; direct peer competition is attractive because it answers passivity |
| Fujita Kotone | **STRENGTHEN** | S0002 uses exaggerated `だいしゅきぃ♪` to end Saki's intervention and later recruits Hiro to hide her from Sena while dismissing her own talent | performative sweetness is a boundary-management tool; self-denial and material motivation remain durable ordinary-life priors |
| Arimura Mao | **STRENGTHEN / REJECT** | S0003 practices cute performance but resists public exposure for image-strategy reasons; returns from dojo under a proper curfew exception and lectures Kotone | reject “cannot perform cute”; embarrassment concerns exposure/authorship; senior competence includes mundane dorm governance and ongoing martial practice |
| Himesaki Rinami | **STRENGTHEN / REVISE** | S0004 improves an acting exercise when told to stop imitating “little-sister-ness” and imagine a real close person; actual younger-sister care is affectionate but firm | relational imagination is more authentic than archetype imitation; sisterly care includes direction and skepticism, not only softness |
| Shinosawa Hiro | **STRENGTHEN / REVISE** | S0005 asks Temari for harsher criticism and wants extended observation of China's posture | resistance-seeking extends into interpersonal evaluation and embodied observation; unusual curiosity can overshoot social scale without implying a generic self-harm motive |
| Katsuragi Lilja | **STRENGTHEN** | S0006 struggles specifically with a Japanese tongue twister while functioning normally in ordinary conversation; shares won ice-cream tickets with Sumika | language/culture vulnerability is task-specific; good fortune is readily converted into shared pleasure |
| Shiun Sumika | **STRENGTHEN** | S0007 prefers karaoke to formal singing lesson and uses a promised crepe to restore Kotone's work mood | pleasure is an active renewal/care technology rather than mere avoidance or reward after “real work” |
| Kuramoto China | **STRENGTHEN** | S0008 openly names poor PE history, accepts trainer criticism, asks to retry, and is overwhelmed with excitement by ordinary dorm communal life | weakness-awareness and persistence coexist; wealth does not substitute for horizontal peer-life experience |
| Hanami Ume | **STRENGTHEN** | S0009 shows Saki's extreme running notes converging with trainer calibration because of Ume's athletic history; Ume then converts a disastrous Worst Three vocal lesson into another group attempt | exceptional body is institutionally confirmed; ordinary social leadership is morale conversion rather than domination |
| Hataya Misuzu | **PROMOTE / STRENGTHEN** | S0010 automatically prepares Temari's drink/towel after rupture, then deliberately leaves them indirectly; separately bakes for Ume and accepts help | care persists as habit but contact route can be changed to respect a boundary; domestic care is generalized, not Temari-exclusive |
| Juo Sena | **STRENGTHEN / REVISE** | S0011 interprets trainer praise as proof of personal completion and immediately turns toward scouting younger idols; later reviews incoming-student/council prospects with Rinami | generative work partly answers plateau anxiety; “perfect” is a trainer/self inference, not objective authorial closure |
| Amaya Tsubame | **STRENGTHEN** | S0012 gives Saki exact biomechanical correction, recognizes rapid uptake/etiquette, considers council recommendation, and is again academic first among seniors | severity is translated into actionable teaching; disciplined routine and instructional competence generalize beyond rivalry |

**Phase-5 modeling note:** Series 1 primarily adds low-stakes behavioral priors and default care/avoidance mechanisms; no Phase-3 model is rejected wholesale.

<!-- PHASE5_SUPPORT_SERIES_02_PART_001_025_2026-08-23 -->
## Phase 5 — Support Series 2 Part 001–025 character-state additions

**Authority:** `GKM_SUPPORT_SERIES_02_PART_001_025_DEEP_READING.md` — Drive `1j7SzxEJ0KnP4GNYlvxEqNsJE3rSXFlPM`; 52 scripts / 961 messages, actual story range `story_0000`–`story_0025`.

| character | transition | Series-2 support evidence | current implication |
| --- | --- | --- | --- |
| Hanami Saki | **STRENGTHEN** | accepts Ume's extreme physical affection by changing its delivery; reads Sumika's body as optimization opportunity; stops one training domain before harm but immediately opens another | care increasingly models as channeling intensity rather than suppressing it; optimization remains default attention and can be compartmentally excessive |
| Tsukimura Temari | **STRENGTHEN** | reflexively defends Misuzu while criticizing her; hides diet interest behind hypotheticals; permits Kotone's listening/meal intrusion; rescues and teaches Hiro while denying friendship | attachment, appetite vulnerability, and enacted care can exceed her declared social labels |
| Fujita Kotone | **STRENGTHEN** | completes dorm chores despite evasive presentation; rejects Sena's money because debt/future-income uncertainty violate her material ethics; updates her view of Sena at festival without consenting | practical reliability and financial autonomy are stronger priors than surface unseriousness; admiration and consent remain separate |
| Arimura Mao | **STRENGTHEN** | learns through narrative/role access rather than rote memorization; provides concrete festival aid to Lilja; anticipates Rinami's needs at beach while being flustered by reciprocal cute/protective framing | role cognition is a general cognitive style; princehood is practical competence and can coexist with receiving care awkwardly |
| Himesaki Rinami | **STRENGTHEN** | transfers lesson-state routines into study; explicitly wants a long idol career growing with fans; mirrors Mao's protective logic back onto Mao | continuity/reversible hospitality now includes explicit career philosophy and cross-domain self-regulation |
| Katsuragi Lilja | **STRENGTHEN** | initiates playful cheek-poking with Sumika, studies through kanji difficulty, gives Mao homemade thanks and wants to become a similarly kind senior | familiar safety permits mischievous initiative; received care is converted into future senpai identity |
| Shiun Sumika | **STRENGTHEN** | refuses Saki's unwanted muscle optimization directly; tolerates Ume monologue-trigger fallout; reassures Lilja by naming her real incremental-work strength; trades fashion knowledge with China | social intelligence includes boundaries, listening labor, and recipient-specific reassurance rather than indiscriminate cheerfulness |
| Kuramoto China | **STRENGTHEN / REVISE** | ordinary walking/nature is novel due car-centered life; entrance-day memory shows she physically supported Hiro; knows formal yukata dressing while being naïve about youth-fashion reinvention | sheltered wealth produces uneven experience, not global incompetence; reciprocal competence with peers is increasingly central |
| Shinosawa Hiro | **STRENGTHEN** | chooses Temari as strict swimming teacher, accepts Misuzu's recovery care, states difficult tasks are enjoyable because they are difficult *for her* | resistance-seeking remains recipient-relative, self-chosen, and compatible with care acceptance |
| Hanami Ume | **STRENGTHEN** | tackle-hugging is recipient-specific sibling affection; *2026-11-26 qualification.* In this scene Ume calls the surprise tackle a hug, offers to limit it to Saki and announces a different approach after Saki’s instruction. Standing permission and contact remain open; trusts Saki's nutrition/body governance; defeats Sena in swimming; recognizes senior poses cannot simply be copied | intensity and athletic superiority coexist with relational trust and growing authorship distinct from imitation |
| Hataya Misuzu | **STRENGTHEN** | can nap with Hiro rather than supervise; asks for private swimming instruction after declining group participation; investigates food/body issues indirectly; remains easy low-tempo companion | selective participation is authored condition-setting, not simple apathy; care can be supervisory, participatory, or indirect |
| Juo Sena | **STRENGTHEN / REVISE** | gives China technical producer feedback; offers Kotone money and misreads positive signals; loses to Ume athletically; shows broad festival-community trust | producer/generative authority is concrete but bounded by consent, domain-specific superiority, and others' autonomy |
| Amaya Tsubame | **PRESERVE** | no direct appearance in this tranche | retain current Phase-4/Series-1 formulation |

**Phase-5 support coverage after this tranche:** 78/498 scripts / 1,431/9,777 messages.

<!-- PHASE5_SUPPORT_SERIES_02_PART_026_050_2026-08-23 -->
## Phase 5 — Support Series 2 Part 026–050 character-state additions

**Authority:** `GKM_SUPPORT_SERIES_02_PART_026_050_DEEP_READING.md` — Drive `1N8cUGstn4VM0sTfLJ_IQVhKfxKDIyL-j`; 50 scripts / 995 messages, `story_0026`–`story_0050`.

| character | transition | durable support evidence | current implication |
| --- | --- | --- | --- |
| Hanami Saki | **PROMOTE / STRENGTHEN** | childhood meal-making for Ume developed through practice after failure; Ume independence produces jealousy she explicitly knows is healthy; teaches Lilja while receiving motivation from Lilja's persistence; visual/yoga blind spots corrected immediately | care is system-building; sister exclusivity anxiety does not negate differentiation; peer pedagogy is reciprocal |
| Tsukimura Temari | **PROMOTE / STRENGTHEN** | accepts China as “very close” after resistance; wants Class 1-2 friends at holiday gathering; monitors Misuzu's current effort; accepts trainer fundamentals; inner food/praise delight exceeds outer register | declared distance increasingly understates enacted intimacy; professional severity coexists with ordinary pleasure and continuing relational investment |
| Fujita Kotone | **STRENGTHEN** | explicitly treats lesson time as scarce resource; comparison-shopping is habitual expertise; mutual fashion/food/errand life with Sumika and Temari | scarcity is converted into practical competence rather than only burden; ordinary friendship behavior is now highly modelable |
| Arimura Mao | **PROMOTE / STRENGTHEN** | Rinami face-saves coffee preference; Sumika teaches publicity while Mao freely improvises prince play; Temari sees Mao frightened but still doing dorm safety work and joins | role authorship, duty, and vulnerability coexist; seniority can receive practical help without collapse |
| Katsuragi Lilja | **PROMOTE / STRENGTHEN** | openly angry when Ume ignores her; competitive in skiing; spontaneous smile appears around Sumika affect; explicit friendship/training reciprocity with Saki | softness is not boundarylessness; familiarity permits anger, rivalry, and stronger claim-making |
| Kuramoto China | **STRENGTHEN** | practiced fish cooking earns Sena's respect; returns help to Temari through acting analysis; values friend-game play; accepts future responsibility framing | receptive authority increasingly becomes contribution and domain expertise rather than gratitude alone |
| Shinosawa Hiro | **PROMOTE / STRENGTHEN** | open-ended knitting fascinates because stopping is difficult; reframes Ume's Santa dream through literal analogy; actively hosts games and values friends' enjoyment | resistance includes ambiguous completion; recipient enjoyment provides relational afterlife to effort |
| Himesaki Rinami | **PROMOTE / STRENGTHEN** | becomes Misuzu's learner in Japanese cooking; reads SSD/coffee subtext; relays Ume's admiration to Saki without taking over relationship | receptive authority includes face-saving interpretation and accurate information routing |
| Shiun Sumika | **PROMOTE / STRENGTHEN** | splits food with Temari, plans group hotpot, teaches Mao publicity, trades fashion expertise with Kotone, influences Temari's tracking routine | pleasure and casualness are deliberate social-regulation tools; her expertise is operational, not merely stylistic |
| Hanami Ume | **STRENGTHEN** | childhood bodily resilience and rivalry; Santa aspiration to make people happy; can overrun Lilja's pace but apologizes; sibling affection remains highly direct | intensity is longstanding; calibration/listening is the main ordinary-life failure mode, not lack of care |
| Hataya Misuzu | **PROMOTE / STRENGTHEN** | Japanese cooking competence; Valentine care plans Temari's surrounding diet/skin risk; precise Kotone facial observation; care remains selective and recipient-specific | low effort is not low competence; care often appears as anticipatory environmental design |
| Juo Sena | **PROMOTE / REVISE** | respects China's practical competence; peers see Kotone pursuit as unusually intense; imports Misuzu's care method; “unfinished” Tsubame is praise because growth remains possible and also a deliberate playful rank provocation (HSCA-068) | supremacy is domain-bounded; generative care learns from others but still risks over-management when consent is weak |
| Amaya Tsubame | **PROMOTE / STRENGTHEN** | No.2 dance ranking; hears Sena's “unfinished” as condescension; elite council workflow and explicit next-generation teaching role | rivalry includes deliberate playful rank provocation from Sena alongside her sincere valuation of growth, so the friction is mutual sport as well as misreading (HSCA-068; `adv_csprt-2-0049_01` L32, L44, L102, L136; `_02` L113, L123); administrative competence is itself a major character domain |

**Phase-5 support coverage after this tranche:** **128/498 scripts / 2,426/9,777 messages**.

<!-- PHASE5_SUPPORT_SERIES_02_PART_051_074_2026-08-24 -->
## Phase 5 — Support Series 2 Part 051–074 character-state additions

**Authority:** `GKM_SUPPORT_SERIES_02_PART_051_074_DEEP_READING.md` — Drive `1ltF2IUHs9HJZdHB8zTW2XsIbqmRyTPhP`; 52 scripts / 1,037 messages; actual included story IDs `0051,0052,0053,0054,0056,0058–0077,0079`.

| character | transition | durable final-Series-2 evidence | current implication |
| --- | --- | --- | --- |
| Hanami Saki | **STRENGTHEN** | `0072` accepts nominal defeat in acting when Mao reframes success as audience-facing craft; `0076` converts sleep trouble into bounded body-investment advice | competitiveness is responsive to better success metrics; optimization is highly useful when recipient/cost calibration is good |
| Tsukimura Temari | **STRENGTHEN** | `0061` turns positive body-composition praise into immediate weight anxiety before accepting Rinami's compliment; `0063/0067/0071` show warmth under Ume care and private recognition of Sena fallibility | internal affect is fast and soft while external naming remains resistant; body/weight threat parsing can precede rational clarification |
| Fujita Kotone | **STRENGTHEN / REVISE** | `0058` accepts temporary dependency from Rinami; `0076` considers paid sleep support as investment; `0079` accepts Tsubame's directive health judgment while complaining | reject “resists care”; she resists leverage/debt/future control, not evidence-grounded or bounded care |
| Arimura Mao | **PROMOTE / STRENGTHEN** | `0054` comedy/outreach and styling; `0059` martial instruction; `0066` craft symbolism + explicit future acting ambition; `0075` first-year failure/height insecurity with Rinami affirmation | role plurality is durable; acting remains affirmative; first-year aspirational insecurity is now directly connected to Rinami's early recognition |
| Himesaki Rinami | **PROMOTE / STRENGTHEN** | `0058` suspends Kotone's older-sister role temporarily; `0060` reclassifies non-consequential error; `0061` beauty-care mentoring; `0075` first-year Mao affirmation | reversible hospitality works by changing situational meaning before demanding personal change; early Mao relation is Phase-6-grade |
| Katsuragi Lilja | **STRENGTHEN** | `0053` designs low-intensity progging for herself and Hiro; `0064` converts fandom into etiquette study; `0073` daily running yields visible stamina growth | courage/circulation now includes pacing, research, and cultural translation; technical beginnerhood is actively changing |
| Shiun Sumika | **STRENGTHEN / REVISE** | `0052` slips from guardedness into fluent enthusiasm about ballet; `0054` styling/comedy collaboration; `0073` roommate correction and long-distance-running strength | painful ballet history does not equal rejection of ballet as art; social ease combines aesthetic expertise, body knowledge, and ordinary accountability |
| Kuramoto China | **STRENGTHEN** | `0051/0074` reciprocal tea learning with Misuzu; `0052` draws out Sumika's ballet enthusiasm; `0068` explicitly accepts “friends becoming closer” experiment with Hiro | sheltered background remains uneven, not global; formal register coexists with curious peer play and widening reciprocal expertise |
| Shinosawa Hiro | **STRENGTHEN** | `0053` differentiates her resistance-seeking from Lilja's catch-up effort; `0059` detects gamification side effect; `0068` experiments with conflict as intimacy; `0056` seeks Tsubame mentorship | curiosity increasingly targets systems and relationships as well as bodily resistance; technical/social experimentation remains bounded by feedback |
| Hanami Ume | **STRENGTHEN / REVISE** | `0063/0067` notices Temari's physical/social need quickly but can over-deliver; `0077` teaches Sena watermelon smashing and proposes successor-generation council rituals | social perception is stronger than a “blunt athlete” model; recurring error is intensity calibration, not failure to notice |
| Hataya Misuzu | **STRENGTHEN** | `0051/0074` tea posture, tea knowledge, baking, ingredient adaptation; `0065` respects Mao while preserving her own pace | low-effort orientation is selective motivation layered over real practical/cultural competence, not generalized incapacity |
| Juo Sena | **STRENGTHEN / REVISE** | `0069` fan labor and distributed succession; `0071` deliberately routes Kotone campaign through school to avoid anticipated refusal; `0077` accepts novice status under Ume | generative authority is receptive when she sees value; in `0071` she conceals her authorship of the campaign to pre-empt a refusal based on who proposed it, while Kotone retains and exercises the choice to accept and Temari reads the move as clumsiness (HSCA-067; `adv_csprt-2-0071_01` L71, L136, L140, L144); successor legitimacy includes junior authorship |
| Amaya Tsubame | **PROMOTE / STRENGTHEN** | `0056` reverses from severity to safety care with Hiro; `0066` receives Mao's symbolic craft; `0079` integrates Sena fandom with rivalry and ends Kotone training on health grounds | severity is condition-sensitive and professional rather than indiscriminate; mentorship can be directive care; fandom does not weaken rivalry |

**Phase-5 support coverage after this tranche:** **180/498 scripts / 3,463/9,777 messages**. Architecture-defined Support Series 2 is COMPLETE; Phase 5 remains IN PROGRESS.

<!-- PHASE5_SUPPORT_SERIES_03_PART_001_025_2026-08-24 -->
## Phase 5 — Support Series 3 Part 001–025 character-state additions

**Authority:** `GKM_SUPPORT_SERIES_03_PART_001_025_DEEP_READING.md` — Drive `1Snam3YqLTESB_7hHz2_OYdhHoEoNk7YG`; 78 scripts / 1,534 messages, actual boundary `story_0000`–`story_0025` (26 three-part stories).

| character | transition | durable Series-3 evidence | current implication |
| --- | --- | --- | --- |
| Hanami Saki | **STRENGTHEN / REVISE** | explicitly claims Temari/Kotone as friends; tutors Kotone without demanding immediate repayment; enforces Ume rest and trainer-program discipline; snake-lunch and massage scenes expose recipient-calibration failures | friendship and care are deliberate social infrastructure, but optimization must be modeled on a separate consent/preference axis |
| Tsukimura Temari | **PROMOTE / STRENGTHEN** | checks injured Kotone and verifies she skipped work; appreciates Class 1-1 closeness while tiring socially; remains mutual regulator with Misuzu during estrangement; calls `りんはぁ` during thunder panic | declared distance understates enacted care; Rinha now has direct attachment/safety evidence; social belonging and social battery must both be modeled |
| Fujita Kotone | **PROMOTE / STRENGTHEN** | cleaning competence from jobs/siblings; academic failure linked to work time; accepts hardship-system help from Rinami; Sena belief becomes private short-term motivational scaffolding without recruitment consent | time poverty, not global incompetence, explains several weaknesses; help acceptance depends on leverage, repayment, reputation, and control |
| Arimura Mao | **PROMOTE / STRENGTHEN** | Rinami mistakes first-year Mao for a senior; early prince behavior already solves orientation problems; mature Mao declines council because she wants the spotlight (GKM-SAA-013); protects work-exhausted Kotone | princehood is practical care technology and positive aspiration, not a mask to discard; spotlight desire is consciously owned |
| Katsuragi Lilja | **STRENGTHEN** | early dorm anxiety and self-assessed talent deficit; Mao becomes senior anchor; refuses karaoke for an idol stream; domestic best-friend life with Sumika | shyness is compatible with firm preference boundaries; overwork is driven by fear of falling behind, not weak desire |
| Kuramoto China | **PROMOTE / STRENGTHEN** | Rinami is explicit idol ideal; future-presidency possibility is visible to seniors; home visit establishes first school-friend invitation; verbally affirms Ume/Hiro friendship | admiration is evaluative and can correct an admired person's self-downgrade; friendship and authority grow through explicit reciprocation |
| Shinosawa Hiro | **PROMOTE / STRENGTHEN** | explicitly says she has never had friends; asks Ume/China to classify the relationship; difficulty/overexertion remains intrinsically interesting; academic mastery does not translate automatically into teaching | prior friendlessness is direct biography; social praise can destabilize her more than academic difficulty; pedagogy requires theory-of-mind calibration |
| Himesaki Rinami | **PROMOTE / STRENGTHEN** | first Mao encounter; student-council and newcomer support; China treats her as idol ideal; identifies Kotone hardship aid and offers to navigate it | receptive authority includes institutional routing and can itself become idol charisma; support of aspirants is a positive vocation |
| Shiun Sumika | **PROMOTE / STRENGTHEN** | `親友` for Lilja; notices distress but preserves nondisclosure; late-return boundary asks communication, not less ambition; domestic food/shopping/photo routines | friction reduction and agency preservation are stable care principles; Lilja relationship is a domestic operating system, not episodic support |
| Hanami Ume | **PROMOTE / STRENGTHEN** | explicit friendship cluster with China/Hiro; private-room competence; accepts sibling rest governance; intuitively trusted Sena to make her stronger | social ecology is richer than athletic-rival framing; calibration rather than perception is the main ordinary-life error mode |
| Hataya Misuzu | **PROMOTE / STRENGTHEN** | uses council work as legitimate route toward Temari; indirect moderate-training demonstration; elite lesson produces mutual compromise; class-wide anti-overwork care lowers injuries but snack care raises weight | even estranged, Temari remains part of her regulation system; care can scale to environment/class and can also overcorrect |
| Juo Sena | **PROMOTE / REVISE** | Kotone is first person she says she wanted to produce; current council explicitly designed as pseudo-agency; she accepts Misuzu's refusal to explain and resolves to earn voluntary disclosure; pursuit of Kotone remains invasive | production ethics are state/domain-dependent, not uniformly coercive or uniformly consent-safe; institution-building and pursuit must be separated |
| Amaya Tsubame | **STRENGTHEN** | council-formation material reaffirms vice-president / standards-enforcer role beside Rinami's softer support | administrative severity is part of a differentiated governance system, not generic hostility |

**Phase-5 support coverage after this tranche:** **258/498 scripts / 4,997/9,777 messages**.

<!-- PHASE5_SUPPORT_SERIES_03_PART_026_050_2026-08-24 -->
## Phase 5 — Support Series 3 Part 026–050 durable character deltas

| character | transition | evidence delta | current modeling consequence |
| --- | --- | --- | --- |
| Hanami Saki | **STRENGTHEN / OPEN** | nutrition study expands beyond Ume; jealousy at Ume's friend-vacation triggers her own friendship display; arcade play becomes accessible through challenge; asks what Ume wants after defeating her | optimization expertise is becoming socially portable; leisure is not rejected when it can be entered through mastery; Ume's future beyond Saki remains an open identity question |
| Tsukimura Temari | **MAJOR REVISE / STRENGTHEN** | practical ceasefire with Misuzu under estrangement; post-reconciliation explicitly refuses full restoration of old SyngUp form; learns culture-festival enjoyment from Sumika; trusts Lilja while physically afraid on ice; first-year peers use her as `Campus mode!!` reference | relationship labels remain weaker than access behavior; repaired Misuzu bond preserves functions while rejecting old fusion; defended competence is state-dependent and collapses in unfamiliar physical domains |
| Fujita Kotone | **STRENGTHEN** | coordinated summer play with Saki/Temari; visibly affected by Saki's direct affection; Sena's elite running baseline irritates but also motivates self-authored effort | can accept belonging without accepting exaggerated intimacy or Sena's production claim; competitive irritation is a viable motivational input when autonomy remains intact |
| Arimura Mao | **PROMOTE / STRENGTHEN** | mundane laundry/tea/craft intimacy with Rinami; passes dorm cooking tradition to Lilja; practices `Campus mode!!` critique so knowledge can be handed to juniors | princehood, cute craft preference, domestic labor, and senior pedagogy coexist; institutional inheritance is enacted through ordinary care rather than persona abandonment |
| Katsuragi Lilja | **MAJOR STRENGTHEN** | childhood persistence memory from Sumika; Sumika's original idol invitation is a causal courage anchor; teaches Temari skating; reciprocal Sweden/Japan food exchange with Mao | courage-made-circulatory gains a concrete early input; competence is domain-specific and allows Lilja to become teacher rather than perpetual beginner |
| Kuramoto China | **STRENGTHEN** | learns to design invitations around Ume's motives; first festival with Rinami becomes inherited council ritual; Valentine burden-awareness correction with Sena; friendship with Ume/Hiro explicitly survives rising work demands | sheltered experience increasingly coexists with sophisticated recipient modeling; admiration can be corrected by attention to burden; institutional memory becomes something she is expected to pass forward |
| Shinosawa Hiro | **MAJOR PROMOTE** | first multiday friend vacation; shared practical incompetence with China; friendship definition matures from verification-seeking to simple durable affection that can survive adult distance | friendlessness is no longer the governing social state; relationship simulation should treat Ume/China as a secure friendship home whose validity does not require constant proof |
| Himesaki Rinami | **PROMOTE / STRENGTHEN** | passes a private festival viewing place from an older council member to China; becomes safe low-pressure person for Sena; personalized Valentine design tracks individual tastes; `Campus mode!!` teaching framed as baton handoff | receptive authority includes memory transmission and network-scale recipient modeling; care is increasingly institutional without ceasing to be personal |
| Shiun Sumika | **MAJOR STRENGTHEN** | childhood support and idol invitation catalyze Lilja's action; teaches Temari how to enjoy culture-festival work; teaches Saki leisure through game competition | friction-reduction is a durable pedagogy: she expands another person's options without asking them to renounce ambition or seriousness |
| Hanami Ume | **STRENGTHEN** | private multiday vacation with China/Hiro; consciously copies Saki's ideal routine; wants daily friend proximity but accepts growing professional busyness | rivalry with Saki is a copied life system, while peer friendship is now an independent social category; imitation is conscious strategy rather than absence of self |
| Hataya Misuzu | **MAJOR REVISE / STRENGTHEN** | estrangement-era body care resumes under a bounded ceasefire; post-reconciliation explicitly abandons becoming Temari's `翼`; still wants to help Temari shine by another route | repair is continuity without restoration; care remains highly recipient-specific and sometimes boundary-blurring, but old SyngUp fusion is explicitly rejected |
| Juo Sena | **REVISE / STRENGTHEN** | admits talent-only scouting failed to model recruits' personalities; Ume exposes physical-baseline limits; Rinami is a safe person for fatigue; Kotone exposes elite baseline distortion; public Valentine popularity becomes a time/body-management burden | talent perception remains exceptional but human/consent/dosage calibration is incomplete; public exemplar labor and private exhaustion must coexist in simulation |
| Amaya Tsubame | **STRENGTHEN** | `Campus mode!!` treated as Hatsuboshi itself and as a generational standard; rejects “perfect” as endpoint and helps set harsh but purposeful senior training | institutional severity is tied to succession and representative duty, not merely personal harshness |

**Phase-5 support coverage after this tranche:** **333/498 scripts / 6,486/9,777 messages**.

<!-- PHASE5_SUPPORT_SERIES_03_PART_051_075_2026-08-24 -->
## Phase 5 — Support Series 3 Part 051–075 integration — 2026-08-24

Source authority: `GKM_SUPPORT_SERIES_03_PART_051_075_DEEP_READING.md` — 75 scripts / 1,494 messages, `story_0051`–`story_0075`.

| character | transition | durable new evidence | modeling consequence |
| --- | --- | --- | --- |
| Hanami Saki | **STRENGTHEN** | accepts relational recovery as distinct from efficient sleep; converts fighting games into research/practice/competition; explicitly treats reciprocal specialization as friendship | optimization remains dominant, but recovery and leisure can be relational; competence-seeking transfers across domains |
| Tsukimura Temari | **STRENGTHEN** | credits Saki with helping restore condition; teaches peers using received technique; accepts Kotone/Misuzu food care while denying need; remembers ramen with Misuzu + Rinha | denial remains poor proxy for access; old unit intimacy includes mundane ritual memory |
| Fujita Kotone | **PROMOTE / STRENGTHEN** | becomes broker between Temari and Misuzu; refuses payment-without-labor; workplace leadership remains strong while academics suffer from time poverty; anticipates Tsubame's preferences | commerciality is bounded by fairness; social brokerage is a first-class competence |
| Arimura Mao | **STRENGTHEN** | theatre labor grounds practical strength; black-coffee adulthood performance fails comically; protects dorm privacy; redirects China's unsafe imitation; ordinary takoyaki/melon-pan tastes | refractive role authorship expands into mundane aspiration, privacy governance, and method translation |
| Katsuragi Lilja | **MAJOR PROMOTE** | elite fighting-game rank; reproduces Sumika's old rescue method during injury-dream distress; animated fandom register; homesickness + parent attachment; ribbon-braiding expertise | competence is highly domain-specific; care can reverse direction; family distance remains emotionally active |
| Kuramoto China | **STRENGTHEN** | persists under Tsubame's severe multi-domain mentoring; explicitly knows she is loved despite low self-confidence; enters Lilja fandom sincerely; learns personalized gift reciprocity; literal imitation risk corrected by Mao | receptivity is active learning, not passivity; social/cultural competence and academic weakness coexist |
| Shinosawa Hiro | **MAJOR PROMOTE** | becomes unresolved anomaly in Sena's talent model; accepts responsibility when popularity outpaces technical readiness; experiments playfully with identity; benefits from challenge-preserving accommodations | attraction to difficulty coexists with professional accountability; support should preserve challenge while reducing unsafe load |
| Himesaki Rinami | **PROMOTE / STRENGTHEN** | first-year insecurity remains visible; discloses post-`Love☆しすたぁず` stage fear to Sumika; anime/fanart history with sister; uses own relocation loneliness to support Lilja | receptive authority is partly built from remembered vulnerability, not timeless maternal competence |
| Shiun Sumika | **MAJOR PROMOTE** | recurrent injury nightmare and fear of dancing; can receive direct comfort; athletic speed remains elite enough for Ume's respect; facilitates Hiro's identity/play through accommodation | brightness and expertise do not erase trauma; peer-cultural translation is a core social competence |
| Hanami Ume | **PROMOTE / STRENGTHEN** | explicitly separates sister-following from self-authored idol reason; recognizes stage as something everyone makes even without unit membership | individuation is authored participation, not detachment from Saki; ensemble thinking is now explicit |
| Hataya Misuzu | **PROMOTE / STRENGTHEN** | engineers indirect ramen contact during estrangement; routes cooking through Kotone; Hiro elicits genuine effort; civic care framing increases participation | care can move through intermediaries; motivation is relationally/functionally selective rather than globally low |
| Juo Sena | **REVISE / STRENGTHEN** | Hiro resists conventional talent perception; gathers testimony and direct live evidence; ordinary fandom/food/sentiment remain active | producer model can admit anomaly rather than force premature classification; elite status does not erase ordinary preference |
| Amaya Tsubame | **MAJOR PROMOTE** | high-effort China mentorship across council/idol/academics; accurate junior civic evaluation; Kotone work/academic care; public-recognition asymmetry; workload support for Sena | severity is often backed by costly preparation and systems awareness; No.2 identity includes visibility anxiety |
| Kaya Rinha | **PROMOTE distributed evidence** | `story_0058` remembers ramen queues as an ordinary three-person routine with Temari and Misuzu | Phase-6 Rinha reconstruction must include mundane attachment infrastructure, not performance evidence alone |

**Phase-5 support coverage after this tranche:** **408/498 scripts / 7,980/9,777 messages**.


<!-- PHASE5_SUPPORT_SERIES_03_PART_076_102_2026-08-24 -->
## Phase 5 closure - Support Series 3 Part 076-102 durable character deltas

Source authority: `GKM_SUPPORT_SERIES_03_PART_076_102_DEEP_READING.md` - Drive `1B43voVD6wXug902H9K49VFFDtCFLYnws` - 90 scripts / 1,797 messages.

| character | transition | durable closure evidence | Phase-6/7 modeling consequence |
| --- | --- | --- | --- |
| Hanami Saki | **STRENGTHEN** | explicitly formulates recipient-specific food care as love plus chemistry; learns from China/Tsubame; audits Sena by role rather than prestige | optimization is a care language only when calibrated to recipient physiology, consent, and current purpose |
| Tsukimura Temari | **PROMOTE / STRENGTHEN** | repaired Misuzu access creates new lunches/travel/memories; exports SyngUp unit expertise; accepts Hiro calming/teaching in unfamiliar domains | post-conflict closeness is future creation, not restoration; reluctant-care denial remains a poor access proxy |
| Fujita Kotone | **STRENGTHEN** | personalized Sena care remains emotionally powerful while production consent stays separate; prior brokerage role remains intact | affection, gratitude, and professional jurisdiction must remain separate variables |
| Arimura Mao | **PROMOTE / STRENGTHEN** | dorm leadership is explicitly repayment of care received from prior seniors; only-child history, private fantasy taste, and emotional interpretation deepen repertoire | senior/prince identity is authored through received-care reproduction rather than a fixed mask |
| Katsuragi Lilja | **PROMOTE / STRENGTHEN** | elite gaming identity confirmed; Japanese writing remains a bounded academic difficulty; private fandom and rest-permission intimacy expand social range | technical beginnerhood cannot be generalized into low competence; domain switches are essential |
| Kuramoto China | **PROMOTE / STRENGTHEN** | explicitly carries an internal Hiro model during difficult training; ordinary-life gaps remain specific; Saki identifies China as someone she can learn from | receptive authority now includes internalized peers and genuine senior-to-junior reverse expertise |
| Shinosawa Hiro | **PROMOTE / STRENGTHEN** | explicitly carries an internal China decision model; initiates public prosocial help; teaches procedural tasks patiently | important friends function as action-selection priors even when absent |
| Himesaki Rinami | **STRENGTHEN** | Love Sisters experience yields explicit unit-role/communication theory; same-year Mao intimacy remains durable | older-sister coding must coexist with peer history and institutionally useful reflective expertise |
| Shiun Sumika | **PROMOTE / STRENGTHEN** | pre-idol karaoke competence, SNS/photo expertise, and resilient entrance-exam partnership with Lilja | casual culture knowledge is teachable professional/social expertise, not decorative texture |
| Hanami Ume | **STRENGTHEN** | Tsubame uses Ume's physical expertise; rivalry drives intellectual study; nostalgia becomes future community/alumni practice | immediate physicality coexists with increasingly abstract institutional imagination |
| Hataya Misuzu | **PROMOTE / STRENGTHEN** | Tsubame designates her as future support for China/Ume; repaired Temari relation creates new memories; practical competence remains broad but selectively deployed | authored participation and hidden competence are central; low visible effort is not low capacity |
| Juo Sena | **REVISE / STRENGTHEN** | First Star status is explicit representative stewardship; ordinary adolescent leisure is comparatively underdeveloped; Saki separates president trust from producer trust | supremacy must be role-bounded; prestige does not collapse civic, producer, rival, friend, and teenager modes into one |
| Amaya Tsubame | **PROMOTE / STRENGTHEN** | private anime fandom, upward learning from Ume/Sumika, revisable traditionalism, and deliberate non-inquiry toward Sumika | mature authority includes boundary-sensitive restraint and willingness to learn down hierarchy |

### Distributed Rinha routing

Kaya Rinha receives **PROMOTE distributed evidence**, not a fourteenth playable-core row: ordinary Temari/Misuzu/Rinha food memory, direct H.I.F. interiority, future-tense dissolution-live coordination, continued worry, and playful/serious access to Ume all route to the mandatory Phase-6 distributed-character reconstruction.

**Phase-5 support coverage: COMPLETE - 498/498 scripts / 9,777/9,777 messages.**

<!-- SAKI_U1_NIGHTMARE_CORRECTION_2026-11-07 -->
## Correction — Hanami Saki U1 Episode 04 fear structure — 2026-11-07

Source authority: `GKM_CORE_01_HANAMI_SAKI.md` v2.1 §3.6.1. The A1 raw scripts were re-inspected under Source Lock 1.0. No new source object is admitted, because Unit Story 01 was already inside the Saki core’s Phase-3 scope. These rows refine the Phase-3 `U1 old-rules summer H.I.F.` row above; they do not replace it. Delta labels follow architecture §18.

| character | story_state | source_id | self_concept | desire | fear_or_constraint | behavior_delta | confidence | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Hanami Saki | U1 before the Selection (`04_04` premonition C3 @ U1, `咲季さん` only) | `adv_unit_01-04_04`; `04_05` | older sister who must not run from Ume this time | beat Ume at idolhood | premonition that one loss means never winning again and that Ume will accelerate out of reach; losing would make her `お姉ちゃん失格` | admits the fear to the Producer and refuses to flee | high within U1 | **EXTENDS** — U1 counterpart of the `D-SAKI` Dear 008–009 fear; a cross-track invariant, not a shared event |
| Hanami Saki | U1 after the Selection defeat | `04_07`; `04_09`–`04_12` | heart broken, body still driven (`15年ぶんのわたし`) | win even without a chance | belief that being overtaken once is permanent; slowed growth | acts before recovering; for the first time in her life stays in a contest after Ume has overtaken her; accepts the Producer’s correction that she is still growing | high within U1 | **CONFIRMS** SAKI-C08 across tracks |
| Hanami Saki | U1 training interval — nightmare | `04_13` | older sister whose worth to Ume depends on remaining a contest worth having | remain someone Ume wants to race | in the dream, Ume calls their contest boring, chooses a Begrazia dream and says goodbye; Temari reports recent sleeplessness | wakes and minimizes (`すごーく嫌な夢を見ただけ`), performs, and rejects the “world’s best supporter” consolation in favour of “world’s best idol” | high for occurrence and fear | **EXTENDS / COMPLICATES** — fear of losing the counterpart, not only the lead; dream-Ume is Saki-imagined and never Ume evidence |
| Hanami Saki | U1 eve of the summer H.I.F. | `04_15` | broken competitor who is not yet sure her drive survives | sleep, then compete | fear that losing again would not frustrate her; near-nightly waking and crying reported by Kotone | admits the fear to Kotone, accepts her company, and ends anticipating morning | high within U1 | **EXTENDS** — fear of losing her own competitive affect, distinct from fear of defeat; no clinical claim; no evidence that the nightmare recurs |
| Hanami Saki | U1 H.I.F. day to Prima Stella | `04_18`; `04_20`–`04_21`; `04_25` | Saki who has shown Ume her hidden flaws | beat Ume “this time” and lead every idol | sleep deprivation; still “broken” in her peers’ description | confesses before the result, gives a personal best while broken, concedes Ume’s physical superiority while welcoming every challenge, and restates the `負けたら悔しい勝負` criterion as Prima Stella | high within U1 | **RESOLVES** the relational premise of the nightmare; the fear of losing without frustration remains untested because Saki does not lose again in U1 |

## Historical source corrections — 2026-11-12

| Character | Story state | State and development | Counterevidence or limit | Locator |
| --- | --- | --- | --- | --- |
| Hataya Misuzu | C1 @ U1 | Tries to recruit Temari into Begrazia; chooses full effort, experiences Temari's pace, then recommits to winning at a walk after defeat. | Wounded self-protection and playful self-reassertion are both plausible. Misuzu's denial on Rinha's behalf is other-report. | `LOC-HSCA-001A`–`001D` |
| Hanami Saki | C1 @ D-UME | Re-enters competition after the N.I.A. loss and reports a self-producing 100 Pro plan without a new Producer. | Summer Prima Stella is Sena; the sisters' accounts of their own result differ. Burnout is observer assessment, and continuation is prospective. | `LOC-HSCA-002A`–`002E` |
| Juo Sena | C1 @ U1 | Announces retirement, reopens the decision in talking to Saki, retracts it after the unit loss and revises her evaluative criterion. | Sena's self-ranking is contested. The after-graduation roster is open. | `LOC-HSCA-004A`–`004D` |


## Source Lock 1.1 — transcript refresh, 2026-11-12

| character | story_state | source_id | self_concept | desire | fear_or_constraint | behavior_delta | confidence | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Fujita Kotone | D-KOTONE 028–037 | GKM-R86-01 | work as `天職` | wealth, acclaim and audience enjoyment | past financial emergency and continued ambition | reports repayment, wins the winter title, accepts its responsibilities and defers acting on her declared love | high within D-KOTONE | P3 final-failure names Sena |
| Juo Sena | D-SENA late winter | GKM-R86-02 | top idol and Producer | keep advancing and invite successors to compete | President's initial objection, time and workload | earns external Triple Crown, receives institutional acceptance of dual work and retains title in this track | high within D-SENA | P3 final-failure names Kotone |
| Amaya Tsubame | D-TSUBAME 028–037 | GKM-R86-03 | public title as earned office | defeat Sena and continue as rivals | mutable `学園No.2` and limited school tenure | wins winter H.I.F., invites pursuit and chooses her professional Producer | high within D-TSUBAME | P3 final-failure names Sena |
| Himesaki Rinami | E028 and separate support 3-0106 | GKM-R86-05, GKM-R86-07 | experienced worker who doubts her professional qualification | make people smile and become a professional idol | care and operations commitments, fear of replaceability | enters the festival contest, decides to sit the September exam and separately exchanges working knowledge with Temari | high in each state | exam and hiring outcome open |
| Katsuragi Lilja | E030 | GKM-R86-06 | campaign leader and cosplay practitioner | deliver a brief with Saki and Ume | initially tries to solve everything herself | consults the group, chooses the product and differentiates acting guidance for Ume | high within E030 | existing fragrance communications are separately scoped |
| Kuramoto China | Kanae 000 and M-CHINA 018 | GKM-R86-04, GKM-R86-08 | incoming president and winner | preserve a style of public leadership and support Kanae's development | concern about stature and limits of family support | wins the election, retains president-elect status during transition and approaches the Producer about Kanae | high within stated scenes | keep the two compatible witnesses separately sourced |
| Tsukimura Temari | E027 and M-TEMARI 021 | GKM-R86-05, GKM-R86-08 | professional singer learning acting and reception | gain confidence, maintain idol time and learn to receive praise | voice/acting distinction and appearance comparison | requests a lesson without joining the council and separately treats praise as professional compensation | high in each state | E027 and apparel variant differ in campaign slot |
| Hataya Misuzu | M-MISUZU 018 and support 2-0057 | GKM-R86-08, GKM-R86-07 | deliberate worker and close peer | be recognized for chosen effort | uncertainty about effort and pace as evaluated by others | accepts praise for rehearsal and demonstrates administrative recall to Sena | high in each state | relationships do not imply a reformed unit |
| Hanami Saki | M-SAKI 022 and support 2-0055 | GKM-R86-08, GKM-R86-07 | actively shaped future self | expand future performance capacity | asks whether her looks have peaked | seeks feedback, constructs a second presentation and deliberately preserves rest | high in each state | both proposed cuts remain reported plans |
| Hanami Ume | M-UME 022 and E030 | GKM-R86-08, GKM-R86-06 | actual self can compete with a projected ideal | acquire a distinct mode of expression | performance brief and imperfect fit of imitation | uses her own composure and, in E030, a separately imagined familial audience | high in each state | no shared commercial personnel assumption |
| Shiun Sumika | M-SUMIKA 018 | GKM-R86-08 | titleholder and idol using ballet-derived skill | support others' own transformations | renewed attention, family misunderstanding | pauses REVERSI by agreement and speaks directly with her mother | high within local winning state | father follow-up open |
| Arimura Mao | M-MAO 018 | GKM-R86-08 | former actor, winner and prospective professional | continue as a prince after school | deferred agreement and responsibility of title | credits juniors and has 100 Pro offer put under review | high within local winning state | no signed agreement |
| Hiro Shinosawa | M-HIRO 022 | GKM-R86-08 | idol who can seek capacity through others | give audiences a worthwhile difficult attempt | prior feat retired and expectations exceed present capacity | takes owl's advice, differentiates her answer and works on `め` | high within local winning state | publication and heard performance unresolved |

## Source Lock 1.2 — transcript refresh, 2026-11-15

| character | source state | evidence | current orientation | goal | friction | bounded exit | confidence | unresolved |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Hiwatari Kanae | Dear 001–002 | GKM-R88-01 | China’s close attendant and third-term Idol Department transfer student | learn from practical training and take the Producer's know-how | selective entrance, second assessment, terms protecting China's work | enters the department and accepts provisional production | high, C1 | desire for her own idol work has yet to be stated at entry |
| Hiwatari Kanae | Dear 008–010 | GKM-R88-01 | idol trainee who wants the stage and continues attending China | advance, catch up to China and perform again | exposure, fear, time split, incomplete sense of artistic identity | passes, accepts simultaneous production and asks to share some care work | high, C1 | future title, shared stage and performance identity open |
| Hiwatari Kanae | Produce 001 endings | GKM-R88-02 | capacity to get personal pleasure or stakes from performance across distinct outcomes | by state, improve, earn China's praise, decide whether to return, or pursue an own dream | result, knowledge gap, and state-specific trust | a true-labeled ending has explicit commitment; two normal-labeled endings debrief a failure | high for each C3 outcome | ending dispatch and chronology relative to Dear open |
| Hiwatari Kanae | Communication rank 3 episode 000 | GKM-R88-04 | performer preparing a first solo, still naming China as a source of light | inhabit song and costume in her own right | novelty of the voice she is asked to present | goes to perform her own stage in part 03 | high for stated readiness | performance result and cross-family placement open |
| Kuramoto China | H05 → Dear 001–010 | GKM-R86-04, GKM-R88-01 | Prima Stella and president-elect on entry, mentor and beneficiary of care | help Kanae find an ambition without turning it into an instruction | existing hierarchy, competing production time and imperfect household skills | facilitates transfer, finds a way to help on exam day and invites Kanae to pursue the title | high, C1 | exact China Produce route and timing of future rivalry open |

## Source-to-analysis audit corrections — 2026-11-15

Source authority: the owner-authorized change plan of the source-to-analysis audit of 2026-11-15, as landed by the content editors in the canonical homes named in the last column. Each row records what that home now says, with its A1 locators, and adds no interpretation of its own. `C1 @ [track]` means C1 within the named track; C2–C4 follow architecture §18; `C3` marks a branch or result state. Romance-coded material follows the owner policy of 2026-11-15: it is recorded and bounded, and any romance conclusion stays OPEN. Changed claims and preserved dissents (GKM-SAA-004 severity; GKM-SAA-158 against HSCA-119) are recorded in the claim-revision ledger.

Home abbreviations: CORE-x, EVM-x and AVA-x are a character's core, evidence matrix and AV revision addendum in `03_SOURCE_FACING_READINGS/01_CHARACTER_CORE_READINGS/`; RS-I and RS-II are the two relationship-systems syntheses; SIDE is the side-character synthesis; E001–005, E006–012, E013–020 and E021+ are the event readings; S01, S02a/b/c and S03a/b/c/d are the support readings; KANAE is `GKM_HIWATARI_KANAE_SOURCE_LOCK_12_READING.md`.

### Rows corrected in place

Rows above that carried a demonstrated error now carry the corrected wording and the audit ID. The earlier wording is kept here.

| Section and row | Earlier wording | Correction | Audit ID and home |
| --- | --- | --- | --- |
| Phase 3 Saki, `D-SAKI first direct Ume contest` | source `adv_dear_hski_011–012`; "wins by preparation, strategy, and total competitive construction" | first direct win placed at Dear 009: a narrow win on idol appeal while Saki concedes technical inferiority (`adv_dear_hski_009` L145, L267, L287, L313); Dear 011–012 are N.I.A. set-up and a tied ranking contest (`adv_dear_hski_012` L186–L205, L285); the FINALE is won in Dear 019. The 008–010 row gains a cross-reference, not a cut | GKM-SAA-005; RS-I §3.3, §12.1; model CORE-Saki §3.2.4 |
| Phase 3 Saki, `D-SAKI post-loss reconstruction` (source) | `adv_cidol-hski-3-017–018` cited as one post-loss block | `017_01` is set the day after the N.I.A. win, before the summer H.I.F.; `017_02–03` and `018_01` follow the summer H.I.F. (`adv_cidol-hski-3-017_01` L4; `017_02` L4; `018_01` L134) | GKM-SAA-168; CORE-Saki §16.7, SAKI-L046 |
| Phase 3 Temari, `D-TEMARI summer H.I.F.` | "agrees to SyngUp training/disbandment-live plan" | accepts SyngUp training and agrees with the Producer's veto to defer the dissolution live until after winter H.I.F. (`adv_dear_ttmr_023` L468–L514) | GKM-SAA-121; CORE-Temari §2.4 |
| Phase 3 Temari, `D-TEMARI winter victory` | "requests ramen" | calls the meeting and accepts the Producer's ramen proposal (`adv_dear_ttmr_037` L396–L432) | GKM-SAA-006; CORE-Temari §2.5, §10.4 |
| Phase 3 Kotone, `D-KOTONE H.I.F.` | "luck anxiety" | comparative doubt about Sena and the ideal; the `超自信` / `超自信がない` formula is the Producer's, endorsed by Kotone (`adv_dear_fktn_023` L43, L171–L204) | GKM-SAA-122; CORE-Kotone §3.2.17 |
| Phase 3 Mao, `D-MAO summer H.I.F. loss` | "speaks constructively in public, then privately cries `負けた`" | unguarded cry at the result with the Producer; composed framing; inner grief about not going pro with the Producer now; breakdown in front of Rinami after the party (`adv_dear_amao_027` L10–L16, L52–L57, L501–L516, L528–L598) | GKM-SAA-012; CORE-Mao §2.9; EVM-Mao MAO-C20 |
| Phase 3 Hiro, `D-HIRO crisis strategy` | "Producer engineers reputational and relationship stakes" | the Producer stakes his producer career and their dream/hobby time; Hiro infers that he would stake even their relationship and he tacitly accepts (`adv_dear_shro_028` L204–L248) | GKM-SAA-017; CORE-Hiro §14, §21, §27.3 |
| Phase 3 Sumika, `artistic coauthor` | "coauthors lyrics, choreography, styling, ballet-derived movement" | authors the choreography and drafts lyrics; the ballet-derived motion is hers, endorsed by the Producer; outfit and ponytail are chosen by the Producer at her request; fanservice and staging are his proposal, co-designed (`adv_cidol-ssmk-3-012_02` L55–L84, L112–L125; `012_03` L11, L72–L114, L183–L192) | GKM-SAA-131; CORE-Sumika §14.3, §7; AVA-Sumika `Love & Joy` row |
| Phase 3 Character 12 Sena, item 4 | "Producing Kotone, Ume, China, Misuzu, Saki, and the surrounding golden generation" | "Producing Kotone, Ume, China and Misuzu, and being challenged by Saki and the wider golden generation" (rosters `adv_dear_jsna_025` L99–L131; `026` L50–L71; `022` L369; `028` L84) | GKM-SAA-146; CORE-Sena §21, §25, already consistent |
| Phase 4 E001–005, Hataya Misuzu | motive question only | the E002 friend is unnamed there, and cross-event evidence strongly supports Temari; the motive stays OPEN | GKM-SAA-106; E001–005 §4.6, §7.6; RS-I §5.8, §12.3 |
| Phase 4 E021+, Amaya Tsubame | transition **PROMOTE / REVISE** | **STRENGTHEN** (origin datum) | HSCA-108; E021+ §2.4, §10 |
| Phase 5 S2 026–050, Sena and Tsubame | Tsubame: "rivalry includes a stable semantic mismatch" | Sena's deliberate playful rank provocation plus sincere valuation of growth; mutual sport as well as misreading | HSCA-068; S02b §25, §27, §28, §30.4 |
| Phase 5 S2 051–074, Sena | "confidence can become consent-avoidant" | she conceals her authorship to pre-empt a refusal based on who proposed it; Kotone retains and exercises the choice to accept; Temari reads the move as clumsiness | HSCA-067; S02c §20, §28.12, §33.7 |
| Phase 5 S3 001–025, Mao | "because he wants the spotlight" | "because she wants the spotlight": Mao is a girl who uses `ボク` (`adv_dear_amao_003` L81; `adv_cidol-amao-3-015_02` L147); wording only, per MAO-C14 | GKM-SAA-013; S03a |
| Phase 3 China, `C-CHINA family roots` (notes) | Kanae identification stated without qualification | rested on inference under Source Lock 1.0; explicit under Source Lock 1.2 (`adv_dear_hkne_001` L425) | GKM-SAA-212, A1 checked by the ledger editor; register entry |

### New and extended states

| Character | Story state | State and development | Counterevidence or limit | Locator | Audit ID and home |
| --- | --- | --- | --- | --- | --- |
| Hanami Saki | C1 @ D-SAKI Dear 030 | Tsubame's lesson is affirmative: Saki already has it and should know her appeal; it does not reject breadth | the judgement is Tsubame's statement | `adv_dear_hski_030` L462–L471 | GKM-SAA-039; CORE-Saki §3.2.13, §5.2–§5.3, §12.1 |
| Hanami Saki | C1 @ D-SAKI Dear 027 | holds that she owes those she has beaten a proud stance and performs confidence over doubt (answerability to opponents) | the doubt persists beneath the performance | `adv_dear_hski_027` L257–L294 | GKM-SAA-036; CORE-Saki §4.1 item 6, §7.5, §17.1 |
| Hanami Saki | C1 @ D-SAKI Dear 036–037 | closes the `勝ち逃げ` thread: her first true win is announced (Dear 036) and former athletes say their contest was not over (Dear 037) | D-SAKI-scoped | `adv_dear_hski_036` L500–L516; `adv_dear_hski_037` L308–L400 | GKM-SAA-038; CORE-Saki §3.2.14, §4.3, SAKI-L018 |
| Hanami Saki | C1 @ D-MAO 031 (cross-track) | re-authors her motive for beating Ume from sisterly duty to idol desire while still saying `お姉ちゃんなのに` | cross-track corroboration, not D-SAKI chronology | `adv_dear_amao_031` L343–L404 | GKM-SAA-120; CORE-Saki §8.1, §24 |
| Hanami Saki | supports 2-0082 and 3-0112 (SL1.1, C4) | chooses Ume's costume for movement and rips; the family keeps the sisters' bodily data with photos; the grandparents made matching costumes; Hanami Farm pumpkins for the dorm | support continuity, not dated against D-SAKI | `adv_csprt-2-0082_01` L55–L63; `adv_csprt-3-0112_01` L110; `adv_csprt-3-0112_02` L15–L90 | GKM-SAA-108; CORE-Saki §9.3, §3.4.6 |
| Tsukimura Temari | C1 @ D-TEMARI Dear 025–027 | extends the winter-preparation row with the STEP3 technical turn: the upside ceiling is raised through 961 bouts, stamina is spent efficiently under an unlosable series, and variance is embraced | Dear-scoped | `adv_dear_ttmr_025` L432–L444; `adv_dear_ttmr_026` L23–L40; `adv_dear_ttmr_027` L240–L251 | GKM-SAA-007; CORE-Temari §6.2, §3.1.1, §2.4 |
| Tsukimura Temari | support 3-0106 (SL1.1, C4) | learns audience-facing report technique from Rinami; answers Rinami's question about quitting with past hardship, self-blame toward unnamed `仲間` and `でも、アイドル、好きだから` | the `仲間` stay unnamed | `adv_csprt-3-0106_01` L76–L152; `adv_csprt-3-0106_03` L122–L159 | GKM-SAA-275; EVM-Temari TMR-R86-C03; CORE-Temari §3.4.3 |
| Tsukimura Temari | support 3-0112 (SL1.1, C4) | a low-stakes Halloween errand with Saki; asks for simmered pumpkin; family-resemblance exchange; entrusts Saki with a childhood princess-costume story and asks her to keep it from Kotone | support continuity only | `adv_csprt-3-0112_01` L110–L180; `adv_csprt-3-0112_03` L49–L176 | GKM-SAA-108; CORE-Temari §12.1, §5.1 |
| Tsukimura Temari | support 2-0078 (SL1.1, C4) | frightened in the dorm test of courage, calls for Rinha; recognises Mao's fear, reframes courage as going first while afraid and proposes a shared cheerful song | support continuity only | `adv_csprt-2-0078_01` L155; `adv_csprt-2-0078_02` L79–L182 | GKM-SAA-108; CORE-Temari §9.4 |
| Tsukimura Temari | support 3-0114 (C4) | Misuzu reports making Temari's bento each morning | Misuzu's report; care infrastructure only | `adv_csprt-3-0114_03` L42–L48 | GKM-SAA-108; CORE-Temari §7.2 |
| Tsukimura Temari | E008, E011 | in E008 Saki suggests an idol ideal and Temari’s audibly voiced private thought says that is not it and wonders how to say so. Other characters receive no spoken answer at L262. E011 supplies a separate self-monitoring witness. [Animate fan encounter](../05_AUDIOVISUAL_ANALYSIS/GKM_PHASE7_FOUR_EVENT_PERCEPTUAL_ADJUDICATION_20261125.md#the-fan-and-the-idol-image) | inner speech | `adv_event_008_main-02` L262; `adv_event_011_main-03` L320 | HSCA-174; E006–012 §13.4 |
| Fujita Kotone | C1 @ D-KOTONE Dear 012–020 | extends the Sena/N.I.A. row: the Producer seats the family in the front row of the N.I.A. final to remove her strain; her composure breaks, then turns into resolve, not instability | Dear-scoped | `adv_dear_fktn_018` L135–L136, L159–L176, L221–L231 | GKM-SAA-009; CORE-Kotone §3.2.14, §9.3, §11.2 |
| Fujita Kotone | SL1.1 D-KOTONE 028–037 | narrows the Source Lock 1.1 row's "accepts its responsibilities": an earned inheritance; after winning she takes up Sena's pride and duties toward juniors and still refuses designated succession | KOTO-C12 core preserved | `adv_dear_fktn_037` L197–L214; `adv_dear_fktn_033` L256 | GKM-SAA-010; CORE-Kotone §3.2.10, §10.3, §18.5 |
| Fujita Kotone | E012, E005 | self-described internal-progression student (`内部進学組`); Tsubame had dealt with her as a middle-division student working without permission | the E005 account is Tsubame's report | `adv_event_012_main-02` L117; `adv_event_005_main-02` L62–L95 | GKM-SAA-267; CORE-Kotone §2.1; E001–005 §3.1 |
| Arimura Mao | C1 @ D-MAO Dear 022–026 | extends the 100Pro-transition row: Mao acts first on the promise when the Producer defers; her need is grounded in adults having left her when she lost prince roles; the Producer was willing to step aside | the two-sided sequence is in the relationship ledger; the row's endpoint stands | `adv_dear_amao_022` L374–L377; `adv_dear_amao_024` L19–L22; `adv_dear_amao_025` L347–L361 | GKM-SAA-001 (P1); CORE-Mao §2.8, §8.4a, §8.5 |
| Arimura Mao | pre-Producer Hatsuboshi years 1–2 (track-labelled) | enrolled clinging on after her dismissal from the troupe (Dear 003 L92; cidol 007_01 L96); first-year Prima Stella aim; poor N.I.A. result; missed the second-year H.I.F. main stage; declined scout offers; near-abandonment before the Producer | mostly self-report; Mao refuses the scouts (Dear 002 L230) | `adv_cidol-amao-3-007_01` L96–L157; `adv_dear_amao_002` L225–L230; `adv_dear_amao_010` L39; `adv_dear_amao_011` L18; `adv_event_021_main-04` L199 | GKM-SAA-055; CORE-Mao §2.2, §2.3a, §13.3 |
| Arimura Mao | ordinary-life invariants (C2/C4) | only child who missed school for work and played alone; wished for a sister; hides sweets, melon bread and children's books to protect the cool image; height device; revue-troupe motto; nerves before the stage; calls herself always wavering | modular; not dated | `adv_cidol-amao-3-009_02` L192–L201; `adv_event_022_main-05` L42–L74; `adv_csprt-3-0040_03` L124 | GKM-SAA-196 (with the HSCA-102 residual); CORE-Mao §14.5 |
| Arimura Mao | E028 school festival (SL1.1) | coaches first-years in theatre to leave something to juniors; will sit the September 100 Pro affiliation exam though unsure of `本所属` | numbered-event variant, not dated against D-MAO | `adv_event_028_main-02` L124–L160; `adv_event_028_main-01` L272 | GKM-SAA-104; CORE-Mao §2.8 |
| Arimura Mao | support 3-0078 (C4) | the loss of the admired figure is still active in support-time Mao | state undated | `adv_csprt-3-0078_03` L136–L151 | HSCA-008; S03d §4 |
| Katsuragi Lilja | ordinary life (C2/C4; C3 items labelled) | Advent candles, Lucia and Lussekatter; Drömmar from her mother, her father's favourite; Hasselback; wagashi; つむじちゃん goods from her father and her シルヴェスタ fandom; fear of crowds; insects (C3); childhood fevers (Sumika's report, E012); ribbon braid learned from her mother; active homesickness | "mother's perfume" was not landed (no locator found) | `adv_cidol-kllj-3-005_01` L88–L191; `adv_cidol-kllj-3-018_02` L21–L42; `adv_cidol-kllj-3-005_02` L145–L171; `adv_event_012_main-04` L676–L684; `adv_csprt-3-0074_02` L104–L119 | GKM-SAA-205 (PARTIAL); CORE-Lilja §13.5 |
| Kuramoto China | C1 @ D-CHINA 003, 032; E005 | the headmaster (Sena's grandfather) appraises China's latent talent as comparable to Sena's and China above Sena as an entertainer; her technique stays weak | the headmaster's interested appraisal; CHINA-C02 preserved | `adv_dear_kcna_003` L97; `adv_event_005_main-02` L187; `adv_dear_kcna_032` L164 | GKM-SAA-062; CORE-China §4, §24.9 |
| Kuramoto China | C1 @ D-SENA; C1 @ D-HIRO (cross-track) | in D-SENA Sena produces China: a media-first career in which China sometimes forgets she is an idol; in D-HIRO China is more famous than Sena, has an unlimited-budget song and names Hiro her top rival; core traits recur | exclusive with D-CHINA; the core's dependency claims are scoped to China-owned tracks | `adv_dear_jsna_017` L244–L275; `adv_dear_shro_027` L222–L231; `adv_dear_shro_032` L394 | GKM-SAA-065; CORE-China §18, §24.4 |
| Kuramoto China | C-CHINA family roots (cidol 009; supports 3-0075, 3-0122) | early-childhood loneliness while the family was away on Kuramoto Group duty, which China frames as `わがまま`; resolved after the apprentice's petition (Kanae, explicit at SL1.2); a present-tense secure sense of being loved | "loved" is scoped to the present; CHINA-C01 preserved | `adv_cidol-kcna-3-009_02` L43–L217; `adv_csprt-3-0075_02` L60–L108; `adv_csprt-3-0122_01` L77–L99; `adv_dear_hkne_001` L425 | GKM-SAA-061, GKM-SAA-212; CORE-China §2, §19, §25 |
| Kuramoto China | Produce Events (C3, choice-labelled) | villa with maids; dorm longing and a self-petition resolve; maid-chosen clothes; managed meals and car commute; household-conditioned overnight stays; preferences for rain and milk tea, milkshakes, hamburgers, hot springs and hamsters; dislike of shooting; the S1-0008 dorm tour | felt-dog hobby, promise-keeping and last-minute work were not landed (no A1 locator) | `adv_pevent_001_kcna_activity_005` L13–L80; `activity_014` L20, L62; P1 `after-step-1-normal-03` L56–L89; `sales_3-005-01` L6, L41 | GKM-SAA-064 (PARTIAL); CORE-China §20 |
| Kuramoto China | support 3-0122 (SL1.1, C4) | a bear plush eased loneliness when her parents were busy; Kanae's companionship reduced it; China has pulled Kanae into photos since childhood; Kanae's `私のアイドル` and lifelong-photobook frame are aspirational | support continuity only | `adv_csprt-3-0122_01` L77–L182; `_02` L62–L165; `_03` L51–L162 | GKM-SAA-108; CORE-China §19 |
| Shinosawa Hiro | C1 @ D-HIRO origin | a longing layer beneath the unsuitability entry logic: the wish to be cute, with owl as trigger (`それが、きっかけ`); HIRO-C01's central claim (no pre-formed top-idol dream) is preserved | P1 `final-normal-03` L41–L43 and Dear 019 L34–L44 are choice 1 only | `adv_dear_shro_010` L183–L199; `adv_dear_shro_024` L185–L203 | GKM-SAA-002 (P1); CORE-Hiro §1.1, §9, §11, §16–§18, §26 |
| Shinosawa Hiro | P3-C final-failure (C3) | the stake is paid and the partnership continues with Hiro's consent | C3 result state; ethics OPEN | `adv_pstory_003_shro_final-failure-01` L16–L82 | GKM-SAA-017; CORE-Hiro §14, §27.3 |
| Himesaki Rinami | P1[RINAMI], P2[RINAMI] (C3) | P1 failure opens with self-removal or `私なんか`; recommitment is invariant after the Producer's words and measured against `みんなのお姉さん`; in P2 the resolve is partly self-sourced (`悔しい`) while inner speech confirms borrowed belief | the Producer's speech precedes recommitment even in P3; parallel to, not identical with, D-RINAMI | P1 `after-audition-final-failure-01` L51, L95, L111–L117; `ending-normal-05` L17; P2 `final-failure-01` L67; P2 `b-normal-03` L68 | GKM-SAA-072; CORE-Rinami §8 |
| Himesaki Rinami | ordinary life (C1–C4 by source) | Fukuoka home and a rural hometown with many rice fields (C3); rice sent from home; parents often away at work in her childhood; snacks from her father's evening drinks instead of sweets; honey umeboshi sent by her mother; home-style ginger seasoning (choice 1 of 3) and her grandmother's recipe (choice 2 of 3); frugal packed lunch; large appetite held back during N.I.A.; karaoke self-encouragement with `ガラクタロード`; an onsen-trip wish fulfilled by chance; historical drama, evening anime with her younger sister and romance manga or film as song study; getting lost on campus as a first-year | hidden sweets and her own weight worries were not verified and are not recorded | `adv_dear_hrnm_006` L160–L193; `adv_event_017_main-01` L48; `adv_csprt-3-0071_02` L30, L33; `adv_dear_hrnm_020` L263; `adv_pstory_001_hrnm_ending-normal-01` L36; `adv_event_013_main-03` L78; Dear 021 L199; `adv_cidol-hrnm-3-004_01` L14; `adv_cidol-hrnm-3-004_03` L15–L71; `adv_csprt-2-0003_01` L106; `adv_csprt-3-0051_01` L80 | GKM-SAA-222 (PARTIAL; extended in the delta sweep with the verifier-added items); CORE-Rinami §5 |
| Himesaki Rinami | C1 @ D-RINAMI Dear 033 (H.O.F.) | at the older-sister idol festival, Saki enters as an older sister who will not yield first place and Kotone because her younger siblings call her the best older sister; Rinami answers `負けないよ、相手が誰でも。私が一番の、お姉さんなんだから。`; sisterhood becomes a competitive category | D-RINAMI-scoped; one of the core's sisterhood counter-models | `adv_dear_hrnm_033` L68, L116–L135, L333 | GKM-SAA-020 (added after verification); CORE-Rinami §9 |
| Himesaki Rinami | E021, E022 | bounds the E021+ row: her protective command applies to council and duty overwork, not to shared final-year idol ambition; she will not tell Mao not to overdo it | event-scoped | `adv_event_021_main-01` L294–L316; `adv_event_022_main-03` L21–L32 | GKM-SAA-271; E021+ §2.1, §10 |
| Shiun Sumika | P2[SUMIKA] (C3) | loud competitive regret, which the Producer reads as seriousness; discomfort at being watched; unspoken bodily concern before audition B | state-scoped; not merged with D-SUMIKA | `adv_pstory_002_ssmk_after-audition-final-failure-01` L19–L71; `after-audition-a-normal-03` L37–L39; `before-audition-b-normal-01` L17–L41 | GKM-SAA-234; CORE-Sumika §6 |
| Shiun Sumika | support 3-0111 (SL1.1, C4) | Lilja's cosplay makeup teacher and photographer; shows a photo before Lilja consents (a privacy boundary); competence as care with a consent cost | support continuity only | `adv_csprt-3-0111_02` L48–L148; `adv_csprt-3-0111_03` L81–L127 | GKM-SAA-108; CORE-Sumika §8 |
| Shiun Sumika | supports 3-0093, 3-0108 (C4) | annotates the Phase-5 closure row: earnest pre-admission entry (S0093), then first-year dance-lesson skipping with the reason withheld, then Tsubame's observer claim `戻った` (S0108) | `戻った` is Tsubame's observation | `adv_csprt-3-0093_02` L23–L36; `adv_csprt-3-0108_03` L101–L200 | HSCA-092; CORE-Sumika §3 |
| Shiun Sumika | E020 | first-person gyaru origin: after ballet, as rebellion against her mother; learned from friends and magazines; became natural | her own account | `adv_event_020_main-03` L186–L211 | GKM-SAA-078; E013–020 §9.4; CORE-Sumika §3, §12 |
| Hanami Ume | C1 @ U1 | initiates production by Sena after Hiro declines China's unit; passes the Selection test; loves idolhood and Begrazia; keeps Sena on stage; names a self-authored dream after her first win over Saki | U1 is a parallel track | `adv_unit_01-03_05` L419–L602; `adv_unit_01-04_14` L406–L700; `adv_unit_01-04_21` L527–L562 | GKM-SAA-113; CORE-Ume §22.8 |
| Hataya Misuzu | C1 @ D-MISUZU Dear 032–036 | extends the `Temari reconfiguration` row: in Misuzu's route Temari recalls feeling Misuzu taken by Rinha and Kei (D032); Temari declines to rank Misuzu above Kei and Rinha (D034), an open asymmetry added to fear_or_constraint; Misuzu cries before Temari and tells her the idol origin in bare `手毬` (D036) | difference-compatible attachment preserved; D-TEMARI 018/022 are cross-track corroboration only; P1 severity applied with the specialist's borderline-P2 view recorded as dissent | `adv_dear_hmsz_032` L286, L317–L327; `adv_dear_hmsz_034` L594–L612; `adv_dear_hmsz_036` L1047–L1276 | GKM-SAA-004 (P1); CORE-Misuzu §3, §7.2, §14.1, §25; RS-I §5.9.2 |
| Hataya Misuzu | support 2-0055 (SL1.1, C4) | recognises a rest method unlike her own (Saki's `完全休養日`) and arranges a shared nap; the methods are not merged | support continuity only | `adv_csprt-2-0055_01` L93–L121; `adv_csprt-2-0055_02` L71–L151 | GKM-SAA-108; CORE-Misuzu §2.4 |
| Hataya Misuzu | M-MISUZU 020, 018 (C2/C4) | context-specific appearance doubt and an "only complex" about an unnamed closest idol, thinned by the Producer's conviction; in 018_02 laziness covers frustration | the referent stays open | `adv_cidol-hmsz-3-020_03` L161–L249; `adv_cidol-hmsz-3-018_02` L85–L204 | GKM-SAA-243; CORE-Misuzu §3.1 |
| Hataya Misuzu | E014 | twice names the motivated state `懐かしい`; Temari predicts the comeback from acquaintance | the referent stays open | `adv_event_014_main-03` L514; `adv_event_014_main-05` L116 | HSCA-118; E013–020 §3.5 |
| Hataya Misuzu | E024 | claims ENDLESS DANCE as `わたしだけのもの`. Ume defends the song, and Sena later reports broader participation (**REVISE**, 2026-11-25) | event-scoped | `adv_event_024_main-04` L368–L372; `adv_event_024_main-05` L275–L323, L359–L383 | HSCA-028; E021+ §5.4 |
| Juo Sena | cross-route defeat states (C1 in each owning route; mutually exclusive) | D-SAKI 024: producer success hollows the idol before the reform, then she reignites as a challenger; winter H.I.F. losses in other routes' Dear 036, including SL1.1 D-KOTONE and D-TSUBAME; P3-SENA final-failure crowns Kotone (C3) | not D-SENA biography; the scenes also characterize the winners | `adv_dear_hski_024` L336–L430; Dear 036 per route; `adv_pstory_003_jsna_final-failure-01` L6–L66 | GKM-SAA-026; CORE-Sena "Cross-route defeat counter-track", OPEN-SENA-12 |
| Juo Sena | supports 3-0113, 2-0057, 3-0110 (SL1.1, C4) | 3-0113: Kotone's acceptance of her production is considered but not reached; 2-0057: a supervision ethic, with Misuzu's correction; 3-0110: succession without direct guidance | support continuity only | `adv_csprt-3-0113_01`–`_03`; `adv_csprt-2-0057_01`–`_02`; `adv_csprt-3-0110_03` L156–L181 | GKM-SAA-108; CORE-Sena §19–§21 |
| Amaya Tsubame | ordinary life (C3 Produce material labelled) | spectator love of cuteness; academic first place as self-labelled escapism; a home commuter who refuses the dorm over dorm head Mao's orders (a Produce Event choice); archaic `父君` / `母君`; strict cooking training; a self-designed uniform worn with permission | pre-performance routines and other register items were not located and not landed | `adv_pstory_001_atbm_ending-normal-01` L117; `ending-normal-02` L41; `adv_pevent_001_atbm_activity_010` L33–L48 | GKM-SAA-258 (PARTIAL); CORE-Tsubame §17 |
| Hiwatari Kanae | Dear 001–002 (SL1.2) | annotates the Source Lock 1.2 row: Kanae takes the exam under a service rationale (to serve China more closely, with the masters' approval) without knowing that China originated the transfer | — | `adv_dear_hkne_001` L476–L488, L538–L557; `adv_dear_hkne_002` L192 | GKM-SAA-152; KANAE "Admission" |

### Core integration pointers (owner decision 1 as amended)

Each core now carries a section headed `Phase-4/5 integration pointers — 2026-11-15 (source-to-analysis audit)` and integrates event and support evidence into its body as dated additions. The Phase-4 and Phase-5 rows above are unchanged in substance; the pointer tables index where each item now sits in the core.

| Character | Core | Pointer section placed before | Audit IDs |
| --- | --- | --- | --- |
| Hanami Saki | `GKM_CORE_01_HANAMI_SAKI.md` | §22 | GKM-SAA-104, GKM-SAA-108 |
| Tsukimura Temari | `GKM_CORE_02_TSUKIMURA_TEMARI.md` | §22 | GKM-SAA-104, GKM-SAA-108 |
| Fujita Kotone | `GKM_CORE_03_FUJITA_KOTONE.md` | §20 | GKM-SAA-104, GKM-SAA-108 |
| Arimura Mao | `GKM_CORE_04_ARIMURA_MAO.md` | §19 | GKM-SAA-104 |
| Katsuragi Lilja | `GKM_CORE_05_KATSURAGI_LILJA.md` | §22 | GKM-SAA-104, GKM-SAA-108 |
| Kuramoto China | `GKM_CORE_06_KURAMOTO_CHINA.md` | §26 | GKM-SAA-104, GKM-SAA-108 |
| Shinosawa Hiro | `GKM_CORE_07_SHINOSAWA_HIRO.md` | §27 | GKM-SAA-104, GKM-SAA-108, GKM-SAA-219 |
| Himesaki Rinami | `GKM_CORE_08_HIMESAKI_RINAMI.md` | §29 | GKM-SAA-104, GKM-SAA-108 |
| Shiun Sumika | `GKM_CORE_09_SHIUN_SUMIKA.md` | §24 | GKM-SAA-104, GKM-SAA-108 |
| Hanami Ume | `GKM_CORE_10_HANAMI_UME.md` | §26 | GKM-SAA-104, GKM-SAA-108, GKM-SAA-113 |
| Hataya Misuzu | `GKM_CORE_11_HATAYA_MISUZU.md` | §32 | GKM-SAA-104, GKM-SAA-108 |
| Juo Sena | `GKM_CORE_12_JUO_SENA.md` | §40 | GKM-SAA-104, GKM-SAA-108 |
| Amaya Tsubame | `GKM_CORE_13_AMAYA_TSUBAME.md` | §44 | GKM-SAA-104 |

Integration status where the core states it (delta sweep after verification): the Sumika and Ume cores now integrate every CSL Phase-4 and Phase-5 row for their character into the body, and nothing remains indexed only; Events 021–030 carry no Sumika delta, matching the Sumika PRESERVE rows above. The Rinami core integrates its Phase-5 rows except items whose A1 lines were not re-read (China treating Rinami as an idol ideal, the Kotone hardship-aid scene, the Ume/Saki relay, the Hiro and Valentine stories, the laundry story with Mao); those stay ledger-only. The CSL rows themselves are unchanged.

## Carbon character and claim write-through — 2026-11-25

| Person and state | Transition | Evidence and current usable boundary |
| --- | --- | --- |
| Kotone · audience, professional assessment and thanks | REVISE | Dear 036 has earnest gratitude before the late money turn; *Yellow Big Bang!* commu part 3 gives a countercase of no deflection at the end. In the Re;IRIS commu the estimates are the Producer's. The hallway musical play occurs over accompaniment. [Recorded and textual limits](../05_AUDIOVISUAL_ANALYSIS/03_FUJITA_KOTONE/GKM_KOTONE_CARBON_AV_UPDATE_20261125.md) |
| Mao · frightened speech and future-oriented appeal | REVISE / OPEN | Dear 022 written register follows shock. The new recording clock binds the written screen lines; delivered seriousness remains open at this exact cue. *Face Me* shows a professional forward ask alongside romantic-coded language. [Voice and staging limits](../05_AUDIOVISUAL_ANALYSIS/04_ARIMURA_MAO/GKM_MAO_CARBON_AV_UPDATE_20261125.md) |
| Sumika, Lilja and Temari · E001 class voice | REVISE | Sumika performs Lilja under a question-mark nameplate; Temari's visible response is 16 dashes and her later reformulation is phrased more harshly. Lilja is a separate speaker in E030 peer advice and on her Dear 027 partnership address. [Sumika evidence](../05_AUDIOVISUAL_ANALYSIS/09_SHIUN_SUMIKA/GKM_SUMIKA_CARBON_AV_UPDATE_20261125.md) |
| China · selection failure | REVISE | While China is masked, the three messages identify a narration role and match Kanae-coded sound. The narrator's fictional identity remains OPEN. Other personal accountability claims retain China's own authored results. [Scene evidence](../05_AUDIOVISUAL_ANALYSIS/06_KURAMOTO_CHINA/GKM_CHINA_CARBON_AV_UPDATE_20261125.md) |

## Source-scoped support behavior and performance — 2026-11-25

Like their earlier written support readings, these observations apply to the named social settings. Saki responds practically to a sprain and then takes Temari’s account of responsibility into a renewed challenge. Kotone explicitly limits what money she will accept while retaining polite address and comic deflection. Rinami changes a particular acted offer after direction. Tsubame receives a student response appreciating her participation and gives a hesitant thanks. Ume escalates a joke and later recognizes its excess. The source limits on internal motive, long-term change and unshown actions remain with the [individual dispositions](../05_AUDIOVISUAL_ANALYSIS/GKM_PHASE7_FIVE_SUPPORT_PERCEPTUAL_ADJUDICATION_20261125.md).

## Event 014 and 015 played state comparisons — 2026-11-25

**STRENGTHEN.** These are event-track tests of Hiro’s choice despite discomfort, Misuzu’s purposeful effort, Ume’s tailored bluntness, China’s changes of audience, and Rinami’s private reappraisal. Their tempo, vocal shade, printed referents and sampled physical poses have distinct evidence. Do not synchronize with route states outside these events. [Sports day and Hiroshima adjudication](../05_AUDIOVISUAL_ANALYSIS/GKM_PHASE7_SPORTS_DAY_AND_HIROSHIMA_PERCEPTUAL_ADJUDICATION_20261125.md)

## 2026-11-25 bounded Event 022 and 024 character-state dispositions

**STRENGTHEN** Mao's separate giving and receiving of care, and Kotone's ability to name a friendship across seniority. **STRENGTHEN** Ume's active choice to keep Sena in the Shibuya performance, Misuzu's paired coordination alongside an exclusive ambition, and Sena's reported shift from planned withdrawal to continuing participation. Treat the subsequent reception as reported. **PRESERVE** the named characters' independent viewpoints and the separation between the two guarded events and other route states. Sena's spoken explanation in Event 024 part 05 attributes a distinct participation effect to Ume's enjoyment and a different possibility to Misuzu's performance. This evidence has Sena as a named witness (L319–323, L359).

[Guarded Event 022 and 024 adjudication](../05_AUDIOVISUAL_ANALYSIS/GKM_PHASE7_MAO_KOTONE_AND_SHIBUYA_PERCEPTUAL_ADJUDICATION_20261125.md)

## Guarded Event 023 — 2026-11-25

**STRENGTHEN.** Temari asks for practical help while disputing a label of closeness. Hiro supports her choice and reports later to Misuzu. Misuzu's performed response supports a personally significant gift. Earlier knowledge, exact motivation and private group agreement remain open. [Guarded Event 023 adjudication](../05_AUDIOVISUAL_ANALYSIS/GKM_PHASE7_EVENT_023_PRIVATE_PERFORMANCE_PERCEPTUAL_ADJUDICATION_20261125.md)

## Guarded care, chosen company and a summer photograph — 2026-11-25

**REVISE.** Mao’s perceived last chance helps explain why she continues training. When Kotone offers help, Mao says she can manage and worries about causing trouble. She later judges herself against her role as a third-year. Kotone leads care, and Mao asks for the light to stay on. Mao attends Sena’s live with company and then states how she wants to face her and herself. Clinical cause, later action and permanence remain open. [Guarded care and summer adjudication](../05_AUDIOVISUAL_ANALYSIS/GKM_PHASE7_MAO_CARE_AND_LAST_SUMMER_PERCEPTUAL_ADJUDICATION_20261125.md)

## Guarded comparisons of the Hanami sisters — 2026-11-25

**STRENGTHEN.** Ume says an idol should answer her own expectations and addresses herself by her full name. The scenario has no inward flag. Who else heard the turn remains open. Ume’s support part 01 recollection distinguishes following Saki from dreaming specifically of idolhood. Ume affirms her trust and says she wants to find her own answer. The onset of that aspiration remains undated. The after-show cover plan is a proposed aim. [Guarded Event 026 and support comparison](../05_AUDIOVISUAL_ANALYSIS/GKM_PHASE7_HANAMI_SISTERS_EVENT_026_AND_SUPPORT_PERCEPTUAL_ADJUDICATION_20261125.md)

## Guarded refinement of China’s council state — 2026-11-26

China accepts responsibility for the paperwork lapse and explains Ume’s assistance. She later asks the seniors for a chance for all three juniors to answer their concerns. The two guarded scenes distinguish her earlier apology from the later request. China promises to become a dependable president by spring and then asks Ume and Misuzu for continued help. The proposal to widen their group and invite Hiro is prospective. [Guarded Event 025 adjudication](../05_AUDIOVISUAL_ANALYSIS/GKM_PHASE7_EVENT_025_COUNCIL_SUCCESSION_PERCEPTUAL_ADJUDICATION_20261125.md) The state continues to be incoming presidency with responsibility shown at a modular scale.

## Ume’s proposals, relationship labels and terms of approach

Ume’s renewed initiative in Event 006, challenge in support 2-0047 and revised approach in support 2-0000 each have local recorded corroboration. They supply contrasts across separate circumstances and leave later consequences open. [Guarded Ume adjudication](../05_AUDIOVISUAL_ANALYSIS/GKM_PHASE7_UME_INITIATIVE_RELATIONSHIP_AND_BOUNDARIES_PERCEPTUAL_ADJUDICATION_20261126.md).

## Five guarded SyngUp support scenes

Temari’s request to Hiro, Misuzu’s own decision about lunch, Sena’s two distinct invitations and the separate dream and waking states display different permissions and consequences. Source boundaries keep a present action, a represented action, and a future proposal distinct. [Guarded SyngUp adjudication](../05_AUDIOVISUAL_ANALYSIS/GKM_PHASE7_SYNGUP_FIVE_SUPPORT_PERCEPTUAL_ADJUDICATION_20261126.md).
