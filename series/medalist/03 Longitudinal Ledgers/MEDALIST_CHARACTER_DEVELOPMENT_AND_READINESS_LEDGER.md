---
title: "Medalist — Character Development and Reconstruction Readiness"
artifact_id: "MEDALIST_CHARACTER_DEVELOPMENT_AND_READINESS_LEDGER"
artifact_type: "character_state_readiness_ledger"
series: "Medalist / メダリスト"
series_id: "medalist"
generation: "MEDALIST_BOOTSTRAP_V1"
version: "1.3"
status: "canonical"
scope: "Time-indexed character interpretation, identity resolution and evidence-specific promotion readiness"
canonical_home: "series/medalist/03 Longitudinal Ledgers/MEDALIST_CHARACTER_DEVELOPMENT_AND_READINESS_LEDGER.md"
source_boundary: "Japanese V01–V04 closed (Scores 1–15, Short Programs 1–4, own-volume material); fanbooks and later sources unadmitted"
created: "2026-10-11"
updated: "2026-10-13"
review_status: "AUTHOR_REVIEWED_V04_UPDATE"
foundation_owner_approval: "I approve the revised foundation. Begin analysis/deep reading of Volume 1."
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
do_not_use_as_literary_evidence: false
recommended_reasoning_class: "SUBSTANTIVE_ANALYSIS"
---

# Character development and readiness

This ledger owns character-level developmental state and the readiness derived from that evidence. It does not own pair states, competition results or canonical observations. At bootstrap all tables have **zero rows**; no cast identity, psychological trait or readiness grade has been invented.

## Why development and readiness share this home

Readiness depends on the same character's state coverage, ordinary behavior, contradictions and gaps. Keeping the assessment alongside the transition history prevents an independent readiness list from losing its basis. They remain distinct record types and decisions; the [reconstruction specification](../00%20Frameworks%20and%20Methods/MEDALIST_CHARACTER_RECONSTRUCTION_SPEC.md) controls promotion.

## Schema and identifiers

The character register assigns `MD-CHAR-####` on first admitted evidence, preserving source-spelled name, short aliases with language/basis, continuity, first observation and unresolved identity. Global entity/subject IDs remain null unless actually curated. Never infer an unseen cast from publisher summaries.

An append-only state event `MD-CS-####` names character, represented time/range and certainty, revealed-after unit, state/change kind, self-report, observed action, inference/alternatives, evidence IDs, claim/version, confidence/basis, previous-state link and superseded/correction link. Change kinds: `DISPOSITION_CHANGE / KNOWLEDGE_CHANGE / RELATIONSHIP_CHANGE / CONTEXT_CHANGE / REVEALED_NOT_NEW / UNRESOLVED`. Proposed psychological mechanisms are claims; an attributed self-report is not a trait.

The current view names character, valid source/story boundary, active state-event references, scoped formulation and unresolved contradictions. It is a mutable projection of retained history, not the source of earlier freezes. Track capability/self-efficacy, goals/aspirations/fears, coping, decision-making and skating's significance only when consequential evidence exists.

Readiness `MD-RD-####` names character + artifact/domain + source endpoint, context diversity, supporting/counterevidence IDs, language/form coverage, missing domains, proposed scope, test status, assessment/reviewer/date and prerequisite claims. Use `UNASSESSED / INSUFFICIENT_EVIDENCE / BOUNDED_PROVISIONAL / DOMAIN_READY` locally; these are not artifact authority or global capability grades.

## Row triggers, evidence and revision

Add a state event when a new decision, persistent discrepancy, change or disclosure materially alters a character interpretation. A single mood may remain local in its reading; do not manufacture a stable disposition. Add readiness when an actual promotion is assessed or new evidence changes a prior assessment. Multiple observations of one scene are not independent contexts.

Every event requires a frozen reading's `MD-EV-…` locator, qualitative confidence and counterreading where interpretive. Link directional `MD-RL-…` relationship rows, `MD-SK-…` competence records and `MD-KN-…` knowledge records rather than duplicating their authoritative content. Japanese speech evidence is retained in original observation rows and linked here when it changes characterization/readiness.

Historical event identity, first source boundary and original formulation are immutable. Current formulation/readiness may advance through targeted edits with a new event or `MD-RV-…` revision; retain earlier readiness decisions and failed tests. Corrections append a reason and replacement, never erase a prior source-time state.

## V01 evidence tables

The [V01 reading and frozen state](../02%20Sequential%20Readings/MEDALIST_V01_DEEP_READING.md) own all `MD-EV-V01-…` observations. Every new record below is version 1, known after V01 at the specified component frontier; every claim reference is `@1`. Continuity is the admitted Japanese collected witness. Alias romanizations are retrieval aids from readable furigana/profile, not another translation witness. Global entity/subject IDs are null for every row: the current curated registry contained no Medalist match, and local allocation does not perform enrollment.

| Character key | Source-spelled identity / alias basis | Continuity | First observation | Global IDs / unresolved identity |
| --- | --- | --- | --- | --- |
| MD-CHAR-0001 | 明浦路司; Tsukasa Akeuraji, full name/furigana/Roman profile at 0211; earlier 司 | Japanese manga | MD-EV-V01-0002; full-name disclosure 0033 | null/null; no complete competition record |
| MD-CHAR-0002 | 加護耕一; Kago Kōichi, surname early, full name/furigana at 0218 | Japanese manga | MD-EV-V01-0002; full name 0036 | null/null |
| MD-CHAR-0003 | 羊; You, furigana よう; Kago's daughter | Japanese manga | MD-EV-V01-0002; 0009 image | null/null; no medical diagnosis |
| MD-CHAR-0004 | 結束いのり; Inori Yuitsuka, introduction 0067/profile 0072 | Japanese manga | First visible 0012; encounter MD-EV-V01-0003; full name 0009/0033 | null/null |
| MD-CHAR-0005 | 瀬古間; Sekoma, rink clerk | Japanese manga | MD-EV-V01-0003 | null/null; given name unverified |
| MD-CHAR-0006 | 高峰瞳; Hitomi Takamine, introduction in coach conversation | Japanese manga | MD-EV-V01-0005 | null/null |
| MD-CHAR-0007 | 結束さん / Inori's mother; family name and role, no given name supplied here | Japanese manga | Phone voice MD-EV-V01-0004; visit 0006 | null/null; do not import later name |
| MD-CHAR-0008 | Inori's elder sister, unnamed in admitted report | Japanese manga, reported subject | MD-EV-V01-0006 | null/null; narrated by mother, no independent interior |
| MD-CHAR-0009 | Yuri / ゆりちゃん, supportive school peer | Japanese manga | MD-EV-V01-0004 | null/null; surname unverified |
| MD-CHAR-0010 | 狼嵜光; Hikaru Kamisaki, furigana/name caption 0117 | Japanese manga | Girl at 0088, MD-EV-V01-0012; identity 0016 | null/null; unnamed adult's relation unverified |
| MD-CHAR-0011 | 理凰; Rio, furigana りおう at insult scene | Japanese manga | MD-EV-V01-0012 | null/null; family/full identity unverified |
| MD-CHAR-0012 | 那智鞠緒; Nachi Mario, introduction/furigana 0165 | Japanese manga | MD-EV-V01-0022 | null/null; earlier junior reputation attributed only |
| MD-CHAR-0013 | 三家田涼佳; Ryoka Miketa, introduction/furigana 0165; ミケ/Miku nickname | Japanese manga | MD-EV-V01-0022 | null/null; dialect aside 0034 |
| MD-CHAR-0014 | Ryoka's mother / ミケママ, unnamed | Japanese manga | Report 0022; depicted MD-EV-V01-0028 | null/null |
| MD-CHAR-0015 | 卯山雪; Yuki Uyama, furigana うやま/ゆき at 0152 | Japanese manga | MD-EV-V01-0020 | null/null; middle-school second year/grade four are page labels |
| MD-CHAR-0016 | 犬飼総太; Sōta Inukai, furigana at 0152 | Japanese manga | MD-EV-V01-0020 | null/null; primary fourth year/grade three are page labels |
| MD-CHAR-0017 | 芽衣子; Meiko, Kago's recollection of prior support | Japanese manga, remembered subject | MD-EV-V01-0037 | null/null; surname, absence/death circumstances and date unverified |
| MD-CHAR-0018 | 結束ヒロノブ; Inori's father, labeled in four-panel bonus | Japanese manga bonus fiction | MD-EV-V01-0038 | null/null; do not infer incapacity from child's height comparison |
| MD-CHAR-0019 | 原田先生; Harada, teacher aged 32 in jacket gag | Japanese manga jacket fiction | MD-EV-V01-0042 | null/null; given name unverified |
| MD-CHAR-0020 | Unnamed smoking adult outside badge venue | Japanese manga | MD-EV-V01-0011 | null/null; visually similar later glimpse is not verified identity |

