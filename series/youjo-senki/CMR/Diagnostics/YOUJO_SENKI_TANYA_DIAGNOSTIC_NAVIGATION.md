---
series: YOUJO_SENKI
artifact_id: YOUJO_SENKI_TANYA_DIAGNOSTIC_NAVIGATION
artifact_type: interpretive_diagnostic_navigation
scope: "Tanya CMR2B V01-V14 analytical diagnostics; 676 preserved inherited and 138 new source-reviewed records"
generation: V2_CMR
version: "1.1"
status: active_provisional
canonical_home: "series/youjo-senki/CMR/Diagnostics/YOUJO_SENKI_TANYA_DIAGNOSTIC_NAVIGATION.md"
source_index_drive_id: "1i1Ov7u5yGciH55j-04LxIR4CWck61-KH"
source_index_revision: "0B24avie5yJngK0Y5Y0dlSytHNDE1NjI5RjRWdyt5RDFNN2NRPQ"
source_index_sha256: "1240953f6174375e64ddf1eb44af83954984a438c4b2fbc5d8869dabcf42ce68"
frozen_predecessor_copy_drive_id: "1v67_7wmkiYnXE1LJ_okzpR9tNk8ANws9"
current_cumulative_index_sha256: "2b5fbc8caa711ee2c71a028a093b877df8b1335207352528cf9043d2349dc387"
source_event_id: "YS-CMR2-SOURCE-APPEND-2026-10-12"
review_basis: "INHERITED_V01_V12_SOURCE_ADJUDICATION; EXACT_LOCATOR_AND_HASH_REVALIDATED; NOT_FULL_REOPEN_IN_THIS_PORT"
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
---

# Tanya V01-V14 interpretive diagnostic navigation

This surface routes **814 provisional diagnostics** into English findings, conditional states, five separate evidence channels and exact Japanese source coordinates. It combines 676 preserved inherited V01–V12 records with 138 newly source-reviewed V13–V14 records. Every stable ID, substantive finding, counterexample and inference ceiling is retained or explicitly mapped. The inherited port does not claim a second complete Japanese semantic reread; later source adjudication uses bounded contiguous review, not a full-book census.

These JSONL files are controlled analytical derivatives. They retain authored behavioral/linguistic interpretation, exclude Japanese scene-anchor/transcription columns, and expose inherited actor uncertainty. Small address/register forms and specifically preserved lexemes are diagnostic-scoped written-voice facts, not reusable scene quotations or universal character voice.

The admitted primary corpus remains Japanese V01–V14. **All five files below cover that boundary.** The [source closure audit](../Provenance/YOUJO_SENKI_TANYA_CMR2_V14_CLOSURE_AUDIT.md), [44-family register](TANYA_OPERATIONAL_RULE_REGISTER.md) and [complete ID-to-rule crosswalk](TANYA_DIAGNOSTIC_TO_RULE_CROSSWALK.jsonl) retain preservation, chronology and application limits. Source closure establishes no completed model or held-out QA. Follow [the series current-state entrypoint](../../CURRENT_STATE_AND_CORPUS_MAP.md) for current state and [the reconstruction method](../Methods/YOUJO_SENKI_CHARACTER_MODELING_REFERENCE_METHOD.md) for governing constraints.

## Files and stable-ID lookup

| File | Records | Bytes | SHA-256 |
|---|---:|---:|---|
| [TANYA_DIAGNOSTICS_V01_V04.jsonl](TANYA_DIAGNOSTICS_V01_V04.jsonl) | 210 | 743,411 | 300a02bf7b773a754df12b3082d46c6294307aebe72b5b726f585905ce387408 |
| [TANYA_DIAGNOSTICS_V05_V08.jsonl](TANYA_DIAGNOSTICS_V05_V08.jsonl) | 198 | 729,396 | e9503850f4079a622e62868656e37d2faf05280def973d83ad4b398858f94875 |
| [TANYA_DIAGNOSTICS_V09_V12.jsonl](TANYA_DIAGNOSTICS_V09_V12.jsonl) | 268 | 914,914 | ce8c501b2892f82c95fffdaec7b84d072d7c6ed3025134a7b76a572b9e69e321 |
| [TANYA_DIAGNOSTICS_V13.jsonl](TANYA_DIAGNOSTICS_V13.jsonl) | 82 | 922,273 | c9ec85e6616f7b1ae81bc95aa5c0811d59b6f6ced6a1a1a4fb8145f390081a18 |
| [TANYA_DIAGNOSTICS_V14.jsonl](TANYA_DIAGNOSTICS_V14.jsonl) | 56 | 461,646 | 01f322f5d6f494d979de81c0b33863203dd856a4d7c8ee530c643f4ecbf2e82a |

