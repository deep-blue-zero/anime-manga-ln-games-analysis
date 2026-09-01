---
series: OPM
series_title: "One Punch Man"
series_title_jp: "ワンパンマン"
artifact_type: analytical_method
scope: "Manga V2; Japanese tankobon V01-current plus official uncollected web serialization"
generation: V2
status: active_provisional
source_boundary: "Open-ended; collected manga through the latest locked Japanese tankobon, with a separately governed active-provisional current-release layer"
supersedes: null
superseded_by: null
do_not_use_as_current_authority: false
created: 2026-08-15
last_amended: 2026-08-23
---

# One Punch Man — Analytical Method V2
## Japanese-manga sequential deep reading for a long, revised, and still-publishing work

## 1. Purpose

This method governs a second-pass deep reading of the manga version of *One Punch Man* by ONE and Murata Yusuke.

The project is not a continuation of the earlier broad synthesis. It is a new source-grounded analytical generation whose central task is to re-read the manga sequentially from Volume 1, preserve volume-local ambiguity, use later knowledge without flattening earlier uncertainty, and build an evidence architecture capable of continuing for years while the manga remains in publication.

The earlier corpus through Volume 34 remains valuable. It contains strong series-level theses and substantial character work on Saitama, Genos, Garou, King, Tatsumaki, Bang, institutions, satire, recognition, power, monsterhood, and related subjects. In V2, however, those documents are treated as **legacy interpretive inputs and claim candidates**, not as primary evidence and not as automatic current authority.

The V2 project should answer four different questions without collapsing them into one:

1. **What does this volume establish at its own publication boundary?**
2. **What does later manga material cause us to notice differently in that earlier volume?**
3. **Which claims from the earlier analysis survive source-grounded rereading?**
4. **What is the current state of the still-publishing manga, including material not yet stabilized in tankobon form?**

The governing principle is:

> **Read sequentially, preserve uncertainty, separate collected canon from provisional current release, and make every mature claim traceable back to a specific Japanese manga source.**

---

# 2. Why One Punch Man needs a specialized V2 method

A generic volume-by-volume manga protocol is insufficient for *One Punch Man* for five reasons.

## 2.1 Length and ensemble scale

The manga has dozens of tankobon volumes, a very large recurring ensemble, several major institutions, multiple overlapping power systems, long-running mysteries, and arcs whose consequences span many years of publication.

A useful corpus therefore cannot depend on a single giant synthesis. It needs sequential readings plus longitudinal state tracking.

## 2.2 The protagonist breaks ordinary battle-manga structure

Saitama cannot be analyzed only through conventional progression. Much of the dramatic work is displaced onto the supporting cast. V2 must therefore track both:

- Saitama's post-growth existential and relational development; and
- the conventional growth, defeat, recognition, rivalry, mentorship, trauma, institutional, and ideological arcs inherited by the ensemble.

The V1 insight that “Saitama breaks genre, so the supporting cast inherits genre” should be treated as a claim to be tested repeatedly, not a premise that may never be questioned.

## 2.3 The manga is visually constitutive

Murata's page design is not decorative support for plot. Scale, speed, panel density, splash pages, facial simplification, detailed anatomical rendering, page turns, negative space, reaction timing, grotesquerie, environmental destruction, and shifts between hyper-rendered spectacle and flat gag abstraction are part of the argument.

A V2 reading that extracts dialogue while neglecting manga form would miss a large fraction of the work.

## 2.4 Web serialization and tankobon are not one stable text stream

*One Punch Man* has a strong history of revised, replaced, redrawn, reordered, or otherwise unstable web material before book collection. The official web publication/update identifiers also do not map cleanly onto tankobon `撃目` numbering.

Therefore V2 must maintain a formal crosswalk among:

- official web update identifier;
- web publication date;
- narrative chapter label if present;
- collected tankobon chapter number;
- tankobon volume;
- revision/replacement state;
- page-level differences where material changed.

Never infer a tankobon chapter number by arithmetic from a web update number.

## 2.5 The series is ongoing

There is no legitimate “definitive full-series synthesis” while the manga is still publishing. V2 needs a rolling current state, periodic frozen boundary releases, and a way to ingest new web material without rewriting the entire corpus every two weeks.

---

# 3. Source hierarchy and authority

## Tier A — Japanese tankobon: canonical collected authority

For all material collected in a Japanese tankobon, the locked Japanese tankobon is the governing primary source.

