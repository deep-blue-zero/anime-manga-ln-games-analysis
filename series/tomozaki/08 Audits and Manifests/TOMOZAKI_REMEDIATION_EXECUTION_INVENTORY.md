---
series: TOMOZAKI
artifact_type: remediation_execution_inventory
source_boundary: "Locked Japanese V01–V11 plus story-local V06.5/V08.5; no later source admitted"
generation: V2.4
status: canonical
release_state: mutable_active
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
recommended_reasoning_class: PREMIUM_QUALITY_FIRST
execution_reasoning_control: Max
---

# Tomozaki — analytical document spine and remaining-work inventory

## 0. Current task boundary

The owner first limited this work to identifying the analytical spine, then expressly authorized **R01–R03 and their upstream publication**. Those three tasks are now complete under the [longitudinal reconciliation audit](TOMOZAKI_LONGITUDINAL_RECONCILIATION_AUDIT.md). Literary authoring was reserved for a separate session. The owner has now supplied its Fumiya monograph and authorized repository integration. The [Fumiya review](TOMOZAKI_FUMIYA_R04_INTEGRATION_REVIEW.md) passes that individual R04 responsibility; Hinami and the later literary work remain unfinished. This integration does not complete R04, execute R05–R11, complete R12’s literary release responsibility, or admit new source material.

This inventory retains the original remaining-work identities and baseline deficiencies for continuity. The architecture and corpus map govern responsibility/readiness; the new audits record the actual R01–R03 source checks, correction propagation and bounded PASS. Sections 2–4 preserve the earlier dependency assessment, while §6 supplies current execution status, including the later Fumiya-only integration.

## 1. Audited resumption baseline

The resumption began at `512ce17ea310377e9273c60621f8f33b0f93f220`. Fetch found `origin/series/tomozaki` at `98eeb39f8186adffeca968ec4b0d23a46899d133` and `origin/main` at `b331a3b746622760db394ac1a79367263236336f`. The former advanced through nightly reconciliation; the latter integrated the preceding Tomozaki tranche in PR #71. The local stable branch fast-forwarded to the series head, then incorporated current main without content conflicts at `39430a3790a069023af20ce8f03e353b2fdfbc7a`. The sole pre-existing untracked surface was `.scratch/`; it remains excluded from staging.

The controlling [architecture](../00%20Frameworks%20and%20Methods/TOMOZAKI_SYNTHESIS_ARCHITECTURE.md) is v1.1, EVOLVING at this baseline. The [role-gap audit](TOMOZAKI_ARCHITECTURE_AND_SYNTHESIS_ROLE_GAP_AUDIT.md) is an immutable historical checkpoint: its old Git divergence and working-tree observations describe its cutoff, not this resumption. Its semantic gaps remain substantially valid. Later completion will be recorded in a successor current audit and the corpus map, without rewriting that checkpoint.

The inspected root contains thirteen completed source-facing readings, five existing substantive ledgers, seven provisional character files, one provisional full-series file, method/architecture/source controls, and three historical audit/manifest files. No relationship or thematic specialist directory exists at baseline. Directory and filename counts are discovery evidence only; the role decisions below follow the documents' actual responsibilities and evidence routes.

## 2. Dependency inventory at identification; current status in §6

