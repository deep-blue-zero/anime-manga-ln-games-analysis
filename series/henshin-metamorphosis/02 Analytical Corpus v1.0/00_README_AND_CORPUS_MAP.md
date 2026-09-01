---
title: "変身 / Henshin — Definitive Second-Pass Synthesis: README and Corpus Map"
artifact_type: "reader_orientation_and_corpus_map"
version: "1.0"
release_status: "immutable archival release"
release_date: "2026-08-12"
work: "変身 / Henshin / Metamorphosis / Emergence"
creator: "ShindoL / 新堂エル"
primary_language: "Japanese"
primary_source_sha256: "a1107584fbd3f0fab93b485299af82ed9e1f53a10cb49ffeac55813714e3416e"
governing_method: "REFERENCE_HENSHIN_ANALYTICAL_METHOD_V2.md"
governing_architecture: "REFERENCE_HENSHIN_MULTI_DOCUMENT_SYNTHESIS_ARCHITECTURE.md"
spoiler_status: "complete work spoilers"
---

# 『変身』 / *Henshin* — Definitive Second-Pass Synthesis
## README and Corpus Map

This directory is the definitive v1.0 archival release of the Japanese-primary second-pass analysis of ShindoL's 『変身』, also known in English as *Metamorphosis* or *Emergence*.

The corpus was produced by reading the Japanese collected edition sequentially, freezing each chapter's local interpretive state before later events were permitted to revise the retrospective interpretation, then building longitudinal ledgers, specialist full-work documents, a claim-routing evidence layer, and finally a continuous reader-facing synthesis.

The project is designed around one central archival principle:

> **Later knowledge may revise the current full-work interpretation, but it must not silently rewrite what an earlier chapter allowed the reader or Saki herself to know at that point.**

Accordingly, this release contains both immutable prospective chapter artifacts and retrospective full-work analyses.

---

# 1. Primary Japanese source

The governing primary source is the Japanese collected-edition CBZ:

- `Henshin -emergence-.cbz`
- SHA-256: `a1107584fbd3f0fab93b485299af82ed9e1f53a10cb49ffeac55813714e3416e`
- 251 WEBP images
- filename/printed-page sequence: front matter `P00A-P00C`, then `P001-P248`

The source CBZ is **not redistributed** in this analytical release.

The stable page locator used throughout the corpus is:

```text
JP_CBZ_IMG_####
```

When useful, this is paired with the printed page:

```text
JP_CBZ_IMG_0010 / printed p.007
```

The source and page mapping are documented in:

- `SOURCE_INVENTORY.md`
- `SOURCE_CHECKSUMS.sha256`
- `support/LOCATOR_MAP.md`
- `support/JAPANESE_PASSAGE_INDEX.md`
- `support/VISUAL_LOCATOR_INDEX.md`

---

# 2. Comparative English source status

The earlier project analysis was conducted substantially through English-language material and survives primarily as an analytical transcript/hypothesis archive rather than as a complete line-addressable English edition inside this release.

The Japanese second pass therefore uses the English work in a deliberately subordinate role:

1. Japanese text and manga form govern wording, causality, speech acts, agency, and visual evidence.
2. Earlier English analysis is treated as a **first-pass hypothesis archive**.
3. Where an English formulation is recoverable with sufficient precision, Document 05 evaluates whether Japanese preserves, sharpens, complicates, or changes it.
4. Where an exact English line is not reliably preserved, the corpus records the Japanese translation risk without inventing a supposed published English wording.

The principal comparative artifacts are:

- `05_JAPANESE_VOICE_DIALOGUE_AND_TRANSLATION_AUDIT.md`
- `HENSHIN_FIRST_PASS_CLAIM_REVISION_LEDGER.md`
- `08_EVIDENCE_LOCATOR_AND_CLAIM_REVISION_LEDGER.md`

The final first-pass revision inventory records:

- **122 `STRENGTHENED` claims**;
- **16 `NEWLY_VISIBLE_IN_JAPANESE` claims**;
- **12 `COMPLICATED` claims**;
- **9 `STILL_UNDERDETERMINED` claims**;
- **0 load-bearing claims fully overturned**.

This does not mean the Japanese second pass merely confirmed the first pass. Its largest gain was precision: refusal, kinship resistance, option contraction, obedience, ownership, market value, belonging, disposal, self-blame, and rebirth all became materially more auditable in the original language.