| State event | Character | Story time / revealed after | Change kind | Action / self-report / inference | Evidence / claim version | Confidence / alternatives | Prior / correction |
| --- | --- | --- | --- | --- | --- | --- | --- |
| MD-CS-0001 | 0001 | Late-start history to failed audition; Score 1 | REVEALED_NOT_NEW | Self-account treats recognized athlete/show failure as reason not to teach; actual history includes sustained skating/work. | EV-0002/0005; MD-CL-0010@1 | HIGH report, MODERATE self-concept inference; fear of misleading also plausible. | none |
| MD-CS-0002 | 0004 | Before trial; Score 1 | REVEALED_NOT_NEW | Hidden practice and plan to earn permission; school difficulty feeds self-description of being unable. | EV-0004; MD-CL-0002@1 | MODERATE mechanism; ability differs by context, no diagnosis. | none |
| MD-CS-0003 | 0007 | Trial conclusion; Score 1 | CONTEXT_CHANGE | Conditional assent follows demonstration, child plea and coach promise; protection rationale remains. | EV-0006/0008/0009; MD-CL-0001@1 | HIGH assent; pressure and real concern coexist. | none |
| MD-CS-0004 | 0001 | Trial to first lessons; Score 1 | CONTEXT_CHANGE | Accepts coaching and makes public All-Japan commitment; role permits his skill to assist another. | EV-0007/0008/0009; MD-CL-0004@1 | HIGH role/action; no general pedagogy certification. | MD-CS-0001 |
| MD-CS-0005 | 0004 | Trial conclusion; Score 1 | KNOWLEDGE_CHANGE | Expresses desire openly after adult listens; gains practicable permission and instruction. | EV-0007/0008/0009; MD-CL-0002@1 | HIGH disclosure/options; not universal confidence change. | MD-CS-0002 |
| MD-CS-0006 | 0004 | Third lesson and badge day; Score 2 | CONTEXT_CHANGE | Chooses early test, needs situational support, completes patterns and passes. | EV-0010/0013/0014; MD-CL-0005@1 | HIGH bounded outcome; pressure may return elsewhere. | MD-CS-0005; MD-SK-0002 |
| MD-CS-0007 | 0007 | Return train; Score 2 | REVEALED_NOT_NEW | States middle-school endpoint; previous assent was not unrestricted. | EV-0014/0019; MD-CL-0007@1 | HIGH spoken limit; future firmness unknown. | MD-CS-0003; MD-KN-0006 |
| MD-CS-0008 | 0004 | After Hikaru meeting; Score 2 | KNOWLEDGE_CHANGE | Learns effort/help behind elite ability and explicitly requests world-best/gold assistance. | EV-0016/0017/0018; MD-CL-0002@1 | HIGH goal, MODERATE causal account; not complete cost knowledge. | MD-CS-0006 |
| MD-CS-0009 | 0001 | Test to dance demonstration; Scores 2–3 | REVEALED_NOT_NEW | Responsive attention tasks and bodily demonstration reveal competence beyond failed-show self-account. | EV-0013/0020/0021; MD-CL-0004@1 | MODERATE pedagogical pattern; interventions not isolated experimentally. | MD-CS-0004 |
| MD-CS-0010 | 0004 | Training choice; Score 3 | KNOWLEDGE_CHANGE | Declines mind-reading answer and chooses foundations/dancing for beauty and winning. | EV-0025; MD-CL-0002@1/0007@1 | HIGH stated reasons; admiration still shapes preference. | MD-CS-0008; MD-RL-0005 |
| MD-CS-0011 | 0004 | First rehearsal to final rental/spin; Score 3 | CONTEXT_CHANGE | Initial post-jump freeze gives way to continued choreography after fallen double and a flying sit execution. | EV-0020/0026/0031; MD-CL-0005@1 | HIGH task-specific progress; contest/repeatability unknown. | MD-CS-0010; MD-SK-0004/0006 |
| MD-CS-0012 | 0013 | Cafe to challenge; Score 3 | RELATIONSHIP_CHANGE | Invites friend then conditions friendship on rejecting adults; performs advanced jump yet depends on adult resources. | EV-0022/0023/0028; MD-CL-0006@1 | HIGH behavior, MODERATE mechanism; first-friend wish/enthusiasm counter pure domination. | none; MD-RL-0011/0012 |
| MD-CS-0013 | 0012 | Ten-day vicinity to early rental; Score 3 | REVEALED_NOT_NEW | Withholds requested grade advance for winning/pupil retention; gratitude and investment also shown. | EV-0027/0028; MD-CL-0009@1 | HIGH decision/thought; no wholly cynical or wholly benevolent model. | none; MD-IN-0006 |
| MD-CS-0014 | 0001 | Four-day consultation to new plan; Score 3 | KNOWLEDGE_CHANGE | Recognizes insufficient double preparation, doubts estimate and finds spin solution; renews certainty despite uncertainty. | EV-0029/0031/0032; MD-CL-0007@1/0008@1 | HIGH revised plan, MODERATE motive; victory not yet tested. | MD-CS-0009; MD-SK-0005/0007 |
| MD-CS-0015 | 0005 | Inori aged seven onward; Short Program 1 | REVEALED_NOT_NEW | Adult privately pays entry, teaches and fears job consequences; affection coexists with frightening rule enforcement. | EV-0035; MD-CL-0011@1 | HIGH represented subsidy; not new present-time policy. | none; MD-RT-0001 |
| MD-CS-0016 | 0001 | After coaching decision, exact later placement unclear; Short Program 2 | CONTEXT_CHANGE | Denies coaching as compensation; accepts return to Kago household despite prior eligibility/boundary worry. | EV-0036/0037; MD-CL-0010@1/0011@1 | HIGH denial/return, motive UNRESOLVED; care and projection can coexist. | MD-CS-0001/0004; MD-RT-0002/0003 |
| MD-CS-0017 | 0002 | Earlier help and sushi scene; Short Program 2 | REVEALED_NOT_NEW | Says support was always sincere/effort-based and invites return; unasked intervention can intrude. | EV-0036/0037/0038; MD-CL-0011@1 | HIGH speech/actions, MODERATE motivation; Meiko's inner state only remembered. | none; MD-RL-0017/0018 |