| ID | Required work | Existing evidence and deficiency | Completion test |
|---|---|---|---|
| R01 | Reconcile character, relationship, claim/evidence, and social-system backfills with the effort spine | Existing state schemas, chronological rows, CS/REL/SOC/CRI/EFFORT identifiers, 319-claim/140-question universe, and explicit OPENs are substantial. Several current prose routes still call already-authored neighbors future/pending. Shared history and attribution need cross-checking. | Stable claim identities and routes; disagreements classified; current overlapping propositions agree or explicitly remain OPEN. |
| R02 | Discharge ESC-01–ESC-12 as targeted source retrieval tasks | Claim index §13 identifies exactly twelve wording/attribution/causality/chronology queues. Their L1 routes exist; reviewed L2/L3 completion remains unrecorded. | Each queue has locked witness verification, exact package locator, minimal diagnostic marker, attributed interpretation, and bounded disposition. Resolving retrieval does not resolve an undecidable story question. |
| R03 | Author Japanese voice/register/key-terms ledger | Conceptual lexemes are distributed across readings; systematic character-specific inference would currently overreach. | Verified samples by speaker, recipient, narrative layer, and state; explicit distinction between attested local form and unsupported global speech habits. |
| R04 | Mature Tomozaki and Hinami monographs | Existing theses and outline chronology are useful; they lack sustained case reconstruction, deterministic backward evidence, and sufficiently developed counterreadings. | Architecture §7.3; multiple developmental states and recipient/stress contexts; detailed cause/authority and self-theory/conduct separation; actual source corrections propagated. |
| R05 | Mature Kikuchi and Mimimi monographs | Independent authored-world ethics, habitat formation, vocational motive, comparative value, role loss, costly care, and romantic restraint exceed the overview candidates. | Same monograph contract; explicit private supplemental knowledge; no reduced romance-subplot account. |
| R06 | Adjudicate the declared roles of Tama, Mizusawa, and Yuzu before upgrading them | Each has a recurring independent responsibility. Tama's learner/interface/ethical trajectory is a strong candidate for a focused monograph; Mizusawa and Yuzu have substantial conduct evidence but narrower interior and future-state evidence. These are planning assessments, not completed role adjudications. | Decide from detailed evidence whether each existing file becomes a mature monograph or an explicitly bounded dossier; retain paths, provenance, useful analysis, exclusions, and specialist handoffs. No label-only promotion. |
| R07 | Three mandatory relationship specialists | Relationship ledger §§5–7 already preserves directional histories. This is cumulative evidence, not a substitute for independent relational argument. | Tomozaki/Hinami, Tomozaki/Kikuchi, Tomozaki/Mimimi each adds explanatory, adversarial, stateful synthesis beyond repeating chronology. |
| R08 | Core-peer ensemble, including co-equal Mimimi/Tama responsibility | Relationship ledger §13.2 explicitly promotes both responsibilities. Social ledger §13.2 distinguishes field mechanisms from this particular network's agency. | Dedicated ensemble artifact, sustained Mimimi/Tama case; distinct contributors, ordinary practice, asymmetric knowledge/cost, V11 proposal versus execution. |
| R09 | Seven mandatory thematic specialists | Architecture §9 and role audit §12 identify independent recurring domains. No mature owner exists at baseline. | Seven separately retrievable domains: game/form/self-authorship; effort/mastery/rank/goal/future; social atmosphere/punishment/repair; control/causality/meaning; romance/care/disclosure/intervention; authorship/fiction/personhood; Japanese conceptual language/voice/register. |
| R10 | Adversarial claim/locator and cross-specialist convergence | Existing immutable audit predates implementation of these dependencies. | Compare shared claims and terms, source/disclosure clocks, actor knowledge, permission, claim scope, counterevidence, and substantive OPENs. Backward retrieval samples reach actual evidence. |
| R11 | Revise full-series synthesis last | Existing argument contains valuable hypotheses but was written before required layers; broad references cannot confer maturity. | R01–R10 pass first; integrate changing game metaphor, plural agency, form, care, uncontrollability and unresolved boundary without concatenating monographs. Preserve identity and useful established analysis. |
| R12 | Current routing, maturity, manifests, literary release audit, repository publication | Map and controls truthfully reflect earlier open state, but will need synchronized updates. | Exact changed-path manifest, mature responsibility audit, links, authority graph, frozen-source preservation, applicable local validators, normal push, successful source audit, completed housekeeping and exact-head integration status. |

## 3. The document spine to create or revise

All paths in this section are relative to `series/tomozaki/`. Existing filenames are authoritative identities. The three verification-layer paths in §3.3, originally marked **proposed**, are now authored and reviewed. Other proposed downstream products remain future work; their filenames may change without changing their responsibilities.

### 3.1 Preserve the completed foundation

Preserve `01 Source Lock and Inventory/TOMOZAKI_SOURCE_LOCK_AND_INVENTORY.md`, all thirteen readings and the README in `02 Sequential Readings/`, the bootstrap manifest, and the two historical audit checkpoints. The analytical method already supplies the epistemic contract. No new broad sequential reading or replacement evidence summary is needed at this boundary. Earlier freeze metadata discrepancies remain a separate, optional governed migration, not a reason to rewrite their prose.

