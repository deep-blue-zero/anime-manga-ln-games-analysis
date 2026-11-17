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

# HIRO — current automated audio trials and ASR locator review

**Disposition: no freeform audio-model judgment is adopted as qualitative evidence.** Nine bounded clips were processed by a pinned Japanese ASR model as locator aids; five of those clips were also tested with two freeform audio-description models. This is machine-assisted processing, not direct listening by this reviewer. No current claim is upgraded to supported on the basis of these descriptions, and the direct-listening dependency remains explicit.

The host returned an explicit audio-input-unsupported response when a local test excerpt was supplied through its native audio channel. To pursue the authorized audiovisual work, a local audio/ASR environment was installed and tested. The results below record what those tools actually did; extraction, a populated transcript, or a fluent model answer is not treated as hearing the source.

Locked A1 scripts and directly viewed captions remain the wording and scene controls, as documented in [the character execution review](EXECUTION_20260910_REVIEW.md). Their source lock is `DreamGallery/Campus-adv-txts` commit `00d150a069a3ffa723a1ff264752ba242024caad`, revision 32. ASR errors, clipped words, omissions, and inferred segment/word times are not promoted into canonical dialogue. Producer lines visible on-screen can be unvoiced message events; absence from an ASR output is not evidence that a visible exchange did not occur.

## Scope, inputs and clip identity

All times use the source MP4 clock, with inclusive start/exclusive end extraction. The first audio stream is decoded through FFmpeg `atrim`, reset to zero, downmixed to mono and resampled to 16000 Hz float32. There is no normalization, denoising, source separation, speaker isolation or diarization. Clip hashes below cover the exact little-endian float32 bytes passed to the models; they are not hashes of a WAV header or encoded media file.

| Source alias | Recorded Drive ID | Actual input SHA-256 | Actual filename |
| --- | --- | --- | --- |
| H03 | 1EDx0YyXW11f6CNg2Too0fh-7jpaEVU9Q | 3b533ccfdfa1d4a284c660f8f3ab5f87c7ca18d52e5f6a4e758f7197493e6989 | 【学マス】篠澤広 親愛度コミュ21～27話まとめ【STEP3】-(720p60).mp4 |
| H04_ORIGINAL | 1Toi0yHcoq0jV0GMcA4JalcrlLMbnFxQO | 4dc80d8f2431fe8780faf59fa6b9f372f0fafcb599607ce9e04ead81bc4d4468 | 【学マス】 篠澤広 親愛度コミュ28～37話まとめ【H.I.F編】【STEP4】-(720p60).mp4 |
| H01 | 1UELlTgEu9lKMysQKjnLbt4MEUg9XWcbi | d0d161a97a05993a3cb85e33b6b6c0c3c9aa9dba10eb4a26bdfb12ae651d23e3 | 【学マス】篠澤広　親愛度１～１０話【アイドルコミュ】-(720p30).mp4 |
| H09 | 1bFRSUu8i-L7iU9OWTQa_9HJPEDmf08ul | 479d2926eca4eddb1157b49091054f9229eb48a253de9cdb0ac1658f2f667370 | 【ガラクタロード】篠澤広  楽曲コミュまとめ【学マス】-(720p60).mp4 |

Full local receipt routes, sizes, probes, shared relationships and source-identity qualifications are in [current source verification](EXECUTION_SOURCE_VERIFICATION.md). H04_ORIGINAL refers to the full original, never the shorter inherited measurement object.

