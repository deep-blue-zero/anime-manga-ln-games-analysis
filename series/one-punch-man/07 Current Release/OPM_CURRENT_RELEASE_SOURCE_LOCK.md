---
series: OPM
artifact_type: source_lock
scope: Official Tonari no Young Jump web serialization, provider labels 232-284
generation: V2
status: active_provisional
source_boundary: Public official state retrieved 2026-09-16; collected anchor web 232-234 and uncollected web 235-284
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
created: 2026-09-16
retrieval_date: 2026-09-16
evidence_code: PR
---

# One Punch Man — Current-Release Source Lock

## Lock result

**PASS.** The official Tonari no Young Jump series feed and all 53 public episode objects labeled web 232-284 were captured on 2026-09-16. The snapshot contains 1,075 main pages. Every image decoded, every provider restoration round-trip reproduced the original displayed image, and each episode retains its HTML, reader metadata, unmodified response bytes, restored PNGs and per-object manifests under the excluded local staging root.

This document locks the *public state observed on the retrieval date*. It does not assert that an object was never redrawn before that date. No archived prior state was available for web 232-281, so those objects are classified as public-current rather than historically unchanged.

## Provider and snapshot identity

- Official series feed: https://tonarinoyj.jp/rss/series/13932016480028984490
- Official episode form: `https://tonarinoyj.jp/episode/<provider-episode-id>`
- Retrieval: 2026-09-16; snapshot generated `2026-09-16T01:28:34.609318-04:00`
- Feed SHA-256: `3ec749ca931072cf5dce7aeecdc60cf1604423c79d16ea8054d5f468d6453a48`
- Snapshot manifest: `_staging/current-web/tonari_2026-09-16/snapshot_manifest.json`
- Snapshot result: `53 episodes / 1,075 main images / capture PASS / restoration PASS`
- Local staging is provenance only and remains outside Git. Canonical analytical locators use `web<label>/page <n>`.

## Episode object register

The SHA-256 column is the per-episode ordered-content digest over the captured main image sequence. Full HTML hashes, individual response hashes, dimensions, response metadata and restoration receipts remain in the episode manifests.

