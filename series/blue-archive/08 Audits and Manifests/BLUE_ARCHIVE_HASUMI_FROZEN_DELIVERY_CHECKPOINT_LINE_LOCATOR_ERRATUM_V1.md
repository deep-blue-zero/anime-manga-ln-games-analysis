# Hasumi frozen delivery: distinguish Event819 checkpoint lines from episodes

The four frozen Hasumi outputs remain unchanged. ROOT correctly identified ambiguous mixed locator syntax in saved lines108 and110.

E19 binds the 152-line accepted Event819 contextual checkpoint, SHA256 f985eff72b00b1532d668f6e60534a05351d4cb26dbfff17d187da3e501459e2, blob491b6cab49552fdf4039f496b05c17cc91180b17. Its event has eleven episode objects. The numbers118 and120 denote **checkpoint physical lines**, not episodes.

Required canonical-derivative corrections:

- Saved body108: replace `[H01:13003:015; E19:006/009/118]` with `[H01:13003:015; E19:006/009; E19:checkpoint:L118]`. The lexical comparison is directly developed at checkpoint118: 救護, 正義 and the distinction between 回収 and 奪う. The complete episode006/009 arguments remain at checkpoint91–92/99–100.
- Saved body110: replace `E19:120` with `E19:checkpoint:L120`. This line explicitly preserves nonlexical replies, narration, inward/response seams, choices, unit ordering and unreceived performed voice.
- HA25: apply the body108 change to the duplicated saved paragraph; change its E19 argument locator `006/009/118` to `episodes006/009; checkpoint physical L118`.
- HA26: apply the body110 change to the duplicated saved paragraph; change its E19 argument locator `120` to `checkpoint physical L120`.

These are locator clarifications. The literary propositions, original producer scope, all14OPEN limits and source bytes are unchanged. The complete checkpoint was personally received419d02/153af0, including lines118/120. This supplemental erratum is a new C-only file; ROOT owns derivative installation and exact verification, and the earlier frozen group-locator erratum remains separately required.