One physical JSONL line contains one complete object. IDs retain `YS-TAN-CMR2-VNN-NNN`; the volume selects the file. Search the exact ID there, for example:

```text
rg -n -F "YS-TAN-CMR2-V12-032" series/youjo-senki/CMR/Diagnostics/TANYA_DIAGNOSTICS_V09_V12.jsonl
```

Per-volume records are V01 55, V02 54, V03 46, V04 55; V05 59, V06 41, V07 53, V08 45; V09 69, V10 71, V11 68, V12 60. V13 has 82 and V14 has 56 records. All 814 textual IDs are unique; the inherited 676 remain unchanged. Candidate IDs preserve retrieval history: one candidate may support several diagnostics and several candidates may support one diagnostic, while a retrieval-missed supplement can have none. The conditional crosswalk retains every witness.

## Reopen the exact source

The public Git route uses verified Drive IDs. Source labels link to the project-local disposition index, which records original object identity and parents; use its `drive_id` in Drive lookup. This preserves exact source navigation without adding publication-unsafe external Drive URLs.

The `source` tuple identifies the source EPUB, locked hashes, OPF/member, spine index, textual-block ordinal and locator ID. Supporting IDs are separately retained.

1. Open the EPUB with `source.epub_drive_id` within the [Japanese source root](../Provenance/YOUJO_SENKI_CMR_DRIVE_DISPOSITION.jsonl) (Drive folder ID `1s8Ido1uUbAyR-lXstTyOVfoeHaUDop-g`). Match `epub_filename` and verify its bytes against `epub_sha256`. A later/differently packaged edition is not the locked witness.
2. Open the EPUB as ZIP and locate `member_path` in the package identified by `opf_path`. `spine_index` is the original OPF reading-order position, not filename-sort order.
3. Find `locator_id` in the [CMR0 locator index](../Provenance/YOUJO_SENKI_CMR_DRIVE_DISPOSITION.jsonl) (Drive file ID `140ow12czVj4J8Q_JR44MSWI98LUxj3uk`). `paragraph_ordinal` is the deterministic textual-block ordinal within the member, not a reader page. The extractor counts non-empty paragraph, heading, list-item and related blocks while avoiding nested duplicates.
4. Reopen that source member with enough preceding/following text to resolve actual speaker, focalizer, chronology, role and communicative setting. The normalized text must reproduce `text_sha256` and member bytes `member_sha256`. Exact typography/ruby/spacing requires the XHTML, not normalized retrieval text.
5. Resolve each relevant `supporting_locator_ids` through CMR0 and inspect its own source tuple. A support route does not automatically make its speaker or appraisal Tanya.

The [member index](../Provenance/YOUJO_SENKI_CMR_DRIVE_DISPOSITION.jsonl) (Drive file ID `1GlDNvT5spgIQk5VaUU5S2Qsk5dF174hR`) supplies the compact package/spine map; the [audited extractor](../Provenance/YOUJO_SENKI_CMR_DRIVE_DISPOSITION.jsonl) (Drive file ID `1l8ok-FT2RMmDl-qeXJnVaj8hrS7pzKeu`) defines ordinals and normalization. Source-only Japanese anchors and extracted scene text remain in Drive.

## Later-volume extensions and current source home

The V13/V14 objects preserve the same analytical responsibilities while adding scene-reviewed `speaker_certainty`, `focalizer_certainty`, `private_access_type`, primary-anchor assignment, inspected-window references, explicit channel availability, six-step causal assessments and point-in-time chronology. V13-001 is 21 January 1928 at Balk Bridge, after the 14 January forgery; textual/source-ID order is not chronological order. Root V13-001–025 remain separately unscored context-review records; the remaining 113 later records expose their scene-bounded actor assessments. HIGH finding confidence does not override these bands. Draft/self-directed/narrated wording and other-speaker contextual anchors do not become oral Tanya lines.

The current 814-row Drive index at the original stable ID `1i1Ov7u5yGciH55j-04LxIR4CWck61-KH` is 1,353,865 bytes, SHA-256 `2b5fbc8caa711ee2c71a028a093b877df8b1335207352528cf9043d2349dc387`. Its exact frozen 676-row predecessor is separately preserved at `1v67_7wmkiYnXE1LJ_okzpR9tNk8ANws9`. [The source-append disposition](../Provenance/YOUJO_SENKI_CMR_SOURCE_APPEND_DISPOSITION.jsonl) binds current versions, copy IDs, hashes, successors and safe analytical responsibilities; the original intake remains a dated historical snapshot.

