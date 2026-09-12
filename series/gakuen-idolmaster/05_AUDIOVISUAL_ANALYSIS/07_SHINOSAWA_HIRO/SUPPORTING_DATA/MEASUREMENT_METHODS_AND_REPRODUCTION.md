---
series: GKM
generation: V2
artifact_type: historical_supporting_record
status: historical_legacy
supersedes: []
superseded_by: []
do_not_use_as_current_authority: true
source_boundary: "Preserved earlier-generation supporting record; not fresh AVE-FULL evidence."
last_updated: '2026-09-10'
---

> **Public repository representation.** Machine-specific paths use `WORKSPACE/`, `LOCAL_USER/` or `LOCAL_DRIVE_*` placeholders; configure these roots before reproduction. Direct Drive URLs are represented by source-object IDs. Original execution hashes and exported-byte claims identify the archived originals; public code/data snippets containing these substitutions are explicitly derivatives. The import manifest records their final repository hashes and decoded payload hashes.

> Historical record retained from the previous packet. “New/current” in this document refers to that earlier execution, not AVE-FULL-20260910. Fresh results are in [the current measurements](FULL_REBUILD_MEASUREMENTS.md) and [current claim review](FULL_REBUILD_CLAIM_REVIEW.md).

# Measurement methods and reproduction — newly performed work

> **Authorized execution revision — 2026-09-10.** This complete document preserves the supplied rebuild and earlier canonical analysis as inherited work. Statements about “new,” “current,” or “session” processing in preserved historical sections refer to that supplied run, unless explicitly labeled **authorized execution**. They are not evidence that this reviewer performed those inspections. Current findings and source-clock controls are recorded in [the execution review](EXECUTION_20260910_REVIEW.md); source acquisition, numerical processing, direct visual inspection, and automated audio work have separate coverage. This remains an integration candidate; no canonical repository document was replaced.


The recovered appendices advertise tools and feature families, but do not supply original run parameters, script outputs, proxy weights or analysis windows. This session reran independently defined descriptive measurements. These are not recovered original measurements.

## Software and input handling

Python3.12.14; ffmpeg/ffprobe6.1.1-3ubuntu5; NumPy2.5.3; SciPy1.18.1; librosa1.0.0; OpenCV5.0.0; soundfile0.14.0. SHA-256 uses Python hashlib. No normalization, denoising, source separation, speaker diarization or transcription is applied. First audio stream is selected. Attached-cover video streams are excluded from the main moving-video properties; their complete probe fields remain in the manifest. A 90000/1 attached-picture time base is not the source’s playback frame rate.

New measurement inputs are every record’s actual materialized hash in the rebuilt manifest. Hiro STEP4 uses a user-trimmed derivative. Original-object identity and content-equivalence limitations are stated separately from feature reproducibility.

## Source-level audio

- EBU R128: ffmpeg `ebur128=peak=true` on native-channel first audio stream. Integrated loudness in LUFS, LRA in LU, true peak in dBFS, with ffmpeg’s standard gating. Summary precision is0.1; small differences below this are not resolved.
- Low-level intervals: `silencedetect=noise=-50dB:d=0.5`, default combined-channel detection. This is not dialogue silence, a voice-activity detector or a speaker-pause measure. Closed intervals and an unclosed final start are reported separately.
- Spectral/RMS features: ffmpeg downmixes first audio stream to mono float32 at22050Hz. FFT2048, hop512 (23.21995465ms), periodic Hann, no padding for the custom spectral/RMS calculations. Incomplete final windows are excluded. RMS is unweighted raw amplitude. RMS P90/P10 in dB is20log10(P90/P10), using1e-12 floor; it is not LRA.
- Centroid: framewise magnitude-weighted frequency mean, then arithmetic mean over all complete windows including silence.
- Flatness: geometric/arithmetic ratio of power-spectrum bins, with1e-10 power floor in log and denominator. Includes silence; a silent spectrum can produce flatness1 under this convention. It is not vocal breathiness.
- Flux: L1-normalize each magnitude spectrum; retain positive successive-bin differences; compute their L2 norm. Mean and population CV (SD/mean, ddof0) are reported. First frame has no transition. This definition is newly specified, not a recovered historical one.
- Beat/tempo/chroma/tonnetz features are computed only for sources originally classified as music/performance. Librosa onset strength uses22050Hz, hop512, FFT2048, centered analysis, mean aggregation. Beat tracker uses start120BPM, tightness100, trim=true. Beat interval CV is population CV of detected interbeat seconds; not a manually validated rhythmic-irregularity score.
- Local tempo uses start120BPM, std_bpm1, autocorrelation8s, maximum320BPM, aggregate=None. Local-tempo CV is population CV of these tracker estimates. Half/double-time and ambiguous pulse are not corrected manually.
- Chroma: chroma_stft with FFT2048, hop512, tuning0, norm1, center=true. Mean Shannon entropy in bits of each frame’s12-bin chroma distribution. Tonnetz: librosa’s6D transform from this chroma; mean Euclidean distance between adjacent coordinates. These are unseparated mix descriptors, not harmonic complexity verdicts.

