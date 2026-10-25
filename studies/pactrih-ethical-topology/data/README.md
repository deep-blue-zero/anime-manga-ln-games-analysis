# Data

[pactrih_scores.csv](pactrih_scores.csv) is the canonical numerical source: the unchanged v12 snapshot of 100 subjects (85 Character, 7 Faction, 8 Historical Agent).

The exact schema is `Character,P,A,C,T,R,I,H,Type,Humane Regard,Moral Structure,Unit`. `Type` is the supplied ethical description; `Unit` distinguishes the analysis unit. Every axis is an integer in 0..10; Humane Regard=(P+A)/2 and Moral Structure=(C+T)/2. Preserve identity, order, descriptions, punctuation, Unicode, and unit labels.

The source CSV uses a UTF-8 BOM and CRLF, prohibited by the live repository text rules. The Git artifact removes the BOM and converts CRLF to LF without changing any other bytes. Restoring those encoding bytes reproduces the exact supplied source SHA-256; validation checks both hashes. Source and committed byte lengths, versions, and SHA-256 are in the [manifest](../audits/source_manifest.json). Validate with `python studies/pactrih-ethical-topology/scripts/validate_scores.py` from the repository root. A numerical change or addition requires the [reviewed update procedure](../scripts/README.md); editing only the CSV leaves the atlas stale.