Each source object should record at minimum:

- volume number;
- exact filename;
- format;
- edition if known;
- page/image count;
- chapter table of contents;
- SHA-256 when locally available;
- acquisition/provenance note;
- integrity status.

When tankobon material differs from an earlier web version, the tankobon governs **current collected continuity** unless the project has evidence of a later official correction.

Earlier web material may still be important as revision history.

## Tier B — official Tonari no Young Jump serialization: active provisional authority

Official web releases are authoritative for **currently uncollected manga material**, but their status is `active_provisional`.

They should be analyzed seriously, but never merged silently into a frozen tankobon reading.

Every saved web installment should record:

- provider and series;
- provider episode/update ID;
- displayed web label;
- publication date;
- retrieval date;
- source snapshot/hash where possible;
- relation to prior version;
- whether it is main narrative, extra, alternate manuscript, or other category;
- current replacement/supersession state.

## Tier C — replaced or superseded official web versions: historical revision evidence

If a web installment is replaced or materially redrawn, preserve the earlier version when lawfully available and analytically relevant.

It is not current continuity authority once superseded, but it may reveal:

- changes in characterization;
- altered pacing;
- revised causality;
- changed visual emphasis;
- removed dialogue;
- reordered reveals;
- altered power depiction;
- editorial or authorial reconsideration.

These differences belong in the `VISUAL_FORM_REDRAW_AND_REVISION_LEDGER`, not in a vague note that “the chapter was redrawn.”

## Tier D — official translations

Official English or other translations may be used for comparative or localization analysis, but the Japanese manga remains primary.

Do not ground Japanese voice claims in an English localization.

## Tier E — ONE webcomic

ONE's original webcomic is a distinct continuity/source layer.

Unless the project explicitly opens a cross-continuity phase, it is **comparative evidence only**. Do not import webcomic reveals, chronology, characterization, or outcomes into the Murata manga as if they were already manga facts.

## Tier F — anime and other adaptations

Anime, OVAs, games, guidebooks, interviews, promotional material, and other adaptations are secondary or paratextual unless separately source-locked for a specific comparative task.

## Tier G — V1 analysis

The existing analysis through Volume 34 is historical/legacy analysis.

It is useful for:

- claim recovery;
- comparison;
- identifying promising themes;
- detecting what earlier reading overemphasized or missed;
- comparative-analysis continuity.

It must never substitute for a primary-source locator in V2.

---

# 4. Two-horizon reading model

Every canonical V2 volume reading should maintain two explicitly separated interpretive horizons.

## Horizon 1 — publication-boundary reading

Ask what a reader could responsibly conclude **through that volume only**.

This section should preserve:

- uncertainty;
- false leads;
- ambiguous identities;
- unresolved motives;
- incomplete institutional knowledge;
- plausible competing explanations.

Do not erase uncertainty merely because later volumes answer the question.

## Horizon 2 — retrospective recontextualization

After the publication-boundary reading is complete, a separate section may ask what the current full corpus causes us to notice differently.

Examples of appropriate retrospective questions include:

- Does a seemingly comic early behavior later become a stable personality marker?
- Does an institutional joke later reveal a systemic defect?
- Does early imagery acquire significance once God, Blast, the Organization, Neo Heroes, or another later structure becomes legible?
- Does later character development strengthen or weaken an earlier ethical judgment?
- Does a later redraw or tankobon revision change how an early parallel should be read?

Retrospective insight may revise interpretation. It may not falsify the historical fact that the earlier text was ambiguous.

---

# 5. Evidence classification

Each deep reading should distinguish evidence types rather than presenting every claim with the same confidence.

Recommended labels:

- **TF — Textual Fact:** explicit dialogue, narration, caption, title, or stated information.
- **VF — Visual Fact:** directly visible action, composition, expression, body state, panel relation, setting, object, staging, or page design.
- **SF — Structural Fact:** chapter placement, recurrence, parallel scene construction, page-turn organization, formal juxtaposition.
- **IR — Interpretive Reading:** inference strongly supported by textual/visual/structural evidence.
- **TH — Thematic Hypothesis:** broader claim about what the work is doing; requires repeated evidence and counterevidence.
- **RR — Retrospective Recontextualization:** later material changes the significance of an earlier fact without changing what was literally present.
- **PR — Provisional Release Claim:** supported by official uncollected web material but not yet stabilized in tankobon.
- **RX — Revision Evidence:** derives from comparison among official versions/redraws/replacements.
- **CQ — Comparative Qualification:** depends on another continuity, translation, adaptation, or paratext and must not be mistaken for manga-continuity fact.

