---
title: "Medalist — Character Development and Reconstruction Readiness"
artifact_id: "MEDALIST_CHARACTER_DEVELOPMENT_AND_READINESS_LEDGER"
artifact_type: "character_state_readiness_ledger"
series: "Medalist / メダリスト"
series_id: "medalist"
generation: "MEDALIST_BOOTSTRAP_V1"
version: "1.9"
status: "canonical"
scope: "Time-indexed character interpretation, identity resolution and evidence-specific promotion readiness"
canonical_home: "series/medalist/03 Longitudinal Ledgers/MEDALIST_CHARACTER_DEVELOPMENT_AND_READINESS_LEDGER.md"
source_boundary: "Japanese V01–V10 closed (Scores 1–40, Short Programs 1–5, one Exhibition, own-volume material); fanbooks and later sources unadmitted"
created: "2026-10-11"
updated: "2026-10-13"
review_status: "AUTHOR_REVIEWED_V10_UPDATE"
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

## V05 evidence tables

The [V05 reading and frozen state](../02%20Sequential%20Readings/MEDALIST_V05_DEEP_READING.md) own all `MD-EV-V05-…` observations. In this section `EV-####` expands to `MD-EV-V05-####`; earlier volumes are written with their volume prefix. Every new record is version 1, first known after V05. Claim references are the versions in force at `MD-FR-V05`. Earlier tables are unchanged; the current projection is the last projection table in this document. Global entity and subject IDs remain null for every row.

### Identity updates to existing keys

| Character key | V05 disclosure | Basis | Remaining limit |
| --- | --- | --- | --- |
| MD-CHAR-0002 | Meiko was his wife; he never saw Tsukasa skate in person; first visit to a rink | EV-0002/0011/0014 | — |
| MD-CHAR-0003 | Came because she wanted to know the sport Tsukasa loves; finds it unreadable without rules | EV-0017 | — |
| MD-CHAR-0005 | Given name 衛 on the editorial page; has attended every competition Inori has entered | EV-0002/0017 | The name's reading is as noted from that page at first inspection and was not re-verified. |
| MD-CHAR-0010 | Seeded at the Nagano camp; absent from the qualifier; in St Petersburg for ballet; this is her first year in Novice A; the cohort is called by her name | EV-0006/0007/0019/0034 | Her instructor there is unnamed. |
| MD-CHAR-0011 | His father had meant him to start at six; he began earlier under Yūna's influence | EV-0031 | — |
| MD-CHAR-0017 | Kago's wife; hospitalised; followed Tsukasa's ice dance on television and explained the rules to her husband; her wish was that his career be supported; died before seeing him skate in person | EV-0002/0015 | Her death is shown by an emptied room, not captioned; date and cause not given. |
| MD-CHAR-0018 | Attends a competition for the first time on the page | EV-0003 | Comic register. |
| MD-CHAR-0022 | Head coach of 名港ウィンドFSC; his medal was two Olympics ago; his first pupil after retiring was Yūna | EV-0002/0020/0031 | — |
| MD-CHAR-0023 | Named by the field as the only skater who could contend with Hikaru | EV-0005 | Hearsay among rivals. |

### New keys

| Character key | Source-spelled identity / alias basis | Continuity | First observation | Global IDs / unresolved identity |
| --- | --- | --- | --- | --- |
| MD-CHAR-0035 | 八木夕凪; Yagi Yūna, caption with furigana; sixth grade; 名港ウィンドFSC | Japanese manga | Unnamed EV-0005; named EV-0013/0028 | null/null; the pale-haired figure of the prologue and of EV-0005 is identified by drawing only |
| MD-CHAR-0036 | 鯱城理依奈; Kojō Riina, caption with furigana こじょう; nineteen; 間京大学; 名港ウィンドFSC; top-rank designated skater | Japanese manga | EV-0008 | null/null |
| MD-CHAR-0037 | 岡崎いるか; Okazaki Iruka, caption with furigana; sixteen; 愛西ライドFSC; designated skater rank A | Japanese manga | EV-0008 | null/null |
| MD-CHAR-0038 | 栗尾根茉莉花; Kuriobe Marika, caption with furigana; eighteen; 名城クラウンFSC; designated skater rank B | Japanese manga | EV-0008 | null/null |
| MD-CHAR-0039 | 雉多輝也; Kijita Shōya, caption with furigana; twenty-four; assistant coach, 名港ウィンドFSC; ショウ先生 | Japanese manga | EV-0016 | null/null |
| MD-CHAR-0040 | 五里誠二; Gori Seiji, caption with furigana; head coach, 愛西ライドFSC | Japanese manga | EV-0020 (at the boards); named EV-0024 | null/null |
| MD-CHAR-0041 | 炉場愛花; Roba Manaka, caption with furigana; sixth grade; 愛西ライドFSC | Japanese manga | EV-0013 | null/null |
| MD-CHAR-0042 | 申川りんな; Rinna; first year of middle school; 名港ウィンドFSC | Japanese manga | EV-0013 | null/null; family-name reading not given on the pages inspected |
| MD-CHAR-0043 | 牛川四葉; Ushikawa Yotsuha, caption with furigana; sixth grade; 名港ウィンドFSC | Japanese manga | EV-0008 (by given name); EV-0013 | null/null |
| MD-CHAR-0044 | 海月和香; Umitsuki Waka, caption with furigana うみつき; fifth grade; 熱海SC | Japanese manga | EV-0013 | null/null |
| MD-CHAR-0045 | 隈野実将史; Kumano Mimasashi, caption with furigana; figure-skating coach, 熱海SC | Japanese manga | EV-0026 | null/null |
| MD-CHAR-0046 | 足利刹那; Ashikaga Setsuna, caption with furigana; first year of middle school; 名城クラウンFSC; last year's Novice A winner at this event | Japanese manga | EV-0013; EV-0034 | null/null |

The remaining entrants (穴熊咲希奈, 庭取さな, 庭取ひな, 離洲くるみ, 古部多まいん, 都中伊のと, 蟹江ほなみ, 武田桃芽), the coaches 伯備新, 千羽輪太郎 and 山根亜美, and the unnamed ballet master in St Petersburg stay local to the reading and to the skating ledger's performance table.

### State events

| State event | Character | Story time / revealed after | Change kind | Action / self-report / inference | Evidence / claim version | Confidence / alternatives | Prior / correction |
| --- | --- | --- | --- | --- | --- | --- | --- |
| MD-CS-0063 | 0004 | Opening ceremony; Score 16 | CONTEXT_CHANGE | Alone for the first time at a ceremony, gets through by adopting her coach's manner; learns the other entrants are fourth-time competitors and says she had mistaken reaching Novice for being their equal. | EV-0004; MD-CL-0002@5/0015@4 | HIGH; comic register. | MD-CS-0059 |
| MD-CS-0064 | 0010 | Same period, St Petersburg; Score 16 | REVEALED_NOT_NEW | States that she wants to be the magician and not Cinderella, and to know the highest standard of ballet rather than be good for a child skater. | EV-0006; MD-CL-0003@4/0016@4 | HIGH wording; five panels. | MD-CS-0058 |
| MD-CS-0065 | 0004 | Ceremony; Score 16 | KNOWLEDGE_CHANGE | Learns Hikaru is seeded and absent; infers that "at the All-Japan" meant Hikaru expected her to qualify. | EV-0007; MD-CL-0003@4 | HIGH that she infers it. | MD-KN-0044 |
| MD-CS-0066 | 0004 | Ceremony; Score 16 | CONTEXT_CHANGE | Asks an Olympian how to reach the Olympics, is rebuked, apologizes at once; vows before cameras to become an All-Japan gold medalist "someday"; told to prove it today; thinks she is already on the road to the Olympics. | EV-0009/0010; MD-CL-0002@5/0015@4/0019@3 | HIGH. | MD-CS-0063 |
| MD-CS-0067 | 0036 | Ceremony; Score 16 | REVEALED_NOT_NEW | Says she cannot know what practice is right until she competes; won the All-Japan as a new senior four years ago and so went to the Olympics; declares she will do it again; challenges a novice to prove herself today. | EV-0010; MD-CL-0001@5 | HIGH. | none |
| MD-CS-0068 | 0001 | Night before and competition day; Scores 16–17 | REVEALED_NOT_NEW | Studies past score sheets with delight; says the coach's ability is tested from here; once apologized to his patron in mourning dress for giving nothing back. | EV-0003/0012; MD-CL-0010@5/0004@4 | HIGH; occasion of the apology inferred. | MD-CS-0057; MD-RT-0023 |
| MD-CS-0069 | 0002 | Competition day; Score 17 | REVEALED_NOT_NEW | Tells Tsukasa he never saw him skate live, that he and his wife had wanted to, and that Tsukasa's passion let him move forward; comes to watch his work; thanks Inori on meeting her. | EV-0014/0015; MD-CL-0010@5/0011@5 | HIGH. | MD-PROP-0020 |
| MD-CS-0070 | 0001 | Competition day; Score 17 | KNOWLEDGE_CHANGE | Weeps; says his work cannot be seen and that Inori's performance is all of it; asks Kago to watch over her skate as he watched over him. | EV-0015; MD-CL-0010@5/0007@5 | HIGH wording. | MD-CS-0068 |
| MD-CS-0071 | 0042 | Competition day; Score 17 | CONTEXT_CHANGE | Cries at drawing first; opens with a triple Lutz; falls later on a jump she does not miss in practice; leads at 70.04. | EV-0016/0018; MD-CL-0005@4/0023@1 | HIGH. | none |
| MD-CS-0072 | 0041 | Competition day; Score 18 | CONTEXT_CHANGE | Proposed moving her combinations to the bonus zone; falls; recalls her coach's praise of attempting; lands both; "one who cannot bet on herself cannot beat fate"; 72.62. | EV-0024/0025; MD-CL-0023@1/0024@1 | HIGH. | none |
| MD-CS-0073 | 0044 | Competition day; Score 18 | CONTEXT_CHANGE | Eliminated at 49.86; grieves in terms of what her coach's driving cost him; is told it was no burden and not a debt. | EV-0026; MD-CL-0011@5 | HIGH. | none |
| MD-CS-0074 | 0035 | Competition day; Scores 18–19 | REVEALED_NOT_NEW | Vows to bring the gold and prove her coach's club; says skating is not a sport the hardest worker wins; rehearses her coach's praise with hand puppets; her worry is popped jumps. | EV-0028/0029/0030; MD-CL-0001@5/0022@2 | HIGH. | none |
| MD-CS-0075 | 0035 | From age four; Score 19 | REVEALED_NOT_NEW | Began at four under the newly retired Sonidori; learned by sight; pledged with Riina to be the club's number one and two; displaced when Hikaru came; resolved not to envy and to out-jump her. | EV-0032/0033; MD-CL-0001@5/0023@1 | HIGH. | MD-TM-0041/0042 |
| MD-CS-0076 | 0035 | Free skate; Score 19 | CONTEXT_CHANGE | Rejects "the kindness of being believed in" for "the strength to make him turn round"; breaks the planned layout to land a triple Lutz and triple loop; falls; holds the program; resolves that one who does not know the pain of being overtaken shall not win; apologizes; 80.03. | EV-0036/0037/0038/0039; MD-CL-0001@5/0022@2/0024@1 | HIGH wording and outcome; her want is stated at one heated moment. | MD-CS-0074 |
| MD-CS-0077 | 0022 | Competition day; Scores 17–19 | REVEALED_NOT_NEW | Praises a flawed skate specifically; reads the draw tactically and expects the field to escalate; cannot model Inori; answers a broken plan with one sentence and a smile and plans around the jump; by a peer's account humble and abnormally tenacious. | EV-0018/0035/0039; MD-CL-0024@1/0005@4 | HIGH. | MD-CS-0061 |
| MD-CS-0078 | 0004 | Competition day; Score 19 | CONTEXT_CHANGE | Tells Rio and Yūna that she is skating to win gold, not only to make the five. | EV-0031; MD-CL-0002@5/0019@3 | HIGH. | MD-CS-0066 |
| MD-CS-0079 | 0004 | Before her skate; Score 19 | CONTEXT_CHANGE | Having seen 80.03, tells herself she understands the difference in talent and in time, "but"; finds the Novice A girls strong; holds her coach's drawstrings. | EV-0041; MD-CL-0015@4/0019@3 | HIGH wording; outcome unknown. | MD-CS-0078 |
| MD-CS-0080 | 0001 | Before her skate; Score 19 | CONTEXT_CHANGE | Says "today I will make you a gold medalist". | EV-0041; MD-CL-0007@5 | HIGH wording; a regression to promised results and a coach taking the wager on himself are both live readings. | MD-CS-0070 |
| MD-CS-0081 | 0046 | Competition day; Score 19 | CONTEXT_CHANGE | Last year's winner; falls before a back-loaded combination; seventh at 67.4; wanted a second title so as not to vanish in Hikaru's shadow. | EV-0034; MD-CL-0005@4/0023@1 | HIGH. | none |
| MD-CS-0082 | 0040 | Competition day; Score 18 | REVEALED_NOT_NEW | Accepted his pupil's risky layout on a safety condition; had told her that attempting is how she grew; frantic and then overjoyed. | EV-0024/0025; MD-CL-0024@1 | HIGH. | none |
| MD-CS-0083 | 0043 | Competition day; Scores 18–19 | CONTEXT_CHANGE | Three falls and elimination; resolves mid-program to guard what she built with her coach; tells Yūna fate arranged this day for her. | EV-0020/0021/0022/0026/0029; MD-CL-0023@1 | HIGH; some montage lines are assigned by image. | none |
| MD-CS-0084 | 0039 | Competition day; Score 17 | REVEALED_NOT_NEW | Brusque with a crying pupil; has a bouquet ready for each; says he takes her qualification for granted. | EV-0016/0018; MD-CL-0011@5/0024@1 | HIGH. | none |
| MD-CS-0085 | 0005 | Competition day; Scores 17–19 | REVEALED_NOT_NEW | Explains the sport to strangers as a wager without certain success; remembers Inori telling him she passed grade 6; watches with hands clasped. | EV-0017/0027/0040; MD-CL-0011@5 | HIGH. | V01 short-program state |

### Current projection after V05

