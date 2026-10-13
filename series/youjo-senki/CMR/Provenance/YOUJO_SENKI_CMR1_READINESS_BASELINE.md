---
series: YOUJO_SENKI
artifact_type: historical_readiness_baseline
scope: V01-V14
generation: V2_CMR
version: "1.0"
status: historical_legacy
source_boundary: "Original Japanese Youjo Senki light novels Volumes 01-14"
governing_method: "YOUJO_SENKI_CHARACTER_MODELING_REFERENCE_METHOD.md v1.1"
cmr0_manifest: "YOUJO_SENKI_CMR_SOURCE_EXTRACTION_MANIFEST.md"
cmr0_locator_index: "YOUJO_SENKI_CMR_SOURCE_LOCATOR_INDEX.tsv"
secondary_context: "Mature V2 Documents 02, 03, and 04; secondary analysis informs interpretation but does not override Japanese-source coverage"
supersedes: []
superseded_by: []
do_not_use_as_current_authority: true
artifact_id: YOUJO_SENKI_CMR1_READINESS_BASELINE
canonical_home: "series/youjo-senki/CMR/Provenance/YOUJO_SENKI_CMR1_READINESS_BASELINE.md"
port_revision: "1"
port_date: 2026-10-11
source_drive_id: "1LYRzJS4AL6jHAmIAjkaOC-HIWQQdBp51"
source_drive_revision: "0B24avie5yJngQ3BBWHVLcXRXQXRleW5KWkR2Nis0dzBTdEpzPQ"
source_sha256: "30ace4c0f4a0b03aa003aea8e7377cb1595450bed326451908a59bf13c5c3417"
source_status_at_freeze: active_provisional
baseline_role: FIRST_20_SUBJECT_AUDIT_ONLY
promotion_status: PROPOSED_GIT_PROVENANCE_PENDING_VERIFIED_MAIN_INTEGRATION
former_drive_pointer_update_status: NOT_PERFORMED
---

> **Historical first-audit baseline.** The complete original CMR1 audit body and its source locators are preserved below. This Git artifact is `historical_legacy` with `do_not_use_as_current_authority: true`. It preserves how the initial twenty-subject roster was admitted; it does not substitute for the current source-adjudicated readiness/coverage reassessment, confer finished-model status, or permanently cap the discovered roster.

The source audit was `active_provisional` at the frozen Drive revision. Its twenty original classifications remain unchanged:

| Original first-audit class | Subjects |
|---|---|
| `FULL_SPECTRUM` | Tanya Degurechaff (`HIGH`); Erich von Lergen (`MODERATE_HIGH`) |
| High-confidence `DOMAIN_BOUNDED` | Visha, Zettour, Weiss, Grantz, Uger, Rudersdorf, Drake, Mary Sue, Calandro, Loria |
| Narrower `DOMAIN_BOUNDED` | Romel, Conrad, de Lugo, Anson Sioux, Schugel |
| `RECOGNITION_PROFILE` | Meybert, Tospan, Josef |

The preserved body contains the original individual confidence labels, approved domains, representative exact locators, and negative constraints. Alias-hit counts and local-window metrics remain retrieval proxies. Apparent dialogue proximity never establishes actual speaker or focalizer. Unexamined additional figures remain `NOT_YET_AUDITED`; they do not become `INSUFFICIENT` by omission.

The current reconstruction method is routed through [the Git method](../Methods/YOUJO_SENKI_CHARACTER_MODELING_REFERENCE_METHOD.md), with original Drive provenance and the proposed authority transition documented by [the port audit](YOUJO_SENKI_CMR_PORT_AUDIT.md). Current coverage uses the distinct [readiness re-audit](YOUJO_SENKI_CHARACTER_READINESS_REAUDIT.md) and [supplement](YOUJO_SENKI_SUPPLEMENTARY_CHARACTER_READINESS.md); the [series entrypoint](../../CURRENT_STATE_AND_CORPUS_MAP.md) controls current routing. The original first-audit body below remains historical.

<!-- Preserved original CMR1 first-audit substantive body begins below. -->


# YOUJO SENKI CHARACTER RECONSTRUCTION READINESS AUDIT
## CMR-1 — alias control, coverage measurement, and first modeling-roster freeze

## 1. Status and conclusion

