"""Export selected, public-safe observations from local Codex session traces.
Input: {sessions:[{id,session_id,initial_input_sha256}]}.
The input SHA identifies where host context ends and authored test input starts.
No full host bodies, cwd, account IDs or credentials are exported.
"""
import argparse
import datetime as dt
import hashlib
import json
from pathlib import Path

def digest(text):
    return hashlib.sha256(text.encode('utf-8')).hexdigest()

p=argparse.ArgumentParser(description=__doc__)
p.add_argument('--index',type=Path,required=True)
p.add_argument('--sessions-root',type=Path,required=True)
p.add_argument('--out',type=Path,required=True)
a=p.parse_args()
index=json.loads(a.index.read_bytes())
records=[]
for requested in index['sessions']:
    sid=requested['session_id']
    matches=list(a.sessions_root.rglob('*'+sid+'*.jsonl'))
    if len(matches)!=1:
        raise ValueError('Expected exactly one trace for '+requested['id'])
    events=[json.loads(line) for line in matches[0].read_text(encoding='utf-8').splitlines()]
    meta=next(e['payload'] for e in events if e.get('type')=='session_meta')
    base=meta.get('base_instructions','')
    base_text=base.get('text','') if isinstance(base,dict) else str(base)
    contexts=[]
    for e in events:
        if e.get('type')=='turn_context':
            v=e['payload']
            contexts.append({k:v.get(k) for k in ['model','effort','approval_policy','sandbox_policy']})
    host=[]
    found=False
    for e in events:
        if e.get('type')=='response_item' and e.get('payload',{}).get('type')=='message':
            v=e['payload']; text='\n'.join(x.get('text','') for x in v.get('content',[]))
            if digest(text)==requested['initial_input_sha256']:
                found=True;break
            host.append({'role':v.get('role'),'text_utf8_sha256':digest(text),'characters':len(text),'skills_catalog_present':'Available skills' in text,'repository_operating_card_present':'Repository operating card' in text})
    if not found:
        raise ValueError('Authored first prompt hash not found in trace: '+requested['id'])
    records.append({'id':requested['id'],'session_id':sid,'session_meta_cli_version':meta.get('cli_version'),'model_provider':meta.get('model_provider'),'context_window_exposed':meta.get('context_window'),'local_base_instruction_text_sha256':digest(base_text),'initial_host_messages':host,'observed_turn_contexts':contexts})
result={'schema':'character-runtime-context-observations/v1','observed_utc':dt.datetime.now(dt.timezone.utc).isoformat(),'export_boundary':'Selected exposed context fields only. Private absolute paths, account IDs and full host instruction bodies omitted; body digests retained. This is not an assertion of server system prompt access.','sessions':records}
with a.out.open('x',encoding='utf-8',newline='\n') as f:
    f.write(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'sessions':len(records),'turn_contexts':sum(len(r['observed_turn_contexts']) for r in records),'sha256':hashlib.sha256(a.out.read_bytes()).hexdigest()}))
