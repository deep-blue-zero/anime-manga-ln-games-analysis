# Azur Lane Audio Source Inventory

## Authority and packaging

- Preferred source: original/current JP client bytes (`com.YoStarJP.AzurLane`) imported and updated with `nobbyfix/AzurLane-AssetDownloader` `4.7.1` at `0ccb1924c11d06888fa4d0f59a708586139234fe`.
- JP CDN documented by the tool: `https://blhxstatic.yo-star.com`.
- Packaging: client asset-bundle paths preserved under `ClientAssets/JP`, with version and difflog metadata; the pipeline does not assume a codec or container before inspection.
- Current acquisition state: `ACQUIRED`; catalog state: `RESOLVED`; post-download integrity: `PASS`.
- Client versions: `{'CV': '1243', 'AZL': '9.3.386'}`. Catalog: **6609** stream records from **4694** source files; all target technical probes passed.
- Identified format: CRI UTF/ACB containers with CRI HCA subsongs, parsed read-only with `vgmstream` r2083. Original bytes are not re-encoded.
- Primary Sources global bundle root: Drive `1gH4x8twCMAlDOlwZZ15eehyKNcMRIjZZ`; publication manifest `1TFT1bkGIl6_QGsQrUjwDIWDPH60WRq7U`. Drive readback covers all 344 bundles; the 33 newly ledgered bundles were SHA-256 verified.
- Community validation: the EN-only Fernando2603 dataset was consulted for voice-key completeness only and was not used as a JP source.

## Catalog ingestion contract

The augmentation CLI accepts JSON/JSONL asset records with locale, character group or skin ID, source-relative path, original bundle/catalog identity, voice/resource key, optional exact text record ID, client/catalog version, and acquisition method. Source files are copied once by SHA-256, technically probed without re-encoding where possible, and mapped with explicit confidence.

Current batch: **344** globally unique original bundles archived (**344** per-character bundle references) and **1630** text slots mapped. Every unresolved text slot remains distinct from `TEXT_UNVOICED`.