Here `EV-####` abbreviates the exact `MD-EV-V01-####` identifier in the linked reading; character numerals abbreviate `MD-CHAR-####`. These aliases are display conventions, not independently allocated records.

| Character | Current source boundary | Active state references | Bounded current formulation | Open contradictions |
| --- | --- | --- | --- | --- |
| MD-CHAR-0004 | V01/MD-FR-V01 | MD-CS-0005/0006/0008/0010/0011 | Can communicate ambition, choose a strategy and perform practiced tasks with help; explicit beauty and victory aims coexist. | No contest result/general confidence; conditional mother support; earlier school vulnerability survives. |
| MD-CHAR-0001 | V01/MD-FR-V01 | MD-CS-0004/0009/0014/0016 | Responsive novice coach with expressive skill, revised estimate and actual support network; denies regret compensation. | Absolute promises versus uncertain prognosis; sincere denial does not settle projection. |
| MD-CHAR-0007 | V01/MD-FR-V01 | MD-CS-0003/0007 | Effective support within middle-school limit, shaped by reported prior family hurt. | Long-term boundary and child cost knowledge unknown. |
| MD-CHAR-0013 | V01/MD-FR-V01 | MD-CS-0012 | Ambitious, skilled beginner-section entrant; conditional friendship and independence rhetoric. | Relies on coach/mother; response to divergent aims untested. |
| MD-CHAR-0012 | V01/MD-FR-V01 | MD-CS-0013 | Competitive investment includes controlling grade progression; meaningful care/effort also visible. | Welfare/agency effects not resolved by winning. |
| MD-CHAR-0005 | V01/MD-FR-V01 | MD-CS-0015 | Earlier hidden subsidy enabled Inori; affection and fear-based enforcement coexist. | Official permission and duration unknown. |
| MD-CHAR-0002 | V01/MD-FR-V01 | MD-CS-0017 | Material and affectionate support extends beyond athletic usefulness. | Intrusive help/recipient boundary conflict; full Meiko context unknown. |

| Readiness record | Character / target / domain | Boundary / scope | Context coverage / counterevidence | Gaps / tests | Assessment / reviewer / date | History / revision |
| --- | --- | --- | --- | --- | --- | --- |
| MD-RD-0001 | 0004 / monograph / V01 development | V01 manga-only argument | Home/school, test, peers and training; EV-0004/0008/0014/0018/0025/0026; continued vulnerability counters total confidence. | No competition/later states; fanbooks unresolved and explicitly excluded; speech/form covered in reading. | BOUNDED_PROVISIONAL; author; 2026-10-12; prerequisites CL-0002@1/0005@1 | First assessment; no package promoted. |
| MD-RD-0002 | 0004 / operational model / pressure-response | V01 | Test support, program freeze and rehearsal recovery are contrasting tasks, not held-out tests. | Independent validation, knowledge-conditioned rules and contest opportunity absent. | INSUFFICIENT_EVIDENCE; author; 2026-10-12; CL-0005@1 | No MD-RULE or simulation. |
| MD-RD-0003 | 0001 / monograph / V01 coach identity | V01 manga and own-volume bonus | Athlete failure, teaching, deadlines and patron boundaries; EV-0002/0005/0021/0029/0037; denial/care counters simple projection. | Later response to failure/refusal and full career absent; supplemental exclusion explicit. | BOUNDED_PROVISIONAL; author; 2026-10-12; CL-0004@1/0010@1 | First assessment; no full-series identity claim. |
| MD-RD-0004 | 0001 / operational model / coaching decisions | V01 | Responsive interventions and overconfident forecasts both included; EV-0013/0025/0029/0032. | No independent efficacy/holdout test; uncertainty not converted into universal rule. | INSUFFICIENT_EVIDENCE; author; 2026-10-12; CL-0007@1 | No validated coaching model. |
| MD-RD-0005 | 0010 / monograph or model / peer recognition | V01 | Unrecognized friendship, status intervention, joint skating and practice self-report; EV-0012/0015/0016/0017. | Limited focal interior, home/coach context and later conflict unknown. | INSUFFICIENT_EVIDENCE for broad reconstruction; author; 2026-10-12; CL-0003@1 | Supports bounded relational argument only. |
| MD-RD-0006 | 0013 and 0012 / separate reconstruction / rivalry-coaching | V01 | Invite/threat, grade control, skill and maternal effort; EV-0022/0023/0027/0028. | Each subject needs distinct later contexts/contrary reactions; no personality diagnosis. | INSUFFICIENT_EVIDENCE for either model; author; 2026-10-12; CL-0006@1/0009@1 | Dyadic evidence does not establish individual readiness. |
| MD-RD-0007 | 0007 / monograph / conditional support role | V01 | Refusal, assent, equipment and train limit; EV-0006/0008/0009/0014. | Mostly child/coach focalization; her independent ordinary behavior and later boundary response absent. | BOUNDED_PROVISIONAL for V01 supporting-role account; author; 2026-10-12; CL-0001@1/0007@1 | Full monograph/model UNASSESSED; no promotion. |

## V02 evidence tables

The [V02 reading and frozen state](../02%20Sequential%20Readings/MEDALIST_V02_DEEP_READING.md) own all `MD-EV-V02-…` observations. In this section `EV-####` expands to `MD-EV-V02-####`; a V01 observation is written `V01:EV-####`. Every new record is version 1, first known after V02. Claim references are the versions in force at `MD-FR-V02`. The V01 tables above are unchanged and remain the `MD-FR-V01` state; the current projection is the last projection table in this document. Global entity and subject IDs remain null for every row.

### Identity updates to existing keys

Keys are retained; a disclosed name or a probable link is recorded here and does not reassign an ID.

| Character key | V02 disclosure | Basis | Remaining limit |
| --- | --- | --- | --- |
| MD-CHAR-0008 | Named 結束実叶 (ゆいつか みか), Mika Yuitsuka; studying in Canada; calls Inori のんちゃん; eight years older by the gag-strip ages | EV-0002, EV-0050 | Her own competitive record is not given. |
| MD-CHAR-0011 | Rio's family name is 鴗鳥 by his father's caption; enters Novice boys | EV-0023 | Reading of 理凰 as りおう is from V01. |
| MD-CHAR-0017 | 芽衣子 glossed as Yō's late mother | EV-0050 | Date and cause of death not given. |
| MD-CHAR-0018 | Inori's father stayed home on competition day | EV-0025 | Wanted to attend; had work earlier that day. |
| MD-CHAR-0020 | Probable identity with MD-CHAR-0021: the V01 figure outside the badge venue matches Yodaka's drawing closely (long dark coat, dark striped shirt, hair over one eye, cigarette) | V01:EV-0011 compared with EV-0022/0026/0047 | No text links them. Key kept separate until a source does. |

### New keys