| Character | Current source boundary | Active state references | Bounded current formulation | Open contradictions |
| --- | --- | --- | --- | --- |
| MD-CHAR-0004 | V05/MD-FR-V05 | MD-CS-0066/0078/0079 | Entrant drawn fourteenth and not yet skated, aiming aloud at gold, who admits the gaps in talent and time and still keeps one thing from her coach. | Whether the aim is appetite or the old deficit re-measured; untested. |
| MD-CHAR-0001 | V05/MD-FR-V05 | MD-CS-0068/0070/0080 | Coach who locates his whole work in his pupil's performance, released in words from an old debt, who has just declared a result. | Truth-telling about limits (V04) against an unqualified declaration (V05). |
| MD-CHAR-0035 | V05/MD-FR-V05 | MD-CS-0074/0075/0076 | Overtaken first pupil who broke a plan to match the prodigy's jump and leads the event. | What the lead gives her; her verdict on Inori rests on partial knowledge. |
| MD-CHAR-0022 | V05/MD-FR-V05 | MD-CS-0077 | Humble medalist, exact tactician, and a coach who absorbs defiance. | Whether he sees what Yūna says she lacks. |
| MD-CHAR-0010 | V05/MD-FR-V05 | MD-CS-0064 | Absent, seeded, training abroad; wants mastery on its own terms. | Her view of the field she shapes. |
| MD-CHAR-0002 | V05/MD-FR-V05 | MD-CS-0069 | Patron who considers himself repaid and has come to watch. | — |
| MD-CHAR-0041, 0042, 0046 | V05/MD-FR-V05 | MD-CS-0071/0072/0081 | Second, third and seventh with two skaters to come. | Final places. |
| MD-CHAR-0011 | V05/MD-FR-V05 | MD-CS-0060 | Cordial and informative a month on. | — |
| MD-CHAR-0013, 0012, 0024, 0025, 0034 | V04 or earlier | as before | Unchanged in V05. | — |

### Readiness after V05

| Readiness record | Character / target / domain | Boundary / scope | Context coverage / counterevidence | Gaps / tests | Assessment / reviewer / date | History / revision |
| --- | --- | --- | --- | --- | --- | --- |
| MD-RD-0025 | 0004 / monograph / development through the qualifier's eve | V01–V05 manga-only | Adds conduct among elite peers, a self-supplied coach, public commitments, a restated acceptance of the gap; the prologue's "tiny talent" and her admission at the boards counter a simple appetite story. | Her qualifier is unskated; the freeze falls mid-event, so V06 is the sound boundary. | BOUNDED_PROVISIONAL; author; 2026-10-13; MD-CL-0002@5/0015@4/0019@3 | Extends MD-RD-0020. |
| MD-RD-0026 | 0001 / monograph / coach identity, past and method | V01–V05 | Adds the origin of his debt to his patron, a statement of what a coach's work is, and a declared result; EV-0012/0015/0041. | What the declaration rested on; his conduct after the score; the unnamed teacher. | BOUNDED_PROVISIONAL; author; 2026-10-13; MD-CL-0007@5/0010@5 | Extends MD-RD-0022. |
| MD-RD-0027 | 0001 with 0002 / relationship study / patronage, debt and return | V01, V05 | Support, a refused loan, a remembered apology, a wife's wish, reciprocity stated; EV-0012/0014/0015 with V01 basis. | Kago's view between V01 and V05; whether Tsukasa accepts the release. | BOUNDED_PROVISIONAL; author; 2026-10-13; MD-CL-0010@5/0011@5 | First assessment. |
| MD-RD-0028 | 0035 / supporting-character study / the overtaken early starter | V05 | One chapter with history, ritual, a decisive act and a result; EV-0028–0039. | A single volume and an unfinished event; her coach's actual attention; her meeting with Inori's skating. | INSUFFICIENT_EVIDENCE for a dedicated artifact; adequate for ensemble treatment; author; 2026-10-13; MD-CL-0022@2/0001@5 | First assessment. |
| MD-RD-0029 | 0022 / supporting note / coaching manner and tactics | V03–V05 | Delegation of his son, praise, tactics, response to defiance, a peer's testimony; EV-0018/0035/0039 with V04 basis. | The promise with Yodaka; his awareness of the cost of Hikaru inside his club. | BOUNDED_PROVISIONAL for a supporting note; author; 2026-10-13; MD-CL-0024@1 | First assessment. |

MD-RD-0021, 0023 and 0024 are unchanged. MD-CHAR-0010, 0021 and 0036–0046 remain UNASSESSED or INSUFFICIENT_EVIDENCE for a dedicated artifact.

## V06 evidence tables

The [V06 reading and frozen state](../02%20Sequential%20Readings/MEDALIST_V06_DEEP_READING.md) own all `MD-EV-V06-…` observations. In this section `EV-####` expands to `MD-EV-V06-####`; earlier volumes are written with their volume prefix. Every new record is version 1, first known after V06. Claim references are the versions in force at `MD-FR-V06`. Earlier tables are unchanged; the current projection is the last projection table in this document. Global entity and subject IDs remain null for every row.

### Identity updates to existing keys

| Character key | V06 disclosure | Basis | Remaining limit |
| --- | --- | --- | --- |
| MD-CHAR-0001 | Longed for the ice from middle school; self-taught on rental skates by imitating Yodaka from video; began in earnest at twenty; competed in the two seasons at twenty-three and twenty-four | EV-0029/0035 | The ages are Sonidori's report of what Hitomi told him. |
| MD-CHAR-0007 | Addressed as のぞみ by another mother, her one friend among the skating parents; once took the small Inori to 名城クラウン wanting to be told it was impossible | EV-0008/0043 | The visit is an assistant coach's recollection. |
| MD-CHAR-0008 | Skated at 名城クラウン; appeared in the Nagoya Ice Festa with Kuriobe Marika; stopped after a fracture in jump practice; home from abroad | EV-0004/0008/0017/0047 | Her own account is not given. |
| MD-CHAR-0010 | Recorded at the block as withdrawn and advancing by recommendation; lands a triple Axel in practice | EV-0040/0045 | — |
| MD-CHAR-0011 | First of two entrants in the block's Novice A boys | EV-0043 | — |
| MD-CHAR-0012 | Once a member of 名城クラウン, by an assistant coach's profile | EV-0051 | Profile field. |
| MD-CHAR-0016 | Second of two in the block's Novice A boys; his mother is addressed as 恵さん | EV-0043 | The reading of 恵 was not relied on. |
| MD-CHAR-0021 | Retired at twenty, with a press conference; "unbeaten" by a magazine headline; back from abroad; still skates privately | EV-0030/0032/0035 | Reason for retiring not given. |
| MD-CHAR-0022 | His wife is named エイヴァ・F・ロドリゲス and was a skater | EV-0027 | See MD-CHAR-0051. |
| MD-CHAR-0035 | Twelve, born 26 June; fifth at this event last year; joined her club after seeing her coach's Olympic skate; the dark puppet is a kingfisher; by profile, secretly in love with her coach | EV-0022/0041 | The last is an editorial statement. |
| MD-CHAR-0037 | Competes at a Junior Grand Prix event in Italy the following week; coached by Gori; quarrels with her mother; knew Mika as a skater | EV-0044/0048 | — |
| MD-CHAR-0039 | Florists' son; the strongest of his cohort; still a guest in ice shows | EV-0051 | Profile fields. |
| MD-CHAR-0040 | Entered the All-Japan at twenty-two and retired; a middle-school teacher; revived his dissolved home club as 愛西ライド | EV-0051 | Profile fields. |
| MD-CHAR-0041 | Third, bronze; belonged to 長久手フラワー until third grade | EV-0021/0051 | — |
| MD-CHAR-0042 | Family name read さるかわ; fifth, advancing; has a cousin named Tsukasa | EV-0021/0051 | — |
| MD-CHAR-0043 | Thirteenth; had meant to quit when six clubmates left | EV-0022 | — |
| MD-CHAR-0046 | Ninth | EV-0021 | — |

### New keys

| Character key | Source-spelled identity / alias basis | Continuity | First observation | Global IDs / unresolved identity |
| --- | --- | --- | --- | --- |
| MD-CHAR-0047 | 竜宮アキラ; Ryūgū Akira, caption with furigana; head coach, 名城クラウンFSC | Japanese manga | EV-0008 | null/null |
| MD-CHAR-0048 | 千羽輪太郎; Senba Rintarō, caption with furigana; assistant coach, 名城クラウンFSC | Japanese manga | Named in V05 at the boards; consequential from EV-0008 | null/null |
| MD-CHAR-0049 | 王仁敦士; Wani Atsushi, caption with furigana; assistant coach, 愛西ライドFSC | Japanese manga | EV-0023 | null/null |
| MD-CHAR-0050 | 古部多まいん; Kobuta Main, caption with furigana; sixth grade; 名城クラウンFSC | Japanese manga | Listed in V05; EV-0020; speaks EV-0047 | null/null |
| MD-CHAR-0051 | エイヴァ・F・ロドリゲス; Ava F. Rodriguez; Rio's mother; a former skater by Tsukasa's form of reference | Japanese manga | EV-0027 | null/null; earlier volumes called her エイヴァ and gave her nationality in a profile |

Takeda Momoga, Tonakai Noto, Kanie Honami, the Niwatori twins, Umitsuki Waka's and Kumano's profile fields, the head coach 蟻代圭吾, Sōta's mother and the jump specialist seen only in silhouette stay local to the reading and to the skating and institutions ledgers.

### State events

