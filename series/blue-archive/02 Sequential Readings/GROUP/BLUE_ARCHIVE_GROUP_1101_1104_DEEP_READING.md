---
series: BLUE_ARCHIVE
artifact_type: sequential_deep_reading
scope: GROUP_1101_1104
generation: V1
status: canonical
source_story_ids: ["BA:group:1101", "BA:group:1102", "BA:group:1103", "BA:group:1104"]
source_boundary: "Complete canonical Japanese group objects BA:group:1101 through BA:group:1104 at electricgoat/ba-data@jp a038020f1f5ac02dcfe76962426d38f86414cdd8, generation BA_REFRESH_20260928T032248159554Z; four scenes, 221 structured utterances including one location, 220 canonical text anchors, six Sensei choice groups/eight options; 1101–1102 internally connected, 1103 and 1104 independently placed"
source_generation: BA_REFRESH_20260928T032248159554Z
source_commit: a038020f1f5ac02dcfe76962426d38f86414cdd8
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
created: 2026-10-01
updated: 2026-10-01
---

# Gourmet Research Society group stories deep reading

## Distinct pleasures, disputed care, and culinary help without consent

The four complete stories supply a varied ordinary account of the Gourmet Research Society: the pleasure of finding an aroma, frustration at losing the chance to taste, actual different preferences, desire to share enjoyment, teasing, and attempted kitchen assistance. The central argument is that **shared devotion to food does not make the members interchangeable or automatically make their interventions answerable to the people affected**. Haruna's standards can produce both a wish to include Izumi and destructive presumptions; Junko's practical objections do not remove her participation; Akari's courteous playfulness can carry care and provocation; Izumi's sincere pleasure need not match the others' sensory assumptions or their practical expectations.

This combined reading preserves three analytical divisions: the directly connected `1101–1102` truffle/arrest sequence, the independently placed `1103` taste inquiry, and the independently placed `1104` cafeteria episode. Numeric grouping is a retrieval route, not a proved total chronology. **ADMIT_WITH_LIMITS is accepted in cycle002** for exactly these four complete objects. No shared ledger, index, source record, model status, or repository publication is changed by this document alone.

## 1. Witness and complete inspection

The primary source is `electricgoat/ba-data`, branch `jp`, commit `a038020f1f5ac02dcfe76962426d38f86414cdd8`, game `v1.73.459696-r96_3cpn8ebtdjiqi6y9qtn1`, parser `0.2.0`, in ingestion generation `BA_REFRESH_20260928T032248159554Z`. All four raw groups route to `DB/ScenarioScriptExcelTable1.json`. Its actual snapshot SHA-256 was independently checked as `aaa9e2e5d7e2551af2c7db3109b5132507a0df4596470e03e6945168b73e6303`, matching the structured witness.

| Complete object and title | Canonical route relative to that generation | Coverage and canonical file SHA-256 |
|---|---|---|
| `BA:group:1101` — `美食研究会の日常（１）` | `02_CANONICAL_STORIES/GROUP/CLUB_001_001/EPISODE_001_1101.md` | One scene, 65 structured utterances including one location, 64 canonical text anchors, 89 raw records, zero choices. `2dcbc4021c81c0777e3db221af51940f2935459b19738e360e5a3911caed3147`. |
| `BA:group:1102` — `美食研究会の日常（２）` | `02_CANONICAL_STORIES/GROUP/CLUB_001_001/EPISODE_002_1102.md` | One scene, 43 utterances/text anchors, 62 raw records, six choice groups/eight options. `c785eed180c22e15526e0e1ef906b67f344794b60ddf11ffc3b7c8f61be86aba`. |
| `BA:group:1103` — `偏見なき味覚` | `02_CANONICAL_STORIES/GROUP/CLUB_001_001/EPISODE_003_1103.md` | One scene, 64 utterances/text anchors, 83 raw records, zero choices. `e766e615b42de84b7459877f506e71f656452c2ea95ced22ff1a75fb007c8b03`. |
| `BA:group:1104` — `給食部襲撃事件` | `02_CANONICAL_STORIES/GROUP/CLUB_001_001/EPISODE_004_1104.md` | One scene, 49 utterances/text anchors, 68 raw records, zero choices. `c28b61a5f6951de3fe0b2ed81192a2759a9ef34e4e685e57d1188a638682879f`. |

