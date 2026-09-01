---
title: "IDOLY PRIDE V2 — Hoshimi Anime ↔ Game Expansion Audit"
project: "IDOLY PRIDE"
document_id: "IDOLY_PRIDE_V2_HOSHIMI_ANIME_GAME_EXPANSION_AUDIT"
version: "1.0"
status: "phase-1b-tranche-02-complete"
phase: "1B"
source_snapshot_id: "IP-V2-SNAPSHOT-2026-08-13-A"
source_cutoff: "2026-08-13"
anime_baseline: "IDOLY_PRIDE_V2_ANIME_ENDPOINT_LEDGER_EP01-12"
game_scope: "st-original-cmn / Hoshimi main-story retelling"
game_blocks: 23
granular_game_scenes: 122
manager_identity_rule: "Manager (player) is continuing Makino Kouhei; naming/dialogue customization is interface parameterization unless contradictory source evidence appears"
created: "2026-08-14"
updated: "2026-08-14"
---

# IDOLY PRIDE V2 — HOSHIMI ANIME ↔ GAME EXPANSION AUDIT

## 1. Purpose

This document performs the dedicated Phase-1B cross-media audit of the Hoshimi `st-original-cmn` game main story against the frozen twelve-episode television-anime baseline.

The question is not whether the game is "the same story." It is:

> **What does the game preserve, add, make explicit, reorder, reframe, or materially change when it retells the anime-era Hoshimi story from the continuing Makino Kouhei/player-manager position?**

The governing source order is deliberately asymmetric:

1. the anime endpoint was frozen prospectively in Phase 0.5;
2. only after that freeze is the game retelling admitted;
3. game information may explain or recontextualize the anime, but may not be projected backward as knowledge that an anime viewer already possessed;
4. where the game and anime construct materially different event sequences, both versions are preserved as cross-media variants rather than silently harmonized.

This audit therefore functions as a bridge between the anime-native baseline and the post-anime game corpus.

---

# 2. Sources and audit mechanics

## 2.1 Game source

Primary game reading layer:

- `analysis_bundles/00_shared/01_main_story.dialogue.txt`
- Hoshimi story IDs: `st-original-cmn-01-01-01` through `st-original-cmn-01-04-24`
- 122 granular story scenes
- 23 named analytical blocks:
  1. `Shine Purity`
  2. `Short Goodbye`
  3. `like the Sun/Moon`
  4. `Strange One`
  5. `The Sun, Moon and Stars`
  6. `to Trust One`
  7. `Drop of Smile`
  8. `Make up her Mind`
  9. `With a Will`
  10. `Proud Lady`
  11. `Resolution`
  12. `Dear My Sister`
  13. `Sunlight`
  14. `Successor of Miracle`
  15. `Sorrows of Orpheus`
  16. `Cherry,Worry`
  17. `Beat Meets`
  18. `Idoly Pride`
  19. `Still Live`
  20. `on My Way`
  21. `Glory Days`
  22. `Last Step`
  23. `Pray for you`

The Hoshimi slice contains approximately **10,709 dialogue/narration lines**. `Manager (player)` accounts for **2,844 lines (~26.6%)**, of which **1,178** are parenthetical/internal narration (~41.4% of his lines). This is not a cosmetic POV conversion: Makino's interiority is a major component of the game edition.

## 2.2 Anime source

Governing anime baseline:

- `IDOLY_PRIDE_V2_ANIME_ENDPOINT_LEDGER_EP01-12.md`
- twelve frozen episode-level V2 analyses produced before the game retelling was allowed to inform interpretation.

The anime remains the governing source for:

- voice performance;
- music/sound;
- blocking;
- composition;
- shot duration/editing;
- color/light;
- body language and physical proximity;
- performance staging and audience position.

The game retelling can add prose/interiority or change event architecture, but it cannot replace anime-native audiovisual evidence.

---

# 3. Governing Makino rule

For this project:

> **`Manager (player)` is the continuing Makino Kouhei.**

The customizable player name / `{user}` is treated as interface-level parameterization. The game places the player into Makino's established Hoshimi position and preserves his biographical role; external visual/voice continuity further supports that reading.

This produces four evidence classes for later Makino work:

1. **Identity-invariant Makino fact** — history, role, relationships, branch-invariant actions.
2. **Branch-invariant Makino dialogue/interiority** — ordinary canonical characterization.
3. **Player-selected Makino expression** — an authored Makino-compatible possibility, but not all mutually exclusive choices may be treated as simultaneously occurring.
4. **Interface-only parameterization** — custom name / `{user}` and comparable affordances; no identity discontinuity follows from them.

The flattened `01_main_story.dialogue.txt` is excellent for semantic reading but does not always preserve enough branch metadata to decide which Manager line belongs to which selectable option. Exact branch routing therefore belongs in the later Makino Player-Branch Canon Ledger and, when necessary, must descend to the underlying `script.jsonl` provenance layer.

---

# 4. Cross-media relation vocabulary

The audit uses the following labels:

- **DIRECT_RETELLING** — substantially the same dramatic event/function.
- **EXPANDED_MAKINO_POV** — game adds Makino's internal observation, memory, motive, uncertainty, or professional reasoning.
- **EXPLICITATED_MOTIVE_OR_PROFESSIONAL_REASONING** — game states reasoning only implicit or formally conveyed in anime.
- **ADDED_SCENE_OR_CONTEXT** — compatible scene, relationship beat, worldbuilding, or character material absent from anime.
- **GAME_ORIGINAL_CHARACTER_ARC** — substantial game-only or game-dominant development, not merely connective dialogue.
- **INFORMATION_ORDER_SHIFT** — a fact appears materially earlier/later in one medium.
- **REFRAMING_OR_EMPHASIS_SHIFT** — same broad event gains a different causal/thematic center.
- **RETELLING_CONTINUITY_VARIANT** — event architecture differs enough that it should not be silently merged.
- **ANIME_ONLY_AUDIOVISUAL_FORM** — meaning depends on voice/music/camera/body/editing not reproducible by game prose.
- **UNRESOLVED** — relation cannot yet be stabilized from the current reading layer.

---

# 5. Executive findings

## Finding A — The game is a genuine expansion layer, not an anime transcript

All 23 Hoshimi blocks remain **CORE**.

The strongest reason is structural. More than a quarter of the Hoshimi textual lines are assigned to Makino, and more than a thousand of those lines are explicitly internal/parenthetical. The game repeatedly provides:

- Makino's memory before and after Mana's death;
- his private attraction to Mana before they became close;
- his interpretation of candidate strengths and weaknesses;
- professional reasoning behind intervention or non-intervention;
- uncertainty over what good management requires;
- reactions he does not verbalize to the idols;
- ethical hesitation around Sakura's heart, Mana's ghost, Kotono, and performance inheritance;
- a first-person account of why he continues managing.

A source model that discards `st-original-cmn` as redundant would therefore erase a large fraction of Makino's authored characterization.

## Finding B — The game deliberately destroys part of the anime's medical mystery much earlier

The most important information-order difference appears immediately.

In `Shine Purity`, Makino already narrates:

> `さくらは心臓移植をしたと言っていた`

and that Sakura described her heart as directing her toward Hoshimi.

By contrast, the anime proceeds in stages:

- Episode 4: surgical scar;
- Episode 7: surgery explicitly identified as heart surgery;
- Episode 8: `移植` finally confirms transplant;
- Episode 9: Mana is narratively confirmed as donor.

Therefore:

> **The game Hoshimi retelling cannot be used to claim that early-anime Sakura was transparently a transplant recipient.**

The two media deliberately manage revelation differently. The anime builds medical ambiguity as a long-form mystery; the game assumes or reveals more of Sakura's medical history almost from the start.

## Finding C — The game gives the ensemble far more pre-Grand-Prix individual development

The anime's twelve-episode economy forces many secondary-character developments into compressed ensemble beats.

The game inserts full arcs for:

- Rei and the difference between loving dance and initially loving idolhood;
- Shizuku's anxiety over whether she can embody the smiling idol she admires;
- Haruko's finite career horizon and temptation to move into musical theatre;
- Nagisa's fear that she lacks a distinctive idol identity beside Kotono;
- Suzu's family conflict, financial dependence, work, and proof-of-commitment problem;
- Mei's ordinary friendship with ghost Mana and her decision about what sort of idol she wants to become;
- Saki and Chisa's bilateral sister-individuation rather than merely Chisa becoming less dependent.

These are not optional "side stories" inside the Hoshimi retelling. They occupy the main-story spine before the later Grand Prix climax.

## Finding D — The game makes Makino's managerial apprenticeship much more explicit

The anime often lets Makino's development emerge through decisions and audiovisual juxtaposition. The game repeatedly lets him think through the decisions.

Examples include:

- his recognition that group formation is partly experimental rather than omniscient;
- concern that he has become overprotective of Rei;
- identifying the need to tell difficult truths rather than simply soothe;
- his own overwork and collapse, which makes sustainability a manager problem embodied in Makino himself;
- distinguishing what he wants personally from what he should recommend professionally to Haruko;
- accepting that he cannot decide Kotono's sister relationship for her;
- recognizing at the final that "the manager" can ultimately do little except create conditions and watch the idols choose.

The game therefore does not merely give the player more lines. It turns Makino into a much more continuous first-person professional consciousness.

## Finding E — Later game-Hoshimi chronology is not identical to anime chronology

The largest mistake would be to treat the Hoshimi main story as a scene-expanded screenplay of Episodes 1–12.

It is a **retelling** with different sequencing.

Notable examples:

- Rui's relationship to Asakura is disclosed during Suzu's `Proud Lady` development, substantially earlier than the anime's Episode-10 Rui focus.
- Mana's secrecy toward Kotono, Mei's role as her interlocutor, and several Grand Prix identity problems are distributed differently across the game blocks.
- the game resolves or stages several Kotono/Rio issues before/around the semifinal structure in a different order from Episodes 10–11.
- Mana's final disappearance/farewell occurs **before the Grand Prix final** in the game architecture; the anime lets Mana witness the two unit-final performances before she disappears.

This requires explicit cross-media chronology fields in later ledgers.

## Finding F — The finale is a material continuity variant, not simply an expansion

This is the most important concrete divergence found in Tranche 02.

### Anime finale

The anime gives:

1. separate SUNNY PEACE and Tsuki no Tempest final performances;
2. an extraordinary tie / double victory;
3. Mana witnesses their self-authored unit performances and then disappears;
4. the winner-stage privilege becomes a ten-person Hoshimi performance;
5. the tie prevents the final ranking from designating one unit as the singular post-Mana successor.