### 3.2 Reconcile the five existing cumulative owners

These five files in `03 Longitudinal Ledgers/` are the substantive evidence spine. Revision means targeted reconciliation of current claims, source routes, and readiness statements, preserving stable identifiers and historical state.

| Existing file | Required revision and distinct responsibility |
|---|---|
| `TOMOZAKI_EFFORT_COMPETITION_AND_GOAL_OWNERSHIP_LEDGER.md` | Preserve the mature V11 effort history. Compare shared competition, pursuit, goal-origin, and stopping-rule propositions with the newer ledgers; record only necessary bounded corrections. It must not become a generic character or relationship summary. |
| `TOMOZAKI_CHARACTER_STATE_LEDGER.md` | Reconcile chronological state and evidence classes with the other owners; narrow mixed-person family-history attribution, the phone-call action, and renewed-confession wording where applicable. Retain CS identities and supporting-character limits. |
| `TOMOZAKI_RELATIONSHIP_STATE_LEDGER.md` | Reconcile directional knowledge, disclosure, standing, refusal, and cost. Reader access to supplemental/private history is not automatically shared knowledge. Preserve REL identities and the specialist-promotion decisions in §13. |
| `TOMOZAKI_CLAIM_REVISION_AND_EVIDENCE_INDEX.md` | Preserve its 319-claim/140-question universe, promoted/local partition, and CRI families. Connect ESC-01–ESC-12 to actual source-locator results, propagate corrections, update obsolete dependency statements, and retain genuinely unresolved questions. Source retrieval completion and story resolution are different states. |
| `TOMOZAKI_SOCIAL_ATMOSPHERE_AND_GROUP_SYSTEMS_LEDGER.md` | Reconcile SOC propositions with character, relationship, and effort claims; verify speaker attribution for punishment language and distinguish field mechanics from individual motive, accountability, and the specific peer ensemble. |

No sixth generic character-development or relationship ledger is needed: those responsibilities already have owners.

### 3.3 Create the missing verification layer

| Required new artifact | Responsibility and completion evidence |
|---|---|
| `03 Longitudinal Ledgers/TOMOZAKI_JAPANESE_VOICE_REGISTER_AND_KEY_TERMS_LEDGER.md` | Architecture-prescribed missing sixth cumulative owner. Attested language by speaker, recipient, scene/state, and narrative layer; key-term variation; negative limits on extrapolating global speech habits. Use selective locked-Japanese retrieval, not reconstructed quotations from English summaries. |
| `08 Audits and Manifests/TOMOZAKI_TARGETED_SOURCE_LOCATOR_AUDIT.md` **(proposed)** | Witness identity, locator convention, and ESC-01–ESC-12 dispositions. Record package item, scene/paragraph marker, attribution, uncertainty, and the exact claims supported. A retrieval PASS can coexist with unresolved intent, chronology, motive, or consent. |
| `08 Audits and Manifests/TOMOZAKI_LONGITUDINAL_RECONCILIATION_AUDIT.md` **(proposed)** | Review the six cumulative owners together. Record each material discrepancy, surviving and abandoned formulation, affected CRI/CS/REL/SOC/effort routes, propagation status, and remaining OPENs. This is the gate decision, not another duplicate ledger. |

Dependency order: compare the existing five owners and identify discrepancies → perform targeted source verification while building the voice ledger → propagate verified corrections to all affected mutable owners → independently audit longitudinal convergence. Reconciliation can prepare the retrieval queue first, but cannot be declared complete before its required source checks return.

### 3.4 Revise routing and control documents after evidence changes

| Existing control | Required later update |
|---|---|
| `CURRENT_STATE_AND_CORPUS_MAP.md` | Link actual owners and audits; distinguish task handoff from analytical completion; update gates only after their completion tests pass. |
| `00 Frameworks and Methods/TOMOZAKI_SYNTHESIS_ARCHITECTURE.md` | Synchronize artifact states and adjudicated promotions; repair the stale archive-policy path to `governance/source-policies/ARCHIVE_AUTHORITY_AND_SUPERSESSION_POLICY.md`; stabilize the architecture only when responsibility gaps are settled. No synthesis-architecture edit is performed in this identification tranche. |
| `03 Longitudinal Ledgers/README.md` | Synchronize six-owner coverage and source/reconciliation readiness. |
| `04 Character Analysis/README.md` | In the separate literary session, synchronize evidence-based monograph/dossier roles and their maturity after review. |