| Character key | Source-spelled identity / alias basis | Continuity | First observation | Global IDs / unresolved identity |
| --- | --- | --- | --- | --- |
| MD-CHAR-0021 | 夜鷹純; Yodaka Jun; named on a broadcast caption, self-identified in the stairwell, 夜鷹様 with furigana in Short Program 4 | Japanese manga | Named EV-0022; in person EV-0026 | null/null; Olympic gold medalist, retired at twenty; present age not given |
| MD-CHAR-0022 | 鴗鳥慎一郎; Sonidori Shin'ichirō, caption with furigana | Japanese manga | EV-0023 (as "鴗鳥" EV-0022) | null/null; head coach of 名港ウィンドFSC, Rio's father |
| MD-CHAR-0023 | 鹿本すず; Kamoto Suzu, caption with furigana; fifth grade | Japanese manga | EV-0037 | null/null |
| MD-CHAR-0024 | 大和絵馬; Yamato Ema, caption with furigana; fourth grade | Japanese manga | EV-0037 | null/null |
| MD-CHAR-0025 | 蛇崩遊大; Jakuzure Yūdai, caption with furigana; twenty-eight; ジャッキー先生 to Suzu | Japanese manga | EV-0037 | null/null |
| MD-CHAR-0026 | 桜井ひめ; Sakurai Hime, announced only | Japanese manga | EV-0003, placing EV-0020 | null/null; no speech or depiction beyond the podium |
| MD-CHAR-0027 | Tsukasa's former teacher, unnamed, seen only from behind | Japanese manga, remembered subject | EV-0042 | null/null; identity, gender and period unverified |

Other announced entrants (柊木咲, 平野優香, 桐谷ジュリア, 坂城みなこ, 神谷ひな, 柴崎はるか) and Ryoka's father appear only in announcements or gags and stay local to the reading.

### State events

| State event | Character | Story time / revealed after | Change kind | Action / self-report / inference | Evidence / claim version | Confidence / alternatives | Prior / correction |
| --- | --- | --- | --- | --- | --- | --- | --- |
| MD-CS-0018 | 0004 | Between warm-up and skate; Score 4 | CONTEXT_CHANGE | After a failed warm-up and overhearing her mother's request, blames herself, then reverses the thought ("変えてないだけだ") and tells her mother she wants to compete as an athlete. | EV-0004/0005/0006; MD-CL-0002@2/0015@1 | HIGH sequence; whether the reframing lasts is untested. | MD-CS-0011 |
| MD-CS-0019 | 0004 | Free skate; Score 4 | CONTEXT_CHANGE | Falls on the first jump, resumes smiling, completes the rest and adds an unplanned broken-leg variation; wins with 12.64. | EV-0008/0009/0011/0014; MD-CL-0005@2/0002@2 | HIGH bounded outcome; one competition, a win. | MD-CS-0018; MD-PERF-0011 |
| MD-CS-0020 | 0007 | During and after the skate; Score 4 | RELATIONSHIP_CHANGE | Says her "can't" was fear of being hurt and belief in others' evaluations; asks which medal; commits to supporting the Olympic aim. | EV-0001/0005/0010/0014; MD-CL-0014@1 | HIGH utterance, MODERATE motive (her account, one scene); endpoint of V01 not mentioned. | MD-CS-0007; MD-RT-0004 |
| MD-CS-0021 | 0001 | Before her skate; Score 4 | CONTEXT_CHANGE | Withdraws the victory guarantee: falling is allowed, he will re-teach indefinitely, "どんな貴方でも". | EV-0007/0013; MD-CL-0007@2 | HIGH speech; MODERATE that it marks a lasting boundary, since absolutes return later. | MD-CS-0014 |
| MD-CS-0022 | 0013 | Free skate and corridor; Score 5 | REVEALED_NOT_NEW | Panics after a broken combination and repeats it into an invalid element; says she wanted to manage alone because she could not get adults on her side; regrets losing Inori; accepts her back. | EV-0018/0019/0020/0021; MD-CL-0006@2 | HIGH self-report, MODERATE as explanation of the V01 stance. | MD-CS-0012; MD-RT-0005 |
| MD-CS-0023 | 0012 | After the loss; Score 5 | REVEALED_NOT_NEW | Does not punish; affirms Ryoka's temperament; states that the strong are right; her club has one pupil and marginal costs. | EV-0016/0019/0021; MD-CL-0009@2/0018@1 | HIGH conduct and speech; evaluation MODERATE. | MD-CS-0013 |
| MD-CS-0024 | 0001 | Stairwell; Score 6 | REVEALED_NOT_NEW | Began skating after seeing Yodaka on television; confronts him for the pupil; pledges his own lifetime for as long as she needs him; later resolves to be the world's best coach. | EV-0022/0027/0028/0029/0032; MD-CL-0010@2 | HIGH statements; mechanism OPEN. | MD-CS-0016/0021; MD-RT-0006 |
| MD-CS-0025 | 0004 | After Hikaru's skate and that night; Score 6 / Short Program 3 | KNOWLEDGE_CHANGE | Measures the distance to Hikaru, questions her friend's meaning, sends thanks and a refusal to stop; says she fears joy will dissolve the cold dissatisfaction that drives her; asks for the next competition. | EV-0025/0027/0030; MD-CL-0003@2/0015@1 | HIGH self-report; pattern claim MODERATE. | MD-CS-0019 |
| MD-CS-0026 | 0004 | Training to six days before the meet; Score 7 | CONTEXT_CHANGE | Repeated double falls, refusal to stop, comparison with girls her age; accepts that failing time has value; self-chosen worm routine; reads the video herself; lands one double loop. | EV-0034/0035/0036/0044; MD-CL-0015@1/0005@2 | HIGH events; one landing, repeatability unknown. | MD-CS-0025; MD-SK-0011 |
| MD-CS-0027 | 0001 | Training and the Kyoto visit; Score 7 | KNOWLEDGE_CHANGE | Recognizes his own haste; asks a rival club's coach for method; is told his eye is exceptional; resolves that confidence is not given by others. | EV-0035/0039/0041/0042/0044; MD-CL-0004@2/0017@1 | HIGH appraisal and resolution; whether it holds unprompted is untested. | MD-CS-0024 |
| MD-CS-0028 | 0021 | Stairwell, and five years earlier; Score 6 / Short Program 4 | UNRESOLVED | Tells a beginner she will never beat Hikaru; defines himself as Hikaru's coach; five years earlier judged a child by reported circumstances and "luck", reversed on seeing her, and expected her to follow his own road. | EV-0026/0027/0028/0047/0048; MD-CL-0016@1 | HIGH words; motive UNRESOLVED; two scenes only. | none |
| MD-CS-0029 | 0010 | Novice B; bonus disclosure | REVEALED_NOT_NEW | Wins with 97.23; grade 6; coached and choreographed by Yodaka though her sheet names Sonidori; an orphan adopted into a wealthy household. | EV-0024/0025/0027/0047; MD-CL-0003@2 | HIGH disclosed facts; no interior access in V02. | none; MD-RT-0007 |
| MD-CS-0030 | 0008 | Competition day and earlier; Score 4, gags | REVEALED_NOT_NEW | Came home to watch; corrects Inori's reading of their mother; openly proud; as a child carried and played roughly with her sister. | EV-0001/0002/0009/0050; MD-CL-0011@2 | HIGH conduct; her own skating history only glimpsed. | none |
| MD-CS-0031 | 0025 | Badge-test visit; Score 7 | REVEALED_NOT_NEW | Shares his view freely, names Tsukasa's ability, wants Ema acknowledged, intends to win without straining. | EV-0039/0041/0043; MD-CL-0017@1 | HIGH speech; two scenes, one interlocutor. | none |

### Current projection after V02

