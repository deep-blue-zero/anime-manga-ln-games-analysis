---
series: WUWA
character: Yinlin
artifact_type: factory_dual_channel_coercion_tablet_trust_profile
analytical_responsibility: "Separate performed captor speech, puppet-mediated tablet text, branch alternatives, device attribution, and render variants"
scope: YINLIN_PINNED_3_6_0_TEXT_AUDIO_PRE_AV
analysis_generation: YINLIN_PRE_AV_V0_1
status: draft_noncurrent
release_state: author_working_draft_pending_owner_review
source_commit: 353f2eaed119bc9f680eab92807d20ac75a79b40
source_generation: arikatsu-3.6.0-353f2eae-expanded-v0.3.0-ko
source_generation_frozen: true
source_freeze_metadata: conflicting_collection_and_embedded_lock_fields
text_authority: zh-Hans
localization_witnesses: [en, ja, ko]
supersedes: []
superseded_by: []
do_not_use_as_current_authority: true
---

# Yinlin — two channels inside the factory hostage performance

The source is `flow#/668/Actions!/3`, state `剧情_角色_吟霖线_副本临时_1_2`, linked in the pinned `PlotHandBook#/12` to character quest `114000018`. Its one `ShowTalk` contains 24 TalkItems and four stored sequences. Sequence 0 contains items T0–10. At its end, Rover can select *hand over the encrypted tablet* or *refuse*. Those alternatives lead to separate one-line Yinlin replies, T11 or T12, and then converge on T13–23. Thus the compliant “good” and the refusal-denying retort are not cumulative utterances in a single route. The remaining single-option prompts do not create another stored alternative here. This is a source graph, not a record of which option an individual player selected [YIN-E42, YIN-C40].

## The audible cover and the written counterchannel

Three technical speakers are visible. ID 370 names Yinlin and carries 14 selected direct-character occurrences. ID 811 names Dollmaker and carries his replies, including the claim that *he* placed listening and tracking equipment on Rover at T5 (`Character_YinLin_45_6`). ID 812 is named “Zapstring” and carries six parenthetical items, T14, T15, T18, T20, T21 and T23. At T15 (`_45_19`), the Chinese text itself describes using the puppet to type on the tablet to communicate without Dollmaker noticing. This gives the parentheticals a plausible character-authored, puppet-mediated semantic role, but the **display/technical speaker is not Yinlin**. An analyst must not count those six as additional direct Yinlin speech or borrow the four-dub audio of nearby ID-370 turns for them. The six items have raw `PlayVoice: true`, yet this selected ledger has no resolved plot-audio join or production-media objects for them. That discrepancy leaves actual audible realization open; it does not license the assertion that the messages were heard in a Yinlin voice, or that no runtime sound can exist [YIN-E42, YIN-C40].

Yinlin's public lines sustain the captivity performance. She describes Rover as dangerous and likely to flee, demands the encrypted tablet, says refusal is not allowed on one branch, and calls Rover a valuable experimental subject. Meanwhile the tablet text warns that Dollmaker may be listening, alleges a Fractsidus exchange of dangerous puppets for resources, admits a lack of proof, asks for cooperation, and promises to remove restraints while Rover continues to act bound. The private channel changes what the public words are *for*: an attempt to preserve cover while reaching Rover. It does not make the public threats physically harmless. Nor does `_45_30` prove the restraints were in fact removed; it is a future-tense promise within this action. Her later private account of using and shocking Rover still matters when assessing the tactic's cost [YIN-E12, E15, E19, E42; YIN-C04–C05, C40].

## Whose tracker, and when?

At `flow#/1006/7/9–16`, Yinlin separately admits planting a listening/location device on Rover when they first met because she did not trust them. In the factory action, T5 is **Dollmaker's** first-person claim that he installed listening and tracking equipment; T14's tablet message says Dollmaker installed listening equipment. These records cannot be collapsed into “Yinlin says she planted the factory device,” nor can the packet infer a count of one or two physical devices, prove either character's installation method, or silently convert Dollmaker's self-report into independent instrumentation evidence. Different speaker, audience, time and possible hardware identity must remain separate. The more constrained behavioral inference is that surveillance made covert communication salient to Yinlin and that her own earlier surveillance remains an unconsented act even when she later uses a counterchannel [YIN-E12, E42; YIN-C04, C40].

## A trust request that is not identical in every localization

The Chinese `_45_19` frames the tablet channel as a request that Rover *choose* to trust Yinlin while keeping Dollmaker unaware. Korean also explicitly asks for trust, conditionally on avoiding detection. English instead says she wants Rover to follow her instructions. Japanese explains that the puppet will write without his noticing, with no explicit trust appeal in this item. The operational act is common, but the interpersonal offer is not four-language invariant. To model this encounter as a consensual reset solely from the English instruction would erase the Chinese choice framing; to claim every dub says “trust me” would misquote English/Japanese [YIN-E42, YIN-C40].

Other intensifications also deserve local treatment. In the compliant branch `_45_15`, Chinese says Rover understands this is no time for bravado, while English uses the gendered “Good boy/girl”; that dominance coloring is a localization witness, not a universal line. Chinese/Korean `_45_10` say the factory is difficult to breach, while English says no rescue is coming soon. In `_45_17`, Chinese/Korean put a practical limit on troubling a valuable subject unless necessary; Japanese says a problem would embarrass Yinlin. None of these variations by itself reveals her actual internal intent behind cover. The branch choice and text language have to accompany any claim about how she positions Rover [YIN-E42].

## Audio identity and limits

The selected direct Yinlin voice index has 14 semantic occurrences in this action, not 20. That is the **union of two paths**: any one execution takes T11 or T12, so at most 13 of those direct Yinlin turns belong to one route through this action. The 14-line union yields 64 language/render associations and 58 distinct canonical PCM hashes, all with verified source WEM hashes and FLAC roundtrip PCM identity. `_45_5` and `_45_15` each have female/male-path associations in all four dubs; English has two distinct PCM hashes for each key, while JA/KO/ZH reuse the same PCM within their pair. Multiple render associations are not extra words spoken, and same-PCM aliases are not new takes. In this external-source route, numeric event/bank/media IDs are not established merely by the filename; keep unresolved fields null. There has been no human listening or runtime playback review to decide exact heard delivery, sex-route selection, whether the tablet items sound, or how forcefully the cover is performed [YIN-E27, E42; YIN-C22, C40].

The next useful observation is a synchronized runtime trace of both tablet branches: record displayed speaker, audio dispatch, restraint state, Dollmaker's presence and the return to the common sequence. Paired four-dub listening of `_45_5`, `_45_15`, `_45_16` and `_45_17` can test performance differences only after render variant and loudness are controlled. A hypothetical character response to an objection may acknowledge that she needed a hidden channel and still accept that its presence did not grant retroactive consent to tracking or shock. That is a testable extrapolation, not a line the source has already given her.
