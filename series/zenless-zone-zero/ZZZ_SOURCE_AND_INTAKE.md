---
title: "Zenless Zone Zero — Source, intake and channel register"
artifact_id: ZZZ_SOURCE_AND_INTAKE
artifact_type: source_lock_coverage_and_intake_register
series: zenless-zone-zero
version: "1.0"
generation: INITIAL_BOOTSTRAP
status: canonical
scope: "Source, intake and channel register"
authority_scope: source_bounded_initial_design_only
source_boundary: "Historical target-projection metadata only; native source lock unbound; no narrative or AV inspection and no admitted units"
canonical_home: series/zenless-zone-zero/ZZZ_SOURCE_AND_INTAKE.md
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
---

# Zenless Zone Zero — source, coverage and intake

## Observed source versus admitted source

Reserved public alias `ZZZ-TARGET-20260823` refers to the metadata-described Anby target projection; it is **not yet bound to an independently verified native fingerprint**. Historical version label: 3.1.0; observation date: 2026-11-07. Native/build manifest references appear in the reports, but their existence and byte identity were not verified in the listed subtree. The metadata reports CHS primary text with aligned parallel localizations. No native records, normalized narrative nodes, audio or runtime images were substantively inspected.

The source layer reports readiness `PARTIAL` for a requested behavioral profile with main-story dialogue blocking. Preserve its exact narrow scope. These counts are historical reported units, not present independent measurements; classes overlap and must not be summed into a corpus size:

| Reported class | Count | Reported status | Meaning / limit stated by prior report |
|---|---|---|---|
| main_story_dialogue | 28 | PARTIAL | Explicit Anby-labelled ongoing text is recovered; broader primary-story graph attribution remains schema-blocked. |
| character_story_dialogue | 18 | PARTIAL | The Anby archive chain and explicitly labelled ongoing text are recovered; mixed-speaker GalGame scene text remains unattributed. |
| trust_dialogue | 78 | PARTIAL | Anby date graphs, explicitly labelled tips, and joined bubble assets are recovered; unbound fragments remain independent and broader Trust coverage is not claimed. |
| private_messages | 303 | PARTIAL | Message rows are parsed; contact-to-partner identity resolution is partial. |
| social_posts | 0 | ABSENT_NOT_INGESTED | Inter-Knot posts/comments are parsed with conservative attribution. |
| profiles | 6 | COMPLETE_FOR_DECLARED_SCOPE | Known partner profile fields are extracted with documented mappings. |
| profile_voice | 0 | NOT_IMPLEMENTED | Dedicated agent voice-line extraction is not implemented. |
| audio_metadata | 0 | NOT_IMPLEMENTED | No approved Tier-D audio provider is configured. |
| spoken_dialogue | 427 | PRESENT | Character-attributed canonical nodes. |
| context_preserved | 365 | PRESENT | Adjacent graph or same-scene context exists. |
| multiple_situational_contexts | 107 | PRESENT | Distinct source StoryUnits provide non-interpretive situational boundaries. |

Projection “spoken dialogue” means attributed text nodes, not audio heard. Source-order coordinates do not establish diegetic chronology. Declared-scope completeness of profiles is not subject or full-game completeness. The report's advice on possible safe uses is not an analytical run approval. Full restricted locations and technical receipts remain in governed private source records.

## Admission blockers and next evidence

| ID | Gap | Required next operation |
|---|---|---|
| ZZZ-SRC-01 | Native source/build identity unbound | Locate approved immutable manifest, native hashes, region/platform/language and extraction/normalization lineage; verify alias binding |
| ZZZ-SRC-02 | Main-story foundation incomplete | Recover missing timeline/graph sources and full-unit context for proposed horizon; classify remaining exclusions explicitly |
| ZZZ-SRC-03 | Partner/contact/speaker joins are partial; mixed-speaker scene fragments and unresolved graph branches remain unbound. | Adjudicate native keys/joins and graph reachability; preserve unknown candidates |
| ZZZ-SRC-04 | Social-post coverage is zero/ABSENT_NOT_INGESTED despite parsed-table notes; distinguish surface ingestion from target-attributed coverage. | Compare exact target-specific source sets and earlier report logic; append correction without overwriting provenance |
| ZZZ-SRC-05 | Native locator grammar and branch coverage unverified | Verify resolver/index conventions and crosswalk every admitted projection to native records/all choice paths |
| ZZZ-SRC-06 | Audio/runtime channels uninspected or unavailable | Bind actual assets and playback/runtime contexts for any proposed performance claim; otherwise keep those claims unavailable |

Metadata is sufficient to design this CLOSED bootstrap; these gaps block source admission and affected substantive conclusions, not architectural review. No character-first reading is authorized as a workaround.

## Lock, coverage and source-delta contracts

**Lock row unit:** immutable native witness plus a versioned projection. Fields: public alias, game/build/region/platform/language, native fingerprint and private receipt reference, upstream revision, normalization/tool versions, transformations, source classes, exact member-set digest, locator grammar version, admitted scope and limitations. A changed native corpus receives a new alias/version and predecessor crosswalk before citation changes. No current bound lock rows exist.

**Coverage row unit:** one native script/story unit or independently bounded graph, not each target view. Fields: unit ID, lock, source class and narrative function, membership/choice-path manifest, dedup identities, ordering basis, state selectors, `inventoried`, `admitted`, `screened`, `narratively_reconstructed`, `closely_analyzed`, `integrated`, `av_review`, missing members and next obligation. Update on actual inspection/admission/accepted reading; record gaps as sets, not highest-number frontier. Current narrative unit rows: **none**.

**Source delta row unit:** one addition/removal/revision/reupload/rerun. Fields: old/new identity, byte/semantic change basis, impacted source units and locators, dependent claims, new verification duties and disposition. A rename or byte-identical rerun adds no narrative evidence. Preserve historical rows and source receipts.

## Relevance, impact and freshness

**Intake row unit:** one release with exact source membership and scope routing. Fields: release/lock, represented scopes, source functions, relevance `PRIMARY/SECONDARY/CROSS_GROUP/INCIDENTAL/NONE/UNRESOLVED`, native locators and exclusions; separate impact `DEFERRED_PENDING_FOUNDATION` or I0/I1/I2/I3 only after baseline exists; required reading/claim/state/model updates, responsible reviewer and disposition. Screen a complete release once, reuse that record for later target retrieval, and record any scope not screened. Current release screening: **not performed**.

**Freshness row unit:** one analytical scope/artifact. Track source-current, analysis-current, reconstruction-current, pending I2/I3, last actual retest and source lock. Advances require completed affected work, not new source arrival. Current analysis/reconstruction horizons are EMPTY for every scope.

## AV and missing-channel queue

**Queue row unit:** one claim-relevant scene/channel need. Fields: source lock/unit/state, exact cue/native reference, proposed claim, required lane, resolved asset/runtime witness, inspection status, gap consequence, priority and next owner. Update when a text reading raises a question or the asset is actually inspected; resolved text or metadata never marks AV done. No claim-driven rows exist before reading. The source-level ZZZ-SRC-06 gap is open; direct listening/viewing none.

## Control history

| Date | Event | Consequence |
|---|---|---|
| 2026-11-07 | Historical target metadata and immediate source hierarchy reconciled | Six source admission obligations open; no narrative, audio or runtime admission; lock CLOSED |
