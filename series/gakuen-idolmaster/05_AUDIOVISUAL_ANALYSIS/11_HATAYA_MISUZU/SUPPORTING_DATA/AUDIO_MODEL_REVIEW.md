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

# MISUZU — current automated audio trials and ASR locator review

**Disposition: no freeform audio-model judgment is adopted as qualitative evidence.** Nine bounded clips were processed by a pinned Japanese ASR model as locator aids; five of those clips were also tested with two freeform audio-description models. This is machine-assisted processing, not direct listening by this reviewer. No current claim is upgraded to supported on the basis of these descriptions, and the direct-listening dependency remains explicit.

The host returned an explicit audio-input-unsupported response when a local test excerpt was supplied through its native audio channel. To pursue the authorized audiovisual work, a local audio/ASR environment was installed and tested. The results below record what those tools actually did; extraction, a populated transcript, or a fluent model answer is not treated as hearing the source.

Locked A1 scripts and directly viewed captions remain the wording and scene controls, as documented in [the character execution review](EXECUTION_EXTENSION_20260910.md). Their source lock is `DreamGallery/Campus-adv-txts` commit `00d150a069a3ffa723a1ff264752ba242024caad`, revision 32. ASR errors, clipped words, omissions, and inferred segment/word times are not promoted into canonical dialogue. Producer lines visible on-screen can be unvoiced message events; absence from an ASR output is not evidence that a visible exchange did not occur.

## Scope, inputs and clip identity

All times use the source MP4 clock, with inclusive start/exclusive end extraction. The first audio stream is decoded through FFmpeg `atrim`, reset to zero, downmixed to mono and resampled to 16000 Hz float32. There is no normalization, denoising, source separation, speaker isolation or diarization. Clip hashes below cover the exact little-endian float32 bytes passed to the models; they are not hashes of a WAV header or encoded media file.

| Source alias | Recorded Drive ID | Actual input SHA-256 | Actual filename |
| --- | --- | --- | --- |
| M03 | 149ubZq2LgWA1zuE4U8dICF0X9bZvWv5w | 5d78050758fecdf8b961926ee2f1dbdaa7bea9894983d378fff40585a5125763 | 【学マス】 秦谷美鈴 親愛度コミュ21～27話まとめ【STEP3】-(720p60).mp4 |
| M01 | 1Fw_4i3PsiFG-qE3FcpTNPQEH7ZwcVEkd | f7b7c8e6dbdb7199a6ef99429bdf4380d5f7dae9d4e194338d5b398f2ee3f8be | 【学マス】秦谷美鈴　親愛度１～１０話【アイドルコミュ】-(720p30).mp4 |
| M04 | 1zZaheh3YRcrXMFCcWQIS-_Pxd32m3ChE | 38500c9908eee6a44ab630fd6bf317ca1d37e3f4282995a2fb3d45ee2621638a | 【学マス】秦谷美鈴　親愛度２８～３７話【アイドルコミュ STEP4 HIF】-(720p30).mp4 |

Full local receipt routes, sizes, probes, shared relationships and source-identity qualifications are in [current source verification](EXECUTION_SOURCE_VERIFICATION.md).

| Clip ID | Source start s | Source end s | Duration s | PCM samples | PCM SHA-256 |
| --- | --- | --- | --- | --- | --- |
| M03_509_534 | 509 | 534 | 25.0 | 400000 | 883796147fd2c587bfe405f368e5b1a68455d2f9847112803ac26a97f4ba774d |
| M03_1930_1954 | 1930 | 1954 | 24.0 | 384000 | a456004300a5796094b459c1d29f613c3f9009cf93e5a298b60215fe63422fd6 |
| M03_1958_1982 | 1958 | 1982 | 24.0 | 384000 | 96524ace8ff9f513d322e0f3bf4ca6078d44d58a75c67b20e22a725e098e8908 |
| M03_2020_2044 | 2020 | 2044 | 24.0 | 384000 | d61e57e677f6bb8a41df29b5308d766e4b4c81b578973898a5d67334bd3fd69e |
| M03_2048_2072 | 2048 | 2072 | 24.0 | 384000 | 804712731ee70f7c08d703bc18c3d2a0e6dd2e03e46d535f450ca3d8812a6db1 |
| M01_28_52 | 28 | 52 | 24.0 | 384000 | b02193b33e7c2c8790337cfe3e036110054d22141f6ffdaa0a6831df7775cd02 |
| M01_2738_2752 | 2738 | 2752 | 14.0 | 224000 | ba33dc26e192657a09675fbb7ee626d409432b4d0dfe6266d3f3943895a629b2 |
| M04_3380_3404 | 3380 | 3404 | 24.0 | 384000 | e8fa18dbe2722a061f2bf7308a4515e5c0c4777a58960a82d1b173cd99b04b29 |
| M04_3798_3818 | 3798 | 3818 | 20.0 | 320000 | e0016dfeeac2745afa52ad9665feff838f5a518175078d69557a0fd5493b62d8 |

