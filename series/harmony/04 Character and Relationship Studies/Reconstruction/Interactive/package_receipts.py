"""Package actual Harmony runs; stdlib only, no source media or credentials.

Pass the directory containing the seven named runtime directories below and a
NEW output directory. Raw artifact hashes are checked before public projection.
Plugin catalog query cursors in incidental stderr warnings are redacted with
their unmodified raw hashes retained; no response, condition or event is edited.
"""
import argparse
import datetime as dt
import hashlib
import json
from pathlib import Path
import re

INITIAL = [('initial-001','original'),('successors-001','successor'),('keita-successor-001','successor')]
ADAPTIVE = [('adaptive-first-six-001','original',6),('adaptive-first-four-001','original',6),('adaptive-final-ten-001','original',7),('keita-successor-coreknowledge-001','successor',6)]

def sha(data): return hashlib.sha256(data).hexdigest()
def load(path): return json.loads(path.read_bytes())
def save(path,obj): path.write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')

def package(runs,out):
    out.mkdir(parents=True,exist_ok=False)
    sessions={}; receipts=[]; manifests=[]
    def stream(path,expected,kind):
        data=path.read_bytes()
        assert sha(data)==expected,(str(path),expected,sha(data))
        text=data.decode('utf-8')
        if kind=='stderr':
            projected=re.sub(r'https://chatgpt\.com/backend-api/ps/plugins/list\?[^\s]+','https://chatgpt.com/backend-api/ps/plugins/list?[REDACTED_CATALOG_QUERY]',text)
        else: projected=text
        assert not re.search(r'[A-Za-z]:\\(?:Users|Anime Media)',projected),path.name
        return {'raw_sha256':expected,'raw_bytes':len(data),'projection':'EXACT' if text==projected else 'CATALOG_QUERY_REDACTED','text':projected}
    def addturn(run,cid,phase,n,record,folder,prefix):
        key=phase+':'+cid
        assert record.get('returncode')==0 and not record.get('timed_out') and not record.get('unexpected_items'),(run,cid,n)
        assert not record.get('parse_error'),(run,cid,n)
        if prefix:
            paths=[folder/(prefix+'.input.txt'),folder/(prefix+'.events.jsonl'),folder/(prefix+'.stderr.txt')]
        else: paths=[folder/'input.txt',folder/'events.jsonl',folder/'stderr.txt']
        streams={kind:stream(path,record[field],kind) for kind,path,field in zip(['input','events','stderr'],paths,['input_sha256','events_sha256','stderr_sha256'])}
        events=[json.loads(line) for line in streams['events']['text'].splitlines()]
        ids=[e['thread_id'] for e in events if e.get('type')=='thread.started']
        assert ids==[sessions[key]['session_id']]
        actual=[e['item']['text'] for e in events if e.get('type')=='item.completed' and e.get('item',{}).get('type')=='agent_message']
        assert actual==record['responses'] and actual
        assert any(e.get('type')=='turn.completed' for e in events)
        usage=[e['usage'] for e in events if e.get('type')=='turn.completed']
        turn={'turn':n,'run':run,'started_utc':record['started_utc'],'elapsed_seconds':record['elapsed_seconds'],'interlocutor':record.get('interlocutor',record.get('case',{}).get('prompt')),'responses':actual,'usage_cumulative_session':usage,'input_sha256':record['input_sha256'],'events_sha256':record['events_sha256'],'stderr_sha256':record['stderr_sha256'],'execution':'COMPLETED_ZERO_EXIT_NO_TOOL_ITEMS'}
        if 'case' in record: turn['independent_adaptive_selection']=record['case']
        sessions[key]['turns'].append(turn)
        receipts.append({'session_key':key,'turn':n,'run':run,'streams':streams})
    for run,phase in INITIAL:
        folder=runs/run; manifest=load(folder/'run_manifest.json')
        assert all(r['status']=='EXECUTED_AWAITING_INDEPENDENT_EVALUATION' for r in manifest['results'])
        manifests.append({'run':run,'raw_manifest_sha256':sha((folder/'run_manifest.json').read_bytes()),'manifest':manifest})
        for result in sorted(manifest['results'],key=lambda x:x['id']):
            cid=result['id']; c=load(folder/cid/'conversation.json'); key=phase+':'+cid
            assert key not in sessions and len(c['turns'])==5
            sessions[key]={'key':key,'subject':cid,'phase':phase,'session_id':result['session_id'],'case':c['case'],'initial_run':run,'turns':[]}
            for t in c['turns']: addturn(run,cid,phase,t['turn'],t,folder/cid,'turn-%02d'%t['turn'])
    for run,phase,n in ADAPTIVE:
        folder=runs/run; manifest=load(folder/'run_manifest.json')
        assert all(r['status']=='EXECUTED_AWAITING_INDEPENDENT_EVALUATION' for r in manifest['results'])
        manifests.append({'run':run,'raw_manifest_sha256':sha((folder/'run_manifest.json').read_bytes()),'manifest':manifest})
        for result in sorted(manifest['results'],key=lambda x:x['id']):
            cid=result['id']; c=load(folder/cid/'conversation.json'); key=phase+':'+cid
            assert sessions[key]['case']['policy_sha256']==c['case']['policy_sha256']
            assert sessions[key]['session_id']==c['case']['session_id']
            addturn(run,cid,phase,n,c,folder/cid,None)
    ordered=[sessions[k] for k in sorted(sessions)]
    assert len(ordered)==15 and len({s['session_id'] for s in ordered})==15
    for s in ordered:
        s['turns'].sort(key=lambda t:t['turn'])
        assert [t['turn'] for t in s['turns']]==list(range(1,(7 if s['phase']=='original' else 6 if s['subject']=='keita' else 5)+1))
    count=sum(len(s['turns']) for s in ordered)
    assert count==96,count
    final_usage={}
    for s in ordered:
        for k,v in s['turns'][-1]['usage_cumulative_session'][-1].items(): final_usage[k]=final_usage.get(k,0)+v
    report={'schema':'harmony-actual-interactions/v1','counts':{'subjects':10,'distinct_sessions':15,'original_turns':70,'successor_turns':26,'actual_responses':count,'source_retrospective_cases_separate':32},'interpretation':'Original10 policies each executed five fixed turns plus two independent observed-response-adaptive turns. Five corrected policies each rerun in a fresh five-turn context; Keita additionally receives an independent targeted positive-knowledge probe. All are source-exposed bounded tests, not blind predictions.','usage_note':'CLI usage increases cumulatively within each resumed UUID. Aggregate uses each distinct UUID final counter once; no billing cost inferred.','sum_final_session_usage':final_usage,'sessions':ordered}
    save(out/'interactions.json',report)
    save(out/'runtime_receipt.json',{'schema':'harmony-actual-runtime-receipts/v1','projection_note':'Full authored inputs and stdout exact. Stderr exact except remote plugin catalog query cursors removed where present; raw hash/length retained. Local execution files retain originals. No character response edited.','manifests':manifests,'turns':receipts})
    save(out/'session_context_index.json',{'sessions':[{'id':s['key'],'session_id':s['session_id'],'initial_input_sha256':s['turns'][0]['input_sha256']} for s in ordered]})
    print(json.dumps({'sessions':15,'turns':count,'stderr_redactions':sum(r['streams']['stderr']['projection']!='EXACT' for r in receipts),'final_session_usage':final_usage}))

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--runs-root',type=Path,required=True)
    p.add_argument('--out',type=Path,required=True)
    a=p.parse_args(); package(a.runs_root,a.out)