| State event | Character | Story time / revealed after | Change kind | Action / self-report / inference | Evidence / claim version | Confidence / alternatives | Prior / correction |
| --- | --- | --- | --- | --- | --- | --- | --- |
| MD-CS-0086 | 0001 | Before her skate; Score 20 | REVEALED_NOT_NEW | Chooses his send-off words; says he is confident he can make her win, that he alone is not enough and that her resolve matters most; prays that the words' force will only push her forward; says he believes; "I leave it to you". | EV-0002/0003/0004; MD-CL-0007@6 | HIGH wording. | MD-CS-0080 |
| MD-CS-0087 | 0004 | Before her skate; Score 20 | CONTEXT_CHANGE | Asks whether he believes it too; on his answer says "leave it to me". | EV-0003; MD-CL-0002@6 | HIGH. | MD-CS-0079 |
| MD-CS-0088 | 0004 | Free skate; Scores 20–21 | CONTEXT_CHANGE | Skates ten credited elements, counts her own final spin, completes the first clean program of the event; 81.20, first. | EV-0005/0012/0015/0020; MD-CL-0008@5/0005@5 | HIGH outcome. | MD-CS-0087; MD-PERF-0051 |
| MD-CS-0089 | 0001 | Before and during her skate; Score 20 | REVEALED_NOT_NEW | Tested instruction on his own body; analysed her practice logs by condition and found a perfect record on one jump; during the skate holds that fifth is no good and that he has staked everything on the last pass. | EV-0011/0014/0015; MD-CL-0004@5/0007@6 | HIGH. | MD-CS-0068 |
| MD-CS-0090 | 0048 | During her skate; Score 20 | KNOWLEDGE_CHANGE | Recognizes the leading skater as a child he turned away at her mother's wish when he was a trainee. | EV-0008; MD-CL-0001@6/0014@3 | HIGH that he recalls it so. | none |
| MD-CS-0091 | 0002 | During and after her skate; Score 20 | KNOWLEDGE_CHANGE | Hears from a stranger that Tsukasa is a remarkable teacher because he was an excellent ice dancer; concludes that the past of a man nobody chose became this child's quality; calls the sport the watching of a miracle. | EV-0009/0010/0016; MD-CL-0010@6/0017@4 | HIGH. | MD-CS-0069 |
| MD-CS-0092 | 0001 | After her skate; Score 21 | REVEALED_NOT_NEW | Offers the coach's seat to the head coach and is pushed into it; taken to a coaches' dinner, sits at the head of the table and wants to leave. | EV-0018/0023; MD-CL-0010@6 | HIGH; comic register. | MD-CS-0070 |
| MD-CS-0093 | 0004 | Kiss-and-cry; Score 21 | REVEALED_NOT_NEW | Tells him that as a small child she dreamed repeatedly of sitting there and prayed for the dream to stop because waking was sad; a skater was someone who could sit in that place. | EV-0019; MD-CL-0015@5 | HIGH wording. | MD-CS-0088 |
| MD-CS-0094 | 0035 | After the result; Score 21 | CONTEXT_CHANGE | Second; reasons with herself that she should be glad; told she was a clubmate's reason to stay; says chasing is what she is good at. | EV-0022; MD-CL-0022@3/0001@6 | HIGH; one scene. | MD-CS-0076 |
| MD-CS-0095 | 0043 | After the result; Score 21 | REVEALED_NOT_NEW | Says she had come to hate skating when six clubmates left and stayed because Yūna did not give up. | EV-0022; MD-CL-0023@2 | HIGH. | MD-CS-0083 |
| MD-CS-0096 | 0022 | During and after the event; Scores 20–21 | REVEALED_NOT_NEW | Sees his prediction about Inori confirmed; privately regrets the broken plan a little; tells Yūna she is not alone and commits to a layout round her jump. | EV-0009/0015/0022; MD-CL-0024@2 | HIGH. | MD-CS-0077 |
| MD-CS-0097 | 0046 | After the result; Score 21 | CONTEXT_CHANGE | Ninth; had never imagined not reaching the All-Japan; says she wants to get better. | EV-0021; MD-CL-0005@5/0023@2 | HIGH. | MD-CS-0081 |
| MD-CS-0098 | 0001 | Night of the block; Score 21 | REVEALED_NOT_NEW | Tells Sonidori the gold was a promise and a passport to support, absolutely necessary now, to challenge Hikaru; privately adds Yodaka; affirms Sonidori as truly her coach. | EV-0024/0025/0026; MD-CL-0007@6/0011@6 | HIGH wording. | MD-CS-0086 |
| MD-CS-0099 | 0022 | Night of the block; Scores 21–22 | REVEALED_NOT_NEW | Keeps the secret of his own will to protect Hikaru and Yodaka's skating; uneasy about seeming to take credit; did not know the two coaches had met; brings Tsukasa home and to the ice to show him Yodaka skating. | EV-0026/0027/0030/0032/0033; MD-CL-0016@5 | HIGH that he says so. | MD-CS-0096 |
| MD-CS-0100 | 0001 | Middle school; Score 22 | REVEALED_NOT_NEW | Taught himself by imitating Yodaka; wanted someone to check what he had and a verdict on his talent as permission to continue; believed nobody wanted him on the ice. | EV-0029; MD-CL-0010@6/0001@6 | HIGH wording. | MD-CS-0049; MD-RT-0030/0031 |
| MD-CS-0101 | 0021 | Night of the block; Scores 21–22 | REVEALED_NOT_NEW | Interrupts the disclosure; skates better than when he competed, by Sonidori's judgment; smokes; asks about Tsukasa's career. | EV-0028/0030/0032/0035; MD-CL-0016@5 | HIGH conduct. | MD-CS-0062 |
| MD-CS-0102 | 0021 | After retiring at twenty, as reported | REVEALED_NOT_NEW | Could not get used to life off the ice; took an interest in coaching Hikaru when the request came with private ice for himself; asked Sonidori by letter for secrecy and for her daily care. | EV-0027/0033; MD-CL-0016@5 | HIGH that it was said; hearsay; the requester is unnamed. | MD-CS-0101 |
| MD-CS-0103 | 0001 | Night ice; Score 22 | CONTEXT_CHANGE | Falls in singles boots; sees Yodaka skate in person for the first time; jumps and crashes; resolves to use the chance for Inori; improves a Lutz take-off by watching; lands a backflip at first attempt. | EV-0031/0032/0034/0036; MD-CL-0004@5/0017@4 | HIGH. | MD-CS-0100; MD-PERF-0054 |
| MD-CS-0104 | 0021 | Night ice; Score 22 | REVEALED_NOT_NEW | Says ability unproven in the limited time is the same as none; teaches a backflip by one demonstration; hands Tsukasa a recording and tells him to audition again; says he knows his ability is rare and wasted it on backstage work; allows he may become a good coach. | EV-0035/0036/0037; MD-CL-0016@5/0025@1 | HIGH wording; contempt and a form of respect are both live readings. | MD-CS-0101 |
| MD-CS-0105 | 0001 | Night ice; Score 22 | DISPOSITION_CHANGE (candidate) | Declines the ice-show route; calls coaching his dream and his way of using his possibility, as long as he is entrusted by her; says there is no absolute on the ice; accepts the challenge. | EV-0037/0039; MD-CL-0010@6/0025@1 | HIGH wording; first such statement; durability unknown. | MD-CS-0103 |
| MD-CS-0106 | 0021 | Night ice; Score 22 | REVEALED_NOT_NEW | States that he contracted to coach Hikaru because she had the aptitude and will have her win gold at every competition for life as he did; says there is an absolute; tells Tsukasa to prove otherwise at the All-Japan. | EV-0038/0039; MD-CL-0016@5/0023@2/0025@1 | HIGH wording. | MD-CS-0104 |
| MD-CS-0107 | 0004 | Designated practice; Score 23 | KNOWLEDGE_CHANGE | Shares selected ice with Hikaru; sees her triple Axel and concludes the gap is real; finds she is the only qualifier without a triple Lutz; falls four times; skates the rest of the session without stopping. | EV-0043/0045/0046/0047; MD-CL-0015@5/0019@4/0003@5 | HIGH. | MD-CS-0093 |
| MD-CS-0108 | 0010 | Designated practice; Score 23 | CONTEXT_CHANGE | Waves to Inori; lands a triple Axel; stops over Inori after a fall and asks if she is all right; turns and skates away as Inori says her name; leaves early. | EV-0043/0045/0046/0047; MD-CL-0003@5 | HIGH conduct; no interior. | MD-CS-0064 |
| MD-CS-0109 | 0040 | Block day and a week later; Scores 20 and 23 | REVEALED_NOT_NEW | Says the last combination needed a conviction of absolute success; judges the strategy a long-term mistake and the medal a risk that will tighten round her. | EV-0013/0046; MD-CL-0008@5/0024@2 | HIGH that he thinks so; his chart is an estimate. | MD-CS-0082 |
| MD-CS-0110 | 0004 | Designated practice; Score 23 | CONTEXT_CHANGE | Stops Iruka to say her sister was not bad at jumps; accepts the rule against "if"; vows to land the hard jumps and take the gold without excuses. | EV-0048; MD-CL-0002@6 | HIGH. | MD-CS-0107 |
| MD-CS-0111 | 0037 | Designated practice; Score 23 | CONTEXT_CHANGE | Mocks Inori through her sister; says one does not say "if" in a world decided by probability; is disarmed into laughter. | EV-0044/0048/0050; MD-CL-0025@1 | HIGH. | V05 ceremony state |
| MD-CS-0112 | 0004 | Next day; Score 23 | CONTEXT_CHANGE | Counts about two weeks; says that even if it is impossible, and knowing how far she has come, she wants the triple Lutz and flip to fight Hikaru. | EV-0049; MD-CL-0015@5/0019@4 | HIGH wording. | MD-CS-0110 |
| MD-CS-0113 | 0001 | Next day; Score 23 | REVEALED_NOT_NEW | Gives her the arithmetic; says he does not think it impossible, that he foresaw this deficit at the summer camp, and that the support the gold has bought is the real reward; a jump specialist is coming. | EV-0049; MD-CL-0007@6/0008@5/0017@4 | HIGH wording; the plan's second half is untested. | MD-CS-0105 |
| MD-CS-0114 | 0011 | Block day and a week later | REVEALED_NOT_NEW | Explains the source of Inori's skating; says the method is efficient and that he could not bear it daily; finds his title hollow; still wants Tsukasa to himself. | EV-0007/0043; MD-CL-0021@3/0004@5 | HIGH. | MD-CS-0060 |
| MD-CS-0115 | 0007 | Years earlier and present | REVEALED_NOT_NEW | Sought a coach's verdict that her younger daughter could not skate; is now present with one friend among the parents and celebrates the win at home. | EV-0008/0017/0043; MD-CL-0014@3 | HIGH for the present; the past is a third party's recollection. | MD-CS-0034 |
| MD-CS-0116 | 0008 | Years earlier | REVEALED_NOT_NEW | Stopped skating after breaking a bone in jump practice. | EV-0047; MD-CL-0014@3 | HIGH as Inori's memory. | V02 identity rows |

### Current projection after V06

| Character | Current source boundary | Active state references | Bounded current formulation | Open contradictions |
| --- | --- | --- | --- | --- |
| MD-CHAR-0004 | V06/MD-FR-V06 | MD-CS-0088/0107/0110/0112 | Regional champion by a clean program, two triples short of what the next event is said to require, who measures herself against Hikaru and wants the fight. | Appetite and haste both shown within one week. |
| MD-CHAR-0001 | V06/MD-FR-V06 | MD-CS-0098/0105/0113 | Coach who won a qualifier by design for what it would buy, has claimed the work as his own dream, and has a wager with the champion he copied. | A first-person purpose conditioned on her trust; still does not know what she withheld. |
| MD-CHAR-0021 | V06/MD-FR-V06 | MD-CS-0102/0104/0106 | Retired champion who cannot leave the ice, coaching one child in secret so that she will never lose. | Contempt or a kind of respect toward Tsukasa; why he retired. |
| MD-CHAR-0022 | V06/MD-FR-V06 | MD-CS-0096/0099 | Keeper of a friend's secret and a coach who absorbs his pupil's lost gamble. | The reason he did not finish giving. |
| MD-CHAR-0035 | V06/MD-FR-V06 | MD-CS-0094 | Silver medalist who calls pursuit her strength. | One scene; her V05 grievance unspoken since. |
| MD-CHAR-0010 | V06/MD-FR-V06 | MD-CS-0108 | Present, far ahead, and for one moment unreadable toward Inori. | Whether she knows what is intended for her. |
| MD-CHAR-0040 | V06/MD-FR-V06 | MD-CS-0109 | The strategy's sharpest critic. | Wrong about foresight by Tsukasa's account; untested on risk. |
| MD-CHAR-0011 | V06/MD-FR-V06 | MD-CS-0114 | Attached, candid about his limits, holder of a hollow title. | — |
| MD-CHAR-0007, 0008 | V06/MD-FR-V06 | MD-CS-0115/0116 | A mother whose fear had a cause; a sister whose skating ended in injury. | Their own accounts. |
| MD-CHAR-0013, 0012, 0024, 0025, 0034 | V04 or earlier | as before | Unchanged in V06. | — |

### Readiness after V06

| Readiness record | Character / target / domain | Boundary / scope | Context coverage / counterevidence | Gaps / tests | Assessment / reviewer / date | History / revision |
| --- | --- | --- | --- | --- | --- | --- |
| MD-RD-0030 | 0004 / monograph / development through a first major title | V01–V06 manga-only | Adds a won qualifier, its aftermath, the pre-story longing and the family injury; the nonstop session and the admitted odds counter a triumph reading. | The single ground of her standing pattern; a setback at the national level; fanbooks excluded. | BOUNDED_PROVISIONAL; author; 2026-10-13; MD-CL-0002@6/0015@5/0019@4 | Extends MD-RD-0025; the mid-event caveat is lifted. |
| MD-RD-0031 | 0001 / monograph / coach identity, past and method | V01–V06 | His adolescence in his own narration; method disclosed and witnessed; a first-person claim; two named objections; EV-0014/0025/0029/0037/0046/0049. | What his claim on coaching rests on apart from her; the outcome of the wager; the unnamed early teacher. | BOUNDED_PROVISIONAL; author; 2026-10-13; MD-CL-0004@5/0007@6/0010@6/0017@4 | Extends MD-RD-0026. |
| MD-RD-0032 | 0001 with 0021 / relationship study / idol, opponent, opposite | V02, V04, V06 | A stairwell clash, a resemblance seen by a third party, a night on the ice with both creeds stated and a wager set. | Yodaka's side beyond his own statements; the wager's result. | BOUNDED_PROVISIONAL; author; 2026-10-13; MD-CL-0025@1/0016@5/0010@6 | First assessment. |
| MD-RD-0033 | 0021 / supporting-character study / the unbeaten champion as coach | V02–V06 | His verdicts, method, purpose and creed in his words; a friend's account of his retirement and the arrangement. | Why he retired; the contract's counter-party; any interior not spoken as doctrine. | BOUNDED_PROVISIONAL for a supporting study; author; 2026-10-13; MD-CL-0016@5 | First assessment above entry level. |
| MD-RD-0034 | 0035 / supporting-character study / the overtaken early starter | V05–V06 | A grievance stated, a gamble lost by a point, the grievance turned into a claim of skill; an editorial statement about her attachment. | Two volumes; whether pursuit holds; her view of Inori. | BOUNDED_PROVISIONAL for a supporting study; author; 2026-10-13; MD-CL-0022@3/0001@6 | Raises MD-RD-0028. |
| MD-RD-0035 | 0022 / supporting note / coaching manner, tactics and a kept secret | V03–V06 | Adds regret unspoken, a commitment after a loss, the secrecy's terms and his reasons. | The reason left unfinished. | BOUNDED_PROVISIONAL for a supporting note; author; 2026-10-13; MD-CL-0024@2/0016@5 | Extends MD-RD-0029. |

MD-RD-0021, 0023, 0024 and 0027 are unchanged. MD-CHAR-0010 remains INSUFFICIENT_EVIDENCE for a dedicated artifact in her own voice; MD-CHAR-0036–0051 other than those assessed above remain UNASSESSED.

## V07 evidence tables

The [V07 reading and frozen state](../02%20Sequential%20Readings/MEDALIST_V07_DEEP_READING.md) own all `MD-EV-V07-…` observations. In this section `EV-####` expands to `MD-EV-V07-####`; earlier volumes are written with their volume prefix. Every new record is version 1, first known after V07. Claim references are the versions in force at `MD-FR-V07`. Earlier tables are unchanged; the current projection is the last projection table in this document. Global entity and subject IDs remain null for every row.

### Identity updates to existing keys

| Character key | V07 disclosure | Basis | Remaining limit |
| --- | --- | --- | --- |
| MD-CHAR-0001 | Second of four brothers (肇 above; 誠 and 健 below); as a competitor could not choose what he ate; staked all his remaining skating money on the championship at which his partner planned to retire; cracked ribs | EV-0010/0035/0038/0043 | The brothers are named in a gag strip. |
| MD-CHAR-0004 | Thirteenth nationally by block score in her coach's table; her jumps travel | EV-0008/0033 | The table's comparability is assumed. |
| MD-CHAR-0006 | Planned to retire at the championship she skated with Tsukasa; runs a designated practice for ice-dance pupils | EV-0009/0038 | The first is his statement in a flashback. |
| MD-CHAR-0007 | Given name のぞみ confirmed in writing on a telephone screen | EV-0013 | — |
| MD-CHAR-0010 | 101.16 in Novice A at this summer's 名港杯; one of six national seeds | EV-0001/0033 | — |
| MD-CHAR-0015 | In her examination year; below grade 6; had been stuck on a double Axel since before the summer camp | EV-0007 | — |
| MD-CHAR-0018 | Away on a business trip during the drive; brings Inori home from Niigata by train | EV-0009/0039 | — |
| MD-CHAR-0023 | Kinki block champion with over 100 (101.23 in the table); a national seed; the clubmate who brought Ema into skating | EV-0031/0033 | — |
| MD-CHAR-0024 | Now in Novice A; seventh at the Kinki block with 80.01 | EV-0031 | — |
| MD-CHAR-0027 | The teacher was also Kōhei's and Juna's; taught a three-jump test in which the third attempt decides | EV-0037 | Identity with the teacher of V02–V03 is by context; still unnamed and unseen. |
| MD-CHAR-0032 | Shown as a man of monastic bearing who fixes layouts after official practice | EV-0032 | — |

### New keys

| Character key | Source-spelled identity / alias basis | Continuity | First observation | Global IDs / unresolved identity |
| --- | --- | --- | --- | --- |
| MD-CHAR-0052 | 魚淵翔; Uobuchi Kakeru, caption and profile with furigana; thirty-two; freelance jump coach | Japanese manga | EV-0003 | null/null |
| MD-CHAR-0053 | 鴨川洸平; Kamogawa Kōhei, caption with furigana; former ice dancer; head coach of 十南町レイクFSC; コウ to a clubmate | Japanese manga | EV-0019 (unnamed); named EV-0035 | null/null |
| MD-CHAR-0054 | 白鳥珠那; Shiratori Juna, family name with furigana; ジュナ; former skater, television personality, choreographer | Japanese manga | EV-0030 (on a television); EV-0035 | null/null |
| MD-CHAR-0055 | 亜昼美玖; Ahiru Miku, caption with furigana; a middle-schooler; 十南町レイクFSC | Japanese manga | EV-0019 (by given name); named EV-0033 | null/null |
| MD-CHAR-0056 | ライリー・フォックス; Riley Fox; Olympic champion for the United States; head of スターフォックスFSC, Tokyo | Japanese manga | EV-0030 | null/null |
| MD-CHAR-0057 | 胡荒亜子; Koara Ako, caption with furigana; twelve; スターフォックスFSC | Japanese manga | EV-0030 | null/null |
| MD-CHAR-0058 | 小雀白花; Kosuzume Kiyoka, caption with furigana; eleven; やまびこFSC | Japanese manga | EV-0030 | null/null |
| MD-CHAR-0059 | Hikaru's choreographer, unnamed; a man with tied hair, stubble and an earring who calls Yodaka ジュン and Sonidori 慎一郎 | Japanese manga | EV-0018 | null/null; identity with the ballet master of V05 is not established |

