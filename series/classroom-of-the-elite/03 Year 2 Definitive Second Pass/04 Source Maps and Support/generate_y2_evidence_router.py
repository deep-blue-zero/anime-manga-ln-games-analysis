"""Generate the Y2SL evidence router from locked local EPUBs and frozen readings.

Requires Python 3.11+, beautifulsoup4, lxml, PyYAML. No network, source export,
or governance writes. Paths in outputs are relative to the Year 2 corpus root.
Run with --source-dir PATH; --check compares without writing either output.
The adjacent SOURCE_ROUTING_SPEC is reviewed input, not a generated output.
"""
from pathlib import Path
import argparse
import hashlib
import json
import posixpath
import re
import unicodedata
import zipfile
import xml.etree.ElementTree as ET
import yaml
from bs4 import BeautifulSoup

HERE = Path(__file__).resolve().parent
BASE = HERE.parent
SERIALIZATION = ('UTF-8; NFKC; whitespace collapsed; ruby rt/rp removed; nonempty '
                 'p/h1-h6 in OPF order; source_code TAB canonical_spine_integer '
                 'TAB one_based_paragraph TAB text LF, including final LF. '
                 'Y2SL uses zero-based OPF integer solely for this new digest. '
                 'Distinct from the inherited fingerprint serialization.')

def sha(data):
    return hashlib.sha256(data).hexdigest()

def norm(text):
    return re.sub(r'\s+', ' ', unicodedata.normalize('NFKC', text)).strip()

