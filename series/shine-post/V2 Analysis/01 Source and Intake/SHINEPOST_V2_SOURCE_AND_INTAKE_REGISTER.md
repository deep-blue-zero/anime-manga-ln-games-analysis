---
title: "SHINE POST V2 — Source and Intake Register"
artifact_id: SHINEPOST_V2_SOURCE_AND_INTAKE_REGISTER
artifact_type: source_and_intake_register
series: SHINE POST
series_id: shine-post
generation: V2
version: "1.1"
status: canonical
authority_scope: "Witness and derivative identity, admission state, candidate provenance and intake routing"
source_boundary: "Japanese television anime E01–E12 technical inventory; E01 admitted for bundle-mediated reading; no accepted V2 narrative units"
canonical_home: series/shine-post/V2 Analysis/01 Source and Intake/SHINEPOST_V2_SOURCE_AND_INTAKE_REGISTER.md
created: 2026-11-19
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
do_not_use_as_literary_evidence: true
---

# SHINE POST V2 — Source and Intake Register

## 1. Present inventory

This register records the source/intake state, not analytical findings. The [entrypoint](../../CURRENT_STATE_AND_CORPUS_MAP.md) controls current execution; the [intake protocol](../00%20Frameworks/SHINEPOST_V2_AV_RECONCILIATION_AND_INTAKE_PROTOCOL.md) governs verification. The bootstrap had no admitted witnesses. Section 5 records the first verified technical inventory and its inspection limits.

| Object | Established state | Limits |
| --- | --- | --- |
| Existing V1 corpus | Repository contains E01–E12 readings, six character documents covering seven indexed people, two specialists, final synthesis and historical material | Inventory establishes artifact existence, not fresh source verification or V2 qualification |
| V2 TV target | Twelve release objects bound to exact derivative sets | Retail and broadcast edition equivalence unverified |
| Antigravity candidate | Owner reports a frozen E01–E12 Gemini candidate | Contents sealed until independent freeze; no intake receipt |
| V2 bundles / source-language text / AV objects | Twelve ZIPs, extracted trees, FLACs and Japanese subtitle derivatives verified | Subtitle accuracy and narrative coverage await source inspection |
| V2 inspection capability | Text and still images available; decoded programme sample omitted by model interface | Hearing and synchronized audiovisual perception require a verified route |

V1 routes through [its original corpus map](../../V1%20Analysis/00_README_AND_CORPUS_MAP.md). Historical transcripts are provenance, not primary audiovisual witnesses. The existing registry's `LIGHT_NOVEL` / `ANIME` labels describe the catalog identity; they do not admit light-novel or other franchise evidence to this V2 anime boundary.

## 2. Witness record contract

Create a witness record only when an actual object is supplied. Assign a stable `SPV2-W-…` identity and record:

- Official/work identity and edition/distribution provenance, including what remains unverified; medium, language and continuity.
- Exact original filename where publication-safe, episode/unit mapping, byte length and full SHA-256 when bytes are available. A reported hash is marked as reported, not locally verified.
- Duration and program-start definition; video stream, native rate/resolution; audio stream/language/channel identity; subtitle and onscreen-text routes and provenance.
- Derivative identities and hashes, parent witness, transforms, crop/trim/resample/subtitle shifts, losses and mapping to the source clock.
- Content/technical coverage, QA evidence, material gaps and replacement history. Keep transport success, decode success and actual model inspection separate.
- Admission decision, exact authorized source boundary and linked receipt; narrative inspection state remains separate from admission.

Keep primary media, frame/audio packages, raw acquisition evidence and private retrieval paths in the authorized source environment. Public records use sanitized stable identities and repository-relative analytical routes. Do not publish local absolute paths, signed URLs, credentials or raw copyrighted source packages.

## 3. Candidate receipt contract

The current candidate has no invented delivery ID or manifest. On actual receipt assign `SPV2-IN-…`, retain the producer's original title/version/generation, and record the receiving date and complete file inventory. Compare original and publication derivative bytes explicitly if a transformation is required; do not overwrite the original identity with V2.

