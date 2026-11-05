# Scripts

[validate_scores.py](validate_scores.py) adapts the handoff's read-only validator to stable Git paths and adds independent frozen-source pins. It never writes scores, an atlas, or a manifest. Python 3.10+ and Node.js on PATH are required; no third-party Python package is needed. Run from the repository root:

```sh
python studies/pactrih-ethical-topology/scripts/validate_scores.py
python -m unittest discover -s studies/pactrih-ethical-topology/scripts/tests -p 'test_*.py'
```

The first command checks committed hashes, reversal of the encoding-only CSV conversion against the original source hash, and exact embedding parity, formulas, finite PCA values, cluster ranges, standalone resources, and embedded JavaScript syntax. The tests deliberately corrupt scores, descriptions, row order/counts, units, formulas, PCA/cluster metadata, encoding, and JavaScript to exercise failure paths. These commands are explicit study preflight obligations; the global audit currently discovers only `tools/tests`.

## Reviewed update procedure

1. Start from current main and the continuing `studies/pactrih-ethical-topology` branch under the live repository checklist. Preserve the adopted baseline in Git history. Obtain authorized evidence-backed additions or corrections; retain unaffected records verbatim. Never reconstruct scores from the methodological handoff.
2. Update the CSV as the numerical source and recompute only the documented ethics-map formulas. The validator deliberately rejects a changed count, byte hash, or stale embedding. Do not suppress that failure or simply repin a changed file.
3. Before accepting a successor atlas, obtain a matching reviewed standalone producer snapshot, or establish and test a deterministic generator. Document PCA centering, component/sign orientation, precision and explained variance; Ward distance/linkage/cut and tie handling; equal-weight unstandardized raw axes; dependency versions; identity/order; priority labels; and stable cluster ID/color mapping. No CSV-only reconstruction of those missing fields is established here.
4. Compare every identity, axis, description and unit with the CSV; review all derived metadata and changes. Only then update the validator's baseline pins/counts, manifest, mutation tests, version records and receipt together in the study PR. A deliberate successor must preserve the baseline's audit trail, rather than representing the old v12/v3 hashes as new data.
5. Run both commands above, then smoke-test the local HTML offline: ethics/PCA, each k=8/10/12 cluster view, every unit filter and marker, search/selection, four-profile radar, nearest-neighbor selection, labels and clear. Confirm no page errors or external requests. Run the live repository author preflight and required commit preparation, publish without force, and await housekeeping and the final-head integration audit. The CI agent/owner handles integration.

Until step 3 is satisfied, additions can be proposed but cannot be accepted as a synchronized atlas release. This is a frozen-snapshot guard, not an unverified rebuild script.