### Game finale

`Pray for you`, especially `st-original-cmn-01-04-24`, instead has:

1. the two units decide **before the final** to perform together;
2. they tell the audience to judge whether SUNNY PEACE or Tsuki no Tempest deserves victory from the same ten-person performance;
3. the joint final song is `サヨナラから始まる物語`;
4. the encore is `First Step`;
5. Makino explicitly interprets the encore as Mana's song being sung for Mana and the whole stage being offered to her;
6. the available Hoshimi text does not reproduce the anime's tie architecture.

This is a genuine **RETELLING_CONTINUITY_VARIANT**.

It changes thematic emphasis:

- the anime finale is more strongly **anti-singular** and post-succession: two differentiated units first prove themselves independently, tie, and then reunite;
- the game finale is more strongly **integrative and memorial**: the decisive final is already a ten-person Hoshimi act and explicitly returns to `First Step` for Mana.

Neither version should be silently used to explain the other's formal finale.

---

# 6. Block-by-block expansion matrix

The anime anchors below indicate the nearest dramatic material, not a claim of one-to-one adaptation.

## 01. `Shine Purity`
**Source:** `st-original-cmn-01-01-01`–`06`  
**Nearest anime anchor:** Episodes 1–2  
**Relation:** DIRECT_RETELLING + EXPANDED_MAKINO_POV + INFORMATION_ORDER_SHIFT

### What the game adds
- A much fuller first-person history of Makino and Mana before her career: Makino describes her as a popular, beautiful classmate socially distant from his own `日陰組` self.
- Makino admits ordinary adolescent attraction while also emphasizing that they were not initially close.
- Mana's request that Makino enter Hoshimi with her is explicitly motivated by his unusually "normal" treatment of her.
- The two-year path from school request → Hoshimi employment → assistant-manager identity is narrated rather than left as fragmented backstory.
- Makino explicitly explains why he remained after graduation: the work had become interesting and he wanted to see how far Mana could go.
- Saegusa's BanPro background and the post-Mana project pact are made more explicit.
- Makino's evaluation of Sakura and Kotono is much more internal/professional than the anime can supply through dialogue alone.

### Major sequencing difference
- Sakura's heart transplant and her claim that her heart guided her to Hoshimi are already explicit at the end of the block.
- This is radically earlier than the anime's Episode-8 transplant confirmation.

### V2 consequence
`Shine Purity` is foundational Makino material but **cannot retroactively resolve the anime's early medical ambiguity**.

---

## 02. `Short Goodbye`
**Source:** `st-original-cmn-01-01-07`–`11`  
**Nearest anime anchor:** Episodes 2–3, with material later distributed elsewhere  
**Relation:** DIRECT_RETELLING + ADDED_SCENE_OR_CONTEXT + EXPANDED_MAKINO_POV

### Expansion
- New-member intake is slower and more individualized.
- Makino supplies explicit evaluations of temperament and professional fit rather than the anime relying primarily on ensemble presentation.
- The dorm-manager role and Hoshimi City's relation to Mana's earlier popularity receive more worldbuilding.
- Hoshimi Festival memory gives the local institution a longer social history.
- Sun/moon language enters not merely as later performance branding but as a practical problem of how different personalities might coexist.

### Reframing
The game makes Hoshimi's early ensemble feel less like a cast being assembled by narrative necessity and more like a **managerial design problem with visible uncertainty**.

---

## 03. `like the Sun/Moon`
**Source:** `st-original-cmn-01-01-12`–`16`  
**Nearest anime anchor:** Episodes 3–5  
**Relation:** EXPANDED_MAKINO_POV + ADDED_SCENE_OR_CONTEXT + EXPLICITATED_MOTIVE

### Expansion
- Makino explicitly recognizes mistakes in how he has structured or communicated the group project.
- The game gives more recruitment/settling-in material for the quieter members.
- It articulates Sakura's preference for collective singing more directly.
- It places more weight on Makino observing how solitude, confidence and aspiration differ among members who may all superficially look "quiet."
- Photography and ordinary group interaction turn "forming a group" into a longer social process.

### Anime-only remainder
The anime remains superior evidence for the physical grammar by which group space becomes more or less permeable.

---

## 04. `Strange One`
**Source:** `st-original-cmn-01-01-17`–`21`  
**Nearest anime anchor:** Episode 4, plus Grand-Prix material the anime delays until Episode 7  
**Relation:** DIRECT_RETELLING + INFORMATION_ORDER_SHIFT + EXPANDED_MAKINO_POV

### Expansion / shift
- Mei recruitment and the search for missing group dynamism align broadly with Episode 4.
- The NEXT VENUS Grand Prix restoration/institutional context enters materially earlier than in anime sequencing.
- Makino's sense that the current group is technically capable but missing something is stated internally instead of inferred through rehearsal form.
- Mana functions more overtly as a conversational sounding board for Makino's professional uncertainty.

### V2 consequence
Do not use the game's earlier Grand Prix knowledge when reconstructing what anime Episodes 4–6 prospectively establish.

---

## 05. `The Sun, Moon and Stars`
**Source:** `st-original-cmn-01-01-22`–`28`  
**Nearest anime anchor:** Episodes 4–6  
**Relation:** DIRECT_RETELLING + GAME-ADDED MANAGER ARC + ADDED_SCENE_OR_CONTEXT