All four full Japanese canonical sources, their story metadata, the relevant structured utterance/choice records, and raw branch/control records were inspected. The total is **221 utterances, one location unit, 220 text anchors, six choice groups with eight displayed options, four scenes, 302 raw records**. Raw records include control/formatting material and are not an utterance count. No person projection, localization, wiki, or franchise memory replaces the narrative.

`03_STRUCTURED_DATA/stories.jsonl` establishes source type/path; `utterances.jsonl` preserves speaker labels, selection group, and per-record locators; `choices.jsonl` preserves option IDs and selection group. Raw source routes use the immutable snapshot named by `00_MANIFESTS/SOURCE_MANIFEST.json`. For example, `BA:group:1101:scene:001:u:0066` maps to `ScenarioScriptExcelTable1.json:DataList[103391]`, and `BA:group:1102:scene:001:choice:003` to `DataList[103517]`. No raw transcript is copied into analytical Git.

The club is established by explicit `美食研究会` speech/narration, including detention, Veritas visit, and cafeteria self-description. The `CLUB_001_001` numeric route remains generically unresolved in metadata (`unresolved_pending_participant_membership_audit`); this reading does not normalize it by guesswork. It supplies a secure local institutional identification from the text itself.

## 2. Narrative order and branch contract

All four objects have no release date and unresolved story-world placement in `RELEASE_CHRONOLOGY.csv`. `1101` ends with printed arrests and `1102` begins with the whole club detained and discussing that truffle; their local continuation is secure. `1103` recalls a mint-product arrest **yesterday**, without identifying it as that earlier truffle detention. `1104` begins with **today's** cafeteria menu mismatch and independently moves into the kitchen. Nothing orders those last two incidents against the first sequence or against a main-story chapter.

Within `1101`, stable IDs do not equal narrative position: after `u:0002`, **`u:0066` and `u:0067` occur at structured `seq=3` and `seq=4`**, before `u:0005`. `u:0003/0004` are absent from this canonical witness. Preserve the displayed/structured sequence, not numeric sorting of the suffix. The complete set is the location `u:0001`, then `u:0002`, `u:0066-0067`, and `u:0005-0065` in their recorded order.

Raw `SelectionGroup` records supply the branch boundaries in `1102`; the flattened canonical page alone must not create one simultaneous Sensei performance:

| Choice group | Exact options and scoped continuation |
|---|---|
| `choice:001` | Singleton greeting, `や、みんな。` |
| `choice:002` | Option `1`: `違う！濡れ衣！冤罪！` → Akari's skeptical `u:0026`, selection group 1. Option `2`: `話すと長くて……。` → Junko's `u:0027`, selection group 2. These replies are alternatives, not accumulated audience judgments. |
| `choice:003` | Option `3`: `ぜひ！` → sniff narration `u:0029`, selection group 3. Option `4`: `それは流石に却下で。` → Izumi's persuasion `u:0030`, selection group 4, then the branch-local singleton `choice:004`. |
| `choice:004` | Option `5`, `じゃあ、せっかくだし！`, is itself within selection group 4; its continuation is sniff narration `u:0031`, selection group 5. It is not a second sniff required on the initial acceptance route. |
| `choice:005` | Singleton written sniff/reaction `スーハー、スーハー、スーハー……！？` in the later Hina encounter. |
| `choice:006` | Singleton explanation `いや、あの、これも誤解で！`. The script stops without an adjudicated acceptance or full punishment outcome. |

The raw rows at `DataList[103511-103521]` confirm these option/group links. `branch_effect_known=false` in several structured choice records does not mean no branch-marked response exists; conversely, selection markers do not provide a complete executable graph or independent played-through audiovisual verification. Both printed aroma routes reach sniffing in the represented continuation, but the initially refused option is not evidence of a stable refusal untouched by later persuasion.

Inspected raw controls include portrait/visibility operations, waits, background shaking, and separate empty-Japanese records; all 302 raw records have `VoiceId=0`. This observation does not claim that the game has no audio or animated content. Sounds, movements, and written stage directions support only their textual representation here; no performed voice, actual shots heard, or unseen damage visuals are admitted.

## 3. Exact speaking roster and audience limits

