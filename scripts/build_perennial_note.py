"""Publish the supplied Obsidian note without changing its wording."""
from pathlib import Path
from html import escape
import re
from markdown_it import MarkdownIt

ROOT = Path(__file__).resolve().parents[1]
source = (ROOT / 'books/perennial-plants/note.md').read_text(encoding='utf-8-sig')
headings = re.findall(r'^# (.+)$', source, re.M)
body = re.sub(r'^# (.+)$', r'## \1', source, flags=re.M)
# Separate bold run-in headings from their paragraphs; words remain unchanged.
body = re.sub(r'^(\*\*[^\n]+?\*\*)(?=\S)', r'\1\n\n', body, flags=re.M)
# Obsidian permits bold spans next to Korean text even when their edge is
# punctuation. CommonMark leaves those delimiters visible. Escape source HTML
# first, then explicitly translate paired bold markers without changing words.
body = escape(body, quote=False)
body = re.sub(r'\*\*([^\n]+?)\*\*', r'<strong>\1</strong>', body)
engine = MarkdownIt('commonmark', {'html': True})
rendered = engine.render(body)
for i, title in enumerate(headings, 1):
    rendered = rendered.replace('<h2>' + escape(title) + '</h2>', f'<h2 id="section-{i}">' + escape(title) + '</h2>', 1)
toc = ''.join(f'<li><a href="#section-{i}">{escape(title)}</a></li>' for i, title in enumerate(headings, 1))
page = '''<!doctype html>
<html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>숙근초의 정의 및 특성 | SPATIALFLARE</title>
<meta name="description" content="숙근초의 정의 및 특성과 식재 설계.">
<link rel="canonical" href="https://navicoby.github.io/perennial-plants/">
<style>
:root{color-scheme:light;--bg:#f5f6f2;--ink:#17201c;--muted:#57635c;--line:#d6ded8;--green:#245f45}
*{box-sizing:border-box}html{scroll-behavior:smooth;scroll-padding-top:110px}body{margin:0;background:var(--bg);color:var(--ink);font:17px/1.85 -apple-system,BlinkMacSystemFont,"Segoe UI",Arial,sans-serif;overflow-wrap:anywhere}a{color:var(--green);text-underline-offset:4px}a:focus-visible,summary:focus-visible{outline:2px solid var(--green);outline-offset:5px}.skip{position:absolute;top:-80px;left:20px}.skip:focus{top:16px;background:var(--bg);padding:10px;z-index:100}main{max-width:820px;margin:auto;padding:54px 32px 70px}h1{font-size:clamp(29px,6vw,44px);line-height:1.3;letter-spacing:-.04em;margin:12px 0 24px}h2{font-size:clamp(23px,4vw,29px);line-height:1.45;margin:50px 0 22px;letter-spacing:-.025em}p{margin:0 0 20px}strong{font-weight:650}li{margin:12px 0}ul,ol{padding-left:26px}hr{border:0;border-top:1px solid var(--line);margin:44px 0}.eyebrow{font:12px/1.7 ui-monospace,Consolas,monospace;letter-spacing:.12em;color:var(--muted)}.source-info{font-size:14px;color:var(--muted);border-left:3px solid var(--line);padding-left:18px;margin:24px 0}details{border-block:1px solid var(--line);padding:18px 0;margin:32px 0}summary{cursor:pointer;color:var(--green)}details ol{font-size:15px}article>p:last-child{font-size:14px;color:var(--green)}@media(max-width:560px){main{padding:32px 22px 48px}body{font-size:16px;line-height:1.85}h2{margin-top:38px}}@media(prefers-reduced-motion:reduce){html{scroll-behavior:auto}}
</style></head><body>
<a class="skip" href="#content">본문으로 바로가기</a>
<header><a href="/">SPATIALFLARE</a> · <a href="/#literature">Literature</a></header>
<main id="content"><div class="eyebrow">LITERATURE / PLANTING NOTE</div>
<h1>숙근초의 정의 및 특성</h1>
<details><summary>목차 · 6개 절</summary><ol>''' + toc + '''</ol></details>
<article>''' + rendered + '''</article></main>
<footer><a href="/#literature">← Literature</a></footer></body></html>'''
out = ROOT / 'static/perennial-plants/index.html'
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(page, encoding='utf-8')
print(f'Built {out.relative_to(ROOT)}: {len(headings)} sections')
