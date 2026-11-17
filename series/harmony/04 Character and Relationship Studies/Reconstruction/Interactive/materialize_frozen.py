"""Reconstruct an exact historical harness tree without Git ancestry.

Use --repo ROOT --freeze original|successors|keita-successor --out NEW_DIRECTORY.
Archived UTF-8 policy payloads recover original/tested versions after protected
squash integration. Every manifest hash is checked. Existing output is refused.
This reconstructs inputs; it does not promise deterministic model responses.
"""
import argparse,hashlib,json
from pathlib import Path,PurePosixPath

def sha(b): return hashlib.sha256(b).hexdigest()
def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--repo',type=Path,required=True)
    p.add_argument('--freeze',choices=['original','successors','keita-successor'],required=True)
    p.add_argument('--out',type=Path,required=True)
    a=p.parse_args(); root=a.repo.resolve()
    relative=Path('series/harmony/04 Character and Relationship Studies/Reconstruction')
    home=root/relative
    names={'original':'HARMONY_G5_FREEZE_V1.json','successors':'HARMONY_G5_SUCCESSOR_FREEZE_V1_1.json','keita-successor':'HARMONY_G5_KEITA_SUCCESSOR_FREEZE_V1_1.json'}
    manifest=json.loads((home/names[a.freeze]).read_bytes())
    archived={}
    for name in ['HARMONY_G5_ORIGINAL_V1_POLICIES.json','HARMONY_G5_KEITA_ORIGINAL_V1.json','HARMONY_G5_TESTED_V1_1_PAYLOADS.json']:
        for item in json.loads((home/name).read_bytes())['policies']:
            data=item['content_utf8'].encode('utf-8'); assert sha(data)==item['sha256']
            archived[(item['path'],item['sha256'])]=data
    files={r['path']:r for r in manifest['files']}
    # Successor manifests list only changed inputs; original manifest supplies
    # the unchanged runner/protocol and other inputs required for execution.
    if a.freeze!='original':
        original=json.loads((home/names['original']).read_bytes())
        files={**{r['path']:r for r in original['files']},**files}
    prepared=[]
    for path,item in files.items():
        parts=PurePosixPath(path)
        assert not parts.is_absolute() and '..' not in parts.parts and path.startswith('series/harmony/'),path
        data=(root/Path(*parts.parts)).read_bytes()
        if sha(data)!=item['sha256']: data=archived[(path,item['sha256'])]
        assert sha(data)==item['sha256'] and len(data)==item['bytes']
        prepared.append((path,data))
    a.out.mkdir(parents=True,exist_ok=False)
    for path,data in prepared:
        target=a.out/Path(*PurePosixPath(path).parts); target.parent.mkdir(parents=True,exist_ok=True); target.write_bytes(data)
    print(json.dumps({'files_materialized':len(prepared),'freeze':a.freeze,'all_hashes_verified':True}))
if __name__=='__main__': main()