| Clip ID | Source start s | Source end s | Duration s | PCM samples | PCM SHA-256 |
| --- | --- | --- | --- | --- | --- |
| H03_1875_1900 | 1875 | 1900 | 25.0 | 400000 | da798ef9445004983a11a9438ae45d454c2c5c1826252f4a7f37438736b64236 |
| H03_1982_2001 | 1982 | 2001 | 19.0 | 304000 | 4bd38302631be41b660f6b385e05fb76a518e3b95e5a78090814fa510becd98a |
| H04_ORIGINAL_140_163 | 140 | 163 | 23.0 | 368000 | 9b9cee8e3cd985b997819bfea49e01b595dba8d6a046f337120aa19526efbdd9 |
| H04_ORIGINAL_3165_3189 | 3165 | 3189 | 24.0 | 384000 | 5bb14c488c46a7ee292be1dea6590392f7250858c8f4b28e5a0da9ce1a1c72ef |
| H04_ORIGINAL_3248_3267 | 3248 | 3267 | 19.0 | 304000 | 360efab6ac6ab1344803c2c06959473a60e9f9f753810142f123ddb1b91f0c13 |
| H01_2140_2164 | 2140 | 2164 | 24.0 | 384000 | b608b785f86ce2a32d6c51e5d8f4c07c5c673cd0691d07f79af250c73650df0b |
| H01_2175_2198 | 2175 | 2198 | 23.0 | 368000 | 746f17eb66d4b22a7f814bb78ba8670c5f431d7804a4b1856eb74ef187758ae4 |
| H09_417_440 | 417 | 440 | 23.0 | 368000 | dba928cbcfa851b057563f39fe710575aebb6636c47f70f22989eb8039f6d26a |
| H09_480_505 | 480 | 505 | 25.0 | 400000 | f3a20eb51d81cc87568babf601b0556c164b5598b5272f3184b6449aaac3742c |

## ASR: limited locator corroboration

