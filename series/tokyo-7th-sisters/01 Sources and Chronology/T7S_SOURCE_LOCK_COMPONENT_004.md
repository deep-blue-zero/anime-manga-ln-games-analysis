---
title: Tokyo 7th Sisters source-lock logical component 4
artifact_id: T7S_SOURCE_LOCK_COMPONENT_004
artifact_type: source_lock_component
series: Tokyo 7th Sisters
generation: V1
version: '1.0'
status: canonical
do_not_use_as_current_authority: false
do_not_use_as_literary_evidence: true
supersedes: []
superseded_by: []
---

Ordered byte interval of the complete logical SourceLock; read only through its current owner and manifest. No primary-source payload.

<!-- T7S SOURCE LOCK PAYLOAD BEGIN -->
      "operation": "T7S_2034_NON_MAIN_ELIGIBILITY_AND_ROUTING_AUDIT",
      "database_sha256": "1bc0bf5d140e675554cf38ed4e3108be3c8c932c375c494bd29d3e4bb7b2ed87",
      "database_mode": "mode=ro&immutable=1; PRAGMA query_only=ON",
      "screening_manifest_sha256": "fff84f8a0e0a5fa185df0782139a9ccb61a9ce1c23a65696ce3894e1aee257bc",
      "screening_manifest_bytes": 155587,
      "packet_files": 269,
      "packet_bytes": 11417645,
      "eligible_2034_sub_episodes": 743,
      "eligible_2034_event_episodes": 231,
      "eligible_2034_episode_membership_sha256": "afce2d28c27baa949bde41088be50720e4aa53874166946d9da032e191689c5c",
      "blocked_2053_sub_episodes": 11,
      "blocked_2053_episode_membership_sha256": "4f74c9c6fd33d37d49ef0af4eb4ee1f0d72d1f745067e0ed43b193919d4948c8",
      "crossover_episodes": 1,
      "crossover_episode_membership_sha256": "a3129428958e3333d4015dca7ec73ac7a49e3efd27557858e01be7d0547fd3a5",
      "additional_2034_audited": 133,
      "additional_2053_blocked": 9,
      "additional_main_attachments_reconciled": 86,
      "supplemental_records_partitioned": 30991,
      "coverage_records_after_split": 1591,
      "guardrail": "2053-blocked episode, additional-resource, and supplemental-message text was not emitted or consumed",
      "boundary": "Eligibility and routing only; newly admitted 2034 non-Main sources remain unreconstructed and unintegrated until their assigned portfolios close"
    },
    "b0080_open_verification": {
      "checked_at": "2026-09-24T00:00:00-04:00",
      "operation": "T7S_B0080_OPEN",
      "native_category": "Sub",
      "native_top_layer_id": 100010,
      "native_character_family_layer_id": 200130,
      "native_chapter_layer_id": 300520,
      "episode_ids": [
        "202001101",
        "202001102"
      ],
      "script_ids": [
        "scout_041_01_01.json__5574dd10d3af0d42",
        "scout_041_01_03.json__d5f035a78e7c3749"
      ],
      "primary_document_pages": 91,
      "text_records_reconstructed": 78,
      "command_only_pages_pending": 13,
      "native_voice_reference_pages": 62,
      "character_visual_refs_pending": 890,
      "authored_choice_markers": 0,
      "status": "SUPERSEDED_BY_T7S_ING_B0080_B0099_CLOSE",
      "boundary": "Historical open receipt; all pending presentation and cumulative integration obligations were closed by T7S_ING_B0080_B0099_CLOSE."
    },
    "ing_b0080_b0099_close_verification": {
      "checked_at": "2026-09-24T00:00:00-04:00",
      "operation": "T7S_ING_B0080_B0099_CLOSE",
      "database_sha256": "1bc0bf5d140e675554cf38ed4e3108be3c8c932c375c494bd29d3e4bb7b2ed87",
      "database_mode": "mode=ro&immutable=1; PRAGMA query_only=ON; PRAGMA temp_store=MEMORY",
      "selection_rule": "First 20 complete native i-n-g chapter layers in source order beginning with already-open chapter 300520; category Sub; top layer 100010.",
      "block_ids": [
        "T7S_B0080",
        "T7S_B0081",
        "T7S_B0082",
        "T7S_B0083",
        "T7S_B0084",
        "T7S_B0085",
        "T7S_B0086",
        "T7S_B0087",
        "T7S_B0088",
        "T7S_B0089",
        "T7S_B0090",
        "T7S_B0091",
        "T7S_B0092",
        "T7S_B0093",
        "T7S_B0094",
        "T7S_B0095",
        "T7S_B0096",
        "T7S_B0097",
        "T7S_B0098",
        "T7S_B0099"
      ],
      "native_chapter_layer_ids": [
        300520,
        300530,
        300540,
        300550,
        300560,
        300570,
        300580,
        300590,
        300600,
        300610,
        300620,
        300630,
        300640,
        300650,
        300660,
        300670,
        300680,
        300690,
        300700,
        300710
      ],
      "episode_ids": [
        "202001101",
        "202001102",
        "202001201",
        "202001202",
        "202001301",
        "202001302",
        "202001401",
        "202001402",
        "202001501",
        "202001502",
        "202001601",
        "202001602",
        "202001701",
        "202001702",
        "202001801",
        "202001802",
        "202001901",
        "202001902",
        "202002001",
        "202002002",
        "202002101",
        "202002102",
        "202002201",
        "202002202",
        "202002301",
        "202002302",
        "202002401",
        "202002402",
        "202002501",
        "202002502",
        "202002601",
        "202002602",
        "202002701",
        "202002702",
        "202002801",
        "202002802",
        "202002901",
        "202002902",
        "202003001",
        "202003002"
      ],
      "primary_episodes_verified": 40,
      "primary_document_pages_verified": 2624,
      "text_records_verified": 2434,
      "command_only_pages_verified": 190,
      "native_voice_reference_pages_verified": 1866,
      "visual_references_verified": 21356,
      "authored_choice_groups_verified": 0,
      "inline_movies_verified": 0,
      "coverage_records_reconciled": 40,
      "canonical_targeted_case_readings": 20,
      "selected_character_composites_verified": 40,
      "performed_audio_reviewed": false,
      "episode_membership_sha256": "8093a07bbbbb082012cd77a08486c8d8fc113190d3046e756d791b49615404ec",
      "tranche_manifest_sha256": "dce8b0793bea11ba03a0fc212fbf5cff769eecb72e07ed5b6356c9decd792c3b",
      "static_review_receipt_sha256": "afd38529d60ac016a75c9c1113a6655ac17e62817b7c0b41bef1666f8fceeb9c",
      "source_sha256_by_script": {
        "scout_041_01_01.json__5574dd10d3af0d42": "51ce93cd52e49b41cd5934bf29ea62c4ead07334a155a6b428e71b6c7d481f7d",
        "scout_041_01_03.json__d5f035a78e7c3749": "9a4ab386c2dadc458c9092ae49e0a706123f03a8a7ba2c1c36a76a44d26ace3c",
        "scout_042_01_01.json__99ecd1a35abb3284": "15520bd7ee73f6c7699621adc15b583275fc0ec62565cd9f2e55ac702dc34ade",
        "scout_042_01_03.json__3ce4ba12c291e605": "34d85fee74fa7fce560e1e0f80c2c452c93cb391f71033d63b9964231018d12c",
        "scout_043_01_01.json__c8047e6f485f6073": "6e919c59e86d61b9cf5232f12c79cad7f0913fa798db0c243f5c5da4d83da382",
        "scout_043_01_03.json__7722f6c116884eab": "2e4a30805169af879d05bc062088fa75b789c429a800d6a4953311366e4d2cf0",
        "scout_044_01_01.json__15644133881b9cd3": "2d53f06a0301cc57882efb9f9a284eb6419318a6897bfc52de6b2c63f9a8928b",
        "scout_044_01_03.json__f525848d0ec3add8": "67073e5c345ff3753ea63c500605a3dc16c2f5d25f9c74e86c56e827bba5dc8f",
        "scout_045_01_01.json__37c43e7ffd1d0144": "fa23fd96d181cec5226630dba1fe1097b2cdfb10c2178aefa8c363dda04073c3",
        "scout_045_01_03.json__251e15c016a5ba2a": "6f278166d2589b2d68f22e43e5228db03a4e1fb36c2ccbcbc22a4f590c8e77a3",
        "scout_046_01_01.json__685807f4f1866805": "d61be0575b8be485630b4f18ac1f8bbecfff1a54d3215313367de7952a373aac",
        "scout_046_01_03.json__11d9d0d57d3a83f5": "5d71732a64ec26e8780b0752442f6468fbcd68704c62c25f4d081c5503f694cf",
        "scout_047_01_01.json__89c3073b14531e33": "bdd4b4d6ba279a2f63c7a75cdc01cbc48df6a63a0aacf70b9cc1cbd13b14ce85",
        "scout_047_01_03.json__54aa3d0b0654c8f1": "cd78a510165edc52ca1c222ae2fbb764943aaddf6aee4bb0421e640992232f75",
        "scout_048_01_01.json__dc5be3a33a92189a": "126d32b0c7986d20eb376451ddb8d1611a9ee8ba8d5dd097737158e842ce298c",
        "scout_048_01_03.json__0d4aa734e59e3689": "7409dcfbe2704fcdd48f5132f493e718c0d2d7c05d898d34207dcce629cee774",
        "scout_049_01_01.json__e8451ec6cf0a9cd4": "1482a2e545002c84ac75dfed5f762ecaba9986b19f2b46fbed4b66e0b87e12f3",
        "scout_049_01_03.json__614dd483932cbf10": "24c2c5d41d1596a629ad2c584822d363ad043e55c63fd7f30bb6984ddf9d1457",
        "scout_050_01_01.json__9f5ac0f4e17c3780": "6ca01aa3b2176850ebd358bf5561cdd7c5f06a8cb33dcba92cbb2cc4908b5116",
        "scout_050_01_03.json__7fe92c3e3b420639": "999cb80dca3e5e8820bff89be03da26e09af7d55ea3add28b62a239af2e33640",
        "scout_051_01_01.json__7a2a6e6369f8adcf": "7bdd385c36ea1e7876ba616b5e46457324a506895ef4b85bf9eb1f3f16986272",
        "scout_051_01_03.json__d5c812ea91329291": "ede2381a4ec1d7402813e912a3a72a0ace984c3b6806ea53116dfcb0a4a780e6",
        "scout_052_01_01.json__69531669a998774b": "d777cf4c0d35812cd4436bca0543b3fd8743be0db6698a6ec6a40f275bfff5ea",
        "scout_052_01_03.json__8df1e6c179838968": "5038a4150c60fc0238ed02437bac1b564d34f72e560bc6a341d55d3ffdefe197",
        "scout_081_01_01.json__50d9050e014846c9": "60ea33cf044c10809778c2f8fc264be3a1f04c1f92f27071bb349307c7dfd379",
        "scout_081_01_03.json__f3b0ad95a2c8a6dd": "770269a69d69c06b4bc4322cdaf0111858c16215c1cb5427ba207570dd3d1649",
        "scout_082_01_01.json__312179e87ee349d1": "2619905992ce689039de524f05907050f8c1079a76571f36e32bcb9a68b5a116",
        "scout_082_01_03.json__a477648aa044487c": "6540af809884139517d0d112f0c7df332397e9f6587ab1ff6f83b53ffd21bb8c",
        "scout_083_01_01.json__54047400e2aaad03": "301e6dceed69923112506aedbe012ad650920fa3132093ef85835f1ab3e307a5",
        "scout_083_01_03.json__7386a76042693404": "70e0b6f4487ded60646f87a518d932fcd2ab18c8b032e158c72f10170aea9bc2",
        "scout_084_01_01.json__50cbc54adcd47aa2": "d457916fe5f5a7ca95ac4eeb26d31df60fac495cf9b99474645c47cc6fe3786c",
        "scout_084_01_03.json__688044377d8e400b": "82b469bd4eee058762ca94e6c2a31ed3475a114a295872369cdf29031eccc915",
        "scout_085_01_01.json__a2f0c4ae2baade70": "6a0a7748718a4c62bc4494f08f29dc78b047072babd0602a995ce7a861d8e124",
        "scout_085_01_03.json__f05ff0a67c90bd89": "4cd10da19c37df138530b7da048b289303aae9e7aa13606817861139cfbe81bc",
        "scout_086_01_01.json__ce53371e0698251e": "82ad06720dd8f132e3b1dae28693de808bb443f5d0c20326e0b8cb79e34e5615",
        "scout_086_01_03.json__0325ce74c3cefe45": "857331a4eb7265617809531e4c12ccecd7c1d8323e82a96247693255ad71a575",
        "scout_087_01_01.json__ddf6e3b435c36987": "7e0e18acf505faae69e024581d1a90646eaa8554a51928877512a766cb075299",
        "scout_087_01_03.json__f9601d404d6b0182": "eaefb9026d7ca71d2a825d29f6f0847604b24d42fbf692a45ac042226d4cc741",
        "scout_088_01_01.json__8768cd44ae2c6eca": "fb3eda224533de81236c2832e47dec1c360072199f599f3f497781031bb333be",
        "scout_088_01_03.json__bbf43e5db5b24503": "3d869c169190b4740dffa253ab2978df0f70c55f3b9703f1f4942d500d5bf207"
      },
      "normalized_sha256_by_script": {
        "scout_041_01_01.json__5574dd10d3af0d42": "890bf2a112b0f976ad6dd4ea5123a0ff5e05661b050dbcb588680199be618eed",
        "scout_041_01_03.json__d5f035a78e7c3749": "84fbd338446b44f0e996cc1b5bf31ad6b881cb9d9381686b80cfb5d17ee0a726",
        "scout_042_01_01.json__99ecd1a35abb3284": "6c8b15d1e7b0fe069930221ed14d5f54b29484cf9212a337bd725aaf63564ea5",
        "scout_042_01_03.json__3ce4ba12c291e605": "3970daa3ba56c66e0292b6ad93af0944670a569df8aa94e7af9d9ad208e746f3",
        "scout_043_01_01.json__c8047e6f485f6073": "6bff208b58138fd55848128041ccbf095dffa7303d2b9911fd870cb504acb162",
        "scout_043_01_03.json__7722f6c116884eab": "165ee98dbc915bf61126621148104d60179ff724cc53131d18a2bda6565c09bc",
        "scout_044_01_01.json__15644133881b9cd3": "7a8c2497c204e170f6591de2d8754af3d3385fb54f402917fcc1d13ea4127df6",
        "scout_044_01_03.json__f525848d0ec3add8": "c70ef18ac9ffa612b234d91b2613dcc3a87d98988c6683f4881f95d70cdb284a",
        "scout_045_01_01.json__37c43e7ffd1d0144": "5de3668303dad3b9e165f8ebec875b6f0230b1d608e2e5916f1d17b71f0b5423",
        "scout_045_01_03.json__251e15c016a5ba2a": "f6a209d4dea974bd7c602778f999f107f52e0afe9c49881da74e212bdc2d4254",
        "scout_046_01_01.json__685807f4f1866805": "0d4621383784949d40165c3a950d76fec504d9b88b8a910620eab8c092b408e7",
        "scout_046_01_03.json__11d9d0d57d3a83f5": "2acf27fed4e4fa50f51a90b4fb82f10d9533a943139a14c55f8f29a409557ddf",
        "scout_047_01_01.json__89c3073b14531e33": "102248dd357d3076502da16b34ec3669ae1830e77063c6c4c6592c3c0a97741d",
        "scout_047_01_03.json__54aa3d0b0654c8f1": "4abe4ded843129dce1754434176aa37d5062771e0d667910307b33fc90a5dd63",
        "scout_048_01_01.json__dc5be3a33a92189a": "be7232edf34a8b17af76dadb6228295a1d28714c393d6e4d45c151b081aff9de",
        "scout_048_01_03.json__0d4aa734e59e3689": "2b5047365fd0462b0eef5523531ebc660c41a108e2fd9ced26c7d6ac79ff92b2",
        "scout_049_01_01.json__e8451ec6cf0a9cd4": "6cb1b58e9be98dce97e038f25a444cf1cd743461c638566b16dbbf48ff4f3a82",
        "scout_049_01_03.json__614dd483932cbf10": "e3bd1c2fcb99bba256f5a582c7f1cd165634d1abd20096b2058f266a8a3162f2",
        "scout_050_01_01.json__9f5ac0f4e17c3780": "1631ec3a7f73103bde5dc693799b9e7c8d0d61fc758b06c5d9d2f24f60e63fbe",
        "scout_050_01_03.json__7fe92c3e3b420639": "da37e92dff5c31e5cae3b4edcef12fb4761bea5e0d0a19ee56e250da6a90ef42",
        "scout_051_01_01.json__7a2a6e6369f8adcf": "07aeb7be601b1cea86b626e9f2c9434f06af8915a3a42f7cbf4e5f09582f6cd7",
        "scout_051_01_03.json__d5c812ea91329291": "f21898341e1e62979b9736b96fc8e8d7ad1ae667f6e577e16c1c52269e9a8026",
        "scout_052_01_01.json__69531669a998774b": "8904c641fb0efcbd250ae4d037552e11d2dc5ea406e1853b20a5e2cbcb226170",
        "scout_052_01_03.json__8df1e6c179838968": "4df61034eed167a9de1519dc3ab482e569609f4e0e223bd0e45ad911a83110c0",
        "scout_081_01_01.json__50d9050e014846c9": "0ce7c754acb88808fe99287930a0e5c5d26288f066a961e05a8fbe92a75d6961",
        "scout_081_01_03.json__f3b0ad95a2c8a6dd": "de8168932f4f87c4161ffe7ea2a698621353559e61e76531216830c84e3bb1fe",
        "scout_082_01_01.json__312179e87ee349d1": "d18a91cb49755b0f6a8733df7e40400897dd17d4762c8bd0e0efa159062f38f1",
        "scout_082_01_03.json__a477648aa044487c": "1c3a5936c25d643e78b9d90046bd96b918ca1cc88f53769fb745d815ca13b3ec",
        "scout_083_01_01.json__54047400e2aaad03": "0259083ff49688059ad7b4093247c65e23f9f77a09b633d3e95e9919cc512bb2",
        "scout_083_01_03.json__7386a76042693404": "91be09804ece6f60cb95d7d75a8029ecbbd9b15b47a6731d9676fc1da22f0ebf",
        "scout_084_01_01.json__50cbc54adcd47aa2": "452a430f0eadb86a5ec9f26d7584c2390655c442ea31989821bb0a2c7fc1f49b",
        "scout_084_01_03.json__688044377d8e400b": "20665d9f7463594fdddb9442d3cecf654314e8e6551f025cd9fb65e57c35dcbe",
        "scout_085_01_01.json__a2f0c4ae2baade70": "4a3e6cc1fe489cea69e61440b084209ab3ccb0663a15b9dbd956e06adf86d5df",
        "scout_085_01_03.json__f05ff0a67c90bd89": "96c3df88e250cec0509c054b9922f0121fefa37e5e4699792d785eec9c02454f",
        "scout_086_01_01.json__ce53371e0698251e": "dd3f591840b1f671cf5c00b339caf6d950c793a8cb42d32f28f66835c1f4fa61",
        "scout_086_01_03.json__0325ce74c3cefe45": "3b67aeb841ec5b318198dbfd25d9808bbece6deadac8032c082f93d04b48d01e",
        "scout_087_01_01.json__ddf6e3b435c36987": "84543aacfde9f656f21cb0f14b0ad17e9eeb1db99d92d711290f6032d41d0596",
        "scout_087_01_03.json__f9601d404d6b0182": "53ac442085f8ccd2ad32509b8e40690964f2800981be029443f6dbecdb50fc1d",
        "scout_088_01_01.json__8768cd44ae2c6eca": "689f699c1a827fc06ffa575f466cb369ed5586dbd82b5d3efc526b1699e235ac",
        "scout_088_01_03.json__bbf43e5db5b24503": "f6995ae54e3da04f36d686a3e8c6f06b16fe4ace691580ac80c0a6d6e960ee91"
      },
      "boundary": "Exact first twenty complete native i-n-g chapter layers, T7S_B0080–T7S_B0099; every primary page and command-only state reviewed, two episodes per block, no choices or inline movies, performed audio explicitly unauditioned, no cross-chapter total chronology inferred."
    },
    "coverage_ledger_shard_transition": {
      "checked_at": "2026-09-24T00:00:00-04:00",
      "operation": "T7S_COVERAGE_LEDGER_SHARD_TRANSITION",
      "logical_data_records": 1590,
      "scenario_records": 1578,
      "supplemental_tranche_records": 12,
      "current_or_consumed_records": 361,
      "routed_or_unconsumed_records": 1229,
      "primary_path": "T7S_COVERAGE_AND_ROUTING.jsonl",
      "primary_bytes": 530853,
      "primary_sha256": "ba7d0f20be6138c72e89f35e1d6efcfb42faa7e3fee6103ba9d1e5d96447e00b",
      "primary_membership_sha256": "c0ad7cc4a0c267aca2b7ec55b3bb42d3f16f90561295dca4a94ad05c0817be5e",
      "routed_path": "T7S_COVERAGE_AND_ROUTING_ROUTED.jsonl",
      "routed_bytes": 688668,
      "routed_sha256": "b3bfb469125aa05cfcf63c2646474a848ae39d679f3f0300b4d446e4ecff7724",
      "routed_membership_sha256": "af17e208f415b0ed2624e6c6a1667acff6ba87932c4dda7408efa221be668af7",
      "manifest_path": "T7S_COVERAGE_AND_ROUTING_MANIFEST.json",
      "manifest_bytes": 2421,
      "manifest_sha256": "1c3b5cecf8c3affb4e45ca38dc2503df47b4b2525b87ea1b626758df60007aab",
      "effective_state_sha256_before": "a0d2d51ff77de76130112a845e2a226137788a83b0efa272624e18ff38b76302",
      "effective_state_sha256_after": "a0d2d51ff77de76130112a845e2a226137788a83b0efa272624e18ff38b76302",
      "disjoint": true,
      "complete": true,
      "semantic_change": "NONE",
      "boundary": "The canonical coverage state is one logical ledger represented by the manifest and two disjoint shards; consume routed records by atomically preserving their effective state and history while moving them to the current-or-consumed shard."
    },
    "selected_media_recovery": [
      {
        "kind": "audio",
        "asset_id": "wav:6520d70a302f4f72da934bcd51dccb5d361ee980ca136e0d04d547dd9ff3f248",
        "sha256": "6520d70a302f4f72da934bcd51dccb5d361ee980ca136e0d04d547dd9ff3f248",
        "origin_artifact": "media:audio_relations.jsonl",
        "source_row_index": 0,
        "document_ref": "primary",
        "resolution_status": "decoded",
        "review": "BYTE_AND_RELATION_RECOVERY_ONLY; NOT_LISTENED_OR_VIEWED"
      },
      {
        "kind": "video",
        "asset_id": "movie:38beabd1e25a6d24ebee9f937b8d4ad024667cc6f539c6a4ed447e7a501fb590",
        "sha256": "38beabd1e25a6d24ebee9f937b8d4ad024667cc6f539c6a4ed447e7a501fb590",
        "origin_artifact": "media:video_relations.jsonl",
        "source_row_index": 0,
        "document_ref": "primary",
        "resolution_status": "copied_and_probed",
        "review": "BYTE_AND_RELATION_RECOVERY_ONLY; NOT_LISTENED_OR_VIEWED"
      }
    ],
    "b0100_close_verification": {
      "operation": "T7S_B0100_CLOSE",
      "checked_at": "2026-09-25",
      "status": "PASS_BOUNDED_TEXT_NATIVE_AND_STATIC_REVIEW",
      "episode_ids": [
        "202003101",
        "202003102"
      ],
      "source_bindings": [
        {
          "episode_id": "202003101",
          "script_id": "scout_089_01_01.json__db528778e1db1b91",
          "source_sha256": "77ce4edd2a02dfd43045b004b2f0631130d4b848aad82df8a3631d0cc06739cf",
          "decoded_sha256": "c83737c24fe905ae122a398fcc9299d85c3541ef8064586020d549a134cc7156",
          "normalized_sha256": "7bd13baaf3c0d2750f3fa9c1be2b21bcda31397b1e000dec12387e3a2f0ef1fe",
          "structured_sha256": "7bd13baaf3c0d2750f3fa9c1be2b21bcda31397b1e000dec12387e3a2f0ef1fe",
          "pages": 58,
          "text_records": 49,
          "command_only_pages": 9,
          "voice_pages": 27,
          "native_pages_verified": 58
        },
        {
          "episode_id": "202003102",
          "script_id": "scout_089_01_03.json__b1a455e04bfec1c7",
          "source_sha256": "ec2ae7fb3026b65763b8e3c78d38331d854e5456f7751f0e94842a7d8f6c0aa0",
          "decoded_sha256": "9c34e0c0785c31205e338efd36775ae0d1f7ef869cdf0213fe5607887e20f131",
          "normalized_sha256": "701439c47e50013f1099c68e53b9cd8353e8ff2b074246a80481c7dc546ac271",
          "structured_sha256": "701439c47e50013f1099c68e53b9cd8353e8ff2b074246a80481c7dc546ac271",
          "pages": 49,
          "text_records": 41,
          "command_only_pages": 8,
          "voice_pages": 27,
          "native_pages_verified": 49
        }
      ],
      "totals": {
        "pages": 107,
        "text_records": 90,
        "command_only_pages": 17,
        "voice_pages": 54,
        "visual_refs": 970
      },
      "native_packet_sha256": "67b5b5ff23ffaf2ad1b365992580e04a1da0ae687ae00b73787f833499e2afe7",
      "dialogue_packet_sha256": "b50ce4228a8befcd26f408a0bf51289b2a8ab0d99cab31512ba0a2c43cb84d51",
      "visual_assets": [
        {
          "resource": "adv_chara_144_01_01",
          "body": "adv_chara_144_01.png",
          "body_sha256": "20fc6bc7ed22a88c88e06eb84b21be11f06fa69cfd7f19e0de37a95c939d9f1e",
          "face": "adv_chara_144_01_01.png",
          "face_sha256": "0053bcd17594dda6eaad535480776a89040ccd77a5dec68e97d01666651bf7c0",
          "native_face_offset": [
            120,
            74
          ],
          "output_sha256": "399bb9344c170367460db6429a432ce79587937a515b68b27ff185193fdc93bf"
        },
        {
          "resource": "adv_chara_144_01_02",
          "body": "adv_chara_144_01.png",
          "body_sha256": "20fc6bc7ed22a88c88e06eb84b21be11f06fa69cfd7f19e0de37a95c939d9f1e",
          "face": "adv_chara_144_01_02.png",
          "face_sha256": "65cd13cbe3a95acd7e20cdbbcbd9a481417d7a79465c58649391550c59ab0a21",
          "native_face_offset": [
            120,
            74
          ],
          "output_sha256": "73bb9a9c4e3ccdb50b9c9d3ee2ba518a537fdb31424f0a5f154b4edc4141a532"
        },
        {
          "resource": "adv_chara_144_01_03",
          "body": "adv_chara_144_01.png",
          "body_sha256": "20fc6bc7ed22a88c88e06eb84b21be11f06fa69cfd7f19e0de37a95c939d9f1e",
          "face": "adv_chara_144_01_03.png",
          "face_sha256": "2bab9ec0eddb5ca11051d49b2714267809d6965d75a56ca837d7147a40dadd55",
          "native_face_offset": [
            120,
            74
          ],
          "output_sha256": "fce4fa840b78e077a55999b9fee26166bd8e611434d6931e5e29a8d639b83fdf"
        },
        {
          "resource": "adv_obj_0069",
          "body": "adv_obj_0069.png",
          "body_sha256": "f260112b43f0be320b021020fe0300eca3c92c883ebaf92334e3097c604b1f0d",
          "output_sha256": "a86095001df60d947da617149accedc57768ba17edaf1f263115a860641214cf"
        }
      ],
      "coverage_effective_state_sha256": "e96f0bf0e651e3f3f75580e725b2b78c04b96c7227562650b679b6c80f703800",
      "execution_record": "09 Audits and Manifests/T7S_B0100_B0159_EXECUTION_RECORD.md",
      "boundary": "All native pages and text pointers verified; selected static composites inspected; no authored choices or inline movies; performed audio not reviewed; no later-block semantic evidence used.",
      "mechanical_correction": "Correct historical routed-membership transcription 87930c to 87932c after recomputation against unchanged pre-B0100 routed membership and the original manifest; historical file/effective-state hashes remain unchanged."
    },
    "b0101_close_verification": {
      "operation": "T7S_B0101_CLOSE",
      "checked_at": "2026-09-25",
      "status": "PASS_BOUNDED_TEXT_NATIVE_AND_STATIC_REVIEW",
      "episode_ids": [
        "202003201",
        "202003202"
      ],
      "source_bindings": [
        {
          "episode_id": "202003201",
          "script_id": "scout_090_01_01.json__07d007bf25ac5813",
          "source_sha256": "9df0e61c2ace9c351e5fe2430213ec897d7b66078e79f3472b9ebd341ed1af96",
          "decoded_sha256": "f0c565e4c75c759a6f82ba020f334debd5ad05ec95d1f68304572e25174ebfa5",
          "normalized_sha256": "b4fa457cbf588cd0f47b26ad5f1c5e76a15df01f25577a4b333cc534883a3bfb",
          "structured_sha256": "b4fa457cbf588cd0f47b26ad5f1c5e76a15df01f25577a4b333cc534883a3bfb",
          "pages": 43,
          "text_records": 41,
          "command_only_pages": 2,
          "voice_pages": 31,
          "native_pages_verified": 43
        },
        {
          "episode_id": "202003202",
          "script_id": "scout_090_01_03.json__b2fb98338c660450",
          "source_sha256": "1226e9a13cbb1c67a52458c028b3c16fcbeb2f9dcb3319e57aebe585c016ce4e",
          "decoded_sha256": "1b9a6abe982be7a8f7c28a37fabfa8cbb9c675e3ebeae3a20415d7765ef25cc8",
          "normalized_sha256": "22f1f63d874d3de6371512e41a9aa10a57b564c9a566859dc495200f72c94a5b",
          "structured_sha256": "22f1f63d874d3de6371512e41a9aa10a57b564c9a566859dc495200f72c94a5b",
          "pages": 59,
          "text_records": 54,
          "command_only_pages": 5,
          "voice_pages": 45,
          "native_pages_verified": 59
        }
      ],
      "totals": {
        "pages": 102,
        "text_records": 95,
        "command_only_pages": 7,
        "voice_pages": 76,
        "visual_refs": 672
      },
      "voice_count_basis": "Distinct dialogue log-order indexes with voice resource; title-only cues additional; no performed audio reviewed.",
      "native_packet_sha256": "a797fdecfe063a97541369329c8f892b6619042366588c61509b09d893c62476",
      "dialogue_packet_sha256": "45414b9dce9be80e21d813f802810254d3bca8d293b07d3340e7a775cdf277b9",
      "visual_assets": [
        {
          "resource": "adv_chara_148_01_01",
          "body": "adv_chara_148_01.png",
          "body_sha256": "4ce7650d14226a78ef84e7be754b8b8600b9cff0d48dfd59a9ca03a3a9a029e4",
          "face": "adv_chara_148_01_01.png",
          "face_sha256": "9ebe31db2b7e89c6e81e25eebc43864dde38a46404a13c55e27e2207e9040f3a",
          "native_face_offset": [
            112,
            96
          ],
          "output_sha256": "e308635b1566fea246d92f4a6a8b2084632b8904a3def3639029ee73ddfc9353"
        },
        {
          "resource": "adv_chara_148_01_02",
          "body": "adv_chara_148_01.png",
          "body_sha256": "4ce7650d14226a78ef84e7be754b8b8600b9cff0d48dfd59a9ca03a3a9a029e4",
          "face": "adv_chara_148_01_02.png",
          "face_sha256": "7cad173b7de25029a7db1c1105f55b2ae602a066377c7aa2b3a2343b4b7bd193",
          "native_face_offset": [
            112,
            96
          ],
          "output_sha256": "df7a07f2b79226ef26b75ef9aab9ccb49082deab6ffe6880e68412a59fd9ec78"
        },
        {
          "resource": "adv_chara_148_01_03",
          "body": "adv_chara_148_01.png",
          "body_sha256": "4ce7650d14226a78ef84e7be754b8b8600b9cff0d48dfd59a9ca03a3a9a029e4",
          "face": "adv_chara_148_01_03.png",
          "face_sha256": "6ded9a9a7ba2f29e71dd1cf57276f9ab334207d361a230b9f6629d62184cb2dc",
          "native_face_offset": [
            112,
            96
          ],
          "output_sha256": "e3b2de86d548142516c59cb821ada3a095e02734ff6defd5dbc9b370737d8e16"
        },
        {
          "resource": "adv_chara_009_03_02",
          "body": "adv_chara_009_03.png",
          "body_sha256": "ffc2406a944338eecacf731a83cc2ecfedce4b3e932bcbf3574528e5939035c8",
          "face": "adv_chara_009_03_02.png",
          "face_sha256": "b7a199eafdad5a8779657a7155338e1dfea0bdef71d13dafe6561b8d93094f81",
          "native_face_offset": [
            109,
            85
          ],
          "output_sha256": "8e5270f32164291bcfe10b40ba20dab120c64d5a6e95f5e2022bc1634130836c"
        },
        {
          "resource": "adv_chara_132_01_01",
          "body": "adv_chara_132_01.png",
          "body_sha256": "0d49191320a09a7eee93f32d7af333bd6edcbf5ec4259ea97bca67053a4f43d0",
          "face": "adv_chara_132_01_01.png",
          "face_sha256": "ef98328fec3d962d011f35666c3595ffd10fc839c49a2825993359daea0761d0",
          "native_face_offset": [
            58,
            91
          ],
          "output_sha256": "b71fc3bb24fb825eb09e46085c6737d0c66ab4193c81765de9b7dc5ae09d6d76"
        },
        {
          "resource": "adv_chara_011_01_06",
          "body": "adv_chara_011_01.png",
          "body_sha256": "16fc2472d10c8972da16fad1f65b0bbc8c49cfb9daf7ebf2c583e54fedfb6004",
          "face": "adv_chara_011_01_06.png",
          "face_sha256": "300b99809fe080a24c3803e10c451b06c95aacbd519cf4db7883ed5ae8aef5d6",
          "native_face_offset": [
            89,
            54
          ],
          "output_sha256": "265da1873ada23d3876ae477923a70e2d8849383bee31407f9cb9dec78179271"
        }
      ],
      "coverage_effective_state_sha256": "8d05f4028dfd0d5a249a5362257ba7f5b431e589b8635c37075d680c9f6ce53a",
      "execution_record": "09 Audits and Manifests/T7S_B0100_B0159_EXECUTION_RECORD.md",
      "boundary": "Complete chapter-local text/native state plus selected static review; no authored choice or inline movie; no later-source semantic evidence; performed audio unreviewed."
    },
    "b0102_close_verification": {
      "operation": "T7S_B0102_CLOSE",
      "checked_at": "2026-09-25",
      "status": "PASS_BOUNDED_TEXT_NATIVE_AND_STATIC_REVIEW",
      "episode_ids": [
        "202003301",
        "202003302"
      ],
      "source_bindings": [
        {
          "episode_id": "202003301",
          "script_id": "scout_091_01_01.json__0ce11fbbdf461338",
          "source_sha256": "9790f6b47007bc0c4768e2d919416c32e5ed77fcf2269fd52a3c5918a04daa14",
          "decoded_sha256": "b253e6485e389f1cd667029247b8eddfaacbe5ee09539543708df63b1812f36a",
          "normalized_sha256": "faf0e245ce5be3c9379931b1c05d0b2669ee7e0958209deb6ab20f17c10afcd8",
          "structured_sha256": "faf0e245ce5be3c9379931b1c05d0b2669ee7e0958209deb6ab20f17c10afcd8",
          "pages": 45,
          "text_records": 42,
          "command_only_pages": 3,
          "voice_pages": 32,
          "native_pages_verified": 45
        },
        {
          "episode_id": "202003302",
          "script_id": "scout_091_01_03.json__57bf6ec7b72c72e3",
          "source_sha256": "b3095699981e88dc83e8a7941f120603bd442afd9770cb3160888722ed3b873e",
          "decoded_sha256": "282886ac8fcb1f415c578fc9b09e523fc9914e7f2f9994a7eb16ad84b53ab60e",
          "normalized_sha256": "a32e9ddeea920d4fa110e3433cc0c7fa2bc891848c0bfbc85ddda163fe79db2f",
          "structured_sha256": "a32e9ddeea920d4fa110e3433cc0c7fa2bc891848c0bfbc85ddda163fe79db2f",
          "pages": 58,
          "text_records": 53,
          "command_only_pages": 5,
          "voice_pages": 47,
          "native_pages_verified": 58
        }
      ],
      "totals": {
        "pages": 103,
        "text_records": 95,
        "command_only_pages": 8,
        "voice_pages": 79,
        "visual_refs": 679
      },
      "voice_count_basis": "Distinct dialogue log-order indexes with voice resource; title-only cues additional; no performed audio reviewed.",
      "native_packet_sha256": "4153e4ff76c42cf6762dc2608c25de56a5b78928b62f2a1ffe5aba6735bdbc56",
      "dialogue_packet_sha256": "3e8728ec297980bcb3fd751a56912bf1d810adfe32da690be2e695ff295f331e",
      "visual_assets": [
        {
          "resource": "adv_chara_149_01_01",
          "body": "adv_chara_149_01.png",
          "body_sha256": "99e954f4fe105fc93364cb6978bfe112dd69fe45e6f2cb11cee62fbf83b00624",
          "face": "adv_chara_149_01_01.png",
          "face_sha256": "bb5b4245ffe5fa87521be9d525e7ea0abbe50b196e62834094f210ce3046e4a5",
          "native_face_offset": [
            79,
            59
          ],
          "output_sha256": "3f0f91931eb0fc25d2f20338942093f17e0a75e0df8b1ab54171209b685eff88"
        },
        {
          "resource": "adv_chara_149_01_02",
          "body": "adv_chara_149_01.png",
          "body_sha256": "99e954f4fe105fc93364cb6978bfe112dd69fe45e6f2cb11cee62fbf83b00624",
          "face": "adv_chara_149_01_02.png",
          "face_sha256": "acd921623382b5c9cf86ee530ed78e9721f52a789288d30af9da7eeee21317d6",
          "native_face_offset": [
            79,
            59
          ],
          "output_sha256": "0fe63728387fac7967c412e5ede5ac4d5df29fca61d6472da7c1744ae3583551"
        },
        {
          "resource": "adv_chara_149_01_03",
          "body": "adv_chara_149_01.png",
          "body_sha256": "99e954f4fe105fc93364cb6978bfe112dd69fe45e6f2cb11cee62fbf83b00624",
          "face": "adv_chara_149_01_03.png",
          "face_sha256": "39a62df2370ea33491d48a23fbb67db4c1dee8624359207a202b938ca26da139",
          "native_face_offset": [
            79,
            59
          ],
          "output_sha256": "703038416a4d8f2b11768850fae9901880f5181252133ddf7e7d099c02a7be36"
        },
        {
          "resource": "adv_chara_149_01_04",
          "body": "adv_chara_149_01.png",
          "body_sha256": "99e954f4fe105fc93364cb6978bfe112dd69fe45e6f2cb11cee62fbf83b00624",
          "face": "adv_chara_149_01_04.png",
          "face_sha256": "89bde1ee7810d2d1788d6cc531b14129304b7420fc4defa1dbb38a81aa5aa880",
          "native_face_offset": [
            79,
            59
          ],
          "output_sha256": "0e33bc4baac5cdfb68cf14d75b052bf5ba02c943202480a7062247ea168f02c1"
        },
        {
          "resource": "adv_chara_002_07_02",
          "body": "adv_chara_002_07.png",
          "body_sha256": "e299b2ccb8f49c9014aa59242afb0c5fb260b54d819620e7d17728597f06c015",
          "face": "adv_chara_002_07_02.png",
          "face_sha256": "36f5de896b1f9324d2693ded5d0b7cf2a39df2520d7c1d0f22c7b80c07c9ba99",
          "native_face_offset": [
            132,
            64
          ],
          "output_sha256": "763b90f28f302abc02baf72d1b434de6a810c051618de5a44f0fc725a68a6274"
        },
        {
          "resource": "adv_chara_004_01_12",
          "body": "adv_chara_004_01.png",
          "body_sha256": "5d8b60092117906b699d98ccabfc88344ea61f82e9b27a23bec1fa15d0cb65be",
          "face": "adv_chara_004_01_12.png",
          "face_sha256": "ccf54121bf174d8bdc145dedb96d53b110cfbb881e5e0a4bd078739cce7f4b2e",
          "native_face_offset": [
            194,
            74
          ],
          "output_sha256": "6d4ebb0aae92d93ecf03f1dc53193e039d8e245a2fade03819d2e16adbb4d526"
        },
        {
          "resource": "adv_obj_0078",
          "body": "adv_obj_0078.png",
          "body_sha256": "c822bc9d28ced7fd5efc82ddf611faaeacdd98383c96882b7bf20821bdf8ed80",
          "output_sha256": "a31482b98b116e233f99cafac8dc41af452b8a22cd720f7af494d3c77c628fdc"
        }
      ],
      "coverage_effective_state_sha256": "40010ae5286d824a10ecb809835ceaa7de178a3d46b0bc0259d5b61d1511cd48",
      "execution_record": "09 Audits and Manifests/T7S_B0100_B0159_EXECUTION_RECORD.md",
      "boundary": "Complete chapter-local text/native state plus selected static review; no authored choice or inline movie; no later-source semantic evidence; performed audio unreviewed."
    },
    "b0103_close_verification": {
      "operation": "T7S_B0103_CLOSE",
      "checked_at": "2026-09-25",
      "status": "PASS_BOUNDED_TEXT_NATIVE_AND_STATIC_REVIEW",
      "episode_ids": [
        "202003401",
        "202003402"
      ],
      "source_bindings": [
        {
          "episode_id": "202003401",
          "script_id": "scout_092_01_01.json__73aec676bb89afce",
          "source_sha256": "4205c56b1f4ca4e7c8188440aa7a530f93f2d1ffefd25de0ef9ec2711665ca38",
          "decoded_sha256": "a674262d4e9ec456bb6e11cdf4d896b797189f07dc942373349073592da78eca",
          "normalized_sha256": "2ec53bf66d3302b26488cf0049ed280b2e050df01c46cc560aa9f92744367023",
          "structured_sha256": "2ec53bf66d3302b26488cf0049ed280b2e050df01c46cc560aa9f92744367023",
          "pages": 58,
          "text_records": 51,
          "command_only_pages": 7,
          "voice_pages": 21,
          "native_pages_verified": 58
        },
        {
          "episode_id": "202003402",
          "script_id": "scout_092_01_03.json__c228b1e149183f9d",
          "source_sha256": "299a3aa3d684c4553f2842418718b8324adf2feeb65378d5d549094f5e7d5fa1",
          "decoded_sha256": "2e885d022f1c37a9ffc1457807ed58d7214160ce96f5cd830f0c95be95aaed56",
          "normalized_sha256": "2064cb47e50d28f74e399b1c3256e5ff1c714ab6ce61df0f8ce11e067cc26ba3",
          "structured_sha256": "2064cb47e50d28f74e399b1c3256e5ff1c714ab6ce61df0f8ce11e067cc26ba3",
          "pages": 72,
          "text_records": 67,
          "command_only_pages": 5,
          "voice_pages": 41,
          "native_pages_verified": 72
        }
      ],
      "totals": {
        "pages": 130,
        "text_records": 118,
        "command_only_pages": 12,
        "voice_pages": 62,
        "visual_refs": 859
      },
      "voice_count_basis": "Distinct dialogue log-order indexes with voice resource; title-only cues additional; no performed audio reviewed.",
      "native_packet_sha256": "b88fba1b9bbaba32ee88e807069c670bdd39c4cbb6bb2dd28bd57ba52ad2a546",
      "dialogue_packet_sha256": "a4228a58d0a3987f73a2211540179d0c0ebcab4171ae2bdf57aad580f6ce9a85",
      "visual_assets": [
        {
          "resource": "adv_chara_145_01_01",
          "body": "adv_chara_145_01.png",
          "body_sha256": "e7e4e7d94dadbb80e074cefd5e23ff1fc6cd5fbe2b6f60c39e6ecab367a58bb2",
          "face": "adv_chara_145_01_01.png",
          "face_sha256": "a8045a092f539cf3ee1987c8dffe76439e50c7c42f382458e945c76fd79decc1",
          "native_face_offset": [
            78,
            63
          ],
          "output_sha256": "ea67105eeee5254b86289fbd17a03cc53cc4e36bd71c0b8ce536893aec1fddcf"
        },
        {
          "resource": "adv_chara_145_01_02",
          "body": "adv_chara_145_01.png",
          "body_sha256": "e7e4e7d94dadbb80e074cefd5e23ff1fc6cd5fbe2b6f60c39e6ecab367a58bb2",
          "face": "adv_chara_145_01_02.png",
          "face_sha256": "4ef3e561795beef0fe996afe979e12e2f638b74317bc24fcd3907c4808bf0b03",
          "native_face_offset": [
            78,
            63
          ],
          "output_sha256": "f2e6379db50f250a7c97442d6a1c396d802b2366dff3af87016ffab5f1b86239"
        },
        {
          "resource": "adv_chara_145_01_03",
          "body": "adv_chara_145_01.png",
          "body_sha256": "e7e4e7d94dadbb80e074cefd5e23ff1fc6cd5fbe2b6f60c39e6ecab367a58bb2",
          "face": "adv_chara_145_01_03.png",
          "face_sha256": "ede176c9694db9d0185ba6b876bb9ce18e45eecf08af097e1f91e0fc95444506",
          "native_face_offset": [
            78,
            63
          ],
          "output_sha256": "250c386302617c55e2909ea3ac9359cfdc855db715dd404c12f6c49a1fe09f0f"
        },
        {
          "resource": "adv_chara_145_01_04",
          "body": "adv_chara_145_01.png",
          "body_sha256": "e7e4e7d94dadbb80e074cefd5e23ff1fc6cd5fbe2b6f60c39e6ecab367a58bb2",
          "face": "adv_chara_145_01_04.png",
          "face_sha256": "c5f3bb014ac84cbde0b7f21531d83425cf1d750b8b42a3b59816c574d03c72b7",
          "native_face_offset": [
            78,
            63
          ],
          "output_sha256": "dfcd78341be78a177f8069e49b9d762eeb2cdfaa6380c22f5edb3d00e7f8be64"
        },
        {
          "resource": "adv_chara_002_04_05",
          "body": "adv_chara_002_04.png",
          "body_sha256": "938fccd1b7bf1b8316a3ebb3c1da299beba659c3e51c5bcbb7abea4c41bb627a",
          "face": "adv_chara_002_04_05.png",
          "face_sha256": "77535cae016ad3013ba64f2189c8a6f49584f928920a5b12c6e3276504ab1ed9",
          "native_face_offset": [
            132,
            64
          ],
          "output_sha256": "ad4d2eca13636dd7d71e0e7bd428e67c3d1653fcf6e8b7312ac2dd3e0a3fc950"
        },
        {
          "resource": "adv_chara_003_01_03",
          "body": "adv_chara_003_01.png",
          "body_sha256": "cfd3a3dd39c6fd67b6ffc63190a2da76e8d1ef5cedcb8eb895afd2a9bd870064",
          "face": "adv_chara_003_01_03.png",
          "face_sha256": "93a9a5a307de8f0bbd274e26dd966320a83ef4b76926376f6747db8801e68482",
          "native_face_offset": [
            98,
            92
          ],
          "output_sha256": "bd1adc2a89fc090c3d171b2bd42b4ced859b152dd582cae30d31fadcbaccd7fb"
        },
        {
          "resource": "adv_chara_133_01_04",
          "body": "adv_chara_133_01.png",
          "body_sha256": "ee3e5303e0e6ee798401ba7e6e276138169525925f4058c03f1d01ddd73fa7e5",
          "face": "adv_chara_133_01_04.png",
          "face_sha256": "ab8241d63657c77008b1e2bc1f25581962a46bff70e9b5223fcce0b6012d4149",
          "native_face_offset": [
            142,
            66
          ],
          "output_sha256": "c7f1894752617462576a0a8c73068e76e132f610b955126fb169b9dd8b492df4"
        },
        {
          "resource": "adv_obj_0027",
          "body": "adv_obj_0027.png",
          "body_sha256": "5f8f7e302456a74fb0b57ecbf770b18515cfba5aabadb7c692f2db788e7ed322",
          "output_sha256": "a2cba3e2732a36e1ef0d6f4c3eee4f4072e570784eadafca4020d1b90da2cb93"
        }
      ],
      "coverage_effective_state_sha256": "137b8d91ed0a6f6a40ee549c43f7c1dbec77a8295f3912dc9286640b8c0ce820",
      "execution_record": "09 Audits and Manifests/T7S_B0100_B0159_EXECUTION_RECORD.md",
      "boundary": "Complete chapter-local text/native state plus selected static review; no authored choice or inline movie; no later-source semantic evidence; performed audio unreviewed."
    },
    "b0104_close_verification": {
      "operation": "T7S_B0104_CLOSE",
      "checked_at": "2026-09-25",
      "status": "PASS_BOUNDED_TEXT_NATIVE_AND_STATIC_REVIEW",
      "episode_ids": [
        "202003501",
        "202003502"
      ],
      "source_bindings": [
        {
          "episode_id": "202003501",
          "script_id": "scout_121_01_01.json__73d48f19cb3dba05",
          "source_sha256": "a7a484095b6b6624f666b89c66a0db9b1ec7c10bbccd3c3e5baf6706ba40cb4f",
          "decoded_sha256": "c3c617ed40a6eed14f8f7c003c578917a02d00fa695793e6a34c5574f32b0528",
          "normalized_sha256": "9418c7b5470a8f7c6c702b850cd1046a8f13805a1db137dddf3ee23bb4065874",
          "structured_sha256": "9418c7b5470a8f7c6c702b850cd1046a8f13805a1db137dddf3ee23bb4065874",
          "pages": 42,
          "text_records": 39,
          "command_only_pages": 3,
          "voice_pages": 29,
          "native_pages_verified": 42
        },
        {
          "episode_id": "202003502",
          "script_id": "scout_121_01_03.json__1efa5946f6e2df85",
          "source_sha256": "a3b9a0faaafc51a55ce6cc6fdbf10d856e1eba476824bc3a0c709e5c7a59b2b9",
          "decoded_sha256": "9c23341ce0603ee571783600abe045a94a6f0bb530101863ad4ba643296644ab",
          "normalized_sha256": "67ac9c59f6fe4d0cb8105b937781bd8c3dbea8734f280f092c9bbf0547c742b5",
          "structured_sha256": "67ac9c59f6fe4d0cb8105b937781bd8c3dbea8734f280f092c9bbf0547c742b5",
          "pages": 69,
          "text_records": 64,
          "command_only_pages": 5,
          "voice_pages": 58,
          "native_pages_verified": 69
        }
      ],
      "totals": {
        "pages": 111,
        "text_records": 103,
        "command_only_pages": 8,
        "voice_pages": 87,
        "visual_refs": 721
      },
      "voice_count_basis": "Distinct dialogue log-order indexes with voice resource; title-only cues additional; no performed audio reviewed.",
      "native_packet_sha256": "70fcb829f6521230aa38c8914119350cc71abb470b592e95f4a54b61eeb2e098",
      "dialogue_packet_sha256": "294eec296198b4fb7db89d9f31d065c5b6bc5be3b15289d414c8ea8a6c2cff3b",
      "visual_assets": [
        {
          "resource": "adv_chara_146_01_01",
          "body": "adv_chara_146_01.png",
          "body_sha256": "46fc3087e9a017bed96eb313d1311e9f939877b7d723a80efa91284489a7c112",
          "face": "adv_chara_146_01_01.png",
          "face_sha256": "801a2257357486bc74f1a57b3b5329afed804e5b0b0c8712d5d4c9ad690505fe",
          "native_face_offset": [
            81,
            44
          ],
          "output_sha256": "d08286dce366a3675dbb094b32d19834b0e32a730faf6930c3e74bae930d9566"
        },
        {
          "resource": "adv_chara_146_01_02",
          "body": "adv_chara_146_01.png",
          "body_sha256": "46fc3087e9a017bed96eb313d1311e9f939877b7d723a80efa91284489a7c112",
          "face": "adv_chara_146_01_02.png",
          "face_sha256": "ecf0b8ba7e74f17b5328b6e93c55795db32d7211eceedefe000b38d61f6e4a5b",
          "native_face_offset": [
            81,
            44
          ],
          "output_sha256": "79551c4a5c3b39299498d0df479567bf99bf0436e1d75180e6aa314488a55a78"
        },
        {
          "resource": "adv_chara_146_01_03",
          "body": "adv_chara_146_01.png",
          "body_sha256": "46fc3087e9a017bed96eb313d1311e9f939877b7d723a80efa91284489a7c112",
          "face": "adv_chara_146_01_03.png",
          "face_sha256": "3895f8ae5772a2e74e9e7c99b85b687b881de0b04d752937bd2533942f472b37",
          "native_face_offset": [
            81,
            44
          ],
          "output_sha256": "90848e3ee257ebdfd45b59a89121e3670941a0fefd909aed189c99c12593e29f"
        },
        {
          "resource": "adv_chara_005_01_09",
          "body": "adv_chara_005_01.png",
          "body_sha256": "5eacc7b48f482d043fd5ebcb64d978a16ea335fd2c83a4b641983d2938444f21",
          "face": "adv_chara_005_01_09.png",
          "face_sha256": "a28832f4321bb584428dadca33a32e415d6ad2721e64734cecd4a1fa86eeebd1",
          "native_face_offset": [
            76,
            85
          ],
          "output_sha256": "405852b697f2f18672b5747a64b646390ee1704db0dd603652a5d0d0a05746cc"
        },
        {
          "resource": "adv_chara_004_01_05",
          "body": "adv_chara_004_01.png",
          "body_sha256": "5d8b60092117906b699d98ccabfc88344ea61f82e9b27a23bec1fa15d0cb65be",
          "face": "adv_chara_004_01_05.png",
          "face_sha256": "d33567411d5de61bb7060fa8c50ed1242c479810eafe455f0a1b8106fd7463a4",
          "native_face_offset": [
            194,
            74
          ],
          "output_sha256": "54e3487d89e826843cfb32c814eb2a27bd91293fcea2d3a2b9393a5dd9f775bd"
        }
      ],
      "coverage_effective_state_sha256": "912ff29e3197594b146f4eaf3a31285d314317a2387b93f99f88cb35850c6cb6",
      "execution_record": "09 Audits and Manifests/T7S_B0100_B0159_EXECUTION_RECORD.md",
      "boundary": "Complete chapter-local text/native state plus selected static review; no authored choice or inline movie; no later-source semantic evidence; performed audio unreviewed."
    },
    "b0105_close_verification": {
      "operation": "T7S_B0105_CLOSE",
      "checked_at": "2026-09-25",
      "status": "PASS_BOUNDED_TEXT_NATIVE_AND_STATIC_REVIEW",
      "episode_ids": [
        "202003601",
        "202003602"
      ],
      "source_bindings": [
        {
          "episode_id": "202003601",
          "script_id": "scout_122_01_01.json__762d610266ff8b28",
          "source_sha256": "52ed04697af7f00507cf09c1993bab8f1d1f08ef65db0f5b29e3b33ba7ccb59c",
          "decoded_sha256": "bb27554edcc61142e1ab8e6b446d59be809f6e50f9eba614c1e10c7df0bb2c64",
          "normalized_sha256": "e5e5d3619c567be7af6c9343df30fb009a85553b0352860fa7c25b39927206ff",
          "structured_sha256": "e5e5d3619c567be7af6c9343df30fb009a85553b0352860fa7c25b39927206ff",
          "pages": 49,
          "text_records": 46,
          "command_only_pages": 3,
          "voice_pages": 46,
          "native_pages_verified": 49
        },
        {
          "episode_id": "202003602",
          "script_id": "scout_122_01_03.json__733d0712033d4864",
          "source_sha256": "a0204aa4924638f46912781041a30075e27057cd189760c567a5b61d4945a0e0",
          "decoded_sha256": "b2c52796886008f653b6d1af550ccd4a1dd46bf61d6d653b83a3bde4b0a6498a",
          "normalized_sha256": "dcb8d27d5becf5a3c6ee8fdbb7ce7f3d0865440a8fe0a721009048f1be8731b7",
          "structured_sha256": "dcb8d27d5becf5a3c6ee8fdbb7ce7f3d0865440a8fe0a721009048f1be8731b7",
          "pages": 54,
          "text_records": 51,
          "command_only_pages": 3,
          "voice_pages": 41,
          "native_pages_verified": 54
        }
      ],
      "totals": {
        "pages": 103,
        "text_records": 97,
        "command_only_pages": 6,
        "voice_pages": 87,
        "visual_refs": 686
      },
      "voice_count_basis": "Distinct dialogue log-order indexes with voice resource; title-only cues additional; no performed audio reviewed.",
      "native_packet_sha256": "43798f075ac4a04b4f5be88c22cba2bada7914f8289ab383783c675afed1b41a",
      "dialogue_packet_sha256": "9e5b2039180dce07df7fa1e4790431cdefa5a294395ecd82b1a0a06d50bd2b9e",
      "visual_assets": [
        {
          "resource": "adv_chara_147_01_01",
          "body": "adv_chara_147_01.png",
          "body_sha256": "df3ba4aa9a0969ae5dbb2f3d8b7e26c938ab1294692d595b12c3090fa8a47982",
          "face": "adv_chara_147_01_01.png",
          "face_sha256": "c97bdaea12f5d9f9bfb81e9ff25f5857cad50a11eb4fa75f0efd392c6f2c6874",
          "native_face_offset": [
            209,
            62
          ],
          "output_sha256": "08c669b14f3c489b3460361737a7d4d1e93fadd065a9f55b874701326f3956de"
        },
        {
          "resource": "adv_chara_147_01_03",
          "body": "adv_chara_147_01.png",
          "body_sha256": "df3ba4aa9a0969ae5dbb2f3d8b7e26c938ab1294692d595b12c3090fa8a47982",
          "face": "adv_chara_147_01_03.png",
          "face_sha256": "b425dcb4e4aa81dee126a29a549706faa3ac8ed578ea2a62d61085fb2d4d42e7",
          "native_face_offset": [
            209,
            62
          ],
          "output_sha256": "ffc811201455c6317889d113ab65a7851d117424772b55baceecc61ffef2c255"
        },
        {
          "resource": "adv_chara_147_01_04",
          "body": "adv_chara_147_01.png",
          "body_sha256": "df3ba4aa9a0969ae5dbb2f3d8b7e26c938ab1294692d595b12c3090fa8a47982",
          "face": "adv_chara_147_01_04.png",
          "face_sha256": "bbbb497cd064596c0e15191fae552209ae3fb9d3fb25e9f38677876ee95dfcbd",
          "native_face_offset": [
            209,
            62
          ],
          "output_sha256": "d59081021329b6f06fd3583c40f5e4ec2e0f0e447708968ec9543615692d5411"
        },
        {
          "resource": "adv_chara_008_01_02",
          "body": "adv_chara_008_01.png",
          "body_sha256": "a72bd127faade4229587eff774c6b319fd99e8221290d4cfbd61769441d8afa4",
          "face": "adv_chara_008_01_02.png",
          "face_sha256": "1f06820770dbdbe057d0c94542c68d0c825df03dc8ae9887ec18a31cb8ab85c0",
          "native_face_offset": [
            166,
            84
          ],
          "output_sha256": "c042e0d18c4dca082a331b7cf20f57a0867e57edfbc9698178628eecf003126d"
        },
        {
          "resource": "adv_obj_0075",
          "body": "adv_obj_0075.png",
          "body_sha256": "dd49de5a45d78f980bec89d8239fef3757617283433f1ceee852b61d73607c9b",
          "output_sha256": "c7397c2ced2075fed5c1b4823ef92bdc9da7612099efedd26dbbdf2227f37bcc"
        },
        {
          "resource": "adv_obj_0076",
          "body": "adv_obj_0076.png",
          "body_sha256": "c70c4345e264bddffca115c312a3b8cf2c52c671ade2cd7a4a2f65f63c05536f",
          "output_sha256": "af83999ceca8970527d738a32dbe0887b4c58bfb2c3be17bdbe7b179f6d9e541"
        },
        {
          "resource": "adv_obj_0077",
          "body": "adv_obj_0077.png",
          "body_sha256": "fc024044b72bf06c43abdc8caf8a7535ad53f670d960dea65a7ad5d56f56787e",
          "output_sha256": "f2f452af304278fc6bbb55182a32f8d4e3f6555f16ebe0af20b7f5a928b04407"
        }
      ],
      "coverage_effective_state_sha256": "5e978302ce4e7f00964f865bfc68965bb4660b58d37d4acacd4e410c28a3b53c",
      "execution_record": "09 Audits and Manifests/T7S_B0100_B0159_EXECUTION_RECORD.md",
      "boundary": "Complete chapter-local text/native state plus selected static review; no authored choice or inline movie; no later-source semantic evidence; performed audio unreviewed."
    },
    "b0106_close_verification": {
      "operation": "T7S_B0106_CLOSE",
      "checked_at": "2026-09-25",
      "status": "PASS_BOUNDED_TEXT_NATIVE_AND_STATIC_REVIEW",
      "episode_ids": [
        "312200101",
        "312200102",
        "312200103"
      ],
      "source_bindings": [
        {
          "episode_id": "312200101",
          "script_id": "ing_102001_01.json__e88d17661720a7ec",
          "source_sha256": "285dcc177b14f73b76fb2d99e8e9533bbb518c4f8ade5a64844c694269ca39b4",
          "decoded_sha256": "1ea5d0dd99d64c9f297c4c5677721844376f66b0a39569752cb059630890ccda",
          "normalized_sha256": "c76ff7312012d666a95368602013b3e26848ad21e4658057d5b1492ac11bfdde",
          "structured_sha256": "c76ff7312012d666a95368602013b3e26848ad21e4658057d5b1492ac11bfdde",
          "pages": 42,
          "text_records": 38,
          "command_only_pages": 4,
          "voice_pages": 33,
          "native_pages_verified": 42
        },
        {
          "episode_id": "312200102",
          "script_id": "ing_102001_02.json__4f48c1bce9742f9e",
          "source_sha256": "2cba36aa2c37ba07051af6113d22f3ed4135ed528e444d6f66378741a938b3f9",
          "decoded_sha256": "d961177eeed185b4216f6fda11f43ae4b6c7bbe31ca2f04dfaea1047c96c2dde",
          "normalized_sha256": "7b6637f72238d013268da1dd69ff7c1a41ac6860845daf7af6e8b8e33c950085",
          "structured_sha256": "7b6637f72238d013268da1dd69ff7c1a41ac6860845daf7af6e8b8e33c950085",
          "pages": 54,
          "text_records": 51,
          "command_only_pages": 3,
          "voice_pages": 33,
          "native_pages_verified": 54
        },
        {
          "episode_id": "312200103",
          "script_id": "ing_102001_03.json__8ce51bbfb37035f3",
          "source_sha256": "d6bb55226057fcac056d4e1e17b7791b2d46a23d9ace9ee5d5f2184466a6cd81",
          "decoded_sha256": "6b07ef4d386a04d01d4a2fc0894ba9a385f07c555e1b06837148ecddeafba693",
          "normalized_sha256": "1824ce329d8a2adbd5570b38a12b72fdbce02fce38159f801a4352d3a379d867",
          "structured_sha256": "1824ce329d8a2adbd5570b38a12b72fdbce02fce38159f801a4352d3a379d867",
          "pages": 78,
          "text_records": 71,
          "command_only_pages": 7,
          "voice_pages": 51,
          "native_pages_verified": 78
        }
      ],
      "totals": {
        "pages": 174,
        "text_records": 160,
        "command_only_pages": 14,
        "voice_pages": 117,
        "visual_refs": 1639
      },
      "voice_count_basis": "Distinct dialogue log-order indexes with voice resource; title-only cues additional; no performed audio reviewed.",
      "native_packet_sha256": "3216cf0aca6efd72487233cfb28341a8e1fd102532d7b9ebefdde1fdbacbe094",
      "dialogue_packet_sha256": "99a74d2d6c765f5113670f83944e63107148b0b89e5547832dc7e9ebfd61c61b",
      "visual_assets": [
        {
          "resource": "adv_chara_003_02_04",
          "body": "adv_chara_003_02.png",
          "body_sha256": "81ca424b3db7ec06f59bdef201d73426c018b984f1b1864b82404efe3b25deb9",
          "face": "adv_chara_003_02_04.png",
          "face_sha256": "f8c2fc7bdcb9d87ff516ef86efbbf63740724fe8ad3c958329540dad27631df6",
          "native_face_offset": [
            98,
            92
          ],
          "output_sha256": "b4bf32d325cb5f15891ebf9214a2fe54cb4313b4039776afcd2c844d161baff6"
        },
        {
          "resource": "adv_chara_013_01_08",
          "body": "adv_chara_013_01.png",
          "body_sha256": "2d4ca61240c61c15796eacab3c3a0ea5cf48f56c8b772d95e1b3ac1be0b7937c",
          "face": "adv_chara_013_01_08.png",
          "face_sha256": "5780dd966218bf492c6754984c5f75c3a0e59a77fd2c00f23e2e295bf432ad9a",
          "native_face_offset": [
            105,
            60
          ],
          "output_sha256": "b8eded5cef4a04c115c9b4db8549e72ce8e657552911bc3bde476f95a7ab6eed"
        },
        {
          "resource": "adv_chara_010_01_08",
          "body": "adv_chara_010_01.png",
          "body_sha256": "ac05f3cd59cf77b2e8a37a23f406bd671a62496ebe681ec9bf0983fc6c843168",
          "face": "adv_chara_010_01_08.png",
          "face_sha256": "8237835e72e154cf9b77a0e2f6fc9e8fcac006f8f8112048f7f8fa06c98167d6",
          "native_face_offset": [
            150,
            104
          ],
          "output_sha256": "c562b2e3fcdb0381eb8ce3530418427fd596f587882de4fe717e9c945d515682"
        },
        {
          "resource": "adv_chara_008_01_05",
          "body": "adv_chara_008_01.png",
          "body_sha256": "a72bd127faade4229587eff774c6b319fd99e8221290d4cfbd61769441d8afa4",
          "face": "adv_chara_008_01_05.png",
          "face_sha256": "54eba0f49d3cf6f60a2ca1898d582deba1878ff4a93d74714d67a645ce138599",
          "native_face_offset": [
            166,
            84
          ],
          "output_sha256": "af57134822fe190980e93a60e5e4579a2dd1e3c68af007fb979943d5e1107a9c"
        },
        {
          "resource": "adv_chara_002_03_01",
          "body": "adv_chara_002_03.png",
          "body_sha256": "4bb14d813389b79055c4a24b5b3020e06bde9122d7b203b04a5489b358a7f1c7",
          "face": "adv_chara_002_03_01.png",
          "face_sha256": "44744b274cd5f728379c329e9a722c0639e1fab23ae5e846a483a3f131e80e14",
          "native_face_offset": [
            132,
            64
          ],
          "output_sha256": "59b13c2655e6f3619ff902a52aac22ff6c10c4c63f17d56ed1b58b339f46165c"
        }
      ],
      "coverage_effective_state_sha256": "9e665ae64441978d20c651b99f353cedd4a5c3533dea1f56c3bfc6f6584f85a6",
      "execution_record": "09 Audits and Manifests/T7S_B0100_B0159_EXECUTION_RECORD.md",
      "boundary": "Complete chapter-local text/native state plus selected static review; no authored choice or inline movie; no later-source semantic evidence; performed audio unreviewed."
    },
    "b0107_close_verification": {
      "operation": "T7S_B0107_CLOSE",
      "checked_at": "2026-09-25",
      "status": "PASS_BOUNDED_TEXT_NATIVE_AND_STATIC_REVIEW",
      "episode_ids": [
        "312200201",
        "312200202",
        "312200203"
      ],
      "source_bindings": [
        {
          "episode_id": "312200201",
          "script_id": "ing_102002_01.json__9e22e1b2840eecec",
          "source_sha256": "101819b461dbfdb14a5a174d89c36aa2ede0a55f726f3f40b67a637ee620c1d0",
          "decoded_sha256": "9602b8c4a132825002bfa339cfbc449ac2b7119726a76dffd35d03c5e0cad9b9",
          "normalized_sha256": "1e6a71454ae1fc6f57c0c88bc1d4e6753f042e832044b5636868f164737d6c4c",
          "structured_sha256": "1e6a71454ae1fc6f57c0c88bc1d4e6753f042e832044b5636868f164737d6c4c",
          "pages": 67,
          "text_records": 61,
          "command_only_pages": 6,
          "voice_pages": 53,
          "native_pages_verified": 67
        },
        {
          "episode_id": "312200202",
          "script_id": "ing_102002_02.json__c768773976f3d960",
          "source_sha256": "a71cefcc195a817a81c48e17259d7655c8483403151f1c409455045a2b2f211c",
          "decoded_sha256": "687f6327e2c9f34805b6280b93a0c3c3dda85329901986132607d67971c0a0cf",
          "normalized_sha256": "69f514013ed6f86c9b80b834ba07539f2cc7ec7e39e35aee9407a615fd14ef63",
          "structured_sha256": "69f514013ed6f86c9b80b834ba07539f2cc7ec7e39e35aee9407a615fd14ef63",
          "pages": 51,
          "text_records": 47,
          "command_only_pages": 4,
          "voice_pages": 32,
          "native_pages_verified": 51
        },
        {
          "episode_id": "312200203",
          "script_id": "ing_102002_03.json__0dba75f141a30695",
          "source_sha256": "dcc5891c0aed6c2e3b93a7351a859e86a9d0c2cd533841e805172d0846865c12",
          "decoded_sha256": "33701be7d63c096947badbc6f1ed1c20b09c42876b2bac4a93a8e7e878081b58",
          "normalized_sha256": "8a77cd3a311bf3c4b03f55d3cb732e12ab5cef27e4eec92af5fc100d2c025ae3",
          "structured_sha256": "8a77cd3a311bf3c4b03f55d3cb732e12ab5cef27e4eec92af5fc100d2c025ae3",
          "pages": 138,
          "text_records": 132,
          "command_only_pages": 6,
          "voice_pages": 65,
          "native_pages_verified": 138
        }
      ],
      "totals": {
        "pages": 256,
        "text_records": 240,
        "command_only_pages": 16,
        "voice_pages": 150,
        "visual_refs": 1680
      },
      "voice_count_basis": "Distinct dialogue log-order indexes with voice resource; title-only cues additional; no performed audio reviewed.",
      "native_packet_sha256": "8516f490293fc25e27ca779040baa99f6d75b48f06289788fbc3b93bcf155ee7",
      "dialogue_packet_sha256": "91eb924ff0f1337115179bdf007647cd39418945cf0c5a794ad803c1c44992b7",
      "visual_assets": [
        {
          "resource": "adv_chara_004_01_01",
          "body": "adv_chara_004_01.png",
          "body_sha256": "5d8b60092117906b699d98ccabfc88344ea61f82e9b27a23bec1fa15d0cb65be",
          "face": "adv_chara_004_01_01.png",
          "face_sha256": "95e34c62c3396b29b6716cf56c2dabd1af0752f0bb56e1f1a9735860ca0dac2c",
          "native_face_offset": [
            194,
            74
          ],
          "output_sha256": "d21f450fd21f3b0278a6a4d2d0bc099bb9cc7877d04a0c56bae2a56868935f88"
        },
        {
          "resource": "adv_chara_004_05_22",
          "body": "adv_chara_004_05.png",
          "body_sha256": "651d7a22320e425a802532660fdb19a88dedeeba590c6fc79da73b1429ef8f8a",
          "face": "adv_chara_004_05_22.png",
          "face_sha256": "00d4e79ddbac61a10eb36c72f9b6cb453576cc178f21d9ada8118317f089c6a8",
          "native_face_offset": [
            194,
            74
          ],
          "output_sha256": "69de86c5cbedfb272b8dc90ad8fd4ca9ebbc904764342d196b91a1c7f94684ec"
        },
        {
          "resource": "adv_chara_004_06_05",
          "body": "adv_chara_004_06.png",
          "body_sha256": "2fa07637cb12479aa6a36a4d33fcda9dadc4f265786390ccbfdae5beb4279b75",
          "face": "adv_chara_004_06_05.png",
          "face_sha256": "101a944dfd3f8fdb0d9ba72b33069059e70dbeef9ba3e7576621ac8567ff600c",
          "native_face_offset": [
            194,
            74
          ],
          "output_sha256": "1d21c4322c40f7f8047c4f32c130a16feed0a0751c4757520dcde3b8dcbc5653"
        },
        {
          "resource": "adv_chara_004_06_09",
          "body": "adv_chara_004_06.png",
          "body_sha256": "2fa07637cb12479aa6a36a4d33fcda9dadc4f265786390ccbfdae5beb4279b75",
          "face": "adv_chara_004_06_09.png",
          "face_sha256": "7587eb1019d9dc95d4015c527ccd3322bbbda326f67cb224f5afea097d136b18",
          "native_face_offset": [
            194,
            74
          ],
          "output_sha256": "2d9984d55e5991fb2594902ae09e06963bd94982f8089525835934d86604e2db"
        },
        {
          "resource": "adv_chara_005_01_04",
          "body": "adv_chara_005_01.png",
          "body_sha256": "5eacc7b48f482d043fd5ebcb64d978a16ea335fd2c83a4b641983d2938444f21",
          "face": "adv_chara_005_01_04.png",
          "face_sha256": "ad98aa82a2fae4dfb7e1788688004d0549b3b52c86f26608b9b85e89998cca88",
          "native_face_offset": [
            76,
            85
          ],
          "output_sha256": "9335b3959b31b6bb77cbb834d0151071dd8ccecd28dbee2097aecb73087f68cd"
        },
        {
          "resource": "adv_chara_008_01_11",
          "body": "adv_chara_008_01.png",
          "body_sha256": "a72bd127faade4229587eff774c6b319fd99e8221290d4cfbd61769441d8afa4",
          "face": "adv_chara_008_01_11.png",
          "face_sha256": "90bd4ef9754ef0bb4feb08a9f247f3f14eae229693e43ad72d542ec37440898f",
          "native_face_offset": [
            166,
            84
          ],
          "output_sha256": "e7f53af41f122b88fdce7e49f85229221a9d923457a9907d0681530eceb070e6"
        },
        {
          "resource": "adv_chara_002_07_02",
          "body": "adv_chara_002_07.png",
          "body_sha256": "e299b2ccb8f49c9014aa59242afb0c5fb260b54d819620e7d17728597f06c015",
          "face": "adv_chara_002_07_02.png",
          "face_sha256": "36f5de896b1f9324d2693ded5d0b7cf2a39df2520d7c1d0f22c7b80c07c9ba99",
          "native_face_offset": [
            132,
            64
          ],
          "output_sha256": "763b90f28f302abc02baf72d1b434de6a810c051618de5a44f0fc725a68a6274"
        }
      ],
      "coverage_effective_state_sha256": "69c9b36624375711e28908b55a1648593293b0b0d3fb98217893fbfa072133c4",
      "execution_record": "09 Audits and Manifests/T7S_B0100_B0159_EXECUTION_RECORD.md",
      "boundary": "Complete chapter-local text/native state plus selected static review; no authored choice or inline movie; no later-source semantic evidence; performed audio unreviewed."
    },
    "b0108_close_verification": {
      "operation": "T7S_B0108_CLOSE",
      "checked_at": "2026-09-26",
      "status": "PASS_BOUNDED_TEXT_NATIVE_AND_STATIC_REVIEW",
      "episode_ids": [
        "312200301",
        "312200302",
        "312200303"
      ],
      "source_bindings": [
        {
          "episode_id": "312200301",
          "script_id": "ing_102003_01.json__4c864df5f4550bc3",
          "source_sha256": "3f1ddadeaab2f73b58e238332109015baf7a3029e2e4dff8f0025056f44637e4",
          "decoded_sha256": "dd9b0d12b6dce74f7d2ade7324f70cb67d09652e68d7d03f5c8bc49c790b2779",
          "normalized_sha256": "3ec35b955097400d04cd9b1432825a948f9a7dc3ff775d27a86043e9a8c85d62",
          "structured_sha256": "3ec35b955097400d04cd9b1432825a948f9a7dc3ff775d27a86043e9a8c85d62",
          "pages": 62,
          "text_records": 53,
          "command_only_pages": 9,
          "voice_pages": 43,
          "native_pages_verified": 62
        },
        {
          "episode_id": "312200302",
          "script_id": "ing_102003_02.json__c8650ab62e623abd",
          "source_sha256": "f11eef96469cd6c43eacc3d3e07c7242e1072702cbdfef65d857fb7e2212aa80",
          "decoded_sha256": "50093fb6d455ddaf0d8220788367d8e092d95d59c034e04ca7d2733169588b09",
          "normalized_sha256": "7c42a2a64f7d24c2383649eab932b3c9204425a950326b507fe0bf3d0e31d04c",
          "structured_sha256": "7c42a2a64f7d24c2383649eab932b3c9204425a950326b507fe0bf3d0e31d04c",
          "pages": 65,
          "text_records": 61,
          "command_only_pages": 4,
          "voice_pages": 45,
          "native_pages_verified": 65
        },
        {
          "episode_id": "312200303",
          "script_id": "ing_102003_03.json__99725c66af249e2b",
          "source_sha256": "fd15f48a0bf020f69f3c6e1476b8371c12f303da76ecd3d953ba1a9056b00976",
          "decoded_sha256": "3ea200480a045c22a31de70b62a0ef74604ed41ea8068a143c55ae2d8b5bdc53",
          "normalized_sha256": "52379646863192fbc82168ae6ef8c2814a65b1929527afa69d16544605bac00d",
          "structured_sha256": "52379646863192fbc82168ae6ef8c2814a65b1929527afa69d16544605bac00d",
          "pages": 81,
          "text_records": 69,
          "command_only_pages": 12,
          "voice_pages": 55,
          "native_pages_verified": 81
        }
      ],
      "totals": {
        "pages": 208,
        "text_records": 183,
        "command_only_pages": 25,
        "voice_pages": 143,
        "visual_refs": 1828
      },
      "voice_count_basis": "Distinct dialogue log-order indexes with voice resource; title-only cues additional; no performed audio reviewed.",
      "native_packet_sha256": "7dd9cedbe61aa4638fa7d3b56caad4ce099d09345b28e8a4ab68231084733889",
      "dialogue_packet_sha256": "aedd9479b925b9f63ff6467c62cc8b9346b5e1e7ff3873b5d00e7ce65ee2b7fa",
      "visual_assets": [
        {
          "resource": "adv_chara_005_01_09",
          "body": "adv_chara_005_01.png",
          "body_sha256": "5eacc7b48f482d043fd5ebcb64d978a16ea335fd2c83a4b641983d2938444f21",
          "face": "adv_chara_005_01_09.png",
          "face_sha256": "a28832f4321bb584428dadca33a32e415d6ad2721e64734cecd4a1fa86eeebd1",
          "native_face_offset": [
            76,
            85
          ],
          "output_sha256": "405852b697f2f18672b5747a64b646390ee1704db0dd603652a5d0d0a05746cc"
        },
        {
          "resource": "adv_chara_005_08_10",
          "body": "adv_chara_005_08.png",
          "body_sha256": "600d38a8971d9c8bb0501dde8f3ce4baa8aa9e94d39e578b269ed098ffb4140c",
          "face": "adv_chara_005_08_10.png",
          "face_sha256": "2c2043e30bf71bf60c881c9537a3f728313cf6d2441105a283c932f1c952bc75",
          "native_face_offset": [
            76,
            85
          ],
          "output_sha256": "6f92ad55e95ef4eb18c453a5cc1bfc463a0a5c31c127168abf9da85016554980"
        },
        {
          "resource": "adv_chara_005_03_02",
          "body": "adv_chara_005_03.png",
          "body_sha256": "a11dbcc15b03d77cbb5b2b0a5314ad7cccd010be2a7de17b3fbfe75dad4cdc1c",
          "face": "adv_chara_005_03_02.png",
          "face_sha256": "3e6b7c600977a4ca24cdf5b5b61de4c194e4989838de964780dc58b478ac3227",
          "native_face_offset": [
            113,
            61
          ],
          "output_sha256": "12a1493425931580d2f37476b9ad9d1f31ab6ad2f347c18ea1f434992dfa30b0"
        },
        {
          "resource": "adv_chara_002_03_14",
          "body": "adv_chara_002_03.png",
          "body_sha256": "4bb14d813389b79055c4a24b5b3020e06bde9122d7b203b04a5489b358a7f1c7",
          "face": "adv_chara_002_03_14.png",
          "face_sha256": "cfeadce6fac9eacfd77d935a20c2a5c5a89bfc009a3d640c55638578ceabf5e0",
          "native_face_offset": [
            132,
            64
          ],
          "output_sha256": "94354a5b2d3d120baf13f35127f2821d423ce2f8744732ade9df178ecc7ecda5"
        },
        {
          "resource": "adv_chara_003_06_05",
          "body": "adv_chara_003_06.png",
          "body_sha256": "a41fb44cc61027bc6f9f0a44fe7ff477be4bd04e6e671c3d77d6efbfdf7fc55e",
          "face": "adv_chara_003_06_05.png",
          "face_sha256": "bf22ef028c42ed207e7d2d4243113aca2286050bcf6c25f3d68074505cd88ebb",
          "native_face_offset": [
            98,
            92
          ],
          "output_sha256": "dc88ab73b874767a74542663ca12abca8ca2dc398cbed1f15dff7b7a1a4eba70"
        },
        {
          "resource": "adv_chara_004_04_01",
          "body": "adv_chara_004_04.png",
          "body_sha256": "8e2b351704a00f1fba0d55a2074251c17db34706506673c978aa87c8c22de7ae",
          "face": "adv_chara_004_04_01.png",
          "face_sha256": "adb48af4e82001808a861d3e912e3e9c78b75f3b576060877ee10731b94e6521",
          "native_face_offset": [
            194,
            74
          ],
          "output_sha256": "e792a837770a0a8802ece7cce39833f7a5cf969bb12012a3246fd0c9a0c431c0"
        },
        {
          "resource": "adv_obj_0014",
          "body": "adv_obj_0014.png",
          "body_sha256": "0ca76a3d2adfdb7a899dc828a583132f6461e99e424aadf1f4fb364925f4704e",
          "output_sha256": "6964bceef80a9d47be5c5fdb22998ca7b5f00aa1c70041042ffb7ca047dea565"
        }
      ],
      "coverage_effective_state_sha256": "77068d1eeb0b37184509d42494db30438f0296bdd2a3e4ba3c823e947aca87dc",
      "execution_record": "09 Audits and Manifests/T7S_B0100_B0159_EXECUTION_RECORD.md",
      "boundary": "Complete chapter-local text/native state plus selected static review; no authored choice or inline movie; no later-source semantic evidence; performed audio unreviewed."
    },
    "b0109_close_verification": {
      "operation": "T7S_B0109_CLOSE",
      "checked_at": "2026-09-26",
      "status": "PASS_BOUNDED_TEXT_NATIVE_AND_STATIC_REVIEW",
      "episode_ids": [
        "312200401",
        "312200402",
        "312200403"
      ],
      "source_bindings": [
        {
          "episode_id": "312200401",
          "script_id": "ing_102004_01.json__add42eb31242af87",
          "source_sha256": "8b15081f7bea268d56f49fba5cfaf70197937e4f90c482175a62f9995eee88b1",
          "decoded_sha256": "af8e17376eba109c914f448661ab3d66f52da64a7da52bc7001e986c6a65997b",
          "normalized_sha256": "17c36aaf805a3ad40994286f9887e003db62d14aab026dc46fa589d2be4db189",
          "structured_sha256": "17c36aaf805a3ad40994286f9887e003db62d14aab026dc46fa589d2be4db189",
          "pages": 55,
          "text_records": 50,
          "command_only_pages": 5,
          "voice_pages": 46,
          "native_pages_verified": 55
        },
        {
          "episode_id": "312200402",
          "script_id": "ing_102004_02.json__0ed3607d15105c24",
          "source_sha256": "9d86f5298bb6a3050ff04c2397256daa41a7463a9da172097770e4ed035d2ac2",
          "decoded_sha256": "7bdda7bbc576a7fd9ee84220999c5baad2acf9aba8aac1faad2440866962d705",
          "normalized_sha256": "90fa6ecbfc6b4487cefb9816384efd6b0896a1e2292e5ec056eb998f29dab498",
          "structured_sha256": "90fa6ecbfc6b4487cefb9816384efd6b0896a1e2292e5ec056eb998f29dab498",
          "pages": 38,
          "text_records": 31,
          "command_only_pages": 7,
          "voice_pages": 20,
          "native_pages_verified": 38
        },
        {
          "episode_id": "312200403",
          "script_id": "ing_102004_03.json__23e1c3cef3b2e3e3",
          "source_sha256": "d6b17f1cb1ae2cfb1222b7a1ff50638430df5a9945a575079d275466ea8a8e64",
          "decoded_sha256": "b9d4210fd7a8105798f04e91b777538de9a7e88cdb9b10fcd9a87d0ba55e27be",
          "normalized_sha256": "786c427948556f4a965a9761b57591a787823ea4cd4de2c8a2b019156b6e8316",
          "structured_sha256": "786c427948556f4a965a9761b57591a787823ea4cd4de2c8a2b019156b6e8316",
          "pages": 81,
          "text_records": 74,
          "command_only_pages": 7,
          "voice_pages": 67,
          "native_pages_verified": 81
        }
      ],
      "totals": {
        "pages": 174,
        "text_records": 155,
        "command_only_pages": 19,
        "voice_pages": 133,
        "visual_refs": 1057
      },
      "voice_count_basis": "Distinct dialogue log-order indexes with voice resource; title-only cues additional; no performed audio reviewed.",
      "native_packet_sha256": "e57231d71fd033b97d935bf06cd532fc3696c61888aaf741e6a3bb72b645a76d",
      "dialogue_packet_sha256": "1672c7cc3c643c16f5f98a340a5f9000c7e3ba3574fcaa8e3efe67dda1f4bbba",
      "visual_assets": [
        {
          "resource": "adv_chara_006_01_09",
          "body": "adv_chara_006_01.png",
          "body_sha256": "d40ded643748164bb05d319c4a3889a41f99d102a3fcfeb60675b59529a6c392",
          "face": "adv_chara_006_01_09.png",
          "face_sha256": "c148998468216435d916810a8bb31c33cd9c4236a5b85daed64ec2d01d1c617a",
          "native_face_offset": [
            134,
            91
          ],
          "output_sha256": "6fd10baf9d8396e6126e722d8fb31f63c8fa00a5c1b46ba224f484f496e5b6b4"
        },
        {
          "resource": "adv_chara_006_05_11",
          "body": "adv_chara_006_05.png",
          "body_sha256": "1a89f978482f6bb81f66cc1fb9bee3f0b1822858566a023e836f8fb598bd9f0a",
          "face": "adv_chara_006_05_11.png",
          "face_sha256": "747214e58d7fd8e179e66029965004316f3c85f89ef7bbd39e6d2f4a5dabcc2c",
          "native_face_offset": [
            134,
            91
          ],
          "output_sha256": "b068850471ce3122174e02a8dac55b1b8d1dcf42ea207cc2c872797e26442747"
        },
        {
          "resource": "adv_chara_005_01_10",
          "body": "adv_chara_005_01.png",
          "body_sha256": "5eacc7b48f482d043fd5ebcb64d978a16ea335fd2c83a4b641983d2938444f21",
          "face": "adv_chara_005_01_10.png",
          "face_sha256": "f5b35d9a9ddd49c33a5b264ea4ea612397791ef61f6156c3f460c55409c7477a",
          "native_face_offset": [
            76,
            85
          ],
          "output_sha256": "4544d58dc737b4cba221346b12cbca2d6fdbfa7457e9772d79c553db8957f250"
        },
        {
          "resource": "adv_chara_009_03_08",
          "body": "adv_chara_009_03.png",
          "body_sha256": "ffc2406a944338eecacf731a83cc2ecfedce4b3e932bcbf3574528e5939035c8",
          "face": "adv_chara_009_03_08.png",
          "face_sha256": "8a13ebaaa2668320fe1b74b08dd12f0a0f634193489ac59d7c548d83a92e2583",
          "native_face_offset": [
            109,
            85
          ],
          "output_sha256": "8c7b1afb15f3d22f02dd29fa7af1465890e47772e40a221ff6abc263180f11ab"
        },
        {
          "resource": "adv_chara_007_02_07",
          "body": "adv_chara_007_02.png",
          "body_sha256": "92aaed359500dd8fd52b4cecb0a7e1f60b0e63e466320ae2036086461c29edc1",
          "face": "adv_chara_007_02_07.png",
          "face_sha256": "d7201dfba64c1e66436917c45a7fc485d0de53582944daf0b3e2aa373f004fcc",
          "native_face_offset": [
            84,
            80
          ],
          "output_sha256": "3deeabcc8478b56cb32a503cdd952572eb87b07ee6856fdb8af39b9f7aad9c76"
        },
        {
          "resource": "adv_obj_0107",
          "body": "adv_obj_0107.png",
          "body_sha256": "85aa38482d18aeaeb84a6e561dd293bf65097cc5c14f6701a6471d3cd830f3d7",
          "output_sha256": "40d9d0194ad7d8d3c6491ccb9527ee2eff8e287218a0820c8b64bdf7b1dd0e01"
        },
        {
          "resource": "adv_obj_0108",
          "body": "adv_obj_0108.png",
          "body_sha256": "ea2199216f1414be91d4412b4cc28aa6fa33f9e2118f82b9dd0cedc574a0bd6d",
          "output_sha256": "60793441159a5edc71dfee4e18c589813915d729255f9fb8e4eac5830833bb7b"
        }
      ],
      "coverage_effective_state_sha256": "77af28b7cc3f60b2c53fe46e4e47d8356250c6dff4849348d5de66ddd7ca7772",
      "execution_record": "09 Audits and Manifests/T7S_B0100_B0159_EXECUTION_RECORD.md",
      "boundary": "Complete chapter-local text/native state plus selected static review; no authored choice or inline movie; no later-source semantic evidence; performed audio unreviewed."
    },
    "b0110_close_verification": {
      "operation": "T7S_B0110_CLOSE",
      "checked_at": "2026-09-26",
      "status": "PASS_BOUNDED_TEXT_NATIVE_AND_STATIC_REVIEW",
      "episode_ids": [
        "312200501",
        "312200502",
        "312200503"
      ],
      "source_bindings": [
        {
          "episode_id": "312200501",
          "script_id": "ing_102005_01.json__1b971e66e111c22e",
          "source_sha256": "d93d781ae9ef7731224b76a19dd8e2b8a26156cf103d81d465d84d23c76189eb",
          "decoded_sha256": "d4d3a3243a2cc0a2c1747081252a6b1840e41ba728567afded915953dd1f0205",
          "normalized_sha256": "25fc84770f8d5d23216beb6b780fbb03b537d0b0f668112e6a6b6750597928e1",
          "structured_sha256": "25fc84770f8d5d23216beb6b780fbb03b537d0b0f668112e6a6b6750597928e1",
          "pages": 59,
          "text_records": 53,
          "command_only_pages": 6,
          "voice_pages": 35,
          "native_pages_verified": 59
        },
        {
          "episode_id": "312200502",
          "script_id": "ing_102005_02.json__bb95a4bec962cfb0",
          "source_sha256": "462549421373f2b3b8365e116dab179c4e89f8bf9d2f9adcd2379fffbb119e9d",
          "decoded_sha256": "2ec9044a44d2004390750895b16691e52da671aedfeb7cfb85327f8d7458bbd4",
          "normalized_sha256": "53036c2220519841d1fa78cd650dfa8c856f97e8002a9a39f956d56b5c7304a3",
          "structured_sha256": "53036c2220519841d1fa78cd650dfa8c856f97e8002a9a39f956d56b5c7304a3",
          "pages": 47,
          "text_records": 42,
          "command_only_pages": 5,
          "voice_pages": 33,
          "native_pages_verified": 47
        },
        {
          "episode_id": "312200503",
          "script_id": "ing_102005_03.json__5e0031bd3180189e",
          "source_sha256": "88c272c2d5177d61143ef945b32056324649d4bbdd4a5234d4b9ea975edaec87",
          "decoded_sha256": "a6a505acc2b6c955830a354cc26140034b360a87b579b9e4a6dbbaeff33daea2",
          "normalized_sha256": "102506ea264d7b65b7ec578b58f6ea07c331200a791cc4d36ef6097b47da254e",
          "structured_sha256": "102506ea264d7b65b7ec578b58f6ea07c331200a791cc4d36ef6097b47da254e",
          "pages": 28,
          "text_records": 24,
          "command_only_pages": 4,
          "voice_pages": 17,
          "native_pages_verified": 28
        }
      ],
      "totals": {
        "pages": 134,
        "text_records": 119,
        "command_only_pages": 15,
        "voice_pages": 85,
        "visual_refs": 868
      },
      "voice_count_basis": "Distinct dialogue log-order indexes with voice resource; title-only cues additional; no performed audio reviewed.",
      "native_packet_sha256": "cdcc6d62867db90b34118eb0f385556229e297f3d6d3f35f476426a5946ce356",
      "dialogue_packet_sha256": "fd7b5cd9f01d2ae6d65047ab97a1dfb12daa5b20b74030f69038fe5d877dbde8",
      "visual_assets": [
        {
          "resource": "adv_chara_007_01_01",
          "body": "adv_chara_007_01.png",
          "body_sha256": "1bf0de43c70899cafbf9ae8fedfba9663293ade0a774d004e620c158af87ccf0",
          "face": "adv_chara_007_01_01.png",
          "face_sha256": "cbbc596096c690e698bca606f704579f2bf8ad84a9a2ab336891c2b66c54c9f9",
          "native_face_offset": [
            84,
            80
          ],
          "output_sha256": "b221806b4688af7613b359a7957cb939c4fa6df4327677023bcb8196f7731a55"
        },
        {
          "resource": "adv_chara_007_02_06",
          "body": "adv_chara_007_02.png",
          "body_sha256": "92aaed359500dd8fd52b4cecb0a7e1f60b0e63e466320ae2036086461c29edc1",
          "face": "adv_chara_007_02_06.png",
          "face_sha256": "3715729e4ecb1bba784cfc512b794e5a40d4391022410eee407b6268d1677301",
          "native_face_offset": [
            84,
            80
          ],
          "output_sha256": "e9d8a7493853644efd68ae0ce213546659fa74473afb1c77ae60bf6357248085"
        },
        {
          "resource": "adv_chara_007_02_04",
          "body": "adv_chara_007_02.png",
          "body_sha256": "92aaed359500dd8fd52b4cecb0a7e1f60b0e63e466320ae2036086461c29edc1",
          "face": "adv_chara_007_02_04.png",
          "face_sha256": "fb89b901b0e8076d950a9e3476f1b0698f5f1a7b538fa933ee49069598bd3eba",
          "native_face_offset": [
            84,
            80
          ],
          "output_sha256": "6d4b2b3c825752d1c692fa38042b05c78c3e785bc504ce9c682c5257778b8bc4"
        },
        {
          "resource": "adv_chara_004_01_06",
          "body": "adv_chara_004_01.png",
          "body_sha256": "5d8b60092117906b699d98ccabfc88344ea61f82e9b27a23bec1fa15d0cb65be",
          "face": "adv_chara_004_01_06.png",
          "face_sha256": "2ed7745b3f1906230a645b992a93e8259f8fd0466efab7fe91237c02d74440e7",
          "native_face_offset": [
            194,
            74
          ],
          "output_sha256": "768a21438bdc393bae3afad31a52cb7669988a04282251c52576a5353b7de373"
        },
        {
          "resource": "adv_chara_003_02_03",
          "body": "adv_chara_003_02.png",
          "body_sha256": "81ca424b3db7ec06f59bdef201d73426c018b984f1b1864b82404efe3b25deb9",
          "face": "adv_chara_003_02_03.png",
          "face_sha256": "1045b2d405e6f8885e97bc62bf2a34c0cd565ef0fd73726a2585cc52e8eca16b",
          "native_face_offset": [
            98,
            92
          ],
          "output_sha256": "a78e5fb090df397f20f5bc1b40fcf7768210283c8e967a0ea14fce37cfc69ed3"
        },
        {
          "resource": "adv_chara_005_01_04",
          "body": "adv_chara_005_01.png",
          "body_sha256": "5eacc7b48f482d043fd5ebcb64d978a16ea335fd2c83a4b641983d2938444f21",
          "face": "adv_chara_005_01_04.png",
          "face_sha256": "ad98aa82a2fae4dfb7e1788688004d0549b3b52c86f26608b9b85e89998cca88",
          "native_face_offset": [
            76,
            85
          ],
          "output_sha256": "9335b3959b31b6bb77cbb834d0151071dd8ccecd28dbee2097aecb73087f68cd"
        }
      ],
      "coverage_effective_state_sha256": "b3cbfbb54e366b46874cc83941fb288252d21b0e63a786cd889150c3620e36ad",
      "execution_record": "09 Audits and Manifests/T7S_B0100_B0159_EXECUTION_RECORD.md",
      "boundary": "Complete chapter-local text/native state plus selected static review; no authored choice or inline movie; no later-source semantic evidence; performed audio unreviewed."
    },
    "b0111_close_verification": {
      "operation": "T7S_B0111_CLOSE",
      "checked_at": "2026-09-26",
      "status": "PASS_BOUNDED_TEXT_NATIVE_AND_STATIC_REVIEW",
      "episode_ids": [
        "312200601",
        "312200602",
        "312200603"
      ],
      "source_bindings": [
        {
          "episode_id": "312200601",
          "script_id": "ing_102006_01.json__3ad223e841f150fa",
          "source_sha256": "8ea61ed2924e153409f5288aece81df07f2858ee80c9ac8222cca5f9a80cef3d",
          "decoded_sha256": "0d15d7cfbea8d913de58c5fb6144e70d68b9dbc16699aeff7242cabff12e2301",
          "normalized_sha256": "10b2bec2790f341b9cffd731b5829b23d79993d88a006f7e4aaa1ec527de2ede",
          "structured_sha256": "10b2bec2790f341b9cffd731b5829b23d79993d88a006f7e4aaa1ec527de2ede",
          "pages": 52,
          "text_records": 48,
          "command_only_pages": 4,
          "voice_pages": 40,
          "native_pages_verified": 52
        },
        {
          "episode_id": "312200602",
          "script_id": "ing_102006_02.json__a3a6d9fcf2c88fc4",
          "source_sha256": "055f6021ef532a6c5c166af91569343f8610fe29e1a6493989757eebfd498589",
          "decoded_sha256": "7647ed34ff57dcad23d819894d6b81b01ba69dcc432a0035f416834b09f76d8d",
          "normalized_sha256": "f778c05950ee76120b6dd61bc7a560ca8ff06e7780fcf548c504eea7be8470a2",
          "structured_sha256": "f778c05950ee76120b6dd61bc7a560ca8ff06e7780fcf548c504eea7be8470a2",
          "pages": 40,
          "text_records": 38,
          "command_only_pages": 2,
          "voice_pages": 29,
          "native_pages_verified": 40
        },
        {
          "episode_id": "312200603",
          "script_id": "ing_102006_03.json__2b2b92ee6a8c3535",
          "source_sha256": "e0e6281fead0f8690444384338bc84dcbedfea4f7dca21d2daed276b9c006189",
          "decoded_sha256": "54a17f9aeeec518177ff6a8ae2db916dd8f0f01f5703ae6945c37dfb9f52595a",
          "normalized_sha256": "130937355405c3e67975d34f33ad45b929703c1eee321f024d9ed398c3e1438c",
          "structured_sha256": "130937355405c3e67975d34f33ad45b929703c1eee321f024d9ed398c3e1438c",
          "pages": 104,
          "text_records": 92,
          "command_only_pages": 12,
          "voice_pages": 78,
          "native_pages_verified": 104
        }
      ],
      "totals": {
        "pages": 196,
        "text_records": 178,
        "command_only_pages": 18,
        "voice_pages": 147,
        "visual_refs": 1897
      },
      "voice_count_basis": "Distinct dialogue log-order indexes with voice resource; title-only cues additional; no performed audio reviewed.",
      "native_packet_sha256": "fd760be9870c78eaca3ad6e1ebc27ec7ae0cee1ed5d77b0847373d0fa2e2e0cc",
      "dialogue_packet_sha256": "6bee432fc43aab6e527e448403f6f23db53d0fec96c4bd280969edaec3e810d1",
      "visual_assets": [
        {
          "resource": "adv_chara_008_01_01",
          "body": "adv_chara_008_01.png",
          "body_sha256": "a72bd127faade4229587eff774c6b319fd99e8221290d4cfbd61769441d8afa4",
          "face": "adv_chara_008_01_01.png",
          "face_sha256": "6cde466239545bdd5ef7cf3a50542c810e853eb59f7519d9d476f4bd59f0e0a0",
          "native_face_offset": [
            166,
            84
          ],
          "output_sha256": "5da4d642d552e04c85241ddb25ebfa6707dabb3e06e17c22083e7151dfc9e16b"
        },
        {
          "resource": "adv_chara_008_01_06",
          "body": "adv_chara_008_01.png",
          "body_sha256": "a72bd127faade4229587eff774c6b319fd99e8221290d4cfbd61769441d8afa4",
          "face": "adv_chara_008_01_06.png",
          "face_sha256": "26ec902c22f1897ea8b85d86688b1ea0e7a106ee69ea32c9bb9fd24d06243540",
          "native_face_offset": [
            166,
            84
          ],
          "output_sha256": "6053156e36e572edc1d740f4ef998c5fd65da86841fb8d4373e1f40922976aca"
        },
        {
          "resource": "adv_chara_008_01_11",
          "body": "adv_chara_008_01.png",
          "body_sha256": "a72bd127faade4229587eff774c6b319fd99e8221290d4cfbd61769441d8afa4",
          "face": "adv_chara_008_01_11.png",
          "face_sha256": "90bd4ef9754ef0bb4feb08a9f247f3f14eae229693e43ad72d542ec37440898f",
          "native_face_offset": [
            166,
            84
          ],
          "output_sha256": "e7f53af41f122b88fdce7e49f85229221a9d923457a9907d0681530eceb070e6"
        },
        {
          "resource": "adv_chara_008_01_03",
          "body": "adv_chara_008_01.png",
          "body_sha256": "a72bd127faade4229587eff774c6b319fd99e8221290d4cfbd61769441d8afa4",
          "face": "adv_chara_008_01_03.png",
          "face_sha256": "4ef21b05b42aa3e64dd5741c2d3f06e773733eeddbb71cdc98a56be3d22e0127",
          "native_face_offset": [
            166,
            84
          ],
          "output_sha256": "53c41138168f8a5b7337d8aa92b9ece2bd86df0181e0c5430475cb57c6f635a7"
        },
        {
          "resource": "adv_chara_003_02_04",
          "body": "adv_chara_003_02.png",
          "body_sha256": "81ca424b3db7ec06f59bdef201d73426c018b984f1b1864b82404efe3b25deb9",
          "face": "adv_chara_003_02_04.png",
          "face_sha256": "f8c2fc7bdcb9d87ff516ef86efbbf63740724fe8ad3c958329540dad27631df6",
          "native_face_offset": [
            98,
            92
          ],
          "output_sha256": "b4bf32d325cb5f15891ebf9214a2fe54cb4313b4039776afcd2c844d161baff6"
        },
        {
          "resource": "adv_chara_009_03_01",
          "body": "adv_chara_009_03.png",
          "body_sha256": "ffc2406a944338eecacf731a83cc2ecfedce4b3e932bcbf3574528e5939035c8",
          "face": "adv_chara_009_03_01.png",
          "face_sha256": "3930e1f45971c7020b6faf9806089ec8aad2c2bb2d100c0270a687c519899f6a",
          "native_face_offset": [
            109,
            85
          ],
          "output_sha256": "b68b10b4530c261991b4afa29dd60a3716090e68734c8a2b542708567dd98343"
        },
        {
          "resource": "adv_chara_010_01_02",
          "body": "adv_chara_010_01.png",
          "body_sha256": "ac05f3cd59cf77b2e8a37a23f406bd671a62496ebe681ec9bf0983fc6c843168",
          "face": "adv_chara_010_01_02.png",
          "face_sha256": "6b0f9429d27ad703b8f7e98e3fb7c898757cea51e7676db2de77742ab1d52503",
          "native_face_offset": [
            150,
            104
          ],
          "output_sha256": "49dad82a25a931b7556bd121b4481b835e863671718daa55813abfc5a33b971d"
        }
      ],
      "coverage_effective_state_sha256": "c1e2a9c918b898f53a33512a210d80e99447a51f835ea87b2ebb20103427e087",
      "execution_record": "09 Audits and Manifests/T7S_B0100_B0159_EXECUTION_RECORD.md",
      "boundary": "Complete chapter-local text/native state plus selected static review; no authored choice or inline movie; no later-source semantic evidence; performed audio unreviewed."
    },
    "b0112_close_verification": {
      "operation": "T7S_B0112_CLOSE",
      "checked_at": "2026-09-26",
      "status": "PASS_BOUNDED_TEXT_NATIVE_AND_STATIC_REVIEW",
      "episode_ids": [
        "312200701",
        "312200702",
        "312200703"
      ],
      "source_bindings": [
        {
          "episode_id": "312200701",
          "script_id": "ing_102007_01.json__ae7fe6e91532e45c",
          "source_sha256": "9630c1eab10647e1fba4cdd43891c51ca2c26e243445c2bc98b6910fb3ee8f7a",
          "decoded_sha256": "9cd1a1832fdc465d7fbd9e99c65cb0117a7d8a5b2ffb41cb31110baf33bb2719",
          "normalized_sha256": "544799cfd46c9c041d90a0510abc6c330b6017a06fd3804b50ed790b9d618b0d",
          "structured_sha256": "544799cfd46c9c041d90a0510abc6c330b6017a06fd3804b50ed790b9d618b0d",
          "pages": 50,
          "text_records": 43,
          "command_only_pages": 7,
          "voice_pages": 37,
          "native_pages_verified": 50
        },
        {
          "episode_id": "312200702",
          "script_id": "ing_102007_02.json__8eb4895f3e2425f6",
          "source_sha256": "a6c91c06d825948664cea004f634ed0e158c3670f0ccfc39743ef1e1a51f88a1",
          "decoded_sha256": "e5b29082ba57ed9d2dcd45ecb99f95c5e0fcd8dde6d910ed499dd6b247cf26c9",
          "normalized_sha256": "0b86d1a52c7f8f0d1da01770948fa395ce3c58dc3369230389a37257102a56d7",
          "structured_sha256": "0b86d1a52c7f8f0d1da01770948fa395ce3c58dc3369230389a37257102a56d7",
          "pages": 53,
          "text_records": 51,
          "command_only_pages": 2,
          "voice_pages": 47,
          "native_pages_verified": 53
        },
        {
          "episode_id": "312200703",
          "script_id": "ing_102007_03.json__0cd008f9558d2f52",
          "source_sha256": "6f4b394ae101976d69e8852c020548ff866c9c631d1254ac3caf47f1188487bf",
          "decoded_sha256": "43f6324d8bf5ed5a00bc10c18b44253cb81f86a357fad26a643ef25f4a601bde",
          "normalized_sha256": "0a8bcd04c92492e10043095ff5a40a119d0b8863e97b5ac1b74b454919dc8d1c",
          "structured_sha256": "0a8bcd04c92492e10043095ff5a40a119d0b8863e97b5ac1b74b454919dc8d1c",
          "pages": 71,
          "text_records": 61,
          "command_only_pages": 10,
          "voice_pages": 44,
          "native_pages_verified": 71
        }
      ],
      "totals": {
        "pages": 174,
        "text_records": 155,
        "command_only_pages": 19,
        "voice_pages": 128,
        "visual_refs": 1183
      },
      "voice_count_basis": "Distinct dialogue log-order indexes with voice resource; title-only cues additional; no performed audio reviewed.",
      "native_packet_sha256": "1d96fd00eab9e8bdc885188a92fbcaf07dbb228fc8fafc6bd75a4260ffbf3fef",
      "dialogue_packet_sha256": "2a07c452e04e6327565c6ffae72cde1916137f466fcc94874083f2e9e21273b9",
      "visual_assets": [
        {
          "resource": "adv_chara_009_03_12",
          "body": "adv_chara_009_03.png",
          "body_sha256": "ffc2406a944338eecacf731a83cc2ecfedce4b3e932bcbf3574528e5939035c8",
          "face": "adv_chara_009_03_12.png",
          "face_sha256": "8571371c4ff1ef4cfcde3dc25d0d26c96c9545731a97794152932c4ec203c165",
          "native_face_offset": [
            109,
            85
          ],
          "output_sha256": "156099a7209717a971a477b449f0d307c2121433dee5bcaefb21763fcf4337ab"
        },
        {
          "resource": "adv_chara_009_04_05",
          "body": "adv_chara_009_04.png",
          "body_sha256": "e9227fe6f31a495a3edae3a153780043bcd944776a1736ccd4413b17caca8a7b",
          "face": "adv_chara_009_04_05.png",
          "face_sha256": "570cced2b6e3e60f61c3c52413b523ae163414814b4e02170811210c369a52c3",
          "native_face_offset": [
            109,
            85
          ],
          "output_sha256": "8ccb2ee36912b87532de6dd287408bcbddc402f64f7227cf60de9819f5ce9c37"
        },
        {
          "resource": "adv_chara_006_01_05",
          "body": "adv_chara_006_01.png",
          "body_sha256": "d40ded643748164bb05d319c4a3889a41f99d102a3fcfeb60675b59529a6c392",
          "face": "adv_chara_006_01_05.png",
          "face_sha256": "4358c5a3ca68737fd4b6a1afa0edc2094c8ba9ed3985d0d71dea87f59ceca6b8",
          "native_face_offset": [
            134,
            91
          ],
          "output_sha256": "b1605bd99b38c2eb79e4dc83c899affa69c635b1c323fa57b217f3e3d4826fa7"
        },
        {
          "resource": "adv_chara_008_01_11",
          "body": "adv_chara_008_01.png",
          "body_sha256": "a72bd127faade4229587eff774c6b319fd99e8221290d4cfbd61769441d8afa4",
          "face": "adv_chara_008_01_11.png",
          "face_sha256": "90bd4ef9754ef0bb4feb08a9f247f3f14eae229693e43ad72d542ec37440898f",
          "native_face_offset": [
            166,
            84
          ],
          "output_sha256": "e7f53af41f122b88fdce7e49f85229221a9d923457a9907d0681530eceb070e6"
        },
        {
          "resource": "adv_chara_005_01_04",
          "body": "adv_chara_005_01.png",
          "body_sha256": "5eacc7b48f482d043fd5ebcb64d978a16ea335fd2c83a4b641983d2938444f21",
          "face": "adv_chara_005_01_04.png",
          "face_sha256": "ad98aa82a2fae4dfb7e1788688004d0549b3b52c86f26608b9b85e89998cca88",
          "native_face_offset": [
            76,
            85
          ],
          "output_sha256": "9335b3959b31b6bb77cbb834d0151071dd8ccecd28dbee2097aecb73087f68cd"
        },
        {
          "resource": "adv_chara_002_03_09",
          "body": "adv_chara_002_03.png",
          "body_sha256": "4bb14d813389b79055c4a24b5b3020e06bde9122d7b203b04a5489b358a7f1c7",
          "face": "adv_chara_002_03_09.png",
          "face_sha256": "1fbe266add4f4354eaa78d04c5616b2b2c265c0f8bece8f515c717df6dc5ae1f",
          "native_face_offset": [
            132,
            64
          ],
          "output_sha256": "8a3b5e12f4e5597ecc2a32bd2abc1b9932c08698d6a54809bf8cbb911b3f8609"
        }
      ],
      "coverage_effective_state_sha256": "72f688ee6583b5f55ae6e30361b23db07309b845fab3ed7041e624b5a472f645",
      "execution_record": "09 Audits and Manifests/T7S_B0100_B0159_EXECUTION_RECORD.md",
      "boundary": "Complete chapter-local text/native state plus selected static review; no authored choice or inline movie; no later-source semantic evidence; performed audio unreviewed."
    },
    "b0113_close_verification": {
      "operation": "T7S_B0113_CLOSE",
      "checked_at": "2026-09-26",
      "status": "PASS_BOUNDED_TEXT_NATIVE_AND_STATIC_REVIEW",
      "episode_ids": [
        "312200801",
        "312200802",
        "312200803"
      ],
      "source_bindings": [
        {
          "episode_id": "312200801",
          "script_id": "ing_102008_01.json__29c53004fe9e4559",
          "source_sha256": "b71eb2a078f67db225ad6db54e365d61638f7ba2e3065a50c8a2459bd138c628",
          "decoded_sha256": "cbb20a82e518b6ceadaebc011d56f24d9230ff2dd9deca33080a406a40af59c4",
          "normalized_sha256": "95957a31004368e652ade0b1a066ce4291b2dce4337ad886ad0dbd2c34b01229",
          "structured_sha256": "95957a31004368e652ade0b1a066ce4291b2dce4337ad886ad0dbd2c34b01229",
          "pages": 67,
          "text_records": 62,
          "command_only_pages": 5,
          "voice_pages": 47,
          "native_pages_verified": 67
        },
        {
          "episode_id": "312200802",
          "script_id": "ing_102008_02.json__00d1853f4a2e9660",
          "source_sha256": "67520b90200a3f19d83190dec000032e40dcdb08a73841903c4e2441e07ae75d",
          "decoded_sha256": "4cb0338b904f305d1dced39b8ee326be2735f6036766249e4d40096b9f991257",
          "normalized_sha256": "a71b2bba578868d80b014a00fd1f50921a78677422e1e5fe695acec54d50edd1",
          "structured_sha256": "a71b2bba578868d80b014a00fd1f50921a78677422e1e5fe695acec54d50edd1",
          "pages": 46,
          "text_records": 43,
          "command_only_pages": 3,
          "voice_pages": 27,
          "native_pages_verified": 46
        },
        {
          "episode_id": "312200803",
          "script_id": "ing_102008_03.json__ee132d916d5e737e",
          "source_sha256": "abb663aa550c1d28e83d8bbca3c57c9bd21a24c9ce52daf7a0f405794805ba0c",
          "decoded_sha256": "b8f15e8db6d379ca96c9eacfa293bb21ac81977fe74890ee8d6511bf148f04e4",
          "normalized_sha256": "4f1835f197f696d3a764e35470a6dd4430a1f3fd46a4b0b2de6295b7874bf81c",
          "structured_sha256": "4f1835f197f696d3a764e35470a6dd4430a1f3fd46a4b0b2de6295b7874bf81c",
          "pages": 89,
          "text_records": 80,
          "command_only_pages": 9,
          "voice_pages": 63,
          "native_pages_verified": 89
        }
      ],
      "totals": {
        "pages": 202,
        "text_records": 185,
        "command_only_pages": 17,
        "voice_pages": 137,
        "visual_refs": 2119
      },
      "voice_count_basis": "Distinct dialogue log-order indexes with voice resource; title-only cues additional; no performed audio reviewed.",
      "native_packet_sha256": "485735e3373e40b0deaecd8cd2abc8373c58b1826c87fe9e8a5248c6c92f42fe",
      "dialogue_packet_sha256": "dddb072f13f32c5d0448caedbf75aa6833d84592c17a355c8d47c362bcebff61",
      "visual_assets": [
        {
          "resource": "adv_chara_010_01_09",
          "body": "adv_chara_010_01.png",
          "body_sha256": "ac05f3cd59cf77b2e8a37a23f406bd671a62496ebe681ec9bf0983fc6c843168",
          "face": "adv_chara_010_01_09.png",
          "face_sha256": "59892c874433b4f16bc92afe202a72fcf403dd47e8478ed5c6605a12b6156b89",
          "native_face_offset": [
            150,
            104
          ],
          "output_sha256": "32eebfe4e0310945012fe72f1f500109db925f1541bd8b00e78351078a711dcf"
        },
        {
          "resource": "adv_chara_010_02_08",
          "body": "adv_chara_010_02.png",
          "body_sha256": "ae740226c3df25917ab2a2709ae40afb64cbcd2578c61ae1db3cc7325142583e",
          "face": "adv_chara_010_02_08.png",
          "face_sha256": "817f05599adef522d41d6e7d97a7948554a0344746adb84afbc5d1f1706d1172",
          "native_face_offset": [
            150,
            104
          ],
          "output_sha256": "25757c0ed32db3139a8b21f7bcd61f990f2d54bf34a5476e420d26a52fac45c6"
        },
        {
          "resource": "adv_chara_014_01_06",
          "body": "adv_chara_014_01.png",
          "body_sha256": "b8665daef47ba3fbf338538586adc18c16ed72c65092ad9d57cf2a4f128f3677",
          "face": "adv_chara_014_01_06.png",
          "face_sha256": "5d33ee9fd5886e7ceb6c858a98c5457c079a5032f6b823b4b2a49a95e96cc85f",
          "native_face_offset": [
            128,
            78
          ],
          "output_sha256": "07fdf3d9b19e57fce471ebd1f9dd1e74549cb46212b63d111b155edebb84cb02"
        },
        {
          "resource": "adv_chara_012_01_03",
          "body": "adv_chara_012_01.png",
          "body_sha256": "d142646f64071ed43061fd75721befa778228cd90a1c9d04fd996d739fc468b9",
          "face": "adv_chara_012_01_03.png",
          "face_sha256": "eb52d81955ecb2937d0fb351b050ac78936223bef86d63aff0cce86334bff491",
          "native_face_offset": [
            59,
            74
          ],
          "output_sha256": "9c43590c77bc51f510f387629f92f2eb3f1308230cedca8d2d2744eed9f2a8a5"
        },
        {
          "resource": "adv_chara_013_03_06",
          "body": "adv_chara_013_03.png",
          "body_sha256": "92050b6b91789e040270af209db2e8f7073dbf2732cf835f0846a64a1191dd02",
          "face": "adv_chara_013_03_06.png",
          "face_sha256": "83363ff59bf6ed3963568c04488d5c30b184e48acfb91dc344f1160b869555d2",
          "native_face_offset": [
            105,
            60
          ],
          "output_sha256": "29b26c31351c5255d4b8260ad896047951cf2462de286baa1d03fd3ac63bcfef"
        },
        {
          "resource": "adv_obj_0110",
          "body": "adv_obj_0110.png",
          "body_sha256": "1fee2d016a267c41f7fa1627499700975bc4cf418a6a1921ceea993002018e63",
          "output_sha256": "0139b04ad4c5381120f653b0026124e9076bb89428d8c5681b556cb90bb0ba8b"
        }
      ],
      "coverage_effective_state_sha256": "00f11e40ec54df81ca2ad55d8a7a15afa9bad16a9f7cc1a73c13c3e4f913f187",
      "execution_record": "09 Audits and Manifests/T7S_B0100_B0159_EXECUTION_RECORD.md",
      "boundary": "Complete chapter-local text/native state plus selected static review; no authored choice or inline movie; no later-source semantic evidence; performed audio unreviewed."
    },
    "b0114_close_verification": {
      "operation": "T7S_B0114_CLOSE",
      "checked_at": "2026-09-26",
      "status": "PASS_BOUNDED_TEXT_NATIVE_AND_STATIC_REVIEW",
      "episode_ids": [
        "312200901",
        "312200902",
        "312200903"
      ],
      "source_bindings": [
        {
          "episode_id": "312200901",
          "script_id": "ing_102009_01.json__dc0bbd76e10afcd7",
          "source_sha256": "bf3cd9928bb306523e3ab1c5a7da2a4e39b69f317af4702e8b32eab35d2ba754",
          "decoded_sha256": "ca90b7f2773a53181eb78086aa991c1e004580463cf62f9dc5e0b3fb24499db5",
          "normalized_sha256": "779c998d2edcf7d8c753ef448bddb1052bb5a2500962f2a00270d283b4dc6581",
          "structured_sha256": "779c998d2edcf7d8c753ef448bddb1052bb5a2500962f2a00270d283b4dc6581",
          "pages": 73,
          "text_records": 68,
          "command_only_pages": 5,
          "voice_pages": 68,
          "native_pages_verified": 73
        },
        {
          "episode_id": "312200902",
          "script_id": "ing_102009_02.json__a4c5c25706c5fb2d",
          "source_sha256": "2d7a4c606ab9a6741073eac5cab552518923e96e3eb54f4db4ef0b022b600cb4",
          "decoded_sha256": "67fa07d8c9676147fd3123794ba249cebe26f0993a179c0575686f207564da5f",
          "normalized_sha256": "bc42e1bfd362b1c802c3a2232a8cc9c0ce9eecebf99555539bd20635a9902c22",
          "structured_sha256": "bc42e1bfd362b1c802c3a2232a8cc9c0ce9eecebf99555539bd20635a9902c22",
          "pages": 97,
          "text_records": 88,
          "command_only_pages": 9,
          "voice_pages": 76,
          "native_pages_verified": 97
        },
        {
          "episode_id": "312200903",
          "script_id": "ing_102009_03.json__f19b0636a99c04de",
          "source_sha256": "8e58d9b3c67cb6ec965e507950af59741bc0e9056125b734539216c5223b9f2a",
          "decoded_sha256": "61e7d0a92aa1ce1047e084613f4fe124e367b8cf41f97c3253ae8eff7c2a09ee",
          "normalized_sha256": "1fa579f44d0cfc8185e6a20f98b9fbadae4f9a394db1ce44a3f15a0fdcebb663",
          "structured_sha256": "1fa579f44d0cfc8185e6a20f98b9fbadae4f9a394db1ce44a3f15a0fdcebb663",
          "pages": 81,
          "text_records": 74,
          "command_only_pages": 7,
          "voice_pages": 61,
          "native_pages_verified": 81
        }
      ],
      "totals": {
        "pages": 251,
        "text_records": 230,
        "command_only_pages": 21,
        "voice_pages": 205,
        "visual_refs": 1708
      },
      "voice_count_basis": "Distinct dialogue log-order indexes with voice resource; title-only cues additional; no performed audio reviewed.",
      "native_packet_sha256": "1619ce0d1d2fbe12b7f2c1f6c8921b60fe6abbfef0a6d32ed1798022cf291765",
      "dialogue_packet_sha256": "054e82fb3ce0a8a0277223643863a6bbc454851092d347b6bc99b2d137d13153",
      "visual_assets": [
        {
          "resource": "adv_chara_011_01_04",
          "body": "adv_chara_011_01.png",
          "body_sha256": "16fc2472d10c8972da16fad1f65b0bbc8c49cfb9daf7ebf2c583e54fedfb6004",
          "face": "adv_chara_011_01_04.png",
          "face_sha256": "e76bfd42497e39e6a02a908c937c3f49da9135d4b935569b01fd6763e655fbee",
          "native_face_offset": [
            89,
            54
          ],
          "output_sha256": "9832f830da4789df9cf72e429441032450520bb378e52dbcc0017488a91880ae"
        },
        {
          "resource": "adv_chara_004_01_06",
          "body": "adv_chara_004_01.png",
          "body_sha256": "5d8b60092117906b699d98ccabfc88344ea61f82e9b27a23bec1fa15d0cb65be",
          "face": "adv_chara_004_01_06.png",
          "face_sha256": "2ed7745b3f1906230a645b992a93e8259f8fd0466efab7fe91237c02d74440e7",
          "native_face_offset": [
            194,
            74
          ],
          "output_sha256": "768a21438bdc393bae3afad31a52cb7669988a04282251c52576a5353b7de373"
        },
        {
          "resource": "adv_chara_008_01_01",
          "body": "adv_chara_008_01.png",
          "body_sha256": "a72bd127faade4229587eff774c6b319fd99e8221290d4cfbd61769441d8afa4",
          "face": "adv_chara_008_01_01.png",
          "face_sha256": "6cde466239545bdd5ef7cf3a50542c810e853eb59f7519d9d476f4bd59f0e0a0",
          "native_face_offset": [
            166,
            84
          ],
          "output_sha256": "5da4d642d552e04c85241ddb25ebfa6707dabb3e06e17c22083e7151dfc9e16b"
        },
        {
          "resource": "adv_chara_012_01_03",
          "body": "adv_chara_012_01.png",
          "body_sha256": "d142646f64071ed43061fd75721befa778228cd90a1c9d04fd996d739fc468b9",
          "face": "adv_chara_012_01_03.png",
          "face_sha256": "eb52d81955ecb2937d0fb351b050ac78936223bef86d63aff0cce86334bff491",
          "native_face_offset": [
            59,
            74
          ],
          "output_sha256": "9c43590c77bc51f510f387629f92f2eb3f1308230cedca8d2d2744eed9f2a8a5"
        },
        {
          "resource": "adv_chara_003_01_15",
          "body": "adv_chara_003_01.png",
          "body_sha256": "cfd3a3dd39c6fd67b6ffc63190a2da76e8d1ef5cedcb8eb895afd2a9bd870064",
          "face": "adv_chara_003_01_15.png",
          "face_sha256": "db40498b8146a9523a96f19768e8f6dacce12589719ffb55933d731a6abca5cc",
          "native_face_offset": [
            98,
            92
          ],
          "output_sha256": "eb37c618b8433165c54168434b09fd165790b9651a6abe317fe9ee5a44323468"
        },
        {
          "resource": "adv_obj_0014",
          "body": "adv_obj_0014.png",
          "body_sha256": "0ca76a3d2adfdb7a899dc828a583132f6461e99e424aadf1f4fb364925f4704e",
          "output_sha256": "6964bceef80a9d47be5c5fdb22998ca7b5f00aa1c70041042ffb7ca047dea565"
        }
      ],
      "coverage_effective_state_sha256": "38fcd33f3abeca9cddaf149dec25226b4062c36b788e2ff22eea427332e6f58f",
      "execution_record": "09 Audits and Manifests/T7S_B0100_B0159_EXECUTION_RECORD.md",
      "boundary": "Complete chapter-local text/native state plus selected static review; no authored choice or inline movie; no later-source semantic evidence; performed audio unreviewed."
    },
    "b0115_close_verification": {
      "operation": "T7S_B0115_CLOSE",
      "checked_at": "2026-09-26",
      "status": "PASS_BOUNDED_TEXT_NATIVE_AND_STATIC_REVIEW",
      "episode_ids": [
        "312201001",
        "312201002",
        "312201003"
      ],
      "source_bindings": [
        {
          "episode_id": "312201001",
          "script_id": "ing_102010_01.json__16b79b30edef372b",
          "source_sha256": "9d0c4dcdc60027b94a1692f626733ecda84b4ca4dad144b84b6e9d5b3cec6a77",
          "decoded_sha256": "9805deb7e1d260527fe29ce77be97cddb46b258ddca3ccff004bb8b22d38972f",
          "normalized_sha256": "6798dcf8075b7e897d313b37a6900e381f4c1cf99613a55819228ca47a6369af",
          "structured_sha256": "6798dcf8075b7e897d313b37a6900e381f4c1cf99613a55819228ca47a6369af",
          "pages": 49,
          "text_records": 45,
          "command_only_pages": 4,
          "voice_pages": 10,
          "native_pages_verified": 49
        },
        {
          "episode_id": "312201002",
          "script_id": "ing_102010_02.json__546c4ad6dbb521a4",
          "source_sha256": "2606d8076586b1ccaae47bdea5d5cd8f9e892eda45502c82cf26765dd3e1336f",
          "decoded_sha256": "0b92c7fa28eb71bc80f8906356e373d714e4384bcea6e98b86e8200b0c5fb606",
          "normalized_sha256": "dafa06c8fea98ab5512fd27ce5518b4696ef0920d4114e11f79d8539b101f37c",
          "structured_sha256": "dafa06c8fea98ab5512fd27ce5518b4696ef0920d4114e11f79d8539b101f37c",
          "pages": 78,
          "text_records": 72,
          "command_only_pages": 6,
          "voice_pages": 41,
          "native_pages_verified": 78
        },
        {
          "episode_id": "312201003",
          "script_id": "ing_102010_03.json__0029607168c30667",
          "source_sha256": "d84a1aa982e8abe9bc79b22f617a657a823ca581d65c235488d0cdbaad542660",
          "decoded_sha256": "90a9fb0a67268661f3b65af4d34d6e4325c72ab3c66e958f02e45b15684f20fd",
          "normalized_sha256": "7aea61d42132c231854b5cf871476407f9d8ec84e090a49c5084da8a364e32a3",
          "structured_sha256": "7aea61d42132c231854b5cf871476407f9d8ec84e090a49c5084da8a364e32a3",
          "pages": 74,
          "text_records": 67,
          "command_only_pages": 7,
          "voice_pages": 38,
          "native_pages_verified": 74
        }
      ],
      "totals": {
        "pages": 201,
        "text_records": 184,
        "command_only_pages": 17,
        "voice_pages": 89,
        "visual_refs": 1484
      },
      "voice_count_basis": "Distinct dialogue log-order indexes with voice resource; title-only cues additional; no performed audio reviewed.",
      "native_packet_sha256": "e586f0bd38e4620c1d260845238a9502fde6cdbe9e930f2637bdae7675773f27",
      "dialogue_packet_sha256": "90388268a958f266ab8e64e8435f4e2f53d596a8ebd727a112197e5ba8ea7435",
      "visual_assets": [
        {
          "resource": "adv_chara_012_01_01",
          "body": "adv_chara_012_01.png",
          "body_sha256": "d142646f64071ed43061fd75721befa778228cd90a1c9d04fd996d739fc468b9",
          "face": "adv_chara_012_01_01.png",
          "face_sha256": "48fb3d5af2ec98fe05dd274e15e82fd680c07f6723ab0a2f5dceb188b7fcffd7",
          "native_face_offset": [
            59,
            74
          ],
          "output_sha256": "1a3b01fe595284bb8b645118dd34a3df4190b302bad562466afad619b5724c2b"
        },
        {
          "resource": "adv_chara_012_04_01",
          "body": "adv_chara_012_04.png",
          "body_sha256": "b8b023353bdebe02a2aef4266aab68372d50d18d4eb844f6bf2a8a65d065002a",
          "face": "adv_chara_012_04_01.png",
          "face_sha256": "f5ff02d5a714e368d1dd21c99a4d42ed923a70ab77806a866e3182d94734b111",
          "native_face_offset": [
            117,
            74
          ],
          "output_sha256": "9d93d07268979ff090f8cc89a60a4edf0bf28852949edab261dd3cb60b300f68"
        },
        {
          "resource": "adv_chara_014_01_05",
          "body": "adv_chara_014_01.png",
          "body_sha256": "b8665daef47ba3fbf338538586adc18c16ed72c65092ad9d57cf2a4f128f3677",
          "face": "adv_chara_014_01_05.png",
          "face_sha256": "ed32750fad9e53a36ed88a92c1a1344b25bb2e58684c66b433dce87ca8c475fe",
          "native_face_offset": [
            128,
            78
          ],
          "output_sha256": "9fbc6ee02ba0c8709964a98bf3f65d167b6b4d09f964141ec9bc9c3e4479c944"
        },
        {
          "resource": "adv_chara_007_01_02",
          "body": "adv_chara_007_01.png",
          "body_sha256": "1bf0de43c70899cafbf9ae8fedfba9663293ade0a774d004e620c158af87ccf0",
          "face": "adv_chara_007_01_02.png",
          "face_sha256": "447a64d6fb7ad56536043b47f3ce6f2bbc7784641d7915c577645ae1fb83f644",
          "native_face_offset": [
            84,
            80
          ],
          "output_sha256": "15f7a3434cf0f5029a643d8d16eb41fd459e289aee7072e2c47ad85e920ed869"
        },
        {
          "resource": "adv_chara_002_05_03",
          "body": "adv_chara_002_05.png",
          "body_sha256": "cb016340fb0d82c4b3f5e1c47bcd449550f680719951d70b9cbb10018be79a0b",
          "face": "adv_chara_002_05_03.png",
          "face_sha256": "bd26f12ebf371ca0f0dcbd14bd681b114b478139f5ac5204be8c1e92f7359027",
          "native_face_offset": [
            132,
            64
          ],
          "output_sha256": "9dbec5359d6fd116edc4d16bf92764c4eb13f21b9c73afff2f4d3b12070f1c88"
        },
        {
          "resource": "adv_obj_0014",
          "body": "adv_obj_0014.png",
          "body_sha256": "0ca76a3d2adfdb7a899dc828a583132f6461e99e424aadf1f4fb364925f4704e",
          "output_sha256": "6964bceef80a9d47be5c5fdb22998ca7b5f00aa1c70041042ffb7ca047dea565"
        }
      ],
      "coverage_effective_state_sha256": "ad86d7c66ee08fcaf643ec595e8a4a93d7f851ea568f6ef68b4903c6542879a8",
      "execution_record": "09 Audits and Manifests/T7S_B0100_B0159_EXECUTION_RECORD.md",
      "boundary": "Complete chapter-local text/native state plus selected static review; no authored choice or inline movie; no later-source semantic evidence; performed audio unreviewed."
    },
    "b0116_close_verification": {
      "operation": "T7S_B0116_CLOSE",
      "checked_at": "2026-09-26",
      "status": "PASS_BOUNDED_TEXT_NATIVE_AND_STATIC_REVIEW",
      "episode_ids": [
        "312201101",
        "312201102",
        "312201103"
      ],
      "source_bindings": [
        {
          "episode_id": "312201101",
          "script_id": "ing_102011_01.json__a9b92accd4908d59",
          "source_sha256": "8987c93c5e92d8a6f6e4038c1dd3d43f33ad2a48028fcdc62b476c9706fa58d4",
          "decoded_sha256": "6a8208eed1117e6d09cf77bab0d05b1f1ebc628e10a7d6a4c3160cd5b161678a",
          "normalized_sha256": "740b29c2da3d15d01597d492a089e5ae27d5045cd4ac128ef826bb53f09fda1d",
          "structured_sha256": "740b29c2da3d15d01597d492a089e5ae27d5045cd4ac128ef826bb53f09fda1d",
          "pages": 60,
          "text_records": 57,
          "command_only_pages": 3,
          "voice_pages": 25,
          "native_pages_verified": 60
        },
        {
          "episode_id": "312201102",
          "script_id": "ing_102011_02.json__87033737887480f6",
          "source_sha256": "8d823cab18a5a388c06d60f827da035c62dd23ea2151692f36a2dc102d2c59bc",
          "decoded_sha256": "966b40600b7403893a52d2fa1f38883ec48c600fcfd6c40cec37cfd4d5f4429a",
          "normalized_sha256": "1d07b8bb79c10f21c30f1f556021229d0889c8d564b51e3722fa7f7b788b0269",
          "structured_sha256": "1d07b8bb79c10f21c30f1f556021229d0889c8d564b51e3722fa7f7b788b0269",
          "pages": 76,
          "text_records": 69,
          "command_only_pages": 7,
          "voice_pages": 41,
          "native_pages_verified": 76
        },
        {
          "episode_id": "312201103",
          "script_id": "ing_102011_03.json__653c9be217a621d5",
          "source_sha256": "f15483fbf42178c329eb58398743e113629a4f110ca859e25b124972e8c0ac6b",
          "decoded_sha256": "1901a1f6cb02960eb29a39f71eec9de255402b317242a5bbc6a301cea1f71a25",
          "normalized_sha256": "3624dc2f0cf7329a02a36b131124a4be288ee06709443b90a4d0db30e84dd303",
          "structured_sha256": "3624dc2f0cf7329a02a36b131124a4be288ee06709443b90a4d0db30e84dd303",
          "pages": 71,
          "text_records": 66,
          "command_only_pages": 5,
          "voice_pages": 49,
          "native_pages_verified": 71
        }
      ],
      "totals": {
        "pages": 207,
        "text_records": 192,
        "command_only_pages": 15,
        "voice_pages": 115,
        "visual_refs": 1330
      },
      "voice_count_basis": "Distinct dialogue log-order indexes with voice resource; title-only cues additional; no performed audio reviewed.",
      "native_packet_sha256": "47529d4395aa62d91cc5d34fe738320dfa355a61175094a6177853617d93de56",
      "dialogue_packet_sha256": "99ff6514602aafc78247e97562c534b7d48c107159a01380a5eeb1a843100be5",
      "visual_assets": [
        {
          "resource": "adv_chara_013_01_01",
          "body": "adv_chara_013_01.png",
          "body_sha256": "2d4ca61240c61c15796eacab3c3a0ea5cf48f56c8b772d95e1b3ac1be0b7937c",
          "face": "adv_chara_013_01_01.png",
          "face_sha256": "a236fe22cae50a537cd68a6815caf0cc1accac77684eff2b648583d94cf7699d",
          "native_face_offset": [
            105,
            60
          ],
          "output_sha256": "262b62a2fe6a20eaad5f2a488b69373b9433688833bcc6a61d9efb4e5e1190d0"
        },
        {
          "resource": "adv_chara_013_04_08",
          "body": "adv_chara_013_04.png",
          "body_sha256": "db5a514c4560e26bae82ab5c5049fcb3221b5a95dbe79ce51032d43219a2d732",
          "face": "adv_chara_013_04_08.png",
          "face_sha256": "fd200db174220f61f275bab0e66835f6cc88189481f9a6698d23bf47325f10b4",
          "native_face_offset": [
            105,
            60
          ],
          "output_sha256": "195748b52be8f07bf171e6fc868f6b09587610808a443d8a097c6fb3c0ef9049"
        },
        {
          "resource": "adv_chara_014_05_05",
          "body": "adv_chara_014_05.png",
          "body_sha256": "3c82f1d57651d5a9716a723f297ba99fb24586ffe3272bac2353e7661b9d0192",
          "face": "adv_chara_014_05_05.png",
          "face_sha256": "062f6747ca84fcb8f8f9ebbf647e95f934a337a1efcd031b155f2014cffbf54c",
          "native_face_offset": [
            128,
            78
          ],
          "output_sha256": "346a594c71fcb99fff9b846f3120342ebd426a8af1732eda42ea53ac5a5837c6"
        },
        {
          "resource": "adv_chara_014_05_06",
          "body": "adv_chara_014_05.png",
          "body_sha256": "3c82f1d57651d5a9716a723f297ba99fb24586ffe3272bac2353e7661b9d0192",
          "face": "adv_chara_014_05_06.png",
          "face_sha256": "4f172cca81abe4cc0568f4f1fe0dfebce2ccb7bce8b35a1220e3a826f33972e1",
          "native_face_offset": [
            128,
            78
          ],
          "output_sha256": "9121894d3ebd6b5119325da785f21d9eca1f81a1addc8f4f7274ada99e53fca8"
        },
        {
          "resource": "adv_chara_002_03_01",
          "body": "adv_chara_002_03.png",
          "body_sha256": "4bb14d813389b79055c4a24b5b3020e06bde9122d7b203b04a5489b358a7f1c7",
          "face": "adv_chara_002_03_01.png",
          "face_sha256": "44744b274cd5f728379c329e9a722c0639e1fab23ae5e846a483a3f131e80e14",
          "native_face_offset": [
            132,
            64
          ],
          "output_sha256": "59b13c2655e6f3619ff902a52aac22ff6c10c4c63f17d56ed1b58b339f46165c"
        },
        {
          "resource": "adv_chara_003_01_02",
          "body": "adv_chara_003_01.png",
          "body_sha256": "cfd3a3dd39c6fd67b6ffc63190a2da76e8d1ef5cedcb8eb895afd2a9bd870064",
          "face": "adv_chara_003_01_02.png",
          "face_sha256": "662cc0b58a540e09b7adbde4607480e06779daf39145f86d2e22fc86ee8b5e41",
          "native_face_offset": [
            98,
            92
          ],
          "output_sha256": "928c5c610a0421a851f0389e209c6f315cfb7716c7519eb6d588c850410bd80b"
        }
      ],
      "coverage_effective_state_sha256": "223c64e7260d4328d2fdd4a8d756845bb8bf1aeb4664c87bfc9fa317cfe3771e",
      "execution_record": "09 Audits and Manifests/T7S_B0100_B0159_EXECUTION_RECORD.md",
      "boundary": "Complete chapter-local text/native state plus selected static review; no authored choice or inline movie; no later-source semantic evidence; performed audio unreviewed."
    },
    "b0117_close_verification": {
      "operation": "T7S_B0117_CLOSE",
      "checked_at": "2026-09-26",
      "status": "PASS_BOUNDED_TEXT_NATIVE_AND_STATIC_REVIEW",
      "episode_ids": [
        "312201201",
        "312201202",
        "312201203"
      ],
      "source_bindings": [
        {
          "episode_id": "312201201",
          "script_id": "ing_102012_01.json__35f16ad3de27654f",
          "source_sha256": "75d8917ef4a63c9c8e1fc35b14be0b6a00da9d4da00e564a59450e41909fd02b",
          "decoded_sha256": "bbecf0dc1fa0f2a7ff15dfd9567a9e02d8dd4a7885589203de233d10e804ba21",
          "normalized_sha256": "52331b51458233b4db696c5262015309356c84ceb873250ceaa598357c03de7e",
          "structured_sha256": "52331b51458233b4db696c5262015309356c84ceb873250ceaa598357c03de7e",
          "pages": 49,
          "text_records": 45,
          "command_only_pages": 4,
          "voice_pages": 26,
          "native_pages_verified": 49
        },
        {
          "episode_id": "312201202",
          "script_id": "ing_102012_02.json__dfded2ccfe9fc872",
          "source_sha256": "dddee9f0cb67f2b3f8ccfc95fb45979cfa89a79863b9e19aae893833987d4d2a",
          "decoded_sha256": "cae39603084afd60a1e04b227aa2edb0183a8fdc2cd7eaccce560c79bb7a4683",
          "normalized_sha256": "bad9004e01f97b10177cb8944f04fd1813665f28eddcb3fe0a48fc93e9069d6a",
          "structured_sha256": "bad9004e01f97b10177cb8944f04fd1813665f28eddcb3fe0a48fc93e9069d6a",
          "pages": 62,
          "text_records": 56,
          "command_only_pages": 6,
          "voice_pages": 38,
          "native_pages_verified": 62
        },
        {
          "episode_id": "312201203",
          "script_id": "ing_102012_03.json__3c0f277de16f74e0",
          "source_sha256": "b7a7f30a128f0d2b666a6f996991f9bc1e07cc7dc8b66ee32d26f8b7870cfd58",
          "decoded_sha256": "87bd56b7ee39c62f93473b0683d59cc1d485aac586f81e2c5cba10654052969e",
          "normalized_sha256": "d5c86a96fafb64b73d34c6a6fdae73dfcec7851a6cb5f4333ed80792bdbe7025",
          "structured_sha256": "d5c86a96fafb64b73d34c6a6fdae73dfcec7851a6cb5f4333ed80792bdbe7025",
          "pages": 93,
          "text_records": 84,
          "command_only_pages": 9,
          "voice_pages": 50,
          "native_pages_verified": 93
        }
      ],
      "totals": {
        "pages": 204,
        "text_records": 185,
        "command_only_pages": 19,
        "voice_pages": 114,
        "visual_refs": 1386
      },
      "voice_count_basis": "Distinct dialogue log-order indexes with voice resource; title-only cues additional; no performed audio reviewed.",
      "native_packet_sha256": "a320bc4114befa48ee12469f31078b8fa66c527bbf36dd5194db5ad360548b8b",
      "dialogue_packet_sha256": "83522c81a197f2ad1532ca60acb2a8a53c9de92259420b723b1e96b9025f1748",
      "visual_assets": [
        {
          "resource": "adv_chara_014_01_03",
          "body": "adv_chara_014_01.png",
          "body_sha256": "b8665daef47ba3fbf338538586adc18c16ed72c65092ad9d57cf2a4f128f3677",
          "face": "adv_chara_014_01_03.png",
          "face_sha256": "f57e067228e96a507dbbdc97128ed82caeb74e135b19891607478ec06797f877",
          "native_face_offset": [
            128,
            78
          ],
          "output_sha256": "730ce3c414094080338eb51ffefe4762e1062f10acebfeacdf8a601ced44da8a"
        },
        {
          "resource": "adv_chara_014_01_06",
          "body": "adv_chara_014_01.png",
          "body_sha256": "b8665daef47ba3fbf338538586adc18c16ed72c65092ad9d57cf2a4f128f3677",
          "face": "adv_chara_014_01_06.png",
          "face_sha256": "5d33ee9fd5886e7ceb6c858a98c5457c079a5032f6b823b4b2a49a95e96cc85f",
          "native_face_offset": [
            128,
            78
          ],
          "output_sha256": "07fdf3d9b19e57fce471ebd1f9dd1e74549cb46212b63d111b155edebb84cb02"
        },
        {
          "resource": "adv_chara_012_01_03",
          "body": "adv_chara_012_01.png",
          "body_sha256": "d142646f64071ed43061fd75721befa778228cd90a1c9d04fd996d739fc468b9",
          "face": "adv_chara_012_01_03.png",
          "face_sha256": "eb52d81955ecb2937d0fb351b050ac78936223bef86d63aff0cce86334bff491",
          "native_face_offset": [
            59,
            74
          ],
          "output_sha256": "9c43590c77bc51f510f387629f92f2eb3f1308230cedca8d2d2744eed9f2a8a5"
        },
        {
          "resource": "adv_chara_002_05_03",
          "body": "adv_chara_002_05.png",
          "body_sha256": "cb016340fb0d82c4b3f5e1c47bcd449550f680719951d70b9cbb10018be79a0b",
          "face": "adv_chara_002_05_03.png",
          "face_sha256": "bd26f12ebf371ca0f0dcbd14bd681b114b478139f5ac5204be8c1e92f7359027",
          "native_face_offset": [
            132,
            64
          ],
          "output_sha256": "9dbec5359d6fd116edc4d16bf92764c4eb13f21b9c73afff2f4d3b12070f1c88"
        },
        {
          "resource": "adv_chara_007_02_05",
          "body": "adv_chara_007_02.png",
          "body_sha256": "92aaed359500dd8fd52b4cecb0a7e1f60b0e63e466320ae2036086461c29edc1",
          "face": "adv_chara_007_02_05.png",
          "face_sha256": "9aff5c77bd3d5faee6ebad2fd36f3e60b82129041938f1c259062835f09e12c7",
          "native_face_offset": [
            84,
            80
          ],
          "output_sha256": "e6158174227e8535f778cec55e2720da5098ec41e7dec95fc24e61040aba0249"
        },
        {
          "resource": "adv_chara_008_01_05",
          "body": "adv_chara_008_01.png",
          "body_sha256": "a72bd127faade4229587eff774c6b319fd99e8221290d4cfbd61769441d8afa4",
          "face": "adv_chara_008_01_05.png",
          "face_sha256": "54eba0f49d3cf6f60a2ca1898d582deba1878ff4a93d74714d67a645ce138599",
          "native_face_offset": [
            166,
            84
          ],
          "output_sha256": "af57134822fe190980e93a60e5e4579a2dd1e3c68af007fb979943d5e1107a9c"
        }
      ],
      "coverage_effective_state_sha256": "4829c9eae8aca0111d3aac17b6bd4afb6a029b515892e573c575475ff8b6e9db",
      "execution_record": "09 Audits and Manifests/T7S_B0100_B0159_EXECUTION_RECORD.md",
      "boundary": "Complete chapter-local text/native state plus selected static review; no authored choice or inline movie; no later-source semantic evidence; performed audio unreviewed."
    },
    "b0118_close_verification": {
      "operation": "T7S_B0118_CLOSE",
      "checked_at": "2026-09-26",
      "status": "PASS_BOUNDED_TEXT_NATIVE_AND_STATIC_REVIEW",
      "episode_ids": [
        "312201301",
        "312201302",
        "312201303"
      ],
      "source_bindings": [
        {
          "episode_id": "312201301",
          "script_id": "ing_102013_01.json__91d426ea53103878",
          "source_sha256": "51571b3510dd785b761ed14019151a7b2ac43153106d65f1d4b8121ecfeb5b4a",
          "decoded_sha256": "71cdfbe3322ddb391a1336cc90ef97dde6e2dd84533338544f18ddbc2903d41f",
          "normalized_sha256": "3045e69c2ec76cf564a6be33a6d085d0317b3a5e12b121a138fd80162c59a273",
          "structured_sha256": "3045e69c2ec76cf564a6be33a6d085d0317b3a5e12b121a138fd80162c59a273",
          "pages": 36,
          "text_records": 32,
          "command_only_pages": 4,
          "voice_pages": 21,
          "native_pages_verified": 36
        },
        {
          "episode_id": "312201302",
          "script_id": "ing_102013_02.json__74c2ebdeb21ac1d1",
          "source_sha256": "693228318f0c3b515b53391646f0a5a29eab31c3c047d8c0dacd951ed65888ab",
          "decoded_sha256": "d5ac71441bcccf9c00d1b61b4e674aeffc8d2b848381941834e3af37e9a5bf75",
          "normalized_sha256": "5f0742f0cfc7a5304d0559a5d939891e997d1bbc7cbb0e6077c73344cbaab8ad",
          "structured_sha256": "5f0742f0cfc7a5304d0559a5d939891e997d1bbc7cbb0e6077c73344cbaab8ad",
          "pages": 50,
          "text_records": 46,
          "command_only_pages": 4,
          "voice_pages": 26,
          "native_pages_verified": 50
        },
        {
          "episode_id": "312201303",
          "script_id": "ing_102013_03.json__0e7130ff5bd2e570",
          "source_sha256": "20316c166fbb9dffd37a2f246f525f8e20db1d204b0003a700614bb227ba62ec",
          "decoded_sha256": "b886c47cc62c46d1df1f4165b987cec7453d9428dcc44aaa48f66b208a83eb83",
          "normalized_sha256": "a73bab892fb8ae7ee2eb84193e1bf3b624e6eb8d79c6037f758f828383193a3d",
          "structured_sha256": "a73bab892fb8ae7ee2eb84193e1bf3b624e6eb8d79c6037f758f828383193a3d",
          "pages": 70,
          "text_records": 63,
          "command_only_pages": 7,
          "voice_pages": 51,
          "native_pages_verified": 70
        }
      ],
      "totals": {
        "pages": 156,
        "text_records": 141,
        "command_only_pages": 15,
        "voice_pages": 98,
        "visual_refs": 1616
      },
      "voice_count_basis": "Distinct dialogue log-order indexes with voice resource; title-only cues additional; no performed audio reviewed.",
      "native_packet_sha256": "0ee940964f87cfb216632f03993280af315ae70bb1f597cee02ffdc52c7640ab",
      "dialogue_packet_sha256": "d08ba18285bfbae452d283a8c668bdee66f2f6f6495907dd7c94c4b61c573cd8",
      "visual_assets": [
        {
          "resource": "adv_chara_120_01_01",
          "body": "adv_chara_120_01.png",
          "body_sha256": "02b5a8e89ee8f85d06aea585dd4fa249ad9f2cb305e1f0446dd8891072ef682b",
          "face": "adv_chara_120_01_01.png",
          "face_sha256": "cb2aeece8bbe1e54d008bb68bf16e9d24ec4305378fb178bd309845d726408e8",
          "native_face_offset": [
            92,
            78
          ],
          "output_sha256": "aa09c7f2c3e32704dba98cc2cbf4bb5612137aee9418965a1e7e2b66c81bef9a"
        },
        {
          "resource": "adv_chara_120_02_02",
          "body": "adv_chara_120_02.png",
          "body_sha256": "145599551327a45a3bf0e6e57a87321333da314eaf8216f977f5c21d5a02f008",
          "face": "adv_chara_120_02_02.png",
          "face_sha256": "96a9463c65e7455100e7bb5871cecddd9d09cf85a91e20202907b0f89c2e88ff",
          "native_face_offset": [
            82,
            78
          ],
          "output_sha256": "1cede751b9faaeeeff49de3301faf9336f55eb89711253de1a9b45e6e6837edf"
        },
        {
          "resource": "adv_chara_006_01_01",
          "body": "adv_chara_006_01.png",
          "body_sha256": "d40ded643748164bb05d319c4a3889a41f99d102a3fcfeb60675b59529a6c392",
          "face": "adv_chara_006_01_01.png",
          "face_sha256": "f0b4ac890758947d8c9d96bbe5586eb8a06696cf88dc64fc805a27d544c71519",
          "native_face_offset": [
            134,
            91
          ],
          "output_sha256": "b7d30980c8b8f1232502f7de7c0892fd124efe982ad0e843cdf182cdbc4c2896"
        },
        {
          "resource": "adv_chara_006_03_01",
          "body": "adv_chara_006_03.png",
          "body_sha256": "97adf92e7dd722a0a3cf9d31e400351f042087f900cd1c83fc8bc0e2af7cbeed",
          "face": "adv_chara_006_03_01.png",
          "face_sha256": "2c87a07c735e9669eb78c6893fbcdc9c6c272aa3373d2b868d2ae7dd64f3ba13",
          "native_face_offset": [
            134,
            91
          ],
          "output_sha256": "bd7ae4da266891370350a869da8e3952490dd6e2edf7ff65c88163d14afdd287"
        },
        {
          "resource": "adv_chara_003_01_03",
          "body": "adv_chara_003_01.png",
          "body_sha256": "cfd3a3dd39c6fd67b6ffc63190a2da76e8d1ef5cedcb8eb895afd2a9bd870064",
          "face": "adv_chara_003_01_03.png",
          "face_sha256": "93a9a5a307de8f0bbd274e26dd966320a83ef4b76926376f6747db8801e68482",
          "native_face_offset": [
            98,
            92
          ],
          "output_sha256": "bd1adc2a89fc090c3d171b2bd42b4ced859b152dd582cae30d31fadcbaccd7fb"
        },
        {
          "resource": "adv_chara_003_06_05",
          "body": "adv_chara_003_06.png",
          "body_sha256": "a41fb44cc61027bc6f9f0a44fe7ff477be4bd04e6e671c3d77d6efbfdf7fc55e",
          "face": "adv_chara_003_06_05.png",
          "face_sha256": "bf22ef028c42ed207e7d2d4243113aca2286050bcf6c25f3d68074505cd88ebb",
          "native_face_offset": [
            98,
            92
          ],
          "output_sha256": "dc88ab73b874767a74542663ca12abca8ca2dc398cbed1f15dff7b7a1a4eba70"
        }
      ],
      "coverage_effective_state_sha256": "ec713a5b71e029aa17026b225cbfca730976a4708102954c0cb9cabdec509b20",
      "execution_record": "09 Audits and Manifests/T7S_B0100_B0159_EXECUTION_RECORD.md",
      "boundary": "Complete chapter-local text/native state plus selected static review; no authored choice or inline movie; no later-source semantic evidence; performed audio unreviewed."
    },
    "b0119_close_verification": {
      "operation": "T7S_B0119_CLOSE",
      "checked_at": "2026-09-26",
      "status": "PASS_BOUNDED_TEXT_NATIVE_AND_STATIC_REVIEW",
      "episode_ids": [
        "312201401",
        "312201402",
        "312201403"
      ],
      "source_bindings": [
        {
          "episode_id": "312201401",
          "script_id": "ing_102014_01.json__a9d4cdcc1c366bcb",
          "source_sha256": "001e4189503b0fa90af93660412adaffb7e5ddf5b5e33fc96a0e77faadc3e7e2",
          "decoded_sha256": "0960b16bd565dca4d1d382de7b1e3daca0c92326268f12116d039a2a81b34d19",
          "normalized_sha256": "bf61a4d5adfc43c9f94c061316f35a25f58b9efc60d6938f2b1f1264fd9fdeba",
          "structured_sha256": "bf61a4d5adfc43c9f94c061316f35a25f58b9efc60d6938f2b1f1264fd9fdeba",
          "pages": 56,
          "text_records": 53,
          "command_only_pages": 3,
          "voice_pages": 40,
          "native_pages_verified": 56
        },
        {
          "episode_id": "312201402",
          "script_id": "ing_102014_02.json__886babd6975ad5d6",
          "source_sha256": "0ac642dfb4179c4e2a439aa2434dddd6c7c467fe062bd8068bbb57e0470bab22",
          "decoded_sha256": "3e6256137d3e0e24462f7613cdcf6c14280c05e657f928325be552383c2a2696",
          "normalized_sha256": "7cf97b64df941ed0fed5604c4a3b9e49eeb7f994883b8ba535af8248172275eb",
          "structured_sha256": "7cf97b64df941ed0fed5604c4a3b9e49eeb7f994883b8ba535af8248172275eb",
          "pages": 90,
          "text_records": 73,
          "command_only_pages": 17,
          "voice_pages": 72,
          "native_pages_verified": 90
        },
        {
          "episode_id": "312201403",
          "script_id": "ing_102014_03.json__38884bf3da8b94e8",
          "source_sha256": "0eb78401d6d155fdb86b5d9cc29700cc7acd345fb3dbfa84f2a0058aea503fc3",
          "decoded_sha256": "b80f0234dc39713b39710f59353baa0732fc229eac36a1f02edf143aaa0beb05",
          "normalized_sha256": "4cdd0ae64db951c5f9e8779cc9fbbe3e758834a5367dfa21e307346ae1fd7b8b",
          "structured_sha256": "4cdd0ae64db951c5f9e8779cc9fbbe3e758834a5367dfa21e307346ae1fd7b8b",
          "pages": 38,
          "text_records": 35,
          "command_only_pages": 3,
          "voice_pages": 31,
          "native_pages_verified": 38
        }
      ],
      "totals": {
        "pages": 184,
        "text_records": 161,
        "command_only_pages": 23,
        "voice_pages": 143,
        "visual_refs": 1253
      },
      "voice_count_basis": "Distinct dialogue log-order indexes with voice resource; title-only cues additional; no performed audio reviewed.",
      "native_packet_sha256": "07acc829bb9d3b6053f7bebdbb1c95bbb704af00c2a3e85a6e474af481dda73c",
      "dialogue_packet_sha256": "e7c999fcebe5cd3c342107d2d829e2786aff62151df94863cc378e2551e821fc",
      "visual_assets": [
        {
          "resource": "adv_chara_121_01_01",
          "body": "adv_chara_121_01.png",
          "body_sha256": "1c2133d1d764b59e1518e767fc8cebc27ab0a16d1b8fb2a0f3fb2f4279318002",
          "face": "adv_chara_121_01_01.png",
          "face_sha256": "be564fb8a9438da3248212f2f91a722f45e7a84203960302db296cbdc1885730",
          "native_face_offset": [
            107,
            90
          ],
          "output_sha256": "e4b8f6f358c86cb20849bc57ea5510a17f4919d40b1cf105fe87475ac329abd2"
        },
        {
          "resource": "adv_chara_144_02_01",
          "body": "adv_chara_144_02.png",
          "body_sha256": "b3add9963f1235965c9608f3f10913deb12de7f6cd76d94940c7d600839a104a",
          "face": "adv_chara_144_02_01.png",
          "face_sha256": "1432117f75a344a342a2e12ee5b7c13a1e52add2f3a2321604ca17aa20a546d5",
          "native_face_offset": [
            120,
            74
          ],
          "output_sha256": "837bc84e2c9baa6f39b14dca77ae38dc104002a45ea1303001f13093d703820d"
        },
        {
          "resource": "adv_chara_145_01_02",
          "body": "adv_chara_145_01.png",
          "body_sha256": "e7e4e7d94dadbb80e074cefd5e23ff1fc6cd5fbe2b6f60c39e6ecab367a58bb2",
          "face": "adv_chara_145_01_02.png",
          "face_sha256": "4ef3e561795beef0fe996afe979e12e2f638b74317bc24fcd3907c4808bf0b03",
          "native_face_offset": [
            78,
            63
          ],
          "output_sha256": "f2e6379db50f250a7c97442d6a1c396d802b2366dff3af87016ffab5f1b86239"
        },
        {
          "resource": "adv_chara_013_01_01",
          "body": "adv_chara_013_01.png",
          "body_sha256": "2d4ca61240c61c15796eacab3c3a0ea5cf48f56c8b772d95e1b3ac1be0b7937c",
          "face": "adv_chara_013_01_01.png",
          "face_sha256": "a236fe22cae50a537cd68a6815caf0cc1accac77684eff2b648583d94cf7699d",
          "native_face_offset": [
            105,
            60
          ],
          "output_sha256": "262b62a2fe6a20eaad5f2a488b69373b9433688833bcc6a61d9efb4e5e1190d0"
        },
        {
          "resource": "adv_chara_005_01_01",
          "body": "adv_chara_005_01.png",
          "body_sha256": "5eacc7b48f482d043fd5ebcb64d978a16ea335fd2c83a4b641983d2938444f21",
          "face": "adv_chara_005_01_01.png",
          "face_sha256": "087da32ef5957a1827c9ba84e43c2e8e4d19b71d55561220f01057f33768af2a",
          "native_face_offset": [
            76,
            85
          ],
          "output_sha256": "08577674aaec962626b0189c6933a38fa2c4a709874b6ebf768ea9364402d105"
        },
        {
          "resource": "adv_chara_009_03_05",
          "body": "adv_chara_009_03.png",
          "body_sha256": "ffc2406a944338eecacf731a83cc2ecfedce4b3e932bcbf3574528e5939035c8",
          "face": "adv_chara_009_03_05.png",
          "face_sha256": "570cced2b6e3e60f61c3c52413b523ae163414814b4e02170811210c369a52c3",
          "native_face_offset": [
            109,
            85
          ],
          "output_sha256": "819de191090fdfae2393e4e56dd4e8b5dfbe623097cd04e418e7002327e37189"
        }
      ],
      "coverage_effective_state_sha256": "db4b2fc6b648c5929fb5c735aa72ae988d2d607d2a2e241a2997dc2304b33dbb",
      "execution_record": "09 Audits and Manifests/T7S_B0100_B0159_EXECUTION_RECORD.md",
      "boundary": "Complete chapter-local text/native state plus selected static review; no authored choice or inline movie; no later-source semantic evidence; performed audio unreviewed."
    },
    "b0120_close_verification": {
      "operation": "T7S_B0120_CLOSE",
      "checked_at": "2026-09-26",
      "status": "PASS_BOUNDED_TEXT_NATIVE_AND_STATIC_REVIEW",
      "episode_ids": [
        "312201501",
        "312201502",
        "312201503"
      ],
      "source_bindings": [
        {
          "episode_id": "312201501",
          "script_id": "ing_102015_01.json__49c5506b92e5fd2a",
          "source_sha256": "6b6daa91482c87f1936ccacc55099c229978aa46c1a0ca04445520351b83e545",
          "decoded_sha256": "2e5aece6dd5a8394367b19c4a0b39ac4ee1d8fe0bee8b681e2f9cb6f64707a8e",
          "normalized_sha256": "f66b1c36ec3cf810447b77ca9b9618e21fa6f77fa958be86720bed9e8cd2b241",
          "structured_sha256": "f66b1c36ec3cf810447b77ca9b9618e21fa6f77fa958be86720bed9e8cd2b241",
          "pages": 38,
          "text_records": 35,
          "command_only_pages": 3,
          "voice_pages": 28,
          "native_pages_verified": 38
        },
        {
          "episode_id": "312201502",
          "script_id": "ing_102015_02.json__9f8a3258e7e0193c",
          "source_sha256": "991736253574c1bd11e275481eb0838f7f871e2a3a2a8c9ecfe162c8e3f1cbfb",
          "decoded_sha256": "c58b6144c301b01594dd98c76621753e5ef9a67f1382188c88687774cdc7d8b5",
          "normalized_sha256": "6eb0372241e754758443c500b03d147d0a85d4048b311dc9bba3017d558fc134",
          "structured_sha256": "6eb0372241e754758443c500b03d147d0a85d4048b311dc9bba3017d558fc134",
          "pages": 45,
          "text_records": 39,
          "command_only_pages": 6,
          "voice_pages": 32,
          "native_pages_verified": 45
        },
        {
          "episode_id": "312201503",
          "script_id": "ing_102015_03.json__9c86365e07234036",
          "source_sha256": "0b65a09a68e789d3fb873e6a5ff7fd085975918471ef9c5e9aa2d7d83eae23a1",
          "decoded_sha256": "3e2d0f2bd22ed68fb65ba7987762c62ab725027a5840be3b51ffb31f732e770d",
          "normalized_sha256": "a3001f6eebed014ccfdb9d102d51aa561a41d4ea401ea6817390781ec87ce96e",
          "structured_sha256": "a3001f6eebed014ccfdb9d102d51aa561a41d4ea401ea6817390781ec87ce96e",
          "pages": 79,
          "text_records": 71,
          "command_only_pages": 8,
          "voice_pages": 52,
          "native_pages_verified": 79
        }
      ],
      "totals": {
        "pages": 162,
        "text_records": 145,
        "command_only_pages": 17,
        "voice_pages": 112,
        "visual_refs": 1092
      },
      "voice_count_basis": "Distinct dialogue log-order indexes with voice resource; title-only cues additional; no performed audio reviewed.",
      "native_packet_sha256": "a61a3ef019407fa874c7db0cbad80d59f63410628b6a17fb5eb43a0740e4d528",
      "dialogue_packet_sha256": "582750320a8e303c15ecd02e4ecca5da38a8a33fd377c31d19ef602004a50e0c",
      "visual_assets": [
        {
          "resource": "adv_chara_122_01_01",
          "body": "adv_chara_122_01.png",
          "body_sha256": "87d7bb854bb0d05f5199139cf5b973a010f739936e1fe48ed07134ed15558e44",
          "face": "adv_chara_122_01_01.png",
          "face_sha256": "13c648aa7a348d9002d24e456e87b608fcf3eaad8e0fed754cce947b0db10be7",
          "native_face_offset": [
            104,
            104
          ],
          "output_sha256": "d7a3b9f5970eaa62b24a67cff84c2583e45e0cd783a21f49adfa44fd0a60b6d4"
        },
        {
          "resource": "adv_chara_122_03_04",
          "body": "adv_chara_122_03.png",
          "body_sha256": "1084fddf805e05a0839333213f525e754782d67da05bdbab8c884c197f5a7063",
          "face": "adv_chara_122_03_04.png",
          "face_sha256": "1e4f9d4e99ae91bed685823c5773a8b5108c6e903b8289951457a9b1993380cf",
          "native_face_offset": [
            104,
            104
          ],
          "output_sha256": "7e66ef5d92e70308cb22a2906a49a027aa892acb7273c1a48aa0ae3713b5d7e0"
        },
        {
          "resource": "adv_chara_134_01_01",
          "body": "adv_chara_134_01.png",
          "body_sha256": "59e54f3c7e045ef97681badac43daacab7c317c2456705c43ecd6e9021fcf960",
          "face": "adv_chara_134_01_01.png",
          "face_sha256": "fea863297cb5f0cc69f7afc53507625eb68936a5fd4e8d8a38edcf2b8dad8d11",
          "native_face_offset": [
            96,
            67
          ],
          "output_sha256": "a363b198ca80ebfe8335cd699850f068582b52cd7ebfff6f9bd1247a7de42a79"
        },
        {
          "resource": "adv_chara_128_01_01",
          "body": "adv_chara_128_01.png",
          "body_sha256": "627e3280d607585cb27dfda5c076a66f36a62cc9b23ce08780dd7fe85513829d",
          "face": "adv_chara_128_01_01.png",
          "face_sha256": "984450530f4a0bda0b2d44ac6eadb17a2f4867424684d0baa9e3309d6732cc1d",
          "native_face_offset": [
            105,
            107
          ],
          "output_sha256": "04e0efd55701ff973ae98c30d2406f7a2c5d4c3987294d966f8e2dc481be258b"
        },
        {
          "resource": "adv_chara_146_01_01",
          "body": "adv_chara_146_01.png",
          "body_sha256": "46fc3087e9a017bed96eb313d1311e9f939877b7d723a80efa91284489a7c112",
          "face": "adv_chara_146_01_01.png",
          "face_sha256": "801a2257357486bc74f1a57b3b5329afed804e5b0b0c8712d5d4c9ad690505fe",
          "native_face_offset": [
            81,
            44
          ],
          "output_sha256": "d08286dce366a3675dbb094b32d19834b0e32a730faf6930c3e74bae930d9566"
        },
        {
          "resource": "adv_chara_002_04_03",
          "body": "adv_chara_002_04.png",
          "body_sha256": "938fccd1b7bf1b8316a3ebb3c1da299beba659c3e51c5bcbb7abea4c41bb627a",
          "face": "adv_chara_002_04_03.png",
          "face_sha256": "64f33233995694810a22d6eafcf22501042f16f77d5bdfe057c3fc4dcf962117",
          "native_face_offset": [
            132,
            64
          ],
          "output_sha256": "10e56d3b3cc2ba4b736c35ea13de5a8cbd9da4f9245c5b5d47ac2ba0663a98c9"
        }
      ],
      "coverage_effective_state_sha256": "777094359ef7fd95d244a5e8bbd0ef9f03889693b83e838e84c2278abe1bc80e",
      "execution_record": "09 Audits and Manifests/T7S_B0100_B0159_EXECUTION_RECORD.md",
      "boundary": "Complete chapter-local text/native state plus selected static review; no authored choice or inline movie; no later-source semantic evidence; performed audio unreviewed."
    },
    "b0121_close_verification": {
      "operation": "T7S_B0121_CLOSE",
      "checked_at": "2026-09-26",
      "status": "PASS_BOUNDED_TEXT_NATIVE_AND_STATIC_REVIEW",
      "episode_ids": [
        "312201601",
        "312201602",
        "312201603"
      ],
      "source_bindings": [
        {
          "episode_id": "312201601",
          "script_id": "ing_102016_01.json__6a3387496207339a",
          "source_sha256": "18a9e5c13fd71c494d97369d547eb5f5925876f1aaef1aa123aa453ddd26ce5d",
          "decoded_sha256": "17beaaf86d398aaa25066f1cd1dc4d49dc5f7f79fc72085fc51a174bc429261a",
          "normalized_sha256": "6f94d2aa5e827a866d81594e299252e22450fa4a9026756dad84407d8148a4d8",
          "structured_sha256": "6f94d2aa5e827a866d81594e299252e22450fa4a9026756dad84407d8148a4d8",
          "pages": 46,
          "text_records": 43,
          "command_only_pages": 3,
          "voice_pages": 28,
          "native_pages_verified": 46
        },
        {
          "episode_id": "312201602",
          "script_id": "ing_102016_02.json__0aa105417e5c72d7",
          "source_sha256": "bfcc7ccd11b3b3bf73da439cadbf5467509155b23e6d0bdaed2eb4f47d6459aa",
          "decoded_sha256": "d8c7ad1989ee30388a26141c5544b2e7e8942fc16da5ea3e190f08e662dd044a",
          "normalized_sha256": "c2a6b8f674086af8b1d59fb8f63d96c7b3a12233482de0b694c0b8ae8c05f8bb",
          "structured_sha256": "c2a6b8f674086af8b1d59fb8f63d96c7b3a12233482de0b694c0b8ae8c05f8bb",
          "pages": 35,
          "text_records": 33,
          "command_only_pages": 2,
          "voice_pages": 20,
          "native_pages_verified": 35
        },
        {
          "episode_id": "312201603",
          "script_id": "ing_102016_03.json__86bf88a58ac97f8b",
          "source_sha256": "7c3b46f058b29cffac59bff0dffdede846ece3ab333bf2ac9598ddd3c00ee8c5",
          "decoded_sha256": "bc9fc4f79c55bf98ad0a7c105b9fc9b4e515d30919f9b31c6083953d60c5658f",
          "normalized_sha256": "ff7ce5e0d7c50b633fbb2d1141628d6a2d7f51bfa79afd1f0fd4fb1fbe65d932",
          "structured_sha256": "ff7ce5e0d7c50b633fbb2d1141628d6a2d7f51bfa79afd1f0fd4fb1fbe65d932",
          "pages": 104,
          "text_records": 90,
          "command_only_pages": 14,
          "voice_pages": 55,
          "native_pages_verified": 104
        }
      ],
      "totals": {
        "pages": 185,
        "text_records": 166,
        "command_only_pages": 19,
        "voice_pages": 103,
        "visual_refs": 1239
      },
      "voice_count_basis": "Distinct dialogue log-order indexes with voice resource; title-only cues additional; no performed audio reviewed.",
      "native_packet_sha256": "b8cff61c764bf79ce4b80caf6cde294872bdb7f5f6ce7c17fc9dc10254df0288",
      "dialogue_packet_sha256": "b865a28d77a7906825991da7cec851d51b9d413b7171487f4295ecd3d2d8ef08",
      "visual_assets": [
        {
          "resource": "adv_chara_123_01_01",
          "body": "adv_chara_123_01.png",
          "body_sha256": "bf9dd13377050333bee12690b2cb5cc31035c1f0269f79493d6b1761efb819fd",
          "face": "adv_chara_123_01_01.png",
          "face_sha256": "a85209f6800000479df29e7204bc6556f8ba99ac7bb14e2846dc64f666131a18",
          "native_face_offset": [
            99,
            78
          ],
          "output_sha256": "3429f48b8106558324a426cba3a9406f91b8e8972d8846a5de8a330b52dc43e4"
        },
        {
          "resource": "adv_chara_123_01_08",
          "body": "adv_chara_123_01.png",
          "body_sha256": "bf9dd13377050333bee12690b2cb5cc31035c1f0269f79493d6b1761efb819fd",
          "face": "adv_chara_123_01_08.png",
          "face_sha256": "cedfaa6968d3940dfafb88f55d977d4ecbc5db121e87f0599bd64729b8891a71",
          "native_face_offset": [
            99,
            78
          ],
          "output_sha256": "b77b27037f8546c2ee45e6213766824d8cae593220d7ec1f7590f5d617873870"
        },
        {
          "resource": "adv_chara_131_01_01",
          "body": "adv_chara_131_01.png",
          "body_sha256": "1a9960701b204ddf456de522c3d4e51d2820a1870f85ee2e0bcb8edd55d7f867",
          "face": "adv_chara_131_01_01.png",
          "face_sha256": "6109a77e56396791f1323cbbd533e126d66d38d6a1a6d042951d88771c8fdfdc",
          "native_face_offset": [
            118,
            62
          ],
          "output_sha256": "5dd9f639c14366e982f568ba01e22c7bec3fcb5bfac4a0373bb5971e31862127"
        },
        {
          "resource": "adv_chara_145_01_01",
          "body": "adv_chara_145_01.png",
          "body_sha256": "e7e4e7d94dadbb80e074cefd5e23ff1fc6cd5fbe2b6f60c39e6ecab367a58bb2",
          "face": "adv_chara_145_01_01.png",
          "face_sha256": "a8045a092f539cf3ee1987c8dffe76439e50c7c42f382458e945c76fd79decc1",
          "native_face_offset": [
            78,
            63
          ],
          "output_sha256": "ea67105eeee5254b86289fbd17a03cc53cc4e36bd71c0b8ce536893aec1fddcf"
        },
        {
          "resource": "adv_chara_144_02_03",
          "body": "adv_chara_144_02.png",
          "body_sha256": "b3add9963f1235965c9608f3f10913deb12de7f6cd76d94940c7d600839a104a",
          "face": "adv_chara_144_02_03.png",
          "face_sha256": "3a09bb67961d44af0e4080584f305a8b9f48979d7f3d67100b65929c7e1b3e40",
          "native_face_offset": [
            120,
            74
          ],
          "output_sha256": "0553efa4e33b588ba26936e06cc0eccf69ed4d20653fe049b303e24a82efff91"
        },
        {
          "resource": "adv_chara_120_01_05",
          "body": "adv_chara_120_01.png",
          "body_sha256": "02b5a8e89ee8f85d06aea585dd4fa249ad9f2cb305e1f0446dd8891072ef682b",
          "face": "adv_chara_120_01_05.png",
          "face_sha256": "1aa2c8b381614c0131620222c2f42f67f80ed42bbafe270ac5fca4917813797d",
          "native_face_offset": [
            92,
            78
          ],
          "output_sha256": "a77979c34e0a29251b98ea24fe621deb4b2677fcb78623a39f727a2a3d390e60"
        }
      ],
      "coverage_effective_state_sha256": "00dea25f860aea5c219842203436e2314b1cfafdc16273e6134a0363e1bfe493",
      "execution_record": "09 Audits and Manifests/T7S_B0100_B0159_EXECUTION_RECORD.md",
      "boundary": "Complete chapter-local text/native state plus selected static review; no authored choice or inline movie; no later-source semantic evidence; performed audio unreviewed."
    },
    "b0122_close_verification": {
      "operation": "T7S_B0122_CLOSE",
      "checked_at": "2026-09-26",
      "status": "PASS_BOUNDED_TEXT_NATIVE_AND_STATIC_REVIEW",
      "episode_ids": [
        "312201701",
        "312201702",
        "312201703"
      ],
      "source_bindings": [
        {
          "episode_id": "312201701",
          "script_id": "ing_102017_01.json__6524976942515a88",
          "source_sha256": "5d5fb1b5848f3a7ab5797a7d1aa9f2063d29ff350b4cb9f5b163fdd9cf60b4b9",
          "decoded_sha256": "21781036a622163bf85e13aa472b9a321ccd8a58beaed22a3744d02b70f62249",
          "normalized_sha256": "052fbc972077daa3efd8616ba1cca5ac1a99add9588fa7eccdeddea80d05bb26",
          "structured_sha256": "052fbc972077daa3efd8616ba1cca5ac1a99add9588fa7eccdeddea80d05bb26",
          "pages": 65,
          "text_records": 61,
          "command_only_pages": 4,
          "voice_pages": 43,
          "native_pages_verified": 65
        },
        {
          "episode_id": "312201702",
          "script_id": "ing_102017_02.json__af9de771e7d24268",
          "source_sha256": "e14f317e51ec60577aa69c5f834de63d66683cd2452d07c1dc2c64bac41200b9",
          "decoded_sha256": "70e3d46d9b6d67b41134e67fa7361de729528fd43d0975f573e3f55003e1586f",
          "normalized_sha256": "089c7ebf0bc90178b7b3892db082d905512189ca4947aa7caa74d94100daa05b",
          "structured_sha256": "089c7ebf0bc90178b7b3892db082d905512189ca4947aa7caa74d94100daa05b",
          "pages": 63,
          "text_records": 59,
          "command_only_pages": 4,
          "voice_pages": 44,
          "native_pages_verified": 63
        },
        {
          "episode_id": "312201703",
          "script_id": "ing_102017_03.json__9269ca9fa20133f9",
          "source_sha256": "45a61ec0a29dfccfd992fcf65f23886548a0fe1ea2b8dab251fe1f1278104af4",
          "decoded_sha256": "079c8cef633bd2f7385af76807188b40b5d0c42055b3b2264c8c5c9460e2ffb5",
          "normalized_sha256": "dafedac28ee01130da0e6a0248c911b05eccfd10dd9bc3052cf95dcaf4ecb1ca",
          "structured_sha256": "dafedac28ee01130da0e6a0248c911b05eccfd10dd9bc3052cf95dcaf4ecb1ca",
          "pages": 52,
          "text_records": 45,
          "command_only_pages": 7,
          "voice_pages": 34,
          "native_pages_verified": 52
        }
      ],
      "totals": {
        "pages": 180,
        "text_records": 165,
        "command_only_pages": 15,
        "voice_pages": 121,
        "visual_refs": 1211
      },
      "voice_count_basis": "Distinct dialogue log-order indexes with voice resource; title-only cues additional; no performed audio reviewed.",
      "native_packet_sha256": "6f1ad4e762acdd5112babc3b461bf8227a049edb7dd448e452dc22b1a9308de2",
      "dialogue_packet_sha256": "d44bd82fc3401c3e73c366309cb03e10d9a6068eb2eaf237f27f6ed40f28be6d",
      "visual_assets": [
        {
          "resource": "adv_chara_124_01_01",
          "body": "adv_chara_124_01.png",
          "body_sha256": "8bcac9ca97a13c056fec42fba89bd89a106b1ecf4be98535afb69c0c36f2a9fe",
          "face": "adv_chara_124_01_01.png",
          "face_sha256": "143562b5abec14ae3e7ce3b0245c7c4632d70ea6b1cf76d0b81967c674556fb0",
          "native_face_offset": [
            187,
            64
          ],
          "output_sha256": "016f1596228338d4e4977bc9634fc795a7d3ef0593af4763679c6be44a1d0a95"
        },
        {
          "resource": "adv_chara_124_01_03",
          "body": "adv_chara_124_01.png",
          "body_sha256": "8bcac9ca97a13c056fec42fba89bd89a106b1ecf4be98535afb69c0c36f2a9fe",
          "face": "adv_chara_124_01_03.png",
          "face_sha256": "e3a5356ccff82b369aa1dc9a13ce0826aa8f4f0a105d3d06f86e697617dd18fb",
          "native_face_offset": [
            187,
            64
          ],
          "output_sha256": "9aed98546115381957951ec7430332586d05ef61a723a741bbb3f63d45c44b9a"
        },
        {
          "resource": "adv_chara_124_01_04",
          "body": "adv_chara_124_01.png",
          "body_sha256": "8bcac9ca97a13c056fec42fba89bd89a106b1ecf4be98535afb69c0c36f2a9fe",
          "face": "adv_chara_124_01_04.png",
          "face_sha256": "eaf248f6894cedd92012492c5c8acd40a6ffed01015446788249a349a1e31669",
          "native_face_offset": [
            187,
            64
          ],
          "output_sha256": "2a0b5535703d7106856c673460820d1297ea4d9e85dea0b62bdc34b238164a5a"
        },
        {
          "resource": "adv_chara_125_01_01",
          "body": "adv_chara_125_01.png",
          "body_sha256": "8f7e41d6904a7ce92c78aefd75b75a66b2592a6f0563f6e1fee3cf89fb99a777",
          "face": "adv_chara_125_01_01.png",
          "face_sha256": "188c3338d01b40786fedcb0b8ca4dd626bc907e7681176808ed1dd2c23f0153b",
          "native_face_offset": [
            131,
            59
          ],
          "output_sha256": "aa5890b064149259e39d2fe85286d8eced2a8b89b30c3ab498c60cff429f2bed"
        },
        {
          "resource": "adv_chara_123_01_01",
          "body": "adv_chara_123_01.png",
          "body_sha256": "bf9dd13377050333bee12690b2cb5cc31035c1f0269f79493d6b1761efb819fd",
          "face": "adv_chara_123_01_01.png",
          "face_sha256": "a85209f6800000479df29e7204bc6556f8ba99ac7bb14e2846dc64f666131a18",
          "native_face_offset": [
            99,
            78
          ],
          "output_sha256": "3429f48b8106558324a426cba3a9406f91b8e8972d8846a5de8a330b52dc43e4"
        },
        {
          "resource": "adv_chara_133_01_03",
          "body": "adv_chara_133_01.png",
          "body_sha256": "ee3e5303e0e6ee798401ba7e6e276138169525925f4058c03f1d01ddd73fa7e5",
          "face": "adv_chara_133_01_03.png",
          "face_sha256": "d5c6e26da4ac5dd45ad6c8df4bee8161cb1f58c93ae06038b745b09603d8cacd",
          "native_face_offset": [
            142,
            66
          ],
          "output_sha256": "3a4d47c0b3943eb6f3cb819a278619cd88e251f3044c68d759c0edd84140d48d"
        }
      ],
      "coverage_effective_state_sha256": "948ef171543af776e571bcd136e6c76eedd93e10f1a3ccb60f8b7e60e5bb247b",
      "execution_record": "09 Audits and Manifests/T7S_B0100_B0159_EXECUTION_RECORD.md",
      "boundary": "Complete chapter-local text/native state plus selected static review; no authored choice or inline movie; no later-source semantic evidence; performed audio unreviewed."
    },
    "b0123_close_verification": {
      "operation": "T7S_B0123_CLOSE",
      "checked_at": "2026-09-26",
      "status": "PASS_BOUNDED_TEXT_NATIVE_AND_STATIC_REVIEW",
      "episode_ids": [
        "312201801",
        "312201802",
        "312201803"
      ],
      "source_bindings": [
        {
          "episode_id": "312201801",
          "script_id": "ing_102018_01.json__c9ad97d5edfa8210",
          "source_sha256": "a777120119f4fd92d7b905d6772436f20d073e4d7892647e6fb17bf485173d42",
          "decoded_sha256": "b512fd55ee356a4d202040747cdcd111a67f04051bc66a27b655336c5410fa8c",
          "normalized_sha256": "34cfe189f0f07815efda349ff457a525e3ca9c56500b8ec7ece6bdd164d26f18",
          "structured_sha256": "34cfe189f0f07815efda349ff457a525e3ca9c56500b8ec7ece6bdd164d26f18",
          "pages": 60,
          "text_records": 55,
          "command_only_pages": 5,
          "voice_pages": 47,
          "native_pages_verified": 60
        },
        {
          "episode_id": "312201802",
          "script_id": "ing_102018_02.json__ca87f74f9956e9fb",
          "source_sha256": "f01e8894ec2c8a2b95bf4040371d4c3d4a52cb1d8620f7647f8770234d2f9f22",
          "decoded_sha256": "121efb587b2657fe76035b8f1efe79f6fdbedb83147c93f5338bf528e6ba0fc6",
          "normalized_sha256": "530581a849b8ce76841d29b0353acf8e2498a2d2accbdb956a62820f11becf19",
          "structured_sha256": "530581a849b8ce76841d29b0353acf8e2498a2d2accbdb956a62820f11becf19",
          "pages": 42,
          "text_records": 39,
          "command_only_pages": 3,
          "voice_pages": 33,
          "native_pages_verified": 42
        },
        {
          "episode_id": "312201803",
          "script_id": "ing_102018_03.json__51d1ba1eac5e38f6",
          "source_sha256": "ea969d3dd47b77bb79d6477cdb3abf2dfef271187faee18924f0543da565fb77",
          "decoded_sha256": "a360b5b49247590e8363900d4de026b09a747f83943d8fdb602fb4fde809c409",
          "normalized_sha256": "b309549f24aa20f84dd6d78d9aeeffd07e7d1c2ae132c1c5e8983a963e26aed2",
          "structured_sha256": "b309549f24aa20f84dd6d78d9aeeffd07e7d1c2ae132c1c5e8983a963e26aed2",
          "pages": 72,
          "text_records": 67,
          "command_only_pages": 5,
          "voice_pages": 41,
          "native_pages_verified": 72
        }
      ],
      "totals": {
        "pages": 174,
        "text_records": 161,
        "command_only_pages": 13,
        "voice_pages": 121,
        "visual_refs": 1169
      },
      "voice_count_basis": "Distinct dialogue log-order indexes with voice resource; title-only cues additional; no performed audio reviewed.",
      "native_packet_sha256": "0a63548c6b1370823c4c64c3fbcc807375306d0243d0402a55c567de69247177",
      "dialogue_packet_sha256": "48072d804ec70ffd9c89b80e104bcfcc9fa76edbf2fde74ac770b2a189d9ff83",
      "visual_assets": [
        {
          "resource": "adv_chara_125_01_01",
          "body": "adv_chara_125_01.png",
          "body_sha256": "8f7e41d6904a7ce92c78aefd75b75a66b2592a6f0563f6e1fee3cf89fb99a777",
          "face": "adv_chara_125_01_01.png",
          "face_sha256": "188c3338d01b40786fedcb0b8ca4dd626bc907e7681176808ed1dd2c23f0153b",
          "native_face_offset": [
            131,
            59
          ],
          "output_sha256": "aa5890b064149259e39d2fe85286d8eced2a8b89b30c3ab498c60cff429f2bed"
        },
        {
          "resource": "adv_chara_125_01_04",
          "body": "adv_chara_125_01.png",
          "body_sha256": "8f7e41d6904a7ce92c78aefd75b75a66b2592a6f0563f6e1fee3cf89fb99a777",
          "face": "adv_chara_125_01_04.png",
          "face_sha256": "6af164c7ef926343c946e95ea2f54f23eddeff68029845f01c513f92b8b01bbe",
          "native_face_offset": [
            131,
            59
          ],
          "output_sha256": "6ceca233125d9e5cf01684deb029d7571fc9c30cd540301f3445409e468a34ad"
        },
        {
          "resource": "adv_chara_125_01_03",
          "body": "adv_chara_125_01.png",
          "body_sha256": "8f7e41d6904a7ce92c78aefd75b75a66b2592a6f0563f6e1fee3cf89fb99a777",
          "face": "adv_chara_125_01_03.png",
          "face_sha256": "4eaecf12c175e3f6e6ede2211505f10e996b730f781fa9203ba9e80d64065a8b",
          "native_face_offset": [
            131,
            59
          ],
          "output_sha256": "67e45af960c11ce4f6e697ea36dd55cb3636b5f23912e244c6e195daa84ebe3b"
        },
        {
          "resource": "adv_chara_123_01_02",
          "body": "adv_chara_123_01.png",
          "body_sha256": "bf9dd13377050333bee12690b2cb5cc31035c1f0269f79493d6b1761efb819fd",
          "face": "adv_chara_123_01_02.png",
          "face_sha256": "97612d00049a4509fc020fdbe32df26f26c39c6b1e652b6c118d1169a5f09838",
          "native_face_offset": [
            99,
            78
          ],
          "output_sha256": "337473b3f4e5d4a8b64ea1ea4a20444f1907599f8eac24415fbf14ccab0d6991"
        },
        {
          "resource": "adv_chara_124_01_03",
          "body": "adv_chara_124_01.png",
          "body_sha256": "8bcac9ca97a13c056fec42fba89bd89a106b1ecf4be98535afb69c0c36f2a9fe",
          "face": "adv_chara_124_01_03.png",
          "face_sha256": "e3a5356ccff82b369aa1dc9a13ce0826aa8f4f0a105d3d06f86e697617dd18fb",
          "native_face_offset": [
            187,
            64
          ],
          "output_sha256": "9aed98546115381957951ec7430332586d05ef61a723a741bbb3f63d45c44b9a"
        },
        {
          "resource": "adv_chara_002_03_09",
          "body": "adv_chara_002_03.png",
          "body_sha256": "4bb14d813389b79055c4a24b5b3020e06bde9122d7b203b04a5489b358a7f1c7",
          "face": "adv_chara_002_03_09.png",
          "face_sha256": "1fbe266add4f4354eaa78d04c5616b2b2c265c0f8bece8f515c717df6dc5ae1f",
          "native_face_offset": [
            132,
            64
          ],
          "output_sha256": "8a3b5e12f4e5597ecc2a32bd2abc1b9932c08698d6a54809bf8cbb911b3f8609"
        },
        {
          "resource": "adv_obj_0111",
          "body": "adv_obj_0111.png",
          "body_sha256": "1aa5c1e8c9499c7627a43a391030bd24a3bbe66a02d0d43b0ac739162986bbd6",
          "output_sha256": "b027e4ac69858b0a89274b315a065b21ddced2a22fff9b46202abaab8a0dbc22"
        }
      ],
      "coverage_effective_state_sha256": "5857c03bb70607d8cbf3a1bf60cba421a9fce575664211783ddd0c41caf8feb9",
      "execution_record": "09 Audits and Manifests/T7S_B0100_B0159_EXECUTION_RECORD.md",
      "boundary": "Complete chapter-local text/native state plus selected static review; no authored choice or inline movie; no later-source semantic evidence; performed audio unreviewed."
    },
    "b0124_close_verification": {
      "operation": "T7S_B0124_CLOSE",
      "checked_at": "2026-09-26",
      "status": "PASS_BOUNDED_TEXT_NATIVE_AND_STATIC_REVIEW",
      "episode_ids": [
        "312201901",
        "312201902",
        "312201903"
      ],
      "source_bindings": [
        {
          "episode_id": "312201901",
          "script_id": "ing_102019_01.json__3058a3892b9799e0",
          "source_sha256": "5742fba518ec5ff771e25e93584e4e0eb52f2387c29678df82bca13b028fa9d2",
          "decoded_sha256": "6fa6c2210bafaa91198ca6ffee1da9e07abb5c585c6d3dcbb68edb81f2ffc2a7",
          "normalized_sha256": "01ae2de304fe7329e175fe8df5f807d06a0efd2e7fa2e5f625845f6a4498bf90",
          "structured_sha256": "01ae2de304fe7329e175fe8df5f807d06a0efd2e7fa2e5f625845f6a4498bf90",
          "pages": 63,
          "text_records": 56,
          "command_only_pages": 7,
          "voice_pages": 27,
          "native_pages_verified": 63
        },
        {
          "episode_id": "312201902",
          "script_id": "ing_102019_02.json__69995a424d0fb9b8",
          "source_sha256": "e89b7c67e3798433d1721d429318c50cbee2e1a1b65b5e58c2f51e0ff95a8824",
          "decoded_sha256": "454fed7c3fc9f0f307b2b7efe0adf6288046456bd11a543132a31268d1492e05",
          "normalized_sha256": "c13f51672a13adce560c184cece3e77010aab0d2736d3b3b36e1c34759903229",
          "structured_sha256": "c13f51672a13adce560c184cece3e77010aab0d2736d3b3b36e1c34759903229",
          "pages": 49,
          "text_records": 45,
          "command_only_pages": 4,
          "voice_pages": 33,
          "native_pages_verified": 49
        },
        {
          "episode_id": "312201903",
          "script_id": "ing_102019_03.json__215acac05ea7137e",
          "source_sha256": "ecade343733b3086fe2641307341a68407ebbf11bc93344f9a5ca81821418594",
          "decoded_sha256": "e478851b6720f8ac77499487a0f60d708e2dcb050cc596a06ce4031a0e3edd92",
          "normalized_sha256": "63e9e00fa043a29c96527e54b297064d703c7c220d7d9822160161e0e94ac201",
          "structured_sha256": "63e9e00fa043a29c96527e54b297064d703c7c220d7d9822160161e0e94ac201",
          "pages": 80,
          "text_records": 73,
          "command_only_pages": 7,
          "voice_pages": 60,
          "native_pages_verified": 80
        }
      ],
      "totals": {
        "pages": 192,
        "text_records": 174,
        "command_only_pages": 18,
        "voice_pages": 120,
        "visual_refs": 1295
      },
      "voice_count_basis": "Distinct dialogue log-order indexes with voice resource; title-only cues additional; no performed audio reviewed.",
      "native_packet_sha256": "23c0267ef51f549c51e22a460884b69fb94558de10490ea07fe350c29e45508f",
      "dialogue_packet_sha256": "a75e24731c901da977e9dd2ae610bea4741535418c4c00b614aa1a35eea23e81",
      "visual_assets": [
        {
          "resource": "adv_chara_126_01_01",
          "body": "adv_chara_126_01.png",
          "body_sha256": "00ce923f755ee73078d66152d8d3d3bc5b0189a1d61173875e3443796d80e987",
          "face": "adv_chara_126_01_01.png",
          "face_sha256": "774420432ab233a6519985dfa12e34e197a97a5680a978723b6dcc7b10a7395e",
          "native_face_offset": [
            67,
            59
          ],
          "output_sha256": "49932c912ca5a89570312410bc57ba9f42ed947e5576332cefa5d7e8e0ba39b5"
        },
        {
          "resource": "adv_chara_126_01_05",
          "body": "adv_chara_126_01.png",
          "body_sha256": "00ce923f755ee73078d66152d8d3d3bc5b0189a1d61173875e3443796d80e987",
          "face": "adv_chara_126_01_05.png",
          "face_sha256": "a8a338ef42c4430026b134982eb7a2dbe278e43b24595cca0a435f3d98627167",
          "native_face_offset": [
            67,
            59
          ],
          "output_sha256": "f97c0857fb4390f47ef18d77693eec6458bc18895ce194a7654ab3556fd881ac"
        },
        {
          "resource": "adv_chara_005_01_04",
          "body": "adv_chara_005_01.png",
          "body_sha256": "5eacc7b48f482d043fd5ebcb64d978a16ea335fd2c83a4b641983d2938444f21",
          "face": "adv_chara_005_01_04.png",
          "face_sha256": "ad98aa82a2fae4dfb7e1788688004d0549b3b52c86f26608b9b85e89998cca88",
          "native_face_offset": [
            76,
            85
          ],
          "output_sha256": "9335b3959b31b6bb77cbb834d0151071dd8ccecd28dbee2097aecb73087f68cd"
        },
        {
          "resource": "adv_chara_120_01_04",
          "body": "adv_chara_120_01.png",
          "body_sha256": "02b5a8e89ee8f85d06aea585dd4fa249ad9f2cb305e1f0446dd8891072ef682b",
          "face": "adv_chara_120_01_04.png",
          "face_sha256": "93bcd625c105ccf6586f5a2b6d34fb1a641bef65c713acb3603d3119d14a7ab4",
          "native_face_offset": [
            92,
            78
          ],
          "output_sha256": "612bf8eef97f274e22a5d7302e1131472a798b148e878a25f39634187a18b6dc"
        },
        {
          "resource": "adv_chara_123_01_01",
          "body": "adv_chara_123_01.png",
          "body_sha256": "bf9dd13377050333bee12690b2cb5cc31035c1f0269f79493d6b1761efb819fd",
          "face": "adv_chara_123_01_01.png",
          "face_sha256": "a85209f6800000479df29e7204bc6556f8ba99ac7bb14e2846dc64f666131a18",
          "native_face_offset": [
            99,
            78
          ],
          "output_sha256": "3429f48b8106558324a426cba3a9406f91b8e8972d8846a5de8a330b52dc43e4"
        },
        {
          "resource": "adv_chara_147_01_05",
          "body": "adv_chara_147_01.png",
          "body_sha256": "df3ba4aa9a0969ae5dbb2f3d8b7e26c938ab1294692d595b12c3090fa8a47982",
          "face": "adv_chara_147_01_05.png",
          "face_sha256": "3c7fe6f30a65d203ac767fe46d4de76c5c0ac25de7327a57a7fd02f243fb49c1",
          "native_face_offset": [
            209,
            62
          ],
          "output_sha256": "642fecb3a5f8dce9bf90ca16ef600740b6f05b2e1bfec2faa7fb37de0121c0fc"
        },
        {
          "resource": "adv_chara_002_07_02",
          "body": "adv_chara_002_07.png",
          "body_sha256": "e299b2ccb8f49c9014aa59242afb0c5fb260b54d819620e7d17728597f06c015",
          "face": "adv_chara_002_07_02.png",
          "face_sha256": "36f5de896b1f9324d2693ded5d0b7cf2a39df2520d7c1d0f22c7b80c07c9ba99",
          "native_face_offset": [
            132,
            64
          ],
          "output_sha256": "763b90f28f302abc02baf72d1b434de6a810c051618de5a44f0fc725a68a6274"
        },
        {
          "resource": "adv_obj_0027",
          "body": "adv_obj_0027.png",
          "body_sha256": "5f8f7e302456a74fb0b57ecbf770b18515cfba5aabadb7c692f2db788e7ed322",
          "output_sha256": "a2cba3e2732a36e1ef0d6f4c3eee4f4072e570784eadafca4020d1b90da2cb93"
        },
        {
          "resource": "adv_obj_0026",
          "body": "adv_obj_0026.png",
          "body_sha256": "71d38c48ab7eaf915c6b8e2fd2dacffd45fc8be9c450b1e7c8f13c7bdd513950",
          "output_sha256": "05b4c5a41b2b5058922a1aa68b1121d46e5d789f25e7677c59c9d351540d05f6"
        }
      ],
      "coverage_effective_state_sha256": "41a059c28aa7927a838c6fb83d1b21dac5dbd25128e4dd2c9a45b8d5f16321b7",
      "execution_record": "09 Audits and Manifests/T7S_B0100_B0159_EXECUTION_RECORD.md",
      "boundary": "Complete chapter-local text/native state plus selected static review; no authored choice or inline movie; no later-source semantic evidence; performed audio unreviewed."
    },
    "b0125_close_verification": {
      "operation": "T7S_B0125_CLOSE",
      "checked_at": "2026-09-26",
      "status": "PASS_BOUNDED_TEXT_NATIVE_AND_STATIC_REVIEW",
      "episode_ids": [
        "312202001",
        "312202002",
        "312202003"
      ],
      "source_bindings": [
        {
          "episode_id": "312202001",
          "script_id": "ing_102020_01.json__1de22b624ed0446c",
          "source_sha256": "bfae3650dbce26f026d5024da16a5c5a0454aa0168f8b775db18a1b18106d1ac",
          "decoded_sha256": "f41a860e07732d900d3b171d83d556e3af0a7e5a6e331bc5b63da290e88f3f4a",
          "normalized_sha256": "e9212b3963d560c83160015ccc5d9cab58db784576746d9efeeb8df3665deb4c",
          "structured_sha256": "e9212b3963d560c83160015ccc5d9cab58db784576746d9efeeb8df3665deb4c",
          "pages": 33,
          "text_records": 28,
          "command_only_pages": 5,
          "voice_pages": 15,
          "native_pages_verified": 33
        },
        {
          "episode_id": "312202002",
          "script_id": "ing_102020_02.json__5aa980740c304030",
          "source_sha256": "3d35f825230c54fb2f37be5011a67365fe4a2193e2d55f34245b6258c143dc2a",
          "decoded_sha256": "232e5e5a9ece3fddad464964d7c4355cdc3b5c913c383485968a80d0462296c0",
          "normalized_sha256": "ca1fdd0607d2400e9018cce9dbfd3cce987fe9ecbef4170f02c145da0005c3ef",
          "structured_sha256": "ca1fdd0607d2400e9018cce9dbfd3cce987fe9ecbef4170f02c145da0005c3ef",
          "pages": 46,
          "text_records": 43,
          "command_only_pages": 3,
          "voice_pages": 29,
          "native_pages_verified": 46
        },
        {
          "episode_id": "312202003",
          "script_id": "ing_102020_03.json__8018795fc8a42d7a",
          "source_sha256": "04357235c3540d3ac8689a48a3dffa0581a77799373a346e2332d95869229c03",
          "decoded_sha256": "d11e43ea6da07037bb5481c16dc7b13e45efde5dbe1f9da76e111cccf1ddc01e",
          "normalized_sha256": "ae6d46b4b028f29eaa4856d34f01bea9a142e339d2563c2abb5ff30470ea2501",
          "structured_sha256": "ae6d46b4b028f29eaa4856d34f01bea9a142e339d2563c2abb5ff30470ea2501",
          "pages": 70,
          "text_records": 65,
          "command_only_pages": 5,
          "voice_pages": 57,
          "native_pages_verified": 70
        }
      ],
      "totals": {
        "pages": 149,
        "text_records": 136,
        "command_only_pages": 13,
        "voice_pages": 101,
        "visual_refs": 1595
      },
      "voice_count_basis": "Distinct dialogue log-order indexes with voice resource; title-only cues additional; no performed audio reviewed.",
      "native_packet_sha256": "b46bfcae27b42482407e9956176d58820f27e22febd2462c8a6e86fdc0422e6d",
      "dialogue_packet_sha256": "9c2b9277bfe02e5350ca733539fed36e0f96e92f706e43a8287fd2df0f5e84e8",
      "visual_assets": [
        {
          "resource": "adv_chara_127_01_03",
          "body": "adv_chara_127_01.png",
          "body_sha256": "55ab7e21679b73357782950a32dba638beb20b7be142cb9810b5021b94af28db",
          "face": "adv_chara_127_01_03.png",
          "face_sha256": "ff97821b4fc033cd5288f882f4600db3067eef61f46d40f383604d55f047c50e",
          "native_face_offset": [
            176,
            108
          ],
          "output_sha256": "05f7402263599adb912e13b0266c47b51c864deb64003106249ca55081beb435"
        },
        {
          "resource": "adv_chara_127_02_02",
          "body": "adv_chara_127_02.png",
          "body_sha256": "eca3cd36fc801dcf1e93e85ffaa806839d28ae78ee599b6848dd5d5bb0c64074",
          "face": "adv_chara_127_02_02.png",
          "face_sha256": "da731d1459ead146d090305d4b965516b2570e123830b6f21dfa5b741cfcf279",
          "native_face_offset": [
            176,
            108
          ],
          "output_sha256": "3c9540da0ac7dd60f68967a210609f667081fe64f69a177cc233ce23a6ce8b33"
        },
        {
          "resource": "adv_chara_127_02_01",
          "body": "adv_chara_127_02.png",
          "body_sha256": "eca3cd36fc801dcf1e93e85ffaa806839d28ae78ee599b6848dd5d5bb0c64074",
          "face": "adv_chara_127_02_01.png",
          "face_sha256": "1cc62adbbe97ae4da7e14f9818fd0e2780ca9941ec2184379e740cf07d0a28d0",
          "native_face_offset": [
            176,
            108
          ],
          "output_sha256": "b9d64f08b9cdd22bebd57e5907fa0b5d62213057b3a515a4a53218e7e7d752c6"
        },
        {
          "resource": "adv_chara_129_01_01",
          "body": "adv_chara_129_01.png",
          "body_sha256": "550d00a117209938229f026ddaaf021c465b7ea799a2e804e5364428050ed47b",
          "face": "adv_chara_129_01_01.png",
          "face_sha256": "1ddeb0f0e4f45308f0e37242f9932b63ad3d51db8609dd8e704bafaf4e5270e9",
          "native_face_offset": [
            108,
            72
          ],
          "output_sha256": "9b1b4ea703842a62f7299dc84b91205d849dcba84179625bafb7829e31876139"
        },
        {
          "resource": "adv_chara_129_01_03",
          "body": "adv_chara_129_01.png",
          "body_sha256": "550d00a117209938229f026ddaaf021c465b7ea799a2e804e5364428050ed47b",
          "face": "adv_chara_129_01_03.png",
          "face_sha256": "271ac55b0a59bd2cd9ee8e02b496408832335748f83f91d41d499da58f2959b5",
          "native_face_offset": [
            108,
            72
          ],
          "output_sha256": "d79737ba55018e8699606d00c0e09cde893db6387c706f60875e31d1d4843370"
        },
        {
          "resource": "adv_chara_146_01_02",
          "body": "adv_chara_146_01.png",
          "body_sha256": "46fc3087e9a017bed96eb313d1311e9f939877b7d723a80efa91284489a7c112",
          "face": "adv_chara_146_01_02.png",
          "face_sha256": "ecf0b8ba7e74f17b5328b6e93c55795db32d7211eceedefe000b38d61f6e4a5b",
          "native_face_offset": [
            81,
            44
          ],
          "output_sha256": "79551c4a5c3b39299498d0df479567bf99bf0436e1d75180e6aa314488a55a78"
        }
      ],
      "coverage_effective_state_sha256": "45fd21a637d58aa1ea85818336601cc824cf9c04c0f3db00e9b285ac99c16552",
      "execution_record": "09 Audits and Manifests/T7S_B0100_B0159_EXECUTION_RECORD.md",
      "boundary": "Complete chapter-local text/native state plus selected static review; no authored choice or inline movie; no later-source semantic evidence; performed audio unreviewed."
    },
    "b0126_close_verification": {
      "operation": "T7S_B0126_CLOSE",
      "checked_at": "2026-09-26",
      "status": "PASS_BOUNDED_TEXT_NATIVE_AND_STATIC_REVIEW",
      "episode_ids": [
        "312202101",
        "312202102",
        "312202103"
      ],
      "source_bindings": [
        {
          "episode_id": "312202101",
          "script_id": "ing_102021_01.json__c48279d6528646f1",
          "source_sha256": "cb1d0f2ba283918ec26bf35b5d06c360c67c2ac76a109b5089436500cc14c9d4",
          "decoded_sha256": "f9c670c8d82aa62b3daca7df9aa21c0801cd3c4b11536bc2c425a4466914e417",
          "normalized_sha256": "cf02205e7ea1fd6b54eacb00689b27fc3c476f57b3ed0b5d7ed6e155fe4c0582",
          "structured_sha256": "cf02205e7ea1fd6b54eacb00689b27fc3c476f57b3ed0b5d7ed6e155fe4c0582",
          "pages": 62,
          "text_records": 56,
          "command_only_pages": 6,
          "voice_pages": 38,
          "native_pages_verified": 62
        },
        {
          "episode_id": "312202102",
          "script_id": "ing_102021_02.json__ae76d53b850bf0c1",
          "source_sha256": "d6fbae05f517f922c8cb06042847c99419f3790e38b8187d806bf17d5b0c0edb",
          "decoded_sha256": "5eea13bb0609a52976b8a5df5f806d6a62e3e28d4a91c1be822e8c40c3147a9c",
          "normalized_sha256": "7b6bd19adf40a535ff140dad314e52ad0fb40e34a3eb39d14b881dbf2c8a6b6a",
          "structured_sha256": "7b6bd19adf40a535ff140dad314e52ad0fb40e34a3eb39d14b881dbf2c8a6b6a",
          "pages": 110,
          "text_records": 103,
          "command_only_pages": 7,
          "voice_pages": 76,
          "native_pages_verified": 110
        },
        {
          "episode_id": "312202103",
          "script_id": "ing_102021_03.json__ea5bf566af50809c",
          "source_sha256": "f3bae6b1cedf2706aeb2c1efe5a0a6212f18555ceb099d319c99e479a6751437",
          "decoded_sha256": "d35025d6005f8fb6c364330ca8c38ffbf73e2ea498216139fd6fed6c5d86f3ee",
          "normalized_sha256": "81dd5c1481ad07faeac8b1f7ce312180c7569a0cf9e27e04618ff68c98273ef0",
          "structured_sha256": "81dd5c1481ad07faeac8b1f7ce312180c7569a0cf9e27e04618ff68c98273ef0",
          "pages": 56,
          "text_records": 51,
          "command_only_pages": 5,
          "voice_pages": 41,
          "native_pages_verified": 56
        }
      ],
      "totals": {
        "pages": 228,
        "text_records": 210,
        "command_only_pages": 18,
        "voice_pages": 155,
        "visual_refs": 1561
      },
      "voice_count_basis": "Distinct dialogue log-order indexes with voice resource; title-only cues additional; no performed audio reviewed.",
      "native_packet_sha256": "91c94382b86a162554d1455e0a35029febbc89de923a626278343f61c6eb3086",
      "dialogue_packet_sha256": "7af67e3cdf5ccd0c0d385e164d25de6c135f890b9af884727c8710f10ccd8c41",
      "visual_assets": [
        {
          "resource": "adv_chara_128_01_03",
          "body": "adv_chara_128_01.png",
          "body_sha256": "627e3280d607585cb27dfda5c076a66f36a62cc9b23ce08780dd7fe85513829d",
          "face": "adv_chara_128_01_03.png",
          "face_sha256": "d4fe0a05b95c45312612503a6717d51781fed60b52bdf051e63220476179023f",
          "native_face_offset": [
            105,
            107
          ],
          "output_sha256": "f3078d3275e5b00ef7094abffb907b51efb889006d70762d07e890fd79215ece"
        },
        {
          "resource": "adv_chara_128_02_04",
          "body": "adv_chara_128_02.png",
          "body_sha256": "9d55ccbbe2712db4eb595f22ee58323e1e01784483ffbdb4ca33608f4cb4e9a5",
          "face": "adv_chara_128_02_04.png",
          "face_sha256": "a20a2d3b638597e5de52ec09660be5051beea3c59feae454fecc629f96d234ac",
          "native_face_offset": [
            105,
            107
          ],
          "output_sha256": "beb943bfc593c9b90cde1b96403dde4359328e07db3d5dc8a05f7219c96aa82e"
        },
        {
          "resource": "adv_chara_013_01_06",
          "body": "adv_chara_013_01.png",
          "body_sha256": "2d4ca61240c61c15796eacab3c3a0ea5cf48f56c8b772d95e1b3ac1be0b7937c",
          "face": "adv_chara_013_01_06.png",
          "face_sha256": "b0b643aa76ca4872ae5bca279ef63d17eff51a36d7a02ae1778b10a1ae15638b",
          "native_face_offset": [
            105,
            60
          ],
          "output_sha256": "ace194b5a470d1dc6761770df1a65c21e5767baa488651973a756f9e8bc206c2"
        },
        {
          "resource": "adv_chara_145_01_01",
          "body": "adv_chara_145_01.png",
          "body_sha256": "e7e4e7d94dadbb80e074cefd5e23ff1fc6cd5fbe2b6f60c39e6ecab367a58bb2",
          "face": "adv_chara_145_01_01.png",
          "face_sha256": "a8045a092f539cf3ee1987c8dffe76439e50c7c42f382458e945c76fd79decc1",
          "native_face_offset": [
            78,
            63
          ],
          "output_sha256": "ea67105eeee5254b86289fbd17a03cc53cc4e36bd71c0b8ce536893aec1fddcf"
        },
        {
          "resource": "adv_chara_144_01_04",
          "body": "adv_chara_144_01.png",
          "body_sha256": "20fc6bc7ed22a88c88e06eb84b21be11f06fa69cfd7f19e0de37a95c939d9f1e",
          "face": "adv_chara_144_01_04.png",
          "face_sha256": "14ef49097c42a359cc064c8d0453c65b86d80f47db681381141888c6c9cf3e9c",
          "native_face_offset": [
            120,
            74
          ],
          "output_sha256": "9ceb226d93a5b94c0b3433589b6e875670d261d8d24dd03dbae32715e2bc7943"
        },
        {
          "resource": "adv_chara_121_01_03",
          "body": "adv_chara_121_01.png",
          "body_sha256": "1c2133d1d764b59e1518e767fc8cebc27ab0a16d1b8fb2a0f3fb2f4279318002",
          "face": "adv_chara_121_01_03.png",
          "face_sha256": "33ef7661f2b56916fb83cffd1b39bd2a5d3e9633557421faf5b9651ee4e8890f",
          "native_face_offset": [
            107,
            90
          ],
          "output_sha256": "dbf819dc5d5ac6ef2a9f701b774e49f41174f1d5bc478fbf4d6bfd487f37f65f"
        },
        {
          "resource": "adv_chara_006_01_19",
          "body": "adv_chara_006_01.png",
          "body_sha256": "d40ded643748164bb05d319c4a3889a41f99d102a3fcfeb60675b59529a6c392",
          "face": "adv_chara_006_01_19.png",
          "face_sha256": "22164aee9604a09076dd075c02737d037bf46abde195eb4580e9cafbc6cfe6c4",
          "native_face_offset": [
            134,
            91
          ],
          "output_sha256": "867f8729e63a5a9952c62e5fc2fee72fd0d85c322b92e32a9f0262e82ccf1d0f"
        },
        {
          "resource": "adv_chara_002_03_06",
          "body": "adv_chara_002_03.png",
          "body_sha256": "4bb14d813389b79055c4a24b5b3020e06bde9122d7b203b04a5489b358a7f1c7",
          "face": "adv_chara_002_03_06.png",
          "face_sha256": "636d620d1336656ba031b88e5610fd04c6192ca6d40a1b779e32b8d306d77790",
          "native_face_offset": [
            132,
            64
          ],
          "output_sha256": "d4acd9b6bbdd52e118b16b068915911053dba4926cb1a27c3be5a4ed479f72fa"
        },
        {
          "resource": "adv_obj_0117",
          "body": "adv_obj_0117.png",
          "body_sha256": "33795d08a327a863825511da1a99f09aed67b963dbc59b597056ca0f4c01216d",
          "output_sha256": "647840791ecd01a83180539c9192346ac7e3e0897ef475e305d62511d658d93b"
        }
      ],
      "coverage_effective_state_sha256": "e937a1c70ea48835890bd8a7800c8b7edcd105e93c003067824f6a7ddc35367c",
      "execution_record": "09 Audits and Manifests/T7S_B0100_B0159_EXECUTION_RECORD.md",
      "boundary": "Complete chapter-local text/native state plus selected static review; no authored choice or inline movie; no later-source semantic evidence; performed audio unreviewed."
    },
    "b0127_close_verification": {
      "operation": "T7S_B0127_CLOSE",
      "checked_at": "2026-09-26",
      "status": "PASS_BOUNDED_TEXT_NATIVE_AND_STATIC_REVIEW",
      "episode_ids": [
        "312202201",
        "312202202",
        "312202203"
      ],
      "source_bindings": [
        {
          "episode_id": "312202201",
          "script_id": "ing_102022_01.json__23d4e5e8076b3159",
          "source_sha256": "6ddbbc0cbea27f69582348cb4eba2dacb063e8520e9d8491eccffd89ee8f03ac",
          "decoded_sha256": "f192ffa9c9314adf86330b384ca2c4ff5c8973e562b111187a9daa2bc72f9779",
          "normalized_sha256": "850ab5db40e39d92212a3d07196531318d8b0714a212b6bea748133907f44e4e",
          "structured_sha256": "850ab5db40e39d92212a3d07196531318d8b0714a212b6bea748133907f44e4e",
          "pages": 50,
          "text_records": 43,
          "command_only_pages": 7,
          "voice_pages": 26,
          "native_pages_verified": 50
        },
        {
          "episode_id": "312202202",
          "script_id": "ing_102022_02.json__fbf9c63477d465c5",
          "source_sha256": "c78cc28987bbb40fb3d738d8793be18c15263835a65f4d3e7150492e8c43e37a",
          "decoded_sha256": "4405f052919864313696ec0f22be1def4ff4a4e4fa268802efb79f1d9be69b1b",
          "normalized_sha256": "d68f1b483dce0a8744987056236169bf39ef540ef686e610f8a3d2b5c474bb44",
          "structured_sha256": "d68f1b483dce0a8744987056236169bf39ef540ef686e610f8a3d2b5c474bb44",
          "pages": 49,
          "text_records": 44,
          "command_only_pages": 5,
          "voice_pages": 44,
          "native_pages_verified": 49
        },
        {
          "episode_id": "312202203",
          "script_id": "ing_102022_03.json__4e4a1773aab5a677",
          "source_sha256": "63cc7dff9bc8570942d9899d1db9a3013a0dac9b29b5706c6a174dcbdb6af71c",
          "decoded_sha256": "8ee742c11b4b245933b761462b23a87ec3d10bcd38330c0ec59274f974f7b121",
          "normalized_sha256": "624298c94e4066cfc6fa77c01edea3a120c33b2390a964f08c9f235b55659888",
          "structured_sha256": "624298c94e4066cfc6fa77c01edea3a120c33b2390a964f08c9f235b55659888",
          "pages": 61,
          "text_records": 56,
          "command_only_pages": 5,
          "voice_pages": 56,
          "native_pages_verified": 61
        }
      ],
      "totals": {
        "pages": 160,
        "text_records": 143,
        "command_only_pages": 17,
        "voice_pages": 126,
        "visual_refs": 1078
      },
      "voice_count_basis": "Distinct dialogue log-order indexes with voice resource; title-only cues additional; no performed audio reviewed.",
      "native_packet_sha256": "e331b1feb2874713b4ac018a3a725ea36b886b390de13c5859d4e22d4de67967",
      "dialogue_packet_sha256": "b55960da866da378a57f818efc5dacadffc53e6bac9d8d5971fb7877b469325b",
      "visual_assets": [
        {
          "resource": "adv_chara_129_02_04",
          "body": "adv_chara_129_02.png",
          "body_sha256": "3b3561b12d9e97b5c8b46bce7ee758f05f1b08e6aed6a705210707efa3573371",
          "face": "adv_chara_129_02_04.png",
          "face_sha256": "562d109777d01e8ddc270f18b9af4726bdd8b3c93c71d454eba823b1716edb25",
          "native_face_offset": [
            128,
            72
          ],
          "output_sha256": "ca3972767d3a93245a6bb22450791ce059d6d0d3133e641ea74e3548b8fc9bfb"
        },
        {
          "resource": "adv_chara_129_02_01",
          "body": "adv_chara_129_02.png",
          "body_sha256": "3b3561b12d9e97b5c8b46bce7ee758f05f1b08e6aed6a705210707efa3573371",
          "face": "adv_chara_129_02_01.png",
          "face_sha256": "17c3ca03fb5874971606598ed0c8ae1d97c6da90888447c0d0ba95ae9642ef28",
          "native_face_offset": [
            128,
            72
          ],
          "output_sha256": "9043e944d99c3f348e9fa5e9bd0a043490107fc4354187feed2b5668bcca88a3"
        },
        {
          "resource": "adv_chara_129_02_05",
          "body": "adv_chara_129_02.png",
          "body_sha256": "3b3561b12d9e97b5c8b46bce7ee758f05f1b08e6aed6a705210707efa3573371",
          "face": "adv_chara_129_02_05.png",
          "face_sha256": "1b9b4484f775bb57443229f98ed573ee26096afb065b04dc0b20f9b632c1ef8d",
          "native_face_offset": [
            128,
            72
          ],
          "output_sha256": "22b0e17d4f06e1df741bb92b37876dd6dbb5b87da9a4afb0dc8872d06ed90f08"
        },
        {
          "resource": "adv_chara_149_01_01",
          "body": "adv_chara_149_01.png",
          "body_sha256": "99e954f4fe105fc93364cb6978bfe112dd69fe45e6f2cb11cee62fbf83b00624",
          "face": "adv_chara_149_01_01.png",
          "face_sha256": "bb5b4245ffe5fa87521be9d525e7ea0abbe50b196e62834094f210ce3046e4a5",
          "native_face_offset": [
            79,
            59
          ],
          "output_sha256": "3f0f91931eb0fc25d2f20338942093f17e0a75e0df8b1ab54171209b685eff88"
        },
        {
          "resource": "adv_chara_124_01_01",
          "body": "adv_chara_124_01.png",
          "body_sha256": "8bcac9ca97a13c056fec42fba89bd89a106b1ecf4be98535afb69c0c36f2a9fe",
          "face": "adv_chara_124_01_01.png",
          "face_sha256": "143562b5abec14ae3e7ce3b0245c7c4632d70ea6b1cf76d0b81967c674556fb0",
          "native_face_offset": [
            187,
            64
          ],
          "output_sha256": "016f1596228338d4e4977bc9634fc795a7d3ef0593af4763679c6be44a1d0a95"
        },
        {
          "resource": "adv_chara_002_03_01",
          "body": "adv_chara_002_03.png",
          "body_sha256": "4bb14d813389b79055c4a24b5b3020e06bde9122d7b203b04a5489b358a7f1c7",
          "face": "adv_chara_002_03_01.png",
          "face_sha256": "44744b274cd5f728379c329e9a722c0639e1fab23ae5e846a483a3f131e80e14",
          "native_face_offset": [
            132,
            64
          ],
          "output_sha256": "59b13c2655e6f3619ff902a52aac22ff6c10c4c63f17d56ed1b58b339f46165c"
        },
        {
          "resource": "adv_obj_0027",
          "body": "adv_obj_0027.png",
          "body_sha256": "5f8f7e302456a74fb0b57ecbf770b18515cfba5aabadb7c692f2db788e7ed322",
          "output_sha256": "a2cba3e2732a36e1ef0d6f4c3eee4f4072e570784eadafca4020d1b90da2cb93"
        }
      ],
      "coverage_effective_state_sha256": "5be377acc223f2e7c30bcb9f850843b4918fe624a0751eec33d9f073b89f51db",
      "execution_record": "09 Audits and Manifests/T7S_B0100_B0159_EXECUTION_RECORD.md",
      "boundary": "Complete chapter-local text/native state plus selected static review; no authored choice or inline movie; no later-source semantic evidence; performed audio unreviewed."
    },
    "b0128_close_verification": {
      "operation": "T7S_B0128_CLOSE",
      "checked_at": "2026-09-26",
      "status": "PASS_BOUNDED_TEXT_NATIVE_AND_STATIC_REVIEW",
      "episode_ids": [
        "312202301",
        "312202302",
        "312202303"
      ],
      "source_bindings": [
        {
          "episode_id": "312202301",
          "script_id": "ing_102023_01.json__4136e55f49a6fb74",
          "source_sha256": "d8b6eed33efba517475903e0a60da0ee1ca9fed2082e0c2c8104add29ebcafe4",
          "decoded_sha256": "35c9053f2dec95f53e04e5ba0b34b69cd5e708cbe0f6b7f4463346b0d273ca1c",
          "normalized_sha256": "19537c1f1b9d1383ac2f7d9562ea527071325318d2736cb59a830284d722257c",
          "structured_sha256": "19537c1f1b9d1383ac2f7d9562ea527071325318d2736cb59a830284d722257c",
          "pages": 46,
          "text_records": 39,
          "command_only_pages": 7,
          "voice_pages": 35,
          "native_pages_verified": 46
        },
        {
          "episode_id": "312202302",
          "script_id": "ing_102023_02.json__cd2b7d74c5de765b",
          "source_sha256": "8a9c4fd3cbd0f8aadeb312f4f52f73e64cb06a94873c11328ff537e7c6ea517d",
          "decoded_sha256": "cd9b0452df5bb02ab5685b605a70ec8cbfb7f43fd7f37feb8c0ade8565ce3767",
          "normalized_sha256": "60da40de11a0dc716189c91fb6628867c48c9e5a373d84ec64456ee1827a2795",
          "structured_sha256": "60da40de11a0dc716189c91fb6628867c48c9e5a373d84ec64456ee1827a2795",
          "pages": 83,
          "text_records": 77,
          "command_only_pages": 6,
          "voice_pages": 60,
          "native_pages_verified": 83
        },
        {
          "episode_id": "312202303",
          "script_id": "ing_102023_03.json__b3c1a7ea995ba81f",
          "source_sha256": "8434eed10c44938b1008e17d548e94fea7db4bd82f5a71f329b67614fb0dc9eb",
          "decoded_sha256": "72ba583700b020f3d21456880d6d4c70f37bfd4eb0d5dc3b6ca2cc8e4db6ed28",
          "normalized_sha256": "eaeab4fa61d2b4d3fcd76dcd5f61dc2e04ebb7352207f4b5bc948b47ff36187f",
          "structured_sha256": "eaeab4fa61d2b4d3fcd76dcd5f61dc2e04ebb7352207f4b5bc948b47ff36187f",
          "pages": 56,
          "text_records": 50,
          "command_only_pages": 6,
          "voice_pages": 39,
          "native_pages_verified": 56
        }
      ],
      "totals": {
        "pages": 185,
        "text_records": 166,
        "command_only_pages": 19,
        "voice_pages": 134,
        "visual_refs": 1584
      },
      "voice_count_basis": "Distinct dialogue log-order indexes with voice resource; title-only cues additional; no performed audio reviewed.",
      "native_packet_sha256": "6603664f0fca81ff4b1ab1533269659ffdab42ae48be2c7c0e9ce55274240f0f",
      "dialogue_packet_sha256": "e110772b162403e545066107a94156a0525481b8e9b4f0196558d5e5153c34b1",
      "visual_assets": [
        {
          "resource": "adv_chara_130_01_02",
          "body": "adv_chara_130_01.png",
          "body_sha256": "c1f245d9bc7282b4d8705cd84733794e6855e67f256bf11c51ea47ef2b679efa",
          "face": "adv_chara_130_01_02.png",
          "face_sha256": "8e0425aba1e614c513fbf1ade0652e8df97ca0e177c3fa722e04f4888a09fb3b",
          "native_face_offset": [
            145,
            74
          ],
          "output_sha256": "833d31b700f2c584e89da789e3306bf322df71206c3c2ce45a4a43d2a94b7a44"
        },
        {
          "resource": "adv_chara_130_02_01",
          "body": "adv_chara_130_02.png",
          "body_sha256": "e299c7a58277156abccfb24c37adbcb29cb82a5d867696156d62d9e71361e97f",
          "face": "adv_chara_130_02_01.png",
          "face_sha256": "2b648a7320b4606821af616600c13a4758180f4a26a74707379d3d00877cfb4b",
          "native_face_offset": [
            145,
            74
          ],
          "output_sha256": "b2b73f832c23ab411210ecda248358be7f6714effb92c5a71d332625c6da2a48"
        },
        {
          "resource": "adv_chara_130_02_04",
          "body": "adv_chara_130_02.png",
          "body_sha256": "e299c7a58277156abccfb24c37adbcb29cb82a5d867696156d62d9e71361e97f",
          "face": "adv_chara_130_02_04.png",
          "face_sha256": "cb1f53ea39d6748350b36a1d10bf3094c7877c4934caf564505b9779363ac272",
          "native_face_offset": [
            145,
            74
          ],
          "output_sha256": "d9220329f7a42ef841863f7ea01f39ce2393e4f07d617b85067d05606acc9bd1"
        },
        {
          "resource": "adv_chara_127_01_01",
          "body": "adv_chara_127_01.png",
          "body_sha256": "55ab7e21679b73357782950a32dba638beb20b7be142cb9810b5021b94af28db",
          "face": "adv_chara_127_01_01.png",
          "face_sha256": "4cb29f702bfc626726aa369fd36a1e62fc518fff214338cb4ce6dc4237bbcaf0",
          "native_face_offset": [
            176,
            108
          ],
          "output_sha256": "2173b61a37f0aaa3172f20921551ed6a21b62e82e33875b67c2df2805aeafa72"
        },
        {
          "resource": "adv_chara_137_01_01",
          "body": "adv_chara_137_01.png",
          "body_sha256": "8da617d5736a9e233312322d4f1a1edff77c9f764832a0665ddc3d9adb9610ba",
          "face": "adv_chara_137_01_01.png",
          "face_sha256": "0c0e4d6ada1b1001af6571102309321d09bc1cba4d9eb26428af34ea6ac8ee54",
          "native_face_offset": [
            104,
            62
          ],
          "output_sha256": "b84e2673dec0b2f5a4af5064939e3a7dc08e5a33ad883448b5f98f422146b833"
        },
        {
          "resource": "adv_chara_146_01_01",
          "body": "adv_chara_146_01.png",
          "body_sha256": "46fc3087e9a017bed96eb313d1311e9f939877b7d723a80efa91284489a7c112",
          "face": "adv_chara_146_01_01.png",
          "face_sha256": "801a2257357486bc74f1a57b3b5329afed804e5b0b0c8712d5d4c9ad690505fe",
          "native_face_offset": [
            81,
            44
          ],
          "output_sha256": "d08286dce366a3675dbb094b32d19834b0e32a730faf6930c3e74bae930d9566"
        },
        {
          "resource": "adv_chara_004_01_07",
          "body": "adv_chara_004_01.png",
          "body_sha256": "5d8b60092117906b699d98ccabfc88344ea61f82e9b27a23bec1fa15d0cb65be",
          "face": "adv_chara_004_01_07.png",
          "face_sha256": "70378b0def42ea636a290d9f331afccb82c82df811d80c28f353d08ab5a3e44b",
          "native_face_offset": [
            194,
            74
          ],
          "output_sha256": "8b4b7fdf857db0be4aef3f3f9c0b6c9d78fb6645bdd9a2f6ffe24fc03501c010"
        },
        {
          "resource": "adv_chara_004_01_11",
          "body": "adv_chara_004_01.png",
          "body_sha256": "5d8b60092117906b699d98ccabfc88344ea61f82e9b27a23bec1fa15d0cb65be",
          "face": "adv_chara_004_01_11.png",
          "face_sha256": "cf841e0d8f869f74800eb312e1b32d7e4489456ebf5514ca43a0d753210cbbc2",
          "native_face_offset": [
            194,
            74
          ],
          "output_sha256": "119de115ceebee886b60f467a8e77f4348c22e2f264d757035d05a752c091d1a"
        }
      ],
      "coverage_effective_state_sha256": "3352a314e920fbb7cc5644ea3367c3eba28026fb8e2dbde7f4f07d04e6be16e8",
      "execution_record": "09 Audits and Manifests/T7S_B0100_B0159_EXECUTION_RECORD.md",
      "boundary": "Complete chapter-local text/native state plus selected static review; no authored choice or inline movie; no later-source semantic evidence; performed audio unreviewed."
    },
    "b0129_close_verification": {
      "operation": "T7S_B0129_CLOSE",
      "checked_at": "2026-09-26",
      "status": "PASS_BOUNDED_TEXT_NATIVE_AND_STATIC_REVIEW",
      "episode_ids": [
        "312202401",
        "312202402",
        "312202403"
      ],
      "source_bindings": [
        {
          "episode_id": "312202401",
          "script_id": "ing_102024_01.json__d01ed3abe79e0f67",
          "source_sha256": "692d1489341ebd56550c487f5dfb7e48629af6d3013bd7586488229c87a8c7a2",
          "decoded_sha256": "c562d78ecb71882139bc851d3eba3905cb719de6daebb24e43eee3f011c72c2b",
          "normalized_sha256": "8930e970a894ff7d44668ebb6a2c0551c452193a5f526dc52512dae7c70c0552",
          "structured_sha256": "8930e970a894ff7d44668ebb6a2c0551c452193a5f526dc52512dae7c70c0552",
          "pages": 50,
          "text_records": 46,
          "command_only_pages": 4,
          "voice_pages": 37,
          "native_pages_verified": 50
        },
        {
          "episode_id": "312202402",
          "script_id": "ing_102024_02.json__c15e16a5b0b79caf",
          "source_sha256": "28b5efbf71c215525910940d6bb97f55db922b0dd38315a333fee151debeb2ee",
          "decoded_sha256": "2fddc29f88eac1a851eeddf16f5d5053d0a43b534f7799b063fabd1f02fd71d1",
          "normalized_sha256": "053cfd2c9465edda628d6d235774c1bdf5b888dc96365a5aad07cf3a269bddb3",
          "structured_sha256": "053cfd2c9465edda628d6d235774c1bdf5b888dc96365a5aad07cf3a269bddb3",
          "pages": 30,
          "text_records": 28,
          "command_only_pages": 2,
          "voice_pages": 19,
          "native_pages_verified": 30
        },
        {
          "episode_id": "312202403",
          "script_id": "ing_102024_03.json__0633a80b29da464f",
          "source_sha256": "d485de991ca22b0b49e2a8851aea5170caaf3befd8b72cdc419d8938d0f8148d",
          "decoded_sha256": "a2e28c42d51594d09c1a0fdcb760734565435de381843c50ac4322bd63bd77cb",
          "normalized_sha256": "afd3371d99602801974cd2047ee626c043bb256b9d021bd4765a78bd9569cd32",
          "structured_sha256": "afd3371d99602801974cd2047ee626c043bb256b9d021bd4765a78bd9569cd32",
          "pages": 76,
          "text_records": 69,
          "command_only_pages": 7,
          "voice_pages": 48,
          "native_pages_verified": 76
        }
      ],
      "totals": {
        "pages": 156,
        "text_records": 143,
        "command_only_pages": 13,
        "voice_pages": 104,
        "visual_refs": 1057
      },
      "voice_count_basis": "Distinct dialogue log-order indexes with voice resource; title-only cues additional; no performed audio reviewed.",
      "native_packet_sha256": "e519460845b337fd1675551c851ba03545ef1fe47366adb26ef2480b7dc07898",
      "dialogue_packet_sha256": "6e516d536ac163207bb3a757fd433b59d05ddd76b87d02cf4c34aac2adcd33fb",
      "visual_assets": [
        {
          "resource": "adv_chara_131_01_03",
          "body": "adv_chara_131_01.png",
          "body_sha256": "1a9960701b204ddf456de522c3d4e51d2820a1870f85ee2e0bcb8edd55d7f867",
          "face": "adv_chara_131_01_03.png",
          "face_sha256": "57165766efb46361b4a3be3e6b8d573ca3cf5546082fa11ab4d5acf882c1dad8",
          "native_face_offset": [
            118,
            62
          ],
          "output_sha256": "7210555ae2077e689413a13884376a87b5b3a0c3294ee4c29badc384902a2113"
        },
        {
          "resource": "adv_chara_131_02_05",
          "body": "adv_chara_131_02.png",
          "body_sha256": "22a3c6a5b1a0300c526f23ea000bbb526cb9040148799821b8c87afd50ccc205",
          "face": "adv_chara_131_02_05.png",
          "face_sha256": "df808dbb731bfa3baba87a169542ceedba84546273ed7a91376ef4ec7f954077",
          "native_face_offset": [
            196,
            62
          ],
          "output_sha256": "53c919ed02f2c225f53374647a53e4218656c6b719fd30d59dd47a709ff05065"
        },
        {
          "resource": "adv_chara_131_03_01",
          "body": "adv_chara_131_03.png",
          "body_sha256": "f16bd315a199e715b87d5d964fcd500a617dd89ac7522bfbdfa1db682b66e9c8",
          "face": "adv_chara_131_03_01.png",
          "face_sha256": "5f8e3a343da14e30a6240eaeea142e4c3c117d8a50017cd0a069e245d852c453",
          "native_face_offset": [
            215,
            78
          ],
          "output_sha256": "9fae1b5331e38cd54906347f940e732418b5ba35730d133dcc695b518b6ef4ae"
        },
        {
          "resource": "adv_chara_132_01_02",
          "body": "adv_chara_132_01.png",
          "body_sha256": "0d49191320a09a7eee93f32d7af333bd6edcbf5ec4259ea97bca67053a4f43d0",
          "face": "adv_chara_132_01_02.png",
          "face_sha256": "35090ee6bc3090ed915f79362067b7ebaa71b9069293a4d72670beb4b7497173",
          "native_face_offset": [
            58,
            91
          ],
          "output_sha256": "ceffa056dc2f7e90ce04c709e42b8149e2509cb1be1254991dd1e821db27ea0d"
        },
        {
          "resource": "adv_chara_144_02_02",
          "body": "adv_chara_144_02.png",
          "body_sha256": "b3add9963f1235965c9608f3f10913deb12de7f6cd76d94940c7d600839a104a",
          "face": "adv_chara_144_02_02.png",
          "face_sha256": "13213e7481b0b8055c50327eb6110e1bb1ab545246f253652bfd9710fa5f0e69",
          "native_face_offset": [
            120,
            74
          ],
          "output_sha256": "4b2d07d9a4f86b236a4f6069b7e2ac6255a5efdd8b0be13c0e82c1b759907664"
        },
        {
          "resource": "adv_chara_144_04_03",
          "body": "adv_chara_144_04.png",
          "body_sha256": "cbf2b6248799f922091cef84bceaddb23951a53ec687c361fbd7f618473be1ac",
          "face": "adv_chara_144_04_03.png",
          "face_sha256": "cfe0357c389611232b092151abe79aca71ba0457e6ac7e8a793d86c52a774dd9",
          "native_face_offset": [
            166,
            74
          ],
          "output_sha256": "2d9f1247b50356f5ca089bec0dbba22c2ad8aa1540ed5424ca9d495b3912fe31"
        },
        {
          "resource": "adv_chara_137_04_04",
          "body": "adv_chara_137_04.png",
          "body_sha256": "29c45367f49be98c6e29dd11eb24744aa7f0a38f5fa616145f1815fa8fbe0dfa",
          "face": "adv_chara_137_04_04.png",
          "face_sha256": "dd72f37793248579a0ab1f8f725b814f511c16568329b3e0df39874b77b0b1a1",
          "native_face_offset": [
            280,
            62
          ],
          "output_sha256": "73b0f14ad8a49c543fa6a91776013fa51aa31f5a742725de85ea997e942039de"
        },
        {
          "resource": "adv_chara_136_04_04",
          "body": "adv_chara_136_04.png",
          "body_sha256": "309c9374be5a1914c4a11901f8b1e33377549f8e6a5557df3d9eae288db0205f",
          "face": "adv_chara_136_04_04.png",
          "face_sha256": "4e51cce479a375aade36da0959478843743b03e98e8074520d2c5394f0ff2183",
          "native_face_offset": [
            214,
            34
          ],
          "output_sha256": "06a4c1dfac6b507faaeb26fbedada7e6fd002f39c691db8262196cd18de3608f"
        }
      ],
      "coverage_effective_state_sha256": "db8e39787cbffe62d3433e00a6e96e4b5a7e6b854c7599353a4a193e47b306bb",
      "execution_record": "09 Audits and Manifests/T7S_B0100_B0159_EXECUTION_RECORD.md",
      "boundary": "Complete chapter-local text/native state plus selected static review; no authored choice or inline movie; no later-source semantic evidence; performed audio unreviewed."
    },
    "b0130_close_verification": {
      "operation": "T7S_B0130_CLOSE",
      "checked_at": "2026-09-26",
      "status": "PASS_BOUNDED_TEXT_NATIVE_AND_STATIC_REVIEW",
      "episode_ids": [
        "312202501",
        "312202502",
        "312202503"
      ],
      "source_bindings": [
        {
          "episode_id": "312202501",
          "script_id": "ing_102025_01.json__62547b6d86731171",
          "source_sha256": "4a6d90740dffeefa90b2a6e92cd1199cb81d446f90071508662c9100339bcd7b",
          "decoded_sha256": "16e3be4993864d95b459459ddc5a273da2d448c0b5fa4446104231635606b8d6",
          "normalized_sha256": "103224594ef6fcc09c9b8175d149fbc744327cedfa33e942d105e3a5a49c6580",
          "structured_sha256": "103224594ef6fcc09c9b8175d149fbc744327cedfa33e942d105e3a5a49c6580",
          "pages": 90,
          "text_records": 81,
          "command_only_pages": 9,
          "voice_pages": 44,
          "native_pages_verified": 90
        },
        {
          "episode_id": "312202502",
          "script_id": "ing_102025_02.json__5d048964744cf7cb",
          "source_sha256": "0eadb3ea6a986148381fa9e2bde130607f8ad02520afd8219a3309fb48a619f5",
          "decoded_sha256": "c54b22eb052ec6415c78a3b3ce3ebfbf9d1f12c030d10f3d903cb208cdcffe91",
          "normalized_sha256": "2e536919200e79ba6290f8af55fb8823f8b9c41c8bffcddbb8518dabb7005820",
          "structured_sha256": "2e536919200e79ba6290f8af55fb8823f8b9c41c8bffcddbb8518dabb7005820",
          "pages": 72,
          "text_records": 59,
          "command_only_pages": 13,
          "voice_pages": 38,
          "native_pages_verified": 72
        },
        {
          "episode_id": "312202503",
          "script_id": "ing_102025_03.json__afc290c8edbc4503",
          "source_sha256": "8b06cdbed3c91e92df971d23820e8ea7983408924ee6226fba1a968ec70afa7b",
          "decoded_sha256": "894b18cbebf727af44fc02d5351b135d1be1c890e03a79df53e1fb572beb7717",
          "normalized_sha256": "a34d4d23d7f443507dc25e9e40dda7f59edc0977599a2670a66bf410f320e00c",
          "structured_sha256": "a34d4d23d7f443507dc25e9e40dda7f59edc0977599a2670a66bf410f320e00c",
          "pages": 46,
          "text_records": 41,
          "command_only_pages": 5,
          "voice_pages": 24,
          "native_pages_verified": 46
        }
      ],
      "totals": {
        "pages": 208,
        "text_records": 181,
        "command_only_pages": 27,
        "voice_pages": 106,
        "visual_refs": 1645
      },
      "voice_count_basis": "Distinct dialogue log-order indexes with voice resource; title-only cues additional; no performed audio reviewed.",
      "native_packet_sha256": "0d472e4f45df27ceda3b28fc2c24178713dfece1f4ab171ecd3d5d76d6389358",
      "dialogue_packet_sha256": "26b829680e01b6b2b5411a717f5e36a6bbaf22bfb96c2c0d017dfb1306298922",
      "visual_assets": [
        {
          "resource": "adv_chara_132_01_01",
          "body": "adv_chara_132_01.png",
          "body_sha256": "0d49191320a09a7eee93f32d7af333bd6edcbf5ec4259ea97bca67053a4f43d0",
          "face": "adv_chara_132_01_01.png",
          "face_sha256": "ef98328fec3d962d011f35666c3595ffd10fc839c49a2825993359daea0761d0",
          "native_face_offset": [
            58,
            91
          ],
          "output_sha256": "b71fc3bb24fb825eb09e46085c6737d0c66ab4193c81765de9b7dc5ae09d6d76"
        },
        {
          "resource": "adv_chara_132_01_03",
          "body": "adv_chara_132_01.png",
          "body_sha256": "0d49191320a09a7eee93f32d7af333bd6edcbf5ec4259ea97bca67053a4f43d0",
          "face": "adv_chara_132_01_03.png",
          "face_sha256": "285d0d6fb39e136912ee01ef31a544fcec9a9f6824a843f96739f2c61a474f9c",
          "native_face_offset": [
            58,
            91
          ],
          "output_sha256": "2646fb9305ce9ffdd66039ccd9a1e630887f9adc37b6f9e2f8f293f1cce912c4"
        },
        {
          "resource": "adv_chara_132_01_04",
          "body": "adv_chara_132_01.png",
          "body_sha256": "0d49191320a09a7eee93f32d7af333bd6edcbf5ec4259ea97bca67053a4f43d0",
          "face": "adv_chara_132_01_04.png",
          "face_sha256": "e6a202f89ce5348f19c749b967b49fe82f0dd5d5da945456d32f5f403e501b4c",
          "native_face_offset": [
            58,
            91
          ],
          "output_sha256": "223381868542a533641a2c8d7b0a28a24304302f224ef3a3b66b641f55e0b81c"
        },
        {
          "resource": "adv_chara_007_02_03",
          "body": "adv_chara_007_02.png",
          "body_sha256": "92aaed359500dd8fd52b4cecb0a7e1f60b0e63e466320ae2036086461c29edc1",
          "face": "adv_chara_007_02_03.png",
          "face_sha256": "ded853be7a19257573d2b8f406146168a1a1a3a0a658b843608f3f86fd3d6862",
          "native_face_offset": [
            84,
            80
          ],
          "output_sha256": "615430d161b895f1a41493d4ba82d40f9836c6733d2fa871c34dbeb8f256d5d2"
        },
        {
          "resource": "adv_chara_007_02_05",
          "body": "adv_chara_007_02.png",
          "body_sha256": "92aaed359500dd8fd52b4cecb0a7e1f60b0e63e466320ae2036086461c29edc1",
          "face": "adv_chara_007_02_05.png",
          "face_sha256": "9aff5c77bd3d5faee6ebad2fd36f3e60b82129041938f1c259062835f09e12c7",
          "native_face_offset": [
            84,
            80
          ],
          "output_sha256": "e6158174227e8535f778cec55e2720da5098ec41e7dec95fc24e61040aba0249"
        },
        {
          "resource": "adv_chara_002_05_03",
          "body": "adv_chara_002_05.png",
          "body_sha256": "cb016340fb0d82c4b3f5e1c47bcd449550f680719951d70b9cbb10018be79a0b",
          "face": "adv_chara_002_05_03.png",
          "face_sha256": "bd26f12ebf371ca0f0dcbd14bd681b114b478139f5ac5204be8c1e92f7359027",
          "native_face_offset": [
            132,
            64
          ],
          "output_sha256": "9dbec5359d6fd116edc4d16bf92764c4eb13f21b9c73afff2f4d3b12070f1c88"
        },
        {
          "resource": "adv_chara_002_03_11",
          "body": "adv_chara_002_03.png",
          "body_sha256": "4bb14d813389b79055c4a24b5b3020e06bde9122d7b203b04a5489b358a7f1c7",
          "face": "adv_chara_002_03_11.png",
          "face_sha256": "a4f478e7621a53a877e16735445088d7fe40afde731cec0752906efe9e3b703a",
          "native_face_offset": [
            132,
            64
          ],
          "output_sha256": "dfdd6eb62836ea33189c85517d8aa2ecccd8eb77edfbdd7755d85828e77e6dcd"
        }
      ],
      "coverage_effective_state_sha256": "3056025fd7c7afddc8f95beeb31322771d72d10795ef6fa64d34f28bd0e61acf",
      "execution_record": "09 Audits and Manifests/T7S_B0100_B0159_EXECUTION_RECORD.md",
      "boundary": "Complete chapter-local text/native state plus selected static review; no authored choice or inline movie; no later-source semantic evidence; performed audio unreviewed."
    },
    "b0131_close_verification": {
      "operation": "T7S_B0131_CLOSE",
      "checked_at": "2026-09-26",
      "status": "PASS_BOUNDED_TEXT_NATIVE_AND_STATIC_REVIEW",
      "episode_ids": [
        "312202601",
        "312202602",
        "312202603"
      ],
      "source_bindings": [
        {
          "episode_id": "312202601",
          "script_id": "ing_102026_01.json__6250a1ce2a88b338",
          "source_sha256": "606c527b0e8f2b089310af75fe7aa13fbfaf133a4f02e2c1483b270076c6f13f",
          "decoded_sha256": "96fa3fde995f4ebec7a4f16c408ec4dd8fa1f34cda2f74f24e95a210d70171fd",
          "normalized_sha256": "95f2675ff5c672270e058153ea46c7d6aee5ce3d0efbca80bc6fd96a535f42c3",
          "structured_sha256": "95f2675ff5c672270e058153ea46c7d6aee5ce3d0efbca80bc6fd96a535f42c3",
          "pages": 54,
          "text_records": 41,
          "command_only_pages": 13,
          "voice_pages": 34,
          "native_pages_verified": 54
        },
        {
          "episode_id": "312202602",
          "script_id": "ing_102026_02.json__9375d418acb0d8ff",
          "source_sha256": "30d7ef0dd28c4b2cd9ab8a745ec97cd39ff247ace8b47805561ae2b9ebd872f6",
          "decoded_sha256": "4841fd2226555a9270492350a498e896002b0da4adec3a3b70dd36fde5c12c7c",
          "normalized_sha256": "5d0e2ead332c6d821ef72dd6418edb2834603b07f70381c5a1995f849f3109ed",
          "structured_sha256": "5d0e2ead332c6d821ef72dd6418edb2834603b07f70381c5a1995f849f3109ed",
          "pages": 76,
          "text_records": 68,
          "command_only_pages": 8,
          "voice_pages": 60,
          "native_pages_verified": 76
        },
        {
          "episode_id": "312202603",
          "script_id": "ing_102026_03.json__8c300ade23188b9b",
          "source_sha256": "e6996c9ed8ae311ca445b0907eb60c92b970e865b899cd4c243c5024defe6006",
          "decoded_sha256": "49a12f2d9466db03ce2f14795687200a51622e5d58f9437b9e0c9bd32356cc1a",
          "normalized_sha256": "d4025e1787b727ea4a3a3098d481fc02bdfb7c6afc8615e78f9e6410c964872a",
          "structured_sha256": "d4025e1787b727ea4a3a3098d481fc02bdfb7c6afc8615e78f9e6410c964872a",
          "pages": 58,
          "text_records": 50,
          "command_only_pages": 8,
          "voice_pages": 46,
          "native_pages_verified": 58
        }
      ],
      "totals": {
        "pages": 188,
        "text_records": 159,
        "command_only_pages": 29,
        "voice_pages": 140,
        "visual_refs": 1211
      },
      "voice_count_basis": "Distinct dialogue log-order indexes with voice resource; title-only cues additional; no performed audio reviewed.",
      "native_packet_sha256": "091ccf8a9b4483c7a70cd831bdf489b611d4ba12474a14df89a3ab5d8e1173eb",
      "dialogue_packet_sha256": "8f9fc294630c89c57ec2245708754c9ed05221bbf592a45fc405ddfd22d6ee9a",
      "visual_assets": [
        {
          "resource": "adv_chara_133_01_02",
          "body": "adv_chara_133_01.png",
          "body_sha256": "ee3e5303e0e6ee798401ba7e6e276138169525925f4058c03f1d01ddd73fa7e5",
          "face": "adv_chara_133_01_02.png",
          "face_sha256": "651d1c98afbc3978bc392857a996b74675d6f8e5daed3b506d0a8d4b7d21edfa",
          "native_face_offset": [
            142,
            66
          ],
          "output_sha256": "0ce587628d11ea9fb71c8a40d53445995693764b47b94e2e11622c41cf8d0bdf"
        },
        {
          "resource": "adv_chara_133_02_07",
          "body": "adv_chara_133_02.png",
          "body_sha256": "5754d2a958e1d7526c9e9b1b32db1346ecc4fbaf6bfc428016f5049c461d70fd",
          "face": "adv_chara_133_02_07.png",
          "face_sha256": "2d0906fb56e02cee45fd0b563b5c4984695e0ae3589d48b2353a886049574930",
          "native_face_offset": [
            76,
            60
          ],
          "output_sha256": "b33682144a4588c33efcc72ff12bbc794da6a03f02f1dd37454c54327e69f309"
        },
        {
          "resource": "adv_chara_133_01_03",
          "body": "adv_chara_133_01.png",
          "body_sha256": "ee3e5303e0e6ee798401ba7e6e276138169525925f4058c03f1d01ddd73fa7e5",
          "face": "adv_chara_133_01_03.png",
          "face_sha256": "d5c6e26da4ac5dd45ad6c8df4bee8161cb1f58c93ae06038b745b09603d8cacd",
          "native_face_offset": [
            142,
            66
          ],
          "output_sha256": "3a4d47c0b3943eb6f3cb819a278619cd88e251f3044c68d759c0edd84140d48d"
        },
        {
          "resource": "adv_chara_006_01_12",
          "body": "adv_chara_006_01.png",
          "body_sha256": "d40ded643748164bb05d319c4a3889a41f99d102a3fcfeb60675b59529a6c392",
          "face": "adv_chara_006_01_12.png",
          "face_sha256": "f36e7c9ec3fda34be7c6f8700fad84e397ddf74b2b2951b500d59366a7adf0d1",
          "native_face_offset": [
            134,
            91
          ],
          "output_sha256": "fe6f50beb87a906463a9bae1dd63d8b4faf704cb22159541330f9318a30fb68d"
        },
        {
          "resource": "adv_chara_006_01_03",
          "body": "adv_chara_006_01.png",
          "body_sha256": "d40ded643748164bb05d319c4a3889a41f99d102a3fcfeb60675b59529a6c392",
          "face": "adv_chara_006_01_03.png",
          "face_sha256": "983e2f580f3daeb763f26c7d1cab33b2916aa623cb657c3cf93f6762ad00a2a4",
          "native_face_offset": [
            134,
            91
          ],
          "output_sha256": "ffc7695c83f20c6244c9343974d642c34c9fe8acb227011be71a330bc7ccadde"
        },
        {
          "resource": "adv_chara_127_02_01",
          "body": "adv_chara_127_02.png",
          "body_sha256": "eca3cd36fc801dcf1e93e85ffaa806839d28ae78ee599b6848dd5d5bb0c64074",
          "face": "adv_chara_127_02_01.png",
          "face_sha256": "1cc62adbbe97ae4da7e14f9818fd0e2780ca9941ec2184379e740cf07d0a28d0",
          "native_face_offset": [
            176,
            108
          ],
          "output_sha256": "b9d64f08b9cdd22bebd57e5907fa0b5d62213057b3a515a4a53218e7e7d752c6"
        },
        {
          "resource": "adv_chara_147_01_01",
          "body": "adv_chara_147_01.png",
          "body_sha256": "df3ba4aa9a0969ae5dbb2f3d8b7e26c938ab1294692d595b12c3090fa8a47982",
          "face": "adv_chara_147_01_01.png",
          "face_sha256": "c97bdaea12f5d9f9bfb81e9ff25f5857cad50a11eb4fa75f0efd392c6f2c6874",
          "native_face_offset": [
            209,
            62
          ],
          "output_sha256": "08c669b14f3c489b3460361737a7d4d1e93fadd065a9f55b874701326f3956de"
        },
        {
          "resource": "adv_chara_002_03_02",
          "body": "adv_chara_002_03.png",
          "body_sha256": "4bb14d813389b79055c4a24b5b3020e06bde9122d7b203b04a5489b358a7f1c7",
          "face": "adv_chara_002_03_02.png",
          "face_sha256": "b3dd46d4ffd6aaf7b538ed8be9d5b749b66f5245e46f784ba4c1d47b0c5515e8",
          "native_face_offset": [
            132,
            64
          ],
          "output_sha256": "52041a1326e1ce2e9c79167904fc5dbec69df3012b00bb3c26657b14beb45e35"
        }
      ],
      "coverage_effective_state_sha256": "4571c588c1c0c35ac7ac56fc90cdfefbc814c0ba9914f194aabc63de654b09c4",
      "execution_record": "09 Audits and Manifests/T7S_B0100_B0159_EXECUTION_RECORD.md",
      "boundary": "Complete chapter-local text/native state plus selected static review; no authored choice or inline movie; no later-source semantic evidence; performed audio unreviewed."
    },
    "b0132_close_verification": {
      "operation": "T7S_B0132_CLOSE",
      "checked_at": "2026-09-26",
      "status": "PASS_BOUNDED_TEXT_NATIVE_AND_STATIC_REVIEW",
      "episode_ids": [
        "312202701",
        "312202702",
        "312202703"
      ],
      "source_bindings": [
        {
          "episode_id": "312202701",
          "script_id": "ing_102027_01.json__342025c83594abd7",
          "source_sha256": "909d648d8a4f68ab92e3c3d9b8dd483a8cc4cda4700fd844ebe8baf60ba3af16",
          "decoded_sha256": "10e65a7af5582e824262a5d9c92a1c561cb6da3e62486d0fb7f4e53bb22433b1",
          "normalized_sha256": "83b75c982d21baecfcbc5c76ffa5b1e2e623a2fc336bdc14e21e7796f39ef27d",
          "structured_sha256": "83b75c982d21baecfcbc5c76ffa5b1e2e623a2fc336bdc14e21e7796f39ef27d",
          "pages": 63,
          "text_records": 60,
          "command_only_pages": 3,
          "voice_pages": 46,
          "native_pages_verified": 63
        },
        {
          "episode_id": "312202702",
          "script_id": "ing_102027_02.json__52e6d44621436223",
          "source_sha256": "925bd333bfb5fa76c0d974ab8dce48a51abe4690ef128fe23b2176167c4dadf2",
          "decoded_sha256": "0f6f23b48f1ba506eed22027ec94535abca9ff68568d76f542453fbab7f00995",
          "normalized_sha256": "714ceedc1bf715f9db54c7dc1ce7dc9f1cb1dd5932145bc8ef489fc68d77cb73",
          "structured_sha256": "714ceedc1bf715f9db54c7dc1ce7dc9f1cb1dd5932145bc8ef489fc68d77cb73",
          "pages": 49,
          "text_records": 46,
          "command_only_pages": 3,
          "voice_pages": 46,
          "native_pages_verified": 49
        },
        {
          "episode_id": "312202703",
          "script_id": "ing_102027_03.json__a728ed4c63113063",
          "source_sha256": "ae2ed3b9bbe9fef786a62a060d319e26561eca85a214f44862d9bd9911fbecc3",
          "decoded_sha256": "7cc4ad6f5095c9543d7639a4f80f9ff64ff06e51da6677417b1f11bad8f4640f",
          "normalized_sha256": "094e6511c18903afbece9f913e69a7db6ca60d92ac41245ec28a7152581b9bf1",
          "structured_sha256": "094e6511c18903afbece9f913e69a7db6ca60d92ac41245ec28a7152581b9bf1",
          "pages": 81,
          "text_records": 73,
          "command_only_pages": 8,
          "voice_pages": 68,
          "native_pages_verified": 81
        }
      ],
      "totals": {
        "pages": 193,
        "text_records": 179,
        "command_only_pages": 14,
        "voice_pages": 160,
        "visual_refs": 1777
      },
      "voice_count_basis": "Distinct dialogue log-order indexes with voice resource; title-only cues additional; no performed audio reviewed.",
      "native_packet_sha256": "a12fbfbf7d3418f5839c8058d6f73809316784bd102b44c76c842056662be5f9",
      "dialogue_packet_sha256": "81357bb131dda8dde1f9b2ec28ec86b06b01753d1859455a8dbff3eb78028a90",
      "visual_assets": [
        {
          "resource": "adv_chara_134_01_01",
          "body": "adv_chara_134_01.png",
          "body_sha256": "59e54f3c7e045ef97681badac43daacab7c317c2456705c43ecd6e9021fcf960",
          "face": "adv_chara_134_01_01.png",
          "face_sha256": "fea863297cb5f0cc69f7afc53507625eb68936a5fd4e8d8a38edcf2b8dad8d11",
          "native_face_offset": [
            96,
            67
          ],
          "output_sha256": "a363b198ca80ebfe8335cd699850f068582b52cd7ebfff6f9bd1247a7de42a79"
        },
        {
          "resource": "adv_chara_134_02_05",
          "body": "adv_chara_134_02.png",
          "body_sha256": "e0be08f5af4bfbbafbe28cabe5b5e022104254a3ed1ac1a838b556d0c55c645d",
          "face": "adv_chara_134_02_05.png",
          "face_sha256": "bb2b28960232e11b7d655f195d9fd82d4fba447b8b628f1767d4617b749eaddb",
          "native_face_offset": [
            96,
            67
          ],
          "output_sha256": "3dd5e38b567b39a0c9ccb57ad8d68970bcdb7defd91c2cdf14fc74c8678c450f"
        },
        {
          "resource": "adv_chara_127_03_01",
          "body": "adv_chara_127_03.png",
          "body_sha256": "d8ba7fee4f73bcf0fae28261f7ee22af84a8e7c8185f6944ea1c16662865e79e",
          "face": "adv_chara_127_03_01.png",
          "face_sha256": "8589c4b895fe4fe0ac99483b5f026ec58a261aafd34ee9af803d30814e72554c",
          "native_face_offset": [
            82,
            108
          ],
          "output_sha256": "a0e9a5be981f3e658b32dc8a594d1125fa863f0cef3b8a8e3ca48e21cb265478"
        },
        {
          "resource": "adv_chara_008_06_01",
          "body": "adv_chara_008_06.png",
          "body_sha256": "c1ae77093d7a887b00206ee320c811e66626baebcd0e9f814264577b8b1805aa",
          "face": "adv_chara_008_06_01.png",
          "face_sha256": "ab07404b000fe13a5ad7054c4c7f80ad90fd2dade77d8db6a557e7a1cccab000",
          "native_face_offset": [
            166,
            84
          ],
          "output_sha256": "c7bf4c30a44693917c078240dce9d6dacdc50a6fb24be4621989267ba0c644f3"
        },
        {
          "resource": "adv_chara_133_04_01",
          "body": "adv_chara_133_04.png",
          "body_sha256": "3fc5ebb3ee6e7ecea1f2e2e2c69eae305d741afe30396015292e0aac6b61f87a",
          "face": "adv_chara_133_04_01.png",
          "face_sha256": "5519673fa044697038d1539ec880cbdf09753e111c70871c8ec26bca5a62fb4f",
          "native_face_offset": [
            142,
            66
          ],
          "output_sha256": "b9f9dc4c8746e2830b51fbf3130188710ece60853dc775fc825c8df9f6a30590"
        },
        {
          "resource": "adv_chara_137_03_05",
          "body": "adv_chara_137_03.png",
          "body_sha256": "87b04dee6b94110b1c553d6f01d5e9ca0e4cc88b98fc9a97b7afa761ec14e352",
          "face": "adv_chara_137_03_05.png",
          "face_sha256": "4048a179e04f1f46b6ad9cf7910a52685812b0d3b03ea98ffb906c257b721101",
          "native_face_offset": [
            104,
            62
          ],
          "output_sha256": "fc025348847d91256312822007af310f2a54cb43aab7435e357ec28a0f7ea203"
        },
        {
          "resource": "adv_chara_002_01_01",
          "body": "adv_chara_002_01.png",
          "body_sha256": "9afeb35f4f6391ea896d756d3f0cd3f2af54bb96a38199155349ee4e7444ca0c",
          "face": "adv_chara_002_01_01.png",
          "face_sha256": "ba998f335d676a6d263949b93597743a7ece82d280d93c7c12e7b524a4b29ee9",
          "native_face_offset": [
            132,
            64
          ],
          "output_sha256": "39f2704157d7045e1788989365e64fbbe1f333f2ab3ac942fe3906b3aaabc5c2"
        }
      ],
      "coverage_effective_state_sha256": "1a0a7c3f21cb635f53370c176119c33f0daca91814f2ba61697f304946a407ee",
      "execution_record": "09 Audits and Manifests/T7S_B0100_B0159_EXECUTION_RECORD.md",
      "boundary": "Complete chapter-local text/native state plus selected static review; no authored choice or inline movie; no later-source semantic evidence; performed audio unreviewed."
    },
    "b0133_close_verification": {
      "operation": "T7S_B0133_CLOSE",
      "checked_at": "2026-09-26",
      "status": "PASS_BOUNDED_TEXT_NATIVE_AND_STATIC_REVIEW",
      "episode_ids": [
        "312202801",
        "312202802",
        "312202803"
      ],
      "source_bindings": [
        {
          "episode_id": "312202801",
          "script_id": "ing_102028_01.json__51f0b55864ab8f34",
          "source_sha256": "1dd7c027c41c8e5a3556b1a38058ee5edd983984d9b301572ba3e1968c2f6e03",
          "decoded_sha256": "687b18b5008de3ecb64712bf5d4a4d484ff2260d2f97f263abe40b0bd133e952",
          "normalized_sha256": "b44ec86c106c840ec4950634d42944a205f09acd07363ca4fa959f67d42b3954",
          "structured_sha256": "b44ec86c106c840ec4950634d42944a205f09acd07363ca4fa959f67d42b3954",
          "pages": 56,
          "text_records": 53,
          "command_only_pages": 3,
          "voice_pages": 35,
          "native_pages_verified": 56
        },
        {
          "episode_id": "312202802",
          "script_id": "ing_102028_02.json__ae2cf71a104f3f22",
          "source_sha256": "f48011c4f945595458d5fcd4ea199c4c9b6b879ba3834748120fcd6a887bbe11",
          "decoded_sha256": "42348ce795c52fd412b8f7e897d8389d9d017412ee80b4dea866bcf2b71a8f49",
          "normalized_sha256": "18f714589d657356a49e0847c855428de412cfc43d15fab7720287ef200112e7",
          "structured_sha256": "18f714589d657356a49e0847c855428de412cfc43d15fab7720287ef200112e7",
          "pages": 34,
          "text_records": 31,
          "command_only_pages": 3,
          "voice_pages": 16,
          "native_pages_verified": 34
        },
        {
          "episode_id": "312202803",
          "script_id": "ing_102028_03.json__6a94777f7e9e9904",
          "source_sha256": "e0020ab16f67dea872dfe56b7750da7be7a9b6b5e4c90fd0a65ba4fdd72d31d3",
          "decoded_sha256": "1ee0729ca7b8a4e31ef65cd4534566a169439b928d2fc5c1204dadbcbcc0cf65",
          "normalized_sha256": "b4e1881dcbe2333263adc60d5cd16d1e23324ba86237381a9367ab3e1f7e84a4",
          "structured_sha256": "b4e1881dcbe2333263adc60d5cd16d1e23324ba86237381a9367ab3e1f7e84a4",
          "pages": 82,
          "text_records": 78,
          "command_only_pages": 4,
          "voice_pages": 53,
          "native_pages_verified": 82
        }
      ],
      "totals": {
        "pages": 172,
        "text_records": 162,
        "command_only_pages": 10,
        "voice_pages": 104,
        "visual_refs": 1341
      },
      "voice_count_basis": "Distinct dialogue log-order indexes with voice resource; title-only cues additional; no performed audio reviewed.",
      "native_packet_sha256": "d4aee3b28663890edb6f56c679fb6f27ecfce93eb57627fb3b457a5b8fa8ba4a",
      "dialogue_packet_sha256": "f52fc1b9f3d666f92d0de4e828b9b68c3a8623c66f905966418f5e7b22335e62",
      "visual_assets": [
        {
          "resource": "adv_chara_135_01_01",
          "body": "adv_chara_135_01.png",
          "body_sha256": "cd24c39770bdb5d8134998d731217d541cd18c12c966c277618c7d27a07e76bd",
          "face": "adv_chara_135_01_01.png",
          "face_sha256": "9d2702cea14d0a7dee334e96e4233017924d2e0454a1a8c61730b2ef1840a653",
          "native_face_offset": [
            174,
            84
          ],
          "output_sha256": "364162522dfd7533ddb67ca2f783d803ec68e59f56779e64313b181e65930e61"
        },
        {
          "resource": "adv_chara_135_01_03",
          "body": "adv_chara_135_01.png",
          "body_sha256": "cd24c39770bdb5d8134998d731217d541cd18c12c966c277618c7d27a07e76bd",
          "face": "adv_chara_135_01_03.png",
          "face_sha256": "468e25bc84e06594996cf6d3bb63953e46d2aa3e0c0a498470ac623b1634c6bd",
          "native_face_offset": [
            174,
            84
          ],
          "output_sha256": "10119bde3a894a6fd74bded90b47cf64da549405e7a5efbb43182bf42e726a76"
        },
        {
          "resource": "adv_chara_126_01_01",
          "body": "adv_chara_126_01.png",
          "body_sha256": "00ce923f755ee73078d66152d8d3d3bc5b0189a1d61173875e3443796d80e987",
          "face": "adv_chara_126_01_01.png",
          "face_sha256": "774420432ab233a6519985dfa12e34e197a97a5680a978723b6dcc7b10a7395e",
          "native_face_offset": [
            67,
            59
          ],
          "output_sha256": "49932c912ca5a89570312410bc57ba9f42ed947e5576332cefa5d7e8e0ba39b5"
        },
        {
          "resource": "adv_chara_129_02_04",
          "body": "adv_chara_129_02.png",
          "body_sha256": "3b3561b12d9e97b5c8b46bce7ee758f05f1b08e6aed6a705210707efa3573371",
          "face": "adv_chara_129_02_04.png",
          "face_sha256": "562d109777d01e8ddc270f18b9af4726bdd8b3c93c71d454eba823b1716edb25",
          "native_face_offset": [
            128,
            72
          ],
          "output_sha256": "ca3972767d3a93245a6bb22450791ce059d6d0d3133e641ea74e3548b8fc9bfb"
        },
        {
          "resource": "adv_chara_134_01_01",
          "body": "adv_chara_134_01.png",
          "body_sha256": "59e54f3c7e045ef97681badac43daacab7c317c2456705c43ecd6e9021fcf960",
          "face": "adv_chara_134_01_01.png",
          "face_sha256": "fea863297cb5f0cc69f7afc53507625eb68936a5fd4e8d8a38edcf2b8dad8d11",
          "native_face_offset": [
            96,
            67
          ],
          "output_sha256": "a363b198ca80ebfe8335cd699850f068582b52cd7ebfff6f9bd1247a7de42a79"
        },
        {
          "resource": "adv_chara_138_01_04",
          "body": "adv_chara_138_01.png",
          "body_sha256": "cd5b6d322e4dc013f5c79a4449e8d5e7a89f2f4238ad257e6710dc02b016c4e7",
          "face": "adv_chara_138_01_04.png",
          "face_sha256": "65fca530051887adb22a9bf679e67d260c0e0fa6dc0452767d440cb6446301ae",
          "native_face_offset": [
            110,
            91
          ],
          "output_sha256": "3b74baa13dabdc867ce7a9279237f1f2c818613cec1827d41b0965743e62222f"
        }
      ],
      "coverage_effective_state_sha256": "9de4a04b75b20da3c39b11015642c6ee04d6a0ab9f15d99d7afa6810a13e9f39",
      "execution_record": "09 Audits and Manifests/T7S_B0100_B0159_EXECUTION_RECORD.md",
      "boundary": "Complete chapter-local text/native state plus selected static review; no authored choice or inline movie; no later-source semantic evidence; performed audio unreviewed."
    },
    "b0134_close_verification": {
      "operation": "T7S_B0134_CLOSE",
      "checked_at": "2026-09-26",
      "status": "PASS_BOUNDED_TEXT_NATIVE_AND_STATIC_REVIEW",
      "episode_ids": [
        "312202901",
        "312202902",
        "312202903"
      ],
      "source_bindings": [
        {
          "episode_id": "312202901",
          "script_id": "ing_102029_01.json__dca94eb54425b40b",
          "source_sha256": "bbc4d8b56094f2c5e1774d814cfb00d542a1b1d3903f7ccb09d68b7fe3ba8cc6",
          "decoded_sha256": "5e92e41257d1ceeaace3392be4eb9ddc5c13d35e1985330e98c67db8e260cb86",
          "normalized_sha256": "30162aa0713b832316d8ebb6667f179f05a67cb87a731568e16f42e68de07c27",
          "structured_sha256": "30162aa0713b832316d8ebb6667f179f05a67cb87a731568e16f42e68de07c27",
          "pages": 32,
          "text_records": 25,
          "command_only_pages": 7,
          "voice_pages": 19,
          "native_pages_verified": 32
        },
        {
          "episode_id": "312202902",
          "script_id": "ing_102029_02.json__5f55898827135cde",
          "source_sha256": "3fa671458f401b95544e15f0311f636bf7aa065edd99bef5571c3896272723c6",
          "decoded_sha256": "68038824f6903292968846f4292b92a63380ef0f62f9d0009da512abdee8f883",
          "normalized_sha256": "8b142a96c90fe07cf056bca42233db0b6ebb099ac4aaad32feffe369a7d86ee0",
          "structured_sha256": "8b142a96c90fe07cf056bca42233db0b6ebb099ac4aaad32feffe369a7d86ee0",
          "pages": 64,
          "text_records": 51,
          "command_only_pages": 13,
          "voice_pages": 45,
          "native_pages_verified": 64
        },
        {
          "episode_id": "312202903",
          "script_id": "ing_102029_03.json__efb270938a946f78",
          "source_sha256": "d41245ac43898b8c31bcf511c0022d045148cd0183e4f43b80537d106d71653b",
          "decoded_sha256": "61a65d7752a764d61786250bf4497f2017e0927ba3615e441f22c853b3817d08",
          "normalized_sha256": "4c6e09d6a86f88acc5a4f1fa90558d13bdc39cc4b11fadce37a4c6f23db97d3f",
          "structured_sha256": "4c6e09d6a86f88acc5a4f1fa90558d13bdc39cc4b11fadce37a4c6f23db97d3f",
          "pages": 78,
          "text_records": 69,
          "command_only_pages": 9,
          "voice_pages": 47,
          "native_pages_verified": 78
        }
      ],
      "totals": {
        "pages": 174,
        "text_records": 145,
        "command_only_pages": 29,
        "voice_pages": 111,
        "visual_refs": 2028
      },
      "voice_count_basis": "Distinct dialogue log-order indexes with voice resource; title-only cues additional; no performed audio reviewed.",
      "native_packet_sha256": "f4f02fd25174cb9c17fa4cde3da6ee48bd5c46dc8b156c478972a85cb6650215",
      "dialogue_packet_sha256": "06d7134713dd056c861aeb0d2a40084a41e09b8f38349033656a5b1b015bab7a",
      "visual_assets": [
        {
          "resource": "adv_chara_003_06_15",
          "body": "adv_chara_003_06.png",
          "body_sha256": "a41fb44cc61027bc6f9f0a44fe7ff477be4bd04e6e671c3d77d6efbfdf7fc55e",
          "face": "adv_chara_003_06_15.png",
          "face_sha256": "4b6716a676b81f503908ed04fd14fec27e0c31072e2b32e124979ff107f94266",
          "native_face_offset": [
            98,
            92
          ],
          "output_sha256": "00becbe383c1a451a1dd7c4963e9213ffcd24ed00107479dd8404001daa87a0e"
        },
        {
          "resource": "adv_chara_120_01_02",
          "body": "adv_chara_120_01.png",
          "body_sha256": "02b5a8e89ee8f85d06aea585dd4fa249ad9f2cb305e1f0446dd8891072ef682b",
          "face": "adv_chara_120_01_02.png",
          "face_sha256": "f3f8ab0f32e86b488a29c8e943a0244e23307639a50b634970a4e2ccd2707b6e",
          "native_face_offset": [
            92,
            78
          ],
          "output_sha256": "04d53eb6389e7f72ea812d1fa5685ef1dfe93dbbef6f1e12319c0f8b99e35976"
        },
        {
          "resource": "adv_chara_120_03_04",
          "body": "adv_chara_120_03.png",
          "body_sha256": "7e0c70cbe5f0e63e7164690bd1fb5b9c1ba20e86c0b9f8cf560ecf0ab01a16bb",
          "face": "adv_chara_120_03_04.png",
          "face_sha256": "ab96f0753120a968b5d582d0121122a5931bc487ca8da7028854dc16dc773002",
          "native_face_offset": [
            92,
            78
          ],
          "output_sha256": "216cb4108ce1888268a6a22b0276f9a19f3d1a9aa09f7de319a75ccce5504c7e"
        },
        {
          "resource": "adv_chara_136_01_01",
          "body": "adv_chara_136_01.png",
          "body_sha256": "200a9e40c75a925f2991b38854443b5b026c20e01c466aef28b79b3904400bd3",
          "face": "adv_chara_136_01_01.png",
          "face_sha256": "811e413aa7ef6a7078bcb69a5a7ef73dfa67a800303c20299fe590a8214f2658",
          "native_face_offset": [
            115,
            34
          ],
          "output_sha256": "31d25641e42954c7cdb0be726d9333ce831a698bacc13ba4cc9c0c39a8d94069"
        },
        {
          "resource": "adv_chara_136_03_04",
          "body": "adv_chara_136_03.png",
          "body_sha256": "5adaa504d8137ded922f1cff73c9a24998f3ea8b693e2304a51aab446316ac2f",
          "face": "adv_chara_136_03_04.png",
          "face_sha256": "4aae3ba887ea1132bcf2b44619846ed8af0b52f1353fa412deb3312cd4a06962",
          "native_face_offset": [
            115,
            82
          ],
          "output_sha256": "b5ff0fea7192eb5c66f41d4896be76eb18346e58fa2aa97359e4076924b7dc82"
        }
      ],
      "coverage_effective_state_sha256": "f183e3f67d172ca866059293296484782849a71f11ced8a2ef226e7490f2376e",
      "execution_record": "09 Audits and Manifests/T7S_B0100_B0159_EXECUTION_RECORD.md",
      "boundary": "Complete chapter-local text/native state plus selected static review; no authored choice or inline movie; no later-source semantic evidence; performed audio unreviewed."
    },
    "b0135_close_verification": {
      "operation": "T7S_B0135_CLOSE",
      "checked_at": "2026-09-26",
      "status": "PASS_BOUNDED_TEXT_NATIVE_AND_STATIC_REVIEW",
      "episode_ids": [
        "312203001",
        "312203002",
        "312203003"
      ],
      "source_bindings": [
        {
          "episode_id": "312203001",
          "script_id": "ing_102030_01.json__68950b2d6526cd4b",
          "source_sha256": "25abfe1ed7cf64ba91deba57cb1acb47a2a39b089dcf57f7bcb846a42dc8d8f9",
          "decoded_sha256": "8b5506874785e740a1ccbf046cd5151cb9ba5a6493603ed1b4a1c6a878d4b957",
          "normalized_sha256": "20c1501eae616f90821de6e280a041e1a8fc00b6671144f95cf3ba71365885f3",
          "structured_sha256": "20c1501eae616f90821de6e280a041e1a8fc00b6671144f95cf3ba71365885f3",
          "pages": 43,
          "text_records": 40,
          "command_only_pages": 3,
          "voice_pages": 32,
          "native_pages_verified": 43
        },
        {
          "episode_id": "312203002",
          "script_id": "ing_102030_02.json__49dd300de1ed1024",
          "source_sha256": "a412dc0d2de3ed42e8298364c1a36fde10b8e03b07c81642eb8cb0fe3a0f8a29",
          "decoded_sha256": "be278f5d2ba486fd1b464fdc1de068bcde7d14ec612a3182306e95cc20d211aa",
          "normalized_sha256": "bf6ab5997f2d51c3d17829c6d6017b93d5bcd79fe07f185f3c64ee11e2982148",
          "structured_sha256": "bf6ab5997f2d51c3d17829c6d6017b93d5bcd79fe07f185f3c64ee11e2982148",
          "pages": 41,
          "text_records": 37,
          "command_only_pages": 4,
          "voice_pages": 28,
          "native_pages_verified": 41
        },
        {
          "episode_id": "312203003",
          "script_id": "ing_102030_03.json__51b7768a5feec6dc",
          "source_sha256": "c442583f1db6e8dcb6ba921be927bc6fc21004cc8d03bf650e0e8d8e312e50e6",
          "decoded_sha256": "e3a283b962275a785ef8266f5ad1bbabb0c2f859b4c9c505e9742d8023d55571",
          "normalized_sha256": "e4d812b72960c10656fbcd57aedec5bdd806c6cae13eddded4013be072a74efc",
          "structured_sha256": "e4d812b72960c10656fbcd57aedec5bdd806c6cae13eddded4013be072a74efc",
          "pages": 79,
          "text_records": 69,
          "command_only_pages": 10,
          "voice_pages": 56,
          "native_pages_verified": 79
        }
      ],
      "totals": {
        "pages": 163,
        "text_records": 146,
        "command_only_pages": 17,
        "voice_pages": 116,
        "visual_refs": 1099
      },
      "voice_count_basis": "Distinct dialogue log-order indexes with voice resource; title-only cues additional; no performed audio reviewed.",
      "native_packet_sha256": "0742a62f186c4d8349217cd0c0ec6c6049d2ecbd01c2414194aa2c6b3604e23e",
      "dialogue_packet_sha256": "f1af314e75b3ac3121127c230dd575b6fb77e30c1f7e259b5963e63fe503d2b5",
      "visual_assets": [
        {
          "resource": "adv_chara_137_01_02",
          "body": "adv_chara_137_01.png",
          "body_sha256": "8da617d5736a9e233312322d4f1a1edff77c9f764832a0665ddc3d9adb9610ba",
          "face": "adv_chara_137_01_02.png",
          "face_sha256": "9a6ebbf7e2e28b54160372c10ad30d7ef44bb186000e0e32b9eb47919f12435f",
          "native_face_offset": [
            104,
            62
          ],
          "output_sha256": "b38990d4f7a133b0d2a6cda04e8eb61d23364b768b24df8ea24d7cf72cf4d7b2"
        },
        {
          "resource": "adv_chara_137_02_05",
          "body": "adv_chara_137_02.png",
          "body_sha256": "79615d0c821b7f341103cf9b91859459191552d42e7971d3b8030ab5131b9169",
          "face": "adv_chara_137_02_05.png",
          "face_sha256": "69afe31efd8efb36e35ac5fd1c58fa8fabee0d4726f93202cb8b08f73983b137",
          "native_face_offset": [
            104,
            62
          ],
          "output_sha256": "c48fe00165f63330fceefa0cc5a123e264344eeae4454160514590445ad56876"
        },
        {
          "resource": "adv_chara_006_01_04",
          "body": "adv_chara_006_01.png",
          "body_sha256": "d40ded643748164bb05d319c4a3889a41f99d102a3fcfeb60675b59529a6c392",
          "face": "adv_chara_006_01_04.png",
          "face_sha256": "dd096a9d2553de3cc6ed017456142d7e1d63f9d0f152452f2a356aae40c4674f",
          "native_face_offset": [
            134,
            91
          ],
          "output_sha256": "58d2c91aa2d15c4423ed4ff5339d7d4cbcb803b64b7ac3fae6fb10cefffed72a"
        },
        {
          "resource": "adv_chara_132_01_02",
          "body": "adv_chara_132_01.png",
          "body_sha256": "0d49191320a09a7eee93f32d7af333bd6edcbf5ec4259ea97bca67053a4f43d0",
          "face": "adv_chara_132_01_02.png",
          "face_sha256": "35090ee6bc3090ed915f79362067b7ebaa71b9069293a4d72670beb4b7497173",
          "native_face_offset": [
            58,
            91
          ],
          "output_sha256": "ceffa056dc2f7e90ce04c709e42b8149e2509cb1be1254991dd1e821db27ea0d"
        },
        {
          "resource": "adv_chara_135_01_02",
          "body": "adv_chara_135_01.png",
          "body_sha256": "cd24c39770bdb5d8134998d731217d541cd18c12c966c277618c7d27a07e76bd",
          "face": "adv_chara_135_01_02.png",
          "face_sha256": "f6dd75d2e7cd700f0f1cfaa28c91500e52068190873e890d0ec80da411d3ead8",
          "native_face_offset": [
            174,
            84
          ],
          "output_sha256": "2f0e4871d9ffbff212df10b6ea145382ce6b23cc8faba30e19d2f1a3e2341a5f"
        },
        {
          "resource": "adv_chara_148_01_03",
          "body": "adv_chara_148_01.png",
          "body_sha256": "4ce7650d14226a78ef84e7be754b8b8600b9cff0d48dfd59a9ca03a3a9a029e4",
          "face": "adv_chara_148_01_03.png",
          "face_sha256": "6ded9a9a7ba2f29e71dd1cf57276f9ab334207d361a230b9f6629d62184cb2dc",
          "native_face_offset": [
            112,
            96
          ],
          "output_sha256": "e3b2de86d548142516c59cb821ada3a095e02734ff6defd5dbc9b370737d8e16"
        }
      ],
      "coverage_effective_state_sha256": "3e427e6235727d7dee565f49b339a0ab28f94384085bedcadefe62827e02ca64",
      "execution_record": "09 Audits and Manifests/T7S_B0100_B0159_EXECUTION_RECORD.md",
      "boundary": "Complete chapter-local text/native state plus selected static review; no authored choice or inline movie; no later-source semantic evidence; performed audio unreviewed."
    },
    "b0136_close_verification": {
      "operation": "T7S_B0136_CLOSE",
      "checked_at": "2026-09-26",
      "status": "PASS_BOUNDED_TEXT_NATIVE_AND_STATIC_REVIEW",
      "episode_ids": [
        "312203101",
        "312203102",
        "312203103"
      ],
      "source_bindings": [
        {
          "episode_id": "312203101",
          "script_id": "ing_102031_01.json__11fe04a1d548b8e0",
          "source_sha256": "69993de217fd7a98fe2ce7a7bfdcae202913fe2f32dfb8e5f237058b6c4ba804",
          "decoded_sha256": "e920fc4430e3e972762db9279505bcc6b3ba349874aedf939665b4b943f81935",
          "normalized_sha256": "cab0d3119e7510771ada918996e3696afdbf2a52b3e4e296eff4a265efe66223",
          "structured_sha256": "cab0d3119e7510771ada918996e3696afdbf2a52b3e4e296eff4a265efe66223",
          "pages": 76,
          "text_records": 63,
          "command_only_pages": 13,
          "voice_pages": 47,
          "native_pages_verified": 76
        },
        {
          "episode_id": "312203102",
          "script_id": "ing_102031_02.json__371f2336f117e403",
          "source_sha256": "63de25b6e5bd87c17dbc30c49bafc2bf7265f7e81d6b063e12d4b43d2fde0a9b",
          "decoded_sha256": "0f609020e40ae9686f1c0386bcd42416c60ba2584bf0032767b0deb860f15d10",
          "normalized_sha256": "ff2407280ed54b2fad8fed5eef4983edae6f298b50906fe84ed640d301200b10",
          "structured_sha256": "ff2407280ed54b2fad8fed5eef4983edae6f298b50906fe84ed640d301200b10",
          "pages": 53,
          "text_records": 43,
          "command_only_pages": 10,
          "voice_pages": 36,
          "native_pages_verified": 53
        },
        {
          "episode_id": "312203103",
          "script_id": "ing_102031_03.json__737ff4b13f4a334f",
          "source_sha256": "be8b44563e942ffb5f06dcc4732b25f5a4edb2b87db9aaea2e29897de6c28294",
          "decoded_sha256": "c7175390cbd0211a65b218898d4553f27058ef6b61fddf3d3f1d17e8c1451698",
          "normalized_sha256": "ab3565762c04e3a417016679514f9ed84e2776d3d21c2d3f4c01588a295cca32",
          "structured_sha256": "ab3565762c04e3a417016679514f9ed84e2776d3d21c2d3f4c01588a295cca32",
          "pages": 56,
          "text_records": 48,
          "command_only_pages": 8,
          "voice_pages": 39,
          "native_pages_verified": 56
        }
      ],
      "totals": {
        "pages": 185,
        "text_records": 154,
        "command_only_pages": 31,
        "voice_pages": 122,
        "visual_refs": 1253
      },
      "voice_count_basis": "Distinct dialogue log-order indexes with voice resource; title-only cues additional; no performed audio reviewed.",
      "native_packet_sha256": "77ea9f86b437af9eb285b1561e1b6b60d12714c3e4d4006ce4bb457698afeba2",
      "dialogue_packet_sha256": "621d0137a5628274c8facad78b26f2a598822b08682d58e33502635cc15bddc8",
      "visual_assets": [
        {
          "resource": "adv_chara_138_01_04",
          "body": "adv_chara_138_01.png",
          "body_sha256": "cd5b6d322e4dc013f5c79a4449e8d5e7a89f2f4238ad257e6710dc02b016c4e7",
          "face": "adv_chara_138_01_04.png",
          "face_sha256": "65fca530051887adb22a9bf679e67d260c0e0fa6dc0452767d440cb6446301ae",
          "native_face_offset": [
            110,
            91
          ],
          "output_sha256": "3b74baa13dabdc867ce7a9279237f1f2c818613cec1827d41b0965743e62222f"
        },
        {
          "resource": "adv_chara_138_02_02",
          "body": "adv_chara_138_02.png",
          "body_sha256": "784907ac9965476f87acba871f5d259de6b0e863d887f605980026d2773a8795",
          "face": "adv_chara_138_02_02.png",
          "face_sha256": "fb5360671b3d53eb5f45854d918f4218f2b7e7b5b4d16339721d233d43624c69",
          "native_face_offset": [
            181,
            91
          ],
          "output_sha256": "eaaba51f77ad2e238b24129c831a718411b75421ee2e331071f6002ca4db29c1"
        },
        {
          "resource": "adv_chara_007_07_01",
          "body": "adv_chara_007_07.png",
          "body_sha256": "36e21f6c17f2cc339f318d8423487ed28913cd7b3372eb0b8d89c16103e88dc6",
          "face": "adv_chara_007_07_01.png",
          "face_sha256": "dc9e678fd2bb687c3ec4785a6529c65718a0fcaf64fec7aca532dfd34e29451f",
          "native_face_offset": [
            136,
            86
          ],
          "output_sha256": "81d3e207aa26257f8076f3af7f038c0343715c7562fdf4aa2cb835a92235425a"
        },
        {
          "resource": "adv_chara_133_03_01",
          "body": "adv_chara_133_03.png",
          "body_sha256": "690e5a5d50a4a6f89ba47e93eeaa1c145fcb31e00d85912ca956ddbd509a7e4d",
          "face": "adv_chara_133_03_01.png",
          "face_sha256": "ddda3f85d6ab7e1b4f1e21c40c646c461f269c19fffcc4828e792b9d92d1738a",
          "native_face_offset": [
            142,
            66
          ],
          "output_sha256": "6fa23b2f871da979d1e10277994058d07a1b99bd694089bb7310bd676dfb2689"
        },
        {
          "resource": "adv_chara_133_01_02",
          "body": "adv_chara_133_01.png",
          "body_sha256": "ee3e5303e0e6ee798401ba7e6e276138169525925f4058c03f1d01ddd73fa7e5",
          "face": "adv_chara_133_01_02.png",
          "face_sha256": "651d1c98afbc3978bc392857a996b74675d6f8e5daed3b506d0a8d4b7d21edfa",
          "native_face_offset": [
            142,
            66
          ],
          "output_sha256": "0ce587628d11ea9fb71c8a40d53445995693764b47b94e2e11622c41cf8d0bdf"
        },
        {
          "resource": "adv_chara_005_02_01",
          "body": "adv_chara_005_02.png",
          "body_sha256": "495af8e9da9f07ee113a270a242ad90534d119db02f8bb7a25ef89ef2f81a948",
          "face": "adv_chara_005_02_01.png",
          "face_sha256": "d67b1b54daa9ec5da6b1338ef59328093c2e2bd93c2fe4514257f0e37a3a5955",
          "native_face_offset": [
            76,
            85
          ],
          "output_sha256": "b98c99190320c43761acf00754508c1bb7a96f189555b188a8dcf96014b12f90"
        },
        {
          "resource": "adv_chara_122_03_01",
          "body": "adv_chara_122_03.png",
          "body_sha256": "1084fddf805e05a0839333213f525e754782d67da05bdbab8c884c197f5a7063",
          "face": "adv_chara_122_03_01.png",
          "face_sha256": "ead71ba97d581a2691204ff7311175d463d34ad83a5a7e8e6f00723826db7119",
          "native_face_offset": [
            104,
            104
          ],
          "output_sha256": "774aeec7107a999c9176ac442c1cda7afe651f32e2f088360f4fd35dc148e7c1"
        },
        {
          "resource": "adv_chara_004_01_10",
          "body": "adv_chara_004_01.png",
          "body_sha256": "5d8b60092117906b699d98ccabfc88344ea61f82e9b27a23bec1fa15d0cb65be",
          "face": "adv_chara_004_01_10.png",
          "face_sha256": "42fc75298dc9734890b153d26b256ac430e207bda971490c28fed5465625f0bf",
          "native_face_offset": [
            194,
            74
          ],
          "output_sha256": "849fc43dfa7325ef942f97b9f339552450a3b7eae72c06740ffa8b4d48d00e9c"
        }
      ],
      "coverage_effective_state_sha256": "2732727fa46895da816fdf5c6b03af1edaa0887649f794e1fceabecef56b0b6a",
      "execution_record": "09 Audits and Manifests/T7S_B0100_B0159_EXECUTION_RECORD.md",
      "boundary": "Complete chapter-local text/native state plus selected static review; no authored choice or inline movie; no later-source semantic evidence; performed audio unreviewed."
    },
    "b0137_close_verification": {
      "operation": "T7S_B0137_CLOSE",
      "checked_at": "2026-09-26",
      "status": "PASS_BOUNDED_TEXT_NATIVE_AND_STATIC_REVIEW",
      "episode_ids": [
        "312203201",
        "312203202",
        "312203203"
      ],
      "source_bindings": [
        {
          "episode_id": "312203201",
          "script_id": "ing_102032_01.json__296808264d296d9f",
          "source_sha256": "2521f65026510c5d1d0e4a8ad9610bfb65be449167c01d61d391a0d91237bb13",
          "decoded_sha256": "8e99f2041aa2f9f0ed0e56c9a828bc7698f59db7493d6ce4613a64ab322b475b",
          "normalized_sha256": "1db4f3c12abe1b4d702d869e06046bed10899676b716d9d1ca5f7320e0fbfc75",
          "structured_sha256": "1db4f3c12abe1b4d702d869e06046bed10899676b716d9d1ca5f7320e0fbfc75",
          "pages": 72,
          "text_records": 66,
          "command_only_pages": 6,
          "voice_pages": 52,
          "native_pages_verified": 72
        },
        {
          "episode_id": "312203202",
          "script_id": "ing_102032_02.json__1ed24d2821a152fa",
          "source_sha256": "9c007c9a3b01a7813587876625ed9ea0927c1a018e3ee838fff9ff96eb3c1aa9",
          "decoded_sha256": "1226e59412a994a6ea9335c27b54f361dfc3d3d3c07dd890ae303e0c14c5eb32",
          "normalized_sha256": "6746627a0dc1ea3aa9aa576db11fffb99460628adc96e962438959fea747557d",
          "structured_sha256": "6746627a0dc1ea3aa9aa576db11fffb99460628adc96e962438959fea747557d",
          "pages": 44,
          "text_records": 40,
          "command_only_pages": 4,
          "voice_pages": 21,
          "native_pages_verified": 44
        },
        {
          "episode_id": "312203203",
          "script_id": "ing_102032_03.json__3e4955df80d0f2c8",
          "source_sha256": "3a95f51e3efc39bcfecba2210be41a97b119ce5c5f195326861fccb67e773524",
          "decoded_sha256": "a56fe8fcd4192bfba68daed8efbd6722780192d5cf20a864f0ea62c7e9baa4a3",
          "normalized_sha256": "a9c26a87c98db3f6083e507d4fecac4ebe4a9359907b57ac288a875d50e09468",
          "structured_sha256": "a9c26a87c98db3f6083e507d4fecac4ebe4a9359907b57ac288a875d50e09468",
          "pages": 83,
          "text_records": 78,
          "command_only_pages": 5,
          "voice_pages": 61,
          "native_pages_verified": 83
        }
      ],
      "totals": {
        "pages": 199,
        "text_records": 184,
        "command_only_pages": 15,
        "voice_pages": 134,
        "visual_refs": 1767
      },
      "voice_count_basis": "Distinct dialogue log-order indexes with voice resource; title-only cues additional; no performed audio reviewed.",
      "native_packet_sha256": "6e8b392d42caa23466946cba68c1f71b4aaa4f767dfc19deeee1a2fb75c12bee",
      "dialogue_packet_sha256": "fc45178a98dfd9af7353edb21bf45fdd5a4821570cb795fd3bbd57671b12aea0",
      "visual_assets": [
        {
          "resource": "adv_chara_139_01_01",
          "body": "adv_chara_139_01.png",
          "body_sha256": "4b3b72b680ffd52d354d5b64a16301f5112201a6b95341c8d32ff5cf2292071c",
          "face": "adv_chara_139_01_01.png",
          "face_sha256": "0a88cc98f6b9cdea573d01d9775412ba58496a866d68174830129daf891089e1",
          "native_face_offset": [
            116,
            92
          ],
          "output_sha256": "a509f37196869efc19f11ec11987dec0ea58513f3242b4e58a68a2d5d5d64cea"
        },
        {
          "resource": "adv_chara_139_01_03",
          "body": "adv_chara_139_01.png",
          "body_sha256": "4b3b72b680ffd52d354d5b64a16301f5112201a6b95341c8d32ff5cf2292071c",
          "face": "adv_chara_139_01_03.png",
          "face_sha256": "3cc4f3f5002dbc16f7083d494fac297c7e6f08e40a001c4d2862f5090ead23bb",
          "native_face_offset": [
            116,
            92
          ],
          "output_sha256": "354e3b1a033ef48c8b4f688c0e379183ea4a551096e79e77d9b3cbaa20ddcb30"
        },
        {
          "resource": "adv_chara_009_03_05",
          "body": "adv_chara_009_03.png",
          "body_sha256": "ffc2406a944338eecacf731a83cc2ecfedce4b3e932bcbf3574528e5939035c8",
          "face": "adv_chara_009_03_05.png",
          "face_sha256": "570cced2b6e3e60f61c3c52413b523ae163414814b4e02170811210c369a52c3",
          "native_face_offset": [
            109,
            85
          ],
          "output_sha256": "819de191090fdfae2393e4e56dd4e8b5dfbe623097cd04e418e7002327e37189"
        },
        {
          "resource": "adv_chara_009_03_12",
          "body": "adv_chara_009_03.png",
          "body_sha256": "ffc2406a944338eecacf731a83cc2ecfedce4b3e932bcbf3574528e5939035c8",
          "face": "adv_chara_009_03_12.png",
          "face_sha256": "8571371c4ff1ef4cfcde3dc25d0d26c96c9545731a97794152932c4ec203c165",
          "native_face_offset": [
            109,
            85
          ],
          "output_sha256": "156099a7209717a971a477b449f0d307c2121433dee5bcaefb21763fcf4337ab"
        },
        {
          "resource": "adv_chara_005_01_01",
          "body": "adv_chara_005_01.png",
          "body_sha256": "5eacc7b48f482d043fd5ebcb64d978a16ea335fd2c83a4b641983d2938444f21",
          "face": "adv_chara_005_01_01.png",
          "face_sha256": "087da32ef5957a1827c9ba84e43c2e8e4d19b71d55561220f01057f33768af2a",
          "native_face_offset": [
            76,
            85
          ],
          "output_sha256": "08577674aaec962626b0189c6933a38fa2c4a709874b6ebf768ea9364402d105"
        },
        {
          "resource": "adv_chara_126_01_01",
          "body": "adv_chara_126_01.png",
          "body_sha256": "00ce923f755ee73078d66152d8d3d3bc5b0189a1d61173875e3443796d80e987",
          "face": "adv_chara_126_01_01.png",
          "face_sha256": "774420432ab233a6519985dfa12e34e197a97a5680a978723b6dcc7b10a7395e",
          "native_face_offset": [
            67,
            59
          ],
          "output_sha256": "49932c912ca5a89570312410bc57ba9f42ed947e5576332cefa5d7e8e0ba39b5"
        },
        {
          "resource": "adv_chara_137_01_02",
          "body": "adv_chara_137_01.png",
          "body_sha256": "8da617d5736a9e233312322d4f1a1edff77c9f764832a0665ddc3d9adb9610ba",
          "face": "adv_chara_137_01_02.png",
          "face_sha256": "9a6ebbf7e2e28b54160372c10ad30d7ef44bb186000e0e32b9eb47919f12435f",
          "native_face_offset": [
            104,
            62
          ],
          "output_sha256": "b38990d4f7a133b0d2a6cda04e8eb61d23364b768b24df8ea24d7cf72cf4d7b2"
        }
      ],
      "coverage_effective_state_sha256": "b56b40fd7edce5b12a017e34b4a9d472c6f6186b92fa957c9b8651f0ce10deea",
      "execution_record": "09 Audits and Manifests/T7S_B0100_B0159_EXECUTION_RECORD.md",
      "boundary": "Complete chapter-local text/native state plus selected static review; no authored choice or inline movie; no later-source semantic evidence; performed audio unreviewed."
    },
    "b0138_close_verification": {
      "operation": "T7S_B0138_CLOSE",
      "checked_at": "2026-09-26",
      "status": "PASS_BOUNDED_TEXT_NATIVE_AND_STATIC_REVIEW",
      "episode_ids": [
        "312203301",
        "312203302",
        "312203303"
      ],
      "source_bindings": [
        {
          "episode_id": "312203301",
          "script_id": "ing_102033_01.json__bdfa2be747137cb8",
          "source_sha256": "a2403a352944236be114a90f3a714875d2e32bfb801597f5a45d8cd4ed184a57",
          "decoded_sha256": "a2bf70e430bf393ebc7e03788dceef70c41072e52d698c3f5376d32a133c48ee",
          "normalized_sha256": "e616150d86eb89594c87305a5f2c471965aeb300004c99930b0b69e12507d4a2",
          "structured_sha256": "e616150d86eb89594c87305a5f2c471965aeb300004c99930b0b69e12507d4a2",
          "pages": 60,
          "text_records": 53,
          "command_only_pages": 7,
          "voice_pages": 33,
          "native_pages_verified": 60
        },
        {
          "episode_id": "312203302",
          "script_id": "ing_102033_02.json__435a205fe14e8e15",
          "source_sha256": "f4e954dee5ba20d7b117ea5c189de2e5d82b604f6729bedd43f4e0982d268ab8",
          "decoded_sha256": "848ba3e6ca47eb76b136f89c469c77492fac0ba646a072bff90ded5b1bd66fed",
          "normalized_sha256": "3a85a8aef5ac6c1f6f7ffc2c62e01cbf46166bde3a96ff9ee80ba7e9d5f29812",
          "structured_sha256": "3a85a8aef5ac6c1f6f7ffc2c62e01cbf46166bde3a96ff9ee80ba7e9d5f29812",
          "pages": 43,
          "text_records": 40,
          "command_only_pages": 3,
          "voice_pages": 40,
          "native_pages_verified": 43
        },
        {
          "episode_id": "312203303",
          "script_id": "ing_102033_03.json__8f39540cb0542654",
          "source_sha256": "3ee8307a001514dea008d534c8a728d049d83e889e42d98915d342cf51c088c2",
          "decoded_sha256": "25aec6a13a0b1e642cf5aa0497a7bab8e13510ca0db42e6385d0752f453c3dab",
          "normalized_sha256": "643d1a3c62083cde5bf73478ae864b0d8233bb2e292e041d9401ff740742b97a",
          "structured_sha256": "643d1a3c62083cde5bf73478ae864b0d8233bb2e292e041d9401ff740742b97a",
          "pages": 58,
          "text_records": 49,
          "command_only_pages": 9,
          "voice_pages": 39,
          "native_pages_verified": 58
        }
      ],
      "totals": {
        "pages": 161,
        "text_records": 142,
        "command_only_pages": 19,
        "voice_pages": 112,
        "visual_refs": 1730
      },
      "voice_count_basis": "Distinct dialogue log-order indexes with voice resource; title-only cues additional; no performed audio reviewed.",
      "native_packet_sha256": "1a11d826671e53337cf7f9facea31c26ca203fa4293d87a4c0d25378edb55939",
      "dialogue_packet_sha256": "ec4f9ec5052afaab4b571d8d27a9063d4051ca941b88aabe3126b87e816baad2",
      "visual_assets": [
        {
          "resource": "adv_chara_012_01_01",
          "body": "adv_chara_012_01.png",
          "body_sha256": "d142646f64071ed43061fd75721befa778228cd90a1c9d04fd996d739fc468b9",
          "face": "adv_chara_012_01_01.png",
          "face_sha256": "48fb3d5af2ec98fe05dd274e15e82fd680c07f6723ab0a2f5dceb188b7fcffd7",
          "native_face_offset": [
            59,
            74
          ],
          "output_sha256": "1a3b01fe595284bb8b645118dd34a3df4190b302bad562466afad619b5724c2b"
        },
        {
          "resource": "adv_chara_012_03_01",
          "body": "adv_chara_012_03.png",
          "body_sha256": "a0e26982d9e65e3c9d0892b910b529cdc340aa2b5e2e99d5da8764c3175bbc12",
          "face": "adv_chara_012_03_01.png",
          "face_sha256": "a5f428229fc32bff1e4699e2c4a3b8aa8bc1f82285dae2cf2ba22fc329484fda",
          "native_face_offset": [
            117,
            74
          ],
          "output_sha256": "76639a045daa91598492254c884bcf1444de5d161490e8eceeda954cb325a736"
        },
        {
          "resource": "adv_chara_144_01_02",
          "body": "adv_chara_144_01.png",
          "body_sha256": "20fc6bc7ed22a88c88e06eb84b21be11f06fa69cfd7f19e0de37a95c939d9f1e",
          "face": "adv_chara_144_01_02.png",
          "face_sha256": "65cd13cbe3a95acd7e20cdbbcbd9a481417d7a79465c58649391550c59ab0a21",
          "native_face_offset": [
            120,
            74
          ],
          "output_sha256": "73bb9a9c4e3ccdb50b9c9d3ee2ba518a537fdb31424f0a5f154b4edc4141a532"
        },
        {
          "resource": "adv_chara_144_03_02",
          "body": "adv_chara_144_03.png",
          "body_sha256": "74211e7c5ba4cb4bc4e4470e8cfe500cb4d7f399169cebf7376c1031ab36469d",
          "face": "adv_chara_144_03_02.png",
          "face_sha256": "8725ec793c438315477a79b20402621c7948ff15622d46223f390579e9c9a326",
          "native_face_offset": [
            200,
            74
          ],
          "output_sha256": "951ea6d19606fab90f11f07098d2aed60073c6a93c623baa17483bd04fb608a1"
        },
        {
          "resource": "adv_chara_002_03_03",
          "body": "adv_chara_002_03.png",
          "body_sha256": "4bb14d813389b79055c4a24b5b3020e06bde9122d7b203b04a5489b358a7f1c7",
          "face": "adv_chara_002_03_03.png",
          "face_sha256": "d5239a37aae80fa8dbc6c3f2315fe90e4f1b3c4c86269687c378cf7b7d953436",
          "native_face_offset": [
            132,
            64
          ],
          "output_sha256": "734ecbe5ddc087c842ec5486b20a2d02f0429e5fa46bd0d16346dcb66df9f213"
        },
        {
          "resource": "adv_chara_022_01",
          "body": "adv_chara_022_01.png",
          "body_sha256": "e0e4387d7819b9ced9fa032f8fd12c83ff13fecea344be28625590ea0ed40d23",
          "output_sha256": "f8f338d2c20c525516746ef2d014fb3271683f03081808c04ca5968d348e9322"
        }
      ],
      "coverage_effective_state_sha256": "83d877f231c12506e345d9c7832e96af02bc7d382348cdf73c31cfeccc528278",
      "execution_record": "09 Audits and Manifests/T7S_B0100_B0159_EXECUTION_RECORD.md",
      "boundary": "Complete chapter-local text/native state plus selected static review; no authored choice or inline movie; no later-source semantic evidence; performed audio unreviewed."
    },
    "b0139_close_verification": {
      "operation": "T7S_B0139_CLOSE",
      "checked_at": "2026-09-26",
      "status": "PASS_BOUNDED_TEXT_NATIVE_AND_STATIC_REVIEW",
      "episode_ids": [
        "312203401",
        "312203402",
        "312203403"
      ],
      "source_bindings": [
        {
          "episode_id": "312203401",
          "script_id": "ing_102034_01.json__a90cccaa92d8aec5",
          "source_sha256": "4c047d1a98e4988c94278ce9b8c27acfd680d872d70ee75de4ab003bf281a770",
          "decoded_sha256": "df52e2837f6bb38db53e8b9eb2f6740e4cb49ee7ff70491875169e4e888ba77c",
          "normalized_sha256": "ace6320777a305dc4135bfb33065ba999443c5adffe142d0a48e4093d6c85b53",
          "structured_sha256": "ace6320777a305dc4135bfb33065ba999443c5adffe142d0a48e4093d6c85b53",
          "pages": 43,
          "text_records": 38,
          "command_only_pages": 5,
          "voice_pages": 34,
          "native_pages_verified": 43
        },
        {
          "episode_id": "312203402",
          "script_id": "ing_102034_02.json__f6dd30b188e8fcfc",
          "source_sha256": "c08ed8697bccf016f96bdb8f5660daf125a02aad4b81d2f415ad5dd33fb45187",
          "decoded_sha256": "04c6a3d935e80f292557c43af6a8e74272af90989dfba77c21e1cf1c3128ec45",
          "normalized_sha256": "804394553d410cf4461e6e4c47d3f96d578c6a7d94813f3e37b84f8de78d6e96",
          "structured_sha256": "804394553d410cf4461e6e4c47d3f96d578c6a7d94813f3e37b84f8de78d6e96",
          "pages": 38,
          "text_records": 31,
          "command_only_pages": 7,
          "voice_pages": 31,
          "native_pages_verified": 38
        },
        {
          "episode_id": "312203403",
          "script_id": "ing_102034_03.json__b55f97fb065c22f4",
          "source_sha256": "4d2340431a637db7c98bac5ab331f6fbc92dc987849e1b73c0c7b0bbb86de67f",
          "decoded_sha256": "8183449b8cd637e9a273fe5b17054d18d483ec00a8c09fb70fa9ef2c06fd35a6",
          "normalized_sha256": "5873336575acc40558901e4df3fc444ef1526e4d1d47575d1111d1188c8228d2",
          "structured_sha256": "5873336575acc40558901e4df3fc444ef1526e4d1d47575d1111d1188c8228d2",
          "pages": 60,
          "text_records": 57,
          "command_only_pages": 3,
          "voice_pages": 50,
          "native_pages_verified": 60
        }
      ],
      "totals": {
        "pages": 141,
        "text_records": 126,
        "command_only_pages": 15,
        "voice_pages": 115,
        "visual_refs": 945
      },
      "voice_count_basis": "Distinct dialogue log-order indexes with voice resource; title-only cues additional; no performed audio reviewed.",
      "native_packet_sha256": "0dbc1fa0763fdfea6fd1ed00bdd523352651a3bf57347dc770cf6440f11156e4",
      "dialogue_packet_sha256": "664fb6b8605247ec2f95f90fcf2b7df5260b8185013b87913dd3558007535a58",
      "visual_assets": [
        {
          "resource": "adv_chara_148_01_01",
          "body": "adv_chara_148_01.png",
          "body_sha256": "4ce7650d14226a78ef84e7be754b8b8600b9cff0d48dfd59a9ca03a3a9a029e4",
          "face": "adv_chara_148_01_01.png",
          "face_sha256": "9ebe31db2b7e89c6e81e25eebc43864dde38a46404a13c55e27e2207e9040f3a",
          "native_face_offset": [
            112,
            96
          ],
          "output_sha256": "e308635b1566fea246d92f4a6a8b2084632b8904a3def3639029ee73ddfc9353"
        },
        {
          "resource": "adv_chara_148_01_03",
          "body": "adv_chara_148_01.png",
          "body_sha256": "4ce7650d14226a78ef84e7be754b8b8600b9cff0d48dfd59a9ca03a3a9a029e4",
          "face": "adv_chara_148_01_03.png",
          "face_sha256": "6ded9a9a7ba2f29e71dd1cf57276f9ab334207d361a230b9f6629d62184cb2dc",
          "native_face_offset": [
            112,
            96
          ],
          "output_sha256": "e3b2de86d548142516c59cb821ada3a095e02734ff6defd5dbc9b370737d8e16"
        },
        {
          "resource": "adv_chara_014_01_05",
          "body": "adv_chara_014_01.png",
          "body_sha256": "b8665daef47ba3fbf338538586adc18c16ed72c65092ad9d57cf2a4f128f3677",
          "face": "adv_chara_014_01_05.png",
          "face_sha256": "ed32750fad9e53a36ed88a92c1a1344b25bb2e58684c66b433dce87ca8c475fe",
          "native_face_offset": [
            128,
            78
          ],
          "output_sha256": "9fbc6ee02ba0c8709964a98bf3f65d167b6b4d09f964141ec9bc9c3e4479c944"
        },
        {
          "resource": "adv_chara_132_01_02",
          "body": "adv_chara_132_01.png",
          "body_sha256": "0d49191320a09a7eee93f32d7af333bd6edcbf5ec4259ea97bca67053a4f43d0",
          "face": "adv_chara_132_01_02.png",
          "face_sha256": "35090ee6bc3090ed915f79362067b7ebaa71b9069293a4d72670beb4b7497173",
          "native_face_offset": [
            58,
            91
          ],
          "output_sha256": "ceffa056dc2f7e90ce04c709e42b8149e2509cb1be1254991dd1e821db27ea0d"
        },
        {
          "resource": "adv_chara_135_01_02",
          "body": "adv_chara_135_01.png",
          "body_sha256": "cd24c39770bdb5d8134998d731217d541cd18c12c966c277618c7d27a07e76bd",
          "face": "adv_chara_135_01_02.png",
          "face_sha256": "f6dd75d2e7cd700f0f1cfaa28c91500e52068190873e890d0ec80da411d3ead8",
          "native_face_offset": [
            174,
            84
          ],
          "output_sha256": "2f0e4871d9ffbff212df10b6ea145382ce6b23cc8faba30e19d2f1a3e2341a5f"
        },
        {
          "resource": "adv_chara_126_01_05",
          "body": "adv_chara_126_01.png",
          "body_sha256": "00ce923f755ee73078d66152d8d3d3bc5b0189a1d61173875e3443796d80e987",
          "face": "adv_chara_126_01_05.png",
          "face_sha256": "a8a338ef42c4430026b134982eb7a2dbe278e43b24595cca0a435f3d98627167",
          "native_face_offset": [
            67,
            59
          ],
          "output_sha256": "f97c0857fb4390f47ef18d77693eec6458bc18895ce194a7654ab3556fd881ac"
        },
        {
          "resource": "adv_chara_134_01_04",
          "body": "adv_chara_134_01.png",
          "body_sha256": "59e54f3c7e045ef97681badac43daacab7c317c2456705c43ecd6e9021fcf960",
          "face": "adv_chara_134_01_04.png",
          "face_sha256": "453b64f5eef3b1ab03688bb90741b50da546046c326763e805c3fbba0084ff8e",
          "native_face_offset": [
            96,
            67
          ],
          "output_sha256": "f17fdfc684d675efe4eba6924cc956c3a65659c4979eb5255fa75561aa2988a9"
        },
        {
          "resource": "adv_chara_006_01_19",
          "body": "adv_chara_006_01.png",
          "body_sha256": "d40ded643748164bb05d319c4a3889a41f99d102a3fcfeb60675b59529a6c392",
          "face": "adv_chara_006_01_19.png",
          "face_sha256": "22164aee9604a09076dd075c02737d037bf46abde195eb4580e9cafbc6cfe6c4",
          "native_face_offset": [
            134,
            91
          ],
          "output_sha256": "867f8729e63a5a9952c62e5fc2fee72fd0d85c322b92e32a9f0262e82ccf1d0f"
        }
      ],
      "coverage_effective_state_sha256": "aead5ba83f65121f180e706d5de03db7eaafdc8302b67b4b3c13a149a069a550",
      "execution_record": "09 Audits and Manifests/T7S_B0100_B0159_EXECUTION_RECORD.md",
      "boundary": "Complete chapter-local text/native state plus selected static review; no authored choice or inline movie; no later-source semantic evidence; performed audio unreviewed."
    },
    "b0140_close_verification": {
      "operation": "T7S_B0140_CLOSE",
      "checked_at": "2026-09-26",
      "status": "PASS_BOUNDED_TEXT_NATIVE_AND_STATIC_REVIEW",
      "episode_ids": [
        "312203501",
        "312203502",
        "312203503"
      ],
      "source_bindings": [
        {
          "episode_id": "312203501",
          "script_id": "ing_102035_01.json__e386cf4dc5d671da",
          "source_sha256": "53622a2b128fbccadc5f1a8794935143280ac99be4b96587269497deeb897504",
          "decoded_sha256": "6e0f76999ef0b4569b7b945cf15cb4aeab7606bf650f2cba866df35c699bb86f",
          "normalized_sha256": "1b9776f37edb4866f2e80bf7827d5bfa9707d2fe1ee18bc951ad04408316e1bf",
          "structured_sha256": "1b9776f37edb4866f2e80bf7827d5bfa9707d2fe1ee18bc951ad04408316e1bf",
          "pages": 41,
          "text_records": 35,
          "command_only_pages": 6,
          "voice_pages": 25,
          "native_pages_verified": 41
        },
        {
          "episode_id": "312203502",
          "script_id": "ing_102035_02.json__0375709dd6a80432",
          "source_sha256": "2e354af8c9a396f750aa4c83a29a1be17e9fb66568b9883c658f76397f718015",
          "decoded_sha256": "ec13d871ebcd3a1b78bfa0d4e9012170b59b0515a700f43ebb2c19b870a48ca9",
          "normalized_sha256": "5f2db6634ca0b13b9ffb038c40e3525372f72ab210983728528ddfd74bf9016b",
          "structured_sha256": "5f2db6634ca0b13b9ffb038c40e3525372f72ab210983728528ddfd74bf9016b",
          "pages": 70,
          "text_records": 60,
          "command_only_pages": 10,
          "voice_pages": 56,
          "native_pages_verified": 70
        },
        {
          "episode_id": "312203503",
          "script_id": "ing_102035_03.json__519e2300dadad1bd",
          "source_sha256": "24ad65ddf286cb27860ba329051bd803aad2d4980774ef585afb112febf04fc9",
          "decoded_sha256": "c4e5c8c90433b6b673434ebd119e52131e2e2bfabd794b2ccd3740a6aa7f083d",
          "normalized_sha256": "100a478c71e612648fd1550f6dff8ed9140bad0220394c8f337d0cfa1bcc2805",
          "structured_sha256": "100a478c71e612648fd1550f6dff8ed9140bad0220394c8f337d0cfa1bcc2805",
          "pages": 42,
          "text_records": 39,
          "command_only_pages": 3,
          "voice_pages": 29,
          "native_pages_verified": 42
        }
      ],
      "totals": {
        "pages": 153,
        "text_records": 134,
        "command_only_pages": 19,
        "voice_pages": 110,
        "visual_refs": 1664
      },
      "voice_count_basis": "Distinct dialogue log-order indexes with voice resource; title-only cues additional; no performed audio reviewed.",
      "native_packet_sha256": "bbb93314033f4bbd9509d2e7ae0fe650b2e0cf8664b81f6ec82d9cdfc34c1694",
      "dialogue_packet_sha256": "762e4efe9a3c3023b6d1078c5023fccea11eecfa60229c380c147abf2d6e031a",
      "visual_assets": [
        {
          "resource": "adv_chara_149_01_03",
          "body": "adv_chara_149_01.png",
          "body_sha256": "99e954f4fe105fc93364cb6978bfe112dd69fe45e6f2cb11cee62fbf83b00624",
          "face": "adv_chara_149_01_03.png",
          "face_sha256": "39a62df2370ea33491d48a23fbb67db4c1dee8624359207a202b938ca26da139",
          "native_face_offset": [
            79,
            59
          ],
          "output_sha256": "703038416a4d8f2b11768850fae9901880f5181252133ddf7e7d099c02a7be36"
        },
        {
          "resource": "adv_chara_149_01_04",
          "body": "adv_chara_149_01.png",
          "body_sha256": "99e954f4fe105fc93364cb6978bfe112dd69fe45e6f2cb11cee62fbf83b00624",
          "face": "adv_chara_149_01_04.png",
          "face_sha256": "89bde1ee7810d2d1788d6cc531b14129304b7420fc4defa1dbb38a81aa5aa880",
          "native_face_offset": [
            79,
            59
          ],
          "output_sha256": "0e33bc4baac5cdfb68cf14d75b052bf5ba02c943202480a7062247ea168f02c1"
        },
        {
          "resource": "adv_chara_127_02_01",
          "body": "adv_chara_127_02.png",
          "body_sha256": "eca3cd36fc801dcf1e93e85ffaa806839d28ae78ee599b6848dd5d5bb0c64074",
          "face": "adv_chara_127_02_01.png",
          "face_sha256": "1cc62adbbe97ae4da7e14f9818fd0e2780ca9941ec2184379e740cf07d0a28d0",
          "native_face_offset": [
            176,
            108
          ],
          "output_sha256": "b9d64f08b9cdd22bebd57e5907fa0b5d62213057b3a515a4a53218e7e7d752c6"
        },
        {
          "resource": "adv_chara_133_01_01",
          "body": "adv_chara_133_01.png",
          "body_sha256": "ee3e5303e0e6ee798401ba7e6e276138169525925f4058c03f1d01ddd73fa7e5",
          "face": "adv_chara_133_01_01.png",
          "face_sha256": "63b69d8fabb391cca809bb9376ebb26c871ac483bfc47ea1c9e2bb39fa2ff6b2",
          "native_face_offset": [
            142,
            66
          ],
          "output_sha256": "05d20565d7469c9ad43a12430c4704ca5d2e209f4b41e6e98446c3c5ef4c9a38"
        },
        {
          "resource": "adv_chara_131_01_03",
          "body": "adv_chara_131_01.png",
          "body_sha256": "1a9960701b204ddf456de522c3d4e51d2820a1870f85ee2e0bcb8edd55d7f867",
          "face": "adv_chara_131_01_03.png",
          "face_sha256": "57165766efb46361b4a3be3e6b8d573ca3cf5546082fa11ab4d5acf882c1dad8",
          "native_face_offset": [
            118,
            62
          ],
          "output_sha256": "7210555ae2077e689413a13884376a87b5b3a0c3294ee4c29badc384902a2113"
        },
        {
          "resource": "adv_chara_139_01_01",
          "body": "adv_chara_139_01.png",
          "body_sha256": "4b3b72b680ffd52d354d5b64a16301f5112201a6b95341c8d32ff5cf2292071c",
          "face": "adv_chara_139_01_01.png",
          "face_sha256": "0a88cc98f6b9cdea573d01d9775412ba58496a866d68174830129daf891089e1",
          "native_face_offset": [
            116,
            92
          ],
          "output_sha256": "a509f37196869efc19f11ec11987dec0ea58513f3242b4e58a68a2d5d5d64cea"
        },
        {
          "resource": "adv_chara_145_01_02",
          "body": "adv_chara_145_01.png",
          "body_sha256": "e7e4e7d94dadbb80e074cefd5e23ff1fc6cd5fbe2b6f60c39e6ecab367a58bb2",
          "face": "adv_chara_145_01_02.png",
          "face_sha256": "4ef3e561795beef0fe996afe979e12e2f638b74317bc24fcd3907c4808bf0b03",
          "native_face_offset": [
            78,
            63
          ],
          "output_sha256": "f2e6379db50f250a7c97442d6a1c396d802b2366dff3af87016ffab5f1b86239"
        },
        {
          "resource": "adv_chara_148_01_01",
          "body": "adv_chara_148_01.png",
          "body_sha256": "4ce7650d14226a78ef84e7be754b8b8600b9cff0d48dfd59a9ca03a3a9a029e4",
          "face": "adv_chara_148_01_01.png",
          "face_sha256": "9ebe31db2b7e89c6e81e25eebc43864dde38a46404a13c55e27e2207e9040f3a",
          "native_face_offset": [
            112,
            96
          ],
          "output_sha256": "e308635b1566fea246d92f4a6a8b2084632b8904a3def3639029ee73ddfc9353"
        }
      ],
      "coverage_effective_state_sha256": "b7be6499c9a93c8ef1d4981db07f26376daf8c495674e0703479e4429f3408d6",
      "execution_record": "09 Audits and Manifests/T7S_B0100_B0159_EXECUTION_RECORD.md",
      "boundary": "Complete chapter-local text/native state plus selected static review; no authored choice or inline movie; no later-source semantic evidence; performed audio unreviewed."
    },
    "b0141_close_verification": {
      "operation": "T7S_B0141_CLOSE",
      "checked_at": "2026-09-26",
      "status": "PASS_BOUNDED_TEXT_NATIVE_AND_STATIC_REVIEW",
      "episode_ids": [
        "312203601",
        "312203602",
        "312203603"
      ],
      "source_bindings": [
        {
          "episode_id": "312203601",
          "script_id": "ing_102036_01.json__d6f6fbf32e3f62e3",
          "source_sha256": "f580889af7b8ab53bbd153078860278dbe5fff7c8027567038df7597a1fa7aa2",
          "decoded_sha256": "dde00dd378519c7f630afb7fd49686d8d1d3fbb60ef4f2f4c3a1034047a47500",
          "normalized_sha256": "18615443a552477079d23f80cf594880d8cc4621473a1d737149d803e2e70a6c",
          "structured_sha256": "18615443a552477079d23f80cf594880d8cc4621473a1d737149d803e2e70a6c",
          "pages": 50,
          "text_records": 44,
          "command_only_pages": 6,
          "voice_pages": 34,
          "native_pages_verified": 50
        },
        {
          "episode_id": "312203602",
          "script_id": "ing_102036_02.json__5bbf91f75c88b7f0",
          "source_sha256": "a85ef1d9b0fc7020acd504a87332545f71b330961d60a341b2adebb8b77cdb2f",
          "decoded_sha256": "cd2fab078fff9523a59b7ca4fc1690d79c7b5d3b0e96fcc26da216937535a846",
          "normalized_sha256": "b1064b9a4274cba83630c7c72087f270b607cac4bc3c17d5e7fa94f2b3cceaa0",
          "structured_sha256": "b1064b9a4274cba83630c7c72087f270b607cac4bc3c17d5e7fa94f2b3cceaa0",
          "pages": 40,
          "text_records": 34,
          "command_only_pages": 6,
          "voice_pages": 34,
          "native_pages_verified": 40
        },
        {
          "episode_id": "312203603",
          "script_id": "ing_102036_03.json__02f1c676ebd40c9a",
          "source_sha256": "311cdfc0f9ecc23788bf6aaacbf5d33dd0152b21844df03d7324a8afe669609d",
          "decoded_sha256": "0a86a05fa1ef4827ac6145345880974a4f9563c4ef91d70a7b305a5642281f08",
          "normalized_sha256": "fc788b8bd951570c6ee999da51945a3ccc057a6084941a109810a90c9df16ae7",
          "structured_sha256": "fc788b8bd951570c6ee999da51945a3ccc057a6084941a109810a90c9df16ae7",
          "pages": 57,
          "text_records": 48,
          "command_only_pages": 9,
          "voice_pages": 40,
          "native_pages_verified": 57
        }
      ],
      "totals": {
        "pages": 147,
        "text_records": 126,
        "command_only_pages": 21,
        "voice_pages": 108,
        "visual_refs": 987
      },
      "voice_count_basis": "Distinct dialogue log-order indexes with voice resource; title-only cues additional; no performed audio reviewed.",
      "native_packet_sha256": "a50855b8ca6005cd9f0c5938e65b8ea5515645b5c343f91801f9fa96f767f6b0",
      "dialogue_packet_sha256": "4aafc6668537104c9f6fdabc4763f812d4a79e052edbf99b2b6e0fc3a5443abd",
      "visual_assets": [
        {
          "resource": "adv_chara_008_01_11",
          "body": "adv_chara_008_01.png",
          "body_sha256": "a72bd127faade4229587eff774c6b319fd99e8221290d4cfbd61769441d8afa4",
          "face": "adv_chara_008_01_11.png",
          "face_sha256": "90bd4ef9754ef0bb4feb08a9f247f3f14eae229693e43ad72d542ec37440898f",
          "native_face_offset": [
            166,
            84
          ],
          "output_sha256": "e7f53af41f122b88fdce7e49f85229221a9d923457a9907d0681530eceb070e6"
        },
        {
          "resource": "adv_chara_008_01_13",
          "body": "adv_chara_008_01.png",
          "body_sha256": "a72bd127faade4229587eff774c6b319fd99e8221290d4cfbd61769441d8afa4",
          "face": "adv_chara_008_01_13.png",
          "face_sha256": "24d7fbb743cf60a9aa01072a9ee58d7e2264ba07a3324b3ade314d03b7f7b755",
          "native_face_offset": [
            166,
            84
          ],
          "output_sha256": "4db0308da75395b7b590866ad4e66793d7925f619d986935559321ca26d6f5d3"
        },
        {
          "resource": "adv_chara_145_01_03",
          "body": "adv_chara_145_01.png",
          "body_sha256": "e7e4e7d94dadbb80e074cefd5e23ff1fc6cd5fbe2b6f60c39e6ecab367a58bb2",
          "face": "adv_chara_145_01_03.png",
          "face_sha256": "ede176c9694db9d0185ba6b876bb9ce18e45eecf08af097e1f91e0fc95444506",
          "native_face_offset": [
            78,
            63
          ],
          "output_sha256": "250c386302617c55e2909ea3ac9359cfdc855db715dd404c12f6c49a1fe09f0f"
        },
        {
          "resource": "adv_chara_145_01_02",
          "body": "adv_chara_145_01.png",
          "body_sha256": "e7e4e7d94dadbb80e074cefd5e23ff1fc6cd5fbe2b6f60c39e6ecab367a58bb2",
          "face": "adv_chara_145_01_02.png",
          "face_sha256": "4ef3e561795beef0fe996afe979e12e2f638b74317bc24fcd3907c4808bf0b03",
          "native_face_offset": [
            78,
            63
          ],
          "output_sha256": "f2e6379db50f250a7c97442d6a1c396d802b2366dff3af87016ffab5f1b86239"
        },
        {
          "resource": "adv_chara_003_02_10",
          "body": "adv_chara_003_02.png",
          "body_sha256": "81ca424b3db7ec06f59bdef201d73426c018b984f1b1864b82404efe3b25deb9",
          "face": "adv_chara_003_02_10.png",
          "face_sha256": "88eefc306c623c676673843040c0b9e1c152e5084624d7b9dbb91fde0666b1be",
          "native_face_offset": [
            98,
            92
          ],
          "output_sha256": "0db94fb555bcd572aa2f0384b418304dd7425c3de1112f3ff2e6f136e01df380"
        },
        {
          "resource": "adv_chara_133_05_05",
          "body": "adv_chara_133_05.png",
          "body_sha256": "e581949b4f392f1a309f9d5d6fd705a3b8cca23cade4775714a9a02155edf94a",
          "face": "adv_chara_133_05_05.png",
          "face_sha256": "c0aed1b0ba253742a96f8942cb0813e04380e836214dc5a948a7d06565be6e4b",
          "native_face_offset": [
            142,
            66
          ],
          "output_sha256": "9dd9e75c6f430fe3f6671698c901cb09c901282313332b104a211ad51d36e6cb"
        },
        {
          "resource": "adv_chara_002_03_08",
          "body": "adv_chara_002_03.png",
          "body_sha256": "4bb14d813389b79055c4a24b5b3020e06bde9122d7b203b04a5489b358a7f1c7",
          "face": "adv_chara_002_03_08.png",
          "face_sha256": "eeb76812be1f3ae648dc4a29697b89a44bea80b06674296cda3ecb221a0f28b4",
          "native_face_offset": [
            132,
            64
          ],
          "output_sha256": "7ff7b40bcc94113ad178ce1261b241ccc9fc2f653b6694293a865a49756fced9"
        },
        {
          "resource": "adv_obj_0112",
          "body": "adv_obj_0112.png",
          "body_sha256": "b280970e117495bbe685da4a67844fc24374e21d4ac38c9de7500676e47988b4",
          "output_sha256": "152865549a15660808473a2ad6ec50643a506c5b81ca8a124e9e33162229e6de"
        }
      ],
      "coverage_effective_state_sha256": "33a06ee64eff3a91c475c5467b9f089f63e2d793369dd741f861978ae6d738e6",
      "execution_record": "09 Audits and Manifests/T7S_B0100_B0159_EXECUTION_RECORD.md",
      "boundary": "Complete chapter-local text/native state plus selected static review; no authored choice or inline movie; no later-source semantic evidence; performed audio unreviewed."
    },
    "b0142_close_verification": {
      "operation": "T7S_B0142_CLOSE",
      "checked_at": "2026-09-26",
      "status": "PASS_BOUNDED_TEXT_NATIVE_AND_STATIC_REVIEW",
      "episode_ids": [
        "312203701",
        "312203702",
        "312203703"
      ],
      "source_bindings": [
        {
          "episode_id": "312203701",
          "script_id": "ing_102037_01.json__4eec3d5059bfbde9",
          "source_sha256": "26bd4456e952449069732a393a492c1ac3b6983c3b8fc087813247e5588e8309",
          "decoded_sha256": "f4a5e9ba9e957f3d73e8feefb25d77e23e24267f1c3eeec14fcb174f0aeff46d",
          "normalized_sha256": "5754fe245c86bddf79f19904636c58565987037e965854edfe911e02c3f0a502",
          "structured_sha256": "5754fe245c86bddf79f19904636c58565987037e965854edfe911e02c3f0a502",
          "pages": 65,
          "text_records": 62,
          "command_only_pages": 3,
          "voice_pages": 45,
          "native_pages_verified": 65
        },
        {
          "episode_id": "312203702",
          "script_id": "ing_102037_02.json__417fa74381a9d816",
          "source_sha256": "af307cefad8c35764b12749b52daa3dfddf4e3db73b1f1316901b7b83e24a903",
          "decoded_sha256": "402f0745ca219265cc907ddd9a8837e5326cab9a7f9e1e4ea796c2d3f330e11c",
          "normalized_sha256": "07af6bb0205f91f551cfadde903ac97e5ea5d034b5f6e06427791c4b61e51250",
          "structured_sha256": "07af6bb0205f91f551cfadde903ac97e5ea5d034b5f6e06427791c4b61e51250",
          "pages": 54,
          "text_records": 42,
          "command_only_pages": 12,
          "voice_pages": 32,
          "native_pages_verified": 54
        },
        {
          "episode_id": "312203703",
          "script_id": "ing_102037_03.json__c0af14e2be84245f",
          "source_sha256": "d26014c09dee06d4734e2074726705603ff9572f9d717a0963ebea4e9d641380",
          "decoded_sha256": "080b88a8aaea3492efbd697baac10974da4af829ff37d07983b2a9966c77d69a",
          "normalized_sha256": "5b4d90bad3584fa4bab262a2cb96d04fd62af9b4e2d47957f53a362b1b9b17c9",
          "structured_sha256": "5b4d90bad3584fa4bab262a2cb96d04fd62af9b4e2d47957f53a362b1b9b17c9",
          "pages": 53,
          "text_records": 47,
          "command_only_pages": 6,
          "voice_pages": 40,
          "native_pages_verified": 53
        }
      ],
      "totals": {
        "pages": 172,
        "text_records": 151,
        "command_only_pages": 21,
        "voice_pages": 117,
        "visual_refs": 1162
      },
      "voice_count_basis": "Distinct dialogue log-order indexes with voice resource; title-only cues additional; no performed audio reviewed.",
      "native_packet_sha256": "605e30b3a312acff8cde71c11dd4b4dc92259b98ef2d75f46f8771776f370e43",
      "dialogue_packet_sha256": "91a96a4c34d9bd6ec3bb904c13f002be206f67dbd2aaa1ff9cbbdf5322c1ce33",
      "visual_assets": [
        {
          "resource": "adv_chara_146_01_01",
          "body": "adv_chara_146_01.png",
          "body_sha256": "46fc3087e9a017bed96eb313d1311e9f939877b7d723a80efa91284489a7c112",
          "face": "adv_chara_146_01_01.png",
          "face_sha256": "801a2257357486bc74f1a57b3b5329afed804e5b0b0c8712d5d4c9ad690505fe",
          "native_face_offset": [
            81,
            44
          ],
          "output_sha256": "d08286dce366a3675dbb094b32d19834b0e32a730faf6930c3e74bae930d9566"
        },
        {
          "resource": "adv_chara_146_01_02",
          "body": "adv_chara_146_01.png",
          "body_sha256": "46fc3087e9a017bed96eb313d1311e9f939877b7d723a80efa91284489a7c112",
          "face": "adv_chara_146_01_02.png",
          "face_sha256": "ecf0b8ba7e74f17b5328b6e93c55795db32d7211eceedefe000b38d61f6e4a5b",
          "native_face_offset": [
            81,
            44
          ],
          "output_sha256": "79551c4a5c3b39299498d0df479567bf99bf0436e1d75180e6aa314488a55a78"
        },
        {
          "resource": "adv_chara_149_01_01",
          "body": "adv_chara_149_01.png",
          "body_sha256": "99e954f4fe105fc93364cb6978bfe112dd69fe45e6f2cb11cee62fbf83b00624",
          "face": "adv_chara_149_01_01.png",
          "face_sha256": "bb5b4245ffe5fa87521be9d525e7ea0abbe50b196e62834094f210ce3046e4a5",
          "native_face_offset": [
            79,
            59
          ],
          "output_sha256": "3f0f91931eb0fc25d2f20338942093f17e0a75e0df8b1ab54171209b685eff88"
        },
        {
          "resource": "adv_chara_128_01_01",
          "body": "adv_chara_128_01.png",
          "body_sha256": "627e3280d607585cb27dfda5c076a66f36a62cc9b23ce08780dd7fe85513829d",
          "face": "adv_chara_128_01_01.png",
          "face_sha256": "984450530f4a0bda0b2d44ac6eadb17a2f4867424684d0baa9e3309d6732cc1d",
          "native_face_offset": [
            105,
            107
          ],
          "output_sha256": "04e0efd55701ff973ae98c30d2406f7a2c5d4c3987294d966f8e2dc481be258b"
        },
        {
          "resource": "adv_chara_124_01_01",
          "body": "adv_chara_124_01.png",
          "body_sha256": "8bcac9ca97a13c056fec42fba89bd89a106b1ecf4be98535afb69c0c36f2a9fe",
          "face": "adv_chara_124_01_01.png",
          "face_sha256": "143562b5abec14ae3e7ce3b0245c7c4632d70ea6b1cf76d0b81967c674556fb0",
          "native_face_offset": [
            187,
            64
          ],
          "output_sha256": "016f1596228338d4e4977bc9634fc795a7d3ef0593af4763679c6be44a1d0a95"
        },
        {
          "resource": "adv_chara_037_01",
          "body": "adv_chara_037_01.png",
          "body_sha256": "fc3ecb9193f6223b5686d213dcc8f2a9c1afdf39ebca459bff71362d4ba0a5d5",
          "output_sha256": "0b24bb2871d7302a44e59fd3edf0992a2c3a3e057fa4eab02eca0fd022fe3fdc"
        },
        {
          "resource": "adv_chara_027_01",
          "body": "adv_chara_027_01.png",
          "body_sha256": "810a321a0caa3684cb49ee9d614be39546da445df27bd0896e56a6c295b90f97",
          "output_sha256": "d215fdeb03bfde804de0105b121aa682ce9f8d876f8b50948a02898afaecfcf4"
        },
        {
          "resource": "adv_obj_0078",
          "body": "adv_obj_0078.png",
          "body_sha256": "c822bc9d28ced7fd5efc82ddf611faaeacdd98383c96882b7bf20821bdf8ed80",
          "output_sha256": "a31482b98b116e233f99cafac8dc41af452b8a22cd720f7af494d3c77c628fdc"
        }
      ],
      "coverage_effective_state_sha256": "b87de281c1e74fa6036c2ac8d5d1e7798a0d3d3a75a51ff56a4bdcfe5ca91444",
      "execution_record": "09 Audits and Manifests/T7S_B0100_B0159_EXECUTION_RECORD.md",
      "boundary": "Complete chapter-local text/native state plus selected static review; no authored choice or inline movie; no later-source semantic evidence; performed audio unreviewed."
    },
    "b0143_close_verification": {
      "operation": "T7S_B0143_CLOSE",
      "checked_at": "2026-09-26",
      "status": "PASS_BOUNDED_TEXT_NATIVE_AND_STATIC_REVIEW",
      "episode_ids": [
        "312203801",
        "312203802",
        "312203803"
      ],
      "source_bindings": [
        {
          "episode_id": "312203801",
          "script_id": "ing_102038_01.json__72fde96adf8012ac",
          "source_sha256": "f8a8bd5e0f9da2e498e3352f8d3906a55da4c0cd06c0e5327c7e71f9618fe041",
          "decoded_sha256": "4834d584a5a76ab1a835995c5d8c86c5b4cbc74d95bdf6576d220ea7cef1e047",
          "normalized_sha256": "04499b6da3d771314ecab4514561be567e552cce5acf6ad972ba49251d701ab0",
          "structured_sha256": "04499b6da3d771314ecab4514561be567e552cce5acf6ad972ba49251d701ab0",
          "pages": 32,
          "text_records": 29,
          "command_only_pages": 3,
          "voice_pages": 19,
          "native_pages_verified": 32
        },
        {
          "episode_id": "312203802",
          "script_id": "ing_102038_02.json__b3af1443a3a4335c",
          "source_sha256": "a56a770c7eb182de4e9498cdd0526d7861dd846ba10b19dd5a1087b38b917991",
          "decoded_sha256": "bc509f93b1c62280c9e118984493fa4edf04581a45207f277a620709d41b8ecf",
          "normalized_sha256": "fa4565951e60d28d3f6546284d355afac5cfaf3d77fd2af4315020d93d97f147",
          "structured_sha256": "fa4565951e60d28d3f6546284d355afac5cfaf3d77fd2af4315020d93d97f147",
          "pages": 39,
          "text_records": 25,
          "command_only_pages": 14,
          "voice_pages": 20,
          "native_pages_verified": 39
        },
        {
          "episode_id": "312203803",
          "script_id": "ing_102038_03.json__c4768948bba9ee80",
          "source_sha256": "fcf403143aa3630e01987600780ccd38ec48fbee06ed15445146bb63a5c5591e",
          "decoded_sha256": "441c6b6271a449acc04335b65e3c7ad3986a15f54142b2cebcb9663a87d94c8c",
          "normalized_sha256": "6fd57eabd0d4d7653837ee828cac6761d1e8fc12309f9bebce0f55ba530b58b1",
          "structured_sha256": "6fd57eabd0d4d7653837ee828cac6761d1e8fc12309f9bebce0f55ba530b58b1",
          "pages": 62,
          "text_records": 56,
          "command_only_pages": 6,
          "voice_pages": 40,
          "native_pages_verified": 62
        }
      ],
      "totals": {
        "pages": 133,
        "text_records": 110,
        "command_only_pages": 23,
        "voice_pages": 79,
        "visual_refs": 819
      },
      "voice_count_basis": "Distinct dialogue log-order indexes with voice resource; title-only cues additional; no performed audio reviewed.",
      "native_packet_sha256": "116305279f99136f9e9a8c78725b49f4ea507fa049e349108baadd6585306d95",
      "dialogue_packet_sha256": "d48a453813361b4f9b1f33043e4b420a07fa0905cf05b7a89bfc2968ab534e80",
      "visual_assets": [
        {
          "resource": "adv_chara_147_01_01",
          "body": "adv_chara_147_01.png",
          "body_sha256": "df3ba4aa9a0969ae5dbb2f3d8b7e26c938ab1294692d595b12c3090fa8a47982",
          "face": "adv_chara_147_01_01.png",
          "face_sha256": "c97bdaea12f5d9f9bfb81e9ff25f5857cad50a11eb4fa75f0efd392c6f2c6874",
          "native_face_offset": [
            209,
            62
          ],
          "output_sha256": "08c669b14f3c489b3460361737a7d4d1e93fadd065a9f55b874701326f3956de"
        },
        {
          "resource": "adv_chara_147_01_03",
          "body": "adv_chara_147_01.png",
          "body_sha256": "df3ba4aa9a0969ae5dbb2f3d8b7e26c938ab1294692d595b12c3090fa8a47982",
          "face": "adv_chara_147_01_03.png",
          "face_sha256": "b425dcb4e4aa81dee126a29a549706faa3ac8ed578ea2a62d61085fb2d4d42e7",
          "native_face_offset": [
            209,
            62
          ],
          "output_sha256": "ffc811201455c6317889d113ab65a7851d117424772b55baceecc61ffef2c255"
        },
        {
          "resource": "adv_chara_147_01_04",
          "body": "adv_chara_147_01.png",
          "body_sha256": "df3ba4aa9a0969ae5dbb2f3d8b7e26c938ab1294692d595b12c3090fa8a47982",
          "face": "adv_chara_147_01_04.png",
          "face_sha256": "bbbb497cd064596c0e15191fae552209ae3fb9d3fb25e9f38677876ee95dfcbd",
          "native_face_offset": [
            209,
            62
          ],
          "output_sha256": "d59081021329b6f06fd3583c40f5e4ec2e0f0e447708968ec9543615692d5411"
        },
        {
          "resource": "adv_chara_147_01_05",
          "body": "adv_chara_147_01.png",
          "body_sha256": "df3ba4aa9a0969ae5dbb2f3d8b7e26c938ab1294692d595b12c3090fa8a47982",
          "face": "adv_chara_147_01_05.png",
          "face_sha256": "3c7fe6f30a65d203ac767fe46d4de76c5c0ac25de7327a57a7fd02f243fb49c1",
          "native_face_offset": [
            209,
            62
          ],
          "output_sha256": "642fecb3a5f8dce9bf90ca16ef600740b6f05b2e1bfec2faa7fb37de0121c0fc"
        },
        {
          "resource": "adv_chara_011_01_08",
          "body": "adv_chara_011_01.png",
          "body_sha256": "16fc2472d10c8972da16fad1f65b0bbc8c49cfb9daf7ebf2c583e54fedfb6004",
          "face": "adv_chara_011_01_08.png",
          "face_sha256": "a02bbb9aa26326274c620e56e9174c1137bb02a9f48ceb5d0d8dee6dcde4c84b",
          "native_face_offset": [
            89,
            54
          ],
          "output_sha256": "84e4d56c1f90737b8cbd9eadf7531126bb306032dde9156192b14809f395b309"
        },
        {
          "resource": "adv_chara_129_02_03",
          "body": "adv_chara_129_02.png",
          "body_sha256": "3b3561b12d9e97b5c8b46bce7ee758f05f1b08e6aed6a705210707efa3573371",
          "face": "adv_chara_129_02_03.png",
          "face_sha256": "91a194bb7efd8fd18b15de7adaf8649875d650a10b91f3db1e6749425c6713ab",
          "native_face_offset": [
            128,
            72
          ],
          "output_sha256": "0d05f067eb31e3b2e45040e013d8bd6ab8b8b129f3fe7b828f189c3a50d04222"
        },
        {
          "resource": "adv_chara_145_01_02",
          "body": "adv_chara_145_01.png",
          "body_sha256": "e7e4e7d94dadbb80e074cefd5e23ff1fc6cd5fbe2b6f60c39e6ecab367a58bb2",
          "face": "adv_chara_145_01_02.png",
          "face_sha256": "4ef3e561795beef0fe996afe979e12e2f638b74317bc24fcd3907c4808bf0b03",
          "native_face_offset": [
            78,
            63
          ],
          "output_sha256": "f2e6379db50f250a7c97442d6a1c396d802b2366dff3af87016ffab5f1b86239"
        },
        {
          "resource": "adv_chara_040_01",
          "body": "adv_chara_040_01.png",
          "body_sha256": "b31a962e523ec3200fee06279c4f845898bfef5ccf12ae47eaccfad7a9b2eca0",
          "output_sha256": "6ff3db2337ca97918b503b55cdb77e44b0e0a0883a138b868dc9cd33f55c9702"
        }
      ],
      "coverage_effective_state_sha256": "245d05000c1a446dd3960d129bd2dd7549c33d710a194f76ca56662fd14a03c9",
      "execution_record": "09 Audits and Manifests/T7S_B0100_B0159_EXECUTION_RECORD.md",
      "boundary": "Complete chapter-local text/native state plus selected static review; no authored choice or inline movie; no later-source semantic evidence; performed audio unreviewed."
    },
    "b0144_close_verification": {
      "operation": "T7S_B0144_CLOSE",
      "checked_at": "2026-09-26",
      "status": "PASS_BOUNDED_TEXT_NATIVE_AND_STATIC_REVIEW",
      "episode_ids": [
        "612200101",
        "612200102",
        "612200103"
      ],
      "source_bindings": [
        {
          "episode_id": "612200101",
          "script_id": "ing3_102001_01.json__542bb424f1a4f19a",
          "source_sha256": "97754c388d28325604d7412f25e7bfcce743cde7d196b8c150105b72b8f07ccd",
          "decoded_sha256": "8717e336cd79cbfc9a8f43bd971316d45845332cf4e0131f4e75ad9f0dad52b5",
          "normalized_sha256": "d8d1bf1efa036f27385e1ee5d9874676852b4fa59fc231c9d521001252fc93e6",
          "structured_sha256": "d8d1bf1efa036f27385e1ee5d9874676852b4fa59fc231c9d521001252fc93e6",
          "pages": 93,
          "text_records": 79,
          "command_only_pages": 14,
          "voice_pages": 60,
          "native_pages_verified": 93
        },
        {
          "episode_id": "612200102",
          "script_id": "ing3_102001_02.json__97b4f8bb7230c5af",
          "source_sha256": "fea9119b6fb79691b5eac66e4275ff996f6a15eec1ac46cf5e169a36cd9e50ee",
          "decoded_sha256": "fa761b80813326383868eff374eb3eed578c4a36627a268931542e2bd25f9470",
          "normalized_sha256": "849848289f7c7ab0fb7e3dd5a404726cf6c37dc3b78ffb4e0e34c0a908267fed",
          "structured_sha256": "849848289f7c7ab0fb7e3dd5a404726cf6c37dc3b78ffb4e0e34c0a908267fed",
          "pages": 86,
          "text_records": 79,
          "command_only_pages": 7,
          "voice_pages": 79,
          "native_pages_verified": 86
        },
        {
          "episode_id": "612200103",
          "script_id": "ing3_102001_03.json__3d214c380978e21f",
          "source_sha256": "91c77ceed554a8d0baab93f5a6aa83fbdc4081834dd042c67af822c9bbec3a91",
          "decoded_sha256": "4515b73dfd66ce24448bfd61b7c707b858af155ff0cb6cf92bd9220da56d32bc",
          "normalized_sha256": "08315fa4867ba8a31b9c6e608aec9c20adccc7ceaf87296c3fc622ff12d3bd5b",
          "structured_sha256": "08315fa4867ba8a31b9c6e608aec9c20adccc7ceaf87296c3fc622ff12d3bd5b",
          "pages": 97,
          "text_records": 76,
          "command_only_pages": 21,
          "voice_pages": 59,
          "native_pages_verified": 97
        }
      ],
      "totals": {
        "pages": 276,
        "text_records": 234,
        "command_only_pages": 42,
        "voice_pages": 198,
        "visual_refs": 2824
      },
      "voice_count_basis": "Distinct dialogue log-order indexes with voice resource; title-only cues additional; no performed audio reviewed.",
      "native_packet_sha256": "b653aac2e266c5824a431bff648e48962b6fdd610f500ea88aa1360c8041be9a",
      "dialogue_packet_sha256": "aa08a47e2ccfcec1283de9462a42644a9889fa3576b4d42dc26cbad9bda00468",
      "visual_assets": [
        {
          "resource": "adv_chara_003_01_15",
          "body": "adv_chara_003_01.png",
          "body_sha256": "cfd3a3dd39c6fd67b6ffc63190a2da76e8d1ef5cedcb8eb895afd2a9bd870064",
          "face": "adv_chara_003_01_15.png",
          "face_sha256": "db40498b8146a9523a96f19768e8f6dacce12589719ffb55933d731a6abca5cc",
          "native_face_offset": [
            98,
            92
          ],
          "output_sha256": "eb37c618b8433165c54168434b09fd165790b9651a6abe317fe9ee5a44323468"
        },
        {
          "resource": "adv_chara_003_09_04",
          "body": "adv_chara_003_09.png",
          "body_sha256": "9ecad20ec37b6f79c3b26635384ec6d05773cc8c86d035a663b0b3816138f503",
          "face": "adv_chara_003_09_04.png",
          "face_sha256": "a5f7084909550f806945052fbfc12967aecb8521099b3a74bb78b868ff4deb83",
          "native_face_offset": [
            108,
            92
          ],
          "output_sha256": "c622f5171871acbdeb602e01f374c3d593003f1dffedc166ab0e12b72af36e40"
        },
        {
          "resource": "adv_chara_003_09_05",
          "body": "adv_chara_003_09.png",
          "body_sha256": "9ecad20ec37b6f79c3b26635384ec6d05773cc8c86d035a663b0b3816138f503",
          "face": "adv_chara_003_09_05.png",
          "face_sha256": "fbbaf1283c650ea8161600bb701eb08cb84327d33ec8fb4d4c3af7020d7b7675",
          "native_face_offset": [
            108,
            92
          ],
          "output_sha256": "16b283bb05d7c0f44ee729ce132451660813f649a65fef40e2ff99a50fefadd7"
        },
        {
          "resource": "adv_chara_010_01_02",
          "body": "adv_chara_010_01.png",
          "body_sha256": "ac05f3cd59cf77b2e8a37a23f406bd671a62496ebe681ec9bf0983fc6c843168",
          "face": "adv_chara_010_01_02.png",
          "face_sha256": "6b0f9429d27ad703b8f7e98e3fb7c898757cea51e7676db2de77742ab1d52503",
          "native_face_offset": [
            150,
            104
          ],
          "output_sha256": "49dad82a25a931b7556bd121b4481b835e863671718daa55813abfc5a33b971d"
        },
        {
          "resource": "adv_chara_006_01_05",
          "body": "adv_chara_006_01.png",
          "body_sha256": "d40ded643748164bb05d319c4a3889a41f99d102a3fcfeb60675b59529a6c392",
          "face": "adv_chara_006_01_05.png",
          "face_sha256": "4358c5a3ca68737fd4b6a1afa0edc2094c8ba9ed3985d0d71dea87f59ceca6b8",
          "native_face_offset": [
            134,
            91
          ],
          "output_sha256": "b1605bd99b38c2eb79e4dc83c899affa69c635b1c323fa57b217f3e3d4826fa7"
        },
        {
          "resource": "adv_chara_014_01_06",
          "body": "adv_chara_014_01.png",
          "body_sha256": "b8665daef47ba3fbf338538586adc18c16ed72c65092ad9d57cf2a4f128f3677",
          "face": "adv_chara_014_01_06.png",
          "face_sha256": "5d33ee9fd5886e7ceb6c858a98c5457c079a5032f6b823b4b2a49a95e96cc85f",
          "native_face_offset": [
            128,
            78
          ],
          "output_sha256": "07fdf3d9b19e57fce471ebd1f9dd1e74549cb46212b63d111b155edebb84cb02"
        },
        {
          "resource": "adv_chara_012_01_01",
          "body": "adv_chara_012_01.png",
          "body_sha256": "d142646f64071ed43061fd75721befa778228cd90a1c9d04fd996d739fc468b9",
          "face": "adv_chara_012_01_01.png",
          "face_sha256": "48fb3d5af2ec98fe05dd274e15e82fd680c07f6723ab0a2f5dceb188b7fcffd7",
          "native_face_offset": [
            59,
            74
          ],
          "output_sha256": "1a3b01fe595284bb8b645118dd34a3df4190b302bad562466afad619b5724c2b"
        },
        {
          "resource": "adv_chara_004_01_17",
          "body": "adv_chara_004_01.png",
          "body_sha256": "5d8b60092117906b699d98ccabfc88344ea61f82e9b27a23bec1fa15d0cb65be",
          "face": "adv_chara_004_01_17.png",
          "face_sha256": "7728206d121dd15b51bdda76a695e7d4589efa4d064c7da09ceb238bfa1617bc",
          "native_face_offset": [
            194,
            74
          ],
          "output_sha256": "c468cd213eabc4df4e2fe2296df56d4a75b1a5e00fadf6c3a7e5dd4640d6590d"
        },
        {
          "resource": "adv_obj_0150",
          "body": "adv_obj_0150.png",
          "body_sha256": "837eea14b33e06c957ee42bb71d4f40376c141446a0921f979febae38deeaf33",
          "output_sha256": "6cf55a0f61a3d19ff9e1379ebe7ffd3fb09b79c04ac8800c6a5686fb049dc5fb"
        },
        {
          "resource": "adv_obj_0151",
          "body": "adv_obj_0151.png",
          "body_sha256": "21cd4a25f61c29c2248f79dc616bbe828ab43a04b404c2dd69213895411bea41",
          "output_sha256": "b17edfaca39c42ffd7682d3c7544af68a03d97015cc4eee5db46ef5426652dbd"
        },
        {
          "resource": "adv_obj_0152",
          "body": "adv_obj_0152.png",
          "body_sha256": "552f6bd72e7dfac09eb42284ee606eaa100a47ffcd9c2773f4d0f5adbaab4d55",
          "output_sha256": "ed74dab8bf09e5e90bc5e095c4dd1270bf71cae121b5a934285c85b9ef33925a"
        }
      ],
      "coverage_effective_state_sha256": "cab3964bfb48da53233b712308f5279f8ae5cee7b045646c40cc88e93097b7b4",
      "execution_record": "09 Audits and Manifests/T7S_B0100_B0159_EXECUTION_RECORD.md",
      "boundary": "Complete chapter-local text/native state plus selected static review; no authored choice or inline movie; no later-source semantic evidence; performed audio unreviewed."
    },
    "b0145_close_verification": {
      "operation": "T7S_B0145_CLOSE",
      "checked_at": "2026-09-26",
      "status": "PASS_BOUNDED_TEXT_NATIVE_AND_STATIC_REVIEW",
      "episode_ids": [
        "612200201",
        "612200202",
        "612200203"
      ],
      "source_bindings": [
        {
          "episode_id": "612200201",
          "script_id": "ing3_102002_01.json__0cb9d3190c08cfd0",
          "source_sha256": "faab22b87eb8f5e4d3e5404cc201f639fa95346d9fc225646855738375e21938",
          "decoded_sha256": "ec41ee0c82f7e4f71390c2bb06548398fef4621cad0d4be1f715f057192c0999",
          "normalized_sha256": "f131a6c11a17f45c0613e91d9b9c4af6071cb30c4f21dcd854558e27a8884073",
          "structured_sha256": "f131a6c11a17f45c0613e91d9b9c4af6071cb30c4f21dcd854558e27a8884073",
          "pages": 95,
          "text_records": 82,
          "command_only_pages": 13,
          "voice_pages": 56,
          "native_pages_verified": 95
        },
        {
          "episode_id": "612200202",
          "script_id": "ing3_102002_02.json__2c27306569ab2062",
          "source_sha256": "4ca6c7b6ea789867a181541ce46d4faa9d60834d8199a56a9792433439e1cbf8",
          "decoded_sha256": "5720b2e8005c6cc799ad4a911d5641278fd8eae1073b09d562a51d0a759d3049",
          "normalized_sha256": "4cbb2674e5ce53d4180ef45d319aa9c055d01e3b4d27b2bdf4577a93ccb5ad78",
          "structured_sha256": "4cbb2674e5ce53d4180ef45d319aa9c055d01e3b4d27b2bdf4577a93ccb5ad78",
          "pages": 186,
          "text_records": 151,
          "command_only_pages": 35,
          "voice_pages": 91,
          "native_pages_verified": 186
        },
        {
          "episode_id": "612200203",
          "script_id": "ing3_102002_03.json__8e267eba9365f1cd",
          "source_sha256": "d815ba5dc00a8860e31c64f6584d32f8a43dc2f7dfca610f0cf48bd853b7b7f2",
          "decoded_sha256": "7a3d0abe9ce7007430137ae7f0744c6f64882026394beee665468c4c2ac69abc",
          "normalized_sha256": "a290bc454b2dc29bf405cfa3dd130ec0f2879783030c1f3c97dccc12a678ee84",
          "structured_sha256": "a290bc454b2dc29bf405cfa3dd130ec0f2879783030c1f3c97dccc12a678ee84",
          "pages": 169,
          "text_records": 152,
          "command_only_pages": 17,
          "voice_pages": 73,
          "native_pages_verified": 169
        }
      ],
      "totals": {
        "pages": 450,
        "text_records": 385,
        "command_only_pages": 65,
        "voice_pages": 220,
        "visual_refs": 4837
      },
      "voice_count_basis": "Distinct dialogue log-order indexes with voice resource; title-only cues additional; no performed audio reviewed.",
      "native_packet_sha256": "918e9177c2105aacf3529b866074a3ba7063f29f6753079c7ead76aea2ffd321",
      "dialogue_packet_sha256": "c43950214126f29e37600e7999743403a3206e2d4e9902b1b6286a8330e7bacb",
      "visual_assets": [
        {
          "resource": "adv_chara_004_01_22",
          "body": "adv_chara_004_01.png",
          "body_sha256": "5d8b60092117906b699d98ccabfc88344ea61f82e9b27a23bec1fa15d0cb65be",
          "face": "adv_chara_004_01_22.png",
          "face_sha256": "d2183810c0daea1272c02a7e88fbf2fe4b25419579692de5de56f3078a12ec49",
          "native_face_offset": [
            194,
            74
          ],
          "output_sha256": "fee7bb5c819408e7a92f203713028038124495f47fe575a4c5926c3831a7d465"
        },
        {
          "resource": "adv_chara_004_06_22",
          "body": "adv_chara_004_06.png",
          "body_sha256": "2fa07637cb12479aa6a36a4d33fcda9dadc4f265786390ccbfdae5beb4279b75",
          "face": "adv_chara_004_06_22.png",
          "face_sha256": "f747e4f6f4ccc673c3e80319164ceef50b1ccc5ab22055c771b83089f7df82d4",
          "native_face_offset": [
            194,
            74
          ],
          "output_sha256": "1b42d67740b25ead024707668d455feba72fc50e4f014e73f0793c4d6311b7e9"
        },
        {
          "resource": "adv_chara_004_04_08",
          "body": "adv_chara_004_04.png",
          "body_sha256": "8e2b351704a00f1fba0d55a2074251c17db34706506673c978aa87c8c22de7ae",
          "face": "adv_chara_004_04_08.png",
          "face_sha256": "b0d5660d9be172a6b50aa6627ae920c66be00c1aeff7088f9d831d71277fb610",
          "native_face_offset": [
            194,
            74
          ],
          "output_sha256": "bcfecf75403f35c4470e832ac6e997c40589dc6d2ea1965581ce7618e3d6d9b2"
        },
        {
          "resource": "adv_chara_011_05_05",
          "body": "adv_chara_011_05.png",
          "body_sha256": "52eabf25d0efedbf44676da80f8be5d81557d65bc9cf2152a341c9d504db91c0",
          "face": "adv_chara_011_05_05.png",
          "face_sha256": "f216ab148ae0b52db5180bf860d1643f5d98cdaaa88a880611ab08c33d52763f",
          "native_face_offset": [
            89,
            54
          ],
          "output_sha256": "eb4f27e6b5e902d82561c4310bfe69e8575acc194cdb16277ae4b847560e06f4"
        },
        {
          "resource": "adv_chara_010_01_09",
          "body": "adv_chara_010_01.png",
          "body_sha256": "ac05f3cd59cf77b2e8a37a23f406bd671a62496ebe681ec9bf0983fc6c843168",
          "face": "adv_chara_010_01_09.png",
          "face_sha256": "59892c874433b4f16bc92afe202a72fcf403dd47e8478ed5c6605a12b6156b89",
          "native_face_offset": [
            150,
            104
          ],
          "output_sha256": "32eebfe4e0310945012fe72f1f500109db925f1541bd8b00e78351078a711dcf"
        },
        {
          "resource": "adv_chara_002_03_01",
          "body": "adv_chara_002_03.png",
          "body_sha256": "4bb14d813389b79055c4a24b5b3020e06bde9122d7b203b04a5489b358a7f1c7",
          "face": "adv_chara_002_03_01.png",
          "face_sha256": "44744b274cd5f728379c329e9a722c0639e1fab23ae5e846a483a3f131e80e14",
          "native_face_offset": [
            132,
            64
          ],
          "output_sha256": "59b13c2655e6f3619ff902a52aac22ff6c10c4c63f17d56ed1b58b339f46165c"
        },
        {
          "resource": "adv_chara_026_01",
          "body": "adv_chara_026_01.png",
          "body_sha256": "435520dbdfcecb1be65373f7f826393b5d36197f949ad969a335ce7d5f06d36b",
          "output_sha256": "79e882ee1c05288a7be068b74a60b1d28afeeec0801c38d7ba9b23321b935aad"
        },
        {
          "resource": "adv_chara_025_01",
          "body": "adv_chara_025_01.png",
          "body_sha256": "ac49f2c40ad43d558d14951f8ab879b5204c6b62f03d637176e97b00883f755b",
          "output_sha256": "d2b28f770664736a9c8d7b99b5ff985cd47674a82923709e7694ebd61b586b36"
        },
        {
          "resource": "adv_chara_003_02_08",
          "body": "adv_chara_003_02.png",
          "body_sha256": "81ca424b3db7ec06f59bdef201d73426c018b984f1b1864b82404efe3b25deb9",
          "face": "adv_chara_003_02_08.png",
          "face_sha256": "2b26ec3efb4e35cb11eb963b11c1d8ba22a15585019eb839b8c2674270726f23",
          "native_face_offset": [
            98,
            92
          ],
          "output_sha256": "3e0fcb3ea8dabf9aa3fe8003c45ca9ac7ad2c92adda0e39478156ae883a5ce56"
        }
      ],
      "coverage_effective_state_sha256": "3467d258df2c394e67efab64d18b1757e1c65e7ef077ce1eea6ff4fc93177509",
      "execution_record": "09 Audits and Manifests/T7S_B0100_B0159_EXECUTION_RECORD.md",
      "boundary": "Complete chapter-local text/native state plus selected static review; no authored choice or inline movie; no later-source semantic evidence; performed audio unreviewed."
    },
    "b0146_close_verification": {
      "operation": "T7S_B0146_CLOSE",
      "checked_at": "2026-09-26",
      "status": "PASS_BOUNDED_TEXT_NATIVE_AND_STATIC_REVIEW",
      "episode_ids": [
        "612200301",
        "612200302",
        "612200303"
      ],
      "source_bindings": [
        {
          "episode_id": "612200301",
          "script_id": "ing3_102003_01.json__ea2f54bad67fbd41",
          "source_sha256": "ec45e746ed6dc4423a44a976d0ae939c2acf6d7399259d19f26a8924cc67a8bd",
          "decoded_sha256": "e9385bad3d9e094bd0bc507d1bf1acdfe81a8c36a279992f494ae301feba748d",
          "normalized_sha256": "5340d0c941927fbdfbe2afded3649fabb3c4e0d433fa615e2fd664cecea9afb2",
          "structured_sha256": "5340d0c941927fbdfbe2afded3649fabb3c4e0d433fa615e2fd664cecea9afb2",
          "pages": 64,
          "text_records": 57,
          "command_only_pages": 7,
          "voice_pages": 48,
          "native_pages_verified": 64
        },
        {
          "episode_id": "612200302",
          "script_id": "ing3_102003_02.json__6ece0ab1fddda651",
          "source_sha256": "744ef84699c3e0d125f79a2aa332108a6ed759ba02783abb24c8890490eebd57",
          "decoded_sha256": "12811abf3f251c01bf5920538e4d55a05731f1e544f457ad6ffd18b8dfcd2b99",
          "normalized_sha256": "25f5031f55525f4898ff4949c021af5d17a30ef4cdf48dd4c77e2fadbf9cb2e8",
          "structured_sha256": "25f5031f55525f4898ff4949c021af5d17a30ef4cdf48dd4c77e2fadbf9cb2e8",
          "pages": 108,
          "text_records": 90,
          "command_only_pages": 18,
          "voice_pages": 72,
          "native_pages_verified": 108
        },
        {
          "episode_id": "612200303",
          "script_id": "ing3_102003_03.json__249df5ee371188f1",
          "source_sha256": "687a87c942dc0c794f54c93f3263206d24d1955dd64bef2ed7c7d95ec89bf18a",
          "decoded_sha256": "9c566352afa2a05d11edd73dd58949b4b5f7132f85bde0cce65ec04feb192b28",
          "normalized_sha256": "09c6c8b9b7a151d5d7a63e993fedb50419a1e52a62470a56d142c3f8585d430e",
          "structured_sha256": "09c6c8b9b7a151d5d7a63e993fedb50419a1e52a62470a56d142c3f8585d430e",
          "pages": 145,
          "text_records": 126,
          "command_only_pages": 19,
          "voice_pages": 75,
          "native_pages_verified": 145
        }
      ],
      "totals": {
        "pages": 317,
        "text_records": 273,
        "command_only_pages": 44,
        "voice_pages": 195,
        "visual_refs": 2439
      },
      "voice_count_basis": "Distinct dialogue log-order indexes with voice resource; title-only cues additional; no performed audio reviewed.",
      "native_packet_sha256": "f6d9bd01018870827dd32d0c7b75d61682f8417d07c62fae520e10b517904297",
      "dialogue_packet_sha256": "f66bc23a474ca943e33247f116955c098e71a3e6aebae8ae92cf2b3aa47febe0",
      "visual_assets": [
        {
          "resource": "adv_chara_005_07_01",
          "body": "adv_chara_005_07.png",
          "body_sha256": "669800c2c0d3e46d13f8c901a6fde2ffc34297bbb5da126342875e969acaca8e",
          "face": "adv_chara_005_07_01.png",
          "face_sha256": "e99eee9a2a874aefc832a87ee2fe8575a8002b8eff49156e02587d2d3b9c0d58",
          "native_face_offset": [
            76,
            85
          ],
          "output_sha256": "27dee514244f96615b3b1467d2d3c9d91269aaff290d21f5499402cd01b7152e"
        },
        {
          "resource": "adv_chara_005_01_04",
          "body": "adv_chara_005_01.png",
          "body_sha256": "5eacc7b48f482d043fd5ebcb64d978a16ea335fd2c83a4b641983d2938444f21",
          "face": "adv_chara_005_01_04.png",
          "face_sha256": "ad98aa82a2fae4dfb7e1788688004d0549b3b52c86f26608b9b85e89998cca88",
          "native_face_offset": [
            76,
            85
          ],
          "output_sha256": "9335b3959b31b6bb77cbb834d0151071dd8ccecd28dbee2097aecb73087f68cd"
        },
        {
          "resource": "adv_chara_005_01_01",
          "body": "adv_chara_005_01.png",
          "body_sha256": "5eacc7b48f482d043fd5ebcb64d978a16ea335fd2c83a4b641983d2938444f21",
          "face": "adv_chara_005_01_01.png",
          "face_sha256": "087da32ef5957a1827c9ba84e43c2e8e4d19b71d55561220f01057f33768af2a",
          "native_face_offset": [
            76,
            85
          ],
          "output_sha256": "08577674aaec962626b0189c6933a38fa2c4a709874b6ebf768ea9364402d105"
        },
        {
          "resource": "adv_chara_023_01",
          "body": "adv_chara_023_01.png",
          "body_sha256": "3fd815ee09c3188f1f3851d046ceb8de19f2d7aa7afa552c1e2c2e07f60688af",
          "output_sha256": "06a85428681d0e36ca6f80f9c00737488546c0953a17a4bf167003058d026fb3"
        },
        {
          "resource": "adv_chara_002_07_01",
          "body": "adv_chara_002_07.png",
          "body_sha256": "e299b2ccb8f49c9014aa59242afb0c5fb260b54d819620e7d17728597f06c015",
          "face": "adv_chara_002_07_01.png",
          "face_sha256": "98f0505282bf20e08955869bcbbe697e33472d041689970983ea023328825f9d",
          "native_face_offset": [
            132,
            64
          ],
          "output_sha256": "b8841c7581fe3e042083832122c3d080b2c404937eaf5d558d5d7d6bd54474ea"
        },
        {
          "resource": "adv_chara_003_06_04",
          "body": "adv_chara_003_06.png",
          "body_sha256": "a41fb44cc61027bc6f9f0a44fe7ff477be4bd04e6e671c3d77d6efbfdf7fc55e",
          "face": "adv_chara_003_06_04.png",
          "face_sha256": "50ba658dd9bc2fe8a967a5f329a27feee656e0520dfed6c6e4d8e6a3e075d7ab",
          "native_face_offset": [
            98,
            92
          ],
          "output_sha256": "534055ec859b854627e7c380f3961e3b4a7af9391165ac56166d9f86bb0e5340"
        },
        {
          "resource": "adv_chara_013_03_01",
          "body": "adv_chara_013_03.png",
          "body_sha256": "92050b6b91789e040270af209db2e8f7073dbf2732cf835f0846a64a1191dd02",
          "face": "adv_chara_013_03_01.png",
          "face_sha256": "fe126914c29b85d5b39fc0ca7e017c91ad52ba1d372b046f30c0e20c56f75ecd",
          "native_face_offset": [
            105,
            60
          ],
          "output_sha256": "c3823359367b66f8005fcf01363d5c3c4566dcca260cd00ee4c6b2de21c6b113"
        },
        {
          "resource": "adv_chara_004_01_05",
          "body": "adv_chara_004_01.png",
          "body_sha256": "5d8b60092117906b699d98ccabfc88344ea61f82e9b27a23bec1fa15d0cb65be",
          "face": "adv_chara_004_01_05.png",
          "face_sha256": "d33567411d5de61bb7060fa8c50ed1242c479810eafe455f0a1b8106fd7463a4",
          "native_face_offset": [
            194,
            74
          ],
          "output_sha256": "54e3487d89e826843cfb32c814eb2a27bd91293fcea2d3a2b9393a5dd9f775bd"
        }
      ],
      "coverage_effective_state_sha256": "92b75d0212d443164d63d6b98de7ffb61f1860f76f68a52268c0e9a189024e3e",
      "execution_record": "09 Audits and Manifests/T7S_B0100_B0159_EXECUTION_RECORD.md",
      "boundary": "Complete chapter-local text/native state plus selected static review; no authored choice or inline movie; no later-source semantic evidence; performed audio unreviewed."
    },
    "b0147_close_verification": {
      "operation": "T7S_B0147_CLOSE",
      "checked_at": "2026-09-26",
      "status": "PASS_BOUNDED_TEXT_NATIVE_AND_STATIC_REVIEW",
      "episode_ids": [
        "612200401",
        "612200402",
        "612200403"
      ],
      "source_bindings": [
        {
          "episode_id": "612200401",
          "script_id": "ing3_102004_01.json__ce10787e289bf5f4",
          "source_sha256": "cb7f3d8b235192d27927c48afa618722f8fffb43f3c64f808efe1f768befa030",
          "decoded_sha256": "3b0d03a6ae4c18382cd564ba21873dbfef544d3d8a604af86722ee81ea0bf5b9",
          "normalized_sha256": "24f4203e7e6fd3ce4d6dddee5c6c0186f0ca3ad8c0ceb2b589acfd0c5f517f37",
          "structured_sha256": "24f4203e7e6fd3ce4d6dddee5c6c0186f0ca3ad8c0ceb2b589acfd0c5f517f37",
          "pages": 159,
          "text_records": 129,
          "command_only_pages": 30,
          "voice_pages": 111,
          "native_pages_verified": 159
        },
        {
          "episode_id": "612200402",
          "script_id": "ing3_102004_02.json__c08733a3ab401d8b",
          "source_sha256": "f007b30b7936c147c9162cbc10a25e206959b0d33f08eb61e7be64d7ca2fca2c",
          "decoded_sha256": "78fcba2a8ae93a59b93982e1cc040baf58e85cee447e5cc909dfd5c4d84d8f8f",
          "normalized_sha256": "a0d741eead0958e0ea96f367e572ad2e23c362056d39010e24a3badb923c7e09",
          "structured_sha256": "a0d741eead0958e0ea96f367e572ad2e23c362056d39010e24a3badb923c7e09",
          "pages": 137,
          "text_records": 120,
          "command_only_pages": 17,
          "voice_pages": 84,
          "native_pages_verified": 137
        },
        {
          "episode_id": "612200403",
          "script_id": "ing3_102004_03.json__b29fb47374a7f958",
          "source_sha256": "fa57a9aeda521e37b48c192bee40dcb3aff630e411adaf49c85ff280536e704a",
          "decoded_sha256": "42cf219d713f83859c224171707e31925ca68c9c978e97afb87db1d91d821394",
          "normalized_sha256": "79a8e8a8bb21ed8c23c2b6821061db35fc1f8f21639c44c5ebcfe35c7fcbeda9",
          "structured_sha256": "79a8e8a8bb21ed8c23c2b6821061db35fc1f8f21639c44c5ebcfe35c7fcbeda9",
          "pages": 129,
          "text_records": 93,
          "command_only_pages": 36,
          "voice_pages": 59,
          "native_pages_verified": 129
        }
      ],
      "totals": {
        "pages": 425,
        "text_records": 342,
        "command_only_pages": 83,
        "voice_pages": 254,
        "visual_refs": 4348
      },
      "voice_count_basis": "Distinct dialogue log-order indexes with voice resource; title-only cues additional; no performed audio reviewed.",
      "native_packet_sha256": "587369b15e730079158bfb8260c376b22c579161b433c0c5c50b76bf19518a8c",
      "dialogue_packet_sha256": "ebcfba5185a9b78b922ec9087fb0479876bc60ca8d12774bdaf0245ce355f66f",
      "visual_assets": [
        {
          "resource": "adv_chara_006_01_01",
          "body": "adv_chara_006_01.png",
          "body_sha256": "d40ded643748164bb05d319c4a3889a41f99d102a3fcfeb60675b59529a6c392",
          "face": "adv_chara_006_01_01.png",
          "face_sha256": "f0b4ac890758947d8c9d96bbe5586eb8a06696cf88dc64fc805a27d544c71519",
          "native_face_offset": [
            134,
            91
          ],
          "output_sha256": "b7d30980c8b8f1232502f7de7c0892fd124efe982ad0e843cdf182cdbc4c2896"
        },
        {
          "resource": "adv_chara_006_06_01",
          "body": "adv_chara_006_06.png",
          "body_sha256": "29431c3bc4dc12d0b99208c925005183b9bd10dcfc7ca2323b2359a67b05a3a8",
          "face": "adv_chara_006_06_01.png",
          "face_sha256": "44e2c6118762fb3daf32d99841ce2a814cbb718a6eb8ff66149eeb7c79da93d7",
          "native_face_offset": [
            134,
            91
          ],
          "output_sha256": "f8d9b4dbed41b29335c16a75e28c4923f901769dbd0fc86369caffb911205a14"
        },
        {
          "resource": "adv_chara_006_07_01",
          "body": "adv_chara_006_07.png",
          "body_sha256": "057cef3f79987120e579f6a4797b9c988abb56a69ea6aed0848f4e951e38b134",
          "face": "adv_chara_006_07_01.png",
          "face_sha256": "c2e8245dd3d0a87f310d4296e9446a7e99687713123dddd7ee98181419ed2b92",
          "native_face_offset": [
            134,
            91
          ],
          "output_sha256": "d5f0d4d1b338e37bb52703a385374100917d378e0f422ce898fd75a5c91cbc9b"
        },
        {
          "resource": "adv_chara_006_08_01",
          "body": "adv_chara_006_08.png",
          "body_sha256": "568d30d8fa638f835a1248757468db40776e400ef904d04f30e15ec0e4a93658",
          "face": "adv_chara_006_08_01.png",
          "face_sha256": "75f42a32c2eb87931f3b907720338e014df24ad2576884be97322a55f55f74dd",
          "native_face_offset": [
            134,
            91
          ],
          "output_sha256": "0bbc34b4ca52fecdf841e39d992693f2d1df85cda4b7f36ca62ff8817d4a162e"
        },
        {
          "resource": "adv_chara_010_04_01",
          "body": "adv_chara_010_04.png",
          "body_sha256": "11998ea8dfd3b6e3fa9058bf650311d5715c2ffd05055644b70d2d0144f71e4f",
          "face": "adv_chara_010_04_01.png",
          "face_sha256": "4374fea41ce4bd55f9394876a55b42731cf7a11310a4bc4c16b930c7c38e9c0b",
          "native_face_offset": [
            176,
            104
          ],
          "output_sha256": "587b482d52c112d2f0804a9b85d2d55aaf3a448f5e6853a8924795adcef10dc8"
        },
        {
          "resource": "adv_chara_002_12_01",
          "body": "adv_chara_002_12.png",
          "body_sha256": "4be092a9ae922002f4360ac55f4feea518ab06f62cf7d3b35e43eabe4df9f158",
          "face": "adv_chara_002_12_01.png",
          "face_sha256": "55fbade9e0e752c15e6375a9fde6df50835bbd3e9c9e8b3d52530dc5274a6c0b",
          "native_face_offset": [
            230,
            64
          ],
          "output_sha256": "5c972122ce07055839a1813fea6f43a9394a9e7ec7f3947405786953cace7c62"
        },
        {
          "resource": "adv_chara_028_01",
          "body": "adv_chara_028_01.png",
          "body_sha256": "b7cd9bbbc28c6ca3d69e98feecd003ac336326021cba303942407e5d561a72bf",
          "output_sha256": "98a121d6f7250f9dca69d313ea1077930bd1c8d6d4c268a8c349dca660aac2c0"
        },
        {
          "resource": "adv_chara_029_01",
          "body": "adv_chara_029_01.png",
          "body_sha256": "5e14c1d3e5bd683050f21c156125d9622b1c5fa9b2a061de96f2e233399a4654",
          "output_sha256": "6360b68147e58754f2d8d59ffc273de330e26f0d042a17e89fc08cb9bfbbb5a2"
        },
        {
          "resource": "adv_chara_030_01",
          "body": "adv_chara_030_01.png",
          "body_sha256": "744f975ebfb9b66c7e9d63fdba35451045becbe6b1e0c2c9e20298cde9bce04f",
          "output_sha256": "6224afa1c784b9d4f21fbcb2a61eb386d784ec807ec29912d4b5d46b501146a6"
        },
        {
          "resource": "adv_chara_038_01",
          "body": "adv_chara_038_01.png",
          "body_sha256": "e7f35df30d8860f553a5bedc452a601515f2c0bd2fc28f458e71df798e742526",
          "output_sha256": "8680f95acf1b40c8cba4b899230ed93bc0bfb75d63924e775b91a86429397f50"
        },
        {
          "resource": "adv_chara_041_01",
          "body": "adv_chara_041_01.png",
          "body_sha256": "3b0eca8698583351944125aa1b068171ebc7edffc58620c74ad49ead6fa01663",
          "output_sha256": "81280039b415d765e44f72fd1852658a4980179097723de60b95dc31609a5c5c"
        },
        {
          "resource": "adv_obj_0008",
          "body": "adv_obj_0008.png",
          "body_sha256": "42f50c3884b9e5ec2a8cb5a1bdeda2afde1d5bf78f38e9506e2f2d1841da994a",
          "output_sha256": "68be87278a150b2370ac89167bc32eee877de87b603c56df0b042ebc7f8f01c9"
        },
        {
          "resource": "adv_chara_009_03_01",
          "body": "adv_chara_009_03.png",
          "body_sha256": "ffc2406a944338eecacf731a83cc2ecfedce4b3e932bcbf3574528e5939035c8",
          "face": "adv_chara_009_03_01.png",
          "face_sha256": "3930e1f45971c7020b6faf9806089ec8aad2c2bb2d100c0270a687c519899f6a",
          "native_face_offset": [
            109,
            85
          ],
          "output_sha256": "b68b10b4530c261991b4afa29dd60a3716090e68734c8a2b542708567dd98343"
        }
      ],
      "coverage_effective_state_sha256": "67371b476ac26f94faf25419118d6c93d9e014a2a72be4cef3f660c4e96740dc",
      "execution_record": "09 Audits and Manifests/T7S_B0100_B0159_EXECUTION_RECORD.md",
      "boundary": "Complete chapter-local text/native state plus selected static review; no authored choice or inline movie; no later-source semantic evidence; performed audio unreviewed."
    },
    "b0148_close_verification": {
      "operation": "T7S_B0148_CLOSE",
      "checked_at": "2026-09-26",
      "status": "PASS_BOUNDED_TEXT_NATIVE_AND_STATIC_REVIEW",
      "episode_ids": [
        "612200501",
        "612200502",
        "612200503"
      ],
      "source_bindings": [
        {
          "episode_id": "612200501",
          "script_id": "ing3_102005_01.json__25a0be9cbf0e3e87",
          "source_sha256": "a5543c7da3a7733ecd56b634c510b1da5997a884eef8f4a70c9b43b219ba13c2",
          "decoded_sha256": "4845c9fadfa0dad5f713237e4cfd4942dfcbdbb02a1c65eb19def6dfd789e375",
          "normalized_sha256": "9e903b51aa8b582cc16225618b65c486b58b88c629f02e715794a26dbeebd8d9",
          "structured_sha256": "9e903b51aa8b582cc16225618b65c486b58b88c629f02e715794a26dbeebd8d9",
          "pages": 122,
          "text_records": 110,
          "command_only_pages": 12,
          "voice_pages": 90,
          "native_pages_verified": 122
        },
        {
          "episode_id": "612200502",
          "script_id": "ing3_102005_02.json__bb609a698248eb31",
          "source_sha256": "06049e4e919cd3f4f6904fc03090ca4ab10cf1e0f362873a84a8f8016250c29a",
          "decoded_sha256": "c03373285dd341249dbb66d11d39af719d21543af130fde7ab17bb8a04d97833",
          "normalized_sha256": "ce89fd21646a26163a586680e47eab13496b5030f6cc8068ff5060d65e477a2a",
          "structured_sha256": "ce89fd21646a26163a586680e47eab13496b5030f6cc8068ff5060d65e477a2a",
          "pages": 77,
          "text_records": 73,
          "command_only_pages": 4,
          "voice_pages": 62,
          "native_pages_verified": 77
        },
        {
          "episode_id": "612200503",
          "script_id": "ing3_102005_03.json__3569c33fe73c847e",
          "source_sha256": "8bf81c5d60b18547e98ab34c46a67bc25b5d9543ea509e09e1b7588592b92ae4",
          "decoded_sha256": "c43ab4f49341a965ccf343f8c68479550b90f2b75e5e4a40116ed264b5e3b0c5",
          "normalized_sha256": "61f49e87bf1089b488664fa9e55a3455baf7d79b7876902554e6029f82736fb9",
          "structured_sha256": "61f49e87bf1089b488664fa9e55a3455baf7d79b7876902554e6029f82736fb9",
          "pages": 140,
          "text_records": 118,
          "command_only_pages": 22,
          "voice_pages": 91,
          "native_pages_verified": 140
        }
      ],
      "totals": {
        "pages": 339,
        "text_records": 301,
        "command_only_pages": 38,
        "voice_pages": 243,
        "visual_refs": 2296
      },
      "voice_count_basis": "Distinct dialogue log-order indexes with voice resource; title-only cues additional; no performed audio reviewed.",
      "native_packet_sha256": "43da96776ba1568b7318d3fb30a88f0b05bdd73141cfc05c581b1060389beac2",
      "dialogue_packet_sha256": "6c515cdf41b2f7e81ec7a3ef25b73d2137e8b7b225e748ab89e7fe5109b0c1ce",
      "visual_assets": [
        {
          "resource": "adv_chara_007_02_01",
          "body": "adv_chara_007_02.png",
          "body_sha256": "92aaed359500dd8fd52b4cecb0a7e1f60b0e63e466320ae2036086461c29edc1",
          "face": "adv_chara_007_02_01.png",
          "face_sha256": "058fe38238d4a9536ad725405934be5e959a9398a2fe97137d92fe2699cab509",
          "native_face_offset": [
            84,
            80
          ],
          "output_sha256": "804d4fcd682cec681f71da56c4462f4bc0e861fb85ea5f4fad9e5ccc10d469c4"
        },
        {
          "resource": "adv_chara_007_01_01",
          "body": "adv_chara_007_01.png",
          "body_sha256": "1bf0de43c70899cafbf9ae8fedfba9663293ade0a774d004e620c158af87ccf0",
          "face": "adv_chara_007_01_01.png",
          "face_sha256": "cbbc596096c690e698bca606f704579f2bf8ad84a9a2ab336891c2b66c54c9f9",
          "native_face_offset": [
            84,
            80
          ],
          "output_sha256": "b221806b4688af7613b359a7957cb939c4fa6df4327677023bcb8196f7731a55"
        },
        {
          "resource": "adv_chara_004_01_06",
          "body": "adv_chara_004_01.png",
          "body_sha256": "5d8b60092117906b699d98ccabfc88344ea61f82e9b27a23bec1fa15d0cb65be",
          "face": "adv_chara_004_01_06.png",
          "face_sha256": "2ed7745b3f1906230a645b992a93e8259f8fd0466efab7fe91237c02d74440e7",
          "native_face_offset": [
            194,
            74
          ],
          "output_sha256": "768a21438bdc393bae3afad31a52cb7669988a04282251c52576a5353b7de373"
        },
        {
          "resource": "adv_chara_008_01_01",
          "body": "adv_chara_008_01.png",
          "body_sha256": "a72bd127faade4229587eff774c6b319fd99e8221290d4cfbd61769441d8afa4",
          "face": "adv_chara_008_01_01.png",
          "face_sha256": "6cde466239545bdd5ef7cf3a50542c810e853eb59f7519d9d476f4bd59f0e0a0",
          "native_face_offset": [
            166,
            84
          ],
          "output_sha256": "5da4d642d552e04c85241ddb25ebfa6707dabb3e06e17c22083e7151dfc9e16b"
        },
        {
          "resource": "adv_chara_012_01_01",
          "body": "adv_chara_012_01.png",
          "body_sha256": "d142646f64071ed43061fd75721befa778228cd90a1c9d04fd996d739fc468b9",
          "face": "adv_chara_012_01_01.png",
          "face_sha256": "48fb3d5af2ec98fe05dd274e15e82fd680c07f6723ab0a2f5dceb188b7fcffd7",
          "native_face_offset": [
            59,
            74
          ],
          "output_sha256": "1a3b01fe595284bb8b645118dd34a3df4190b302bad562466afad619b5724c2b"
        },
        {
          "resource": "adv_chara_013_01_01",
          "body": "adv_chara_013_01.png",
          "body_sha256": "2d4ca61240c61c15796eacab3c3a0ea5cf48f56c8b772d95e1b3ac1be0b7937c",
          "face": "adv_chara_013_01_01.png",
          "face_sha256": "a236fe22cae50a537cd68a6815caf0cc1accac77684eff2b648583d94cf7699d",
          "native_face_offset": [
            105,
            60
          ],
          "output_sha256": "262b62a2fe6a20eaad5f2a488b69373b9433688833bcc6a61d9efb4e5e1190d0"
        },
        {
          "resource": "adv_chara_014_01_01",
          "body": "adv_chara_014_01.png",
          "body_sha256": "b8665daef47ba3fbf338538586adc18c16ed72c65092ad9d57cf2a4f128f3677",
          "face": "adv_chara_014_01_01.png",
          "face_sha256": "4e079f9164ae0c42544a85ddb20759dec6c1b5f99809e08a5e306cec26572c9b",
          "native_face_offset": [
            128,
            78
          ],
          "output_sha256": "36c04514f1a826ffda4d191b8b88a05f8f1d280bda4532a579a4a964a69c13aa"
        },
        {
          "resource": "adv_chara_027_01",
          "body": "adv_chara_027_01.png",
          "body_sha256": "810a321a0caa3684cb49ee9d614be39546da445df27bd0896e56a6c295b90f97",
          "output_sha256": "d215fdeb03bfde804de0105b121aa682ce9f8d876f8b50948a02898afaecfcf4"
        },
        {
          "resource": "adv_obj_0027",
          "body": "adv_obj_0027.png",
          "body_sha256": "5f8f7e302456a74fb0b57ecbf770b18515cfba5aabadb7c692f2db788e7ed322",
          "output_sha256": "a2cba3e2732a36e1ef0d6f4c3eee4f4072e570784eadafca4020d1b90da2cb93"
        }
      ],
      "coverage_effective_state_sha256": "4024a252da040ec7eacbff8eabc16232c1442ce855c704cc872f5adbab055aa9",
      "execution_record": "09 Audits and Manifests/T7S_B0100_B0159_EXECUTION_RECORD.md",
      "boundary": "Complete chapter-local text/native state plus selected static review; no authored choice or inline movie; no later-source semantic evidence; performed audio unreviewed."
    },
    "b0149_close_verification": {
      "operation": "T7S_B0149_CLOSE",
      "checked_at": "2026-09-26",
      "status": "PASS_BOUNDED_TEXT_NATIVE_AND_STATIC_REVIEW",
      "episode_ids": [
        "612200601",
        "612200602",
        "612200603"
      ],
      "source_bindings": [
        {
          "episode_id": "612200601",
          "script_id": "ing3_102006_01.json__7110a79fd0286fdd",
          "source_sha256": "49119956e9264e0514a27d02c0033c3ef9c4c78089887cf8160b78c7cfe296c4",
          "decoded_sha256": "8f13347bd709f0903c2fc37f9e4e5ae64d6e6983684d6e2000bc297220c08c76",
          "normalized_sha256": "cf68874fea8d48549f5d5d6d612a971d1a80c0f8a197ccb00e81d3ded613287e",
          "structured_sha256": "cf68874fea8d48549f5d5d6d612a971d1a80c0f8a197ccb00e81d3ded613287e",
          "pages": 86,
          "text_records": 70,
          "command_only_pages": 16,
          "voice_pages": 47,
          "native_pages_verified": 86
        },
        {
          "episode_id": "612200602",
          "script_id": "ing3_102006_02.json__d391d9e765a48348",
          "source_sha256": "53847d98c95fc9f991d2b891af716ddcb7338de4f359215ae0c01568c10eac89",
          "decoded_sha256": "b6668adaa262e574c0511a2589072c7efd9d7eefbec1fb6d5f0c2225799cd61d",
          "normalized_sha256": "b4642a4995e547e7c1e5f337ab37827d321faf4b6059f2eac0d2d42090849b0d",
          "structured_sha256": "b4642a4995e547e7c1e5f337ab37827d321faf4b6059f2eac0d2d42090849b0d",
          "pages": 130,
          "text_records": 97,
          "command_only_pages": 33,
          "voice_pages": 97,
          "native_pages_verified": 130
        },
        {
          "episode_id": "612200603",
          "script_id": "ing3_102006_03.json__4876734b3f04c450",
          "source_sha256": "79fe1e7f0a98eace0d2dd2d252b23939d1d6839297ea9706e8d83e37d8029549",
          "decoded_sha256": "bc8c94b377a7320ffe2d558b16f64c98dfe405022c6cefec37c8d95299b54d48",
          "normalized_sha256": "f66e9bafceaa805586520f9314daf89e52e17aacfd1e07d4a49842ba8ecda6f4",
          "structured_sha256": "f66e9bafceaa805586520f9314daf89e52e17aacfd1e07d4a49842ba8ecda6f4",
          "pages": 204,
          "text_records": 174,
          "command_only_pages": 30,
          "voice_pages": 143,
          "native_pages_verified": 204
        }
      ],
      "totals": {
        "pages": 420,
        "text_records": 341,
        "command_only_pages": 79,
        "voice_pages": 287,
        "visual_refs": 4227
      },
      "voice_count_basis": "Distinct dialogue log-order indexes with voice resource; title-only cues additional; no performed audio reviewed.",
      "native_packet_sha256": "d6896fcd1027994177991df0e344719e9aff03c58183a5916c56700e3f78c4c5",
      "dialogue_packet_sha256": "456899e61608b1eb89db5be4d3ea5165d4745ebdba43f735004f7585a8f9490c",
      "visual_assets": [
        {
          "resource": "adv_chara_008_05_02",
          "body": "adv_chara_008_05.png",
          "body_sha256": "87ca9c245b469ea22a8c7aeb378a61a4c4539dcd955416211062a44cc4350639",
          "face": "adv_chara_008_05_02.png",
          "face_sha256": "0fc269bb7a8049f0e00b22c150bf3051d5678e70433a87857f5a6ab39cbeaa0d",
          "native_face_offset": [
            166,
            94
          ],
          "output_sha256": "738cb9a9a883f70a4d5d7b3c48612314a2538ff72d97635fe11fe7772ba121b9"
        },
        {
          "resource": "adv_chara_008_01_08",
          "body": "adv_chara_008_01.png",
          "body_sha256": "a72bd127faade4229587eff774c6b319fd99e8221290d4cfbd61769441d8afa4",
          "face": "adv_chara_008_01_08.png",
          "face_sha256": "f25f8e7458ddefe35e093699690893a1d19f5767c26bebc8f50f5e802fe9c5ef",
          "native_face_offset": [
            166,
            84
          ],
          "output_sha256": "cea0defa1de4ba0313630d1d7d52b832c1f31e9e35169dbb7427d2acc3719da3"
        },
        {
          "resource": "adv_chara_008_07_01",
          "body": "adv_chara_008_07.png",
          "body_sha256": "676312d6ae1f999450f4ed8c9f72fdb84837735797ab97bc45df8909175e9e14",
          "face": "adv_chara_008_07_01.png",
          "face_sha256": "4cf4a954f3db20e2aab35b758d766a4b5ff22768c172bbebb7a266f61bb4633b",
          "native_face_offset": [
            166,
            154
          ],
          "output_sha256": "76464f867587b954fdcf5651370fd887a8ada9f16c4c62af72d7930b9ac63152"
        },
        {
          "resource": "adv_chara_002_03_01",
          "body": "adv_chara_002_03.png",
          "body_sha256": "4bb14d813389b79055c4a24b5b3020e06bde9122d7b203b04a5489b358a7f1c7",
          "face": "adv_chara_002_03_01.png",
          "face_sha256": "44744b274cd5f728379c329e9a722c0639e1fab23ae5e846a483a3f131e80e14",
          "native_face_offset": [
            132,
            64
          ],
          "output_sha256": "59b13c2655e6f3619ff902a52aac22ff6c10c4c63f17d56ed1b58b339f46165c"
        },
        {
          "resource": "adv_chara_003_06_04",
          "body": "adv_chara_003_06.png",
          "body_sha256": "a41fb44cc61027bc6f9f0a44fe7ff477be4bd04e6e671c3d77d6efbfdf7fc55e",
          "face": "adv_chara_003_06_04.png",
          "face_sha256": "50ba658dd9bc2fe8a967a5f329a27feee656e0520dfed6c6e4d8e6a3e075d7ab",
          "native_face_offset": [
            98,
            92
          ],
          "output_sha256": "534055ec859b854627e7c380f3961e3b4a7af9391165ac56166d9f86bb0e5340"
        },
        {
          "resource": "adv_chara_006_03_01",
          "body": "adv_chara_006_03.png",
          "body_sha256": "97adf92e7dd722a0a3cf9d31e400351f042087f900cd1c83fc8bc0e2af7cbeed",
          "face": "adv_chara_006_03_01.png",
          "face_sha256": "2c87a07c735e9669eb78c6893fbcdc9c6c272aa3373d2b868d2ae7dd64f3ba13",
          "native_face_offset": [
            134,
            91
          ],
          "output_sha256": "bd7ae4da266891370350a869da8e3952490dd6e2edf7ff65c88163d14afdd287"
        },
        {
          "resource": "adv_chara_005_07_01",
          "body": "adv_chara_005_07.png",
          "body_sha256": "669800c2c0d3e46d13f8c901a6fde2ffc34297bbb5da126342875e969acaca8e",
          "face": "adv_chara_005_07_01.png",
          "face_sha256": "e99eee9a2a874aefc832a87ee2fe8575a8002b8eff49156e02587d2d3b9c0d58",
          "native_face_offset": [
            76,
            85
          ],
          "output_sha256": "27dee514244f96615b3b1467d2d3c9d91269aaff290d21f5499402cd01b7152e"
        },
        {
          "resource": "adv_chara_027_01",
          "body": "adv_chara_027_01.png",
          "body_sha256": "810a321a0caa3684cb49ee9d614be39546da445df27bd0896e56a6c295b90f97",
          "output_sha256": "d215fdeb03bfde804de0105b121aa682ce9f8d876f8b50948a02898afaecfcf4"
        }
      ],
      "coverage_effective_state_sha256": "357aa093481c8c9bb0bcc03acef6a85d008e5ad273ce953b51c8f4b0c16b2673",
      "execution_record": "09 Audits and Manifests/T7S_B0100_B0159_EXECUTION_RECORD.md",
      "boundary": "Complete chapter-local text/native state plus selected static review; no authored choice or inline movie; no later-source semantic evidence; performed audio unreviewed."
    },
    "b0150_close_verification": {
      "operation": "T7S_B0150_CLOSE",
      "checked_at": "2026-09-26",
      "status": "PASS_BOUNDED_TEXT_NATIVE_AND_STATIC_REVIEW",
      "episode_ids": [
        "612200701",
        "612200702",
        "612200703"
      ],
      "source_bindings": [
        {
          "episode_id": "612200701",
          "script_id": "ing3_102007_01.json__4c27c4ae333965da",
          "source_sha256": "614463307807bc108fedd2337ae5cb62711cf798680a8093ff2931d2b862aff1",
          "decoded_sha256": "7dc4db0cd5748f694dd307178932459e3e79232f7d248f75d39d36e0fc52dc73",
          "normalized_sha256": "f693fa063ace4efc13d94d253b95277cf68b297048e556d1a469554c9c699ba6",
          "structured_sha256": "f693fa063ace4efc13d94d253b95277cf68b297048e556d1a469554c9c699ba6",
          "pages": 205,
          "text_records": 161,
          "command_only_pages": 44,
          "voice_pages": 131,
          "native_pages_verified": 205
        },
        {
          "episode_id": "612200702",
          "script_id": "ing3_102007_02.json__4491c282f2ab5d13",
          "source_sha256": "c73815c1fcc69f61b15171130828c5b30eede5a215568ebce9665a6481bdf96e",
          "decoded_sha256": "ec95e76f1452c82fbffcbc57c7e91fbf976ec263414e45b5b04f89473e2e18c9",
          "normalized_sha256": "37fe822cf636dec7740ef21e69d20a924549875b3e04616191fe78bb44175464",
          "structured_sha256": "37fe822cf636dec7740ef21e69d20a924549875b3e04616191fe78bb44175464",
          "pages": 84,
          "text_records": 70,
          "command_only_pages": 14,
          "voice_pages": 70,
          "native_pages_verified": 84
        },
        {
          "episode_id": "612200703",
          "script_id": "ing3_102007_03.json__054d2ab6e7df46a6",
          "source_sha256": "9cd0aca43a95020bbaf13c201341d934437a47b53a0b23a35cb5770139c9e33d",
          "decoded_sha256": "146e6920e48a1adf7bad87b4c09b34227c10a6e0654a6109ab178be6b10384ad",
          "normalized_sha256": "d279017ee454b87131a497a09e773b252920f623e881ab56ae9f10947db57feb",
          "structured_sha256": "d279017ee454b87131a497a09e773b252920f623e881ab56ae9f10947db57feb",
          "pages": 150,
          "text_records": 127,
          "command_only_pages": 23,
          "voice_pages": 97,
          "native_pages_verified": 150
        }
      ],
      "totals": {
        "pages": 439,
        "text_records": 358,
        "command_only_pages": 81,
        "voice_pages": 298,
        "visual_refs": 4746
      },
      "voice_count_basis": "Distinct dialogue log-order indexes with voice resource; title-only cues additional; no performed audio reviewed.",
      "native_packet_sha256": "18c0f84a12a991ea75939491e4214c75057bb73c3177269820c4213ede47f207",
      "dialogue_packet_sha256": "c490504eebf57e07df4354e0d0e0183dadb4bb47a2039fac131704a6051a1c44",
      "visual_assets": [
        {
          "resource": "adv_chara_009_03_01",
          "body": "adv_chara_009_03.png",
          "body_sha256": "ffc2406a944338eecacf731a83cc2ecfedce4b3e932bcbf3574528e5939035c8",
          "face": "adv_chara_009_03_01.png",
          "face_sha256": "3930e1f45971c7020b6faf9806089ec8aad2c2bb2d100c0270a687c519899f6a",
          "native_face_offset": [
            109,
            85
          ],
          "output_sha256": "b68b10b4530c261991b4afa29dd60a3716090e68734c8a2b542708567dd98343"
        },
        {
          "resource": "adv_chara_009_04_01",
          "body": "adv_chara_009_04.png",
          "body_sha256": "e9227fe6f31a495a3edae3a153780043bcd944776a1736ccd4413b17caca8a7b",
          "face": "adv_chara_009_04_01.png",
          "face_sha256": "5967531d55f9d5cb2973783a45459f866ce239c388a2e1c487d408ceefc963b1",
          "native_face_offset": [
            109,
            85
          ],
          "output_sha256": "784da511313d8fbdf30ee835f83866a8f777e52335b735fa321b5686a7e0738b"
        },
        {
          "resource": "adv_chara_009_08_01",
          "body": "adv_chara_009_08.png",
          "body_sha256": "8855103200b426d0f3fe338072afa5f51f735eaed54d2936e4871e1967239274",
          "face": "adv_chara_009_08_01.png",
          "face_sha256": "77133a80f7879af6051e7630d98181f9b06d0d8a2d3fb7f509049716b9f1d84e",
          "native_face_offset": [
            105,
            91
          ],
          "output_sha256": "ffa1b70542ae12d4dbaf6c31fd51b4496553722aaf7889cfd39feecdf77f0d5f"
        },
        {
          "resource": "adv_chara_042_01",
          "body": "adv_chara_042_01.png",
          "body_sha256": "af79e9cf59d381c0d480fbedfc7f1b08430e66b4e68343f2318f39a4d274d359",
          "output_sha256": "f9b5b1adc705f71bb6fd4bde778b6805584b7b95091c814f163b0470bb1ff0cb"
        },
        {
          "resource": "adv_chara_043_01",
          "body": "adv_chara_043_01.png",
          "body_sha256": "48a817c713be5cefbdaa05841901821b98caf46d1fa870010f6ff06214ffded2",
          "output_sha256": "5f0308e6d20e673f60248fcd119a0073db8ebb1a72304204eb3a77e503e62458"
        },
        {
          "resource": "adv_chara_011_01_01",
          "body": "adv_chara_011_01.png",
          "body_sha256": "16fc2472d10c8972da16fad1f65b0bbc8c49cfb9daf7ebf2c583e54fedfb6004",
          "face": "adv_chara_011_01_01.png",
          "face_sha256": "9956f30044002e511040dad3aff1cb23bb76a02dee8f34635c555bcc49e64c00",
          "native_face_offset": [
            89,
            54
          ],
          "output_sha256": "4f610e7477a872aea3dcd8a87134f5e19d033ce60825f36fbbacd671ee554801"
        },
        {
          "resource": "adv_chara_014_01_01",
          "body": "adv_chara_014_01.png",
          "body_sha256": "b8665daef47ba3fbf338538586adc18c16ed72c65092ad9d57cf2a4f128f3677",
          "face": "adv_chara_014_01_01.png",
          "face_sha256": "4e079f9164ae0c42544a85ddb20759dec6c1b5f99809e08a5e306cec26572c9b",
          "native_face_offset": [
            128,
            78
          ],
          "output_sha256": "36c04514f1a826ffda4d191b8b88a05f8f1d280bda4532a579a4a964a69c13aa"
        },
        {
          "resource": "adv_chara_008_01_01",
          "body": "adv_chara_008_01.png",
          "body_sha256": "a72bd127faade4229587eff774c6b319fd99e8221290d4cfbd61769441d8afa4",
          "face": "adv_chara_008_01_01.png",
          "face_sha256": "6cde466239545bdd5ef7cf3a50542c810e853eb59f7519d9d476f4bd59f0e0a0",
          "native_face_offset": [
            166,
            84
          ],
          "output_sha256": "5da4d642d552e04c85241ddb25ebfa6707dabb3e06e17c22083e7151dfc9e16b"
        },
        {
          "resource": "adv_chara_010_01_01",
          "body": "adv_chara_010_01.png",
          "body_sha256": "ac05f3cd59cf77b2e8a37a23f406bd671a62496ebe681ec9bf0983fc6c843168",
          "face": "adv_chara_010_01_01.png",
          "face_sha256": "e156a889a518228a13bd2d898924eff617fd3e2203459121f168c34dfda6c1e4",
          "native_face_offset": [
            150,
            104
          ],
          "output_sha256": "55297badaa1b20a1e6c97f6786df6184e5d1df66feae66f8ed6f2f5ad45ec953"
        },
        {
          "resource": "adv_chara_007_02_01",
          "body": "adv_chara_007_02.png",
          "body_sha256": "92aaed359500dd8fd52b4cecb0a7e1f60b0e63e466320ae2036086461c29edc1",
          "face": "adv_chara_007_02_01.png",
          "face_sha256": "058fe38238d4a9536ad725405934be5e959a9398a2fe97137d92fe2699cab509",
          "native_face_offset": [
            84,
            80
          ],
          "output_sha256": "804d4fcd682cec681f71da56c4462f4bc0e861fb85ea5f4fad9e5ccc10d469c4"
        },
        {
          "resource": "adv_chara_013_01_01",
          "body": "adv_chara_013_01.png",
          "body_sha256": "2d4ca61240c61c15796eacab3c3a0ea5cf48f56c8b772d95e1b3ac1be0b7937c",
          "face": "adv_chara_013_01_01.png",
          "face_sha256": "a236fe22cae50a537cd68a6815caf0cc1accac77684eff2b648583d94cf7699d",
          "native_face_offset": [
            105,
            60
          ],
          "output_sha256": "262b62a2fe6a20eaad5f2a488b69373b9433688833bcc6a61d9efb4e5e1190d0"
        }
      ],
      "coverage_effective_state_sha256": "b31b18b60eb6d7e10f1ef7666da5932508a6b9cbe770e407ba66cddcba1cf285",
      "execution_record": "09 Audits and Manifests/T7S_B0100_B0159_EXECUTION_RECORD.md",
      "boundary": "Complete chapter-local text/native state plus selected static review; no authored choice or inline movie; no later-source semantic evidence; performed audio unreviewed."
    },
    "b0151_close_verification": {
      "operation": "T7S_B0151_CLOSE",
      "checked_at": "2026-09-26",
      "status": "PASS_BOUNDED_TEXT_NATIVE_AND_STATIC_REVIEW",
      "episode_ids": [
        "612200801",
        "612200802",
        "612200803"
      ],
      "source_bindings": [
        {
          "episode_id": "612200801",
          "script_id": "ing3_102008_01.json__bec930eefef27b24",
          "source_sha256": "fc646dabd7d6995bb08ee93ebb4233403e35b3a88fe75c5d16961602d2b237b3",
          "decoded_sha256": "2e2392490857060d55ebdab28066e3383322575cea4bfc74c97a4dd2cdd9efe7",
          "normalized_sha256": "c9fe3530e9781e5557e5c07fb80eb8d84f7668d4e56383ea0d4fd5ea22b8e313",
          "structured_sha256": "c9fe3530e9781e5557e5c07fb80eb8d84f7668d4e56383ea0d4fd5ea22b8e313",
          "pages": 70,
          "text_records": 61,
          "command_only_pages": 9,
          "voice_pages": 52,
          "native_pages_verified": 70
        },
        {
          "episode_id": "612200802",
          "script_id": "ing3_102008_02.json__451be2edcd9db955",
          "source_sha256": "ad5d7b878950a3e57f9ce9965b6234d289e93639591067e25c8905b7ec1e2b52",
          "decoded_sha256": "2ac716902b579832022a2d2ec326545e71618ab74ce7ff6516102aed074c51c2",
          "normalized_sha256": "fe39d7d971d212b5fea5d8384c8113b5454d24a5d93eb2e554f25975bd44ee53",
          "structured_sha256": "fe39d7d971d212b5fea5d8384c8113b5454d24a5d93eb2e554f25975bd44ee53",
          "pages": 125,
          "text_records": 108,
          "command_only_pages": 17,
          "voice_pages": 77,
          "native_pages_verified": 125
        },
        {
          "episode_id": "612200803",
          "script_id": "ing3_102008_03.json__6754e05fcb9352e6",
          "source_sha256": "5f25198fe1dd669e967bd95cd6a608c8052edcfcad0b1f3884b43f6f3ce18043",
          "decoded_sha256": "215470e703d83cbd0113344c4091c6ad5b82852ffdb7c38dc4b354ee70df3e47",
          "normalized_sha256": "f3c9db3c81b78ff82cde4e653a7eb783dd5d7f029595319034f3b722c2381f4a",
          "structured_sha256": "f3c9db3c81b78ff82cde4e653a7eb783dd5d7f029595319034f3b722c2381f4a",
          "pages": 179,
          "text_records": 162,
          "command_only_pages": 17,
          "voice_pages": 126,
          "native_pages_verified": 179
        }
      ],
      "totals": {
        "pages": 374,
        "text_records": 331,
        "command_only_pages": 43,
        "voice_pages": 255,
        "visual_refs": 4206
      },
      "voice_count_basis": "Distinct dialogue log-order indexes with voice resource; title-only cues additional; no performed audio reviewed.",
      "native_packet_sha256": "c5ee14ed927403332939a3d760a3655ea1b41971468514710b03d0b4494803c8",
      "dialogue_packet_sha256": "fd8ecafe52ae518bdb9b2630f211153fc2f8713bb395ce92645ba508b4694ac3",
      "visual_assets": [
        {
          "resource": "adv_chara_010_01_01",
          "body": "adv_chara_010_01.png",
          "body_sha256": "ac05f3cd59cf77b2e8a37a23f406bd671a62496ebe681ec9bf0983fc6c843168",
          "face": "adv_chara_010_01_01.png",
          "face_sha256": "e156a889a518228a13bd2d898924eff617fd3e2203459121f168c34dfda6c1e4",
          "native_face_offset": [
            150,
            104
          ],
          "output_sha256": "55297badaa1b20a1e6c97f6786df6184e5d1df66feae66f8ed6f2f5ad45ec953"
        },
        {
          "resource": "adv_chara_010_01_09",
          "body": "adv_chara_010_01.png",
          "body_sha256": "ac05f3cd59cf77b2e8a37a23f406bd671a62496ebe681ec9bf0983fc6c843168",
          "face": "adv_chara_010_01_09.png",
          "face_sha256": "59892c874433b4f16bc92afe202a72fcf403dd47e8478ed5c6605a12b6156b89",
          "native_face_offset": [
            150,
            104
          ],
          "output_sha256": "32eebfe4e0310945012fe72f1f500109db925f1541bd8b00e78351078a711dcf"
        },
        {
          "resource": "adv_chara_010_02_10",
          "body": "adv_chara_010_02.png",
          "body_sha256": "ae740226c3df25917ab2a2709ae40afb64cbcd2578c61ae1db3cc7325142583e",
          "face": "adv_chara_010_02_10.png",
          "face_sha256": "6904d137c1ada4c278a72844e8b45994c7390131cb919f39f0ea69158f1b986c",
          "native_face_offset": [
            150,
            104
          ],
          "output_sha256": "42706c124ab7c640f8fef1dc723dd467aa758940e8b7b2d2289532e88aae8a25"
        },
        {
          "resource": "adv_chara_002_03_01",
          "body": "adv_chara_002_03.png",
          "body_sha256": "4bb14d813389b79055c4a24b5b3020e06bde9122d7b203b04a5489b358a7f1c7",
          "face": "adv_chara_002_03_01.png",
          "face_sha256": "44744b274cd5f728379c329e9a722c0639e1fab23ae5e846a483a3f131e80e14",
          "native_face_offset": [
            132,
            64
          ],
          "output_sha256": "59b13c2655e6f3619ff902a52aac22ff6c10c4c63f17d56ed1b58b339f46165c"
        },
        {
          "resource": "adv_chara_002_05_03",
          "body": "adv_chara_002_05.png",
          "body_sha256": "cb016340fb0d82c4b3f5e1c47bcd449550f680719951d70b9cbb10018be79a0b",
          "face": "adv_chara_002_05_03.png",
          "face_sha256": "bd26f12ebf371ca0f0dcbd14bd681b114b478139f5ac5204be8c1e92f7359027",
          "native_face_offset": [
            132,
            64
          ],
          "output_sha256": "9dbec5359d6fd116edc4d16bf92764c4eb13f21b9c73afff2f4d3b12070f1c88"
        },
        {
          "resource": "adv_chara_003_06_10",
          "body": "adv_chara_003_06.png",
          "body_sha256": "a41fb44cc61027bc6f9f0a44fe7ff477be4bd04e6e671c3d77d6efbfdf7fc55e",
          "face": "adv_chara_003_06_10.png",
          "face_sha256": "de031005ce5c6258afc6e74a1eb4422b276c8c633af8ff52bbde15897ed6c970",
          "native_face_offset": [
            98,
            92
          ],
          "output_sha256": "407e8687b7f6fec9bfe69c4710dce7a85670c89d5463aa8528e9b7257f9854d8"
        },
        {
          "resource": "adv_chara_003_06_05",
          "body": "adv_chara_003_06.png",
          "body_sha256": "a41fb44cc61027bc6f9f0a44fe7ff477be4bd04e6e671c3d77d6efbfdf7fc55e",
          "face": "adv_chara_003_06_05.png",
          "face_sha256": "bf22ef028c42ed207e7d2d4243113aca2286050bcf6c25f3d68074505cd88ebb",
          "native_face_offset": [
            98,
            92
          ],
          "output_sha256": "dc88ab73b874767a74542663ca12abca8ca2dc398cbed1f15dff7b7a1a4eba70"
        },
        {
          "resource": "adv_chara_012_03_01",
          "body": "adv_chara_012_03.png",
          "body_sha256": "a0e26982d9e65e3c9d0892b910b529cdc340aa2b5e2e99d5da8764c3175bbc12",
          "face": "adv_chara_012_03_01.png",
          "face_sha256": "a5f428229fc32bff1e4699e2c4a3b8aa8bc1f82285dae2cf2ba22fc329484fda",
          "native_face_offset": [
            117,
            74
          ],
          "output_sha256": "76639a045daa91598492254c884bcf1444de5d161490e8eceeda954cb325a736"
        },
        {
          "resource": "adv_chara_040_01",
          "body": "adv_chara_040_01.png",
          "body_sha256": "b31a962e523ec3200fee06279c4f845898bfef5ccf12ae47eaccfad7a9b2eca0",
          "output_sha256": "6ff3db2337ca97918b503b55cdb77e44b0e0a0883a138b868dc9cd33f55c9702"
        }
      ],
      "coverage_effective_state_sha256": "d6818eb55b1f190097f37d82176cadeca93d9290a2d183173c4a9c3cd062e345",
      "execution_record": "09 Audits and Manifests/T7S_B0100_B0159_EXECUTION_RECORD.md",
      "boundary": "Complete chapter-local text/native state plus selected static review; no authored choice or inline movie; no later-source semantic evidence; performed audio unreviewed."
    },
    "b0152_close_verification": {
      "operation": "T7S_B0152_CLOSE",
      "checked_at": "2026-09-26",
      "status": "PASS_BOUNDED_TEXT_NATIVE_AND_STATIC_REVIEW",
      "episode_ids": [
        "612200901",
        "612200902",
        "612200903"
      ],
      "source_bindings": [
        {
          "episode_id": "612200901",
          "script_id": "ing3_102009_01.json__11f6ade79587ae99",
          "source_sha256": "f82a8d4ab399c844347bbef71ed8feda005871001e782ce0c382a378728d1848",
          "decoded_sha256": "4b8320b3f8109ea962244e337beee3828254d5778c7af445465878f686383cce",
          "normalized_sha256": "96138ab34a2c119a17ad6ef1b9bfe21c50fe3ebf4d1f3d54636513f580c746dd",
          "structured_sha256": "96138ab34a2c119a17ad6ef1b9bfe21c50fe3ebf4d1f3d54636513f580c746dd",
          "pages": 49,
          "text_records": 45,
          "command_only_pages": 4,
          "voice_pages": 39,
          "native_pages_verified": 49
        },
        {
          "episode_id": "612200902",
          "script_id": "ing3_102009_02.json__9cfd0bc1632b9179",
          "source_sha256": "fd0d5a7c834afcf716365d2893a810351c09cf0df2b34de0160989d8de8b673d",
          "decoded_sha256": "8c1eda316d05c056ac6ed190c9961f5c63887f626e2fa9f64908db5564160359",
          "normalized_sha256": "f100a3baa39666e4bccc114fb0f836b5688dc6617c3d6b52b5ed2388f6343735",
          "structured_sha256": "f100a3baa39666e4bccc114fb0f836b5688dc6617c3d6b52b5ed2388f6343735",
          "pages": 139,
          "text_records": 113,
          "command_only_pages": 26,
          "voice_pages": 94,
          "native_pages_verified": 139
        },
        {
          "episode_id": "612200903",
          "script_id": "ing3_102009_03.json__5b05fda7444f8663",
          "source_sha256": "dd689becca1a6d66c29ff5339214952b1ab5d8f3ee8d599a114b5baf512595ab",
          "decoded_sha256": "7704e97f01096d84146311a12e048445a1d8823729043d1be9cb29b9430fec4f",
          "normalized_sha256": "006b14c7332ba6e0606a0d372c520bc56be31bd979772b0543888ecbab25fdd4",
          "structured_sha256": "006b14c7332ba6e0606a0d372c520bc56be31bd979772b0543888ecbab25fdd4",
          "pages": 165,
          "text_records": 137,
          "command_only_pages": 28,
          "voice_pages": 98,
          "native_pages_verified": 165
        }
      ],
      "totals": {
        "pages": 353,
        "text_records": 295,
        "command_only_pages": 58,
        "voice_pages": 231,
        "visual_refs": 2951
      },
      "voice_count_basis": "Distinct dialogue log-order indexes with voice resource; title-only cues additional; no performed audio reviewed.",
      "native_packet_sha256": "09a7978ea07611d33f11da14e6c867b1413fa9b1549bec64524ee238d5628443",
      "dialogue_packet_sha256": "02c93477d23c755246917fc9df9929828bfdafeab5fe004745bbb8028fde9aec",
      "visual_assets": [
        {
          "resource": "adv_chara_011_01_06",
          "body": "adv_chara_011_01.png",
          "body_sha256": "16fc2472d10c8972da16fad1f65b0bbc8c49cfb9daf7ebf2c583e54fedfb6004",
          "face": "adv_chara_011_01_06.png",
          "face_sha256": "300b99809fe080a24c3803e10c451b06c95aacbd519cf4db7883ed5ae8aef5d6",
          "native_face_offset": [
            89,
            54
          ],
          "output_sha256": "265da1873ada23d3876ae477923a70e2d8849383bee31407f9cb9dec78179271"
        },
        {
          "resource": "adv_chara_011_05_15",
          "body": "adv_chara_011_05.png",
          "body_sha256": "52eabf25d0efedbf44676da80f8be5d81557d65bc9cf2152a341c9d504db91c0",
          "face": "adv_chara_011_05_15.png",
          "face_sha256": "3b9f97f67e2367537f5b536126d470a79882df941ae21ec7dd99bc5e46ac9d4c",
          "native_face_offset": [
            89,
            54
          ],
          "output_sha256": "5a871bb12a678d3a9c7395584866ecfae681c57651d13f85fe99269ae5adb371"
        },
        {
          "resource": "adv_chara_011_06_08",
          "body": "adv_chara_011_06.png",
          "body_sha256": "c9104d066b2ca9d34b2d9a3ff4aa7fb603e84cb2947865531aefbc3668907db2",
          "face": "adv_chara_011_06_08.png",
          "face_sha256": "2a4f6981995d96304bbd4fcfc19f3c04bbe8907fa23b5b404ce6959e494c242f",
          "native_face_offset": [
            89,
            54
          ],
          "output_sha256": "de6a63d7b31a78d6148c5df53792b53b1c2d613ed0c858063dd33ead1949893d"
        },
        {
          "resource": "adv_chara_011_07_10",
          "body": "adv_chara_011_07.png",
          "body_sha256": "0a6a8ac1c5cba2e585cfafea64037b20d16ab45449120a70a840a554f3a978d9",
          "face": "adv_chara_011_07_10.png",
          "face_sha256": "f38d26f8fcaae5ddfc77bf5d0266bb4436473f0773c902ce72505b75910bac4b",
          "native_face_offset": [
            159,
            54
          ],
          "output_sha256": "091e878ba973689193b9cd290064c2d5af1b02d662c81ba81b76a633eece8ee3"
        },
        {
          "resource": "adv_chara_011_07_06",
          "body": "adv_chara_011_07.png",
          "body_sha256": "0a6a8ac1c5cba2e585cfafea64037b20d16ab45449120a70a840a554f3a978d9",
          "face": "adv_chara_011_07_06.png",
          "face_sha256": "8597c95ff4358947407a95c5d7865f54383080c7f5f61c37adbda86a03b9a957",
          "native_face_offset": [
            159,
            54
          ],
          "output_sha256": "e9e35e790e0d377e209918d69643a4c17354ec9b30d03ddf2041e60d0dd703ea"
        },
        {
          "resource": "adv_chara_004_06_06",
          "body": "adv_chara_004_06.png",
          "body_sha256": "2fa07637cb12479aa6a36a4d33fcda9dadc4f265786390ccbfdae5beb4279b75",
          "face": "adv_chara_004_06_06.png",
          "face_sha256": "a99218634c4ced512d7d9fe7a14f1dcdd7966bb5b6b11eb6d174eca4dc9f3946",
          "native_face_offset": [
            194,
            74
          ],
          "output_sha256": "05687fb68537e8008dc12b8cde11204d6d4df52828f89512f8caf2194d718fd0"
        },
        {
          "resource": "adv_chara_003_02_10",
          "body": "adv_chara_003_02.png",
          "body_sha256": "81ca424b3db7ec06f59bdef201d73426c018b984f1b1864b82404efe3b25deb9",
          "face": "adv_chara_003_02_10.png",
          "face_sha256": "88eefc306c623c676673843040c0b9e1c152e5084624d7b9dbb91fde0666b1be",
          "native_face_offset": [
            98,
            92
          ],
          "output_sha256": "0db94fb555bcd572aa2f0384b418304dd7425c3de1112f3ff2e6f136e01df380"
        },
        {
          "resource": "adv_chara_012_01_06",
          "body": "adv_chara_012_01.png",
          "body_sha256": "d142646f64071ed43061fd75721befa778228cd90a1c9d04fd996d739fc468b9",
          "face": "adv_chara_012_01_06.png",
          "face_sha256": "281a989f5be46d7506dfe5c66907782d1d764d694ce25a12af33d425957721ab",
          "native_face_offset": [
            59,
            74
          ],
          "output_sha256": "4be277c0ccb819234949e583e9fb0f0b58cc70dfa41a0b697611dcd3135ef757"
        },
        {
          "resource": "adv_obj_0153",
          "body": "adv_obj_0153.png",
          "body_sha256": "34827f0be02544308dfef984e13322c652358b8e7f41c24d80997ec25b574aa0",
          "output_sha256": "8791fa09b37cc7d29b4234568f95b237d3ea8e6fefbb74e47b607f27dcb32fa2"
        },
        {
          "resource": "adv_obj_0027",
          "body": "adv_obj_0027.png",
          "body_sha256": "5f8f7e302456a74fb0b57ecbf770b18515cfba5aabadb7c692f2db788e7ed322",
          "output_sha256": "a2cba3e2732a36e1ef0d6f4c3eee4f4072e570784eadafca4020d1b90da2cb93"
        }
      ],
      "coverage_effective_state_sha256": "89de20f6a314c20531d89b281e969ea8bc3f791c7e69379a4bbfb82e8b5e931a",
      "execution_record": "09 Audits and Manifests/T7S_B0100_B0159_EXECUTION_RECORD.md",
      "boundary": "Complete chapter-local text/native state plus selected static review; no authored choice or inline movie; no later-source semantic evidence; performed audio unreviewed."
    },
    "b0153_close_verification": {
      "operation": "T7S_B0153_CLOSE",
      "checked_at": "2026-09-26",
      "status": "PASS_BOUNDED_TEXT_NATIVE_AND_STATIC_REVIEW",
      "episode_ids": [
        "612201001",
        "612201002",
        "612201003"
      ],
      "source_bindings": [
        {
          "episode_id": "612201001",
          "script_id": "ing3_102010_01.json__cd197c0b3549fc3c",
          "source_sha256": "b4e20cf34c1b4754544aea795e852d8e78dafdf733160d65290fa5eca3193fa8",
          "decoded_sha256": "f90d700e2791a107b72aab1e2c1bf69d9a9901a51e2154b9d6efbaf357903278",
          "normalized_sha256": "a9c5b880ea4e8c15ed03c06d921bd4ddd837b375520bc9def5ee777d7ae95c99",
          "structured_sha256": "a9c5b880ea4e8c15ed03c06d921bd4ddd837b375520bc9def5ee777d7ae95c99",
          "pages": 82,
          "text_records": 71,
          "command_only_pages": 11,
          "voice_pages": 40,
          "native_pages_verified": 82
        },
        {
          "episode_id": "612201002",
          "script_id": "ing3_102010_02.json__69f48ff501438cfc",
          "source_sha256": "b9eb4f1d8bfd61a18973d232b107d0a42255d2ecdc7aa9628787d1406b1a4b58",
          "decoded_sha256": "e7024b1afa8a0cb413e25e2a34fee3cfc61708d4042419eb0ad37ec533f35bc3",
          "normalized_sha256": "2879f2a3e3b374dc22cd33dd58b87c278197a60d5d70d5d14648d4c3646a30e6",
          "structured_sha256": "2879f2a3e3b374dc22cd33dd58b87c278197a60d5d70d5d14648d4c3646a30e6",
          "pages": 108,
          "text_records": 96,
          "command_only_pages": 12,
          "voice_pages": 50,
          "native_pages_verified": 108
        },
        {
          "episode_id": "612201003",
          "script_id": "ing3_102010_03.json__1999867c716144d5",
          "source_sha256": "e95dc5611f04da0f3044ec6b0c7a5beb091846e063d88f21a4de552a92423a3c",
          "decoded_sha256": "2af4a3d56e2c64d7939020de1f97208c0f15a4807d71b1ea85b1cb42b7753d70",
          "normalized_sha256": "bdbf09dceb0ef5c7d18ba8e36b7a3fa31e70a8700e71cd2e2759f596b048b08c",
          "structured_sha256": "bdbf09dceb0ef5c7d18ba8e36b7a3fa31e70a8700e71cd2e2759f596b048b08c",
          "pages": 93,
          "text_records": 84,
          "command_only_pages": 9,
          "voice_pages": 33,
          "native_pages_verified": 93
        }
      ],
      "totals": {
        "pages": 283,
        "text_records": 251,
        "command_only_pages": 32,
        "voice_pages": 123,
        "visual_refs": 2756
      },
      "voice_count_basis": "Distinct dialogue log-order indexes with voice resource; title-only cues additional; no performed audio reviewed.",
      "native_packet_sha256": "cb1790977f6209504b20c25a6520a0a31a6a51714a46344895420331c813eeb9",
      "dialogue_packet_sha256": "6d3a2de3df12f14f787d73d96f1c684a7215048b8611111d87267b1833d2faf5",
      "visual_assets": [
        {
          "resource": "adv_chara_012_01_01",
          "body": "adv_chara_012_01.png",
          "body_sha256": "d142646f64071ed43061fd75721befa778228cd90a1c9d04fd996d739fc468b9",
          "face": "adv_chara_012_01_01.png",
          "face_sha256": "48fb3d5af2ec98fe05dd274e15e82fd680c07f6723ab0a2f5dceb188b7fcffd7",
          "native_face_offset": [
            59,
            74
          ],
          "output_sha256": "1a3b01fe595284bb8b645118dd34a3df4190b302bad562466afad619b5724c2b"
        },
        {
          "resource": "adv_chara_012_05_01",
          "body": "adv_chara_012_05.png",
          "body_sha256": "12c92eaf4236428955e8717dbc0b532b712b8dd370772ba00fea8b81e905f641",
          "face": "adv_chara_012_05_01.png",
          "face_sha256": "48fb3d5af2ec98fe05dd274e15e82fd680c07f6723ab0a2f5dceb188b7fcffd7",
          "native_face_offset": [
            117,
            74
          ],
          "output_sha256": "fb6a34667152e4f7415ea9836173bfeca6111100e722da54c456da23baa7de7d"
        },
        {
          "resource": "adv_chara_012_05_06",
          "body": "adv_chara_012_05.png",
          "body_sha256": "12c92eaf4236428955e8717dbc0b532b712b8dd370772ba00fea8b81e905f641",
          "face": "adv_chara_012_05_06.png",
          "face_sha256": "929c15f57720030c1f693ca5afbd6abde19ae8d022b228786c63be03b296232e",
          "native_face_offset": [
            117,
            74
          ],
          "output_sha256": "724cc927d3f9acd9f9f49fc84627cce9fb4fea6e64caac49a6413a14f419e25a"
        },
        {
          "resource": "adv_chara_012_06_01",
          "body": "adv_chara_012_06.png",
          "body_sha256": "9c9a06bfe205f02419707e129aab582d1f4e409acddffad3e04de615b1a3f87c",
          "face": "adv_chara_012_06_01.png",
          "face_sha256": "48fb3d5af2ec98fe05dd274e15e82fd680c07f6723ab0a2f5dceb188b7fcffd7",
          "native_face_offset": [
            117,
            74
          ],
          "output_sha256": "380edb5309c8c4a370c6736847ce9f78d36fa1d2925e939646add3c39cf11ab4"
        },
        {
          "resource": "adv_chara_012_06_04",
          "body": "adv_chara_012_06.png",
          "body_sha256": "9c9a06bfe205f02419707e129aab582d1f4e409acddffad3e04de615b1a3f87c",
          "face": "adv_chara_012_06_04.png",
          "face_sha256": "ace3d5ce734aacee1865eac288f1dc602cafe7aa879bbf73906b6d3d47bf7619",
          "native_face_offset": [
            117,
            74
          ],
          "output_sha256": "ff783454c948e48e977eec67984f8c9005af2c38c719b3b62805d5d4f0e22684"
        },
        {
          "resource": "adv_chara_014_01_03",
          "body": "adv_chara_014_01.png",
          "body_sha256": "b8665daef47ba3fbf338538586adc18c16ed72c65092ad9d57cf2a4f128f3677",
          "face": "adv_chara_014_01_03.png",
          "face_sha256": "f57e067228e96a507dbbdc97128ed82caeb74e135b19891607478ec06797f877",
          "native_face_offset": [
            128,
            78
          ],
          "output_sha256": "730ce3c414094080338eb51ffefe4762e1062f10acebfeacdf8a601ced44da8a"
        },
        {
          "resource": "adv_chara_003_01_04",
          "body": "adv_chara_003_01.png",
          "body_sha256": "cfd3a3dd39c6fd67b6ffc63190a2da76e8d1ef5cedcb8eb895afd2a9bd870064",
          "face": "adv_chara_003_01_04.png",
          "face_sha256": "3f0e6ce20ffeb671db9eda2341367f9cdc4c2af4891bbb36235470da845a34ad",
          "native_face_offset": [
            98,
            92
          ],
          "output_sha256": "5feeba42d8ca1072dc2a8f5f8e621669756ca251bd3f647f97f5e8449697ed98"
        },
        {
          "resource": "adv_chara_002_03_11",
          "body": "adv_chara_002_03.png",
          "body_sha256": "4bb14d813389b79055c4a24b5b3020e06bde9122d7b203b04a5489b358a7f1c7",
          "face": "adv_chara_002_03_11.png",
          "face_sha256": "a4f478e7621a53a877e16735445088d7fe40afde731cec0752906efe9e3b703a",
          "native_face_offset": [
            132,
            64
          ],
          "output_sha256": "dfdd6eb62836ea33189c85517d8aa2ecccd8eb77edfbdd7755d85828e77e6dcd"
        },
        {
          "resource": "adv_obj_0027",
          "body": "adv_obj_0027.png",
          "body_sha256": "5f8f7e302456a74fb0b57ecbf770b18515cfba5aabadb7c692f2db788e7ed322",
          "output_sha256": "a2cba3e2732a36e1ef0d6f4c3eee4f4072e570784eadafca4020d1b90da2cb93"
        }
      ],
      "coverage_effective_state_sha256": "9318f21279524927afd98ee994311b691fc1e49770a517291d5063dc54ba8243",
      "execution_record": "09 Audits and Manifests/T7S_B0100_B0159_EXECUTION_RECORD.md",
      "boundary": "Complete chapter-local text/native state plus selected static review; no authored choice or inline movie; no later-source semantic evidence; performed audio unreviewed."
    },
    "b0154_close_verification": {
      "operation": "T7S_B0154_CLOSE",
      "checked_at": "2026-09-26",
      "status": "PASS_BOUNDED_TEXT_NATIVE_AND_STATIC_REVIEW",
      "episode_ids": [
        "612201101",
        "612201102",
        "612201103"
      ],
      "source_bindings": [
        {
          "episode_id": "612201101",
          "script_id": "ing3_102011_01.json__0813ab72f129aee9",
          "source_sha256": "b03b0b0cb6cfddd9a2e0a474f2140f0abc359df5d46d75f6938ac6ab54e615ea",
          "decoded_sha256": "af1d695dbd1f8484c513f2164797b7cec78196e8d20be475f49fcae7b8c41a4a",
          "normalized_sha256": "0d9769a16ac0ca67dd2c52ca2ba1f7a8ca1b59cf13a7123611116930b1278f2d",
          "structured_sha256": "0d9769a16ac0ca67dd2c52ca2ba1f7a8ca1b59cf13a7123611116930b1278f2d",
          "pages": 88,
          "text_records": 78,
          "command_only_pages": 10,
          "voice_pages": 57,
          "native_pages_verified": 88
        },
        {
          "episode_id": "612201102",
          "script_id": "ing3_102011_02.json__fb93780c159a2305",
          "source_sha256": "954692e535f05d75e24ab9adf8faef90f79a952fab1bcd84e51c3a9f324f260a",
          "decoded_sha256": "068f39ad651f04506224b9a2bfa3c1091811fe8e47f01f32cc80065f63b2438d",
          "normalized_sha256": "f746b55acd081b21ee7907722543be7310fc33a1c79da69b82cb4d3bf1ee1ca4",
          "structured_sha256": "f746b55acd081b21ee7907722543be7310fc33a1c79da69b82cb4d3bf1ee1ca4",
          "pages": 74,
          "text_records": 72,
          "command_only_pages": 2,
          "voice_pages": 72,
          "native_pages_verified": 74
        },
        {
          "episode_id": "612201103",
          "script_id": "ing3_102011_03.json__10a681adde4bc4b4",
          "source_sha256": "ebd620bffa6e670594ccdda81b9f9c7ccbdeb491fdb468b2f0179d85b18330f2",
          "decoded_sha256": "63e073890ed5b9443cbf84dacefed48885dafeefa6e0c09449eccdf7c2336285",
          "normalized_sha256": "a9919b4978e06fcd7f4f3259053834f64de7cc704719e9f2e7530d03d297d10c",
          "structured_sha256": "a9919b4978e06fcd7f4f3259053834f64de7cc704719e9f2e7530d03d297d10c",
          "pages": 77,
          "text_records": 67,
          "command_only_pages": 10,
          "voice_pages": 64,
          "native_pages_verified": 77
        }
      ],
      "totals": {
        "pages": 239,
        "text_records": 217,
        "command_only_pages": 22,
        "voice_pages": 193,
        "visual_refs": 1638
      },
      "voice_count_basis": "Distinct dialogue log-order indexes with voice resource; title-only cues additional; no performed audio reviewed.",
      "native_packet_sha256": "762493e5eec408314579413d1b11fa2eab44ec378d93fb248f22fb9ae9c730d0",
      "dialogue_packet_sha256": "9c07f3b86d059bc13313c783bfee41f64cde38c193e7cf0669f27012b2223f58",
      "visual_assets": [
        {
          "resource": "adv_chara_013_01_06",
          "body": "adv_chara_013_01.png",
          "body_sha256": "2d4ca61240c61c15796eacab3c3a0ea5cf48f56c8b772d95e1b3ac1be0b7937c",
          "face": "adv_chara_013_01_06.png",
          "face_sha256": "b0b643aa76ca4872ae5bca279ef63d17eff51a36d7a02ae1778b10a1ae15638b",
          "native_face_offset": [
            105,
            60
          ],
          "output_sha256": "ace194b5a470d1dc6761770df1a65c21e5767baa488651973a756f9e8bc206c2"
        },
        {
          "resource": "adv_chara_013_05_05",
          "body": "adv_chara_013_05.png",
          "body_sha256": "295bdefa8b6914ae56cc18a4cc8bb024300a7b6233b8366fdc34f1a18c771cef",
          "face": "adv_chara_013_05_05.png",
          "face_sha256": "5cfcb6f3271a3d0c453a21a7b7fca0482b595e0504d019f8dec6f1e1554e89f9",
          "native_face_offset": [
            105,
            60
          ],
          "output_sha256": "aa3c024efda05450bf2c7fb5bed442bee77e5e92eebeb55d717f59a62a79064a"
        },
        {
          "resource": "adv_chara_013_05_11",
          "body": "adv_chara_013_05.png",
          "body_sha256": "295bdefa8b6914ae56cc18a4cc8bb024300a7b6233b8366fdc34f1a18c771cef",
          "face": "adv_chara_013_05_11.png",
          "face_sha256": "9918870388d0f6f7b32a5d2be7ef455182adacc24e28060e5838144018b99b2f",
          "native_face_offset": [
            105,
            60
          ],
          "output_sha256": "b5bf1f3f1b1e5a776dfe814b036f2d051393743d3007c6b4600d21eefc507548"
        },
        {
          "resource": "adv_chara_012_01_01",
          "body": "adv_chara_012_01.png",
          "body_sha256": "d142646f64071ed43061fd75721befa778228cd90a1c9d04fd996d739fc468b9",
          "face": "adv_chara_012_01_01.png",
          "face_sha256": "48fb3d5af2ec98fe05dd274e15e82fd680c07f6723ab0a2f5dceb188b7fcffd7",
          "native_face_offset": [
            59,
            74
          ],
          "output_sha256": "1a3b01fe595284bb8b645118dd34a3df4190b302bad562466afad619b5724c2b"
        },
        {
          "resource": "adv_chara_003_01_05",
          "body": "adv_chara_003_01.png",
          "body_sha256": "cfd3a3dd39c6fd67b6ffc63190a2da76e8d1ef5cedcb8eb895afd2a9bd870064",
          "face": "adv_chara_003_01_05.png",
          "face_sha256": "8b9e8ec1f153625b408821c2aadc4dba45baa771fa51a5e4cb8d1c36948b421b",
          "native_face_offset": [
            98,
            92
          ],
          "output_sha256": "9c56d9bce61665bc22ec08136ec269517b842ff857f0bb85f34616eea4cf157e"
        },
        {
          "resource": "adv_chara_014_01_03",
          "body": "adv_chara_014_01.png",
          "body_sha256": "b8665daef47ba3fbf338538586adc18c16ed72c65092ad9d57cf2a4f128f3677",
          "face": "adv_chara_014_01_03.png",
          "face_sha256": "f57e067228e96a507dbbdc97128ed82caeb74e135b19891607478ec06797f877",
          "native_face_offset": [
            128,
            78
          ],
          "output_sha256": "730ce3c414094080338eb51ffefe4762e1062f10acebfeacdf8a601ced44da8a"
        },
        {
          "resource": "adv_chara_004_01_01",
          "body": "adv_chara_004_01.png",
          "body_sha256": "5d8b60092117906b699d98ccabfc88344ea61f82e9b27a23bec1fa15d0cb65be",
          "face": "adv_chara_004_01_01.png",
          "face_sha256": "95e34c62c3396b29b6716cf56c2dabd1af0752f0bb56e1f1a9735860ca0dac2c",
          "native_face_offset": [
            194,
            74
          ],
          "output_sha256": "d21f450fd21f3b0278a6a4d2d0bc099bb9cc7877d04a0c56bae2a56868935f88"
        },
        {
          "resource": "adv_chara_007_02_01",
          "body": "adv_chara_007_02.png",
          "body_sha256": "92aaed359500dd8fd52b4cecb0a7e1f60b0e63e466320ae2036086461c29edc1",
          "face": "adv_chara_007_02_01.png",
          "face_sha256": "058fe38238d4a9536ad725405934be5e959a9398a2fe97137d92fe2699cab509",
          "native_face_offset": [
            84,
            80
          ],
          "output_sha256": "804d4fcd682cec681f71da56c4462f4bc0e861fb85ea5f4fad9e5ccc10d469c4"
        },
        {
          "resource": "adv_chara_002_03_01",
          "body": "adv_chara_002_03.png",
          "body_sha256": "4bb14d813389b79055c4a24b5b3020e06bde9122d7b203b04a5489b358a7f1c7",
          "face": "adv_chara_002_03_01.png",
          "face_sha256": "44744b274cd5f728379c329e9a722c0639e1fab23ae5e846a483a3f131e80e14",
          "native_face_offset": [
            132,
            64
          ],
          "output_sha256": "59b13c2655e6f3619ff902a52aac22ff6c10c4c63f17d56ed1b58b339f46165c"
        }
      ],
      "coverage_effective_state_sha256": "3833e81df68776ecb5eeccd65a94b58bb72ccc23a259e3f3330cae1fb7f82cc2",
      "execution_record": "09 Audits and Manifests/T7S_B0100_B0159_EXECUTION_RECORD.md",
      "boundary": "Complete chapter-local text/native state plus selected static review; no authored choice or inline movie; no later-source semantic evidence; performed audio unreviewed."
    },
    "b0155_close_verification": {
      "operation": "T7S_B0155_CLOSE",
      "checked_at": "2026-09-26",
      "status": "PASS_BOUNDED_TEXT_NATIVE_AND_STATIC_REVIEW",
      "episode_ids": [
        "612201201",
        "612201202",
        "612201203"
      ],
      "source_bindings": [
        {
          "episode_id": "612201201",
          "script_id": "ing3_102012_01.json__0d2e329a170b80bb",
          "source_sha256": "a360a10c66a9536de34d27bc7c00b17d962d17596f17ff4844b5f7fe814e7a98",
          "decoded_sha256": "71e872351a4950830a5208b4ae64e1153b4990be39799982b1ead5c8a50c5102",
          "normalized_sha256": "27f52b998222b2b6037c97d7db0dfcb181c717dcc645b12ffae19b2287b2231a",
          "structured_sha256": "27f52b998222b2b6037c97d7db0dfcb181c717dcc645b12ffae19b2287b2231a",
          "pages": 66,
          "text_records": 53,
          "command_only_pages": 13,
          "voice_pages": 50,
          "native_pages_verified": 66
        },
        {
          "episode_id": "612201202",
          "script_id": "ing3_102012_02.json__33a3b7a370586b3d",
          "source_sha256": "ee9dda587389b0e3d367eaeabfc06c5225c8a0447409d01e6b1f7642347f1fbf",
          "decoded_sha256": "62d049bc7376f1bd1c521f91d3fb9a525fc86ef3ae5de03b36974e2dc10c7542",
          "normalized_sha256": "56dbe2266d59abb2e699eca7210d86dadc937bfefdf477f17f29fae22b673119",
          "structured_sha256": "56dbe2266d59abb2e699eca7210d86dadc937bfefdf477f17f29fae22b673119",
          "pages": 76,
          "text_records": 70,
          "command_only_pages": 6,
          "voice_pages": 70,
          "native_pages_verified": 76
        },
        {
          "episode_id": "612201203",
          "script_id": "ing3_102012_03.json__2693d9fb12e39a4c",
          "source_sha256": "5ec157b0ef8798b6d343dbded72052fbe2b266791c9680d66d777d7b131ebeaf",
          "decoded_sha256": "673b7cfedb17a59a9e93cea652281f39d2e7b3416c3d564f44ca3a9dd3b95dab",
          "normalized_sha256": "c0171124ce6ad81409ff46902d79395fa7efc7a3a393d98e7790749c02da3cb6",
          "structured_sha256": "c0171124ce6ad81409ff46902d79395fa7efc7a3a393d98e7790749c02da3cb6",
          "pages": 169,
          "text_records": 134,
          "command_only_pages": 35,
          "voice_pages": 129,
          "native_pages_verified": 169
        }
      ],
      "totals": {
        "pages": 311,
        "text_records": 257,
        "command_only_pages": 54,
        "voice_pages": 249,
        "visual_refs": 3359
      },
      "voice_count_basis": "Distinct dialogue log-order indexes with voice resource; title-only cues additional; no performed audio reviewed.",
      "native_packet_sha256": "08975857439639103a9fdaa213559724e948a8db90ac9f724a121a25e4ed9c41",
      "dialogue_packet_sha256": "1db1b0df05782502a795cc929d9737f9f240fc63fa3713464513c1acf3b99f62",
      "visual_assets": [
        {
          "resource": "adv_chara_152_02_01",
          "body": "adv_chara_152_02.png",
          "body_sha256": "968a2df74abf0261fe9005071ad05b5476693e2b077c7506b525ef52f0a8e7b5",
          "face": "adv_chara_152_02_01.png",
          "face_sha256": "209ed05cd33fbf5e9ca853f7832b1bb5f34fd6171036444a7d7ce4af74ed7636",
          "native_face_offset": [
            0,
            0
          ],
          "output_sha256": "86867604a5f2e147ae4fadb898868221dd95f2b699147676f3f8852798a69d13"
        },
        {
          "resource": "adv_chara_152_04_01",
          "body": "adv_chara_152_04.png",
          "body_sha256": "19577ba9d94a554f9f0393730a835af398c3293b0a4d2cd3be960b592330a5b2",
          "face": "adv_chara_152_04_01.png",
          "face_sha256": "209ed05cd33fbf5e9ca853f7832b1bb5f34fd6171036444a7d7ce4af74ed7636",
          "native_face_offset": [
            0,
            0
          ],
          "output_sha256": "f06121d3b9a6d6c5c2ee664a83b1e9ba76dd00786e32ae6f16c8ba0731fa847f"
        },
        {
          "resource": "adv_chara_152_06_01",
          "body": "adv_chara_152_06.png",
          "body_sha256": "e28ca47be7cffba778469edec6aa0197b091fc57b1921fde942920043205f47d",
          "face": "adv_chara_152_06_01.png",
          "face_sha256": "209ed05cd33fbf5e9ca853f7832b1bb5f34fd6171036444a7d7ce4af74ed7636",
          "native_face_offset": [
            0,
            0
          ],
          "output_sha256": "1f6b1d7959852e7dbdeb4d8640ca929b3e299edbcb081d52d7c98b262feef124"
        },
        {
          "resource": "adv_chara_014_01_01",
          "body": "adv_chara_014_01.png",
          "body_sha256": "b8665daef47ba3fbf338538586adc18c16ed72c65092ad9d57cf2a4f128f3677",
          "face": "adv_chara_014_01_01.png",
          "face_sha256": "4e079f9164ae0c42544a85ddb20759dec6c1b5f99809e08a5e306cec26572c9b",
          "native_face_offset": [
            128,
            78
          ],
          "output_sha256": "36c04514f1a826ffda4d191b8b88a05f8f1d280bda4532a579a4a964a69c13aa"
        },
        {
          "resource": "adv_chara_014_01_06",
          "body": "adv_chara_014_01.png",
          "body_sha256": "b8665daef47ba3fbf338538586adc18c16ed72c65092ad9d57cf2a4f128f3677",
          "face": "adv_chara_014_01_06.png",
          "face_sha256": "5d33ee9fd5886e7ceb6c858a98c5457c079a5032f6b823b4b2a49a95e96cc85f",
          "native_face_offset": [
            128,
            78
          ],
          "output_sha256": "07fdf3d9b19e57fce471ebd1f9dd1e74549cb46212b63d111b155edebb84cb02"
        },
        {
          "resource": "adv_chara_009_03_01",
          "body": "adv_chara_009_03.png",
          "body_sha256": "ffc2406a944338eecacf731a83cc2ecfedce4b3e932bcbf3574528e5939035c8",
          "face": "adv_chara_009_03_01.png",
          "face_sha256": "3930e1f45971c7020b6faf9806089ec8aad2c2bb2d100c0270a687c519899f6a",
          "native_face_offset": [
            109,
            85
<!-- T7S SOURCE LOCK PAYLOAD END -->