| Character | Current source boundary | Active state references | Bounded current formulation | Open contradictions |
| --- | --- | --- | --- | --- |
| MD-CHAR-0004 | V02/MD-FR-V02 | MD-CS-0019/0025/0026 | Beginner champion and grade-1 skater who acts beyond plan and protection, names her own driving dissatisfaction and has one double. | Not shown losing; self-blame recurs; haste. |
| MD-CHAR-0001 | V02/MD-FR-V02 | MD-CS-0021/0024/0027 | Coach whose guarantee gave way to permission at the critical moment, whose eye is attested from outside, and whose ambition is now bound to his pupil's. | Absolutes persist at long range; fused interests untested; self-trust newly asserted. |
| MD-CHAR-0007 | V02/MD-FR-V02 | MD-CS-0020 | Committed supporter by her own revised account. | Endpoint unwithdrawn in words; costs not yet faced. |
| MD-CHAR-0013 | V02/MD-FR-V02 | MD-CS-0022 | Skilled, proud, shaken by a rules defeat; has explained and dropped her condition on friendship. | Grade unchanged; response to Nachi's creed unknown. |
| MD-CHAR-0012 | V02/MD-FR-V02 | MD-CS-0023 | Affirming after defeat; ties being right to winning; one pupil. | Whether the creed becomes pressure. |
| MD-CHAR-0021 | V02/MD-FR-V02 | MD-CS-0028 | Champion turned concealed coach who forecasts from status and reverses on sight. | Motive and "the same road" unresolved. |
| MD-CHAR-0010 | V02/MD-FR-V02 | MD-CS-0029 | Dominant novice with a hidden coach and an adoptive household. | No V02 interior; her view of Inori unknown. |
| MD-CHAR-0025 | V02/MD-FR-V02 | MD-CS-0031 | Generous and competitive peer coach. | Thin evidence. |
| MD-CHAR-0005 / 0002 | V01/MD-FR-V01 | MD-CS-0015 / 0017 | Unchanged from V01 except that Tsukasa pays Kago rent. | As at V01. |

### Readiness after V02

| Readiness record | Character / target / domain | Boundary / scope | Context coverage / counterevidence | Gaps / tests | Assessment / reviewer / date | History / revision |
| --- | --- | --- | --- | --- | --- | --- |
| MD-RD-0008 | 0004 / monograph / development through first competition | V01–V02 manga-only | Home, school memory, tests, peers, training, competition, a hostile adult; EV-0006/0011/0025/0030/0034; reframing and self-chosen coping counter a fixed self-blame account. | No losing result; little non-evaluative ordinary life; fanbooks unresolved and excluded. | BOUNDED_PROVISIONAL; author; 2026-10-13; MD-CL-0002@2/0005@2/0015@1 | Extends MD-RD-0001; no package promoted. |
| MD-RD-0009 | 0004 / operational model / pressure and setback response | V01–V02 | One competition with recovery; repeated practice failure with persistence. | No unwelcome result; no held-out test. | INSUFFICIENT_EVIDENCE; author; 2026-10-13 | Extends MD-RD-0002; no MD-RULE. |
| MD-RD-0010 | 0001 / monograph / coach identity and ambition | V01–V02 manga and own-volume bonus | Athlete history, teaching, a crisis, a confrontation, peer appraisal; EV-0007/0029/0041/0044; conditional pledge and prior defence counter simple projection. | No divergence of his and her interests; former teacher unidentified. | BOUNDED_PROVISIONAL; author; 2026-10-13; MD-CL-0004@2/0007@2/0010@2/0017@1 | Extends MD-RD-0003. |
| MD-RD-0011 | 0001 / operational model / coaching decisions | V01–V02 | Permission versus guarantee by context; help-seeking. | Boundary seen once; no test under a loss. | INSUFFICIENT_EVIDENCE; author; 2026-10-13 | Extends MD-RD-0004. |
| MD-RD-0012 | 0013 with 0012 / dyadic study / coach and pupil through a defeat | V01–V02 | Preparation, competition, aftermath, profiles; EV-0016–0021. | Individual models still unsupported; one defeat. | BOUNDED_PROVISIONAL for a dyadic study; INSUFFICIENT_EVIDENCE for either individual model; author; 2026-10-13; MD-CL-0006@2/0009@2/0018@1 | Revises the scope of MD-RD-0006. |
| MD-RD-0013 | 0007 / monograph / supporting role | V01–V02 | Refusal, limit, request, self-account, commitment; EV-0005/0010/0014. | Ordinary independent behaviour; the endpoint's formal status. | BOUNDED_PROVISIONAL for a supporting-role account; author; 2026-10-13; MD-CL-0014@1 | Extends MD-RD-0007. |

MD-CHAR-0021, 0010 as an independent subject, 0022–0027 and 0008 are UNASSESSED or INSUFFICIENT_EVIDENCE for any dedicated artifact at this boundary; no row is added for them.

## V03 evidence tables

The [V03 reading and frozen state](../02%20Sequential%20Readings/MEDALIST_V03_DEEP_READING.md) own all `MD-EV-V03-…` observations. In this section `EV-####` expands to `MD-EV-V03-####`; earlier volumes are written `V01:EV-####` or `V02:EV-####`. Every new record is version 1, first known after V03. Claim references are the versions in force at `MD-FR-V03`. Earlier tables are unchanged; the current projection is the last projection table in this document. Global entity and subject IDs remain null for every row.

### Identity updates to existing keys

| Character key | V03 disclosure | Basis | Remaining limit |
| --- | --- | --- | --- |
| MD-CHAR-0003 | Yō is sickly, often misses school, sometimes feigns illness; now in sixth grade, the same school year as Inori | EV-0057 | No condition named. |
| MD-CHAR-0010 | Hikaru lives in the Sonidori household and has since about seven; second All-Japan Novice B title with a triple Axel; badge grade 7; a Kansai verb form in a gag | EV-0044/0054/0057 | Still no interior access. |
| MD-CHAR-0011 | Full name 鴗鳥理凰; fifth grade at the Kyoto meet's date and a year older by Score 11; badge grade 5; American mother | EV-0002/0050/0057 | — |
| MD-CHAR-0022 | Sonidori is an Olympic silver medalist; Hikaru's listed coach while Yodaka's role is non-public | EV-0002/0049/0050 | His own view of the arrangement unstated. |
| MD-CHAR-0027 | The former teacher is shared by Tsukasa and Hitomi (恩師) and is on good terms with Okayama's head coach | EV-0058 | Still unnamed and unseen. |
| MD-CHAR-0013 | Ryoka is ten and at grade 5 a year on | EV-0047 | Consistent with Nachi's "nine" in V02; the V02 profile's "eight" likely predates a birthday. |

### New keys

| Character key | Source-spelled identity / alias basis | Continuity | First observation | Global IDs / unresolved identity |
| --- | --- | --- | --- | --- |
| MD-CHAR-0028 | 獅子堂星羅; Shishidō Seira, caption; fifth grade; スター広島FSC, moving to 岡山ティナFSC | Japanese manga | EV-0003 | null/null; daughter of a national-team speed skater by spectators' report |
| MD-CHAR-0029 | 黒澤美豹; Kurosawa Miho, caption with furigana みいひ in a pencil gag; fifth grade; same clubs as Seira | Japanese manga | EV-0003 | null/null |
| MD-CHAR-0030 | 小熊梨月; Oguma Ritsuki, caption; fourth grade; 岡山ティナFSC | Japanese manga | EV-0003 | null/null; an elder brother appears unnamed |
| MD-CHAR-0031 | 鬼寅カンナ; Kitora Kanna, announced; second grade per a judge; 福岡パークFSC | Japanese manga | EV-0016/0017 | null/null |
| MD-CHAR-0032 | 亀金谷澄覚; Kameganya Chōkaku, caption with furigana; head coach of 蓮華茶FSC | Japanese manga | EV-0003 | null/null |
| MD-CHAR-0033 | Trainer employed by 福岡パークFSC, unnamed; a woman with glasses and a long braid | Japanese manga | EV-0012; role EV-0017 | null/null |