Create `06 Specialist Synthesis/README.md` when the first substantive specialist is actually authored. Maintain a changed-path/validation manifest for each later implementation tranche; do not rewrite the historical bootstrap manifest into a live inventory. No new global registry or housekeeping-owned output is needed merely because this root gains analytical files.

### 3.5 Downstream work reserved for the separate session

**Character documents:** revise the existing seven files under `04 Character Analysis/`: Tomozaki Fumiya, Hinami Aoi, Kikuchi Fuka, Nanami Minami, Natsubayashi Hanabi, Mizusawa Takahiro, and Izumi Yuzu. The first four have mandatory full-monograph responsibilities; the last three require the scope adjudication described in R06. Use the reconciled spine as evidence authority, not the pre-remediation full-series candidate.

**Relationship specialists:** create independent Tomozaki/Hinami, Tomozaki/Kikuchi, and Tomozaki/Mimimi studies under `06 Specialist Synthesis/`. The relationship ledger also promotes a core-peer ensemble and Mimimi/Tama responsibility; a dedicated ensemble with a co-equal major Mimimi/Tama analysis is a proposed compliant grouping. That grouping must be tested for adequate scope, not accepted because a heading exists.

**Thematic specialists:** architecture §9.1 requires seven retrievable domains: game models/form/authenticity/self-authorship; effort/mastery/rank/goal ownership/future viability; social atmosphere/reputation/punishment/repair; control/causality/result/reason/meaning; romance/care/disclosure/boundaries/intervention; authorship/fiction/observation/personhood; Japanese conceptual language/voice/register. Seven separate files are a conservative implementation plan, not a claim that the architecture forbids justified consolidation. The voice specialist interprets attested language across the series; it does not replace the evidential voice ledger.

**Final integration controls:** create an adversarial claim/locator and cross-specialist convergence audit after those literary owners mature; revise `05 Full-Series Synthesis/TOMOZAKI_FULL_SERIES_SYNTHESIS.md` only after that audit passes; then create a literary validation/release audit and update routing/maturity/manifest records. Exact audit filenames are implementation choices. Historical checkpoints remain unchanged. Reconstruction models under `07` remain optional, downstream, and deferred.

### 3.6 Bounded coverage decisions

The proposed eleven-file specialist grouping consists of three primary dyads, one ensemble with a major Mimimi/Tama section, and seven thematic domains. Hinami/Tama requires a major case in the relevant character and intervention studies; Hinami/Mizusawa requires pursuit and authority treatment; Tomozaki/Mizusawa requires friendship/disclosure treatment; Tomozaki/Rena requires bodily/contact/disclosure treatment. Kikuchi/Mimimi routes through primary relationship and ensemble studies. These coverage responsibilities follow relationship-ledger §13; exact grouping remains subject to substantive review.

Nakamura, Konno, Akiyama, Takei, Haruka, Nagisa, Yoko, Rena, and Ashigaru receive evidence-proportionate specialist/ensemble treatment. Their sparse or focalized interior evidence does not justify invented full biographies. Professional institutions, gendered performance, and ordinary life remain distributed within the required domains; no additional specialist is needed merely for symmetry. Adaptations and V12+ remain outside admission. Derived reconstruction models remain optional and deferred; they are not prerequisites for literary release and cannot repair missing literary authority.

## 4. Initial correction queue; disposition now in the reconciliation audit

This section records issues discovered during preparation; it does **not** silently correct a frozen reading or certify a completed source audit. The primary checks below used the locked local EPUBs read-only. `P` means one-based order of all HTML `p` elements within the named package item, including empty/image paragraphs, counted before ruby annotations are removed for display. These are reproducible package-relative markers, not printed page numbers or vendor EPUB locations. Witness authority remains the source lock.

