"""Validate chapter completeness, local navigation, exports and preserved sources."""
from pathlib import Path
from urllib.parse import urlsplit, unquote
from collections import Counter
import hashlib,json,csv
from bs4 import BeautifulSoup

root=Path(__file__).resolve().parents[2]/'static'
site=root/'augmented-reality-landscape'
errors=[]
pages={p.resolve():BeautifulSoup(p.read_text(),'html.parser') for p in site.rglob('*.html')}
checked=0
for path,soup in pages.items():
    if path.name=='v1.html':continue  # preserved version renders its headings client-side
    if len(soup.find_all('h1'))!=1:errors.append(f'{path.name}: expected one h1')
    duplicates=[k for k,v in Counter(t['id'] for t in soup.select('[id]')).items() if v>1]
    if duplicates:errors.append(f'{path.name}: duplicate IDs {duplicates}')
    for tag in soup.select('[href], [src]'):
        url=urlsplit(tag.get('href',tag.get('src','')))
        if url.scheme or url.netloc:continue
        if url.path=='/':continue # checked by repository-wide navigation validation
        target=(root/url.path.lstrip('/') if url.path.startswith('/') else path.parent/unquote(url.path)).resolve() if url.path else path
        if target.is_dir():target=target/'index.html'
        if not target.exists():errors.append(f'{path.name}: missing {url.path}');continue
        if url.fragment and target.suffix=='.html' and target.name!='v1.html':
            target_soup=pages.get(target) or BeautifulSoup(target.read_text(),'html.parser')
            if not target_soup.find(id=unquote(url.fragment)):errors.append(f'{path.name}: missing anchor {url.path}#{url.fragment}')
        checked+=1
chapters=json.loads((site/'text/chapters.json').read_text())
assert len(chapters)==33
assert [c['n'] for c in chapters if c['status']=='planned']==[2,3,7,8]
assert sum(c['status']=='available' for c in chapters)==29
for c in chapters:
    md=(site/'text'/f'ch{c["n"]:02}.md').read_text()
    page=pages[(site/'chapters'/f'ch{c["n"]:02}.html').resolve()]
    if c['status']=='available' and len(page.select_one('.prose').get_text())<len(md)*.7:errors.append(f'ch{c["n"]}: body appears truncated')
manifest=json.loads((site/'downloads/source-manifest.json').read_text())
for item in manifest:
    assert hashlib.sha256((site/item['file']).read_bytes()).hexdigest()==item['sha256'],item['file']
papers=json.loads((site/'downloads/literature.json').read_text())
assert len(papers)==140
assert len(pages[(site/'literature.html').resolve()].select('.paper'))==140
with (site/'downloads/literature.csv').open(encoding='utf-8-sig') as f:assert len(list(csv.reader(f)))==141
search=json.loads((site/'assets/search-index.json').read_text())
assert len(search)==176
for doc in search:
    assert (site/urlsplit(doc['url']).path).is_file(),doc['url']
    assert '/Users/' not in doc['text']
for p in site.rglob('*'):
    if p.suffix in {'.html','.md','.json','.js','.csv'}:
        text=p.read_text(encoding='utf-8-sig')
        if '/Users/navicoby/' in text:errors.append(f'{p.name}: local absolute path in published content')
if errors:raise SystemExit('\n'.join(errors))
print(f'PASS: {len(pages)} HTML pages; {checked} internal links/assets; 29 full chapters + 4 planned; 140 literature records; {len(manifest)} original file hashes.')
