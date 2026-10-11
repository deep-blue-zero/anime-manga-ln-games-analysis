#!/usr/bin/env python3
"""Aggregate Sigrika measurements, normalize within language, and nominate review cases.
No emotion labels are inferred. Source-defined cohorts are not acoustic clusters.
"""
from __future__ import annotations
import json, math, re, hashlib, sys
from collections import Counter, defaultdict
from pathlib import Path
import numpy as np
import scipy.stats as stats
from sklearn.linear_model import HuberRegressor
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score, silhouette_score
import sklearn
from analyze_audio import read_jsonl,quant,text_units,witness,clean_text

if len(sys.argv)!=2:
    raise SystemExit('Usage: python summarize_audio.py WORK_DIRECTORY')
W=Path(sys.argv[1]).resolve()
S=W/'source'
R=read_jsonl(W/'AUDIO_OBJECT_MEASUREMENTS.jsonl');rmap={r['canonical_pcm_sha256']:r for r in R}
L=read_jsonl(S/'COMPLETE_VOICE_LINE_ANALYSIS.jsonl');C=read_jsonl(S/'COUNTERPART_COMPLETE_VOICE_LINE_ANALYSIS.jsonl')
lmap={l['semantic_voice_occurrence_id']:l for l in L+C};direct={l['semantic_voice_occurrence_id'] for l in L}

def qc(r):
    return r['status']=='measured' and r['channels']==1 and r.get('pitch') and r['pitch']['n']>=10 and not any(f in r['flags'] for f in ['pitch_parameter_sensitive','pitch_edge_band_frequent'])

def subtype(l):
    if l['record_class']=='story_dialogue':return 'story_dialogue'
    m=re.search(r'FavorWord_1412(\d\d)',l.get('text_key') or '')
    i=int(m[1]) if m else 0
    if 1<=i<=18:return 'archive_conversation_01_18'
    if 19<=i<=22:return 'archive_idle_intro_19_22'
    if 23<=i<=31:return 'archive_greeting_team_ascension_23_31'
    return 'archive_gameplay_32_73'

def lexical_units(t,lang):
    t=clean_text(t).strip()
    if re.fullmatch(r'[（(\[].*[）)\]]',t,flags=re.S):return None,'nonlexical_parenthetical_annotation'
    return text_units(t,lang)

flat=[]
for scope,lines in [('direct_character',L),('dark_side_counterpart',C)]:
    for l in lines:
        for a in l['renders']:
            r=rmap[a['canonical_pcm_sha256']];lang=a['voice_language'];units,label=lexical_units(witness(l,lang),lang)
            g=r['gates']['-45'];p=r['pitch'] or {}
            x={'scope':scope,'language':lang,'semantic_id':l['semantic_voice_occurrence_id'],
               'render_id':a['render_analysis_id'],'pcm':r['canonical_pcm_sha256'],'flac_sha256':r['flac_sha256'],
               'source_locator':l['source_locator'],'text_key':l.get('text_key'),'state_key':l.get('state_key'),
               'source_class':l['record_class'],'source_subclass':subtype(l),'duration':r['duration_seconds'],
               'units':units,'unit_definition':label,'channels':r['channels'],'pitch_qc_qualified':bool(qc(r)),
               'f0_hz':p.get('median'),'f0_range_st':p.get('robust_range_semitones'),
               'active_frame_median_dbfs':g['active_frame_energy_dbfs']['median'],'rms_dbfs':r['rms_dbfs'],
               'silent_fraction':g['silent_fraction'],'active_seconds':g['active_seconds'],
               'leading_seconds':g['leading_seconds'],'trailing_seconds':g['trailing_seconds'],
               'internal_gap_seconds':g['internal_gap_seconds'],'internal_gap_count':g['internal_gap_count'],
               'gap_density':g['internal_gaps_per_second'],
               'hnr_db':r['harmonicity_db']['median'] if r['harmonicity_db'] else None,
               'centroid_hz':r['spectral']['centroid_hz']['median'] if r['spectral'] else None,
               'spectral_tilt_db_octave':r['spectral']['tilt_db_per_octave']['median'] if r['spectral'] else None,
               'f0_last_minus_first_third_st':p.get('last_minus_first_third_semitones'),
               'lexical_units_per_second':units/r['duration_seconds'] if units else None,
               'lexical_units_per_active_second':units/g['active_seconds'] if units and g['active_seconds'] else None,
               'flags':r['flags']}
            flat.append(x)