| Issue | Verified evidence / deterministic corpus route | Required disposition and downstream owners |
|---|---|---|
| Nagisa's school-year chronology | V10 `text/part0024.html` P139 identifies Nagisa as a sixth grader; V11 `item/xhtml/p-0030.xhtml` P826–827 identifies Aoi as a sixth grader and Nagisa as two years younger; P1010 again gives Aoi/Haruka as sixth/third graders. These passages were independently checked. | Preserve genuine textual tension; exact school-year alignment remains OPEN. Do not harmonize by inventing chronology or resolve intent. Character, relationship, CRI, voice/locator, and later causality owners must share the limit. |
| V11 family-history narrative layer | `item/xhtml/p-0030.xhtml` P721/P728 frame Hinami's disclosure; P730 marks a scene break; P732 begins third-person Aoi-centered retrospective; P1092 returns first-person interior language. Independently checked. | Describe disclosure-framed, mixed-person internally focalized retrospective. Reader access to its rendered interiority does not establish that Tomozaki heard every thought or scene. Preserve the earlier reading and correct current downstream shorthand. |
| Kikuchi's phone-call agency | V11 `item/xhtml/p-0033.xhtml` P97 names failed reception; P98 states that the call ended. Independently checked. | Attribute her words to her; do not assign the physical hang-up act. Character, relationship, and any effort/ethics claims must narrow the action. |
| Spoken versus unspoken qualification of liking Hinami | V11 `item/xhtml/p-0019.xhtml` P239 is the spoken affirmative; P240 narrates a qualification Tomozaki considers and omits. Independently checked. | Do not claim Haruka heard the unspoken qualification or use it to establish permanent non-romance. CRI-REL-003 and associated relationship/character routes require review. |
| Punishment-language speaker | V05 `text/part0014.html` P34–41 contains Mizusawa's explanation; P46–47 attributes the attack/punishment reformulation to Tomozaki, followed by agreement. Independently checked. | Preserve the co-developed social mechanism while correcting exact lexical attribution in the social/voice layers. |
| Mizusawa's confession chronology | V03 deep reading §9 and V11 §5.5 distinguish the earlier confession/refusal from the unexecuted renewed declaration. | Narrow V11 open-state wording to renewed/formal confession; do not erase the earlier event. Review character, relationship, effort, CRI, and map references. |
| Mimimi's future emotional freedom | V07 deep reading §12 and the relationship ledger's response chronology; ESC-07 is the required primary-language route. | Do not convert freedom of future feeling into a specified waiting period or terminal stopping policy. Complete source-locator review before closing ESC-07. |
| Individual game versus set victory | V06 deep reading §4 and V11 §4.8 separate an individual win from the later 3–2 set victory. | V11 challenges Tomozaki's claimed unique credential; it is not Hinami's first individual-game win. Align effort, character, and relationship owners. |

At identification, the first five rows were primary verification findings and the last three retained L1 routes. The completed [source-locator audit](TOMOZAKI_TARGETED_SOURCE_LOCATOR_AUDIT.md) now records all twelve retrieval queues; the [reconciliation audit](TOMOZAKI_LONGITUDINAL_RECONCILIATION_AUDIT.md) records these and additional corrections, including teacher-question counterevidence, scoped refusal, current effort dispositions and voice recipients. Those receipts govern current use. This original queue is preserved as provenance.

## 5. Preservation, ownership, and tranche manifest

All author-created and author-modified analytical paths remain inside the existing Tomozaki analytical root. Source witnesses are read-only. Scratch stays in the analysis checkout and is never staged. The preserved thirteen readings, sequential README, source lock, bootstrap manifest, and immutable historical audits remain unchanged. The effort spine is not regenerated or shortened; any discovered correction must be a clearly dated downstream reconciliation, with a targeted spine correction only if actually required.

All literary drafting was stopped when the owner narrowed the task; no monograph draft was written. The later R01–R03 authorization used exclusive ownership for the character-state ledger, relationship-state ledger, and paired source-locator/voice artifacts, followed by independent parent review. Separate read-only review checked the effort/social changes and the longitudinal audit. No literary draft assignment carries forward automatically.

The historical authored staging allowlist for the completed identification tranche was:

1. `series/tomozaki/08 Audits and Manifests/TOMOZAKI_REMEDIATION_EXECUTION_INVENTORY.md` — new inventory and handoff only.
2. `series/tomozaki/CURRENT_STATE_AND_CORPUS_MAP.md` — a targeted link and task-boundary notice; no readiness promotion or substantive literary correction.