The seeded skaters 蝉丸ひまり and 大蜘蛛蘭, the other names in the national table, the grandfather in Aomori, Kōhei's small pupils and an unnamed man with glasses at やまびこFSC stay local to the reading and to the skating ledger.

### State events

| State event | Character | Story time / revealed after | Change kind | Action / self-report / inference | Evidence / claim version | Confidence / alternatives | Prior / correction |
| --- | --- | --- | --- | --- | --- | --- | --- |
| MD-CS-0117 | 0001 | Two weeks before the All-Japan; Score 24 | CONTEXT_CHANGE | Has begun demonstrating jumps for her since the block competition; takes her calm for disappointment and resolves to be a better model; says a teacher who can jump will look after her. | EV-0002/0003; MD-CL-0004@6/0010@7 | HIGH; comic register. | MD-CS-0113 |
| MD-CS-0118 | 0004 | Same; Score 24 | CONTEXT_CHANGE | Conceals her delight at his demonstrations so that he will not be embarrassed into stopping; resolves that she too must change. | EV-0002; MD-CL-0002@7 | HIGH; comic register. | MD-CS-0112 |
| MD-CS-0119 | 0052 | Same evening; Score 24 | REVEALED_NOT_NEW | Explains the harness as axis correction and his trade as knowledge renewed across the country; calls two new triples in a day common; stays a neutral freelance and admits that skaters with big events come first. | EV-0004/0005/0006/0042; MD-CL-0011@7/0005@6 | HIGH. | none |
| MD-CS-0120 | 0004 | Same evening; Score 24 | CONTEXT_CHANGE | Lands a triple flip and a triple Lutz in the harness and without it; counts all five triples; sets triple-triple and a triple Axel as next walls. | EV-0005/0006; MD-CL-0008@6 | HIGH; first landings. | MD-CS-0118; MD-SK-0041 |
| MD-CS-0121 | 0001 | A few days later; Score 24 | CONTEXT_CHANGE | Buys a harness with his own money for the club; learns its timing by watching; resolves to master it as a way for a non-jumper to coach jumps. | EV-0007; MD-CL-0017@5/0004@6 | HIGH. | MD-CS-0117 |
| MD-CS-0122 | 0015 | Same session; Score 24 | DISPOSITION_CHANGE (candidate) | Lands a double Axel in the harness; says she had meant to quit if she could never enter junior competition and can now try again. | EV-0007; MD-CL-0022@4 | HIGH wording; one scene. | V01 identity rows |
| MD-CS-0123 | 0001 | Same session; Score 24 | CONTEXT_CHANGE | Falling, keeps hold of the pole so that it cannot hit her, and takes the fall unbroken; winded; asks first whether she is hurt; cracked ribs; tells her not to worry. | EV-0008/0010; MD-CL-0010@7/0024@3 | HIGH. | MD-CS-0121 |
| MD-CS-0124 | 0004 | Days after the fall; Score 25 | CONTEXT_CHANGE | Can land the Lutz with one rotation only; watches her coach bow to her mother; counts the days. | EV-0011/0012; MD-CL-0019@5/0015@6 | HIGH conduct; cause stated later. | MD-CS-0120 |
| MD-CS-0125 | 0001 | Days after the fall; Score 25 | CONTEXT_CHANGE | Stops her checking outcomes and directs her to components; apologizes to her mother; consults the specialist; arranges an overnight drive with the adults' agreement. | EV-0009/0011/0012; MD-CL-0007@7/0017@5 | HIGH; what he said to her mother is not given. | MD-CS-0123 |
| MD-CS-0126 | 0004 | The night drive; Score 25 | REVEALED_NOT_NEW | Giddy; says it is the first time they have talked about anything but skating; sees his unguarded face; begins a vow to recover by tomorrow. | EV-0013/0014/0015; MD-CL-0002@7 | HIGH. | MD-CS-0124 |
| MD-CS-0127 | 0001 | Lake Suwa; Score 25 | REVEALED_NOT_NEW | Sits alone with a grave face; talks across her vow; says it is all right if she cannot jump tomorrow and that they will build it up together across the country; carries her to prove he is sturdy. | EV-0014/0015; MD-CL-0007@7 | HIGH wording. | MD-CS-0125 |
| MD-CS-0128 | 0001 | Lake Suwa; Score 25 | REVEALED_NOT_NEW | At her half-asleep remark that he was born to skate, recalls being turned away and "clinging on" by changing the dream's shape; weeps; vows to make her a skater the world calls born to it. | EV-0016; MD-CL-0010@7/0001@7 | HIGH for the large lettering; cropped fragments not relied on singly. | MD-CS-0127; MD-RT-0040 |
| MD-CS-0129 | 0010 | Same period; Score 26 | REVEALED_NOT_NEW | Stays behind in secret to study Yodaka's old programs; says she hates being ignorant of the world he saw and wants everything to be hers, beyond what she is given. | EV-0018; MD-CL-0003@6/0016@6 | HIGH wording. | MD-CS-0108 |
| MD-CS-0130 | 0004 | Niigata; Score 26 | REVEALED_NOT_NEW | Starts at the harness; classes saying she is frightened as selfish and suppresses it; later says aloud that she fears falling because she remembers her sister and her coach breaking bones, and that her body will not obey. | EV-0019/0022/0025; MD-CL-0002@7/0019@5 | HIGH wording. | MD-CS-0126 |
| MD-CS-0131 | 0001 | Niigata; Score 26 | CONTEXT_CHANGE | Takes the pole with cracked ribs, taught by the specialist; vows not to fall; had hoped only to recover the double Lutz. | EV-0020/0021; MD-CL-0017@5/0024@3 | HIGH. | MD-CS-0128 |
| MD-CS-0132 | 0004 | Niigata; Score 26 | CONTEXT_CHANGE | Offered a triple Lutz restored or a quadruple Salchow begun, leans to the safer; asks her coach to set out both branches as he once taught her; chooses the quad. | EV-0023/0024; MD-CL-0002@7/0024@3 | HIGH. | MD-CS-0130 |
| MD-CS-0133 | 0004 | Niigata; Score 26 | CONTEXT_CHANGE | With fifteen minutes left falls into compulsion and pleading; redirected, attends to sensation, takes off the harness, and lands unaided. | EV-0026/0027/0028; MD-CL-0015@6/0019@5 | HIGH; one landing. | MD-CS-0132; MD-PERF-0064 |
| MD-CS-0134 | 0001 | Niigata; Score 26 | REVEALED_NOT_NEW | Tells her not to wish for success too much, that jumping is not magic, that she need not be frantic; asks her to teach him what a quad feels like and to jump for one more word. | EV-0027; MD-CL-0004@6/0007@7 | HIGH wording. | MD-CS-0131 |
| MD-CS-0135 | 0024 | The 24th and after; Score 27 | CONTEXT_CHANGE | Seventh at the Kinki block with 80.01 and out; tells her coach not to console her; calls her first medal a charm and starting over her speciality; admits she is still sometimes sad; finds the block's winner farther away the closer she gets. | EV-0031; MD-CL-0020@2/0022@4/0023@3 | HIGH. | MD-CS-0042 |
| MD-CS-0136 | 0025 | The 24th and after; Score 27 | REVEALED_NOT_NEW | Names one fault and one best; will not tell her the opponents were too strong; reframes an early wall as a head start; chafes at his head coach's improvisation. | EV-0031/0032; MD-CL-0024@3 | HIGH. | V03 state |
| MD-CS-0137 | 0055 | Niigata; Scores 27–28 | REVEALED_NOT_NEW | Hands the decision on a quad to her coach as the owner of strategy; says her aim is one more month of skating; will stop when the season ends because the rink is closing. | EV-0034/0036; MD-CL-0024@3/0022@4 | HIGH. | none |
| MD-CS-0138 | 0053 | Niigata; Scores 27–28 | REVEALED_NOT_NEW | Declines the quad; holds, as a former ice dancer, to completeness and avoiding deductions; says neither of them knows a quad's risk; tells Tsukasa he has not changed. | EV-0034/0036/0037/0038; MD-CL-0008@6/0024@3/0025@2 | HIGH. | none |
| MD-CS-0139 | 0054 | Niigata; Score 28 | REVEALED_NOT_NEW | Teases Tsukasa; says a jump landed once went straight into competition in his day, that there is no right answer on the ice, and that adult caution is ego. | EV-0035/0037; MD-CL-0024@3 | HIGH. | none |
| MD-CS-0140 | 0001 | Niigata and the past; Score 28 | DISPOSITION_CHANGE (candidate) | Curt and self-deprecating before a famous clubmate; hears Yodaka's verdict in a friend's caution; decides the quad goes in and that making it succeed is his task; once staked everything on one championship to earn a reason to continue. | EV-0035/0037/0038; MD-CL-0007@7/0008@6/0010@7/0025@2 | HIGH wording. | MD-CS-0134; MD-RT-0041 |
| MD-CS-0141 | 0004 | Return and the following days; Score 28 | REVEALED_NOT_NEW | Lands a quadruple Salchow on home ice; says she chose it on purpose knowing it would bring attention, because one who is not beaten by attention can become the best in the world; states her goal as beating Hikaru. | EV-0036/0039; MD-CL-0002@7/0015@6 | HIGH. | MD-CS-0133 |
| MD-CS-0142 | 0021 | Same days; Score 28 | REVEALED_NOT_NEW | Names the quadruple Salchow before he is told, as the only card that could beat Hikaru; considers what to do. | EV-0040; MD-CL-0016@6/0025@2 | HIGH. | MD-CS-0106 |
| MD-CS-0143 | 0010 | Opening ceremony; Score 28 | CONTEXT_CHANGE | Walks barefoot past the field to Inori and says she has been waiting. | EV-0041; MD-CL-0003@6 | HIGH conduct. | MD-CS-0129 |

### Current projection after V07

| Character | Current source boundary | Active state references | Bounded current formulation | Open contradictions |
| --- | --- | --- | --- | --- |
| MD-CHAR-0004 | V07/MD-FR-V07 | MD-CS-0130/0132/0133/0141 | Entrant at her first national event with a quad landed twice in practice and a lost Lutz, who has named her fear aloud and chose exposure on purpose. | Frantic and attentive within one hour; layout unknown. |
| MD-CHAR-0001 | V07/MD-FR-V07 | MD-CS-0123/0127/0128/0134/0140 | Injured coach who removed the demand for an outcome at night and committed to a quadruple by day, and who has been told by his pupil what he once needed to hear. | "All right if you cannot" beside "make it succeed"; his body; his silence about his teacher. |
| MD-CHAR-0010 | V07/MD-FR-V07 | MD-CS-0129/0143 | Seeded favourite who wants everything her coach knows and has been waiting for Inori. | Whether she knows his design. |
| MD-CHAR-0021 | V07/MD-FR-V07 | MD-CS-0142 | Has modelled Inori correctly and is deciding on a response. | The response. |
| MD-CHAR-0052 | V07/MD-FR-V07 | MD-CS-0119 | Neutral technician who arms every club. | — |
| MD-CHAR-0053, 0054, 0055 | V07/MD-FR-V07 | MD-CS-0137/0138/0139 | A three-person team on a closing rink, divided over risk. | Miku's result; whether the delegation holds. |
| MD-CHAR-0024 | V07/MD-FR-V07 | MD-CS-0135 | Eliminated at 80.01 and starting over. | Sadness beside resolve. |
| MD-CHAR-0015 | V07/MD-FR-V07 | MD-CS-0122 | Past a jump that nearly ended her skating. | Grade 6 still ahead. |
| MD-CHAR-0035, 0022, 0011 | V06 state | as before | Unchanged in V07 beyond a table rank, a telephone call and a gag. | — |
| MD-CHAR-0013, 0012, 0034 | V04 or earlier | as before | Unchanged in V07. | — |

### Readiness after V07

| Readiness record | Character / target / domain | Boundary / scope | Context coverage / counterevidence | Gaps / tests | Assessment / reviewer / date | History / revision |
| --- | --- | --- | --- | --- | --- | --- |
| MD-RD-0036 | 0004 / monograph / development to the eve of a national event | V01–V07 manga-only | Adds her own account of fear and its sources, a deliberated choice with a stated reason, two modes of one pattern, a standing habit of shielding her coach. | The championship; the Lutz; whether naming fear holds; fanbooks excluded. | BOUNDED_PROVISIONAL; author; 2026-10-13; MD-CL-0002@7/0015@6/0019@5 | Extends MD-RD-0030. |
| MD-RD-0037 | 0001 / monograph / coach identity, past and method | V01–V07 | Adds a staked championship, bodily self-disregard, a coaching act that states his method, a decision made without his usual data. | The decision's outcome; his teacher; his family. | BOUNDED_PROVISIONAL; author; 2026-10-13; MD-CL-0004@6/0007@7/0010@7 | Extends MD-RD-0031. |
| MD-RD-0038 | 0001 with 0004 / relationship study / coach and pupil | V01–V07 | Mutual management of feeling; a first conversation outside the work; recognition passing from her to him; fear said and met; choices explained and made. | What each still keeps from the other; the event. | BOUNDED_PROVISIONAL; author; 2026-10-13; MD-CL-0002@7/0007@7/0010@7 | First dedicated assessment of the pair. |
| MD-RD-0039 | 0024 / supporting-character study / the detour and the restart | V03, V07 | A history of injury and patience, a first medal, an elimination at a high score, her own formulation and its residue. | Two volumes far apart; her coach's plan from here. | BOUNDED_PROVISIONAL for a supporting study; author; 2026-10-13; MD-CL-0020@2 | Raises MD-RD-0018. |
| MD-RD-0040 | 0010 / supporting note / ambition in her own words | V05–V07 | Three statements across three volumes, all about mastery and possession; warm conduct toward Inori at two meetings and one unreadable moment. | No statement about a rival; her knowledge of her coach's design. | BOUNDED_PROVISIONAL for a supporting note only; author; 2026-10-13; MD-CL-0003@6 | First assessment above entry level. |