| Source | Printed speaking subjects | Absence or source-mode limits |
|---|---|---|
| `1101` | Junko `BA_PERSON_ZUNKO`; Akari `BA_PERSON_AKARI`; Haruna `BA_PERSON_HARUNA`; Izumi `BA_PERSON_IZUMI`; Hina `BA_PERSON_HINA`; Chinatsu `BA_PERSON_CHINATSU`. | Izumi's abandonment plea is a recalled/dramatized passage before Akari's `だそうです`, not proof she is present beside the other three in the park. She is later present in the detention continuation. No Iori/Sensei speech here. |
| `1102` | The four Gourmet members; Iori `BA_PERSON_IORI`; Chinatsu; Hina; Sensei via `BA_SPEAKER_SENSEI` choices. | Narration and choice modes are separate. The pool allegation comes through Hina's report and acknowledged haste, not an independently shown pool scene. |
| `1103` | The four Gourmet members and Hare `BA_PERSON_HARE`. | Iori is reported and identified by narration, not a present speaking actor. The explanatory narration gives her liking for mint; it does not establish her view of every food. |
| `1104` | The four Gourmet members and Fuuka `BA_PERSON_FUUKA`. | Juri is mentioned as absent, with no speech or witnessed reason for absence. No Prefect/Sensei appearance. |

There are **ten distinct printed speaking subjects across the packet**, including branch-speaking Sensei; no new unnamed person is required. The source's `ZUNKO` ID is preserved even though the analytical coverage row renders the name Junko. No playable variant, future club membership, or cross-time identity is established. The kitchenette's sound-only accident passages do not securely assign every intermediate physical act to an individual.

## 4. Connected truffle sequence

### 4.1 Taste devotion coexists with abandonment and intervention

The club flees after Haruna reports destroying an unpalatable dining hall (`:1101:scene:001:u:0067`). Her tap-left-running analogy turns her destructive impulse into a seemingly necessary corrective act; Junko says enforcement is what Prefects do, then refuses further explanation (`u:0005-0009`). This is Haruna's justification and Junko's disagreement, not evidence that destroying an unpopular restaurant is legitimate or that the whole club shares one moral rule.

Akari admits Izumi fell behind and is probably captured, dressing the last words as a heartfelt sacrifice. The embedded plea instead shows Izumi asking not to be abandoned and threatening revenge (`u:0010-0023`). Haruna's solemn sacrifice language is deflated by the actual words. No willing self-sacrifice is established. This is ordinary peer unreliability inside a group capable of affection; a later wish to include her cannot erase how she was left.

Junko notices an appealing scent and finds what Haruna identifies as a truffle. Haruna stresses its aroma and freshness; Akari teases Junko with a pig comparison; Junko refuses the insulting praise (`u:0024-0040`). This is strong affirmative sensory pleasure and negotiated teasing, not a mere transition to a battle. Culinary rarity, relative prices, and processing rules are Haruna/Akari's statements, not verified real-world food facts.

Akari supplies unopened silk underwear as clean wrapping when everyone is muddy; Haruna approves the material and calls Akari's cleanliness habit useful (`u:0041-0050`). The object is newly packaged and repurposed for food aroma, not shown as worn or linked to intimate bodily contact. Haruna's `潔癖症` description is her characterization of a habit, not a clinical diagnosis.

Haruna then says they must rescue Izumi before tasting because no member should be absent (`u:0052`). Her inclusion is sincere in its printed form and bound to a particular desired experience. Hina interrupts the proposed return with severe enforcement language; after beginning `始末`, she changes the order to leaving them only barely alive. Chinatsu requests no resistance; gunfire notation and explicit arrest narration close the scene (`u:0055-0065`). The source prints custody, but no death, clinical injuries, exact fired weapon, or completed sanction ledger. Comic framing does not make the command gentle.

### 4.2 Shared aroma and mistaken adult judgment

In detention, Haruna mourns the confiscated truffle and the lost chance to eat it. Chinatsu says it will be returned after checking criminal relevance, estimating a month (`:1102:scene:001:u:0001-0010`). Return is promised, not shown; the delay interacts with the earlier freshness wish without proving a final recovered food condition.

Akari offers the wrapping's residual aroma. Izumi first dismisses the underwear, then eagerly accepts after the truffle explanation and tries to remember the scent. Haruna praises the pursuit; Junko calls the spectacle improper (`u:0011-0022`). Shared enjoyment and disagreement coexist. No actual truffle meal occurs, yet aroma enjoyment is an achieved sensory experience in the represented text and should not be discarded because it changes no political status.