CMR-1 has completed its first production audit against the deterministic CMR-0 Japanese source layer.

The audit covers **20 recurring or analytically significant characters** selected from the governing CMR method and the mature V2 Imperial/counterperspective syntheses. It combines:

1. exact Japanese alias attestation against the CMR-0 locator index;
2. corpus-level quantitative retrieval proxies;
3. targeted primary-source reopening across high-stakes, low-stakes, internal, relational, and professional contexts;
4. the mature V2 character/relationship syntheses as secondary interpretive context;
5. conservative readiness classification under the v1.1 CMR method.

The central result is:

- **Tanya Degurechaff** clearly qualifies as `FULL_SPECTRUM` and remains the required first production model.
- **Erich von Lergen** also qualifies as `FULL_SPECTRUM`, with a narrower domestic/private-life evidence ceiling than Tanya but unusually broad professional, political, interpersonal, retrospective, and internal coverage.
- **Visha, Zettour, Weiss, Rudersdorf, Uger, Grantz, Drake, Mary Sue, Romel, Calandro, Loria, Conrad, de Lugo, Anson Sioux, and Schugel** qualify for `DOMAIN_BOUNDED` reconstruction at varying strengths.
- **Meybert, Tospan, and Josef** should remain `RECOGNITION_PROFILE` at this stage. Their source presence is sufficient for compatibility judgments and bounded traits, but not yet for unconstrained conversational generation.
- No character outside the audited roster is promoted automatically. Absence from this audit means **not yet audited**, not `INSUFFICIENT`.

This audit freezes the **first modeling roster**, not a permanent ceiling. Readiness may be upgraded or downgraded when speaker-attributed diagnostic indexing exposes stronger or weaker coverage than the CMR-0 proxies suggest.

---

# 2. Authority and inference rules

## 2.1 Primary authority

The original Japanese V01-V14 EPUB text controls exact wording, speech register, chronology, and source fact.

CMR-0 provides deterministic coordinates but does not infer speaker identity or motive.

## 2.2 Secondary analytical authority

The mature V2 corpus remains the interpretive authority for established characterization. CMR-1 uses especially:

- `02_TANYA_DEGURECHAFF_CHARACTER_DEEP_DIVE.md`;
- `03_IMPERIAL_PROFESSIONALS_RELATIONSHIPS_AND_COMMAND_CULTURE.md`;
- `04_COUNTERPERSPECTIVES_ENEMIES_ALLIES_AND_PARALLEL_PROFESSIONALS.md`.

These documents help distinguish meaningful recurrence from mere name frequency. They do not convert weak primary coverage into strong reconstruction readiness.

## 2.3 Quantitative-proxy warning

The companion metrics file is **not a speaker-count table**.

`mention_rows` means CMR-0 source blocks containing a controlled retrieval alias. A character's name may appear in narration or in another character's speech.

Likewise:

- `window_dialogue_pct` means that a dialogue/mixed block occurs within a small local window; it is not proof the candidate is speaking;
- `window_internal_proxy_pct` is lexical triage for thought/appraisal language, not proof of focalization;
- `window_low_stakes_proxy_pct` is coarse retrieval triage for food, rest, travel, family, hospitality, and similar material;
- co-character counts are local textual co-presence, not a finished relationship graph.

Final character models must use speaker-attributed, context-reviewed diagnostic scenes.

---

# 3. Canonical CMR-1 support artifacts

CMR-1 produces three machine/retrieval support artifacts alongside this audit:

- `YOUJO_SENKI_CHARACTER_ALIAS_MAP.tsv`
  - controlled source-attested Japanese aliases;
  - full-name, surname, nickname, title/address, and selected callsign forms;
  - source locator for each alias form;
  - retrieval-safety notes for ambiguous or state-bound aliases.

- `YOUJO_SENKI_CHARACTER_RECONSTRUCTION_READINESS_METRICS.tsv`
  - quantitative retrieval proxies for the 20-character audit roster;
  - volume/section spread, local dialogue/internal/low-stakes/context proxies, and co-character breadth.

- `YOUJO_SENKI_CMR1_READINESS_AUDIT_SCRIPT.py`
  - reproducible alias-attestation and quantitative-proxy implementation;
  - intentionally does **not** assign final readiness classes automatically.