---

# 3. First-pass analysis status

The older English-led analysis is not discarded. It is preserved conceptually as a historical first pass and tested claim by claim against the Japanese reread.

The definitive corpus therefore distinguishes:

- `FP` — first-pass claim;
- `RC` — retrospective correction or refinement;
- current Japanese-primary synthesis.

The root-level `HENSHIN_FIRST_PASS_CLAIM_REVISION_LEDGER.md` is the exhaustive comparative record. Document 08 then routes the most important mature claims back through chapter freezes, evidence IDs, Japanese passages, visual locators, and revision status.

The first-pass archive is a **hypothesis source**, not a coequal primary text.

---

# 4. Chapter structure and prospective reading states

The collected edition is divided as follows:

| Unit | Original serialization | Printed pages | CBZ image range |
|---|---|---:|---|
| Chapter 1 | `COMIC X-EROS #09` | 003-030 | `JP_CBZ_IMG_0006-0033` |
| Chapter 2 | `COMIC X-EROS #14` | 031-060 | `JP_CBZ_IMG_0034-0063` |
| Chapter 3 | `COMIC X-EROS #18` | 061-090 | `JP_CBZ_IMG_0064-0093` |
| Chapter 4 | `COMIC X-EROS #25 + 描き下ろし` | 091-126 | `JP_CBZ_IMG_0094-0129` |
| Chapter 5 | `COMIC X-EROS #29` | 127-166 | `JP_CBZ_IMG_0130-0169` |
| Chapter 6 | `COMIC X-EROS #38` | 167-202 | `JP_CBZ_IMG_0170-0205` |
| Finale | `COMIC X-EROS #41` | 203-248 collected unit | `JP_CBZ_IMG_0206-0251` |

For the Finale, the source boundary was corrected during the second pass:

- narrative Finale: printed pp.203-242;
- p.243: ShindoL afterword;
- p.244: publication/colophon material;
- pp.245-248: separate Melonbooks bonus leaflet.

The narrative Finale is therefore frozen before the afterword is allowed to settle authorial-intent questions.

The immutable prospective artifacts are in `chapters/`.

The two retained prospective checkpoints are:

- `HENSHIN_MIDPOINT_AUDIT_AFTER_CH03.md`
- `HENSHIN_PRE_FINALE_AUDIT_AFTER_CH06.md`

The explicitly temporary `HENSHIN_MIDPOINT_AUDIT_WORKING_LEDGER.md` from the historical workspace is intentionally omitted from the v1.0 release because its function was superseded by the frozen midpoint audit and final longitudinal ledgers.

---

# 5. Evidence classification

The corpus uses the following evidence labels:

| Label | Meaning |
|---|---|
| `TF` | textual fact |
| `VF` | visual fact |
| `CB` | character belief |
| `SI` | strong inference |
| `TI` | thematic interpretation |
| `EI` | ethical interpretation |
| `GI` | genre/form inference |
| `LI` | linguistic interpretation |
| `TR` | translation-relevant observation |
| `RC` | retrospective correction |
| `FP` | first-pass claim |
| `UA` | unresolved ambiguity |
| `SP` | speculation |

Confidence may additionally be marked `HIGH`, `MEDIUM`, or `LOW` where useful.

The governing discipline is that a persuasive synthesis claim must not be upgraded into source fact merely because it recurs across documents.

Examples:

- Saki's repeated `しか…ない` constructions are textual facts; reading them as a grammar of perceived option collapse is linguistic/thematic interpretation.
- The narrative ending makes Saki's death a very strong inference; p.243 retrospectively confirms intended death at the authorial level.
- Protective institutions are visibly absent from the depicted chain; the claim that meaningful intervention was impossible would exceed the evidence.
- Reader structural implication is strongly supported; deliberate authorial indictment of the reader remains unresolved.

---

# 6. Agency classification

The project treats agency, preference, consent, material capacity, and authorship as distinct variables.

The analytical agency taxonomy is:

```text
A1_AUTONOMOUS
A2_UNEQUAL_BUT_VOLUNTARY
A3_PRESSURED
A4_DEPENDENCY_SHAPED
A5_IMPAIRED
A6_BARGAINING_WITHIN_COERCION
A7_MATERIALLY_CONSTRAINED
A8_MANIPULATIVELY_ENGINEERED
A9_EXPLICITLY_COERCED
A10_NON_CHOICE
UA_UNRESOLVED
```