## Documented object schema

Schema: `youjo-senki/tanya-interpretive-diagnostic/v1`. Empty strings preserve unpopulated legacy fields. They do not prove absence of motive, speech, body state or relationship. Literal `N/A` explanations remain intact.

| Field | Meaning |
|---|---|
| `schema` | Names this analytical schema. |
| `diagnostic_id`, `character`, `status` | Original witness identity/subject and `active_provisional` derivative status. Subject is not automatically every channel’s focalizer. |
| `source.volume` | Original volume/knowledge horizon. |
| `source.epub_drive_id`, `epub_filename`, `epub_sha256` | Locked primary identity and byte integrity. |
| `source.opf_path`, `member_path`, `member_sha256`, `spine_index` | Package/member/reading-order route and member integrity. |
| `source.paragraph_ordinal`, `locator_id`, `text_sha256` | Deterministic block route and normalized-text integrity. |
| `source.supporting_locator_ids` | Original support IDs in recorded order; every route checked. |
| `source.source_candidate_ids` | Original candidate history IDs in recorded order. |
| `attribution.statement` | Literal prior `pov_source`, never normalized into a stronger actor assertion. |
| `attribution.certainty` | `NOT_SEPARATELY_SCORED_LEGACY`, separate from diagnostic confidence. |
| `attribution.generic_caveat_present` | Flags “unless otherwise” attribution. Such a caveat is not definitive actor evidence. |
| `condition` | Twelve original state/relationship/situation fields below. |
| `channels` | Five separate responsibilities below. |
| `speech_transform` | Six-stage retrieval references; surface source text excluded. |
| `finding.paraphrase` | Full prior `diagnostic_responsibility`, subject only to the explicitly reviewed microquotation mappings. |
| `evidence.modes_literal`, `mode_mapping` | Literal mode labels and the shared explicit tag mapping below. |
| `evidence.class_literal`, `confidence`, `legacy_review_status` | Original evidence classes, qualitative diagnostic confidence and review status. |
| `limits.counterevidence_or_exception`, `inference_ceiling` | Complete prior limits and forbidden inference jumps. |
| `written_voice_facts` | Specifically preserved microlexemes/forms, each with `source_field`, `lexeme`, `kind` and diagnostic-only `scope`. |
| `review_basis` | Exact inheritance/revalidation statement below. |
| `provenance_ref` | Routes to this document’s frozen integrity bindings. |

The twelve `condition` fields are `developmental_state`, `rank_role`, `interlocutor`, `relationship_class`, `power_relation`, `setting`, `stakes`, `immediate_objective`, `emotional_state`, `physical_state`, `information_state` and `attention_target`. They are not filled from later volumes or a generic trait model.

The five `channels` are:

- `private_cognition.private_appraisal`: literal inherited appraisal. Check attribution/content first; this can describe an observer’s appraisal or explicitly say ordinary-Tanya cognition is unavailable.
- `observable_behavior`: inherited behavior/action, with the specifically recorded contextual English microquotation mappings.
- `public_speech`: thirteen inherited speech/transform fields: `speech_act`, `communicative_objective`, `withheld_private_content`, `speech_act_subtype`, `directness_level`, `politeness_register`, `address_form`, `disagreement_strategy`, `disclosure_level`, `humor_sarcasm_mode`, `utterance_length_class`, `register_observations` and `surface_voice_notes`. **Withheld content describes what was not said; its storage here never makes it public dialogue.**
- `external_interpretation`: others’ readings, not transparent access to Tanya’s motive.
- `institutional_consequence`: separately recorded organizational effect; blanks do not authorize invented promotions or outcomes.

## Six-step speech transformation

The required causal chain remains `private appraisal -> communicative objective -> speech act -> relationship/role constraint -> register -> surface wording`.

| Stage field | Resolution |
|---|---|
| `private_appraisal_ref` | `channels.private_cognition.private_appraisal` |
| `communicative_objective_ref` | `channels.public_speech.communicative_objective` |
| `speech_act_ref` | `channels.public_speech.speech_act` |
| `role_relationship_ref` | Top-level `condition`, especially rank/role, interlocutor, relationship class and power relation |
| `register_ref` | `channels.public_speech`, especially politeness/address/directness/disclosure/disagreement/humor |
| `surface_wording` | Always `SOURCE_TEXT_EXCLUDED`; reopen source and consult preserved register/voice notes and microlexemes |

References are relative to `channels` except top-level `condition`. These are retrieval controls, not fabricated utterances. A blank communicative objective is not automatically the situational objective. External-observer/Type95 states retain actor/causality restrictions. Decision fidelity and Japanese surface fidelity remain independent.