# A semantic association is preserved, but object-weighted fits do not duplicate shared PCM.
fits=[]
for lang in ['zh','en','ja','ko']:
    for sub in sorted({f['source_subclass'] for f in flat if f['scope']=='direct_character'}):
        arr=[f for f in flat if f['scope']=='direct_character' and f['language']==lang and f['source_subclass']==sub and f['channels']==1 and f['units'] and f['units']>=2]
        arr=list({f['pcm']:f for f in arr}.values())
        if len(arr)<8:continue
        X=np.log([f['units'] for f in arr]).reshape(-1,1)
        for outcome in ['duration','active_seconds']:
            selected=[i for i,f in enumerate(arr) if f[outcome]>.05]
            if len(selected)<8:continue
            model=HuberRegressor(epsilon=1.35,alpha=0.,max_iter=1000).fit(X[selected],np.log([arr[i][outcome] for i in selected]))
            fit={'language':lang,'source_subclass':sub,'outcome':outcome,'n_unique_fit_objects':len(selected),'intercept':float(model.intercept_),'slope':float(model.coef_[0]),'huber_epsilon':1.35,'unit_definition':arr[0]['unit_definition']}
            fits.append(fit)
            for f in flat:
                if f['scope']=='direct_character' and f['language']==lang and f['source_subclass']==sub and f['units'] and f[outcome]>.05:
                    f[outcome+'_log_residual']=float(np.log(f[outcome])-(model.intercept_+model.coef_[0]*np.log(f['units'])))

# Within-language percentiles use unique mono direct objects; pitch additionally uses the QC gate.
for lang in ['zh','en','ja','ko']:
    arr=list({f['pcm']:f for f in flat if f['scope']=='direct_character' and f['language']==lang and f['channels']==1}.values())
    for feature in ['f0_hz','f0_range_st','active_frame_median_dbfs','silent_fraction','duration_log_residual','gap_density']:
        baseline=np.array([f[feature] for f in arr if f.get(feature) is not None and (not feature.startswith('f0') or f['pitch_qc_qualified'])])
        if not len(baseline):continue
        for f in flat:
            if f['scope']=='direct_character' and f['language']==lang and f.get(feature) is not None:
                f[feature+'_within_language_percentile']=float(stats.percentileofscore(baseline,f[feature],kind='mean'))

summary={'schema_version':'sigrika.audio-summary.v0.2','measurement_basis':'new native FLAC decoding and waveform analysis',
         'total_unique_objects':len(R),'failures':[r for r in R if r['status']!='measured'],
         'total_verified_shards':sum(x['status']=='sha256_verified' for x in json.loads((W/'SHARD_ACQUISITION_AUDIT.json').read_text())),
         'source_wem_redecode_performed':False,'human_perceptual_review_performed':False,'video_review_performed':False,
         'scopes':{},'by_language':{},'by_language_source_subclass':{},'normalization_fits':fits,
         'pitch_qc_rule':'mono; >=10 voiced frames; <=20% matched frames differ >3 semitones across settings; <=10% voiced frames in edge bands (<90 or >600 Hz)',
         'software':{'sklearn':sklearn.__version__},'method_file':'AUDIO_METHOD_PARAMETERS.json'}
fields=['duration','f0_hz','f0_range_st','active_frame_median_dbfs','rms_dbfs','silent_fraction','leading_seconds','trailing_seconds','internal_gap_seconds','gap_density','hnr_db','centroid_hz','spectral_tilt_db_octave','lexical_units_per_second','lexical_units_per_active_second','duration_log_residual']