MD-RD-0021, 0023, 0024, 0027 and 0032–0035 are unchanged. MD-CHAR-0052–0059 remain UNASSESSED for a dedicated artifact.

## V08 evidence tables

The [V08 reading and frozen state](../02%20Sequential%20Readings/MEDALIST_V08_DEEP_READING.md) own all `MD-EV-V08-…` observations. In this section `EV-####` expands to `MD-EV-V08-####`; earlier volumes are written with their volume prefix. Every new record is version 1, first known after V08. Claim references are the versions in force at `MD-FR-V08`. Earlier tables are unchanged; the current projection is the last projection table in this document. Global entity and subject IDs remain null for every row.

### Identity updates to existing keys

| Character key | V08 disclosure | Basis | Remaining limit |
| --- | --- | --- | --- |
| MD-CHAR-0001 | Worked a night job directing traffic to pay for the harness while his ribs were cracked; wears a suit Kago chose | EV-0032/0044 | The suit's price is a gag. |
| MD-CHAR-0003 | Has taught herself to tell the six jumps apart and follows the event closely; her father sees her mother's love of skating in her | EV-0014 | — |
| MD-CHAR-0007 | Travels to Aomori for the championship | EV-0003 | — |
| MD-CHAR-0010 | Badge grade seven; start order eleven; gives the athletes' oath; often absent from school; trains alone at night on inline skates; a broadcast crew follows her | EV-0002/0003/0025/0032/0038 | — |
| MD-CHAR-0012 | Named as a former pupil of Ryūgū who could jump a quadruple and never landed it in competition | EV-0005 | Stated by her former coach; she does not appear. |
| MD-CHAR-0021 | Not present at the championship; watches by broadcast; still uses the towel Inori gave him; visits the Sonidori house | EV-0025/0026/0029/0044 | The last is a gag strip. |
| MD-CHAR-0023 | Eleven, sixth grade; last year's Novice B silver medalist and twice second at that level; youngest of four sisters; three times Kinki block champion; start order six | EV-0001/0016/0022 | Profile fields. |
| MD-CHAR-0032 | Promised to make Suzu first in the world and forbade her to carry others' hopes | EV-0017 | An inset memory of his is unidentified. |
| MD-CHAR-0047 | Was Nachi Mario's coach | EV-0005 | — |
| MD-CHAR-0056 | Lets pupils attempt what they picture succeeding; her club took the whole Tokyo podium; wants Tsukasa as a coach | EV-0008/0011 | The last is one thought. |
| MD-CHAR-0058 | Start order eight; a grandfather who can again stand to watch; an improviser by profile | EV-0023/0043 | — |
| MD-CHAR-0059 | Identified as レオニード・ソロキン, Leonid Sorokin: Yodaka's former choreographer and Hikaru's present one; by wording and motif the ballet master of V05 | EV-0025/0026/0035 | No caption equates the V05 scene. |

### New keys

| Character key | Source-spelled identity / alias basis | Continuity | First observation | Global IDs / unresolved identity |
| --- | --- | --- | --- | --- |
| MD-CHAR-0060 | 平新谷萌栄; Hiraniya Moe, caption with furigana; スターフォックスFSC | Japanese manga | EV-0011 | null/null |
| MD-CHAR-0061 | 九猪桃子; Kokonoi Momoko, caption with furigana; 仙台スクエアFSC | Japanese manga | EV-0010 | null/null |
| MD-CHAR-0062 | 大蜘蛛蘭; Ōgumo Ran, caption and profile with furigana; thirteen; 福岡パークFSC | Japanese manga | Named V07; EV-0023 | null/null |
| MD-CHAR-0063 | 子出藤絃; Nedefuji Ito, caption with furigana; 蓮華茶FSC; one of three skating siblings | Japanese manga | Listed V07; EV-0021/0027 | null/null |

The coaches named at the boards (梟木豊, 目城理世, 伊文里青紫, 家守朝緑, 蜻堂緋紗子, 日瀧常, 布袋野兎太, 蕨一, 西猯郡志), the skater 釈取, the seed 蝉丸ひまり and the siblings 環 and 唯 stay local to the reading and to the skating and institutions ledgers.

### State events

| State event | Character | Story time / revealed after | Change kind | Action / self-report / inference | Evidence / claim version | Confidence / alternatives | Prior / correction |
| --- | --- | --- | --- | --- | --- | --- | --- |
| MD-CS-0144 | 0001 | Days before Niigata; Score 32 | REVEALED_NOT_NEW | Works nights on cracked ribs to pay for the harness and is ashamed to have it known; tells Hikaru his work is no sacrifice, that he does it for his own happiness whether Inori wins or loses, and that he will not make Inori pay one. | EV-0032/0037; MD-CL-0010@8/0007@8/0026@1 | HIGH wording. | MD-CS-0123 |
| MD-CS-0145 | 0010 | Days before Niigata; Score 32 | REVEALED_NOT_NEW | Skating alone at night, stops a rival's coach from calling her guardian and asks him whether his second job is a sacrifice for his pupil; reports her coach's teaching that victory needs sacrifice; afterwards says to herself that in the end everyone is like that. | EV-0032/0037; MD-CL-0003@7/0016@7 | HIGH wording; the last line is open between wistful, dismissive and resigned readings. | MD-CS-0129 |
| MD-CS-0146 | 0001 | Event day, morning; Score 29 | CONTEXT_CHANGE | Takes "unproven on the ice is the same as none" as the day's measure; has his pupil prove the quadruple in official practice to change the event's mood; throws her his drawstrings. | EV-0006/0007; MD-CL-0004@7/0025@3 | HIGH. | MD-CS-0140 |
| MD-CS-0147 | 0004 | Event day, morning; Score 29 | CONTEXT_CHANGE | Under the whole hall's gaze, says it is as she had braced for and that this is the air Hikaru jumps in; runs her attention routine; lands the quadruple Salchow in her run-through. | EV-0006/0007; MD-CL-0015@7/0008@7 | HIGH; practice. | MD-CS-0141; MD-PERF-0071 |
| MD-CS-0148 | 0047 | Event day; Score 29 | REVEALED_NOT_NEW | Says a pupil of his never landed her quadruple in competition and that only competition successes are recorded; names the gaze that presses such attempts down; would like to see this one done. | EV-0005/0006/0008; MD-CL-0005@7/0025@3 | HIGH. | V06 state |
| MD-CS-0149 | 0061 | Event, group one; Score 30 | CONTEXT_CHANGE | Adopts Inori's block-closing combination and scores 85.88; resents the quadruple as a projectile. | EV-0010; MD-CL-0008@7 | HIGH. | none |
| MD-CS-0150 | 0060 | Event, group one; Score 30 | CONTEXT_CHANGE | Attempts a quadruple Salchow after seeing Inori's arm position once; it opens to a single; skates the rest clean and leads for a time. | EV-0011; MD-CL-0004@7/0024@4 | HIGH. | none |
| MD-CS-0151 | 0056 | Event; Score 30 | REVEALED_NOT_NEW | Permits a pupil's untested attempt on the ground that she herself often could do unpractised things and that a child's sense of "maybe I can" is to be valued. | EV-0011; MD-CL-0024@4/0026@1 | HIGH. | V07 state |
| MD-CS-0152 | 0004 | Event, during group one; Score 30 | CONTEXT_CHANGE | Agrees to a division of roles in which her coach chooses the layout and she does not watch other skaters. | EV-0012; MD-CL-0002@8/0024@4 | HIGH. | MD-CS-0147 |
| MD-CS-0153 | 0023 | Before and during her skate; Score 30 | REVEALED_NOT_NEW | Tells Ema she skates only for herself and cannot carry her feelings; tells Inori the centre of the podium will be hers; by her coach's account fell and practised more than anyone for the sake of standing in that centre. | EV-0013/0015/0016/0022; MD-CL-0026@1/0023@4 | HIGH. | V03 state |
| MD-CS-0154 | 0032 | Remembered and present; Score 30 | REVEALED_NOT_NEW | Promised to make Suzu first in the world; forbade her to be a "good child" who needs others' reasons to skate; undertook to hold what would be loaded on her; keeps her layout after she fell on its hardest jump at practice. | EV-0013/0017/0020; MD-CL-0024@4/0026@1 | HIGH wording; an inset memory is unidentified. | V07 state |
| MD-CS-0155 | 0023 | Her free skate; Score 30 | CONTEXT_CHANGE | Opens with a triple Axel marked for review; lands two triple-triple combinations; changes manner in mid-program; 110.55, first by more than twenty points. | EV-0018/0019/0020; MD-CL-0008@7/0005@7 | HIGH. | MD-CS-0153; MD-PERF-0074 |
| MD-CS-0156 | 0024 | Event; Score 30 | REVEALED_NOT_NEW | Says she came to Aomori for herself, to see her target's best effort in person. | EV-0015; MD-CL-0020@2 | HIGH. | MD-CS-0135 |
| MD-CS-0157 | 0011 | Event; Scores 31–32 | REVEALED_NOT_NEW | Tells Inori it is better not to watch Hikaru; once told Hikaru she had done enough and that his father disapproves and cannot oppose her coach; prays for her last jump. | EV-0024/0038/0039; MD-CL-0021@4 | HIGH. | MD-CS-0114 |
| MD-CS-0158 | 0001 | Event, before Hikaru's skate; Score 31 | CONTEXT_CHANGE | Recognizes Inori's towel on Yodaka; declines to talk and says they will talk on the ice; tells Sorokin he believes his skater can outscore Hikaru. | EV-0026; MD-CL-0007@8/0025@3 | HIGH. | MD-CS-0146 |
| MD-CS-0159 | 0004 | Event, before Hikaru's skate; Score 31 | DISPOSITION_CHANGE (candidate) | Returns to ask to watch Hikaru after all; shows composure at a rival's score; gives reasons: Hikaru will always be ahead of her on the same road and is her special rival; she wants to take the whole performance in and stand against it. | EV-0027; MD-CL-0002@8/0015@7 | HIGH wording. | MD-CS-0152 |
| MD-CS-0160 | 0001 | Same; Score 31 | REVEALED_NOT_NEW | Does not refuse; restates the instruction as a common aid and not a prohibition; asks what reason she has found; lets her stay. | EV-0027/0028; MD-CL-0007@8/0024@4 | HIGH. | MD-CS-0158 |
| MD-CS-0161 | 0035 | Event, group two; Scores 31–32 | CONTEXT_CHANGE | Skates clean with the triple Lutz and triple loop; praised for it by Hikaru, struggles visibly and answers with good wishes; 105.43; backstage asks why her coach makes only Hikaru do dangerous things; weeps at Hikaru's score. | EV-0028/0034/0041; MD-CL-0001@8/0023@4 | HIGH. | MD-CS-0094 |
| MD-CS-0162 | 0010 | Event day; Scores 31–32 | REVEALED_NOT_NEW | Having seen Inori's quadruple, asks to open with one; says the assigned piece must be a step she needs; says she will challenge Yodaka; praises Yūna from the boards. | EV-0028/0033/0035; MD-CL-0003@7/0016@7 | HIGH wording. | MD-CS-0145 |
| MD-CS-0163 | 0021 | Event day, remote; Scores 31–32 | REVEALED_NOT_NEW | Asleep and unreachable during her warm-up; then permits an untested quadruple and changes her last jump; watches on a screen; says it is Tsukasa's turn. | EV-0029/0033/0042; MD-CL-0016@7/0024@4/0025@3 | HIGH. | MD-CS-0142 |
| MD-CS-0164 | 0010 | Remembered; Score 32 | REVEALED_NOT_NEW | Tells Rio of the rule that one fall in the nightly run-through ends her skating; finds competition easy by comparison; has no use for a self that would fail. | EV-0038/0039; MD-CL-0003@7/0016@7/0026@1 | HIGH wording. | MD-CS-0162; MD-PROP-0029 |
| MD-CS-0165 | 0010 | Her free skate; Scores 31–32 | CONTEXT_CHANGE | Opens with a quadruple toe loop untried on that ice; is shown straining; closes with a triple Axel, Euler and triple Salchow; all ten elements credited; 128.98; smiles at a plush wolf. | EV-0030/0034/0039/0040/0041; MD-CL-0023@4/0008@7 | HIGH. | MD-CS-0164; MD-PERF-0079 |
| MD-CS-0166 | 0022 | Event day; Scores 31–32 | REVEALED_NOT_NEW | As coach of record advises against the quadruple, refers the decision by telephone, and relays it; is blamed by rival coaches and doubted by his first pupil for it; by his son's account disapproves of the rule and cannot oppose it. | EV-0033/0034/0036/0038; MD-CL-0016@7 | HIGH. | MD-CS-0099 |
| MD-CS-0167 | 0001 with 0004 | After Hikaru's score; Score 32 | CONTEXT_CHANGE | He reasons that the present layout secures a high place and a junior-championship entry and resolves to say so; she says she absolutely wants to beat Hikaru and asks him to believe in her once more; he says the layout will change; she vows to make him a gold medalist's coach. | EV-0042; MD-CL-0002@8/0007@8/0010@8/0015@7/0026@1 | HIGH wording; whether the reversal is sound is open. | MD-CS-0159/0160 |

### Current projection after V08