The receipt must recover the complete output, not just a synopsis: all analyses, evidence routes, cumulative state, reviews, unresolved items and execution/source records that actually exist. Record hashes/byte counts where accessible, acquisition channel, authoring environment/model/effort if observed, actual scope, interruptions, source/edition match and all disclosed prior exposure. Missing producer information remains unknown.

Record producer/base state, returned candidate and current repository target separately, then identify drift and overlapping edits before integration. An independent pass that had no repository base says so. Its successful transfer does not establish semantic acceptance, literary authority, current-run authorization or lawful publication.

Completed external work needs the legitimate historical/completed-candidate route described by the intake protocol and current initiation policy. Never fabricate an earlier active run, original freeze date or completed-run proof. If an exact frozen noncurrent publication needs a separate owner-merged binding, record that blocker and exact scope; a `draft_noncurrent` label alone is not such a binding.

## 4. Coverage and capability matrix

For each actual unit/stage, record requirements and inspection independently:

| Field | Allowed meaning |
| --- | --- |
| Requirement | `REQUIRED`, `OPTIONAL`, `OUT_OF_SCOPE` for the task/claim |
| Inspection | `COMPLETE_FOR_DECLARED_SCOPE`, `PARTIAL`, `PENDING`, `UNAVAILABLE`, `NOT_APPLICABLE` |
| Boundary | Exact episode/intervals, channel and source/derivative inspected; remaining gaps |
| Capability | `VERIFIED`, `UNVERIFIED`, `UNAVAILABLE` with observed probe and route |
| Acceptance | Actual receiver disposition with reasons and unresolved dependencies |

Cover narrative sequence, Japanese wording, static imagery, audio/delivery, continuous movement/editing, musical events, clock alignment and required independent verification. These are no-count schema rows at bootstrap, not a claim that each source channel exists. Effective visual sampling is recorded as observed or `UNKNOWN`; media frame rate cannot fill it.

Required unresolved items block the dependent completion claim. Missing primary-language TXT specifically blocks unsupported exact-wording claims; do not treat AO/HL listening as TXT or impose a universal TXT gate on otherwise supportable observations. Optional gaps remain disclosed. Never mark uninspected evidence `NOT_APPLICABLE` merely to close a checklist.

## 5. Actual records and next intake action

**Technical witness set, 2026-11-20.** The owner authorized the twelve Japanese TV episodes for a sequential independent run. All twelve release objects and their derivatives are identified for technical reconnaissance. The entrypoint admits E01 for bundle-mediated reading with the owner-authorized measurement route. E02–E12 remain technical inventory. The narrative high-water mark is NONE. The owner identified a separate Gemini generation. Candidate intake awaits the independent E12 freeze.

The release filenames identify Nekomoe kissaten and VCB-Studio, `Ma10p_1080p`. Retail mastering and broadcast equivalence were not independently established. Each E-number maps the release MKV to the episode entry in the outer batch summary. The inner batch summary describes only the E12 invocation. The pipeline produced a Japanese-only ASS sidecar from the supplied bilingual JPSC witness, a soft-sub remux, a picture derivative with Japanese text burned in and a sampling bundle from that derivative. Open the release video for an unobscured composition check when the burn-in covers significant detail. The ZIP and unpacked directory have the same members. Complete audio is the separately supplied FLAC. Neither the heuristic scenes nor the shot-labelled rows in the manifest supply an editorial shot list.

### 5.1 Exact episode witnesses

Each stable prefix has the form `SPV2-W-E01` through `SPV2-W-E12`. Suffixes identify the release (`-SRC`), original bilingual subtitle witness (`-JPSC`), Japanese-only text (`-JP`), soft-sub remux (`-SOFT`), burned-in picture parent (`-HARD`), ZIP (`-ZIP`) and main-programme FLAC (`-AO`). The AO suffix identifies the audio object. A listening claim additionally requires a perceptual receipt. Private records retain original filenames. The source and derivative hashes below were calculated from complete local files.