def group_stats(arr):
    arr=list({f['pcm']:f for f in arr}.values());ret={'unique_objects':len(arr),'duration_sum_seconds':sum(f['duration'] for f in arr),'pitch_qc_qualified':sum(f['pitch_qc_qualified'] for f in arr)}
    for key in fields:
        ret[key]=quant([f[key] for f in arr if f.get(key) is not None])
    ret['qc_f0_hz']=quant([f['f0_hz'] for f in arr if f['pitch_qc_qualified']]);ret['qc_f0_range_st']=quant([f['f0_range_st'] for f in arr if f['pitch_qc_qualified']])
    return ret

for scope,lines in [('direct_character',L),('dark_side_counterpart',C)]:
    arr=[r for r in R if scope in r['evidence_scopes']]
    summary['scopes'][scope]={'semantic_lines':len(lines),'render_associations':sum(len(l['renders']) for l in lines),
        'unique_objects':len(arr),'flac_bytes':sum(r['integrity']['flac_bytes'] for r in arr),
        'duration_sum_seconds':sum(r['duration_seconds'] for r in arr),'channel_counts':dict(Counter(r['channels'] for r in arr)),
        'flags':dict(Counter(f for r in arr for f in r['flags'])),
        'pitch_qc_qualified':sum(bool(qc(r)) for r in arr),
        'integrity_pass_count':sum(r['integrity']['flac_sha256_match'] and r['integrity']['native_pcm_payload_match'] for r in arr)}
    for lang in ['zh','en','ja','ko']:
        summary['by_language'][scope+':'+lang]=group_stats([f for f in flat if f['scope']==scope and f['language']==lang])
        if scope=='direct_character':
            for sub in sorted({f['source_subclass'] for f in flat if f['scope']==scope}):
                summary['by_language_source_subclass'][lang+':'+sub]=group_stats([f for f in flat if f['scope']==scope and f['language']==lang and f['source_subclass']==sub])
summary['prior_signal_validation']={key:max(r['prior_measurement_comparison'][key] for r in R) for key in ['duration_max_abs_error','rms_dbfs_max_abs_error','peak_dbfs_max_abs_error']}

# Context-defined cohorts use literal source addresses, not acoustic emotion labels.
def address(l):
    m=re.search(r'#/([0-9]+)/Actions!/([0-9]+)/Params/TalkItems/([0-9]+)',l['source_locator'] or '')
    return tuple(map(int,m.groups())) if m else None
cohort_rules=[
 ('SIG-AC-01','After-nightmare self-blame and request for help','SIG-E22',lambda l: address(l) and address(l)[:2]==(12423,4)),
 ('SIG-AC-02','Admitting the weight of expectations and choosing action','SIG-E25',lambda l: address(l) and address(l)[:2]==(12966,3) and address(l)[2]>=28),
 ('SIG-AC-03','Rooftop retreat and request for company','SIG-E31',lambda l: address(l) and address(l)[:2]==(15255,6)),
 ('SIG-AC-04','Later rooftop break and chosen activities','SIG-E31',lambda l: address(l) and address(l)[:2]==(15256,4)),
 ('SIG-AC-05','Birdwatching, photographic mistakes, and return to training','SIG-E30',lambda l: address(l) and address(l)[:2]==(15252,4)),
 ('SIG-AC-06','Denia birthday: noticing differences and asking about next year','SIG-E47',lambda l: address(l) and address(l)[:2]==(12586,7) and 12<=address(l)[2]<=33),
 ('SIG-AC-07','Earlier childhood game converted to repeated victory','SIG-E13',lambda l: address(l) and address(l)[0] in [12406,12407]),
 ('SIG-AC-08','Post-resolution festival thanks, candy, birds, and photograph','SIG-E27',lambda l: address(l) and address(l)[:2]==(12437,4)),
]
cohorts=[]
for cid,label,ev,rule in cohort_rules:
    ids=[l['semantic_voice_occurrence_id'] for l in L if rule(l)]
    group={'id':cid,'label':label,'textual_evidence_bundle':ev,'label_basis':'source/context, not inferred from sound','semantic_ids':ids,'semantic_line_count':len(ids),'languages':{}}
    for lang in ['zh','en','ja','ko']:
        arr=[f for f in flat if f['scope']=='direct_character' and f['language']==lang and f['semantic_id'] in ids]
        gs=group_stats(arr)
        gs['f0_percentile_median']=quant([f['f0_hz_within_language_percentile'] for f in arr if f['pitch_qc_qualified']])['median']
        gs['active_energy_percentile_median']=quant([f['active_frame_median_dbfs_within_language_percentile'] for f in arr if f.get('active_frame_median_dbfs_within_language_percentile') is not None])['median']
        group['languages'][lang]=gs
    cohorts.append(group)
