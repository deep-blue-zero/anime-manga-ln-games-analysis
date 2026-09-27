---
title: "Mushoku Tensei - Current State and Corpus Map"
artifact_id: MT_CURRENT_STATE_AND_CORPUS_MAP
artifact_type: corpus_map
series: "Mushoku Tensei"
generation: "V1"
version: "1.17"
status: canonical
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
do_not_use_as_literary_evidence: true
created: "2026-09-25"
adoption_basis_commit: "a2a1ab9a5ecd0512a5ac460c1b79655af1bca0bd"
source_boundary: "Japanese LN V01–V15 inspected; V01–V14 published/audited at preparation, V01–V06 verified on main; V15 content/publication separate; terminal authorized source."
---

# Mushoku Tensei — current state and corpus map

This is the single first-read surface for `series/mushoku-tensei/`. Git owns interpretation; private Drive folder `1bx_IkoTqVZy9I8SmcyGvgRmj3JX0Rjug` owns primary/derived evidence. The owner-approved [V01 pilot](02%20Sequential%20Readings/MT_V01_DEEP_READING.md) is closed and audited. [V02](02%20Sequential%20Readings/MT_V02_DEEP_READING.md) is published and finally audited at `687a13ac1a661270ab566c9e1a6028acd607d846`. [V03](02%20Sequential%20Readings/MT_V03_DEEP_READING.md) is published and finally audited at `56e1daa4bdc287cb9f2f3e4abbbea30be494628d`. [V04](02%20Sequential%20Readings/MT_V04_DEEP_READING.md) is published and finally audited at `f3dfe47b549cf33fddc7d2128e2b6f0bba7a8e8e`. [V05](02%20Sequential%20Readings/MT_V05_DEEP_READING.md) and its [first cumulative checkpoint](05%20Checkpoint%20Syntheses/MT_V01_V05_CHECKPOINT.md) are published and finally audited at `3dc6b173b044abdafc013dc989bd96914620d13d`. [V06](02%20Sequential%20Readings/MT_V06_DEEP_READING.md) records complete prose, image and paratext inspection, retained byte-verified map, 31 observations, synchronized ledgers/model revisions and a [targeted disclosure checkpoint](05%20Checkpoint%20Syntheses/MT_V06_DISCLOSURE_CHECKPOINT.md). V06 is published and finally audited at `0e72e531278055c0dbb7a6054285337a1cc37a93`. [V07](02%20Sequential%20Readings/MT_V07_DEEP_READING.md) adds a complete nine-unit reading, 30 observations, six ledger updates, a Rudeus revision, first Sara model and [recognition checkpoint](05%20Checkpoint%20Syntheses/MT_V07_RECOGNITION_CHECKPOINT.md). V07 is published and finally audited at `523625ec4a57b95dec7d5acbb217bae5cc7ba5d3`. [V08](02%20Sequential%20Readings/MT_V08_DEEP_READING.md) adds thirteen-unit coverage, thirty observations, six ledger updates, Rudeus revision 1.5, first bounded Zanoba/Sylphiette packages and a [consent and institutional-power checkpoint](05%20Checkpoint%20Syntheses/MT_V08_CONSENT_AND_INSTITUTION_CHECKPOINT.md). V08 is published and finally audited at `210894fd2b5894b7e499bab80251e8f5ea761138`. [V09](02%20Sequential%20Readings/MT_V09_DEEP_READING.md) adds fifteen-unit coverage, thirty-five observations, six ledger updates, four model revisions, first Cliff/Nanahoshi packages and a [disclosure and recovery checkpoint](05%20Checkpoint%20Syntheses/MT_V09_DISCLOSURE_AND_RECOVERY_CHECKPOINT.md). V09 is published and finally audited at `40018b5caedfba456da199ed2fea613ec991015a`. [V10](02%20Sequential%20Readings/MT_V10_DEEP_READING.md) adds fourteen-unit coverage, thirty-four observations, six ledger updates, nine model revisions, first Elinalise package, a [Rudeus monograph](04%20Character%20Analysis/rudeus/CHARACTER_MONOGRAPH.md) and the required [V01–V10 cumulative checkpoint](05%20Checkpoint%20Syntheses/MT_V01_V10_CHECKPOINT.md). V10 is published and finally audited at `4823e7f9cecff45d86f3045304b5825c79bcb628`. [V11](02%20Sequential%20Readings/MT_V11_DEEP_READING.md) adds16-unit coverage,35 observations, six ledger updates, six model revisions, first Norn/Aisha packages and a [knowledge/duty checkpoint](05%20Checkpoint%20Syntheses/MT_V11_KNOWLEDGE_AND_DUTY_CHECKPOINT.md). V11 is published and finally audited at `0670b4dfc16a7a5a6c0e35dc62d520f90758a3a5`. [V12](02%20Sequential%20Readings/MT_V12_DEEP_READING.md) adds16-unit coverage,34 observations, six ledger updates, seven model revisions and a [loss/household checkpoint](05%20Checkpoint%20Syntheses/MT_V12_LOSS_AND_HOUSEHOLD_CHECKPOINT.md). V12 is published and finally audited at `e1018971ce195163277565ca1e4e7e298332bb21`. [V13](02%20Sequential%20Readings/MT_V13_DEEP_READING.md) adds13-unit coverage,37 observations, six ledger updates and eleven model revisions. V13 is published and finally audited at `eece6816d98e076847e65507bc9e83d03b1ed77d`. [V14](02%20Sequential%20Readings/MT_V14_DEEP_READING.md) adds12-unit coverage,36 observations, six ledger updates, eight model revisions and a [testimony/agency checkpoint](05%20Checkpoint%20Syntheses/MT_V14_TESTIMONY_AND_AGENCY_CHECKPOINT.md). V14 is published and finally audited at `992e696dabd6acf5646e3498a5fd20c46267c580`. [V15](02%20Sequential%20Readings/MT_V15_DEEP_READING.md) adds14-unit coverage,38 observations, six ledger updates, ten model revisions, the [mandatory cumulative checkpoint](05%20Checkpoint%20Syntheses/MT_V01_V15_MAINTENANCE_CHECKPOINT.md) and a [new scoped Rudeus monograph](04%20Character%20Analysis/rudeus/CHARACTER_MONOGRAPH_V01_V15.md). V15 is terminal; its publication closure requires the containing commit's exact final audit.

## Project initialization

```yaml
project_initialization:
  status: canonical
  architecture_lifecycle: EVOLVING
  analytical_phase: V15_CONTENT_AND_EVIDENCE_CLOSED_PUBLICATION_AUDIT_SEPARATE
  source_reconnaissance_complete: true
  governing_method: "00 Frameworks and Methods/MT_ANALYTICAL_METHOD.md"
  method_status: canonical
  synthesis_architecture: "00 Frameworks and Methods/MT_SERIES_ARCHITECTURE.md"
  architecture_status: canonical
  reconstruction_specification: "00 Frameworks and Methods/MT_CHARACTER_RECONSTRUCTION_SPEC.md"
  reconstruction_specification_status: canonical
  required_day_one_infrastructure_initialized: true
  required_day_one_infrastructure:
    - "03 Longitudinal Ledgers/MT_CHARACTER_STATE_AND_READINESS_LEDGER.md"
    - "03 Longitudinal Ledgers/MT_CHRONOLOGY_AND_KNOWLEDGE_LEDGER.md"
    - "03 Longitudinal Ledgers/MT_CLAIMS_AND_REVISIONS_LEDGER.md"
    - "03 Longitudinal Ledgers/MT_FORM_THEMES_AND_WORLD_LEDGER.md"
    - "03 Longitudinal Ledgers/MT_NORMATIVE_FRAMING_LEDGER.md"
    - "03 Longitudinal Ledgers/MT_RELATIONSHIP_AND_AGENCY_LEDGER.md"
  sequential_analysis_lock: OPEN
```