### Expansion
- Rei receives more explicit recruitment logic around elite dance ability versus idol-specific play/relationality.
- Makino openly worries about whether the roster he designed is adequate.
- Makino's sleep deprivation culminates in **his own collapse and hospitalization**, a major game-only embodiment of unsustainable professional devotion.
- The idols continue training while he is unavailable, preventing the manager from becoming the sole causal engine of progress.
- Sakura/Kotono discussion around Mana's debut stage and Makino's past is more extensive.
- The debut performance is framed textually as an `産声`—a birth cry—giving the group's public emergence an explicit metaphor the anime largely leaves to form/music.

### Reframing
The game turns the ethics of rest from something Makino administers to idols into something **Makino himself fails to practice**.

---

## 06. `to Trust One`
**Source:** `st-original-cmn-01-02-01`–`05`  
**Nearest anime anchor:** Episode 5, especially Rei/Chisa discipline conflicts  
**Relation:** GAME_ORIGINAL_CHARACTER_ARC + EXPLICITATED_MOTIVE + EXPANDED_MAKINO_POV

### Expansion
- Rei explicitly says she did not originally dream of being an idol; idolhood is a way to make dance her work.
- Her severe practice ethic is connected to the fear that elite rivals such as LizNoir are already beyond ordinary effort.
- The game gives her direct professional exposure to LizNoir's dance standard.
- Makino recognizes that overprotection/intervention can become its own problem and that trust may require allowing members to solve interpersonal difficulties.

### V2 consequence
The anime's Episode-5 Rei should no longer be treated as if her entire professional philosophy were already exhausted by "discipline." The game reveals a more specific initial vocational route: **dance first, idolhood as professional container, then broader idol identity.**

---

## 07. `Drop of Smile`
**Source:** `st-original-cmn-01-02-06`–`10`  
**Nearest anime anchor:** Episode 5 ensemble differentiation  
**Relation:** GAME_ORIGINAL_CHARACTER_ARC + ADDED_SCENE_OR_CONTEXT

### Expansion
- Shizuku's idol fandom becomes a direct source of self-doubt: if idols smile and radiate confidence, what does it mean that she cannot naturally perform that way?
- Chisa and Shizuku become mutually useful precisely because their insecurities are different.
- Idol quiz / media appearances turn fandom knowledge into both comic texture and professional competence.
- Makino learns to give criticism without flattening temperament into deficiency.

### Reframing
The anime showed that Chisa and Shizuku are both quiet but not quiet in the same way. The game turns that distinction into a sustained developmental arc.

---

## 08. `Make up her Mind`
**Source:** `st-original-cmn-01-02-11`–`15`  
**Nearest anime anchor:** Haruko's continuity role; no close anime plot equivalent  
**Relation:** GAME_ORIGINAL_CHARACTER_ARC

### Expansion
- A false "omiai" setup becomes a serious career fork when Haruko is offered a route toward musical theatre.
- Haruko explicitly confronts the finite duration of idolhood, her insecurity about whether effort can overcome limits of talent/age, and the possibility that another performing-art path may fit her.
- Sakura and the others have to distinguish wanting Haruko to stay from claiming authority over Haruko's career.
- Makino explicitly separates his **professional** obligation to respect Haruko's choice from his **personal** desire that she remain with SUNNY PEACE.

### V2 consequence
This is foundational later evidence for Haruko, adult idol longevity, professional labor, and manager ethics. The anime alone substantially underdetermines these dimensions.

---

## 09. `With a Will`
**Source:** `st-original-cmn-01-02-16`–`20`  
**Nearest anime anchor:** Nagisa/Kotono relational material from Episodes 3–6  
**Relation:** GAME_ORIGINAL_CHARACTER_ARC + ADDED_CROSS-UNIT CONTEXT

### Expansion
- Nagisa worries that technical adequacy and loyalty to Kotono do not amount to an independently legible idol identity.
- Her insecurity centers on what she contributes when she is not simply "the person who understands Kotono."
- TRINITYAiLE members, especially Yu/Sumire, provide a comparative relational model rather than merely functioning as elite rivals.
- Makino explicitly treats self-concept as a professional performance problem rather than only an emotional problem.

### Reframing
Nagisa's relational intelligence remains real, but the game prevents it from becoming her entire ontology.

---

## 10. `Proud Lady`
**Source:** `st-original-cmn-01-02-21`–`25`  
**Nearest anime anchor:** Suzu characterization, plus Rui/Asakura information the anime develops in Episode 10  
**Relation:** GAME_ORIGINAL_CHARACTER_ARC + INFORMATION_ORDER_SHIFT

### Expansion
- Suzu's family directly challenges her idol career.
- Her economic dependence becomes concrete when access to family money is removed.
- She confronts the actual monetary value of ordinary paid work and the difference between theatrical self-confidence and demonstrated independence.
- Her idol dream is linked to Mana's earlier influence on her as a girl.
- The conflict becomes a test of whether Suzu can persist when the prestige language disappears.

### Major order shift
Rui tells Suzu that Asakura is her father here, **far earlier** than the anime's concentrated Episode-10 treatment.

### V2 consequence
The game provides major Suzu/family/class evidence, but its Rui knowledge must not be projected backward into early anime episodes.

---

