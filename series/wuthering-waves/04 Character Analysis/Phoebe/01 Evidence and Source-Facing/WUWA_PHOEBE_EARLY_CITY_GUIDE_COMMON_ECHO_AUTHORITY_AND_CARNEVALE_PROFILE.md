---
series: WUWA
character: Phoebe
artifact_type: character_specialist_profile
analytical_responsibility: "Separate an early acolyte's civic teaching, public Echo access, reserved armed Echoes, and Carnival role-play from verified institutional fact or later reform"
scope: PHOEBE_PINNED_3_6_0_TEXT_AUDIO_PRE_AV
analysis_generation: PHOEBE_PRE_AV_V0_1
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

# Phoebe's first city lesson: a generous interface with reserved authority

## Exact scene and its routes

The pinned flow row `BinData/flowState/flowstate.json#/4203`, action 2, is an early conversation in which Phoebe answers newcomers' questions about Ragunna. All 26 `TalkItems` in this action use technical speaker 1475, are accepted as solo Phoebe occurrences in the local identity crosswalk, and are marked `PlayVoice: true`. Each has four resolved media associations in the selected corpus. This establishes **retrievable source-linked sound**, not a claim that this packet has listened to the deliveries. The four topic buttons and a finish button are at `flow#/4203/2/0`. Their explicit `JumpTalk` targets are TalkIDs 2 (Sentinel), 9 (Order), 14 (Carnevale), 22 (Common Echoes), and 26 (finish). The Sentinel, Order, Carnival and Echo explanations return to TalkID 1 by explicit jumps at TalkIDs 8, 13, 21 and 25. TalkID 26 finishes the conversation. This is a revisitable guide menu, **not** a single 26-line monologue or five consecutive questions Rover must ask.

There is a second choice at Carnival TalkID 17. Its two option records contain no explicit `JumpTalk` actions in this extracted row, so the exact runtime relationship between the replies and TalkIDs 18–21 needs direct traversal or engine-semantic corroboration. The texts after the options are present; this profile does not invent a proven option-to-reply mapping from their adjacency. The exact-state quest candidate is `QuestNodeData/questnodedata.json#/5943` (quest `114000027`, child `114000027_24`), whose condition names flow list `剧情_2_0_黎那汐塔主线_第一幕`, FlowId 11, StateId 1. That is a candidate join to this state, not proof of every runtime path.

## What the guide tells visitors, and who is speaking

Phoebe describes the Sentinel through virtues, unification, sea protection, lighthouse legend and a devotional passage (`Main_Linaxita_2_1_11_6–12`). Those are evidence of what an early acolyte **teaches** and sometimes explicitly calls legend or scripture. They are not an omniscient narrator's independent verification of the Sentinel's deeds or an assurance that Phoebe retains every institutional interpretation after Lorelei and Fenrico. Her easy recitation matters behaviorally: she knows how to make an unfamiliar city intelligible to guests, and faith is part of that public-service register. Later critical judgment grows from, rather than erases, this fluency [PHO-E10, E38; PHO-C05, C35].

The Order branch names the Order of the Deep as Ragunna's actual civic manager, including policy, diplomacy and disputes (`…_13`). She describes its members as earthly deputies of the Sentinel and managers of Common Echoes (`…_14`); armed La Guardia also belong to the Order (`…_15`). This is Phoebe's in-world account of her institution's authority. A generated early Phoebe can explain procedures confidently, refer a guest with a problem to the Order, and believe the office exists to protect lawful interests. It should not make her a neutral constitutional historian, the sole author of the Order's policies, or someone able to pardon the whole institution for later wrongdoing. Her later personal apology to Cetus at `5606/3/11–12` is a useful counterexample to conflating membership with plenary representation [PHO-E18, E38; PHO-C12, C35].

The lesson contains a precise qualification that a benevolent summary can lose. At `…_16` she says citizens may register with the Nexus for Common Echo use. At `…_31–32` she says **not all** Common Echoes are available for personal use: armed La Guardia are reserved to Order administration, and halo-marked Order Echoes respond to clergy rather than the general public in the Chinese anchor. Broad citizen access to a category and restricted control over its armed subset can coexist; the source does not prove that every Echo is equally available, that the guard monopoly is benign in every use, or that citizens lack meaningful access altogether. The institutional boundary is factual *as Phoebe presents it*, while its justice and later operational practice require separate evidence. This is an early civic state, not a later reform charter [PHO-E38; PHO-C35].

## Carnival equality is staged and socially meaningful, not a government audit

Phoebe's Carnival branch traces a reported festival origin through maritime isolation, shared tales, spring ritual, costume and a parade in which people put aside rank or prejudice (`…_18–21`). She then describes a free stage and masks that let participants take on other roles (`…_24–25`). The source supports her attraction to hospitality, performance and moments of freer social relation. It does **not** prove that institutional hierarchy disappears outside the stage, that every visitor participates, or that an actor's temporary license overturns the acolyte/Echo boundary. Indeed the same *menu* also describes reserved armed Echoes. That juxtaposition is an interpretive comparison across optional topics, not a transcript in which she necessarily states the two claims back-to-back.

This makes a sharper chronology for Phoebe's later responses. She is not learning the ideal of equal standing for the first time when she questions Fenrico or defends nonbelievers. Early Phoebe already speaks of a shared festival and access for citizens, while accepting institutional exceptions and teaching official history. A model can later make her ask whether proclaimed inclusion reaches an Echo kept at a distance or a family harmed by authority. It may not backdate the later open hugs at `11375/2` or the proposed governance changes at `11779/2` and `11983/1` to this tour [PHO-E22, E38; PHO-C13, C35].

## Four-language scope and retrieval

The Chinese anchor at `…_16` explicitly makes the Order the agent that **shares use rights** with all Ragunna citizens. Japanese and Korean retain that institutional sharing; English emphasizes use “by the Sentinel's will” through registration and leaves the Order's distributing agency less explicit. At `…_32` Chinese, Japanese and Korean specify **clergy** as the responders' authorized operators; English says Order “members,” a potentially broader category. Japanese `…_31` calls the restricted portion small, whereas the Chinese anchor only says not all are available. These are wording differences, not four independent civic events or proof of different gameplay permissions. The cautious model says: citizen access is represented as broad but not universal across Echo types; the actual scope of authorization and who may operate guarded assets should be tied to the chosen locale and runtime evidence.

For a future human four-dub review, start with the exact source keys `Main_Linaxita_2_1_11_13–17` and `…_29–32`, their `flow#/4203/2` item locators and selected occurrence/render IDs. Listen for whether the delivery sounds welcoming, rehearsed, proud, or uneasy only **after** the corresponding PCM is retrieved. This packet has verified text, graph, identity and media associations, but has not adjudicated these performed qualities or the Carnival subchoice's runtime behavior. The [evidence matrix](WUWA_PHOEBE_EVIDENCE_AND_FALSIFICATION_MATRIX.md) makes the source limits testable.