Confidence can be marked `high`, `medium`, or `low` when useful.

---

# 6. Primary-source locator standard

A V2 claim should be recoverable from the source without relying on conversation memory.

For tankobon:

`OPM|V07|chapter:XX|image:NNN|page:NN|anchor:<short description>`

If reliable printed page numbers exist, record them. If the source is a CBZ/image archive without stable printed pagination, use deterministic image number plus chapter.

For official web material:

`OPM|WEB|provider_episode_id:<ID>|display_label:<LABEL>|date:YYYY-MM-DD|panel/page:<N>|anchor:<description>`

Never use only “chapter 280” as a locator when the archival object has a provider-specific episode ID and may later be revised.

A source inventory/crosswalk should make it possible to route:

> synthesis claim → specialist/ledger claim → volume or web reading → evidence ID → source locator → original page/panel

---

# 7. Canonical volume deep-reading template

Every `OPM_VXX_DEEP_READING.md` should normally contain the following.

## 7.1 Authority and source block

- YAML front matter;
- exact source object;
- hash/integrity where available;
- included chapters/extras;
- publication-boundary spoiler scope;
- V2 method version;
- authority state.

## 7.2 Volume orientation

A compact statement of what changes in this volume:

- narrative position;
- dominant conflicts;
- new characters/institutions;
- major carryover questions;
- ending state.

Avoid long plot-summary retelling unless chronology itself is analytically important.

## 7.3 Central volume thesis and strongest counter-reading

State the strongest interpretive claim the volume supports, followed by at least one competing or limiting reading.

The goal is not forced contrarianism. It is to prevent later synthesis from mistaking an attractive first formulation for settled fact.

## 7.4 Sequential close reading

Analyze the load-bearing scenes in order.

For each major scene, consider as relevant:

- what changes causally;
- who knows what;
- what characters want;
- what is said and not said;
- visual presentation;
- comedic timing;
- bodily consequence;
- institutional context;
- public/private audience;
- power relation;
- relationship-state change;
- later callback potential.

## 7.5 Saitama state

Track separately:

- affect and boredom;
- heroic self-concept;
- desire for recognition;
- ethical instincts;
- ordinary-life concerns;
- relationships and domestic orbit;
- reactions to worthy opponents/power;
- evidence of emotional change;
- difference between what Saitama says and what the manga shows.

Do not force conventional protagonist growth onto him.

## 7.6 Ensemble character deltas

For every materially affected recurring character, record:

- goal;
- self-concept;
- fear/wound;
- institutional position;
- relationship state;
- combat/power state if relevant;
- moral or ideological movement;
- unresolved contradiction.

Only record deltas that the volume actually changes.

## 7.7 Heroism, rank, recognition, and institutions

Track:

- Hero Association classification;
- professional hero labor;
- public opinion;
- celebrity/image effects;
- rank incentives;
- donor/elite influence;
- legitimacy;
- coordination and bureaucracy;
- Neo Heroes or successor structures when they enter scope;
- cases where institutions recognize or misrecognize reality.

## 7.8 Monsterhood, personhood, and body

Distinguish among:

- biological monster status;
- social labeling;
- self-identification;
- obsession-driven transformation;
- monster-cell transformation;
- scientific modification;
- cyborg/mechanical reconstruction;
- psychic abnormality;
- divine/cosmic alteration;
- costume/persona identification;
- moral behavior.

Never treat “monster” as one stable ontological category if the source does not.

## 7.9 Power, technique, and explanatory systems

Track what the volume establishes about:

- training;
- martial lineage;
- technological modification;
- psychic ability;
- biological evolution;
- monsterization;
- limiter discourse;
- God-granted power;
- Blast/cosmic systems;
- copying/adaptation;
- institutional threat classification.

Power-scaling may be recorded when the text makes it relevant, but it should not replace analysis of what power means, how it is used, or what it costs.

## 7.10 Humor, satire, and genre mechanics

Identify the target and mechanism of jokes rather than merely noting that a scene is funny.

Possible targets include:

- shonen escalation;
- named-technique inflation;
- heroic celebrity;
- bureaucracy;
- rankings;
- public judgment;
- masculine self-mythology;
- martial prestige;
- villain monologues;
- chosen-one logic;
- cosmic grandeur;
- power-scaling culture;
- ordinary consumer life.

Also note when satire coexists with sincere admiration. *One Punch Man* frequently mocks battle-manga language while still enjoying it.

## 7.11 Japanese language and voice

Record recurring language only when the Japanese materially clarifies character or theme.

Useful areas include:

- pronouns and address terms;
- politeness/register shifts;
- hero names versus personal names;
- monster/self-labeling language;
- terms for strength, justice, heroism, fear, popularity, rank, humanity, monsters, God, and institutions;
- distinctive speech rhythms;
- slogans, public relations language, and bureaucratic terminology;
- linguistic contrast between grandiose rhetoric and Saitama's plain speech.

Avoid turning every line into a translation note.

## 7.12 Visual and formal analysis

Treat manga form as primary evidence.

Track as relevant:

- panel density and decompression;
- full-page and double-page spreads;
- page-turn reveals;
- speed lines and motion continuity;
- scale relationships;
- environmental destruction;
- face/body simplification;
- hyper-rendering versus gag abstraction;
- grotesque bodily form;
- recurring silhouettes and framing;
- blank/negative space;
- reaction-shot sequencing;
- visual rhyme between heroes and monsters;
- crowd staging;
- visual treatment of reputation versus reality;
- redraw/revision differences.

## 7.13 V1 claim audit

Only address earlier claims implicated by this volume.

Use:

- `PRESERVE`
- `STRENGTHEN`
- `REVISE`
- `DOWNGRADE`
- `REJECT`
- `OPEN`

Each transition should point to the earlier formulation, the current formulation, and the primary evidence route.

## 7.14 Publication-boundary open questions

Record what remains genuinely unresolved **at this volume boundary**.

Do not answer this section with later knowledge.

## 7.15 Retrospective recontextualization

Only after the prospective section is complete, add current-corpus hindsight.

Clearly label it `RR`.

## 7.16 Ledger updates and cumulative delta

List which longitudinal ledgers must be updated and what changed.

---

# 8. Longitudinal ledger system

The V2 project should maintain a limited set of durable cumulative ledgers.

## 8.1 Saitama: meaning, affect, ordinary life, and relationships

`OPM_SAITAMA_CHARACTER_STATE_LEDGER.md`

Tracks the problem of post-growth existence and whether ordinary attachment increasingly replaces battle intensity as Saitama's route back into consequence.

## 8.2 Heroism, recognition, rank, and institutional legitimacy

`OPM_HEROISM_RECOGNITION_RANK_AND_INSTITUTION_LEDGER.md`

Tracks Hero Association, public opinion, King/Saitama misrecognition, celebrity heroism, rank, professional legitimacy, Neo Heroes, and institutional transitions.

## 8.3 Monsterhood, personhood, body, and transformation

`OPM_MONSTERHOOD_PERSONHOOD_BODY_AND_TRANSFORMATION_LEDGER.md`

Tracks unstable monster ontology and the relation among body, desire, label, moral action, technology, biology, divine intervention, and self-authorship.

## 8.4 Power, technique, limiter, God, and cosmic ontology

`OPM_POWER_TECHNIQUE_LIMITER_GOD_AND_COSMIC_LEDGER.md`

Tracks explanatory systems without prematurely forcing them into one unified power system.

## 8.5 Ensemble character and relationship states

`OPM_CHARACTER_STATE_LEDGER_SET` plus `OPM_RELATIONSHIP_STATE_LEDGER.md`

Tracks only recurring characters whose state materially changes. This avoids creating dozens of isolated character documents prematurely.

## 8.6 Technology, the Organization, and hidden strategic actors

`OPM_TECHNOLOGY_ORGANIZATION_AND_HIDDEN_ACTORS_LEDGER.md`

Tracks Genos/Kuseno, Metal Knight, Drive Knight, the Organization, artificial bodies, weapons infrastructure, surveillance, research, and related unresolved actors.

## 8.7 Satire, genre, public narrative, and reputation

`OPM_SATIRE_GENRE_AND_PUBLIC_NARRATIVE_LEDGER.md`

Tracks recurring satirical mechanisms and how parody, sincerity, spectacle, and social narrative interact.

## 8.8 Visual form, motifs, redraws, and revision history