## 11. `Resolution`
**Source:** `st-original-cmn-01-02-26`–`30`  
**Nearest anime anchor:** Episode 4 Mei-sees-Mana revelation, Episode 7 ordinary Mana, Episode 9 secrecy ethics  
**Relation:** DIRECT_RETELLING SEED + MAJOR ADDED_SCENE_OR_CONTEXT + GAME_ORIGINAL_MEI/MANA ARC

### Expansion
- Mei's ability to see Mana becomes an extended ordinary friendship rather than a one-scene supernatural confirmation.
- Mana finally has another girl with whom she can talk, joke and play.
- Board/card-game scenes emphasize the awkward material logistics of friendship with an incorporeal person.
- Mei seriously considers telling Kotono.
- Mana gives a more explicit early justification for secrecy: she fears becoming "older sister" again rather than remaining Kotono's unreachable professional goal.
- Mei chooses an idol aspiration partly through seeing both ordinary Mana and stage-Mana.

### Ethical significance
The game makes Mana's paternalistic logic substantially more explicit, strengthening the later V2 critique that love and autonomy do not automatically coincide.

---

## 12. `Dear My Sister`
**Source:** `st-original-cmn-01-02-31`–`39`  
**Nearest anime anchor:** Episodes 5 and 7  
**Relation:** DIRECT_RETELLING THEMATIC SEED + GAME_ORIGINAL EXPANSION

### Expansion
- The game supplies interior narration for **both sisters**.
- Chisa's dependence is paired with Saki's dependence on being the responsible older sister.
- The problem is therefore bilateral: Chisa must become capable of acting without Saki, while Saki must relinquish the identity reward of always being needed.
- Sumire functions as a younger but more experienced idol model for Chisa.
- The endpoint is not separation but horizontalized sisterhood: two people able to run beside one another.

### V2 consequence
This is much stronger evidence for Saki than the anime alone provides and should be routed to both sisters' Phase-2 longitudinal ledgers.

---

## 13. `Sunlight`
**Source:** `st-original-cmn-01-02-40`–`45`  
**Nearest anime anchor:** Episodes 7–8  
**Relation:** DIRECT_RETELLING + EXPANDED_MAKINO_POV

### Expansion
- Grand Prix anxiety and elite-rival context receive more connective material.
- Sakura's hospital follow-up is more heavily filtered through Makino's memory of Mana's death.
- Ghost Mana independently feels warmth around the hospital, adding a supernatural clue outside Sakura's own narration.
- Makino asks the donor question and receives the same institutional confidentiality barrier.
- Makino explicitly narrates the medical/privacy problem and what he has told the physician.

### Guardrail
The doctor still does **not** publicly provide donor identity here. The game has already front-loaded the transplant fact, but donor attribution remains inferential at this stage.

---

## 14. `Successor of Miracle`
**Source:** `st-original-cmn-01-03-01`–`05`  
**Nearest anime anchor:** Episode 8  
**Relation:** DIRECT_RETELLING + EXPANDED_INTERIORITY

### Expansion
- The `後継者 / successor` discourse becomes more explicit and sustained.
- Sakura researches Mana and tries changing her own singing because resemblance feels presumptuous and potentially painful to Kotono.
- Kotono verbalizes the empirical failure of her attempt to reproduce Mana.
- Kotono's wish that Sakura carry Mana's lost song is tied more fully to the last pre-death sister conflict.
- Makino already thinks of Sakura's heart as Mana's and agonizes over whether silence is sustainable, although the source basis remains inferential rather than a clean doctor disclosure.

### Reframing
The game gives the successor problem more explanatory prose; the anime gives it stronger visual/aural identity pressure.

---

## 15. `Sorrows of Orpheus`
**Source:** `st-original-cmn-01-03-06`–`10`  
**Nearest anime anchor:** Episode 8  
**Relation:** DIRECT_RETELLING + EXPANDED_GROUP RESPONSE

### Expansion
- Kotono's loss of purpose is distributed through more ordinary group interaction.
- The other Tsuki members articulate why they want **Kotono's** voice/person, not merely an adequate center.
- Makino's internal narration makes the distinction between "fixing" Kotono and allowing the group to answer her more explicit.

### V2 result
The anime's `私たちの頂上` finding survives; the game gives more social scaffolding around how that plural grammar becomes possible.

---

## 16. `Cherry,Worry`
**Source:** `st-original-cmn-01-03-11`–`15`  
**Nearest anime anchor:** Episodes 8–10  
**Relation:** DIRECT_RETELLING + ADDED_COMPETITIVE CONTEXT

### Expansion
- Sakura's "Mana's return" public label is tested through additional rivals and audience commentary.
- She articulates the wish to find `自分達の歌`, linking her individuation to SUNNY PEACE's group individuation earlier and more continuously.
- Rui directly tests Sakura's relationship to the Mana label.
- The game gives Makino more internal concern about whether media demand is pulling Sakura back toward inherited identity.

### Reframing
The crisis becomes not only "Who is Sakura?" but "What is SUNNY PEACE if its most marketable feature is Sakura's resemblance to someone else?"

---

## 17. `Beat Meets`
**Source:** `st-original-cmn-01-03-16`–`20`  
**Nearest anime anchor:** Episode 9  
**Relation:** DIRECT_RETELLING + EXPANDED_MAKINO_ETHICAL CRISIS

