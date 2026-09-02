---
series: COTE
artifact_type: source_lock
scope: Y2
status: active_provisional
source_boundary: "Y2V01-Y2V12.5 + V00 + Y2SL"
generation: V2
updated_at: "2026-08-24"
---
# COTE Year 2 V2 — Source Inventory and Lock

All 15 numbered/decimal Year 2 Japanese EPUBs and Volume 0 were fetched directly from the canonical Drive source tree and audited as ZIP/EPUB containers. All pass CRC/container/OPF/spine/XHTML/image-readability checks and contain Japanese narrative prose.

| Code | Bytes | SHA-256 | Spine | XHTML | Images |
|---|---:|---|---:|---:|---:|
| Y2V01 | 1,033,179 | `6f31df73f2bcd05954b6c2886f6be20a844a4db8cf9ca4f6085acfeb516ad531` | 25 | 25 | 23 |
| Y2V02 | 2,466,176 | `e8b1024a70a8d5eed20f0c5b155c44bed7b4552366828a9cf7d6fba8b877025a` | 22 | 23 | 23 |
| Y2V03 | 2,715,806 | `0c9eec27725ec03969f6eda94736fe234e7ce63fe4ba088f841b036d8ce5309b` | 27 | 28 | 26 |
| Y2V04 | 2,681,573 | `ad3a8eb0a69a77fa959fbece462a3af65cc67fbcb6a2e9b2375de0b957e6f059` | 25 | 26 | 24 |
| Y2V04.5 | 2,534,757 | `4f23997a4f72b7ed59df6d3c334178bcc7b17c34551b6c9621a9054cd9f2f9f3` | 23 | 24 | 26 |
| Y2V05 | 2,155,499 | `829bf63db3496f654d8d9c871d0fbbacfd699d169eb0cc4d17235faadf24c719` | 24 | 25 | 21 |
| Y2V06 | 16,440,065 | `b4daa5f1998a3d1e05a783371233b5bd6c9a3d7b6624971a227653b2f0ae436b` | 23 | 24 | 22 |
| Y2V07 | 14,888,219 | `db45b6e29206b048d9311d05214550ad4f2d0e5907034b27092103d848cbde0c` | 24 | 25 | 24 |
| Y2V08 | 10,858,802 | `81059e92ce187302489bca9c2116745a1e6b31f46b736b908b11e308e391c263` | 22 | 23 | 23 |
| Y2V09 | 10,472,032 | `da89761bfd848fbc0c1a846cc8c647a03778357a005f66fd491c4aeb38b590f3` | 23 | 24 | 24 |
| Y2V09.5 | 9,575,530 | `8a4cadb422d030e60dca2b3b65b5e65321be3c4cdb13b102f0acdce45ed6620b` | 24 | 24 | 25 |
| Y2V10 | 9,871,375 | `310bb57a23fe737f7dae1f5b91c7acb37b195658cfc6071c91a96c8a94fbfe7e` | 24 | 25 | 23 |
| Y2V11 | 11,174,532 | `348f541675bfe30ad8d1894d43c32eef7641d366dee5a5544dbcded0886ffde5` | 25 | 26 | 21 |
| Y2V12 | 10,581,855 | `45a62f74e72c621162e9bbf8e7b8aae4a97ed719a1decb7b2fcf97462ddd7195` | 26 | 27 | 22 |
| Y2V12.5 | 12,848,788 | `d547dbfe5a57850b26b8d25201af8e0986126019fb0525fb733f23a8ca6da352` | 30 | 31 | 25 |
| V00 | 9,460,508 | `ec30387a4de96870b53e88a4a2ca5d28ac27455e5ffb15936f4895852fcdb209` | 69 | 69 | 18 |
| Y2SL | 119,398,463 | `fcc6f15ff674c9833263247816bf23ce67a7b337924fe87901567285331e98b5` | 251 | 252 | 246 |

## V09.5 / V10 provenance note
Earlier project history records mislabeled Simplified-Chinese copies followed by validated Japanese replacements. The current Drive payloads are Japanese throughout and structurally match the replacement-audit descriptions. Their current byte hashes are locked above. Preserve earlier hashes only as provenance; do not silently substitute them.

## Second List
`Y2SL` was reacquired by direct chat upload on 2026-08-24 because the ~119 MB guidebook binary remains above the established Drive connector transfer path used for the Primary Sources mirror. The reacquired byte object exactly matches the historically staged source identity.

Audit result:
- bytes: `119398463`
- SHA-256: `fcc6f15ff674c9833263247816bf23ce67a7b337924fe87901567285331e98b5`
- ZIP/CRC integrity: pass
- OPF spine: `251`
- XHTML resources: `252`
- JPEG resources: `246`
- documentary body: fixed-layout Japanese image resources
- bonus fiction: `Text/part0241.xhtml` (`模擬デート`) and `Text/part0242.xhtml` (`あの頃から───`)
- canonical audit: `COTE_Y2_SECOND_LIST_PARATEXT_AUDIT.md`

The source identity is now locked for Year-2 analytical purposes even though the large EPUB binary itself remains outside the Drive mirror. Do not substitute summaries or prior synthesis for the verified guidebook.