## Sampled visual features

OpenCV seeks to0,5,10,...seconds while time < container end, reads a frame, then resizes the entire image to160×90 with INTER_AREA. Square/static media are therefore geometrically normalized; aspect distortion is a limitation. Grayscale conversion uses OpenCV BGR2GRAY, normalized by255; HSV saturation mean is S/255. Consecutive sample mean absolute grayscale difference is reported, without division by elapsed time. Histogram proxy uses8×8×8 BGR bins, L1 normalization, Bhattacharyya distance, and counts adjacent sample distances strictly greater than0.5.

No optical flow, pose quality, shot count, frame-by-frame movement or character-area isolation is inferred. Uploader mattes, text, subtitle overlays, credits and letterboxes can dominate results. Some H.264 reads emitted `mmco: unref short failure`; the decoder continued. Expected/successful counts and decoder-reported time are retained; successful reads are not proof of artifact-free decoding. Do not use a small scalar difference as a fine performance judgment.

## Measures deliberately unavailable or retired

| Historical field | Disposition | Reason / replacement |
|---|---|---|
| experimental proxy and rank | RETIRED | No formula, weights, normalization, calibration or original group assignments recovered. Ingredient list alone is insufficient. |
| two empty/nan composite group means | RETIRED | No valid composite observations; new independent feature group means replace them with explicit n. |
| structural novelty CV | RETIRED | Original novelty function, representation, lag/kernel and windowing are unknown. Flux is separately defined, not silently relabeled as novelty. |
| aggregate F0 median/span | NOT GENERATED | Original extractor and voicing rules not recovered; polyphonic mixes and multiple speakers make voice attribution invalid. No actor-specific pitch claim is repaired using mixed pitch tracking. |
| original dynamic range | NOT RECOVERED | Original definition unknown; report separate EBU LRA and explicitly defined RMS P90/P10 instead. |
| estimated major cuts / motion | RELABELED | Newly specified5s image differences and histogram jumps are not true cuts or motion speed. |
| pose-estimation working output | HISTORICAL-ONLY | Hiro appendix says working output existed; it was not recovered here. No new pose score or historical nonexistence claim. |
| isolated voice properties, speaker/BGM/SFX proportions | UNRESOLVED | No stems or validated diarization/semantic audio annotation; full mixes remain full mixes. |

## Reproduction procedure