Sensei greets them. Haruna guesses the teacher was detained for another strange act; the denial/explanation and acceptance/refusal replies branch as specified above (`u:0023-0031; choice:001-004`). That accusation does not prove prior habitual wrongdoing. Izumi invites Sensei into the pleasure and the represented routes reach sniffing, while one first declines before being persuaded. This supplies a limited playful, nonauthoritative teacher presence, not a single mandatory enthusiastic persona across every possible response.

Hina enters, apologizes, and says she detained Sensei too hastily based on a report about naked swimming in the school pool. The text does not verify the alleged conduct. She begins advice about everyday behavior, sees the aroma/underwear situation, and responds to the teacher's explanation with `言い訳は地獄で聞くから` (`u:0032-0043; choice:005-006`). A crash ends the joke. Her first correction is directly observed; the second suspicion is not adjudicated as fact, and no literal death or eternal punishment follows from the idiom. Main-source bodily-boundary counterevidence is neither explained away nor merged with this different clean-object/aroma gag.

## 5. Independently placed taste inquiry

The club visits Hare at Veritas. Hare presents a written account linking mint perception to `OR6A4`/SNPs; Haruna asks about treatment, and Hare rejects treating liking mint as disease (`:1103:scene:001:u:0001-0009`). This is a character's in-fiction scientific explanation. The analysis does not correct its terminology from outside knowledge, validate its biology, or use it as diagnosis.

Junko explains yesterday's detention. Akari discloses the supposedly mint drink was water with toothpaste, causing Hare to revise her initial disbelief at arrest. Izumi argues resemblance, dental benefit and low cost; Junko rejects selling it just because Izumi consumes it (`u:0010-0023`). The distinction is between a sincere preference and responsibility for what is offered to others. Respect for taste does not establish the safety, suitability, or honest description of every claimed food product. No sale count, injury, ingredients analysis, or legal adjudication is printed.

Hare proposes checking everyone's receptor status, suggesting that understanding oneself may support tolerance. Akari is curious; Haruna frames an attempt at impartiality despite disliking mint. Hare reports no receptor for Akari/Junko and presence for Haruna, then unexpectedly reports presence for Izumi (`u:0030-0056`). No method, laboratory record, diagnostic validity or independent genotype is shown. The reported result challenges **the characters' prediction that this sensory account determines what Izumi will enjoy**; it does not prove taste genetically determined or prove that the explanation is scientifically complete.

Izumi still calls mint delicious while being startled that it was supposedly a shampoo-like taste. Hare hesitates about whether someone could like that taste; Junko condemns it; Izumi asks whether commercial shampoo would therefore taste the same (`u:0057-0064`). The final question is not an act of drinking it or a practical recommendation. The title's impartiality is tested by the group's response: a declared intention not to discriminate does not guarantee tolerance when another person's pleasure remains puzzling. Izumi's felt enjoyment is direct self-report; the conceptual label attached to that enjoyment is uncertain and contested.

## 6. Independently placed cafeteria episode

The meal differs from the announced fried egg menu. Izumi complains; Junko says boiled eggs are fine; Akari explicitly likes them and asks for the unwanted serving; Haruna distinguishes respect for eggs from fidelity to the menu (`:1104:scene:001:u:0001-0008`). This differentiates preferences before any accident. It does not establish that all food is objectively bad or that the club invariably refuses ordinary school meals.

Fuuka explains that making 4,000 fried eggs alone within two hours is impossible, Juri is absent, oil unavailable and only one pan present. These are Fuuka's workload/resource reports, not audited procurement figures. Haruna says she anticipated such constraints, brings oil and offers help; Akari calls it friendship; Junko joins in. Fuuka's warning not to touch things without checking is interrupted by their action (`u:0009-0024`).

The intervention has a positive stated intention and actual supplied material. Its failure is nonetheless about coordination and consent: the person responsible for the kitchen is not given effective control over the intervention. Izumi reaches for eggs before cooking, movement on oil initiates a chaotic chain, and the group becomes covered in egg/flour while objects crash. Individual choreography is incomplete in the sound/text rendering (`u:0025-0047`). The members' food jokes continue: being a takoyaki is not the same as liking to eat one. Fuuka's final silence closes the story (`u:0048-0049`) without a prepared meal, cleanup, apology, cost audit, injury report, or repaired labor arrangement.