| Episode | Witness suffix | Bytes | SHA-256 |
| --- | --- | ---: | --- |
| E01 | SRC | 1028900069 | `7086003a39963e1afa5a2e3da30a065a390f5e7126b78941204dd704871ddb54` |
| E01 | JPSC | 548601 | `a755d7d198533b0c1aaca04aee26aba47562d6faf1b021f284ede23831dc51c6` |
| E01 | JP | 41896 | `ce93a24660eea14d9a4b31b10e33652dbf2d14520ceedf41e48ea45bd7f80b00` |
| E01 | SOFT | 1029321121 | `b48003f392fd2e5b89c95e1114f6fd72a1bdf69e6704bb5a1bd6cf75b1656e0f` |
| E01 | HARD | 902664208 | `57419dcf8e8a61e3beb3cbfa04f225150e3da1fcae99c34d0dcdaa4cd3f94e2e` |
| E01 | ZIP | 102079345 | `4aad8ad3f5865db20129a8a59521156696369eedfb9f71abc948a0c61433844a` |
| E01 | AO | 241366212 | `f309347fe1ece33f077cb5ff4bf7619095cad30735ba31bed63632363c7e9694` |
| E02 | SRC | 877060330 | `be5e96aa8e3436bb472b88611a9a8c18bf22d102d6e68349abee16808aaa56e7` |
| E02 | JPSC | 9718083 | `465bb12241000babbbe83417cf99c9939c62fc294b6f977b2e98d92f15998ee0` |
| E02 | JP | 4670403 | `75a3b9fe06eb8d3e205b87641400c8fb3bfa8af118987846972c66c31285e58d` |
| E02 | SOFT | 881813236 | `70babc0e6981dab2704e14a31372754b8301a3397efb303baa694c2d7ab9c34a` |
| E02 | HARD | 753194482 | `5f069e778ef43e70c944d18e32a33ad4fa341f0c68097bbdacbcb0ced9cd4a43` |
| E02 | ZIP | 122463352 | `8b6668bc1a7b86ef3c6250990f57e4beab224ace2f7db9cbd32b774c06f6b5f9` |
| E02 | AO | 252503268 | `04dae667e89cc911cdef199951c5e2e7a35ad211d98240a8a6be89fe7949fefd` |
| E03 | SRC | 763108493 | `edcaefe45390bb4ce083e11c6e24a54e9d089ca9f105df639b066c8475857b2e` |
| E03 | JPSC | 9739003 | `20f2c3af6bad561e1d7d5c37d4ef754b4a909ee693999fe58c2ac8b96517d8c4` |
| E03 | JP | 4672268 | `36a443359aeb7755fa0433ffdaa081a20931ab9748c9e946e6859b55ac5fb60c` |
| E03 | SOFT | 767862630 | `72fd51e0e506878d5e21c3cdabe1d222fdafdc3a399ce2522cb8c872eec97395` |
| E03 | HARD | 686156640 | `c9d3dbfcff1f4b7d28bf04828e4e0766074eb0d20edf7160da51431e58356839` |
| E03 | ZIP | 108248885 | `70d749fb7576f4e1c27e93db5ab805b510bca3b974a415acb19a9593baa1482d` |
| E03 | AO | 234418754 | `018c05c90a86be7c4833043d16edb6ebf61ce0111e5ce353bc859210261e89a2` |
| E04 | SRC | 816729017 | `b45b9b0dce648bfe4e57c0df6b0b9e4f214b7aee35590f6c0b004b413830a8f9` |
| E04 | JPSC | 9727655 | `06d62d0a96f15477b5fec2f9929ef4b00d36fae95ff37b9b9afd5a252da5cd96` |
| E04 | JP | 4666301 | `90d9dd53bd94c5494ec61b0976fbc2e8832b89b4ef8701653f1949121e11bec9` |
| E04 | SOFT | 821476408 | `e635e083c89edbf002f7f39780118bc0897c879bd3831a4edde842fc62be5aa9` |
| E04 | HARD | 719873518 | `272ad2fe77cdbbdd28aa56fd68e0cb11391376bf63fb3a752356acc5c9786172` |
| E04 | ZIP | 119024854 | `c9d23962ba66396ae49f27d0b67993ce8757a08174a66db71a386033c5485159` |
| E04 | AO | 243910504 | `5265a555132a925d6f2774692821582895f0386e55ff331de3ab775cf0d1c57a` |
| E05 | SRC | 836499148 | `4b7cc54bc2b1bda7ff348bc79a2a5949e6783de834f72d3c9cf255cc874f41a0` |
| E05 | JPSC | 9716927 | `9c01386e58c5036b822bbe3c77037c784f780a8e78184a36fd481048e6e67fa1` |
| E05 | JP | 4669895 | `d29e850cd43ff293f498634a1c1be5ca075547c226a90ed59efb29ef4404fd36` |
| E05 | SOFT | 841250636 | `8ed0e2510b435261ee1ef6ec1dd78645da4929107ec7516d2febd3ba7e47ffca` |
| E05 | HARD | 717149033 | `459e4e7dac296da076a413d0610ca2c01aa52b01b21ad4deb9e0315ff29d1a8a` |
| E05 | ZIP | 135909845 | `b9e946b9d551e728d677da847545840fe7b37f72bf63db7262f922e3a8119d25` |
| E05 | AO | 243182495 | `b6a547a46482b5f55f241bcb1f459abd6f1ca7d8bf2d2046d8527ae276e08844` |
| E06 | SRC | 855448388 | `dde3e819d53a287f6b2c7327482b6db4a0aa04496ff50bcccf25e18d99fdba18` |
| E06 | JPSC | 9811098 | `fbd3408edf3bc8b0e7f0d04ca974e612f9f9422ee06b2a213b0e884ada495d35` |
| E06 | JP | 4667090 | `05b38429cbc75dbc6fd475891fecdc15db142c52ac94ae94f3ce7c9156d63a5c` |
| E06 | SOFT | 860197013 | `93334b43786c9a9e153abe0ab59be901f1c48cf9382a471c8261ecd5325d4253` |
| E06 | HARD | 769974236 | `fb30205168e61a6148ab9e0f42c699dc96269e2c375cc40d2291d797515fc0a8` |
| E06 | ZIP | 111679828 | `f6ec75da507aa23195e49e2d914d005d6d3350cbcb321a3a15ca6cfb993a5b68` |
| E06 | AO | 244954434 | `c2b5b107732ea8681a0d6a8330d5c6b8de75ecd36a3c7ef75c522ee3bf1794e7` |
| E07 | SRC | 800227151 | `4cc1c348f65df1f5c181bc064c2f610044345689ca2e3134de42425ad22716a7` |
| E07 | JPSC | 9727867 | `ced189559f97fdbeaa03e0cbbdc34ada64b5237eade97882d4f8339750275a42` |
| E07 | JP | 4673682 | `2bfbbf02b1d512b78157c51e27c279a10093ca07b5f0e35dc25468491eb7d807` |
| E07 | SOFT | 804982394 | `913fe9f5fc029678d3429870088ba504700f494ebe50421dbf6021ea0491aef3` |
| E07 | HARD | 719507053 | `47090e392188e950357ba0d147f5175866268ab92626d29f122e333cc0e43b25` |
| E07 | ZIP | 113868775 | `114e8a5b03cd0e5d9afff85098e69ecf6ab58dcd9170ddc5fdc38e394048be70` |
| E07 | AO | 241210771 | `9ab55694bfaeee414a2c784342af33705af1ef22753dbba7f6b1408f54228395` |
| E08 | SRC | 801383467 | `b2607d5d3cae8f49e660b2c841d2508630b2aad5a565491c7e8c642d6eca0fc7` |
| E08 | JPSC | 9713123 | `8b2a229e0b4110e56457f7414cab9d7e34a00af127ef94a04399b0440a235a29` |
| E08 | JP | 4668640 | `1cc0fc958a859cf0868c141e0b40a7f8aa095588e23c26bef4eb9a265d03eb44` |
| E08 | SOFT | 806133183 | `0d7acbbd979896c6ca749adccae8178d6b89b6d7d6a855e4acaa5b088304c77b` |
| E08 | HARD | 683093956 | `59388060e84b3a060ba20e6e40a71329abe771797c2cc5ac6166dc96e2e434c3` |
| E08 | ZIP | 110063673 | `c7ddb6b19d2ee080fc0bc644301d824e9d39461a8265e00ad6f7ef0806fc8963` |
| E08 | AO | 237429250 | `a51d4fa8526582ced0a4b557bc464c9521a294d82d4875c0150fec2e35e312c3` |
| E09 | SRC | 891689437 | `ec801b5fbcc6bd59b0f30e76810838bd9c4adf16dce4768b5705ce9577e219e2` |
| E09 | JPSC | 9714624 | `62fbbead39dfae7f69e25b33a3c06313cfffba4309e4353e7586ea271962aefd` |
| E09 | JP | 4665299 | `75c566bcaab650f38b459d6b5fdfc1a2da83d4caf9442032efdffa5ade335d85` |
| E09 | SOFT | 896434479 | `bea93794435c88a62d4a8c1baf207c8755f85f7f4b727aa6034085000dde8115` |
| E09 | HARD | 764577567 | `ad4ac4b8511b25492775370ad20f9dfbba6bcbae49b62d5fb550625441df428d` |
| E09 | ZIP | 121005494 | `754b36bc9ab417c7ca96424f5b3dedcc9b32ebdd85178752f2b688e182ece494` |
| E09 | AO | 240793679 | `a358f38ac998001e92952de746700accbcdddad6bd6004c1b422dca3466b95ed` |
| E10 | SRC | 918514721 | `6d648123e2f41832f0c3bf99c6175b51b2892cb49fdd7874e6acbc627498b0f7` |
| E10 | JPSC | 14113643 | `6e6c1d822c50e9034feda8632cd2250409637c432bcb67992af5bb6a27b33433` |
| E10 | JP | 4670636 | `7c294c79c2ec23a53a9a093d392f3f32323b571ffcb6b1290f643bd4f79a58b6` |
| E10 | SOFT | 923267324 | `6360ddcfb5ea49a1d3687ed112e282215bed3b6b3ed0b3666b10c4bed56c6c0b` |
| E10 | HARD | 761800942 | `41a25298e8472985a23aa8facd716ff17cbc5a8ea8aa94f43cfab2203889f422` |
| E10 | ZIP | 122871803 | `643ef206bdd7cc66b846f51f843f97a15f830563f0314bfaa61c2ff73151f604` |
| E10 | AO | 249362541 | `cdfaaa088cb0c536df04bd2e4e70357295613214f4826d506a22dd5f5f331785` |
| E11 | SRC | 830741325 | `a6ecd817b9eac63a254c5d133f943d084b197817113fc9366616ce5ca88f58e3` |
| E11 | JPSC | 9711414 | `62594876a89f648869c6bbb12aa340c779c27c7dfccd341a670cc4498a4e7d0a` |
| E11 | JP | 4667136 | `3bedfe67fc2269ff984c7728a90df42f461cdbe7ac89732d1de2aa688572b42c` |
| E11 | SOFT | 835488864 | `6b9e8b5adfaef1c3ba7b82143b24f1af62e02aa8db3421f7e9fe772eac5353a5` |
| E11 | HARD | 715268610 | `992cfa390af853702fb57f7fa05ef4405c2cf5e273d16a1f939a61ab51c9029a` |
| E11 | ZIP | 112160823 | `47ea54d4611dbb02f7ada01bfe2db0773c4c80406e30d1d26fa6194f6943b329` |
| E11 | AO | 236611774 | `a19f1fc9f7e5468035f58faf943a5b59a48d3f1b9e48b30f4f73e7e6ea465e56` |
| E12 | SRC | 975887200 | `4c7c3dbddd28c081ee51af52607146258d0c57262639a73042fa4f5ea8ad985e` |
| E12 | JPSC | 9708494 | `bb3eb12ad1e9e6324700ed8a684f50c8ca8a7657d8bd9fe751f524a877bab74d` |
| E12 | JP | 4665524 | `9b3e5773b9e0e68bccd559c39488de23c62f6313a494e33366f75297afdc29e3` |
| E12 | SOFT | 980944158 | `f66ec1bb1dbe7c6199d12aaab8d40bd75a2ee3227cf9e0f18622839cea75f976` |
| E12 | HARD | 850320797 | `c7177c3ac492229fb5500e4006bb911c6bc4b013eeda5cee8693ce4a618ecc3b` |
| E12 | ZIP | 121218107 | `6f49f6c2cc0505b4683d86fb560ee6712d8fdb8dc8719146b43e1e622c2e801c` |
| E12 | AO | 251452168 | `c9ce5e732d1885849cc9bd7285b860ef166884cd5f96ff489274fac556641374` |