These labels are analytical, not legal conclusions.

For each major decision, the corpus asks separately:

- What does Saki physically do?
- What does she verbally agree to?
- What does she positively want?
- What does she believe will happen?
- What alternatives does she perceive?
- What alternatives objectively exist?
- Which alternatives are realistically accessible?
- What dependencies structure the decision?
- Who controls relevant information?
- Who authored the decision environment?

This distinction is central to the final reading. Saki often retains or even improves tactical competence while losing strategic authorship over the environment in which that competence is exercised.

Primary homes:

- `03_AGENCY_CONSENT_DEPENDENCY_AND_DECISION_ENVIRONMENT_AUTHORSHIP.md`
- `ledgers/HENSHIN_AGENCY_CONSENT_AND_DECISION_ENVIRONMENT_LEDGER.md`

---

# 7. Naming and romanization

This release uses:

- **Yoshida Saki / 吉田咲** as the protagonist's full name where formal identification is useful;
- **Saki** in ordinary analysis;
- **Hayato / ハヤト**;
- **Obata / 小幡**;
- **ShindoL / 新堂エル** for the creator.

The work is referenced primarily as:

- 『変身』 / *Henshin*;

with *Metamorphosis* and *Emergence* retained as common English titles where useful for retrieval.

Japanese phrases are preserved when their exact form carries analytical force. Translation is supplied selectively rather than replacing the Japanese evidence.

---

# 8. Content and scope note

This corpus analyzes an explicit adult manga whose protagonist is a high-school-age minor for much of the work. It includes sexual exploitation, coercion, substance use, family abuse, pregnancy, homelessness, severe violence, and probable suicide/overdose.

The analytical artifacts therefore discuss sexual material **non-graphically**, with emphasis on:

- agency and refusal;
- coercion;
- decision environments;
- money and material dependence;
- substances;
- reader position;
- visual framing;
- consequences;
- literary and ethical structure.

Bodily response is never treated as equivalent to consent.

The project does not identify the drug pharmacologically because the manga does not name it. It also does not assign a formal clinical diagnosis where the source does not provide one.

---

# 9. Mature full-work thesis

The mature second-pass thesis is:

> **『変身』 begins with a girl deliberately remaking her appearance because she wants the social world finally to recognize her. Its tragedy is not that transformation itself is corrupting. The tragedy is that recognition progressively becomes a mechanism through which other people acquire authorship over the conditions and meanings of Saki's life. She remains a continuous desiring, relationally sensitive subject even while her social, economic, chemical, sexual, and bodily autonomy deteriorate. The work converts pornographic scenario taxonomy into cumulative causal chronology, but never fully escapes the ethical contradiction of asking the reader to mourn the objectification and exploitation of a person whose body it continues to make erotically consumable.**

The continuous synthesis sharpens the visibility arc as:

> **invisibility → desired visibility → portable visibility → hyper-visibility without causal control → visibility without obligation.**

By the end, Saki is not unseen. She is repeatedly seen as body, reputation, homelessness, pregnancy, cash, injury, or social category without being recognized as a causal person whose history generates obligations in others.

The final title-level movement is:

> `変わりたい` — I want to change  
> → change for Hayato  
> → `この子のために…変わってみせる` — I will change for this child  
> → `生まれ変われた` — I was able to be reborn.

The final imagined metamorphosis is therefore not cosmetic, sexual, commercial, or chemical. It is survival long enough for suffering to become biography rather than permanent present.

The corpus's final ethical classification is:

> **an ethically compromised cumulative pornographic tragedy.**

The tragedy meaningfully transforms pornographic scenarios into biography and preserves Saki's personhood, but it does not retroactively redeem every erotic use of coercion, impairment, destitution, or reproductive vulnerability.

---

# 10. Document map

## Reader-facing entry point

### `HENSHIN_FULL_WORK_SYNTHESIS.md`

The preferred single-document reading.

A continuous literary argument from Saki's initial `変わりたい` through the inaccessible `生まれ変われた` future. It draws on the whole specialist/evidence corpus without reproducing its modular structure.