`SEQUENTIAL_ANALYSIS_LOCK = OPEN`: the accepted methods and six ledger homes support sequential work. This initiation gate does not certify publication or authorize crossing an open transaction. V15 now has individually verified local/Drive/manifest agreement, full reading and retained map. V16 and later volumes remain outside this authorization; the open initiation gate does not authorize them.

## Authorization and progress

```yaml
pilot_execution:
  authorized_operation: V01_CLOSURE_THEN_SEQUENTIAL_V02_THROUGH_V15
  new_sequential_analysis_authorized: true
  authorization_limit: V15
  completed_new_sequential_units: [V01, V02, V03, V04, V05, V06, V07, V08, V09, V10, V11, V12, V13, V14, V15]
  candidate_unit: V15
  owner_review: V01_CONTENT_APPROVED_2026-09-25
  owner_authorized_following_unit: NONE_V15_TERMINAL
  next_permitted_action: CLOSE_V15_PUBLICATION_AND_EXACT_HEAD_AUDIT_THEN_STOP_SOURCE_EXPANSION
lane_progress:
  ln_sequential_closed_through: V15
  ln_published_and_audited_through_at_preparation: V14
  wn_comparison_closed_scope: null
  supplemental_readings_closed_scope: null
  adaptation_scope: OUT_OF_SCOPE
  reception_scope: NOT_STARTED
```

The analytical/evidence candidate boundary is **V15**; published and audited at preparation is **V14**. The containing V15 commit requires exact remote readback and final audit for published closure; no further source is authorized. Current revised packages are [Rudeus1.12](04%20Character%20Analysis/rudeus/RECONSTRUCTION_MODEL.md), [Roxy1.6](04%20Character%20Analysis/roxy/RECONSTRUCTION_MODEL.md), [Sylphiette1.7](04%20Character%20Analysis/sylphiette/RECONSTRUCTION_MODEL.md), [Zanoba1.6](04%20Character%20Analysis/zanoba/RECONSTRUCTION_MODEL.md), [Cliff1.5](04%20Character%20Analysis/cliff/RECONSTRUCTION_MODEL.md), [Elinalise1.5](04%20Character%20Analysis/elinalise/RECONSTRUCTION_MODEL.md), [Nanahoshi1.5](04%20Character%20Analysis/nanahoshi/RECONSTRUCTION_MODEL.md), [Eris1.7](04%20Character%20Analysis/eris/RECONSTRUCTION_MODEL.md), [Norn1.3](04%20Character%20Analysis/norn/RECONSTRUCTION_MODEL.md), [Aisha1.3](04%20Character%20Analysis/aisha/RECONSTRUCTION_MODEL.md). Paul1.3, Ruijerd1.2 and Sara1.1 retain earlier ceilings after review. The [V01–V10 Rudeus monograph](04%20Character%20Analysis/rudeus/CHARACTER_MONOGRAPH.md) and all earlier checkpoints remain unchanged historical syntheses. The [V01–V15 Rudeus monograph](04%20Character%20Analysis/rudeus/CHARACTER_MONOGRAPH_V01_V15.md), [mandatory cumulative checkpoint](05%20Checkpoint%20Syntheses/MT_V01_V15_MAINTENANCE_CHECKPOINT.md) and V15 reading Section K own current synthesis/maintenance decisions. All models remain BOUNDED_PROVISIONAL, no global enrollment or clean holdout. V15 is terminal for this instruction.

## Source and gate route

Read [MT_SOURCE_LOCK_AND_INVENTORY.md](01%20Source%20Lock%20and%20Inventory/MT_SOURCE_LOCK_AND_INVENTORY.md) for the actual V01–V15 fingerprints, locator checks and unverified later files. The main analytical object is the Japanese published LN, one volume per authorized transaction. WN, supplements, adaptations, interviews and reception have separate admission and authorization boundaries. The historical manifest is an evidence lead, not a narrative finding.

V01 prose/paratext and illustrations have been inspected to the scope recorded in the reading. Retention receipt: `MT-LNJP-V01-locator-map.json`, Drive file ID `1VE1ti8fs90PHM0Ey4mvT7eQbMjUZm_u9`, retained in source folder `1bx_IkoTqVZy9I8SmcyGvgRmj3JX0Rjug`; 650,286 bytes; SHA-256 `6c782f0a8f5f30fb8a3c9d67d138185c2adae3e1b8b8d2f947424a16798c0e5c`. A fresh download on 2026-09-26 UTC reproduced that size and hash. V15 fresh verification establishes Drive file `1nt6tg8Xsk1Y20P_kYddIbhBiWuM4jVDN`,2,051,042bytes with local/Drive/manifest hash agreement and complete reading as recorded below. V16–V26 are not individually byte-certified or narratively admitted here. The original V01 upload approval was file-specific; later maps now have separate authorization under the current clarified V02–V15 run.

## Accepted framework and read order

Start with this entrypoint, then the governing [analytical method](00%20Frameworks%20and%20Methods/MT_ANALYTICAL_METHOD.md), [series architecture](00%20Frameworks%20and%20Methods/MT_SERIES_ARCHITECTURE.md), [source/scope map](00%20Frameworks%20and%20Methods/MT_SOURCE_AND_SCOPE_MAP.md), and [character](00%20Frameworks%20and%20Methods/MT_CHARACTER_RECONSTRUCTION_SPEC.md) and [normative framing](00%20Frameworks%20and%20Methods/MT_NORMATIVE_FRAMING_PROTOCOL.md) methods as relevant. The full adopted set is:

- [MT_ANALYTICAL_METHOD](00%20Frameworks%20and%20Methods/MT_ANALYTICAL_METHOD.md)
- [MT_BOOTSTRAP_AND_LEDGER_TEMPLATES](00%20Frameworks%20and%20Methods/MT_BOOTSTRAP_AND_LEDGER_TEMPLATES.md)
- [MT_CHARACTER_RECONSTRUCTION_SPEC](00%20Frameworks%20and%20Methods/MT_CHARACTER_RECONSTRUCTION_SPEC.md)
- [MT_DISCOURSE_HYPOTHESIS_METHOD](00%20Frameworks%20and%20Methods/MT_DISCOURSE_HYPOTHESIS_METHOD.md)
- [MT_NORMATIVE_FRAMING_PROTOCOL](00%20Frameworks%20and%20Methods/MT_NORMATIVE_FRAMING_PROTOCOL.md)
- [MT_SERIES_ARCHITECTURE](00%20Frameworks%20and%20Methods/MT_SERIES_ARCHITECTURE.md)
- [MT_SOURCE_AND_SCOPE_MAP](00%20Frameworks%20and%20Methods/MT_SOURCE_AND_SCOPE_MAP.md)
- [MT_SYNTHESIS_AND_HANDOFF_SPEC](00%20Frameworks%20and%20Methods/MT_SYNTHESIS_AND_HANDOFF_SPEC.md)
- [MT_TEXTUAL_HISTORY_METHOD](00%20Frameworks%20and%20Methods/MT_TEXTUAL_HISTORY_METHOD.md)
- [MT_VOLUME_READING_TEMPLATE](00%20Frameworks%20and%20Methods/MT_VOLUME_READING_TEMPLATE.md)

The volume-reading and bootstrap documents are templates. The V01–V15 readings own their respective source observations; V01 owner approval and later execution under the continuing authorization remain distinct. Textual-history and discourse lanes remain unopened.

## Required day-one ledgers