1. Check out the exact repository commit stated in the README in a separate working directory. Keep original manifests unchanged. Stage the exact media hashes under `media/HIRO/<drive_id>/` or `media/MISUZU/<drive_id>/`; the filename is arbitrary for discovery but must be recorded. The trimmed Hiro derivative must remain a separate object from original Drive bytes.
2. Use the listed versions. Put the following code into `measure_media.py` outside the delivered Markdown-only package, set ROOT to that working root, and run `python measure_media.py HIRO MISUZU`. The ROOT directory must contain `repo/series/gakuen-idolmaster/...` and the staged media. Existing output JSON is a cache: remove stale output for any changed input hash before rerunning. Check hashes before accepting cached results.
3. Tables in this package render the resulting numerical fields with up to12 significant digits. Means are arithmetic, source-group means are equal-weighted by source, CV uses population SD. Visual sample rows and every input hash permit independent recomputation of summaries.
4. Segment analysis extracts an explicitly bounded native-rate/channel float32 WAV with `atrim=start=A:end=B,asetpts=PTS-STARTPTS` before R128 integration; this avoids output-seek filtering of the full file. Apply the same audio functions to the extracted interval, and sample original video at A,A+5,... <B. Segment-local silence times start at zero; absolute source time is A + detector time. No temporary WAV is delivered.
5. No direct listening or continuous audiovisual watching is claimed. Human/model visual inspection consists only of the exact frames in the inspection log. Technical extraction and audio attachment playback capability are not certified auditory judgments.

## Exact source-processing code used in this session