| Web label | Provider episode ID | Published UTC | Main pages | Ordered-content SHA-256 | Classification | Analytical relation |
|---:|---|---|---:|---|---|---|
| 232 | 4856001361388410249 | 2023-06-28T15:00:00Z | 41 | 7ddc6a34d025c0f6edcd36b2c96e0961c1a1807973a255d18600f015cb3f9fc7 | main narrative; collected anchor | V37 192撃目 |
| 233 | 4856001361511369675 | 2023-07-12T15:00:00Z | 29 | 5f4d4eda0534eda3198fac2a305b57dcf734faa4adc9ffc31f97caca7bc88cb9 | main narrative; collected anchor | V37 193撃目 |
| 234 | 4856001361558227256 | 2023-07-26T15:00:00Z | 31 | fe7cc1b9275957d19b4a53d849324f37100154a388c791616af3ed5cd9729b91 | main narrative; collected anchor | V37 194撃目 |
| 235 | 14079602755080540915 | 2023-08-09T15:00:00Z | 35 | c1744ffb59757e883af758f83d94432a780bae0370860f7b382319fb7fcdb5c8 | main narrative | uncollected continuation |
| 236 | 14079602755178180638 | 2023-09-06T15:00:00Z | 32 | 3cf8086ce25359f871fa996a7212aaea645808515c96beb1073ab60ccce33342 | main narrative | uncollected continuation |
| 237 | 14079602755225457808 | 2023-09-20T15:00:00Z | 35 | 6bb8f264d7c4b768e7ff701e1734c39c9bbb9407b45cbc40491544ee2f0f1100 | main narrative | uncollected continuation |
| 238 | 14079602755278351476 | 2023-10-04T15:00:00Z | 32 | f09ddfcb7a3e715d30e7c7f765390c037dec2bf6caaf97f712c824cfcc153759 | main narrative | uncollected continuation |
| 239 | 14079602755331321453 | 2023-10-18T15:00:00Z | 37 | dd2e4d8b9ae30a5645ab540408884cca7916acc37bc309b65220fc97a4a9086c | main narrative | uncollected continuation |
| 240 | 2550912965179935335 | 2025-01-22T15:00:00Z | 27 | 80f7b1b782e267a422f68776b8999152e93ce60b12836114d108547ec91dcc63 | main narrative | uncollected continuation |
| 241 | 2550912965215227081 | 2025-01-29T15:00:00Z | 23 | 295b10049dfffa08694226993847d8b9279db6e335f7f6965c7bb74562c85578 | main narrative | uncollected continuation |
| 242 | 2550912965279722993 | 2025-02-12T15:00:00Z | 16 | d553bc53209291557a5a27504b9ab2174e7f7c3d12d169c1f8afb17107b7f1ef | main narrative | uncollected continuation |
| 243 | 2550912965345820769 | 2025-02-26T15:00:00Z | 23 | beeb90a4d9f75779d4f5c3f182f2a42000a09748e80423b310176b6a86848558 | main narrative | uncollected continuation |
| 244 | 2550912965411353304 | 2025-03-12T15:00:00Z | 16 | 17aeac78379cfdaaf180800d4029cc2b618298c917c185911a8eef42961e1fe7 | main narrative | uncollected continuation |
| 245 | 2550912965476562726 | 2025-03-26T15:00:00Z | 20 | c432ada098454be3bc3ad85886b0805da90a50d07534ec2b833517f55c824474 | main narrative | uncollected continuation |
| 246 | 2550912965538709779 | 2025-04-09T15:00:00Z | 15 | 4d690d9598ac94b505b795ad5833e2398858ff28960b50ea0c9e32f02b507a7b | main narrative | uncollected continuation |
| 247 | 2550912965598112646 | 2025-04-23T15:00:00Z | 15 | 3d33b8e5a37dd8bcbf2dacd355a3e65d5765a144b00309d206f781b810942380 | main narrative | uncollected continuation |
| 248 | 2550912965667071899 | 2025-05-07T15:00:00Z | 22 | 5619071aa148acaadfcaf804827e27b5a80791e54e0d3ead92bc36257796f882 | main narrative | uncollected continuation |
| 249 | 2550912965853717872 | 2025-06-18T15:00:00Z | 15 | 7ac4969d5223cb4aae757c279f54ca5aa75012f2d70e0cd0439fe3c83b3e3bde | main narrative with shared recap lead-in | uncollected continuation |
| 250 | 2550912965853717876 | 2025-06-18T15:00:00Z | 17 | 21fe317cf0e4b8b3d477c1a3db392bd3d2d04f5c2b199e708d8de1fea081cb30 | main narrative with shared recap lead-in | uncollected continuation |
| 251 | 2550912965853717882 | 2025-06-18T15:00:00Z | 16 | 35347773b4d74cca6b66ea31f749c93283e9f5e6a0735ceadd2bbaf8f9d0b337 | main narrative with shared recap lead-in | uncollected continuation |
| 252 | 2550912965853717886 | 2025-06-18T15:00:00Z | 16 | 2a28d9e96016a9ab76c56be4fd6cc28c9be1299d61e8efe02d0f85a73c59ec7e | main narrative with shared recap lead-in | uncollected continuation |
| 253 | 2550912965853717895 | 2025-06-18T15:00:00Z | 17 | e6c014d20443d06212152c9f9c2f92a5a53d7ea954d990613db86c1ff1e7f2fe | main narrative with shared recap lead-in | uncollected continuation |
| 254 | 2550912965853717899 | 2025-06-18T15:00:00Z | 7 | 4fbe0a169308953e58d0545200dd5094b0411d0651d07b1f9301f5850e18fbf4 | main narrative with shared recap lead-in | uncollected continuation |
| 255 | 2550912965980708742 | 2025-07-16T15:00:00Z | 17 | a63ac69d656b0f905a693dce0aa9fb2a008b2a7f2c413309e65b72b60e8e9608 | main narrative | uncollected continuation |
| 256 | 2550912966040594627 | 2025-07-30T15:00:00Z | 17 | 43005ab424f29d42734b50f392ff9e89cd71e2de149020c19d7a064be6fedb1a | main narrative | uncollected continuation |
| 257 | 2550912966094393927 | 2025-08-13T15:00:00Z | 17 | 46ebf5d8c8f39b70263636cfd6c9937799e3ee7ab65ce70fe26d1a0563be3bd2 | main narrative | uncollected continuation |
| 258 | 2551460909509845437 | 2025-08-27T15:00:00Z | 15 | 849ee304f730099be599296c6b301bda5e640cee8a18b01cec53aa007e17a9a7 | main narrative | uncollected continuation |
| 259 | 2551460909568310718 | 2025-09-10T15:00:00Z | 17 | e1ded2767c9573c09e4a63e18ff58c84ff4efaaf0762444283089956415d1b57 | main narrative | uncollected continuation |
| 260 | 2551460909626059092 | 2025-09-24T15:00:00Z | 21 | c5f0d9b51a928321f854cf50c58e95f525829bdeae988e8378c8deae0a260f3e | main narrative | uncollected continuation |
| 261 | 2551460909680169234 | 2025-10-08T15:00:00Z | 18 | 51d5a01d8e2ca9514634fe8042f197e70ca4bb4b4280e4ebd9cca9a334c56921 | main narrative | uncollected continuation |
| 262 | 2551460909729791906 | 2025-10-22T15:00:00Z | 21 | 9a801ee586e56ccf569046f0d3c90b8929b745b9720a3cf5e587080a64052010 | main narrative | uncollected continuation |
| 263 | 2551460909784610390 | 2025-11-05T15:00:00Z | 21 | 96b9a3a892a70081f0b751ce609fc44269cb6549d96a591b3738c536558e6070 | main narrative | uncollected continuation |
| 264 | 2551460909833781502 | 2025-11-19T15:00:00Z | 14 | 999da41613efb1bad6ed07483378f7661cbb2ffa92ca69b5174a1f507e8a0e25 | main narrative | uncollected continuation |
| 265 | 2551460909889117066 | 2025-12-03T15:00:00Z | 20 | 6ef8c59b996117dd6b154ebe7dc954a7f94cf63da73224c9b69ef89d1a97432f | main narrative | uncollected continuation |
| 266 | 2551460909940033541 | 2025-12-17T15:00:00Z | 17 | b09b186252d879c118fa02fddc4d1b580e9af1d745eb3c7d02a6434fef72adf5 | main narrative | uncollected continuation |
| 267 | 2551460910038164617 | 2026-01-14T15:00:00Z | 16 | 8446a601c206978247953ebb989a2c7d7f2f82bd91a180a98e2f9fd3f08afa7f | main narrative | uncollected continuation |
| 268 | 12207421983319377393 | 2026-01-28T15:00:00Z | 19 | 92e1a80715369e7219562c8a83e00101b1446eff806ac08c5308efc6b1846eee | main narrative | uncollected continuation |
| 269 | 12207421983430409833 | 2026-02-25T15:00:00Z | 30 | 9b566a44fae60baa939b2edd09760b5cff3dc8ddd22a929b8ffb90b7bcc5b5e7 | main narrative | uncollected continuation |
| 270 | 12207421983430409842 | 2026-02-25T15:00:00Z | 16 | 76ee4559ef4fed6f62ed6b5a795deb2f32a8c2b0b14f5d919b6ca4b29df5631b | main narrative | uncollected continuation |
| 271 | 12207421983477981001 | 2026-03-11T15:00:00Z | 20 | 3228a36bbe40e536a41e3219a1fda4ef1970e4948eadbd21d06b8a6c2b76cd10 | main narrative | uncollected continuation |
| 272 | 12207421983530467658 | 2026-03-25T15:00:00Z | 17 | ecb1fd935db0623362ee0080777d854bf995fc50da63260e926a161d1212b5c1 | main narrative | uncollected continuation |
| 273 | 12207421983582011020 | 2026-04-08T15:00:00Z | 15 | 4422b5e0d522d61058271a7f44629b83374a6d211f3cd0aad403afb423af56f4 | main narrative | uncollected continuation |
| 274 | 12207421983638405950 | 2026-04-22T15:00:00Z | 16 | 95913213e223187798bd1f440c21e33947946887bce3145d529bac5127823df7 | main narrative | uncollected continuation |
| 275 | 12207421983661137049 | 2026-05-06T15:00:00Z | 17 | f6a322a3ad1bc17badc859b43c8698d4cb949d62fa6ee9a761d08829e4548cdd | main narrative | uncollected continuation |
| 276 | 12207421983746616006 | 2026-05-20T15:00:00Z | 18 | 000a124b624b252cb8d7713654ee8f3921776ee6848dfd33ab5a6b33d7ec6963 | main narrative | uncollected continuation |
| 277 | 12207421983782428034 | 2026-06-03T15:00:00Z | 17 | 7ece9f1d2de3843a391aa224f9d1c12b5aec1cc75629057626bc65838f1fb844 | main narrative | uncollected continuation |
| 278 | 12207421983858673174 | 2026-06-17T15:00:00Z | 15 | eadbe9365fac072c63f5c56e26007ccf840ba9b9d62c184f65cd41a3d5c0f63b | main narrative | uncollected continuation |
| 279 | 12207421983914398381 | 2026-07-01T15:00:00Z | 15 | 007a1dce43b6a9cec13b8d5802b41f08005f7da4c593fdd6bcd5e9de2bbb45d3 | main narrative | uncollected continuation |
| 280 | 12207421983970095493 | 2026-07-15T15:00:00Z | 17 | 4da2e59660fe93f43c437c34b034894e9a19bc0e1fdb6f8c21025d900508635c | main narrative | uncollected continuation |
| 281 | 12207421984027809074 | 2026-07-29T15:00:00Z | 17 | 65c942f85d9b282af63ebaaf3e24724150a7791645502c45ae9ece1eb65eb0f7 | main narrative | uncollected continuation |
| 282 | 12207421984090138482 | 2026-08-12T15:00:00Z | 24 | dd545a8c328e51a3b39b4f157749cd169038ed79c011c5b2fcb80bf35aad40ff | main narrative | uncollected continuation |
| 283 | 12207421984148777688 | 2026-08-26T15:00:00Z | 17 | 3a2b69d5c76254c56e77d326cd5e93193d45cb52539afdd4092aa6e0656f7d39 | main narrative | uncollected continuation |
| 284 | 12207421984214112687 | 2026-09-09T15:00:00Z | 17 | 51fb45da2e979840484ebfbb345fcc1a0dcd05ef504e4829e83204105fafbd1c | main narrative | uncollected continuation |