The episode does not show the Gourmet members deliberately attacking Fuuka or intending kitchen damage. Its title frames the intrusion as an assault on the school-lunch department after offered help has produced disorder. Good purpose and brought supplies are insufficient to make an intervention successful or answerable to its recipient.

## 7. Character and directed relationship additions

| Subject or direction | Added situated repertoire | Limit and contrary evidence |
|---|---|---|
| Haruna | Aroma appreciation; specific shared-tasting inclusion; elegant justification of restaurant destruction; declared impartiality under disliked mint; corrective menu norm and offered labor. `:1101:u:0067,0006-0008,0031-0052; :1102:u:0003-0006,0021; :1103:u:0004,0043-0044; :1104:u:0005-0014`. | Standards do not establish legitimate destructive power or successful tolerance. Inclusion follows earlier abandonment; help fails to respect Fuuka's practical warning. |
| Akari | Playful teasing, useful clean supplies, shared residual aroma, curiosity about taste, explicit boiled-egg preference and offered help. `:1101:u:0011-0023,0038-0039,0044-0048; :1102:u:0011-0015; :1103:u:0033,0035,0039; :1104:u:0004,0016-0017`. | Politeness/stars do not erase manipulation, insulting praise, or intrusion. Cleanliness label is not diagnosis; no total appetite/psychology model. |
| Junko | Practical criticism, scent finding, resistance to teasing, disapproval of dubious drink sales, mint tolerance, meal flexibility, willing participation in help. `:1101:u:0005-0009,0024-0047; :1102:u:0012,0020,0022; :1103:u:0012,0023,0046,0056-0063; :1104:u:0003,0018-0019,0022`. | The rational objection role is neither invariant tolerance nor a guarantee against participating in harmful group action. Her condemnation of Izumi is contrary evidence to pure nonjudgmental pragmatism. |
| Izumi | Protest at abandonment, desire for shared aroma, sincere mint pleasure, invited teacher participation, egg/rice and takoyaki preferences. `:1101:u:0016-0019; :1102:u:0002-0007,0013-0019,0028-0030,0037; :1103:u:0022,0027-0028,0049-0062; :1104:u:0021-0024,0040,0044`. | Product preference does not prove suitability for sale or bodily safety. The final shampoo analogy is a question; no consumption occurs. Desire for food does not erase her claim not to be left behind. |
| Hina → detainees/Sensei | Pursuit, severe arrest command, apology for haste in teacher detention, then another negatively interpreted circumstance. `:1101:u:0055-0065; :1102:u:0033-0042; choice:005-006`. | Local apology is correction, not general infallibility, complete due process or crisis restitution. Neither pool wrongdoing nor literal killing is established. |
| Chinatsu/Iori → club | Chinatsu directs no resistance and explains investigation/return schedule; Iori demands quiet in detention, while mint preference is later narrator information. `:1101:u:0062-0063; :1102:u:0008-0009; :1103:u:0019-0021`. | No printed evidence-return outcome, complete detention procedure, or Iori speech in `1103`. |
| Hare → Gourmet | Distinguishes preference from disease, proposes self-knowledge/tolerance, supplies reported tests and revises expectations under Izumi's case. `:1103:u:0002-0009,0024-0045,0050-0058`. | Scientific/clinical validity and the exact testing procedure are unverified. This is an ordinary explanatory/helping role, not proof of omniscience. |
| Gourmet → Fuuka | Menu grievance becomes supplied oil and volunteered work, then disrupted kitchen despite a warning. `:1104:u:0009-0049`. | Intentional aid and actual failure coexist; no apology, restitution or finished meal. Fuuka's workload statement and silence remain distinct from inferred emotions. |
| Society members → Izumi | Abandonment/teasing followed by desired inclusion in a valued pleasure, dispute over taste and attempted aroma sharing. | No stable loving/hateful group verdict, involuntary suffering erased by affection, or completed exclusive friendship model. |

All shorthand in this table uses `scene:001` after the explicit story prefix; no other scene is implied.

## 8. Written language and attribution cautions