### 5.2 Coverage for navigation

| Episode | Release duration (s) | Retained frames | Largest internal gap (s) | Head / tail outside retained frames (s) | Indexed cues |
| --- | ---: | ---: | ---: | --- | ---: |
| E01 | 1371.221 | 736 | 7.632 | 0.000 / 1.144 | 439 |
| E02 | 1371.040 | 808 | 7.860 | 0.000 / 1.046 | 1181 |
| E03 | 1371.205 | 785 | 10.090 | 0.000 / 1.128 | 1209 |
| E04 | 1371.205 | 891 | 9.760 | 0.000 / 1.205 | 1133 |
| E05 | 1371.040 | 876 | 8.322 | 0.250 / 1.005 | 1186 |
| E06 | 1371.037 | 826 | 7.832 | 0.000 / 6.527 | 1147 |
| E07 | 1371.040 | 778 | 7.007 | 0.000 / 1.088 | 1213 |
| E08 | 1371.040 | 767 | 7.414 | 1.252 / 1.088 | 1157 |
| E09 | 1371.037 | 856 | 8.880 | 0.000 / 1.043 | 1090 |
| E10 | 1371.205 | 831 | 8.231 | 0.550 / 1.086 | 1165 |
| E11 | 1371.040 | 797 | 7.633 | 1.250 / 1.005 | 1129 |
| E12 | 1371.050 | 860 | 7.944 | 0.250 / 1.098 | 1111 |