No global character-registry/index or housekeeping-owned output is assigned to this author. Existing curated Tomozaki records point to the preserved effort spine; new discovery may lag under repository policy.

## 6. Current execution receipt and handoff

R01–R03 began at `c20fa4359e34d549da3514a6106cda1756c1a962`; the initial fetch found `origin/series/tomozaki` at that same commit and `origin/main` unchanged at `b331a3b746622760db394ac1a79367263236336f`.

| Task | Current status and acceptance evidence |
|---|---|
| R01 | **PASS.** Five existing owners reconciled with the new voice input; all 29 EFFORT, 30 CS, 16 REL, 22 SOC, 36 CRI claim-family and 15 CRI question-family identities preserved and reviewed. Current corrections and OPENs propagate through the six-owner spine. |
| R02 | **PASS.** ESC-01–ESC-12 have exact locked witnesses, member/paragraph routes, diagnostic wording, attributed adjudication and independent context review; 49 locator records and 92 paragraph-specific diagnostics verified. Story uncertainty is not discharged. |
| R03 | **PASS at declared scope.** Twenty-four JVL rows cover seven principals through state, recipient, layer and exact-source controls. No complete habitual voice model is claimed. |
| R04 | **PARTIAL. Fumiya local literary role PASS** under the [integration review](TOMOZAKI_FUMIYA_R04_INTEGRATION_REVIEW.md). Hinami remains provisional and unfinished. |
| R05–R09 | **RESERVED literary work remains unfinished.** Kikuchi/Mimimi require mature monographs; Tama/Mizusawa/Yuzu require role adjudication and backfill; relationship/thematic specialists remain unfinished. |
| R10–R11 | **CLOSED.** Cross-specialist convergence and full-series revision depend on the deferred literary work. |
| R12 | **PARTIAL SUPPORT ONLY.** This tranche updates current routing, records its path/preservation manifest, and requires repository publication checks. It does not complete the future whole-corpus literary validation/release responsibility. |

Current completion evidence is the [longitudinal reconciliation audit](TOMOZAKI_LONGITUDINAL_RECONCILIATION_AUDIT.md), [targeted source-locator audit](TOMOZAKI_TARGETED_SOURCE_LOCATOR_AUDIT.md), and [voice ledger](../03%20Longitudinal%20Ledgers/TOMOZAKI_JAPANESE_VOICE_REGISTER_AND_KEY_TERMS_LEDGER.md). The exact authored allowlist and baseline preservation hashes for this execution are in [TOMOZAKI_R01_R03_PATH_AND_VALIDATION_MANIFEST.json](TOMOZAKI_R01_R03_PATH_AND_VALIDATION_MANIFEST.json); the earlier two-path allowlist in §5 is historical.

Acceptance requires independent semantic review, verified correction propagation, preserved source-facing and literary candidates, valid links/routing, applicable staged-tree validators, normal push, successful source audit, completed housekeeping and successful exact-head integration status. Publication checks remain separate from the analytical PASS; CI cannot promote the deferred literary roles. The later session must read the successful reconciliation and actual cumulative evidence before writing any monograph or synthesis.

### 6.1 Later Fumiya-only R04 integration

The owner-supplied candidate and handoff were reviewed against unchanged branch `919b71662a8be869f648f34120aae8493c37897f`; current main remained `b331a3b746622760db394ac1a79367263236336f`. The candidate replaces only Fumiya’s earlier provisional monograph at its existing path. Independent review and integrating-agent verification corrected bounded wording, preserved the owned-reason-to-play OPEN, and accepted the local §7.3 responsibility. Character-state §6.6, relationship §6.1 and effort §31.5 receive exact-source ordinary-life enrichment without new claim families. The original R01–R03 manifest and audits remain unchanged historical receipts for their own snapshots.

The [integration review](TOMOZAKI_FUMIYA_R04_INTEGRATION_REVIEW.md) and [ten-path manifest](TOMOZAKI_FUMIYA_R04_PATH_AND_VALIDATION_MANIFEST.json) govern this later authored delta. All six other character candidates and the full-series candidate remain unchanged. R04 overall, R05–R11 and whole-corpus R12 release remain unpassed; publication checks certify only the exact repository revision.
