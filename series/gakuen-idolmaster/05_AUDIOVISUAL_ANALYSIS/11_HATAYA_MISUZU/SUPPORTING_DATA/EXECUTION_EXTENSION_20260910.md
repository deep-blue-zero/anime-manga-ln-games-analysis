---
series: GKM
generation: V2
artifact_type: historical_supporting_record
status: historical_legacy
supersedes: []
superseded_by: []
do_not_use_as_current_authority: true
source_boundary: "Preserved earlier-generation supporting record; not fresh AVE-FULL evidence."
last_updated: '2026-09-10'
---
> Historical record retained from the previous packet. “New/current” in this document refers to that earlier execution, not AVE-FULL-20260910. Fresh results are in [the current measurements](FULL_REBUILD_MEASUREMENTS.md) and [current claim review](FULL_REBUILD_CLAIM_REVIEW.md).

# Misuzu execution extension — source alignment and direct visual review

This document records work newly performed after the user authorized execution of the attached prompt. The supplied rebuild ZIP, SHA-256 `bd11dcc056314fc3d1816a58499d91ba24f2eeac9fe5496c62cc8fae9fc775d8`, remains a separate input artifact. Its source metrics and `VIS-` entries are inherited records. `EXEC-MZ-` entries below identify fresh work; a shared calendar date does not merge the runs.

## Evidence modes and runtime

The current reviewer can inspect extracted images and read exact A1 source text. The runtime's native audio-content test did not provide audible content to the model, so no direct listening is claimed. Machine transcription or acoustic calculations, where separately supplied, are machine-assisted evidence and do not certify heard timbre, emotion, singing softness, or voice identity.

Fresh frame work uses Python 3.12.4, OpenCV 4.13.0 and Pillow 12.2.0 on Windows. FFmpeg/ffprobe 8.1.1 is available for decoding/probing. These are distinct from the input ZIP's recorded Linux measurement environment. Each frame log records requested source-relative seconds and decoder-reported seconds. Cropping removes uploader side artwork only for visual reading; it does not alter or replace the inherited whole-frame numerical dataset.

## Exact locked A1 acquisition

All 37 Misuzu Dear scripts were retrieved from `DreamGallery/Campus-adv-txts` at Source Lock 1.0 commit `00d150a069a3ffa723a1ff264752ba242024caad`. Each downloaded byte sequence was verified against the corresponding Git blob SHA-1 from that commit's recursive tree and independently SHA-256 hashed. This is a new retrieval of locked text, not incorporation of post-lock revisions. Script-relative `_startTime` values guide passage discovery only; they are not substituted for observed compilation timestamps because choices, edited inserts, and playback can change alignment. The acquisition inventory below contains no transcript reproduction.