All release pictures are 1920×1080 at 24000/1001 fps. Retained stills are event-selected and irregular. Entries for scene boundaries and deduplicated images are navigation aids. Every retained JPEG and contact sheet decoded, and all nonempty frame and sheet references resolved. A missing still at an episode boundary is a gap in the sample. The full release remains available for targeted inspection.

All twelve release containers identify default stream 1 as Japanese main audio. Each companion FLAC's decoded 24-bit stereo PCM at 48 kHz matched the original main stream’s declared PCM digest and sample count. E01 and E12 also contain nondefault Japanese AAC commentary at stream 2. The extraction preserved a playable main-programme witness. The principal’s audio payload was omitted by the model interface.

The three stored copies of each episode’s Japanese-only ASS matched by SHA-256. Speaker and paired-translation fields were empty throughout the cue index. E01 has 439 raw ASS Dialogue events and 439 indexed cues. E02–E12 have more raw ASS Dialogue events than indexed cues. Row counts cannot establish the number of utterances, identify speakers or verify transcription. Japanese wording, translation accuracy, cues, staging and musical events await episode inspection.

See the [independent run-entry checkpoint](../07%20Audits%20and%20Handoffs/SHINEPOST_V2_INDEPENDENT_RUN_ENTRY_20261120.md) for clock testing, actual channel availability, limitations and the next permitted technical operation.

When accepted work later advances, update this register's inventory/coverage and the root entrypoint's boundary in the same transaction. Preserve earlier receipt and witness identities. The [evidence ledger](../03%20Longitudinal%20Ledgers/SHINEPOST_V2_EVIDENCE_AND_CLAIM_LEDGER.md) owns claims and dispositions, while this register owns what objects and channels were actually available and inspected.