Model: [Systran/faster-whisper-small](https://huggingface.co/Systran/faster-whisper-small), exact revision `536b0662742c02347bc0e980a01041f333bce120`. CPU int8, six threads, one worker. The language was explicitly set to Japanese; these results are not an independent language-identification test. Temperature is 0 with beam size 5; previous-text conditioning and VAD are disabled. Word timestamps were requested but remain model estimates. No word error rate, speaker-attribution accuracy or emotion accuracy is claimed.

The following alignment findings were checked against the already retrieved locked scripts and inspected source frames. They concern passage identity and lexical limits, not audible expression.

| Clip ID | Locked-text / viewed-content alignment and limitation |
| --- | --- |
| H03_1875_1900 | Dear026 lines93/103/108. ASR misrenders きちく as キッチク and される番 as されれば, and ends before the failure clause. Producer lines99/102 are displayed/interface-only. This corroborates passage location only. |
| H03_1982_2001 | Observed live-performance insert. The retrieved A1 dialogue script has no lyric transcript for this insert; ASR wording cannot be adopted as exact lyric evidence or a heard quality judgment. |
| H04_ORIGINAL_140_163 | Dear028 lines205/212/217/223/227. Names and 窮地 are rendered phonetically as シノサワヒロ/キューチ; A1 controls orthography. Producer lines204/211/226 (including the career wager) are displayed/interface-only and absent from ASR. |
| H04_ORIGINAL_3165_3189 | Dear037 lines186/196/202. ASR merges Hiro&#x27;s いいの…トップアイドルじゃなくて with the later よくはないんだ. Intervening displayed Producer lines194 (the one-time-only proposal) and201 are absent. The ASR segment span is not a continuous utterance or a valid cadence measurement. |
| H04_ORIGINAL_3248_3267 | Dear037 lines267/269/276/283/288. First line begins before the clip; よ is attached to the next ASR segment; この後に及んで is wrong for この期に及んで and 今更のこと differs from いまさらなこと. Final 約束した is clipped before the rest. Producer line282 is displayed/interface-only. |
| H01_2140_2164 | Observed live-performance insert at this source interval. Dear009 A1 does not transcribe its sung lyrics, so the lyric-like ASR strings remain unverified candidates; they do not establish exact lyrics or song identity. |
| H01_2175_2198 | Dear009 lines 142/149/157 match the passage; ASR omits the first え in えへへ. Producer assessments at lines145/152, displayed around2180/2190s, are interface-only and absent from ASR. Their omission is not narrative silence or evidence that the evaluation did not occur. |
| H09_417_440 | CIDOL018 part03 lines82/91/96/103. Initial ASR 初めて is wrong for clipped 苦しめて; オフ misrenders おっふ. The excess clause is recognizable, but the final って is clipped before 思ってた. Producer lines88/95 are displayed/interface-only. |
| H09_480_505 | CIDOL018 part03 lines149/154/160/164/180. おらやましく is wrong for 羨ましく. Dream/hobby wording is recognizable; final 楽しんでいこうね is missing at the clip end. Its full caption being visible at505s does not prove all speech has already occurred. Producer lines170/172/179 are displayed/interface-only. |

### ASR candidate — H03_1875_1900

Generated UTC: `2026-09-10T06:34:38.520764+00:00`. Working-result SHA-256: `f06a7a3102c0538abaa68a3c2997536f59af8ad29684fa09c2fc6f8299cff43c`. These are uncorrected machine candidates, retained so mistakes remain inspectable. Source times below add the clip start to the model-estimated segment boundaries; their decimal display is not timing accuracy.

| Estimated source start s | Estimated source end s | Uncorrected ASR candidate | Average log probability | No-speech probability |
| --- | --- | --- | --- | --- |
| 1875 | 1881.4 | ドエス、キッチク、私をイジメて楽しんでる | -0.575141167154 | 0.0810580551624 |
| 1893.44 | 1895.62 | 今日は、私が無茶ぶりをされれば | -0.575141167154 | 0.0810580551624 |
| 1896.42 | 1898.66 | ねえ、プロデューサー | -0.575141167154 | 0.0810580551624 |

### ASR candidate — H03_1982_2001

Generated UTC: `2026-09-10T06:34:41.923007+00:00`. Working-result SHA-256: `f32d595cded7b5ac3b76c642c27cd97ab1d86f8083fc99d8520a2cdf1910c7dc`. These are uncorrected machine candidates, retained so mistakes remain inspectable. Source times below add the clip start to the model-estimated segment boundaries; their decimal display is not timing accuracy.

| Estimated source start s | Estimated source end s | Uncorrected ASR candidate | Average log probability | No-speech probability |
| --- | --- | --- | --- | --- |
| 1983.16 | 1991.04 | Ah 気づけたね あの思いのままでいいほど | -0.90055300934 | 0.720972299576 |
| 1991.04 | 2000.32 | あんなにも大きなコーブ 話すはすれに行こう | -0.90055300934 | 0.720972299576 |

### ASR candidate — H04_ORIGINAL_140_163

Generated UTC: `2026-09-10T06:34:45.843870+00:00`. Working-result SHA-256: `6ccac13eafd7cb36693823ac31b56d6502434ab50f1d751d4d1329d708cb74d9`. These are uncorrected machine candidates, retained so mistakes remain inspectable. Source times below add the clip start to the model-estimated segment boundaries; their decimal display is not timing accuracy.

| Estimated source start s | Estimated source end s | Uncorrected ASR candidate | Average log probability | No-speech probability |
| --- | --- | --- | --- | --- |
| 140 | 143.96 | 私がプリマステラになれなかったら | -0.252655187622 | 0.0519936084747 |
| 148.76 | 149.56 | そう、なんだ | -0.252655187622 | 0.0519936084747 |
| 150.38 | 153.96 | シノサワヒロはキューチに強いアイドル | -0.252655187622 | 0.0519936084747 |
| 154.8 | 158.98 | あなたはそういった私を追い込もうとしてる | -0.252655187622 | 0.0519936084747 |
| 160.52 | 161.3 | そっか | -0.252655187622 | 0.0519936084747 |

### ASR candidate — H04_ORIGINAL_3165_3189

Generated UTC: `2026-09-10T06:34:49.631042+00:00`. Working-result SHA-256: `4731f96cfb8e7d8063787a96c2ae96d7e9d862499ab8dce411d51b2610615738`. These are uncorrected machine candidates, retained so mistakes remain inspectable. Source times below add the clip start to the model-estimated segment boundaries; their decimal display is not timing accuracy.

| Estimated source start s | Estimated source end s | Uncorrected ASR candidate | Average log probability | No-speech probability |
| --- | --- | --- | --- | --- |
| 3165.72 | 3170.1 | 明日の私は…違うよ | -0.403411790729 | 0.203245416284 |
| 3173.82 | 3183.2 | いいの?私が…トップアイドルじゃなくて…よくはないんだ | -0.403411790729 | 0.203245416284 |

### ASR candidate — H04_ORIGINAL_3248_3267

Generated UTC: `2026-09-10T06:34:53.806716+00:00`. Working-result SHA-256: `d5e3ace5009982742ba3fb6f5eb9a190295a32a6297765a6bbd830ac8108db77`. These are uncorrected machine candidates, retained so mistakes remain inspectable. Source times below add the clip start to the model-estimated segment boundaries; their decimal display is not timing accuracy.

| Estimated source start s | Estimated source end s | Uncorrected ASR candidate | Average log probability | No-speech probability |
| --- | --- | --- | --- | --- |
| 3248 | 3250.5 | 私の夢聞いて欲しい | -0.246885819513 | 0.193553760648 |
| 3250.5 | 3253.16 | トップアイドルになる | -0.246885819513 | 0.193553760648 |
| 3253.16 | 3256.38 | よ、今度こそちゃんと言えた | -0.246885819513 | 0.193553760648 |
| 3258.62 | 3264 | プロデューサーはこの後に及んで今更のことを言う | -0.246885819513 | 0.193553760648 |
| 3265.02 | 3265.88 | 約束した | -0.246885819513 | 0.193553760648 |

### ASR candidate — H01_2140_2164

Generated UTC: `2026-09-10T06:35:22.627185+00:00`. Working-result SHA-256: `6b367dcd39919033fffc19a581884693e1adf45d4f9cb97ed5769d5a0a2673dc`. These are uncorrected machine candidates, retained so mistakes remain inspectable. Source times below add the clip start to the model-estimated segment boundaries; their decimal display is not timing accuracy.

| Estimated source start s | Estimated source end s | Uncorrected ASR candidate | Average log probability | No-speech probability |
| --- | --- | --- | --- | --- |
| 2140 | 2146.26 | 夢の夢を考えたい 想いはきっと | -0.294627453767 | 0.834008932114 |
| 2147 | 2155.2 | 誰にも負けないわ 例え苦しくきらめ | -0.294627453767 | 0.834008932114 |
| 2155.2 | 2162.48 | そうでも負けられない 掴み取るのには | -0.294627453767 | 0.834008932114 |

### ASR candidate — H01_2175_2198

Generated UTC: `2026-09-10T06:35:26.066484+00:00`. Working-result SHA-256: `db4190f4239a202314f75c495648551af893d00bdee9ad6b0ff230219aefe3af`. These are uncorrected machine candidates, retained so mistakes remain inspectable. Source times below add the clip start to the model-estimated segment boundaries; their decimal display is not timing accuracy.

| Estimated source start s | Estimated source end s | Uncorrected ASR candidate | Average log probability | No-speech probability |
| --- | --- | --- | --- | --- |
| 2175 | 2177.3 | 私のライブ、どうだった? | -0.477301052809 | 0.0375430285931 |
| 2182 | 2184.04 | 私、褒められてる? | -0.477301052809 | 0.0375430285931 |
| 2191.06 | 2195.98 | へへ、こんなにプロデューサーが褒めてくれるの、初めて。 | -0.477301052809 | 0.0375430285931 |

### ASR candidate — H09_417_440

Generated UTC: `2026-09-10T06:35:29.382605+00:00`. Working-result SHA-256: `dd6a118f0dcd9d23314c6c4411937c02e441f4162d57d7ec0249c422ed9ea96d`. These are uncorrected machine candidates, retained so mistakes remain inspectable. Source times below add the clip start to the model-estimated segment boundaries; their decimal display is not timing accuracy.

| Estimated source start s | Estimated source end s | Uncorrected ASR candidate | Average log probability | No-speech probability |
| --- | --- | --- | --- | --- |
| 417 | 420.46 | 初めて、喜ばせるものばかり。 | -0.310124960584 | 0.626834213734 |
| 423.46 | 429.26 | たまに、オフ、これはやりすぎ、ってなるよ。 | -0.310124960584 | 0.626834213734 |
| 432.12 | 439.48 | プロデューサー、最初は私に付き合って、仕方なく無茶ぶりしてくれているのかな?って。 | -0.310124960584 | 0.626834213734 |

### ASR candidate — H09_480_505

Generated UTC: `2026-09-10T06:35:32.249813+00:00`. Working-result SHA-256: `b28dcf07baa82f6d373ab35b8a197cbe0d1d0fa907feace9d4b8f248f680f579`. These are uncorrected machine candidates, retained so mistakes remain inspectable. Source times below add the clip start to the model-estimated segment boundaries; their decimal display is not timing accuracy.

| Estimated source start s | Estimated source end s | Uncorrected ASR candidate | Average log probability | No-speech probability |
| --- | --- | --- | --- | --- |
| 480 | 482.22 | 私は夢がおらやましくなっていった | -0.368751819317 | 0.437989443541 |
| 482.22 | 484.18 | あなたがくれた夢は | -0.368751819317 | 0.437989443541 |
| 484.8 | 486.08 | 私の趣味を | -0.368751819317 | 0.437989443541 |
| 486.66 | 488.6 | もっと輝かせてくれた | -0.368751819317 | 0.437989443541 |
| 489.8 | 490.68 | よ、ありがとう | -0.368751819317 | 0.437989443541 |
| 499.04 | 501.72 | プロデューサー | -0.368751819317 | 0.437989443541 |
| 501.72 | 502.76 | 夢も | -0.368751819317 | 0.437989443541 |
| 503.44 | 504.24 | 趣味も | -0.368751819317 | 0.437989443541 |

## Freeform model trials: rejected as claim evidence

These were neutral prompts without character identities, A1 text, visible frames, or story context. Both models were run locally with NF4 double quantization, float16 compute, CUDA device 0, SDPA attention and deterministic generation (sampling disabled, seed 0). This evaluation concerns these local model/runtime/quantization runs; it does not establish a general capability limit of either model.

- [Qwen2-Audio-7B-Instruct](https://huggingface.co/Qwen/Qwen2-Audio-7B-Instruct), revision `0a095220c30b7b31434169c3086508ef3ea5bf0a`, maximum 180 new text tokens. An initial trial used the stale processor argument `audios=`: the installed processor did not ingest audio, so those text-only outputs are invalid and excluded. The corrected trial used `audio=[waveform]` and asserted that nonempty `input_features` were present. Only that corrected trial is recorded below.
- [Qwen2.5-Omni-3B](https://huggingface.co/Qwen/Qwen2.5-Omni-3B), revision `f75b40e3da2003cdd6e1829b1f420ca70797c34e`, audio output disabled, `return_audio=False`, `thinker_max_new_tokens=180`, `thinker_do_sample=False`. The pinned repository speaker dictionary was fetched to satisfy the loader even though speech generation was disabled. Audio features were asserted present.

Exact prompt:

> Describe the audible content of this short clip. Separate speech or singing, vocal pacing and changes in force or pitch, background music, and salient non-speech sounds. Do not infer character identities, story events, motives, or speaker personality. Do not assume the soundtrack is isolated voice. State uncertainty. Keep the description under 120 words.

The corrected Qwen2-Audio run invented a three-minute event in the 25-second H03 1875–1900s clip and identified the H04 140–163s passage as Mandarin despite the locked Japanese exchange and recognizable Japanese ASR wording. The Omni run partly recognized Japanese words but described the spoken H04 3165–3189 and3248–3267s dialogue as songs, supplied unsupported keys/tempi, and produced repetitive passages. These failures prevent reliable use of either run for pacing, breath, affect, instrumental identity, exact silence, or speech/song discrimination. Apparently agreeable descriptions elsewhere in the batch are not selectively adopted.

The raw responses below are rejected trial outputs, not descriptions asserted by this package. Their only function is to make the rejection inspectable. Omni feature hashes use the float32 representation of the post-cast feature tensor; the corrected Qwen2-Audio run saved input shapes but did not save a feature digest. Input shape is a processing check, not a content-validity score.


### Rejected trial — H03_1875_1900

**Qwen2-Audio-7B-Instruct: rejected.** Working result SHA-256 `2c0525fbdd58539fb28d8c15b9e3f90aa5c9581642240fda20781dc112c0afec`; feature SHA-256 `not recorded in this trial`; input feature shape `[1, 128, 3000]`.

> The audio contains a segment of singing accompanied by background music throughout. There's a noticeable shift in pitch around the 3-minute mark. Additionally, there are instances of respiratory sounds, specifically breathing, interspersed within the audio track. The speech content is sparse, mainly featuring the phrase '私は駄馬鹿にされれば' spoken by a female voice.

**Qwen2.5-Omni-3B: rejected.** Working result SHA-256 `01f0ef0b1130c61abe382170fa8b7d6dcc4443c5f21fafa34b95a53e0972ba9b`; feature SHA-256 `b782b83491913b2183a238e1d1d26a63ca48c68ed6017ad38c0199b02fc65854`; input feature shape `[1, 128, 30000]`.

> The audio contains a woman speaking in Japanese, with a speech synthesizer. The speech is in a language other than English, and the speaker is female. The speaker's mood is neutral. The audio type is music, and the style is electronic. The audio contains a synthesizer, and the synthesizer is playing a melody. The synthesizer is playing a melody in the key of C major, with a time signature of 4/4, and a tempo of 175.0 bpm. The synthesizer is playing a C major chord, and the chord progression is C major. The synthesizer is playing a C major chord, and the chord progression is C major. The synthesizer is playing a C major chord, and the chord progression is C major. The synthesizer is playing a C major chord, and the chord progression is C major. The synthesizer is playing a


### Rejected trial — H03_1982_2001

**Qwen2-Audio-7B-Instruct: rejected.** Working result SHA-256 `5de5b7cb4214ef641c2c628c028eaa9b00a66702d1459e1a40c0dbc8a5ba2b10`; feature SHA-256 `not recorded in this trial`; input feature shape `[1, 128, 3000]`.

> The audio contains a fast-paced, energetic instrumental piece with drums and bass that could be classified as either pop or electronic music, featuring synthesizers and electric guitar. A female voice sings in a high pitch with a sad mood over the instrumental track. There are no other voices or instruments present. The music has a time signature of 4/4 and a tempo of 109.09 bpm.

**Qwen2.5-Omni-3B: rejected.** Working result SHA-256 `3376dfe2b8b5dc765e1a4a3c16e1fb241053947bb311a0ccf0b6a738ca3a4103`; feature SHA-256 `ce8c9154d195fe7e1fa8da0cc14bce9895e208cd7c4cbb0d6ec1bdd1409838e0`; input feature shape `[1, 128, 30000]`.

> The audio contains a woman singing, with a background of music. The singing is in Japanese and the song is in a major key. The tempo is 103.0 bpm. The song is in 4/4 time signature.


### Rejected trial — H04_ORIGINAL_140_163

**Qwen2-Audio-7B-Instruct: rejected.** Working result SHA-256 `7f9efb7225fae0310287a0d4fd86845d0feeab67dc755ac5ea616caf569797b9`; feature SHA-256 `not recorded in this trial`; input feature shape `[1, 128, 3000]`.

> The audio contains a background track with a medium tempo electronic feel, featuring synthesizers, drums, bass, and keyboard. It has a slow build but lacks melody, creating a dark and suspenseful atmosphere suitable for a film score. A Mandarin-speaking male aged between 16-25 with a fearful mood says '我追逐你到那种强度' during the clip.

**Qwen2.5-Omni-3B: rejected.** Working result SHA-256 `9f5c3981818226a032195137975dc994b146b5ebb3a012191ff0a7370a7dd472`; feature SHA-256 `f5f550f7d1c17dd37330f3a4e8ca95d9066d20be731925fd3dc7b2016f4ea86f`; input feature shape `[1, 128, 30000]`.

> The audio contains a woman speaking in Japanese, with a background music track. The speech is in a language other than English, and the speaker is likely female. The audio is a recording of a conversation or monologue, with no other voices or sounds present. The speaker's tone is neutral, and the speech is clear and easy to understand. The background music is instrumental and has a tempo of 105.0 bpm. The song is in the key of C minor, with a 4/4 time signature. The song has a moderate tempo and a simple, catchy melody. The lyrics are in Japanese, and the speaker's voice is clear and easy to understand. The song is likely a pop or rock song, and the speaker is likely a female singer. The song is likely to be popular and well-known, and the speaker is likely to be a well-known singer. The


### Rejected trial — H04_ORIGINAL_3165_3189

**Qwen2-Audio-7B-Instruct: rejected.** Working result SHA-256 `867bf86642d6fb1969813fe3618c0f33108825144246dc878d60a0bdf1a5e23b`; feature SHA-256 `not recorded in this trial`; input feature shape `[1, 128, 3000]`.

> The audio contains a background track with a medium tempo instrumental piece featuring drums and bass that could be part of a soundtrack. There's also a female voice speaking in Japanese with a sad mood. The speech consists of words like '明日の私は' and 'シーガー4'.

**Qwen2.5-Omni-3B: rejected.** Working result SHA-256 `7453bfbf835389d2e9dd7b906ea0c91d7c9d305d4db0085648d4d3d62f4e8a1e`; feature SHA-256 `60b264b3e2bcd30932a64921eea923ae19eea26eb257166404eaec66a14f9868`; input feature shape `[1, 128, 30000]`.

> The audio contains a woman singing in Japanese, with a background music track. The song is in the key of E minor, with a 4/4 time signature and a tempo of 147.0 bpm. The lyrics are '明日の私は違うよ いいの 私がトップアイドルじゃなくて よくはないんだ'. The song features a vocal pacing that includes a crescendo from the beginning to the end.


### Rejected trial — H04_ORIGINAL_3248_3267

**Qwen2-Audio-7B-Instruct: rejected.** Working result SHA-256 `6baa81994d5fedf76cc4333037d69091162bd576ac4768ebb8bef9c930e5d801`; feature SHA-256 `not recorded in this trial`; input feature shape `[1, 128, 3000]`.

> The audio contains a female voice speaking in Japanese with a medium pace and a neutral mood. There's no discernible background music or sound effects. The speech consists of the phrase '私の夢聞いてほしい ポップアイドルになるよ' from the start to the 5th second.

**Qwen2.5-Omni-3B: rejected.** Working result SHA-256 `80fe91d833a1f3bf18a809e6ae7ae6e3bcf2e63461652ecdc45d25ea80f5eb83`; feature SHA-256 `eb6ed288145a12d26684a318596b99f5a1df79b1491650ea0a7ed1d005c7f75e`; input feature shape `[1, 128, 30000]`.

> The audio contains a woman singing in Japanese, with a background music track. The song is in the key of G minor, with a 4/4 time signature and a tempo of 175.0 bpm. The lyrics are '私の夢を聞いてほしい トップアイドルになるよ 今度こそちゃんと言えた プロデューサーはこの後に呼んでいます そろそろ言える約束した'.

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
    "clip_id": "H03_1875_1900",
    "alias": "H03",
    "path": "<actual local path for H03>",
    "source_sha256": "3b533ccfdfa1d4a284c660f8f3ab5f87c7ca18d52e5f6a4e758f7197493e6989",
    "start_s": 1875,
    "end_s": 1900
  },
  {
    "clip_id": "H03_1982_2001",
    "alias": "H03",
    "path": "<actual local path for H03>",
    "source_sha256": "3b533ccfdfa1d4a284c660f8f3ab5f87c7ca18d52e5f6a4e758f7197493e6989",
    "start_s": 1982,
    "end_s": 2001
  },
  {
    "clip_id": "H04_ORIGINAL_140_163",
    "alias": "H04_ORIGINAL",
    "path": "<actual local path for H04_ORIGINAL>",
    "source_sha256": "4dc80d8f2431fe8780faf59fa6b9f372f0fafcb599607ce9e04ead81bc4d4468",
    "start_s": 140,
    "end_s": 163
  },
  {
    "clip_id": "H04_ORIGINAL_3165_3189",
    "alias": "H04_ORIGINAL",
    "path": "<actual local path for H04_ORIGINAL>",
    "source_sha256": "4dc80d8f2431fe8780faf59fa6b9f372f0fafcb599607ce9e04ead81bc4d4468",
    "start_s": 3165,
    "end_s": 3189
  },
  {
    "clip_id": "H04_ORIGINAL_3248_3267",
    "alias": "H04_ORIGINAL",
    "path": "<actual local path for H04_ORIGINAL>",
    "source_sha256": "4dc80d8f2431fe8780faf59fa6b9f372f0fafcb599607ce9e04ead81bc4d4468",
    "start_s": 3248,
    "end_s": 3267
  },
  {
    "clip_id": "H01_2140_2164",
    "alias": "H01",
    "path": "<actual local path for H01>",
    "source_sha256": "d0d161a97a05993a3cb85e33b6b6c0c3c9aa9dba10eb4a26bdfb12ae651d23e3",
    "start_s": 2140,
    "end_s": 2164
  },
  {
    "clip_id": "H01_2175_2198",
    "alias": "H01",
    "path": "<actual local path for H01>",
    "source_sha256": "d0d161a97a05993a3cb85e33b6b6c0c3c9aa9dba10eb4a26bdfb12ae651d23e3",
    "start_s": 2175,
    "end_s": 2198
  },
  {
    "clip_id": "H09_417_440",
    "alias": "H09",
    "path": "<actual local path for H09>",
    "source_sha256": "479d2926eca4eddb1157b49091054f9229eb48a253de9cdb0ac1658f2f667370",
    "start_s": 417,
    "end_s": 440
  },
  {
    "clip_id": "H09_480_505",
    "alias": "H09",
    "path": "<actual local path for H09>",
    "source_sha256": "479d2926eca4eddb1157b49091054f9229eb48a253de9cdb0ac1658f2f667370",
    "start_s": 480,
    "end_s": 505
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