| Locked source | Bytes | Git blob SHA-1 | SHA-256 |
| --- | ---: | --- | --- |
| [adv_dear_hmsz_001.txt](https://raw.githubusercontent.com/DreamGallery/Campus-adv-txts/00d150a069a3ffa723a1ff264752ba242024caad/Resource/adv_dear_hmsz_001.txt) | 165991 | 796ea948f4e020311c4daa943d182960c7376cca | 2c459e83e293f5bcfcf7c759d608dd1d8fcd06a684e12ef45bfbbb9539a1526c |
| [adv_dear_hmsz_002.txt](https://raw.githubusercontent.com/DreamGallery/Campus-adv-txts/00d150a069a3ffa723a1ff264752ba242024caad/Resource/adv_dear_hmsz_002.txt) | 158521 | 06dbf672a1d216d542b6c8877765b4643ae90401 | db81077e5520b21e6aa2e2e74b85eb929faeb46f57d2e929beb3bf280dfe9264 |
| [adv_dear_hmsz_003.txt](https://raw.githubusercontent.com/DreamGallery/Campus-adv-txts/00d150a069a3ffa723a1ff264752ba242024caad/Resource/adv_dear_hmsz_003.txt) | 128880 | a6af33e134649d328c4b9c8c86625307bf32f48e | d6851c92aa5d57132cf52ad98af3b8c2688c9e2edc3c66ba28278fe887edfef1 |
| [adv_dear_hmsz_004.txt](https://raw.githubusercontent.com/DreamGallery/Campus-adv-txts/00d150a069a3ffa723a1ff264752ba242024caad/Resource/adv_dear_hmsz_004.txt) | 148208 | 3a6110454456ddc3828f29ccf9e2e81aed35be77 | 49729b61549ad78cb67f495e594f83b7a1ef9ba713183d6a971746bffa7d6464 |
| [adv_dear_hmsz_005.txt](https://raw.githubusercontent.com/DreamGallery/Campus-adv-txts/00d150a069a3ffa723a1ff264752ba242024caad/Resource/adv_dear_hmsz_005.txt) | 134062 | c42aa4853816c9aed4553ca8e3e45be1e10d4c81 | d2b11095431b72d4e293d013449228c7d476e0cc4872771e56b20a3cba3ad407 |
| [adv_dear_hmsz_006.txt](https://raw.githubusercontent.com/DreamGallery/Campus-adv-txts/00d150a069a3ffa723a1ff264752ba242024caad/Resource/adv_dear_hmsz_006.txt) | 152407 | f2508ef1674bbf5df25e5616ff7ca7745fe1984a | 6ebd0dfd67dd8e52eb2544d4d977e20b8898d3671b38265aa02724d86ad41f90 |
| [adv_dear_hmsz_007.txt](https://raw.githubusercontent.com/DreamGallery/Campus-adv-txts/00d150a069a3ffa723a1ff264752ba242024caad/Resource/adv_dear_hmsz_007.txt) | 254121 | 6df6339e8cd008fe1370df08576a27b297728042 | cd4a63b22d8bcfe37e610dc0e7562a86d75f3613281267ffc0aa2d9292e9a60a |
| [adv_dear_hmsz_008.txt](https://raw.githubusercontent.com/DreamGallery/Campus-adv-txts/00d150a069a3ffa723a1ff264752ba242024caad/Resource/adv_dear_hmsz_008.txt) | 199442 | c0cd3426b17b91b9955be3ccc2d64574e9d0191e | 7fec42b3926cc328deb6237df0cef980bae8d44aac6790eea5eb4db56e2d2ce4 |
| [adv_dear_hmsz_009.txt](https://raw.githubusercontent.com/DreamGallery/Campus-adv-txts/00d150a069a3ffa723a1ff264752ba242024caad/Resource/adv_dear_hmsz_009.txt) | 237963 | 4a31af7bb075a77ac89f93d8d7b10458e42855f7 | 8be5d42ba9390b8bf8d28af4f00ce6908c390b38dceffa84456d48d55ea98c5c |
| [adv_dear_hmsz_010.txt](https://raw.githubusercontent.com/DreamGallery/Campus-adv-txts/00d150a069a3ffa723a1ff264752ba242024caad/Resource/adv_dear_hmsz_010.txt) | 223884 | 49d4ac8ba94ff8375b8820a03ad616339abb9fbd | 4f8d6665ea799b41fee3a56f5863ce2f0d1379d8e8a514c7f23ad6400b4a61eb |
| [adv_dear_hmsz_011.txt](https://raw.githubusercontent.com/DreamGallery/Campus-adv-txts/00d150a069a3ffa723a1ff264752ba242024caad/Resource/adv_dear_hmsz_011.txt) | 128255 | ded954e326c968f06ef0ba688237c9b3387af046 | d1fb259d725388345e18e90d69c522428232470d5f722dbc9d2c51720146a2a9 |
| [adv_dear_hmsz_012.txt](https://raw.githubusercontent.com/DreamGallery/Campus-adv-txts/00d150a069a3ffa723a1ff264752ba242024caad/Resource/adv_dear_hmsz_012.txt) | 135844 | 6948f271c08ce47d92205a8c202d94439ac104db | 30603dc54b79904b8f3138b7dfa9b904ee615f631f6168081aa8ebaa3db4bd70 |
| [adv_dear_hmsz_013.txt](https://raw.githubusercontent.com/DreamGallery/Campus-adv-txts/00d150a069a3ffa723a1ff264752ba242024caad/Resource/adv_dear_hmsz_013.txt) | 193988 | a9e231e77fcd033660debfab608094e4ae3fef02 | 97fb902e29681e20ff93b7517a14dcdc95523295ffef34c911b341b84e5f0165 |
| [adv_dear_hmsz_014.txt](https://raw.githubusercontent.com/DreamGallery/Campus-adv-txts/00d150a069a3ffa723a1ff264752ba242024caad/Resource/adv_dear_hmsz_014.txt) | 180703 | 7d665de3de0cbf645c6f1933c4a26d149d818d6f | a4357680a306c76cf8915933551a12b60476e102e32ee214ddbd775b32422858 |
| [adv_dear_hmsz_015.txt](https://raw.githubusercontent.com/DreamGallery/Campus-adv-txts/00d150a069a3ffa723a1ff264752ba242024caad/Resource/adv_dear_hmsz_015.txt) | 134411 | b61c7bb0445f2a15c0148bde4edeaaeada0398a3 | 2ad7658a97e917916353f3b121ea0c6567e0fb29b43f87601d23bee73fb85e4d |
| [adv_dear_hmsz_016.txt](https://raw.githubusercontent.com/DreamGallery/Campus-adv-txts/00d150a069a3ffa723a1ff264752ba242024caad/Resource/adv_dear_hmsz_016.txt) | 179854 | 8cd2ea22e9f36a1e0e5f45dfd5f5acf38aa21e86 | 291931d399dba2545099e632090398d031c4a94afc6954eef8ef451ef28c17a8 |
| [adv_dear_hmsz_017.txt](https://raw.githubusercontent.com/DreamGallery/Campus-adv-txts/00d150a069a3ffa723a1ff264752ba242024caad/Resource/adv_dear_hmsz_017.txt) | 300086 | 154a0211f5e2d1e21db9120785f73fb983302e64 | b08964d7ed0d2b79167e0d6b51e03ea177fdd395fc1d7f06ad89912f58fdfe7f |
| [adv_dear_hmsz_018.txt](https://raw.githubusercontent.com/DreamGallery/Campus-adv-txts/00d150a069a3ffa723a1ff264752ba242024caad/Resource/adv_dear_hmsz_018.txt) | 137754 | 99f2376ace21c984ab2cba1cac84677d463a2642 | 9b86d3c7c84a6d183d9f1d926ad571da0df9cb86daeece457fe49444919b11e9 |
| [adv_dear_hmsz_019.txt](https://raw.githubusercontent.com/DreamGallery/Campus-adv-txts/00d150a069a3ffa723a1ff264752ba242024caad/Resource/adv_dear_hmsz_019.txt) | 200311 | ed1871aa3c9d996e1060c318780a5a06b491a49d | 380e23095992b34f3ea6dfd4890c0701e6b285a81b022725ce13069320ce8c93 |
| [adv_dear_hmsz_020.txt](https://raw.githubusercontent.com/DreamGallery/Campus-adv-txts/00d150a069a3ffa723a1ff264752ba242024caad/Resource/adv_dear_hmsz_020.txt) | 204853 | c4e77ecc3c3822371ff3ec79542af64213641a21 | 85abea5f0c4b7333e457bf3673a7c39ae54359b324d4e479cc33ddfcc7e0b7e8 |
| [adv_dear_hmsz_021.txt](https://raw.githubusercontent.com/DreamGallery/Campus-adv-txts/00d150a069a3ffa723a1ff264752ba242024caad/Resource/adv_dear_hmsz_021.txt) | 317132 | 7925ce2d6df8d9225bebcc3588c4b85e6c2bd4a8 | d3cb0cca06a8aea78df05101596494294aa8db70546a40e037d31f4bc9b9a371 |
| [adv_dear_hmsz_022.txt](https://raw.githubusercontent.com/DreamGallery/Campus-adv-txts/00d150a069a3ffa723a1ff264752ba242024caad/Resource/adv_dear_hmsz_022.txt) | 173332 | 8b226f372517a54fb5ae674e554582ca6fc698ce | dfb587fb014d25ccb7c80311ba776e823a3a31ac116e2db520cbe5682c0b2869 |
| [adv_dear_hmsz_023.txt](https://raw.githubusercontent.com/DreamGallery/Campus-adv-txts/00d150a069a3ffa723a1ff264752ba242024caad/Resource/adv_dear_hmsz_023.txt) | 263770 | e87fadd6794cb55b94faf4355bdc0280b71f1eca | 32fef18fc09ac79b7ac5d111f0c181cd1bd7974c7803deff93dae8c96223baa5 |
| [adv_dear_hmsz_024.txt](https://raw.githubusercontent.com/DreamGallery/Campus-adv-txts/00d150a069a3ffa723a1ff264752ba242024caad/Resource/adv_dear_hmsz_024.txt) | 389341 | 0caa924ecb31ba2ee666d0aba61d3e740337b73a | ef5227b2b7550e638b268c8e9a7621d55ffd571118a349924a1f3ead816d984c |
| [adv_dear_hmsz_025.txt](https://raw.githubusercontent.com/DreamGallery/Campus-adv-txts/00d150a069a3ffa723a1ff264752ba242024caad/Resource/adv_dear_hmsz_025.txt) | 228458 | 4e5bda04537e5b603244e549fcc8e3864fc5f4da | b3309ae03e5364eff14f04132e60b955f3e85d57e07391abf761bd92ef49d5ac |
| [adv_dear_hmsz_026.txt](https://raw.githubusercontent.com/DreamGallery/Campus-adv-txts/00d150a069a3ffa723a1ff264752ba242024caad/Resource/adv_dear_hmsz_026.txt) | 277806 | d659fff55531e39f4a3d19dff2c360a29f9eb062 | 244537b94eb2b0d1781a65904a726e2d3ebadcf55b9b70f23d37283e7413a55d |
| [adv_dear_hmsz_027.txt](https://raw.githubusercontent.com/DreamGallery/Campus-adv-txts/00d150a069a3ffa723a1ff264752ba242024caad/Resource/adv_dear_hmsz_027.txt) | 345982 | ad7fdf6b73cc4dce245e1061487224b56206b748 | da842833cc9c876550373773401fa4411591761fb0d45c1e72407f1c7c929b97 |
| [adv_dear_hmsz_028.txt](https://raw.githubusercontent.com/DreamGallery/Campus-adv-txts/00d150a069a3ffa723a1ff264752ba242024caad/Resource/adv_dear_hmsz_028.txt) | 258360 | 0dd5343d78fc035e26094d58e974ae680b58ae58 | 1054627d6187ce4ecf5fabe8abf990f43d63bdfa63b7772db754a6c6224a7ccc |
| [adv_dear_hmsz_029.txt](https://raw.githubusercontent.com/DreamGallery/Campus-adv-txts/00d150a069a3ffa723a1ff264752ba242024caad/Resource/adv_dear_hmsz_029.txt) | 306189 | c3cf0d9f0ae9eb4205c43179c6345a43aa79b9f0 | c51b5ecdb00b2ebc98e771cb535ea2252523f1e110a6f99ed2061daf55ecd227 |
| [adv_dear_hmsz_030.txt](https://raw.githubusercontent.com/DreamGallery/Campus-adv-txts/00d150a069a3ffa723a1ff264752ba242024caad/Resource/adv_dear_hmsz_030.txt) | 269929 | 4bfafa73b0844d1919dd8f537d5ea9d4f1f8e2bc | e89ac0f445e249f1ea0456abcb1626cb5fa9079a15f080eab514523dccf8f00c |
| [adv_dear_hmsz_031.txt](https://raw.githubusercontent.com/DreamGallery/Campus-adv-txts/00d150a069a3ffa723a1ff264752ba242024caad/Resource/adv_dear_hmsz_031.txt) | 350371 | 483e28b46c78ee5da615e15b19a78ee1497b3679 | 0b9de435aa8bde7d7a8b4fd1c96e0a67c3b54c6d01949b6eeeff6d4990046041 |
| [adv_dear_hmsz_032.txt](https://raw.githubusercontent.com/DreamGallery/Campus-adv-txts/00d150a069a3ffa723a1ff264752ba242024caad/Resource/adv_dear_hmsz_032.txt) | 234820 | bfda7caea9aef1f69c670c41ebc11dbcb242a8af | 847fa96a380100de8fc3cf3adbb68865780eefb46dbcca1f542b047b0c7aec77 |
| [adv_dear_hmsz_033.txt](https://raw.githubusercontent.com/DreamGallery/Campus-adv-txts/00d150a069a3ffa723a1ff264752ba242024caad/Resource/adv_dear_hmsz_033.txt) | 201950 | c035e97b3f69e5f3096e49388f11f5e765c707a5 | 3faecb9bdb46354f07c27a3d758b4f757cfa90126b163f3c05379e02e4088b1d |
| [adv_dear_hmsz_034.txt](https://raw.githubusercontent.com/DreamGallery/Campus-adv-txts/00d150a069a3ffa723a1ff264752ba242024caad/Resource/adv_dear_hmsz_034.txt) | 422727 | 126397f89e473164720116130c97e710ced05fbe | 2c7b0b19138d3511fa221274d76d8ff4ef0d21ff2f98764278ac66e7dce315f7 |
| [adv_dear_hmsz_035.txt](https://raw.githubusercontent.com/DreamGallery/Campus-adv-txts/00d150a069a3ffa723a1ff264752ba242024caad/Resource/adv_dear_hmsz_035.txt) | 144552 | 826607df0b175b29bb4075ce1a114ca02a780b5f | 6f20802027ca8c08e883e69c1d9f06eb8227544f750b3e14239a5dba5be92892 |
| [adv_dear_hmsz_036.txt](https://raw.githubusercontent.com/DreamGallery/Campus-adv-txts/00d150a069a3ffa723a1ff264752ba242024caad/Resource/adv_dear_hmsz_036.txt) | 1306912 | ef794c375d3f35c794e47a812e202b8dc1f4619a | 3c339f40171b9d9e33724ebbc9abe22cce71882d4208b499fb4d370239a33940 |
| [adv_dear_hmsz_037.txt](https://raw.githubusercontent.com/DreamGallery/Campus-adv-txts/00d150a069a3ffa723a1ff264752ba242024caad/Resource/adv_dear_hmsz_037.txt) | 275797 | e924654b2e3e859ce9106f6928b9762d9a9e178c | 7cc1dd5585df6b2b61df728d42eac18cc3999b8a2bc346c43223f2a8bf9fe230 |

## Fresh direct visual inspection

### EXEC-MZ-M03-RESENTMENT

- Source: M03 / Drive `149ubZq2LgWA1zuE4U8dICF0X9bZvWv5w`, supplied file `【学マス】 秦谷美鈴 親愛度コミュ21～27話まとめ【STEP3】-(720p60).mp4`.
- Freshly checked SHA-256: `5d78050758fecdf8b961926ee2f1dbdaa7bea9894983d378fff40585a5125763`; this matches the input ZIP's M03 hash.
- Directly inspected frames: 490, 495, 500, 505, 510, 515, 520, 525, 530, 535, 540, 545, 550, 555, 560, 565 seconds. Crop: x=368, y=0, width=544, height=720 from the 1280×720 source.
- Visible observations: the central classroom image alternates waist-up and face views. Misuzu lowers her head with a hand at her chest at 490 seconds; close views at 500–515 retain a small smile and then closed/half-closed eyes while the text describes accumulated hot, muddy feeling. At 525 she folds her arms while asking why she should discharge it; 530–535 put both hands near the chest as she calls it valuable. At 560 she smiles while stating she does not show tears except in exceptional circumstances.
- Exact A1 controls: `Resource/adv_dear_hmsz_022.txt`, raw lines 159–226; specifically 182 (accumulation), 191 (refusal to discharge), 198–202 (value for desire), and 226 (withheld tears).
- Interpretation: the visible combination of composure and explicit negative-affect language supports MZ-AV-004/032's bounded claim that calm presentation does not establish weak stakes. It does not newly establish breath pressure, a resentful vocal register, or an absence of pain outside these frames.

### EXEC-MZ-M03-IDENTITY

- Source/hash/crop: same M03 input and crop as above.
- Directly inspected frames: 1810, 1815, 1820, 1825, 1830, 1835, 1840, 1845, 1850, 1855, 1860, 1865, 1870 seconds.
- Visible observations: an outdoor campus conversation alternates a medium view and close views. At 1840–1850, the caption identifies hurried behavior as incompatible with her chosen idol image while her current face remains composed. The visual evidence here is retrospective explanation of the training period, rather than a filmed record of exhaustion. A hand returns to the chest at 1855–1860, followed by a hand at the mouth at 1865.
- Exact A1 control: `Resource/adv_dear_hmsz_026.txt`, raw lines 66–96; lines 75–94 distinguish raising fundamentals from retaining the desired idol form.
- Interpretation: MZ-AV-033 gains a precise source locator for the character's self-assessment. It remains qualified for claims about newly observed physical fatigue or vocal strain. The document must not turn the composed appearance during a retrospective conversation into proof that the earlier overtraining was harmless.

### EXEC-MZ-M03-PROMISE

- Source/hash/crop: same M03 input and crop as above.
- Directly inspected frames: 1910, 1915, 1920, 1925, 1930, 1935, 1940, 1945, 1950, 1955, 1960, 1965, 1970, 1975, 1980, 1985 seconds.
- Visible observations: the account of impatience at 1910–1925 moves into a closer face view as Misuzu addresses Producer and apologizes at 1930–1935. At 1965–1970 her eyes are closed and head lowered while the caption says the hurt was greater than he supposed and remains. By 1980 the camera is much closer as she requests kind words. At 1985 a choice interface is visible, which cautions against treating the entire rendered response sequence as an unbranching A1 timeline.
- Exact A1 control: `Resource/adv_dear_hmsz_026.txt`, raw lines 137–194, especially 158 (failed promise apology), 186–189 (continuing pain), and 194 (request for kind words).
- Interpretation: concrete staging and exact text support the relational specificity of the hurt. They do not support an isolated acoustic pain metric. Claims MZ-AV-004/012/032/033 retain the distinction between what is visible, stated, and historically heard.

### EXEC-MZ-M03-RECOVERY

- Source/hash/crop: same M03 input and crop as above.
- Directly inspected frames: 2000, 2005, 2010, 2015, 2020, 2025, 2030, 2035, 2040, 2045, 2050, 2055, 2060, 2065, 2070, 2075 seconds.
- Visible observations: the later exchange moves through a narrow-eyed close view at 2010–2015 into a small smile and chin-rest gesture at 2020–2025. The caption at 2035–2040 explicitly pairs stopping the impatience with fulfilling the promise slowly. At 2055–2065 the camera closes in again while the text combines offering Producer a star, yawning at a high place, and subduing the other idols. The sequence does not present rest as abandoned ambition.
- Exact A1 control: `Resource/adv_dear_hmsz_026.txt`, raw lines 260–302, especially 272 (stop hurrying; fulfill slowly), 283–302 (star, yawn, competition).
- Interpretation: fresh textual/visual support for MZ-AV-003/028/034. The reappearance of competitive language after the recovery instruction supplies a better control than equating speed, RMS, or visible workload with ambition.

## Limit on visual coverage

These are directly inspected sequential still samples, with every displayed timestamp listed. They do not certify continuous playback, all intervening frames, direct listening, or full-source audiovisual inspection. Dense still sampling can improve locators and reveal expression/framing changes; it does not by itself measure the smoothness of motion or prove vocal delivery. Full original propositions and their historical analytical confidence remain in the maintained documents, with current review qualifications kept separate.

## New chapter boundaries: all 37 chapters now have operational intervals

The inherited package had 17 container-marker intervals (Dear011–027), ten late interior windows, and ten early chapters without individual boundaries. Fresh inspection closes the twenty missing full chapter-associated intervals using chapter labels in M01 and M04. All 37 chapters now have individually identified, reproducible intervals: 17 inherited marker-defined intervals and 20 newly measured label-cycle intervals. These are two explicitly different boundary methods. They are not 37 manually certified original-game narrative starts.

For the new intervals, a 30-second header survey was refined to one-second transition surveys and then adjacent frames at the actual 30 fps playback rate. The enlarged header crop was `(407,0,100,45)`. Every boundary sheet was directly inspected; machine image differences only helped find likely transitions. A canonical reference frame was chosen at the opening of the newly legible chapter number. A few low-opacity fade frames are ambiguous: frame-number precision makes the chosen interval reproducible, but does not eliminate this semantic uncertainty. No equal-duration division, inferred black-frame chapter count, or script-clock substitution is used.

Each nonfinal interval ends at the next canonical label reference, retaining the intervening uploader crossfade in the preceding compilation segment. For Dear010/037, the end is the first inspected frame after the closing chapter label disappears before uploader ending material. Opening material before the first reference is excluded. M01's omitted opening is 1.166666667 s; M04's is 0.966666667 s. These small openings are not claimed to contain no narrative material. The segments include report screens, choices, BGM and other speakers, and can contain performance inserts. They are suitable for chapter-associated mixed-source descriptors, not isolated dialogue statistics.

| Source | Existing ID | Current local SHA-256 |
| --- | --- | --- |
| M01 | 1Fw_4i3PsiFG-qE3FcpTNPQEH7ZwcVEkd | f7b7c8e6dbdb7199a6ef99429bdf4380d5f7dae9d4e194338d5b398f2ee3f8be |
| M04 | 1zZaheh3YRcrXMFCcWQIS-_Pxd32m3ChE | 38500c9908eee6a44ab630fd6bf317ca1d37e3f4282995a2fb3d45ee2621638a |

| Fresh boundary ID | Dear | Start frame / 30 | End frame / 30 | Start s inclusive | End s exclusive | Direct boundary sheets |
| --- | --- | --- | --- | --- | --- | --- |
| EXEC-MZ-M01-BOUNDARY-001 | 001 | 35 | 6058 | 1.16666666667 | 201.933333333 | M01_frame_header_00.jpg and M01_frame_header_01.jpg |
| EXEC-MZ-M01-BOUNDARY-002 | 002 | 6058 | 15011 | 201.933333333 | 500.366666667 | M01_frame_header_01.jpg and M01_frame_header_02.jpg |
| EXEC-MZ-M01-BOUNDARY-003 | 003 | 15011 | 22178 | 500.366666667 | 739.266666667 | M01_frame_header_02.jpg and M01_frame_header_03.jpg |
| EXEC-MZ-M01-BOUNDARY-004 | 004 | 22178 | 30201 | 739.266666667 | 1006.7 | M01_frame_header_03.jpg and M01_frame_header_04.jpg |
| EXEC-MZ-M01-BOUNDARY-005 | 005 | 30201 | 37808 | 1006.7 | 1260.26666667 | M01_frame_header_04.jpg and M01_frame_header_05.jpg |
| EXEC-MZ-M01-BOUNDARY-006 | 006 | 37808 | 46448 | 1260.26666667 | 1548.26666667 | M01_frame_header_05.jpg and M01_frame_header_06.jpg |
| EXEC-MZ-M01-BOUNDARY-007 | 007 | 46448 | 53704 | 1548.26666667 | 1790.13333333 | M01_frame_header_06.jpg and M01_frame_header_07.jpg |
| EXEC-MZ-M01-BOUNDARY-008 | 008 | 53704 | 62785 | 1790.13333333 | 2092.83333333 | M01_frame_header_07.jpg and M01_frame_header_08.jpg |
| EXEC-MZ-M01-BOUNDARY-009 | 009 | 62785 | 71951 | 2092.83333333 | 2398.36666667 | M01_frame_header_08.jpg and M01_frame_header_09.jpg |
| EXEC-MZ-M01-BOUNDARY-010 | 010 | 71951 | 82596 | 2398.36666667 | 2753.2 | M01_frame_header_09.jpg and M01_frame_header_10.jpg |
| EXEC-MZ-M04-BOUNDARY-028 | 028 | 29 | 9894 | 0.966666666667 | 329.8 | M04_frame_header_00.jpg and M04_frame_header_01.jpg |
| EXEC-MZ-M04-BOUNDARY-029 | 029 | 9894 | 21705 | 329.8 | 723.5 | M04_frame_header_01.jpg and M04_frame_header_02.jpg |
| EXEC-MZ-M04-BOUNDARY-030 | 030 | 21705 | 30322 | 723.5 | 1010.73333333 | M04_frame_header_02.jpg and M04_frame_header_03.jpg |
| EXEC-MZ-M04-BOUNDARY-031 | 031 | 30322 | 43840 | 1010.73333333 | 1461.33333333 | M04_frame_header_03.jpg and M04_frame_header_04.jpg |
| EXEC-MZ-M04-BOUNDARY-032 | 032 | 43840 | 53614 | 1461.33333333 | 1787.13333333 | M04_frame_header_04.jpg and M04_frame_header_05.jpg |
| EXEC-MZ-M04-BOUNDARY-033 | 033 | 53614 | 64870 | 1787.13333333 | 2162.33333333 | M04_frame_header_05.jpg and M04_frame_header_06.jpg |
| EXEC-MZ-M04-BOUNDARY-034 | 034 | 64870 | 75777 | 2162.33333333 | 2525.9 | M04_frame_header_06.jpg and M04_frame_header_07.jpg |
| EXEC-MZ-M04-BOUNDARY-035 | 035 | 75777 | 82441 | 2525.9 | 2748.03333333 | M04_frame_header_07.jpg and M04_frame_header_08.jpg |
| EXEC-MZ-M04-BOUNDARY-036 | 036 | 82441 | 102545 | 2748.03333333 | 3418.16666667 | M04_frame_header_08.jpg and M04_frame_header_09.jpg |
| EXEC-MZ-M04-BOUNDARY-037 | 037 | 102545 | 114565 | 3418.16666667 | 3818.83333333 | M04_frame_header_09.jpg and M04_frame_header_10.jpg |

The start/end columns are canonical calculation inputs; the frame counts divided by 30 retain exact rational locators. The fresh numerical outputs, versions, processing fingerprints and complete per-frame numerical rows are in [EXECUTION_MEASUREMENTS.md](EXECUTION_MEASUREMENTS.md). Inherited late interior-window results remain labeled in the old detailed ledger so they cannot be confused with these longer intervals. M01 [2753.2,2917.958821) s and M04 [3818.833333333,4048.631293) s are excluded ending regions; final container tails are included in those exclusions, not chapter totals.

## New first/last content controls for boundary assignment

After selecting each chapter label, two central scene samples were inspected at `start+5` and `end-7` seconds. These are content controls, not a claim to have found every first/last utterance. For each row the adjacent header sheets above establish the chapter number; the images below additionally identify the scene and occasional report/transition screens. A title card or transition is reported as such instead of invented dialogue.

| Dear/source | Inspected times s | Observed scene/caption control | A1 raw-line control |
| --- | --- | --- | --- |
| 001/M01 | 6.16666666667, 194.933333333 | Tea-room episode title; last sample smiling Misuzu after first high-place promise | Dear001 raw252 and262; first greeting separately inspected at28–52s |
| 002/M01 | 206.933333333, 493.366666667 | Misuzu greets Producer in courtyard; report screen describes her behavior | Dear002 raw12 and277–278 |
| 003/M01 | 505.366666667, 732.266666667 | Blue in-game transition with Dear3 header; later Producer report screen | Dear003 raw218–220; header identifies interval independently of transition image |
| 004/M01 | 744.266666667, 999.7 | Asari classroom; Producer says Misuzu herself is progressing; report screen closes | Dear004 raw11 and249–251 |
| 005/M01 | 1011.7, 1253.26666667 | Misuzu complains of cloudy days; Producer report screen | Dear005 raw6 and228–230 |
| 006/M01 | 1265.26666667, 1541.26666667 | Misuzu says the day has come; later desk/report transition | Dear006 raw12; final report text267–269 remains A1 control, not claimed legible in this frame |
| 007/M01 | 1553.26666667, 1783.13333333 | Misuzu in dressing-room setting; later Producer report screen | Dear007 raw426–428; anger passage separately inspected below |
| 008/M01 | 1795.13333333, 2085.83333333 | Vocal trainer opens meeting; report caption credits protection of her pace | Dear008 raw7 and333 |
| 009/M01 | 2097.83333333, 2391.36666667 | Sleeping Misuzu and Producer waking her; later report revision caption | Dear009 raw16 and405 |
| 010/M01 | 2403.36666667, 2746.2 | Temari thanks Producer for moving help; final illustrated Misuzu promises to walk together | Dear010 raw18 and392 |
| 028/M04 | 5.96666666667, 322.8 | Misuzu naps/greeting in classroom; ending close view asks Producer to worry for her | Dear028 raw7 and436 |
| 029/M04 | 334.8, 716.5 | Sena entering school corridor; ending chairman silhouette introduces prior Prima Stella | Dear029 raw10–33 and508–510 |
| 030/M04 | 728.5, 1003.73333333 | Producer addresses Temari before meeting; Sena invites watching the top-idol stage | Dear030 raw16 and446–454 |
| 031/M04 | 1015.73333333, 1454.33333333 | Costumed Misuzu reacts to stage; later thanks senior | Dear031 raw13 and583 |
| 032/M04 | 1466.33333333, 1780.13333333 | Temari reports a fulfilling challenge; ending promise to make Misuzu cry with her song | Dear032 raw7 and398 |
| 033/M04 | 1792.13333333, 2155.33333333 | Misuzu thinking, long ellipsis; ending promises a happy path | Dear033 raw8 and356 |
| 034/M04 | 2167.33333333, 2518.9 | Temari asks about departure preparation; ending Temari support before farewell | Dear034 raw9 and chapter-ending exchange; label/caption controls identify content |
| 035/M04 | 2530.9, 2741.03333333 | Costumed Misuzu disputes Producer waking her; ending promises one dream | Dear035 raw12 and244–249 |
| 036/M04 | 2753.03333333, 3411.16666667 | Arena audience and headmaster announcement; ending tearful Misuzu with Temari | Dear036 raw267 and1404–1413; dense tears record below |
| 037/M04 | 3423.16666667, 3811.83333333 | Rooftop Producer/Misuzu encounter; final illustrated Misuzu proposes fulfilling promise | Dear037 raw15 and436; dense final-yawn record below |

These forty samples were displayed as `M01_content_anchors_01/02.jpg` and `M04_content_anchors_01/02.jpg`, with requested and decoder-reported timestamps saved in the working frame logs. Both sources' hashes above bind the controls.

## Fresh early/late visual-textual passage review

### EXEC-MZ-M01-GREETING

- Existing source: `M01=1Fw_4i3PsiFG-qE3FcpTNPQEH7ZwcVEkd`; input SHA-256 `f7b7c8e6dbdb7199a6ef99429bdf4380d5f7dae9d4e194338d5b398f2ee3f8be`.
- Directly inspected times: 24–62 s inclusive, every 2 s (20 images). Mode: ordered extracted stills; crop `393,0,494,720` in source pixels. The timestamps are source-relative, not script time. All specified images were displayed to the executing reviewer.
- Visible observations: A close view with closed eyes at24s opens to a smile; she bows at32s and returns upright by34s. At42–46s her hands meet near her chest while politely thanking the invitation; the refusal at48–52s retains a small smile and close framing.
- Exact locked text/control: Resource/adv_dear_hmsz_001.txt raw59–92, especially the introduction and inability-to-meet-expectation refusal.
- Claim consequences: MZ-AV-001/007/031 receive precise visual/textual controls for courteous presentation. A smile or bow does not establish benevolence by itself, and no vocal softness is newly heard.
- Reproduction locator: frame schedule `m01_greeting`; generate every stated timestamp with the extractor below. Local contact sheets and JSON logs remain working evidence outside this Markdown-only package.

### EXEC-MZ-M01-CARE

- Existing source: `M01=1Fw_4i3PsiFG-qE3FcpTNPQEH7ZwcVEkd`; input SHA-256 `f7b7c8e6dbdb7199a6ef99429bdf4380d5f7dae9d4e194338d5b398f2ee3f8be`.
- Directly inspected times: 828–866 s inclusive, every 2 s (20 images). Mode: ordered extracted stills; crop `393,0,494,720` in source pixels. The timestamps are source-relative, not script time. All specified images were displayed to the executing reviewer.
- Visible observations: Medium view with hands near chest at828–832s precedes the statement at836–840s that she likes caring for close people. At846–852s the camera closes while she says friends were too self-sufficient for her satisfaction. At854–858s her hands return together as she asks to care for Producer; his rest reminder at860s is followed by her bow and smile.
- Exact locked text/control: Resource/adv_dear_hmsz_004.txt raw90–112; care, dissatisfaction with independence, request, and no-tiredness reply occur in this exact order.
- Claim consequences: MZ-AV-001/006/007/031: care and desire to be needed coexist in the same visible exchange. This sharpens the duality without declaring every act manipulative or newly certifying tonal warmth.
- Reproduction locator: frame schedule `m01_care`; generate every stated timestamp with the extractor below. Local contact sheets and JSON logs remain working evidence outside this Markdown-only package.

### EXEC-MZ-M01-ENCLOSURE

- Existing source: `M01=1Fw_4i3PsiFG-qE3FcpTNPQEH7ZwcVEkd`; input SHA-256 `f7b7c8e6dbdb7199a6ef99429bdf4380d5f7dae9d4e194338d5b398f2ee3f8be`.
- Directly inspected times: 1194–1232 s inclusive, every 2 s (20 images). Mode: ordered extracted stills; crop `393,0,494,720` in source pixels. The timestamps are source-relative, not script time. All specified images were displayed to the executing reviewer.
- Visible observations: An eyes-closed, hands-together medium pose accompanies restful-feeling language at1194–1198s. After Producer asks if that is all, the camera closes at1206–1214s: the same composed face and hands accompany filling others' hearts with herself and making them unable to live without her. At1216s Producer reacts; she folds one arm and returns to direct admission at1228–1232s.
- Exact locked text/control: Resource/adv_dear_hmsz_005.txt raw176–201 (possession, dependence, own true intention, complaint redirected to Producer).
- Claim consequences: MZ-AV-001/006/007/031 receive a concrete comparison with the care passage. The shared visible composure supports continuity of presentation; it does not supply a new acoustic comparison.
- Reproduction locator: frame schedule `m01_enclosure`; generate every stated timestamp with the extractor below. Local contact sheets and JSON logs remain working evidence outside this Markdown-only package.

### EXEC-MZ-M01-ANGER

- Existing source: `M01=1Fw_4i3PsiFG-qE3FcpTNPQEH7ZwcVEkd`; input SHA-256 `f7b7c8e6dbdb7199a6ef99429bdf4380d5f7dae9d4e194338d5b398f2ee3f8be`.
- Directly inspected times: 1696–1746 s inclusive, every 2 s (26 images). Mode: ordered extracted stills; crop `393,0,494,720` in source pixels. The timestamps are source-relative, not script time. All specified images were displayed to the executing reviewer.
- Visible observations: Temari asks if Misuzu is angry at1700–1702s; a close view at1704s explicitly answers yes. Misuzu's relatively level face and small mouth movement are followed by hand-to-chin at1708s, a wider view saying she will scold at1714s, and hands gathered at chest while reserving trouble for herself at1722–1724s. At1730s she asserts that she is speaking, and Temari acknowledges hearing this from her for the first time at1738–1742s.
- Exact locked text/control: Resource/adv_dear_hmsz_007.txt raw300–381; explicit anger307, own scolding328, exclusivity338, self-authored address347 and later regret381.
- Claim consequences: MZ-AV-008/009 renew the reciprocal-conflict textual/visible control. This is restrained visible posture alongside explicit anger, not a measured intensity or newly heard anger contour.
- Reproduction locator: frame schedule `m01_anger`; generate every stated timestamp with the extractor below. Local contact sheets and JSON logs remain working evidence outside this Markdown-only package.

### EXEC-MZ-M01-FIRST-PROMISE

- Existing source: `M01=1Fw_4i3PsiFG-qE3FcpTNPQEH7ZwcVEkd`; input SHA-256 `f7b7c8e6dbdb7199a6ef99429bdf4380d5f7dae9d4e194338d5b398f2ee3f8be`.
- Directly inspected times: 175–194 s inclusive, every 1 s (20 images). Mode: ordered extracted stills; crop `393,0,494,720` in source pixels. The timestamps are source-relative, not script time. All specified images were displayed to the executing reviewer.
- Visible observations: Misuzu accepts the proposal at181–184s, gathers hands at chest in closer framing for slow/steady walking at185–189s, then speaks of yawning together high up at190–194s with an opening smile and head tilt.
- Exact locked text/control: Resource/adv_dear_hmsz_001.txt raw240–262, especially252.
- Claim consequences: MZ-AV-003/012/036: this directly located beginning supplies the other half of the Dear037 callback. It is a spoken proposition displayed in captions, not a bodily or heard yawn in Dear001.
- Reproduction locator: frame schedule `m01_first_promise`; generate every stated timestamp with the extractor below. Local contact sheets and JSON logs remain working evidence outside this Markdown-only package.

### EXEC-MZ-M01-POSSESSIVE-CLOSE

- Existing source: `M01=1Fw_4i3PsiFG-qE3FcpTNPQEH7ZwcVEkd`; input SHA-256 `f7b7c8e6dbdb7199a6ef99429bdf4380d5f7dae9d4e194338d5b398f2ee3f8be`.
- Directly inspected times: 2714–2752 s inclusive, every 2 s (20 images). Mode: ordered extracted stills; crop `393,0,494,720` in source pixels. The timestamps are source-relative, not script time. All specified images were displayed to the executing reviewer.
- Visible observations: In courtyard sunset framing, hands at chest accompany the wish that the world look at her, followed by Producer's promise choice at2732s. The image shifts through white at2738s into an illustrated close portrait at2740s. Walking together at2744–2748s leads to the exclusive Producer phrase and eyes-closed smile at2750s.
- Exact locked text/control: Resource/adv_dear_hmsz_010.txt raw371–394, especially380 (high-place yawn callback) and384–394 (choice, walking, exclusivity).
- Claim consequences: MZ-AV-001/012: intimacy and exclusivity coexist with a mutually acknowledged promise. This supports relation-specific presentation, leaving actual voice quality and authority asymmetry separately open.
- Reproduction locator: frame schedule `m01_possessive`; generate every stated timestamp with the extractor below. Local contact sheets and JSON logs remain working evidence outside this Markdown-only package.

### EXEC-MZ-M04-TEARS

- Existing source: `M04=1zZaheh3YRcrXMFCcWQIS-_Pxd32m3ChE`; input SHA-256 `38500c9908eee6a44ab630fd6bf317ca1d37e3f4282995a2fb3d45ee2621638a`.
- Directly inspected times: 3348–3416 s inclusive, every 2 s (35 images). Mode: ordered extracted stills; crop `393,0,494,720` in source pixels. The timestamps are source-relative, not script time. All specified images were displayed to the executing reviewer.
- Visible observations: Temari asks about the origin of idol ambition at3348–3356s. Misuzu's tear-lined eyes appear in a close view at3364–3366s as she names Temari's admiration. At3382–3386s, tears remain while she asks whether she has become a top idol. Temari asks whether she may decide; Misuzu says no at3390–3392s. Framing moves into an embrace around3400s; tearful close views continue through3416s with Temari's promise to listen.
- Exact locked text/control: Resource/adv_dear_hmsz_036.txt raw1252–1413; uncertainty1322–1330, Temari's question1338, refusal1347, listening1404–1413.
- Claim consequences: MZ-AV-004/005/009/035: visible vulnerability does not erase the explicit textual refusal to outsource self-definition. This is a bounded interpretive control within D-MISUZU, not a conclusion that the new reviewer heard crying or that sovereignty is ethically settled.
- Reproduction locator: frame schedule `m04_tears`; generate every stated timestamp with the extractor below. Local contact sheets and JSON logs remain working evidence outside this Markdown-only package.

### EXEC-MZ-M04-YAWN

- Existing source: `M04=1zZaheh3YRcrXMFCcWQIS-_Pxd32m3ChE`; input SHA-256 `38500c9908eee6a44ab630fd6bf317ca1d37e3f4282995a2fb3d45ee2621638a`.
- Directly inspected times: 3784–3819 s inclusive, every 1 s (36 images). Mode: ordered extracted stills; crop `393,0,494,720` in source pixels. The timestamps are source-relative, not script time. All specified images were displayed to the executing reviewer.
- Visible observations: The rooftop illustration continues through a reciprocal top-idol/top-producer exchange. Producer's yawn anticipation appears at3798–3799s; Misuzu shares it at3800–3807s and offers to fulfill the promise at3808–3811s. At3812s the speaker label changes to ふたり while the moon begins to crossfade over her illustration. Moon-only imagery and the shared-yawn caption remain at3813–3815s, followed by caption disappearance/fade and uploader art at3819s.
- Exact locked text/control: Resource/adv_dear_hmsz_037.txt raw425–441, especially433–441. Compare fresh Dear001 raw252 atM01 190–194s.
- Claim consequences: MZ-AV-003/012/034/036: the callback and reciprocal caption are directly renewed. No full-body yawn, two audible voices, prosody or heard timing is asserted from these images. Ethical significance remains an interpretation rather than a fact measured by loudness.
- Reproduction locator: frame schedule `m04_yawn`; generate every stated timestamp with the extractor below. Local contact sheets and JSON logs remain working evidence outside this Markdown-only package.

## Fresh dense music/performance frame review

These targeted 20-second sequences replace selected four-snapshot gaps with 41 ordered images each, sampled every 0.5 s including both endpoints. They are not full-source playback, motion-capture analysis, frame-complete editing counts, or an audio comparison. Camera translation, lighting and editing remain distinct from the performer changing pose. The windows were selected to test the existing repertoire, stillness and group-position claims; they are not a random sample or a claimed song-wide distribution. No lyrics are inferred from the audio.

### EXEC-MZ-M10-PERFORMANCE

- Existing source: `M10=1WmrTOKijFtOCAUZeN_T361MXAx6SBgDC`; input SHA-256 `a88ad4fe405de061a3877d53cdbe238910e549a70bee1df9bbf0ef6039a73154`.
- Directly inspected times: 50–70 s inclusive, every 0.5 s (41 images). Mode: ordered extracted stills; crop `none; full decoded image resized to 360×203 maximum` in source pixels. The timestamps are source-relative, not script time. All specified images were displayed to the executing reviewer.
- Visible observations: Tsuki no Kame 3DMV: At50–51.5s Misuzu opens an arm and changes torso orientation;52–54.5s uses wide orbital-stage views. Close views at56–57.5s move from raised fingers by the face to raised hands and a horizontal face-level gesture. Later overhead and close views alternate while purple lighting shifts toward green around65.5–67s.
- Exact locked text/control: Existing locked source identity and historical textual/music claim, not a new transcript or inferred lyric.
- Claim consequences: MZ-AV-016/024/025/029: the night/orbital staging is concrete; the passage is not literal stillness. No comparative dance speed or sung calmness is established.
- Reproduction locator: frame schedule `M10_motion`; generate every stated timestamp with the extractor below. Local contact sheets and JSON logs remain working evidence outside this Markdown-only package.

### EXEC-MZ-M24-PERFORMANCE

- Existing source: `M24=14TF8iaQLD4mibJIlLy1UZmx43m4LffTM`; input SHA-256 `af4f7355ac382dce4772a63cf365cda05b20f429a0be573c699a320e867de01b`.
- Directly inspected times: 40–60 s inclusive, every 0.5 s (41 images). Mode: ordered extracted stills; crop `none; full decoded image resized to 360×203 maximum` in source pixels. The timestamps are source-relative, not script time. All specified images were displayed to the executing reviewer.
- Visible observations: Gamushara ni Ikou! solo performance: At40–43s the school-set performance depicts a lowered head/lean over a desk; thought-bubble graphics accompany chin-rest poses at44–45.5s. A bottle gesture occurs at46–47s; she stands and turns at49.5–51s. At53.5s the image switches to a graphic set with emphatic arm/face poses, followed by downward head and near-eye gesture at56–58s.
- Exact locked text/control: Existing locked source identity and historical textual/music claim, not a new transcript or inferred lyric.
- Claim consequences: MZ-AV-002/024/025/028: visible strain-like and comic actions are part of staged repertoire; they do not make suffering her moral ideal or document real physical exhaustion.
- Reproduction locator: frame schedule `M24_motion`; generate every stated timestamp with the extractor below. Local contact sheets and JSON logs remain working evidence outside this Markdown-only package.

### EXEC-MZ-M23-PERFORMANCE

- Existing source: `M23=1FD-G-EejV1b4YCNwfXdiTs4MC1y_fh4R`; input SHA-256 `0fa235b1eb273707fbd33438a79b9b3cff2df3108d713d70c1758efb3c701fec`.
- Directly inspected times: 40–60 s inclusive, every 0.5 s (41 images). Mode: ordered extracted stills; crop `none; full decoded image resized to 360×203 maximum` in source pixels. The timestamps are source-relative, not script time. All specified images were displayed to the executing reviewer.
- Visible observations: Howling over the World solo performance: The performer alternates open arms, directed reach and lowered crouching/kneeling poses among luminous chain-like structures. A floor-level/kneeling position is visible around51–55s; at55.5–60s the presentation alternates industrial neon setting and close views. Red, cyan and green cuts contribute strongly to image differences.
- Exact locked text/control: Existing locked source identity and historical textual/music claim, not a new transcript or inferred lyric.
- Claim consequences: MZ-AV-024/025/026: concrete pose variation and source form are renewed. Whether singing softness survives the repertoire remains UNRESOLVED in direct auditory review; open mouth and sharp lighting cannot answer it.
- Reproduction locator: frame schedule `M23_motion`; generate every stated timestamp with the extractor below. Local contact sheets and JSON logs remain working evidence outside this Markdown-only package.

### EXEC-MZ-M20-PERFORMANCE

- Existing source: `M20=16up-So-St6oIqDkLO8fO5hmDcp675ras`; input SHA-256 `05bfb52fef8398601a86d4db2920cdf8d4670ea2a6c739ece52336249aab0525`.
- Directly inspected times: 50–70 s inclusive, every 0.5 s (41 images). Mode: ordered extracted stills; crop `none; full decoded image resized to 360×203 maximum` in source pixels. The timestamps are source-relative, not script time. All specified images were displayed to the executing reviewer.
- Visible observations: Hajime solo 3DMV: A handheld microphone is retained while the free arm opens at50–50.5s; the image cuts to lifted/stepping feet at52–52.5s. Later free-hand gestures, turns and medium/wide stage views continue through61s; expressive head/hand poses at61.5–66s lead into brighter warm-light smiling address at67.5–69.5s.
- Exact locked text/control: Existing locked source identity and historical textual/music claim, not a new transcript or inferred lyric.
- Claim consequences: MZ-AV-025/039: this source was not visually sampled in the incoming four-point set. The fresh sequence supplies a source-specific performance locator and variation control; it does not prove a unique vocal signature.
- Reproduction locator: frame schedule `M20_motion`; generate every stated timestamp with the extractor below. Local contact sheets and JSON logs remain working evidence outside this Markdown-only package.

### EXEC-MZ-M22-PERFORMANCE

- Existing source: `M22=1hoOWfl9Xf-XefaIRyTskrcUdHiQeOrNa`; input SHA-256 `e13c304126711786c8bc9efedbc1dbb22c0df7b67a57dcb0676d6ade51a404c8`.
- Directly inspected times: 35–55 s inclusive, every 0.5 s (41 images). Mode: ordered extracted stills; crop `none; full decoded image resized to 360×203 maximum` in source pixels. The timestamps are source-relative, not script time. All specified images were displayed to the executing reviewer.
- Visible observations: Miracle Nanau solo performance: Colored stage screens and mascot/game graphics accompany changing arm and orientation poses at35–50.5s. At51s a white transition leads into a flat green interface-like world; Misuzu walks then sits at a desk around51.5–53.5s. Blue icon graphics and smiling close address follow at54–55s.
- Exact locked text/control: Existing locked source identity and historical textual/music claim, not a new transcript or inferred lyric.
- Claim consequences: MZ-AV-024/027/039: comic/interface scenery and acted everyday actions are plainly present. The images renew visual repertoire breadth while comic vocal timing remains unauditioned.
- Reproduction locator: frame schedule `M22_motion`; generate every stated timestamp with the extractor below. Local contact sheets and JSON logs remain working evidence outside this Markdown-only package.

### EXEC-MZ-M17-PERFORMANCE

- Existing source: `M17=1UyUsSr7ZUed6Kh6oHtIsmyjo4GiWvLTo`; input SHA-256 `f1143c1aaa2ca5df6c577c1b9d27c88cc19208e0c6218441455547a8e5130430`.
- Directly inspected times: 65–85 s inclusive, every 0.5 s (41 images). Mode: ordered extracted stills; crop `none; full decoded image resized to 360×203 maximum` in source pixels. The timestamps are source-relative, not script time. All specified images were displayed to the executing reviewer.
- Visible observations: Star-mine shared 3DMV: Three performers occupy the stage at65–66s. Misuzu moves to a foreground close view at67.5–69.5s with the other two behind/on opposing axes; golden-light close views hold her at71–74s. A trio wide view returns at74.5–76s, Misuzu receives further close views at77–78.5s, Sena is foregrounded at79–82.5s, and the other member receives close framing around84.5–85s.
- Exact locked text/control: Existing locked source identity and historical textual/music claim, not a new transcript or inferred lyric.
- Claim consequences: MZ-AV-021/022/023/037/040/045: Misuzu receives sustained local foregrounding within distributed group presentation. This is stronger than a single center pose, but neither total shot-share nor universal mediation is measured. The independent-stars ethical question remains open.
- Reproduction locator: frame schedule `M17_shared`; generate every stated timestamp with the extractor below. Local contact sheets and JSON logs remain working evidence outside this Markdown-only package.

### EXEC-MZ-M18-PERFORMANCE

- Existing source: `M18=1emxDRAvHC46s-v0x4eYFW1pCjdDGvIM9`; input SHA-256 `d0ce84afef4bb91d1f20f15ecd02fe459f5a906cd6b64b9abda98e299f837fd6`.
- Directly inspected times: 75–95 s inclusive, every 0.5 s (41 images). Mode: ordered extracted stills; crop `none; full decoded image resized to 360×203 maximum` in source pixels. The timestamps are source-relative, not script time. All specified images were displayed to the executing reviewer.
- Visible observations: Star-mine shared authored MV: Rotating circular masks reveal individual illustrated portraits in succession: Misuzu at75s, red-haired member around76.5–78s, Sena at79–83s; a star-field image intervenes. Misuzu returns against orbital graphics at84.5–88.5s. All three figures share a radial composition at89.5–94s, followed by the star field again.
- Exact locked text/control: Existing locked source identity and historical textual/music claim, not a new transcript or inferred lyric.
- Claim consequences: MZ-AV-021/022/037/040/045: this is graphic/illustrative composition and mask animation rather than the rendered 3DMV blocking. The two excerpts are not asserted to be temporally synchronized, and visible individuality does not settle the philosophical sovereignty claim.
- Reproduction locator: frame schedule `M18_shared`; generate every stated timestamp with the extractor below. Local contact sheets and JSON logs remain working evidence outside this Markdown-only package.

### EXEC-MZ-M26-SOURCE-FORM

- Existing source: `M26=1RKfLuzy0LHXCOwYry2Dtv9XPAnngly55`; input SHA-256 `4e527d9c1eb85480bfb36cd21998005c3da22e2805894c23ce4f5f46ec0e0efb`.
- Directly inspected times: 20, 120, 220 s (3 images). Mode: ordered extracted stills; crop `none; full decoded image resized to 360×203 maximum` in source pixels. The timestamps are source-relative, not script time. All specified images were displayed to the executing reviewer.
- Visible observations: All three display the same square cover design of colored interlocking Howling rings on black. No rendered performers or choreography are visible in these inspected images.
- Exact locked text/control: Shared source identity; this is an image-form control, not a listening pass.
- Claim consequences: MZ-AV-026/037/040: the audio-source cover cannot provide group-blocking evidence or resolve vocal softness.
- Reproduction locator: frame schedule `M26_shared`; generate every stated timestamp with the extractor below. Local contact sheets and JSON logs remain working evidence outside this Markdown-only package.

## Reproduction of fresh visual locators

The following self-contained Python function reproduces named frame schedules without needing an unbundled working JSON. Supply the exact hash-bound input path from the manifest. For boundary crops use `(407,0,100,45)` and frame indices from the boundary table; for readable central story images use `(393,0,494,720)` in M01/M04 or `(368,0,544,720)` in M03. Performance sequences use the whole frame. The function saves local images; it does not certify that an observer has viewed or heard them. Exact boundary frames are requested by frame index at 30 fps; ordinary passage schedules use source-relative seconds. Selecting an audio stream never creates a listening observation.

```python
from pathlib import Path
import hashlib, cv2
from PIL import Image

def verify_source(path, expected_sha256):
    h = hashlib.sha256()
    with Path(path).open('rb') as f:
        for block in iter(lambda: f.read(1024 * 1024), b''):
            h.update(block)
    assert h.hexdigest() == expected_sha256, 'Different source bytes'

def frames(path, expected_sha256, out_dir, times=None,
           indices=None, crop=None):
    verify_source(path, expected_sha256)
    assert (times is None) != (indices is None)
    out = Path(out_dir); out.mkdir(parents=True, exist_ok=True)
    cap = cv2.VideoCapture(str(path)); assert cap.isOpened()
    schedule = indices if indices is not None else times
    for value in schedule:
        mode = cv2.CAP_PROP_POS_FRAMES if indices is not None else cv2.CAP_PROP_POS_MSEC
        cap.set(mode, value if indices is not None else value * 1000)
        ok, frame = cap.read(); assert ok, value
        reported_s = cap.get(cv2.CAP_PROP_POS_MSEC) / 1000
        if crop is not None:
            x, y, w, h = crop; frame = frame[y:y+h, x:x+w]
        im = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        im.save(out / f'{value}_{reported_s:.9f}s.png')
    cap.release()

# Exact boundary example: inspect frame35 and its immediate neighbors.
# frames(M01_path, M01_sha256, 'boundary001',
#        indices=[33,34,35,36,37], crop=(407,0,100,45))
# Dense performance example: 40..60 s inclusive at0.5 s cadence.
# frames(M23_path, M23_sha256, 'howling',
#        times=[40+k/2 for k in range(41)])
```

To retrieve the locked text, use the exact raw URLs in the acquisition table. Git blob verification is `sha1(b'blob '+str(len(payload)).encode()+b'\0'+payload)`, checked against the table; raw-line references count UTF-8 text lines beginning at1. No later upstream revision or script-time offset replaces video inspection.

## Limits that remain after execution

The chapter-locator gap is closed under the stated operational convention. Source checks establish present bytes rather than retrospectively proving the old acquisition run. Fresh ordered images renew the identified visual/textual facets; full audiovisual re-verification remains partial because direct listening is unavailable and still sampling omits intervening frames. Machine audio trials and ASR, if delivered elsewhere in this package, retain their own acceptance/rejection records. They do not convert these entries into heard performances. The six UNRESOLVED review dispositions include both absent new auditory evidence and intentionally open ethical/relational questions; those are not all media-acquisition blockers.
