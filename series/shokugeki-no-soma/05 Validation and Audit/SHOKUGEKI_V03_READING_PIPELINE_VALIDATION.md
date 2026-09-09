---
series: SHOKUGEKI
artifact_type: reading_pipeline_validation
scope: V03_REPRESENTATIVE_SAMPLE
generation: V2
status: canonical
source_boundary: Original Japanese manga Volume 3; representative validation sample only
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
created: 2026-09-06
source_sha256: 16fceceb8c958a4b5c7b575573d7f3852e05e55811f9ed26120c72fdea7c6fed
---

# SHOKUGEKI_V03_READING_PIPELINE_VALIDATION

## 1. Purpose and gate result

This artifact validates the manga-reading pipeline required before the V2 sequential run advances beyond Volume 2. It tests Japanese OCR as a supporting retrieval channel and direct multimodal inspection of the original manga pages as the visual authority.

**Gate result: PASS.** The current Codex environment can inspect the original extracted page images directly at page resolution. OCR is useful for candidate discovery and rough transcription, but it is not reliable enough to determine speaker identity, reading order, text category, or fine visual meaning without page inspection.

The extracted pages, OCR output, navigation contact sheets, and close-reading crops remain outside Git under the contained analytical workspace. No source CBZ was modified.

## 2. Source identity and sample boundary

- source file: `[附田祐斗×佐伯俊] 食戟のソーマ 第03巻.cbz`
- canonical Drive ID: `1YPXp7kBXvwLgrGAIdQHgemGLq0bAH303`
- SHA-256: `16fceceb8c958a4b5c7b575573d7f3852e05e55811f9ed26120c72fdea7c6fed`
- image members: 204 (`03-000` through `03-203`)
- archive extraction / CRC traversal: PASS
- ordinary page class: approximately 1260-1274 x 2000 px
- sample pages: `03-031`, `03-067`, `03-081`, `03-100`, `03-122`, `03-124`, `03-127`, `03-144`, and `03-146`

The sample spans multi-character dialogue, tailed and untailed balloons, off-panel continuation, internal monologue, narration, visually dense pages, small/furigana-bearing text, stylized sound effects, reaction shots, a silent reaction montage, and an unconventional negative-space composition.

## 3. OCR behavior and normalization rule

The Japanese Windows OCR engine recognized a substantial share of ordinary printed text, but it frequently:

- inserted spaces between Japanese characters;
- interleaved furigana with base text;
- scrambled the order of columns and balloons;
- confused punctuation and sound effects with dialogue;
- dropped nearly all text from sparse or unconventional pages;
- produced unusable fragments from the silent reaction page;
- and could not identify speaker, balloon ownership, or text category.

Therefore the retained raw OCR is never silently promoted to quotation. Corrected transcription below is admitted only after direct page inspection. Text that remains unclear is marked rather than reconstructed from plausibility.

## 4. Representative-page validation

### 4.1 `V03 / Ch16 / 03-031` — dense multi-character briefing

**Raw OCR excerpt:** `ま だ 何 の 説 明 も 受 け て な い ... 乾 シ ェ フ ... 私 が 出 す 課 題 は ... こ こ に あ る 食 材 を 使 っ て 日 本 料 理 で メ イ ン と な る 一 品 を 作 る 事 で す`

**Page-corrected text:**

- student: `あの…乾シェフ？ まだ何の説明も受けてないんですが…`
- Inui Hinako: `ああ…そうでしたか？`
- Inui: `では説明をしなくてはですね！`
- Inui: `私が出す課題は…ここにある食材を使って 日本料理でメインとなる一品を作る事です！`
- students: `ここに…って？ 食材なんてどこにも`
- Inui: `ありますよー…？ 清流のゆく雄大な自然 すばらしい素材の宝庫です`

**Reading order:** top row right-to-left, then the narrow right-middle panel, the two-part landscape panel, and the bottom row right-to-left. OCR flattened all of these into one sequence.

**Attribution:** Inui's close-up and continued gesturing establish her explanation as `explicit_visual` or `strong_contextual` depending on the balloon. The first student's identity is not recoverable from the page with confidence; retain `unknown student / probable group representative` rather than assign the line to a named character.

**Visual evidence unavailable from OCR:** Inui's relaxed smile and seated posture make the severe wilderness assignment initially look socially gentle; the students' bottom-row shock panels supply the tonal reversal.

### 4.2 `V03 / Ch18 / 03-067` — internal reasoning and reveal