`OPM_VISUAL_FORM_MOTIF_AND_REDRAW_LEDGER.md`

Tracks recurring visual grammar plus material web-to-tankobon revisions.

## 8.9 Open questions and mystery state

`OPM_OPEN_QUESTIONS_AND_MYSTERY_LEDGER.md`

For each mystery, record:

- first appearance;
- current evidence;
- live hypotheses;
- disconfirmed hypotheses;
- current confidence;
- last volume/update affecting it.

This is especially important for an ongoing work because old speculative language otherwise hardens into “fact” through repetition.

---

# 9. Checkpoint method

A 37-plus-volume project needs intermediate synthesis, but checkpoints should not become mini full-series syntheses.

Create a checkpoint when either condition is met:

1. roughly 4–6 volumes have accumulated since the last checkpoint; or
2. a major arc/institutional/character-state boundary makes an earlier checkpoint analytically natural.

Each checkpoint should:

- summarize cumulative state changes;
- identify claims that strengthened or weakened;
- reconcile repeated terminology;
- surface contradictions among volume readings;
- prune duplicate hypotheses;
- identify which ledgers need restructuring;
- define the next reading tranche;
- preserve unresolved questions.

A checkpoint should not rewrite all prior volume arguments.

---

# 10. Current-release protocol for uncollected web manga

The current-release layer is deliberately separate from sequential tankobon analysis.

## 10.1 Intake

For each official new installment:

1. identify the provider episode/update ID;
2. save or reference the lawful source snapshot;
3. record publication date;
4. classify main chapter / extra / alternate / revision;
5. compare against the immediately prior official state if a redraw/replacement is suspected;
6. assign a provisional source locator;
7. update the current-release source lock.

## 10.2 Reading cadence

Do **not** create one large permanent synthesis after every update.

Prefer one of:

- compact update notes for minor installments; or
- `OPM_WEB_<RANGE>_DEEP_READING.md` for coherent narrative tranches.

A tranche should normally close when:

- a local scene/mini-arc resolves;
- a major revelation changes an existing ledger;
- enough material accumulates to justify synthesis;
- a new tankobon boundary is announced or released.

## 10.3 Authority marking

All uncollected conclusions must be labeled `active_provisional` and evidence code `PR` where relevant.

Do not silently rewrite canonical tankobon specialist documents merely because a web update suggests a new direction. Update the current-state map and provisional ledgers first.

## 10.4 Tankobon reconciliation event

When a new volume is released:

1. lock and hash the new Japanese tankobon;
2. build a web-to-tankobon crosswalk;
3. identify included web updates;
4. diff meaningful redraws, rewrites, reordering, omissions, additions, and extras;
5. produce the canonical `OPM_VXX_DEEP_READING.md` from the tankobon itself;
6. route all provisional claims through `PRESERVE / STRENGTHEN / REVISE / DOWNGRADE / REJECT / OPEN`;
7. move superseded current-release notes into a historical sublayer rather than deleting them;
8. update the cumulative collected-boundary synthesis;
9. advance `CURRENT_STATE_AND_CORPUS_MAP.md`.

This tankobon reconciliation is the natural freeze point for the ongoing project.

---

# 11. V1-to-V2 migration rule

The existing analysis should be preserved under `90 Legacy and Superseded`, including the broad through-Volume-34 synthesis and major character/thematic references.

Do not copy its conclusions automatically into V2.

Instead:

1. extract load-bearing V1 claims into a revision ledger;
2. assign stable claim IDs;
3. identify the earliest V2 volume that can test each claim;
4. adjudicate only when enough primary evidence exists;
5. point mature V2 syntheses to the revised formulation and evidence chain.

Example schema:

| Claim ID | V1 formulation | First test scope | Status | V2 formulation | Evidence route |
|---|---|---|---|---|---|
| OPM-V1-C001 | Saitama breaks genre so the supporting cast inherits genre | V01 onward | OPEN | pending | pending |

This preserves intellectual continuity without allowing the earlier synthesis to dictate the reread.

---

# 12. Specialist synthesis rule

Do not produce character monographs simply because a character is popular.

A specialist document is justified when a subject:

- recurs across many volumes;
- accumulates enough evidence to become hard to retrieve from volume files;
- supports later cumulative synthesis;
- has a distinct analytical responsibility;
- is likely to require continuing revision.

When a specialist document exists, later insights should update that canonical topical home rather than generate `UPDATED`, `FINAL`, `NEW THOUGHTS`, or other near-duplicate files.