### Expansion
- Makino's fear that Sakura's will may be overwritten by Mana becomes explicit internal narration.
- He searches/reads the public transplant discourse while worrying about what the heart means.
- Mana's simultaneous physical weakness is more directly observed and theorized by Makino.
- The game gives him a sustained conflict between wanting Mana to remain and refusing to make Sakura perform Mana for that purpose.

### V2 significance
This is unusually strong manager-ethics evidence: Makino's anti-possession choice is not effortless virtue; the game lets us see the temptation and cost from inside him.

---

## 18. `Idoly Pride`
**Source:** `st-original-cmn-01-03-21`–`25`  
**Nearest anime anchor:** Episode 9  
**Relation:** DIRECT_RETELLING + EXPLICITATED_METAPHYSICS/ETHICS

### Expansion
- Mana's `私の歌は私だけのもの` anti-substitution position is preserved.
- Sakura's heart is explicitly incorporated into Sakura's personhood.
- Kotono's heartbeat-listening scene is preserved with more textual access to surrounding thought.
- Makino more openly theorizes that Sakura's increasing self-authorship is weakening whatever binds ghost Mana to the world.
- His desire to protect Sakura's artistic future is juxtaposed against knowledge that doing so may mean losing Mana.

### Guardrail
Makino's ghost-heart mechanism remains a character inference/model, not automatically a scientific rule of the setting.

---

## 19. `Still Live`
**Source:** `st-original-cmn-01-04-01`–`05`  
**Nearest anime anchor:** Episodes 9–11  
**Relation:** RETELLING RESEQUENCING + ADDED_SCENE_OR_CONTEXT

### Expansion / difference
- Sakura's inherited-song performance and Kotono's movement away from Mana are woven into a longer competition sequence.
- Tsuki's own stage follows with a moment where Kotono literally inserts `さよなら` outside the expected lyric, giving departure a textual rupture rather than only thematic implication.
- BanPro/Asakura/Rui reactions are integrated earlier into the bracket progression.
- SUNNY PEACE's search for a distributed new vocal identity is dramatized as members literally trying to create/songwrite together.
- Mana's fading becomes directly tied, in Makino's reasoning, to Sakura's new voice.
- Mei's concern about Kotono and Mana produces the explicit `最後の宿題` setup.

### V2 consequence
This block crosses several anime episode boundaries; it should not be forced into a single episode equivalence.

---

## 20. `on My Way`
**Source:** `st-original-cmn-01-04-06`–`10`  
**Nearest anime anchor:** Episode 11  
**Relation:** DIRECT_RETELLING CORE + EXPANDED_DIALOGUE/INTERIORITY

### Expansion
- The final Kotono/Mana conflict is reconstructed with fuller internal narration from Kotono.
- Makino explicitly argues that neither he nor Sakura has jurisdiction to decide the sisters' action for them.
- Rio gives Kotono a long account of entering idolhood initially for money, discovering idol power through Mana, and outsourcing self-recognition to surpassing Mana.
- Kotono reasons more explicitly about why Mana may have appeared for someone other than herself.
- Mana's pre-idol description of the person she likes gives Kotono a route to infer the Makino relationship.
- Kotono's one-way conversation includes internal subjective impressions of warmth/embrace despite not seeing Mana.

### V2 result
The anime's "approval is no longer necessary" reading is strengthened, while the game adds much stronger linguistic access to how Kotono reaches it.

---

## 21. `Glory Days`
**Source:** `st-original-cmn-01-04-11`–`15`  
**Nearest anime anchor:** Episodes 10–11, but with substantial resequencing  
**Relation:** RETELLING RESEQUENCING + EXPANDED_RIVAL CONTEXT + EXPANDED_MAKINO_POV

### Expansion
- SUNNY PEACE's new song is explicitly self-written in the game retelling.
- Mana discusses the professional meaning of a demanding instructor and Makino's growth.
- Rui's desire to surpass Mana, her father relation, and the relational support inside TRINITYAiLE are integrated into semifinal preparation.
- Hoshimi asks Mana/Makino to watch from the audience perspective.
- Makino frames himself simply as `彼女達のマネージャー`, emphasizing current responsibility over old legend.
- The semifinal results allow Rui and Rio to acknowledge the Hoshimi units directly.
- Mana disappears after witnessing the semifinals/self-authored performance state rather than waiting through the game final itself.

### Major cross-media difference
The anime lets Mana witness the two Hoshimi units' **final** performances. The game moves her decisive disappearance/farewell earlier, so the actual final is more completely a stage after Mana.

---

## 22. `Last Step`
**Source:** `st-original-cmn-01-04-16`–`20`  
**Nearest anime anchor:** Episode 12  
**Relation:** EXPANDED_MAKINO_POV + RETELLING RESEQUENCING

### Expansion
- A major flashback gives Makino's post-death grief in far more detail: gravesite, accident site, the unused final venue, and finally returning to the classroom where Mana first recruited him.
- The game explicitly identifies that classroom visit as the point at which ghost Mana first became perceptible to Makino.
- After the semifinals, Makino initially tries to prioritize his current idols over chasing Mana's voice, demonstrating his professional transformation.
- Mana's `本当の夢` is narrated as making Makino the manager of a top idol while still explicitly preserving her own desire to become top idol.
- Mana says the project through Sakura/Kotono was the remaining route by which that dream could be realized after her death.
- The romantic confession and `キスくらい` line occur **before the final**, after which Makino describes this as their last conversation.