```python
import os,sys,json,hashlib,subprocess,re,traceback
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor,as_completed
import numpy as np, cv2, librosa, scipy, soundfile
ROOT=Path('/workspace/scratch/5ad90d169bca')
OUT=ROOT/'measurements';OUT.mkdir(exist_ok=True)
SR=22050;NFFT=2048;HOP=512
def run(args):
 p=subprocess.run(args,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
 if p.returncode:raise RuntimeError(p.stderr.decode(errors='replace')[-2000:])
 return p
def cv(a):
 a=np.asarray(a);return float(a.std(ddof=0)/a.mean()) if len(a) and a.mean()>1e-12 else None
def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for b in iter(lambda:f.read(1024*1024),b''):h.update(b)
 return h.hexdigest()
def sound(p,start=0,end=None,music=False):
 args=['ffmpeg','-v','error','-threads','1','-i',str(p),'-ss',str(start)]
 if end is not None:args+=['-t',str(end-start)]
 args+=['-map','0:a:0','-vn','-ac','1','-ar',str(SR),'-f','f32le','-']
 y=np.frombuffer(run(args).stdout,dtype='<f4')
 rms=[];cent=[];flat=[];flux=[];chroma_chunks=[]
 prev=None;window=np.hanning(NFFT+1)[:-1];freq=np.fft.rfftfreq(NFFT,1/SR)
 for k in range(0,max(0,len(y)-NFFT+1),HOP*1024):
  block=y[k:min(len(y),k+HOP*1024+NFFT-HOP)]
  frames=np.lib.stride_tricks.sliding_window_view(block,NFFT)[::HOP].astype(np.float64)
  rms.extend(np.sqrt(np.mean(frames**2,axis=1)).tolist())
  mag=np.abs(np.fft.rfft(frames*window,axis=1));power=mag**2
  cent.extend((np.sum(mag*freq,axis=1)/np.maximum(mag.sum(axis=1),1e-20)).tolist())
  flat.extend((np.exp(np.mean(np.log(np.maximum(power,1e-10)),axis=1))/np.maximum(np.mean(power,axis=1),1e-10)).tolist())
  norm=mag/np.maximum(mag.sum(axis=1,keepdims=True),1e-20)
  seq=np.vstack([prev,norm]) if prev is not None else norm
  flux.extend(np.sqrt(np.sum(np.maximum(np.diff(seq,axis=0),0)**2,axis=1)).tolist());prev=norm[-1]
 out={'sample_rate_hz':SR,'audio_samples':len(y),'analyzed_audio_duration_s':len(y)/SR,'stft_frames':len(rms),'flux_transitions':len(flux),'rms_linear':float(np.sqrt(np.mean(y.astype(np.float64)**2))),'rms_p10_linear':float(np.percentile(rms,10)),'rms_p90_linear':float(np.percentile(rms,90)),'rms_p90_p10_db':float(20*np.log10(max(np.percentile(rms,90),1e-12)/max(np.percentile(rms,10),1e-12))),'centroid_hz_mean':float(np.mean(cent)),'flatness_mean':float(np.mean(flat)),'positive_normalized_flux_mean':float(np.mean(flux)),'flux_cv':cv(flux)}
 if music:
  onset=librosa.onset.onset_strength(y=y,sr=SR,hop_length=HOP,n_fft=NFFT,center=True,aggregate=np.mean)
  tempo,beats=librosa.beat.beat_track(onset_envelope=onset,sr=SR,hop_length=HOP,start_bpm=120,tightness=100,trim=True)
  local=librosa.feature.tempo(onset_envelope=onset,sr=SR,hop_length=HOP,start_bpm=120,std_bpm=1,ac_size=8,max_tempo=320,aggregate=None)
  chrom=librosa.feature.chroma_stft(y=y,sr=SR,n_fft=NFFT,hop_length=HOP,tuning=0,norm=1,center=True)
  probs=chrom/np.maximum(chrom.sum(axis=0,keepdims=True),1e-20)
  entropy=-np.sum(probs*np.log2(np.maximum(probs,1e-20)),axis=0)
  ton=librosa.feature.tonnetz(chroma=chrom,sr=SR)
  tm=np.linalg.norm(np.diff(ton,axis=1),axis=0)
  out.update({'tempo_bpm':float(np.asarray(tempo).ravel()[0]),'beat_count':len(beats),'beat_interval_count':max(0,len(beats)-1),'beat_interval_cv':cv(np.diff(beats)*HOP/SR),'local_tempo_count':len(local),'local_tempo_cv':cv(local),'chroma_frames':chrom.shape[1],'chroma_entropy_bits_mean':float(entropy.mean()),'tonnetz_transition_count':len(tm),'tonnetz_motion_mean':float(tm.mean())})
 return out
def loudness(p,start=0,end=None):
 args=['ffmpeg','-hide_banner','-nostats','-threads','1','-i',str(p),'-ss',str(start)]
 if end is not None:args+=['-t',str(end-start)]
 args+=['-map','0:a:0','-vn','-af','ebur128=peak=true,silencedetect=noise=-50dB:d=0.5','-f','null','-']
 txt=run(args).stderr.decode(errors='replace')
 summary=txt[txt.rfind('Summary:'):]
 def val(pattern):
  m=re.search(pattern,summary);return float(m.group(1)) if m else None
 intervals=[];s=None
 for line in txt.splitlines():
  m=re.search(r'silence_start: ([\d.]+)',line)
  if m:s=float(m.group(1))
  m=re.search(r'silence_end: ([\d.]+)',line)
  if m and s is not None:intervals.append([s,float(m.group(1))]);s=None
 return {'integrated_lufs':val(r'LOCAL_DRIVE_I\s+(-?[\d.]+) LUFS'),'lra_lu':val(r'LRA:\s+([\d.]+) LU'),'true_peak_dbfs':val(r'Peak:\s+(-?[\d.]+) dBFS'),'silence_intervals_s':intervals,'silence_seconds':sum(b-a for a,b in intervals),'unclosed_silence_start_s':s,'ebur128_summary':summary.strip()}
def visual(p,start,end,step=5):
 cap=cv2.VideoCapture(str(p));rows=[];prev=None;prevh=None
 for t in np.arange(start,end,step):
  cap.set(cv2.CAP_PROP_POS_MSEC,float(t)*1000);ok,im=cap.read()
  if not ok:continue
  im=cv2.resize(im,(160,90),interpolation=cv2.INTER_AREA)
  gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY).astype(np.float32)/255
  hsv=cv2.cvtColor(im,cv2.COLOR_BGR2HSV)
  hist=cv2.calcHist([im],[0,1,2],None,[8,8,8],[0,256]*3);hist=cv2.normalize(hist,hist,alpha=1,norm_type=cv2.NORM_L1)
  motion=float(np.abs(gray-prev).mean()) if prev is not None else None
  dist=float(cv2.compareHist(prevh,hist,cv2.HISTCMP_BHATTACHARYYA)) if prevh is not None else None
  rows.append({'requested_time_s':float(t),'reported_time_s':cap.get(cv2.CAP_PROP_POS_MSEC)/1000,'brightness':float(gray.mean()),'saturation':float(hsv[:,:,1].mean()/255),'frame_difference':motion,'histogram_distance':dist})
  prev=gray;prevh=hist
 cap.release()
 return {'sample_step_s':step,'sample_width':160,'sample_height':90,'samples':len(rows),'brightness_mean':float(np.mean([x['brightness'] for x in rows])) if rows else None,'saturation_mean':float(np.mean([x['saturation'] for x in rows])) if rows else None,'frame_difference_mean':float(np.mean([x['frame_difference'] for x in rows[1:]])) if len(rows)>1 else None,'histogram_jumps_gt_0_5':sum(x['histogram_distance']>0.5 for x in rows[1:]),'rows':rows}
def process(char,d,s):
 ident=s['drive_id'];op=OUT/char/(ident+'.json');op.parent.mkdir(exist_ok=True)
 if op.exists():return ident+' cached'
 paths=list((ROOT/'media'/char/ident).glob('*.mp4'))
 if not paths:return ident+' unavailable'
 p=paths[0];probe=json.loads(run(['ffprobe','-v','error','-show_format','-show_streams','-show_chapters','-of','json',str(p)]).stdout)
 music=(s.get('source_folder')=='music' if char=='HIRO' else s.get('class') not in ['dear_compilation','song_commu'])
 duration=float(probe['format']['duration'])
 r={'source_id':ident,'character':char,'filename':p.name,'size_bytes':p.stat().st_size,'sha256':sha(p),'probe':probe,'audio_metrics':sound(p,music=music),'loudness':loudness(p),'visual':visual(p,0,duration),'new_direct_listening':False,'new_direct_visual_inspection':False}
 op.write_text(json.dumps(r,ensure_ascii=False,indent=2));return char+' '+ident+' processed'
def main():
 chars=sys.argv[1:] or ['MISUZU','HIRO'];tasks=[]
 for c,d in [('HIRO','07_SHINOSAWA_HIRO'),('MISUZU','11_HATAYA_MISUZU')]:
  if c not in chars:continue
  m=json.loads((ROOT/'repo/series/gakuen-idolmaster/05_AUDIOVISUAL_ANALYSIS'/d/f'GKM_PHASE3_{c}_AUDIOVISUAL_SOURCE_MANIFEST.json').read_text())
  tasks.extend((c,d,s) for s in m['sources'])
 with ThreadPoolExecutor(max_workers=3) as ex:
  futs={ex.submit(process,*x):x for x in tasks}
  for f in as_completed(futs):
   try:print(f.result(),flush=True)
   except Exception:traceback.print_exc()
if __name__=='__main__':main()

```