---

# 13. Ongoing-series claim discipline

Use these terms carefully:

- **established through VXX** — strongly supported within a defined collected boundary;
- **current provisional** — supported by official uncollected material;
- **open** — unresolved;
- **retrospectively strengthened/revised** — later material changes confidence;
- **final** — reserve for a closed question, not for the series as a whole;
- **full-series** — do not use for the main manga until serialization is actually complete.

Prefer filenames such as:

`OPM_CUMULATIVE_SERIES_SYNTHESIS_THROUGH_V37.md`

not:

`OPM_DEFINITIVE_FULL_SERIES_SYNTHESIS.md`

---

# 14. Quality-control checklist for every deep reading

Before freezing a volume artifact, verify:

- source identity and chapter contents are correct;
- spoiler boundary is explicit;
- webcomic/anime knowledge has not leaked into manga fact claims;
- Japanese-language claims are based on Japanese text;
- visual claims have recoverable locators;
- Saitama is not forced into a conventional power-growth arc;
- supporting characters are not reduced to functions of Saitama;
- heroism is not equated automatically with strength, rank, legality, popularity, or effectiveness;
- monsterhood is not treated as a single stable category without evidence;
- power-scaling claims do not substitute for thematic or causal analysis;
- satire and sincere genre pleasure are both considered;
- strongest counterevidence is recorded for major thematic claims;
- V1 claims are explicitly adjudicated rather than silently inherited;
- retrospective insight is separated from publication-boundary knowledge;
- cumulative ledgers are updated only where state actually changed.

---

# 15. Recommended initial V2 sequence

## Phase 0 — corpus audit, source lock, and V1 claim inventory

Deliverables:

- `OPM_SOURCE_INVENTORY_AND_LOCK.md`
- `OPM_TANKOBON_CHAPTER_CROSSWALK.md`
- `OPM_WEB_SERIALIZATION_AND_REVISION_CROSSWALK.md`
- `OPM_V1_TO_V2_CLAIM_REVISION_LEDGER.md`
- `CURRENT_STATE_AND_CORPUS_MAP.md`

Phase 0 should determine the precise chapter/extra contents of the contiguous collected volumes actually present before fixed arc checkpoints are finalized. Later isolated holdings or newly acquired volumes are appended without redefining earlier source identity.

## Phase 1 — sequential reread from Volume 1

Produce one canonical deep reading per volume.

Do not skip directly to Volume 35 because V1 already covered 1–34. The point of V2 is source-grounded longitudinal reconstruction.

## Phase 2 — rolling checkpoints and ledgers

Use approximately 4–6-volume or natural arc boundaries.

Candidate early checkpoint boundaries can be adjusted after the source audit; they are architectural aids, not canon.

## Phase 3 — collected-boundary synthesis at the latest reconciled volume

After the currently contiguous collected boundary has been re-read and its ledgers stabilized, produce specialist syntheses and a cumulative collected-manga synthesis. Extend that boundary when later volumes are acquired and reconciled; do not hard-code an unpublished, unavailable, or sequence-gapped volume as a prerequisite.

## Phase 4 — current web release

Analyze the official uncollected layer under active-provisional authority.

## Phase 5 — tankobon reconciliation and rolling continuation

Each new volume becomes a new canonical collected boundary and triggers reconciliation rather than a parallel project.

---

# 16. Governing rule

The V2 project should remain useful even if *One Punch Man* publishes for many more years.

That requires resisting two temptations:

1. treating every new web update as if it rewrites the whole series; and
2. treating a mature synthesis as if publication has ended.

The durable model is:

> **stable tankobon spine + provisional current-release layer + longitudinal ledgers + boundary-specific synthesis + explicit revision history.**

That structure allows the corpus to grow without losing provenance, chronology, or analytical authority.


---

# 16. Character-state and reconstruction amendment

This amendment adds a formal longitudinal character-modeling layer without reducing the literary, visual, linguistic, institutional, source-critical, or revision-aware requirements above.

The governing addition is:

> **Every volume must preserve not only what characters mean thematically, but also the source-grounded conditional behavioral state needed to reconstruct how they perceive, decide, speak, and relate under different conditions.**

Character reconstruction is downstream of analysis. Predictions, scenario probes, and model outputs are never canonical evidence and must not be cited back into the observational corpus.