### Reframing
Compared with the anime, the game is even more strongly a **Makino grief memoir** at this point. The final stage occurs only after this private relationship has already ended.

---

## 23. `Pray for you`
**Source:** `st-original-cmn-01-04-21`–`24`  
**Nearest anime anchor:** Episode 12  
**Relation:** RETELLING_CONTINUITY_VARIANT + EXPANDED_MAKINO_POV

### Shared core
- final-day ordinariness;
- Hoshimi remains socially one community despite unit rivalry;
- rivals/predecessors attend;
- the final becomes a statement about what the living generation now is;
- Makino recognizes that the decisive moment belongs to the idols rather than the manager.

### Material variant
The game final is constructed differently:

- SUNNY PEACE and Tsuki agree in advance to perform the **same ten-person final**;
- they ask the audience to decide which group is more deserving from that shared performance;
- the joint song is `サヨナラから始まる物語`;
- the encore is `First Step`;
- Makino explicitly narrates `First Step` as Mana's song being sung for Mana and the stage being offered to her;
- the game-Hoshimi text does not reproduce the anime's separate-unit performances → tie → joint winner-stage sequence.

### Interpretation
The two finales should remain distinct analytical objects.

**Anime:** differentiation first, non-singular tie, reunion after autonomy.  
**Game:** joint Hoshimi identity enters the decisive final itself, followed by explicit memorial return to the originating song.

This is the single clearest example in the Hoshimi corpus where "expansion" is an insufficient description.

---

# 7. What the game most strongly adds to Makino

Across the 23 blocks, five Makino dimensions become much more recoverable.

## 7.1 Pre-manager ordinary self

The game lets Makino remember being socially ordinary, comparatively peripheral, attracted to Mana but not initially close to her, and suspicious that her sudden attention might even be a prank.

Mana selects precisely that ordinariness as useful: he treats her more normally than boys who become awkward around the attractive popular girl.

This gives later Makino ethics a plausible origin. His professional value begins not with industry expertise but with **non-mythologizing perception**.

## 7.2 Vocation as acquired rather than innate

Makino expects the Hoshimi job may last only months.

He stays because:

- management becomes interesting;
- Mana's growth becomes worth witnessing;
- he acquires professional responsibility through doing rather than through prior dream.

The anime already established transformation-witnessing as a positive vocation. The game makes the biographical acquisition of that vocation much clearer.

## 7.3 Managerial fallibility

The game's Makino repeatedly:

- misjudges;
- overworks;
- becomes too protective;
- asks the wrong question;
- discovers that an idol understood the situation better than he did;
- distinguishes personal desire from professional recommendation.

This is important because it prevents "good manager" from collapsing into omniscient therapist.

## 7.4 Interior ethical cost

The Sakura/Mana heart arc is much harsher from Makino's first-person position.

He has reason to suspect:

> Sakura becoming more fully Sakura may cause Mana to disappear.

He therefore experiences the anti-substitution ethic as something that may personally cost him the person he loves.

That substantially strengthens the anime-native conclusion that good management requires refusing to preserve the first miracle by controlling the living performer.

## 7.5 The final limit of management

In `Pray for you`, Makino arrives at:

> **本当に大切な時、俺は見ていることしか出来ない**

At the truly decisive moment, he can only watch.

That line should become a major Phase-4 manager-ethics locator.

His mature authority is therefore paradoxical:

> he becomes a capable manager partly by learning where managerial authority must stop.

---

# 8. Character expansions the anime underdetermines

## Haruko
The game is indispensable for her as a working adult performer. Her musical-theatre offer and finite-idol-life reflection make age, career transition, self-confidence, and professional choice central rather than peripheral.

## Rei
The game establishes that dance precedes idolhood as vocation. Her discipline should therefore not be read as generic perfectionism; it originates in the attempt to preserve dance as serious life work and only later broadens into idol identity.

## Nagisa
The game protects her from being reduced to "Kotono's emotionally intelligent childhood friend." She has to discover what makes *Nagisa* legible as an idol.

## Suzu
The anime makes her theatricality easy to enjoy; the game asks whether it survives loss of money, parental backing and status insulation. This is fundamental class/family evidence.

## Mei
The game makes her perhaps Mana's most ordinary post-death friend. Their joking, games, secrecy conflict, and Mei's decision to become an idol like the Mana she now knows in multiple registers deepen both characters.

## Saki and Chisa
The game proves their individuation is bilateral. Saki is not merely the healthy helper whom Chisa must outgrow; Saki has also organized herself around being needed.

## Shizuku
Her quietness becomes an explicit crisis of idol ontology: she adores idols yet fears that her temperament prevents her from becoming the kind of luminous person she admires.

---

# 9. Information-order ledger

These differences must remain explicit in later synthesis.