The script was rerun against the canonical CMR-0 locator index and reproduced byte-identical alias-map and metrics outputs.

---

# 4. Corpus-level quantitative coverage

The following values are retrieval indicators only.

| Character | Alias-hit source blocks | Volumes | Distinct section routes | Local dialogue proxy | Internal-context proxy | Low-stakes proxy | Local co-character breadth |
|---|---:|---:|---:|---:|---:|---:|---:|
| Tanya Degurechaff | 6,738 | 14 | 90 | 90.7% | 57.5% | 12.4% | 19 |
| Hans von Zettour | 2,283 | 14 | 83 | 92.6% | 52.0% | 9.4% | 16 |
| Erich von Lergen | 1,133 | 14 | 66 | 92.2% | 53.0% | 9.9% | 14 |
| Matheus Johann Weiss | 1,058 | 13 | 63 | 96.6% | 57.4% | 13.8% | 13 |
| Viktoriya Serebryakov | 789 | 14 | 67 | 95.2% | 52.6% | 15.2% | 12 |
| Drake | 721 | 11 | 25 | 93.2% | 55.3% | 10.3% | 6 |
| Grantz | 716 | 13 | 50 | 92.7% | 53.1% | 9.1% | 11 |
| Kurt von Rudersdorf | 672 | 14 | 62 | 94.9% | 53.1% | 10.3% | 10 |
| Uger | 468 | 13 | 43 | 95.1% | 50.9% | 17.1% | 11 |
| Meybert | 330 | 10 | 29 | 93.6% | 49.4% | 5.5% | 9 |
| Loria | 331 | 8 | 17 | 84.6% | 54.1% | 5.7% | 6 |
| Calandro | 303 | 8 | 18 | 95.0% | 48.8% | 11.9% | 12 |
| Tospan | 233 | 10 | 29 | 92.7% | 47.6% | 9.9% | 9 |
| Conrad | 203 | 4 | 9 | 93.1% | 45.3% | 11.8% | 6 |
| Romel | 174 | 7 | 21 | 87.4% | 63.2% | 20.7% | 10 |
| Mary Sue | 154 | 9 | 15 | 79.9% | 65.6% | 15.6% | 4 |
| de Lugo | 84 | 3 | 7 | 63.1% | 76.2% | 13.1% | 5 |
| Schugel | 55 | 10 | 16 | 85.5% | 65.5% | 5.5% | 7 |
| Josef | 52 | 3 | 6 | 32.7% | 61.5% | 9.6% | 2 |
| Anson Sioux | 49 | 4 | 7 | 81.6% | 75.5% | 8.2% | 2 |

Raw mention totals are deliberately not converted into a numerical readiness score. The CMR method defines readiness qualitatively because context diversity, speaker certainty, developmental structure, and inference ceilings matter more than simple volume.

---

# 5. Readiness decisions

## 5.1 `FULL_SPECTRUM`

### Tanya Degurechaff — `FULL_SPECTRUM` — confidence `HIGH`

**Why she clears the threshold**

Tanya has an exceptional combination of:

- all-14-volume temporal spread;
- first-person/private cognition;
- multiple military roles and ranks;
- superior-facing, peer, subordinate, civilian, enemy, and metaphysical interaction;
- combat, staff, training, travel, meals, coffee, waiting, irritation, comfort-seeking, fatigue, praise, fear, anger, and relief;
- unusually explicit divergence between private motive and public presentation;
- mature secondary synthesis already separating stable engine from developmental change.

Representative primary anchors include:

- `YS-CMR0-V01-013-00003` — self-consciousness attached to the identity `ターニャ・デグレチャフ魔導少尉`;
- `YS-CMR0-V01-031-00116` — restaurant/social-professional encounter with Uger;
- `YS-CMR0-V02-021-00102` — coffee/comfort embedded in deployed life;
- CMR-0 provides thousands of later military, political, strategic, and low-stakes analogues.

**Reconstruction ceiling**

Broad behavioral and speech reconstruction is justified, provided developmental state and public/private distinction are preserved.

**Mandatory CMR-2 special audits**

- private cognition versus actual spoken wording;
- body/gender-salience events;
- attraction/non-attraction evidence, with orientation remaining `OPEN` unless the source supports stronger claims;
- food/coffee/hospitality/comfort evidence;
- no-shared-hierarchy professional-peer extrapolation;
- Being-X register isolated from ordinary professional speech.