Coaches named only in the profile page (布袋野蕨一, 布袋野兎太, 梟木豊, 目城理世, 伊太刀小五郎), Rio's mother, Suzu's sisters and other announced entrants stay local to the reading.

### State events

| State event | Character | Story time / revealed after | Change kind | Action / self-report / inference | Evidence / claim version | Confidence / alternatives | Prior / correction |
| --- | --- | --- | --- | --- | --- | --- | --- |
| MD-CS-0032 | 0004 | Meet morning; Score 8 | CONTEXT_CHANGE | Loses her skates on a train; blames herself ("私また…", "こんな私で"); Yodaka's sentence intrudes; she postpones self-reproach so as to be able to skate. | EV-0006/0009; MD-CL-0015@2 | HIGH. | MD-CS-0026 |
| MD-CS-0033 | 0004 | Alone outside; Score 8 | DISPOSITION_CHANGE (candidate) | Decides not to wait for encouragement; describes a place for failure always prepared for her; chooses to be the self her coach believed in. | EV-0011/0012; MD-CL-0002@3/0015@2 | HIGH wording; whether this is a lasting change is the open point. | MD-CS-0032 |
| MD-CS-0034 | 0007 | Meet morning; Score 8 | CONTEXT_CHANGE | Self-reproach checked; forbids herself to sigh; supports; moderates the warm-up in the coach's absence. | EV-0006/0008; MD-CL-0014@2 | HIGH conduct. | MD-CS-0020 |
| MD-CS-0035 | 0001 | Meet morning; Score 8 | CONTEXT_CHANGE | Runs for the skates, leaving his pupil coachless; criticizes his own decision; is rebuked. | EV-0007/0013/0015/0042; MD-CL-0004@3/0007@3/0017@2 | HIGH events; the author's aside confirms a better option existed. | MD-CS-0027 |
| MD-CS-0036 | 0001 | At the boards; Score 9 | CONTEXT_CHANGE | Declines her proposed escalation and explains in scoring terms. | EV-0022; MD-CL-0007@3 | HIGH. | MD-CS-0035 |
| MD-CS-0037 | 0004 | Free skate; Score 9 | KNOWLEDGE_CHANGE | Finds the weight-over-blade feel her coach had described; keeps it at a cost; derives a rule of slow movement from his V01 dance; reframes missing strength as room to grow. | EV-0023/0024/0025/0027; MD-CL-0002@3/0008@3 | HIGH. | MD-CS-0033; MD-SK-0015 |
| MD-CS-0038 | 0004 | First-aid room; Score 10 | REVEALED_NOT_NEW | Had trained two days on shin pain she took for muscle soreness; protests rest because she is behind. | EV-0032; MD-CL-0015@2 | HIGH speech. | MD-CS-0037; MD-KN-0027 |
| MD-CS-0039 | 0001 | First-aid room to five days later; Score 10 | CONTEXT_CHANGE | Orders rest against her wish; apologizes to her for what the coaching side lacked; decides with her on a winter without competitions; states the aim is not to catch up fastest. | EV-0032/0040/0043; MD-CL-0007@3/0010@3 | HIGH. | MD-CS-0036 |
| MD-CS-0040 | 0004 | Train home; Score 10 | DISPOSITION_CHANGE (candidate) | Accepts that the time lost cannot be recovered, refuses it as a reason to give up, renounces haste and sadness about it. | EV-0037/0040; MD-CL-0019@1 | HIGH wording; durability tested only by an unshown year and bent in Score 11. | MD-CS-0038 |
| MD-CS-0041 | 0024 | Years before to the meet; Score 10 | REVEALED_NOT_NEW | Years at beginner grade, growth pain, overtraining, food refusal, two failed tests; resolved never to hate skating; wins with content no rival has; thinks it only natural. | EV-0033/0034/0035/0036/0037/0042; MD-CL-0020@1 | HIGH events; mechanism is her coach's account. | none |
| MD-CS-0042 | 0025 | A year before to five days after; Score 10 | REVEALED_NOT_NEW | Objected to referring Ema elsewhere; promised to make her a skater at any height; set rest as her task; credits her alone. | EV-0033/0034/0035/0042; MD-CL-0020@1/0017@2 | HIGH. | MD-CS-0031 |
| MD-CS-0043 | 0004 | A year later; Scores 10–11 | CONTEXT_CHANGE | Twelve, grade 5, 名港杯 champion at that grade; working on the double Axel; judged by her coach to be strong against "can't". | EV-0045/0047; MD-CL-0019@1/0004@3 | HIGH outcome; the year itself unshown. | MD-CS-0040 |
| MD-CS-0044 | 0011 | Night and at Lux; Score 11 | REVEALED_NOT_NEW | Confronts Yodaka; wants distance from him; calls himself talentless and finished; has failed the grade-6 test repeatedly; panics at specific praise; advises Inori to change coach; wishes he could speak as she does. | EV-0046/0049/0050/0052/0053/0054/0055; MD-CL-0021@1/0001@3 | HIGH speech and facts; inner account LOW-MODERATE (one chapter). | none |
| MD-CS-0045 | 0004 | Locker room; Score 11 | UNRESOLVED | In anger vows a double Axel, this year's All-Japan Novice A, a win over Hikaru, and a triple and double before Rio to prove her coach. | EV-0054/0055/0056; MD-CL-0019@1/0010@3 | HIGH wording; relation to MD-CS-0040 unresolved. | MD-CS-0043 |
| MD-CS-0046 | 0021 | Night; Score 11 and memory | UNRESOLVED | Leaves his purpose unstated; reacts to "ran away"; tells Rio he is the obstacle; still jumps, by demonstration, for Hikaru. | EV-0002/0046/0053; MD-CL-0016@2 | HIGH events; motive UNRESOLVED. | MD-CS-0028 |

### Current projection after V03

| Character | Current source boundary | Active state references | Bounded current formulation | Open contradictions |
| --- | --- | --- | --- | --- |
| MD-CHAR-0004 | V03/MD-FR-V03 | MD-CS-0040/0043/0045 | Grade-5 champion who has lost once, accepted an unrecoverable gap, and can supply her own belief; self-blame still arrives first. | The train vow against the Score 11 vow; the year unshown. |
| MD-CHAR-0001 | V03/MD-FR-V03 | MD-CS-0035/0036/0039 | Instructor with a year's result, a record of one costly impulse and several corrections, and a stated preference for building over catching up. | Still learns his own soundness from others; now the object of his pupil's vow. |
| MD-CHAR-0007 | V03/MD-FR-V03 | MD-CS-0034 | Supportive under a mishap, checking her own reflex. | Endpoint unmentioned; unaware of the unpaid entries. |
| MD-CHAR-0024 | V03/MD-FR-V03 | MD-CS-0041 | Slow, self-built winner who treats her work as ordinary. | Whether growth pain persists. |
| MD-CHAR-0025 | V03/MD-FR-V03 | MD-CS-0042 | Patient, credit-refusing coach inside a selective club. | His standing with his head coach. |
| MD-CHAR-0011 | V03/MD-FR-V03 | MD-CS-0044 | Credentialed and skilled, convinced he is finished. | Technical versus motivational cause; what his family knows. |
| MD-CHAR-0021 | V03/MD-FR-V03 | MD-CS-0046 | Hidden coach who teaches by demonstration and wounds a second child. | Purpose; the meaning of "ran away". |
| MD-CHAR-0010 | V03/MD-FR-V03 | MD-CS-0029 plus identity update | Twice national novice champion with a triple Axel, living in her listed coach's house. | No interior. |
| MD-CHAR-0013 / 0012 | V02 state with V03 update | MD-CS-0022 / 0023 | Ryoka at grade 5; otherwise unchanged. | Who decided the advance. |