summary['context_cohorts']=cohorts

# Matched semantic cases: actually acquired audio, with all localization texts retained.
selected_addresses=[(12423,4,2),(12423,4,8),(12423,4,24),(12423,4,33),(12966,3,28),(12966,3,32),(12966,3,34),(12966,3,36),(15255,6,11),(15256,4,6),(15256,4,9),(12586,7,17),(12586,7,20),(12586,7,22)]
selected_keys=['FavorWord_141201_Content','FavorWord_141204_Content','FavorWord_141205_Content','FavorWord_141208_Content','FavorWord_141215_Content','FavorWord_141221_Content']
case_lines=[l for l in L if address(l) in selected_addresses or l.get('text_key') in selected_keys]
case_lines.sort(key=lambda l:(0,selected_addresses.index(address(l))) if address(l) in selected_addresses else (1,selected_keys.index(l['text_key'])))
cases=[]
for i,l in enumerate(case_lines,1):
    cases.append({'id':f'SIG-AM-{i:02d}','semantic_id':l['semantic_voice_occurrence_id'],'text_key':l['text_key'],'source_locator':l['source_locator'],
      'localized_texts':{lang:witness(l,lang) for lang in ['zh','en','ja','ko']},'mapping_relation':'same semantic occurrence, not certified sample-level multilingual edit equivalence',
      'perceptual_review_status':'not_performed','machine_review_status':'measured',
      'renders':[f for f in flat if f['semantic_id']==l['semantic_voice_occurrence_id']]})

# Acoustic clusters are descriptive, language-normalized review organizers only.
clusters=[];feat=['f0_hz','f0_range_st','active_frame_median_dbfs','silent_fraction','duration_log_residual','hnr_db','centroid_hz']
for lang in ['zh','en','ja','ko']:
    arr=list({f['pcm']:f for f in flat if f['scope']=='direct_character' and f['language']==lang and f['pitch_qc_qualified'] and all(f.get(k) is not None for k in feat)}.values())
    X=np.array([[math.log(f[k]) if k=='f0_hz' else f[k] for k in feat] for f in arr]);med=np.median(X,axis=0);iqr=np.quantile(X,.75,axis=0)-np.quantile(X,.25,axis=0);iqr[iqr<1e-8]=1
    Z=np.clip((X-med)/iqr,-5,5)
    km=KMeans(n_clusters=3,n_init=30,random_state=7).fit(Z);alt=KMeans(n_clusters=3,n_init=30,random_state=19).fit(Z);k4=KMeans(n_clusters=4,n_init=30,random_state=7).fit(Z)
    group={'language':lang,'n':len(arr),'features':feat,'log_transform':['f0_hz'],'scaling':'within-language median/IQR; clip [-5,5]',
           'k':3,'random_seed':7,'n_init':30,'seed_stability_ari':float(adjusted_rand_score(km.labels_,alt.labels_)),
           'k3_vs_k4_ari':float(adjusted_rand_score(km.labels_,k4.labels_)),
           'silhouette':float(silhouette_score(Z,km.labels_,sample_size=min(500,len(arr)),random_state=7)),
           'interpretation':'no emotion, state, sincerity, or personality labels','clusters':[]}
    for k in range(3):
        ii=np.flatnonzero(km.labels_==k);j=ii[np.argmin(np.linalg.norm(Z[ii]-km.cluster_centers_[k],axis=1))]
        sub=[arr[t] for t in ii]
        group['clusters'].append({'cluster_id':k,'n':len(ii),'normalized_center':dict(zip(feat,[float(v) for v in km.cluster_centers_[k]])),
             'raw_feature_medians':{f:float(np.median([a[f] for a in sub])) for f in feat},
             'representative':arr[j],'source_subclass_counts':dict(Counter(a['source_subclass'] for a in sub)),
             'top_source_states':Counter(a['state_key'] or 'archive' for a in sub).most_common(5)})
    clusters.append(group)