---

### Erich von Lergen — `FULL_SPECTRUM` — confidence `MODERATE_HIGH`

Lergen is the only non-Tanya candidate in the first audit promoted to `FULL_SPECTRUM`.

Evidence includes:

- presence across all 14 volumes and 66 section routes;
- direct internal anxiety and judgment from the earliest volumes;
- staff, personnel, command, diplomacy, war-termination, covert action, and retrospective memoir contexts;
- multiple durable relationships: Tanya, Zettour, Rudersdorf, Uger, Conrad, Calandro, and broader political/military actors;
- social-professional scenes including meals, smoking, office interaction, travel, and diplomatic conversation;
- explicit retrospective first-person material in Volume 11: `YS-CMR0-V11-014-00001` / `00002` identifies the memoir author as `エーリッヒ・フォン・レルゲン` and grants unusually direct access to retrospective self-presentation.

Early evidence such as `YS-CMR0-V01-015-00287` through `00308` also gives private reaction, disgust, professional judgment, and observer anxiety rather than merely external description.

**Ceiling**

Broad professional-social reconstruction is supported. Domestic/intimate/private-life behavior beyond the source remains open and must not be invented merely because the overall class is `FULL_SPECTRUM`.

---

# 5.2 `DOMAIN_BOUNDED` — high-confidence candidates

### Viktoriya “Visha” Serebryakov — `DOMAIN_BOUNDED` — confidence `HIGH`

Source strengths:

- all 14 volumes / 67 section routes;
- direct first-person access beginning with `YS-CMR0-V01-023-00181` (`私、ヴィクトーリヤ...の朝は早い`);
- sustained dialogue and action inside the 203rd/Salamander environment;
- Tanya, Weiss, Grantz, unit personnel, local/cultural encounters, translation, care, and field logistics;
- meaningful ordinary deployed-life material, including coffee and physical hardship.

Why not `FULL_SPECTRUM` yet:

Her evidence remains disproportionately bound to military service and the Tanya-centered relational network. CMR-2/transfer sampling should test whether enough independently motivated, non-Tanya and low-stakes interaction exists to justify promotion.

**Approved model domain:** adjutant/subordinate professionalism, Tanya relationship, unit social life, translation/relational intelligence, combat/deployment, ordinary military downtime.

---

### Hans von Zettour — `DOMAIN_BOUNDED` — confidence `HIGH`

Source strengths:

- 2,283 alias-hit blocks, all 14 volumes, 83 section routes;
- extensive internal strategic reasoning and self-critique;
- Tanya, Rudersdorf, Lergen, Uger, Conrad, Calandro, and institutional audiences;
- staff meals, professional humor, mentorship, deception, defeat management, and late-series political authorship;
- `YS-CMR0-V01-029-00117` shows off-duty intellectual habit—remaining at his desk with philosophy after work;
- `YS-CMR0-V01-029-00146` exposes private moral shock at his own willingness to send a child to war;
- V05 and later provide explicit `ハンス・フォン・ゼートゥーア` self-address and internal judgment.

Why bounded:

The source is extraordinarily rich but overwhelmingly strategic/institutional. Ordinary domestic identity, intimate life, and nonprofessional social baseline remain thin.

**Approved model domain:** staff strategy, political-military judgment, mentoring, manipulation/indirection, professional meals/sociality, crisis authorship, defeat management.

---

### Matheus Johann Weiss — `DOMAIN_BOUNDED` — confidence `HIGH`

Strengths:

- 13 volumes / 63 routes;
- dense dialogue-associated presence;
- direct focalization and evaluative thought in multiple volumes;
- Tanya, Visha, Grantz, other subordinates, and combined-arms personnel;
- field command, deputy work, disagreement, loyalty, care, and practical low-stakes assistance;
- `YS-CMR0-V02-021-00066` gives mundane professional care: arranging a coat and coffee for Tanya;
- `YS-CMR0-V04-029-00119` gives Weiss's own expectation/judgment of Tanya.

Bound:

The model should remain military-relational. Civilian/private identity is weakly evidenced.

---

### Grantz — `DOMAIN_BOUNDED` — confidence `HIGH`

Strengths:

