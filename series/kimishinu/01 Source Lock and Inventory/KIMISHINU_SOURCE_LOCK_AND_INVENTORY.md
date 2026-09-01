\---  
series: KIMISHINU  
artifact\_type: source\_lock  
scope: V01-V09 \+ supplements  
generation: V1  
status: canonical  
source\_boundary: "Japanese digital manga EPUBs currently published through Volume 9"  
supersedes: null  
superseded\_by: null  
do\_not\_use\_as\_current\_authority: false  
\---

\# KIMISHINU\_SOURCE\_LOCK\_AND\_INVENTORY.md

\#\# Canonical source boundary

The initial KimiShinu deep-reading corpus is locked to the Japanese digital manga objects currently present in the source folder:

\- KimiShinu \- Volume 01.epub  
\- KimiShinu \- Volume 02.epub  
\- KimiShinu \- Volume 03.epub  
\- KimiShinu \- Volume 04.epub  
\- KimiShinu \- Volume 05.epub  
\- KimiShinu \- Volume 06.epub  
\- KimiShinu \- Volume 07.epub  
\- KimiShinu \- Volume 08.epub  
\- KimiShinu \- Volume 09.epub  
\- KimiShinu \- Volume 05 \- Special Booklet \- After the Quarrel.epub  
\- KimiShinu \- Side Stories.epub

Primary-source folder ID: \`1smT9-Bbr1mNKaCxBM-fvYitaJxoTkM50\`.

\#\# Audit state

The source manifest dated 2026-08-26 reports:  
\- 11 EPUB files;  
\- main series complete through V09;  
\- 2 supplemental books;  
\- 0 exact duplicate groups;  
\- ZIP CRC checks passed: 11/11;  
\- EPUB container checks passed: 11/11;  
\- EPUB packaging conformance: 11/11;  
\- all files image-based fixed-layout EPUBs.

Representative direct inspection of early and late volumes confirmed original Japanese-language manga pages with legible dialogue, narration, furigana, SFX, and intact page composition. The corpus is therefore suitable for page-first Japanese deep reading without routine OCR.

\#\# Provenance rule

Acquisition provenance and publication identity are separate claims. The manifest preserves original filenames and hashes. Some earlier volumes' filenames indicate acquisition through Anna's Archive; V09 was user-purchased and passed through Calibre before normalization. These facts should be retained as provenance but must not be confused with a claim of storefront-byte identity.

For literary analysis, the authoritative object is the audited Japanese page content. If a future discrepancy between editions is discovered, open an edition audit rather than silently replacing evidence.

\#\# Main-series inventory

| Scope | Images | SHA-256 |  
|---|---:|---|  
| V01 | 171 | 21b2e914341d33480ce4a6867b1a18db8cfd617b258ea13178355ac55b96df94 |  
| V02 | 171 | b56d4f28564c789ff0ca78047982b9c6068f04be458c2a712ffff094a738e11c |  
| V03 | 171 | 5c499a13849ccad1e29bc21d31ca08434df93288c90fef8a9b49ef36f5e6870a |  
| V04 | 171 | a91fcf1c5d8e2ead200d77c9ae599318b0e4fa435e63af10fdcc50591628bca8 |  
| V05 | 171 | f47174b93e3a0956eaa3dba265ea40d014a070ce6b4cf45111c08bfd34310c6a |  
| V06 | 155 | d9f7b48ea59ae1b408c40d36376492d5cd737a8c3d1eb26369cb1b27e70e48fd |  
| V07 | 187 | 1f397f0edde60e8c48d17c3b0df89fc5fa15be367abcc226c1f0422d613e4bf8 |  
| V08 | 155 | d919a55f384d336a0ab8aafbf71e49876a2aef9febc3dc5704ec082bd78b9154 |  
| V09 | 155 | 2ed64ead82890e4cf9cebf648d00856465abed67d86051af254d019f319dde44 |

V09 embedded title: \`きみが死ぬまで恋をしたい: 9【イラスト特典付】\`.

\#\# Supplemental inventory

\#\#\# V05 special booklet  
Normalized filename: \`KimiShinu \- Volume 05 \- Special Booklet \- After the Quarrel.epub\`  
Japanese title: \`きみが死ぬまで恋をしたい：5 「けんかのあとは」 特装版小冊子電子版\`  
Images: 21  
SHA-256: \`ddb07fbf19b48c3dbec3a3af1d1e050bc39288c170744e9e945b9675686b3c55\`

\#\#\# Side Stories  
Normalized filename: \`KimiShinu \- Side Stories.epub\`  
Japanese title: \`きみが死ぬまで恋をしたい side stories 【イラスト特典付】\`  
Images: 153  
SHA-256: \`ae2347cea7116917e00d9daea97b7b3809a8bdb68de91c0170bb16eec6a8330c\`

\#\# Evidence classes

Use three source classes:  
1\. MAINLINE — numbered tankobon narrative V01-V09.  
2\. SUPPLEMENTAL\_NARRATIVE — V05 booklet and Side Stories where they contain narrative material.  
3\. PARATEXT — covers, bonus illustrations, advertisements, contents pages, publication furniture, and other non-narrative material.

A supplemental source may strengthen character or relationship modeling without being silently treated as part of the numbered mainline chronology.

\#\# Prospective opening order

1\. Read V01-V05 sequentially.  
2\. After completing and freezing V05, inspect the V05 booklet's chronology; read it then unless internal evidence requires a more precise placement.  
3\. Continue V06-V09 sequentially.  
4\. Inspect Side Stories metadata/contents before opening narrative pages; place each story chronologically where possible, but do not let later-published supplemental knowledge contaminate already-frozen mainline readings.

\#\# Temporary extraction policy

EPUBs may be downloaded and unpacked temporarily for analysis. Preserve native image order and navigation structure while reading. Do not permanently duplicate the full manga into the analytical root. Temporary extracted pages may be discarded after the corresponding deep reading and evidence locators are stable.

\#\# Source-change protocol

If V10 or later material is added:  
\- audit integrity and language first;  
\- append its hash and structural metadata here;  
\- update CURRENT\_STATE\_AND\_CORPUS\_MAP.md;  
\- do not modify completed V01-V09 readings merely because the publication boundary advanced;  
\- treat the newly added volume as the next prospective source boundary.

\#\# Lock status

Current lock: GREEN.  
Current complete numbered boundary: V09.  
Deep reading may begin at V01.  