## Explicit mode-to-channel mapping

`LEGACY_FIVE_CHANNEL_TAG_MAP_V1` splits `evidence.modes_literal` on `|` and treats the following original labels as retrieval hints. No actor certainty or new evidence confidence follows from projection.

| Channel hint | Literal tags |
|---|---|
| Private cognition | `private_cognition`, `private_appraisal`, `private_affect`, `private_reaction`, `internal_voice`, `private_motive_inferred_from_direct_statement` |
| Observable behavior | `observable_behavior`, `observable_action`, `observable_affect`, `observable_exterior`, `public_behavior`, `public_action`, `command_behavior`, `combat_behavior`, `combat_action`, `nonverbal_behavior`, `relationship_behavior` |
| Public speech | `public_speech`, `public_command`, `public_comment`, `public_order`, `public_orders`, `public_praise`, `public_guidance`, `public_feedback`, `public_self_speech`, `public_or_self_speech`, `coerced_speech`, `coerced_public_speech`, `coerced_sacred_speech`, `superior_facing_speech`, `professional_peer_speech`, `staff_speech`, `speech_interaction`, `external_observer_speech` |
| External interpretation | `observer_interpretation`, `external_interpretation`, `external_observer`, `external_observer_speech`, `observer_misinterpretation`, `observer_misreading`, `observer_inference` |
| Institutional consequence | `institutional_effect`, `institutional_consequence` |

`private_public_divergence`, `private_public_transformation` and `public_private_divergence` provide both private/public hints. All other literal tags remain contextual/analytical dimensions without forced channel attribution. A tag such as humor, career, body_age, institutional_learning or reputation does not alone establish actor or consequence. External-observer speech can supply several channel hints. Inferred private motive remains inference; public-or-self speech retains audience ambiguity.

Inherited V01–V12 diagnostic confidence remains **619 HIGH / 57 MODERATE**. The complete V01–V14 inventory is 748 HIGH / 66 MODERATE; these are finding confidence, not speaker/focalizer certainty. Inherited labels do not provide separately scored speaker/focalizer certainty; later records declare their own scene-bounded assessments as documented above. **450 records** retain generic attribution caveats; non-generic statements are also separately unscored in this inherited port.

## Curated thematic routes

Selected complete inherited rows were read to check these navigation summaries. They supplement the full records and ceilings; they are not new canonical dialogue or held-out validation.

| Contrast/question | Actual IDs | Navigation purpose and limit |
|---|---|---|
| Peace preference with military duty | `YS-TAN-CMR2-V11-017`; `YS-TAN-CMR2-V10-064` | Peace/order and opposition to pleasure killing coexist with lawful force. Staying to cover slower allies can oppose private withdrawal preference. Neither establishes absolute pacifism or love of danger. |
| Institutional feedback and assignment pressure | `YS-TAN-CMR2-V04-026`; `YS-TAN-CMR2-V04-054`; `YS-TAN-CMR2-V07-044` | Inquiry can damage institutional trust; senior “dangerous but useful” or “hound” readings can cause further risky tasking. Reputation cannot overwrite private rear-duty motives. |
| Role/state and legitimate disagreement | `YS-TAN-CMR2-V03-028`; `YS-TAN-CMR2-V12-032` | Major/radio-policy dissent requires anger regulation; later trusted-deputy conversation permits more candor while still withholding harsh private assessment. These do not average into one register. |
| Appraisal withheld from wording | `YS-TAN-CMR2-V11-018`; `YS-TAN-CMR2-V12-032` | Salary/exit calculus is not spoken verbatim in the peace/duty explanation; harsh Zettour judgments become milder wording with Weiss. Withholding does not make public values fake. |
| Ordinary/material texture | `YS-TAN-CMR2-V03-025`; `YS-TAN-CMR2-V09-056`; `YS-TAN-CMR2-V12-014`; `YS-TAN-CMR2-V10-071` | Coffee preference, proper porcelain, coffee/chocolate reciprocity, leave jokes and pineapple interest preserve mundane behavior. Coffee does not prove absolute alcohol refusal; care does not prove romance. |
| Access rights versus consumption habit | `YS-TAN-CMR2-V05-026` | Club exclusion concerns paid-for access/legal standing; alcohol/tobacco are explicitly irrelevant to the dispute. Do not infer drinking or smoking taste. |
| Relationship-specific interaction | `YS-TAN-CMR2-V11-038`; `YS-TAN-CMR2-V12-049`; `YS-TAN-CMR2-V12-014` | Lergen’s culinary black humor relies on shared grim context; Uger can correct a hypothesis; Visha’s care is reciprocated with a valued sweet. These registers do not globalize. |
| Body/orientation false positives | `YS-TAN-CMR2-V02-025`; `YS-TAN-CMR2-V09-033`; `YS-TAN-CMR2-V10-071` | “Normal” concerns religious-fanatic reputation; Schugel imposes parental metaphor; leave/food pleasure is not attraction evidence. No modern orientation or categorical gender conclusion follows. |
| Error/regulation/repair | `YS-TAN-CMR2-V03-028`; `YS-TAN-CMR2-V05-050`; `YS-TAN-CMR2-V12-049` | Anger is regulated; Meybert counterexample restrains premature Tohn judgment; Uger correction is accepted. These limit omniscience, uncontrolled rage and compulsory face-saving. |
| Type95 surface versus ordinary cognition | `YS-TAN-CMR2-V05-039` | Sacred ecstatic-looking combat and Visha’s interpretation remain quarantined from ordinary chosen religiosity/motive/voice. Ordinary-Tanya appraisal is explicitly unavailable in this witness. |

