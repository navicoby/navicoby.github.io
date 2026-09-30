"""Publish the Research repository's daily index under this site's /research/."""
from pathlib import Path
import argparse
import re
import urllib.request
import json
from apply_site_chrome import apply

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--public', type=Path, default=Path('public'))
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    source = 'https://raw.githubusercontent.com/navicoby/Research/main/'
    # Fetch everything before publishing, so failed requests do not leave partial data.
    files = {}
    for name in ('index.html', 'papers.json', 'abstracts.json'):
        request = urllib.request.Request(source + name, headers={'User-Agent': 'SpatialFlare-Publisher'})
        with urllib.request.urlopen(request, timeout=60) as response:
            files[name] = response.read()
    for name in ('papers.json', 'abstracts.json'):
        json.loads(files[name])
    text = files['index.html'].decode('utf-8')
    # Always use this site's current chrome rather than a copied upstream version.
    text = re.sub(r'<spatialflare-(header|footer)\b.*?</spatialflare-\1>', '', text, flags=re.S)
    text = re.sub(r'<script\b[^>]*src=["\'][^"\']*site-chrome\.js["\'][^>]*>\s*</script>', '', text)
    heading = re.search(r'<header\b[^>]*>(.*?)</header>', text, re.S)
    existing_controls = re.search(r'<details class="sf-page-menu">.*?</details>', text, re.S)
    controls = existing_controls.group() if existing_controls else ''
    if existing_controls:
        text = text.replace(existing_controls.group(), '', 1)
        heading = re.search(r'<header\b[^>]*>(.*?)</header>', text, re.S)
    if heading and '<h1' in heading.group(1):
        inner = heading.group(1)
        theme = re.search(r'<div class="theme".*?</div>', inner, re.S)
        if theme:
            controls = '<details class="sf-page-menu"><summary>페이지 메뉴</summary><div class="sf-page-menu-panel">' + theme.group() + '</div></details>'
            inner = inner.replace(theme.group(), '')
        text = text[:heading.start()] + '<section class="research-heading">' + inner + '</section>' + text[heading.end():]
    # Preserve source attribution as article content, separate from the site footer.
    text = re.sub(r'<footer\b[^>]*>(.*?)</footer>', r'<p class="research-source-notice">\1</p>', text, flags=re.S)
    if controls:
        text = re.sub(r'(<body\b[^>]*>)', lambda m: m.group(1) + controls, text, count=1)
    header = (root / 'scripts/site-chrome/header.html').read_text(encoding='utf-8')
    footer = (root / 'scripts/site-chrome/footer.html').read_text(encoding='utf-8')
    text = apply(text, header, footer)
    style = '<style>:root[data-theme="light"]{--bg:#f5f6f2}body{--bg:inherit;background-color:var(--bg)!important}.research-heading{padding:28px 0 24px;border-bottom:1px solid var(--line);margin-bottom:22px}.research-source-notice{font-size:12px;color:var(--ink-soft);border-top:1px solid var(--line);padding-top:22px;margin-top:32px}</style>'
    text = text.replace('</head>', style + '</head>', 1)
    files['index.html'] = text.encode('utf-8')
    destination = args.public / 'research'
    destination.mkdir(parents=True, exist_ok=True)
    for name, content in files.items():
        (destination / name).write_bytes(content)
    print('Published current research index and paper data at /research/.')

if __name__ == '__main__':
    main()