**Raw OCR excerpt:** `俺 た ち が 作 る 品 の 鍵 に な る 食 材 は ... 柵 の 中 の エ リ ア な ら な ん で も ... こ い つ だ っ`

**Page-corrected text:**

- Inui: `はい`
- Inui: `柵の中のエリアならなんでもー`
- Soma, internal reasoning: `俺たちが作る品の鍵になる食材は`
- Soma: `こいつだっ…!!`
- Megumi: `え…!!`
- Inui / nearby observer: `そ それはー!?`

**Text-category correction:** The black, untailed boxes beside Soma's narrowed-eye close-up are internal reasoning, not spoken dialogue. OCR cannot make this distinction.

**Reading order:** right-top permission exchange, center close-up/internal boxes, then the large lower reveal and left-edge reaction insets.

**Attribution confidence:** Soma's culminating reveal is `explicit_visual`; the internal boxes are `strong_contextual`; the exact owner of the partially cropped `そ それはー!?` is not certain enough to force and remains `probable`.

**Visual evidence unavailable from OCR:** the tightening from eye close-up to hand/reveal panel marks a shift from open search to decisive improvisation.

### 4.3 `V03 / Ch18 / 03-081` — food texture and reaction

**Raw OCR excerpt:** OCR recovers fragments including `柿 の 種 自 体 の 味 の お か げ`, `衣 に 守 ら れ`, and `岩 魚 の 旨 味 が ... 凝 縮` but scrambles order and furigana.

**Page-corrected core text:**

- Inui: `なんて素晴らしい歯ごたえでしょう！`
- Inui: `それでいて中の身はほくほく…`
- Inui: `衣に守られ 岩魚の旨味がしっかり凝縮されています！`
- Inui: `柿の種自体の味のおかげで 衣からもしっかりとした美味しさが感じられます`

**Attribution:** `explicit_visual`; Inui is shown biting, chewing, and then explaining.

**Visual evidence unavailable from OCR:** the page alternates extreme mouth/food close-up, chewing sound effects, bodily reaction, and explanatory portrait. Texture is staged as rhythm and impact before it becomes verbal description.

### 4.4 `V03 / Ch19 / 03-100` — dense service escalation

**Raw OCR excerpt:** `その人達は誰ですか ... 近くの施設で合宿中の上腕大学ボディービル部 ... 彼らの夕食を完成させた者から自由時間 ... これを各自50食分作ってもらう`

**Page-corrected core text:**

- student: `その人達は誰ですか!?`
- instructor: `近くの施設で合宿中の上腕大学ボディービル部の皆さんだ`
- instructor: `続いてアメフト部・レスリング部もここへ来ることになっている`
- instructor: `彼らの夕食を完成させた者から自由時間とする`
- instructor: `これを各自50食分作ってもらう`
- menu caption: `本日のメニュー「牛肉ステーキ御膳」`

**Reading order:** the bodybuilder reveal occupies the top after the right-side instructor balloon; the large `その人達は誰ですか!?` reaction overlays the group; the assignment then descends into the meal panel and lower reaction row.

**Attribution:** instructor lines are `explicit_visual` or `strong_contextual`; the shouted question is a collective/student reaction and should not be assigned to a named face from OCR proximity.

**Visual evidence unavailable from OCR:** the muscular guests fill and compress the upper panel, turning a numerical assignment into bodily intimidation before the number `50` lands.

### 4.5 `V03 / Ch20 / 03-122` — narration plus exhausted ensemble

**Raw OCR:** `へ 2 ル`.

**Page-corrected text:**

- narration: `数分後…`
- background student: `疲れが一気に来たって感じね`
- background student: `まぁ消灯時刻まで転がしとくか`
- Ryoko: `恵はまだ眠くないの？ 珍しいわね いつもなら早々におねむなのに`
- Megumi: `うん…おかしいね 疲れてるのに目が冴えてるんだ…`

**Text-category correction:** `数分後…` is a rectangular temporal narration box. The remaining lines are spoken group dialogue. OCR misses the narrative function entirely.

**Visual evidence unavailable from OCR:** the card-strewn floor and sprawled bodies establish collective exhaustion; Megumi's upright posture and open eyes create the exception before she verbalizes it.

### 4.6 `V03 / Ch20 / 03-124` — encouragement, interiority, and aspiration

**Raw OCR excerpt:** OCR recovers most lexical content but merges the speakers and places `もっと料理が上手になりたいよ` before `もっと皆と一緒に居たい`.