- [MT_CHARACTER_STATE_AND_READINESS_LEDGER](03%20Longitudinal%20Ledgers/MT_CHARACTER_STATE_AND_READINESS_LEDGER.md) — preserved earlier history plus V15 states and ten bounded model revisions.
- [MT_CHRONOLOGY_AND_KNOWLEDGE_LEDGER](03%20Longitudinal%20Ledgers/MT_CHRONOLOGY_AND_KNOWLEDGE_LEDGER.md) — preserved earlier history plus V15 current events, alternative diary, attributed history, hypotheses and actual disclosure.
- [MT_CLAIMS_AND_REVISIONS_LEDGER](03%20Longitudinal%20Ledgers/MT_CLAIMS_AND_REVISIONS_LEDGER.md) — preserved earlier history plus V15 transitions for C001–015 with cumulative limitations.
- [MT_FORM_THEMES_AND_WORLD_LEDGER](03%20Longitudinal%20Ledgers/MT_FORM_THEMES_AND_WORLD_LEDGER.md) — preserved earlier history plus V15 embedded self, rewinds, collective rescue and provisional explanations.
- [MT_NORMATIVE_FRAMING_LEDGER](03%20Longitudinal%20Ledgers/MT_NORMATIVE_FRAMING_LEDGER.md) — preserved earlier history plus V15 pressure, protection, consent, service terms and particular repair.
- [MT_RELATIONSHIP_AND_AGENCY_LEDGER](03%20Longitudinal%20Ledgers/MT_RELATIONSHIP_AND_AGENCY_LEDGER.md) — preserved earlier history plus V15 distributed initiative, independent household choices and unfinished knowledge sharing.

The [bootstrap report](10%20Audits%20and%20Handoffs/MT_BOOTSTRAP_REPORT.md) records acceptance, verification, and publication state. Only the analytical integrator updates shared current state. Character curation and global index housekeeping retain their distinct designated writers.

## Next authorized boundary

The current owner request adopts the handoff's sequential V02–V15 run. On 2026-09-26 UTC the owner explicitly clarified: “Allow GitHub and Drive writes; keep local files in that directory.” This authorizes publication of the reviewed analytical updates to the public repository and retention of required V02–V15 locator maps in the designated private Drive source folder, with all local working files confined to the specified Mushoku Tensei directory. Raw books, normalized prose, images and locator-map payloads remain outside public Git. The required published, audited V01 gate was completed before the V02 recap/freeze and source inspection. V02 publication/audit also completed before the V03 recap/freeze and source inspection. V03 publication/audit completed before the V04 recap/freeze and source inspection. V04 publication/audit completed before the V05 recap/freeze and source inspection. V05 publication/audit completed before the V06 recap/freeze and source inspection. V06 publication/audit completed before the V07 recap/freeze and source inspection. V07 publication/audit completed before the V08 recap/freeze and source inspection. V08 publication/audit completed before the V09 recap/freeze and source inspection. V10 publication/audit completed before the V11 recap/freeze and source inspection. V11 publication/audit completed before the V12 recap/freeze and source inspection. V12 publication/audit completed before the V13 recap/freeze and source inspection. V14 publication/audit completed before the V15 recap/freeze and source inspection. Finish V15 publication/readback/source audit/housekeeping/final exact-head audit, then retain the terminal handoff. No V16 freeze or opening is authorized. Close each subsequent volume in order, with maintenance checkpoints after V05, V10 and V15; stop at V15. WN, supplements, adaptations and reception remain separately scoped.

## Historical V01 closure preparation snapshot — 2026-09-26 UTC

The following table preserves the pre-publication state of the V01 candidate. It is superseded for current routing by the verified receipt and V02 preparation record below.

| Field | Verified state |
| --- | --- |
| Candidate base / current source branch | `13579bb2b35c4a742fa5badeb2270e3341604da2` |
| Current main | `d18678270a112d6d673a8a0ee7768125f8be741a`; ancestor of candidate base |
| Existing source audit | `Repository integration audit` success for the base SHA, run `36213797333`; does not certify this candidate |
| V01 content and scope | Owner-approved synopsis and analysis; 13 narrative units / 12 narrative-bearing spine items; declared illustrations and paratext inspected in the accepted reading |
| V01 evidence retention | Exact map identity, size and SHA-256 above; fresh byte readback verified |
| Six ledgers | Existing V01 rows retained; current closure labels synchronized; no new literary findings |
| Local closure / publication at preparation | Content and evidence complete; nine-file closure candidate. The containing commit, remote readback and subsequent exact-head workflow results establish publication; this snapshot does not self-certify those later results. |
| Integration to main | This closure is not integrated; later synopsis/method branch changes also remain outside current main |
| Next permitted source | V02 only after closure publication and successful final exact-head audit |

## Historical V01 receipt and V02 preparation snapshot — 2026-09-26 UTC

| Dimension | V01 completed receipt | V02 candidate |
| --- | --- | --- |
| Frozen analytical input | Owner-approved V01 pilot/synopsis; closure preserved its findings | Audited V01 commit `eaf159559c6fc76ddd820178d7588545f08c351d`; recap and entering freeze written before V02 inspection at `2026-09-26T04:17:41.995410+00:00`, original draft SHA-256 `551b65179227962679adbd954db1134c4385a400a40944d147745d8b29977418` |
| Witness | `MT-LNJP-V01`, fingerprint above and in source lock | `MT-LNJP-V02`, Drive `1bI6zvLG7pRv-9TE-ZUaksdOHpeSlq0JX`, 1,861,079 bytes; SHA-256 `9b8c4e654779cc792224d514cca8907379586e9dcc58bf11c3bcf86580fabd7b`; fresh local/Drive byte match and container/spine check |
| Actual coverage | 13 narrative units; accepted visual/paratext scope | All 12 narrative units in order, 35 spine entries accounted for, all 16 images and paratext inspected; 117,517 trimmed ruby-base narrative characters |
| Private map | `1VE1ti8fs90PHM0Ey4mvT7eQbMjUZm_u9`, size/hash above | `1FUJVaE3aL3-MgsTE9HUQQzIbUJssQDRL`, 1,096,232 bytes, SHA-256 `213f8c674769fbe9ca77db4f638060ac2876556114f04ce9bc007756d386eba1`; private upload and raw-download hash match; independent original-XHTML verification of 4,895 paragraphs and 574 ruby nodes |
| Reading and ledgers | [V01 reading](02%20Sequential%20Readings/MT_V01_DEEP_READING.md), six V01 ledger histories | [V02 reading](02%20Sequential%20Readings/MT_V02_DEEP_READING.md), 19 diagnostic observations; material updates in all six ledgers; earlier rows/freeze preserved |
| Closure decision | Content/evidence complete, published and audited | Analytical/evidence complete; publication/audit gate remains at this snapshot |
| Publication / remote readback | Commit `eaf159559c6fc76ddd820178d7588545f08c351d`, all nine authored files byte-verified remotely | Containing commit to be established by publication; do not invent a self-referential commit ID |
| Workflows | Source audit `36216371710` SUCCESS; housekeeping `36216836816` SUCCESS, routing unchanged; final `Repository integration audit` `36216848522` SUCCESS on exact SHA `eaf159559c6fc76ddd820178d7588545f08c351d` | Source audit, housekeeping and final exact-head audit required; pending is not success |
| Main integration | Not established; last checked main `d18678270a112d6d673a8a0ee7768125f8be741a` excludes this closure | Not claimed; source-branch audit alone never establishes main integration |
| Next source | V02 was permitted and is now fully inspected | V03 only after V02 publication/audit, and only after its own pre-inspection recap/freeze |

The V02 displacement and expanded viewpoints warrant a targeted checkpoint in its Section L. Existing ledgers can track the new questions; no standalone model or specialist is promoted. Scheduled cumulative checkpoints remain due after V05, V10 and V15. Prior franchise familiarity is disclosed throughout and is not admitted as evidence.


## Verified V02 publication and V03 preparation — 2026-09-26 UTC

This is the preserved V03 preparation record; subsequent receipt below supplies its completed publication state.