## 16.1 Character-centered ledgers

Replace the single undifferentiated ensemble character/relationship ledger concept with these character-centered homes, which coexist with all concept-centered thematic ledgers:

1. `OPM_SAITAMA_CHARACTER_STATE_LEDGER.md`
2. `OPM_HERO_CHARACTER_STATE_LEDGER.md`
3. `OPM_MONSTER_ANTAGONIST_CHARACTER_STATE_LEDGER.md`
4. `OPM_INDEPENDENT_CIVILIAN_CHARACTER_STATE_LEDGER.md`
5. `OPM_RELATIONSHIP_STATE_LEDGER.md`
6. `OPM_CHARACTER_MODEL_READINESS_INDEX.md`

Do not create further cohort splits merely for symmetry. If a ledger becomes persistently unwieldy, split it deliberately, preserve cross-links, and update the corpus map.

Saitama receives a dedicated state ledger because conventional danger/stress evidence is unusually non-diagnostic for him and because ordinary-life, recognition, boredom, irritation, friendship, shopping, games, food, and social-intrusion contexts are disproportionately important to his model.

## 16.2 Mandatory modeling fields

When evidence supports them, preserve:

- identity/current role and institutional affiliation;
- desire hierarchy;
- fears, vulnerabilities, pride/shame/status sensitivities;
- self-conception;
- values and power philosophy;
- perception/attention tendencies;
- blind spots and attribution habits;
- decision heuristics;
- risk tolerance and action threshold;
- response to uncertainty and authority;
- conflict/escalation and restraint/de-escalation behavior;
- care/help behavior;
- stress, failure, defeat, humiliation, praise, grief, injury, and exhaustion responses;
- low-stakes baseline behavior;
- relationship-specific behavior;
- Japanese speech/register conditioned by partner and situation;
- embodiment, injury, transformation, and bodily-cost behavior;
- knowledge/epistemic limits;
- public reputation versus actual capability;
- public persona versus private behavior;
- hero/monster/self-label identity;
- relation to rank and recognition;
- power perception and danger calibration;
- current contradictions and counterexamples;
- state transition from the prior boundary;
- primary-source locators;
- evidence authority/revision state;
- confidence and model-readiness.

Do not fabricate fields merely to fill a template.

## 16.3 Behavioral evidence atoms

A modeling claim must be traceable to an observed scene. Preferred compact form:

| Context | Trigger | Partner | Observed behavior | Interpretation | Locator | Evidence class | Authority | Confidence |
|---|---|---|---|---|---|---|---|---|

Repeated observations across contexts are more valuable than elaborate trait adjectives.

For OPM, `Authority` should normally distinguish at least:

- `tankobon_canonical`;
- `web_active_provisional`;
- `web_superseded_revision_evidence`.

A web-derived character claim that is redrawn, replaced, reordered, or collected differently must be reconciled rather than silently retained.

## 16.4 State/trait discipline

Every apparent personality feature should be classified, where possible, as one of:

- stable tendency;
- current developmental state;
- relationship-specific tendency;
- role-specific behavior;
- stress-specific behavior;
- exceptional one-off;
- unresolved hypothesis.

The burden of proof rises when moving from a local observation to a stable trait. Avoid global descriptors such as `hotheaded`, `cowardly`, `arrogant`, or `kind` when the evidence supports a more conditional rule.

## 16.5 Relationship conditioning

Relationships are directional unless the evidence supports a truly reciprocal formulation. Preserve asymmetry rather than averaging two participants' understandings.

Examples likely to require directional tracking include Saitama→Genos and Genos→Saitama; Saitama→King and King→Saitama; Fubuki→Saitama and Saitama→Fubuki; Tatsumaki→Fubuki and Fubuki→Tatsumaki; Bang→Garou and Garou→Bang; Garou→Tareo and Tareo→Garou.

The relationship ledger should track trust, affection, rivalry, fear, dependency, authority, resentment, idealization, protectiveness, communication style, recurring conflict, repair behavior, speech/register differences, major state transitions, and asymmetries in knowledge or interpretation.

## 16.6 Low-stakes evidence is first-class evidence

Do not model characters primarily from battles and ideological speeches. Preserve ordinary contexts such as meals, shopping, games, domestic routines, waiting, jokes, embarrassment, hobbies, mundane frustration, friendship maintenance, bureaucratic encounters, casual status behavior, and small acts of care.