| Fact / issue | Anime revelation | Game-Hoshimi handling | Rule |
|---|---|---|---|
| Sakura has surgical history | E04 scar | early Hoshimi | do not back-project |
| surgery is specifically cardiac | E07 | early Hoshimi framing | do not back-project |
| Sakura received transplant | E08 | explicit in `Shine Purity` | major order shift |
| donor identity is Mana | E09 narrative confirmation | Makino progressively treats it as true after confidentiality scene; certainty is distributed differently | keep source-specific epistemology |
| Rui is Asakura's daughter | E10 concentrated reveal | disclosed much earlier in `Proud Lady` | chronology shift |
| Mei/Mana ordinary friendship | E07 movie + prior E04 sight | extended early arc in `Resolution` | game expansion |
| Mana secrecy rationale | E09/E11 | explicit earlier through Mei | game makes motive explicit |
| Mana final romantic confession | E12 near disappearance during final-day architecture | before final, after semifinal sequence | chronology variant |
| Mana witnesses Hoshimi final unit performances | yes | no; decisive farewell occurs before final | continuity variant |
| Hoshimi final structure | separate unit performances → tie → joint stage | planned ten-person final → `First Step` encore | continuity variant |

---

# 10. Anime-only evidence that the game must not overwrite

Even where dialogue is similar, the anime remains uniquely authoritative for several high-value claims:

- Kotono's room/body/negative-space progression;
- the color and stage-world distinction between SUNNY PEACE and Tsuki no Tempest;
- Sakura's voice performance before/after the Mana-like register;
- the audible heartbeat and sound-field construction in Episode 9;
- Rui's controlled vocal register breaking into post-performance crying;
- the camera's handling of ghost Mana during Sakura-heart conversations;
- how physical proximity changes Kotono's grief grammar;
- the performance editing and audience orientation of Episodes 6, 10, 11 and 12;
- the anime finale's separate performances and tie.

The game's explanatory prose often answers **why** a character thinks something. The anime frequently supplies meaning through **how the body, voice, image and time behave**.

Neither mode should subsume the other.

---

# 11. Priority consequences for Phase 1

## All 23 Hoshimi blocks remain CORE

No Hoshimi block should be demoted as redundant.

However their Phase-2 routing differs.

### Highest-priority foundational/character-routing blocks

- `Shine Purity` — Makino/Mana, Sakura/Kotono beginning, medical order shift.
- `The Sun, Moon and Stars` — Makino overwork/collapse; Rei recruitment; debut architecture.
- `to Trust One` — Rei vocational foundation.
- `Make up her Mind` — Haruko adult-career foundation.
- `Proud Lady` — Suzu family/class foundation; early Rui information.
- `Resolution` — Mei/Mana friendship and secrecy ethics.
- `Dear My Sister` — bilateral Saki/Chisa model.
- `Beat Meets` + `Idoly Pride` — Makino/Sakura/Mana personhood and management ethics.
- `on My Way` — Kotono/Rio/Mana closure and self-authorship.
- `Last Step` — Makino/Mana grief/romance/vocation.
- `Pray for you` — cross-media finale divergence.

### Formal-retrospective routing

Blocks corresponding to major performances should be retained for Phase 5 comparison, but their prose cannot substitute for anime audiovisual inspection.

---

# 12. Revision to the Phase-1 route

This audit completes the previously inserted **Hoshimi anime↔game expansion tranche**.

The post-anime governing sequence can now proceed without treating the game manager as a separate protagonist and without treating the anime retelling as redundant.

The next Phase-1B semantic tranche is:

1. `tokyo_001_new_wind` → `tokyo_014_with_beyond_the_miracle`;
2. then `big4_001_dark_of_the_moon` → `big4_014_epilogue`;
3. then `stellar_001_to_soar_high` → `stellar_011_all_my_youth`;
4. remaining unit-origin bundles;
5. independent re-ranking of the 60 event bundles;
6. bonds, specials, cards/messages according to contradiction and longitudinal-value signals.

---

# 13. Phase-2 claims generated by this audit

The audit does not yet write definitive character syntheses, but it creates several ledger requirements.

## Makino Player-Branch Canon Ledger
Must distinguish fixed Makino characterization from selectable authored expression.

## Makino managerial apprenticeship ledger
Track:
- ordinary perception → assistant role → Mana witness → grief → producer of groups → willingness to step back.

## Anime/game information-order ledger
Prevent later game facts from rewriting the anime's prospective reveal structure.

## Cross-media continuity-variant ledger
At minimum include:
- timing of Rui/Asakura reveal;
- Mana disappearance/farewell placement;
- Grand Prix final structure;
- `First Step` finale function;
- tie versus no reproduced tie.

## Secondary-character escalation ledger
Haruko, Rei, Nagisa, Suzu, Mei, Saki, Chisa and Shizuku all require game main-story evidence to be treated as central rather than texture.

---

# 14. Final Phase-1B judgment

The Hoshimi game story should be understood as:

> **a Makino-centered, character-expansive retelling of the anime-era narrative that preserves many major dramatic propositions while substantially changing information order, adding several full character arcs, and diverging materially in the architecture of the ending.**

Its most important contribution is not "more dialogue."

It changes what kinds of knowledge are available:

- the anime gives us bodies, voices, color, time, silence and stage form;
- the game gives us Makino's interiority, longer character-development bridges, explicit professional reasoning, and alternate/reordered narrative architecture.

The correct V2 synthesis is therefore neither:

> anime governs, game is redundant

nor:

> game is more detailed, therefore game supersedes anime.

It is:

> **the anime and game are mutually illuminating but non-identical witnesses to the Hoshimi story. Their convergences strengthen claims; their information-order differences must remain historically visible; and their genuine continuity variants—especially the finale—must be analyzed rather than harmonized away.**