| Dimension | Verified V02 receipt / V03 preparation |
| --- | --- |
| V02 publication | Authored `eba2064186272c17cf080a66bcbc9e409426c3a1`; all ten remote analytical files byte-verified. |
| V02 workflows | Source audit `36218928824` SUCCESS; housekeeping `36219382710` SUCCESS produced only expected three catalog-note changes at `687a13ac1a661270ab566c9e1a6028acd607d846`; final `Repository integration audit` `36219504894` SUCCESS on that exact SHA, 276 tests passed. |
| V03 frozen input | Exact V02 final SHA above; recap/freeze written before internal source inspection at `2026-09-26T05:12:01.4854312Z`; original draft SHA-256 `19454e8de6fe3d158ce893bd6334396ed1120c597c74a095a17f58ef285570ae`; wording preserved. |
| V03 witness | Drive `1VvZMAjmv9CF8c1A7g7BjrxycOAVNPuiJ`; 1,532,476 bytes; SHA-256 `ca635c479a6a0b2e871bfb17acf50c29a277af2485b54c1dac4988d508dddbf6`; local/Drive/manifest match, container/spine verified. |
| V03 actual coverage | 15 narrative units, ten narrative XHTML items including heading-only extra title, 144,603 trimmed ruby-base characters; all 55 text chunks, 29 spine items, 12 images and paratext inspected in order. |
| V03 retained map | Drive `1KRv1vf_Nckq70FcOGlSC-1MSNP0x6lDk`; 1,105,143 bytes; SHA-256 `6d261e509711e3fec834b28c0e12999f7460c3705e3053cabf8c7603b7c4dee8`; private upload and raw-readback match. All 4,941 paragraphs and 725 ruby nodes independently checked against original XHTML. |
| Analysis and synchronization | [V03 reading](02%20Sequential%20Readings/MT_V03_DEEP_READING.md), 22 diagnostic observations, synopsis, preserved entering recap/freeze and exit freeze; material additions to all six ledgers; first bounded Rudeus model/evidence index. |
| V03 closure decision | Analytical/evidence candidate complete following semantic and locator review; containing publication commit and subsequent workflows establish the remaining publication/audit dimensions. This table is not a self-certified final audit. |
| Main integration | Not established. Last checked main `d18678270a112d6d673a8a0ee7768125f8be741a` excludes V02 closure; source-branch audit is not main integration. Recheck before publication. |
| Next permitted source | V04 only after V03 remote readback, source audit, housekeeping and final exact-head audit, then its own recap/freeze. Continue sequentially through V15. |

V03's targeted checkpoint identifies failed transfer in staged-rescue judgment and new consultation practices. C011/C012 and a conditional model now have distinct responsibilities; no model domain is ready for unqualified simulation. Scheduled cumulative reviews remain V05, V10 and V15. Prior familiarity is not source evidence.


## Verified V03 publication and V04 preparation — 2026-09-26 UTC

This is the preserved V04 preparation record; the following V04 receipt establishes its completed publication state.

| Dimension | Verified receipt / current candidate |
| --- | --- |
| V03 publication | Authored `80f2c0758e1fc70164068803fc8e3520bfcd8ca1`; all twelve remote analytical files byte-verified. |
| V03 workflows | Source audit `36222201491` SUCCESS; housekeeping `36222684939` SUCCESS, only three expected catalog changes; final audit `36222895568` SUCCESS, 276 tests, exact head `56e1daa4bdc287cb9f2f3e4abbbea30be494628d`. Analytical blobs unchanged. |
| V04 input/freeze | That final V03 head; original `2026-09-26T06:15:47.035974+00:00` freeze precedes source inspection. Original SHA-256 `ad301454c33c91bd05004fdd168fe9c9ded1a1d1b3e4c45f0a7d7acb8d05cc00`; recap and questions preserved. |
| V04 witness | Drive `11rU7IAAsGUK8MIQ7mCzeM6Lzwmff1unN`; 1,848,117 bytes; SHA-256 `d06ed6f483a3f8c4135011789c1e6d36f8e3c7e9cdb6144a7b55db221814f5af`; local/Drive/manifest match. |
| Actual coverage | Twelve narrative units; twelve narrative XHTML items including one heading-only; 129,847 trimmed ruby-base characters. All 53 chunks, 35 spine entries, 16 images and paratext inspected in order. |
| Private map | `11Dyc2EzowOPvxmzq04NKZn60M0O_c2-Y`, 1,051,680 bytes; SHA-256 `1c065fe28a3f47dd2164a9dbf993dec12643c3dea6aee693e9215f0cf516828c`; correct private folder, raw-readback exact; all 4,694 paragraph positions/hashes and 648 ruby nodes independently checked. |
| Analysis | [V04 reading](02%20Sequential%20Readings/MT_V04_DEEP_READING.md), synopsis, preserved freeze, 26 observations, full coverage and exit freeze; all six ledgers updated, Rudeus model revised, bounded Eris model/index added. |
| Closure/publication | Analytical/evidence candidate reviewed before publication; containing authored commit, remote verification and subsequent workflows establish publication/audit dimensions. Pending workflow is not success. |
| Main | Not established; last checked main `d18678270a112d6d673a8a0ee7768125f8be741a` does not include these closures. Fresh ancestry check required before push. |
| Next | V05 only after V04 source audit, housekeeping and final exact-head audit, then its own recap/freeze; V05 cumulative checkpoint covers V01–V05. Continue in order through V15. |

V04 adds a targeted model/claim review: immediate aid qualifies the gratitude-control mechanism, consultation has both corrected choices and continued secrecy, and perceived usefulness can impose burdens. Existing ledger homes remain adequate. V05 must review model calibration, possible monographs/specialists and missing perspectives. No later identity or remembered franchise outcome is admitted.


## Verified V04 publication and V05 preparation — 2026-09-26 UTC

This is the preserved V05 preparation record; the following receipt establishes its completed publication state.

| Dimension | Verified receipt / current candidate |
| --- | --- |
| V04 publication | Authored/final `f3dfe47b549cf33fddc7d2128e2b6f0bba7a8e8e`; all thirteen remote files byte-verified. |
| V04 workflows | Source audit `36225860394` SUCCESS; housekeeping `36226328148` SUCCESS, no changes; final audit `36226338487` SUCCESS on that exact SHA. Both audits passed 276 tests. |
| V05 input/freeze | Exact final V04 head; original freeze `2026-09-26T07:27:07.489389+00:00` precedes source inspection, SHA-256 `0a28df0e930fe2b7bc04a1d4afc76ba2b574c32c50ff6e4034f7399517168b99`; recap/questions preserved. |
| V05 witness | Drive `16o_T1ZGBhsKkKickK9GVZF5zovncxKEe`; 1,750,510 bytes; SHA-256 `9d9e160205eb7a317e499697cfeca98799d4747af254823e6c2bbb00c30a0d41`; local/Drive/manifest agree. |
| Actual coverage | Eleven narrative units, thirteen narrative XHTML items including two heading-only; 126,774 trimmed ruby-base characters. All 53 text chunks, 36 spine entries, 16 images and paratext inspected in order. |
| Private map | `14RaaULS1ApqDHTdPqt4sU4KNfe01CaS3`; 1,048,716 bytes; SHA-256 `a36d67ffc0bfa8e54ccee5efde94d55bebef5e5590192c09d09e04498d173a1d`; correct private folder, raw readback exact; 4,679 paragraphs and 608 ruby nodes independently checked. |
| Analysis | [V05 reading](02%20Sequential%20Readings/MT_V05_DEEP_READING.md), 28 observations, synopsis, preserved freeze and full coverage; six ledgers updated, two model revisions and three first bounded model/index packages. |
| Cumulative review | [V01–V05 checkpoint](05%20Checkpoint%20Syntheses/MT_V01_V05_CHECKPOINT.md): comparative claims/countercases, calibration, missing perspectives and artifact responsibilities; no assumed arc completion. |
| Publication | Analytical/evidence candidate; containing authored commit, remote readback, source audit, housekeeping and exact-head final audit establish remaining dimensions. Pending is not success. |
| Main | NOT_ESTABLISHED; last fetched main `d18678270a112d6d673a8a0ee7768125f8be741a` excludes these closures; recheck before push. |
| Next | V06 only after V05 gate, then its own pre-inspection recap/freeze. Continue sequentially through V15; cumulative reviews next V10/V15. |

