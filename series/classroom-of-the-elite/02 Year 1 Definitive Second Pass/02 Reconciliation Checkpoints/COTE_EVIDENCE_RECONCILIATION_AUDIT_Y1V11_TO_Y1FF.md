---
title: "COTE Year 1 Evidence Reconciliation Audit — Y1V11 through Y1FF"
artifact_type: "evidence_reconciliation_audit"
checkpoint_id: "Y1-FINAL-LOCK"
status: "pass"
updated_at: "2026-08-14"
---
# Evidence Reconciliation Audit — Y1V11 → Y1FF

## Result: PASS

### Evidence cardinality

- cumulative through Y1V10: 1,037
- Y1V11: +149 → 1,186
- Y1V11.5: +151 → 1,337
- Y1FF: +82 → **1,419**
- unique final IDs: **1,419**

### Fresh locator validation

| Source | Evidence | Text | Visual | Valid | Errors |
|---|---:|---:|---:|---:|---:|
| Y1V11 | 149 | 140 | 9 | 149 | 0 |
| Y1V11.5 | 151 | 141 | 10 | 151 | 0 |

Canonical paragraph addressing counts a `<p>` node when it contains base text or an image and excludes pure `<br>` spacer paragraphs. Ruby `rt/rp` text is not promoted into the base-text address layer.

### Inherited First File source audit

| Layer | Count | Authority |
|---|---:|---|
| fixed-layout documentary | 58 | source page image |
| bonus fiction | 24 | XHTML paragraph |
| total | 82 | mixed dual-locator scheme |
| Japanese anchors | 18 | image-primary or XHTML-primary according to source layer |

The guidebook binary was not remounted during this final lock. No OCR-derived wording was introduced.

### Terminology

- prior through Y1V11: 253
- Y1V11.5 additions: 12
- Y1FF additions: 18
- final: **283**

### Spoiler/source-boundary checks

- no Year 2 evidence IDs added;
- no Volume 0 evidence IDs added;
- no *Second List* evidence IDs added;
- no Year 3 evidence IDs added;
- later sources appear only in explicit exclusion/future-work language.

### Claim-status reconciliation

- Ayanokōji ordinary-life self-authorship: strengthened.
- Ayanokōji developmental authorship: strengthened and ethically darkened.
- reciprocal authorship: newly governing.
- Horikita independence: corrected toward integrated self-authorship.
- Kei tool-only reading: rejected as total account; irreplaceability remains unresolved.
- Ichinose kindness-as-defect reading: corrected toward solidarity + adversarial-security/result-conversion problem.
- Ryūen moral-reform inference: not established.
- `実力`: expanded with legibility/model and record layers.
- OAA: activated as retrospective/counterfactual paratext only.
- detailed Tsukishiro White Room claims: retain testimony tier where uncorroborated.

### Administrative decision

Create immutable `THROUGH_Y1` ledgers rather than rewriting `THROUGH_Y1V11`. Update only mutable retrieval/admin artifacts to the final boundary.