The Japanese layer includes Haruna's polite/elegant formulations, Akari's courtesy with stars, Junko's blunt correction/threats, Izumi's enthusiastic invitations/protests, Hare's explanation and epistemic hedges, Hina's compressed severe commands, and Chinatsu's procedure. These are written registers. Humming, sniff spelling, gunfire and crashes provide no acted prosody or audio evidence.

`美食`, `香り`, `実食`, `味`, and `先入観` make enjoyment and interpretation an argument of their own. `犠牲` is explicitly contradicted by Izumi's plea; `友情` names desired or claimed relation without demonstrating successful care. `治療` is contested; Hare's `推察`, `かもしれない`, and eventual hesitations preserve the limits of her explanatory claims. `誤解`, `冤罪`, and `早とちり` distinguish allegations, denial, and authority correction in detention.

| Locator | Source caution |
|---|---|
| `BA:group:1101:scene:001:u:0035` | Haruna-tagged surprised reply follows Haruna's own rarity comparison; exact respondent is uncertain. Do not repair to Junko or use as secure individual voice. |
| `BA:group:1101:scene:001:u:0053-0054` | Haruna tags praise the chair and shift into a bright friendship/violence register immediately after her own rescue proposal. Preserve labels; use ensemble reaction cautiously rather than silently assigning Junko/Akari. |
| `BA:group:1102:scene:001:u:0023` | Haruna-tagged colloquial surprise differs from nearby formal turns. This is a caution, not proof of another speaker. Teacher presence is independently established by greeting and subsequent securely attributed responses. |
| `BA:group:1104:scene:001:u:0031-0037` | Rapid catches, warnings, motion and crashes do not fully identify each bodily act. Do not reconstruct exact collision choreography or resulting injury from personality expectations. |
| `BA:group:1102` choices and branch responses | Retain the exact §2 selection-group conditions. Narration of two possible sniff routes is not two sequential sniffs on every route; skeptical branch replies are not simultaneously heard. |

Food or receptor labels are character/source claims at this witness, not scientifically checked measurements. No source spelling or claim is silently fixed to a different presumed biological/culinary concept.

## 9. Counterreadings and main-state comparison

**“The club cares about food and nothing else.”** Destruction, product sale and kitchen intrusion support an uncompromising-priority reading. Izumi's abandonment grievance, Haruna's later insistence on including her, aroma sharing, teacher invitation, and actual offered oil/labor supply contrary interpersonal motives. Those motives do not absolve their failures.

**“The funny food scenes can be discarded once preferences are logged.”** Their scene structures matter: rescue language misreads abandonment; loss of an ingredient becomes shared residual aroma; a reported test fails to settle a person's pleasure; helpful intrusion creates work for its recipient. They are mechanisms and relations, not just a list of favorite foods.

**“Hare explains Izumi scientifically, so the mystery is solved.”** Her prediction of receptor absence is contradicted by her own reported result, while Izumi's enjoyment persists. The text also lacks independent test validity. A strong interpretation preserves the distinction between reported sensory classification and pleasure instead of closing it through imagined physiology.

**“Hina's apology proves her enforcement is always proportionate.”** It corrects one haste claim; harsh arrest language and a new prejudgment qualify any universal formulation. Conversely, the unordered gag does not prove timeless cruelty or explain NK Ultra causality. Literal casualties and outcomes remain unprinted.

**“Bringing oil makes the kitchen intervention recipient-centered.”** Supplied resources are real helpful intent. Fuuka's warning and the resulting disorder expose practical control and coordination limits. This case does not show the source recipient accepting the intervention or the promised food being made.

The current [S2 V002 C002 checkpoint](../MAIN/SERIES2_VOLUME_002/BLUE_ARCHIVE_MAIN_S2_V002_C002_CHECKPOINT.md) separately preserves coerced food control, Gourmet apologies, Fuuka/Izumi boundaries, Hina's custody/accountability and incomplete repair. These side scenes broaden ordinary comparison; their unresolved chronology cannot make them post-apology regression, prove brainwashing caused prior culinary misconduct, or erase a crisis victim's grievance. Fuuka's ordinary workload and warning are independently relevant even without that later crisis comparison. The earlier [V001 C002 checkpoint](../MAIN/VOLUME_001_%E5%AF%BE%E7%AD%96%E5%A7%94%E5%93%A1%E4%BC%9A%E7%B7%A8/BLUE_ARCHIVE_MAIN_V001_C002_CHECKPOINT.md) retains its specific Hina mandate correction and Sensei/Iori bodily-boundary counterevidence; this different comic detention does not acquit or repeat that act by inference.