### Readiness after V03

| Readiness record | Character / target / domain | Boundary / scope | Context coverage / counterevidence | Gaps / tests | Assessment / reviewer / date | History / revision |
| --- | --- | --- | --- | --- | --- | --- |
| MD-RD-0014 | 0004 / monograph / development through a defeat and a year | V01–V03 manga-only | Win, loss, injury, solitude, a peer's challenge; EV-0012/0027/0040/0056; persistent self-blame and the Score 11 vow counter a clean growth story. | The training year unshown; non-evaluative life thin; fanbooks excluded. | BOUNDED_PROVISIONAL; author; 2026-10-13; MD-CL-0002@3/0015@2/0019@1 | Extends MD-RD-0008. |
| MD-RD-0015 | 0004 / operational model / response to setback | V01–V03 | Failed warm-up, fall, loss, injury, provocation: five distinct setbacks with distinguishable responses. | No held-out test; one loss. | BOUNDED_PROVISIONAL for this domain only; author; 2026-10-13 | Revises MD-RD-0009 from INSUFFICIENT_EVIDENCE; no MD-RULE written. |
| MD-RD-0016 | 0001 / monograph / coach identity, error and correction | V01–V03 | Run, refusal, rest, apology, year plan, endorsements; EV-0013/0022/0032/0040/0043. | Self-trust without confirmation; a decision under the new vow. | BOUNDED_PROVISIONAL; author; 2026-10-13; MD-CL-0004@3/0007@3/0010@3/0017@2 | Extends MD-RD-0010. |
| MD-RD-0017 | 0001 / operational model / decisions when pupil's wish and welfare diverge | V01–V03 | One clear divergence resolved toward welfare; one escalation refused; one impulsive error. | Small number of cases; no test under direct pressure from the Yodaka rivalry. | BOUNDED_PROVISIONAL for this domain only; author; 2026-10-13 | Revises MD-RD-0011; no MD-RULE written. |
| MD-RD-0018 | 0024 with 0025 / dyadic study / a slow developer and her coach | V02–V03 | Flashbacks, competition, the coach's retrospective account; EV-0033–0037/0042. | Ema's interior is brief; the head coach's view is one scene. | BOUNDED_PROVISIONAL for a dyadic study; author; 2026-10-13; MD-CL-0020@1 | First assessment. |
| MD-RD-0019 | 0007 / monograph / supporting role | V01–V03 | Adds conduct under a mishap. | Ordinary independent behaviour; the endpoint. | BOUNDED_PROVISIONAL for a supporting-role account; author; 2026-10-13; MD-CL-0014@2 | Extends MD-RD-0013. |

MD-CHAR-0011, 0021, 0010, 0022 and 0028–0033 are UNASSESSED or INSUFFICIENT_EVIDENCE for a dedicated artifact at this boundary. MD-RD-0012 (Ryoka with Nachi) is unchanged.

## V04 evidence tables

The [V04 reading and frozen state](../02%20Sequential%20Readings/MEDALIST_V04_DEEP_READING.md) own all `MD-EV-V04-…` observations. In this section `EV-####` expands to `MD-EV-V04-####`; earlier volumes are written with their volume prefix. Every new record is version 1, first known after V04. Claim references are the versions in force at `MD-FR-V04`. Earlier tables are unchanged; the current projection is the last projection table in this document. Global entity and subject IDs remain null for every row.

### Identity updates to existing keys

| Character key | V04 disclosure | Basis | Remaining limit |
| --- | --- | --- | --- |
| MD-CHAR-0001 | Singles badge grade: beginner, taken self-taught without a club; has a younger brother; works a clerical job overnight | EV-0011/0014/0047 | The teacher he "wishes he had met sooner" is still unnamed. |
| MD-CHAR-0011 | Eleven, sixth grade; eighth at All-Japan Novice two years ago; a four-year-old sister; mother Brazilian-American, called エイヴァ by Hikaru; badge grade 6 at the end of V04 | EV-0019/0045/0046/0047 | — |
| MD-CHAR-0018 | Inori's father drives her to the rink at night and envies her ease with her coach | EV-0004/0017 | Comic register. |
| MD-CHAR-0021 | Novice record as recited by Tsukasa: triple Lutz and triple loop and a triple Axel in Novice B, seeded every year at the selection camp, four titles; called 純くん by Sonidori | EV-0023 | A character's statement, not a document. |
| MD-CHAR-0022 | Thirty-six; retired at twenty-eight with an Olympic silver medal; father of two | EV-0046 | Profile fields. |
| MD-CHAR-0013 | Fourth grade a year on; does her own hair | EV-0002/0017 | — |

### New keys

| Character key | Source-spelled identity / alias basis | Continuity | First observation | Global IDs / unresolved identity |
| --- | --- | --- | --- | --- |
| MD-CHAR-0034 | 白根琥珀; Shirone Kohaku, caption with furigana; twenty-one; instructor at a Nagoya ballet studio; シロ先生 | Japanese manga | EV-0030; named EV-0031 | null/null; the page assigns no gendered term and none is assumed |

Rio's mother and small sister, Tsukasa's younger brother and named badge-test candidates stay local to the reading.

### State events