| Character | Current source boundary | Active state references | Bounded current formulation | Open contradictions |
| --- | --- | --- | --- | --- |
| MD-CHAR-0004 | V08/MD-FR-V08 | MD-CS-0147/0159/0167 | Entrant yet to skate, who proved her quadruple in practice under full attention, insisted on watching her rival, and has taken on her coach's standing as her own stake. | Attentive in practice; unconditional in wanting; layout unknown. |
| MD-CHAR-0001 | V08/MD-FR-V08 | MD-CS-0144/0146/0160/0167 | Coach who says his work is its own good and that he will exact no sacrifice, and who has just set aside his own prudent judgment at his pupil's request. | Statement against act; a demonstration that armed rivals. |
| MD-CHAR-0010 | V08/MD-FR-V08 | MD-CS-0145/0162/0164/0165 | Leader at 128.98 under a rule that makes practice the trial and competition the respite, who means to challenge her coach and was moved by Inori's jump. | What she meant on the road; whether surpassing him is escape or obedience. |
| MD-CHAR-0021 | V08/MD-FR-V08 | MD-CS-0163 | Absent coach who governs by telephone, escalates risk, and keeps a child's towel. | Why the adults round him cannot oppose him. |
| MD-CHAR-0022 | V08/MD-FR-V08 | MD-CS-0166 | Coach of record carrying blame for decisions that are not his. | — |
| MD-CHAR-0023, 0032 | V08/MD-FR-V08 | MD-CS-0153/0154/0155 | A skater who carries nothing, second at 110.55 and in tears; a coach who holds her burdens. | His unexplained memory. |
| MD-CHAR-0035 | V08/MD-FR-V08 | MD-CS-0161 | Clean at last, third, able to wish her rival well and unable to understand her coach. | — |
| MD-CHAR-0011 | V08/MD-FR-V08 | MD-CS-0157 | Keeper of Hikaru's rule and her anxious supporter. | — |
| MD-CHAR-0056, 0060, 0061 | V08/MD-FR-V08 | MD-CS-0149/0150/0151 | A permissive champion-coach and two skaters who copied Inori. | — |
| MD-CHAR-0055, 0053, 0054 | V07 state | as before | Miku on the ice at the volume's end. | Her skate. |
| Others | V07 or earlier | as before | Unchanged in V08. | — |

### Readiness after V08

| Readiness record | Character / target / domain | Boundary / scope | Context coverage / counterevidence | Gaps / tests | Assessment / reviewer / date | History / revision |
| --- | --- | --- | --- | --- | --- | --- |
| MD-RD-0041 | 0004 / monograph / development to the middle of a national event | V01–V08 manga-only | Adds a method used under full attention, a reasoned override of her coach, and a vow that reverses his. | Her skate; the freeze falls mid-event, so V09 is the sound boundary. | BOUNDED_PROVISIONAL; author; 2026-10-13; MD-CL-0002@8/0015@7 | Extends MD-RD-0036. |
| MD-RD-0042 | 0001 / monograph / coach identity, past and method | V01–V08 | Adds a stated purpose apart from results, a tactic and its recoil, and a judgment reversed at his pupil's request. | The reversal's outcome and his conduct after it; the same mid-event caution. | BOUNDED_PROVISIONAL; author; 2026-10-13; MD-CL-0004@7/0007@8/0010@8 | Extends MD-RD-0037. |
| MD-RD-0043 | 0010 / supporting-character study / the prodigy's terms | V01–V08 | Her rule, her aims, her coach's doctrine, a complete program and its making; statements in her own voice across four volumes. | Her regard for Inori in words; what she meant on the road; her knowledge of the design for her career. | BOUNDED_PROVISIONAL for a supporting study; author; 2026-10-13; MD-CL-0003@7/0016@7 | Raises MD-RD-0040. |
| MD-RD-0044 | Ensemble / comparative study / coaching doctrines on risk and burden | V02–V08 | Stated positions of Tsukasa, Yodaka, Sonidori, Gori, Kameganya, Riley Fox, Kōhei and Juna, with cases. | Several doctrines untested by a costly failure; outcomes of the present event. | BOUNDED_PROVISIONAL; author; 2026-10-13; MD-CL-0024@4/0025@3/0026@1 | First assessment. |
| MD-RD-0045 | 0023 / supporting-character study / the unburdened contender | V03, V08 | One dense chapter, a doctrine, a program, a profile and her tears. | Her event is unfinished; little outside this volume. | INSUFFICIENT_EVIDENCE for a dedicated artifact; adequate for ensemble treatment; author; 2026-10-13; MD-CL-0026@1 | First assessment. |

MD-RD-0033 (Yodaka) is extended by MD-CS-0163 and the disclosures in MD-CS-0145/0164 without a new record. MD-RD-0021, 0023, 0024, 0027, 0032, 0034, 0035, 0038 and 0039 are unchanged. MD-CHAR-0060–0063 remain UNASSESSED.

## V09 evidence tables

The [V09 reading and frozen state](../02%20Sequential%20Readings/MEDALIST_V09_DEEP_READING.md) own all `MD-EV-V09-…` observations. In this section `EV-####` expands to `MD-EV-V09-####`; earlier volumes are written with their volume prefix. Every new record is version 1, first known after V09. Claim references are the versions in force at `MD-FR-V09`. Earlier tables are unchanged; the current projection is the last projection table in this document. Global entity and subject IDs remain null for every row.

### Identity updates to existing keys

| Character key | V09 disclosure | Basis | Remaining limit |
| --- | --- | --- | --- |
| MD-CHAR-0001 | Came to his former club from Nagoya with no experience of singles or dance; led an elite partner within a year; needed a medal at the national championships to ask for sponsorship before his savings ran out; left Lux Higashiyama for some months after the Novice championship to study, and has returned | EV-0009/0050/0051 | The first group is a clubmate's memory. Where he studied is not said. |
| MD-CHAR-0004 | Thirteen at the volume's end; first year of middle school and first year in the junior class; a federation designated skater, rank B; fourth at the All-Japan Novice A | EV-0039/0050/0051 | The calendar year is not given. |
| MD-CHAR-0006 | Shares Inori's coaching with Kōhei during Tsukasa's absence | EV-0050 | One caption. |
| MD-CHAR-0023 | Silver medalist of the All-Japan Novice A; on the visible part of the designation list at rank B | EV-0037/0051 | Her place is by the podium drawing and V08's score. |
| MD-CHAR-0025 | Studying to become a technical specialist | EV-0027 | — |
| MD-CHAR-0029 | Qualified for the All-Japan Novice A; 74.32 | EV-0010/0055 | That her friend Seira did not qualify comes from an under-jacket comic. |
| MD-CHAR-0052 | Taught the triple Axel to the bronze medalist as well as jumps to Inori | EV-0038 | — |
| MD-CHAR-0053 | Head coach of his club only from this year; himself a medalist at the national championships at which Tsukasa failed; now coaches at Lux Higashiyama | EV-0002/0009/0050/0055 | His medal is by his own memory. |
| MD-CHAR-0054 | Once aimed at the Olympics and concluded he lacked the talent | EV-0002 | His own words. |
| MD-CHAR-0055 | Began skating as a small child invited onto the ice by Kōhei and Juna; eleventh when announced at 74.67; has stopped skating | EV-0006/0007/0055 | Her final rank is not printed. |
| MD-CHAR-0057 | Bronze medalist of the All-Japan Novice A at 110.40 with a credited triple Axel; on the visible part of the designation list at rank B | EV-0038/0051 | — |

No new key is allocated. The skater 紅熊寧々子, named on the designation list, the older skaters who comment beside Iruka, and the advisers credited in the acknowledgements stay local to the reading and to the institutions ledger.

### State events

| State event | Character | Story time / revealed after | Change kind | Action / self-report / inference | Evidence / claim version | Confidence / alternatives | Prior / correction |
| --- | --- | --- | --- | --- | --- | --- | --- |
| MD-CS-0168 | 0055 | Remembered; Score 33 | REVEALED_NOT_NEW | Was a child alone in the snow whom two young adults invited onto the ice; on learning the rink would close said she would stop, and thanked them for looking for a way; took their proposal of the junior championship as a team aim. | EV-0002/0007; MD-CL-0022@5 | HIGH. | MD-CS-0137 |
| MD-CS-0169 | 0055 | Her free skate; Score 33 | CONTEXT_CHANGE | Takes the ice after the leader meaning to leave a record for her rink's adults; opens a Lutz to a single, falls on the next combination, lands her last one; 74.67, eleventh when announced. | EV-0003/0004/0005/0006; MD-CL-0005@8/0023@5 | HIGH; the cause is a rival coach's appraisal. | MD-CS-0168; MD-PERF-0082 |
| MD-CS-0170 | 0055 | After her score; Score 33 | CONTEXT_CHANGE | Will not leave the bench, because leaving it ends her being a skater; lists what she is about to lose; gives the bench up when another needs it. | EV-0007/0010; MD-CL-0022@5/0024@5 | HIGH. | MD-CS-0169 |
| MD-CS-0171 | 0055 | Niigata, remembered; Score 33 | REVEALED_NOT_NEW | Had told Inori that she decided to stop because everyone would have to strain for her, and that between that and her dream she could not choose the dream; marked it as her own view. | EV-0011; MD-CL-0026@2 | HIGH wording. | MD-CS-0137 |
| MD-CS-0172 | 0053 | Event; Score 33 | REVEALED_NOT_NEW | Cannot account for her collapse; lets her sit until she can accept it; holds, from a friend's failure, that talent has value only when someone has been able to use it; thanks her for having chosen the ice. | EV-0005/0007/0009/0010; MD-CL-0022@5/0024@5 | HIGH. | MD-CS-0138 |
| MD-CS-0173 | 0001 | His past, by a clubmate's memory; Score 33 | REVEALED_NOT_NEW | Staked a deadline and a condition on one championship: a medal with which to ask for support before his money ran out; failed at a point never missed in practice; his peers thought his talent sufficient. | EV-0005/0009; MD-CL-0010@9 | HIGH that it is remembered so. | MD-CS-0140; MD-TM-0062 |
| MD-CS-0174 | 0054 | Remembered and event; Score 33 | REVEALED_NOT_NEW | Says he wanted the Olympics and lacked the talent for that world; without a pass tries to reach her; tells her the ice is not the only place she can shine. | EV-0002/0005/0010; MD-CL-0022@5 | HIGH. | MD-CS-0139 |
| MD-CS-0175 | 0004 | Before her skate; Score 33 | REVEALED_NOT_NEW | Sets herself against Miku's reason in two words, "I chose", and concludes that she must therefore beat Hikaru properly. | EV-0011; MD-CL-0002@9/0026@2/0027@1 | HIGH wording. | MD-CS-0167 |
| MD-CS-0176 | 0037 | Event day, elsewhere; Score 33 | REVEALED_NOT_NEW | Would change a layout and lean on luck if her life could be changed by it; holds that whoever can make luck an ally is the real genius; a peer beside her holds that a jump is used only once polished. | EV-0012; MD-CL-0024@5/0025@4 | HIGH. | V06 state |
| MD-CS-0177 | 0004 | Five days and one hour before; Score 34 | REVEALED_NOT_NEW | Re-practises the triple Lutz alone at a public session because she does not want to compete unable to land the jump her coach was hurt on; asks that it be kept from him; an hour before her skate admits it and sets a condition for including it. | EV-0023; MD-CL-0002@9/0027@1 | HIGH. | MD-CS-0159 |
| MD-CS-0178 | 0001 | Before her skate; Score 34 | CONTEXT_CHANGE | Tabulates the champion's layout and plans to approach its base value; having overheard the secret, accepts the Lutz on a three-of-four tally; resolves never again to make her ask to be believed in; tells her nothing is fixed and that the colour of the medal is hers to choose. | EV-0017/0018/0019/0023; MD-CL-0004@8/0007@9 | HIGH. | MD-CS-0167 |
| MD-CS-0179 | 0004 | Her free skate, first eight elements; Scores 34–35 | CONTEXT_CHANGE | Runs her attention routine twice for two quadruple Salchows; falls on the Lutz; is on the music at once with the face the choreography asks for; finds the fall has restored feeling to her legs; skates a level-four step sequence thinking of what she loves. | EV-0020/0021/0022/0024/0025/0028/0029; MD-CL-0015@8/0008@8 | HIGH. | MD-CS-0147; MD-PERF-0083 |
| MD-CS-0180 | 0004 | Her free skate, last two jumps; Score 35 | CONTEXT_CHANGE | Changes the layout alone; reasons that only a triple Axel can now pass the champion's base value; discloses in thought that she believes she ended her coach's dream and means to prove otherwise to Yodaka; approaches in the frantic state; is interrupted by her coach's remembered sentence and her own earlier resolution; jumps on his old cue; lands without a fall. | EV-0030/0031/0032/0033/0034/0035; MD-CL-0002@9/0015@8/0027@1 | HIGH wording and order. | MD-CS-0179 |
| MD-CS-0181 | 0001 | During and after her skate; Score 35 | REVEALED_NOT_NEW | Shouts her name when she changes the plan; afterwards speaks only of how magnificent it was and of his thanks for watching from the nearest place; does not mention the change. | EV-0030/0036; MD-CL-0007@9/0024@5 | HIGH. | MD-CS-0178 |
| MD-CS-0182 | 0021 | During her skate; Score 35 | CONTEXT_CHANGE | Says aloud that her step sequence is remarkable; looks grim at her base value; his chair is empty before her score. | EV-0029/0034/0036; MD-CL-0016@8 | HIGH as shown; no thought is given. | MD-CS-0163 |
| MD-CS-0183 | 0010 | Event; Scores 33–35 | CONTEXT_CHANGE | Walks out expressionless during the collapse of the skater after her; returns to watch Inori; laughs when Inori is called faster; is delighted by the quadruple; grips her knee at the Axel. | EV-0004/0014/0020/0021/0034; MD-CL-0003@8/0023@5 | HIGH as shown. | MD-CS-0165 |
| MD-CS-0184 | 0025 | Event; Score 35 | REVEALED_NOT_NEW | Is studying to be a technical specialist and was asked by Tsukasa to watch the step sequence; explains the fall and the criteria; remarks that a sport which cannot call such children geniuses is a strange one. | EV-0025/0026/0027/0028; MD-CL-0001@9/0025@4 | HIGH. | MD-CS-0136 |
| MD-CS-0185 | 0057 | Event and after; Score 36 | CONTEXT_CHANGE | The only clean skater after the leader; credited with a triple Axel; third at 110.40; thanks the jump specialist by telephone. | EV-0038; MD-CL-0005@8/0011@9 | HIGH. | V07 state |
| MD-CS-0186 | 0052 | After the event; Score 36 | REVEALED_NOT_NEW | Is thanked by two competing skaters in turn; is glad for each; takes no side. | EV-0038; MD-CL-0011@9 | HIGH. | V07 state |
| MD-CS-0187 | 0004 | That night, a playground; Score 36 | CONTEXT_CHANGE | Says she told a lie about the gold; says she is not downcast and has been happy to be called a genius; says she used to envy the children who aimed at first; thanks him for making her someone people expect things of; her last look is unsmiling. | EV-0040/0041; MD-CL-0001@9/0019@6 | HIGH wording; the look is uncaptioned. | MD-CS-0180 |
| MD-CS-0188 | 0001 | That night, a playground; Score 36 | REVEALED_NOT_NEW | Says talent, diligence and luck are real and not the whole of her; that no one is made only of what others want; that she may aim at first even if no one expects it. | EV-0041; MD-CL-0001@9/0010@9/0027@1 | HIGH wording. | MD-CS-0144 |
| MD-CS-0189 | 0004 | That night, a hotel room; Score 36 | CONTEXT_CHANGE | Dreams of a discarded manual, an invitation and a lake; wakes crying; tells her sister that anything but first was unbearable; with fists clenched swears never to lose again and to prove her strength by gold. | EV-0042/0043/0048; MD-CL-0015@8/0019@6/0025@4 | HIGH. | MD-CS-0187; MD-CS-0040 (the acceptance on the train) |
| MD-CS-0190 | 0001 | That night, under a bridge; Score 36 | REVEALED_NOT_NEW | Calls the result his complete defeat and is ashamed to be thanked again; tells Hikaru that sacrifice is the self-harm someone blinded by inferiority reaches for, speaking of his own past, and that he will stop Inori from it; shouts at the rain by leave; says sacrifices cannot be weighed on one scale; sees her to her hotel. | EV-0044/0046/0047/0049; MD-CL-0010@9/0025@4/0026@2 | HIGH wording. | MD-CS-0188 |
| MD-CS-0191 | 0010 | That night, under a bridge; Score 36 | REVEALED_NOT_NEW | Goes out to find him; credits Inori's step sequence and says she wanted her to win; blames his refusal of sacrifice; calls Inori strong because a little abnormal; charges him with fear of blame and want of nerve; concedes his answer and condemns her own sneer; owns a debt to him for Rio; says she knows a shadow falls when she shines and will not seek forgiveness; will not doubt her coach if Inori loses again in a year; asks whether Inori will come at her in earnest. | EV-0045/0046/0047/0048; MD-CL-0003@8/0016@8/0023@5/0026@2 | HIGH wording; her tears are uncaptioned. | MD-CS-0183 |
| MD-CS-0192 | 0001 | That night and the following months; Score 36 | CONTEXT_CHANGE | Reckons the advantages of a strong start in junior lost and asks what he can do; leaves the club to study; returns unannounced with the news of her designation, which he wanted to give in person. | EV-0049/0050/0051; MD-CL-0017@6/0011@9 | HIGH for the acts; the content of the study is not shown. | MD-CS-0190 |
| MD-CS-0193 | 0004 | About eight months later; Score 36 | CONTEXT_CHANGE | Taller, with growing pains in a knee, recovering jumps; does not ask when her coach will return; had waited to show him her uniform; thinks that if she had not lost they might have stayed together; meets his return with anger, then tears of joy at the designation. | EV-0050/0051; MD-CL-0002@9/0022@5/0027@1 | HIGH. | MD-CS-0189 |
| MD-CS-0194 | 0053 | About eight months later; Score 36 and an aside | CONTEXT_CHANGE | Coaches Inori at Lux Higashiyama; was seen off to the post by Miku and her clubmates. | EV-0050/0055; MD-CL-0022@5 | HIGH; the send-off is a creator aside. | MD-CS-0172 |