**Observed behavioral delta:** several situated repertoires are added, rather than one universal rule. They include valued sensory experience shared under loss; a preference account resisting a classificatory prediction; inclusion following unreliable peer care; good-purpose aid failing without coordination; and accusation/correction/reaccusation in a comic authority setting. The sources were read without a frozen prospective rule or prediction: `NO_DIAGNOSTIC_OPPORTUNITY`. No model, validation score, new durable claim ID, clinical diagnosis, or performed-voice conclusion is proposed.

## 10. Proposed seven-ledger effects

All effects await the integrating owner's scoped acceptance and reconciliation. Preserve existing first-pass prose, main-state knowledge and source witnesses.

| Ledger | Proposed contextual addition |
|---|---|
| Character state | Add differentiated Gourmet sensory pleasure, peer motives and failures; Hare's ordinary explanatory/limited role; Fuuka's resource/workload statement and warning; Hina's severe comic enforcement/apology; Chinatsu/Iori's narrow procedure. §7 supplies exact scope. No medical or model-status promotion. |
| Relationship state | Add society↔Izumi unreliable care versus shared pleasure; Akari→Junko teasing and resistance; Izumi→Sensei branch-aware sharing; Hina→Sensei haste/apology/new suspicion; Gourmet→Hare inquiry/disagreement; Gourmet→Fuuka offered aid without effective recipient control. No universal romance, friendship or reconciliation. |
| School club institution | Add preference-driven restaurant destruction as reported, arrest and confiscation procedure as stated, dubious labeled-drink sale as reported, interschool inquiry, and kitchen resource/coordination failure. No full legality finding, evidence-return result, clinical safety proof or completed restitution. |
| Sensei role and ethics | Material direct delta in `1102`: detained teacher enters shared aroma joke; alternative denial/explanation and acceptance/refusal→persuasion routes remain distinct. Hina admits premature custody on a pool report; final explanation is unaccepted/unadjudicated. No naked-swimming proof, sexual motive inference, literal death or universal teacher persona. No direct Sensei appearance in the other three objects. |
| Japanese voice/address | Add §8's secure taste/pleasure, alleged sacrifice, friendship, explanation, authority and misunderstanding clusters; retain stable-ID order, disputed speaker turns, exact branches and written-only limits. |
| Motif/theme/callback | Add valued scent without consumed ingredient, improvised clean wrapping, difference between taste and pleasure, imagined food transformation, menu versus labor, helpful intent versus intrusive means, and repeated misunderstandings. Analogies to main agency/repair remain comparisons rather than proved timeline/callbacks. |
| Claim revision | `BA-C016` **STRENGTHEN / SCOPED ORDINARY TEST**: positive intention/material aid does not replace recipient control, as Fuuka's warning and failed help show. `BA-C017` **COMPLICATE locally**: ability to object, classify, explain and correct is unevenly respected. `BA-C007/C010/C011` **PRESERVE / DIRECT SENSEI TEST LIMITED**: the teacher is chiefly a detainee/participant, not an observed corrective intervention; fallibility and misunderstanding alone do not prove these entire adult-role claims. `BA-C008` **STRENGTHEN FIREWALL** through six branch groups. `BA-C015/BA-C018` **PRESERVE / NO DIRECT ABYDOS TEST**: food and hospitality analogies do not restate those institutions' history. No new durable claim ID. |

## 11. Coverage, source gaps, and acceptance boundary

After parent acceptance, group coverage cells can record **Haruna, Akari, Junko/BA_PERSON_ZUNKO, and Izumi** across all four complete objects; **Hina and Chinatsu** in `1101/1102`; **Iori and Sensei** as speaking in `1102`; **Hare** in `1103`; **Fuuka** in `1104`. Izumi's `1101` mode is recalled until the continuation; Iori's `1103` appearance is reported/narratorial rather than speaking. Juri is an absent mention. No new generic speaking person or variant is added, and none of these cells closes all remaining group/private/profile coverage.

The contribution is **HIGH for the Gourmet ordinary/peer/institution account** and material to Hina's lower-pressure authority comparison. Quiet pleasure and unusual tastes have affirmative standing independent of scandal, danger or continuity consequence. The scope is these complete Japanese scenes, not general scientific or legal conclusions.