## Provenance and integrity

Frozen historical source: [YOUJO_SENKI_TANYA_CMR2_DIAGNOSTIC_EVIDENCE_INDEX.tsv](../Provenance/YOUJO_SENKI_CMR_DRIVE_DISPOSITION.jsonl) (Drive file ID `1i1Ov7u5yGciH55j-04LxIR4CWck61-KH`), intake revision `0B24avie5yJngK0Y5Y0dlSytHNDE1NjI5RjRWdyt5RDFNN2NRPQ`, 1,043,995 bytes, SHA-256 `1240953f6174375e64ddf1eb44af83954984a438c4b2fbc5d8869dabcf42ce68`. The original stable ID has advanced through V14. The exact predecessor bytes are now retrieved from frozen copy `1v67_7wmkiYnXE1LJ_okzpR9tNk8ANws9`, independently read back before the append. Its actual 45-column header governs the inherited mapping. If the Drive object advances, do not call newest bytes this frozen hash: use the bound revision or preserved-history/current evidence crosswalk, retaining stable IDs.

Locator: [YOUJO_SENKI_CMR_SOURCE_LOCATOR_INDEX.tsv](../Provenance/YOUJO_SENKI_CMR_DRIVE_DISPOSITION.jsonl) (Drive file ID `140ow12czVj4J8Q_JR44MSWI98LUxj3uk`), 52,894,654 bytes, SHA-256 `c84fa4c8e0251730887b51913a8f32ea68c39be68ff4adae8d995d49292f5cfe`. This port used the identical deterministic rebuild and claims no current giant-Drive-body materialization. Member map: [YOUJO_SENKI_CMR_SOURCE_MEMBER_INDEX.tsv](../Provenance/YOUJO_SENKI_CMR_DRIVE_DISPOSITION.jsonl) (Drive file ID `1GlDNvT5spgIQk5VaUU5S2Qsk5dF174hR`), 203,927 bytes, SHA-256 `e05b9fe26ec35e4590b9e148005b49f7ed142ec2f6ca2868e99561981372e220`.

Primary/supporting references resolve to **2,497 unique validated CMR0 locators**. Each normalized text reproduces its hash and source EPUB/member coordinates match the member index. Primary tuple prefixes match original diagnostic routes. The 676 previous IDs and 40 substantive identity/state/channel/finding/confidence/limit fields are retained or explicitly mapped. Two source-anchor columns are excluded; three route columns become typed coordinates/history IDs.

Seventeen short Japanese citation cells receive contextual English mappings. Ten small address/register cells remain analytical forms; specifically retained microlexemes remain diagnostic-scoped written-voice facts. The [public field-mapping record](../Provenance/TANYA_INTERPRETIVE_FIELD_MAPPING.json) binds exact source/target cell digests and safe target paraphrases. The private controlled receipt additionally preserves the original source cell strings, retained lexemes, all field mappings, source/destination hashes, root’s independent review and four requested grammar repairs. No other substantive value is revised. English mappings are analytical paraphrases, not official translation or canonical English dialogue. Full Japanese utterance quotes and scene anchors are excluded.

Exact review basis, present in every object:

`INHERITED_V01_V12_SOURCE_ADJUDICATION; EXACT_LOCATOR_AND_HASH_REVALIDATED; NOT_FULL_REOPEN_IN_THIS_PORT`

Root reviewed all seventeen inherited mappings. The three V01–V12 files were published and passed exact-commit source, housekeeping and final audits at checkpoint 01; the later files and maintained navigation remain a continuing branch package pending their own publication/integration checks. Generated dialogue and missing-field guesses never enter this evidence layer.
