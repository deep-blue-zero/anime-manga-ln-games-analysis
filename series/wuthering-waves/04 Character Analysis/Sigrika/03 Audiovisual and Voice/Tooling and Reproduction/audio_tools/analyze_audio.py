#!/usr/bin/env python3
"""Reproduce source-bound Sigrika waveform measurements without perception claims.

Reads exact members from user-authorized Drive ZIP archives. No network access,
no uploads, no speech synthesis, no emotion inference, no channel downmix.
Native signed-16-bit PCM and full FLAC digests are verified before analysis.
Time is object-relative sample time, never an inferred in-game/video timestamp.
"""
from __future__ import annotations
import argparse, concurrent.futures, hashlib, io, json, math, os, platform, re, sys, time, zipfile
from collections import defaultdict
from pathlib import Path
import numpy as np
import scipy
from scipy import signal
import soundfile as sf
import parselmouth

VERSION = 'sigrika-waveform-analysis-0.2.0'
PARAMS = {
    'native_integrity': 'sha256(FLAC bytes); sha256(interleaved native s16le payload)',
    'analysis_channel': 'highest native RMS channel, zero-based; no downmix or spatial interpretation',
    'analysis_sample_rate_hz': 16000,
    'resampling': 'scipy.signal.resample_poly; gcd ratio; default Kaiser beta=5.0',
    'gate_window_seconds': 0.02,
    'gate_thresholds_dbfs': [-50, -45, -40],
    'minimum_internal_gap_seconds': 0.10,
    'pitch': {'method':'Praat autocorrelation via Parselmouth Sound.to_pitch_ac',
              'time_step':0.01,'pitch_floor':75.0,'pitch_ceiling':650.0,
              'max_number_of_candidates':15,'very_accurate':False,
              'silence_threshold':0.03,'voicing_threshold':0.45,
              'octave_cost':0.01,'octave_jump_cost':0.35,'voiced_unvoiced_cost':0.14},
    'pitch_sensitivity': {'pitch_floor':100.0,'pitch_ceiling':750.0},
    'hnr': {'method':'Praat cross-correlation harmonicity','time_step':0.01,
            'minimum_pitch':75.0,'silence_threshold':0.1,'periods_per_window':1.0},
    'spectral': {'window_seconds':0.04,'hop_seconds':0.01,'window':'Hann',
                 'frequency_band_hz':[80,8000], 'tilt_fit_hz':[500,4000],
                 'tilt_definition':'linear least squares: 10log10 power versus log2 frequency'},
    'text_rate': 'language-specific written units / object duration or energy-active duration; not syllables, not forced alignment',
    'uncertainty': 'all pitch and harmonicity values are signal estimates; no perceptual review; mixtures and estimator failures are flagged',
}

def read_jsonl(path: Path) -> list[dict]:
    return [json.loads(x) for x in path.read_text(encoding='utf-8').splitlines() if x.strip()]

def sha(path:Path)->str:
    h=hashlib.sha256()
    with path.open('rb') as f:
        for b in iter(lambda:f.read(1024*1024),b''):h.update(b)
    return h.hexdigest()

def db(x):
    return 20*np.log10(np.maximum(x,1e-12))

def quant(x)->dict:
    x=np.asarray(x,dtype=float);x=x[np.isfinite(x)]
    if not len(x):return {'n':0,'p10':None,'median':None,'p90':None,'mean':None,'sd':None}
    q=np.quantile(x,[.1,.5,.9])
    return {'n':int(len(x)),'p10':float(q[0]),'median':float(q[1]),'p90':float(q[2]),'mean':float(np.mean(x)),'sd':float(np.std(x))}

def coarse_contour(values, times, duration, bins=12):
    out=[]
    for i in range(bins):
        v=values[(times>=duration*i/bins)&(times<duration*(i+1)/bins)];v=v[np.isfinite(v)]
        out.append(float(np.median(v)) if len(v) else None)
    return out