**Page-corrected core text:**

- Megumi: `指示を出してくれた創真くんのおかげで…私は何も偉くねぇんだけど…`
- Soma: `んな事ねーよ 田所が素材集めてくれなきゃ あの品は出来なかったし 調理もバッチリこなしてくれたじゃねーか`
- Ryoko: `そうよ 恵はやればできる子だもの もっと自信もって ね！`
- Megumi, internal: `私…頑張るね…！`
- Megumi, internal: `もっと皆と一緒に居たい もっと料理が上手になりたいよ`

**Text-category correction:** the last three aspirations occupy open white/softly patterned space without ordinary dialogue balloons and are paired with Megumi's inward posture. They are internal thought, not speech to the room.

**Attribution confidence:** the spoken turns are `explicit_visual`; Megumi's final interiority is `strong_contextual` from page convention, pose, and sequence.

**Visual evidence unavailable from OCR:** Megumi shrinks into a small isolated figure while the white field expands. The composition converts encouragement into a private decision and makes belonging precede technical ambition.

### 4.7 `V03 / Ch20 / 03-127` — untailed judgment in negative space

**Raw OCR:** `退 学 だ`.

**Page-corrected text:** Shinomiya Kojiro: `退学だ`.

**Attribution:** `strong_contextual`, not tail-based. The balloon has no usable tail. Shinomiya sits above Megumi after inspecting her dish; she faces him from below. The surrounding sequence establishes that he is the evaluator delivering the result.

**Reading order:** one composed vertical unit rather than multiple independent panels.

**Visual evidence unavailable from OCR:** extreme white space, scale disparity, and vertical separation turn the verdict into institutional distance. Shinomiya is elevated and composed; Megumi is small, back-turned, and shadowed beneath him.

### 4.8 `V03 / Ch21 / 03-144` — silent reaction montage

**Raw OCR:** unusable noise only.

**Direct observation:** no narrative dialogue is present. The page cuts from Megumi reflected inside Soma's eye, to Shinomiya's widened eye, to a low insect/ground image and an extreme ear/profile fragment.

**Reading order:** top to bottom. The inset at the lower right is read with the middle reaction panel before the final low environmental fragment.

**Visual evidence unavailable from OCR:** reciprocal looking becomes the event. Soma registers Megumi's distress; Shinomiya registers Soma's intervention; the low natural fragment suspends speech and stretches the instant before escalation. Claiming “nothing happens” because OCR finds no text would erase the page's principal narrative work.

### 4.9 `V03 / Ch21 / 03-146` — visually explicit challenge

**Raw OCR:** `食 戟 で あ ん た を 、 負 か し た ら`.

**Page-corrected text:** Soma: `食戟であんたを負かしたら`

**Attribution:** `explicit_visual`; Soma fills the page, speaks directly toward Shinomiya, and the balloon occupies his foreground.

**Visual evidence unavailable from OCR:** Soma's enlarged foreshortened hand and nearly full-page face convert a procedural proposal into direct embodied defiance. The page is not merely informational dialogue.

## 5. Pipeline operating rules established by the sample

1. Use OCR for retrieval, rough transcription, candidate passage discovery, and deterministic page indexing.
2. Inspect every admitted quotation against the original page; preserve uncertain text instead of normalizing it silently.
3. Determine speaker ownership from tails, panel topology, mouth state, pose, gaze, conversational turn, and surrounding-page continuity.
4. Use `explicit_visual`, `strong_contextual`, `probable`, `ambiguous`, or `unknown` internally; do not promote the last three to certainty for analytical convenience.
5. Classify narration, internal monologue, spoken dialogue, signs, captions, and sound effects separately.
6. Resolve Japanese manga reading order from the page, not OCR order.
7. Treat contact sheets as navigation only; inspect original pages for fine claims.
8. Preserve silent panels and visual transitions as evidence.
9. Escalate an analytically load-bearing ambiguous attribution to surrounding-page review; if ambiguity remains, state it in the analytical artifact.
10. Keep raw pages and derived OCR/contact-sheet/crop artifacts outside Git.

## 6. Gate conclusion

The environment supports the required visual-primary-source workflow. The V03 full reading may proceed with OCR as a subordinate channel and original-page inspection as controlling evidence.

This validation does not itself establish Volume 3's literary thesis, cumulative character state, prediction adjudication, or V1-to-V2 transitions. Those responsibilities belong to the complete `SHOKUGEKI_V03_DEEP_READING.md` transaction after the whole volume has been read.