def paragraphs(raw):
    soup = BeautifulSoup(raw, 'xml')
    for tag in soup.find_all(['rt', 'rp']):
        tag.decompose()
    return [v for el in soup.find_all(['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
            if (v := norm(el.get_text()))]

def rows(text, code):
    prefix = code.replace('.', '_')
    found = {}
    for line_number, line in enumerate(text.splitlines(), 1):
        cells = [c.strip().strip('`') for c in line.strip().strip('|').split('|')]
        if not line.startswith('|') or len(cells) < 4:
            continue
        if not re.fullmatch(re.escape(prefix) + r'-E\d{3}', cells[0]):
            continue
        if cells[0] in found:
            continue
        locator = cells[4] if code == 'Y2SL' else next(
            c for c in cells[1:] if 'COTE:' in c or re.search(r'\bspine\d+:para', c))
        found[cells[0]] = (locator, line_number, cells)
    return found

def generate(source_dir):
    spec = json.loads((HERE / 'COTE_Y2_SOURCE_ROUTING_SPEC.json').read_text(encoding='utf-8'))
    index, maps = [], []
    for src in spec['sources']:
        code = src['source_code']
        path = source_dir / src['source_relative_path']
        raw = path.read_bytes()
        assert len(raw) == src['source_bytes'] and sha(raw) == src['source_sha256'], code
        artifact = BASE / src['canonical_artifact']
        blob = artifact.read_bytes()
        text = blob.decode('utf-8')
        metadata = yaml.safe_load(text.split('---', 2)[1])
        evidence = rows(text, code)
        assert len(evidence) == src['expected_evidence_count'], code
        assert list(evidence) == [f"{code.replace('.', '_')}-E{i:03d}"
                                  for i in range(1, len(evidence) + 1)], code
        with zipfile.ZipFile(path) as z:
            assert z.testzip() is None, code
            names = z.namelist()
            container = ET.fromstring(z.read('META-INF/container.xml'))
            opf = next(e.attrib['full-path'] for e in container.iter()
                       if e.tag.endswith('rootfile'))
            package = ET.fromstring(z.read(opf))
            manifest = {e.attrib['id']: posixpath.normpath(posixpath.join(
                        posixpath.dirname(opf), e.attrib['href']))
                        for e in package.iter() if e.tag.endswith('}item')}
            spine = [manifest[e.attrib['idref']] for e in package.iter()
                     if e.tag.endswith('}itemref')]
            offset = src['canonical_spine_index_offset'] or 0
            values = {i + offset: paragraphs(z.read(p)) for i, p in enumerate(spine)}
            fiction = {fid: next(n for n in names if n.endswith(suffix)) for fid, suffix in
                       [('FIC1', 'Text/part0241.xhtml'), ('FIC2', 'Text/part0242.xhtml')]} if code == 'Y2SL' else {}
            aliases = src['illustration_aliases']
            for entry in aliases.values():
                assert entry['resource'] in names, (code, entry)
            entries, semantic_checks, paragraph_checks, resource_checks = [], 0, 0, 0
            for eid, (locator, line_number, cells) in evidence.items():
                resolved = []
                # Some frozen rows spell both endpoints in full; retain the
                # original locator but resolve its complete same-spine interval.
                parse_locator = re.sub(
                    r'(spine(\d+):para\d+)\s*[–—-]\s*COTE:[^:]+:spine\2:para(\d+)',
                    lambda mt: mt[1] + '-para' + mt[3], locator)
                ranges = list(re.finditer(r'(?:COTE:[A-Za-z0-9_.]+:)?spine(\d+):para(\d+)(?:\s*[–—-]\s*(?:para)?(\d+))?', parse_locator))
                for mt in ranges:
                    number, start, end = int(mt[1]), int(mt[2]), int(mt[3] or mt[2])
                    assert 1 <= start <= end <= len(values[number]), (eid, locator)
                    resolved.append({'kind': 'paragraphs', 'resource': spine[number-offset],
                                     'start': start, 'end': end})
                    paragraph_checks += 1
                for alias in dict.fromkeys(re.findall(r'ill-\d+', locator)):
                    resolved.append({'kind': 'illustration', 'alias': alias,
                                     'resource': aliases[alias]['resource']})
                    resource_checks += 1
                # Preserve an explicitly written illustration interval, including ornaments.
                interval = re.search(r'ill-(\d+)\s*-\s*COTE:[^:]+:ill-(\d+)', locator)
                if interval:
                    resolved = [{'kind': 'illustration_interval', 'resources':
                                 [aliases[f'ill-{n:02d}']['resource'] for n in
                                  range(int(interval[1]), int(interval[2])+1)]}]
                for mt in re.finditer(r'FIC([12]):P(\d+)(?:-P(\d+))?', locator):
                    fid, start, end = 'FIC'+mt[1], int(mt[2]), int(mt[3] or mt[2])
                    assert 1 <= start <= end <= len(paragraphs(z.read(fiction[fid]))), eid
                    resolved.append({'kind': 'fiction_paragraphs', 'resource': fiction[fid],
                                     'start': start, 'end': end})
                    paragraph_checks += 1
                for fname in dict.fromkeys(re.findall(r'[A-Za-z0-9_-]+\.(?:jpe?g|png|xhtml|html)', locator, re.I)):
                    matching = [n for n in names if n == fname or n.endswith('/'+fname)]
                    assert len(matching) == 1, (eid, fname)
                    resolved.append({'kind': 'resource', 'resource': matching[0]})
                    resource_checks += 1
                if code == 'Y2SL' and not resolved:
                    assert locator in ['EPUB-byte-object', 'EPUB-container', 'OPF:spine', 'OPF:manifest-images']
                    resolved.append({'kind': 'container', 'target': locator, 'opf': opf})
                assert resolved, (eid, locator)
                anchor = cells[6] if code in ['Y2V08', 'Y2V09', 'Y2V09.5'] else (
                    cells[-1].split(' Anchor: ', 1)[1] if ' Anchor: ' in cells[-1] else None)
                if anchor:
                    assert ranges, eid
                    target = ' '.join(' '.join(values[int(mt[1])][int(mt[2])-1:int(mt[3] or mt[2])]) for mt in ranges)
                    needle = re.sub(r'\s+', '', norm(anchor.rstrip('…')).rstrip('.'))
                    assert needle in re.sub(r'\s+', '', target), eid
                    semantic_checks += 1
                entry = {'id': eid, 'original_locator': locator, 'artifact_line': line_number,
                         'resolved_targets': resolved}
                if eid == 'Y2V01-E064':
                    entry['closeout_correction'] = 'Y2_12 section 6: pictured companion is Nanase, not Horikita; frozen claim preserved.'
                entries.append(entry)
            fresh = ''.join(f'{code}\t{number}\t{i}\t{value}\n'
                            for number, ps in values.items() for i, value in enumerate(ps, 1))
            mapping = {k: src[k] for k in ['source_code', 'source_filename', 'source_bytes',
                       'source_sha256', 'canonical_artifact', 'canonical_spine_index_offset']}
            mapping.update({'canonical_artifact_sha256': sha(blob), 'opf': opf,
                'historical_normalized_fingerprint': metadata.get('locator_text_sha256', metadata.get('normalized_text_sha256')),
                'historical_parser': metadata.get('locator_parser'),
                'fresh_router_text_fingerprint': sha(fresh.encode('utf-8')),
                'fresh_router_serialization': SERIALIZATION,
                'spine_map': [{'opf_position_1_based': i+1, 'canonical_spine_label':
                    None if code == 'Y2SL' else f'spine{i+offset:02d}', 'xhtml_path': p,
                    'nonempty_paragraph_records': len(values[i+offset])} for i, p in enumerate(spine)],
                'xhtml_manifest': [n for n in names if re.search(r'\.(?:html|xhtml)$', n, re.I)],
                'image_inventory': [n for n in names if re.search(r'\.(?:jpe?g|png|gif|svg|webp)$', n, re.I)],
                'illustration_aliases': aliases, 'fiction_map': {fid: {'path': p,
                    'count': len(paragraphs(z.read(p)))} for fid, p in fiction.items()},
                'validation': {'crc': 'PASS', 'source_identity': 'PASS',
                    'paragraph_ranges_checked': paragraph_checks, 'resource_references_checked': resource_checks,
                    'canonical_anchor_identity_checks': semantic_checks,
                    'anchor_comparison': 'NFKC, ignore whitespace and terminal excerpt ellipsis; paragraph identity only, not an assertion of byte-identical quotation'}})
            maps.append(mapping)
            index.append({'source_code': code, 'canonical_artifact': src['canonical_artifact'],
                          'evidence_count': len(entries), 'entries': entries})
    assert sum(s['evidence_count'] for s in index) == 2697
    return {'COTE_Y2_EVIDENCE_INDEX.json': index, 'COTE_Y2_SOURCE_LOCATOR_MAP.json': maps}

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source-dir', required=True, type=Path)
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    outputs = generate(args.source_dir)
    for name, data in outputs.items():
        # Compact line-per-record JSON keeps the evidence index below one megabyte.
        encoded = ('[\n' + ',\n'.join(json.dumps(v, ensure_ascii=False, separators=(',', ':'))
                   for v in data) + '\n]\n').encode('utf-8')
        path = HERE / name
        if args.check:
            assert path.read_bytes() == encoded, f'Generated output differs: {name}'
        else:
            path.write_bytes(encoded)
        print(f'{name}: {len(encoded)} bytes; {sha(encoded)}; '+('CHECK PASS' if args.check else 'written'))

if __name__ == '__main__':
    main()