V05 strengthens the distinction between ability and available care, local repair and general restraint, personal gratitude and group acceptance. New C014 separates unavailable knowledge from knowingly leaving error uncorrected. Earlier freezes remain immutable; Fitts's prior identity and missing relatives' current fates remain unresolved. No raw evidence payload enters Git.


## Verified V05 publication and V06 preparation — 2026-09-26 UTC

This is the preserved V06 preparation record; the following receipt establishes its completed publication state.

| Dimension | Verified receipt / current candidate |
| --- | --- |
| V05 publication | Authored/final `3dc6b173b044abdafc013dc989bd96914620d13d`; all twenty remote files byte-verified. |
| V05 workflows | Source audit `36229399170` SUCCESS; housekeeping `36229685254` SUCCESS, no changes; final audit `36229698214` SUCCESS on that exact SHA. Both audits passed 276 tests. |
| V06 input/freeze | Exact final V05 head; original freeze `2026-09-26T08:34:55.390333+00:00` precedes source inspection, SHA-256 `27cd8d3bcc2a3f37aa2d4a5e8b90e5ee367c70ecad9c6657c4f5bdc3b384b257`; recap/questions preserved. |
| V06 witness | Drive `1CYS3psLrGOxye1yXXIn5h9dZfj5PrmFe`; 1,389,986 bytes; SHA-256 `209fe60c569035b9e786e024f8901fea44bc11a0412ce1f1001b45942a99059b`; local/Drive/manifest agree. |
| Actual coverage | Fifteen narrative units, ten narrative XHTML items; 145,767 trimmed ruby-base characters. All 57 text chunks, 29 spine entries, 12 images and declared paratext inspected in order. |
| Private map | `12pNmHq5akEgbs4p04uwwKAdBei231wTA`; 1,122,380 bytes; SHA-256 `8fb10df78c8ab7fe2b603c6baf2a01b22653577edc7ca17b7e30c46f7714f632`; private folder and raw readback verified; 5,020 paragraphs and 636 ruby nodes independently checked. |
| Analysis | [V06 reading](02%20Sequential%20Readings/MT_V06_DEEP_READING.md), 31 observations, synopsis, preserved freeze and full coverage; six ledgers and five existing model/index packages revised. No new present Paul state. |
| Targeted review | [V06 disclosure checkpoint](05%20Checkpoint%20Syntheses/MT_V06_DISCLOSURE_CHECKPOINT.md) reviews knowledge, care and decision access; V01–V05 cumulative checkpoint preserved. New standalone character packages deferred with reasons. |
| Publication | Analytical/evidence candidate; containing authored commit, remote readback, source audit, housekeeping and exact-head final audit establish remaining dimensions. Pending is not success. |
| Main | NOT_ESTABLISHED; last fetched main `d18678270a112d6d673a8a0ee7768125f8be741a` excludes these closures; recheck before push. |
| Next | V07 only after V06 gate, then its own pre-inspection recap/freeze. Continue sequentially through V15; cumulative reviews next V10/V15. |

V06 corrects Rudeus's explanation of Eris's departure without endorsing her communication or inventing knowledge of his resulting error. Lilia's historical account changes affected-person access; Hitogami's explanations and Kishirika's lead remain attributed and qualified. Prior freezes and claim identities remain intact. No raw evidence payload enters Git.


## Verified V06 publication and V07 preparation — 2026-09-26 UTC

| Dimension | Verified receipt / current candidate |
| --- | --- |
| V06 publication | Authored/final `0e72e531278055c0dbb7a6054285337a1cc37a93`; all twenty remote analytical files byte-verified. |
| V06 workflows | Source audit `36232828869` SUCCESS; housekeeping `36233305105` SUCCESS/no changes; final audit `36233317437` SUCCESS on that exact SHA; both audits passed 276 tests. |
| V07 input/freeze | Exact final V06 head; original freeze `2026-09-26T09:45:57.226555+00:00`, SHA-256 `7c42635c6160682426945a25fe82f9a680e87ca3cf1c0186198b9b967f6da4c8`; created before source inspection and preserved. |
| V07 witness | Drive `1O_jNgJHYB0q2LVq6CDMPaQeUXFKRS0sI`; 2,591,583 bytes; SHA-256 `9b242132a32ffe24547569e22bd6bcdca86e175d403d373ebea2d85c261de60f`; local/Drive/manifest agree. |
| Actual coverage | Nine narrative units, eleven narrative XHTML items including heading-only; 133,290 trimmed ruby-base characters; all 53 chunks, 35 spine entries, 19 image occurrences (18 distinct files) and paratext inspected in order. |
| Private map | `1B5WiKfHXrywIKX_1O332mrhrrwEv4R4W`, 959,383 bytes, SHA-256 `26c0f5cba06dc96dbe3829174bc1cad2859d3c2e50760175d99de8aa594ea825`; private parent/raw readback verified; 4,277 paragraphs/418 ruby nodes independently checked. |
| Analysis | [V07 reading](02%20Sequential%20Readings/MT_V07_DEEP_READING.md), 30 observations, readable synopsis, preserved input and exit freeze; all six ledgers, Rudeus 1.4, first Sara 1.0 model/index and [targeted checkpoint](05%20Checkpoint%20Syntheses/MT_V07_RECOGNITION_CHECKPOINT.md). |
| Publication | Content/evidence candidate; containing authored commit, remote readback, source audit, housekeeping and final exact-head audit establish remaining dimensions. Pending is not success. |
| Main integration of prior work | PR 100 integrated source `08baeff3a8f476b4f88119f737308d9c92c6223f` as `208c63c48ae8af25bddc2ea57ce49e326cf4ceaf`, ancestor of fetched main `2658ac7fb5472530d5502263f664a7d7a4f70938`. Complete Mushoku Tensei subtree matches audited V06 content; main exact-head status SUCCESS, run 36251338898. V07 is not thereby integrated. |
| Reconciliation | Remote source's intervening main merge preserved; current main cleanly merged as local `bd7805a99a8a7bf9e0e3167d063dce6f0745d8aa`. No analytical input/freeze changed; no governance/tool changes arrived. Recheck heads before publication. |
| Next | V08 only after V07 publication/audit, then its own pre-inspection recap/freeze. Continue through V15; cumulative reviews at V10/V15. |

V07 distinguishes restored work, received companionship, bodily difficulty and romantic security. Sara's corrective viewpoint establishes affection while preserving her false inference; actual demeaning speech remains actual. School reputation depends on deliberately unequal access. Earlier freezes remain unchanged; no raw evidence payload enters Git.


## Verified V07 publication and V08 preparation — 2026-09-26 UTC