High-stakes scenes reveal values under pressure. Low-stakes scenes reveal baseline social personality. For Saitama, King, Genos, Fubuki, and many supporting characters, low-stakes material may be especially diagnostic.

## 16.7 Japanese voice as conditional behavior

The Japanese-language lens now feeds per-character speech models. Record not only distinctive forms but their conditions:

- partner;
- social hierarchy;
- public versus private audience;
- emotional state;
- serious versus comedic mode;
- fatigue/injury;
- professional versus intimate context;
- stable identity marker versus momentary effect.

Surface catchphrase imitation without register logic is a failed reconstruction.

## 16.8 Knowledge-state and misrecognition control

Any reconstruction must lock chronology and character knowledge. Analyst hindsight may inform interpretation, but simulated characters must not know future reveals, private scenes they did not witness, hidden identities they have not learned, objective power facts unavailable to them, or motives shown only to the reader.

This is especially important in OPM because public reputation, mistaken threat assessment, false attribution of feats, hidden strength, secret identities, and institutional misrecognition are constitutive parts of characterization.

## 16.9 Dual model horizons for an ongoing redraw-prone work

Maintain two character-model horizons:

### Collected model state
Only evidence stabilized in canonical Japanese tankobon.

### Current-release overlay
Official uncollected web evidence marked `active_provisional`.

Do not silently merge the current-release overlay into the collected model. When provisional material is replaced or collected, reconcile its evidence atoms and authority states explicitly.

## 16.10 Per-volume character-model update pass

After the existing literary/revision synthesis, perform a mandatory character-model pass for every character receiving meaningful new evidence:

1. route the character to the canonical state ledger;
2. update current state only where changed;
3. append new behavioral evidence atoms;
4. update directional relationship deltas;
5. update speech/register observations;
6. preserve low-stakes evidence even without a character arc;
7. record contradictions/counterexamples;
8. reconcile collected versus provisional authority;
9. update model-readiness only when evidence breadth materially changes.

Each `OPM_VXX_DEEP_READING.md` must therefore include a `Character-modeling updates` section with, as applicable:

- state delta;
- new context coverage;
- decision/behavior evidence;
- relationship-specific update;
- speech/register update;
- contradiction/uncertainty;
- authority/revision note;
- readiness change.

If a volume adds no modeling-relevant evidence for a character, do not manufacture an entry.

## 16.11 Model readiness

Use:

- `insufficient`;
- `emerging`;
- `moderate`;
- `strong`;
- `specialist_ready`.

Readiness measures evidence breadth, not popularity, combat importance, thematic confidence, or number of appearances.

The readiness index should track at minimum context breadth, relationship breadth, Japanese-language breadth, longitudinal depth, low-stakes breadth, stress breadth, current readiness, and the principal missing evidence.

## 16.12 Prediction and held-out validation

Prediction is downstream, never evidence. At major checkpoints, use held-out canonical scenes where feasible:

1. freeze the model at boundary `Vn`;
2. permit only evidence whose `available_from` boundary is `<= Vn`;
3. exclude later `RR` knowledge from the prediction;
4. predict likely behavior/speech with plausible alternatives and confidence;
5. reveal the later canonical scene;
6. classify mismatch as missing context, wrong stable-trait inference, relationship-specific exception, stress-specific exception, genuine growth, genuine surprise, revision instability, or insufficient evidence;
7. revise the model rather than rationalizing the miss.

Do not rewrite a prediction after seeing the result.

## 16.13 Per-volume update manifest

Every completed volume should emit `OPM_VXX_UPDATE_MANIFEST.md` under `08 Audits and Manifests` or its established manifest subfolder. It should record:

- deep-reading artifact and Drive ID;
- character ledgers touched;
- relationship ledger status;
- thematic ledgers touched;
- readiness changes;
- claim-revision updates;
- locator/index updates;
- current corpus-map change if any;
- checksums/IDs when maintained;
- explicit `NO CHANGE` for expected cumulative surfaces legitimately unaffected.

The manifest is an audit of propagation, not a second analytical summary.

## 16.14 Governing modeling principle

The character model should answer:

> **Given this chronology, knowledge state, relationship, stakes, role, audience, and stress regime, what response is best supported by the character's observed behavioral history?**

It should never answer:

> **What response would be dramatically convenient or stereotypically in character?**

The goal is evidence-grounded conditional reconstruction, not roleplay by vibe.