### Current projection after V09

| Character | Current source boundary | Active state references | Bounded current formulation | Open contradictions |
| --- | --- | --- | --- | --- |
| MD-CHAR-0004 | V09/MD-FR-V09 | MD-CS-0175/0177/0180/0187/0189/0193 | Fourth at her first national event and now a designated junior, who skated to redeem a loss she believes she caused her coach, thanked him in public, grieved in private, and swore to prove herself by gold. | Told that worth does not wait on expectation; rejoices in being expected-of. Attentive in execution; compelled in choosing. |
| MD-CHAR-0001 | V09/MD-FR-V09 | MD-CS-0173/0178/0181/0188/0190/0192 | Coach whose plan held and whose pupil's addition lost the podium; who answered with thanks, a self-verdict of defeat, a doctrine grounded in his own failed sacrifice, and months away to study. | Says proof is not what a person is for; delivers proof as a promise kept. Does not know what she believes she owes him. |
| MD-CHAR-0010 | V09/MD-FR-V09 | MD-CS-0183/0191 | Champion who knows the shadow she casts, wants Inori as a rival of her own kind, defends her coach and has set a year's test between two doctrines. | Calls Tsukasa's doctrine too convenient and concedes its premise. |
| MD-CHAR-0021 | V09/MD-FR-V09 | MD-CS-0182 | Watcher who praised a step sequence and left before a score. | His view of the result. |
| MD-CHAR-0055, 0053, 0054 | V09/MD-FR-V09 | MD-CS-0170/0171/0172/0174/0194 | A skater who has stopped and was told she owes nothing; a coach who holds that talent must be used and has moved to a new club; a friend who names other places to shine. | — |
| MD-CHAR-0057, 0023, 0052 | V09/MD-FR-V09 | MD-CS-0185/0186 | Two medalists, both designated at rank B, and a specialist who armed one of them and the fourth-placed skater alike. | — |
| MD-CHAR-0025, 0037 | V09/MD-FR-V09 | MD-CS-0176/0184 | A coach training to judge technique; an elder skater for whom luck is part of genius. | — |
| Others | V08 or earlier | as before | Unchanged in V09. | — |

### Readiness after V09

| Readiness record | Character / target / domain | Boundary / scope | Context coverage / counterevidence | Gaps / tests | Assessment / reviewer / date | History / revision |
| --- | --- | --- | --- | --- | --- | --- |
| MD-RD-0046 | 0004 / monograph / development through a first national defeat | V01–V09 manga-only | A complete arc with a scored result; her deepest stated motive; both modes inside one jump; public and private responses to defeat; a later state across an elision. | Eight months unshown; whether the playground changed anything; conduct in junior. | BOUNDED_PROVISIONAL; author; 2026-10-13; MD-CL-0002@9/0015@8/0019@6/0027@1 | Extends MD-RD-0041; its mid-event caution is lifted. |
| MD-RD-0047 | 0001 / monograph / coach identity, past and method | V01–V09 | His history from two sides; a plan with a result; a stated account of what a person is; a doctrine with its ground; his response to defeat. | What he studied; whether he learns what she believes; his teacher. | BOUNDED_PROVISIONAL; author; 2026-10-13; MD-CL-0004@8/0007@9/0010@9/0017@6 | Extends MD-RD-0042; its mid-event caution is lifted. |
| MD-RD-0048 | 0001 with 0004 / relationship study / coach and pupil | V01–V09 | Adds a central asymmetry of knowledge, two departures from plan traced to it, an answer that removes its ground without naming it, and a separation. | Disclosure by either; the months apart. | BOUNDED_PROVISIONAL; author; 2026-10-13; MD-CL-0027@1/0002@9/0007@9 | Extends MD-RD-0038. |
| MD-RD-0049 | 0010 / supporting-character study / the prodigy's terms | V01–V09 | Adds her view of Inori, of sacrifice and of her own cost in her own voice, and a stated test. | Her year; her coach's reply; whether she knows the design for her career. | BOUNDED_PROVISIONAL for a supporting study; author; 2026-10-13; MD-CL-0003@8/0023@5 | Extends MD-RD-0043. |
| MD-RD-0050 | 0055 with 0053 / supporting study / an ending and a creed | V07–V09 | A motive, a skate, a bench, a stated reason, a coach's creed and its source, and an afterword. | Little outside three volumes; her life after skating is one aside. | BOUNDED_PROVISIONAL for ensemble or short supporting treatment; author; 2026-10-13; MD-CL-0022@5/0026@2 | First assessment. |

MD-RD-0044 (coaching doctrines) is extended by MD-CS-0172, 0176, 0181 and 0190 without a new record; several positions now have outcomes. MD-RD-0033 (Yodaka) gains only MD-CS-0182. MD-RD-0045 (Suzu) gains a final place and nothing else. MD-RD-0021, 0023, 0024, 0027, 0032, 0034, 0035 and 0039 are unchanged.

## V10 evidence tables

The [V10 reading and frozen state](../02%20Sequential%20Readings/MEDALIST_V10_DEEP_READING.md) own all `MD-EV-V10-…` observations. In this section `EV-####` expands to `MD-EV-V10-####`; earlier volumes are written with their volume prefix. Every new record is version 1, first known after V10. Claim references are the versions in force at `MD-FR-V10`. Earlier tables are unchanged; the current projection is the last projection table in this document. Global entity and subject IDs remain null for every row.

Adult readings of a child that the volume offers as guesses are recorded below as what was said and by whom. They are not written into the projection as traits; `MD-CL-0028@1` holds them as a hypothesis.

### Identity updates to existing keys

| Character key | V10 disclosure | Basis | Remaining limit |
| --- | --- | --- | --- |
| MD-CHAR-0001 | Took leave from coaching between February and about June and visited clubs round the country in search of a medical trainer; now also gives regular skating lessons at the Fukuoka club; his teacher is named | EV-0023/0024/0037 | Dates are relative captions. |
| MD-CHAR-0004 | Assigned to two Junior Grand Prix events; holds the national-team jacket | EV-0009/0045 | Which events is not said. |
| MD-CHAR-0006 | Daughter of Takamine Shō; became head coach of Lux Higashiyama in his stead; married, her husband having taken the family name | EV-0037/0053 | The marriage is from a gag strip. |
| MD-CHAR-0007 | Returned to full-time employment in the spring of Inori's first middle-school year; until then travelled to every away event | EV-0006 | — |
| MD-CHAR-0008 | Given name written 実叶 (Mika); by a junior's report won the Chūbu block in Novice B; skated at Meijō Crown; called a genius by others | EV-0016/0019/0045 | The block title is second-hand. |
| MD-CHAR-0010 | First-year middle-schooler still in the novice class by a footnote; taught steps by Takamine | EV-0011/0037/0038 | — |
| MD-CHAR-0011 | Champion of the All-Japan Novice A boys' event with 91.85 | EV-0049 | — |
| MD-CHAR-0021 | Changed coach every year from his first novice season; coached for one season by Kyōboku; once taught by Takamine; first eligible for the Olympics at twenty, as his pupil will be | EV-0002/0032/0034 | The first two are one former coach's testimony. |
| MD-CHAR-0027 | **Identified:** 高峰匠, Takamine, addressed as Shō; Tsukasa's teacher and Hitomi's father; formerly an ice-dance coach in Yokohama with Olympic experience; successor-designate of an earlier Lux Higashiyama who then refused to coach | EV-0002/0037 | Family-name furigana in a caption; the given name's reading is from address and a gag. "Olympic experience" is from the letter's wording. |
| MD-CHAR-0037 | Special designated skater from this season; winner of last season's Junior Grand Prix final; once a pupil at Meijō Crown; entered the senior national championships by recommendation | EV-0001/0013/0019 | — |
| MD-CHAR-0040 | A middle-school teacher for ten years before coaching | EV-0053 | A gag strip. |
| MD-CHAR-0053 | By profile disliked jumps after a childhood fall and did ice dance only; silver medalist at the national championships at which Tsukasa first competed; coach at Lux from February, mainly of adult beginners | EV-0003/0014 | Creator profile. |

### New keys

| Character key | Source-spelled identity / alias basis | Continuity | First observation | Global IDs / unresolved identity |
| --- | --- | --- | --- | --- |
| MD-CHAR-0064 | 烏羽ダリア; Karasuba Daria, caption with furigana on the family name; 岡山ティナFSC; a junior assigned to two Junior Grand Prix events | Japanese manga | EV-0009/0019 | null/null |
| MD-CHAR-0065 | 高井原麒乃; Takaihara Kino, caption with furigana; 福岡パークFSC; a leading junior, 183 cm by caption | Japanese manga | EV-0015 | null/null |
| MD-CHAR-0066 | 紅熊寧々子; Kurekuma Neneko, caption with furigana; 蓮華茶FSC; a leading junior; on V09's designation list | Japanese manga | Listed V09; EV-0015 | null/null |
| MD-CHAR-0067 | 梟木豊; Kyōboku Yutaka, caption with furigana; head coach of 岡山ティナFSC; Yodaka's coach for one season | Japanese manga | Named at the boards V08; EV-0023/0032 | null/null |

布袋野兎太 (Hotaino Tōta by furigana), head coach of the Fukuoka club, the shared medical trainer, who is not captioned in this volume, and the federation's advisers stay local to the reading and to the institutions ledger.

### State events