## Direct collected-boundary proof

Web 232-234 were not mapped by numeric offset. Their page sequences were compared directly against V37:

| Official web object | Printed web heading | Direct V37 destination | Page correspondence | Result |
|---|---|---|---|---|
| web 232 | 185撃目 | V37 192撃目, images 0099-0139 | web pages 1-41 → V37 0099-0139 | 41/41 strict pHash best matches |
| web 233 | 186撃目 | V37 193撃目, images 0141-0169 | web pages 1-29 → V37 0141-0169 | 29/29 strict pHash best matches |
| web 234 | 187撃目「試し斬り」 | V37 194撃目「試し斬り」, images 0171-0201 | web pages 1-31 → V37 0171-0201 | 30/30 strict page matches plus direct visual confirmation of revised title art |

V37 image 0140 is a collected-only coda after the web-232 sequence; image 0170 is a collected-only coda after web 233. Web 234 page 1 and V37 image 0171 share the central title illustration, while crop and typography changed; the remaining 30 pages form the strict monotonic match. Receipt: `_staging/verification/WEB_V37_overlap_verification.json`.

Therefore:

- web 232-234 are preserved as revision/crosswalk evidence but are analytically superseded by the V37 tankobon;
- web 235 is the first uncollected official installment;
- no arithmetic numbering rule is promoted from this observed overlap.

## Independent stability check

The separate technical pilot captured web 282-284 on 2026-09-12. Comparison against the 2026-09-16 snapshot finds identical ordered-content digests and identical page hashes for all 58 pages:

- web 282: `dd545a8c328e51a3b39b4f157749cd169038ed79c011c5b2fcb80bf35aad40ff`
- web 283: `3a2b69d5c76254c56e77d326cd5e93193d45cb52539afdd4092aa6e0656f7d39`
- web 284: `51fb45da2e979840484ebfbb345fcc1a0dcd05ef504e4829e83204105fafbd1c`

This proves stability only across those two retrievals. It does not convert the uncollected layer to canonical collected authority.

## Revision and authority rules

1. Web 235-284 remain `active_provisional`, evidence code `PR`.
2. The snapshot is the current public state, not a complete revision history.
3. A later provider replacement requires a fresh snapshot and explicit diff; the prior object remains historical revision evidence.
4. A future tankobon replaces the corresponding web material as stable analytical authority only after direct reconciliation.
5. No raw page image, capture payload, restoration output or receipt is committed to Git.