summary['clustering']=clusters

# Outlier nominations preserve exact identity and are already measured, never 'not acquired'.
outliers=[]
for lang in ['zh','en','ja','ko']:
    arr=list({f['pcm']:f for f in flat if f['scope']=='direct_character' and f['language']==lang}.values())
    for name,key,largest,qual in [('longest','duration',True,False),('lowest_rms','rms_dbfs',False,False),('largest_positive_duration_residual','duration_log_residual',True,False),('widest_qc_pitch_range','f0_range_st',True,True)]:
        eligible=[f for f in arr if f.get(key) is not None and (not qual or f['pitch_qc_qualified'])]
        pick=sorted(eligible,key=lambda f:f[key],reverse=largest)[0]
        outliers.append({'id':f'SIG-AO-{len(outliers)+1:02d}','language':lang,'selection':name,'measure':key,'value':pick[key],
                         'record':pick,'status':'acquired_decoded_measured; perceptual_review_open'})
summary['outlier_nominations']=outliers

# Missing audio is a source-mapping boundary, not a failed audio download.
O=read_jsonl(S/'occurrence_identity_crosswalk.jsonl')
gaps=[]
for row,act,label in [(12967,1,'final this-time declaration'),(16901,4,'later telephone/ordinary-state conversation'),(16826,2,'later fulfilling-life/nonreturn conversation')]:
    rows=[o for o in O if o['flow_state_row_index']==row and o['action_index']==act and o['character_attribution']=='accepted_solo']
    gaps.append({'row':row,'action':act,'label':label,'accepted_direct_occurrences':len(rows),'play_voice_counts':dict(Counter(str(o['play_voice']) for o in rows)),
                 'mapped_media_associations':sum(o['resolved_media_association_count'] for o in rows),
                 'scope':'no accepted line-level recording in this pinned mapping; does not establish absence of audio in future video witness',
                 'text_keys':[o['text_key'] for o in rows]})
summary['diagnostic_unvoiced_boundaries']=gaps

for name,data in [('AUDIO_WAVEFORM_ANALYSIS_SUMMARY.json',summary),('AUDIO_MATCHED_SEMANTIC_CASES.json',cases),('AUDIO_CONTEXT_COHORTS.json',cohorts),('AUDIO_CLUSTER_RESULTS.json',clusters),('AUDIO_OUTLIER_REVIEW_COHORT.json',outliers)]:
    (W/name).write_text(json.dumps(data,indent=2,ensure_ascii=False,allow_nan=False),encoding='utf-8')
with (W/'AUDIO_ASSOCIATION_FEATURES.jsonl').open('w',encoding='utf-8') as f:
    for row in flat:f.write(json.dumps(row,sort_keys=True,ensure_ascii=False,allow_nan=False)+'\n')
print(json.dumps({'scopes':summary['scopes'],'cases':len(cases),'associations':len(flat),'clusters':[{k:g[k] for k in ['language','n','seed_stability_ari','k3_vs_k4_ari','silhouette']} for g in clusters],'unvoiced':gaps},ensure_ascii=False,indent=2))