| State event | Character | Story time / revealed after | Change kind | Action / self-report / inference | Evidence / claim version | Confidence / alternatives | Prior / correction |
| --- | --- | --- | --- | --- | --- | --- | --- |
| MD-CS-0195 | 0021 | Present, an aquarium; Score 37 | REVEALED_NOT_NEW | Has his pupil write to his old teacher for one skill; states that she will win every competition for seven years so that her Olympic place depends on no one's choice; to the objection that it is too long answers that he could. | EV-0002; MD-CL-0016@9/0025@5 | HIGH wording. | MD-CS-0182 |
| MD-CS-0196 | 0027 | Same | REVEALED_NOT_NEW | Asks whether he is making her repeat his own path; counsels against compelling continuous victory because body and heart change; says growth is loss. | EV-0002; MD-CL-0022@6/0026@3 | HIGH wording. | V07 aside (V07:EV-0017) |
| MD-CS-0197 | 0001 | February; Score 37 | CONTEXT_CHANGE | Brings in Kōhei; holds a handover; tabulates her credited jumps; sets two tasks; leaves that evening by his own decision, saying he hates it. | EV-0003/0004/0005; MD-CL-0004@9/0017@7 | HIGH. | MD-CS-0192 |
| MD-CS-0198 | 0004 | February; Score 37 | DISPOSITION_CHANGE (candidate) | Sets herself a rule not to telephone him, so as to learn to do well in his absence and surprise him with growth; thinks that she hates the parting too; asks for his drawstrings; a day later says she is lonely. | EV-0005/0008; MD-CL-0002@10/0027@2 | HIGH wording. | MD-CS-0193 |
| MD-CS-0199 | 0007 | February to spring; Score 37 | CONTEXT_CHANGE | Returns to full-time work and entrusts away events to the coaches; says the junior class is a world she does not know. | EV-0006/0007; MD-CL-0014@5 | HIGH. | MD-CS-0115 |
| MD-CS-0200 | 0004 | February to spring; Score 37 | CONTEXT_CHANGE | Growing pains begin in both knees; told to work on singles and basic turns, wonders whether she is so poor that she must start again; is named for two overseas events and asks herself why. | EV-0006/0008/0009; MD-CL-0015@9/0022@6 | HIGH. | MD-CS-0198 |
| MD-CS-0201 | 0053 | February onward; Score 37 | CONTEXT_CHANGE | Calls his new pupil by his old pupil's name, apologizes, and pledges to back her dream; explains what selection for overseas events requires; works with her on jump height. | EV-0005/0007/0008/0019; MD-CL-0011@10 | HIGH. | MD-CS-0194 |
| MD-CS-0202 | 0001 | December to June, as told; Score 39 | REVEALED_NOT_NEW | Decides the club needs a trainer; searches the country for a medical trainer against a page of conditions; cannot forgive the thought of careless handling; could hardly get up on hearing of her growing pains and hid it on the telephone. | EV-0024/0026; MD-CL-0010@10/0017@7 | HIGH. | MD-CS-0197 |
| MD-CS-0203 | 0004 | Arrival at the camp; Score 37 | CONTEXT_CHANGE | Reports to herself that she fell on the Lutz at the selection, cannot train the quadruple, could not skate last autumn's layout, and could not grow. | EV-0010; MD-CL-0015@9/0019@7 | HIGH. | MD-CS-0200 |
| MD-CS-0204 | 0057 | Camp; Scores 37 and 40 | REVEALED_NOT_NEW | Declares that her aim is to beat Inori, because Hikaru has found something in her; later is crushed that a triple Axel did not make her special. | EV-0011/0042; MD-CL-0001@10/0023@6 | HIGH. | MD-CS-0185 |
| MD-CS-0205 | 0004 | Camp, day one; Score 37 | CONTEXT_CHANGE | Cannot answer Hikaru's greeting; feels her as pitch black out of chagrin; hates a self that is standing still; cries; thinks there is no going back; resolves to leave the camp stronger and asks Iruka to model a junior who can fight abroad. | EV-0012/0013; MD-CL-0015@9/0019@7 | HIGH wording. | MD-CS-0203; MD-CS-0189 |
| MD-CS-0206 | 0010 | Camp, days one and two; Scores 37 and 39 | CONTEXT_CHANGE | Greets Inori warmly; watches her leave in tears with a flushed smile; watches her closely the next morning; says she forgot to watch Tsukasa jump. | EV-0012/0029/0038; MD-CL-0003@9 | HIGH as shown; uncaptioned. | MD-CS-0191 |
| MD-CS-0207 | 0037 | Camp, day one; Score 38 | REVEALED_NOT_NEW | Hides fondness for Inori behind insult; stills at the word genius; says those who quit in junior are the ones who grew heavy and ceased to be praised, and that nobody stops them; says Mika forgot their promises and quit, that she is angry, and that she will not speak to her until she has an Olympic gold medal; kicks a chair and later nurses the girl who covered for her. | EV-0015/0016/0019/0020/0021; MD-CL-0022@6/0026@3 | HIGH wording. | MD-CS-0176; MD-CS-0111 |
| MD-CS-0208 | 0004 | Camp, day one; Score 38 | REVEALED_NOT_NEW | Objects to an insult as her coach taught; says she will not quit, that she may aim even if no one praises her, and that the dream is not for herself alone; feigns a fall to keep Iruka out of trouble; remembers her from infancy and offers to telephone her sister. | EV-0015/0016/0020/0021; MD-CL-0002@10/0027@2 | HIGH. | MD-CS-0205 |
| MD-CS-0209 | 0004 | Camp, day one; Score 38 | CONTEXT_CHANGE | Meets rules under which her weakest jump is compulsory and her strongest barred; falls on the Lutz; is warned about her edge; hears her coach's analysis as one more correction; resolves to grow at double speed; returns unasked to old basic drills. | EV-0017/0018/0027; MD-CL-0015@9/0008@9 | HIGH for conduct; the reversion is his report. | MD-CS-0208 |
| MD-CS-0210 | 0001 | Camp, day one; Scores 38–39 | REVEALED_NOT_NEW | Judges that she is treating him as someone to show results to and trying to solve alone; diagnoses the Lutz as an edge laid too deep and refuses the shortcut; says his teaching no longer gets through; asks senior coaches for help. | EV-0018/0021/0026/0027; MD-CL-0004@9/0027@2 | HIGH. | MD-CS-0202 |
| MD-CS-0211 | 0040 | Camp, night one; Scores 38–39 | REVEALED_NOT_NEW | Says the loss of jumps in growth is half fact and half curse and that injury is now the common cause; wants more precedents of uninjured careers and no pain for children but that of competing; offers, as a guess, that Inori moves by adults' faces and listens to her coach because his cannot lie; says a failure to convey must never be put on the receiver; holds that a coach is another pair of eyes. | EV-0022/0025/0028/0030; MD-CL-0026@3/0028@1 | HIGH that it was said; his reading of her is explicitly tentative. | MD-CS-0109 |
| MD-CS-0212 | 0067 | Camp, night one; Scores 39–40 | REVEALED_NOT_NEW | Says Yodaka corrected himself without video and saw his own career from above, needed no coach, and left before the season's end; felt an ornament beside him; regrets not telling him that a child needs an adult who stays. | EV-0032/0034; MD-CL-0016@9/0026@3 | HIGH that it was said; the hawk's eye is his metaphor. | none |
| MD-CS-0213 | 0022 | Camp, night one; Score 40 | REVEALED_NOT_NEW | Says that if Hikaru wished to leave he could not hold her, and that her reliance on his household may be shown out of consideration. | EV-0035; MD-CL-0016@9 | HIGH wording. | MD-CS-0166 |
| MD-CS-0214 | 0001 | Camp, night one and day two; Scores 39–40 | KNOWLEDGE_CHANGE (candidate) | Asks himself whether her strength was built on her lonely years; lands a double Lutz within the hour and is shaken at its ease; identifies the faculty described in Yodaka with his own sense of his movement; concludes that he had no guide, denied his talent out of inferiority, and may have wasted his weapon. | EV-0028/0031/0036; MD-CL-0010@10/0025@5/0028@1 | HIGH wording; each step is his inference. | MD-CS-0210; MD-CS-0190 |
| MD-CS-0215 | 0004 | Camp, day two; Score 39 | CONTEXT_CHANGE | Accepts take-off drills inside a contest and from Hitomi; says she had thought her skating worse than everyone's; assembles the jump as a puzzle and lands a clean triple Lutz; feels little, because she ought to be able to; is overjoyed at his double. | EV-0029/0030/0031; MD-CL-0015@9/0004@9/0028@1 | HIGH. | MD-CS-0209 |
| MD-CS-0216 | 0027 | Camp, day two; Score 40 | CONTEXT_CHANGE | Appears at the camp as Hikaru's teacher; tells his daughter that Yodaka coaches her; says this is the last time, that he realized too late he has no capacity to guide people, and that he is tidying up what he left undone. | EV-0037; MD-CL-0016@9/0017@7 | HIGH wording; what was left undone is not said. | MD-CS-0196 |
| MD-CS-0217 | 0006 | Camp, day two; Score 40 | KNOWLEDGE_CHANGE | Learns from her father that Yodaka coaches Hikaru; recounts that she became head coach when he refused to; is vexed that he has taken another pupil. | EV-0037; MD-CL-0011@10 | HIGH. | V08 state |
| MD-CS-0218 | 0010 | Camp, day three; Score 40 | REVEALED_NOT_NEW | Breaks her peers' quarantine to question Inori; asks on what grounds she believes in victory; recalls being told to become someone who can live only on the ice; concludes that Inori resembles Yodaka and that Tsukasa is her own kind; asks for a promise to win the series final; an unattached line says she can still wait. | EV-0039/0040/0041; MD-CL-0003@9/0025@5 | HIGH that she thinks it; the last line's speaker is by placement. | MD-CS-0206 |
| MD-CS-0219 | 0004 | Camp, day three; Score 40 | REVEALED_NOT_NEW | States her goal as winning the series final; says she has never aimed at gold on grounds, cannot forgive a self that cannot take it, is on the ice thanks to the one who believes in her victory, and must go on proving with gold that she ought to be there; gives the promise asked. | EV-0040/0041; MD-CL-0001@10/0019@7/0027@2 | HIGH wording. | MD-CS-0215; MD-CS-0189 |
| MD-CS-0220 | 0010 | Camp, day three; Score 40 | CONTEXT_CHANGE | Has lower-back pain in practice; accepts a support from Iruka, who tells her she is taking skating lightly; remarks that her coach has not noticed; has grown and lands more lightly. | EV-0038/0043; MD-CL-0003@9/0022@6 | HIGH. | MD-CS-0218 |
| MD-CS-0221 | 0001 | After the camp; Score 40 | CONTEXT_CHANGE | Reads her practice log; concludes that her growth came from a concentration that pares her down and narrows her view; weeps at the national jacket and does not want her to lose it; resolves to hand on to her the use of the faculty he believes he has; renews the vow of gold abroad. | EV-0044/0045/0046/0047; MD-CL-0004@9/0010@10/0001@10 | HIGH. | MD-CS-0214 |
| MD-CS-0222 | 0011 with 0004 | The day after the All-Japan Novice girls' event; Short Program 5 | CONTEXT_CHANGE | He skates a personal best, expects to be overtaken, wins when the favourites fall, and calls the title worthless beside Hikaru's and Inori's fourth place; she tells him not to make a fool of the gold medalist everyone aimed to be, and names his self-deprecation as a defence she knows; he weeps that he could not rejoice, calls her by her name, and tells the press he will aim at the title again. | EV-0049/0050/0051/0052; MD-CL-0021@5/0019@7 | HIGH. | MD-CS-0157; MD-CS-0189 |

### Current projection after V10

| Character | Current source boundary | Active state references | Bounded current formulation | Open contradictions |
| --- | --- | --- | --- | --- |
| MD-CHAR-0004 | V10/MD-FR-V10 | MD-CS-0198/0205/0208/0215/0219 | A junior assigned abroad, in pain and short of her autumn jumps, who holds that gold is how she proves she belongs on the ice, shows her coach results, and recovered a lost jump inside a game. | Quotes his release and refuses it; generous to a friend's gold on the morning after her own loss. |
| MD-CHAR-0001 | V10/MD-FR-V10 | MD-CS-0202/0210/0214/0221 | Coach who answered defeat by finding a trainer, returned to find his words not arriving, and has decided that he wasted a faculty of his own and will give it to her. | Told her worth does not wait on proof; calls the jacket a decoration she must not lose. Does not know her creed. |
| MD-CHAR-0010 | V10/MD-FR-V10 | MD-CS-0206/0218/0220 | Champion who sought out Inori, read her as her own coach's likeness, is acquiring the other team's weapon, and has a back that hurts. | Calls Tsukasa her own kind after calling Inori her own kind in V09. |
| MD-CHAR-0021 | V10/MD-FR-V10 | MD-CS-0195 | Coach who was never coached, applying his own path to a child for seven years. | Whether he sees the cost his old coaches name. |
| MD-CHAR-0027 | V10/MD-FR-V10 | MD-CS-0196/0216 | Teacher of both rival coaches, returned once to teach the rival's pupil, who denies his own capacity to guide. | What he left undone. |
| MD-CHAR-0037 | V10/MD-FR-V10 | MD-CS-0207 | The leading junior, oriented by a vow toward a friend who stopped, who notices what coaches miss. | — |
| MD-CHAR-0040, 0067, 0022 | V10/MD-FR-V10 | MD-CS-0211/0212/0213 | Three head coaches with a shared aim of protecting children from foreseeable harm and separate regrets. | One remark in their room has no fixed speaker. |
| MD-CHAR-0011 | V10/MD-FR-V10 | MD-CS-0222 | National novice champion who learned to value his title from the girl who missed hers. | — |
| MD-CHAR-0006, 0007, 0008, 0053 | V10/MD-FR-V10 | MD-CS-0199/0201/0217 | A head coach who now knows the secret; a mother back at work; a sister with a history of her own; a second coach settled in. | — |
| Others | V09 or earlier | as before | Unchanged in V10. | — |

### Readiness after V10

| Readiness record | Character / target / domain | Boundary / scope | Context coverage / counterevidence | Gaps / tests | Assessment / reviewer / date | History / revision |
| --- | --- | --- | --- | --- | --- | --- |
| MD-RD-0051 | 0004 / monograph / development into the junior class | V01–V10 manga-only | Adds her stated creed, a documented reversion and recovery, three adult readings and a counter-instance of generosity. | No junior result; the adult readings are guesses and must be weighed as such; nine months partly reconstructed. | BOUNDED_PROVISIONAL; author; 2026-10-13; MD-CL-0002@10/0015@9/0019@7/0028@1 | Extends MD-RD-0046. |
| MD-RD-0052 | 0001 / monograph / coach identity, past and method | V01–V10 | Adds the content of his absence, his fear, a self-assessment of wasted talent, his teacher, and a new programme. | Whether the programme is coherent; his teacher's account of him. | BOUNDED_PROVISIONAL; author; 2026-10-13; MD-CL-0004@9/0010@10/0017@7 | Extends MD-RD-0047. |
| MD-RD-0053 | 0001 with 0004 / relationship study / coach and pupil | V01–V10 | Adds an announced separation, her rule, a failure of instruction with its diagnosis and repair, and a creed he has not heard. | Disclosure by either. | BOUNDED_PROVISIONAL; author; 2026-10-13; MD-CL-0027@2/0002@10 | Extends MD-RD-0048. |
| MD-RD-0054 | 0021 / supporting-character study / the champion who needed no coach | V02–V10 | A former coach's testimony, a remembered program, a plan in his own words, and two teachers. | His family; why he left each coach; his own account. | BOUNDED_PROVISIONAL for a supporting study; author; 2026-10-13; MD-CL-0016@9 | Raises MD-RD-0033. |
| MD-RD-0055 | 0037 / supporting-character study / the leading junior and a broken promise | V05–V10 | A vow, a history with the protagonist's family, conduct toward two younger skaters. | One camp; Mika's side absent. | INSUFFICIENT_EVIDENCE for a dedicated artifact; adequate in outline for ensemble treatment; author; 2026-10-13; MD-CL-0022@6 | First assessment. |

MD-RD-0049 (Hikaru) is extended by MD-CS-0218 and 0220 without a new record. MD-RD-0024 (Rio) is extended by MD-CS-0222. MD-RD-0044 (coaching doctrines) is extended by MD-CS-0196, 0211, 0212 and 0213. MD-RD-0050 (Miku and Kōhei) gains a profile and nothing else. MD-CHAR-0064–0066 remain UNASSESSED; MD-CHAR-0067 is a witness, not a study target.