| Dimension | Verified receipt / current candidate |
| --- | --- |
| V07 publication | Authored/final `523625ec4a57b95dec7d5acbb217bae5cc7ba5d3`; all 14 analytical files matched exact remote content. |
| V07 workflows | Source `36270850776` SUCCESS; housekeeping `36271366357` SUCCESS/no changes; final `36271379146` SUCCESS on exact SHA; both audits 276 tests. |
| Main integration | V01–V06 content verified on main `2658ac7fb5472530d5502263f664a7d7a4f70938`; V07 integration NOT_ESTABLISHED. Successful source audit alone is not main integration. |
| V08 entering freeze | `2026-09-26T21:10:24.788651+00:00`, before internal source inspection, based on final V07; SHA-256 `d35c9eea2dd687a1f477c6d4b8003e66f7d9e68f54ed65cea27280e670cfc7c3`; original wording retained. |
| V08 source | Drive `1fjytmS18iNQ9ajTqICZIHePoadvhlF02`; 1,550,790 bytes; SHA-256 `b2a831efa2a2b03286bbbbf45029db4947088c1c45223a9f64fccd1be9bafb1d`; local/Drive/manifest agree. |
| Actual reading | All 53 text chunks, 30 spine entries, 13 narrative units, 9 narrative XHTML items including heading-only, 135,176 trimmed ruby-base characters, 16 image occurrences/15 distinct files and paratext; no ordering exception. |
| Private map | Drive `15NLBBlEYXb1UWgBgDEmgsXyr-GYuCYNr`, 1,017,824 bytes; SHA-256 `3081cd3e7efdb39b0774ade48a379f991e10a7db945fb7cac4a7cb276a8de676`; private/correct parent and fresh byte-identical readback; 4,545 paragraphs/497 ruby independently verified. |
| Analytical package | 30 observations, complete synopsis/coverage, six ledger appendices, Rudy 1.5, Zanoba 1.0, Sylphiette 1.0 and targeted consent/institution checkpoint; semantic review and exact publication states separately recorded. |
| Next gate | Publish reviewed V08 paths, verify remote content and source/HK/final exact-head audits, then freeze/open V09. No V09 source inspected during candidate preparation. |

The preceding V07 preparation table is historical and superseded for publication status by this receipt. Fitts/Sylphiette attribution and the enrollment month-count tension remain explicit uncertainties. V08 does not establish mother rescue, a cure, emancipated Juli or a freely agreed captive hierarchy.


## Verified V08 publication and V09 preparation — 2026-09-26 UTC

| Dimension | Verified receipt / current candidate |
| --- | --- |
| V08 publication | Authored/final `210894fd2b5894b7e499bab80251e8f5ea761138`; all16 analytical files matched remote bytes. |
| V08 workflows | Source `36274566635` SUCCESS; housekeeping `36274933387` SUCCESS/no changes; final `36274949035` SUCCESS on exact SHA; both audits276 tests. |
| Main integration | V01–V06 content verified on main `2658ac7fb5472530d5502263f664a7d7a4f70938`; V07/V08 integration NOT_ESTABLISHED. |
| V09 entering freeze | `2026-09-26T22:12:19.343782+00:00`, before internal source inspection; SHA-256 `514c8e459bc4ab9960a9927386b9b3bda6ff43d4d7527b5267e71d6772c61621`; original wording retained. |
| V09 source | `MT-LNJP-V09`, Drive `1KLJn7gyLgExGho_5i2jeiycf-_iJgixW`;1,418,021 bytes; SHA-256 `549ac6eb074cca8d9a2d8eff78dd9b1fcfdc4845b24417d0319b26e7b5a0bb4c`; local/Drive/September25 manifest agree. |
| Actual reading |58 ordered chunks,29 spine entries,15 narrative units,10 narrative XHTML items including heading-only,149,815 trimmed ruby-base characters,14 image occurrences/13 distinct and declared paratext; no ordering exception. |
| Private map | Drive `1aKLjglJL-alQrx9V-0MHO9VyxxY8sYKR`,1,114,993 bytes; SHA-256 `30435a447cd0ed77d4ad73cb213ab7d7b6b2ecd003173ec25e795b2619fd43f1`; private/correct parent and fresh byte-identical readback;4,985 paragraphs/539 ruby independently checked. |
| Analytical package |35 observations, synopsis/coverage, six ledger appendices, Rudy1.6, Sylphiette1.1, Zanoba1.1, Eris1.3, first Cliff/Nanahoshi packages and targeted disclosure/recovery checkpoint. |
| Next gate | Publish reviewed V09 paths, verify remote content and source/HK/final exact-head audits, then freeze/open V10. V10 cumulative review follows actual reading. |

Earlier preparation snapshots remain historical. Identity resolution is scene-specific; earlier disclosure permission revises the explanation for delay. Local recovery does not certify general ethical maturity or equality. No V10 source was inspected during candidate preparation.


## Verified V09 publication and V10 preparation — 2026-09-26 UTC

| Dimension | Verified receipt / current candidate |
| --- | --- |
| V09 publication | Authored/final `40018b5caedfba456da199ed2fea613ec991015a`; all22 analytical files matched remote bytes. |
| V09 workflows | Source `36278156334` SUCCESS; housekeeping `36278653531` SUCCESS/no changes; automatic final `36278669762` and redundant manual final `36278686182` both SUCCESS. Latest exact-head status points to36278686182; no pending run counted as success. |
| Main integration | V01–V06 content verified on main `2658ac7fb5472530d5502263f664a7d7a4f70938`; V07–V09 integration NOT_ESTABLISHED. |
| V10 entering freeze | `2026-09-26T23:22:26.020976+00:00`, before internal source inspection; original SHA-256 `a64a1a174ab2be43578d6d36d110f9358684c4d7102bfede98598f89995a69be`; original recap/questions preserved. |
| V10 source | `MT-LNJP-V10`, Drive `13wT0EKO51PmpMlYhusk3c6Q98E9tTU8N`;1,499,457 bytes; SHA-256 `d6cae30a23a5dc24f57485a5a8bbe6a6954eb85450d3eb6fb97fd7b59fa01419`; local/Drive/September25 manifest agree. |
| Actual reading |63 ordered chunks,29 spine entries,14 narrative units,10 narrative XHTML items including heading-only,135,183 trimmed ruby-base characters,14 image occurrences/13 distinct files and declared paratext. A truncated text display was immediately recovered; no source or image interval skipped. |
| Private map | Drive `1hDPpz_ai0HaggK0ZaSrb7dbKs7GFoeQN`;1,093,044 bytes; SHA-256 `5cd0d06e15a06d7b158364a6b17d579c6d8755567e41afbca2c033d56ff6d81b`; private/correct parent and byte-identical raw readback;4,887 paragraphs/535 ruby nodes independently checked. |
| Analytical package |34 observations, synopsis/coverage, six ledger appendices, nine model revisions, first Elinalise model/index, Rudeus monograph and required V01–V10 cumulative checkpoint. |
| Closure dimensions | Content/evidence candidate and semantic acceptance are distinct from the containing publication commit, remote readback and successful source/HK/final exact-head audit. This preparation snapshot cannot certify those future results. |
| Next gate | Publish and audit V10, then freeze/open V11. Continue one closed volume at a time through V15; no V11 source admitted during this preparation. |

Earlier preparation snapshots remain historical. Corrected beliefs, felt safety and relational trust have distinct evidential trajectories. Marriage, house safety, a summoned bottle and completed escort are bounded achievements. The new monograph and checkpoint do not replace earlier freezes or source-era readings.


## Verified V10 publication and V11 preparation — 2026-09-27 UTC

| Dimension | Verified receipt / current candidate |
| --- | --- |
| V10 publication | Authored/final `4823e7f9cecff45d86f3045304b5825c79bcb628`; all31 authored files matched remote bytes. |
| V10 workflows | Source `36282513960` SUCCESS; housekeeping `36282995329` SUCCESS/no changes; automatic final `36283008039` SUCCESS and exact-head status verified. |
| Main integration | V01–V06 content verified on main `2658ac7fb5472530d5502263f664a7d7a4f70938`; V07–V10 integration NOT_ESTABLISHED. A separate nightly run failed on source movement and does not undo these successful exact-head checks. |
| V11 entering freeze | `2026-09-27T00:46:59.346818+00:00`, before internal source inspection; original SHA-256 `25f22a47593d195ba38af34edb4406c9f2efda3c92fc65b04c81f1f6f31daa1e`; recap/questions unchanged. |
| V11 source | `MT-LNJP-V11`, Drive `184mrGtLmjjzUWZW-DPV1QsAu2RQ41R1t`;1,312,879bytes; SHA-256 `aa3c553fa2119770243a9768ba1f2393ea3d3ce73507d26bb11d90eb7b7b34b9`; local/Drive/September25 manifest agree. |
| Actual reading |65 chunks,29 spine entries,16 narrative units,10 narrative XHTML items including heading-only,150,978 trimmed ruby-base characters;14 image occurrences/13 files and all declared paratext. Text display gap recovered; image13 inspected one text chunk late, explicitly recorded. |
| Private map | Drive `1fJuAgFUN1Tw6o7ombUytxfOrrVFk0Gdq`;979,891bytes; SHA-256 `ea0fc6e2741cab4f5fa7c360dd7b3c7467ba6c594cbb255869bb5b9e56200f18`; private/correct parent, exact raw readback;4,377 paragraphs/514 ruby independently checked. |
| Analytical package |35 observations, synopsis/coverage, six ledger appendices, six revised model/index pairs, first Norn/Aisha pairs and targeted knowledge/duty checkpoint. |
| Closure dimensions | Content/evidence and semantic acceptance are distinct from the containing publication commit, remote readback and source/HK/final exact-head results. This preparation file cannot certify its own future audit. |
| Next gate | Publish and audit V11, then freeze/open V12. Continue individually through V15; V12 remains unopened here. |