## Specialist full-work documents

### `01_NARRATIVE_ARCHITECTURE_SERIALIZATION_AND_CAUSAL_PROGRESSION.md`

Primary home for chronology, serialization structure, causal accumulation, pornographic reset refusal, future-horizon contraction, and the misery-machine stress test.

### `02_YOSHIDA_SAKI_TRANSFORMATION_IDENTITY_AND_CONTINUITY.md`

Primary home for Saki's psychology, personhood, continuity, adaptation, changing self-conception, and the distinction between transformation capacity and transformation authorship.

### `03_AGENCY_CONSENT_DEPENDENCY_AND_DECISION_ENVIRONMENT_AUTHORSHIP.md`

Primary home for action versus preference versus consent, scalar coercion, tactical agency, strategic authorship, material alternatives, and dependency-shaped decision environments.

### `04_RELATIONSHIPS_EXPLOITATION_FAILED_CARE_AND_INSTITUTIONAL_ABSENCE.md`

Primary home for family, peers, Hayato, clients, Obata's network, exploitative care, social contraction, and protective institutional presence/absence.

### `05_JAPANESE_VOICE_DIALOGUE_AND_TRANSLATION_AUDIT.md`

Primary home for Saki's Japanese voice, recurring grammar, address/register, refusal language, ownership, `しか…ない`, `言うこと / 言うとおり`, `価値`, `居場所`, disposal vocabulary, and translation-sensitive revision.

### `06_VISUAL_FORM_EROMANGA_GRAMMAR_GAZE_AND_READER_POSITION.md`

Primary home for visual subject/object oscillation, framing, body fragmentation, photography/screens, eromanga grammar, the reader's privileged causal position, the Hana park, and the final still life.

### `07_TRAGEDY_ETHICS_FATALISM_AND_FULL_WORK_SYNTHESIS.md`

Primary home for ethical adjudication, fatalism, culpability, motherhood, responsibility, pornographic/tragedy coexistence, and diegetic contingency versus authorial predetermination.

### `08_EVIDENCE_LOCATOR_AND_CLAIM_REVISION_LEDGER.md`

Primary reader-facing traceability layer. Routes mature claims backward through specialist ownership, chapter freezes, evidence IDs, Japanese passages, visual locators, agency states, and first-pass revision status.

## Chapter-local prospective corpus

Directory: `chapters/`

- `HENSHIN_CH01_DEEP_READING.md`
- `HENSHIN_CH02_DEEP_READING.md`
- `HENSHIN_CH03_DEEP_READING.md`
- `HENSHIN_CH04_DEEP_READING.md`
- `HENSHIN_CH05_DEEP_READING.md`
- `HENSHIN_CH06_DEEP_READING.md`
- `HENSHIN_FINALE_DEEP_READING.md`
- `HENSHIN_MIDPOINT_AUDIT_AFTER_CH03.md`
- `HENSHIN_PRE_FINALE_AUDIT_AFTER_CH06.md`

These preserve local chapter truth and should not be silently revised using later knowledge.

## Longitudinal ledgers

Directory: `ledgers/`

- `HENSHIN_SAKI_STATE_LEDGER_FINAL.md`
- `HENSHIN_AGENCY_CONSENT_AND_DECISION_ENVIRONMENT_LEDGER.md`
- `HENSHIN_RELATIONSHIP_AND_EXPLOITATION_LEDGER.md`
- `HENSHIN_SUBSTANCE_MONEY_AND_MATERIAL_SECURITY_LEDGER.md`
- `HENSHIN_INSTITUTIONAL_PRESENCE_AND_ABSENCE_LEDGER.md`
- `HENSHIN_JAPANESE_VOICE_LEDGER.md`
- `HENSHIN_VISUAL_SUBJECT_OBJECT_AND_READER_POSITION_LEDGER.md`

These are the cross-chapter state memory of the project.

## First-pass revision

- `HENSHIN_FIRST_PASS_CLAIM_REVISION_LEDGER.md`

This preserves the historical comparison between the English-led first pass and the Japanese-primary reread.

## Evidence and retrieval support

Directory: `support/`