## Segment-processing code used for chapter metadata

First run below covers Misuzu11–20; the second uses the uploaded21–27 probe. Outputs include ED control segments, which must be excluded from narrative chapter counts.

```python
import measure_media as m
import json
from concurrent.futures import ThreadPoolExecutor
C='MISUZU';id='1NyhdO7zo56LTuHdfmfV2kznkr7o8IEqD';p=next((m.ROOT/'media'/C/id).glob('*.mp4'))
d=json.loads((m.OUT/C/(id+'.json')).read_text())
def one(ch):
 a=float(ch['start_time']);b=float(ch['end_time']);n=ch.get('tags',{}).get('title',str(ch['id']));print(n,a,b,flush=True)
 # Extract the requested interval before filtering; this prevents output seek from contaminating loudness integration.
 tmp=m.ROOT/'measurements'/('segment_'+str(ch['id'])+'.wav')
 m.run(['ffmpeg','-v','error','-y','-i',str(p),'-map','0:a:0','-af',f'atrim=start={a}:end={b},asetpts=PTS-STARTPTS','-c:a','pcm_f32le',str(tmp)])
 r={'source_id':id,'input_sha256':d['sha256'],'label':n,'start_s':a,'end_s':b,'duration_s':b-a,'boundary_method':'container chapter metadata; no claim of frame-exact narrative boundary','audio_metrics':m.sound(tmp),'loudness':m.loudness(tmp),'visual':m.visual(p,a,b)}
 tmp.unlink();return r
with ThreadPoolExecutor(max_workers=3) as ex:rs=list(ex.map(one,d['probe']['chapters']))
(m.OUT/'MISUZU_DEAR_SEGMENTS.json').write_text(json.dumps(rs,ensure_ascii=False,indent=2))

```