Earlier snapshots remain historical. New disclosures revise present knowledge without rewriting earlier freezes. Norn's received comfort, Aisha's negotiated room, useful travel aid and Rapan arrival are bounded results, not a common measure of ethical or narrative completion.


## Verified V11 publication and V12 preparation — 2026-09-27 UTC

| Dimension | Verified receipt / current candidate |
| --- | --- |
| V11 publication | Authored/final `0670b4dfc16a7a5a6c0e35dc62d520f90758a3a5`; all26 authored files matched remote bytes. |
| V11 workflows | Source `36285960125` SUCCESS; housekeeping `36286440954` SUCCESS/no changes; final `36286484390` SUCCESS and exact-head status verified. |
| Main integration | V01–V06 content verified on `2658ac7fb5472530d5502263f664a7d7a4f70938`; V07–V11 integration NOT_ESTABLISHED. |
| V12 freeze | `2026-09-27T01:54:36.898980+00:00`, before internal inspection;24,403bytes SHA-256 `a0e7584c0f89006281fd8ef749e349ab5b153630fcc6dc78e9ad18f877c49a7f`; recap/questions unchanged. |
| Witness | `MT-LNJP-V12`, `LN_JP_MAIN`; Drive `1RIKu1ira0Z6yYH2ILkL8BvlNPFSDi615`;1,542,217bytes; SHA-256 `9fdc6620410adc0ed9508cca335b2706bc16bdc33204c56af3448cb815ed2407`; local/Drive/September25 local-manifest row agree. |
| Identity/edition | Japanese volume12, 理不尽な孫の手, KADOKAWA / メディアファクトリー; identifiers `e336a972-9582-43f1-848c-a10be219425c` (twice), `B01KSTEVU2`; colophon electronic2016-08-25/print-basis2016-08-31, OPF `2016-08-25T06:00:00+00:00`. |
| Container/reading | CRC, mimetype, manifest/container and28 spine references PASS; no outside-paragraph prose.62 actual chunks,16 episodes,8 narrative XHTML,144,228 trimmed ruby-base characters; completed `2026-09-27T02:09:29.766552+00:00`. |
| Images/paratext |16 occurrences/15 files, all28 spine entries accounted; covers/art/title/notice/contents/epigraph/plates/profile/credits/colophon/store mark. Image17 inspected after chunk36(spine18p1–87), onechunklate; no missing content. |
| Locator | `mt-lxml-p1`: one-based body-descendant p including empties, omit rt/rp retaining base/tails, edge-trim/no Unicode normalization; no inferred print pagination. Independent original-XHTML check:4,449 paragraphs/585 ruby. |
| Private map | Drive `1zWQk6h7JU9_6nYoLpMSLTYfF3922eosy`, parent `1bx_IkoTqVZy9I8SmcyGvgRmj3JX0Rjug`;995,714bytes; SHA-256 `41eff1ccfac1ad231a84eacb43bbb92d930ee5f530a4adf6118f3db91be6d200`; created `2026-09-27T01:55:09.369Z`; private/correct parent, BYTE_IDENTICAL raw readback. |
| Analytical package |34 observations, readable synopsis/full coverage, all six ledger appendices, seven existing model/index revisions and targeted loss/household checkpoint. |
| Closure dimensions | Bounded content/evidence acceptance is distinct from this candidate's publication/readback/source audit/housekeeping/final exact-head audit; this file cannot certify its own future audit. |
| Next source | V13 remains unopened until V12 publication and exact-head closure, then freeze V13. V15 terminal; no later/source-lane admission. |

The V12 missing-folder snapshot and the present local-manifest match describe different evidence surfaces. Neither is silently rewritten. Earlier dated preparation sections remain historical. Source EPUB, normalized prose, images and map payload never enter public Git.


## Verified V12 publication and V13 preparation — 2026-09-27 UTC

| Dimension | Verified receipt / current candidate |
| --- | --- |
| V12 publication | Authored/final `e1018971ce195163277565ca1e4e7e298332bb21`; all24 authored files matched remote bytes. |
| V12 workflows | Source `36288770714` SUCCESS; housekeeping `36289229470` SUCCESS/no changes; final `36289241421` SUCCESS and exact-head status verified. |
| Main integration | V01–V06 content verified on `2658ac7fb5472530d5502263f664a7d7a4f70938`; V07–V12 integration NOT_ESTABLISHED. |
| V13 freeze | `2026-09-27T02:51:14.835937+00:00`, before internal inspection;30,322bytes SHA-256 `b139dbff0c83829ef1929317d3ae99d7563e4ce9bb0e51b17ba849e040a54375`; recap/questions unchanged. |
| Witness | `MT-LNJP-V13`, `LN_JP_MAIN`; Drive `1b-BRvevOEyzPBg8AzFWtlsuoVoCtNCxA`;1,501,090bytes; SHA-256 `ed2bb187fc68fa60e112d14b08a1fd6f7af57b3e6b700543920cd4d0fb35dbb3`; local/Drive/September25 local-manifest row agree. |
| Identity/edition | Japanese volume13, 理不尽な孫の手, KADOKAWA / メディアファクトリー; identifiers `4386fbeb-904d-4329-a8f0-c52a7fd404d7` (twice), `B01MZ2C6LM`; colophon electronic2016-12-23/print-basis2016-12-31, OPF `2016-12-22T23:00:00+00:00`. |
| Container/reading | CRC, mimetype, manifest/container and28 spine references PASS; no outside-paragraph prose.64 actual chunks,12 episodes plus interlude,9 narrative XHTML,143,551 trimmed ruby-base characters; completed `2026-09-27T03:04:39.697663+00:00`. |
| Images/paratext |15 occurrences/14 files, all28 spine entries accounted; cover/color art/title/notice/contents/epigraph/plates/profile/credits/colophon/store mark. No ordering exception or separate afterword. |
| Locator | `mt-lxml-p1`: one-based body-descendant p including empties, omit rt/rp retaining base/tails, edge-trim/no Unicode normalization; no inferred print pagination. Independent original-XHTML check:4,788 paragraphs/578 ruby. |
| Private map | Drive `1NttjZO4f9paPEIxdDrVAQfoLgLlM0gWl`, parent `1bx_IkoTqVZy9I8SmcyGvgRmj3JX0Rjug`;1,070,662bytes; SHA-256 `b4239cfbd21478023d19d50a6eaa68ad6feecdc3086eb1489b2720af5ad2177c`; created `2026-09-27T02:51:58.028Z`; private/correct parent, BYTE_IDENTICAL raw readback. |
| Analytical package |37 observations, readable synopsis/full coverage, all six ledger appendices and eleven existing model/index revisions. Paul/Ruijerd packages and earlier syntheses remain byte-preserved; V15 cumulative checkpoint still due. |
| Closure dimensions | Bounded content/evidence acceptance is distinct from this candidate's publication/readback/source audit/housekeeping/final exact-head audit; this file cannot certify its own future audit. |
| Next source | V14 remains unopened until V13 publication and exact-head closure, then freeze V14. V15 terminal; no later/source-lane admission. |

