---
series: GKM
generation: V2
status: canonical
supersedes: null
superseded_by: null
do_not_use_as_current_authority: false
last_updated: "2026-08-16"
artifact_type: technical_appendix
scope: CHARACTER_HATAYA_MISUZU_PHASE3_AV_METRICS
character: "Hataya Misuzu / 秦谷美鈴"
source_boundary: "ffprobe, ffmpeg ebur128/silence detection, sampled-frame OpenCV measures, and librosa aggregate features"
---

# MISUZU AV TECHNICAL METRICS APPENDIX

## Interpretation rules

- Metrics are comparative aids, not substitutes for interpretation.
- Aggregate F0 for dialogue compilations includes every voice and BGM.
- Aggregate F0 for songs includes accompaniment leakage and is not isolated singing pitch.
- Motion/brightness/saturation are sampled-frame measures and do not identify narrative meaning by themselves.
- Estimated cuts are histogram-change proxies, not manually verified edit counts.

| class | source | duration s | LUFS | LRA | aggregate F0 med. Hz | F0 span st | tempo BPM | brightness | saturation | motion | estimated major cuts |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|

## Dear chapter/segment table

| Dear | segment duration s | boundary method | aggregate F0 med. | F0 span st | RMS | centroid Hz | brightness | saturation | motion |
|---:|---:|---|---:|---:|---:|---:|---:|---:|---:|