- 13 volumes / 50 routes;
- direct junior-officer POV and maturation;
- moral injury, combat adaptation, unit culture, peer/subordinate relations;
- unusually useful mundane soldier evidence: meals, train travel, rumors, coffee, night watch, nausea, rest;
- `YS-CMR0-V02-029-00463` and `YS-CMR0-V02-035-00252` are strong low-stakes/personhood anchors.

Bound:

Evidence strongly reconstructs the soldier/veteran, not an unconstrained civilian self.

---

### Uger — `DOMAIN_BOUNDED` — confidence `HIGH`

Strengths:

- 13 volumes / 43 routes;
- staff college through senior logistics/political-military work;
- Tanya, Zettour, Lergen, Rudersdorf and others;
- direct thought and strong moral/professional differentiation;
- family and human-cost sensitivity are explicitly important in the mature V2 synthesis;
- source anchors such as `YS-CMR0-V01-031-00108` give Uger-centered reflection, while V05 material differentiates his humorlessness and professional temperament.

Bound:

Best suited to logistics, staff work, family-aware professional judgment, and interprofessional conversation. Broader leisure/private-life simulation should remain cautious.

---

### Kurt von Rudersdorf — `DOMAIN_BOUNDED` — confidence `HIGH`

Strengths:

- all 14 volumes / 62 routes;
- operations, staff, Zettour partnership, Tanya, Lergen, political-military crisis;
- direct internal reactions and recurring decision style;
- limited but valuable mundane evidence, including food complaints and humor around the General Staff dining environment (`YS-CMR0-V02-015-00010` onward).

Bound:

The corpus overwhelmingly observes Rudersdorf as an operations professional. Model confidence should fall sharply in domestic/intimate or noninstitutional civilian settings.

---

### Drake — `DOMAIN_BOUNDED` — confidence `HIGH`

Strengths:

- 11 volumes / 25 routes;
- coalition command, Mary management, professional rivalry/respect, inter-allied politics, subordinate responsibility;
- strong internal access and speech;
- low-stakes stress behavior is explicitly attested: `YS-CMR0-V05-029-00031` has Drake reflecting on wartime alcohol use and the loss of enjoyable drinking;
- broader professional interaction includes Mikel, Johnson, Liliya, Mary, and coalition institutions.

Bound:

Excellent coalition-officer model; insufficient evidence for broad civilian/private reconstruction.

---

### Mary Sue — `DOMAIN_BOUNDED` — confidence `HIGH`

Strengths:

- 9 volumes / 15 routes;
- family, grief, voluntary enlistment, training, faith, justice, combat, coalition relationships;
- unusually high internal-context signal relative to raw coverage;
- ordinary/private anchors include family correspondence and free time (`YS-CMR0-V04-023-00383`).

Bound:

Mary must be reconstructed as a **developmental state machine**, not as one stable voice. Early family/grief state, training state, increasingly ideological state, and late escalation must remain distinct. The source does not provide an ordinary mature-adult baseline beyond the war trajectory.

---

### Calandro — `DOMAIN_BOUNDED` — confidence `HIGH`

Strengths:

- 8 volumes / 18 routes;
- intelligence, diplomacy, neutral-state calculation, professional sociality, Lergen, Zettour, Tanya, Ildoan leadership;
- source gives full form `ヴィルジニオ・カランドロ` at `YS-CMR0-V06-033-00366` and formal self-introduction at `YS-CMR0-V07-021-00198`;
- coffee, meals, humor, smiling deception, timing, and diplomatic politeness provide useful conversational texture.

Bound:

Strong diplomatic/intelligence/professional-social model; ordinary private life remains underdetermined.

---

### Loria — `DOMAIN_BOUNDED` — confidence `HIGH`

Strengths:

- 8 volumes / 17 routes;
- internal security, political integration, propaganda, coercion, war strategy, Josef relationship, and personal obsession;
- direct private desire and self-justification are unusually explicit;
- source clearly shows personal predation and strategic intelligence coexisting rather than one being inferred from the other.

Bound:

Model is reliable for security-state, political, strategic, coercive, and obsession-conditioned behavior. Do not extrapolate this into a generic everyday-social personality without source support.

---

# 5.3 `DOMAIN_BOUNDED` — narrower specialist candidates

### Romel — `DOMAIN_BOUNDED` — confidence `MODERATE_HIGH`