Earlier dated preparation sections remain historical. Source EPUB, normalized prose, images and locator-map payload never enter public Git. The interlude's future-year projection belongs to V13 itself; it does not admit a later source.


## Verified V13 publication and V14 preparation — 2026-09-27 UTC

| Dimension | Verified receipt / current candidate |
| --- | --- |
| V13 publication | Authored/final `eece6816d98e076847e65507bc9e83d03b1ed77d`; all31 authored files matched remote bytes. |
| V13 workflows | Source `36291638965` SUCCESS; housekeeping `36292099915` SUCCESS/no changes; final `36292110530` SUCCESS and exact-head status verified. |
| Main integration | V01–V06 content verified on `2658ac7fb5472530d5502263f664a7d7a4f70938`; V07–V13 integration NOT_ESTABLISHED. |
| V14 freeze | `2026-09-27T03:46:49.311029+00:00`, before inspection;16,508bytes SHA-256 `4a3b4f3ba439ac74ed77809abb0ebe8630c6e2dccdbfdb22775ca9b688ba1248`; recap/questions unchanged. |
| Witness | `MT-LNJP-V14`, `LN_JP_MAIN`; Drive `11QHR_6eQlo6UuHMzxd2_qXWg4Ba7dCiP`;1,572,618bytes; SHA-256 `314d7d04dae2626e6da0ff4ed939114847dfb60f939ca6e74bf087f5bd04825a`; local/Drive/September25 local-manifest row agree. |
| Identity/edition | Japanese volume14, 理不尽な孫の手, KADOKAWA; identifiers `890eb20b-246b-4f1e-bf05-6c5a636c69b6`, `6635c0e0-06e4-4129-8c20-b383fd076517`, `B06ZYHJZW7`; colophon electronic/base-first-print2017-04-25, OPF `2017-04-25T04:00:00+00:00`. |
| Container/reading | CRC, mimetype, manifest/container and28 spine references PASS; no outside-paragraph prose.63 actual chunks,11 episodes plus interlude,9 narrative XHTML,142,295 trimmed ruby-base characters; completed `2026-09-27T03:56:40+00:00`. |
| Images/paratext |15 occurrences/14 files, all28 spine entries; cover/color art/title/notice/contents/epigraph/plates/profile/credits/colophon/store mark. No ordering exception or separate afterword. |
| Locator | `mt-lxml-p1`: one-based body-descendant p including empties, omit rt/rp retaining base/tails, edge-trim/no Unicode normalization; no inferred print pagination. Independent original-XHTML check:4,629 paragraphs/536 ruby. |
| Private map | Drive `1Su9OoNDDcSFZOp37nQE856GugCng0Gaf`, parent `1bx_IkoTqVZy9I8SmcyGvgRmj3JX0Rjug`;1,035,390bytes; SHA-256 `ec0523357fdcf651badfffe250e5df7ebfe25020ef9e99babc91451f3b9a3629`; created `2026-09-27T03:47:28.238Z`; private/correct parent, BYTE_IDENTICAL raw readback. |
| Analytical package |36 observations, readable synopsis/full12-unit coverage, all six ledger appendices, eight existing model/index revisions and targeted testimony/agency checkpoint. Five other packages and earlier syntheses preserved; V15 cumulative review still due. |
| Closure dimensions | Bounded content/evidence acceptance is distinct from publication/readback/source audit/housekeeping/final exact-head audit; this file cannot certify its own future audit. |
| Next source | V15 remains unopened until V14 publication and exact-head closure, then freeze V15. V15 terminal; no later/source-lane admission. |

Earlier dated preparation sections remain historical. Source EPUB, normalized prose, illustrations and locator-map payload never enter public Git. Elder future testimony is internal to V14 and does not admit a later source or rewrite current chronology.


## Verified V14 publication and terminal V15 preparation — 2026-09-27 UTC

| Dimension | Verified receipt / current candidate |
| --- | --- |
| V14 publication | Authored/final `992e696dabd6acf5646e3498a5fd20c46267c580`; all26 authored files matched remote bytes. |
| V14 workflows | Source `36294192960` SUCCESS; housekeeping `36294526150` SUCCESS/no changes; final `36294539373` SUCCESS and exact-head status verified. |
| Main integration | V01–V06 content verified on `2658ac7fb5472530d5502263f664a7d7a4f70938`; V07–V14 integration NOT_ESTABLISHED at preparation. V15 source-branch success alone cannot establish main integration. |
| V15 freeze | `2026-09-27T04:41:20.931337+00:00`, before inspection;13,782bytes SHA-256 `d5a4f33ca07f6758f4fcff808a453f13d41e846021a973532b14a434b0a6b2ba`; recap/questions unchanged. |
| Witness | `MT-LNJP-V15`, `LN_JP_MAIN`; Drive `1nt6tg8Xsk1Y20P_kYddIbhBiWuM4jVDN`;2,051,042bytes; SHA-256 `6f054d77deb97d594e285a6bc5d301a515b3a95de12d51c9ca6c4c8a2ab87d25`; local/Drive/September25 local-manifest row agree. |
| Identity/edition | Japanese volume15, 理不尽な孫の手, KADOKAWA / メディアファクトリー; identifier `efa97959-7100-4e92-a3b9-4aa10acd7e77` in two package fields and `B07431LTTF`; colophon electronic/base-first-print2017-07-25, OPF `2017-07-24T22:00:00+00:00`. |
| Container/reading | CRC, mimetype, manifest/container and37 spine references PASS; no outside-paragraph prose.67 actual chunks,13 episodes plus interlude,11 narrative XHTML,143,032 trimmed ruby-base characters; completed `2026-09-27T04:52:36+00:00`. |
| Images/paratext |22 occurrences/21 files, all37 spine entries; cover variants/cast/frontispiece/title/notice/contents/epigraph/diary images/plates/design pages/profile/credits/colophon/store mark. No ordering exception; spine28 continues interlude, no afterword. |
| Locator | `mt-lxml-p1`: one-based body-descendant p including empties, omit rt/rp retaining base/tails, edge-trim/no Unicode normalization; no inferred print pagination. Independent original-XHTML check:4,604 paragraphs/488 ruby. |
| Private map | Drive `1_insekEL3KeeZq2qSZ3_Qdyf5g4ufAwJ`, parent `1bx_IkoTqVZy9I8SmcyGvgRmj3JX0Rjug`;1,032,578bytes; SHA-256 `a4fc5bd73880f1fb5556d23c928a72ad5d33226070b17deddbbe3c411eceb205`; created `2026-09-27T04:42:00.493Z`; private/correct parent, BYTE_IDENTICAL raw readback. |
| Analytical package |38 observations, readable synopsis/full14-unit coverage, all six ledger appendices, ten existing model/index revisions, mandatory cumulative V01–V15 checkpoint and new scoped Rudeus monograph. Three unchanged packages and all earlier syntheses preserved. |
| Closure dimensions | Content/evidence acceptance is distinct from publication/readback/source audit/housekeeping/final exact-head audit. The containing commit and exact successful final status identify publication closure; this candidate does not predict its own future SHA or audit result. |
| Terminal boundary | V15 is the last authorized volume. No V16 source, freeze, WN, supplement, adaptation or reception admission follows automatically. |

Earlier dated preparation sections remain historical. Source EPUB, normalized prose, illustrations and locator-map payload never enter public Git. The diary's alternative future is internal V15 testimony, not accomplished current chronology or permission to use later sources. Required transaction closure is recorded separately after the final exact-head audit; in-story obligations may remain open even when this bounded analytical task is complete.