- `CORPUS_INDEX.json` — machine-readable file metadata and checksums;
- `CLAIM_ROUTE_INDEX.json` — machine-readable mature-claim routes;
- `LOCATOR_MAP.md` — source/page mapping;
- `JAPANESE_PASSAGE_INDEX.md` — key language anchors;
- `VISUAL_LOCATOR_INDEX.md` — key formal/visual anchors.

## Governing references

- `REFERENCE_HENSHIN_ANALYTICAL_METHOD_V2.md`
- `REFERENCE_HENSHIN_MULTI_DOCUMENT_SYNTHESIS_ARCHITECTURE.md`

These preserve the method under which the corpus was generated.

## Release administration

- `CORPUS_MANIFEST.md`
- `SOURCE_INVENTORY.md`
- `SOURCE_CHECKSUMS.sha256`
- `ARTIFACT_CHECKSUMS.sha256`
- `DELIVERY_AUDIT.md`

---

# 11. Recommended reading paths

## A. Chronological / reconstruct the second pass

1. `chapters/HENSHIN_CH01_DEEP_READING.md`
2. `chapters/HENSHIN_CH02_DEEP_READING.md`
3. `chapters/HENSHIN_CH03_DEEP_READING.md`
4. `chapters/HENSHIN_MIDPOINT_AUDIT_AFTER_CH03.md`
5. `chapters/HENSHIN_CH04_DEEP_READING.md`
6. `chapters/HENSHIN_CH05_DEEP_READING.md`
7. `chapters/HENSHIN_CH06_DEEP_READING.md`
8. `chapters/HENSHIN_PRE_FINALE_AUDIT_AFTER_CH06.md`
9. `chapters/HENSHIN_FINALE_DEEP_READING.md`
10. `HENSHIN_FULL_WORK_SYNTHESIS.md`

Use this route to reproduce the project's strongest anti-hindsight discipline.

## B. Saki character / identity / continuity

1. `HENSHIN_FULL_WORK_SYNTHESIS.md`
2. `02_YOSHIDA_SAKI_TRANSFORMATION_IDENTITY_AND_CONTINUITY.md`
3. `ledgers/HENSHIN_SAKI_STATE_LEDGER_FINAL.md`
4. `05_JAPANESE_VOICE_DIALOGUE_AND_TRANSLATION_AUDIT.md`
5. `ledgers/HENSHIN_JAPANESE_VOICE_LEDGER.md`

## C. Agency / consent / coercion / choice

1. `03_AGENCY_CONSENT_DEPENDENCY_AND_DECISION_ENVIRONMENT_AUTHORSHIP.md`
2. `ledgers/HENSHIN_AGENCY_CONSENT_AND_DECISION_ENVIRONMENT_LEDGER.md`
3. `04_RELATIONSHIPS_EXPLOITATION_FAILED_CARE_AND_INSTITUTIONAL_ABSENCE.md`
4. `08_EVIDENCE_LOCATOR_AND_CLAIM_REVISION_LEDGER.md`

## D. Exploitation / relationships / institutions

1. `04_RELATIONSHIPS_EXPLOITATION_FAILED_CARE_AND_INSTITUTIONAL_ABSENCE.md`
2. `ledgers/HENSHIN_RELATIONSHIP_AND_EXPLOITATION_LEDGER.md`
3. `ledgers/HENSHIN_INSTITUTIONAL_PRESENCE_AND_ABSENCE_LEDGER.md`
4. `ledgers/HENSHIN_SUBSTANCE_MONEY_AND_MATERIAL_SECURITY_LEDGER.md`
5. `01_NARRATIVE_ARCHITECTURE_SERIALIZATION_AND_CAUSAL_PROGRESSION.md`

## E. Japanese language / translation

1. `05_JAPANESE_VOICE_DIALOGUE_AND_TRANSLATION_AUDIT.md`
2. `ledgers/HENSHIN_JAPANESE_VOICE_LEDGER.md`
3. `support/JAPANESE_PASSAGE_INDEX.md`
4. `HENSHIN_FIRST_PASS_CLAIM_REVISION_LEDGER.md`

## F. Visual/formal / gaze / eromanga

1. `06_VISUAL_FORM_EROMANGA_GRAMMAR_GAZE_AND_READER_POSITION.md`
2. `ledgers/HENSHIN_VISUAL_SUBJECT_OBJECT_AND_READER_POSITION_LEDGER.md`
3. `support/VISUAL_LOCATOR_INDEX.md`
4. `07_TRAGEDY_ETHICS_FATALISM_AND_FULL_WORK_SYNTHESIS.md`