Seven-volume presence and strong field-command internal access support reconstruction of active defense, command improvisation, political-military frustration, and professional social interaction. `YS-CMR0-V04-013-00214` even gives a quiet coffee moment while waiting on events.

The model should remain centered on field command and the militarization of political judgment.

### Conrad — `DOMAIN_BOUNDED` — confidence `MODERATE_HIGH`

Only four volumes and nine section routes, but the late-series material is dialogue-dense and socially textured. He has diplomacy, policy translation, humor, argument, smoking/drinking sociality, Lergen, Zettour, and institutional reform.

Good candidate for **diplomatic/professional conversation**, not unconstrained full-life simulation.

### de Lugo — `DOMAIN_BOUNDED` — confidence `MODERATE`

Only three volumes / seven routes, but unusually direct internal access during national defeat and evacuation. `YS-CMR0-V03-019-00757` explicitly gives humiliation, anger, and command self-control; `YS-CMR0-V03-033-00165` adds weary political-office social texture over tea.

Reliable for defeat management, military-political command, evacuation, resistance continuity, and professional frustration.

### Anson Sioux — `DOMAIN_BOUNDED` — confidence `MODERATE`

Coverage is short but multidimensional: combat professionalism, fatherhood, marriage/family, faith, homeland, defeat, and direct interiority. `YS-CMR0-V02-023-00018` is especially valuable because it observes him as husband/father rather than only battlefield officer.

Reliable in the domains actually shown; not enough temporal spread for broad extrapolation.

### Adelheid von Schugel — `DOMAIN_BOUNDED` — confidence `MODERATE`

Only 55 alias-hit blocks, but the dialogue/behavior is highly distinctive and recurs across ten volumes. The source repeatedly establishes experimental obsession, technical brilliance, poor risk calibration, and a recognizable interaction style with Tanya and other professionals.

Reliable for engineering/test/lab/technical-administration scenarios. Ordinary social life beyond that remains mostly open.

---

# 5.4 `RECOGNITION_PROFILE`

### Meybert — `RECOGNITION_PROFILE` — confidence `MODERATE`

The surname appears across ten volumes, but much of the source presence is unit assignment, Tanya's evaluation, combined-arms coordination, or other characters referring to him. The mature synthesis supports a strong professional-trait claim—responsible initiative—but the current CMR-0 layer does not yet demonstrate enough independently speaker-attributed conversational breadth for free generation.

Use now for:

- compatibility checks;
- combined-arms/initiative judgments;
- limited professional responses.

Do not yet generate long casual dialogue.

### Tospan — `RECOGNITION_PROFILE` — confidence `MODERATE`

Similar to Meybert. The source gives repeated professional evaluation and some direct interaction across ten volumes, including visible development, but current evidence is too role-bound for open-ended voice reconstruction.

Use for professional compatibility and recognition, pending speaker-attributed extraction.

### Josef — `RECOGNITION_PROFILE` — confidence `MODERATE`

The character is analytically important but the textual presentation is heavily mediated through satirical propaganda diction (`ヨセフおじさん`), ideological narration, reports, and reactions of subordinates. Direct neutral conversational evidence is sparse.

A model can recognize regime-security logic, paranoia, ideological control, and the relationship with Loria. It should **not** fabricate a natural dinner-table or private conversational voice from propaganda-mediated narration.

---

# 6. First modeling-roster freeze

CMR-1 authorizes the following sequence.

## Tier A — production pilot

1. **Tanya Degurechaff — `FULL_SPECTRUM`**

CMR-2 must begin here.

## Tier B — first transfer tests after Tanya QA

2. **Erich von Lergen — `FULL_SPECTRUM`**
3. **Viktoriya Serebryakov — high `DOMAIN_BOUNDED`, promotion candidate**
4. **Hans von Zettour — high `DOMAIN_BOUNDED`**

These three deliberately test different evidence architectures:

- Lergen: broad professional/social/interior + retrospective self-presentation;
- Visha: relational/ordinary deployed life with less strategic abstraction;
- Zettour: enormous strategic/internal coverage with a narrower ordinary-life ceiling.

## Tier C — approved bounded models

- Weiss;
- Grantz;
- Uger;
- Rudersdorf;
- Drake;
- Mary Sue;
- Calandro;
- Loria;
- Romel;
- Conrad;
- de Lugo;
- Anson Sioux;
- Schugel.