def gate_features(x:np.ndarray,sr:int,threshold:float)->dict:
    # Native, non-overlapping frames; final partial frame uses its actual length.
    win=max(1,round(.02*sr)); starts=np.arange(0,len(x),win); lengths=np.minimum(win,len(x)-starts)
    rms=np.sqrt(np.add.reduceat(x*x,starts)/lengths);en=db(rms); active=en>=threshold
    duration=len(x)/sr; weights=lengths/sr
    spans=[]; edges=np.r_[0,np.flatnonzero(active[1:]!=active[:-1])+1,len(active)]
    for a,b in zip(edges[:-1],edges[1:]):
        spans.append((int(a),int(b),bool(active[a])))
    leading=float(np.sum(weights[:spans[0][1]])) if spans and not spans[0][2] else 0.0
    trailing=float(np.sum(weights[spans[-1][0]:])) if spans and not spans[-1][2] else 0.0
    gaps=[]
    for a,b,on in spans:
        if not on and a>0 and b<len(active):
            start=float(starts[a]/sr);end=float((starts[b-1]+lengths[b-1])/sr)
            if end-start>=.10-1e-9:gaps.append([start,end])
    active_duration=float(np.sum(weights[active])); internal=float(sum(b-a for a,b in gaps))
    times=(starts+lengths/2)/sr
    return {'threshold_dbfs':threshold,'active_seconds':active_duration,
            'silent_seconds':duration-active_duration,'silent_fraction':1-active_duration/duration,
            'leading_seconds':leading,'trailing_seconds':trailing,
            'internal_gaps_ge_100ms':gaps,'internal_gap_seconds':internal,
            'internal_gap_count':len(gaps),'internal_gaps_per_second':len(gaps)/duration,
            'active_frame_energy_dbfs':quant(en[active]),
            'all_frame_energy_dbfs':quant(en),'energy_contour_12_bins_dbfs':coarse_contour(en,times,duration)}

def clean_text(t):
    if not isinstance(t,str):return ''
    t=re.sub(r'<[^>]*>','',t);t=re.sub(r'\{[^}]*\}','',t)
    return t

def text_units(t,lang):
    t=clean_text(t).strip()
    if re.fullmatch(r'[（(\[].*[）)\]]',t,flags=re.S):
        return None,'nonlexical_parenthetical_annotation'
    if lang=='en':return len(re.findall(r"[A-Za-z0-9]+(?:['’-][A-Za-z0-9]+)*",t)),'English orthographic words'
    if lang=='zh':return len(re.findall(r'[\u3400-\u9fff]',t)),'Han characters'
    if lang=='ja':return len(re.findall(r'[\u3040-\u30ff\u3400-\u9fff]',t)),'kana and Han characters'
    if lang=='ko':return len(re.findall(r'[\uac00-\ud7a3]',t)),'Hangul syllable blocks'
    return None,'unsupported'

def witness(l,lang):
    w=l.get('text_witnesses',{}); w=w.get('zh-Hans' if lang=='zh' else lang,w.get(lang,{})) if isinstance(w,dict) else {}
    if isinstance(w,dict):return w.get('text',w.get('content',''))
    return w if isinstance(w,str) else ''