| Gap ID | Reduction and preserved debt |
|---|---|
| `G01` ordinary/private breadth | Partial reduction through specific realized smell pleasure, reported/expressed taste preferences, teasing, shared disappointment, kitchen work and teacher play. No completed truffle meal or full independent/private coverage. |
| `G04` Hina ordinary contrast/accountability | Add pursuit, severe phrasing, acknowledged haste/apology and new suspicion in an unordered side context. NK Ultra causal allocation, victims' repair and lasting institutional change remain open. |
| `G07` chronology | Admit `1101→1102` local continuation and the distinct internal yesterday/today markers. Preserve unresolved relation between all other incidents and main states. |
| `G09` attribution/branches | Add exact warnings, recalled Izumi mode, source-ordered u:0066/u:0067, and six-choice/eight-option branch map with conditional replies. No silently corrected speaker or composite teacher performance. |
| `G10` performed voice | No reduction. Raw zero VoiceIds and textual sound tokens do not establish heard/acted delivery. |
| `G12` person/variant identity | Preserve Junko's actual ZUNKO source ID, ten named speaking subjects, absence/mention modes, and no invented variant or new person. |
| `G13` outcomes/technical claims | Confiscation return, sanctions, injuries, actual food safety/receptor measurements, kitchen restoration and complete accounting remain unprinted or unverified. Actual arrest narration is stronger than a pursuit forecast; it still supplies no whole custody audit. |

Further readings should test recurring ways the members respect others' different pleasures, how Fuuka's work is distributed, and how Prefects and the Society handle correction after comic failures. These are open source questions, not retrospective scored predictions. Material not yet read remains eligible, including uneventful enjoyment scenes that supply no crisis outcome.

## 12. Evidence locator map

| Finding | Exact primary locator |
|---|---|
| Reported dining-hall destruction and Junko's objection | `BA:group:1101:scene:001:u:0002,0066-0067,0005-0009` in recorded order |
| Izumi left behind; false sacrifice interpretation; recalled plea | `BA:group:1101:scene:001:u:0010-0023` |
| Truffle finding/aroma and teasing | `BA:group:1101:scene:001:u:0024-0040` with u:0035 caution |
| Clean wrapping, desired shared tasting and rescue | `BA:group:1101:scene:001:u:0041-0054` with u:0053-0054 caution |
| Severe command, textual gunfire, printed arrests | `BA:group:1101:scene:001:u:0055-0065` |
| Confiscation and achieved shared residual aroma | `BA:group:1102:scene:001:u:0001-0022` |
| Sensei greeting, alternative reply and aroma routes | `BA:group:1102:scene:001:u:0023-0031; choice:001-004` under §2 conditions |
| Hina's custody apology, new suspicion, teacher explanation | `BA:group:1102:scene:001:u:0032-0043; choice:005-006` |
| Preference versus disease and reported toothpaste-water sale | `BA:group:1103:scene:001:u:0001-0029` |
| Proposed self-knowledge, reported tests, prediction failure | `BA:group:1103:scene:001:u:0030-0056` |
| Persistent pleasure, tolerance dispute and unacted shampoo analogy | `BA:group:1103:scene:001:u:0057-0064` |
| Different egg preferences/menu claim | `BA:group:1104:scene:001:u:0001-0008` |
| Fuuka's resource constraint, offered help, ignored warning | `BA:group:1104:scene:001:u:0009-0024` |
| Kitchen disorder, food jokes and unresolved final silence | `BA:group:1104:scene:001:u:0025-0049` with choreography limit |

## Parent acceptance — cycle 002

[Cycle 002](../BLUE_ARCHIVE_PHASE2_CONTEXTUALIZATION_CYCLE_002_CHECKPOINT.md) accepts exactly the source IDs declared above after complete contributor inspection, integrator analysis review, canonical/raw witness checks and consequential Japanese/branch tests. Applicable proposals are now reconciled in all seven ledgers and the current contextual coverage/control surfaces. This acceptance supplies contextual repertoire; no main chronology, performed voice, model promotion or prospective validation is inferred. The cycle owns admission; this packet is not a second admission count. The attribution review distinguishes prior display-actor labels from text-bearing commands at 1101 u0035/u0053/u0054 and 1102 u0023. Their individual voice assignments remain qualified.