| State event | Character | Story time / revealed after | Change kind | Action / self-report / inference | Evidence / claim version | Confidence / alternatives | Prior / correction |
| --- | --- | --- | --- | --- | --- | --- | --- |
| MD-CS-0047 | 0001 | Night park; Score 12 | CONTEXT_CHANGE | Tells his pupil the goal may be out of reach; rules out more volume on health grounds; revises his diagnosis on her evidence and retracts. | EV-0004/0006; MD-CL-0007@4/0004@4 | HIGH. | MD-CS-0039 |
| MD-CS-0048 | 0004 | Night park; Score 12 | CONTEXT_CHANGE | Bases her ambition on having changed (growth, fitness, "no longer a child with nothing"); lands a double Axel off the ice; does not tell him the quarrel. | EV-0005; MD-CL-0002@4/0019@2 | HIGH. | MD-CS-0045 |
| MD-CS-0049 | 0001 | Camp night 1; Score 12 | REVEALED_NOT_NEW | States his beginner grade without defence; remembers calling his self-taught years wasted; says he hesitated to coach for fear of this; vows alone to make both pupils jump the combination. | EV-0011/0014/0015; MD-CL-0010@4 | HIGH statements. | MD-CS-0047; MD-RT-0017/0018 |
| MD-CS-0050 | 0004 | Camp night 1; Score 12 | REVEALED_NOT_NEW | Confides to Ryoka, as a secret from her coach, that she fears he will be blamed for her failures and wants to be strong enough to choose him. | EV-0012; MD-CL-0002@4/0010@4/0019@2 | HIGH wording. | MD-CS-0048; MD-KN-0036 |
| MD-CS-0051 | 0004 | Camp days 2–3; Scores 12–15 | CONTEXT_CHANGE | Lands a double Axel, then a triple Salchow the same day; defers celebration by her coach's own rule; lands a triple and double last of three without distress. | EV-0016/0020/0035; MD-CL-0019@2 | HIGH; single landings. | MD-CS-0050; MD-SK-0021/0022 |
| MD-CS-0052 | 0011 | Camp night 2; Score 13 | REVEALED_NOT_NEW | "I have everything, so I can blame nothing"; learns his standard is Yodaka's novice career; recalls being refused a lesson; concludes he was bound by an illusion. | EV-0021/0022/0023/0024; MD-CL-0021@2/0022@1 | HIGH wording; one night's account. | MD-CS-0044 |
| MD-CS-0053 | 0001 | Camp night 2; Scores 13–14 | REVEALED_NOT_NEW | Skates Rio's program from one viewing; by Rio's judgment his skating is Yodaka's image; by Hitomi's account he had no record, an unmatched hold on the rink and a need to make the ice his place. | EV-0025/0026/0027; MD-CL-0004@4/0010@4/0017@3 | HIGH that these were said and shown; origin of the resemblance inferred. | MD-CS-0049 |
| MD-CS-0054 | 0011 | Camp day 3; Scores 14–15 | DISPOSITION_CHANGE (candidate) | Comes early, addresses the coach by family name, writes one goal, lands a triple and double, claims the coach as his. | EV-0029/0035/0036; MD-CL-0021@2/0001@4 | HIGH events; durability unknown. | MD-CS-0052 |
| MD-CS-0055 | 0013 | Camp day 3; Score 15 | KNOWLEDGE_CHANGE | Sees a four-year gap made by her own choice; resolves to win and make the choice right; lands a triple Salchow and a triple and double. | EV-0033/0035; MD-CL-0018@2/0022@1 | HIGH. | MD-CS-0022 |
| MD-CS-0056 | 0004 | Last evening of camp; Score 15 | DISPOSITION_CHANGE (candidate) | Says the cold feeling let her work, that its role ends at grade 6, and that she owes her hated self goodbye and thanks; describes the present as drawn by what lies beyond difficulty. | EV-0033/0037/0038; MD-CL-0015@3 | HIGH wording; one good season. | MD-CS-0051 |
| MD-CS-0057 | 0001 | Last evening of camp; Score 15 | KNOWLEDGE_CHANGE | Says the efforts of the self he hated have become his ally; denies that her earlier self was no good. | EV-0038; MD-CL-0010@4/0017@3/0022@1 | HIGH. | MD-CS-0053 |
| MD-CS-0058 | 0010 | Test day; Score 15 | REVEALED_NOT_NEW | Recognizes Inori at once, is glad, appears to have expected her progress, promises to meet at the All-Japan. | EV-0039; MD-CL-0003@3 | HIGH conduct; interior still thin. | MD-CS-0029 |
| MD-CS-0059 | 0004 | Test day; Score 15 | CONTEXT_CHANGE | Hands steady where they shook in V01; passes all three parts in one day; frightened while results are read. | EV-0040/0041/0043/0044/0045; MD-CL-0015@3/0005@3 | HIGH. | MD-CS-0056; MD-SK-0025 |
| MD-CS-0060 | 0011 | Test day; Score 15 | CONTEXT_CHANGE | Passes grade 6 at the sixth sitting using the coach's phrase; grins openly; tells Inori she was good. | EV-0041/0044/0045; MD-CL-0021@2 | HIGH. | MD-CS-0054 |
| MD-CS-0061 | 0022 | Past and test day | REVEALED_NOT_NEW | Told his small son to make do with him; spoke of a special promise; delegated his son to another coach; shows restrained pride; his own advice had gone unheard. | EV-0023/0040/0041/0046; MD-CL-0011@4/0016@3 | HIGH. | none |
| MD-CS-0062 | 0021 | Years earlier | REVEALED_NOT_NEW | Told the small Rio, who asked for the same lesson as Hikaru, that he was in the way. | EV-0023; MD-CL-0016@3 | HIGH wording; ground unstated. | MD-CS-0046 |

### Current projection after V04

| Character | Current source boundary | Active state references | Bounded current formulation | Open contradictions |
| --- | --- | --- | --- | --- |
| MD-CHAR-0004 | V04/MD-FR-V04 | MD-CS-0050/0056/0059 | Grade-6 skater entered in the qualifier, who names her old driver as a phase ending, and who has begun to keep one thing from her coach for his sake. | Untested under a setback inside her last eligible year. |
| MD-CHAR-0001 | V04/MD-FR-V04 | MD-CS-0047/0053/0057 | Coach with a beginner's badge and a skater's body of work, who tells the truth about limits, borrows expertise deliberately, and has begun to revalue his own past. | Acts for others, not for himself, by his partner's account; unaware of his pupil's motive. |
| MD-CHAR-0011 | V04/MD-FR-V04 | MD-CS-0054/0060 | Grade-6 skater with a first triple, loosened from a standard he had not known he held. | Whether the change survives his return home. |
| MD-CHAR-0013 | V04/MD-FR-V04 | MD-CS-0055 | Triple-jumping ten-year-old who means to justify her choices by winning. | The creed untested by a loss since V02. |
| MD-CHAR-0010 | V04/MD-FR-V04 | MD-CS-0058 | Warm toward Inori and expecting her as a competitor. | Interior. |
| MD-CHAR-0022 | V04/MD-FR-V04 | MD-CS-0061 | Humble medalist father who delegates what he cannot get heard. | The promise. |
| MD-CHAR-0021 | V04/MD-FR-V04 | MD-CS-0046/0062 | Unchanged in kind; an earlier refusal and a stated promise added. | Purpose. |
| MD-CHAR-0007, 0012, 0024, 0025 | V03 state | as before | Unchanged in V04. | — |

### Readiness after V04

| Readiness record | Character / target / domain | Boundary / scope | Context coverage / counterevidence | Gaps / tests | Assessment / reviewer / date | History / revision |
| --- | --- | --- | --- | --- | --- | --- |
| MD-RD-0020 | 0004 / monograph / development through grade 6 | V01–V04 manga-only | Adds an honest prognosis received, a withheld motive, a new discipline, a self-described change of motive; the secret and the fear at the results counter a completed-growth story. | A setback inside the deadline; the elided year; fanbooks excluded. | BOUNDED_PROVISIONAL; author; 2026-10-13; MD-CL-0002@4/0015@3/0019@2 | Extends MD-RD-0014. |
| MD-RD-0021 | 0004 / operational model / response to setback | V01–V04 | No new setback in V04; a lost informal contest taken lightly. | As MD-RD-0015. | BOUNDED_PROVISIONAL for this domain only; author; 2026-10-13 | Carries MD-RD-0015; no MD-RULE written. |
| MD-RD-0022 | 0001 / monograph / coach identity, past and method | V01–V04 | His own account of his past; Hitomi's and Rio's testimony; decisions in the park and at camp; EV-0004/0011/0014/0025/0027/0038. | The unnamed teacher; how his skating was formed; a decision when his pupil's hidden motive surfaces. | BOUNDED_PROVISIONAL; author; 2026-10-13; MD-CL-0004@4/0007@4/0010@4/0017@3 | Extends MD-RD-0016. |
| MD-RD-0023 | 0001 / operational model / decisions about pace and load | V01–V04 | Adds a veto of volume and a retraction on evidence. | No held-out case. | BOUNDED_PROVISIONAL for this domain only; author; 2026-10-13 | Carries MD-RD-0017; no MD-RULE written. |
| MD-RD-0024 | 0011 / supporting-character study / inherited expectation | V03–V04 | Hostility, self-account, sealed memory, change, a certified pass; EV-0022/0023/0029/0045. | One arc of a month; his family's view; his return home. | BOUNDED_PROVISIONAL for a supporting-character study; author; 2026-10-13; MD-CL-0021@2 | First assessment. |

MD-RD-0012, 0018 and 0019 are unchanged. MD-CHAR-0010, 0021, 0022 and 0034 remain UNASSESSED or INSUFFICIENT_EVIDENCE for a dedicated artifact.