```python
import measure_media as m
import json
from concurrent.futures import ThreadPoolExecutor
C='MISUZU';id='149ubZq2LgWA1zuE4U8dICF0X9bZvWv5w';p=next((m.ROOT/'media'/C/id).glob('*.mp4'))
d=json.loads((m.OUT/'01-21-27-STEP3-720p60-_UPLOAD_PROBE.json').read_text())
def one(ch):
 a=float(ch['start_time']);b=float(ch['end_time']);n=ch.get('tags',{}).get('title',str(ch['id']));print(n,a,b,flush=True)
 # Extract the requested interval before filtering; this prevents output seek from contaminating loudness integration.
 tmp=m.ROOT/'measurements'/('segment_step3_'+str(ch['id'])+'.wav')
 m.run(['ffmpeg','-v','error','-y','-i',str(p),'-map','0:a:0','-af',f'atrim=start={a}:end={b},asetpts=PTS-STARTPTS','-c:a','pcm_f32le',str(tmp)])
 r={'source_id':id,'input_sha256':d['sha256'],'label':n,'start_s':a,'end_s':b,'duration_s':b-a,'boundary_method':'container chapter metadata; no claim of frame-exact narrative boundary','audio_metrics':m.sound(tmp),'loudness':m.loudness(tmp),'visual':m.visual(p,a,b)}
 tmp.unlink();return r
with ThreadPoolExecutor(max_workers=3) as ex:rs=list(ex.map(one,d['probe']['chapters']))
(m.OUT/'MISUZU_DEAR_21_27_SEGMENTS.json').write_text(json.dumps(rs,ensure_ascii=False,indent=2))

```

## Authorized execution numerical qualification

**Authorized execution numerical qualification:** H23 `rms_p90_p10_db = 211.058496695` is dominated by a near-zero P10 (`7.37756150279e-12`); H31 `230.283647623` uses P10 = 0 with the declared `1e-12` floor. These are silence/floor-sensitive source-span ratios, not expressive dynamic range. H23 is in the common group and strongly inflates its mean `60.5825248389 dB`; H31 is individual-only. Preserve the recorded values and memberships for reproducibility, but do not interpret the common-versus-principal difference as a musical result. No replacement mean or silent threshold change is introduced.


## Authorized execution reproduction entry points

The cached-source script and `_UPLOAD_PROBE` code retained above are **supplied-run historical reproduction records**; their inclusion does not claim they were executed in this session. Use [EXECUTION_MEASUREMENTS.md](EXECUTION_MEASUREMENTS.md) for the exact current helper, runtime, eleven current measurement records and nine-song rerun comparison. Use [the visual review](EXECUTION_20260910_REVIEW.md) and [music/breadth review](EXECUTION_MUSIC_AND_BREADTH_REVIEW.md) for the current frame tool, every actually viewed timestamp, crop/decoder details and hashes. Use [AUDIO_MODEL_REVIEW.md](AUDIO_MODEL_REVIEW.md) for current audio decoding/ASR/model methods and rejected model outcomes. These are separate evidence pathways; none substitutes for another.

Across runtimes, a visual histogram proxy can change even with matching input hashes and requested/reported sample times (H20: inherited 16 jumps, current 17). That numerical drift is not a change in Hiro's movement or performance. Preserve each generation and its parameters; do not infer precise choreographic intensity from their difference.