def analyze_one(job):
    path,meta,refs=job; path=Path(path);h=meta['canonical_pcm_sha256']
    result={'analysis_version':VERSION,'canonical_pcm_sha256':h,'flac_sha256':meta['flac_sha256'],
            'drive_relative_path':meta['drive_relative_path'],'archive_member_path':meta['archive_member_path'],
            'evidence_scopes':meta['evidence_scopes'],'voice_languages':meta['voice_languages'],
            'semantic_occurrence_ids':meta['semantic_occurrence_ids'],
            'render_association_ids':meta['render_association_ids'],'source_locators':meta['source_locators'],
            'source_wem_sha256':meta['source_wem_sha256'],'flags':[],
            'perceptual_listening_performed':False}
    try:
        b=path.read_bytes();got=hashlib.sha256(b).hexdigest()
        if got!=meta['flac_sha256']:raise ValueError('FLAC checksum mismatch')
        info=sf.info(io.BytesIO(b))
        if info.subtype!='PCM_16':raise ValueError('Native payload schema only supports PCM_16; refusing conversion')
        pcm,sr=sf.read(io.BytesIO(b),dtype='int16',always_2d=True)
        if not len(pcm):raise ValueError('Empty recording')
        got_pcm=hashlib.sha256(pcm.astype('<i2',copy=False).tobytes()).hexdigest()
        expected=sorted({r['render'].get('pcm_payload_sha256') for r in refs if r['render'].get('pcm_payload_sha256')})
        if len(expected)!=1 or got_pcm!=expected[0]:raise ValueError('Missing or mismatching expected native PCM payload')
        x=pcm.astype(np.float64)/32768.;n,ch=x.shape;dur=n/sr
        mean_rms=np.sqrt(np.mean(x*x,axis=0));channel=int(np.argmax(mean_rms));track=x[:,channel]
        result['integrity']={'flac_sha256_match':True,'flac_bytes':len(b),'native_pcm_payload_sha256':got_pcm,
                             'expected_native_pcm_payload_sha256':expected[0],'native_pcm_payload_match':True,
                             'source_wem_redecoded':False,'canonical_framed_hash_recomputed':False}
        result.update({'sample_rate_hz':sr,'channels':ch,'frame_count':n,'duration_seconds':dur,
                       'analysis_channel_index':channel,'channel_rms_dbfs':[float(y) for y in db(mean_rms)],
                       'rms_dbfs':float(db(np.sqrt(np.mean(x*x)))),
                       'peak_dbfs':float(db(np.max(np.abs(x)))),
                       'exact_full_scale_samples':int(np.sum((pcm==32767)|(pcm==-32768))),
                       'near_full_scale_fraction_abs_ge_0_999':float(np.mean(np.abs(x)>=.999)),
                       'dc_offset_by_channel':[float(y) for y in np.mean(x,axis=0)]})
        if ch>1:
            result['flags'].append('multichannel_not_isolated_speaker')
            cor=np.corrcoef(x,rowvar=False)
            result['channel_correlations_to_selected']=[float(v) if np.isfinite(v) else None for v in cor[channel]]
        for r in refs:
            old=r['render']['machine_acoustic_observations']
            if (old['frame_count'],old['sample_rate_hz'],old['channels'])!=(n,sr,ch):raise ValueError('Native frame metadata mismatch')
        result['prior_measurement_comparison']={
            'duration_max_abs_error':max(abs(r['render']['machine_acoustic_observations']['duration_seconds']-dur) for r in refs),
            'rms_dbfs_max_abs_error':max(abs(r['render']['machine_acoustic_observations']['rms_dbfs']-result['rms_dbfs']) for r in refs),
            'peak_dbfs_max_abs_error':max(abs(r['render']['machine_acoustic_observations']['peak_dbfs']-result['peak_dbfs']) for r in refs)}
        result['gates']={str(t):gate_features(track,sr,t) for t in [-50,-45,-40]}
        result['gate_activity_sensitivity_seconds']=result['gates']['-50']['active_seconds']-result['gates']['-40']['active_seconds']
        if dur<.30:result['flags'].append('very_short_object')
        if result['exact_full_scale_samples']:result['flags'].append('full_scale_samples_not_proof_of_audible_clipping')
        if dur>40:result['flags'].append('long_object_check_subtitle_extent')
        g=math.gcd(sr,16000);y=signal.resample_poly(track,16000//g,sr//g)
        snd=parselmouth.Sound(y,sampling_frequency=16000)
        if dur<.05:
            result['pitch']=None;result['flags'].append('too_short_for_pitch')
        else:
            kwargs={k:v for k,v in PARAMS['pitch'].items() if k!='method'}
            pitch=snd.to_pitch_ac(**kwargs); f=pitch.selected_array['frequency']; ts=pitch.xs();valid=f>0
            strength=pitch.selected_array['strength']
            pf=quant(f[valid]); fv=f[valid];st=12*np.log2(fv) if len(fv) else np.array([])
            pf['robust_range_semitones']=float(12*np.log2(pf['p90']/pf['p10'])) if len(fv) else None
            pf['voiced_frame_fraction']=float(np.mean(valid));pf['voiced_frame_seconds_proxy']=float(np.sum(valid)*.01)
            pf['selected_candidate_strength']=quant(strength[valid]);pf['total_analysis_frames']=len(f)
            adjacent=valid[1:]&valid[:-1]
            steps=np.abs(12*np.log2(f[1:][adjacent]/f[:-1][adjacent]))
            pf['adjacent_jump_fraction_gt_8st']=float(np.mean(steps>8)) if len(steps) else None
            pf['edge_band_fraction_below90_or_above600']=float(np.mean((fv<90)|(fv>600))) if len(fv) else None
            f_nan=np.where(valid,f,np.nan);pf['contour_12_bins_hz']=coarse_contour(f_nan,ts,dur)
            if np.sum(valid)>=5:
                pf['global_slope_semitones_per_second']=float(np.polyfit(ts[valid],st,1)[0])
                a=f[(ts<dur/3)&valid];c=f[(ts>=2*dur/3)&valid]
                pf['last_minus_first_third_semitones']=float(12*np.log2(np.median(c)/np.median(a))) if len(a) and len(c) else None
            else:pf['global_slope_semitones_per_second']=None;pf['last_minus_first_third_semitones']=None
            kw2=dict(kwargs);kw2.update(PARAMS['pitch_sensitivity']);alt=snd.to_pitch_ac(**kw2)
            af=alt.selected_array['frequency'];ats=alt.xs();av=af>0
            aq=quant(af[av]); nearest=np.searchsorted(ats,ts);nearest=np.clip(nearest,0,len(ats)-1)
            left=np.maximum(nearest-1,0);nearest=np.where(abs(ats[left]-ts)<abs(ats[nearest]-ts),left,nearest)
            aligned=(abs(ats[nearest]-ts)<=.005001);shared=valid&aligned&(af[nearest]>0)
            dist=np.abs(12*np.log2(f[shared]/af[nearest][shared])) if np.any(shared) else np.array([])
            pf['sensitivity']={'alternate_median_hz':aq['median'],'matched_voiced_frames':len(dist),
                               'matched_abs_difference_semitones':quant(dist),
                               'matched_fraction_difference_gt3st':float(np.mean(dist>3)) if len(dist) else None,
                               'voicing_disagreement_fraction':float(np.mean(valid[aligned]!=(af[nearest][aligned]>0))) if np.any(aligned) else None}
            if np.sum(valid)<10:result['flags'].append('pitch_fewer_than_10_voiced_frames')
            if len(dist) and np.mean(dist>3)>.20:result['flags'].append('pitch_parameter_sensitive')
            if len(fv) and np.mean((fv<90)|(fv>600))>.1:result['flags'].append('pitch_edge_band_frequent')
            result['pitch']=pf
        # HNR is a signal periodicity measure, not vocal health or perceived breathiness.
        try:
            hn=snd.to_harmonicity_cc(time_step=.01,minimum_pitch=75.0,silence_threshold=.1,periods_per_window=1.0)
            hv=hn.values.ravel();result['harmonicity_db']=quant(hv[hv>-199])
        except Exception as e:result['harmonicity_db']=None;result['flags'].append('harmonicity_unavailable:'+type(e).__name__)
        # Spectral estimates are explicitly band-limited to the analysis track.
        win=640;hop=160
        if len(y)>=win:
            frames=np.lib.stride_tricks.sliding_window_view(y,win)[::hop];frms=np.sqrt(np.mean(frames*frames,axis=1));active=db(frms)>=-45
            spec=np.abs(np.fft.rfft(frames*np.hanning(win),axis=1))**2
            freqs=np.fft.rfftfreq(win,1/16000);band=(freqs>=80)&(freqs<=8000)
            sp=spec[:,band];fq=freqs[band];den=np.sum(sp,axis=1)+1e-24
            centroid=np.sum(sp*fq,axis=1)/den
            flat=np.exp(np.mean(np.log(sp+1e-24),axis=1))/(np.mean(sp,axis=1)+1e-24)
            tb=(freqs>=500)&(freqs<=4000);xx=np.log2(freqs[tb]);xx-=np.mean(xx)
            tilt=((10*np.log10(spec[:,tb]+1e-24))@xx)/np.sum(xx*xx)
            low=(freqs>=500)&(freqs<1000);high=(freqs>=2000)&(freqs<=4000)
            ratio=10*np.log10((np.sum(spec[:,low],axis=1)+1e-24)/(np.sum(spec[:,high],axis=1)+1e-24))
            result['spectral']={'centroid_hz':quant(centroid[active]),'flatness':quant(flat[active]),
                                'tilt_db_per_octave':quant(tilt[active]),'low_to_high_band_power_db':quant(ratio[active]),
                                'energy_active_frame_count':int(np.sum(active))}
        else:result['spectral']=None;result['flags'].append('too_short_for_spectral_window')
        # Retain source-addressed rate proxies for each association, not an invented transcript.
        rates=[]
        for rr in refs:
            l,r=rr['line'],rr['render'];lang=r['voice_language'];t=witness(l,lang);units,label=text_units(t,lang)
            rates.append({'semantic_voice_occurrence_id':l['semantic_voice_occurrence_id'],
                          'render_analysis_id':r['render_analysis_id'],'text_key':l.get('text_key'),
                          'voice_language':lang,'record_class':l.get('record_class'),'source_state_key':l.get('state_key'),
                          'unit_definition':label,'units':units,
                          'units_per_object_second':units/dur if units else None,
                          'units_per_energy_active_second_minus45':units/result['gates']['-45']['active_seconds'] if units and result['gates']['-45']['active_seconds']>0 else None,
                          'text_sha256':hashlib.sha256(t.encode()).hexdigest()})
        result['source_linked_rate_proxies']=rates
        result['status']='measured'
    except Exception as e:
        result['status']='failed';result['error']=type(e).__name__+': '+str(e)
    return result

def run(args):
    root=Path(args.source_dir);work=Path(args.work_dir);objects=work/'objects';results=work/'results'
    objects.mkdir(parents=True,exist_ok=True);results.mkdir(parents=True,exist_ok=True)
    cross=read_jsonl(root/'DRIVE_AUDIO_OBJECT_CROSSWALK.jsonl')
    lines=read_jsonl(root/'COMPLETE_VOICE_LINE_ANALYSIS.jsonl')
    cp=root/'COUNTERPART_COMPLETE_VOICE_LINE_ANALYSIS.jsonl'
    if cp.exists():lines+=read_jsonl(cp)
    refs=defaultdict(list)
    for l in lines:
        for r in l['renders']:refs[r['canonical_pcm_sha256']].append({'line':l,'render':r})
    manifest=json.loads((root/'SIGRIKA_RELEASE_MANIFEST.json').read_text())
    m={Path(r['drive_relative_path']).name:r for r in manifest['physical_files'] if r['drive_relative_path'].endswith('.zip')}
    shard_audit=[];jobs=[]
    group=defaultdict(list)
    for o in cross:group[Path(o['drive_relative_path']).name].append(o)
    for name,items in sorted(group.items()):
        zp=Path(args.shard_dir)/name
        if not zp.exists():
            shard_audit.append({'name':name,'status':'not_materialized'});continue
        actual=sha(zp);expected=m.get(name,{}).get('sha256')
        if actual!=expected:raise ValueError(f'Shard hash mismatch: {name}')
        with zipfile.ZipFile(zp) as z:
            members=z.namelist()
            if len(members)!=len(set(members)):raise ValueError(f'Duplicate archive member: {name}')
            selected={o['archive_member_path'] for o in items};extras=set(members)-selected
            if extras:raise ValueError(f'Unexpected shard members: {name}: {extras}')
            for o in items:
                h=o['canonical_pcm_sha256'];out=objects/(h+'.flac')
                if not out.exists():
                    blob=z.read(o['archive_member_path'])
                    if hashlib.sha256(blob).hexdigest()!=o['flac_sha256']:raise ValueError('FLAC checksum mismatch '+h)
                    out.write_bytes(blob)
                elif sha(out)!=o['flac_sha256']:raise ValueError('Existing FLAC checksum mismatch '+h)
                rp=results/(h+'.json')
                if not rp.exists() or args.redo:jobs.append((str(out),o,refs[h]))
        shard_audit.append({'name':name,'status':'sha256_verified','sha256':actual,'bytes':zp.stat().st_size,'selected_objects':len(items)})
    (work/'SHARD_ACQUISITION_AUDIT.json').write_text(json.dumps(shard_audit,indent=2))
    env={'analysis_version':VERSION,'parameters':PARAMS,'python':sys.version,'platform':platform.platform(),
         'numpy':np.__version__,'scipy':scipy.__version__,'soundfile':sf.__version__,
         'libsndfile':sf.__libsndfile_version__,'parselmouth':parselmouth.__version__,'praat':parselmouth.PRAAT_VERSION}
    (work/'AUDIO_METHOD_PARAMETERS.json').write_text(json.dumps(env,indent=2))
    if args.limit:jobs=jobs[:args.limit]
    print(f'{len(jobs)} objects to analyze; {sum(a["status"]=="sha256_verified" for a in shard_audit)}/{len(group)} shards verified',flush=True)
    started=time.time();done=0
    with concurrent.futures.ProcessPoolExecutor(max_workers=args.workers) as pool:
        for res in pool.map(analyze_one,jobs,chunksize=8):
            (results/(res['canonical_pcm_sha256']+'.json')).write_text(json.dumps(res,ensure_ascii=False,allow_nan=False,sort_keys=True),encoding='utf-8')
            done+=1
            if done%50==0 or res['status']!='measured':print(f'{done}/{len(jobs)} {time.time()-started:.1f}s status={res["status"]} '+res.get('error',''),flush=True)
    all_results=[]
    for o in cross:
        rp=results/(o['canonical_pcm_sha256']+'.json')
        if rp.exists():all_results.append(json.loads(rp.read_text()))
    with (work/'AUDIO_OBJECT_MEASUREMENTS.jsonl').open('w',encoding='utf-8') as f:
        for r in all_results:f.write(json.dumps(r,ensure_ascii=False,sort_keys=True,allow_nan=False)+'\n')
    print(f'Finished: {len(all_results)}/{len(cross)} results; failures={sum(r["status"]!="measured" for r in all_results)}',flush=True)

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source-dir',required=True);parser.add_argument('--shard-dir',required=True);parser.add_argument('--work-dir',required=True)
    parser.add_argument('--workers',type=int,default=4);parser.add_argument('--limit',type=int);parser.add_argument('--redo',action='store_true')
    run(parser.parse_args())