## G. Ethics / tragedy / fatalism

1. `07_TRAGEDY_ETHICS_FATALISM_AND_FULL_WORK_SYNTHESIS.md`
2. `HENSHIN_FULL_WORK_SYNTHESIS.md`
3. `01_NARRATIVE_ARCHITECTURE_SERIALIZATION_AND_CAUSAL_PROGRESSION.md`
4. `06_VISUAL_FORM_EROMANGA_GRAMMAR_GAZE_AND_READER_POSITION.md`
5. `08_EVIDENCE_LOCATOR_AND_CLAIM_REVISION_LEDGER.md`

## H. Audit a specific mature claim

1. Find the claim in `08_EVIDENCE_LOCATOR_AND_CLAIM_REVISION_LEDGER.md`.
2. Follow its specialist primary home.
3. Consult the identified chapter freeze/checkpoint.
4. Use the evidence ID and Japanese/visual index.
5. Return to the original Japanese page using `JP_CBZ_IMG_####` if the source is available.

---

# 12. Traceability standard

The definitive archival chain is:

> **continuous/full-work synthesis claim**  
> → **specialist analytical home**  
> → **longitudinal ledger or prospective checkpoint**  
> → **chapter artifact**  
> → **evidence ID**  
> → **Japanese passage and/or visual locator**  
> → **original CBZ page**

This is the preferred verification path for any future quotation, comparative character analysis, ethical argument, or cross-work synthesis using this corpus.

`08_EVIDENCE_LOCATOR_AND_CLAIM_REVISION_LEDGER.md` is the primary human-readable routing layer.

`support/CLAIM_ROUTE_INDEX.json` and `support/CORPUS_INDEX.json` provide machine-readable retrieval support.

---

# 13. Residual ambiguity notice

The second pass substantially stabilizes the work's character, causal, linguistic, and formal architecture, but the release deliberately leaves several questions unresolved.

## Exact drug identity

The manga never provides sufficient pharmacological identification. Descriptions of stimulant-like effects or dependence may support speculation, but **no exact substance is canonical in this corpus**.

## Clinical diagnosis

The text strongly supports severe dependence-like substance use and withdrawal-like distress. This corpus does not assign a clinical diagnosis that the work itself does not establish.

## Reader indictment

The reader is structurally implicated because the manga gives privileged causal knowledge while simultaneously offering eroticized visual access to Saki. The corpus does **not** claim that ShindoL demonstrably intended a moral indictment of the reader.

## Institutional possibility

Protective institutions are strikingly absent from the depicted chain, especially late in the work. The corpus does not infer that no intervention could realistically have existed.

## Motherhood and self-worth

The Chapter 6 pregnancy project is a genuine restoration of strategic authorship and long-term futurity. It remains unresolved whether this represents fully restored self-authorship or another externally organized telos, because Saki still defines transformation in relation to another person rather than explicitly saying her own life is sufficient reason to survive.

## Finale death status

Within the narrative pages alone, death following the final self-destructive drug use is a very strong inference rather than clinically depicted fact. ShindoL's afterword then confirms retrospectively that he intended the heroine ultimately to die. These two evidence levels remain separate.

## Mirror and glasses

The late mirror/glasses sequence is intentionally polyvalent. The corpus preserves possible readings involving earlier Saki, continuity, failed restoration, self-rejection, and death marking rather than assigning one exclusive symbolism.

## Pornography and tragedy

The final ethical classification remains intentionally non-reductive:

> **The work's tragedy genuinely converts scenario into biography and preserves Saki's personhood, but does not thereby purify or redeem every pornographic mechanism through which her suffering is presented.**

That unresolved contradiction is not a gap the v1.0 release attempts to eliminate. It is one of the work's most important final properties.

---

# Archival release policy

This v1.0 directory is the immutable release state of the second-pass synthesis.

The historical mutable workspace remains separate and contains earlier tranche manifests, delivery audits, and temporary working artifacts. Those are intentionally excluded here when superseded.

Corrections or substantial new scholarship should be released as a new version such as **v1.1** rather than silently mutating v1.0.

The primary manga source is never redistributed with the analytical archive.
