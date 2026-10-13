---
title: "Medalist — Character Development and Reconstruction Readiness"
artifact_id: "MEDALIST_CHARACTER_DEVELOPMENT_AND_READINESS_LEDGER"
artifact_type: "character_state_readiness_ledger"
series: "Medalist / メダリスト"
series_id: "medalist"
generation: "MEDALIST_BOOTSTRAP_V1"
version: "1.0"
status: "canonical"
scope: "Time-indexed character interpretation, identity resolution and evidence-specific promotion readiness"
canonical_home: "series/medalist/03 Longitudinal Ledgers/MEDALIST_CHARACTER_DEVELOPMENT_AND_READINESS_LEDGER.md"
source_boundary: "Japanese V01 Scores 1–3 and own-volume material closed; 233 admitted images; fanbooks/later sources unadmitted"
created: "2026-10-11"
updated: "2026-10-12"
review_status: "AUTHOR_REVIEWED_V01_UPDATE"
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