These should be built only when their domain is useful. Their model headers must state the domain ceiling explicitly.

## Tier D — recognition only unless re-audited

- Meybert;
- Tospan;
- Josef.

No full generative profile should be created merely to complete a roster.

---

# 7. Alias-map findings that matter for later modeling

## 7.1 Tanya's name state is developmental

The source contains both:

- `ターニャ・デグレチャフ`;
- `ターニャ・フォン・デグレチャフ`.

The latter is post-ennoblement and should not be projected backward automatically.

Tanya also has state-bound callsigns including:

- `フェアリー08`;
- `ホークアイ03`;
- `ピクシー01`.

Callsign retrieval must respect era and unit context.

## 7.2 Visha has a stable nickname/full-name split

The source strongly supports both:

- `ヴィクトーリヤ・イヴァーノヴナ・セレブリャコーフ`;
- `ヴィーシャ`.

The nickname is relationally meaningful and should not simply replace the formal name in evidence normalization.

## 7.3 Lergen's full name is directly source-attested late

Volume 11 memoir material explicitly supplies `エーリッヒ・フォン・レルゲン`. Earlier volumes overwhelmingly use `レルゲン` plus rank.

## 7.4 Zettour's full form is strongly source-attested

`ハンス・フォン・ゼートゥーア` occurs directly in the Japanese source from Volume 5 onward.

## 7.5 Some V2 canonical English full labels are not equally explicit in the Japanese text

The governing method uses full labels such as **Kurt von Rudersdorf** and **Matheus Johann Weiss**, while the Japanese novel text normally retrieves them by `ルーデルドルフ` and `ヴァイス`.

The alias map therefore distinguishes:

- canonical analytical label;
- source-attested Japanese alias;
- name-authority note.

It does not manufacture a Japanese full name merely to make rows symmetrical.

---

# 8. CMR-2 handoff requirements for Tanya

CMR-2 should now build a source-verified Tanya diagnostic evidence pack rather than doing another broad literary reread.

Target scale remains roughly **250–350 genuinely diagnostic states**, with diversity more important than count.

Mandatory sampling axes:

1. internal cognition;
2. superior-facing speech;
3. subordinate command;
4. peer/professional discussion;
5. staff/intellectual work;
6. combat;
7. private/off-duty and low-stakes scenes;
8. food, coffee, hospitality, comfort, sleep/fatigue, travel, waiting, leave;
9. praise, embarrassment, irritation, fear, anger, relief, amusement;
10. Being-X interaction isolated as its own register;
11. body/gender-salience evidence;
12. attraction/non-attraction evidence without assuming orientation from the former salaryman's sex;
13. no-shared-hierarchy professional-peer analogues for later crossover extrapolation.

Every high-value speech row should distinguish, where evidence exists:

> `private appraisal -> withheld private content -> communicative objective -> speech act -> relationship/role constraint -> register -> surface wording`

Unknown fields remain unknown.

---

# 9. Revision triggers

Re-audit a character if any of the following occur:

- speaker attribution during CMR-2/CMR-5 shows that apparent dialogue density was mostly other people referring to the character;
- a targeted low-stakes pass materially expands ordinary-life evidence;
- additional Japanese volumes enter the canonical source boundary;
- an alias proves ambiguous enough to contaminate counts;
- a character receives new source material that broadens relationships or developmental states;
- held-out QA demonstrates that the assigned class permits systematic over-extrapolation.

Possible transitions are:

- `STRENGTHEN` — same class, stronger evidence;
- `REVISE` — domain ceiling changes;
- `DOWNGRADE` — class was too permissive;
- `OPEN` — unresolved pending more evidence.

---

# 10. CMR-1 completion state

For the current V01-V14 source lock:

- controlled alias map: **complete for the 20-character audited roster**;
- quantitative readiness metrics: **complete and reproducible**;
- qualitative readiness audit: **complete first production pass**;
- first modeling roster: **frozen for CMR-2/Tanya and initial transfer sequence**;
- CMR-2 Tanya diagnostic evidence pack: **NEXT**.

CMR-1 remains `active_provisional` because later speaker-attributed extraction may revise individual readiness ceilings. This does not block CMR-2.