## ASR: limited locator corroboration

Model: [Systran/faster-whisper-small](https://huggingface.co/Systran/faster-whisper-small), exact revision `536b0662742c02347bc0e980a01041f333bce120`. CPU int8, six threads, one worker. The language was explicitly set to Japanese; these results are not an independent language-identification test. Temperature is 0 with beam size 5; previous-text conditioning and VAD are disabled. Word timestamps were requested but remain model estimates. No word error rate, speaker-attribution accuracy or emotion accuracy is claimed.

The following alignment findings were checked against the already retrieved locked scripts and inspected source frames. They concern passage identity and lexical limits, not audible expression.

| Clip ID | Locked-text / viewed-content alignment and limitation |
| --- | --- |
| M03_509_534 | Dear022 raw lines182/191/198 and the beginning of202. ASR writes 暑い/薄まいて for 熱い/渦巻いて and truncates final words. The accumulation/refusal passage is recognizable; A1 remains the exact wording control. |
| M03_1930_1954 | Dear026 raw lines152/158/168/172/174. ASR garbles the clipped Producer address and renders 傲岸不遜 as 合番不損, 秦谷美鈴 as 肌やミスズ, and 迷走 as 瞑想. The apology passage is identifiable; these errors must not enter canonical quotations. |
| M03_1958_1982 | Dear026 raw lines180/186/189 and the start of194. ASR 倒しましょう is wrong for どうしましょう, and the request for kind words ends mid-sentence at the clip edge. Continuing-pain wording is an alignment aid, not an acoustic pain measurement. |
| M03_2020_2044 | Dear026 raw lines265/272. ASR 迷想 is wrong for 迷走; punctuation and laughter are not exact. The stop-hurrying/fulfill-slowly passage is recognizable, without establishing how soothing or calm the delivery sounds. |
| M03_2048_2072 | Dear026 raw lines279/283/294/302. ASR clips ライバル and writes 岸中 for 眼中, 発星 for 初星, and くっぷく for 屈服. These are passage candidates only; locked A1 controls the rival/star/high-place-yawn/competition wording. |
| M01_28_52 | Dear001 raw lines59/68/71/81/88/92 identify the greeting and refusal. ASR renders 秦谷美鈴 as 肌やミスズ and 答え instead of 応え. Locked A1 and captions control the actual name and wording; the forced-Japanese ASR run is not an independent language test. |
| M01_2738_2752 | Dear010 raw lines384/392/394 identify all three commitment/exclusivity sentences. ASR normalizes punctuation and orthography; it supplies a locator candidate, not proof of a particular intimate tone or cadence. |
| M04_3380_3404 | Dear036 raw lines1322/1330/1338/1347/1364 and the start of1404. ASR turns なれたんでしょうか into 誰だでしょうか and 祝勝会 into 祝祝会, lacks speaker labels, and cuts the final sentence. Do not assign every segment to Misuzu or infer heard crying from this output. |
| M04_3798_3818 | Dear037 raw lines434/436 only. ASR entirely omits the shared-yawn caption at raw441, visible in inspected frames3812–3815s; it therefore neither confirms nor refutes a yawn sound. Raw442 specifies one Misuzu voice event, which is not proof of two audible voices. |

### ASR candidate — M03_509_534

Generated UTC: `2026-09-10T06:34:57.471840+00:00`. Working-result SHA-256: `d1842f84dd4234a3698ab3f2f08a4457adc7d1cbaa325ab918b3f1c07ed382ea`. These are uncorrected machine candidates, retained so mistakes remain inspectable. Source times below add the clip start to the model-estimated segment boundaries; their decimal display is not timing accuracy.

| Estimated source start s | Estimated source end s | Uncorrected ASR candidate | Average log probability | No-speech probability |
| --- | --- | --- | --- | --- |
| 509 | 513.4 | ドロドロとした暑いものが 胸の中で薄まいて | -0.249625599155 | 0.114339612424 |
| 514.38 | 517.08 | じわりと溜まっていくような | -0.249625599155 | 0.114339612424 |
| 520.92 | 522.52 | 発散だなんて | -0.249625599155 | 0.114339612424 |
| 524.14 | 527.7 | そんなことをしたら 減ってしまうでしょ | -0.249625599155 | 0.114339612424 |
| 528.44 | 532.4 | このドロドロは 大切なものなんです | -0.249625599155 | 0.114339612424 |
| 533.12 | 533.94 | 私のの | -0.249625599155 | 0.114339612424 |

### ASR candidate — M03_1930_1954

Generated UTC: `2026-09-10T06:35:08.148284+00:00`. Working-result SHA-256: `f63f1a1939df95fea767b738db536f96137d75311eeebc6b918cb5c2fdc9d02c`. These are uncorrected machine candidates, retained so mistakes remain inspectable. Source times below add the clip start to the model-estimated segment boundaries; their decimal display is not timing accuracy.

| Estimated source start s | Estimated source end s | Uncorrected ASR candidate | Average log probability | No-speech probability |
| --- | --- | --- | --- | --- |
| 1930 | 1936.72 | よさ、ごめんなさい。 約束、守れませんでした。 | -0.158620794084 | 0.542563199997 |
| 1940.3 | 1953.84 | 意外ですか、合番不損な肌やミスズが、プロデューサーとの約束を破ったくらいで、焦燥のあまり瞑想するなんて。ありえないと。 | -0.41672380063 | 0.370277017355 |

### ASR candidate — M03_1958_1982

Generated UTC: `2026-09-10T06:35:11.404212+00:00`. Working-result SHA-256: `5cdef3cc6dc87dd37ea3511c0e515bfa1a63f91e84b3c98aebb91935568eac7d`. These are uncorrected machine candidates, retained so mistakes remain inspectable. Source times below add the clip start to the model-estimated segment boundaries; their decimal display is not timing accuracy.

| Estimated source start s | Estimated source end s | Uncorrected ASR candidate | Average log probability | No-speech probability |
| --- | --- | --- | --- | --- |
| 1958 | 1969.9 | なかったんです。あなたが思っているよりも、ずっと痛かった。今も痛いまま。 | -0.346226390937 | 0.400188714266 |
| 1971.66 | 1981.98 | ああ、倒しましょう。私、あなたから優しい。 | -0.346226390937 | 0.400188714266 |

### ASR candidate — M03_2020_2044

Generated UTC: `2026-09-10T06:35:14.912619+00:00`. Working-result SHA-256: `647b93d048f1656fc22d27279315df17e80155517a7848e78eb01690c2707ab7`. These are uncorrected machine candidates, retained so mistakes remain inspectable. Source times below add the clip start to the model-estimated segment boundaries; their decimal display is not timing accuracy.

| Estimated source start s | Estimated source end s | Uncorrected ASR candidate | Average log probability | No-speech probability |
| --- | --- | --- | --- | --- |
| 2020.96 | 2028.74 | そうでしたね、お互い様、私たちは似たもの同士のようです。 | -0.31376932164 | 0.194269537926 |
| 2029.36 | 2031.9 | では、やめますね。 | -0.31376932164 | 0.194269537926 |
| 2033.42 | 2040.6 | 焦るのも、迷想も、約束はゆっくりと果たします。 | -0.31376932164 | 0.194269537926 |

### ASR candidate — M03_2048_2072

Generated UTC: `2026-09-10T06:35:18.954090+00:00`. Working-result SHA-256: `cd946b1778a3c894bcd314de91886ae6a1d3132dce04af1c506a6cbdc699ffcf`. These are uncorrected machine candidates, retained so mistakes remain inspectable. Source times below add the clip start to the model-estimated segment boundaries; their decimal display is not timing accuracy.

| Estimated source start s | Estimated source end s | Uncorrected ASR candidate | Average log probability | No-speech probability |
| --- | --- | --- | --- | --- |
| 2048 | 2054.92 | アイバロは、あくまで月村手まりただ一人、他のアイドルは岸中にありませんが、 | -0.26324750036 | 0.431437164545 |
| 2056.5 | 2067.04 | あなたに星を捧げるために、高いところであくびをするために、すべての発星アイドルをくっぷくさせましょう。 | -0.26324750036 | 0.431437164545 |

### ASR candidate — M01_28_52

Generated UTC: `2026-09-10T06:35:35.108628+00:00`. Working-result SHA-256: `635d354b3e854ea1a0703469c4317e6f9a1f76dd870f401ba8651138ca2ae785`. These are uncorrected machine candidates, retained so mistakes remain inspectable. Source times below add the clip start to the model-estimated segment boundaries; their decimal display is not timing accuracy.

| Estimated source start s | Estimated source end s | Uncorrected ASR candidate | Average log probability | No-speech probability |
| --- | --- | --- | --- | --- |
| 28 | 29.48 | お待たせしたみたいですね | -0.392316155361 | 0.022736242041 |
| 30.14 | 31.26 | はじめまして | -0.392316155361 | 0.022736242041 |
| 32.08 | 34 | 肌やミスズと申します | -0.392316155361 | 0.022736242041 |
| 34.6 | 37.2 | 何かご用でしょうか | -0.392316155361 | 0.022736242041 |
| 40.42 | 40.84 | まあ | -0.392316155361 | 0.022736242041 |
| 41.74 | 43.56 | お誘いありがとうございます | -0.392316155361 | 0.022736242041 |
| 46.76 | 47.94 | でも私では | -0.392316155361 | 0.022736242041 |
| 48.72 | 51.6 | あなたの期待に答えられないと思いますよ | -0.392316155361 | 0.022736242041 |

### ASR candidate — M01_2738_2752

Generated UTC: `2026-09-10T06:35:38.573656+00:00`. Working-result SHA-256: `c48d7856e3d208def4f573409d2b541bfa478ee7d91c3a95eec19f6e1108453e`. These are uncorrected machine candidates, retained so mistakes remain inspectable. Source times below add the clip start to the model-estimated segment boundaries; their decimal display is not timing accuracy.

| Estimated source start s | Estimated source end s | Uncorrected ASR candidate | Average log probability | No-speech probability |
| --- | --- | --- | --- | --- |
| 2738.7 | 2751.12 | あなたを選んで、本当に良かった。どこまでも一緒に歩いていきましょうね。私だけのプロデューサー。 | -0.212629364803 | 0.120205014944 |

### ASR candidate — M04_3380_3404

Generated UTC: `2026-09-10T06:35:43.506013+00:00`. Working-result SHA-256: `e30603d2c916405cbfcf6526254efd6f9f54bf817638d8c71ca679de907423cf`. These are uncorrected machine candidates, retained so mistakes remain inspectable. Source times below add the clip start to the model-estimated segment boundaries; their decimal display is not timing accuracy.

| Estimated source start s | Estimated source end s | Uncorrected ASR candidate | Average log probability | No-speech probability |
| --- | --- | --- | --- | --- |
| 3380 | 3385.78 | トップアイドル、ふ、誰だでしょうか | -0.48986386803 | 0.101638585329 |
| 3386.48 | 3388.7 | 私が決めていいの? | -0.48986386803 | 0.101638585329 |
| 3389.72 | 3392.54 | ふ、ふ、ダメ | -0.48986386803 | 0.101638585329 |
| 3394.32 | 3395.64 | でしょ? | -0.48986386803 | 0.101638585329 |
| 3400.98 | 3403.98 | 涙、祝祝会までに出しき | -0.48986386803 | 0.101638585329 |

### ASR candidate — M04_3798_3818

Generated UTC: `2026-09-10T06:35:47.645625+00:00`. Working-result SHA-256: `48f904bd7ca7f5126a4c0e22d729e7639749cc18c8fc78b3047ba906e3bafc5b`. These are uncorrected machine candidates, retained so mistakes remain inspectable. Source times below add the clip start to the model-estimated segment boundaries; their decimal display is not timing accuracy.

| Estimated source start s | Estimated source end s | Uncorrected ASR candidate | Average log probability | No-speech probability |
| --- | --- | --- | --- | --- |
| 3798 | 3811.24 | まあ、実は、私もなんです。約束を、果たしましょうか。 | -0.718980642882 | 0.413769006729 |

## Freeform model trials: rejected as claim evidence

These were neutral prompts without character identities, A1 text, visible frames, or story context. Both models were run locally with NF4 double quantization, float16 compute, CUDA device 0, SDPA attention and deterministic generation (sampling disabled, seed 0). This evaluation concerns these local model/runtime/quantization runs; it does not establish a general capability limit of either model.

- [Qwen2-Audio-7B-Instruct](https://huggingface.co/Qwen/Qwen2-Audio-7B-Instruct), revision `0a095220c30b7b31434169c3086508ef3ea5bf0a`, maximum 180 new text tokens. An initial trial used the stale processor argument `audios=`: the installed processor did not ingest audio, so those text-only outputs are invalid and excluded. The corrected trial used `audio=[waveform]` and asserted that nonempty `input_features` were present. Only that corrected trial is recorded below.
- [Qwen2.5-Omni-3B](https://huggingface.co/Qwen/Qwen2.5-Omni-3B), revision `f75b40e3da2003cdd6e1829b1f420ca70797c34e`, audio output disabled, `return_audio=False`, `thinker_max_new_tokens=180`, `thinker_do_sample=False`. The pinned repository speaker dictionary was fetched to satisfy the loader even though speech generation was disabled. Audio features were asserted present.

Exact prompt:

> Describe the audible content of this short clip. Separate speech or singing, vocal pacing and changes in force or pitch, background music, and salient non-speech sounds. Do not infer character identities, story events, motives, or speaker personality. Do not assume the soundtrack is isolated voice. State uncertainty. Keep the description under 120 words.

The corrected Qwen2-Audio run described M03 1958–1982s as English singing with no speech, conflicting with the recognizable Japanese continuing-pain dialogue in the ASR and locked text/visible passage controls. The Omni run repeatedly stated that M03 509–534s was non-English speech instead of providing the requested bounded vocal description, and supplied unsupported key/tempo claims at M03 2048–2072s. It also failed speech/song distinctions in the companion Hiro dialogue trial. Its apparently plausible Misuzu affect descriptions therefore lack validation and are not adopted. These failures prevent reliable use of either run for pacing, breath, affect, instrumental identity, exact silence, or speech/song discrimination. Apparently agreeable descriptions elsewhere in the batch are not selectively adopted.

The raw responses below are rejected trial outputs, not descriptions asserted by this package. Their only function is to make the rejection inspectable. Omni feature hashes use the float32 representation of the post-cast feature tensor; the corrected Qwen2-Audio run saved input shapes but did not save a feature digest. Input shape is a processing check, not a content-validity score.


### Rejected trial — M03_509_534

**Qwen2-Audio-7B-Instruct: rejected.** Working result SHA-256 `2730e1558dcb6eabebd22beb48a729bacfe077762b691b8f68bc6de6c90676fa`; feature SHA-256 `not recorded in this trial`; input feature shape `[1, 128, 3000]`.

> The audio contains a background track with a slow tempo featuring a stringed instrument playing a monotone note, which then transitions into a fast melody. A female voice speaks in a flat tone with no discernible emotion over the instrumental backdrop. The speech consists of the phrase 'ドロドロとした熱いものが胸の中で薄まいて' in Japanese language.

**Qwen2.5-Omni-3B: rejected.** Working result SHA-256 `4396272e0c89f4872d23c0fe7553ef28eef8356ddd1fc1d07c992b8110b6e041`; feature SHA-256 `15a99353bb8c2eccff1f18b71d7ba00eac1aad1090d856fff9facef75e5a8bdb`; input feature shape `[1, 128, 30000]`.

> The audio contains a woman speaking in Japanese, with a background of music. The speech is in a language other than English, and the speaker is likely female. The speech is in a language other than English, and the speaker is likely female. The speech is in a language other than English, and the speaker is likely female. The speech is in a language other than English, and the speaker is likely female. The speech is in a language other than English, and the speaker is likely female. The speech is in a language other than English, and the speaker is likely female. The speech is in a language other than English, and the speaker is likely female. The speech is in a language other than English, and the speaker is likely female. The speech is in a language other than English, and the speaker is likely female. The speech is in a language other than English, and the


### Rejected trial — M03_1930_1954

**Qwen2-Audio-7B-Instruct: rejected.** Working result SHA-256 `068a7f2dcd13a2232812105da06d86e4b2a3bed254d9ee791ecda287a4225264`; feature SHA-256 `not recorded in this trial`; input feature shape `[1, 128, 3000]`.

> The audio contains a female voice speaking in Japanese with a sad mood. The speech consists of words like 'ごめんなさい' and '約束'. There's also a background song which starts at approximately 3.60 seconds and includes elements of pop, rock, and electronic. The song has a sad mood as well and features instruments such as drums, synthesizer, piano, and violin. Additionally, there are some generic impact sounds heard around 9.50 to 9.65 seconds.

**Qwen2.5-Omni-3B: rejected.** Working result SHA-256 `313010de3b73db2e99f2161c16ae157d852f7875ff8b3bd4afffc413538cf387`; feature SHA-256 `f9b93da02a617b6fa5a9ec2c7fd5b0b5cd066348c9437477e42b93f6b016d3c9`; input feature shape `[1, 128, 30000]`.

> The audio features a woman speaking in Japanese, with a sad mood. The speech is accompanied by background music, which is instrumental and has a slow tempo. The woman's speech is in a language other than English, and the content is not specified. The audio is a recording of a live performance, and the recording quality is good. The audio is a mix of speech and music, with no other sounds or effects.


### Rejected trial — M03_1958_1982

**Qwen2-Audio-7B-Instruct: rejected.** Working result SHA-256 `9ea1cfbd4f205750224de03b11717b2f83a3b93d270bd62bef3a045fad006569`; feature SHA-256 `not recorded in this trial`; input feature shape `[1, 128, 3000]`.

> The audio contains a female singing in English with a sad mood. The song's structure includes a soft introduction with vocals, piano, and guitar, followed by a more intense section with drums and bass. There's no speech detected. The music genre seems to be pop or alternative with elements of electronic pop.

**Qwen2.5-Omni-3B: rejected.** Working result SHA-256 `74f5ca486475e323cdadf26bff4c9eb43df00b23491b95670fdfeebda4a33d7c`; feature SHA-256 `80a91ea5f44427ec3d3a96f025ea82a37412a89842b03234e7ffb366403cbb26`; input feature shape `[1, 128, 30000]`.

> The audio features a woman speaking in Japanese, with a sad mood. The speech is accompanied by background music, and there are no other notable sounds. The woman's speech is in a language other than English, and the content is not provided.


### Rejected trial — M03_2020_2044

**Qwen2-Audio-7B-Instruct: rejected.** Working result SHA-256 `744c81c3c91536ec93492d44b7dbb4fcd76b5c7b60e5515ba0a604c08debf995`; feature SHA-256 `not recorded in this trial`; input feature shape `[1, 128, 3000]`.

> The audio contains a female voice speaking in Japanese with a sad mood. The speech consists of words that translate to 'So it was, right? You and I are similar, aren't we? Well, okay, I'll stop now. It's no good rushing things, huh?' There is no discernible background music or sound effects.

**Qwen2.5-Omni-3B: rejected.** Working result SHA-256 `b6e3eef647cf3c3591606ecb829010848a463497c3724e50e17a65cf237f34a5`; feature SHA-256 `76edfc592ef2a64178126378ca26813ad2c99ead6b82fbf1da385f1fb954597c`; input feature shape `[1, 128, 30000]`.

> The audio contains a woman speaking in Japanese, with a calm and soothing tone. The speech is accompanied by background music, which is soft and melodic. The woman's speech is interspersed with breathing sounds, indicating a relaxed and calm demeanor. The overall atmosphere is serene and peaceful.


### Rejected trial — M03_2048_2072

**Qwen2-Audio-7B-Instruct: rejected.** Working result SHA-256 `99eafd0ba2f0760a64c6ee138dfbb7e68aeb3313f70efe5e1b46b66426fe9bdb`; feature SHA-256 `not recorded in this trial`; input feature shape `[1, 128, 3000]`.

> The audio contains a female voice speaking in Japanese with a medium pace and a sad mood. There's no discernible background music or sound effects. The speech consists of words like '月村手まり' and '初音アイドル'.

**Qwen2.5-Omni-3B: rejected.** Working result SHA-256 `068fd1e9fe9fc8dce3018c13cff264063cbf3d6304eb29d0364e182b52c0f0a2`; feature SHA-256 `7772a6795458b81f446ceb18e722451947fac9d80a6a1300f41d4d8070f19206`; input feature shape `[1, 128, 30000]`.

> The audio contains a speech segment in Japanese, with a female voice speaking in a neutral tone. The speech is accompanied by background music, which is instrumental and has a tempo of 160.0 bpm, with a 4/4 time signature and a key of B major. The speech is in the language Japanese and has a speech synthesizer. The speaker's mood is neutral.

## Current audio runtime and reproducible ASR procedure

| Component | Observed version |
| --- | --- |
| python | 3.12.4 |
| platform | Windows-11-10.0.26200-SP0 |
| faster-whisper | 1.2.1 |
| ctranslate2 | 4.8.2 |
| huggingface-hub | 0.36.2 |
| numpy | 2.1.2 |
| torch | 2.10.0+cu128 |
| torchaudio | 2.10.0+cu128 |
| torchvision | 0.25.0+cu128 |
| transformers | 4.57.6 |
| accelerate | 1.15.0 |
| bitsandbytes | 0.50.2 |
| librosa | 1.0.0 |
| soundfile | 0.14.0 |
| FFmpeg | ffmpeg version 8.1.1-essentials_build-www.gyan.dev Copyright (c) 2000-2026 the FFmpeg developers |

The ASR procedure itself requires Python, FFmpeg, NumPy, huggingface-hub and faster-whisper (including its CTranslate2 dependency); the Torch/Transformers GPU stack was used for the rejected freeform trials. The scientific-measurement runtime is documented separately in [current measurements](EXECUTION_MEASUREMENTS.md).

All ASR decoding parameters:

```json
{
  "language": "ja",
  "task": "transcribe",
  "beam_size": 5,
  "temperature": 0,
  "condition_on_previous_text": false,
  "word_timestamps": true,
  "vad_filter": false,
  "no_speech_threshold": 0.6,
  "compression_ratio_threshold": 2.4,
  "log_prob_threshold": -1.0
}
```

For reproduction, save the next fenced JSON as `clip_plan.json`, replacing only each `path` with the actual input path whose SHA-256 matches the table. Save the Python block as `asr_review.py`. These are working files created from Markdown; this ZIP deliberately contains neither scripts nor JSON as separate artifacts. The code downloads only the pinned model revision, hashes each source before accepting a cache, checks duration limits, binds task/parameters/runtime to the cache, and writes labeled candidate results. It supplies no interpretation.

```powershell
python -m pip install faster-whisper==1.2.1 ctranslate2==4.8.2 numpy==2.1.2 huggingface-hub==0.36.2
python asr_review.py clip_plan.json --work-dir "asr-working"
```

```json
[
  {
    "clip_id": "M03_509_534",
    "alias": "M03",
    "path": "<actual local path for M03>",
    "source_sha256": "5d78050758fecdf8b961926ee2f1dbdaa7bea9894983d378fff40585a5125763",
    "start_s": 509,
    "end_s": 534
  },
  {
    "clip_id": "M03_1930_1954",
    "alias": "M03",
    "path": "<actual local path for M03>",
    "source_sha256": "5d78050758fecdf8b961926ee2f1dbdaa7bea9894983d378fff40585a5125763",
    "start_s": 1930,
    "end_s": 1954
  },
  {
    "clip_id": "M03_1958_1982",
    "alias": "M03",
    "path": "<actual local path for M03>",
    "source_sha256": "5d78050758fecdf8b961926ee2f1dbdaa7bea9894983d378fff40585a5125763",
    "start_s": 1958,
    "end_s": 1982
  },
  {
    "clip_id": "M03_2020_2044",
    "alias": "M03",
    "path": "<actual local path for M03>",
    "source_sha256": "5d78050758fecdf8b961926ee2f1dbdaa7bea9894983d378fff40585a5125763",
    "start_s": 2020,
    "end_s": 2044
  },
  {
    "clip_id": "M03_2048_2072",
    "alias": "M03",
    "path": "<actual local path for M03>",
    "source_sha256": "5d78050758fecdf8b961926ee2f1dbdaa7bea9894983d378fff40585a5125763",
    "start_s": 2048,
    "end_s": 2072
  },
  {
    "clip_id": "M01_28_52",
    "alias": "M01",
    "path": "<actual local path for M01>",
    "source_sha256": "f7b7c8e6dbdb7199a6ef99429bdf4380d5f7dae9d4e194338d5b398f2ee3f8be",
    "start_s": 28,
    "end_s": 52
  },
  {
    "clip_id": "M01_2738_2752",
    "alias": "M01",
    "path": "<actual local path for M01>",
    "source_sha256": "f7b7c8e6dbdb7199a6ef99429bdf4380d5f7dae9d4e194338d5b398f2ee3f8be",
    "start_s": 2738,
    "end_s": 2752
  },
  {
    "clip_id": "M04_3380_3404",
    "alias": "M04",
    "path": "<actual local path for M04>",
    "source_sha256": "38500c9908eee6a44ab630fd6bf317ca1d37e3f4282995a2fb3d45ee2621638a",
    "start_s": 3380,
    "end_s": 3404
  },
  {
    "clip_id": "M04_3798_3818",
    "alias": "M04",
    "path": "<actual local path for M04>",
    "source_sha256": "38500c9908eee6a44ab630fd6bf317ca1d37e3f4282995a2fb3d45ee2621638a",
    "start_s": 3798,
    "end_s": 3818
  }
]
```

Executed ASR script SHA-256: `0c695c1fb98ffea5aa6760586a18d1ec645b496a58074c6817951f1ba7d424fd`. The block below is the exact script used for the final 18-clip run across both characters. Each character plan includes only its own nine clips.

```python
"""Non-authoritative Japanese ASR for locating audio; never replaces locked A1 text."""
import pathlib,json,hashlib,subprocess,datetime,sys,os,time,argparse,importlib.metadata
from huggingface_hub import snapshot_download
from faster_whisper import WhisperModel
import numpy as np
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('plan',help='JSON clip plan copied from the Markdown reproduction record')
parser.add_argument('--work-dir',default='asr-working',help='Local directory for pinned model and working results')
args=parser.parse_args()
WORK=pathlib.Path(args.work_dir).resolve();WORK.mkdir(parents=True,exist_ok=True)
name='Systran/faster-whisper-small'
revision='536b0662742c02347bc0e980a01041f333bce120'
modeldir=snapshot_download(name,revision=revision,local_dir=str(WORK/'models/faster-whisper-small'),allow_patterns=['*.json','*.bin','*.txt'],max_workers=3)
model=WhisperModel(modeldir,device='cpu',compute_type='int8',cpu_threads=6,num_workers=1)
tasks=json.loads(pathlib.Path(args.plan).read_text(encoding='utf-8'))
outdir=WORK/'asr_results_v2';outdir.mkdir(exist_ok=True)
params=dict(language='ja',task='transcribe',beam_size=5,temperature=0,condition_on_previous_text=False,word_timestamps=True,vad_filter=False,no_speech_threshold=0.6,compression_ratio_threshold=2.4,log_prob_threshold=-1.0)
versions={n:importlib.metadata.version(n) for n in ['faster-whisper','ctranslate2','numpy','huggingface-hub']}
versions['python']=sys.version
versions['ffmpeg']=subprocess.run(['ffmpeg','-version'],capture_output=True,text=True,check=True).stdout.splitlines()[0]
verified={}
for task in tasks:
    source=pathlib.Path(task['path']).resolve(strict=True)
    if str(source) not in verified:
        h=hashlib.sha256()
        with source.open('rb') as f:
            for block in iter(lambda:f.read(8*1024*1024),b''):h.update(block)
        verified[str(source)]=h.hexdigest()
    if verified[str(source)]!=task['source_sha256']:raise ValueError('Source SHA-256 mismatch: '+str(source))
    if not 0 < task['end_s']-task['start_s'] <= 25:raise ValueError('Invalid bounded clip duration')
    cachekey=hashlib.sha256(json.dumps(dict(task=task,revision=revision,params=params,versions=versions,method='source_hash_bound_asr_v2'),sort_keys=True).encode()).hexdigest()
    target=outdir/(task['clip_id']+'.json')
    if target.exists():
        prior=json.loads(target.read_text(encoding='utf-8'))
        if prior.get('cachekey')==cachekey:continue
    cmd=['ffmpeg','-v','error','-threads','1','-i',task['path'],'-map','0:a:0','-vn','-af',f"atrim=start={task['start_s']}:end={task['end_s']},asetpts=PTS-STARTPTS",'-ac','1','-ar','16000','-f','f32le','-']
    p=subprocess.run(cmd,capture_output=True,check=True);y=np.frombuffer(p.stdout,dtype='<f4').copy()
    segments,info=model.transcribe(y,**params)
    rows=[dict(start_s=s.start,end_s=s.end,text=s.text,avg_logprob=s.avg_logprob,no_speech_prob=s.no_speech_prob,words=[dict(start_s=w.start,end_s=w.end,text=w.word,probability=w.probability) for w in s.words or []]) for s in segments]
    out=dict(task=task,source_sha256=verified[str(source)],clip_pcm_sha256=hashlib.sha256(p.stdout).hexdigest(),sample_rate=16000,samples=len(y),model=name,model_revision=revision,device='cpu',compute_type='int8',cpu_threads=6,parameters=params,versions=versions,ffmpeg_command=cmd,cachekey=cachekey,segments=rows,generated_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),status='ASR CANDIDATE; compare to on-screen captions and locked A1; not direct listening')
    target.write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf-8')
    print(task['clip_id'],[r['text'] for r in rows],flush=True)
```

## Effect on completion status

Source accounting and reproducible numerical processing are unaffected by the rejection of freeform audio descriptions. The visual/textual claim review remains supported by its own locators and source controls. These trials provide no new independent evidence of breathiness, softness, strain, affective timing, singer-isolated properties, or a heard final yawn. The remaining auditory review is an analysis dependency, not a request for more media: all required source slots are locally available. Historical qualitative inspection records are preserved and are not declared nonexistent.
